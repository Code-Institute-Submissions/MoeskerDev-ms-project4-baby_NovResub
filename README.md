                                            Baby!

View the live project <a></a>

![Mockup]()
![Mockup]()
![Mockup]()

# UX
## Project Goals

The final goal is to sell baby clothing online, but with the option to add toys, for example, in the future or other categories if wanted. 
----
## User Stories
Anonymous Visitor Goals

As an anonymous user, I want to 

As a registered/logged in user, I want to be able to 
----
## Design choices
### Fonts
The font used is called Baumans with a backup font of sans serif.
### Icons
All icons have the purpose to add or explicitly visually show the purpose of the related elements. One icon is a link to add a product to your own wishlist.
### Colours
In essence, the idea was to keep it simple and soft. 

The colours were based on Bootstrap's secondary class, which is tone of grey, and white since the images show several colours.
### Styling

----
## Wireframes
All wireframes can be found [here]().
----
# Features
## Existing Features
- 
- Backend code and frontend functionality for all users to search for items.
- Backend code and frontend functionality for all users to sort items via a certain category.
- Secure payments
- Email response
- Responsive for the following screen sizes:
    - 320x568
    - 360x640
    - 375x667
    - 375x812
    - 411x731
    - 411x823
    - 414x736
    - 540x720
    - 768x1024
    - 1024x600
    - 1024x1366
    - 1280x800
    - 1366x768
## Left to implement

----
# Technologies Used
## Languages
HTML5
CSS3
JavaScript
Python
## External libraries and frameworks
Django:
- Python web framework that makes setting up a project faster and easier.
Postgres:
- The relational database used for this project.
Stripe:
- To have a secure payment infrastructure.
Amazon Web Services:
- To store some static files like the images and the main styling file in the cloud.
Google Fonts:
- To use a font that is free and fits the project.
Font Awesome:
- To use the free icons that they provide.
jQuery:
- To support features and functions. 
Git:
- Used for version control by utilizing Gitpod terminal to commit to Git and Push to GitHub.
GitHub:
- To document and store the development process.
Heroku:
- Used to deploy this full stack web application to a cloud platform.
Balsamiq:
- During the design process, the wireframes were created by Balsamiq.
Something else:
- To create the relational database schema.
----
# Testing
## Validators
- [W3C Markup Validator]()

- [W3C CSS Validator]()

- [JSHint Validator]()

- Python code was checked via the command line by typing: ```python3 -m flake8``` and via the online [Python validator]()
Pylint left me with one unused-import error, W0611 for import env, which is okay. I am using it, pylint just cannot see that.
The PEP8 requirements results were: all right.

## Testing User Stories
The most common path through the website for an anonymous user will be the Homepage and then search for a particular piece of clothing via the search bar or click on the button or one of the menu items to view multiple items on a page and scrolling through them. Another frequent path would be from Homepage to the Register page.

1. As an anonymous user, I want to be able to:
*  

The most common path for a registered user is from the homepage to the login page which leads to the profile page.

2. As a registered/logged in user, I want to be able to:
* easily register for an account so that I can have a personal account, be able to view my profile and create my own wishlist.
* easily login or logout so that I can acces my personal account information.
* easily recover my password in case I forget it so that I can recover access to my account.
* receive an email confirmation after registering so that I can verify that my account registration was succesful.
* have a personalized user profile so that I can view my personal order history and order confirmations, as well as saving default delivery information. 

3. As a store owner, I want to be able to:
* add a product to the store so that I can add new items to my store.
* edit or update a product so that I can change product prices, descriptions, images and other product criteria.
* delete a product so that I can remove items that are no longer for sale.

## Further testing
- The website was tested on Google Chrome, Microsoft Edge and Mozilla Firefox.
- The website was viewed on several devices; Laptop, Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, Iphone 5/SE, Iphone 6/7/8, Iphone 6/7/8 Plus, Iphone x, Ipad, Ipad Pro, Surface Duo and Galaxy Fold, Nest Hub, Nest Hub Max.
- The Lighthouse report for mobile can be found [here]().
- The Lighthouse report for desktop can be found [here]().
## Known Bugs

## Fixed Bugs
- Issue: 
    - Fix: 
- Issue: 
    - Fix: 
----
# Deployment
## Deploy app to Heroku
To deploy Baby! to Heroku, take the following steps:

1. Create a requirements.txt file using the terminal command ```pip freeze > requirements.txt```
2. Create a Procfile with the terminal command ```echo web: python app.py > Procfile```
3. git add and git commit the new requirements and Procfile and then git push the project to GitHub.
4. Create a new app on the [Heroku website](https://signup.heroku.com/login) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
5. Inside your newly created application, in the heroku dashboard, click on "Deploy" > "Deployment method" and select GitHub.
6. Confirm the link between the heroku app and the correct GitHub repository.
7. Now, in the heroku dashboard of your application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:
Key|Value
---|-----
AWS_ACCESS_KEY_ID|
AWS_SECRET_ACCESS_KEY|
DATABASE_URL|
EMAIL_HOST_PASS|
EMAIL_HOST_USER|<your_email_address>
SECRET_KEY|<your_secret_key>
STRIPE_PUBLIC_KEY|
STRIPE_SECRET_KEY|
STRIPE_WH_SECRET|
USE_AWS|<True>


9. Click "Deploy" in the heroku dashboard.
10. In the section "Manual Deploy" make sure the main branch is selected and then click on "Deploy Branch".
The site is now successfully deployed.
11. Click on "View" to view the app in your browser.

## Run this project locally
To clone this project into Gidpod you have to:

1. Have a GitHub account: create one [here]() if needed.
2. Use a Chrome Browser. 
According to the steps below:
1. Install the [Gitpod Browser Extention for Chrome]().
2. After installing it, restart the browser.
3. Log into [Gitpod]() with your Gitpod account.
4. Go to your project GitHub repository in GitHub under the tab "Repositories".
5. Click the green "Gitpod" button in the top right corner of the repository.
6. This will trigger a new Gitpod workspace, created from the code in GitHub, where you can work locally.

To work on the project code within a local IDE (Pycharm,VSCode, etc.):

1. Go to the [project GitHub repository]().
2. Click on the "Code" button next to the green "Gitpod" button.
3. In the Clone section, make sure the HTTPS is selected, then copy the clone url of the repository.
4. Open the terminal in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Then, type ```git clone``` and paste the url that you copied in step 3 behind it:

```
git clone https://github.com/USERNAME/REPOSITORY
```

7. Press Enter for your local clone to be created.

- For further information about cloning a repository from GitHub, read [this]().
----
# Credits
## Code
1. For setting up the project I watched and copied most of the mini-project videos of CI. I adjusted some CSS styling.
2. 
## Content
1. The images came from [unsplash]().
2. The data regarding the clothing I created myself.
3. In order to create the mockups I used this [website](http://ami.responsivedesign.is).
4. To create images from screenshots I used [Paste Pics]().
5. To adapt the sizes of the images I used []().
## Acknowledgements

