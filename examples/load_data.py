from dotmap import DotMap
import pandas as pd
from swc.aeon.io import load
from swc.aeon.schema.streams import Device
from ucl_open_vr_corridor_2p.data_types import MatrixArduinoData
from swc.aeon.io.reader import Csv


class MatrixArduinoReader(Csv):
    def __init__(self, pattern: str):
        """Initialize the object with a specified pattern and columns."""
        super().__init__(pattern, columns=("encoder_pos", "last_left_lick_time", "last_right_lick_time"))

exp = DotMap(
    [Device("MatrixArduino")]
)