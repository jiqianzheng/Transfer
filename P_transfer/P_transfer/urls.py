from django.contrib import admin
from django.urls import path
from Annotation import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^classify$', views.classify, name='classify'),
    url(r'^classify_show',views.classify_show,name='classify_show'),

    url(r'^upload/classify$', views.get_classify_image, name="upload_classify"),

    url(r"^classify/process/$", views.process_classify, name="process_classify"),
    # url(r"^classify/process/$", views.classify_result, name="process_classify"), # 跳转到新页面，已放弃
    url(r'^classify/process/1_by_1$', views.process_classify_1_by_1, name="process_classify_1_by_1"),



    url(r'^show$', views.show, name="show"),

]
