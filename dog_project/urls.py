from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pets.views import home, adopt_dog, success_stories  # Import the new view!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('adopt/<int:dog_id>/', adopt_dog, name='adopt_dog'),
    path('adopted/', success_stories, name='success_stories'), # New Link
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)