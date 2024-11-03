# Housing Price Prediction App

This Flask app predicts the price of a house based on the 4 input values:
1. Area (m2)
2. Bedrooms (no. of bedrooms)
3. Bathrooms (no. of bathrooms)
4. Parking (no. of parking spaces)

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory. 
3. Run the setup script:
   - On Unix-based systems:
     ```
     bash ./setup.sh
     ```
   - On Windows systems:
     ```
     setup.bat
     ```
4. The application will start automatically after setup.


## Project Info
1. The project uses the [Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset) 
from Kaggle released under the CC0: Public Domain license.
2. First, a decision tree is trained on 75% of the data and feature importance is calculated. 
3. Then a decision tree is trained using all the data rows but only the top most 4 features/columns. This model is saved
for future use. 
4. The flask app uses this saved model to predict house prices based on the input values of the user. 
5. The app supports all CRUD operations. 

