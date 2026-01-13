import datetime
import os

from ucl_open_vr_corridor_2p.session import UclOpenSession

# TODO - autofill experiment fields
session = UclOpenSession(
    workflow="main.bonsai",
    commit="",
    repository_url="https://github.com/ucl-open/vr-corridor-2p",
    logging_root_path="C:/Users/neurogears/source/repos/ucl-open/vr-corridor-2p/temp_data",
    animal_id="Plimbo",
    session_id="001"
)

def main(path_seed: str = "./local/{schema}.json"):
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [session]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()