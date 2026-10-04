# Mission 1

## bias

-0.0141

## bias_vs_variance

My prediction mostly matched the results. The bias was only about -0.014 m, so the sensor was not consistently shifted very far from the true 2.00 m value. The variance was about 0.0043 m², which shows how spread out the readings were. Bias and variance describe different problems because bias is about being consistently off from the truth, while variance is about how much the readings change from sample to sample.

## dropouts

6

## mean

1.9859

## median

2.0

## more_samples

No, more samples would not remove the main problem because the sensor is quantized. Most readings were stuck at exact values like 2.0 m and 1.9 m instead of changing smoothly. There were also 6 dropouts and 1 outlier. More samples could make the average more stable, but they would not fix the limited measurement resolution.

## outliers

1

## prediction

A biased sensor would have readings that stay consistently above or below 2.00 m, so the mean would be shifted away from the true value. A noisy sensor would have readings more spread out around 2.00 m, with a larger standard deviation or variance.

## prediction_draft

A biased sensor would have readings that stay consistently above or below 2.00 m, so the mean would be shifted away from the true value. A noisy sensor would have readings more spread out around 2.00 m, with a larger standard deviation or variance.

## profile

quantized

## robot_consequence

A robot could use this sensor to decide whether to slow down or stop near an obstacle. Since the readings are quantized, the measured distance could jump between fixed values and cross a decision threshold suddenly. That could make the robot slow down or stop earlier or later than it should, which could inconvenience someone nearby or create a safety risk.

## variance

0.00431
