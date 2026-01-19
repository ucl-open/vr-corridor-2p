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
public class LandmarkIsEmpty
{
    public IObservable<bool> Process(IObservable<Landmark> source)
    {
        return source.Select(value => { return value == null; });
    }
}