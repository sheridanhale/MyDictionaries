person = {} # creates empty dictionary 
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #list
person["pets"] = {"dog": "Fido", "cat": "Sox"} #dictionary

print(person)

print(person['children'][1])

print(person['pets']['cat'])

#print names of all the children with for loop
for child in person['children']:
    print(child)

#print names of all the pets  with for loop
for p in person['pets']:
    print(person['pets'][p])