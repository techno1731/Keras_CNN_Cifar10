# import the necessary packages
from keras.models import load_model as lm
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np

# initialize our application the Keras model
model = None
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def load_model():
    # load the pre-trained model for example in h5 format from keras
    global model
    model = lm('cifar10_chingon.h5')
    return model

def prepare_image(image, target):
	# if the image mode is not RGB, convert it
	if image.mode != "RGB":
		image = image.convert("RGB")

	# resize the input image and preprocess it
	image = image.resize(target)
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = imagenet_utils.preprocess_input(image)

	# return the processed image
	return image

def format_predictions(preds, classes):
    return sorted(dict(zip(classes, *preds.tolist())).items(), key=lambda t: t[1], reverse=True)

def modelo_chingon_predict(img):
    # Load the model
    model = load_model()
    # initialize the data dictionary that will be returned from the view
    prediction = {"success": False}
    # preprocess the image and prepare it for classification
    image = prepare_image(img, target=(32, 32))		
    # classify the input image and then initialize the list
    # of predictions to return to the client
    preds = model.predict(image)
    results = format_predictions(preds, classes)
    prediction["predictions"] = []
    # loop over the results and add them to the list of
    # returned predictions
    for (label, prob) in results:
        r = {"label": label, "probability": float(prob)}
        prediction["predictions"].append(r)
        # indicate that the request was a success
        prediction["success"] = True
    return  prediction

def print_prediction(predictions):
    for (i, result) in enumerate(r["predictions"]):
        print("{}. {}: {:.4f}".format(i + 1, result["label"],
                                      result["probability"]))

