import numpy as np
import pandas as pd

class Die:
    """A class representing a die with customizable faces and weights."""

    def __init__(self, faces):
        """
        Initialize the die with faces and default weights.

        Parameters:
        faces (numpy.ndarray): An array of faces for the die. Must be strings or numbers.

        Raises:
        TypeError: If faces is not a NumPy array.
        ValueError: If faces do not have unique values.
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array")
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces must have unique values")
        self._faces = faces
        self._weights = np.ones_like(faces, dtype=float)
        self._die_df = pd.DataFrame({'weights': self._weights}, index=self._faces)

    def change_weight(self, face, new_weight):
        """
        Change the weight of a specific face.

        Parameters:
        face: The face value to be changed.
        new_weight: The new weight for the specified face.

        Raises:
        ValueError: If the face is not in the die faces.
        TypeError: If the new weight is not numeric.
        """
        if face not in self._faces:
            raise ValueError("Face not found in die faces")
        if not isinstance(new_weight, (int, float)):
            raise TypeError("Weight must be numeric")
        self._die_df.loc[face, 'weights'] = new_weight

    def roll(self, times=1):
        """
        Roll the die a specified number of times.

        Parameters:
        times (int): The number of times to roll the die. Defaults to 1.

        Returns:
        list: A list of outcomes from the rolls.
        """
        return list(np.random.choice(self._faces, size=times, p=self._die_df['weights'] / self._die_df['weights'].sum()))

    def show(self):
        """
        Return the current state of the die.

        Returns:
        pandas.DataFrame: A DataFrame containing faces and their weights.
        """
        return self._die_df.copy()


class Game:
    """A class representing a game with multiple dice."""

    def __init__(self, dice):
        """
        Initialize the game with a list of dice.

        Parameters:
        dice (list): A list of already instantiated Die objects.
        """
        self._dice = dice

    def play(self, rolls):
        """
        Roll all dice a specified number of times.

        Parameters:
        rolls (int): The number of times the dice should be rolled.
        """
        results = {i: die.roll(rolls) for i, die in enumerate(self._dice)}
        self._results_df = pd.DataFrame(results)

    def show_results(self, form='wide'):
        """
        Return the results of the most recent play.

        Parameters:
        form (str): The format of the results, 'wide' or 'narrow'. Defaults to 'wide'.

        Returns:
        pandas.DataFrame: The results in the specified format.

        Raises:
        ValueError: If the form is not 'wide' or 'narrow'.
        """
        if form == 'wide':
            return self._results_df.copy()
        elif form == 'narrow':
            return self._results_df.melt(var_name='die', value_name='result')
        else:
            raise ValueError("Invalid format. Choose 'wide' or 'narrow'.")


class Analyzer:
    """A class for analyzing the results of a game."""

    def __init__(self, game):
        """
        Initialize the analyzer with a game object.

        Parameters:
        game (Game): A Game object to be analyzed.

        Raises:
        ValueError: If the input is not a Game object.
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object")
        self._results_df = game.show_results()

    def jackpot(self):
        """
        Count the number of jackpots in the game.

        Returns:
        int: The number of jackpots.
        """
        return int((self._results_df.nunique(axis=1) == 1).sum())

    def face_counts_per_roll(self):
        """
        Count the occurrences of each face per roll.

        Returns:
        pandas.DataFrame: A DataFrame with roll numbers as index and face counts as columns.
        """
        return self._results_df.apply(pd.Series.value_counts, axis=1).fillna(0)

    def combo_counts(self):
        """
        Count the distinct combinations of faces rolled.

        Returns:
        pandas.DataFrame: A DataFrame with counts of distinct combinations.
        """
        combos = self._results_df.apply(lambda row: tuple(sorted(row)), axis=1)
        return combos.value_counts().reset_index(name='count').rename(columns={'index': 'combo'})

    def permutation_counts(self):
        """
        Count the distinct permutations of faces rolled.

        Returns:
        pandas.DataFrame: A DataFrame with counts of distinct permutations.
        """
        perms = self._results_df.apply(tuple, axis=1)
        return perms.value_counts().reset_index(name='count').rename(columns={'index': 'permutation'})