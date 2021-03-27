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
The app was created to allow users to store and share their home recipes and meal ideas; and to auto generate a weekly meal planner which randomises meal choices based 
on the users own list of input and shared recipes. 

The site allows users to input meal headings and recipe descriptions as a minimum, providing flexibility and ease of use for more casual users focused on meal randomisation over recipe specificity; 
but for more thorough and active users the ability to provide a link to a representative image on the web, enter ingredients and a cooking method are optional features for the user.

Users can easily share recipes with other users if they know the other users username but cannot search through all users or other users recipes to ensure a level of account security is maintained.

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

##### An experienced cook looking to break routine and utilise their entire recipe repetoire.
- Upload all my recipes into one space specific to me.
- Generate a list of randomly selected and ordered meals from my specific recipes for individual weeks.
- Add thorough recipes which include accurate ingredients and method steps.

##### A group of friends who all enjoy cooking and sharing recipes and ideas.
- Upload recipes and share them with people I know.
- Ensure I maintain control over any recipes I upload so others can't change them.

##### An inexperienced cook looking to improve their cooking habits by learning from their friends.
- Have access to recipes that my friends have shared with me.
- Have access to general recipes available on the site.

##### All consumers
- Register an account if I don't already have one.
- Login securely. 
- Be able to logout for security reasons (such as a shared device). 
- See all the recipes I have created or are shared with me in one space. 
- Search for specific recipes in my collection based on keywords. 
- I want to be able to change my recipes if I refine the method or ingredients over time. 
- I want to remove recipes from my curated recipes if I am no longer interested in that meal. 
- Sometimes I only want to put meal ideas down, and don't yet know all the ingredients or method steps. 
- I don't want to delete recipes from others collections if I remove it from my own. 
- I do want control over who can see the recipes I create. 
- I don't want others to be able to edit recipes I create. 
- Want to be directed back to "safety" if an error occurs or I perform an unexpected input. 

##### The business
- Wants to collate a master archive of user recipes with potential future purpose such as trend analysis. 
- Wants to attract business partner customers with a high traffic site based on user "footfall". 
- Prevent malicious use or abuse of the site. 
- Protect user identity and encourage user trust. 

##### An online grocery retailer
- Wants to seek new entry points for new customers. 
- Promote thier business.
- Grow their market share. 

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
| Deployed register page          | Article element without heading element was switched to a div element. A div which had a name attribute had this attribute removed. | <img src="static/images/w3crecipeviewsuccess.jpg"> |
| Deployed recipes page           | Syntax issues regarding header elements within paragraphs and spans for recipe cards. Paragraph and span tags removed. | <img src="static/images/w3cregistersuccess.jpg"> |
| Deployed recipe create page     | Label syntax issues resolved as they were placed within the inputs they related to. All hidden to prevent overwriting. Name attribute removed from div element. | <img src="static/images/w3ccreatesuccess.jpg"> |
| Deployed recipe view page       | No W3C validation issues detected | <img src="static/images/w3crecipeviewsuccess.jpg"> |
| Deployed recipe edit page       | Issues with labels as per create page were rectified, as were issues with blank fields if a classification, origin or unit were not selected. | <img src="static/images/w3crecipeeditsuccess.jpg"> | 
| Deployed weekly menus page      | Syntax issues regarding header elements within paragraphs and spans for recipe cards. Paragraph and span tags removed. Issue with required month select field not containing a size attribute. Issue with required weeks select field first option containing a value and no size attribute. Stray spans present in weeks dropdown options were removed. |  <img src="static/images/w3cweeklymenusuccess.jpg"> |
| Deployed errors page            | No W3C validation issues detected | <img src="static/images/w3cerrorssuccess.jpg"> |

### Chrome Lighthouse
The deployed site was run through Chrome's lighthouse auditing tool, scoring each standard parameter within the top bracket (90-100).
Various potential improvements were identified within the external resources such as materialize, which are not controlled by the developer.

<img src="static/images/chromelighthouse.jpg">

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

### Responsiveness

