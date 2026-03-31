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
public class ShuffleList
{
    public IObservable<List<T>> Process<T>(IObservable<Tuple<List<T>, Random>> source)
    {
        return source.Select(value => value.Item1.OrderBy(x => value.Item2.Next()).ToList());
    }
}
