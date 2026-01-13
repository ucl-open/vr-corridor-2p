import os

from ucl_open_vr_corridor_2p.task import (
    UclOpenVrCorridor2pTaskLogic,
    UclOpenVrCorridor2pTaskParameters,
    Trial,
    Block
)

task_logic = UclOpenVrCorridor2pTaskLogic(
    task_parameters=UclOpenVrCorridor2pTaskParameters(
        blocks = [
            Block(available_trials=[
                
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
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()