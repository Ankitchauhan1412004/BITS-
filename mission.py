from state_machine import StateMachine
from offboard_control import OffboardController
from aruco_detector import ArucoDetector
import time

sm = StateMachine()
ctrl = OffboardController()
detector = ArucoDetector()

condition = {
    "airborne": False,
    "shaft_found": False,
    "reached_floor2": False,
    "marker_found": False
}

while True:
    state = sm.update(condition)

    print("STATE:", state)

    if state == "TAKEOFF":
        ctrl.arm()
        ctrl.takeoff(3)
        time.sleep(5)
        condition["airborne"] = True

    elif state == "SEARCH_SHAFT":
        ctrl.goto(0,0,-3)
        time.sleep(5)
        condition["shaft_found"] = True

    elif state == "DESCEND":
        ctrl.goto(0,0,-8)
        time.sleep(6)
        condition["reached_floor2"] = True

    elif state == "SCAN_MARKER":
        # Camera code would run here
        print("Scanning for marker...")
        time.sleep(3)
        condition["marker_found"] = True

    elif state == "LAND":
        print("Mission Complete")
        break
