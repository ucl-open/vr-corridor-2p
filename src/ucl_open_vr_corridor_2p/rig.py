from typing import Literal, Dict, Annotated, Union
from pydantic import Field

from ucl_open.rigs.base import BaseSchema
from ucl_open.rigs.device import Screen, SerialDeviceModule

from ucl_open_vr_corridor_2p import __semver__

# TODO - should be part of main package?
# TODO - should be able to define generic number of sync quads (e.g. for different screens)
class SyncQuad(BaseSchema):
    extent_x: float
    extent_y: float
    location_x: float
    location_y: float

class MatrixArduino(SerialDeviceModule):
    device_type: Literal["MatrixArduino"] = "MatrixArduino"
    
class MovementSource(BaseSchema):
    source_type: str
    
class SensorMovementSource(MovementSource):
    source_type: Literal["sensor_movement"]
    
class MouseWheelMovementSource(MovementSource):
    source_type: Literal["mouse_wheel"]
    gain: float
    
class PlaybackMovementSource(MovementSource):
    source_type: Literal["playback"]
    file_path: str
    position_index: int
    trial_index_index: int

class UclOpenVrCorridor2pRig(BaseSchema):
    version: Literal[__semver__] = __semver__
    screen: Screen
    gamma_correction_file: str = Field(description="Path to file to be used as gamma LUT.")
    sync_quad: SyncQuad
    arduino: MatrixArduino
    quad_time_lower_bound: float = Field(default=0.2)
    quad_time_upper_bound: float = Field(default=0.5)
    movement_source: Annotated[Union[SensorMovementSource, MouseWheelMovementSource, PlaybackMovementSource], Field(discriminator="source_type")]