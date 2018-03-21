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
    #url(r'^about/$', views.about, name='about'),
    url(r'^contact-us/$', views.contact, name='contact'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^tattoos/$', views.tattoos, name='tattoos'),
    url(r'^upload/$', views.user_post, name='upload'),
    url(r'^success/$', views.successView, name='success'),
    url(r'^test/$', views.submit_comment, name='test'),

]
