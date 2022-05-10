import io
import json
from PIL import Image
from torchvision import models
from flask import Flask, jsonify, request
import torchvision.transforms as transforms


# Creating app object
app = Flask(__name__)
# Loading classes
imagenet_class_index = json.load(open("imagenet_class_index.json"))
# Importing pretrained mode
model = models.densenet121(pretrained=True)
model.eval()    # setting model on evaluation mode


def transform(image_bytes):
    my_transforms = transforms.Compose([
        transforms.Resize(255),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            [0.485, 0.456, 0.406],
            [0.229, 0.224, 0.225]
        )
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


@app.route("/")
def hello():
    return "Hello World"
