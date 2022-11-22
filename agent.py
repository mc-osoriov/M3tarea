from mesa import Agent
import numpy as np
import random


class GrassAgent(Agent):
    def __init__(self,id, x, y, model):
        super().__init__(id, model)
        self.id = id
        self.model = model
        self.coords = x,y
        self.desc = "Grass"
    def step(self):
        return
    def advance(self):
        return
        
class RoadAgent(Agent):
    def __init__(self,id, x, y, model):
        super().__init__(id, model)
        self.id = id
        self.coords = x,y
        self.model = model
        self.desc = "Road"
    def step(self):
        return
    def advance(self):
        return

class TrafficLightAgent(Agent):
    def __init__(self,id, x, y, direction, model):
        super().__init__(id, model)
        self.id = id
        self.coords = x,y
        self.model = model
        self.direction = direction
        self.state = "Yellow"
        self.desc = "TrafficLight"
        self.dist = 1000
    def step(self):
        self.dist=1000
        if self.direction == 0:
            print("dir 0:")
            cellList = self.model.grid.get_cell_list_contents([(self.coords[0]+1, self.coords[1]),(self.coords[0]+2, self.coords[1]), (self.coords[0]+3, self.coords[1])])
            for agent in cellList:
                print("Found agent 0:")
                newCoords = agent.coords
                aux = newCoords[0] - 1
                newCoords = aux, newCoords[1]
                print(newCoords)
                dist = newCoords[0] - self.coords[0] - 1
                print(dist)
                self.dist = dist

        if self.direction == 1:
            print("dir 1:")
            cellList = self.model.grid.get_cell_list_contents([(self.coords[0], self.coords[1]-1),(self.coords[0], self.coords[1]-2), (self.coords[0], self.coords[1]-3)])
            for agent in cellList:
                print("Found agent 1:")
                newCoords = agent.coords
                aux = newCoords[1] + 1
                newCoords = newCoords[0], aux
                print(newCoords)
                dist = self.coords[1] - newCoords[1] - 1
                print(dist)
                self.dist = dist
        
        if self.direction == 2:
            print("dir 2:")
            cellList = self.model.grid.get_cell_list_contents([(self.coords[0]-1, self.coords[1]),(self.coords[0]-2, self.coords[1]), (self.coords[0]-3, self.coords[1])])
            for agent in cellList:
                print("Found agent 2:")
                newCoords = agent.coords
                aux = newCoords[0] + 1
                newCoords = aux, newCoords[1]
                print(newCoords)
                dist = self.coords[0] - newCoords[0] - 1
                print(dist)
                self.dist = dist

        if self.direction == 3:
            print("dir 3:")
            cellList = self.model.grid.get_cell_list_contents([(self.coords[0], self.coords[1]+1),(self.coords[0], self.coords[1]+2), (self.coords[0], self.coords[1]+3)])
            for agent in cellList:
                print("Found agent 3:")
                newCoords = agent.coords
                aux = newCoords[1] - 1
                newCoords = newCoords[0], aux
                print(newCoords)
                dist = newCoords[1] - self.coords[1] - 1
                print(dist)
                self.dist = dist
        
        allLights = self.model.grid.get_cell_list_contents([(3,4), (6,5), (4,6), (5,3)])
        lowestDist = 1000
        agentLowestDist = None
        for agent in allLights:
            if type(agent) == TrafficLightAgent:
                print(agent.dist)
                if agent.dist < lowestDist:
                    agentLowestDist = agent
                    
        if agentLowestDist is not None:
            checkRoad = False

            RoadCells = self.model.grid.get_cell_list_contents([(6,5),(3,4),(4,6), (5,3), (4,4), (4,5), (5,4), (5,5)])
            for agent in RoadCells:
                if type(agent) == CarAgent:
                    checkRoad = True
    
            if checkRoad == False:
                agentLowestDist.state = "Green"
            if agentLowestDist.direction == 0:
                print("Hi0 " + str(agentLowestDist.dist))
                oppositeLights = self.model.grid.get_cell_list_contents([(5,3), (4,6)])
                for agent in oppositeLights:
                    if agentLowestDist.state == "Green":
                        agent.state = "Red"
                    elif agentLowestDist.state == "Red":
                        agent.state = "Green"
                sameLight = self.model.grid.get_cell_list_contents([(3,4)])
                for agent in sameLight:
                    agent.state = agentLowestDist.state

            elif agentLowestDist.direction == 1:
                print("Hi1 " + str(agentLowestDist.dist))
                oppositeLights = self.model.grid.get_cell_list_contents([(3,4), (6,5)])
                for agent in oppositeLights:
                    if agentLowestDist.state == "Green":
                        agent.state = "Red"
                    elif agentLowestDist.state == "Red":
                        agent.state = "Green"
                sameLight = self.model.grid.get_cell_list_contents([(4,6)])
                for agent in sameLight:
                    agent.state = agentLowestDist.state
            
            elif agentLowestDist.direction == 2:
                print("Hi2 " + str(agentLowestDist.dist))
                oppositeLights = self.model.grid.get_cell_list_contents([(5,3), (4,6)])
                for agent in oppositeLights:
                    if agentLowestDist.state == "Green":
                        agent.state = "Red"
                    elif agentLowestDist.state == "Red":
                        agent.state = "Green"
                sameLight = self.model.grid.get_cell_list_contents([(6,5)])
                for agent in sameLight:
                    agent.state = agentLowestDist.state
            
            elif agentLowestDist.direction == 3:
                print("Hi3 " + str(agentLowestDist.dist))
                oppositeLights = self.model.grid.get_cell_list_contents([(3,4), (6,5)])
                for agent in oppositeLights:
                    if agentLowestDist.state == "Green":
                        agent.state = "Red"
                    elif agentLowestDist.state == "Red":
                        agent.state = "Green"
                sameLight = self.model.grid.get_cell_list_contents([(5,3)])
                for agent in sameLight:
                    agent.state = agentLowestDist.state
        
        
        return

    def advance(self):
        return

