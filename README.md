# Teacher Student Project

A micro project to manage the association between teachers and students. Where teachers can star grade any number of students and list out.

## Features

- CRUD Teachers
- CRUD Students
- Teacher's can star grade any number of students

## Project Backend and Structure

This project is built on top of Django Web Framework, and it can be run using Docker in just a single command.

- The backend and frontend is both included in this single application. Where frontend generates using Django View, Forms and Template system

- Also there's few exposed API endpoints to mutate star grade of students and list out. This endpoints backed by GraphQL

## Setting development environemnt

Setup and requirements to run the project in dev mode.

### Prerequisite

- Python 3.8.6+
- Pip
- Bash shell

```bash
# Clone the repositury locally
$ git clone https://github.com/vin-ai/tivix_task.git

# Change the directory
$ cd tivix_task

# Create an .env file and set DEBUG and ALLOWED_HOSTS variable
$ cat > .env
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
# Ctrl+D to save

$ pip install --user pipenv
$ pip install --upgrade pip
$ pipenv --install --python `which python3` --dev
$ pipenv run python manage.py runserver
# The dev server must be running now
# Visit http://localhost:8000/school/
```

## Deploying the project on production

Project has been Dockerised to make the project set up and running just by executing few commands.

### Prerequisite

- Ubuntu Linux
- Any latest Docker and Docker Compose installed

### Running

Just execute the below docker dommands to set the production running in production mdoe

```bash
# Clone the repositury locally
$ git clone https://github.com/vin-ai/tivix_task.git

# Change the working directory
$ cd tivix_task

# Run the project using Docker Compose
$ sudo docker-compose up -d --build
```

After executing the commands above go and visit [localhost](http://localhost:/school/)

### Shutting down

To showdown the docker container of the project, execute the command below:

```bash
$ sudo docker-compose down -v
```

## GraphQL

This project has GraphQL endpoints to query and mutate the models. After running the project in development or production mode, visit the **http://localhost:8000/graphql** to run the interface
