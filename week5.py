# Session 1 Problem Set 1
class Vintager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How is it going?"

appolo = Vintager("Apollo", "Eagle", "pah")

bones = Vintager("Bones", "Dog", "yip yip")
print(bones.greet_player("Bektur"))

        


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