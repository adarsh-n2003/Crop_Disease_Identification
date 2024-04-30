### **Crop Disease Identification Project**

This repository contains code for a crop disease identification tool, enabling farmers to upload images of crops through a user-friendly interface and utilizing a deep learning model (Convolutional Neural Networks) for disease identification.

### **Dataset**

The dataset used in this project is obtained from Kaggle and contains images of various crop diseases. It includes categories such as Tomato_healthy, Tomato_Tomato_mosaic_virus, Potato_Late_blight, and more. The dataset is sourced from the New Plant Diseases Dataset on Kaggle.

You can access the dataset on Kaggle via the following link: [Crop Disease Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

### **Project Overview**

The project involves the following steps:

1. **User Interface Development:** Developing a user-friendly interface using Streamlit to allow farmers to conveniently upload images of crops.
2. **Model Building:** Creating a deep learning model using Convolutional Neural Networks (CNNs) to analyze images and identify various crop diseases with high accuracy.
3. **Model Deployment:** Deploying the model within the Streamlit application to provide real-time disease identification.

### **Files**

- **`crop_disease_identification.py`**: Python script containing the code for the user interface, model building, and deployment.

### **Usage**

To use the code in this repository:

1. Clone the repository to your local machine.
2. Download the dataset from the provided Kaggle link and place it in the repository directory.
3. Install the required dependencies by running the following command:
    
    ```
    Copy code
    pip install streamlit tensorflow numpy pillow
    ```
    
4. Run the **`crop_disease_identification.py`** script to launch the application.

### **Requirements**

The project code requires the following Python libraries:

- streamlit
- tensorflow
- numpy
- pillow

You can install these dependencies using pip:

```
Copy code
pip install streamlit tensorflow numpy pillow
```

### **Contributor**

- [Adarsh Nashine](https://github.com/adarsh-n2003)

### **Acknowledgments**

- Thanks to Kaggle and the dataset contributors for providing the dataset used in this project.

### **License**

This project is licensed under the MIT License. Feel free to use the code for educational and commercial purposes.
