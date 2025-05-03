# exam
## Metadata:
Final project (Monte Carlo simulator for making dice, coins, etc)

## Synopsis:

There are three classes: Die, Game, and Analyzer.  Die and Game all work, but Analyzer does not work in testing (and only parts work when run from a notebook.

## Classes:

### Die Class:

#### Methods:

##### ``__init__(self, faces)``:
Initializer takes an array or list of ``faces``  
Makes sure array is NumPy Array  
Make sure faces are not repeated  
Initializes all weights to 1  
Makes sure face are either all numerical or all alpa

##### ``change_face_weight(self,face_change,new_weight)``:  
Makes sure weight is numeric or castable to numeric
Checks to see if face exists on die
changes a face weight 

##### ``roll(self, rolls=1)``:
rolls the die an inut number of times but the default is 1 roll.

##### ``return_frame(self)``:
Used to check if die has been set up or weight changed properly



### Game Class:
A  class that calles the roll method of Die multiple times.

#### Methods:

##### ``__init__(self, dice)``:
Initializer that takes already defined Dice as an input.  

##### ``play(self,roll)``:
A method that gets an input of how many times to roll.

##### ``my_result(self, form = 'wide')``:  
A method that shows the outout of the game


### Analyzer Class:
A class that analyzes the output of the Game class.

#### Methods:

##### ``___init__(self, game)``:
Checks to see if the input is a Game object (didn't get to work)  

##### ``jackpot(self)``:
A method that determines the number of jackpots (could not get to work with both 2- and 3-die games.  Had to change by hand).  

##### ``face_count(self)``:  
A method that counted how many times each face came up.  Also could not work unless tailored to each type of game.  

##### ``combinations(self)``:  
Returns instances of each combination of outputs.  Did not work.  

##### ``permutations(self)``:  
Returns instances of each permutation (ordered outcomes) of outputs.  Did not work.  







