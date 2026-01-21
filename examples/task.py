import os

from ucl_open_vr_corridor_2p.task import (
    UclOpenVrCorridor2pTaskLogic,
    UclOpenVrCorridor2pTaskParameters,
    Block,
    Trial,
    Landmark
)

trial_base = Trial(landmarks=[
                        [Landmark(size=4, position=50, texture="plaid_50perC", reward_valence=0)],
                        [Landmark(size=4, position=70, texture="vertGrat_50perC", reward_valence=0)],
                        [Landmark(size=4, position=90, texture="plaid_50perC", reward_valence=1)],
                        [Landmark(size=4, position=110, texture="vertGrat_50perC", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=140, position=70, texture="smoothed_fwn1_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_right=Landmark(size=140, position=70, texture="smoothed_fwn2_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_ceil=Landmark(size=140, position=70, texture="smoothed_fwn3_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_floor=Landmark(size=140, position=70, texture="smoothed_fwn4_25perC", reward_valence=0, center_offset=0.0001)
                    )

trial_skip2 = Trial(landmarks=[
                        [Landmark(size=4, position=50, texture="plaid_50perC", reward_valence=0)],
                        [Landmark(size=4, position=90, texture="plaid_50perC", reward_valence=1)],
                        [Landmark(size=4, position=110, texture="vertGrat_50perC", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=140, position=70, texture="smoothed_fwn1_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_right=Landmark(size=140, position=70, texture="smoothed_fwn2_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_ceil=Landmark(size=140, position=70, texture="smoothed_fwn3_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_floor=Landmark(size=140, position=70, texture="smoothed_fwn4_25perC", reward_valence=0, center_offset=0.0001)
                    )

trial_skip3 = Trial(landmarks=[
                        [Landmark(size=4, position=50, texture="plaid_50perC", reward_valence=0)],
                        [Landmark(size=4, position=70, texture="vertGrat_50perC", reward_valence=0)],
                        [Landmark(size=4, position=110, texture="vertGrat_50perC", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=140, position=70, texture="smoothed_fwn1_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_right=Landmark(size=140, position=70, texture="smoothed_fwn2_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_ceil=Landmark(size=140, position=70, texture="smoothed_fwn3_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_floor=Landmark(size=140, position=70, texture="smoothed_fwn4_25perC", reward_valence=0, center_offset=0.0001)
                    )

trial_swap23 = Trial(landmarks=[
                        [Landmark(size=4, position=50, texture="plaid_50perC", reward_valence=0)],
                        [Landmark(size=4, position=70, texture="plaid_50perC", reward_valence=0)],
                        [Landmark(size=4, position=90, texture="vertGrat_50perC", reward_valence=1)],
                        [Landmark(size=4, position=110, texture="vertGrat_50perC", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=140, position=70, texture="smoothed_fwn1_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_right=Landmark(size=140, position=70, texture="smoothed_fwn2_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_ceil=Landmark(size=140, position=70, texture="smoothed_fwn3_25perC", reward_valence=0, center_offset=0.0001),
                    background_landmark_floor=Landmark(size=140, position=70, texture="smoothed_fwn4_25perC", reward_valence=0, center_offset=0.0001)
                    )

task_logic = UclOpenVrCorridor2pTaskLogic(
    task_parameters=UclOpenVrCorridor2pTaskParameters(
        corridor_width=8,
        blocks = [
            Block(
                randomise_trial_order=False,
                available_trials=
                [
                    trial_base,
                    trial_skip2,
                    trial_base,
                    trial_swap23,
                    trial_base,
                    trial_skip3,
                    trial_base
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