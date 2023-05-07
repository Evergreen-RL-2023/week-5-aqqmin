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
X = 45
PH = .4
E = .75
D = .3


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
            print(k)
            needed = N-k
            highest_bet = 0
            if needed < k:
                highest_bet = needed
            else:
                highest_bet  = k
            for j in range(1,highest_bet+1):
                self.memory[k][j]=self.initValue
        

    def choose_action(self):
        choose_from = list(self.memory[self.state].keys())
        if rnd.random() < self.epsilon:
            return rnd.choice(choose_from)
        else:
            highest_val = 0
            key_of = 1
            for a in self.memory[self.state]:
                if self.memory[self.state][a] >= highest_val:
                    highest_val = self.memory[self.state][a]
                    key_of = a
            if highest_val == 0:
                key_of = rnd.choice(choose_from)
            print("choosing bet {} with val {}".format(key_of, highest_val)) 
            return key_of

    def gamble_step(self):
        action = self.choose_action()
        #print("betting{}".format(action))
        prior_state = self.state
        self.state += self.env.get_outcome(action)
        return prior_state,action
    
    def gamble_episode(self):
        actions_this_ep = []
        while self.state >= 1 and self.state<100:
            last_act_and_last_state = self.gamble_step()
            actions_this_ep.append(last_act_and_last_state)
        print(actions_this_ep)
        if self.state >= N:
            print("winner!")
            for i in range((len(actions_this_ep)-1),-1,-1):
                new_val = (self.memory[actions_this_ep[i][0]][actions_this_ep[i][1]] + (1 * (D ** (len(actions_this_ep)-i-1))))
                #print(i)
                #print(actions_this_ep[i])
                print(D**(len(actions_this_ep)-i-1))
                print("updating val for state {} act {} to {}".format(actions_this_ep[i][0],actions_this_ep[i][1], new_val))                
                self.memory[actions_this_ep[i][0]][actions_this_ep[i][1]] = (self.memory[actions_this_ep[i][0]][actions_this_ep[i][1]] + (1 * (D ** (len(actions_this_ep)-i-1))))
        else:
            print("loser!!")
        self.state = X
    
    def print_state_bets(self):
        state_bets_list = []
        for i in self.memory:
            highest_val = max(self.memory[i], key=self.memory[i].get)
            val_tself=self.memory[i][highest_val]
            tup = (i, highest_val,val_tself)
            state_bets_list.append(tup)
        for i in state_bets_list:
            print("state {}".format(i))


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
    #print(env.agent.memory)
    for i in range(50000):
        env.agent.gamble_episode()
    env.agent.print_state_bets()
    
    
