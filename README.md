# CommentSearch

Search through all comments posted to [this web page](http://www.dcrainmaker.com/2015/01/stryd-first-running.html) for search terms submitted through this site. Display the comments which matched at least one of the comma-delimited search terms.

## How to Use Site

- Access site [here](https://commentsearch.herokuapp.com)
- Enter desired search terms, delimited by commas (e.g. `run`, `stryd, power`, `measure,meter`, etc)
- Submit query and see the matching comments displayed on page

## Cloning Project

- Ensure Python, git are installed locally
- Install [heroku](https://www.heroku.com) and the accompanying toolbelt
- Install [pip](https://pip.pypa.io/en/stable/installing/)
- `cd` into directory of choice
- Run `git clone https://github.com/asgaines/commentsearch.git my_directory`
- Run `pip install -r requirements.txt` to install required Python packages
- Login to heroku by running `heroku login`
- Run `heroku create my_site_name`
- Run `python manage.py collect_comments` to update the comments from the review website
- Run `heroku local` to view local state of application
- Follow deployment steps to update production site at url returned by running `heroku create my_site_name`

