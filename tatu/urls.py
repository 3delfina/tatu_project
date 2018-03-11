from django.conf.urls import url
from tatu import views

#PAGES TO BE CREATED. 
#home
#contact-us
#FAQ
#create-account
#login
#login/profile
#login/profile/uploads
#login/profile/favourites
#artists
#artists/artist-page
#artists/artist-page/rate-this-artist
#tattoos
#tattoos/traditional
#tattoos/realism etc...

urlpatterns = [
    url(r'^$', views.index, name='index'),  # home page
    url(r'^about/$', views.about, name='about'),
    url(r'^contact-us/$', views.about, name='contact-us'),
    url(r'^FAQ/$', views.about, name='FAQ'),
    url(r'^register/$', views.about, name='register'),
    url(r'^login/$', views.about, name='login'),
    url(r'^artists/$', views.about, name='artists'),
    url(r'^tattoos/$', views.about, name='tattoos'),
]
