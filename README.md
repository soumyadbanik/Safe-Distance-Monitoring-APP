# Safe-Distance-Monitoring-APP
An web app for monitoring safe distance on [Stanford Drone Dataset](https://cvgl.stanford.edu/projects/uav_data/). Trained on Darknet YOLOv4 for performing small object detection and then tracked only Pedestrians and Bikers using DeepSORT. Here violation index is set(in #pixels) after several trials and measured the number of total violations in a Stanford drone video. Please checkout my [object-detection-on-aerial-videos](https://github.com/soumyadbanik/object-detection-on-aerial-videos) repo for performing multiobject detection on this dataset. Here a larger dataset is used than before. To get an overview of how it works, please see this [slide](https://docs.google.com/presentation/d/1IGtcHEopTI3RaLDRwxQGYA-XjanRLYoY4K2u6hszFt8/edit?usp=sharing)(in presentation mode). 
Deployed using Flask API.

# To-DOs
-[ ] Train on Darknet yolov4 with larger dataset.
-[ X ] Comparative study with other state-of-the-art object detectors.
-[ ] Apply DeepSORT for multi object tracking.
-[ X ] To make compatible for edge devices like IOT and mobile devices (Need to train with yolo-v4 tiny model).
-[ X ] Increase fps (to make realtime).
-[ ] Deploy using Flask API.
-[ X ] Host on cloud.
