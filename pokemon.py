while True:
    play = input("Do you want to play a pokemon? (y/n)? ")
    pokemon = input("Which gen 1 starter pokemon do you want to choose? (charmander, squirtle, bulbasaur) ")
    if pokemon == "charmander":
        enemypokemon = "bulbasaur"
        print("Alright, then ill choose bulbasaur")
    if pokemon == "squirtle":
        enemypokemon = "charmander"
        print("Alright, then ill choose charmander")
    if pokemon == "bulbasaur":
        enemypokemon = "squirtle"
        print("Alright, then ill choose squirtle")

    myhealth = 60
    enemyhealth = 60

    print("Ill let you begin, here are the moves your pokemon is able to do:")
    if pokemon == "charmander":
        begin_fire = input("1: fireball 2: heal 3: tackle 4: growl ")
    if pokemon == "squirtle":
        begin_water = input("1: water_gun 2: heal 3: tackle 4: growl ")
    if pokemon == "bulbasaur":
        begin_grass = input("1: vine_whip 2: heal 3: tackle 4: growl ")
    vine_whip = 40
    water_gun = 40
    fireball = 40
    tackle = 20
    heal = 10
    growl = 20

    if begin_fire == "fireball":
        enemyhealth2 = (enemyhealth - fireball)
        print(f"{enemypokemon} lost {fireball}HP")
        print(f"{pokemon} currently has {myhealth}HP.  {enemypokemon} currently has {enemyhealth2} HP")
    if begin_fire == "heal":
        myhealth2 = (myhealth + heal)
        print(f"{pokemon} gained {heal}HP")
        print(f"{pokemon} currently has {myhealth2}HP.  {enemypokemon} currently has {enemyhealth} HP")
    if begin_fire == "tackle":
        enemyhealth2 = (enemyhealth - tackle)
        print(f"{enemypokemon} lost {tackle}HP")
        print(f"{pokemon} currently has {myhealth}HP.  {enemypokemon} currently has {enemyhealth2} HP")