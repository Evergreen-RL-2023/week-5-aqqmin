'''
template: Richard Weiss, May 2023
The Gamblers Problem (gambler's ruin)
start with x dollars and bet on each round until
either the gambler reaches 0 (reward 0) or 100 (reward 1)

implement uniform random policy
'''
#import numpy as np
import random as rnd

N = 100
X = 50
PH = .4
E = .25
D = .9


class Agent(object):

    '''
        initialize the agent, states and actions, and their values
    '''
    def __init__(self, X, environment):
        self.env = environment
        self.initValue = 0
        self.memory = {}
        self.state = X
        self.epsilon = E
        for i in range(1,N):
            self.memory[i]={}
        for k in self.memory:
            for j in range(1,k+1):
                self.memory[k][j]=self.initValue
        

    def choose_action(self):
        if rnd.random() < self.epsilon:
            return rnd.randrange(1, self.state + 1)
        else:
            highest_val = 0
            key_of = 1
            for a in self.memory[self.state]:
                if self.memory[self.state][a] >= highest_val:
                    highest_val = self.memory[self.state][a]
                    key_of = a
            if highest_val == 0:
                key_of = rnd.randrange(1, self.state + 1)
            print("choosing bet {} with val {}".format(key_of, highest_val)) 
            return key_of

    def gamble_step(self):
        action = self.choose_action()
        print("betting{}".format(action))
        prior_state = self.state
        self.state += self.env.get_outcome(action)
        return prior_state,action
    
    def gamble_episode(self):
        actions_this_ep = []
        while self.state >= 1 and self.state<100:
            last_act_and_last_state = self.gamble_step()
            actions_this_ep.append(last_act_and_last_state)
        if self.state >= N:
            print("winner!")
            for i in range((len(actions_this_ep)-1),-1,-1):
                self.memory[actions_this_ep[i][0]][actions_this_ep[i][1]] = (self.memory[actions_this_ep[i][0]][actions_this_ep[i][1]] + 1 * (D ** (len(actions_this_ep) - i)))
        else:
            print("1loser!!")
        self.state = X


class Environment(object):
    def __init__(self):
        self.ph = PH
        self.agent = Agent(X, self)
    
    def get_outcome(self, action):
        if rnd.random() <= self.ph:
            return action
        else:
            return (0 - action)

        

if __name__ == '__main__':
    rnd.seed(42)
    env = Environment()
    print(env.agent.memory)
    for i in range(1000):
        env.agent.gamble_episode()
    
