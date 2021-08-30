# Cuisine Project

### Technologies

- **Backend**: Python with Flask Framework, reading json content with Pandas library
- **Front-end** : Angular
- **Database**: No database, just two .csv files with content to manage


### Backend

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
	- The sort order is **1.Distance, 2.Customer Rating, 3.Price, 4.Restaurant Name and 5.Cuisine Name**.
	- It searches restaurants based on the params.

#### Running
- Create docker image and then run it (It's necessary to be in the root project folder):
`cd backend && docker build -t cuisine:backend . && docker run cuisine:backend`

##### Installing requirements and creating the backend app (**If the docker process fails**)
- It is necessary to have Python installed. This can be achieved by following instructions here:  https://www.python.org/downloads/
- It is higly recommended to have installed PyPA for installing Python packages on command line. This can be achieved by following instructions here: https://pypi.org/
- Inside the folder **backend**, there is a requirements.txt file.  There, you can find all the necessary packages and its versions to run the backend properly. A faster installion would be running the command **pip3 install -r requirements.txt** .

__Important:__ depending on your system, make sure to use `pip3` and `python3` instead.

- First create virtual env and activate it
`python3 -m venv venv`

`source venv/bin/activate`

- Go to backend and on command line type (Windows):
`set FLASK_APP=main`
`set FLASK_ENV=development`

- Or Linux
`export FLASK_APP=main`
`export FLASK_ENV=development`

- Then move to parent folder and type:
`flask run`

- Check the host and port of flask app:
![Alt text](hostport.jpg)

- It is necessary the file **app.constants.ts** inside the frontend folder and change the value of SERVER_API_URL:
![Alt text](serverapi.jpg)



#### Testing on Postman

- The root folder has a file called **cuisine.postman_collection.json".
- It's json file containing a test suite with 6 different request for testing purpose.
- Every request has at least 2 tests.
- It's necessary to import the json file into Postman. Instructions are here: https://kb.datamotion.com/?ht_kb=postman-instructions-for-exporting-and-importing


### Front-end

- The front-end project was created using **Angular CLI**.
- First all, **Node.js** it is required so later we can install the packages we need and mainly, run the app. Follow instructions: https://nodejs.org/en/download/.

- It is necessary to have it installed to run the app. Follow instructions here:  https://angular.io/cli.

#### Running 

- Create docker image and then run it (It's necessary to be in the root project folder):
`cd frontend/cuisine-app && docker build -t cuisine:frontend . && docker run  -d -p 4200:80  cuisine:frontend`

#### Design

- There is one module called **best-match**, it contains the component **search-component**.
- The UI looks like this:
![Alt text](ui.jpg)

- It shows at most 5 best restaurants according to filter's values added on top of the cards.


##### Installing requirements and creating the front-end app (**If the docker process fails**)
- Inside movie-app folder, run:
`npm install`

- It will check the packages on file packages.json and install locally the packages (**Bootstrap, NGXPagination**) inside the project.

- To run the app, just type inside movie-app:
	 `ng serve`

- Open the browser on **localhost:4200**

#### Testing

- Inside the folder frontend/cuisine-app, run:
`ng test`

- That should be the expected result:
![Alt text](test.jpg)