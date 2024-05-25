import os
import cv2

cap = cv2.VideoCapture(0)

# Set the resolution
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Load the background image
imBackground = cv2.imread('Resources/background.png')
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2. imread(os.path.join(folderModePath, path)))
if imBackground is None:
    print("Error: Background image not found.")
    exit()

while True:
    # Capture frame-by-frame
    success, img = cap.read()
    
    if not success:
        print("Error: Failed to capture image.")
        break
    
    # Place the webcam image onto the background image
    imBackground[162:162+480, 55:55+640] = img
    imBackground[44:44+633, 808:808+414] = imgModeList[2]
    # Display the resulting frame
    cv2.imshow('TickMe', imBackground)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
