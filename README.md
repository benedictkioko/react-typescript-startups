# React (Redux), and Django REST Framework application with Docker and Travis CI

[![Build Status](https://travis-ci.org/benedictkioko/react-typescript-startups.svg?branch=main)](https://travis-ci.org/benedictkioko/react-typescript-startups)

## React (Redux)

React Client sends HTTP Requests and retrieve HTTP Responses using fetch with react hooks, shows data on the components.

React Router will be used for navigating to admin pages.

Tail winds CSS will be used for Styling

## Docker

React app, Django and postgre are set to run in their own containers.

## CI/CD

Run continuous integrations with Travis CI to automatically run linting and unit tests.

## Database

PostgreSQL

## Django Rest API Back-end

**Overview**

REST API will handle:

- User authentication
- Creating startup objects
- Filtering and sorting objects

These are endpoints that Django App will export:

| Methods | Urls             | Actions                     |
| :------ | :--------------- | :-------------------------- |
| POST    | /api/students    | create new student object   |
| GET     | /api/students    | retrieve all Students       |
| GET     | /api/student/:id | retrieve a Student by `:id` |
| PUT     | /api/student/:id | update a Student by `:id`   |
| DELETE  | /api/student/:id | delete a Student by `:id`   |

## API Documentation

[drf-yasg] - Yet another Swagger is used generate schemas for the Django Rest Frame API.

#### Output

**Added screenshots**

![swagger api header](images/swagger.png?raw=true "Header")
![swagger student api](images/swagger2.png?raw=true "Student API")
