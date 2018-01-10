import cv2

cap = cv2.VideoCapture(0)
width = 320
height = 240
cap.set(3, width)
cap.set(4, height)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    cv2.imshow('RGB Colorspace', frame)
    cv2.imshow('Grayscale', gray)
    cv2.imshow('HSV Colorspace', hsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
