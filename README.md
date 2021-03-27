<img src="static/images/wft_logo.png">

## Contents
1. UX Design
2. Features
3. Technologies Used
4. Testing
5. Deployment
6. User Guide
7. Credits
8. Contributing
9. Support
10. License

## 1. UX Design

The What's for Tea? site was designed around User Experience Design Principles. Target users were identified and business and user
goals were defined. A minimum viable product was determined that could achieve these goals. Future app and business potential was also
mapped out. The scope was set to ensure the project remained concise and fit the strategy, and the front and backend structure reflected this
scope whilst identifying the various APIs and technologies that would be used in the initial app version. The skeleton of the site was defined 
using wireframe models, which assisted in making key design decisions prior to commencing site construction, including site responsiveness 
considerations. Surface design was considered to identify suitable look and feel for this site, which is aimed at a personal consumer audience.

A review meeting was held following the initial UXD process which refined some areas including suitable API technologies and the scope of the project.

### Strategy
The app was created to allow users to store and share their home recipes and auto generate a weekly meal planner which randomises meal choices based 
on the users own list of input and shared recipes. 

The site allows users to input recipe descriptions, link to a representative image on the web, enter ingredients and a cooking method. The user can 

Users can easily share recipes with other users if they know the other users username.

The following stakeholders and their goals were identified:

#### The business
- Attract users with a unique service.
- Collate user recipes.
- Attract future commercial partners.

#### Target Users/Customers
This product is primarily B2C focused with the intent of providing a tool to consumers to assist them in achieving their potential goals such as:
- A more varied diet
- More experimental cooking 
- Break routines
- Change their habits
- Socialise over common interests
These could be driven by influences such as for a new year's resolution, social factors or for health reasons. 

#### Future commercial partners
The tertiary user would be at a B2B level, where there is scope to promote recipes or ingredients on site, or consumer users could be directed 
to links to online retail platforms to encourage the purchase of ingredients from these partner retailers. This user is currently uncatered for as 
their interest in the platform requires a large consumer user base to be established. 

The site may also appeal to other commercial partners such as trend analysts researching eating habits or most common ingredients, and also with its 
collection of recipes which could be utilised to generate cookbooks. 

#### User goals
As a user I have made a new year’s resolution to break from my weekly evening meal routine and attempt to cook varied sets of meals each week in order to 
make the experience more interesting and enjoyable. I am able to cook a variety of meals already but tend to stick to the same core meals as its easier 
to shop for these and maintain enough items at home to easily prepare them. The platform can randomise the meals I already know how to cook for me and this 
encourages me to stick to this resolution. 

As a user I can cook some meals but I’m also looking to find new recipes to add to my repertoire. My friends have lots of recipes they want to share with
me to help me learn and this platform is a really simple way of achieving both our aims. I wish I could search through a list of open recipes on the platform
though and them to my collection if the owner is willing to make their recipe open. 

As a user I often am given recipe recommendations by my friends and respond with recommendations of my own. The platform facilitates the sharing of 
recipes really easily. It could be easier to find my friends on the platform to share recipes with though, maybe with a profile and search function. 

As an online grocery retailer I am interested in attracting more “footfall” onto my site. A high traffic social platform which is specifically and 
directly linked to my business activities would be an ideal place for me to advertise and partner with. 

#### Opportunity

An opportunity importance vs feasibility assessment was carried out to inform on decisions regarding the Minimum Viable Product:
[Opportunity Assessment Analysis](static/docs/opportunityAssessment.pdf)

#### Minimum Viable Product
- A non-relational database consisting of several collections:
    - Recipes
    - Classifications
    - Region of Origin
    - Users
    - Weekly plans
- A site consisting of the following pages, generated via a template structure:
    - Home/landing page
        - Intro to site and purpose
        - Sign in
        - Link to register
    - Register page
    - List users recipes page
        - Add a new recipe button
        - The users own recipes
        - Users tagged in recipes
    - Add a new recipe page
    - Edit a recipe page
    - Weekly planner page
        - Includes previous plans

