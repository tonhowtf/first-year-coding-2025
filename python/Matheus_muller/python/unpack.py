test = ("Tonho", 21)


"""nome = test[0]
idade = test[1]

print(f"nome: {nome} | idade: {idade}")"""


"""nome, idade = test
print(nome, idade)"""

def print_person_info(name, age):
    print(f"nome: {name} | idade: {age}")

for person in people:
    print(print_person_info(person[0], person[1]))