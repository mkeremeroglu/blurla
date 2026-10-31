import io

import cv2
import numpy as np
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024 

#hazır yüz tespit modeli 
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def blur_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        face = img[y:y + h, x:x + w]
        k = (max(w // 3, 3) // 2) * 2 + 1
        img[y:y + h, x:x + w] = cv2.GaussianBlur(face, (k, k), 0)
    return img, len(faces)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blur", methods=["POST"])
def blur():
    file = request.files.get("photo")
    if not file:
        return "Dosya yüklenmedi", 400

    data = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if img is None:
        return "Geçerli bir resim değil", 400

    result, _count = blur_faces(img)

    ok, buffer = cv2.imencode(".jpg", result)
    return send_file(io.BytesIO(buffer.tobytes()), mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)