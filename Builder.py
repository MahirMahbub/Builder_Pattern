import abc


# class Item(metaclass=abc.ABCMeta):
#
#    def name(self):
#        pass
#    def packing(self):
#        pass
#    def price(self):
#        pass
#
# class Packing(metaclass=abc.ABCMeta):
#    def pack(self):
#        pass
#
# class Wrapper(Packing):
#     def pack(self):
#         return "Wrapper"
#
# class Bottle(Packing):
#     def pack(self):
#         return "Bottle"
class FoodItem( object ):
    def __init__(self):
        self.name = None

    def foodItemDetails(self):
        print( self.name )


class FoodList( object ):
    def __init__(self):
        self._foodItems = list()

    def addItems(self, foodItem):
        self._foodItems.append( foodItem )

    def printAllItems(self):
        i = 0
        while i < len( self._foodItems ):
            self._foodItems[i].foodItemDetails()
            i += 1

    def listDetails(self):
        pass


class FoodPackage( metaclass=abc.ABCMeta ):

    def addDrinks(self):
        pass

    def addMainFood(self):
        pass

    def addSweet(self):
        pass

    def printFoodPackge(self):
        pass


class MainItems( FoodList ):

    def listDetails(self):
        print( "Main Items Have: " )
        self.printAllItems()


class Meal( FoodPackage ):
    def __init__(self):
        self.drinks = Drinks()
        self.mainItems = MainItems()
        self.sweet = Candied()
        self.addDrinks()
        self.addMainFood()
        self.addSweet()

    def addDrinks(self):
        self.drinks.addItems( Water() )
        self.drinks.addItems( CocaCola() )

    def addMainFood(self):
        self.mainItems.addItems( Rice() )
        self.mainItems.addItems( Meat() )

    def addSweet(self):
        self.sweet.addItems( Dahi() )

    def printFoodPackage(self):
        print( "Details of Meal:" )
        self.drinks.listDetails()
        self.mainItems.listDetails()
        self.sweet.listDetails()


class Snakes( FoodPackage ):
    def __init__(self):
        self.drinks = Drinks()
        self.mainItems = MainItems()
        self.sweet = Candied()
        self.addDrinks()
        self.addMainFood()
        self.addSweet()

    def addDrinks(self):
        self.drinks.addItems( Water() )
        self.drinks.addItems( Tea() )

    def addMainFood(self):
        self.mainItems.addItems( Barger() )
        self.mainItems.addItems( Biscuit() )

    def addSweet(self):
        self.sweet.addItems( Sweet() )

    def printFoodPackge(self):
        print( "Details of Meal:" )
        self.drinks.listDetails()
        self.mainItems.listDetails()
        self.sweet.listDetails()


class Barger( FoodItem ):
    def __init__(self):
        self.name = "Barger"


class Sweet( FoodItem ):
    def __init__(self):
        self.name = "Sweet"


class Tea( FoodItem ):
    def __init__(self):
        self.name = "Tea"


class Meat( FoodItem ):
    def __init__(self):
        self.name = "Meat"


class Biscuit( FoodItem ):

    def __init__(self):
        self.name = "Biscuit"


class CocaCola( FoodItem ):

    def __init__(self):
        self.name = "Coca Cola"


class Dahi( FoodItem ):

    def __init__(self):
        self.name = "Dahi"


class Paratha( FoodItem ):
    def __init__(self):
        self.name = "Paratha"


class Water( FoodItem ):
    def __init__(self):
        self.name = "Water"


class Pepsi( FoodItem ):
    def __init__(self):
        self.name = "Pepsi"


class Rice( FoodItem ):
    def __init__(self):
        self.name = "Rice"


class Candied( FoodList ):
    def listDetails(self):
        print( "Candied have:" )
        self.printAllItems()


class Drinks( FoodList ):
    def listDetails(self):
        print( "Drinks have:" )
        self.printAllItems()


class BreakFast( FoodPackage ):
    def __init__(self):
        self.drinks = Drinks()
        self.mainItem = MainItems()
        self.sweet = Candied()
        self.addDrinks()
        self.addMainFood()
        self.addSweet()

    def addDrinks(self):
        self.drinks.addItems( Water() )
        self.drinks.addItems( Water() )

    def addSweet(self):
        self.drinks.addItems( Sweet() )

    def addMainFood(self):
        self.drinks.addItems( Paratha() )
        self.drinks.addItems( Meat() )

    def printFoodPackage(self):
        print( "Details" )
        self.drinks.listDetails()
        self.mainItem.listDetails()
        self.sweet.listDetails()


class Director( object ):
    def __init__(self):
        self.foodPackage = {}
        self.init()

    def init(self):
        self.foodPackage["breakfast"] = BreakFast()
        self.foodPackage["meal"] = Meal()
        self.foodPackage["snakes"] = Snakes()

    def getPackage(self, packageName):
        return self.foodPackage[packageName]


if __name__ == "__main__":
    packageName = input( "Please enter Package name(breakfast/meal/snakes): " )
    foodPackage = Director().getPackage( packageName )
    print(foodPackage)
    foodPackage.printFoodPackage()
