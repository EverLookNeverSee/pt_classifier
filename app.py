import io
import json
from PIL import Image
from torchvision import models
from flask import Flask, jsonify, request
import torchvision.transforms as transforms


# Creating app object
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"
