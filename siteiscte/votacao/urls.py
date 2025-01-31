from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'votacao'

urlpatterns = [

 # ex: votacao/
 path("", views.index, name='index'),

 # ex: votacao/1
 path('<int:questao_id>', views.detalhe,name='detalhe'),

 # ex: votacao/3/resultados
 path('<int:questao_id>/resultados', views.resultados, name='resultados'),

 # ex: votacao/5/voto
 path('<int:questao_id>/voto', views.voto, name='voto'),

 # ex: votacao/createquestion
 path('createquestion', views.createquestion, name='createquestion'),

 # ex: votacao/5/createoption
 path('<int:questao_id>/createoption', views.createoption, name='createoption'),

 path('userlogin', views.userlogin, name="userlogin"),

 path('userregister', views.userregister, name="userregister"),

 path('logoutview', views.logoutview, name="logoutview"),

 path('userdetails', views.userdetails, name="userdetails"),

 path('<int:questao_id>/deletequestion', views.deletequestion, name="deletequestion"),

 path('<int:questao_id>/deleteoption', views.deleteoption, name="deleteoption"),

 path('fazer_upload', views.fazer_upload, name='fazer_upload')
]

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


