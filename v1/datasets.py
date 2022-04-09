from jsonargparse.typing import path_type


class Cifar10Dataset:
    def __init__(self, data_dir: path_type("dr"), batch_size: int = 128, augment: bool = True):
        """Generates a dataset from CIFAR10 image files in a directory.

        Args:
            data_dir: Directory where the images are stored
            batch_size: Number of images in a single batch
            augment: Whether to do data augmentation (horizontal flipping, random cropping)
        """
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.augment = augment

    def __repr__(self):
        key_values = [f"{key}={value}" for key, value in vars(self).items()]
        return f"{self.__class__.__name__}: {', '.join(key_values)}"

