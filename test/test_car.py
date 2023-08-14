import unittest
from datetime import date
from engine.capulet_engine import CapuletEngine

from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
class TestEngines(unittest.TestCase):
    def test_capuletengine_shouldbe_Service(self):
        current_mileage = 30001
        last_service_mileage= 0
        engine=CapuletEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())

    def test_capuletengine_should_notbe_Service(self):
        current_mileage = 30000
        last_service_mileage= 0
        engine=CapuletEngine(last_service_mileage,current_mileage)
        self.assertFalse(engine.needs_service())

    def test_stermanengine_shouldbe_Service(self):
        warning_light_is_on= True
        engine=SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_stermanengine_should_notbe_Service(self):
        warning_light_is_on= False
        engine=SternmanEngine(warning_light_is_on)
        self.assertF(engine.needs_service())
    
    def test_willoughby_should_be_Service(self):
        current_mileage=60001
        last_service_mileage=0
        engine=WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_should_notbe_Service(self):
        current_mileage=60000
        last_service_mileage=0
        engine=WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestBattery(unittest.TestCase):
    def test_nubbin_should_be_Service(self):
        current_date=date.fromisformat("2004-01-30")
        last_service_date=date.fromisoformat("2000-01-30")
        battery = NubbinBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())


    def test_nubbin_should_notbe_Service(self):
        current_date=date.fromisformat("2004-01-30")
        last_service_date=date.fromisoformat("2003-01-30")
        battery = NubbinBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())
    

    def test_Spindler_should_be_Service(self):
        current_date=date.fromisoformat("2004-01-30")
        last_service_date=date.fromisoformat("2003-01-30")
        battery=SpindlerBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_Spindler_should_notbe_Service(self):
        current_date=date.fromisoformat("2004-01-30")
        last_service_date=date.fromisoformat("2002-01-30")
        battery=SpindlerBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())


    



    


    








if __name__ == '__main__':
    unittest.main()
