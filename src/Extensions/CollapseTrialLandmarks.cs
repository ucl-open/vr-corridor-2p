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
public class CollapseTrialLandmarks
{
    Random random = new Random();
    public IObservable<List<PositionedLandmark>> Process(IObservable<Trial> source)
    {
        return source.Select(value => {
            // var landmarkSet = value.Landmarks.OrderBy(x => random.Next()).ToList();

            var chosenLandmarks = value.Landmarks.Select(x =>
            {
                return x[random.Next(x.Count)];
            }).ToList();

            // Position landmarks
            var positionedLandmarks = new List<PositionedLandmark>();
            double currentPosition = 0;
            double lastSize = 0;

            foreach (var landmark in chosenLandmarks)
            {
                positionedLandmarks.Add(new PositionedLandmark { Position = currentPosition, Landmark = landmark });

                currentPosition += landmark.Size;

                lastSize = landmark.Size;
            }

            return positionedLandmarks;
        });
    }
}
