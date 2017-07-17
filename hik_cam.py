import cv2
import os
import numpy as np

# fisheye camera setting
source1 = "rtsp://admin:startdt123@192.168.1.64/Streaming/Channels/1"
source2 = "rtsp://admin:startdt123@192.168.1.64/Streaming/Channels/2"

# camera intrinsic parameter - frame size: 2160 x 1920
K2560 = np.array([[334.42926712, 0., 308.91948447],
                  [0., 268.59035229, 317.60323673],
                  [0., 0., 1.]])
# distortion coefficient: k1, k2, k3, k4
D2560 = np.array([0.00081044, -0.06958253, 0.00081044, -0.06958253])
# frame size: 1280 x 960
K1280 = np.array([[333.79675414, 0., 638.98982033],
                 [0., 334.40593755, 481.10186754],
                 [0., 0., 1.]])
D1280 = np.array([6.90051332e-01, 4.69019786e-02, 7.87612370e-05, 1.05789473e+00])
# # from https://github.com/smidm/opencv-python-fisheye-example/blob/master/fisheye_example.py
# K = np.array([[689.21, 0., 1295.56],
#               [0., 690.48, 942.17],
#               [0., 0., 1.]])
# zeros distortion coefficient
D0 = np.array([0., 0., 0., 0.])

class ip_cam():
    def __init__(self, source=source1):
        self.cap = cv2.VideoCapture(source)

    def get_stream(self, undist=True, K=K1280, D=D0):
        # use knew to scale output, by default it is identical to K
        Knew = K.copy()
        scale = 0.5
        Knew[(0, 1), (0, 1)] = scale * Knew[(0, 1), (0, 1)]
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            # cv2.imshow('hik', frame)
            if undist:
                # undistorted img
                frame_undist = cv2.fisheye.undistortImage(frame, K, D, Knew=Knew)
                # new_matrix, roi = cv2.getOptimalNewCameraMatrix(K, D, (frame.shape[1], frame.shape[0]), 1, (frame.shape[1], frame.shape[0]))
                # mapx, mapy = cv2.initUndistortRectifyMap(K, D, None, new_matrix, (frame.shape[1], frame.shape[0]), 5)
                # x, y, w, h = roi
                # frame_undist = cv2.remap(frame, mapx, mapy, cv2.INTER_LINEAR)
                # frame_undist = frame_undist[x:x+w, y:y+h]
                # display undistorted image
                # cv2.imshow("hik_undist", frame_undist)
                yield frame_undist
            else:
                yield frame

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    cam = ip_cam()
    for index, frame in enumerate(cam.get_stream()):
        cv2.imshow("hik_undist", frame)
        cv2.waitKey(1)
        if index > 200:
            break
    cam.close()

