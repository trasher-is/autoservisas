# autoservisas

## First commit
added lessons 1 to 8 all together

### lesson 8
- added user field to order's model
- added returned date field to order's model
- added both fields to admins page
- added @property method to display due date
  - added @property to two calculation functions in models
- added links to menu, added tinymce field to automobilis model
- various small css fixes and html cleanup

## lesson 9
- added user registration ability
  - user registration form
  - register view function and template
- fixed css styling of login and pass reset forms
- added ability for user to leave comments on his orders
    - created review form
    - created review model
    - added reviews to orders page
    - some css styling
- some css and html cleanup

## lesson 10
- added user profile
  -ability to change name
  -ability to change email
  -abiliety to chamge profile picture
- added signals.py to check if user is created and save his profile and to check if profile is created to save user
- model for profile added
- profile update form added
- added profile pictures to orders comments
- only user who's order can comment and admin
  - admin can comment on all orders
  - admins comments are css aligned right
- added profile picture to 'automobilis' template (bad css styling need to learn how to do that without absolute positioning)
