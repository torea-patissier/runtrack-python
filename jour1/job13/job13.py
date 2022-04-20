#job13
li = []
demande = 5
while len(li) < demande:
    item = input('Veuillez entrer un nombre :')
    if(item.isnumeric()):
        li.append(int(item))
        li.sort()
        print(li)
    else:
        print('Erreur')
