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

class ProbabilityList:
    def __init__(self, li):
        self.probMap = {}
        for obj in li:
            self.probMap[obj] = 1.0/len(li)
    
    def getLength(self):
        return len(self.probMap)
    
    def remove(self, obj):
        try:
            self.probMap.pop(obj, None)
        except:
            pass
        for key in self.probMap:
            self.probMap[key] = 1.0/len(self.probMap)

    def removeAll(self, li):
        for obj in li:
            try:
                self.probMap.pop(obj, None)
            except:
                pass
        for key in self.probMap:
            self.probMap[key] = 1.0/len(self.probMap)

    def printProbabilities(self):
        for key in self.probMap:
            print(key, ": ", self.probMap[key])



def detective(murderer, murderWeapon, startRoom, endRoom):
    players = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    cards = people + weapons + rooms
    cards.remove(murderer)
    cards.remove(murderWeapon)
    cards.remove(startRoom)
    
    #deal cards out to players
    random.shuffle(cards)
    while cards:
        for i in range(6):
            players[i].append(cards.pop())
    
    possibleMurderers = ProbabilityList(people)
    possibleStartRooms = ProbabilityList(rooms)
    possibleWeapons = ProbabilityList(weapons)

    possibleMurderers.printProbabilities()
    print('\n')
    possibleWeapons.printProbabilities()
    print('\n')
    possibleStartRooms.printProbabilities()
    print('\n')

    for i in range(3):
        for j in range(6):
            obj = players[j].pop()
            print("********Drew: ", obj)
            possibleMurderers.remove(obj)
            possibleStartRooms.remove(obj)
            possibleWeapons.remove(obj)
            possibleMurderers.printProbabilities()
            possibleWeapons.printProbabilities()
            possibleStartRooms.printProbabilities()
            print()

def main():    
    #Pick a weapon, room, and murderer based on the logic rules
    murderer = people[random.randint(0, len(people)-1)]
    endRoom = rooms[random.randint(0, len(rooms)-1)]
    startRoom = None
    if murderer == 'Scarlett' or murderer == 'Peacock' or murderer == 'White':
        startRoom = adjacentRooms[endRoom][random.randint(0, 2)]
    else:
        startRoom = rooms[random.randint(0, len(rooms)-1)]
    tempLength = len(weaponsPerMurderer[murderer])
    murderWeapon = weaponsPerMurderer[murderer][random.randint(0, tempLength-1)]
    
    print("murderer: ", murderer, "\nweapon: ", murderWeapon, 
        "\nstart room: ", startRoom, "\nend room: ", endRoom, "\n")
    
    detective(murderer, murderWeapon, startRoom, endRoom)


if __name__ == '__main__':
    try:
        main()
    except:
        raise
