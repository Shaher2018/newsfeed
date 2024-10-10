NewsFeed App
This project is a simple newsfeed application designed with basic social media features. The app allows users to create posts, interact with posts through likes and comments, share content, and establish friendships or follow other users.

Requirements
Main Entities
The newsfeed app includes the following core entities:

User: Represents the users of the application.
Post: Users can create posts with text or media.
Comment: Users can comment on posts.
Like: Users can like posts or comments.
Share: Users can share posts.
Follow/Friendships: Users can follow or establish friendships with other users.
Deliverables
The project consists of the following deliverables, which are hosted in this repository:

1. ERD Diagram
An Entity-Relationship Diagram (ERD) that illustrates the design of the database, including:

Entities (User, Post, Comment, Like, Share, Friendship)
Field types
Relationships (e.g., one-to-many between User and Post, Post and Comment)
Constraints (e.g., foreign keys, unique constraints)
The ERD is available as a screenshot in this repository under docs/erd.png.

2. SQL Schema
The SQL schema is provided to implement the ERD in a MySQL database. This schema defines:

Tables for each entity
Fields and data types
Constraints (e.g., primary keys, foreign keys, indexes)
You can find the SQL file in db/schema.sql.

3. Python Microservice
The backend is implemented as a Python microservice using the Flask microframework. This microservice connects to the MySQL database and exposes a REST API to manage posts.

Endpoints
POST /user: Create a new user.
POST /login: Create a login and get JWT token.
POST /posts: Create a new post.
PUT /posts/
: Update an existing post by ID.
DELETE /posts/
: Delete a post by ID.
GET /posts/
: Retrieve a post by ID.

Prerequisites
Python 3.8+
MySQL
Docker (optional, for containerized setup)
Setup and Running the Application
Using Docker Compose (Recommended)
To simplify the setup, you can use Docker Compose to run both the MySQL database and the Flask microservice.

1- Clone the repository:
  git clone https://github.com/Shaher2018/newsfeed.git
  cd newsfeed
2-run using docker compose
  docker-compose up --build
