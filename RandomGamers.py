import sys
import random

def BattleField4():
    print ("Welcome to BattleField4")
    #Fill in who's in for the game
    players = ['Lars Ola','Stian','Petter','Trond','Aime']
    # Fill maps
    #maps = ['Operation Metro','DawnBreaker','Operation Locker','Silk road','Shanghai']
    maps = ['Operation Metro','DawnBreaker','Operation Locker','Silk road','Shanghai','Dragon Valley','Flood Zone','Golmud Railway','Hainan Resort','Lancang Dam','Operation Outbreak','Paracel Storm','Rogue Transmision','Zavod 311','Zavod Natt','Altai Range','Dragon Pass','Guilin Peaks','Casbian Border','Gulf of Oman','Op Firestorm','Lost Island','Nanasha Strike','Operation Mortar','Wave Breaker','Lumphini Garden','Pearl Marked','Propaganda','Sunken Dragon','Gigants of Karelia','Hammerhead','Hangar 21','Operation Whiteout']

    # Fill in Gamemode
    GameMode = ['Rush','Domination','Conquest','Team Deathmatch']
    # This is sorting out how many player there is on ONE team, then it will fill in the remains on the rest.
    teams = input('Tell me how many on one team (If its 4 players, it is logical to type 2: ')

    # Sorting out gamemode
    for gm in random.sample(GameMode,1):
        # Sorting out map
        for map in random.sample(maps,1):
            # Printing out map and gamemode
            print ("You are going to play: " + str(gm) + " on " + (str(map)))
    # Shuffle the list for Team1
    team1 = random.sample(players,teams)
    # Puts the rest of the players here.
    team2 = players
    try:
        #Selecting every players who is set in team1
        for pt1 in team1:
            #If some of the players is team1 is in team2, we remove whem
            if pt1 in team2:
                team2.remove(pt1)

    except Exception as e:
        #Printing out if we get some errors
        print (str(e))

    print "Team1:"
    for t1 in team1:
        print t1
    print "Team2:"
    for t2 in team2:
        print t2


def HardLine():
    print ("Welcome to HardLine")
    players = ['Lars Ola', 'Stian', 'Petter', 'Trond', 'Aime']  # Fill in who's in for the game
    maps = ['Bank Job','Derailed','Downtown','Dust Bowl','Everglades','Growhouse','Hollywood heights','Night Job','Nightwood','Riptide','The Block','Backwood','Black Friday','Code blue','The Beat','Break Pointe','Museum','Precinct 7 ','The Dock','Diversion','Double Cross','Pacific Hightway','Train Dodge']  # Fill maps
    GameMode = ['Blood Money', 'Domination', 'Conquest', 'Team Deathmatch']  # Fill in Gamemode

    teams = input(
        'Tell me how many on one team (If its 4 players, it is logical to type 2: ')  # This is sorting out how many player there is on ONE team, then it will fill in the remains on the rest.
    for gm in random.sample(GameMode, 1):  # Sorting out gamemode
        for map in random.sample(maps, 1):  # Sorting out map
            print ("You are going to play: " + str(gm) + " on " + (str(map)))  # Printing out map and gamemode
    team1 = random.sample(players, teams)  # Shuffle the list for Team1
    team2 = players  # Puts the rest of the players here.

    try:
        for pt1 in team1:
            if pt1 in team2:
                team2.remove(pt1)  # Removing players from team one who is in team two
    except Exception as e:
        print (str(e))

    print "Team1:"
    #Printing players to be on team1
    for t1 in team1:
        print t1
    #Printing players to be on team2
    print "Team2:"
    for t2 in team2:
        print t2

def RocketLeague():
    print ("Welcome to Rocket League")
    players = ['Lars Ola', 'Stian', 'Petter', 'Trond', 'Aime']  # Fill in who's in for the game
    maps = ['Wasteland', 'DFH Stadium', 'Underpass', 'Dobbel Goal', 'Urban Stadium','Mannfield','Beckwith Park','Utopia Coliseum(Night)','Mannfield (Snowdy)','Beckwith Park(Stormy)','Beckwith Park(Midnight)','Utopia Coliseum (Dusk)','DFH Stadium(Snowy)','']  # Fill maps
    cars = ['Backfire','BatMobile','Breakout','Delorean Time Machine','Dominus','Gizmos','Grog','Hotshot','Merc','Octane','Paladin','Ripper','Road Hog','Scarab','Takumi','Venom','X-Devil','Zippy']  # Fill in cars

    teams = input(
        'Tell me how many on one team (If its 4 players, it is logical to type 2: ')  # This is sorting out how many player there is on ONE team, then it will fill in the remains on the rest.
    for car in random.sample(cars, 1):  # Sorting out gamemode
        for map in random.sample(maps, 1):  # Sorting out map
            print ("You are going to play with : " + str(car) + " on " + (str(map)))  # Printing out map and gamemode
    team1 = random.sample(players, teams)  # Shuffle the list for Team1
    team2 = players  # Puts the rest of the players here.

    try:
        for pt1 in team1:
            if pt1 in team2:
                team2.remove(pt1)  # Removing players from team one who is in team two
    except Exception as e:
        print (str(e))

    print "Team1:"
    # Printing players to be on team1
    for t1 in team1:
        print t1
    # Printing players to be on team2
    print "Team2:"
    for t2 in team2:
        print t2

def Start():
    #SELECTING THE GAME BY INPUT FROM USER!
    selectedGame = raw_input('Select game: BF, HL or RL: ')

    if selectedGame.lower() == "bf":
        BattleField4()
    elif selectedGame.lower() == "hl":
        HardLine()
    elif selectedGame.lower() == "rl":
        RocketLeague()
    else:
        print ("I don\'t know this game!")
Start()