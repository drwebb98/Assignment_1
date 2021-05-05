#agentsframework.py

import random                                 

class Agent():
    def __init__(self, environment, agents, y , x):
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
        self.environment = environment
        self.agents = agents
        self.store = 0                          

# Moving agents               
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
 
# Allow agents to eat away from environment            
    def eat(self):                                      
        if self.environment[self.y][self.x] > 10:            
            self.environment[self.y][self.x] -= 10           
            self.store += 10                              

# Calculate distance between agents
    def distance_between(self, agents):
        return (((self.x - agents.x)**2) +
        ((self.y - agents.y)**2))**0.5

# Share information between agents and let them interact with each other
    def shared_with_neighbours(self, neighbourhood):
        for agents in self.agents:
            distance = self.distance_between(agents)
            if distance <= neighbourhood:
                if distance > 0:
                    average = ((self.store + agents.store) / 2)
                    self.store = average
                    agents.store = average
                    #print("sharing " + str(distance) + " " + str(average))
            