from django.urls import path, include
import crawler.urls

app_name = "core"

urlpatterns = [
    path('', include(crawler.urls, namespace='crawler')),
]
