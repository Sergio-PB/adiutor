# adiutor
Assistent for LocusPsicodrama

## About
This is an ongoing project designed to attend the needs of therapists at Locus Psicodrama.

## How to use
### Disclaimer
This version does not support containers or virtual environments for a simple reason, it was designed for a single computer. The original idea was to not put it public on Github. A further version will include docker.
### Prerequisites
You'll need only Django to run it, so simply type in bash:
```
pip install django
```
### Setup
It was designed to run in a LAN, so the secret_key is showing and it allows all hosts, feel free to change that.
After pulling the master, you will need a superuser, so open your terminal in the root and do:
```
cd adiutor
python3 manage.py createsuperuser
```
It will ask for *username*, *email*, and *password*. You won't need the *email* so feel free to leave it blank.
After that you can already run it, in the same terminal, type:
```
python3 manage.py runserver **your_lan_ip**:8000
```
And just like that it's up and running!
To stop it just do *Ctrl+C*, and use the last command in the /adiutor/ to run it again.

### Usage
#### Overview
The project consists of two areas, the staff area and therapists area.
The first is used only to add and change pacients data, while the latter is used mainly to write anamnesis and medical records, and also to transfer pacients to another therapist and read the past records as well.
#### First time
For the first time using the project, you need to create your therapist and staff users, so in your browser go to:
**your_lan_ip**:8000/admin
You'll se an admin login page, insert the created superuser data. Then you should see a page with mainly two sections, the first one has **Groups** and **Users**, in the second item you will create the staff users, it's all pretty self explanatory.
Back to the admin page, in the second section you whould see **Terapeutas** and **Pacientes**, in the first item you must create the therapists users, and again, really intuitive.
#### Using - Staff
As a staff, you can add and change pacients data. To do so, go to the admin page in **your_lan_ip**:8000/admin and log with your staff user. Now the page is really simple with only two options, to add and chage in **Pacientes**, but similar to the previous superuser page. You should be ok on your own here.
#### Using - Therapist
Now as a therapist its a whole new thing.
To acess the therapist page on your browser just go to **your_lan_ip**:8000. As you can see, a brand new page, a login page. The platform was designed to be really easy to use, so log in with you *username* and *password*.
Now you have acess to all your pacients, ordered alphabetically and with a status. After selecting a pacient you'll have the possible actions, according to its status. If its **ANAMNESE** you can, and must, do the anamnesis, but if it's **ATENDIMENTO** it means the pacient is in a regular situation consulting yourself, and so you can write a record, read the pacients record, and transfer him to another therapist.
All the actions are really basic, so it's presumed not needed further explanation.
### Notes
This is a first pilot version, many thing as security matters for example are not beign taking in consideration here.
A second version is planned to be released in the future.
