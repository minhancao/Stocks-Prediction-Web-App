GitHub Repository Link: https://github.com/minhancao/Stocks-Web-App
Deployed on Heroku: https://stocks-prediction-web-app-v1.herokuapp.com/

========================================================================================
How to run web app:
========================================================================================
Warning: Because our backend is the NodeJS server calling the Python scripts to run, please take your time in testing out the functionalities and let it load as too many requests to the server would crash it on Heroku and also running it locally. If any functionalities of the web app on Heroku stops working, it is probably because the NodeJS server crashed and it takes a while for Heroku to restart the NodeJS server. This also applies to running it locally so if that happens, just start the NodeJS server again by entering into the terminal the command "node server" in the main project directory.

Option 1 (Testing the web app on the web browser):
Setup: 
Go to https://stocks-prediction-web-app-v1.herokuapp.com/ on your browser. Please be patient and let the website load as Heroku is probably starting up the necessary servers and components needed to run the website.

Option 2 (Locally set it up on your computer to run):
Setup: 
Make sure you have NodeJS installed.
Step 1: In terminal, go to project directory, enter the command "pip install -r requirements.txt" to install all the dependencies needed to run the Python code and scripts.
Step 2: In the same directory, enter the command "npm install" to install all the NodeJS dependencies for the backend.
Step 3: Enter "cd client" to go into the client folder, then enter the command "npm install" to install all dependencies for the React frontend.
Step 4: Enter "cd .." to go back one directory back to the main project directory, then enter the command "npm run dev" to run both the frontend server and backend server. The web app should now launch on localhost:3000 on your browser.

Running:
Currently we only have 3 LSTM models trained for AAPL, AMZN, and GOOG.
Step 1: First go to Predictions page.
Step 2: Select AAPL, AMZN, or GOOG on the left sidebar.
Step 3: Click "Predict next 20 stock points movement" button to predict for the selected stock. Please wait patiently, a pop-up will pop up when it is done.
Step 4: When it's done, navigate to the "Line Chart" on the top navbar below the main top navbar. The line chart should display the graph of the stock line and also the prediction line. 
Step 5: Navigate to "Statistics", you can see the predicted prices for the stock that you predicted for the next 20 days so change the date to see on the DatePicker.
Step 6: Navigate to "Prediction Model" and click on "News Articles Analysis for Stock Movement" button to do news articles analysis for the currently selected model on the left sidebar. Please wait while it does analysis, a pop-up will pop up when it's done. The result of the analysis should appear on the page now.

========================================================================================
How to run Python agent program:
========================================================================================
Setup:
Step 1: In terminal, go to project directory, enter the command "pip install -r requirements.txt" to install all the dependencies needed to run the Python code and scripts.

Running:
Step 1: In same directory, enter the command "python3 Prediction.py" to run the program.
Step 2: There will be a prompt to input a stock symbol, e.g. GOOG, AAPL, AMZN.
Step 3: Wait for the output.
