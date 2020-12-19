**LINK:** https://github.com/Marcestus/cyber-sec-project1

**Instructions:**

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

6. Vote for polls and search them
  - there are three polls available (numbered 2, 3 and 4)
  - notice that the search feature just tells what you have searched for

7. You can find the admin page in localhost:8000/admin
  - user Crusty has superuser access and can view the admin page features

Further instructions and details about the app can be found in the github’s README.md -file.


**FLAW 1: Broken Authentication**

Firstly, the programmer of the app has deleted the password validators from the app’s settings by accident, which enables usage of weak passwords (go to mysite/mysite/settings.py -> the AUTH_PASSWORD_VALIDATORS are missing). This allows weak passwords to be used when creating new users. This is even more bad since the password is the only factor that is needed to login alongside with the username.

Secondly, the app is not protected against credential stuffing, which allows attackers to use unlimited passwords and the app will tell which one was correct. This flaw can be verified by using the tool created in the ”4.19 HackMyPassword” excercise from part 2 of this course.

These two issues together enables attackers to gain access to the app quite easily. There are also studies that show that people use same passwords in multiple places. As weak passwords are a risk on itself, this makes it even more dangerous, because the user can’t control which apps enable these kinds of ”credential sniffing attacks” to happen.

To fix these issues, the programmer should at least return the missing password validators to settings.py. Better passwords give better protection against these attacks. Also, multi-factor authentication tools and protection against the credential stuffing would be a good idea too.

**FLAW 2: Broken Access Control**

Firstly, one of the basic-level users (Crusty) has been given superuser access by mistake. This means that Crusty can access the app’s admin page (localhost:8000/admin). In the admin page, superusers can for example change everyones’ passwords and view their emails. Combined to the previous flaw which enabled Crusty to have a weak password, it is very easy to gain access to the admin page and make a denial-of-service attack or misuse the emails. Attackers can also change the questions and choices of the polls and manipulate the numbers of the votes. Had the vote been about something important – like who is to be named as the next chairman of board of some association – the results might be quite bad.

Secondly, the programmer has also messed up setting the ”login_required” feature to the vote-page (mysite/polls/urls.py -> the last path is missing the login_required – text and it is not set up in the mysite/polls/views.py either). If the attackers were to go exploring the target URLs of the app, they would find that there is no logging required to vote for any of the polls (for example logout and go to localhost:8000/polls/2/vote). Bad mistake! This might also give possibilities to steal important data from the page, like tokens and passwords.

To fix these, Crusty’s superuser access should be removed and the vote-page should be protected with the ”login_required” feature like the other pages.

**FLAW 3: Security Misconfiguration**

The programmer has forgot to change the DEBUG mode to False in mysite/mysite/settings.py. This means that the errors the app gives when going to a page that doesn’t exist, gives way too much information (for example go to localhost:8000). This knowledge combined to the previous flaw (about the ”login_required” feature not being set for the vote page) is a very dangerous combination as the error messages lead the attackers to the vote page very easily:

- Error message from ”localhost:8000” gives you knowledge of ”polls/” page
- Next, trying something that doesn’t exist in ”localhost:8000/polls” like ”localhost:8000/polls/nothing” gives you knowledge of how the vote-page’s URL is constructed
- Then, going to ”localhost:8000/polls/2/vote”, attacker notice that they can vote without being logged in. 

To fix this, the debug mode should be disabled (mysite/mysite/settings.py -> DEBUG = False, not True).

**FLAW 4: Cross-Site Scripting (XSS)**

The programmer has implemented a handy search feature to the ”localhost:8000/polls” page. Unfortunately, as can be seen from mysite/polls/templates/polls/index.html, the script of the search is done unsafely (+ searchResult.get(”search”)), which enables XSS attacks and thus it is possible for example to steal cookies and other sensitive information from the page. As this enables the permanent type of XSS attack, this is very serious flaw, since it can effect everyone who uses the app.

This flaw can be verified by giving some script command to the search field in ”localhost:8000/polls” like (combine these two rows below and give it to search feature -> press search -> the gif is added to the page permanently):
```
<img src="https://media.giphy.com/
media/g9582DNuQppxC/giphy.gif"/>
```

To fix this flaw, the programmer should secure the search feature by escaping the input correctly. For example, Django would detect the possible attack automatically if the code was written like this: <span id="search-query" >The poll you searched is {{ search }}</span>

**FLAW 5: Insufficient Logging & Monitoring**

Last but not least, the programmer hasn’t created any logging features for the app. This means that all of the flaws above – especially the credential stuffing – can go unnoticed for a very long time, if the attackers choose not to attack in a way that can be detected otherwise (like denial-of-service). This is a major flaw which makes all of the above even worse.

To fix this, the programmer should – at the very least – create some sort of logging for all auditable events. And on top of the creation of the loggings, these should be frequently monitored and acted upon.
