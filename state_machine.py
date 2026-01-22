class StateMachine:
    def __init__(self):
        self.state = "IDLE"

    def update(self, condition):
        if self.state == "IDLE":
            self.state = "TAKEOFF"

        elif self.state == "TAKEOFF" and condition["airborne"]:
            self.state = "SEARCH_SHAFT"

        elif self.state == "SEARCH_SHAFT" and condition["shaft_found"]:
            self.state = "DESCEND"

        elif self.state == "DESCEND" and condition["reached_floor2"]:
            self.state = "SCAN_MARKER"

        elif self.state == "SCAN_MARKER" and condition["marker_found"]:
            self.state = "LAND"

        return self.state
