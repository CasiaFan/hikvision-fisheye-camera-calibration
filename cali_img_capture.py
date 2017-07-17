import os
import cv2


img_save_dir = "/home/arkenstone/Pictures/Webcam/chessboard_cali_1280_960"
if not os.path.exists(img_save_dir):
    os.makedirs(img_save_dir)

source = "rtsp://admin:startdt123@192.168.1.64/Streaming/Channels/1"
cam = cv2.VideoCapture(source)
img_counter = 0
while(cam.isOpened()):
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if not ret:
        break
    # press ESC to escape (ESC ASCII value: 27)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    # press Space to capture image (Space ASCII value: 32)
    elif cv2.waitKey(1) & 0xFF == 32:
        print "Saving image ..."
        img_file = img_save_dir + "/opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_file, frame)
        print "WebCam Image {}: {} written!".format(img_counter, img_file)
        img_counter += 1
    else:
        pass

cam.release()
cv2.destroyAllWindows()
