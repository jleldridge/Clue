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
        'Kitchen': ['Kitchen', 'Dining', 'Ballroom'], 
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
        females = 0

        for obj in people:
            self.peopleMap[obj] = 0.0
        for obj in self.people:
            self.peopleMap[obj] += 1.0/len(self.people)
            if obj == 'Scarlett' or obj == 'Peacock' or obj == 'White':
                females += 1
        
        for obj in weapons:
            self.weaponMap[obj] = 0.0
        for obj in self.weapons:
            self.weaponMap[obj] += 1.0/len(self.weapons)

        for obj in rooms:
            self.roomMap[obj] = 0.0
        for obj in self.rooms:
            self.roomMap[obj] += 1.0/len(self.rooms)
        
        return females
    
    def haveGoodGuess(self):
        person = None
        weapon = None
        room = None

        for obj in self.people:
            if self.peopleMap[obj] >= 0.8:
                person = obj
        for obj in self.rooms:
            if self.roomMap[obj] >= 0.8:
                room = obj
        for obj in set(self.weapons):
            if self.weaponMap[obj] >= 0.8:
                weapon = obj
        if person and weapon and room:
            return (person, room, weapon)
        else:
            return False

    def remove(self, obj):
        if obj in people:
            self.removePerson(obj)
            return 0
        elif obj in weapons:
            self.removeWeapon(obj)
            return 2
        elif obj in rooms:
            self.removeRoom(obj)
            return 1

    def removePerson(self, obj):
        try:
            self.people.remove(obj)
        except:
            pass
        for w in weaponsPerMurderer[obj]:
            try:
                self.weapons.remove(w)
            except:
                pass
        females = self.computeProbabilities()
        if females == len(self.people):
            for r in self.rooms:
                if not r in adjacentRooms[self.endRoom]:
                    self.rooms.remove(r)
        self.computeProbabilities()
            
    
    def removeWeapon(self, obj):
        for w in self.weapons:
            if w == obj:
                self.weapons.remove(w)
        self.computeProbabilities()
        if not ("Wrench" in self.weapons or "Lead Pipe" in self.weapons):
            self.removePerson("Green")
        
        if len(self.weapons) == 1 and "Revolver" in self.weapons:
            self.removePerson("Mustard")

        if len(self.weapons) == 1 and "Rope" in self.weapons:
            self.removePerson("Peacock")
        
        if len(self.weapons) == 1 and "Dagger" in self.weapons:
            self.removePerson("Plum")
            self.removePerson("Scarlett")
    
    def removeRoom(self, obj):
        try:
            self.rooms.remove(obj)
        except:
            pass
        
        adj = False
        for r in self.rooms:
            if r in adjacentRooms[self.endRoom]:
                adj = True
        
        if not adj:
            for p in self.people:
                if p == "Scarlett" or p == "Peacock" or p == "White":
                    self.people.remove(p)
        
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
    
    counter = 1
    prw = [0, 0, 0]
    for i in range(3):
        for j in range(6):
            obj = players[j].pop()
            print("*********", counter, " Draw... Drew: ", obj)
            ctype = plist.remove(obj)
            prw[ctype] += 1
            plist.printProbabilities()
            counter += 1
            guess = plist.haveGoodGuess()
            if guess:
                return (guess, prw)

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
    

    temp = detective(murderer, murderWeapon, startRoom, endRoom)
    guess = temp[0]
    pcards = temp[1][0]
    rcards = temp[1][1]
    wcards = temp[1][2]
    
    print("Detective guess: ", guess, " in ", pcards, " People cards, ", rcards, " Room cards, and ", wcards, " Weapon cards.")
    print("Actual: ", (murderer, startRoom, murderWeapon))

if __name__ == '__main__':
    try:
        main()
    except:
        raise
