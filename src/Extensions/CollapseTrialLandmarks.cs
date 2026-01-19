using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;
using UclOpenHfVisualDataSchema;
using System.Drawing;

[Combinator]
[Description("")]
[WorkflowElementCategory(ElementCategory.Transform)]
public class CollapseTrialLandmarks
{
    Random random = new Random();
    public IObservable<List<Landmark>> Process(IObservable<Trial> source)
    {
        return source.Select(value => {
            // var landmarkSet = value.Landmarks.OrderBy(x => random.Next()).ToList();

            var chosenLandmarks = value.Landmarks.Select(x =>
            {
                return x[random.Next(x.Count)];
            }).ToList();

            return chosenLandmarks;
        });
    }
}
