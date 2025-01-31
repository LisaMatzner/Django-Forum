# Django-Forum
Small Django forum project

Project: Simple Forum

- Models:
	- Thread: pk/id, description/name, author → fk (user), date opened at, flag/topic, last edited, 	closed(bool), closed at
	- Post/Comments: pk/id, fk → thread, author (user) fk, date posted, date edited, text, likes, 	(views)
	- User: id, email, username, display_name, number od posts, password, date joined, 	days_since_join (calculation), (lvl), Imagefield → avatar

- Views:

Thread
- list_view
- detail view
- create view
- update view
- delete view

Comments
- create view
- update view
- delete view
- list view
- detail view

User
- detail view
- create view
- update view
- delete view


Authentication
login View, logout view, register
restrictions for actions


Optional 
Styling (CSS etc)
Searchbar (regex?) → Views
Topics
Views
Profile Pic/Avatar
Implement Pics in Comments
