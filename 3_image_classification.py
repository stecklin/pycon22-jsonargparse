from jsonargparse import CLI

from v1.datasets import Cifar10Dataset
from v1.models import ConvNet


def train(dataset: Cifar10Dataset, model: ConvNet):
    """Trains a model on the given dataset.

    Args:
        dataset: Image dataset
        model: Neural network
    """
    print(f"Train using:")
    print(f"  {dataset}")
    print(f"  {model}")


if __name__ == '__main__':
    CLI(as_positional=False)
