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


@app.route("/")
def hello():
    return "Hello World"
