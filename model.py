from mesa import Model
from mesa.time import SimultaneousActivation, RandomActivationByType
from mesa.space import MultiGrid
import time
import numpy as np
import itertools
from agent import GrassAgent, TrafficLightAgent, CarAgent, CarAgentDif, RoadAgent


class StreetModel(Model):
    def __init__(self,M,N):
        self.grid = MultiGrid(M,N,False)
        self.x = M
        self.y = N
        self.schedule = SimultaneousActivation(self)
        self.running = True
        self.id = 0
        self.time = 0
        self.kill_agents = []


        pos = [0,1,2,3,6,7,8,9]
        for i in pos:
            for j in pos:
                a = GrassAgent(self.id, i, j, self)
                self.grid.place_agent(a, (i, j))
                self.schedule.add(a)
                self.id = self.id + 1
        
        posTraffic = [[3,4,2], [6,5,0], [4,6,3], [5,3,1]]

        for i in posTraffic:
            a = TrafficLightAgent(self.id, i[0], i[1], i[2], self)
            self.grid.place_agent(a, (i[0], i[1]))
            self.schedule.add(a)
            self.id = self.id + 1

        a = CarAgentDif(self.id, 0, 4, 0, self)
        self.grid.place_agent(a, (0, 4))
        self.schedule.add(a)
        self.id = self.id + 1

        a = CarAgent(self.id, 9, 5, 2, self)
        self.grid.place_agent(a, (9, 5))
        self.schedule.add(a)
        self.id = self.id + 1

        a = CarAgent(self.id, 5, 0, 3, self)
        self.grid.place_agent(a, (5, 0))
        self.schedule.add(a)
        self.id = self.id + 1

        a = CarAgent(self.id, 4, 9, 1, self)
        self.grid.place_agent(a, (4, 9))
        self.schedule.add(a)
        self.id = self.id + 1

        a = RoadAgent(self.id, 4, 4, self)
        self.grid.place_agent(a, (4, 4))
        self.schedule.add(a)
        self.id = self.id + 1

        a = RoadAgent(self.id, 4, 5, self)
        self.grid.place_agent(a, (4, 5))
        self.schedule.add(a)
        self.id = self.id + 1

        a = RoadAgent(self.id, 5, 4, self)
        self.grid.place_agent(a, (5, 4))
        self.schedule.add(a)
        self.id = self.id + 1

        a = RoadAgent(self.id, 5, 5, self)
        self.grid.place_agent(a, (5, 5))
        self.schedule.add(a)
        self.id = self.id + 1


        
                
    def step(self):
        self.schedule.step()
        self.time += 1
        for x in self.kill_agents:
            self.grid.remove_agent(x)
            self.schedule.remove(x)
            self.kill_agents.remove(x)