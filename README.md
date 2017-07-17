### Device:
Hikvision fisheye ip camera - DS-2CD3955FWD-IWS <br>

### Usage:
First, run `cali_img_capture.py` script and press SPACE button to capture 9x6 chessboard image for calibration (seen [here](http://docs.opencv.org/3.0-beta/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#calibratecamera)). 30-40 images work fine for calibration.

Next, run `hik_cam_calibrate.py` to get camera intrinsic parameters and distortion coefficients (K and D).

Last, in `hik_cam.py` show how to use K and D to undistort images.

### Requirements
opencv 3.2.0

### Referrence
[Here](https://github.com/XinningShen/Fisheye_Camera_Calibration/blob/master/GetCameraCalibrationCoefficient.py)
