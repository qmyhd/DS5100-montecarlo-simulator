```markdown
# Monte Carlo Simulator
DS 5100 | Summer 2024 

## Metadata
- **Package Name**: Montecarlo
- **Description**: Play a Game of Rolling Dice, and Analyze the Results of Those Rolls.
- **Version**: 1.0
- **Author**: Qais Youssef
- **License**: MIT License

## Installation Instructions
To install the package, use the following command:
```sh
pip install git+https://github.com/qmyhd/DS5100-FinalProject-qmy6cv.git
```

## Dependencies
- Python (>= 3.12.3)
- Pandas (>= 2.2.2)
- Numpy (>= 2.0.0)

## Usage
```python
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer
```

### Creating a Die Object
To create a die with custom faces:
```python
faces = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
die = Die(faces)
```

### Setting Weights for Die Faces
To set the weight of face 'A' to 3.0:
```python
die.change_weight('A', 3.0)
```

### Rolling the Die
Roll the die a specified number of times (e.g., roll 10 times):
```python
die.roll(10)
```

### Output of Rolling the Die
Example output after rolling the die 10 times:
```
['A', 'B', 'A', 'C', 'A', 'D', 'B', 'E', 'F', 'A']
```

### Retrieving Die Weights
To get the current weights of the die faces:
```python
die.show()
```

### Output of Retrieving Die Weights
Example output of die weights:
```
  Face  Weight
0    A     3.0
1    B     1.0
2    C     1.0
3    D     1.0
4    E     1.0
5    F     1.0
```

### Creating a Game Object
To create a game with multiple dice, use Die objects in a list:
```python
dice = [
    Die(np.array([1, 2, 3, 4, 5, 6])),
    Die(np.array([1, 2, 3, 4, 5, 6]))  # All Dice Must Have Same Faces
]
game = Game(dice)
```

### Playing the Game
To roll the dice a specified number of times (e.g., roll the dice 10 times):
```python
game.play(10)
```

### Output of Playing the Game
Example output after rolling the dice 10 times:
```
[[1, 2],
 [3, 4],
 [5, 6],
 [1, 1],
 [2, 3],
 [4, 5],
 [6, 1],
 [2, 2],
 [3, 3],
 [4, 4]]
```

### Retrieving the Most Recent Play Results
To get the results of the most recent play in wide format (default):
```python
game.show_results(form='wide')
```
or narrow format:
```python
game.show_results(form='narrow')
```

### Output of Retrieving Play Results
Example output in wide format:
```
    Die 1  Die 2
0      1      2
1      3      4
2      5      6
3      1      1
4      2      3
5      4      5
6      6      1
7      2      2
8      3      3
9      4      4
```

### Creating an Analyzer Object
To analyze the results of a game:
```python
analyzer = Analyzer(game)
```

### Counting Jackpots
To count the number of times the game resulted in a jackpot (i.e., all dice returned the same face in a roll):
```python
analyzer.jackpot()
```

### Output of Counting Jackpots
Example output of jackpots:
```
2
```

### Counting Face Occurrences
To count how many times a given face is rolled in each event:
```python
analyzer.face_counts_per_roll()
```

### Output of Counting Face Occurrences
Example output of face counts per roll:
```
   Roll  Face 1  Face 2  Face 3  Face 4  Face 5  Face 6
0     1       1       0       0       0       0       1
1     2       0       0       1       0       1       0
2     3       1       0       1       0       0       0
3     4       1       1       0       0       0       0
4     5       1       1       0       0       0       0
```

### Counting Combinations
To count the distinct combinations of faces rolled:
```python
analyzer.combo_counts()  # Returns MultiIndex pd.DataFrame
```

### Output of Counting Combinations
Example output of combination counts:
```
       Count
1 1       2
2 3       1
3 4       1
5 6       1
```

### Counting Permutations
To count the distinct permutations of faces rolled:
```python
analyzer.permutation_counts()
```

### Output of Counting Permutations
Example output of permutation counts:
```
       Count
1 2       1
3 4       1
5 6       1
1 1       1
2 3       1
4 5       1
6 1       1
2 2       1
3 3       1
4 4       1
```

## API Documentation

### Class: Die
A class representing a die with customizable faces and weights.

#### Initialization
```python
Die(faces: numpy.ndarray)
```
- **faces**: A NumPy array of faces for the die. Must be strings or numbers.

#### Methods
- `change_weight(face, new_weight)`
  - **face**: The face value to be changed. Must exist in initialized faces and be of the same datatype as elements in the face array.
  - **new_weight**: The new weight for the specified face. Must be numeric or castable as numeric.
- `roll(times=1)`
  - **times**: The number of times to roll the die. Defaults to 1.
- `show()`
  - **Returns**: A pandas DataFrame containing the weights of the die faces.

### Class: Game
A class representing a game played with multiple dice.

#### Initialization
```python
Game(dice: list)
```
- **dice**: A list of already instantiated Die objects.

#### Methods
- `play(rolls)`
  - **rolls**: The number of times the dice should be rolled.
- `show_results(form='wide')`
  - **form**: The format of the returned data frame. Must be 'wide' or 'narrow'. Defaults to 'wide'.

### Class: Analyzer
A class for analyzing the results of a game played with multiple dice.

#### Initialization
```python
Analyzer(game: Game)
```
- **game**: A Game object to be analyzed.

#### Methods
- `jackpot()`
  - **Returns**: An integer for the number of jackpots.
- `face_counts_per_roll()`
  - **Returns**: A pandas DataFrame with roll numbers as index, face values as columns, and count values in the cells.
- `combo_counts()`
  - **Returns**: A pandas DataFrame with a MultiIndex of distinct combinations and a column for the associated counts.
- `permutation_counts()`
  - **Returns**: A pandas DataFrame with a MultiIndex of distinct permutations and a column for the associated counts.
```
