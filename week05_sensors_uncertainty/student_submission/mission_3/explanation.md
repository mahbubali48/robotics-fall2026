# Mission 3

## Assistive.prediction_draft

I think lowering the caution margin from 0.20 m to 0.15 m may reduce unnecessary stops, especially when the obstacle is moving away. I expect the false safe rate to stay low, while the detection delay should stay close to the baseline because the filter and confirmation count are unchanged.

## Warehouse.prediction_draft

I think lowering the caution margin from 0.10 m to 0.05 m will reduce unnecessary stops because the robot will be a little less conservative. I expect the false safe rate may increase slightly, but the response delay should stay about the same since the confirmation count and filter are unchanged.

## context_comparison

The final warehouse policy uses a 0.75 m stopping threshold and 0.10 m caution margin, while the assistive policy uses a larger 0.95 m threshold and 0.20 m margin. The assistive policy is more cautious because mistakes around people could cause injury. It produced a false safe rate of 0 and only 0.0135 unnecessary stops, compared with 0.0062 false safe and 0.0561 unnecessary stops for the warehouse policy. Both policies use a median filter with window 3, one confirmation, and Stop when both readings are missing. The larger safety distances in the assistive setting make sense because the consequence of unsafe movement is more serious for a person than a small delay in warehouse work.

## error_costs

In the warehouse setting, false safe errors could affect workers and equipment because the robot might keep moving when it should stop, while unnecessary stops mainly slow down work and productivity. The baseline had a false safe rate of 0.0062, an unnecessary stop rate of 0.0561, and a maximum detection delay of 0.10 s. Lowering the margin to 0.05 did not change either error rate and increased the delay to 0.15 s, so I would keep the baseline. For the assistive robot, false safe errors could directly put the person using the robot at risk, while unnecessary stops could reduce mobility, access, and trust. Both the baseline and revised policy had a false safe rate of 0, an unnecessary stop rate of 0.0135, a maximum delay of 0.05 s, and 0 dangerous-command events, so the revision did not improve the results.

## limitations

These seven scenarios demonstrate that the policies can handle the specific situations tested, including a fast approach, conflicting sensors, dropouts, and safe or unsafe distances. They do not prove that the robot will be safe in every real world situation because actual environments can have different people, obstacles, sensor failures, lighting, and movement patterns. For the assistive robot, I would immediately consult the people who will actually use the robot, especially users with different mobility needs. Before deployment, I would also test the policy in a longer real world trial with people approaching from different directions and speeds while introducing random sensor dropouts and noise.
