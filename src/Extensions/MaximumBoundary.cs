using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;
using UclOpenHfVisualDataSchema;

[Combinator]
[Description("")]
[WorkflowElementCategory(ElementCategory.Transform)]
public class MaximumBoundary
{
    public IObservable<double> Process(IObservable<List<PositionedLandmark>> source)
    {
        return source.Select(value =>
        {
            return value.Max(x => LandmarkUtils.LandmarkToPositionRange(x)[1]);
        });
    }
}
