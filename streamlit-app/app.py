import streamlit as st
from model_helper import predict

# Set the title of the Streamlit app
st.title('Vehicle Damage Detection')

# Create a file uploader widget that accepts JPG and PNG files
uploaded_file  = st.file_uploader('Upload the file', type=['jpg', 'png'])

# If a file is uploaded by the user
if uploaded_file:
    image_path = 'temp_file.jpg'

    # Save the uploaded image to the temporary path
    with open(image_path, 'wb') as f:

        f.write(uploaded_file.getbuffer())

        # Display the uploaded image in the app
        st.image(uploaded_file, caption='Uploaded File', use_container_width=True)

        # Run the prediction function on the saved image
        prediction = predict(image_path)

        # Display the prediction result in an info box
        st.info(f'Predicted Class: {prediction}')