#### Future Development
- Search all users recipes
- Tag yourself in a recipe to add it to your recipes
- User profile page
- Social interaction
- Easy navigate to online retailer
- Sponsored recipes

### Scope

- Multiple pages
    - Use a framework to build a template page structure to speed up development and reduce code duplication.
    - Use a modified HTML/CSS/JS Library Navbar component.
        - Various navbar items only visible depending on login state/user authorisation
    - A Visually appealing logo that clearly informs the user of the brands purpose.
    - Use of card-components to display individual documents within collections i.e. recipes. 
    - Use of date-time analysis to order on latest time-dependent documents.

#### User Stories

| User                                                   | Story                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New year’s resolution made to vary weekly meals        | The platform was easy to upload my recipes to and maintain/modify them if required. I found the weekly menu generator quick and simple with minimal interaction required from me.                                                                                                                                          |
| Consumer looking for meal inspiration                  | The platform currently allows my friends to share recipes they have uploaded with me, however I wish I could search for recipes that are open to any user.                                                                                                                                                                 |
| Consumer group looking to share meal recipes and ideas | The platform easily and intuitively facilitates the creation and sharing of recipes and I find I rely on this platform to store my recipes and share them with my friends. I'd like to use this platform to comment on recipes and be more socially interactive with posts, and also mare easily find my friends accounts. |
| Online grocery retailer                                | We have recognised the growing uptake in the platform and wish to explore how we might partner with it to promote our business and grow our revenue.                                                                                                                                                                       |

### Structure
#### Database Collections
The database consists of 5 collections stored in MongoDB. The core collections are recipes and weekly plans and these are linked by both the user collection
and directly between one another as the weekly plans documents store recipe document ids to reference them. Most fields are stored as strings with the exception
of several lists such as shared with, and the ingredients which are an array of objects which contain their own fields.

The other collections provide supporting information to be inserted into the recipe documents as required. 
<img src="static/images/databaseStructure.jpg">

Currently these collections are only manageable via the MongoDB backend, however in future releases this functionality will be brought into the frontend via 
administration accounts. 

#### Site Pages
The site is based around a framework template design, offering a common navbar and footer throughout, however content within the navbar alter depending 
upon the user-login state, current page etc. 

Main authorised pages are accessible from all other pages via the common navbar. sub pages are only available via main pages or further sub pages.  

A page along with appropriate routing has been created to handle common 404, 403 and 500 errors which may occur. 

<img src="static/images/pageStructure.jpg">

Forms utilise a common styling and restrict user input to defined options where possible to aid document grouping and linking. Form offer validation 
where possible. 

Flask has been used to provide the framework using the Jinja templating language, with the included Werkzeug security utilised to provide user 
authentication and security. 

Materialize provided the library for styling of the site. 

JQuery has been utilised for any Javascript functionality. 

### Skeleton
The site will be responsive across all device sizes and utilise Materialize breakpoints to achieve this. The site will 
be equally user friendly on all device sizes.

| Materialize Breakpoint ID | Minimum Pixel Width | Maximum Pixel Width |
| -----------------------   | ------------------- | ------------------- |
| Small (mobile)            | 1px                 | 600px               |
| Medium (tablet)           | 601px               | 992px               |
| Large (desktop)           | 992px               | infinite            |


[Wireframes](static/docs/wireframes.pdf) were constructed in Pencil Wireframes in order to provide a design brief for
the project, maximise coding productivity and minimise mission creep. The final product is compared to the wireframes within this document.

### Surface
The site is designed for use in the domestic, home setting at a consumer level and is designed to appeal to this potential customer base. It attempts to 
clearly convey as much of the purpose of the site as is practicable within its title, supported by short succinct content immediately displayed to users 
upon their initial visit.

The site relies on muted, pastel colours which invoke a homely feel. Creams, yellows, greens and blues are used for background and text 
colours.

Buttons and calls to action utilise expected colour conventions, Green for create, amber for save and add functions, orange for edit and update functions 
and red for delete functions. 

Icons are able to quickly describe the function, heading or label they are associated with.

