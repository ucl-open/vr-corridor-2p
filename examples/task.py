import os
import random
import copy

from ucl_open_vr_corridor_2p.task import (
    UclOpenVrCorridor2pTaskLogic,
    UclOpenVrCorridor2pTaskParameters,
    Block,
    Trial,
    Landmark
)

fullGain =  0.0613 #1cm on wheel = 1cm in vr 
halfGain = 0.0306 #2cm on wheel = 1cm in vr 
doubleGain = 0.1226 #1cm on wheel = 2cm in vr 

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
                    boundary_threshold=-36,
                    end_trial_threshold=-35.9,#swap to 35.89 during playback
                    movement_visual_gain=halfGain
                    )

# Swaps the 2nd and 3rd landmark: grating grating plaid plaid
trial_swap2_3 = Trial(landmarks=[
                        [Landmark(size=8, position=40, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=80, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=120, texture="plaid", reward_valence=0)],
                        [Landmark(size=8, position=160, texture="plaid", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=200, position=100, texture="BG1", reward_valence=0, center_offset=0.01),
                    background_landmark_right=Landmark(size=200, position=100, texture="BG2", reward_valence=0, center_offset=0.01),
                    background_landmark_ceil=Landmark(size=200, position=100, texture="BG3", reward_valence=0, center_offset=0.01),
                    background_landmark_floor=Landmark(size=200, position=100, texture="BG4", reward_valence=0, center_offset=0.01),
                    far_landmark=Landmark(size=100, position=200, texture="grey",  reward_valence=0, center_offset=0.0),
                    boundary_threshold=-36,
                    end_trial_threshold=-36,
                    movement_visual_gain=halfGain
                    )

# Swaps the 3rd and 4th landmark: grating plaid plaid grating
trial_swap3_4 = Trial(landmarks=[
                        [Landmark(size=8, position=40, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=80, texture="plaid", reward_valence=0)],
                        [Landmark(size=8, position=120, texture="plaid", reward_valence=0)],
                        [Landmark(size=8, position=160, texture="grating_vertical", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=200, position=100, texture="BG1", reward_valence=0, center_offset=0.01),
                    background_landmark_right=Landmark(size=200, position=100, texture="BG2", reward_valence=0, center_offset=0.01),
                    background_landmark_ceil=Landmark(size=200, position=100, texture="BG3", reward_valence=0, center_offset=0.01),
                    background_landmark_floor=Landmark(size=200, position=100, texture="BG4", reward_valence=0, center_offset=0.01),
                    far_landmark=Landmark(size=100, position=200, texture="grey",  reward_valence=0, center_offset=0.0),
                    boundary_threshold=-36,
                    end_trial_threshold=-36,
                    movement_visual_gain=halfGain
                    )

# Omit the 2nd (plaid) landmark 
trial_omit2 = Trial(landmarks=[
                        [Landmark(size=8, position=40, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=120, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=160, texture="plaid", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=200, position=100, texture="BG1", reward_valence=0, center_offset=0.01),
                    background_landmark_right=Landmark(size=200, position=100, texture="BG2", reward_valence=0, center_offset=0.01),
                    background_landmark_ceil=Landmark(size=200, position=100, texture="BG3", reward_valence=0, center_offset=0.01),
                    background_landmark_floor=Landmark(size=200, position=100, texture="BG4", reward_valence=0, center_offset=0.01),
                    far_landmark=Landmark(size=12, position=200, texture="grey", reward_valence=0, center_offset=0.01), 
                    boundary_threshold=-36,
                    end_trial_threshold=-36,
                    movement_visual_gain=halfGain
                    )


# Omit the 3rd (grating) landmark 
trial_omit3 = Trial(landmarks=[
                        [Landmark(size=8, position=40, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=80, texture="plaid", reward_valence=0)],
                        [Landmark(size=8, position=160, texture="plaid", reward_valence=0)]
                    ],
                    background_landmark_left=Landmark(size=200, position=100, texture="BG1", reward_valence=0, center_offset=0.01),
                    background_landmark_right=Landmark(size=200, position=100, texture="BG2", reward_valence=0, center_offset=0.01),
                    background_landmark_ceil=Landmark(size=200, position=100, texture="BG3", reward_valence=0, center_offset=0.01),
                    background_landmark_floor=Landmark(size=200, position=100, texture="BG4", reward_valence=0, center_offset=0.01),
                    far_landmark=Landmark(size=12, position=200, texture="grey", reward_valence=0, center_offset=0.01), 
                    boundary_threshold=-36,
                    end_trial_threshold=-36,
                    movement_visual_gain=halfGain
                    )

# Omit the 4rd (plaid) landmark
trial_omit4 = Trial(landmarks=[
                        [Landmark(size=8, position=40, texture="grating_vertical", reward_valence=0)],
                        [Landmark(size=8, position=80, texture="plaid", reward_valence=0)],
                        [Landmark(size=8, position=120, texture="grating_vertical", reward_valence=0)],
                      
                    ],
                    background_landmark_left=Landmark(size=200, position=100, texture="BG1", reward_valence=0, center_offset=0.01),
                    background_landmark_right=Landmark(size=200, position=100, texture="BG2", reward_valence=0, center_offset=0.01),
                    background_landmark_ceil=Landmark(size=200, position=100, texture="BG3", reward_valence=0, center_offset=0.01),
                    background_landmark_floor=Landmark(size=200, position=100, texture="BG4", reward_valence=0, center_offset=0.01),
                    far_landmark=Landmark(size=100, position=200, texture="grey",  reward_valence=0, center_offset=0.0),
                    boundary_threshold=-76,
                    end_trial_threshold=-76,
                    movement_visual_gain=halfGain
                    )

# 5 unique test/manipulation trials
test_trials = [
    trial_swap2_3, # condition 2
    trial_swap3_4, # condition 3
    trial_omit2,   # condition 4
    trial_omit3,   # condition 5
    trial_omit4    # condition 6
]



full_manipulation_experiment_sequence = []

for i in range(10):
    
    # create a shuffle of the 5 tests trials for this specific block
    current_test_order = copy.deepcopy(test_trials) 
    random.shuffle(current_test_order)  
    # 20-trial sequence (3 baseline + 1 test which is repeated 5 times)
    for test_condition in current_test_order:
        # add 3 baseline trials
        for _ in range(3):
            full_manipulation_experiment_sequence.append(copy.deepcopy(trial_base))
        # add the test trial
        full_manipulation_experiment_sequence.append(test_condition) 
# So now this generates 10 blocks * 20 trials = 200 trials total



################################################################################
three_test_trials = [
    trial_swap2_3, # condition 2
    trial_omit2,   # condition 3
    trial_omit3,   # condition 4
]

three_manipulation_experiment_sequence = []

for i in range(10): #10 blocks 
    
    # create a shuffle of the 3 tests trials for this specific block
    current_three_test_order = copy.deepcopy(three_test_trials) 
    random.shuffle(current_three_test_order)  
    # 12-trial sequence (3 baseline + 1 test which is repeated 3 times)
    for three_test_condition in current_three_test_order:
        # add 3 baseline trials
        for _ in range(3):
            three_manipulation_experiment_sequence.append(copy.deepcopy(trial_base))
        # add the test trial
        three_manipulation_experiment_sequence.append(three_test_condition) 
# So now this generates 10 blocks * 12 trials = 120 trials total

task_logic = UclOpenVrCorridor2pTaskLogic(
    task_parameters=UclOpenVrCorridor2pTaskParameters(
        corridor_width=12,
        eye_height_offset=-2,
        far_clip=200,
        blocks = [
            Block(
                randomise_trial_order=False,
                #available_trials=full_manipulation_experiment_sequence,
                #available_trials=three_manipulation_experiment_sequence,
                available_trials=
                [
                    trial_base,
                ],
            ),
        ],
        rng_seed=1.1  #needed for open-loop (replay)
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