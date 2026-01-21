import os

from ucl_open_vr_corridor_2p.rig import (
    UclOpenVrCorridor2pRig,
    SyncQuad,
    MatrixArduino
)

from ucl_open.rigs.device import (
    Screen,
)

from ucl_open.rigs.data_types import (
    Vector3
)

from ucl_open.rigs.displays import (
    DisplayCalibration,
    DisplayIntrinsics,
    DisplayExtrinsics
)

rig = UclOpenVrCorridor2pRig(
    gamma_correction_file="C:/Users/saleem_lab/Desktop/Sonali-2PStim/HALFINTENSITY_LUT_NoRed_SALEEM20_20250219.bmp",
    screen=Screen(
        texture_assets_directory="../textures",
        calibration={
            "debug": DisplayCalibration(
                intrinsics=DisplayIntrinsics(
                    frame_width=640,
                    frame_height=480,
                    display_width=0.54,
                    display_height=0.3
                ),
                extrinsics=DisplayExtrinsics(
                    rotation=Vector3(x=0, y=0, z=0),
                    translation=Vector3(x=0, y=0, z=0.3)
                )
            ),
            "left": DisplayCalibration(
                intrinsics=DisplayIntrinsics(
                    frame_width=640,
                    frame_height=480,
                    display_width=15,
                    display_height=19.5
                ),
                extrinsics=DisplayExtrinsics(
                    rotation=Vector3(x=0, y=-1.0472, z=0),
                    translation=Vector3(x=-12, y=0, z=9)
                )
            ),
            "center": DisplayCalibration(
                    intrinsics=DisplayIntrinsics(
                    frame_width=640,
                    frame_height=480,
                    display_width=15,
                    display_height=19.5
                ),
                extrinsics=DisplayExtrinsics(
                    rotation=Vector3(x=0, y=0, z=0),
                    translation=Vector3(x=0, y=0, z=15)
                )
            ),
            "right": DisplayCalibration(
                    intrinsics=DisplayIntrinsics(
                    frame_width=640,
                    frame_height=480,
                    display_width=15,
                    display_height=19.5
                ),
                extrinsics=DisplayExtrinsics(
                    rotation=Vector3(x=0, y=1.0472, z=0),
                    translation=Vector3(x=12, y=0, z=9)
                )
            ),
        }
    ),
    sync_quad=SyncQuad(
        extent_x=0.5,
        extent_y=0.5,
        location_x=1,
        location_y=-1
    ),
    arduino=MatrixArduino(
        port_name="COM3",
        baud_rate=1000000,
        new_line="\n"
    ),
    quad_time_lower_bound=0.2,
    quad_time_upper_bound=0.5
)

def main(path_seed: str = "./local/{schema}.json"):
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [rig]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()