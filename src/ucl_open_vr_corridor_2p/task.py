# Import core types
from typing import Literal, Optional, List
from pydantic import Field

from swc.aeon.io import reader
from swc.aeon.schema import BaseSchema, data_reader

from ucl_open_vr_corridor_2p import __semver__

class TaskParameters(BaseSchema):
    rng_seed: Optional[float] = Field(default=None, description="Seed of the random number generator")
    
class Landmark(BaseSchema):
    size: float = Field(default=1, description="This landmark's size in VR space.")
    texture: str
    reward_valence: int = Field(default=0, description="Flag describing this landmark's reward valence.")
    
class Trial(BaseSchema):
    landmarks: List[List[Landmark]]
    boundary_threshold: float = Field(default=1, description="Buffer applied to far boundary of corridor to determine stopping distance.")
    end_trial_threshold: float = Field(default=1.5, description="Buffer applied to far boundary of corridor to determine trial end distance.")
    maximum_trial_time: float = Field(default=60, description="Maximum amount of time to spend on this trial.")
    inter_trial_interval: float = Field(default=3, description="After boundary is reached, how long to wait before proceeding to next trial.")
    detect_lick_threshold: float = Field(default=-1, description="Threshold after which licks are detected.")
    auto_reward_threshold: float = Field(default=10, description="Reward is automatically given after this threshold is reached.")
    
class Block(BaseSchema):
    available_trials: List[Trial]
    randomise_trial_order: bool = Field(default=False)
    max_trials: int = Field(default=10, ge=1)
    

# TODO - should inherit from some TaskParameters base class rather than BaseSchema
class UclOpenVrCorridor2pTaskParameters(BaseSchema):
    corridor_width: float = Field(default=2)
    blocks: List[Block]


class UclOpenVrCorridor2pTaskLogic(BaseSchema):
    version: Literal[__semver__] = __semver__
    name: Literal["UclOpenVrCorridor2p"] = Field(default="UclOpenVrCorridor2p", description="Name of the task logic", frozen=True)
    task_parameters: UclOpenVrCorridor2pTaskParameters = Field(description="Parameters of the task logic")
    ...