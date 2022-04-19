# pycon22-jsonargparse
Examples used in the talk "jsonargparse - Say goodbye to configuration hassles" at PyConDE / PyData Berlin 2022.

## Links
* Slides: https://speakerdeck.com/stecklin/jsonargparse-say-goodbye-to-configuration-hassles
* Recording: to be added soon
* jsonargparse: https://github.com/omni-us/jsonargparse

## 1st Live Demo

* same usage as argparse, additional information in the help (types, default values, docstring of function)
  * Compare `python 0_argparse.py --help` and `python 1_cli.py --help`
  * Run `python 1_cli.py PyCON --year 2022`
* possible to parse config files, pattern "Print config, edit config, run config"
  * Print config using `python 1_cli.py --print_config > config.yaml`
  * Edit config.yaml
  * Run `python 1_cli.py --config config.yaml`
* order of command line arguments decides if year is picked from config or from command line argument
  * Run `python 1_cli.py --config config.yaml --year 2024`
  * Run `python 1_cli.py --year 2024 --config config.yaml`
* possible to parse from environment variables
  * Run `PYCON_CONFERENCE_NAME=PyCON PYCON_YEAR=2024 python 2_cli_with_env_variables.py`

## 2nd Live Demo

* help shows only the top level configuration options, we can then look deeper into single groups
  * Run `python 3_image_classification.py --help` 
  * Run `python 3_image_classification.py --dataset.help Cifar10Dataset`
* type checks: useful error messages when invalid values are provided, access permissions are checked for paths
  * Run `python 3_image_classification.py --config configs/3_config.yaml --dataset.augment maybe`
  * Run `python 3_image_classification.py --config configs/3_config.yaml --dataset.data_dir /home/ghosts/`

## 3rd Live Demo

* select classes for --print_config, list of classes is displayed in help
  * Run `python 4_subclasses.py --help`
  * Run `python 4_subclasses.py --dataset ImageNetDataset --model ConvNet --print_config`
* possible to split config into subconfigs
  * Run `python 4_subclasses.py --config configs/4_config.yaml`
  * Run `python 4_subclasses.py --dataset configs/4_cifar10.yaml --model configs/4_conv_net.yaml`
  * Run `python 4_subclasses.py --config configs/4_config_with_subconfigs.yaml`
* arbitrary levels of nesting supported
  * Run `python 5_model_composition.py --config configs/5_config.yaml`
