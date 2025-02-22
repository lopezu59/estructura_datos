# nums = list()
# def add(num:int):
#     nums.append(num)

#2
# nums = list()
# go: bool = True

# def attach(num:int)->None:
#         nums.append(num)
        
# def delete()->None:
#         nums.pop()
               
# while go:
#     print("select an option:")
#     print("1. add a number")
#     print("2. delete number")
#     print("3. log out")
#     option = int(input())
#     if option == 1:
#         attach(int(input("type a number:")))   
#         print(nums)
#     elif option == 2:
#         delete()
#         print(nums)
#     elif option == 3:
#         go = False

#3
people = dict()
go: bool = True

def attach(name: str, last_name: str) -> None:
    if name in people or last_name in people.values():
        print(f"The name '{name}' or the last name '{last_name}' already exist in the dictionary.")
    else:
        people[name] = last_name
                         
def delete(key: str) -> None:
    if key in people:
        del people[key]
    else:
        print(f"The value '{key}' does not exist in the dictionary.")
               
while go:
    print("select an option:")
    print("1. add a name")
    print("2. delete name")
    print("3. log out")
    option = int(input())
    if option == 1:
        name = input("type a name:")
        last_name = input("type a last name:")
        attach(name,last_name)
        print(people)
    elif option == 2:
        key = input("type the key to delete:")
        delete(key)
        print(people)
    elif option == 3:
        go = False