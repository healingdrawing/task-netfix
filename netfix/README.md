# Task Netfix

grit:lab Åland Islands 2023  
Authors: [@healingdrawing](https://github.com/healingdrawing)

## Requirements

python3 django4.2

## Details

The database `db.sqlite3` not provided in this repository.  
The database migrations was removed.  
So that stuff will be recreated once by steps bottom.  
Depends on your environment use `python` or `python3` terminal command prefix.

## Make these steps once before use development server:

- Clone this repository
- Open(using ide) the project folder where placed the `manage.py` file. The terminal should be opened in this folder too, to prevent extra terminal `cd netfix` navigations etc.  
  Or just open the terminal in the folder where placed the `manage.py` file.
- terminal: `python -m pip install django==4.2`  
   This version of Django was used to develop this project. Or if you prefer adventures you can try to use the latest version of Django, `python -m pip install django`.
- terminal: `python manage.py makemigrations`  
  This command will create the migrations for the database.
- terminal: `python manage.py migrate`
  This command will apply the migrations to the database.

## Use development server steps:

- terminal: `python manage.py runserver`  
  After that you can open the browser and go to the `http://127.0.0.1:8000/` or just press `Ctrl` + `click` on the link in the terminal.  
  The web application will be available locally.
- to stop the development server press `Ctrl` + `C` in the terminal.

## Conclusion

The `settings.py` file still includes the `SECRET_KEY` and `DEBUG = True` settings, so `DO NOT USE THIS PROJECT IN PRODUCTION` or you will be punished, f.e. temporary ban on pythonanywhere.com (tested personally).  
About details you need discover the Django documentation.
