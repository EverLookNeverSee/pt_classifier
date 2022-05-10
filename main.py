import requests

# Sending the request
resp = requests.post("http://localhost:5000/predict",
                     files={"file": open("sample_images/Bentley-Continental-GT.jpg", "rb")})
