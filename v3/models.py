from abc import ABC


class Backbone(ABC):
    def __repr__(self):
        key_values = [f"{key}={value}" for key, value in vars(self).items()]
        return f"{self.__class__.__name__}: {', '.join(key_values)}"


class ConvNet(Backbone):
    def __init__(self, kernel_size: int = 3, num_layers: int = 5, *args, **kwargs):
        """A simple convolutional neural network.

        Args:
            kernel_size: Size of the convolutional filters
            num_layers: Number of convolutional layers
        """
        super().__init__(*args, **kwargs)
        self.kernel_size = kernel_size
        self.num_layers = num_layers


class VisionTransformer(Backbone):
    def __init__(self,
                 num_layers: int = 12,
                 num_heads: int = 12,
                 hidden_dim: int = 768,
                 mlp_dim: int = 3072,
                 *args,
                 **kwargs):
        """Implementation of Vision Transformer.

        Args:
            num_layers: Number of hidden layers in the Transformer encoder
            num_heads: Number of attention heads for each attention layer in the Transformer encoder
            hidden_dim: Dimensionality of the encoder layers and the pooler layer
            mlp_dim: Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder
        """
        super().__init__(*args, **kwargs)
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.hidden_dim = hidden_dim
        self.mlp_dim = mlp_dim


class Head(ABC):
    def __init__(self, num_classes: int):
        """Base class for all heads.

        Args:
            num_classes: Number of possible classes
        """
        self.num_classes = num_classes

    def __repr__(self):
        key_values = [f"{key}={value}" for key, value in vars(self).items()]
        return f"{self.__class__.__name__}: {', '.join(key_values)}"


class ClassificationHead(Head):
    pass


class ObjectDetectionHead(Head):
    pass


class Model:
    def __init__(self, backbone: Backbone, head: Head):
        self.backbone = backbone
        self.head = head

    def __repr__(self):
        return f"{self.backbone}  +  {self.head}"
