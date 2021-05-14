# -----------------------------------------------------
# Final Project
# Written by: Dhruvkumar Radadiya (2092393)
#             Vidhi Suthar (2093559)
#             Janak Patel (2092733)
# The purpose of this program to create a order management system for a pizza store
# User will have options to add and update the orders and extract different information based on added orders.
# -----------------------------------------------------

class DeluxePizza:
    numberOfPizzas = 0

    # default constructor
    def __init__(self, size, stuffedWithCheese, cheesetoppings, pepperonitoppings, mushroomtoppings, veggietopping):

        if size == 1:
            self.size = 'small'
        elif size == 2:
            self.size = 'medium'
        elif size == 3:
            self.size = 'large'
        else:
            self.size = 'small'

        if stuffedWithCheese == 1:
            self.stuffedWithCheese = True
        else:
            self.stuffedWithCheese = False

        self.cheeseTopping = cheesetoppings
        self.pepperoniToppings = pepperonitoppings
        self.mushroomToppings = mushroomtoppings
        self.veggieTopping = veggietopping

        DeluxePizza.numberOfPizzas += 1

    # accessor and mutator methods for class attributes.
    def get_size(self):
        return self.size

    def set_size(self, size):
        if size == 1:
            self.size = 'small'
        elif size == 2:
            self.size = 'medium'
        elif size == 3:
            self.size = 'large'
        else:
            self.size = 'small'

    def get_cheese_toppings(self):
        return self.cheeseTopping

    def set_cheese_toppings(self, cheese_toppings):
        self.cheeseTopping = cheese_toppings

    def get_pepperoni_toppings(self):
        return self.pepperoniToppings

    def set_pepperoni_toppings(self, pepperoni_toppings):
        self.pepperoniToppings = pepperoni_toppings

    def get_mushroom_toppings(self):
        return self.mushroomToppings

    def set_mushroom_toppings(self, mushroom_toppings):
        self.mushroomToppings = mushroom_toppings

    def get_stuffedWithCheese(self):
        return self.stuffedWithCheese

    def set_stuffedWithCheese(self, stuffedWithCheese):
        if stuffedWithCheese == 1:
            self.stuffedWithCheese = True
        elif stuffedWithCheese == 2:
            self.stuffedWithCheese = False
        else:
            self.stuffedWithCheese = False

    def get_veggieTopping(self):
        return self.veggieTopping

    def set_veggieTopping(self, veggieTopping):
        self.veggieTopping = veggieTopping

    def number_Of_Pizzas(self):
        return self.numberOfPizzas

    # method calCost to calculate the price of a pizza according to it's size, stuffing and toppings.
    def calcCost(self):
        if self.size == 'small':
            if self.stuffedWithCheese:
                return 10 + 2 + (self.cheeseTopping * 2) + (self.pepperoniToppings * 2) + (self.mushroomToppings * 2) \
                       + (self.veggieTopping * 3)
            else:
                return 10 + (self.cheeseTopping * 2) + (self.pepperoniToppings * 2) + (
                        self.mushroomToppings * 2) + (
                               self.veggieTopping * 3)
        elif self.size == 'medium':
            if self.stuffedWithCheese:
                return 12 + 4 + (self.cheeseTopping * 2) + (self.pepperoniToppings * 2) + (self.mushroomToppings * 2) \
                       + (self.veggieTopping * 3)
            else:
                return 12 + (self.cheeseTopping * 2) + (self.pepperoniToppings * 2) + (self.mushroomToppings * 2) \
                       + (self.veggieTopping * 3)
        elif self.size == 'large':
            if self.stuffedWithCheese:
                return 14 + 6 + (self.cheeseTopping * 2) + (self.pepperoniToppings * 2) + (self.mushroomToppings * 2) \
                       + (self.veggieTopping * 3)
            else:
                return 14 + (self.cheeseTopping * 2) + (self.pepperoniToppings * 2) + (self.mushroomToppings * 2) \
                       + (self.veggieTopping * 3)
        else:
            return (self.cheeseTopping * 2) + (self.pepperoniToppings * 2) + (self.mushroomToppings * 2) \
                   + (self.veggieTopping * 3)

    # __str__ methods to display the information about pizza like:
    #   size
    #   stuffing
    #   toppings
    def __str__(self, pizza_num="#"):
        return f"""\t\t\tPizza {pizza_num}
            Size of pizza : {self.size} 
            Cheese filled dough: {self.stuffedWithCheese} 
            Number of cheese toppings : {str(self.cheeseTopping)} 
            Number of pepperoni toppings : {str(self.pepperoniToppings)} 
            Number of mushroom toppings : {str(self.mushroomToppings)} 
            Number of vegetable topping : {str(self.veggieTopping)} 
            Price : $ {str(self.calcCost())}"""


