import os

from ucl_open_vr_corridor_2p.task import (
    UclOpenVrCorridor2pTaskLogic,
    UclOpenVrCorridor2pTaskParameters,
    Block,
    Trial,
    Landmark
)

task_logic = UclOpenVrCorridor2pTaskLogic(
    task_parameters=UclOpenVrCorridor2pTaskParameters(
        corridor_width=2,
        blocks = [
            Block(available_trials=[
                Trial(landmarks=[
                    [Landmark(size=2, texture="grating", reward_valence=0)],
                    [Landmark(size=2, texture="dots", reward_valence=0)],
                    [Landmark(size=2, texture="leaves", reward_valence=0)],
                    [Landmark(size=2, texture="grey", reward_valence=0)]
                ]),
                Trial(landmarks=[
                    [Landmark(size=2, texture="grass", reward_valence=0)],
                    [Landmark(size=2, texture="tiles", reward_valence=0)],
                    [Landmark(size=2, texture="bark", reward_valence=0)],
                    [Landmark(size=2, texture="grey", reward_valence=0)]
                ]),
            ])
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