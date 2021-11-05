print("hello you! ik ben jan")
print("wie ben jij")
inputtxt = input ()
print("hallo", inputtxt)
print("ik ben nieuw op het mediacollege")
print("het is een nieuwe ervaring voor me")
print("maar ik ben helemaal tevreden waar ik nu ben")
print("dus ik ga je een quiz geven om een beetje overmezelf te zeggen")



def start():
    fouten = 0
    print("heb jij huisdieren?")
    print("A ik heb geen huisdieren")
    print("B ik heb 2 katten en een hond")
    print("C ik heb een vis")
    inputtxt = input ()
    if inputtxt == "A":
        fouten = fouten + 1
        if fouten > 1:
            start()
        print("nee dombo")
        print("jij bent zelf een dombo")
        print("):")
        print("je hebt een secret gevonden")
        print("wat?")
        print("ja een secret vraag")
        print("oke wat is de vraag")
        print("wat is mijn favoriete game")
        print("A minecraft")
        print("B ik heb geen favoriete game")
        print("C alle multiplayer vs shooters ")
        print("D terarria")
        print("E roblox games")
        inputtxt = input ()
        if  inputtxt == "A":
            fouten = fouten + 1
            print(fouten)
            if fouten > 1:
                start()
            print("nee dat is fout")
            print("eerste de meest bekende mogelijkheiden afstrepen")
        if inputtxt == "B":
            fouten = fouten + 1
            if fouten > 1:
                print(fouten)
                start()
            print("nee ik heb wel een favoriete game")
            print("mischien was het een trick question en speel je geen games")
        if inputtxt == "C":
            fouten = fouten + 1
            if fouten > 1:
                start()
            print("nee ik ben geen pubg csgo soort gamer")
            print("goedzo")
        if inputtxt == "D":
            print("dat was het goede antwoord")
        if inputtxt == "E":
            fouten = fouten + 1
            if fouten > 1:
                start()
            print("nee hoe oud denk je dat ik ben?")
            print("dat was geen vraag in de quiz dus")
    if inputtxt == "B":
        print("juist")
        print("WAT!!")
        print("ja")
        print("een dier is genoeg")
        print("niet voor mijn familie")
    if inputtxt == "C":
        fouten += 1
        if fouten > 1:
            start()
        print("vissen zijn saai")
        print("maakt toch niet uit")
        print("jij doe jij")
        print("dieren zij gewoon leuk")
    print("over familie gesproken")
    print("hoeveel familie heb jij thuis")
    print("A alleen een vader en moeder")
    print("B twee broertjes en vader en moeder")
    print("C ik met mijn moeder en twee broertjes")
    inputtxt == input ()
    if inputtxt == "A":
        fouten = fouten + 1
        if fouten > 1:
            start()
        print("nee dat is fout")
        print("jammer dan was het zo stil geweest")
        print("je raakt er gewend aan")
    if inputtxt == "B":
        fouten = fouten + 1
        if fouten > 1:
            start()
        print("nee geen vader")
        print("echt waar?")
        print("ja")
    if inputtxt == "C":
        print("dat is hem")
        print("hoe kan je moeder dat nou alleen")
        print("ze is best wel goed voor een moeder")
    print("en wat vind je lekker eten")
    print("goede vraag")
    print("A hamburger patat fastfood")
    print("B rijst zalm soup enzo")
    print("C spaghetti lasange")
    inputtxt == input ()
    if inputtxt == "A":
        fouten = fouten + 1
        if fouten > 1:
            start()
        print("een lekkere snackba~")
        print("nee")
        print("oh dat was een test")
        print("ja ja")
    if inputtxt == "B":
        fouten = fouten + 1
        if fouten > 1:
            start()
        print("er zijn lekkere dingen dan dat")
        print("ja dat is waar")
    if inputtxt == "C":
        print("daar ben ik het mee eens")
        print("hmmm heerlijk")
        print("hmmmm")
        print("hmmm")
        print("je bent klaar")
        print("dit was ez")

start()