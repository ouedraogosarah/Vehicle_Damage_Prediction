# Vehicle Damage Detection App

An easy-to-use web app that lets you upload a car image and predicts the type of damage on the vehicle. The model is specifically trained on front and rear three-quarter views of cars, so please upload images from these perspectives for best accuracy.

![[app](app_screenshot.jpg)

## Model Details

- **Architecture:** ResNet50 (Transfer Learning)  
- **Dataset:** ~1,700 images  
- **Classes:**  
  - Front Normal  
  - Front Crushed  
  - Front Breakage  
  - Rear Normal  
  - Rear Crushed  
  - Rear Breakage  
- **Validation Accuracy:** ~80%

## Setup Instructions

1. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
2. Run the streamlit app:
   ```commandline
   streamlit run app.py
