import random
import numpy as np
import pandas as pd

class Die:
    '''A Class that models the rolls of dice (or tosses of a coin if 2-sided)'''
    
    def __init__(self, faces):
        
        '''Make sure faces are NumPy array, not a list, etc'''
        if not isinstance(faces, np.ndarray):
            raise TypeError("Input must be a NumPy array")
        
        '''Make sure no faces are repeated'''
        unique_faces=np.unique(faces)
        if len(unique_faces) != len(faces):
            raise ValueError("Faces must be unique")
            
        '''check that faces are all alpha or all numeric  '''  
        if not (np.all(np.char.isalpha(faces)) or np.all(np.isreal(faces))):
            raise ValueError("Faces must be all alphabetical or all numeric")
            
        self.faces = faces
        
        '''initiates fair dice to begin with'''
        weights = [1.0] * len(faces)  
        total_weight = sum(weights)
        
        self.weights = weights
        
        self.My_Die_DataFrame = pd.DataFrame(data = weights, index=faces)
        
        print(self.My_Die_DataFrame)
        

    
    def change_face_weight(self,face_change,new_weight):

        '''new weight must be a number or castable'''
        try:
            pd.to_numeric(new_weight)
        except Exception as err:          
            raise TypeError(f"'{new_weight}' cannot be cast as a numeric type.")        
        my_weight = pd.to_numeric(new_weight)
        
        '''check to see if die has this face'''
        if not(face_change in self.My_Die_DataFrame.index):
            raise IndexError("No such face on this die")
        else:
            self.My_Die_DataFrame.at[face_change, 0] = my_weight
    
        
    def roll(self, rolls=1):
        ''' models the rolls of the dice.  First, the seed is randomized'''
        random.seed()
        total_weight = sum(self.weights)
        self.normalized_weights = [weight / total_weight for weight in self.weights]
        
        self.outcomes_list = []
        for x in range(rolls):
            outcome = random.choices(self.faces, weights=self.normalized_weights)[0]
            self.outcomes_list.append(outcome)
            
        return self.outcomes_list
    
    def return_frame(self):
        
        '''pretty self-explanatory'''
        return self.My_Die_DataFrame
                                
                                
class Game:
    '''This class will call the Die class and simulate multiple rolls of multiple dice'''
    def __init__(self, dice):
        
        self.dice = dice
    
    def play(self,rolls):
        
        '''the actual rolling of the dice'''
        self.results = pd.DataFrame()
        self.rolls = rolls
        counter = 0
        
        for die in self.dice:
            my_roll = die.rolls(rolls=rolls)
            counter += 1
            my_rolls = pd.Series(my_roll, name = f'Die{counter}')
            self.results = pd.concat([self.results, my_rolls], axis = 1)
        
        self.results['Roll'] = self.results.index + 1
        self.results = self.results.set_index('Roll')
        
    def my_result(self, form = 'wide'):  
        
        '''setting the output format'''
        self.form = form
        if not (form == 'wide' or form == 'narrow'):
            raise ValueError("Form must be narrow or wide.") 
        elif form == 'wide':
            return self.results
        elif form == 'narrow':
            return self.results.stack().to_frame('Face')
        
        
import random
import numpy as np
import pandas as pd

class Analyzer:
    
    def __init__(self, game):

        self.game = game
        self.die_dtype = type(game.die_list[0])
        self.JPs = 0
        self.counts_df = pd.DataFrame()
        
    def jackpot(self):
        '''counts how many jackpots there were among all rolls.  A jackpot is when all dice have the same result'''
        
        self.jackpots = 0
        for i in range(1, self.game.my_result()):
            if self.game.my_result(i,1) == self.game.my_result(i,2) == self.game.my_result(i,3):
                self.jackpots += 1
                
        return self.jackpots        
    
    def face_count(self):
        '''counts how many times each face is rolled on each play'''

        '''could not get this to work, unless I did it by hand (like all dice have 6 faces)'''


        return 0
    
    def combinations(self):
        ''' no idea on this one'''
        
        return 0
    
    def permutations(self):
        '''or this one'''
        
    
    


        
        
