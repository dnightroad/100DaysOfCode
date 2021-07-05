#Object Oriented Programming
#An OOP approach to a virtual coffee vending machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#turn the machine on
machine = "on"
while machine == "on":
    drinks = Menu().get_items()
    #prompt user by asking them what would they like
    order_name = input(f"What would you like? {drinks}: ")
    #print report
    if order_name == "report":
      report = CoffeeMaker().report()
      profit = MoneyMachine().report()

    elif order_name == "off":
        break
    else:
    #look for the drink
        does_drink_exist = Menu().find_drink(order_name)
    #then check resources
        are_resources_enough = CoffeeMaker().is_resource_sufficient(does_drink_exist)
    #take payment
        if are_resources_enough == True:
            payment = MoneyMachine().make_payment(does_drink_exist.cost)
    #make the coffee
        maker = CoffeeMaker().make_coffee(does_drink_exist)