# method to enter the new order
def enterNewOrder():
    # password stored in a constant.
    password = "deluxepizza"
    count = 0
    # count will keep record for the password attempts for user
    while count < 3:
        pd = input("Enter password to enter pizza details: ")
        if pd == password:
            number_of_pizzas = int(input("How many pizzas you want to enter ? : "))
            print("\n")
            if number_of_pizzas <= 20 - len(todaysPizzas):
                for pizza in range(number_of_pizzas):
                    print(f"Enter the order details of pizza {pizza + 1} : ")
                    size = input("Enter the size of pizza - 1. small 2. medium 3. large :")
                    stuffedWithCheese = int(input("Cheese filled dough - 1. Yes 2. No"))
                    cheese_toppings = int(input("Number of cheese Topping : "))
                    pepperoni_toppings = int(input("Number of pepperoni toppings : "))
                    mushroom_toppings = int(input("Number of mushroom toppings : "))
                    veggieTopping = int(input("Number of veggie toppings : "))
                    print("\n")
                    todaysPizzas.append(
                        DeluxePizza(size, stuffedWithCheese, cheese_toppings, pepperoni_toppings, mushroom_toppings,
                                    veggieTopping))
                break
            else:
                print(f"Unfortunately, We have ingredients for only {20 - len(todaysPizzas)} pizza(s).\n")
                break
        else:
            print("Wrong password\n")
            count += 1


def changeOrder():
    password = "deluxepizza"
    count = 0
    while count < 3:
        pd = input("Enter password to Update pizza details: ")
        print("\n")
        if pd == password:
            count1 = 0
            for update_pizza in todaysPizzas:
                count1 += 1
                print(f"{count1}. : " + update_pizza.__str__(str(count1)) + "\n")
            pizza_number = int(input("Which pizza you want to update ? : "))
            while True:
                if pizza_number <= len(todaysPizzas):
                    while True:
                        print(f"""\nPapa Jhon, what would you like to change for pizza {pizza_number} : 
                        1. Size
                        2. Cheese filled or not
                        3. Number of cheese toppings
                        4. Number of pepperoni toppings
                        5. Number of mushroom toppings
                        6. Number of vegetable toppings
                        7. Quit""")
                        pizza_details = int(input('Enter choice > '))
                        update_pizza = todaysPizzas[pizza_number - 1]
                        if pizza_details == 1:
                            update_pizza.set_size(
                                int(input("\nEnter the size of pizza - 1. small 2. medium 3. large : ")))
                            print("\nPizza Details Updated.")
                            print(update_pizza.__str__(str(pizza_number)))
                            print("\n")
                        elif pizza_details == 2:
                            update_pizza.set_stuffedWithCheese(int(input("Cheese filled dough - 1. Yes 2. No : ")))
                            print("\nPizza Details Updated.")
                            print(update_pizza.__str__(str(pizza_number)))
                            print("\n")
                        elif pizza_details == 3:
                            update_pizza.set_cheese_toppings(int(input("Number of cheese Topping : ")))
                            print("\nPizza Details Updated.")
                            print(update_pizza.__str__(str(pizza_number)))
                            print("\n")
                        elif pizza_details == 4:
                            update_pizza.set_pepperoni_toppings(int(input("Number of pepperoni toppings : ")))
                            print("\nPizza Details Updated. ")
                            print(update_pizza.__str__(str(pizza_number)))
                            print("\n")
                        elif pizza_details == 5:
                            update_pizza.set_mushroom_toppings(int(input("Number of mushroom toppings : ")))
                            print("\nPizza Details Updated.")
                            print(update_pizza.__str__(str(pizza_number)))
                            print("\n")
                        elif pizza_details == 6:
                            update_pizza.set_veggieTopping(int(input("Number of veggie toppings : ")))
                            print("\nPizza Details Updated.")
                            print(update_pizza.__str__(str(pizza_number)))
                            print("\n")
                        elif pizza_details == 7:
                            break
                        else:
                            print('Please enter valid input.')
                    break
                else:
                    print(f"There is no order associated with number {pizza_number}")
                    while True:
                        print("""Would you like to add new order\n1. Yes\n2. No""")
                        choice = int(input('Enter your choice > '))
                        if choice == 1:
                            enterNewOrder()
                            print("Pizza details added.")
                            break
                        elif choice == 2:
                            break
                        else:
                            print('Enter valid input.')
                    break

            break
        else:
            print("Wrong password\n")
            count += 1


