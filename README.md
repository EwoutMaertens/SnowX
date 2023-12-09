# SnowX
Microservice architecture for taking care of all services needed when hosting a Ski Resort. This implementation is based off a school project from UGent and serves only for practice purposes.

## Original Project
The original project and design was created by Cedric Arickx, Matthias De Fré, Nigel Mestach and myself. Credit goes to my colleagues as much to me.

The project was created in Java, as well as it was hosted with docker-compose and it would have to be spun up manually.

## New Project
I will be using the same services as the school project, but I will update the language from Java to Python. I will also update the Docker files to work with Python. The end goal is that I can set up a cluster for the services automatically with Ansible and Kubernetes.

This project only server for learning purposes and should not be used for any other reason.

Architecture is based off: Clean Architectures in Python by Leonardo Giordani

Book is available for free at (pay what you will): https://leanpub.com/clean-architectures-in-python

## Services

* Shop
* Lesson
* Slope
* SkiPass
* Booking
* Calendar
* Medical
* Competition
* Maintenance
* Payment
* Streaming

### Lesson

Domain:
* Instructor
* Language
* LessonGroup
* Student
