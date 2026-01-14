from typing import Literal, Dict
from pydantic import Field

from ucl_open.rigs.base import BaseSchema
from ucl_open.rigs.device import Screen

from ucl_open_vr_corridor_2p import __semver__

# TODO - should be part of main package?
# TODO - should be able to define generic number of sync quads (e.g. for different screens)
class SyncQuad(BaseSchema):
    extent_x: float
    extent_y: float
    location_x: float
    location_y: float

class UclOpenVrCorridor2pRig(BaseSchema):
    version: Literal[__semver__] = __semver__
    screen: Screen
    sync_quad: SyncQuad