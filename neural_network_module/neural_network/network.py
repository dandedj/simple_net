import numpy as np
from .layers import DenseLayer
from .activations import sigmoid, sigmoid_derivative

class Network:
    def __init__(self, learning_rate=0.01):
        self.layers = []
        self.learning_rate = learning_rate

    def add_layer(self, layer):
        self.layers.append(layer)

    def forward_propagate(self, X):
        for layer in self.layers:
            X = layer.forward(X)
        return X

    def back_propagate(self, X, y, output):
        for layer in reversed(self.layers):
            error = layer.calculate_error(y, output)
            layer.update_weights(self.learning_rate, error)
            y = layer.weights

    def train(self, X, y, epochs=1000):
        for _ in range(epochs):
            output = self.forward_propagate(X)
            self.back_propagate(X, y, output)

    def predict(self, X):
        return self.forward_propagate(X)