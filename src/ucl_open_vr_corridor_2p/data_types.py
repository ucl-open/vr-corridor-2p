from ucl_open.rigs.base import BaseSchema
from ucl_open_vr_corridor_2p.task import Landmark

class PositionedLandmark(BaseSchema):
    landmark: Landmark
    position: float