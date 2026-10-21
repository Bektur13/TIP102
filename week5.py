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

    def print_inventory(self):
        if len(self.furniture) <= 0:
            print("Inventory empty")
        else: 
            print(", ".join(f"{item}: {self.furniture.count(item)}" for item in set(self.furniture)))


    
        
# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()



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

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next

def arr_to_ll(arr):
    # if not arr:
    #     return None

    head = Node(arr[0])
    current = head

    for item in arr[1:]:
        current.next = Node(item)
        current = current.next

    return head

mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list(arr_to_ll([mario, luigi, peach]))
print_linked_list(arr_to_ll([peach]))