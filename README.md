# Cuisine Project

### Technologies

- **Backend**: Python with Flask Framework, reading json content with Pandas library
- **Front-end** : Angular
- **Database**: No database, just two .csv files with content to manage

#### Running
- Using docker-compose, just run:
`docker compose up`

### Backend

#### Design
+ The backend has 3 files only:
	* **service.py**:  Module where the dataframe is built, filters are applied and search processed.
	* **resource.py**:  Where all the endpoints of REST API are registered and responses are processed.
	* **__init__.py**: Inside app folder, it is the file that creates the Flask app and its context through the whole project. 

### Front-end

- The front-end project was created using **Angular CLI**.
- First all, **Node.js** it is required so later we can install the packages we need and mainly, run the app. Follow instructions: https://nodejs.org/en/download/.

- It is necessary to have it installed to run the app. Follow instructions here:  https://angular.io/cli.

- It's possible to add, update or delete  a restaurant.

#### Design

- There is one module called **best-match**, it contains the component **search-component**.
- The UI looks like this:
![Alt text](images/ui.jpg)

- It is responsive:
![Alt text](images/responsive.jpg)

- It shows at most 4 best restaurants according to filter's values added on top of the cards.

- To run the app, just type inside movie-app:
	 `ng serve`

- Open the browser on **localhost:4200**

#### Testing

- Inside the folder frontend/cuisine-app, run:
`ng test`

- That should be the expected result like this:
![Alt text](images/test.jpg)