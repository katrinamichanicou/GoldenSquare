class Dish:
    
    def __init__(self, name, price, units_available):
        self.name = name
        self.price = price
        self.units_available = units_available
        self.dish = {
            "dish_name" : self.name, 
            "dish_price" : self.price, 
            "availability" : self.units_available
            }
    
    def format_dish(self):
        return f"{self.name} ---- £{self.price}"

    def update_price(self, new_price):
        self.dish["dish_price"] = new_price

    def update_availability(self, units_sold):
        pass
