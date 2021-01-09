# import the necessary packages
from keras.models import load_model as lm
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np


# initialize our application the Keras model
model = None
classes = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


def load_model():
    # load the pre-trained model for example in h5 format from keras
    global model
    model = lm("cifar10_chingon.h5")
    return model


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")
    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image) / 255
    image = np.expand_dims(image, axis=0)
    # return the processed image
    return image


def format_predictions(preds, classes):
    return sorted(
        dict(zip(classes, *preds.tolist())).items(), key=lambda t: t[1], reverse=True
    )


def modelo_chingon_predict(img):
    # Load the model
    model = load_model()
    # preprocess the image and prepare it for classification
    image = prepare_image(img, target=(32, 32))
    # classify the input image and then initialize the list
    # of predictions to return to the client
    preds = model.predict(image)
    results = format_predictions(preds, classes)
    return results


def print_prediction(predictions):
    for (i, item) in enumerate(predictions):
        print("{}. {}: {:.4f}".format(i + 1, item[0], item[1]))