Cursive script is used convey a sense of informality and different cursive fonts are used for the headers and main text. Indie Flower was selected for 
the main body text as it provided the desired fun and relaxed hand written style whilst maintaining legibility. Permanent Marker was selected for the 
headers as it provided the desired fun and relaxed hand written style that might be found in an analog home cookbook whilst maintaining legibility. 

## 2. Features

### Existing Features
Users are able to:
- Create an account
- Log in with this account
- Send an email to admin if the user forgets login details
- See their recipes and those shared with them
- Search these recipes
- Create new recipes
- Edit recipes they are the owner of
- Delete recipes from their collection
- Generate a 7 day weekly menu for a user selected week which chooses random recipes from their collection
- Log out

### Future Features
Desirable future features to develop are:
- Manage user account
- Search for users
- User profiles
- Social chat/comment functions
- Frontend admin database management
- Search for none owned or shared recipes
- Customise generated menus
- Duplicate shared recipes to allow edits on the duplicated recipe
- Generate shopping lists for each weeks recipes
- Send shopping lists directly to retailer baskets

## 3. Technologies Used

### Python 3.8.7

Python is the backend language used to drive the server side script.

#### License

Python can be utilised under the PSF (Python Software Foundation) Agreement and the Zero-clause BSD License: https://docs.python.org/3/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python

PSF Agreement: https://docs.python.org/3/license.html#psf-license

Zero-clause BSD License: https://docs.python.org/3/license.html#bsd0

### MongoDB

MongoDB provides the hosting of the non-relational database for the site. It was utilised under the Server Side Public License.

#### License

Server Side Public License; https://www.mongodb.com/licensing/server-side-public-license

### Flask 1.1.2

Flask provides the development framework for the site and wraps key features from Jinja2 templating language and Werkzeug security which are used
to populate the site with database content and help write information back to the database.

#### License

All Pallets Projects fall under the three clause BSD license: https://palletsprojects.com/license/

Pallets Projects License and Copyright: https://palletsprojects.com/governance/licenses-and-copyright/

### Materialize 1.0.0 (Material Design)

