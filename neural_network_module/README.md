# Neural Network Module

This is a simple Python module for creating and training a neural network. The module provides classes for creating layers, activation functions, and the network itself. It also includes a testing suite for verifying the functionality of the network.

## Installation

To install the module, navigate to the project directory and run the following command:

```bash
python setup.py install
```

## Usage

To use the module, you first need to import the necessary classes:

```python
from neural_network.network import Network
from neural_network.layers import DenseLayer
from neural_network.activations import relu
```

Then, you can create a network and add layers to it:

```python
network = Network()
network.add_layer(DenseLayer(10, relu))
```

You can train the network using the `train` method:

```python
network.train(X_train, y_train)
```

Where `X_train` and `y_train` are your training data and labels, respectively.

## Testing

To run the tests, navigate to the `tests` directory and run the following command:

```bash
python -m unittest discover
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.