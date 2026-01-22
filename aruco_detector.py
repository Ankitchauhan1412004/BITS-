import cv2

class ArucoDetector:
    def __init__(self):
        self.dict = cv2.aruco.getPredefinedDictionary(
            cv2.aruco.DICT_4X4_50)
        self.params = cv2.aruco.DetectorParameters()

    def detect(self, frame):
        corners, ids, _ = cv2.aruco.detectMarkers(
            frame, self.dict, parameters=self.params)
        return ids
