
# EliteServe

# Project Description

A Customer Relationship Management application made to handle clients and teams in an organization using HTML, Tailwind CSS and Python's Django for database support.

# Project Requirements

- A virtual environment for project isolation.
- Python LTS version.
- Django version == 5.0.1 (preferred)
- Tailwind CSS (either through npm or CDN)

# Features

#### The essential features of this project are -
- User Authentication and Authorization : User registration and login.
- Administrator Page : Handling the users and clients that are created and managing the views and models accordingly.
- Team Management : Easily manage the clients and leads and tranfer the leads to clients, managing the team.
- File Upload : An option to upload files under the comment of a team.
- Dockerizing the project : Leveraging the benefits and components of docker to make sure that the project can be run on different Operating Systems. 

# Project Structure and Build

## Directory Structure
- The Directory contains various types of models and respective views depending upon the requirements for each template.
<div align="center">
 <img src="https://github.com/Udit19-pixel/EliteServe/blob/master/Project_Structure.png" alt="Project Logo" width="280" height="300">
</div>

## Environment and Run Procedure
 - The first step is to create a virtual environment for the project and making that as running the activate.bat file present in the bin/Scripts folder. This is to activate the environment created (you might notice "(env)" before the directory path) -

     ```
        - python -m venv env

        # for macOS -
        - source env/bin/activate
        # for windows -
        - env/bin/activate
    ```

- The next step is to install Django onto the present environment (pip or uv, using uv command is fast though) -

    ```
        pip install django
    ```

- Then, start a new project. These steps are done as an administrator, i.e. building your models and views inside the project. Just go inside the newly created project afterwards -

    ```
        django-admin startproject crm_project
        cd crm_project
    ```

- After creating required models,views and respective templates and building the project code, making changes to the directory, one can run the migrations and create a superuser -

    ```
        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
    ```

- The final step is to deploy it on the localhost machine which is on the default port 8080 -

    ```
        python manage.py runserver
    ```

- After running the above command, following will be the homepage of the project -
<div align="center">
 <img src="https://github.com/Udit19-pixel/EliteServe/blob/master/Homepage.png" alt="Project Logo" width="600" height="350">
</div>

# Dockerizing the application 
- One of the features that was later added on to this project was to leverage the resources provided by docker to create a docker image which contains all the dependencies and configurations of the project.

- The first is to create a requirements.txt file which is done by the following command :

    ```
        pip freeze > requirements.txt
    ```
    - The contents of this file will be :
        ```
        asgiref==3.8.1
        Django==3.2.17
        django-cors-headers==4.3.1
        python-decouple==3.8
        python-dotenv==1.0.1
        sqlparse==0.5.0
        tzdata==2024.1
        ```
        
- Then create a dockerfile and a docker-compose.yaml file for that contains instructions in order to create the image of the project.
    - The dockerfile consists of the base image taken from docker hub (an online marketplace), work directory, copy instructions, run and expose and finally the execution command.
    - The docker-compose.yaml is typically for better understanding of the dockerfile present in human readable format for better understanding.

- Following are the commands that I used for creating a docker image :
    ```
        docker compose build
        docker compose up
    ```
