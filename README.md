# TravelTales API

## Adavanced Front-End - Portfolio Project 5

#### Developer: BekMart

Travel API is a Django REST Framework API that powers a social content-sharing application built for travellers. It allows users to share blog-style posts about their favourite travel destinations, including photos and written content. Other users can log in to like and comment on posts, and follow profiles, making it a platform for both inspiration and connection.

While developed specifically for the [Travel Tales app](https://travel-tales-5c522e360995.herokuapp.com/), the API architecture is flexible enough to be adapted for other content-based or community-driven platforms.

The API supports secure user authentication, photo uploads, content creation, and real-time user engagement features such as likes, comments, follows, and notifications.

## Key Features:
- User authentication
- Authenticated users can create and customise their profiles
- Authenticated users can create, edit, or delete posts
- Posts can be tagged with travel destinations for searchability
- Authenticated users can comment on and like posts
- Authenticated users can follow one another
- Authenticated users receive notifications when someone likes, comments, or follows them
- Users can search and filter posts by profile owner, title, location and content.

The deployed API can be found here: [Travel API](https://travel-api-ca880bcd8809.herokuapp.com/)

<h1 id="contents">Table of Contents</h1> 

- [Design Process](#design-process)
    - [User Stories](#user-stories)
    - [Data Models](#data-models)
    - [API Endpoints](#api-endpoints)
- [Features](#features)
    - [Existing features](#existing-features)
    - [Future Feature Ideas](#future-features)
- [Technologies Used](#technologies)
    - [Frameworks and Languages](#frameworks-langugages)
    - [Additional packages](#additional-packages)
    - [Other Software](#other-software)
- [Testing](#testing)
    - [User Story Testing](#user-story-testing)
    - [Functionality Testing](#functionality-testing)
    - [Validation](#validation)
    - [Issues Found](#issues)
- [Deployment](#deployment)
- [Credits](#credits)

<h1 id="design-process">Design Process</h1>

Much of the [design process](https://github.com/BekMart/travel-tales#design-process) is outlined in the front-end applications [README](https://github.com/BekMart/travel-tales) documentation. This is where you will find the site user stories and details of the [agile development](https://github.com/BekMart/travel-tales#agile-development) process implemented.  

<h2 id="user-stories">User Stories</h2>

User stories for the API were written from a developer's perspective, focusing on the needs of both first-time and returning users, and ensuring the data models and API structure supported their actions effectively.

## [Complete API Build](https://github.com/BekMart/travel-api/milestone/1?closed=1)

The user stories are categorized into four themes:

### [Project API set-up](https://github.com/BekMart/travel-api/issues/31)

1. <u>User Story:</u>
As a web developer I want to create a back end API to host all of the data needed for the front end to operate and link this to the front end repository so that the user can have a seamless experience.

<u>Acceptance Criteria:</u>
- Create Django project and apps
- Install and configure dependancies needed to run
- Set up CORS environmental variables
- Connect to PostgreSQL database

### [Build models and admin](https://github.com/BekMart/travel-api/issues/32)

2. <u>User Story:</u>
As a web developer I want to create models in a custom database so that Users can complete functions such as posting comments/liking posts/following other users.

<u>Acceptance Criteria:</u>
- Create Post/Comment/Like/Follower models
- Run migrations & check admin panel
- Register models in admin.py for testing

### [Create views with appropriate serializers and url patterns](https://github.com/BekMart/travel-api/issues/33)

3. <u>User Story:</u>
As a web developer I want to use serializers to create views which can be accessed by the user by visiting a specific url path.

<u>Acceptance Criteria:</u>
- Create serializers for each model
- Build views using DRF generic views
- Create permissions
- Add urls for each app
- Connect everything in main/urls.py

### [Authentication and testing](https://github.com/BekMart/travel-api/issues/34)

4. <u>User Story:</u>
As a web developer I want to use token authentication to authenticate users login details to ensure users data is secure and updated efficiently.

<u>Acceptance Criteria:</u>
- Set up token authentication with dj-rest-auth
- Test login/register/logout endpoints
- Test all CRUD endpoints
- Deploy API and test production URL

<h2 id="data-models">Data Models</h2>

A simple but effective Entity Relationship Diagram (ERD) was created to visualise the relationships between the models. This guided the API structure and ensured clear, logical connections between user actions and data representation.

![This is the ERD which was created to show the database structure and the relationships held between the different models](https://res.cloudinary.com/dvgobcuck/image/upload/v1746433801/ERD_dlavr8.png)

### Profile Model
Represents user profile data, extending the default User model with a one-to-one relationship. Includes fields for name, bio, and profile image. Profiles are automatically created when a user registers.

### Post Model
The central content model. Authenticated users can create posts with titles, captions, images, and a linked Location. Posts appear on the home page and on the user’s profile.

### Comment Model
Allows users to comment on any post. Users can also edit or delete their own comments.

### Like Model
Authenticated users can like or unlike any post. Each user can only like a post once and they cannot like their own.

### Followers Model
Creates a connection between two users — the owner is following the followed user. Enables social feed potential and profile connections.

### Location Model
A list of travel destinations. Posts are linked to a location via a ForeignKey. Each location has a slug for SEO-friendly URLs and can optionally include a description and image. Enables filtering and destination-specific pages.

### Notification Model
Notifies users of activity related to them, including likes, comments, and follows. Stores sender (from_user), recipient (to_user), type (like, comment, follow), and whether the notification has been read.

<h2 id="api-endpoints">API Endpoints</h2>

The Travel API provides the following endpoints:

| Endpoint | HTTP Method | CRUD | View Type | Permissions | Filter/Search |
|---|---|---|---|---|---|
| **Authentication** |
| /api-auth/login/ | GET | N/A | N/A | Public |  |
|  | POST | N/A | N/A | Public |  |
| /api-auth/logout/ | GET | N/A | N/A | Public |  |
| /dj-rest-auth/registration/ | POST | N/A | N/A | Public |  |
| /dj-rest-auth/login/ | POST | N/A | N/A | Public |  |
| /dj-rest-auth/logout/ | POST | N/A | N/A | Authenticated |  |
| **Profiles** |
| /profiles/ | GET | Read | List | Public | Search fields: "owner__username", "content" |
| /profiles/\<int:pk\>/ | GET | Read | Detail | Public | Filters: "owner__profile" |
|  | PUT | Update | Detail | Owner |  |
| /profiles/popular/ | GET | Read | List | Public | Filters: "followers_count" |
| **Posts** |
| /posts/ | GET | Read | List | Public | Filters:  "location__slug", "likes__owner__profile"<br>Search fields: "owner__username", "title", "location__name", "content" |
| /posts/create/ | POST | Create | Detail | Authenticated |  |
| /posts/\<int:pk\>/ | GET | Read | Detail | Public | |
| | PUT | Update | Detail | Owner | |
| | DELETE | Delete | Detail | Owner | |
| /posts/feed/ | GET | Read | List | Authenticated | Filters: "owner__followed__owner__profile" |
| /posts/popular/ | GET | Read | List | Public | Filters: "likes_count", "comment_count" |
| **Locations** |
| /locations/ | GET | Read | List | Public | |
| /locations/\<slug:slug>/ | GET | Read | List | Public | |
| /locations/\<slug:slug>/posts/ | GET | Read | List | Public | Filters:  "location__slug"<br>Search fields: "location__name" |
| /locations/popular/ | GET | Read | List | Public | Filters: "posts_count", "likes_count", "comment_count" |
| **Likes** |
| /likes/ | GET | Read | List | Public | |
| | POST | Create | List | Authenticated | |
| /likes/\<int:pk\>/ | GET | Read | Detail | Public | | 
| | DELETE | Delete | Detail | Owner | |
| **Comments** |
| /comments/ | GET | Read | List | Public | | 
| | POST | Create | List | Authenticated | | 
| /comments/\<int:pk\>/ | GET | Read | Detail | Public | |
| | PUT | Update | Detail | Owner | |
| | DELETE | Delete | Detail | Owner | |
| **Followers** |
| /followers/ | GET | Read | List | Public | |
| | POST | Create | List | Authenticated | |
| /followers/\<int:pk\>/ | GET | Read | Detail | Public | |
| | DELETE | Delete | Detail | Owner | |
| **Notifications** |
| /notificatioons/ | GET | Read | List | Owner | |
| /notifications/unread/ | GET | Read | List | Owner | Filter: "is_read=False" |
| notifications/\<int:pk\>/mark-read/ | DELETE | Delete | Detail | Owner | |
| notifications/mark-all-unread/ | DELETE | Delete | List | Owner | |

[Back to Contents](#contents)

<h1 id="features">Features</h1>

<h2 id="existing-features">Existing Features</h2>

- **User Authentication**: 
    - On registering an account, a profile is automatically generated for the user.
    - Users can log in and out using secure JWT-based authentication.
    - Passwords are securely hashed, and users can reset or change them via the appropriate endpoints.
- **Profile personalisation**: 
    - Authenticated users are able to personalise their own profile with image and bio details.
- **CRUD functionality for posts**: 
    - Authenticated users can create, read, update, and delete their own travel posts.
    - Posts include titles, images, descriptions, locations, and timestamps.
- **Location**:
    - When a user creates a post, if the location doesn't currently exist, then it will be created and added to the locations list.
    - The most popular locations are hosted at the top.
    - The image representing the location is the one which is currently most popular.
- **User Interactions**: 
    - Authenticated users can like/unlike other users’ posts.
    - Authenticated users can comment on other users' posts and update or delete their own comments. 
    - Users can follow and unfollow other users to stay updated on their activity.
- **Notifications**: 
    - Users receive real-time notifications when someone likes their post, comments on it, or follows them.
    - Unread notifications can be marked as read once viewed or user can mark them all as read at once.
- **Filtering and sorting results**:
    - Depending on the endpoint, posts are arranged based on popularity, creation date, or number of likes/comments.
- **Search Capabilities**:
    - Users can enter keywords to search posts. This includes title, content, owner and location. 
- **Popular Results**:
    - There is a display of most popular profiles, locations and posts based on activity such as amoutn of posts, likes and comments and followers.

<h2 id="future-features">Future Features</h2>

- Users to like specific comments, not only posts
- Implement direct messaging between users for private conversations.
- Add a map view to show posts based on geographic data.
- Introduce tags or hashtags for better content discovery.

[Back to Contents](#contents)

<h1 id="technologies">Technologies Used</h1>

<h2 id="frameworks-langugages">Framework and Languages</h2>

- <b>Python</b> – Core programming language used
- <b> Django </b> – Web framework used to build the backend API
- <b>Django REST Framework (DRF)</b> – Extension for building RESTful APIs
- <b>PostgreSQL</b> – Relational database used in production
- <b>Gunicorn</b> – WSGI server for deploying Django apps on Heroku

<h2 id="additional-packages">Additional Python Packages</h2>

- `dj-rest-auth` - 	Provides login/logout/registration endpoints for Django REST
- `djangorestframework_simplejwt` - JWT authentication support
- `django-allauth` - Handles user authentication, email, and account management
- `django-cors-headers` - Allows frontend and backend to interact across different domains
- `django-filter` -	Enables filtering of querysets in DRF views
- `crispy-bootstrap5`, `django-crispy-forms`, `django-bootstrap5` - For rendering and styling forms using Bootstrap 5
- `django-summernote` -	Adds a rich text editor to admin/content creation forms
- `Markdown` - Used for rendering Markdown content safely
- `bleach`, `defusedxml` - Sanitize HTML and XML inputs to prevent XSS and unsafe content
- `cloudinary`, `django-cloudinary-storage`, `dj3-cloudinary-storage` - Used for image/media uploads and storage on Cloudinary
- `dj-database-url`	- Allows reading database URLs from environment variables
- `psycopg2` -	PostgreSQL database adapter for Django
- `pillow`	- Image processing support for uploaded files
- `whitenoise`	- Serves static files in production without a CDN
- `python3-openid`, `oauthlib`, `requests-oauthlib` -	Support for social login features via allauth
- `cryptography`, `cffi`, `pycparser`	- Required dependencies for handling JWT and HTTPS securely

<h2 id="other-software">Other Software & Tools</h2>

- <b>Visual Studio Code (VS Code)</b> - Source code editor used during development
- <b>GitHub</b> – Version control and project hosting
- <b>GitHub Projects/Issues</b> – Used for Agile methodology by assigning user stories to issues and using labels to organize user stories.
- <b>Git</b> – For source control and version tracking by committing changes
- <b>Lucidchart</b> - Used to generate ERD diagram in planning stages
- <b>Cloudinary</b> – Used for storing and serving uploaded images
- <b>Heroku</b> – Cloud platform used for deployment

[Back to Contents](#contents)

<h1 id="testing">Testing</h1>

<h2 id="user-story-testing">User Story Testing</h1>

1. As a web developer I want to create a back end API to host all of the data needed for the front end to operate and link this to the front end repository so that the user can have a seamless experience.

2. As a web developer I want to create models in a custom database so that Users can complete functions such as posting comments/liking posts/following other users.

3. As a web developer I want to use serializers to create views which can be accessed by the user by visiting a specific url path.

4. As a web developer I want to use token authentication to authenticate users login details to ensure users data is secure and updated efficiently.

I have tested the functionality of all individual features and clearly evidenced their correct behavior in the [User stories section](https://github.com/BekMart/travel-tales#user-story-testing) of the Travel Tales README file. 

Additionally, I have included screenshots that demonstrate how actions taken on the deployed TravelTales front-end are accurately reflected in the deployed API. This confirms the two applications are properly connected and update in real-time, fulfilling the key requirements of the developer-focused user stories. These images serve as proof that the API is working as intended and that users can successfully interact with it through the front-end interface.

### Profile
- The image below shows the `/profiles/10/` endpoint in the deployed API, displaying a user’s details such as username, bio, page stats and profile image. These details match those seen on the front-end app. 
- A second screenshot shows the `/dj-rest-auth/user/` endpoint confirming the user is authenticated. This is also visually confirmed on the front end, where the user’s avatar is visible in the navbar and additional authenticated navigation options are present.
<details><summary>See evidence</summary>

![Image shows the user logged into their profile as their avatar is in the navigation bar](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668472/profile_fqt7vi.png)
![Image show the results in the back end - profile end point displaying user data matching the data of the users profile being displayed](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668469/profile-api_uvo33m.png)
![End point shows that details of currently authenticated user](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668469/authenticated_vjuqy1.png)
</details>
<br/>

### Create Post

- The following image demonstrates that the "Add Post" functionality works as intended. A newly created post appears at the top of the `/posts/` endpoint in the deployed API, displaying all relevant details such as title, content, location, and image. This confirms that the data has been successfully sent from the front end to the back end.
- At the same time, the front-end application reflects this new post immediately on the home screen, and a success message is shown to the user, confirming that the post was created successfully and stored in the database.
<details><summary>See evidence</summary>

![Image shows a post that is displayed in the front end application.](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668493/create-post_dp5dsi.png)
![Image of new post details in the deployed API](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668494/create-post-api_qpqi4v.png) 
</details>
<br/>

### Edit and Delete Posts

- When a post is edited through the front-end application, the updated data (e.g., title, location, or content) is sent to the API, and the changes are applied directly to the same post instance - the post ID remains unchanged. This confirms that the PUT request successfully updates the existing object in the database.
<details><summary>See evidence</summary>

![Image shows the user has edited their post in the front end application](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668500/edit-post_y8zwdl.png)
![Updated details are in the deployed API under the same original post id](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668502/edit-post-api_mq4y3l.png) 
</details>
<br/>

When a post is deleted from the front end, the associated post instance is removed entirely from the back-end API. Visiting the same endpoint (eg `/posts/121/`) after deletion would result in a no post being displayed, confirming that the DELETE request was processed and the object no longer exists in the database.
<details><summary>See evidence</summary>

![Image shows the post has been removed from the deployed API](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668498/delete-post_jwqhlp.png) 
</details>
<br/>

### Follow
The `/followers/` end point displays all follow instances which shows the new instance created in the example below.
<details><summary>See evidence</summary>

![Image shows that the user has followed a profile via the deplpoyed website](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668512/follow_jmbwrg.png)
![All follow details are recorded in the deployed API](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668510/followers-api_wysz4u.png)
</details>
<br/>

### Like
The `/likes/` end point displays all like instances which shows the new instance created in the example below.
<details><summary>See evidence</summary>

![Image shows that the user has liked a post via the deplpoyed website](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668512/follow_jmbwrg.png)
![All like details are recorded in the deployed API](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668510/followers-api_wysz4u.png)
</details>
<br/>

### Locations pages
The `/locations/` endpoint displlays a list of the locations which all have posts associated with them in order of how many posts they have and the amount and the amount of comments and likes they have. The list within the API reflects what is being displayed in the front end application. 
<details><summary>See evidence</summary>

![Image shows the locations list page](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668521/locations_qpc2hy.png)
![The locations list within the API matches the list displayed in the front end app ](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668516/locations-api_tqv9y8.png)
</details>
<br/>

The `/locations/slug/posts/` endpoint displays a list of posts that are assocated with a particular location which is refrenced by the slug in the URL address.
<details><summary>See evidence</summary>

![Image shows like of posts relating to Thailand](https://res.cloudinary.com/dvgobcuck/image/upload/v1746668518/thailand_yax8hw.png)
![The API endpoint for this list shows the same items being listed](https://res.cloudinary.com/dvgobcuck/image/upload/v1746682723/thailand-api_fzbzel.png)
</details>
<br/>

<h2 id="validation">Validation</h2>

All python code written for the project passes through the PEP 8 [CI Python Linter](https://pep8ci.herokuapp.com/) with no issues.

<h2 id="issues">Issues Found</h2>

### Solved Bugs

#### Local Development Configuration Issue
While setting up local development for the front-end, I initially encountered issues connecting to the deployed back-end API. Although the deployed site worked correctly, local requests from the front-end returned a 502 Bad Gateway error.

After reaching out to Tutor Support, I discovered the issue stemmed from misconfigured environment variables and an incomplete understanding of how the front-end communicates with the back-end.

Specifically, I needed to:
- Add the correct local development URL (e.g., http://localhost:3000) as CLIENT_ORIGIN_DEV in the Heroku config vars of the API project.
- Update CORS_ALLOWED_ORIGINS in the API’s settings to include both the deployed front-end and the local development front-end.
- Ensure the Axios baseURL in the front-end project correctly pointed to the back-end URL depending on the environment (local or deployed).

With this guidance, I learned how the front-end and back-end are linked through CORS settings, environment variables, and Axios configuration. Once these were correctly set, the connection was established successfully.

#### Authentication Issue and Resolution
During development, I encountered a persistent 403 Forbidden error when attempting to log in or register users through the front-end application. Although the back-end API responded with a 200 OK status for valid credentials, the application was blocked shortly afterward, preventing authentication from completing.

After troubleshooting and a session with Tutor Support, the issue was traced to a misconfiguration involving environment variables. Specifically, the env.py file had been accidentally committed to version control, causing Heroku to prioritize local variables over the ones set via Config Vars. This led to the front-end and back-end becoming misaligned, especially regarding authentication and CORS settings.

To resolve this, I removed env.py from the project and added it to .gitignore to prevent future exposure. I then regenerated the sensitive environment variables — including the SECRET_KEY and Cloudinary credentials — and configured them securely in Heroku's Config Vars. I chose to retain the original PostgreSQL DATABASE_URL to avoid data loss, and ensured the correct CLIENT_ORIGIN and CLIENT_ORIGIN_DEV values were present.

Following these changes and a redeployment of the API, authentication began working correctly across both local development and the deployed application. This process deepened my understanding of environment management and highlighted the importance of keeping secrets out of version control.

### Unsolved Bugs

#### Safari Compatibility Issue (Authentication)
During testing, I discovered that the site functioned correctly in Chrome and Firefox, but not in Safari. Specifically, the login appeared to succeed—returning valid access and refresh tokens and triggering the success toast notification—but was followed by a 401 Unauthorized error when attempting to fetch user notifications. This prevented users from remaining logged in on Safari.

After a tutoring session with Code Institute, it was confirmed that this issue is caused by Safari's strict handling of third-party cookies, which affects token-based authentication when the front-end and back-end are hosted on different domains (as is the case with Heroku). Since the browser blocks cross-origin cookies, the refresh token cannot be stored or used correctly, leading to the login failure.

This issue is not caused by an error in the application’s code, and the functionality works as expected in modern browsers that do not block third-party cookies. Users are advised to access the site via Chrome or Firefox for full functionality.

[Back to Contents](#contents)

<h1 id="deployment">Deployment</h1>

This project was deployed to [Heroku](https://www.heroku.com/) in the projects early stages to allow continual responsive testing.

The website was deployed via Heroku by following these steps:

1. I cloned my GitHub repository by running `git clone https://github.com/BekMart/travel-api.git` in the terinal of VS Code.

2. In the Cloudinary dashboard, I navigated to `Settings` > `API Keys` and clicked `Generate New API Key` to obtain the `CLOUDINARY_URL` in the format `cloudinary://<your_api_key>:<your_api_secret>@dvgobcuck`.

3. I requested a Code Institute-hosted PostgreSQL database [here](https://dbs.ci-dbs.net/) and received my `DATABASE_URL` via email.

4. I generated a secret key from [Djecrety](https://djecrety.ir/) by clicking the `Generate` button on this site.

5. In `settings.py` file in VS code, I included the following:
- `if os.path.exists('env.py'):
    import env`

- `CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}`

- `SECRET_KEY = os.getenv('SECRET_KEY')`

- `DEBUG = False`

- `ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    os.environ.get("ALLOWED_HOST")
]`

- `CORS_ALLOWED_ORIGINS = [
  origin for origin in [
    os.environ.get('CLIENT_ORIGIN'),
    os.environ.get('CLIENT_ORIGIN_DEV'),
  ] if origin
]`

- `if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }`

6. I created an `env.py` file and added the following environment variables:

`import os`

`os.environ['CLOUDINARY_URL'] = '***The unique URL obtained from Cloudinary***'`

`os.environ['SECRET_KEY'] = '***The secret keyy  generated from Djecrety***'`

`os.environ['DEV'] = '1'`

`os.environ['DATABASE_URL'] = '***The PostgreSQL database URL recieved in the email***'`

`os.environ['CLIENT_ORIGIN'] = 'https://travel-tales-5c522e360995.herokuapp.com'`

`os.environ['CLIENT_ORIGIN_DEV'] = 'http://localhost:3000'`

7. I added `env.py` to `.gitignore` to ensure sensitive credentials were not committed.

8. I created a new app in Heroku by clicking `New` > `Create new app` in the dashboard. I named the app, selected Europe as my region and then clicked `Create app`.

9. Under `Settings` > `Reveal Config Vars`, I added:

| KEY | VALUE |
| --- | --- |
| ALLOWED_HOST | travel-api-ca880bcd8809.herokuapp.com |
| CLIENT_ORIGIN | https://travel-tales-5c522e360995.herokuapp.com |
| CLIENT_ORIGIN_DEV | http://localhost:3000 |
| CLOUDINARY_URL | ***the URL link copied from Cloudinary*** |
| DATABASE_URL | ***the PostgreSQL URL link copied from the email*** |
| DISABLE_COLLECTSTATIC | 1 |
| SECRET_KEY | ***value generated from Djecrety*** |

10. In the `Deploy` tab, I selected the option to `Connect the app to GitHub`, searched for my repository, and connected it.

11. I then scrolled to the `Manual Deploy` section at the bottom of the page. After ensuring the branch was set to `main`, I clicked `Deploy Branch`.

12. Once deployment completed successfully, I clicked `View` to open the deployed site.

[Back to Contents](#contents)

<h1 id="credits">Credits</h1>

### Acknowledgments

The initial setup and the general structure of this API are heavily based on Code Institute's [Django Rest Framework walkthrough project](https://github.com/Code-Institute-Solutions/drf-api/). Core elements such as the Profile, Post, Like, Comment, and Follower models, along with their corresponding serializers and filtering functionality, were adapted from the walkthrough. These components were then customized and extended to suit the unique requirements of the Travel Tales project.

I refrenced the following documentation to help with my understanding of Django and how to implement it within my project:
[Django documentation](https://www.djangoproject.com/)
[Django Rest Framework documentation](https://www.django-rest-framework.org/)
[django-filter documentation](https://django-filter.readthedocs.io/en/stable/)

I recieved help and guidance from the **CI Tutor support** team throughout this build and **ChatGPT** for assistancxe with troubleshooting and logic refinement.

[Back to Contents](#contents)
