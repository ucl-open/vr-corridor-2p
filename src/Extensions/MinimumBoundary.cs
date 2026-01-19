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
public class MinimumBoundary
{
    public IObservable<double> Process(IObservable<List<Landmark>> source)
    {
        return source.Select(value =>
        {
            return value.Min(x => LandmarkUtils.LandmarkToPositionRange(x)[1]);
        });
    }
}