The site was launched in [Am I Responsive.is](http://ami.responsivedesign.is/) to verify that the layout was responsive across various device sizes. 
[responsive.pdf](static/docs/responsive.pdf).

The site has also been tested for responsiveness using Google Chromes' built in devices found in its inspect utilities. 
Examples of Google Chromes' results can be found in [wireframes.pdf](static/docs/wireframes.pdf).

### CRUD functions
In Google Chrome all written Create, Read, Update and Delete functionality across the database was tested with no faults detected:
- User can be created.
- User can login based on user lookup (creates session user).
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

### User Stories - Testing

#### An experienced cook looking to break routine and utilise their entire recipe repetoire.
| User Story (From section 1. UX Design --> Scope --> User Stories) | Site functionality |
|-------------------------------------------------------------------|--------------------|
| Upload all my recipes into one space specific to me.| A user can create as many recipes as they wish using the create recipe call to action on the main recipes page. The main recipes page will show a user all recipes that they have created or have been shared with them, which includes site default recipes.|
| Generate a list of randomly selected and ordered meals from my specific recipes for individual weeks | The Weekly Plans page allows a user to select a date for week commencing and automatically choose recipes that they have created or that have been shared with them. |
| Add thorough recipes which include accurate ingredients and method steps. | In the create recipe form there is functionality to add ingredients including quantities and units, and also detail method steps. |

#### A group of friends who all enjoy cooking and sharing recipes and ideas.
| User Story (From section 1. UX Design --> Scope --> User Stories) | Site functionality |
|-------------------------------------------------------------------|--------------------|
| Upload recipes and share them with people I know. | The owners of a recipe can add to a list of names anyones user name that they already know. This recipe will appear on the shared with users collection upon successful entry of a username to this list. |
| Ensure I maintain control over any recipes I upload so others can't change them. | Only owners are able to access the edit button associated with a recipe. Those who have only been added to the shared with cannot access this button. A security flaw was identified at this stage, as users could 'hack' the url to edit a recipe by changing view to edit in the url regardless of the username, however this was rectfied in app file with the inclusion of an if statement to check the users name against the recipe owners prior to rendering the template. If the user is not the owner the site will return a 500 message and the error.html page will be triggered. |

#### An inexperienced cook looking to improve their cooking habits by learning from their friends.
| User Story (From section 1. UX Design --> Scope --> User Stories) | Site functionality |
|-------------------------------------------------------------------|--------------------|
| Have access to recipes that my friends have shared with me.| An owner can edit a set of adjustable fields to enter the correct username string which is case sensitive. Users cannot be searched for to ensure account privacy. |
| Have access to general recipes available on the site. | When a new account is created the username is immediately added to all the recipes owned by WTF, which is the site (and not a user which can be created as the name is less than the mimimum username field length.) |

#### All consumers
| User Story (From section 1. UX Design --> Scope --> User Stories) | Site functionality |
|-------------------------------------------------------------------|--------------------|
| Register an account if I don't already have one. | An account registration form is provided. It only allows unique usernames. Usernames are case sensitive. |
| Login securely. | Passwords are stored encrypted within the database. The password form field is masked. | 
| Be able to logout for security reasons (such as a shared device). | Users can logout from the navbar, which deletes the session cookie and the user variable and returns them to the login page with a flask flash message. |
| See all the recipes I have created or are shared with me in one space. | The main recipes page uses the "shared with" array to lookup recipes and present them in cards to the user. All recipes they have created or that another user has shared with them will be shown here. |
| Search for specific recipes in my collection based on keywords. | A search bar is provided on the recipes page allowing the user to find recipes based on keywords presented on the cards including name, class and origin. |
| I want to be able to change my recipes if I refine the method or ingredients over time. | A recipe owner has access to the edit button when viewing a recipe. Additonally recipes cannot be hacked as the edit route checks the username against the recipe owner when invoked. |
| I want to remove recipes from my curated recipes if I am no longer interested in that meal. | A delete button is available to all users when viewing a recipe they have created or is shared with them. This button only delete their username from the shared with list. A warning is presented in a modal prior to the function being invoked. |
| Sometimes I only want to put meal ideas down, and don't yet know all the ingredients or method steps. | The only required fields in the recipe create form are the name and the description, all other fields are optional by design. |
| I don't want to delete recipes from others collections if I remove it from my own. | The delete button only removes the users username from the shared with list. The recipe remains on the system. This is the case even if the user is the owner. Essentially the recipe becomes archived and uneditable, but still viewable. |
| I do want control over who can see the recipes I create. | Only the recipe owner can edit a recipe, and only in create and edit can users be added to the shared with list. A user cannot add themselves to another recipes shared with list. |
| I don't want others to be able to edit recipes I create. | Only recipe owners have access to the edit button when viewing a recipe. Additonally recipes cannot be hacked as the edit route checks the logged in username against the recipe owner when invoked. |
| Want to be directed back to "safety" if an error occurs or I perform an unexpected input. | A series of error handlers exist to catch server errors such as 500, 404 and 403. This directs the user to an error page which contains specific links back to other site pages, dependant on user logged in status. | 

#### The business
| User Story (From section 1. UX Design --> Scope --> User Stories) | Site functionality |
|-------------------------------------------------------------------|--------------------|
| Wants to collate a master archive of user recipes with potential future purpose such as trend analysis. | Recipes can never be deleted from the database by any user. Only their username is deleted from the shared with list. |
| Wants to attract business partner customers with a high traffic site based on user "footfall". | Speculative, but the ease and flexibility of parts or all of this site should encourage user up-take and build the userbase. The users collection will support this. |
| Prevent malicious use or abuse of the site. | Checks for username exist in various places on the site including registration, login and recipe editing. |
| Protect user identity and encourage user trust. | Users cannot see other users usernames or search for them. If a users username is included in a shared with list but they are not the owner then the shared with list is hidden from that user. | 

#### An online grocery retailer
| User Story (From section 1. UX Design --> Scope --> User Stories) | Site functionality |
|-------------------------------------------------------------------|--------------------|
| Wants to seek new entry points for new customers. | Speculative but the site will build a userbase interested in an activity strongly linked to the grocery market. |
| Promote thier business. | Future potential for advertising space or links to their store through the site. Potential to add sponsored recipes. |
| Grow their market share. | Attracting new customers from this site would achieve this if there is a benefit to those users, such as ease of shopping by prepopulating a shopping basket with items required from a weekly menu. |

## 5. Deployment

The Site is stored on GitHub pages and hosted on Heroku. These are linked by connecting the github repository to the Heroku app workspace.

It consists of 1 Master branch and no other branches.

### Hosted Location

The URL for the hosted site is: https://meal-planner-wft.herokuapp.com/

### Purpose

The hosted site exists to allow users to utilise all its built in functionality to interact with the MongoDb database which sits behind
the site primarily; with the intent for the user to assess the competence of the creator in developing a data-centric site using a micro-framework and
a non-relational database. 

The site allows user to curate their own recipes and meal ideas, store and edit them, and also share them with others in a secure manner. Recipes can be removed
from the creators recipe book and also from the recipe books of those who have had recipes shared with them, but are never truely deleted to ensure that if recipes
are shared they are not lost by those who still desire access to them. Steps are taken to ensure only creators can edit a recipe they own and created. 

Finally the site provides a means of randomly selecting a range of 7 recipes for the user to assign to specific weeks with the intent of providing the user a means
of randomising their weekly meal plans automatically. 

### GitHub Pages

The URL for the GitHub Project is: https://github.com/KWSNick/meal-planner

You may need to log into GitHub in order to access the github pages. 

#### Fork the GitHub Repository
To create a copy of the original "master" repository log into GitHub with your own account, navigate to this repository using the URL above and click the 
"fork" button at the top of the repository. This should provide you with a local copy in your repositories. 

Forking allows you to view and edit a copy of the repository without affecting the "master". 

### Clone the GitHub Repository
Log in to your GitHub account and navigate to this repository using the URL above. near the top of the repository click on Code dropdown button and
choose HTTPS link, copying it using the provided copy button. 

In your IDE open GIT Bash, change the directory to wherever you wish to save your work, then type git clone and paste in the URL copied earlier. 

### Python Package Requirements
The site utilises server-side python script and relies on a number of pre-built packages to function. 
On its host environment these packages will be installed in advance, however should you wish to duplicate the site the following will be required:
- click==7.1.2
- dnspython==2.1.0
- Flask==1.1.2
- Flask-PyMongo==2.3.0
- itsdangerous==1.1.0
- pymongo==3.11.2
- Werkzeug==1.0.1
- Jinja2==2.11.2

The majority of these packages are installed as standard when FLASK is installed using pip. Freeze the requirements into a requirements.txt file if 
a new instance of the project is create using the terminal command pip3 freeze > requirements.txt

additionally some standard Python packages are used including:
- os
- datetime
- calendar
- random (choice)
- bson

### Environment Variables
The site also depends upon a range of environment variables (also known as "config vars" in Heroku) to correctly function. Within a development
environment such as Gitpod the code will utilise a env.py file, which is ommited from the git intentionally due to security reasons. A new file with 
the following environment variables for the os will need to be created if a new instance of this project is generated. 

- default IP address with the alias "IP"
- default port number with the alias "PORT"
- A secret key for certain flask functions including flash messages with the alias "SECRET_KEY" which can be generated from [randomkeygen](https://randomkeygen.com/)
- A URI to connect to the MongoDb database with the alias "MONGO_URI"
- The name of the database within MongoDb that the site will interact with using the alias "DB_NAME"

| Variable | Value |
|----------|-------|
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | <your_secret_key> |
| MONGO_URI | mongodb+srv://MealPlannerROOT:spagMBESbol7125@myfirstcluster.lcznk.mongodb.net/meal_planner?retryWrites=true&w=majority |
| DB_NAME | meal_planner |

A Procfile also exists to instruct Heroku how to run the site using web: python app.py. This code should be contained in line 1 of the procfile.

Once all the pre-requisites are created and installed add, commit and push the project back to your forked github project and link it to an app created in
Heroku by using the Heroku web interface and navigating to Deploy, then selecting GitHub as the deployment method and searching for and connecting to the 
correct github repository. Ensure you enable Automatic deploys below this for future git pushes. 

### Database
The site uses ATLAS MongoDb database service and it is recommended that this be utilised if alternative builds are developed. 
To mimic the database structure used for this site you will need to create a non-relational database consisting of 5 collections as outlined in 
section 1. UX Design --> Structure subsection of this README. The collections within this database and their fields are: 

1. users
    - username (string)
    - first_name (string)
    - last_name (string)
    - password (string)
2. recipes
    - recipe_name (string)
    - region_of_origin (string)
    - classification (string)
    - image_url (string)
    - image_description (string)
    - description (string)
    - ingredients (array)
        - object
            - ingredient (string)
            - quantity (string)
            - unit (string)
    - method (array)
        - step (string)
    - owner (string)
    - shared_with (array)
        - user (string)
3. classification
    - class_name (string)
4. origin
    - origin (string)
5. weekly_plans
    - owner (string)
    - week_commencing (string)
    - year (string)
    - month (string)
    - days (array)
        - day (int)
    - meals (array)
        - object
            - _id (ObjectId)

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