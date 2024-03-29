<img src="static/assets/img/favicon.png" width="250" alt="250">

# Restaurant kitchen service manager

Kitchen Manager who ensures that the food is supervised and distributed to the team members.

## Check it out
[Restaurant kitchen service project deployed to Render](https://restaurant-kitchen-service-63xv.onrender.com/)

You may use such credentials:

<b>Username:</b> TestUser <br>
<b>Password:</b> pass4X0F2G%4DplF0word

## Installing / Getting started

Python3 must be already installed

```
git clone git@github.com:Vlad1slavo/restaurant_kitchen_service.git
cd restaurant_kitchen_service
python -m venv venv
Windows: venv\Scripts\activate
Linux, Unix: source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Features

* Registered users can track the number of their visits the main page of the project.
* Unregistered user does not have access to view website pages.
* Registered users can create, update and delete Dishes, Dish types, Ingredients and Cookers.
* Registered user can add himself to the Dish and delete from it.
* Users can use the search form on Dishes, Dish types, Ingredients and Cookers pages.

## DB Structure

![DB_structure](db_structure.png)

## Home-page example

![Home-page](homepage.png)
