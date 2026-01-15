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
                currentPosition += (lastSize / 2) + (landmark.Size / 2);
                positionedLandmarks.Add(new PositionedLandmark { Position = currentPosition, Landmark = landmark });

                lastSize = landmark.Size;
            }

            return positionedLandmarks;
        });
    }
}
