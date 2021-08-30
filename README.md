# Cuisine Project

### Technologies

- **Backend**: Python with Flask Framework, reading json content with Pandas library
- **Front-end** : Angular
- **Database**: No database, just two .csv files with content to manage


### Backend

#### Installing requirements
- It is necessary to have Python installed. This can be achieved by following instructions here:  https://www.python.org/downloads/
- It is higly recommended to have installed PyPA for installing Python packages on command line. This can be achieved by following instructions here: https://pypi.org/
- Inside the folder **backend**, there is a requirements.txt file.  There, you can find all the necessary packages and its versions to run the backend properly. A faster installion would be running the command 

`pip3 install -r requirements.txt` 

__Important:__ depending on your system, make sure to use `pip3` and `python3` instead.


#### Design
+ The backend has 4 files only:
	* **controller.py**:  Module where the dataframe is built, filters are applied and search processed.
	* **resource.py**:  Where all the endpoints of REST API are registered and responses are processed.
	* **__init__.py**: Inside app folder, it is the file that creates the Flask app and its context through the whole project. 

#### Endpoints
- **[GET] /resource/search**
	- No requested params.
	- For every request the python library Pandas merges the restaurants.csv and cuisine.csv into one datframe. 
	- Optional params are: **name_restaurant, name_cuisine, price, distance, customer_rating**.
	- If the keys or the values are invalid, a message with status 400 will be sent as response.
	- The sort order is Distance, Customer Rating, Price, Restaurant Name and Cuisine Name.
	- It searches restaurants based on the params.

#### Running

- Create virtual env
`python3 -m venv venv`
`source venv/bin/activate`

- Go to backend and on command line type (Windows):
`set FLASK_APP=main`
`set FLASK_ENV=development`

- Or Linux
`export FLASK_APP = main`
`export FLASK_ENV=development`

- Then move to parent folder and type:
`flask run --host=172.17.0.2 --port=5000`

- Or create docker image and then run it (**It's necessary to be in the root project folder**):
`cd backend && docker build -t cuisine:backend . && docker run cuisine:backend`

- The backend is already running!