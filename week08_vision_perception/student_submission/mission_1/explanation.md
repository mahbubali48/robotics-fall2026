# mission_1

## diagnosis
I compared normal_1 and dim_1 using the saved detector settings. In normal_1, the detector selected a box containing the mug, although it also included part of the wooden desk and shadow. The mask showed that the mug and nearby desk had similar HSV values. Contour 4 was selected because it had the largest eligible area (15,292 pixels).

For the dim condition, both cup present images produced detections, but neither bounding box matched the annotated mug at IoU ≥ 0.50. The reduced lighting changed which pixels passed the fixed HSV thresholds, causing inaccurate localization. The value range of 25–150 could not reliably separate the mug from its surroundings under different lighting conditions.

## limitations
During practice, I changed the maximum HSV value from 180 to 150 while keeping the other settings the same. This excluded some brighter pixels from the mask and reduced the selected contour area from 17,577 to 15,292 pixels. The resulting bounding box was tighter around the mug, although it still included some of the wooden desk and shadow.

A limitation of this detector is that it relies on fixed color thresholds rather than recognizing objects. A mug with a different color or a background with similar HSV values could cause it to miss the mug or select the wrong region.
