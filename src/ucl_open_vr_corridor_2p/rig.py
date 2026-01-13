from typing import Literal, Dict
from pydantic import Field

from ucl_open.rigs.base import BaseSchema
import ucl_open.rigs.device as Device

from ucl_open_vr_corridor_2p import __semver__


class UclOpenVrCorridor2pRig(BaseSchema):
    version: Literal[__semver__] = __semver__
    ...