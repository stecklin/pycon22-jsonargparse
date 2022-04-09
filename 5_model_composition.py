from jsonargparse import CLI

from v3.datasets import Dataset
from v3.models import Model


def train(dataset: Dataset, model: Model):
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
