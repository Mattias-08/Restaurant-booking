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

## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).
- The program can be reached by the [link](https://restaurant-booking-systems-c7e901b3d3c6.herokuapp.com/)

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/Mattias-08/Restaurant-booking).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://8000-mattias08-restaurantboo-z0msi01h5oq.ws.codeinstitute-ide.net/`

- Alternatively, Gitpod can be used by click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://github.com/Mattias-08/Restaurant-booking)

### Using Github & Gitpod

To deploy your Django application, you'll be using the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/ci-full-template).

Getting Started
Create a New Repository:

On GitHub, use the `Use This Template` button on the Code Institute Python Essentials Template.
Give your new repository a name and description.
Set Up Development Environment:

Create a Gitpod workspace from your new repository with `Create Repository from Template`.
Pin your workspace to prevent accidental deletion.
Development Workflow
Frequent Commits: Commit your code changes regularly with clear and descriptive messages.
Use `git add .` to stage changes.
Use `git commit -m "Your commit message"`to commit changes.
Use `git push` to push changes to GitHub.
Note: Always work from your Gitpod workspace to preserve your development environment.

Remember: The master branch is typically used for production deployments. It's recommended to use feature branches for development and merge them into the master branch when ready for deployment.

### Creating an Application with Heroku
This guide outlines the steps to deploy your Django application to Heroku using the Code Institute tutorial and reference to the Django Blog cheatsheet.

Prerequisites:

A GitHub account (https://github.com/)
A Heroku account (https://dashboard.heroku.com/)
Code for your Django application
Steps:

Create Requirements File:

In your Gitpod CLI, run the following command to generate a requirements.txt file listing your project dependencies:
pip3 freeze --local > requirements.txt
Add requirements.txt to your .gitignore file to prevent accidental commits.
Create Procfile:

Create a new file named Procfile in your project root directory.
This file specifies the command to run when your application starts on Heroku.
For a typical Django application, add the following line to your Procfile:
web: gunicorn your_project_name.wsgi:application
Replace your_project_name with the actual name of your Django project.
Set Up Heroku Environment:

Log in to your Heroku account (https://dashboard.heroku.com/).
Click "New" and select "Create New App."
Choose a unique name for your app.
Select your desired region.
Configure Environment Variables:

In the Heroku app settings, navigate to the `Settings` tab and click `Reveal Config Vars.`
Set the following environment variables:
SECRET_KEY: Replace with a strong, randomly generated secret key.
CLOUDINARY_URL (optional): If using Cloudinary for media storage, set your Cloudinary API environment variable here.
Install Heroku Postgres (Optional):

In the "Resources" tab, add the `Heroku Postgres` add-on if your application requires a database.
Connect Heroku to GitHub:

In the `Deploy` tab, click `Deploy` and choose `GitHub - Connect to Github.`
Enter your GitHub repository name and click `Search.`
Select the correct repository and click `Connect.`
Deploy Your Application:

Choose your deployment method:
Automatic deployment: Heroku will deploy changes automatically whenever you push them to GitHub.
Manual deployment: You'll need to click `Deploy Branch` to deploy after making changes.
View Deployed Application:

Once deployment finishes, click the `View` button to access your application running on Heroku.


### Technologies Used

#### Languages

- [Python](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) used to construct styling and colour.

#### Other tools:

- [Django](https://www.djangoproject.com/) was used for the frameworks to build the project.
- [GitHub](https://github.com/) was used to host the code of the website.
- [GitPod](https://gitpod.io//) was used as the development enviroment.
- [Heroku](https://heroku.com/) was used to deploy the app.
- [GIMP](https://www.gimp.org/) was used to make and resize images for the README file.


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