# Safe-Distance-Monitoring-APP
A web app for monitoring safe distance on [Stanford Drone Dataset](https://cvgl.stanford.edu/projects/uav_data/). Trained on Darknet YOLOv4 for performing small object detection and then performed Tracking by detection on two classes Pedestrians and Bikers using DeepSORT. A violation index is then set(in #pixels i.e. 45 pixels) after several trials and measured the number of total violations in a Stanford drone video. Please checkout my [object-detection-on-aerial-videos](https://github.com/soumyadbanik/object-detection-on-aerial-videos) repo for performing multiobject detection on this dataset. Here a larger dataset is used than before. To get an overview of how it works, please go through my [ppt slides](https://docs.google.com/presentation/d/1IGtcHEopTI3RaLDRwxQGYA-XjanRLYoY4K2u6hszFt8/edit?usp=sharing)(in presentation mode). To get a generalized yolov4-DeepSORT implementation checkout [theAIGuysCode-yolov4-deepsort](https://github.com/theAIGuysCode/yolov4-deepsort) repo. I've done several modifications for my own purpose in this project. Deployed using Flask API.
I'll try give a tutorial on how DeepSORT worked here.

## Demo of monitoring social distancing
|<img src="https://github.com/soumyadbanik/Safe-Distance-Monitoring-APP/blob/main/static/outputs/hyang_social_short.gif" width="60%" height="60%" >|
  |---|

# To-DOs
- [X] Train on Darknet yolov4 with larger dataset.
- [X] Apply DeepSORT for multi object tracking.
- [X] Deploy using Flask API.
- [ ] Comparative study with other state-of-the-art object detectors.
- [ ] To make compatible for edge devices like IOT and mobile devices (Need to train with yolo-v4 tiny model).
- [ ] Increase fps (to make realtime).
- [ ] Host on cloud.
