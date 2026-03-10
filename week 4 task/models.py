from abc import ABC, abstractmethod


class StationAsset(ABC):
    def __init__(self, name):
        self.name = name

    
    def calculate_revenue(self):
        """Each asset must implement its own revenue calculation"""
        pass


class FuelDispenser(StationAsset):
    def __init__(self, name, liters_sold, price_per_liter):
        super().__init__(name)
        self.liters_sold = liters_sold
        self.price_per_liter = price_per_liter

    def calculate_revenue(self):
        return self.liters_sold * self.price_per_liter


class CarWash(StationAsset):
    def __init__(self, name, cars_washed, price_per_wash):
        super().__init__(name)
        self.cars_washed = cars_washed
        self.price_per_wash = price_per_wash

    def calculate_revenue(self):
        return self.cars_washed * self.price_per_wash
        from models import FuelDispenser, CarWash


def main():
    assets = [
        FuelDispenser("Pump 1", liters_sold=500, price_per_liter=1.2),
        FuelDispenser("Pump 2", liters_sold=350, price_per_liter=1.2),
        CarWash("Automatic Wash", cars_washed=40, price_per_wash=5),
        CarWash("Manual Wash", cars_washed=25, price_per_wash=3)
    ]

    total_revenue = 0

    print("Station Revenue Report")
    print("----------------------")

    for asset in assets:
        revenue = asset.calculate_revenue()
        print(f"{asset.name} revenue: ${revenue}")
        total_revenue += revenue

    print("----------------------")
    print(f"Total Station Revenue: ${total_revenue}")


if __name__ == "__main__":
    main()