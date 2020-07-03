from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from crypto.sitemaps import PostSitemap , StaticViewSitemap
from crypto import views as crypto_views
sitemaps = {
    'post':PostSitemap,
    'static': StaticViewSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('post/<int:id>', crypto_views.post, name='post'),
    path('map',crypto_views.map, name='map'),
    path('', include('crypto.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),

]
