# Final synthesis

In Mission 1, I saw that sensor errors can come from different sources and need different responses. My assigned sensor had a mean of about 1.986 m for a true distance of 2.00 m, a small bias of about -0.014 m, variance of about 0.0043 m², 6 dropouts, and 1 outlier. The readings were also strongly quantized, so taking more samples would not remove the sensor’s main limitation. 

In Mission 2, filtering and fusion showed the tradeoff between accuracy and responsiveness. My best recorded configuration used a median filter with window 3 and equal sensor weighting of 0.50. It had the lowest RMSE, 0.1270 m, with a response delay of 0.90 s. Giving Sensor A more weight reduced delay to 0.45 s, but increased RMSE to 0.1335 m. This showed that a faster response is not always the most accurate one.

Mission 3 showed that deployment context changes what “good” performance means. The warehouse baseline had a false safe rate of 0.0062 and unnecessary stop rate of 0.0561, while the assistive baseline had 0 false safe rate and 0.0135 unnecessary stop rate. Near people, avoiding unsafe movement matters more, while unnecessary stops can still reduce access and trust.