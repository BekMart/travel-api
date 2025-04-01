# TravelTales API

The TravelTales API is a Django REST Framework API that powers a social content-sharing application built for travellers. It allows users to share blog-style posts about their favourite travel destinations, including photos and written content. Other users can log in to like, comment on, and follow profiles, making it a platform for both inspiration and connection.

While developed specifically for the [TravelTales app](), the API architecture is flexible enough to be adapted for other content-based or community-driven platforms.

The API supports secure user authentication, photo uploads, content creation, and real-time user engagement features such as likes, comments, follows, and notifications.

## Key Features:
- User authentication
- Users can create and customise their profiles
- Authenticated users can create, edit, or delete posts
- Posts can be tagged with travel destinations (locations)
- Users can comment on and like posts
- Users can follow one another
- Users receive notifications when someone likes, comments, or follows them
- Users can search and filter posts by destination, profile and title

The deployed API can be fund here: [TravelTales API]()

<h1 id="contents">Table of Contents</h1> 

- [Design Process](#design-process)
    - [User Stories](#user-stories)
    - [Data Models](#data-models)
- [Agile Development](#agile-development)
    - [Kanban Board](#kanban-board)
- [API Endpoints](#api-endpoints)
- [Features](#features)
    - [Existing features](#existing-features)
    - [Future Feature Ideas](#future-features)
- [Technologies Used](#technologies)
    - [Frameworks and Languages](#frameworks-langugages)
    - [Additional packages](#additional-packages)
    - [Other Software](#other-software)
- [Testing](#testing)
- [Deplloyment](#deployment)
- [Credits](#credits)

<h1 id="design-process">Design Process</h1>

<h2 id="user-stories">User Stories</h2>

User stories for the API were written from a developer's perspective, focusing on the needs of both first-time and returning users, and ensuring the data models and API structure supported their actions effectively.

<h2 id="data-models">Data Models</h2>

A simple but effective Entity Relationship Diagram (ERD) was created to visualise the relationships between the models. This guided the API structure and ensured clear, logical connections between user actions and data representation.

![This is the ERD which was created to show the database structure and the relationships held between the different models]()

### Profile Model
Represents user profile data, extending the default User model with a one-to-one relationship. Includes fields for name, bio, and profile image. Profiles are automatically created when a user registers.

### Post Model
The central content model. Authenticated users can create posts with titles, captions, images, and a linked Location. Posts appear on the home page and on the user’s profile.

### Comment Model
Allows users to comment on any post. Users can also edit or delete their own comments.

### Like Model
Users can like or unlike any post. Each user can only like a post once.

### Followers Model
Creates a connection between two users — the owner is following the followed user. Enables social feed potential and profile connections.

### Location Model
A list of travel destinations. Posts are linked to a location via a ForeignKey. Each location has a slug for SEO-friendly URLs and can optionally include a description and image. Enables filtering and destination-specific pages.

### Notification Model
Notifies users of activity related to them, including likes, comments, and follows. Stores sender (from_user), recipient (to_user), type (like, comment, follow), and whether the notification has been read.

<h1 id="agile-development">AgileDevelopement</h1>

<h2 id="kanban-board">Kanban Board</h2>

For this project, I used a Kanban board in GitHub as an agile tool to visualise my workflow, organise tasks, and maintain steady progress throughout development. This approach helped streamline processes, identify bottlenecks, and prioritise tasks effectively.

- A single GitHub Project was created to manage both the TravelTales back-end and front-end development.
- I used GitHub Issues to represent individual user stories.
- Each user story was grouped into an Epic for better organisation.
- Issues were categorised using the MoSCoW prioritisation technique:
    - Must Have, Should Have, Could Have, and Won’t Have.
- Milestones and the Project Roadmap were used to support effective time management and iterative delivery.
![An image of the issues all set out in the Project Roadmap, completed using Milestones]()
- The Kanban board was divided into three clear stages:
    - To Do, In Progress, and Done.

![Screenshot of my kanban board]()
