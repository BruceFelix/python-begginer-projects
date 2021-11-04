import random

names_of_people = []
def bill_splitter(bill, people):
    return round((bill / people), 2)
    
def people_coming():    
    print("Enter the number of friends joining (including you):")
    return int(input())
number_of_people = people_coming()
print()
if number_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number_of_people):
        names_of_people.append(input())
    print()    
    print("Enter the total bill: ")
    bill = int(input())
    dict_names = dict.fromkeys(names_of_people, (bill_splitter(bill, number_of_people)))
    print()
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No: ")
    feature = input()
    if feature == "Yes":
        lucky_person = random.choice(list(dict_names))
        print(f"{lucky_person} is the lucky one!")
        # bill = round((bill / number_of_people -1), 2)
        new_dict_names = dict.fromkeys(names_of_people, (bill_splitter(bill, number_of_people -1)))
        new_dict_names[lucky_person] = 0
        print(new_dict_names)
    else:
        print("No one is going to be lucky")
        print(dict_names)