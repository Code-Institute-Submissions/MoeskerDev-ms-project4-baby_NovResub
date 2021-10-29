                                            Baby!

View the live project <a></a>

![Mockup]()
![Mockup]()
![Mockup]()

# UX
## Project Goals

The final goal of the store owner is to sell baby clothing online, but with the option to add toys, for example, in the future or other categories if wanted. Providing an easy and safe way to purchase baby clothing online.
----
## User Stories
Anonymous Visitor Goals

As an anonymous user/shopper, I want to be able to:
* view a list of products so that I can select some to purchase.
* view individual product details so that I can identify the image, price, description, product rating,reviews and sizes.
* view a specific category of products so that I can quickly find products I am interested in without going through all products.
* easily view the total of my purchases so that I can avoid spending too much.
* search for a product by name or description so that I can find a specific product I would like to purchase.
* easily to what I have searched for and the number of results, so that I can quickly decide if the product I want is available.
* easily select the size and quantity of a product when purchasing it so that I can ensure I do not accidentally select the wrong product, quantity or size.
* view items in my basket to be purchased, so that I can identify all items I will receive along with the total cost of my purchase.
* adjust the quantity of individual items in my basket so that I can easily make changes to my purchase before paying for the order.
* easily enter my payment information so that I can checkout quickly with no hassels.
* feel my personal and payment info is save and secure so that I can confidently provide the needed information to make a purchase. 
* view an order confirmation after checkout so that I can verify I have made no mistakes.
* receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my own records.

Registered Visitor Goals
As a registered/logged in user, I want to be able to:
* easily register for an account so that I can have a personal account, be able to view my profile and create my own wishlist.
* easily login or logout so that I can acces my personal account information.
* easily recover my password in case I forget it so that I can recover access to my account.
* receive an email confirmation after registering so that I can verify that my account registration was succesful.
* have a personalized user profile so that I can view my personal order history and order confirmations, as well as saving default delivery information. 

