# Parent class
class Aircraft:
    def __init__(self, call_sign):
        self.call_sign = call_sign

    def request_takeoff(self):
        """Generic takeoff request"""
        print(f"{self.call_sign}: Requesting clearance for takeoff.")

# Child class 1
class PassengerPlane(Aircraft):
    def request_takeoff(self):
        # Override with specific behavior
        super().request_takeoff()
        print(f"{self.call_sign}: Passenger boarding complete, ready for departure.")

# Child class 2
class CargoPlane(Aircraft):
    def request_takeoff(self):
        super().request_takeoff()
        print(f"{self.call_sign}: Cargo secured, requesting heavy-lift clearance.")

# Child class 3
class FighterJet(Aircraft):
    def request_takeoff(self):
        super().request_takeoff()
        print(f"{self.call_sign}: Armed and ready, requesting priority takeoff.")

# --- Demonstration of Polymorphism ---
def main():
    fleet = [
        PassengerPlane("Flight GA123"),
        CargoPlane("Cargo CX45"),
        FighterJet("Falcon F16")
    ]

    # Polymorphism
    for aircraft in fleet:
        aircraft.request_takeoff()
        print("-" * 50)

if __name__ == "__main__":
    main()
