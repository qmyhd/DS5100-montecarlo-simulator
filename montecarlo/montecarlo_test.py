import unittest
import numpy as np
import pandas as pd
from montecarlo.montecarlo import Die, Game, Analyzer

class TestDie(unittest.TestCase):

    def setUp(self):
        self.die = Die(np.array([1, 2, 3, 4, 5, 6]))

    def test_faces_not_numpy_array(self):
        """Check that input for faces is a numpy array."""
        faces = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            Die(faces)

    def test_faces_unique(self):
        """Check that faces array contains unique values."""
        faces = np.array([1, 2, 2])
        with self.assertRaises(ValueError):
            Die(faces)

    def test_change_weight(self):
        """Check setting weight to a valid numeric value."""
        self.die.change_weight(1, 2.0)
        self.assertEqual(self.die._die_df.loc[1, 'weights'], 2.0)

    def test_roll(self):
        """Check rolling die with valid number of rolls."""
        result = self.die.roll(10)
        self.assertEqual(len(result), 10)
        for face in result:
            self.assertIn(face, self.die._faces)

    def test_show(self):
        """Check getting die weights."""
        df = self.die.show()
        self.assertTrue(isinstance(df, pd.DataFrame))


class TestGame(unittest.TestCase):

    def setUp(self):
        self.die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.die2 = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.game = Game([self.die1, self.die2])

    def test_play(self):
        """Check playing game with valid number of rolls."""
        self.game.play(10)
        self.assertEqual(self.game._results_df.shape, (10, 2))

    def test_show_results(self):
        """Check retrieving play results with valid format."""
        self.game.play(10)
        df_wide = self.game.show_results('wide')
        self.assertEqual(df_wide.shape, (10, 2))
        df_narrow = self.game.show_results('narrow')
        self.assertEqual(df_narrow.shape, (20, 2))


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.die2 = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.game = Game([self.die1, self.die2])
        self.game.play(10)
        self.analyzer = Analyzer(self.game)

    def test_jackpot(self):
        """Check computing jackpot count."""
        jackpots = self.analyzer.jackpot()
        self.assertTrue(isinstance(jackpots, int))
        self.assertGreaterEqual(jackpots, 0)

    def test_face_counts_per_roll(self):
        """Check face counts per roll."""
        df = self.analyzer.face_counts_per_roll()
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_combo_counts(self):
        """Check combination counts."""
        df = self.analyzer.combo_counts()
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_permutation_counts(self):
        """Check permutation counts."""
        df = self.analyzer.permutation_counts()
        self.assertTrue(isinstance(df, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()