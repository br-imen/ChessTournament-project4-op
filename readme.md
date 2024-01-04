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
* Register a player 
* Create a tournament 
* Show reports 
* Continue a tournament

and then follow the instructions

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