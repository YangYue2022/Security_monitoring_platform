import json
import os

from flask import Flask, request, jsonify,  Response
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
import face_recognition
import dlib

app = Flask(__name__)

# Initialize dlib's face detector and face recognizer
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('./dat/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('./dat/dlib_face_recognition_resnet_model_v1.dat')

# 存储人脸编码和学号的文件路径
registered_faces_file = 'registered_faces.json'


# Load registered faces from file
def load_registered_faces():
    if os.path.exists(registered_faces_file):
        with open(registered_faces_file, 'r') as file:
            return json.load(file)
    return {}


registered_faces = load_registered_faces()


@app.route('/face-register', methods=['POST'])
def face_register():
    data = request.get_json()
    student_id = data['student_id']
    image_data = data['image']
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    image_np = np.array(image)

    # Detect faces
    faces = detector(image_np, 1)
    if len(faces) != 1:
        return jsonify({'error': 'No face or multiple faces detected'}), 400

    # Compute the face descriptor
    shape = sp(image_np, faces[0])
    face_descriptor = facerec.compute_face_descriptor(image_np, shape)

    # Convert descriptor to list to be JSON serializable
    face_descriptor_list = [x for x in face_descriptor]

    # Store or update the face descriptor and student_id
    registered_faces[student_id] = face_descriptor_list
    with open(registered_faces_file, 'w') as file:
        json.dump(registered_faces, file)

    return jsonify({'message': 'Face registered successfully'})

def gen_frames(stream_url):
    cap = cv2.VideoCapture(stream_url)
    # 设置分辨率为640x480
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    frame_skip = 5  # 跳过的帧数
    frame_count = 0
    while True:
        success, frame = cap.read()
        if not success:
            break
        if frame_count % frame_skip == 0:
            # 1. 转换为灰度图像
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 2. 检测人脸
            faces = detector(gray, 1)
            for face in faces:
                shape = sp(frame, face)
                face_encoding = np.array(facerec.compute_face_descriptor(frame, shape))
                matches = face_recognition.compare_faces(list(registered_faces.values()), face_encoding, tolerance=0.4)
                name = "Stranger"
                color = (0, 0, 255)  # 默认红色标记陌生人

                if True in matches:
                    first_match_index = matches.index(True)
                    student_id = list(registered_faces.keys())[first_match_index]
                    name = student_id
                    color = (0, 255, 0)  # 绿色标记已注册人脸

                # 在人脸周围绘制矩形框
                cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), color, 2)
                # 添加文本标签
                cv2.putText(frame, name, (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            # 3. 编码图像
            ret, buffer = cv2.imencode('.jpg', frame,[int(cv2.IMWRITE_JPEG_QUALITY), 70])
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # 构造响应体
        frame_count += 1

@app.route('/video_feed/<stream_id>')
def video_feed(stream_id):
    try:
        stream_url = f'rtmp://101.42.183.175:9090/live/{stream_id}'
        return Response(gen_frames(stream_url),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        app.logger.error(f"Failed to stream video for ID {stream_id}: {str(e)}")
        return jsonify({'error': 'Failed to process video stream'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False,threaded=True)

