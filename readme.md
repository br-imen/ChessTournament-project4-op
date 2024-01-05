# Chess app

## Description:
It's the 4th project with Openclassrooms.
It's a program developed with Python that manage chess tournaments from registering players, adding players to tournaments, creating rounds, update matchs' scores and visualize some reports.
The code architecture uses the MVC model.
we use json file for saving players and tournaments in /data folder.


## Installation:

To run the program, prepare the environement and install requirements.txt, then execute the script chess.py.

```sh
python -m venv venv
source ven/bin/activate
pip install -r requirements.txt
```

## Getting started:

```sh
python3 chess.py
```

The application will be launched

you can then choose from the menu:
1. Register a player 
2. Create a tournament 
3. Show reports 
4. Continue a tournament
0. Quit

and then follow the instructions

### 1. Register a player

For registering a player, you start by giving player's informations such as first name, birthdate, ..., the ID player must be as two letters follwed by 5 numbers (i.e. AB12345)

### 2. Create a tournament

To create a tournament, you have to start by giving tournament's informations as name, place, number of rounds,...
When the tournament is created, a new menu will be displayed as:
    1. Add a player to tournament
    2. Start a round
    0. Quit

#### 1. Add player to tournament

To add a player to tournament, a table of all players will be displayed to choose from.
You can enter the id of the player, and you must register 2 players at minimum

#### 2. Start a round

When starting a round, the round and its matchs wil be displayed as tables. so you have to enter players' scores for each match as (1) if won, (2) if lost, (3) if a tie.
Then you can whether start another round or quit.

When the tournament is ended, the total scores for all matchs for the tournament will be displayed.

### 3. Show reports

You can check the reports to list all players or see reports for each tournaments:
    1. List of all players 
    2. See reports for one tournament 
    0. Go back 

#### 1. List of all players

Listing all players registered.

#### 2.See reports for one tournament

A table for all tournaments will be displayed to choose from.
You can enter the id of the tournament to see its reports:

    1. List of players for this tournament 
    2. List of rounds and matchs for this tournament 
    0. Go back

#### 1. List of players for this tournament 

Listing all players registered for this tournament 

#### 2. List of rounds and matchs of this tournament  

Listing all rounds with each match for this tournament.

### flake8
To generate a html flake report you have to run:

```sh
flake8 --format=html --htmldir=flake8_rapport
```
then you'll find the report under flake8_rapport folder

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.


## Authors and acknowledgments
Special Thanks to my mentor Amine Sghir and OpenClassrooms.