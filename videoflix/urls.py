from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from users.views import LoginView, RegisterView
from video.views import VideosViews
from videoflix import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', VideosViews.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
