# Week 5: Sensors, Noise, and Uncertainty

- name: Mahbub Ali
- email: mahbub.ali86@login.cuny.edu
- course_id: CSCI 39536

## concepts.observation

Increasing the noise made the readings jump around more, so they were less consistent. You can see that in the spread of the graph and in the standard deviation of about 0.39 m.

Increasing the bias shifted the readings away from the true value instead. The true distance was 2.0 m, but the mean was about 1.92 m, so the readings were consistently a little low. Noise makes the readings more scattered, while bias makes them consistently off in one direction.

## final.course_reflection

This activity made me think more about how meticulous and results based robotics work can be. I liked that the lab felt methodical and almost research based because we had to make predictions, test different configurations, compare numerical results, and then justify our choices using evidence instead of just guessing. It also made me think more about safety and the human side of robotics. A technical result can look good on paper, but it still matters how the robot’s decisions affect real people. The assistive robot section especially showed why things like false safe decisions, unnecessary stops, and response delays have consequences beyond just the numbers.

One thing that stood out to me was that the whole lab ran through Streamlit instead of the usual ROS and Gazebo setup. That made it much easier for my computer to run and let me focus more on the actual experiment and analysis instead of dealing with software setup issues.

I did not find this lab quite as fun as last week’s lab, but I still liked the structured, research style approach. I was also glad that I did not run into the same kinds of errors or submission problems that made last week more frustrating.

## final.synthesis

In Mission 1, I saw that sensor errors can come from different sources and need different responses. My assigned sensor had a mean of about 1.986 m for a true distance of 2.00 m, a small bias of about -0.014 m, variance of about 0.0043 m², 6 dropouts, and 1 outlier. The readings were also strongly quantized, so taking more samples would not remove the sensor’s main limitation. 

In Mission 2, filtering and fusion showed the tradeoff between accuracy and responsiveness. My best recorded configuration used a median filter with window 3 and equal sensor weighting of 0.50. It had the lowest RMSE, 0.1270 m, with a response delay of 0.90 s. Giving Sensor A more weight reduced delay to 0.45 s, but increased RMSE to 0.1335 m. This showed that a faster response is not always the most accurate one.

Mission 3 showed that deployment context changes what “good” performance means. The warehouse baseline had a false safe rate of 0.0062 and unnecessary stop rate of 0.0561, while the assistive baseline had 0 false safe rate and 0.0135 unnecessary stop rate. Near people, avoiding unsafe movement matters more, while unnecessary stops can still reduce access and trust.

## mission_1.bias

-0.0141

## mission_1.bias_vs_variance

My prediction mostly matched the results. The bias was only about -0.014 m, so the sensor was not consistently shifted very far from the true 2.00 m value. The variance was about 0.0043 m², which shows how spread out the readings were. Bias and variance describe different problems because bias is about being consistently off from the truth, while variance is about how much the readings change from sample to sample.

## mission_1.dropouts

6

## mission_1.mean

1.9859

## mission_1.median

2.0

## mission_1.more_samples

No, more samples would not remove the main problem because the sensor is quantized. Most readings were stuck at exact values like 2.0 m and 1.9 m instead of changing smoothly. There were also 6 dropouts and 1 outlier. More samples could make the average more stable, but they would not fix the limited measurement resolution.

## mission_1.outliers

1

## mission_1.prediction

A biased sensor would have readings that stay consistently above or below 2.00 m, so the mean would be shifted away from the true value. A noisy sensor would have readings more spread out around 2.00 m, with a larger standard deviation or variance.

## mission_1.prediction_draft

A biased sensor would have readings that stay consistently above or below 2.00 m, so the mean would be shifted away from the true value. A noisy sensor would have readings more spread out around 2.00 m, with a larger standard deviation or variance.

## mission_1.profile

quantized

## mission_1.robot_consequence

A robot could use this sensor to decide whether to slow down or stop near an obstacle. Since the readings are quantized, the measured distance could jump between fixed values and cross a decision threshold suddenly. That could make the robot slow down or stop earlier or later than it should, which could inconvenience someone nearby or create a safety risk.

