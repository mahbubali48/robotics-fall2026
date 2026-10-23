# mission_2

## choice
I recommend the classical detector for further testing using HSV thresholds of H 0–35, S 70–255, V 25–150, a morphology kernel of 3, minimum area of 300 pixels, and minimum circularity of 0.00. At the learned detector's 0.50 acceptance threshold, the classical method located more mugs in the normal and occluded conditions. Its batch processing time averaged approximately 3.57 ms per image, although processing time alone does not establish robot response speed or safety.

For the normal_1 foreground segmentation example, the mask IoU was 0.5756 and Dice was 0.7306. The predicted foreground included some unwanted regions and missed some mug pixels. A detailed foreground mask does not identify the requested mug because the model does not assign object labels. One limitation of this small test is that its 31 images cannot establish reliable performance across different real-world environments, viewpoints, lighting conditions, or mug appearances.

## comparison
I compared the classical and learned detectors on normal, dim, and occluded images. Under normal conditions, the classical detector produced 2 correct boxes, 0 false boxes, and 0 missed mugs, while the learned detector produced 1 correct box, 0 false boxes, and 1 missed mug. Under dim lighting, the classical detector had 0 correct boxes, 2 false boxes, and 2 missed mugs. The learned detector had 0 correct boxes, 0 false boxes, and 2 missed mugs. For occluded images, the classical detector produced 1 correct box, 1 false box, and 1 missed mug, while the learned detector produced 0 correct boxes, 0 false boxes, and 2 missed mugs.

The classical detector located more mugs under these conditions, although it sometimes produced incorrect boxes. For normal_1, the classical detector selected a box covering the mug and some surrounding desk, while the learned detector did not produce an accepted box at the 0.50 threshold. This shows that detecting an object and locating it correctly are different tasks.
