'''
template: Richard Weiss, May 2023
The Gamblers Problem (gambler's ruin)
start with x dollars and bet on each round until
either the gambler reaches 0 (reward 0) or 100 (reward 1)

implement uniform random policy
'''
import numpy as np
import random as rnd

N = 100
X = 50


class Agent(object):

    '''
        initialize the state
    '''
    def __init__(self, X, environment):
        self.env = environment
        self.initValue = 0
        self.memory = {}
        self.state = X
        for i in range(1,N):
            memory[i]={}
        for k in self.memory:
            for j in range(1,k+1):
                self.memory[k][j]=initValue
        

    def choose_action(self):
        return rnd.randrange(1, self.state + 1)

    def gamble_step(self):
        action = choose_action()
        prior_state = self.state
        self.state += get_outcome(action)
        return prior_state,action
    
    def gamble_episode(self):
        while self.state >= 1 or self.state<100:
            last_act_and_last_state = gamble_step()
        if self.state >= N:
            self.memory[last_act_and_last_state[0]][last_act_and_last_state[1]] = (self.memory[last_act_and_last_state[0]][last_act_and_last_state[1]] + 1)
        self.state = X


class Environment(object):
    def __init__(self):
        self.ph = .4
        self.agent = Agent(X, self)
    
    def get_outcome(self, action):
        if rnd.randrange(0,1) < ph:
            return action
        else:
            return (0 - action)

        

if __name__ == '__main__':
    rnd.seed(42)
