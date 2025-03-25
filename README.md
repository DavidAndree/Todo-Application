Todo Application

## Author
David Alvarado

## Description

Created a Django Web Application with a single model to hold Todos and a single home / index page that will list out all of the Todos that have been entered via the admin. The home page should use Class-Based Views and extend a base template even though there is only one page. Once created, you will add testing to make sure the model and all pages work correctly.

The main non-admin page has be a list of all the Todos and the date that they should be completed by. Additionally there are some buttons (as links) for add, edit, and delete that will take the user to the corresponding admin page for that functionality. 


Make sure you have a `requirements.txt` file with your required packages. 

### Database 
I have included an ERD (Entity Relationship Diagram) that shows the database tables. 

![Database Entity Relationship Diagram](https://barnesbrothers.net/cis218/assignment_images/assignment_2/cis218_assignment_2_erd.png "Database Entity Relationship Diagram")


![Todo Page Screenshot](https://barnesbrothers.net/cis218/assignment_images/assignment_2/cis218_assignment_2_screenshot.png "Todo Page Screenshot")



<br>https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#length

In order to be able to link to certain pages within the admin, you can look at the following page it might help
<br>https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls