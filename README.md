# Django Docker App

This project demonstrates how to run a Django application inside a Docker container using Docker Compose. It includes automatic project creation if one does not exist.

## Features
- Django runs in a containerized environment
- Automatic `django-admin startproject` if `manage.py` is missing
- Hot-reloading with volume mounts
- Easy setup and teardown

## Project Structure
```
├── app/                   # Django project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── firstapp/           # Example Django app (created by you)
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations/
│       ├── models.py
│       ├── tests.py
│       ├── views.py        # Your app's views
│       └── urls.py         # Your app's URLs
├── Dockerfile              # Docker build instructions
├── docker-compose.yml      # Docker Compose configuration
├── entrypoint.sh           # Entrypoint script for auto project creation
├── requirements.txt        # Python dependencies
└── manage.py               # Django management script (created automatically)
```

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
