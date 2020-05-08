from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('games/', views.GameListView.as_view(), name = "games"),
    path('game/<int:pk>', views.GameDetailView.as_view(), name = "game-detail"),
    path('authors/', views.AuthorListView.as_view(), name = "authors"),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name = "author-detail"),
    path('mygames/', views.LoanedGamesByUserListView.as_view(), name = 'my-borrowed'),
    path('art/', views.View.as_view(), name = 'art'),
    path("page1/", views.page1, name = "page"),
    path("page2/", views.page2, name = "also page"),
    path("stolen_page1/", views.stolen_page1, name = "page, again"),
    path("stolen_page2/", views.stolen_page2, name = "jusst page"),
    path("game/<uuid:pk>/renew", views.renew_game_librarian, name = "renew-game-librarian"),
    path("author/create/", views.AuthorCreate.as_view(), name = "author_create"),
    path("author/<int:pk>/update/", views.AuthorUpdate.as_view(), name = "author_update"),
    path("author/<int:pk>/delete/", views.AuthorDelete.as_view(), name = "author_delete"),

    ]
