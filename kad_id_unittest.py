from kad_id import *
import unittest
 
class TestIdMethods(unittest.TestCase):
    def setUp(self):
        self.id1_valid = 0b0001110010010010110011110011101011111101110100001011101000001111011101100100010000110100110010111101111110101101101100100111110000010001001100110111000000100111 
        self.id2_valid = 0b1111100100011110010011101001011110100000000100000110000000000100110001100101000110011000110001010110001100111111100111110111101001100001011000100100010101001011
        self.id_invalid = 0b11111100100011110010011101001011110100000000100000110000000000100110001100101000110011000110001010110001100111111100111110111101001100001011000100100010101001011

    def test1_distance(self):
        id1 = self.id1_valid
        id2 = self.id2_valid
        self.assertEqual(KadId.distance(id1, id2),
            0b1110010110001100100000011010110101011101110000001101101000001011101100000001010110101100000011101011110010010010001011010000011001110000010100010011010101101100,
            msg="Incorrect distance")
        # TODO test assertions
    
    def test2_compare_ref(self):
        id1 = self.id1_valid
        id2 = self.id2_valid
        self.assertEqual(KadId.compare_ref(id1, id1, id1),  0)
        self.assertEqual(KadId.compare_ref(id1, id2, id1), -1)
        self.assertEqual(KadId.compare_ref(id2, id1, id1),  1)
        # TODO test assertions

    def test3_compare_exp(self):
        id1 = self.id1_valid
        id2 = self.id2_valid
        self.assertEqual(KadId.compare_exp(id1, id2), 159)
        # TODO test assertions


if __name__ == '__main__':
    unittest.main()
