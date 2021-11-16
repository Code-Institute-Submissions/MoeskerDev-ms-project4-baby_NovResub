                                            Baby!

View the [live project](https://babyadmin4-baby.herokuapp.com/)

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
Since the images I found had colour in them, to let them speak out more I decided to keep it simple, clean and light so they stand out even more. The light and pure is also what babies represent. For that reason I also wanted soft shapes throughout the site. Sometimes the forms for submitting data are not that rounded since bigger text fields start to hide the text behind the rounding, making it difficult to see what you actually type.

----
## Wireframes

- All wireframes can be found [here](https://github.com/MoeskerDev/ms-project4-baby/tree/main/media/wireframes).
----
## Data schema
- The schema can be found [here](https://github.com/MoeskerDev/ms-project4-baby/tree/main/media/database_schema).
----
# Features
## Existing Features

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
    - Most HTML pages no errors or warnings. The only thing is that the shopping basket can create errors once it is not empty due to the fact the the product id numbers are mentioned several times on the same page via a certain syntax, {{ item.item_id}} for example. On the edit product page is an error: duplicate attribute id via id=id(underscore)image. However, I have no idea where to correct this.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - All css files passed; checkout, profile and base no errors.
- [JSHint Validator](https://jshint.com/)
    - All passed. The only warnings I did have: template literal syntax only available in ES6 and 'let' is available in ES6 or Mozilla JS extenstions (use moz). The only errors left: undefined variables $ and Stripe, so that is fine since $ is part of jQuery language and Stripe is part of the payment functionality.
- Python code was checked via the online [Python validator](http://pep8online.com/).
    - I have several strings too long left, since I don't know how to solve them without breaking the function.
    - Also, several avoid using null=True on string-based fields such Charfield.


## Testing User Stories
The most common path through the website for an anonymous user will be the homepage and then search for a particular piece of clothing via the search bar, click on the button or one of the menu items to view multiple items on a page and scrolling through them. Another frequent path would be from Homepage to the Register page.

1. As an anonymous user, I want to be able to:
* view a list of products so that I can select some to purchase.

    - When I land on the home page I see a link to all products and a button to shop babies. Both lead me to a page where all products are listed and I can scroll through them to decide which one(s) I want to select.

* view individual product details so that I can identify the image, price, description, product rating,reviews and sizes.

    - All three links of the menu (all clothing, pieces and specials) lead to a list of products where you can click on the image to go to the product detail page where you can find more detailed information about the product.

* view a specific category of products so that I can quickly find products I am interested in without going through all products.

    - By clicking on pieces or specials in the menu, several categories appear to choose from.

* easily view the total of my purchases so that I can avoid spending too much.

    - Below the basket icon, on the top of the page, you can easily see the total price. 

* search for a product by name or description so that I can find a specific product I would like to purchase.

    - When entering a search query in the search bar, both the name and the description of a product are used to search through and show results.

* easily see what I have searched for and the number of results, so that I can quickly decide if the product I want is available.

    - Once you search for pants, above the results, you will see how many products came up as a result for that particular search query.

* easily select the size and quantity of a product when purchasing it so that I can ensure I do not accidentally select the wrong product, quantity or size.

    - On the product details page, the sizes have a dropdown bar where you can easily choose from. Also, the standard quantity is one, but you can easily adapt the quantity by either clicking on the minus or plus buttons or by entering a number manually.

* view items in my basket to be purchased, so that I can identify all items I will receive along with the total cost of my purchase.

    - Once you either click on the basket icon on top of the page or right after adding a product on the go to secure checkout button, you end up on the basket page where you can view the items and the total cost.

* adjust the quantity of individual items in my basket so that I can easily make changes to my purchase before paying for the order.

    - On the basket page you are still able to increase or decrease the quantity of you items by again, either clicking on the minus or plus button or type it in manually. You do have to click the update link after that to make the change final.

* easily enter my payment information so that I can checkout quickly with no hassels.

    - On the basket page, once you click on the secure checkout button you will end up on the checkout page where you are able to easily fill out a form with some personal details, delivery information and payment, as in creditcard.

* feel my personal and payment info is save and secure so that I can confidently provide the needed information to make a purchase.

    - After filling out the required information in the form on the checkout page, you can click on the complete order button. A blue spinner appears on the page and a success message after that once the order has been processed successfully, which gives a sense of safety regarding the payment. 

* view an order confirmation after checkout so that I can verify I have made no mistakes.

    - After clicking on the complete order button you will end up on the checkout success page if everything went well. Here you will find an overview of your order. 

* receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my own records. 

    - In the success message it says that you will receive a confirmation email regarding this order. This way you can even look at it again at a later moment and you have a reference once you receive the order. When I checked this function was working.

The most common path for a registered user is from the homepage to the login page which leads to the profile page.

2. As a registered/logged in user, I want to be able to:
* easily register for an account so that I can have a personal account, be able to view my profile and create my own wishlist.

    - On the landing page, you can easily see the account link, where you can click register. To sign up you need an email, name and password and click on sign up button.

* easily login or logout so that I can acces my personal account information.
    
    - Once logged out, on the landing page, you can see the account link and easily click on login to login. You have to enter username or email and password, then click on signin button.
    - Once logged in, on the landing page, you can see the account link and easily click on logout and then confirm one more time on the logout page that you really want to logout by clicking on the signout button.

* easily recover my password in case I forget it so that I can recover access to my account.

    - If you want to login and forgot your password, go to login page and click on forgot password? link below the buttons. You go to the password reset page and are asked your email. Click reset my password and a message appears that an email has been sent to your email with a link to reset your password. 
    - Go to your email, find the email, click on the link and reset your password.

* receive an email confirmation after registering so that I can verify that my account registration was succesful.

    - Once you successfully signed up, you see a success message which also mentiones that you will receive an email confirmation.
    - Go to your email, find the specific mail and you can see that your account registration worked.

* have a personal user profile so that I can view my personal order history and order confirmations, as well as saving default delivery information. 

    - Once you have created an account, you will have a profile page as well. By clicking on My Account you will see My Profile. Click on it and it will lead to to the profile page. On this page you will find you can add or update information in the default delivery information and see an overview of you order history. The link link below the order number leads you back to your previous order confirmations.

* add products to my personal wishlist so that I can view all products that I wish to have and delete them as well.

    - From the product detail page I can add a product on my wishlist by clicking on the add to wishlist button in the middle of the page just below the image.
    - Once a product is already on your wishlist you will see that the button on the product detail page will say remove from wishslist.
    - By going to my wishlist, either via my profile page and the view wishlist button or via my account and then my wishslist, you will see an overview of all products on the wishlist.

* add a review to a product that will display on the product detail page so that I can inform other potential buyers about the quality of the clothes I bought and give feedback to the company itself about their products.

    - From the product detail page I can add a review about a product by clicking on the add review button at the reviews section. This will lead you to the add review from/page. You have to enter a rating and a review and click on add review button. 
    - Then look at the product details page of that product and you will see your review at the bottom.

* add a review to my personal reviews page so that I can view, edit and delete all my reviews. 

    - Once you add a review it also appears on your personal reviews page where you can see all the reviews you have written. Go their via either clicking on the view my reviews button in your profile page or by clicking on my reviews in the my account link.

The most common path for a store owner is from the homepage to the login page. After that, it is either going to the store management page where they can add a new product or searching for a particular product to either edit or delete that product.

3. As a store owner, I want to be able to:
* add a product to the store so that I can add new items to my store.

    - Once you are logged in as a superuser you are able to add a product by clicing on my account and select store management. This will lead you to the add a product form/page. Fill out the required or more form inputs and click add product.
    - Once successful you will see a succes message and are redirected to the specific product detail page.

* edit or update a product so that I can change product prices, descriptions, images and other product criteria.

    - With all products and edit link is avaible to click on and to edit or update the product (details).
    - Once you click on edit product you go to the edit product form where the information about the product is pre-filled and ready to adapt.
    - Click on update product button and you are redirected to the product details page so you can see if the changes you have made are visible.

* delete a product so that I can remove items that are no longer for sale, have only left part of an outfit or forever out of stock.

    - Like the edit link, the delete link is also present at all products. Once you click on delete as a store owner the product is deleted at once. 

## Further testing
- The website was tested on Google Chrome, Microsoft Edge and Mozilla Firefox.
- The website was viewed on several devices; Laptop, Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, Iphone 5/SE, Iphone 6/7/8, Iphone 6/7/8 Plus, Iphone x, Ipad, Ipad Pro, Surface Duo and Galaxy Fold, Nest Hub, Nest Hub Max.
## Known Bugs
- In the add review form, the rating is not 1, 2, 3, 4 or 5 like I wanted it to be. I have to add rating choices in forms.py to figure out how that works.
- I thought about how the same user can add more than 1 review to the same product. I want to prevent that.
- The quantity in the shopping basket can go below 0, which should not be the case.
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
2. Create a S3 bucket, read [this](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).
3. To get the access keys, read [this](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html).


Using email confirmation after registration or when ordering products.
    - EMAIL_HOST_PASS|
    - EMAIL_HOST_USER|<your_email_address>
The easiest way to do this is to use a gmail account:
1. Open or create your [gmail account](https://www.google.com/gmail/about/).
2. Your emailaddress is the host user.
To get your host pass:
1. Check online

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
3. Log into [Gitpod](https://www.gitpod.io/) with your Gitpod account.
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
1. For setting up the project I watched and copied most of the mini-project videos of CI. I adjusted mainly the CSS styling.
2. I checked the [django documentation](https://docs.djangoproject.com/en/3.2/topics/db/models/) and used the existing models, views, urls and templates to figure out the new ones.
3. In order to solve the line too long errors I looked at [this stackoverflow page](https://stackoverflow.com/questions/53158284/python-giving-a-e501-line-too-long-error?noredirect=1&lq=1).
4. For the pylint no-member error I used [this](https://stackoverflow.com/questions/26657265/hide-some-maybe-no-member-pylint-errors) solution.
5. To remove the DoesNotExist error I followed [this](https://stackoverflow.com/questions/52455835/where-do-i-import-the-doesnotexist-exception-in-django-1-10-from) code.
6. I used option 2 from [this](https://stackoverflow.com/questions/59136064/python-unused-argument-needed-for-compatibility-how-to-avoid-pylint-complainin) source to solve the unused argument error.
## Content
1. The images came from [unsplash](https://unsplash.com/). I actually kept the name of the person who made the image in the name of the image. When you click on the image the creator is mentioned in the url. For the cover image the source is fe-ngo-bvx3G7RkOts-unsplash.
2. The data regarding the clothing I created myself.
3. In order to create the mockups I used this [website](http://ami.responsivedesign.is).
4. To create images from screenshots I used [Paste Pics](https://paste.pics/).
5. To adapt the sizes of the images, by cropping and resizing, I used [befunky](https://www.befunky.com/features/resize-image/).
## Acknowledgements
- Most of all I would like to thank my mentor for guiding me through this larger project.
- Also thanks to some tutors who took, when available, the time to help when I was stuck.
