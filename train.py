import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from ultralytics import YOLO

# loading a pre-trained model
model = YOLO("yolov8n.pt")

model._check_is_pytorch_model()

data_yaml_path = "data.yaml"

model.train(data=data_yaml_path,
            epochs=500,
            imgsz=100,
            device='cpu')


