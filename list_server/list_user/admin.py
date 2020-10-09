from django.contrib import admin, auth

admin.site.unregister(auth.models.Group)
