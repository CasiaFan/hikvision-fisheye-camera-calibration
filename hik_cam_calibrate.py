import cv2
import glob
import numpy as np


cali_pic_dir = "/home/arkenstone/Pictures/Webcam/chessboard_cali_1280_960"

CV_CALIB_USE_INTRINSIC_GUESS = 1
CV_CALIB_ZERO_TANGENT_DIST = 8
CV_CALIB_RATIONAL_MODEL = 16384

# prepare object points: (0, 0, 0), (1, 0, 0), ...
objp = np.zeros((6*9, 3), np.float32)
objp[:, :2] = np.mgrid[0:6, 0:9].T.reshape(-1, 2)

objps = []
imgps = []

for img in glob.glob(cali_pic_dir+'/*.jpg'):
    im = cv2.imread(img)
    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # find chessboard corners
    pattern_found, corners = cv2.findChessboardCorners(gray_im, (6, 9))
    if pattern_found:
        objps.append(objp)
        imgps.append(corners)
        # refine corner locations
        corners = cv2.cornerSubPix(gray_im, corners, (11, 11), (-1, -1), criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        # draw chessboard corners
        # cv2.drawChessboardCorners(gray_im, (6, 9), corners, pattern_found)
        # cv2.imshow("board", gray_im)
        # cv2.waitKey(0)
cv2.destroyAllWindows()

# initialize matrix initial coefficient for intrinsic_guess is true
matrix_init = np.zeros((3, 3), np.float32)
matrix_init[0][0] = 310.940583445
matrix_init[0][2] = 320.0
matrix_init[1][1] = 310.940583445
matrix_init[1][2] = 320.0
matrix_init[2][2] = 1.0
dist_init = np.zeros((1, 4), np.float32)
pattern_found, K, D, rvecs, tvecs = cv2.calibrateCamera(objps, imgps, gray_im.shape[::-1], matrix_init, None, flags=CV_CALIB_USE_INTRINSIC_GUESS + CV_CALIB_ZERO_TANGENT_DIST + CV_CALIB_RATIONAL_MODEL)
print "mtx=", K
print "dist=", D
