# Session 1 Problem Set 1
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How is it going, {self.catchphrase}"

    def set_cacthphrase(self, new_catchphrase):
        if len(new_catchphrase) <= 20 and new_catchphrase.replace(" ", "").isalpha():
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else: 
            print("Invalid catchphrase")

    def add_item(self, item_name):
        validValues = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in validValues:
            self.furniture.append(item_name)
    
        
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)


# appolo = Vintager("Apollo", "Eagle", "pah")

# bones = Vintager("Bones", "Dog", "yip yip")
# bones.catchphrase = "ruff it up"


        


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next





# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy") 
# tom_nook.next = tommy 
# tom_nook.next = None
# saharah = Node("Saharah")
# tommy.next = saharah
# # print(tom_nook.next) 
# # print(tommy.value) 
# # print(tommy.next.value)
# # print(saharah.value)  
# # print(saharah.next) 


# def print_list(list):
#     elements = []
#     current = list

#     while current:
#         elements.append(str(current.value))
#         current = current.next

#     return " -> ".join(elements)


# isabelle = Node("Isabelle")
# saharah = Node("Saharah")
# cj = Node("C.J.")

# isabelle.next = saharah
# saharah.next = cj
# print(print_list(isabelle))