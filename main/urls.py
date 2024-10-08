from django.contrib import admin
from django.urls import path
from main.views import show_main, create_new_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, delete_product, edit_product, show_product, show_product_by_category, add_new_product_ajax

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main, name="show_main"),
    path("create-new-product", create_new_product, name="create_new_product"),
    path("xml/", show_xml, name="show_xml"), 
    path("json/", show_json, name="show_json"),
    path("xml/<str:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:id>/", show_json_by_id, name="show_json_by_id"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("delete/<uuid:id>", delete_product, name="delete_product"),
    path("edit/<uuid:id>", edit_product, name="edit_product"),
    path("show_product/", show_product, name="show_product"),
    path("show_product/<str:category>/", show_product_by_category, name="show_product_by_category"),
    path("create-new-product-ajax", add_new_product_ajax, name="add_new_product_ajax"),
]