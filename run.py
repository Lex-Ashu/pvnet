import os

os.environ["HYDRA_FULL_ERROR"] = "1"
import dotenv
import hydra
from omegaconf import DictConfig

# this file can be run for example using
#  python run.py experiment=example_simple

# load environment variables from `.env` file if it exists
# recursively searches for `.env` in all folders starting from work dir
dotenv.load_dotenv(override=True)


@hydra.main(config_path="configs/", config_name="config.yaml")
def main(config: DictConfig):

    # Imports should be nested inside @hydra.main to optimize tab completion
    # Read more here: https://github.com/facebookresearch/hydra/issues/934
    from predict_pv_yield.utils import extras, print_config
    from predict_pv_yield.training import train

    # A couple of optional utilities:
    # - disabling python warnings
    # - easier access to debug mode
    # - forcing debug friendly configuration
    # - forcing multi-gpu friendly configuration
    # You can safely get rid of this line if you don't want those
    extras(config)

    #

    # Pretty print config using Rich library
    if config.get("print_config"):
        print_config(config, resolve=True)

    # Train model
    return train(config)


if __name__ == "__main__":
    main()
