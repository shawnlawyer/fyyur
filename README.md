Fyyur
-----

### Introduction

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.

Your job is to build out the data models to power the API endpoints for the Fyyur site by connecting to a PostgreSQL database for storing, querying, and creating information about artists and venues on Fyyur.

### Overview

This app is nearly complete. It is only missing one thing… real data! While the views and controllers are defined in this application, it is missing models and model interactions to be able to store retrieve, and update data from a database. By the end of this project, you should have a fully functioning site that is at least capable of doing the following, if not more, using a PostgreSQL database:

* creating new venues, artists, and creating new shows.
* searching for venues and artists.
* learning more about a specific artist or venue.

We want Fyyur to be the next new platform that artists and musical venues can use to find each other, and discover new music shows. Let's make that happen!

### Tech Stack

Our tech stack will include:

* **Docker** containerization software to package up and run the application
* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend

### Main Files: Project Structure

  ```sh
  ├── README.md
  ├── logs/app/error.log
  ├── requirements.txt
  ├── Dockerfile
  ├── migrate.py
  ├── app.py
  ├── docker-compose.yml
  ├── env.example
  ├── app
  │   ├── config.py
  │   ├── blueprints
  │   ├── controllers
  │   ├── forms
  │   ├── models
  │   ├── static
  │   │   ├── css
  │   │   ├── font
  │   │   ├── ico
  │   │   ├── img
  │   │   └── js
  │   └── templates
  │       ├── artist
  │       ├── show
  │       ├── venue
  │       ├── errors
  │       ├── forms
  │       ├── layouts
  │       └── pages
  ├── docker
  │   └── nginx.conf
  └── logs
      ├── nginx
      │   ├── access.log
      │   └── error.log
      └── app
          └── error.log
  ```
  


Acceptance Criteria
-----

1. The web app should be successfully connected to a PostgreSQL database. A local connection to a database on your local computer is fine.
2. There should be no use of mock data throughout the app. The data structure of the mock data per controller should be kept unmodified when satisfied by real data.
3. The application should behave just as before with mock data, but now uses real data from a real backend server, with real search functionality. For example:
  * when a user submits a new artist record, the user should be able to see it populate in /artists, as well as search for the artist by name and have the search return results.
  * I should be able to go to the URL `/artist/<artist-id>` to visit a particular artist’s page using a unique ID per artist, and see real data about that particular artist.
  * Venues should continue to be displayed in groups by city and state.
  * Search should be allowed to be partial string matching and case-insensitive.
  * Past shows versus Upcoming shows should be distinguished in Venue and Artist pages.
  * A user should be able to click on the venue for an upcoming show in the Artist's page, and on that Venue's page, see the same show in the Venue Page's upcoming shows section.
4. For the models

##### Stand Out

Looking to go above and beyond? This is the right section for you! Here are some challenges to make your submission stand out:

* Implement artist availability. An artist can list available times that they can be booked. Restrict venues from being able to create shows with artists during a show time that is outside of their availability.
* Show Recent Listed Artists and Recently Listed Venues on the homepage, returning results for Artists and Venues sorting by newly created. Limit to the 10 most recently listed items.
* Implement Search Artists by City and State, and Search Venues by City and State. Searching by "San Francisco, CA" should return all artists or venues in San Francisco, CA.

Best of luck in your final project! Fyyur depends on you!

### Development Setup

- cp .env.example .env   
  
- docker-compose up -d --build  
  
- docker exec -it fyyur_app_1 bash

- python3 migrate.py db upgrade

- browse to http://localhost/  
