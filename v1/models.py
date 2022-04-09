class ConvNet:
    def __init__(self, num_classes: int, kernel_size: int = 3, num_layers: int = 5):
        """A simple convolutional neural network.

        Args:
            num_classes: Number of possible classes
            kernel_size: Size of the convolutional filters
            num_layers: Number of convolutional layers
        """
        self.num_classes = num_classes
        self.kernel_size = kernel_size
        self.num_layers = num_layers

    def __repr__(self):
        key_values = [f"{key}={value}" for key, value in vars(self).items()]
        return f"{self.__class__.__name__}: {', '.join(key_values)}"
