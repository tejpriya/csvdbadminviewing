from exports import views
from django.urls import path,include

urlpatterns = [
    path('wxport',views.export_data),
    path('import',views.import_data),
]