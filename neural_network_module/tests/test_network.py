import unittest
from neural_network.network import Network

class TestNetwork(unittest.TestCase):

    def setUp(self):
        self.network = Network()

    def test_add_layer(self):
        self.network.add_layer(10)
        self.assertEqual(len(self.network.layers), 1)

    def test_forward_propagation(self):
        self.network.add_layer(10)
        output = self.network.forward_propagation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(len(output), 10)

    def test_back_propagation(self):
        self.network.add_layer(10)
        self.network.forward_propagation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.network.back_propagation([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        # Check if weights have been updated
        self.assertNotEqual(self.network.layers[0].weights, [0]*10)

    def test_train(self):
        self.network.add_layer(10)
        self.network.train([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]], epochs=10)
        # Check if weights have been updated
        self.assertNotEqual(self.network.layers[0].weights, [0]*10)

if __name__ == '__main__':
    unittest.main()