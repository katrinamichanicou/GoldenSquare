from dish import Dish
from menu import Menu
import os
from datetime import datetime, timedelta
from twilio.rest import Client

class Order:

    def __init__(self, menu):
        self.menu = menu
        self.order_summary = {}

    def print_menu(self):
        menu_list = f"\nMENU:\n{self.menu.format_menu()}"
        print(menu_list)
        user_input = input("To start a new order select ENTER, or type '-' to exit\n")
        if user_input == "":
            self.add_dish_to_order()
        elif user_input == "-":
            pass

    
    def add_dish_to_order(self):
        input_dish = input(f"Please enter the NUMBER of the dish you want to order:\n")
        dish = self.menu.dishes[input_dish - 1]
        
        # //REFACTOR// Remove for loop - should be able to access dish dictionary from line 25 code instead
        #* for dish in self.menu.dishes:

        # //REFACTOR// This units_available code should be moved elsewhere, since it does not take into account the input_dish.
        # //REFACTOR// Therefore it will return 'Sorry, this item has sold out' if the first dish in the list has sold out
        #*     units_available = dish.dish["availability"]
        #*     if units_available == 0:
        #*         print("Sorry, this item has sold out")
        #*         continue

        # //REFACTOR// Could use input_dish number as index for the dish in the menu (dictionary in list) - see line 25 - code already added
        # //REFACTOR// Therefore can remove initial if statement (line 38)
        #*    if input_dish.strip() == str(self.menu.dishes.index(dish)+1):
                quantity = input(f"How many portions of {dish.name} would you like to add to your order?\n")
                
                if int(quantity) > units_available:
                    response = input(f"Sorry we only have {units_available}, do you want to add this to your order (Y/N)\n")
                    if response.lower() == "y":
                        quantity = units_available
                        dish_added_confirmation = f"{quantity} portions of {dish.name} have been added to your order\n"
                        print(dish_added_confirmation)
                    elif response.lower() == "n":
                        self.add_dish_to_order()
                dish_added_confirmation = f"{quantity} portions of {dish.name} have been added to your order\n"
                print(dish_added_confirmation)
                self.order_summary.setdefault(dish.name, int(quantity))
                dish.update_availability(self)
        next_input = input("Type 'ADD' if you would like to add another dish or ENTER to confirm order and see your receipt\n")
        
        if next_input.lower() == "add":
            self.add_dish_to_order()
        else:
            self.print_receipt()
    
    def print_receipt(self):
        receipt_items_format = ""
        order_total = 0
        
        for item in self.order_summary.items():
            item_price = [dish.price for dish in self.menu.dishes if dish.name == item[0]]
            item_total = item[1] * item_price[0]
            order_total += item_total
            receipt_items_format += f"{item[0]} ---- £{item_total}\n"
        
        order_total_format = f"TOTAL ---- £{order_total}\n"
        total_order_receipt_format = f"\nORDER RECEIPT:\n\n{receipt_items_format}\n\n{order_total_format}"
        #self.send_confirmation_text()
        print(total_order_receipt_format)
        
    
    def send_confirmation_text(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        delivery_time = (datetime.now() + timedelta(minutes = 40)).strftime("%H:%M")
        message = client.messages.create(
                            from_='+447488896048',
                            body=f"Thank you! Your order was placed and will be delivered before {delivery_time}",
                            to='+447791704072'
                            )

        return (f"SID: {message.sid} Status: {message.status}")


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# https://www.twilio.com/docs/usage/secure-credentials
# in terminal:
#   export TWILIO_ACCOUNT_SID='ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'"
#   export TWILIO_AUTH_TOKEN='your_auth_token'"

# Then to make sure git ignores the twilio.env file
# in terminal:
#   'twilio.env' >> .gitignore 
#  OR
#   echo "twilio.env" >> .gitignore


# EXAMPLE:
dish_1 = Dish("Halloumi Fries", 5.5, 200)
dish_2 = Dish("Halloumi & Cucumber Salad", 6, 100)
dish_3 = Dish("Halloumi Feast", 11.5, 50)
restaurant_menu_1 = Menu()
restaurant_menu_1.add_dish(dish_1)
restaurant_menu_1.add_dish(dish_2)
restaurant_menu_1.add_dish(dish_3)
order = Order(restaurant_menu_1)
order.print_menu()
# print(dish_1.dish)
# print(dish_2.dish)
# print(dish_3.dish)