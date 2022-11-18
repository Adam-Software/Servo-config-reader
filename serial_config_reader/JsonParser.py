import json
from typing import List

from serial_config_reader.Models.Joint import Joint
from serial_config_reader.Models.Motor import Motor


class JsonParser:

    @staticmethod
    def _ReadConfig(path: str):
        f = open(f'{path}')
        data = json.load(f)
        f.close()

        return data

    @staticmethod
    def ParseConfig(path: str) -> List[Motor]:
        config = JsonParser._ReadConfig(f'{path}')
        motors = []
        for element in config:
            motors.append(Motor(name=element['name'],
                                joint=Joint(element['joint']['lover_limit'],
                                            element['joint']['upper_limit'],
                                            element['joint']['speed'],
                                            element['joint']['id'])))
        return motors