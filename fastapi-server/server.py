from fastapi import FastAPI, File, UploadFile
from model_helper import predict

# Create a FastAPI app instance
app = FastAPI()

# Define a POST endpoint for predictions
@app.post('/predict')

# Prediction function
async def get_prediction(file: UploadFile = File(...)):

    try:
        # Read uploaded file into bytes
        image_bytes = await file.read()

        # Save bytes as a temporary image file
        image_path = 'temp_file.jpg'
        with open(image_path, 'wb') as f:
            f.write(image_bytes)

            # Make prediction using the saved image
            prediction = predict(image_path)

        # Return prediction as JSON
        return {'prediction': prediction}

    except Exception as e:
        # return error message in case of error
        return {'error': str(e)}