using System;
using System.Reactive.Linq;
using Bonsai;
using Bonsai.Harp;
using UclOpenHfVisualDataSchema;

public class ParseMatrixSerialDevice : Transform<string, Timestamped<MatrixArduinoData>>
{
    public override IObservable<Timestamped<MatrixArduinoData>> Process(IObservable<string> source)
    {
        return source.Select(value =>
        {
            var values = value.Split('\t');
            var matrixArduinoData = new MatrixArduinoData
            {
                EncoderPos = Convert.ToInt32(values[0]),
                LastLeftLickTime = Convert.ToInt32(values[1]),
                LastRightLickTime = Convert.ToInt32(values[2]),
                LastSyncPulseTime = Convert.ToInt32(values[3]),
                PhotodiodeValue = Convert.ToSingle(values[4]),
                Last2PFrameTime = Convert.ToInt32(values[5]),
                Last2PLineTime = Convert.ToInt32(values[6]),
                CurrentMillis = Convert.ToInt32(values[7])
            };
            return new Timestamped<MatrixArduinoData>(matrixArduinoData, matrixArduinoData.CurrentMillis / 1000d);
        });
    }
}