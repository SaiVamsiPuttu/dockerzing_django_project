# Dockerising a simple web application built with Django and MySQL
# Author - Sai Vamsi Puttu
<p1>
<br/><br/>
  <section>
    
- visitors_main is the project repository where the web app files reside.
    
- Created a dockerfile inside the root of the repository as below:
    
  </section>
 <br/><br/> 

  ![docker](https://user-images.githubusercontent.com/67168573/134577732-fc20ee88-181f-479b-a3d2-b2bce3807c52.png)

<br/><br/>
<section>
  
- 'FROM' creates a layer from the python:3.6 docker image
  
- 'ENV PYTHONUNBUFFERED' creates a Environmental Variable called PYTHONUNBUFFERED and sets it to 1. Setting a value to PYTHONUNBUFFERED ensures that the python output is being sent straight to the terminal without being first buffered.
  
- 'RUN mkdir /cloud_assessment1' creates cloud_assessment1 directory inside the file system of our container.
  
- 'WORKDIR /cloud_assessment1' makes cloud_assessment1 as working directory
  
- 'ADD requirements.txt /cloud_assessment1/' command will copy requirements.txt file from local repository to the docker container's filesystem
  
  </section>
<br/><br/>

![requirements](https://user-images.githubusercontent.com/62174158/131689961-94b401a7-7183-4192-a2a5-a9c871a7c148.png)

 <br/><br/>

<section>
  
- 'RUN pip install -r requirements.txt' will run pip install command for the list of applications that we require.

- 'ADD . /cloud_assessment1/' copies all the files from the cloud_assessment1 repository to the container's filesystem

- Next, I have created a YAML(Yet Another Markup Language) file called 'docker-compose.yml' where I specified configuration for
my django web server and mysql database server.
  
  </section>

![docker-compose](https://user-images.githubusercontent.com/67168573/134577831-7633643c-9899-43cc-a3a8-a6e66ac70449.png)

 
- I ran into a problem where my webserver was starting before my db server. To counter that I have created a shell script which
allows the webserver to start only after the 'db' server is started.
  
![image](https://user-images.githubusercontent.com/62174158/131687552-fb34efbd-2d09-454e-977b-3b500cda9eca.png)

  
- Next, I have build the docker image by running 'docker build .'
  
![docker_build](https://user-images.githubusercontent.com/62174158/131687700-e9822ce0-4765-4ca6-9ec0-ba8884ad2462.png)

- Next I have run 'docker-compose build': docker-compose build will read docker-compose.yml, look for all services containing in the build: 
statement and run a 'docker build' for each one.
  
![docker-compose-build](https://user-images.githubusercontent.com/62174158/131687787-c0b33928-2743-4356-8ee4-b79754f302cb.png)

- Next I have run 'docker-compose up' which builds, (re)creates, starts, and attaches to containers for a service.
  
![docker-compose-up-1](https://user-images.githubusercontent.com/62174158/131687948-99dc5d4a-eda7-4b02-8c68-01b19189f96c.png)

  
![docker-compose-up-2](https://user-images.githubusercontent.com/62174158/131687959-4066a600-40df-4af6-8cf6-bdcb03a41435.png)

  
  <h1 align:"center"> localserver up and running</h1>
<br/><br/>  

https://user-images.githubusercontent.com/62174158/131688504-f3988cb1-d5de-4de9-9b91-554cb4bdaf47.mp4


</p1>
