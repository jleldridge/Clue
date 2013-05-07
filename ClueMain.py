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
    def __init__(self, endRoom):
        self.endRoom = endRoom
        self.peopleMap = {}
        self.weaponMap = {}
        self.roomMap = {}
        self.weapons = []
        for m in weaponsPerMurderer:
            self.weapons += weaponsPerMurderer[m]
        print(self.weapons)
        self.rooms = list(rooms)
        self.people = list(people)
        
        self.computeProbabilities()

    def computeProbabilities(self):
        for obj in people:
            self.peopleMap[obj] = 0.0
        for obj in self.people:
            self.peopleMap[obj] += 1.0/len(self.people)
        
        for obj in weapons:
            self.weaponMap[obj] = 0.0
        for obj in self.weapons:
            self.weaponMap[obj] += 1.0/len(self.weapons)

        for obj in rooms:
            self.roomMap[obj] = 0.0
        for obj in self.rooms:
            self.roomMap[obj] += 1.0/len(self.rooms)
    
    def remove(self, obj):
        if obj in people:
            self.removePerson(obj)
        elif obj in weapons:
            self.removeWeapon(obj)
        elif obj in rooms:
            self.removeRoom(obj)

    def removePerson(self, obj):
        self.people.remove(obj)
        for w in weaponsPerMurderer[obj]:
            try:
                self.weapons.remove(w)
            except:
                pass
        self.computeProbabilities()

    def removeWeapon(self, obj):
        for w in self.weapons:
            if w == obj:
                self.weapons.remove(w)
        self.computeProbabilities()
    
    def removeRoom(self, obj):
        self.rooms.remove(obj)
        self.computeProbabilities()

    def printProbabilities(self):
        for p in self.people:
            print(p, ": ", self.peopleMap[p])
        for w in set(self.weapons):
            print(w, ": ", self.weaponMap[w])
        for r in self.rooms:
            print(r, ": ", self.roomMap[r])
        print()


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
    
    plist = ProbabilityList(endRoom)

    for i in range(3):
        for j in range(6):
            obj = players[j].pop()
            print("********Drew: ", obj)
            plist.remove(obj)
            plist.printProbabilities()

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