def statistics():
    while True:
        print("""Papa John, what information would you like?\n 
            1. Cost & details of cheapest pizza 
            2. Cost & details of most costly pizza 
            3. Number of pizzas sold to today 
            4. Number of pizzas of specific size 
            5. Average cost of pizzas 
            6. Back to main menu\n""")
        statistics_choice = int(input("Enter your choice > "))
        print("\n")
        if statistics_choice == 1:
            pizza_tup = lowestPrice()
            print(f"\nMinimum Price of pizza is : {pizza_tup[2]}\n")
            print(pizza_tup[0].__str__(str(pizza_tup[1])), "\n")
        elif statistics_choice == 2:
            pizza_tup = highestPrice()
            print(f"\nMaximum Price of pizza is : ${pizza_tup[2]}\n")
            print(pizza_tup[0].__str__(str(pizza_tup[1])), "\n")
        elif statistics_choice == 3:
            print(f"Our chef made  {len(todaysPizzas)} pizzas today.\n\n")
        elif statistics_choice == 4:
            while True:
                find_number_size = int(input("Enter the size of pizza for which you want to count the number : "
                                             "\n\t1. Small  \n\t2. Medium \n\t3. Large \n\t4. Back : \nEnter your "
                                             "choice > "))
                if find_number_size == 1:
                    number_size = numberOfPizzasOfSize("small")
                    print(f"\nIn today's order there are {number_size[0]} pizza(s) of {number_size[1]} size.\n")
                elif find_number_size == 2:
                    number_size = numberOfPizzasOfSize("medium")
                    print(f"\nIn today's order there are {number_size[0]} pizza(s) of {number_size[1]} size.\n")
                elif find_number_size == 3:
                    number_size = numberOfPizzasOfSize("large")
                    print(f"\nIn today's order there are {number_size[0]} pizza(s) of {number_size[1]} size.\n")
                elif find_number_size == 4:
                    break
                else:
                    print('Please enter valid input.')
        elif statistics_choice == 5:
            pizzas = []
            for pizza in todaysPizzas:
                pizzas.append(pizza.calcCost())
            print(f"Total number of pizzas sold today : {len(pizzas)}")
            print(f"Average cost to pizzas : ${sum(pizzas) / len(pizzas)}")
        elif statistics_choice == 6:
            break
        else:
            print("Please enter valid option")


def numberOfPizzasOfSize(size_of_pizza):
    pizza_count = 0
    for pizza in todaysPizzas:
        if pizza.get_size() == size_of_pizza:
            pizza_count += 1
    return pizza_count, size_of_pizza


def pizzasOfSizes(sizeOfPizza):
    count = 0
    pizzacount = 0
    for pizza in todaysPizzas:
        count += 1
        if pizza.get_size() == sizeOfPizza:
            pizzacount += 1
            print("\t\tOrder id : ", todaysPizzas.index(pizza) + 1)
            print(pizza.__str__(), "\n")
    print(f"Our Chef, made {pizzacount} {sizeOfPizza} pizzas today!")


def cheaperThan(requestedprice):
    for pizza in todaysPizzas:
        if pizza.calcCost() < requestedprice:
            print(pizza.__str__(str(todaysPizzas.index(pizza) + 1)), "\n")


def lowestPrice():
    price_list = []
    for pizza in todaysPizzas:
        price_list.append(pizza.calcCost())
    minimum_priced_pizza = min(price_list)
    return todaysPizzas[price_list.index(minimum_priced_pizza)], price_list.index(
        minimum_priced_pizza) + 1, minimum_priced_pizza


def highestPrice():
    price_list = []
    for pizza in todaysPizzas:
        price_list.append(pizza.calcCost())
    maximum_priced_pizza = max(price_list)
    return todaysPizzas[price_list.index(maximum_priced_pizza)], price_list.index(
        maximum_priced_pizza) + 1, maximum_priced_pizza


def first_menu():
    print("""Papa John What do you want to do ?\n
    1. Enter a new pizza order (password required) 
    2. Change information of specific order (password required) 
    3. Display details for all pizzas of a specific size (s/m/l) 
    4. Statistics on today's pizzas 
    5. Find cheaper pizza than specific price.
    6. Quit\n""")


if __name__ == "__main__":

    todaysPizzas = []

    print("""    +-------------------------------------------+
    | Today, we have ingredients for 20 pizzas. |
    +-------------------------------------------+\n""")
    first_menu()
    while True:
        user_input = int(input("Please enter your choice > "))
        print("\n")
        if user_input == 1:
            enterNewOrder()
            first_menu()
        elif user_input == 2:
            changeOrder()
            first_menu()
        elif user_input == 3:
            while True:
                size = int(input("Enter which size of pizzas you want to see : "
                                 "\n\t1. Small  \n\t2. Medium \n\t3. Large \n\t4. Back : \nEnter your choice > "))
                if size == 1:
                    pizzasOfSizes("small")
                elif size == 2:
                    pizzasOfSizes("medium")
                elif size == 3:
                    pizzasOfSizes("large")
                elif size == 4:
                    break
                else:
                    print('Please enter valid input.')
            first_menu()
        elif user_input == 4:
            statistics()
            first_menu()
        elif user_input == 5:
            print('Find all pizzas cheaper than requested price.')
            user_amount = int(input('Enter your choice > '))
            cheaperThan(user_amount)
            first_menu()
        elif user_input == 6:
            print(f"""Thank you for using Dhruv's, Vidhi's and Janak's pizza order management system.
            """)
            break
        else:
            print("Enter a valid option \n\n")
            first_menu()
