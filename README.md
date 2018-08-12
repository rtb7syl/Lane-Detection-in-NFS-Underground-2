# Detecting Lanes in NFS UNderground 2

In this project we detect lanes in one of the popular racing games, __NFS Underground 2__. We used image various precessing techniques to detect lanes frame by frame from the image stream captured from the game. All the processing is done in real time, i.e. the lanes are detected simultaneously as the game is played.

## Processing

We process the captured frames from the game in real time, i.e. the lanes are detected and shown in a separate window at the same time as the game is played. We were able to process about 12 to 13 frames per second with a 5th Gen i3 processor and 8Gb RAM. The average time taken for processing each frame was around 0.08 sec. OpenCV was used used for all image processing tasks.

<p align="center">
  <img src="./images/image_5.png" alt="images/image_5.png" width="600" height="400">
</p>

## Results
Some results are shown below :

<p align="center">
  <img src="./images/image_9.png" alt="images/image_9.png" width="410" height="300">
  <img src="./images/image_7.png" alt="images/image_7.png" width="410" height="300">
</p>

<p align="center">
  <img src="./images/image_8.png" alt="images/image_8.png" width="410" height="300">
  <img src="./images/image_6.png" alt="images/image_6.png" width="410" height="300">
</p>

<p align="center">
  <img src="./images/image_2.png" alt="images/image_2.png" width="410" height="300">
  <img src="./images/image_3.png" alt="images/image_3.png" width="410" height="300">
</p>

<p align="center">
  <img src="./images/image_4.png" alt="images/image_4.png" width="410" height="300">
  <img src="./images/image_1.png" alt="images/image_1.png" width="410" height="300">
</p>
