# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# timmy.right(30)
# timmy.forward(150)

# my_screen = Screen()
# print(my_screen.canvheight, my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable() #constructing object using the blueprint
print(table)
table.add_column("Pokemon Name", ["Squirtle", "Charizard", "Dialga", "Arcues", "Regigigas", "Rayquaza", "Pikachu", "Kyogre", "yveltal", "Magearna", "Marshadow", "Pinsir"])
print(table)
table.add_column("Type", ["Water", "Flying + Fire", "Dragon + Steel", "Normal", "Normal", "Dragon + Flying", "Electric", "Water", "Dark + Flying", "Fairy + Steel", "Fighting + Ghost", "Bug"], align = 'c')
print(table)
table.align = 'l'
print(table)