Store Owner Goals
As a store owner, I want to be able to:
* add a product to the store so that I can add new items to my store.
* edit or update a product so that I can change product prices, descriptions, images and other product criteria.
* delete a product so that I can remove items that are no longer for sale.
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
- Backend code and frontend functionality for all users to sort items via a certain category or by price.
- Secure payments.
- Email response.
- Registered users have a profile page, a wishlist page and a review page.
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
- [jQuery](https://jquery.com/):
    - JavaScript library to support features and functions. 
- [Django](https://www.djangoproject.com/):
    - Python web framework that makes setting up a project faster and easier.
- [Postgres](https://www.postgresql.org/):
    - The relational database used for this project.
- [Stripe](https://stripe.com/en-nl):
    - To have a secure payment infrastructure.
- [Amazon Web Services](https://aws.amazon.com/):
    - In particular S3, to store some static files like the images and the main styling file in the cloud.
- [Google Fonts](https://fonts.google.com/):
    - To use a font that is free and fits the project.
- [Font Awesome](https://fontawesome.com/):
    - To use the free icons that they provide. 
- [Git](https://www.gitpod.io/):
    - Used for version control by utilizing Gitpod terminal to commit to Git and Push to GitHub.
- GitHub():
    - To document and store the development process.
- [Heroku](https://www.heroku.com/):
    - Used to deploy this full stack web application to a cloud platform.
- [Balsamiq](https://balsamiq.com/wireframes/):
    - During the design process, the wireframes were created by Balsamiq.
- [Lucidchart](https://www.lucidchart.com/pages/) or [diagrams](https://app.diagrams.net/):
    - To create the relational database schema.
----
# Testing
## Validators
- [W3C Markup Validator](https://validator.w3.org/)

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

- [JSHint Validator](https://jshint.com/)

- Python code was checked via the command line by typing: ```python3 -m flake8``` and via the online [Python validator](http://pep8online.com/)
Pylint left me with one unused-import error, W0611 for import env, which is okay. I am using it, pylint just cannot see that.
The PEP8 requirements results were: all right.

## Testing User Stories
The most common path through the website for an anonymous user will be the homepage and then search for a particular piece of clothing via the search bar, click on the button or one of the menu items to view multiple items on a page and scrolling through them. Another frequent path would be from Homepage to the Register page.

1. As an anonymous user, I want to be able to:
* view a list of products so that I can select some to purchase.
* view individual product details so that I can identify the image, price, description, product rating,reviews and sizes.
* view a specific category of products so that I can quickly find products I am interested in without going through all products.
* easily view the total of my purchases so that I can avoid spending too much.
* search for a product by name or description so that I can find a specific product I would like to purchase.
* easily to what I have searched for and the number of results, so that I can quickly decide if the product I want is available.
* easily select the size and quantity of a product when purchasing it so that I can ensure I do not accidentally select the wrong product, quantity or size.
* view items in my basket to be purchased, so that I can identify all items I will receive along with the total cost of my purchase.
* adjust the quantity of individual items in my basket so that I can easily make changes to my purchase before paying for the order.
* easily enter my payment information so that I can checkout quickly with no hassels.
* feel my personal and payment info is save and secure so that I can confidently provide the needed information to make a purchase. 
* view an order confirmation after checkout so that I can verify I have made no mistakes.
* receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my own records. 

The most common path for a registered user is from the homepage to the login page which leads to the profile page.

2. As a registered/logged in user, I want to be able to:
* easily register for an account so that I can have a personal account, be able to view my profile and create my own wishlist.
* easily login or logout so that I can acces my personal account information.
* easily recover my password in case I forget it so that I can recover access to my account.
* receive an email confirmation after registering so that I can verify that my account registration was succesful.
* have a personalized user profile so that I can view my personal order history and order confirmations, as well as saving default delivery information. 

The most common path for a store owner is from the homepage to the login page. After that, it is either going to the store management page where they can add a new product or searching for a particular product to either edit or delete that product.

3. As a store owner, I want to be able to:
* add a product to the store so that I can add new items to my store.
* edit or update a product so that I can change product prices, descriptions, images and other product criteria.
* delete a product so that I can remove items that are no longer for sale.

## Further testing
- The website was tested on Google Chrome, Microsoft Edge and Mozilla Firefox.
- The website was viewed on several devices; Laptop, Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, Iphone 5/SE, Iphone 6/7/8, Iphone 6/7/8 Plus, Iphone x, Ipad, Ipad Pro, Surface Duo and Galaxy Fold, Nest Hub, Nest Hub Max.
- The [Lighthouse](https://developers.google.com/web/tools/lighthouse) report for mobile can be found [here]().
- The Lighthouse report for desktop can be found [here]().
## Known Bugs

## Fixed Bugs
- Issue: Getting the NoReverseMatch error. I got this one several times.
    - Fix: In my case I had to either adapt the url in the path itself or the link to the url in the template.
- Issue: I could not get rid of the following error: A field with precision 1, scale  must round to an absolute value less than 1. This was after I changed the decimal places for the rating to 1 in the review model.
    - Fix: First I tried to change it back to 2 to get rid of the error and deal with decimal places later, but whatever number, also tried 3, I changed it into, the error was there to stay. After some time I asked a tutor. In the end the tutor suggested to reset migrations, since it was a weird error and so we did. It took me about a day to get back to where I was before.
- Issue: when clicking on the add review button of the product detail page, landing on the add review page the error message, belonging to submitting the form if the form is not valid, is triggered on page loading since both fields on the form are required before submitting the form.
    - Fix: 
- Issue: after changing my tables into a grid for mobile, the add to wishlist, remove from wishlist add review, remove review and update review buttons, that all submit, all of a sudden trigger, like usual the accompanying message, but also add the basket to the message like when adding a product to the basket instead of only showing the message withouth the basket.
    - Fix: very interesting I just solved it by adding a missing quotation mark at the end of the previous line above the Succes! line in the toast succes page.
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
1. Install the [Gitpod Browser Extention for Chrome](https://www.gitpod.io/docs/browser-extension/).
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

- For further information about cloning a repository from GitHub, read [this](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
----
# Credits
## Code
1. For setting up the project I watched and copied most of the mini-project videos of CI. I adjusted some CSS styling.
2. 
## Content
1. The images came from [unsplash](https://unsplash.com/). I actually kept the name of the person who made the image in the name of the image. When you click on the image the creator is mentioned in the url. For the cover image the source is fe-ngo-bvx3G7RkOts-unsplash.
2. The data regarding the clothing I created myself.
3. In order to create the mockups I used this [website](http://ami.responsivedesign.is).
4. To create images from screenshots I used [Paste Pics](https://paste.pics/).
5. To adapt the sizes of the images, by cropping and resizing, I used [befunky](https://www.befunky.com/features/resize-image/).
## Acknowledgements