[Materialize Homepage](https://materializecss.com/about.html)

Materialize was utilised to provide responsive front-end design via a component library. It is able to provide some
JavaScript functionality including form validation, mobile sidenav and accordion control.

#### License

Materialize is released under the [MIT License](https://tldrlegal.com/license/mit-license)

A copy of this license is provided in Materialize GitHub Project: https://github.com/twbs/bootstrap/blob/v4.5.0/LICENSE

Material Design is owned by Google and falls under their terms of service: https://policies.google.com/terms

### Font Awesome 5.15.2

Font Awesome provides text based icons which can be manipulated and controlled by CSS styling. These were used throughout the site to provide visual ques to content.

#### License
Font Awesome License Page: https://fontawesome.com/license

Icons are licensed under the CC BY 4.0 https://creativecommons.org/licenses/by/4.0/

Fonts are licensed under SIL OFL 1.1 https://scripts.sil.org/OFL

Code is licensed under MIT https://opensource.org/licenses/MIT

### jQuery

[jQuery Homepage](https://jquery.com/)

jQuery is a JavaScript library designed to make html traversal and manipulation
much simpler than raw JavaScript, by presenting the author with a wealth of
simple code and commands which call on much more complex functions.

jQuery was utilised to improve the targeting of elements and provide some support
for animation and user interaction where possible.

#### License

jQuery is provided under the [MIT License](https://tldrlegal.com/license/mit-license)

### LogoMakr

Produced the brand logo using a combination of Google Fonts and icons.

[LogoMakr Homepage](https://logomakr.com)

#### License

Logos created via LogoMakr are approved for both personal and commercial use.

[LogoMakr License](https://logomakr.com/getstarted/terms-conditions/)

### Google Fonts

Google Fonts offers open source font styling options for personal and commercial use. 2 fonts were used within style.css.

#### License

The use of this product was inline with Google API's terms of service [Google Fonts Terms](https://developers.google.com/terms)

## 4. Testing

### W3C Validation

The HTML and CSS syntax for the project was checked using the W3C Validation services provided here:
[W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input)
[W3C Markup Validation](https://validator.w3.org/#validate_by_input)

| Validated File or Deployed Page | Outcome Comments | Result Image |
|---------------------------------|------------------|--------------|
| style.css                       | The CSS validation initially flagged an incorrect (but functional) styling of padding-inline-start applied to ordered list elements at the small breakpoint. This was swapped to padding-left which corrected the validation. A warning was presented regarding the imported Google fonts file at the top of the style.css file indicating that this imported file is not checked by the validation tool. In this instance the imported file is provided by a 3rd party and attributed in this document. | <img src="static/images/w3ccsssuccess.jpg"> |
| Deployed login page             | Semantic markup issues due to absence of messages containing headings, and articles without headings were rectified. A space within the mailto link was also removed.| <img src="static/images/w3cloginsuccess.jpg"> |
| Deployed recipes page           | Syntax issues regarding header elements within paragraphs for recipe cards. Paragraph tags removed. | <img src="static/images/w3crecipessuccess.jpg"> |
| Deployed recipe create page     | Label syntax issues resolved as they were placed within the inputs they related to. All hidden to prevent overwriting. Name attribute removed from div element. | <img src="static/images/w3ccreatesuccess.jpg"> |

### Browser Compatibility

|Browser| Version| Comments| Fixes Applied|
|-------|--------|---------|--------------|
Google Chrome|  88.0.4324.150 | Fully Functional | |
Mozilla Firefox| 85.0 |   Fully Functional | |
Microsoft Edge| 88.0.705.68 |  Fully Functional | |
Microsoft Internet Explorer| 11.630.19041.804 | Javascript/JQuery functions hampered e.g. login/register buttons will not enable when form correctly completed. Tooltip does not show over create recipe call to action. Cannot copy image link from external source. Drop down options missing from forms. Javascript functions to add new rows do not work. Default image address does not auto load into image_url input. Modals do not load. Accordion does not work. | None. Legacy platform not recommended for use with this site due to Javascript JQuery incompatibility.
Samsung Internet| 13.2.2.4 | Fully Functional | |
Opera| 74.0.3911.218 | Fully Functional | |
Apple Safari|	N/A	Could not be tested.|Microsoft Windows no longer supported.| |

A common issue with weeks selection input not displaying the string at small breakpoint has been identified. No fixed is currently applied but the issue is flagged for future development.

An issue was identified where if the units dropdown was left on "Unit" or the blank field the recipes could not be edited. This was recitifed by placing a space in the value of these fields to ensure they assign a value and create a field for each object. 

### Responsiveness

The site was launched in [Am I Responsive.is](http://ami.responsivedesign.is/) to verify that the layout was responsive across various device sizes. 
[responsive.pdf](static/docs/responsive.pdf).

The site has also been tested for responsiveness using Google Chromes' built in devices found in its inspect utilities. 
Examples of Google Chromes' results can be found in [wireframes.pdf](static/docs/wireframes.pdf).

### CRUD functions
In Google Chrome all written Create, Read, Update and Delete functionality across the database was tested with no faults detected:
- User can be created.
- User can login based on user lookup v(creates session user).
- Site-owned recipes assigned new user in shared with.
- Can create new recipe.
- Can edit all fields of recipe. 
- Can delete field contents and update. 
- Can delete user from recipe shared with and therefore remove from the recipes page.
- Can search recipes.
- Can reset search.
- Can create a weekly menu.
- Can delete this weekly menu from the collection. 
- Cannot create more than one menu for that week for logged in user. 
- Can logout (destroys session user)

## 5. Deployment

The Site is stored on GitHub pages hosted on Heroku.

It consists of 1 Master branch and no other branches.

The URL for the site is: https://meal-planner-wft.herokuapp.com/

The URL for the GitHub Project is: https://github.com/KWSNick/meal-planner

The site requires config vars which are stored securely within Heroku. A Procfile also exists to instruct Heroku how to run the site. 

The site has a list of dependencies which are listed in requirements.txt in the root of the site. These must be installed on the server prior to launching the site. These have already been installed on the Heroku app space. 

The site is designed to work on any modern browser, but was developed within Google Chrome version 88.0.4324.150 and it is recommended this platform 
be utilised in preference to others to ensure full compatibility and functionality. See browser compatibility section within testing for further details.

## 6. User Guide

### Register
On first visit to the site you will need to create an account. Navigate to the create account page via the navbar or sidebar menu on mobile devices. 
Alternatively use the link at the bottom of the login page. 

<img src="static/images/register.jpg">

Complete the form on the create account page. Only use letters for your first and last name, a username between 5 and 12 characters long consisting 
of at least one upper and one lower case letter and one number. No special characters or spaces allowed.

Your password should be at least 6 characters long with at least one lower, one upper case letter and a number. You must enter the same password twice 
to complete the form.

Once all form entries are valid click out of the forms inputs to activate the register button, which checks that all inputs are valid first.

<img src="static/images/registerform.jpg">

### login
Once you have successfully completed registration you will be taken back to the login page and you are prompted to login. 

Enter your username and password, and click out of the input fields to activate the login button, which checks that all fields 
are valid. 

If you forget your login details use the contact administrator button below to write an email to the admin team to reset your 
account details. 

<img src="static/images/login.jpg">

### Recipes Page
When successfully logged in you will be taken to your recipes page. Here you will see all recipes that you have either created 
or are shared with you. What's for Tea automatically shares a selection of recipes to get you started. If your friends are already 
active on the account you can ask them to share their recipes with you. 

#### Create a Recipe
To create a new recipe click the "create recipe" button in the bottom right hand corner of the page. 

<img src="static/images/createrecipe.jpg">

This launches the Add a New Recipe page. Complete the form to the best of your knowledge. It's ok to leave fields blank if not required.

To add an image to the recipe you need to find a suitable image online, right click it and copy its link or address and paste it into the url input.
We recommend using Pexels which is a free open source stock photo site, although you are free to use whichever source you wish including your own 
online galleries. Add a suitable image description to act as alternative text if the image cannot be loaded. A placeholder image is provided 
if a suitable image cannot be supplied by yourself. 

Choose an appropriate class if required, and a region of origin for the recipe if appropriate or select the blank options. 

<img src="static/images/addrecipe1.jpg">

Enter a short description of the meal in the Description field. 

To share this recipe with another user enter their username, which is case sensitive, into the input. For multiple users click the plus button to add a 
additional users in individual inputs. To remove a user just delete the text from the input and leave it blank.  

Add ingredients in the ingredients section by entering a name, the quantity for one person and the units from the dropdown options. To add new ingredients 
click the add button below. To remove an ingredient just leave the inputs empty. 

Add method steps by entering a description of the step and clicking the add button to insert a new input. If you decide to remove a step just empty the input 
and it will be skipped when saved, with the step numbering correctly being assigned to the next filled row. 

<img src="static/images/addrecipe2.jpg">

Click "Create" at either the top or bottom of the form when you are done. You will be returned to your recipes page. 

#### View a Recipe. 

Scroll to or search for the recipe you wish to view. Click the card it is presented in to view the recipe. 

<img src="static/images/searchresult.jpg">

If you created the recipe you are the owner, and owners are able to edit the recipe, and see who the recipe is shared with in a scrollable list. 

Recipes which are only shared with the user can only be viewed and deleted from the users recipes. A user who is not the recipe owner cannot see 
the shared with list for data protection purposes. 

<img src="static/images/recipeview.jpg">

#### Delete a Recipe
To delete a recipe from your recipes view the recipe and click delete, and confirm deletion. 

Deleting a recipe only deletes the user from the shared with list. The recipe remains on the server and all users the recipe is currently shared with 
can still view the recipe. Once the recipe has been deleted the user is returned to their recipes page. 

<img src="static/images/confirmdelete.jpg">

#### Edit a Recipe
To edit a recipe you must be the recipes owner. If so you will have access to the edit button in the view recipe page. Click it to launch the edit recipe 
page. It is similar to the Add a New Recipe page except that the fields are pre populated with the recipes existing content.

Alter any of the input field contents as require, or add new inputs to lists such as shared with, ingredients and method. To remove fields just empty the 
input contents and leave blank. Empty inputs are skipped. 

<img src="static/images/recipeedit.jpg">

Click save at the top or bottom of the page when complete and you will return to the recipe view with the new amendments. 

<img src="static/images/recipeeditsuccess.jpg">

To cancel any changes click the back button at the top of the recipe edit page and confirm you want to discard changes. 

<img src="static/images/editback.jpg">

#### Search for a Recipe
To search for a recipe enter a keyword or words in the search box on the recipes page and click the magnifying glass. To reset the results to all of your 
recipes hit the red reset button. The search will only return recipes you own or are shared with you. 

<img src="static/images/search.jpg">

### Weekly menus
To access your weekly menus navigate to the page via the navbar or sidebar on mobile devices. If you have no weekly menus the page will display a warning. 

Recipes are displayed in descending data order. 

<img src="static/images/menuwarning.jpg">

#### Create a new menu
To create a menu use the embedded form at the top of the weekly menus page. Select a year and a month, which defaults to this year and month, and click "Get Weeks" 
to populate the weeks dropdown box. When options are available in the weeks dropdown, select the week commencing you desire to create a menu for and click the create button.

A new accordion row will be created which when clicked expands to shown recipe cards for seven randomly selected recipes from your recipe collection. 

<img src="static/images/menus.jpg">

Each recipe card can be clicked to take you to the recipe view page for that recipe. 

<img src="static/images/menusopen.jpg">

Only one menu can exist for each week, a warning will display is a duplicate week is attempted. You must delete the existing week before generating a 
new menu for that week. 

<img src="static/images/menuerror.jpg">

#### Delete a menu
To delete a menu click the delete button on the accordion header and confirm the delete in the subsequent modal. 
You will be returned to the weekly menus page. 

<img src="static/images/menudelete.jpg">

### Logout
To securely logout from the site click the logout button in the navbar or mobile sidebar. This will return you to the login page. 

<img src="static/images/logout.jpg">

## 7. Credits

### Content

Site content is original and developed by the author to offer services/functionality free-of-charge with the exception of linked URLs used for recipes 
which are sourced from the open source library provided by [Pexels](https://www.pexels.com/). No liability is assumed for any user experiences or 
results obtained from the provided content of the website and users utilise this site, its functionality and its content at their own risk. 

The content, functionality and output was correct to the best of the authors knowledge at the time of issue (see testing for further details). 

Users are able to create and share content within the app and no liability is accepted for the accuracy or correctness of this content.

User content is utilised at users own risk, 3rd party or otherwise. 

### Media

Copyright 2021 Nicholas Bowley

The logo was created by the author in logomakr online tool and is accredited as per the instruction of the tool's developer. It is subject to copyright restrictions and limitations.

### Acknowledgements
Stock photo images sourced from https://www.pexels.com/ which is an open source resource.

Jinja2 variables within the HTML were written based on guidance provided on Stack Overflow posted by Patrick José Pereira April 6th 2018 regarding setting variables for iteration purposes. 

Thanks to machine learning mastery for tips and advice on python random and choice modules. https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/

A special mention to the [Code Institute](https://codeinstitute.net/) mini-project which provided the basis and inspiration for user login and control. 

Thank you to my better half for putting the idea of a random meal generator to me!

Thanks as always to my Code Institute Mentor Akshat Garg for the review time and advice he has provided during this project.

## 8. Contributing

This project is a closed example for educational and ability demonstration purposes. Contribution is not permitted at this time.

## 9. Support

For queries or support contact nicholasbowley@googlemail.com.

## 10. License

This site is licensed under the 2-Clause BSD License

Copyright 2021 Nicholas Bowley

Redistribution and use in source and binary forms, with or without modification, are permitted provided that 
the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following 
disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the 
following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.