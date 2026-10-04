# Mission 2

## comparison

For the moving average, window 3 had an RMSE of 0.1395 and a 1.10 s delay, window 7 had an RMSE of 0.1504 and a 1.10 s delay, and window 11 had an RMSE of 0.1601 with the same 1.10 s delay. The larger windows did not improve RMSE in this test. With the same window 3 and weight 0.25, the median filter had a slightly lower RMSE of 0.1389 compared with 0.1395 for the moving average, while both had a 1.10 s delay.

## fusion_choice

With the median filter and window 3, weight 0.25 gave an RMSE of 0.1389 and delay of 1.10 s, weight 0.50 gave the lowest RMSE of 0.1270 and a 0.90 s delay, and weight 0.75 gave an RMSE of 0.1335 with the fastest delay of 0.45 s. I chose weight 0.50 because it gave the best overall accuracy while still responding faster. Sensor A is fast but noisy and outlier prone, while Sensor B is steadier but biased and slower, so an even weight balances their weaknesses better than relying too much on either one.

## manual_average

4.1667

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

I think giving Sensor A a weight of 0.75 will make the estimate follow Sensor A more closely and respond faster, but the error may increase because more of Sensor A’s noise and outliers will affect the final estimate.

## responsiveness

Smoothing can make the estimate more stable, but it can also make the robot slower to react to a real change. My moving average tests all had a response delay of 1.10 s, while the selected median setup with weight 0.50 had a shorter delay of 0.90 s. For a nearby person, even a small delay could matter because the robot might keep moving toward them for longer before recognizing that it needs to slow down or stop.

## selected

5
