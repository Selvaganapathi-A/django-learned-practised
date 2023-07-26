from django.urls import path

from . import views


# Put app name here
app_name: str = "app02"
# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    #
    path("view/basic-view/", views.BasicView.as_view(), name="basic-view"),
    path(
        "view/template-view/",
        views.ArticleAuthorList.as_view(),
        name="template-view",
    ),
    #
    path(
        "temporary-redirect/<term>",
        views.TemporaryRedirect.as_view(),
        name="temporary-redirect",
    ),
    path(
        "permenant-redirect/",
        views.PermenantRedirect.as_view(),
        name="permenant-redirect",
    ),
    #
    path(
        "complaint/",
        views.CustomerComplaints.as_view(),
        name="customer-complaint",
    ),
    # # list view
    # path("article/list", views.ArticleList.as_view(), name="article-list"),
    # # Detail view
    # path(
    #     "article/detail/<int:pk>",
    #     views.ArticleDetail.as_view(),
    #     name="article-detail",
    # ),
    # # Author
    # # display views
    # path("author/list", views.AuthorList.as_view(), name="author-list"),
    # path(
    #     "author/detail/<int:pk>/",
    #     views.AuthorDetail.as_view(),
    #     name="author-detail",
    # ),
    # # edit views
    # path(
    #     "author/create/",
    #     views.AuthorCreate.as_view(),
    #     name="author-create",
    # ),
    # path(
    #     "author/update/<int:pk>/",
    #     views.AuthorUpdate.as_view(),
    #     name="author-update",
    # ),
    # path(
    #     "author/delete/<int:pk>/",
    #     views.AuthorDelete.as_view(),
    #     name="author-delete",
    # ),
]
