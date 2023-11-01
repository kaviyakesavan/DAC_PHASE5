#Import necessary libraries
# Function to predict churn based on inputs
def predict_churn(customer_id, gender, senior_citizen, partner, dependents, phone_service, tenure, multiple_lines):
    # You would typically use a machine learning model for such predictions
    # This is a simplified example and does not use a real model

    # Convert binary values (yes/no) to 1/0
    partner = 1 if partner.lower() == "yes" else 0
    dependents = 1 if dependents.lower() == "yes" else 0
    phone_service = 1 if phone_service.lower() == "yes" else 0
    multiple_lines = 1 if multiple_lines.lower() == "yes" else 0

    # Example of a simple rule-based prediction
    if (senior_citizen == 1 and tenure < 12) or (partner == 0 and dependents == 0 and tenure < 6):
        churn_prediction = "Yes"
    else:
        churn_prediction = "No"

    # Print the prediction
    print("Customer ID:", customer_id)
    print("Churn Prediction:", churn_prediction)

# Input values (you can replace these with user input or actual data)
customer_id = "9237-HQITU"
gender = "Female"
senior_citizen = 0  # 1 for yes, 0 for no
partner = "Yes"  # Yes or No
dependents = "No"  # Yes or No
phone_service = "Yes"  # Yes or No
tenure = 2  # Number of months
multiple_lines = "No"  # Yes or No

# Call the predict_churn function with input values
predict_churn(customer_id, gender, senior_citizen, partner, dependents, phone_service, tenure, multiple_lines)

