using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;
using UclOpenHfVisualDataSchema;

public static class LandmarkUtils {
    public static double[] LandmarkToPositionRange(Landmark landmark)
    {
        return new double[] { landmark.Position - (landmark.Size / 2), landmark.Position + (landmark.Size / 2) };
    }
}