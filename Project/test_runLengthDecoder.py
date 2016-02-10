import unittest

from RunLengthDecoder import RunLengthDecoder


class TestRunLengthDecoder(unittest.TestCase):

    def test_decode(self):
        test_value = [('t', 6), ('e', 1), ('s', 3), ('t', 1), ('1', 1)]
        run_length_decoder = RunLengthDecoder()

        self.assertRaises(ValueError,
                          lambda: run_length_decoder.decode())  # assert if method raises error when there is no input
        self.assertTrue(run_length_decoder.input is None)  # assert if input is none when it's not set

        run_length_decoder.input = test_value
        self.assertEqual(run_length_decoder.input, test_value)  # assert that input is initialized with proper value
        self.assertEqual(run_length_decoder.decode(),
                         "ttttttessst1")  # assert that result is correct

if __name__ == '__main__':
    unittest.main()
