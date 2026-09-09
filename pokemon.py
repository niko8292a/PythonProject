while True:
    play = input("Do you want to play a pokemon? (y/n): ")

    if play == "n":
        print("Goodbye!")
        break

    pokemon = input("Which gen 1 starter do you want to play? (charmander, squirtle, bulbasaur) ")

    if pokemon == "charmander":
        enemypokemon = "bulbasaur"
        print("Alright, then ill choose bulbasaur!")

    if pokemon == "squirtle":
        enemypokemon = "charmander"
        print("Alright, then ill choose charmander!")

    if pokemon == "bulbasaur":
        enemypokemon = "squirtle"
        print("Alright, then ill choose squirtle!")


    myhealth = 60
    enemyhealth = 60

    fireball = 40
    watergun = 40
    vinewhip = 40
    tackle = 20
    heal = 10
    growl = 20


    while myhealth > 0 and enemyhealth > 0:

        print()
        print(f"{pokemon} has {myhealth} HP")
        print(f"{enemypokemon} has {enemyhealth} HP")
        print()

        print("Here are your moves")

        if pokemon == "charmander":
            print("1: fireball")
            print("2: heal")
            print("3: tackle")
            print("4: growl")

        if pokemon == "squirtle":
            print("1: watergun")
            print("2: heal")
            print("3: tackle")
            print("4: growl")

        if pokemon == "bulbasaur":
            print("1: vinewhip")
            print("2: heal")
            print("3: tackle")
            print("4: growl")


        move = input("Whats your move? ")

        if move == "1":

            if pokemon == "charmander":
                enemyhealth -= fireball
                print(f"{pokemon} used fireball!")
                print(f"{enemypokemon} lost {fireball} HP")

            if pokemon == "squirtle":
                enemyhealth -= watergun
                print(f"{pokemon} used watergun!")
                print(f"{enemypokemon} lost {watergun} HP")

            if pokemon == "bulbasaur":
                enemyhealth -= vinewhip
                print(f"{pokemon} used vinewhip!")
                print(f"{enemypokemon} lost {vinewhip} HP")


        if move == "2":
            myhealth += heal

            if myhealth > 60:
                myhealth = 60

            print(f"{pokemon} healed {heal} HP")


        if move == "3":
            enemyhealth -= tackle
            print(f"{pokemon} used tackle!")
            print(f"{enemypokemon} lost {tackle} HP")


        if move == "4":
            print(f"{pokemon} used growl!")
            print("It doesnt do anything yet!")


        if enemyhealth <= 0:
            print()
            print(f"{enemypokemon} fainted!")
            print()
            print(f"Your {pokemon} won!")
            break

        #modstanders tur

        enemydamage = 10

        myhealth -= enemydamage

        print()
        print(f"{enemypokemon} attacked!")
        print(f"{pokemon} lost {enemydamage} HP")

        if myhealth <= 0:
            print()
            print(f" your {pokemon} fainted!")
            print("You lost!")
            break