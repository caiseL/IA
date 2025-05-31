import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("final_model.keras")
emotion_labels = ['angry', 'disgust', 'happy', 'natural', 'sad', 'surprise'] 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)
    confidence = np.max(pred) * 100
    label = emotion_labels[np.argmax(pred)]

    text = f"{label} ({confidence:.2f}%)"
    cv2.putText(frame, text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Emotion Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or \
       cv2.getWindowProperty("Emotion Detector", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
