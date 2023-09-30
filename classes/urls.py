from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListClasses, name='class_list'),
    path('add_class/', views.AddClasses, name='class_add'),
    path('edit_class/<str:class_name>/', views.UpdateClasses, name='class_update'),
    path('delete_class/<str:class_name>/', views.DeleteClasses, name='class_delete'),
    path('create_section/<str:class_name>', views.SectionAdd, name='section_add'),
    path('list_section/',views.SearchClassToSeeSection,name='section_search'),
    path('list_section/<str:class_name>', views.SectionList, name='section_list'),
    path('delete_section/<str:class_name>/<str:section_name>',views.SectionDelete,name='section_delete'),
    path('update_section/<str:class_name>/<str:section_name>',views.SectionUpdate,name='section_update'),

    # Add other URL patterns as needed
]