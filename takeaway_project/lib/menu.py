

class Menu:

    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        self.dishes.remove(dish)
    
    def format_menu(self):
        formatted_menu = ""
        for dish in self.dishes:
            formatted_menu += f"{self.dishes.index(dish)+1}. {dish.format_dish()} \n"
        return formatted_menu

