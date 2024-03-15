print('"Welcome to the hotdog calculator"')
print()

people = int(input("How many people will attend the cookout?: "))
hotdogs = int(input("How many hotdogs per person?: "))
print()

neededdogs = people * hotdogs

dogP = neededdogs // 10
dogR = neededdogs % 10

if dogR != 0:
    if dogP == 0:
        print("You will need 1 hotdog package.")
        print("You will have", 10 - neededdogs, "hotdogs left.")
    else:
        print("You will need", dogP + 1, "hotdog packages.")
        print("You will have", dogR, "hotdogs left.")
else:
    print("You will need", dogP, "hotdog packages.")
    print("You won't have hotdogs left.")

print()

bunP = neededdogs // 8
bunR = neededdogs % 8

if bunR != 0:
    if bunP == 0:
        print("You will need 1 bun package.")
        print("You will have", 10 - neededdogs, "buns left.")
    else:
        print("You will need", bunP + 1, "bun packages.")
        print("You will have", bunR, "buns left.")
else:
    print("You will need", bunP, "bun packages.")
    print("You won't have buns left.")