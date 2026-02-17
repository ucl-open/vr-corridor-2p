import os

from ucl_open_vr_corridor_2p.task import (
    UclOpenVrCorridor2pTaskLogic,
    UclOpenVrCorridor2pTaskParameters,
    Block,
    Trial,
    Landmark
)

trial_base = Trial(landmarks=[
                        [Landmark(size=8, position=40, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=80, texture="plaid", reward_valence=0)],
                        [Landmark(size=8, position=120, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=160, texture="plaid", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=200, position=100, texture="BG1", reward_valence=0, center_offset=0.01),
                    background_landmark_right=Landmark(size=200, position=100, texture="BG2", reward_valence=0, center_offset=0.01),
                    background_landmark_ceil=Landmark(size=200, position=100, texture="BG3", reward_valence=0, center_offset=0.01),
                    background_landmark_floor=Landmark(size=200, position=100, texture="BG4", reward_valence=0, center_offset=0.01),
                    far_landmark=Landmark(size=100, position=200, texture="grey",  reward_valence=0, center_offset=0.0),
                    boundary_threshold=-35.9,
                    end_trial_threshold=-35.9,
                    movement_visual_gain=0.0613
                    )

trial_skip2 = Trial(landmarks=[
                        [Landmark(size=8, position=40, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=120, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=160, texture="plaid", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=200, position=100, texture="BG1", reward_valence=0, center_offset=0.01),
                    background_landmark_right=Landmark(size=200, position=100, texture="BG2", reward_valence=0, center_offset=0.01),
                    background_landmark_ceil=Landmark(size=200, position=100, texture="BG3", reward_valence=0, center_offset=0.01),
                    background_landmark_floor=Landmark(size=200, position=100, texture="BG4", reward_valence=0, center_offset=0.01),
                    far_landmark=Landmark(size=12, position=200, texture="grey", reward_valence=0, center_offset=0.01), #TODO: change texture to match luminance(?)
                    boundary_threshold=-35.8,
                    end_trial_threshold=-35.7,
                    movement_visual_gain=0.0613
                    )

trial_skip3 = Trial(landmarks=[
                        [Landmark(size=8, position=40, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=80, texture="plaid", reward_valence=0)],
                        [Landmark(size=8, position=160, texture="plaid", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=200, position=100, texture="BG1", reward_valence=0, center_offset=0.01),
                    background_landmark_right=Landmark(size=200, position=100, texture="BG2", reward_valence=0, center_offset=0.01),
                    background_landmark_ceil=Landmark(size=200, position=100, texture="BG3", reward_valence=0, center_offset=0.01),
                    background_landmark_floor=Landmark(size=200, position=100, texture="BG4", reward_valence=0, center_offset=0.01),
                    far_landmark=Landmark(size=12, position=200, texture="grey", reward_valence=0, center_offset=0.01), #TODO: change texture to match luminance(?)
                    boundary_threshold=-35.8,
                    end_trial_threshold=-35.7,
                    movement_visual_gain=0.0613
                    )

task_logic = UclOpenVrCorridor2pTaskLogic(
    task_parameters=UclOpenVrCorridor2pTaskParameters(
        corridor_width=12,
        eye_height_offset=-2,
        far_clip=200,
        blocks = [
            Block(
                randomise_trial_order=False,
                available_trials=
                [
                    trial_base,
                   # trial_skip2,
                   # trial_base,
                   # trial_swap23,
                   # trial_base,
                   # trial_skip3,
                   # trial_base
                ],
            ),
        ]
    ),
)

def main(path_seed: str = "./local/{schema}.json"):
    example_task_logic = task_logic
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [example_task_logic]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()