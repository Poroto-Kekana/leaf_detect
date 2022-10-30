import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model



def getPrediction(filename):
    
    classes = ["Yellow leaf curl virus", "Septoria leaf spot", "Healthy tomato leaf", "Late blight", "Bacterial spot", "Early blight"]
    le = LabelEncoder()
    le.fit(classes)
    le.inverse_transform([2])
    
    
    #Load model
    my_model=load_model("vgg16Epoch5New")
    
    SIZE = 224 #Resize to same size as training images
    img_path = "./" + filename
    img = np.asarray(Image.open(img_path).resize((SIZE,SIZE)))
    
    img = img/255.      #Scale pixel values
    
    img = np.expand_dims(img, axis=0)  #Get it tready as input to the network       
    
    pred = my_model.predict(img) #Predict                    
    
    #Convert prediction to class name
    pred_class = le.inverse_transform([np.argmax(pred)])[0]
    confidence = round(100 * (np.max(pred[0])), 2)
    print("Diagnosis is:", pred_class, confidence)
    return {"pred_class" : pred_class, "confidence" : confidence}
    
    