class CarAgent(Agent):
    def __init__(self,id, x, y, direction, model):
        super().__init__(id, model)
        self.id = id
        self.coords = x,y
        self.model = model
        self.speed = np.random.choice(np.arange(1, 4), p=[0.3, 0.4, 0.3])
        self.next_pos = None
        self.direction = direction
        self.desc = "TrafficLight"
    def step(self):

        
        #semaforo esquina inferior izquierda
        if self.direction == 0: 
            lightCheck = ""
            if self.coords[0] != 9:
                checkLight = self.model.grid.get_cell_list_contents([(self.coords[0]+1,self.coords[1])])
                for agent in checkLight:
                    if type(agent) == TrafficLightAgent:
                        lightCheck = agent.state
            if lightCheck == "Green" or lightCheck == "":
                if(self.coords[0] < 9):
                    if self.model.time % self.speed == 0:
                        self.next_pos = self.coords[0]+1, self.coords[1]
                else:
                    self.next_pos = self.coords[0], self.coords[1]+1
                    self.direction = 2

        #semaforo esquina superior izquierda
        elif self.direction == 1:
            lightCheck = ""
            if self.coords[1] != 0:
                checkLight = self.model.grid.get_cell_list_contents([(self.coords[0],self.coords[1]-1)])
                for agent in checkLight:
                    if type(agent) == TrafficLightAgent:
                        lightCheck = agent.state
            if lightCheck == "Green" or lightCheck == "":
                if(self.coords[1] > 0):
                    if self.model.time % self.speed == 0:
                        self.next_pos = self.coords[0], self.coords[1]-1
                else:
                    self.next_pos = self.coords[0]+1, self.coords[1]
                    self.direction = 3

        #semaforo esquina superior derecha
        elif self.direction == 2:
            lightCheck = ""
            if self.coords[0] != 0:
                checkLight = self.model.grid.get_cell_list_contents([(self.coords[0]-1,self.coords[1])])
                for agent in checkLight:
                    if type(agent) == TrafficLightAgent:
                        lightCheck = agent.state
            if lightCheck == "Green" or lightCheck == "":
                if(self.coords[0] > 0):
                    if self.model.time % self.speed == 0:
                        self.next_pos = self.coords[0]-1, self.coords[1]
                else:
                    self.next_pos = self.coords[0], self.coords[1]-1
                    self.direction = 0

        #semaforo esquina inferior derecha
        elif self.direction == 3:
            lightCheck = ""
            if self.coords[1] != 9:
                checkLight = self.model.grid.get_cell_list_contents([(self.coords[0],self.coords[1]+1)])
                for agent in checkLight:
                    if type(agent) == TrafficLightAgent:
                        lightCheck = agent.state
            if lightCheck == "Green" or lightCheck == "":
                if(self.coords[1] < 9):
                    if self.model.time % self.speed == 0:
                        self.next_pos = self.coords[0], self.coords[1]+1
                else:
                    self.next_pos = self.coords[0]-1, self.coords[1]
                    self.direction = 1
    def advance(self):
        if self.next_pos is not None:
            self.coords = self.next_pos
            self.model.grid.move_agent(self,self.coords)


