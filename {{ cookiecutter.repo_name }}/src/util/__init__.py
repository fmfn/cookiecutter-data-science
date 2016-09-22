import logging
from datetime import datetime


class ModelLogger(object):
    def __init__(self, config):
        logging.basicConfig(
            filename=config.EXPERIMENT_GLOBALS.logs_path + "log",
            filemode='w',
            datefmt='%Y-%m-%d %H:%M:%S',
            format='%(asctime)-15s | %(message)s',
            level=logging.DEBUG
        )

        self.config = config
        self.context = None
        self.start = datetime.now()
        self.logger = logging.getLogger("experiment_logger")
        self.log_line("***** STARTING A NEW EXPERIMENT *****")
        self.log_line("")
        self._parameter_dump()

    def _parameter_dump(self):
        self.context = 'PARAM'

        self.log_line(
            "-------------------- Model Parameters --------------------")
        for config_file_name in self.config.__all__:
            config_file = getattr(self.config, config_file_name)

            self.log_line(config_file.__name__)
            for name in sorted(config_file.to_dict()):
                self.log_line("    {:20} : {}"\
                    .format(name, config_file.to_dict()[name]))
            self.log_line("")
        self.log_line(
            "----------------------------------------------------------")
        self.log_line("")

    def log_line(self, line, context=None):
        try:
            self.logger.info(context + " | " + line)
        except TypeError:
            try:
                self.logger.info(self.context + " | " + line)
            except TypeError:
                self.logger.info(line)
