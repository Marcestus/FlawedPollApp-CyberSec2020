# Course project for Cyber Security Base 2020

The "mysite" app is a course project for Cyber Security Base 2020 course that is held in University of Helsinki. The point is to flaw an app with at least five vulnerabilities that are found in the [OWASP Top Ten list of cyber security vulnerabilities](https://owasp.org/www-project-top-ten/).

The "mysite" app is based on the app that is created in Django's [Writing your first Django app](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) -tutorial. The "mysite_original" directory holds the original version of the app (which has not been flawed with vulnerabilities) and the "mysite" directory holds the flawed one with vulnerabilities.

The "documentation" directory holds a report of the vulnerabilities that are created. It also contains information on how to fix these issues.

More details about the course can be found in [course's webpage](https://cybersecuritybase.mooc.fi/module-3.1).

## Description of the app

The app is a (very) basic voting app. After login, you can choose a poll to vote and view the results of the vote after you have voted. There is also a search feature, which only shows what you have searched.

## How to download and use the app

1. Clone the repository
  - **Notice that there are two versions of the app in the repository: mysite and mysite_original**
  - **Use the mysite version**, since the mysite_original has not been implemented with flaws and is just a back-up of the functioning app!
2. Go to the app’s root directory (mysite)
3. Give terminal a command ”python manage.py runserver”
4. Go to localhost:8000/polls with your browser
5. Login with one of these credentials
  - user Bob password Builder (user access)
  - user Evan password Allmighty (user access)
  - user Crusty password Clown (superuser access)
6. You can find the admin page in localhost:8000/admin
  - user Crusty has superuser access and can view the admin page features

## Screenshots of the pages

- localhost:8000/polls/

the main page of the app, has polls listed and search feature
![mainpage](https://github.com/Marcestus/cyber-sec-project1/blob/master/documentation/pictures/mainpage.png)

- localhost:8000/polls/2

the voting page for poll 2 (there are 3 polls available numbered 2, 3 and 4)
![voting](https://github.com/Marcestus/cyber-sec-project1/blob/master/documentation/pictures/voting.png)

- localhost:8000/polls/2/results

the result page for the poll 2 (again 3 polls available numbered 2, 3 and 4)
![voted](https://github.com/Marcestus/cyber-sec-project1/blob/master/documentation/pictures/voted.png)

- localhost:8000/admin

the admin page of the app
![adminpage](https://github.com/Marcestus/cyber-sec-project1/blob/master/documentation/pictures/adminpage.png)