## mission_1.variance

0.00431

## mission_2.comparison

For the moving average, window 3 had an RMSE of 0.1395 and a 1.10 s delay, window 7 had an RMSE of 0.1504 and a 1.10 s delay, and window 11 had an RMSE of 0.1601 with the same 1.10 s delay. The larger windows did not improve RMSE in this test. With the same window 3 and weight 0.25, the median filter had a slightly lower RMSE of 0.1389 compared with 0.1395 for the moving average, while both had a 1.10 s delay.

## mission_2.fusion_choice

With the median filter and window 3, weight 0.25 gave an RMSE of 0.1389 and delay of 1.10 s, weight 0.50 gave the lowest RMSE of 0.1270 and a 0.90 s delay, and weight 0.75 gave an RMSE of 0.1335 with the fastest delay of 0.45 s. I chose weight 0.50 because it gave the best overall accuracy while still responding faster. Sensor A is fast but noisy and outlier prone, while Sensor B is steadier but biased and slower, so an even weight balances their weaknesses better than relying too much on either one.

## mission_2.manual_average

4.1667

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

I think giving Sensor A a weight of 0.75 will make the estimate follow Sensor A more closely and respond faster, but the error may increase because more of Sensor A’s noise and outliers will affect the final estimate.

## mission_2.responsiveness

Smoothing can make the estimate more stable, but it can also make the robot slower to react to a real change. My moving average tests all had a response delay of 1.10 s, while the selected median setup with weight 0.50 had a shorter delay of 0.90 s. For a nearby person, even a small delay could matter because the robot might keep moving toward them for longer before recognizing that it needs to slow down or stop.

## mission_2.selected

5

## mission_3.Assistive.prediction_draft

I think lowering the caution margin from 0.20 m to 0.15 m may reduce unnecessary stops, especially when the obstacle is moving away. I expect the false safe rate to stay low, while the detection delay should stay close to the baseline because the filter and confirmation count are unchanged.

## mission_3.Warehouse.prediction_draft

I think lowering the caution margin from 0.10 m to 0.05 m will reduce unnecessary stops because the robot will be a little less conservative. I expect the false safe rate may increase slightly, but the response delay should stay about the same since the confirmation count and filter are unchanged.

## mission_3.context_comparison

The final warehouse policy uses a 0.75 m stopping threshold and 0.10 m caution margin, while the assistive policy uses a larger 0.95 m threshold and 0.20 m margin. The assistive policy is more cautious because mistakes around people could cause injury. It produced a false safe rate of 0 and only 0.0135 unnecessary stops, compared with 0.0062 false safe and 0.0561 unnecessary stops for the warehouse policy. Both policies use a median filter with window 3, one confirmation, and Stop when both readings are missing. The larger safety distances in the assistive setting make sense because the consequence of unsafe movement is more serious for a person than a small delay in warehouse work.

## mission_3.error_costs

In the warehouse setting, false safe errors could affect workers and equipment because the robot might keep moving when it should stop, while unnecessary stops mainly slow down work and productivity. The baseline had a false safe rate of 0.0062, an unnecessary stop rate of 0.0561, and a maximum detection delay of 0.10 s. Lowering the margin to 0.05 did not change either error rate and increased the delay to 0.15 s, so I would keep the baseline. For the assistive robot, false safe errors could directly put the person using the robot at risk, while unnecessary stops could reduce mobility, access, and trust. Both the baseline and revised policy had a false safe rate of 0, an unnecessary stop rate of 0.0135, a maximum delay of 0.05 s, and 0 dangerous-command events, so the revision did not improve the results.

## mission_3.limitations

These seven scenarios demonstrate that the policies can handle the specific situations tested, including a fast approach, conflicting sensors, dropouts, and safe or unsafe distances. They do not prove that the robot will be safe in every real world situation because actual environments can have different people, obstacles, sensor failures, lighting, and movement patterns. For the assistive robot, I would immediately consult the people who will actually use the robot, especially users with different mobility needs. Before deployment, I would also test the policy in a longer real world trial with people approaching from different directions and speeds while introducing random sensor dropouts and noise.
