# The Restaurant Reservation System

![Responsive Mockup]

## UX

### User Stories

- As a user, I want to be able to create an account so that I can manage my reservations.
- As a user, I want to log in to my account to access my existing reservations.
- As a user, I want to make a new reservation to book a table at the restaurant.
- As a user, I want to edit my existing reservations if my plans change.
- As a user, I want to delete reservations that I no longer need.

### Scope

The scope of this project is to develop a web application that allows users to manage their restaurant reservations efficiently. The app will provide user authentication, reservation management, and a responsive user interface.

## Site Features

### Existing Features

- User authentication (sign up, log in, log out)
- Make new reservations
- View list of reservations
- Edit existing reservations
- Delete reservations
- Responsive design with Bootstrap
- CSRF protection

### Future Features

- Email notifications for reservation confirmations and reminders
- Integration with a payment gateway for reservation deposits
- Advanced search and filtering options for reservations
- Mobile app version for easier access

### Wireframes

- Home Page
- Reservation Form
- Reservation List
- Edit Reservation Form
- Delete Confirmation

## Database Schema

### Models

**Table**

| Field   | Type                   | Description        |
|---------|------------------------|--------------------|
| seats   | PositiveSmallIntegerField | Number of seats     |

**Reservation**

| Field       | Type                   | Description                    |
|-------------|------------------------|--------------------------------|
| customer    | ForeignKey(User)       | User who made the reservation  |
| date        | DateField              | Reservation date               |
| time_slot   | CharField              | Time slot for the reservation  |
| table       | ForeignKey(Table)      | Table reserved                 |

## Structure

The application consists of several Django apps, each responsible for a different aspect of the functionality. The main apps include:

- `accounts`: Handles user authentication.
- `reservations`: Manages reservations.
- `tables`: Manages table data.




## Colour Palette

![Color Palette]()
* The color palette for this project was used for the calming and basic effect that will help the user to make good and confident bookings.


---

# Flowchart

The flowchart represents the logic of the application:

  ![Flash Card Page](documentation/image_flowchart_three_in_row.png)

---

# **Technologies Used**

## **Languages**
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

## **Frameworks, Libraries and Programs**

- [GitHub](https://github.com/) - GitHub is a web-based platform for version control using Git, enabling collaborative software development and hosting of code repositories. GitHub connects to GitPod and Heroku.

- [GitPod](https://gitpod.io/workspaces) - Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository.

- [Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilized/tested.

- [Django](https://www.djangoproject.com/) - Django is a high-level web framework for building web applications rapidly with a clean and pragmatic design.

- [ElephantSQL](https://api.elephantsql.com) - ElephantSQL is a hosted PostgreSQL database service that can be seamlessly integrated with Django applications, providing scalable and reliable database solutions.

- [Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.

- [Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a front-end framework for developing responsive and mobile-first websites quickly and efficiently.

- [Cloudinary](https://cloudinary.com) - Cloudinary is a cloud-based media management platform that offers solutions for storing, optimizing, and delivering images and videos for web and mobile applications.

- [Summernote](https://summernote.org/) - Summernote is a Django app that enables users to easily integrate a rich text editor into their web applications, enhancing event creation and description functionality.

- [Django-allauth](https://www.intenct.nl/projects/django-allall/) - A comprehensive authentication app for Django, supporting social authentication, registration, and account management.

- [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Django Crispy Forms is a Django app that provides a better way to generate forms in your Django application.

- [Whitenoise](http://whitenoise.evans.io/en/stable/) - WhiteNoise allows your web app to serve its own static files, making it simpler to deploy on services like Heroku.

- [Font Awesome](https://fontawesome.com/) - Font Awesome is a library of scalable vector icons that can be easily customized and used to enhance the visual appeal of websites and applications.

- [Balsamiq](https://balsamiq.com/) - Balsamiq is a wireframing tool used for creating low-fidelity mockups of user interfaces, allowing for quick and easy visualization of design ideas.

- [Lucidchart](https://lucid.app) - Lucidchart is a web-based diagramming tool that allows users to create and collaborate on flowcharts, ERDs, and other visual representations of data and processes.

- [Am I Responsive](http://ami.responsivedesign.is/) - Am I Responsive is a web tool that allows users to quickly preview how their website appears on various devices and screen sizes, helping to ensure responsiveness and compatibility across platforms.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - The W3C CSS Validator is a tool used to check the validity and syntax of CSS code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).

- [W3C Markup Validator](https://validator.w3.org/#validate_by_input) - The W3C Markup Validator is a tool used to check the validity and syntax of HTML code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).

- [JSHint](https://jshint.com/) - JSHint is a static code analysis tool used for checking JavaScript code for errors, potential problems, and stylistic inconsistencies.

- [Pep8ci](https://pep8ci.herokuapp.com/) - Pep8ci provides Python developers with a tool to check their code against the PEP 8 style guide for adherence to coding standards.

- [Lighthouse](https://developer.chrome.com/docs/lighthouse) - Lighthouse is an open-source tool used for auditing web page quality, including performance, accessibility, SEO, and cross-browser testing.

---

The full list of requirements for the project along with versions can be seen below.
  
asgiref==3.7.2  
cloudinary==1.36.0  
crispy-bootstrap5==0.7  
dj-database-url==0.5.0  
dj3-cloudinary-storage==0.0.6  
Django==4.2.11  
django-allauth==0.57.2  
django-bootstrap-v5==1.0.11  
django-crispy-forms==2.1  
django-summernote==0.8.20.0  
gunicorn==20.1.0  
oauthlib==3.2.2  
psycopg2==2.9.9  
PyJWT==2.8.0  
python3-openid==3.2.0  
requests-oauthlib==1.4.0  
sqlparse==0.4.4  
urllib3==1.26.18  
whitenoise==5.3.0  

# **Testing**

[TESTING.md](TESTING.md)

# **Deployment**

The site was deployed on Heroku and connected to GitHub for version control. This was done by following the below steps:

- Log in to GitHub and create a new repository, using the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template).
- Sign up for Heroku and create a new account.
- Create a new app and choose a suitable region for deployment.
- In the app settings, go to config vars and click "reveal config vars".
- The app requires configuration for the following variables: SECRET_KEY, DATABASE_URL, CLOUDINARY_URL. Assign the corresponding values from your project's env.py to these variables.
- Integrate Heroku with your GitHub by choosing the GitHub integration option in Heroku.
- Locate and select the GitHub repository you created earlier from the CI template.
- Choose manual deployment from the selected branch of your GitHub repository.
- Deploy by clicking the manual deploy button.
- Once deployed, the site is accessible through the live link provided at the top of the document.


---


## Bugs

All the bugs are resolved and the program runs well

## Testing

## Compatibility

In order to confirm the correct functionality, responsiveness, and appearance:

+ The website was tested on the following browsers: Chrome, Firefox, Brave.

No issues was found after the manual testing.

## Manual testing

Manual testing have been done on all the features personally and by a friend to make that there are no interactice bugs.

The testing has also been done on a tablet and phone to ensure that the website works and looks like it should on all normal screensizes.

---
## Validator testing

[online validation tool](http://pep8online.com/) was used to ensure didnt have any issues related to the styling or syntax.

The testing was done manually by coping in the code ![Python Validator](documentation/python%20linter.png)

   
---
## Acknowledgements

[Juliia Konn](https://github.com/IuliiaKonovalova)

I am extremely thankful to my mentor Juliia Konn for her advice and support.