#Agente diferente
class CarAgentDif(Agent):
    def __init__(self,id, x, y, direction, model):
        super().__init__(id, model)
        self.id = id
        self.coords = x,y
        self.model = model
        self.speed = np.random.choice(np.arange(1, 4), p=[0.3, 0.4, 0.3])
        self.next_pos = None
        self.direction = direction
        self.desc = "TrafficLight"
    def step(self):

        
        #semaforo esquina inferior izquierda
        if self.direction == 0: 
            lightCheck = ""
            if self.coords[0] != 9:
                checkLight = self.model.grid.get_cell_list_contents([(self.coords[0]+1,self.coords[1])])
                for agent in checkLight:
                    if type(agent) == TrafficLightAgent:
                        lightCheck = agent.state
            if lightCheck == "Green" or lightCheck == "":
                if(self.coords[0] < 4 or (self.coords[0] >= 5 and self.coords[0] < 9)):
                    if self.model.time % self.speed == 0:
                        self.next_pos = self.coords[0]+1, self.coords[1]
                elif(self.coords[0] == 4):
                    self.next_pos = self.coords[0], self.coords[1]
                    self.direction = 1
                elif(self.coords[0] == 9):
                    self.next_pos = self.coords[0], self.coords[1]+1
                    self.direction = 2
            elif lightCheck == "Red":
                self.next_pos = self.coords[0]+1, self.coords[1]

        #semaforo esquina superior izquierda
        elif self.direction == 1:
            lightCheck = ""
            if self.coords[1] != 0:
                checkLight = self.model.grid.get_cell_list_contents([(self.coords[0],self.coords[1]-1)])
                for agent in checkLight:
                    if type(agent) == TrafficLightAgent:
                        lightCheck = agent.state
            if lightCheck == "Green" or lightCheck == "":
                if(self.coords[1] > 5 or (self.coords[1] <= 4 and self.coords[1] > 0)):
                    if self.model.time % self.speed == 0:
                        self.next_pos = self.coords[0], self.coords[1]-1
                elif(self.coords[1] == 5):
                    self.next_pos = self.coords[0], self.coords[1]
                    self.direction = 2
                elif(self.coords[1] == 0):
                    self.next_pos = self.coords[0]+1, self.coords[1]
                    self.direction = 3

        #semaforo esquina superior derecha
        elif self.direction == 2:
            lightCheck = ""
            if self.coords[0] != 0:
                checkLight = self.model.grid.get_cell_list_contents([(self.coords[0]-1,self.coords[1])])
                for agent in checkLight:
                    if type(agent) == TrafficLightAgent:
                        lightCheck = agent.state
            if lightCheck == "Green" or lightCheck == "":
                if(self.coords[0] > 5 or (self.coords[0] <= 4 and self.coords[0] > 0)):
                    if self.model.time % self.speed == 0:
                        self.next_pos = self.coords[0]-1, self.coords[1]
                elif(self.coords[0] == 5):
                    self.next_pos = self.coords[0], self.coords[1]
                    self.direction = 3
                elif(self.coords[0] == 0):
                    self.next_pos = self.coords[0], self.coords[1]-1
                    self.direction = 0
            elif lightCheck == "Red":
                self.next_pos = self.coords[0]-1, self.coords[1]

        #semaforo esquina inferior derecha
        elif self.direction == 3:
            lightCheck = ""
            if self.coords[1] != 9:
                checkLight = self.model.grid.get_cell_list_contents([(self.coords[0],self.coords[1]+1)])
                for agent in checkLight:
                    if type(agent) == TrafficLightAgent:
                        lightCheck = agent.state
            if lightCheck == "Green" or lightCheck == "":
                if(self.coords[1] < 4 or(self.coords[1] >= 5 and self.coords[1] < 9)):
                    if self.model.time % self.speed == 0:
                        self.next_pos = self.coords[0], self.coords[1]+1
                elif(self.coords[1] == 4):
                    self.next_pos = self.coords[0], self.coords[1]
                    self.direction = 0
                elif(self.coords[1] == 9):
                    self.next_pos = self.coords[0]-1, self.coords[1]
                    self.direction = 1

    def advance(self):
        if self.next_pos is not None:
            self.coords = self.next_pos
            self.model.grid.move_agent(self,self.coords)