from ucl_open.rigs.base import BaseSchema
from ucl_open_vr_corridor_2p.task import Landmark


class MatrixArduinoData(BaseSchema):
    encoder_pos: int
    last_left_lick_time: int
    last_right_lick_time: int
    last_sync_pulse_time: int
    photodiode_value: float
    last_2p_frame_time: int
    last_2p_line_time: int
    current_millis: int