# Dash Data Dashboard for Retail Project 
## _Repository Part Two of Two_

## Installation requirements

Installations required if not already installed and at current level of Pip: 
At the time of developing pip was used rather than pip3 for the upgrade and further information about Pip use this link [here](https://pip.pypa.io/en/stable/installation/)
 
The requirements for this dash application includes jupyter notebooks which uses the extension ipynb and Pandas.
If not already globally installed the terminal use the command (if using the first cell of the data.ipynb file precede the command with an exclamation mark and a space e.g. ! pip install pandas)

To visualise the cleansed data an notebook was made called data.ipybn
To create the Dash Application layout app.py was created. Specifically plotly_express, Dash, whitenoise and Pandas will be used here.

```sh
pip install notebook
pip install pandas
pip install dash
pip install dash-bootstrap-components
pip install plotly_express
pip install whitenoise
```
See below for the importing from these installations

## Project Brief 

- 1. Track the most purchased and least purchased products & product categories
overall, per region and per county (limit to top 5 and least 5)
- 2. Track the best performing branches overall per region and per city 
measured in both item quantity sold and monetary value of sales made, limit to best
10 and worst 10)
- 3. Per hour sales for the top 10 branches identified
- 4. Identify the top 10 and bottom 10 profitable branches and indicate how profitable they
are. (Calculate profitability by subtracting expense from total sales)

- Instructions for Use 

A Jupyter Notebook in a file called data.ipybn was created for testing of the implemented csv files. 

To work with Python in Jupyter Notebooks, you must activate a Python or Anaconda environment in VS Code which you've installed the Jupyter package. Using the shortcut Command Palette (Ctrl+Shift+P) and from dropdown Select Interpreter. For this project select the Python environment from Select Interpreter was used.

Within the file you can select a kernel from the top right of the workbook. Selecting code or markdown for notes will produce new cells.
These cells which can be ran all at the same time or can run independently for speed in data assessments.

Installation requirements in the app.py file 

- Setting up the virtual environment 
For current version of software and bash shell use the term
py -m venv env 
command in the terminal, if python3 is used this will be python3 venv env 
This should create the env folder 
Next if using Windows use the command 
env\Scripts\activate
If using Mac or Unix this will be 
Source env/bin/activate
To leave this environment use the command 
deactivate 

This allows for pip install Dash.

Using standard convention

```sh
import plotly.express as px
import pandas as pd
```
Note within the ipynb file pandas and plotly.express is imported. Click on Run All to begin executing these cells

Within the app.py file
Ensure the following is imported 

Within app.py 
```sh
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc, html 
import pandas as pd
import plotly_express as px 
```

BOOTSTRAP 

## Data Files 
Please refer to Dash-Project Part-One which informs further about the data cleansing of the original raw data. 
The files imported from this process are csv files utilised by the Dashboard Application. 

Note the brief informs of city information which is not available, as county information was, this was looked at in raw data however, as county is part of region, this was duplicating and excessive to the user in the graphs in creation of the dash app e.g. for Brief 1 there is already a graph for Top Product for Region Bottom Product for Region and Top Product Category for Region and Top Product Category for Region let alone duplicate these 4 to provide 8 graphs for one Brief question. As County forms part of the Region this was illustrated for top and bottom figures with the raw data for County still available. 

Note that there are not always ten branches in each region which means the difference in top and bottom ten results for performance does not result in any difference in the data shown. 
As the description of of the need for performance as an indicator (sales multiplied by quantity) had some ambiguity in its use of a business indicator as the amount_of_gbp is and can be typically used as an indicator in itself, a hover_data was provided to also show the sales and amount_in_gbp separately.  

## Development Diary 

- For styling there is the option of Dash Bootstrap Components which can be installed with pip install dash-bootstrap-components to be imported and reference to both dbc.themes.BOOTSTRAP and dbc.icons.BOOTSTRAP for a small icon used in the user advisory. 

- Pandas was imported within app.py which holds the Dash application and data.ipybn which holds the testing of files and organisation of cleansed csv files. 

The first three brief points for the Dash Application reference Region data, the final brief references the top ten and least ten from all branches. A NaN value which would alter the results was found within amount_in_gbp and profitability columns for St.Edmundsbury branch relating to the fourth brief. This was tackled with dropna() the axis of 0 indicates row rather than column and how=any means just partial NaN like this instance is tackled rather than all.

Deployment took place with Heroku. 

Note that whitenoise needs to be in place to carry through the CSS styling for the deployment server. 

To add a different preferred style of marker on the line graph using Plotly explore the link in references below.

## Deployment
A runtime.txt file needs to hold the version of Python used which is needed for the Heroku server. 
Gunicorn 'Green Unicorn' is a Python WSGI production grade HTTP Server for UNIX this is reference in the Procfile. The Procfile to be 
created in the Explorer window needs to start with a capital letter. 
Within the ProcFile used for Heroku deployment type web: gunicorn app:server  
Note the space between web and gunicorn is intentional
A requirements.txt file is created with pip freeze > requirements.txt

To run in local host type in the name in the file of the file preceded by python or py version beforehand e.g. 
py app.py
This will bring up an sentence for example Dash is running on http://127.0.0.1:8050/ to click. 

Deployment used a Heroku account. Be aware if within EU, for GDPR select an application hosted on an European server if situated within EU or GB or follow relevant local rules.

Ensure there is a .gitignore file in place which contains any large files and .env/
Upload to Github Repository and then follow the steps on Heroku to connect this repository and 


# References 

- Jupyter Notebooks in Visual Code https://code.visualstudio.com/docs/datascience/jupyter-notebooks

- Runtimes supported by Heroku https://devcenter.heroku.com/articles/python-runtimes

- Dash core components https://dash.plotly.com/dash-core-components

- Dash Bootstrap with a test app code https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/

- Whitenoise required for styling to be transferred from static file for Heroku http://whitenoise.evans.io/en/stable/

- Markers types for Plotly https://plotly.com/python/line-charts/
