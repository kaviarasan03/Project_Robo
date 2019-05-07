import pandas as pd
import numpy as np
import os
import pygame,sys
from pygame.locals import*
import time
class rl:
    def __init__ (self,learn=0.12, rewardd=0.9999,egreedy=0.5):
        self.action=(0,1,2,3)
        self.lr=learn
        self.rd=rewardd #gama
        self.eps=egreedy #epsilon
        self.tab=pd.DataFrame(columns=self.action)
        pygame.init()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        UP = 'up'
        DOWN = 'down'
        LEFT = 'left'
        RIGHT = 'right'
        self.x = 0
        self.y = 0
        self.ell=0
        self.nee=0
        MOVESPEED = 1000
        direction = DOWN
        self.a = 1
        self.hi()
        ds=self.reset()
        print(ds)
    def stntex(self, state):
        if state not in self.tab.index:
            self.tab = self.tab.append(pd.Series([0] * len(self.action), index=self.tab.columns, name=state))
            print(self.tab)
    def chsact(self, o):
        self.stntex(o)
        if np.random.uniform() < self.eps:
            print("o",o)
            d = self.tab.ix[[o],:]
            print("s")
            lk= d.reindex(np.random.permutation(d.index))
            s = lk.max()[lk.max() == lk.max(axis=1).max()].index
            s = s[0]
            print(s)
            return(s)
        else:
            p = np.random.choice(self.action)
            return(p)
    def learn(self,g,u,r,j):
        self.n=self.ell
        self.m=self.nee
        self.stntex(j)
        print("le")
        va=self.tab.ix[[g],u]
        print("\n","va","\n",va)
        #self.n,self.m=j
        if  self.n > 34 and self.n < 116 and self.m > 34 and self.m < 116:
            target = r
        elif   self.n > 84 and self.n < 166 and self.m > 134 and self.m < 216:
            target = r

        elif  self.m>=5 and self.m<225 and self.n==0:
            target = r
        elif self.n>5and self.n < 225 and self.m == 5:
            target = r
        elif self.m >= 15 and self.m < 225and self.n == 190:
            target = r
        elif self.n >= 15 and self.n < 225 and self.m == 195:
            target = r
            print("if", target)


        else:

            target = r + self.rd * self.tab.ix[[j], :].max(axis=1) 
        print("target", target)
        self.tab.ix[[g],u]=self.tab.ix[[g],u]+u*(self.lr*(target-va))
        print("hi")
    def hi(self):
        a = pygame.display.set_mode((200, 250))
        print("f")
        while True:
            self.n = 10 + self.x
            self.m = 115 + self.y
            pygame.draw.circle(a, self.BLUE, (self.n, self.m), 10, 0)
            ops = pygame.draw.rect(a, self.RED, (50, 50, 50, 50))
            ops = pygame.draw.rect(a, self.RED, (100, 150, 50, 50))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            ob = self.reset()
            actio = self.chsact(ob)
            print("actio",actio)
            obj,r=self.step(actio)
            print("reward",r)
            self.learn(ob, actio, r, obj)

    def step(self, action):
        a = pygame.display.set_mode((200, 250))
        print("action",action)

        if action == 0:
            self.x += 10
            a.fill((0, 0, 0))
            pygame.display.flip()
        if action == 1:
            self.x -= 10
            a.fill((0, 0, 0))
            pygame.display.flip()
        if action == 2:
            self.y += 10
            a.fill((0, 0, 0))
            pygame.display.flip()
        if action == 3:
            self.y -= 10
            a.fill((0, 0, 0))
            pygame.display.flip()


        j = self.n, self.m
        #reward = 0
        self.ell = self.n
        self.nee = self.m
        if self.n > 34 and self.n < 116 and self.m > 34 and self.m < 116:
            reward = -2

            self.x = 0
            self.y =0


        elif self.n > 84 and self.n < 166 and self.m > 134 and self.m <= 216:
            reward = -2
            self.x = 0
            self.y = 0


        elif  self.m>=5 and self.m<225 and self.n==0:
            reward=-2
            self.x = 0
            self.y = 0

        elif self.n>5and self.n < 225 and self.m == 5:
            reward=-2
            self.x = 0
            self.y = 0

        elif self.m >= 15 and self.m < 225and self.n == 195:
            reward=-2
            self.x = 0
            self.y = 0
            print('uu')

        elif self.n >= 15 and self.n < 225 and self.m == 225:
            reward=-2
            self.x = 0
            self.y = 0

        else:
            reward = 1
        return j,reward
    def reset(self):
        print("reset")
        time.sleep(0.5)
        print(self.n, self.m)
        return (self.n, self.m)
if __name__ == '__main__':
    kira =rl()
