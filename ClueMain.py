import sys, random

#set up possible weapons, rooms, and people
people = ['Mustard', 'Plum', 'Scarlett', 'Green', 'Peacock', 'White']
weapons = ['Dagger', 'Rope', 'Lead Pipe', 'Candlestick', 'Revolver', 
        'Wrench']
rooms = ['Study', 'Hall', 'Lounge', 'Library', 'Billiard', 'Conservatory',
        'Ballroom', 'Kitchen', 'Dining']
adjacentRooms = {'Study': ['Study', 'Hall', 'Library'], 
        'Hall': ['Hall', 'Study', 'Lounge'],
        'Lounge': ['Lounge', 'Hall', 'Dining'], 
        'Dining': ['Dining', 'Lounge', 'Kitchen'],
        'Kitchen': ['Kitchen', 'Dining', 'Ballrooom'], 
        'Ballroom': ['Ballroom', 'Conservatory','Kitchen'], 
        'Conservatory': ['Conservatory', 'Ballroom', 'Billiard'],
        'Billiard': ['Billiard', 'Conservatory', 'Library'], 
        'Library': ['Library', 'Billiard', 'Study']}
#Set up the possible murder weapons for each person based on the logic rules.
#To account for double probability of white using blunt weapons, added
#an extra of each blunt weapon to her possible weapons.
#Green will only use the pipe or wrench anyway, so no need to account for
#his higher probability of using blunt weapons.
weaponsPerMurderer = {
        'Mustard': ['Dagger', 'Rope', 'Lead Pipe', 'Candlestick', 'Wrench'],
        'Plum': ['Rope', 'Lead Pipe', 'Candlestick', 'Revolver', 'Wrench'],
        'Scarlett': ['Rope', 'Lead Pipe', 'Candlestick', 'Revolver', 'Wrench'],
        'Green': ['Lead Pipe', 'Wrench'],
        'Peacock':
            ['Dagger', 'Lead Pipe', 'Candlestick', 'Revolver', 'Wrench'],
        'White': ['Rope', 'Dagger', 'Lead Pipe', 'Lead Pipe','Candlestick', 
            'Candlestick', 'Revolver', 'Wrench', 'Wrench']}

def detective():
    players = {'p1':[], 'p2':[], 'p3':[], 'p4':[], 'p5':[], 'p6'[]}

def main():    
    #Pick a weapon, room, and murderer based on the logic rules
    murderer = people[random.randint(0, len(people)-1)]
    startRoom = rooms[random.randint(0, len(rooms)-1)]
    endRoom = None
    if murderer == 'Scarlett' or murderer == 'Peacock' or murderer == 'White':
        endRoom = adjacentRooms[startRoom][random.randint(0, 2)]
    else:
        endRoom = rooms[random.randint(0, len(rooms)-1)]
    tempLength = len(weaponsPerMurderer[murderer])
    murderWeapon = weaponsPerMurderer[murderer][random.randint(0, tempLength-1)]
    
    print("murderer: ", murderer, "\nweapon: ", murderWeapon, 
        "\nstart room: ", startRoom, "\nend room: ", endRoom, "\n")
    
if __name__ == '__main__':
    try:
        main()
    except:
        raise
