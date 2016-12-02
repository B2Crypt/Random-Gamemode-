from flask import Flask, render_template, flash, request, redirect, url_for, session
from wtforms import Form, TextField, PasswordField, BooleanField, validators,SelectField,TextAreaField
import random
import string

app = Flask(__name__)

class MainForm(Form):
    gamemode = SelectField(u'Select game:',choices=(['bf','BattleField4'],['rl','RocketLeague'],['hl','HardLine']))
    playerlimit = TextField(u'Set how many players on one team:')
    setPlayers = TextAreaField(u'Name the players (one per line):')


class BattleField4Form(Form):
    players = TextField(u'Players')

@app.route('/', methods=['GET','POST'])
def homepage():
    form = MainForm(request.form)
    try:
        if request.method == "POST":
            session['setPlayers'] = request.form['setPlayers']
            session['playerlimit'] = request.form['playerlimit']
            if request.form['gamemode'] == "bf":
                return redirect(url_for('BattleField4'))
            if request.form['gamemode'] == "hl":
                return redirect(url_for('HardLine'))
            if request.form['gamemode'] == "rl":
                return redirect(url_for('RocketLeague'))
    except Exception as e:
        return (str(e))
    return render_template('main.html',form=form)


@app.route('/BattleField4/', methods=['GET','POST'])
def BattleField4():
    try:

        #teams = session['playerlimit']
        #Fill in who's in for the game

        players = session['setPlayers'].split('\n')

        # Fill maps
        maps = ['Operation Metro','DawnBreaker','Operation Locker','Silk road','Shanghai','Dragon Valley','Flood Zone','Golmud Railway','Hainan Resort','Lancang Dam','Operation Outbreak','Paracel Storm','Rogue Transmision','Zavod 311','Zavod Natt','Altai Range','Dragon Pass','Guilin Peaks','Casbian Border','Gulf of Oman','Op Firestorm','Lost Island','Nanasha Strike','Operation Mortar','Wave Breaker','Lumphini Garden','Pearl Marked','Propaganda','Sunken Dragon','Gigants of Karelia','Hammerhead','Hangar 21','Operation Whiteout']

        # Fill in Gamemode
        GameMode = ['Rush','Domination','Conquest','Team Deathmatch']
        # This is sorting out how many player there is on ONE team, then it will fill in the remains on the rest.

        selectedMap = ''
        selectedGame = ''
        # Sorting out gamemode
        for gm in random.sample(GameMode,1):
            # Sorting out map
            for map in random.sample(maps,1):
                # Printing out map and gamemode
                #print ("You are going to play: " + str(gm) + " on " + (str(map)))
                selectedMap = map
                selectedGame = gm
        # Shuffle the list for Team1
        team1 = random.sample(players,int(session['playerlimit']))
        # Puts the rest of the players here.
        team2 = players
        playerTeam1 = team1
        playerTeam2 = team2
        try:
            #Selecting every players who is set in team1
            for pt1 in team1:
                #If some of the players is team1 is in team2, we remove whem
                if pt1 in team2:
                    team2.remove(pt1)
                    playerTeam2 = team2

        except Exception as e:
            #Printing out if we get some errors
            print (str(e))


        return render_template('battlefield4.html',team1=team1,team2=team2,selectedGame=selectedGame,selectedMap=selectedMap,playerTeam1=playerTeam1,playerTeam2=playerTeam2)
    except Exception as e:
        return (str(e))

@app.route('/HardLine/', methods=['GET', 'POST'])
def HardLine():
    try:
        # teams = session['playerlimit']
        # Fill in who's in for the game
        players = session['setPlayers'].split('\n')
        # Fill maps
        maps = ['Bank Job', 'Derailed', 'Downtown', 'Dust Bowl', 'Everglades', 'Growhouse', 'Hollywood heights', 'Night Job', 'Nightwood', 'Riptide', 'The Block', 'Backwood', 'Black Friday', 'Code blue','The Beat', 'Break Pointe', 'Museum', 'Precinct 7 ', 'The Dock', 'Diversion', 'Double Cross','Pacific Hightway', 'Train Dodge']
        # Fill in Gamemode
        GameMode = ['Blood Money', 'Domination', 'Conquest', 'Team Deathmatch']  # Fill in Gamemode
        # This is sorting out how many player there is on ONE team, then it will fill in the remains on the rest.
        selectedMap = ''
        selectedGame = ''
        # Sorting out gamemode
        for gm in random.sample(GameMode, 1):
            # Sorting out map
            for map in random.sample(maps, 1):
                # Printing out map and gamemode
                # print ("You are going to play: " + str(gm) + " on " + (str(map)))
                selectedMap = map
                selectedGame = gm
        # Shuffle the list for Team1
        team1 = random.sample(players, int(session['playerlimit']))
        # Puts the rest of the players here.
        team2 = players
        playerTeam1 = team1
        playerTeam2 = team2
        try:
            # Selecting every players who is set in team1
            for pt1 in team1:
                # If some of the players is team1 is in team2, we remove whem
                if pt1 in team2:
                    team2.remove(pt1)
                    playerTeam2 = team2

        except Exception as e:
            # Printing out if we get some errors
            print (str(e))

        return render_template('hardline.html', team1=team1, team2=team2, selectedGame=selectedGame,selectedMap=selectedMap, playerTeam1=playerTeam1, playerTeam2=playerTeam2)
    except Exception as e:
        return (str(e))

@app.route('/RocketLeague/', methods=['GET', 'POST'])
def RocketLeague():
    try:
        # teams = session['playerlimit']
        # Fill in who's in for the game
        players = session['setPlayers'].split('\n')
        # Fill maps
        maps = ['Wasteland', 'DFH Stadium', 'Underpass', 'Dobbel Goal', 'Urban Stadium', 'Mannfield', 'Beckwith Park',
                'Utopia Coliseum(Night)', 'Mannfield (Snowdy)', 'Beckwith Park(Stormy)', 'Beckwith Park(Midnight)',
                'Utopia Coliseum (Dusk)', 'DFH Stadium(Snowy)', '']

        cars = ['Backfire', 'BatMobile', 'Breakout', 'Delorean Time Machine', 'Dominus', 'Gizmos', 'Grog', 'Hotshot',
                'Merc', 'Octane', 'Paladin', 'Ripper', 'Road Hog', 'Scarab', 'Takumi', 'Venom', 'X-Devil',
                'Zippy']
        # This is sorting out how many player there is on ONE team, then it will fill in the remains on the rest.
        selectedMap = ''
        selectedCars = ''
        # Sorting out gamemode
        for car in random.sample(cars, 1):
            # Sorting out map
            for map in random.sample(maps, 1):
                # Printing out map and gamemode
                # print ("You are going to play: " + str(gm) + " on " + (str(map)))
                selectedMap = map
                selectedCars = car
        # Shuffle the list for Team1
        team1 = random.sample(players, int(session['playerlimit']))
        # Puts the rest of the players here.
        team2 = players
        playerTeam1 = team1
        playerTeam2 = team2
        try:
            # Selecting every players who is set in team1
            for pt1 in team1:
                # If some of the players is team1 is in team2, we remove whem
                if pt1 in team2:
                    team2.remove(pt1)
                    playerTeam2 = team2

        except Exception as e:
            # Printing out if we get some errors
            print (str(e))

        return render_template('RocketLeague.html', team1=team1, team2=team2, selectedCars=selectedCars,selectedMap=selectedMap, playerTeam1=playerTeam1, playerTeam2=playerTeam2)
    except Exception as e:
        return (str(e))


if __name__ == "__main__":
    app.run(debug=True)
