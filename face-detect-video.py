import cv2

camera_index = 0
vc = cv2.VideoCapture(camera_index)

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        print(":(")
        break


    boxes = detector.detectMultiScale(frame)
    #print(boxes)
    for box in boxes:
        x1, y1, width, height = box
        x2, y2 = x1 + width, y1 + height

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('ali', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
