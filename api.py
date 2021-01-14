import requests
import json

def main():
    PARAMS = {'data':'https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg'}
    response = requests.post(url='http://localhost:5000/predict?',data=PARAMS)
    print(response.text)

if __name__ == "__main__":
    main()

