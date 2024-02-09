# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │   Order                                                    │
  │                                                            │
  │                                                            │
  │   print_menu ==> print dishes and their prices             │
  │                                                            │
  │   add_dish_to_order ==> select some number                 │
  │                         of any available dish              ├──────────────┐
  │                                                            │              │
  │                                                            │              │
  │                                                            │              │
  │                                                            │              │ 
  │                                                            │              ▼
  │                                                            │      ┌──────────────────────────────────────────────────────┐
  │                                                            │      │  OrderConfirmation                                   │
  └──────────────┬─────────────────────────────────────────────┘      │                                                      │
                 │  ▲                                                 │                                                      │
                 ▼  │                                                 │  receipt of order ==> print itemised list of dishes  │
  ┌─────────────────┴───────────────────────────────────┐             │                       ordered, item totals & order   │
  │                                                     │             │                       total                          │
  │  Menu                                               │             │                                                      │
  │                                                     │             │  text_confirmation ==> text sent to                  │
  │  add_dish ==> adds dish to menu                     │             │                        customer for a                │
  │                                                     │             │                        successful order              │
  │  update_dish_price ==> updates dish price           │             │                                                      │
  │                                                     │             │                                                      │
  │  dish_availability ==> updates units_left           │             └──────────────────────────────────────────────────────┘
  └─────────────────────────────────────────────────────┘      
                    ▲                                                 
                    │                                                
  ┌─────────────────┴───────────────────────────────────┐             
  │                                                     │             
  │  Dish                                               │            
  │                                                     │             
  │                                                     │             
  │  dish                                               │             
  │                                                     │             
  │  dish_price                                         │             
  │                                                     │             
  └─────────────────────────────────────────────────────┘

```

_Also design the interface of each class in more detail._

```python
class Order:
    # User-facing properties:
    #   order_summary: {dish_name : total price}

    def __init__(self):
        # Parameters:
        #   order_summary: dictionary of dishes and their total prices for the order
        pass # No code here yet
    
    def print_menu(self):
        # Return:
        #   prints a list of dishes and their prices (*potential addition* only available dishes)
        pass # No code here yet

    def add_dish_to_order(self, dish):
        # Parameters:
        #   dish: string representing dish in list
        # Returns:
        #   prints a confirmation that dish has been added to order
        pass # No code here yet

    def receipt_of_order(self):
        # Returns:
        #   prints out details of order: dishes, item totals and total order price
        pass # No code here yet

class Menu:
    # User-facing properties:
    #   dishes: list of dishes and their prices

    def __init__(self):
        # Parameters:
        #   dishes: dictionary = {dish_name : {'price': dish_price, 'availability': units_left}}
        pass # No code here yet

    # *potential update* MAY NOT BE REQUIRED
    #def print_menu(self):
    #    # Returns:
    #    #   prints menu contents in a readable format
    #    pass # No code here yet

    def add_dish(self, dish):
        # Parameters:
        #   dish: instance of Dish
        # Side-effects:
        #   Adds dish to dishes dictionary
        pass # No code here yet

    # *potential update* COULD ALSO ADD REMOVE DISH METHOD

class Dish:
    # User-facing properties:
    #   dish_name: string representing dish name
    #   *potential addition* allergens: string of allergens in dish
    #   dish_price: float
    
    def __init__(self, dish_name, dish_price, units_available):
        # Parameters:
        #   dish: dictionary {dish_name : {'price': dish_price, 'availability': units_left}}
        #   dish_name: string
        #   dish_price: float
        #   units_available: integer (set inital number of dishes per day)
        pass # No code here yet

    ## MOVED TO DISH CLASS
    def update_dish_price(self, dish_name, new_price):
        # Parameters:
        #   dish_name: string, dish name of dish that price needs to be updated
        #   new_price: float, new price of dish
        # Side-effects:
        #   updates price of dish in dishes dictionary
        pass # No code here yet
    ## MOVED TO DISH CLASS
    def update_dish_availability(self, units_ordered):
        # Parameters:
        #   units_ordered: integer (from Order class)
        # Side-effects:
        #   Updates units_left for 'availability' dish dictionary
        pass # No code here yet


class OrderConfirmation:
    # User-facing properties:
    #   order: order instance (dictionary) from Order class

    def __init__(self, order):
        # Parameters:
        #   order: order instance (dictionary) from Order class
        pass # No code here yet

    def text_confirmation(self):
        # TBC (Twilio)
        pass # No code here yet
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE


```



## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE


```


_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
