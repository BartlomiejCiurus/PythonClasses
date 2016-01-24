from unittest import TestCase

from Project.LempelZivWelchEncoder import LempelZivWelchEncoder

TEST_1_VALUE = "ttttttessst1"

class TestLempelZivWelchEncoder(TestCase):
    def test_encode(self):
        run_length_encoder = LempelZivWelchEncoder()

        self.assertRaises(ValueError,
                          lambda: run_length_encoder.encode())  # assert if method raises error when there is no input
        self.assertTrue(run_length_encoder.input is None)  # assert if input is none when it's not set
        self.assertEqual(0, len(run_length_encoder.memory))  # assert that memory is empty and initialized at start

        run_length_encoder.input = TEST_1_VALUE
        self.assertEqual(run_length_encoder.input, TEST_1_VALUE)  # assert that input is initialized with proper value
        self.assertEqual(run_length_encoder.encode(),
                         ['t', 256, 257, 'e', 's', 260, 't', '1'])  # assert that result is correct
        self.assertEqual(1, len(run_length_encoder.memory))  # assert that result is saved in memory

        run_length_encoder.encode()
        self.assertEqual(1, len(run_length_encoder.memory))  # assert that result is taken from memory
