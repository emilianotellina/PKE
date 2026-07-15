import logging


class LoggingManager:


    def setup(
        self,
        level="INFO"
    ):


        numeric_level = getattr(
            logging,
            level.upper(),
            logging.INFO
        )


        logging.basicConfig(
            level=numeric_level,
            format=
            "%(asctime)s "
            "[%(levelname)s] "
            "%(name)s: "
            "%(message)s"
        )


    def get_logger(
        self,
        name
    ):

        return logging.getLogger(name)