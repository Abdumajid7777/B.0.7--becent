from django.urls import path

from main.views import (
    main, about,

    create_product, product_detail, update_product,
    # group_detail, update_group, create_group,
    # create_teacher, teacher_detail, update_teacher
)

urlpatterns = [
    path("", main, name="main"),
    path("about/", about, name="about"),

    # ===== Students =====
    path("product-create/", create_product, name="create_product"),
    path("product-detail/<int:id>/", product_detail, name="product_detail"),
    path("product-update/<int:id>/", update_product, name="update_product"),

    # # ===== Groups =====
    # path("group-create/", create_group, name="create_group"),
    # path("group-detail/<int:id>/", group_detail, name="group_detail"),
    # path("group-update/<int:id>/", update_group, name="update_group"),

    # # ==== Teacher =====

    # path("teacher-create/", create_teacher, name="create_teacher"),
    # path("teacher-detail/<int:id>/", teacher_detail, name="teacher_detail"),
    # path("teacher-update/<int:id>/", update_teacher, name="update_teacher"),
]