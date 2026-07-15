import argparse

from pke.version import VERSION

from pke.core.config import ConfigManager

from pke.core.logging import LoggingManager

from pke.core.plugins import PluginManager



def main():

    parser = argparse.ArgumentParser(
        prog="pke"
    )


    parser.add_argument(
        "--version",
        action="store_true"
    )


    parser.add_argument(
        "command",
        nargs="?"
    )


    args = parser.parse_args()



    if args.version:

        print(
            f"PKE {VERSION}"
        )

        return


    if args.command == "plugin":

        manager = PluginManager()

        print(
            "Installed plugins:"
        )

        for plugin in manager.registry.all():

            print(
                plugin.name,
                plugin.version
            )

    return

    logging = LoggingManager()

    logging.setup()



    logger = logging.get_logger(
        "pke"
    )


    config = ConfigManager()

    cfg = config.load()


    logger.info(
        "PKE started"
    )


    logger.info(
        f"Project: {cfg.project.name}"
    )



if __name__ == "__main__":
    main()