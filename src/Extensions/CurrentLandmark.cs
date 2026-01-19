using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;
using OpenTK;
using UclOpenHfVisualDataSchema;

[Combinator]
[Description("")]
[WorkflowElementCategory(ElementCategory.Transform)]
public class CurrentLandmark
{
    public IObservable<Landmark> Process(IObservable<Tuple<OpenTK.Vector3, List<Landmark>>> source)
    {
        return source.Select(value =>
        {
            var orderedLandmarks = value.Item2.OrderBy(x => LandmarkUtils.LandmarkToPositionRange(x)[0]).ToList(); // Convert [position, size] to range [min, max] and order by min
            var position = value.Item1.Z;

            return orderedLandmarks.Where(x => (LandmarkUtils.LandmarkToPositionRange(x)[0] <= position) && (LandmarkUtils.LandmarkToPositionRange(x)[1] > position)).FirstOrDefault();
        });
    }
}
