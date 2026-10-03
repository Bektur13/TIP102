# Session 1
# Problem Set 1
# Problem 1
def welcome():
    print("Welcome to The Hundred Acre Wood!")

# Problem 2
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# Problem 3
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")

# Problem 4
def get_item(items, x):
    if x >= len(items) or x < -len(items):
        return None
    print(items[x])

# Problem 5
def sum_honey(hunny_jars):
    sum = 0
    for hunny in hunny_jars:
        sum += hunny
    return sum

# Problem 6 
def doubled(hunny_jars):
    doubled_list = []
    for i in range(len(hunny_jars)):
        doubled_list.append(hunny_jars[i] * 2)
    return doubled_list

#  Problem 7
def count_less_than(race_times, threshold):
    count = 0
    for race in race_times:
        if(race < threshold):
            count += 1
    return count

#  Problem 8
def print_todo_list(tasks):
    print('Pooh To Dos:')
    for i in range(len(tasks)):
        print(f'{i + 1}. {tasks[i]}')

# Problem 9
def can_pair(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum % 2 == 0

# Problem 10
def split_haycorns(quantity):
    result = []
    for i in range(1, quantity + 1):
        divider = quantity / i
        if divider.is_integer():
            result.append(i)

    return result


# Problem 11
def tiggerfy(s):
    chars_to_remove = "tigerTIGER"
    table = str.maketrans("", "", chars_to_remove)
    cleaned = s.translate(table)
    return cleaned

# Problem 12
def locate_thistles(list):
    result = []
    for i in range(len(list)):
        if(list[i] == "thistle"):
            result.append(i)
    return result


# Session 2
# Problem 1
def reverse_function(sentence):
    list = sentence.split(" ")
    list.reverse()
    return " ".join(list)

# Problem 2
d