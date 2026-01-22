from pymavlink import mavutil
import time

class OffboardController:
    def __init__(self):
        self.master = mavutil.mavlink_connection('udp:127.0.0.1:14540')
        self.master.wait_heartbeat()

    def arm(self):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0, 1, 0, 0, 0, 0, 0, 0)

    def takeoff(self, alt):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
            0, 0, 0, 0, 0, 0, alt)

    def goto(self, x, y, z):
        self.master.mav.set_position_target_local_ned_send(
            0, self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            0b0000111111111000,
            x, y, z, 0,0,0, 0,0,0, 0,0)
