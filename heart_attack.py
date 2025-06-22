import pickle
import numpy as np


# Function to get user input
def get_input():
    
    # Prompt user for input
    print("Enter the patient metrics in the following order to predict: ")
    print("age sex cp trtbps chol fps restecg thalachh oldpeak slp caa thall exng")
    user_input = input()
    
    # Split the input into a list of strings
    input_strings = user_input.split()
    
    # Convert the list of string into the list of floats
    user_input = [float(num) for num in input_strings]
    
    return user_input


# Function to predict from input
def predict_heartattack(model, user_input):
    
    # Convert user input to numpy array 
    input_data = np.array(user_input).reshape(1, -1)
    prediction = model.predict(input_data)
    
    return prediction


def convert_to_category(prediction):
    label_mapping = {0: "low chance", 1: "HIGH CHANCE"}
    return label_mapping[prediction[0]]

def main():
    
    # load the model from disk
    filename = 'heartattack_predictor.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    # Get input from user
    user_input = get_input()
    
    # Predict 
    prediction = predict_heartattack(loaded_model, user_input)
    print(f'\nThe patient has a {convert_to_category(prediction)} of having a heart attack.')
    
    # Debug: Show the input data and prediction
    # print("\nDebug Information:")
    # print("Input Data:", user_input)
    # print("Prediction (0=low, 1=high):", prediction[0])

if __name__ == "__main__":
    main()