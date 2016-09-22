import os
import uuid
from datetime import datetime


class ExperimentGlobals:
    id = uuid.uuid1()
    experiment_name = ""
    base_path = "./"

    raw_data_path = base_path + "data/raw/"
    ex_data_path = base_path + "data/external/"
    inte_data_path = base_path + "data/interim/"
    data_path = base_path + "data/processed/"

    experiment_path = base_path + "experiments/" +\
                      datetime.now().strftime("%Y%m%d-%H:%M:%S") +\
                       "__id=" + str(id) + "/"

    ex_models_path = experiment_path + "models/"
    ex_logs_path = experiment_path + "logs/"

    for path in [experiment_path, models_path, logs_path]:
        os.system("mkdir -p {path}".format(path=path))

    @classmethod
    def to_dict(cls):
        # Return dict with all parameters!
        return {key:value for key, value in cls.__dict__.items()
            if not key.startswith("__")
            and not callable(key)
            and key != 'to_dict'
        }

__all__ = []
