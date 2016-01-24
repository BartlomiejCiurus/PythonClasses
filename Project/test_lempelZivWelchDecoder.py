from unittest import TestCase

from Project.LempelZivWelchDecoder import LempelZivWelchDecoder

TEST_1_VALUE = ['t', 256, 257, 'e', 's', 260, 't', '1']


class TestLempelZivWelchDecoder(TestCase):
    def test_decode(self):
        run_length_decoder = LempelZivWelchDecoder()

        self.assertRaises(ValueError,
                          lambda: run_length_decoder.decode())  # assert if method raises error when there is no input
        self.assertTrue(run_length_decoder.input is None)  # assert if input is none when it's not set

        run_length_decoder.input = TEST_1_VALUE
        self.assertEqual(run_length_decoder.input, TEST_1_VALUE)  # assert that input is initialized with proper value
        self.assertEqual(run_length_decoder.decode(),
                         "ttttttessst1")  # assert that result is correct
