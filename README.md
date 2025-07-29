# Django Docker App

This project demonstrates how to run a Django application inside a Docker container using Docker Compose. It includes automatic project creation if one does not exist.

## Features
- Django runs in a containerized environment
- Automatic `django-admin startproject` if `manage.py` is missing
- Hot-reloading with volume mounts
- Easy setup and teardown

## Project Structure
```
├── app/                      # Django project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py
│   └── firstapp/              # Example Django app
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py           # Django forms for Reservation
│       ├── migrations/
│       ├── models.py          # MenuItem and Reservation models
│       ├── tests.py
│       ├── views.py           # Views for hello, GreetingView, home (reservation)
│       └── urls.py            # URL patterns for firstapp
├── Dockerfile                 # Docker build instructions
├── docker-compose.yml         # Docker Compose configuration (web, db, phpmyadmin)
├── entrypoint.sh              # Entrypoint script for auto project creation
├── requirements.txt           # Python dependencies (include mysqlclient)
└── manage.py                  # Django management script (created automatically)
```
## Models, Forms, and Views

**Models:**
- `MenuItem`: Stores menu items with name and price.
- `Reservation`: Stores reservation details (first name, last name, guest count, reservation time, comments).

**Forms:**
- `ReservationsForm`: Django ModelForm for creating reservations.

**Views:**
- `hello`: Returns a simple hello message.
- `GreetingView`: Returns a greeting message.
- `home`: Handles reservation form display and submission.

## Database and Admin

- Uses MySQL as the database (configured in `settings.py`).
- phpMyAdmin is available at [http://localhost:8080](http://localhost:8080) for database management.

## Running the Project

1. Build and start all services:
   ```
   docker-compose up --build
   ```
2. Run migrations:
   ```
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```
3. Access Django at [http://localhost:8000](http://localhost:8000)
4. Access phpMyAdmin at [http://localhost:8080](http://localhost:8080)

## Notes
- Make sure `mysqlclient` is in your `requirements.txt` for MySQL support.
- All Django management commands should be run inside the container using `docker-compose exec web ...`.

## Working with Django Apps (e.g., firstapp)

A Django app (like `firstapp`) is a modular component that lives inside your Django project directory (e.g., `app/firstapp/`).

### Why create apps?
Apps make your Django project modular, reusable, and easier to maintain. Each app can be developed and tested independently, then plugged into your main project.

### Step-by-step: Creating and Registering an App

1. **Create a new app**
   ```
   docker-compose exec web python manage.py startapp firstapp
   ```
   This creates the `app/firstapp/` directory with default files.

2. **Add a view in your app**
   Edit `app/firstapp/views.py` and add:
   ```python
   from django.http import HttpResponse

   def hello(request):
       return HttpResponse("Hello from firstapp!")
   ```

3. **Add a URL pattern in your app**
   Create or edit `app/firstapp/urls.py`:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('function/', views.hello),
   ]
   ```

4. **Include your app's URLs in the main project**
   Edit `app/urls.py` and add:
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('app/', include('firstapp.urls')),
   ]
   ```

5. **Register your app in settings**
   Edit `app/settings.py` and add `'firstapp',` to the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       # ...
       'app',
   ]
   ```

Now, visiting `http://localhost:8000/app/function/` will show your view's response.

## How it Works
- The `entrypoint.sh` script checks if `manage.py` exists. If not, it runs `django-admin startproject app .` to create a new Django project.
- The `Dockerfile` sets up the Python environment, installs dependencies, and uses the entrypoint script.
- `docker-compose.yml` defines the `web` service, mounts your code, and exposes port 8000.

## Usage

### 1. Build and Start the App
```
docker-compose up --build
```
- On first run, this will create a new Django project if one does not exist.
- The app will be available at http://localhost:8000

### 2. Stopping the App
```
docker-compose down
```

### 3. Running Django Commands
You can run Django management commands inside the container:
```
docker-compose exec web python manage.py migrate
```

### 4. Customizing the Project Name
- By default, the project is named `app`. To change this, edit `entrypoint.sh` and update the `django-admin startproject` line.

## Notes
- If you already have a Django project, the script will not overwrite it.
- To start fresh, delete `manage.py` and the `app/` directory, then run `docker-compose up --build` again.

## License
MIT
