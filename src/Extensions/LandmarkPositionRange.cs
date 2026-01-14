using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;
using UclOpenHfVisualDataSchema;

public static class LandmarkUtils {
    public static double[] LandmarkToPositionRange(PositionedLandmark positionedLandmark)
    {
        return new double[] { positionedLandmark.Position - (positionedLandmark.Landmark.Size / 2), positionedLandmark.Position + (positionedLandmark.Landmark.Size / 2) };
    }
}