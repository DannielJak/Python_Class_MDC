def recipe(food,people):
# Ingredients and Recipe steps function
    if food == 1:
        print("--- You selected Ricotta ---")
        print()
        print(f"To cook for {people} people you will need:")
        print()
        if people == 1:
            print("1 litre of whole milk")
        else:
            print(f"- {people} litres of whole milk")
        if people == 1:
            print("1 tablespoon of salt")
        else:
            print(f"- {1/4 * people} tablespoons of salt")
        print(f"- {2 * people} tablespoons of lemon juice")
        print()
        input("--- Press enter to show the steps ---")
        print()
        print(f'''Preparation steps:
              
1) Gently heat the milk and salt in a medium saucepan over a low heat
   for about 10 minutes, stirring often, until it reaches 93°C.
2) Remove from the heat and stir in the lemon juice; the mixture should
   begin to look grainy.
3) Cover the pan and set aside for 10 minutes.
4) Line a sieve or colander with muslin and set over a bowl.
5) Use a slotted spoon to carefully spoon the curds into sieve; set aside
   for 45 minutes to drain off any excess whey.
6) The ricotta can now be eaten, plain or flavoured, or covered and chilled
   for up to 48 hours. ''')
        
    elif food == 2:
        print("--- You selected Waffles ---")
        print()
        print(f"To cook for {people} people you will need:")
        print()
        if people == 1:
            print(f"- 1 large egg")
        else:
            print(f"- {people} large eggs")
        if people == 1:
            print("- 1 cup of all-purpose flour")
        else:
            print(f"- {people} cups of all-purpose flour")
        print(f"- {0.375 * people} cups of vegetable oil")
        if people == 2:
            print("- 1 tablespoon of white sugar")
        else:
            print(f"- {0.5 * people} tablespoons of white sugar")
        print(f"- {2 * people} teaspoons of baking powder")
        if people == 8:
            print("- 1 teaspoon of salt")
        else:
            print(f"- {1/8 * people} teaspoons of salt")
        if people == 4:
            print("- 1 teaspoon of vanilla extract")
        else:
            print(f"- {1/4 * people} teaspoons of vanilla extract")
        print()
        input("--- Press enter to show the steps ---")
        print()
        print(f'''Preparation steps:
              
1) Preheat a waffle iron according to manufacturer's instructions.
2) Whisk eggs in a large bowl until light and fluffy.
3) Add flour, milk, and vegetable oil and mix to combine.
4) Whisk in sugar, then mix in baking powder, salt, and vanilla just until
   smooth, being careful not to overmix.
5) Spray the preheated waffle iron with nonstick spray.
6) Finally, pour batter onto the hot waffle iron and cook until golden brown and the
   iron stops steaming, from 3 to 5 minutes. ''')

    elif food == 3:
        print("--- You selected Lemon Rosemary Salmon ---")
        print()
        print(f"To cook for {people} people you will need:")
        print()
        if people == 1:
            print("- 1 lemon half, thinly sliced")
        elif people == 2:
            print("- 1 lemon, thinly sliced")
        else:
            print(f'- {0.5 * people} lemons, thinly sliced')
        print(f"- {2 * people} sprigs of fresh rosemary")
        if people == 1:
            print("- 1 salmon fillet, bones and skin removed")
        else:
            print(f"- {people} salmon fillets, bones and skin removed")
        if people == 2:
            print("- 1 tablespoon of olive oil")
        else:
            print(f'- {0.5 * people} tablespoons of olive oil')
        print()
        input("--- Press enter to show the steps ---")
        print()
        print(f'''Preparation steps:
              
1) Preheat the oven to 200°C.
2) Arrange half the lemon slices in a single layer in a baking dish.
3) Layer with {people + 1} rosemary sprigs, and top with salmon fillets.
4) Sprinkle salmon with salt, layer with remaining rosemary sprigs, and top
   with remaining lemon slices.
5) Drizzle with olive oil.
6) Finally, bake 20 minutes in the preheated oven, or until fish is easily
   flaked with a fork. ''')

    elif food == 4:
        print("--- You selected PB and Banana French Toast ---")
        print()
        print(f"To cook for {people} people you will need:")
        print()
        if people == 1:
            print("- 1 egg")
        else:
            print(f"- {people} eggs")
        if people == 1:
            print("- 1 dash of vanilla extract")
        else:
            print(f"- {people} dashes of vanilla extract")
        print(f"- {2 * people} tablespoons of creamy peanut butter")
        print(f"- {2 * people} bread slices")
        if people == 1:
            print("- 1 small banana, sliced")
        else:
            print(f"- {people} small bananas, sliced")
        print(f'- {2 * people} tablespoons of butter')
        print()
        input("--- Press enter to show the steps ---")
        print()
        print(f'''Preparation steps:
              
1) Lightly beat eggs and vanilla together in a shallow bowl.
2) Spread one tablespoon of peanut butter on top of each slice of bread.
3) Arrange banana slices on top of peanut butter on one slice of bread;
   place the other slice of bread, peanut butter-side down, on top of the
   banana to make a sandwich.
4) Melt butter on in a skillet over medium heat.
5) Dip sandwich into egg mixture until well coated; transfer into the heated
   skillet.
6) Cook until golden brown on one side, about 2 to 3 minutes; flip and
   continue cooking until other side is browned, about 2 minutes more.
7) Serve hot. ''')

    elif food == 5:
        print("--- You selected Garlic Bread Grilled Cheese ---")
        print()
        print(f"To cook for {people} people you will need:")
        print()
        print(f"- {2 * people} tablespoons of unsalted butter, softened")
        if people == 1:
            print("- 1 tablespoon of chopped fresh parsley")
        else:
            print(f'- {people} tablespoons of chopped fresh parsley')
        if people == 2:
            print("- 1 tablespoon of grated Pecorino Romano cheese")
        else:
            print(f"- {0.5 * people} tablespoons of grated Pecorino Romano cheese")
        if people == 2:
            print("- 1 clove of garlic, minced")
        else:
            print(f'- {0.5 * people} cloves of garlic, minced')
        print(f"- {2 * people} slices of white bread")
        print(f'- {2 * people} slices of provolone cheese')
        if people == 4:
            print("- 1 cup of shredded mozzarella cheese")
        else:
            print(f'- {0.25 * people} cups of shredded mozzarella cheese')
        print()
        input("--- Press enter to show the steps ---")
        print()
        print(f'''Preparation steps:
              
1) Heat a large skillet over medium heat.
2) Combine butter, parsley, Pecorino Romano cheese, and garlic in a small
   bowl. Stir to combine.
3) Lightly coat 1 side of each bread slice with the butter mixture. Flip
   bread and top half the slices evenly with provolone cheese and mozzarella
   cheese.
4) Cover with remaining bread slices, buttered-sides up.
5) Place sandwiches into the hot skillet. Cook until golden brown on one
   side, 3 to 4 minutes. Flip and cook until golden brown on the second side
   and cheese has melted, 3 to 4 minutes more.
6) Finally, cut each sandwich in half and serve. ''')

    else:
        print("You selected an invalid recipe number.")
