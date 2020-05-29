from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from first_app.views import HomeView
from first_app import views

app_name='link'

urlpatterns=[
    url(r'^$',views.index, name='home'),
    url(r'^friends', HomeView.as_view(),name='first_app'),
    url(r'^home/$',views.index, name='home'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^signin/$',views.signin, name='signin'),
    url(r'^login2/$',views.login2, name='signin2'),
    url(r'^signup2/$',views.signup2, name='signup2'),

    url(r'^logout/$',views.user_logout, name='logout'),
    url(r'^navbar/$',views.navbar, name='navbar'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^update/$',views.profile_update, name='profile_update'),
    url(r'^feed/$',views.feed, name='feed'),
    url(r'^friend/$',views.Friend_profile, name='Friend_profile'),

    # url(r'^posts/$',views.posts, name='posts'),
    url(r'^posts/(?P<post>.+)/(?P<pk>\d+)/$', views.posts, name='posts'),

    url(r'^profee/(?P<proo>.+)/(?P<pk>\d+)/$', views.profee, name='profee'),

    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),

    url(r'^post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    # url(r'^signupw/$',views.signupw, name='signupw'),
    # url(r'^signin/$',views.signin, name='signin'),
    # url(r'^content/$',views.content, name='content'),
    # url(r'^postad/$',views.adposting, name='postad'),
    # url(r'^show_ads/$',views.show_ads, name='show'),
    # url(r'^addetails/$',views.addetails, name='addetails'),
    # url(r'^user_login/$',views.user_login, name='user_login'),
    # url(r'^hell/$',views.hell, name='hell'),
    # url(r'^aiding/$',views.aiding, name='aiding'),
    # url(r'^Divission/$',views.divissionadd, name='divissionadd'),
    # url(r'^search/$',views.search, name='search'),
    # url(r'^tattadaa/$',views.tattadaa, name='tattadaa'),

]
