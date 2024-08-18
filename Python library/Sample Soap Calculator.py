# SAP table for some common oils (in ounces)
sap_values = {
    "Oil": 0.0,
    "": 0.0,
}

# Function to calculate the amount of lye (sodium hydroxide)
def calculate_lye(oil_weights):
    total_lye = 0
    for oil, weight in oil_weights.items():
        sap_value = sap_values.get(oil)
        if sap_value:
            total_lye += weight * sap_value
        else:
            print(f"Warning: No SAP value for '{oil}' in the table.")
    return total_lye

# Function to calculate the recipe
def calculate_soap_recipe(oil_percentages, total_batch_weight):
    oil_weights = {}
    for oil, percentage in oil_percentages.items():
        oil_weights[oil] = (percentage / 100) * total_batch_weight
    return oil_weights

# Inputs
oil_percentages = {
    "Oil": 0,  # Percentage
    "": 0,
}

total_batch_weight = 1000  # Total weight in grams

# Calculate weights for different oils
oil_weights = calculate_soap_recipe(oil_percentages, total_batch_weight)
print("Weights of different oils:")
for oil, weight in oil_weights.items():
    print(f"{oil}: {weight:.2f} grams")

# Calculate the amount of lye
total_lye = calculate_lye(oil_weights)
print(f"\nTotal amount of lye required: {total_lye:.2f} grams")
    
