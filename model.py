import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model



def getPrediction(filename):
    
    classes = ["Tomato_Early_blight", "Tomato_Late_blight", "Tomato_healthy", "Tomato_Tomato_YellowLeaf_Curl_Virus", "Tomato_Bacterial_spot", "Tomato_Septoria_leaf_spot"]
    le = LabelEncoder()
    le.fit(classes)
    le.inverse_transform([2])
    
    
    #Load model
    my_model=load_model("model.h5")
    
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
    
    