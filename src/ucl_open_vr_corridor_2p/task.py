# Import core types
from typing import Literal
from pydantic import Field

from swc.aeon.io import reader
from swc.aeon.schema import BaseSchema, data_reader

from ucl_open_vr_corridor_2p import __semver__

# TODO - should inherit from some TaskParameters base class rather than BaseSchema
class UclOpenVrCorridor2pTaskParameters(BaseSchema):
    ...


class UclOpenVrCorridor2pTaskLogic(BaseSchema):
    version: Literal[__semver__] = __semver__
    name: Literal["UclOpenVrCorridor2p"] = Field(default="UclOpenVrCorridor2p", description="Name of the task logic", frozen=True)
    task_parameters: UclOpenVrCorridor2pTaskParameters = Field(description="Parameters of the task logic")
    ...