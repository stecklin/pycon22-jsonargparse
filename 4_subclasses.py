from jsonargparse import CLI

from v2.datasets import Dataset
from v2.models import Model


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