print()
print(f'--- Welcome to this digital cookbook ---')
cook = "yes"
valid = "True"
# Loop start
while valid == "True":
    # First recipe and loop in case of needing another one
    if cook == "yes":
        print()
        print('''The recipes in this cookbook are:

1) Ricotta
2) Waffles
3) Lemon Rosemary Salmon
4) PB and Banana French Toast
5) Garlic Bread Grilled Cheese
''')
        # Input recipe number based on previous output
        food = input("> Which recipe do you want to cook?: ")
        # Checking for correct input (number from 1 to 5)
        real = food.isnumeric()
        if real == True:
            food = int(food)
            if 0 < food < 6:
                print()
                # Input amount of servings to calculate ingredients
                people = input("> How many people will you cook for?: ")
                # Checking for correct input (any natural number)
                real2 = people.isnumeric()
                valid2 = True
                while valid2 == True:
                    if real2 == True:
                        print()
                        valid2 = False
                        people = int(people)
                        # Function start
                        recipe(food,people)
                        print()
                        print("--- Enjoy ---")
                        print()
                        valid3 = True
                        while valid3 == True:
                            # Checking if user wants to see another recipe
                            cook = input("> Do you want to check another recipe? (yes/no): ")
                            if cook == "yes" or cook == "no":
                                print()
                                print(f'--- You selected "{cook}" ---')
                                valid3 = False
                            else:
                                print()
                                print("--- You must write yes or no to continue ---")
                                print()
                    # Incorrect input for servings
                    else:
                        print()
                        print("--- You must write an integer for the amount of people you are cooking for ---")
                        print()
                        people = input("> How many people will you cook for?: ")
                        real2 = people.isnumeric()
            # Incorrect input for recipe number (incorrect number)
            else:
                print()
                print("--- You must select a recipe number (1-5) ---")
        # Incorrect input for recipe number (not a number)
        else:
            print()
            print("--- You must select a recipe number (1-5) ---")
    # Program end
    elif cook == "no":
        print()
        print("Thanks for using this digital cookbook.")
        valid = "False"
    # Incorrect input to check for next recipe
    else:
        print()
        print('--- You must write "yes" or "no" to continue ---')
        print()
        cook = input("> Do you want to check another recipe? (yes/no): ")
