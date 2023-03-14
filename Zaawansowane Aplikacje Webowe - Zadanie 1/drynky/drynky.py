class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Drink:
    def __init__(self, ingredients, volume):
        self.ingredients = ingredients
        self.volume = volume

class Barman:
    def createDrink(self, name1, amount1, name2, amount2, name3, amount3):
        ingredients = [Ingredient(name1, amount1), Ingredient(name2, amount2), Ingredient(name3, amount3)]
        total_amount = amount1 + amount2 + amount3
        proportions = [amount1 / total_amount, amount2 / total_amount, amount3 / total_amount]
        volume = total_amount * 2.5  # one unit is equal 2.5 mililiters
        return Drink(ingredients, volume)

    def printDrink(self, drink):
        names = [ingr.name for ingr in drink.ingredients]
        amounts = [ingr.amount for ingr in drink.ingredients]
        proportions = [ingr.amount / sum(amounts) for ingr in drink.ingredients]
        formatted_proportions = [f"{p:.2f}" for p in proportions]
        print(f"\nSkładniki drinka to: {', '.join(names)} \nW proporcjach {', '.join(formatted_proportions)}. \nJego pojemność to {drink.volume}ml\n")


barman = Barman()
drink = barman.createDrink("Sok ananasowy", 100, " Likier malibu(barbie)", 50, "mleko kokosowe", 100) # my drink is done now I can go and drink it :)
barman.printDrink(drink)
