from random import randint

class Room(object):
    def __init__(self, name, description, deathOnFailure=False, retryAttemptsLimit=None):
        self.name = name
        self.description = description
        self.paths = {}
        self.deathOnFailure = deathOnFailure
        self.retryAttemptsLimit = retryAttemptsLimit
        self.retryAttempts = 1

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central corridor",
""""
Aliens have invaded the ship
You're running down central corrider to the weapons Armoury
when an alien jumps in front of you and about to pull out his weapon
What do you do?
"""
)

laser_weapon_armory = Room("Laser Weapon Armery",
"""
You find a bomb with a keypad on it.
If you get the code wrong 10 times, you die.
The code is 3 digits long.
""", True, 10)

the_bridge = Room("The Bridge",
"""
You have a bomb in your hand running across the bridge.
5 aliens pop out of no where.
They don't attack because you have the bomb.
""")

escape_pod = Room("Escape Pod",
"""
There are 5 pods, which one do you take
""", True)

the_end_winner = Room("The End",
"""
You WIN!
""")

the_end_loser = Room("The End",
"""
You LOSE!
""")

escape_pod.add_paths({
'5' : the_end_winner,
'*' : the_end_loser})

generic_death = Room("death", "You died")

the_bridge.add_paths({'throw the bomb' : generic_death,
                        'slowly place the bomb' : escape_pod})

laser_weapon_armory.add_paths({'000' : the_bridge,
                                '*' : generic_death})

central_corridor.add_paths({'shoot!' : generic_death,
                            'dodge!' : generic_death,
                            'screem' : laser_weapon_armory})

START = 'central_corridor'

def load_room(name):
    print("load_room",name)
    return globals().get(name)



def name_room(room):
    for key, value in globals().items():
        if value == room:
            return key