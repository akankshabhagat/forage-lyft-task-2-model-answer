from tires.tires import Tire
class carrigan(Tire):
    def __init__(self,tire_wear):
        self.tire_wear=tire_wear
    def need_service(self):
        return sum(self.tire_wear) >=3.0
    