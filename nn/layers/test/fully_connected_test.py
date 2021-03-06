import numpy as np

from ..fully_connected import FullyConnected


def test_fc_forward_size(fully_connected: FullyConnected):
    n_inputs = fully_connected.n_inputs
    n_neurons = fully_connected.n_outputs
    batch_size = 2

    output = fully_connected.forward(
        np.random.uniform(
            size=(n_inputs, 1, batch_size)
        )
    )

    assert output.shape == (n_neurons, 1, batch_size)


def test_fc_forward_values(fully_connected: FullyConnected):
    fully_connected.weights = np.array([
        [1, 2],
        [5, 4],
        [1, 2],
        [5, 4]
    ])
    fully_connected.bias = 0.5
    inputs = np.array(
        [
            [[1, 2]],
            [[2, 1]]
        ]
    )

    output = fully_connected.forward(inputs)

    assert np.array_equal(
        output,
        np.array(
            [
                [[5.5, 4.5]],
                [[13.5, 14.5]],
                [[5.5, 4.5]],
                [[13.5, 14.5]]
            ]
        )
    )


def test_fc_backward_size(fully_connected: FullyConnected):
    n_inputs = fully_connected.n_inputs
    n_neurons = fully_connected.n_outputs
    batch_size = 2

    fully_connected.forward(
        np.random.uniform(
            size=(n_inputs, 1, batch_size)
        )
    )

    output = fully_connected.backward(
        np.random.uniform(
            size=(n_neurons, 1, batch_size)
        ),
        lr=0.1
    )

    assert fully_connected.weights.shape == (n_neurons, n_inputs)
    assert output.shape == (n_inputs, 1, batch_size)
