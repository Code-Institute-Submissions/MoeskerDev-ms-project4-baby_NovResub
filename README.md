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
* have a personal user profile so that I can view my personal order history and order confirmations, as well as saving default delivery information. 
* add products to my personal wishlist so that I can view all products that I wish to have and delete them as well.
* add a review to a product that will display on the product detail page so that I can inform other potential buyers about the quality of the clothes I bought and give feedback to the company itself about their products.
* add a review to my personal reviews page so that I can view, edit and delete all my reviews.

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
- I would like to add an average rating on the product page so that users are also able to sort by rating and get feedback from other regarding the product.
- For the sale items I would like to add a strikethrough, previous price, so that the sales price becomes more obvious.
-
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
- [GitHub](https://github.com/):
    - To document and store the development process.
- [Heroku](https://www.heroku.com/):
    - Used to deploy this full stack web application to a cloud platform.
- [Balsamiq](https://balsamiq.com/wireframes/):
    - During the design process, the wireframes were created by Balsamiq.
- [Diagrams](https://app.diagrams.net/):
    - To create the relational database schema.
----
# Testing
## Validators
- [W3C Markup Validator](https://validator.w3.org/)
    - Most HTML no errors or warnings. A few 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - All css files; checkout, profile and base no errors.
- [JSHint Validator](https://jshint.com/)
    - 
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
- 
## Fixed Bugs
- Issue: When using Stripe and sending test webhooks I always received an error with the payment_intent.succeeded option: Test webhook error: 500.
    - Fix: It turned out that it worked on my page so the tutor mentioned that the most important thing is that it worked on my page but I still wonder why I keep receiving the error.
- Issue: Getting the NoReverseMatch error. I got this one several times.
    - Fix: In my case I had to either adapt the url in the path itself or the link to the url in the template and I used this [stackoverflow page](https://stackoverflow.com/questions/38390177/what-is-a-noreversematch-error-and-how-do-i-fix-it) to help me.
- Issue: I could not get rid of the following error: A field with precision 1, scale  must round to an absolute value less than 1. This was after I changed the decimal places for the rating to 1 in the review model.
    - Fix: First I tried to change it back to 2 to get rid of the error and deal with decimal places later, but whatever number, also tried 3, I changed it into, the error was there to stay. After some time I asked a tutor. In the end the tutor suggested to reset migrations, since it was a weird error and so we did. It took me about a day to get back to where I was before.
- Issue: when clicking on the add review button of the product detail page, landing on the add review page the error message, belonging to submitting the form if the form is not valid, is triggered on page loading since both fields on the form are required before submitting the form.
    - Fix: first I thought to replace the input type submit with a link. However, I received an error message NoReverseMatch for add review. It turned out I forgot to remove the form line with csrf token. After removing those the link worked and the error message was gone.
- Issue: after changing my tables into a grid for mobile, the add to wishlist, remove from wishlist add review, remove review and update review buttons, that all submit, all of a sudden trigger, like usual the accompanying message, but also add the basket to the message like when adding a product to the basket instead of only showing the message withouth the basket.
    - Fix: very interesting, I just solved it by adding a missing quotation mark at the end of the previous line above the Succes! line in the toast succes page.
- Issue: In the mobile header, when being logged in as the superuser, the dropdown menu of account created an overflow for the first option: Store Management.
    - Fix: Checking online I came across [this](https://stackoverflow.com/questions/18268078/drop-down-menu-out-of-screen) solution and it worked for me as well. Adding right:0 and position: relative meant that the whole menu actually was shown in another area. The only thing is that other links move towards different places when opening the dropdown menu of account on mobile screens, so I am not sure if that is the idea, but all links are still available along with the entire dropdown menu of account.
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

This is automatically generated once you connect to the postgres database via Heroku. How?
    - DATABASE_URL|
1. Via the Resources tab in Heroku go to the Add-ons section and search for postgres. 
2. Select Heroku Postgres and use the free plan.

Next, these are related to the Amazon Web Services account. 
By using the S3 service, static files stay in the cloud.
    - AWS_ACCESS_KEY_ID|
    - AWS_SECRET_ACCESS_KEY|
    - USE_AWS|<True> 
1. Create your own [AWS account](https://aws.amazon.com/console/).
2. 

Using email confirmation after registration or when ordering products.
    - EMAIL_HOST_PASS|
    - EMAIL_HOST_USER|<your_email_address>
The easiest way to do this is to use a gmail account:
1. Open or create your [gmail account](https://www.google.com/gmail/about/).
2. Your emailaddress is the host user.
To get your host pass:
1. 

This is a secret key for Django.
    - SECRET_KEY|<your_secret_key>
1. You can create a [secret key](https://djecrety.ir/) here.

Safe payments that can let you know if a payment succeeded or failed.
    - STRIPE_PUBLIC_KEY|
    - STRIPE_SECRET_KEY|
    - STRIPE_WH_SECRET|
In order to get the keys above:
1. Create an account at [Stripe](https://dashboard.stripe.com/register).
2. Go to Developers.
3. Then go to API Keys.
4. In the Standard keys section you will find the Public and Secret key.
To get the webhook secret key:
1. Go to Developers.
2. Then go to Webhooks.
3. Click on Add endpoint
4. Add an enpoint URL, select events to listen to and click on Add endpoint.
5. Click on the particular Endpoint URL.
6. Below the Signing Secret column, click on Reveal.

**Now continue after setting config vars in Heroku:**

9. Click "Deploy" in the heroku dashboard.
10. In the section "Manual Deploy" make sure the main branch is selected and then click on "Deploy Branch".
The site is now successfully deployed.
11. Click on "View" to view the app in your browser.

## Run this project locally
To clone this project into Gidpod you have to:

1. Have a GitHub account: create one [here](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) if needed.
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

