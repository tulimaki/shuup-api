# REST API

Shuup API has a powerful API to enable users to access and modify data through endpoints. Users can create several applications to consume the API, from mobile applications to virtual reality devices and whatever platform capable of making HTTP requests.

The Shuup REST API is built on [**Django REST Framework**](http://www.django-rest-framework.org/) with additional functionality built on top of Shuup Provides to auto-discover available API endpoints.

## Setting up the Shuup REST API

First, add `rest_framework` and `shuup_api` to your `INSTALLED_APPS`.

Then -- and this differs from Django REST Framework's defaults -- you *must* add
the `REST_FRAMEWORK` configuration dict to your settings.  Django REST Framework
defaults to no permission checking whatsoever (`rest_framework.permissions.AllowAny`),
which would make all of your data world-readable and writable.

This is not what we want to accidentally happen, so configuration is enforced.

Add the following to your project `setting.py`:

```py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'shuup_api.permissions.ShuupAPIPermission',
    )
}
```

Now just add the API to your root urlconf.

```py
   urlpatterns = [
       # ...
       url(r'^api/', include('shuup_api.urls')),
   ]
```

All done! If you visit the `/api/` URL (as a suitably authenticated user), you should be
presented with Django REST Framework's human-friendly user interface.

## Permissions

You can configure the access level of your API through Shuup Admin panel for each endpoint at **Settings > Permissions > API**.

In order to make it work properly, make sure the permission class `shuup_api.permissions.ShuupAPIPermission` is
in the DRF `DEFAULT_PERMISSION_CLASSES` setting.

Our permission class will read your configuration set through admin and will apply it on the selected endpoints.

**Important**: Not only the access of the endpoint will be restricted but also the API documentation it provides will be restricted.

The available access levels are:

- **Disabled** - No one can make requests.
- **Admin users** (default) - Only administrators can make requests to the API to fetch, save, delete or update data.
- **Authenticated users - Read/Write** - Any authenticated user can fetch, save, delete or update data.
- **Authenticated users - Read** - Any authenticated user can only fetch data.
- **Public users - Read/Write** - Any user (authenticated or not) can fetch, save, delete or update data. Use this with caution.
- **Public users - Read** - Any user (authenticated or not) can only fetch data. Use this with caution.

## API Documentation

As the API is built with Django REST Framework (DRF), you can visit the `/api/` URL to access the browseable API using the default
DRF interface, but only if `rest_framework.renderers.BrowsableAPIRenderer` is in the `DEFAULT_RENDERER_CLASSES` setting, which is the default.

Alongside with the default browseable API, we can see the complete API documentation with URLs, methods and parameters on-the-fly using [**Django REST Swagger**](https://github.com/marcgibbons/django-rest-Swagger). You can access the interactive API documentation at your development server or even at a production one.

To see that, just make sure the application `rest_framework_swagger` is in your `INSTALLED_APPS`.

Visit the `/api/docs/` URL on your browser and it is done. You should see the available APIs endpoints, their descriptions, methods and parameters.
