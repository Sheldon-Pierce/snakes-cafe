from textwrap import dedent

greeting = dedent(
    """
    ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    ** Welcome to the SnakesCafe! **
    ** Please see our menu below. **
    **
    ** To quit at any time, type "quit" **
    ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    """
)

menu = dedent(
    """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """
)

order_prompt = dedent(
    """
    ***********************************
    ** Hello, what would you like to order? **
    ***********************************
    """
)

farewell = dedent(
    """
    ***********************************
    **    Thank you for coming! Goodbye!    **
    ***********************************
    """
)

food_items = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}

def main():
    print(greeting)
    print(menu)
    while True:
        order_item = input("> ")
        if order_item == "quit":
            break

        if order_item not in food_items.keys():
            print("Sorry, we do not have that!")
        else:
            food_items[order_item] += 1
            if food_items[order_item] == 1:
                print(f"** {food_items[order_item]} order of {order_item} has been added to your meal **")
            else:
                print(f"** {food_items[order_item]} orders of {order_item} have been added to your meal **")

    print(farewell)

if __name__ == "__main__":
    main()



