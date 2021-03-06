from django.urls import path

from .views import (
    index,
    record_add,
    record_update,
)

urlpatterns = [
    path('', index, name='record-list'),  # URL для отображения списка записей
    path('product/add', record_add, name='record-add'),
    path('product/<int:pk>/edit', record_update, name='record-update'),
    # path('add/', article_create_view, name='article-add'),  # URL для отображения формы и создания статьи
    # path('<int:pk>/', article_view, name='article-view'),  # URL для просмотра деталей статьи. Обратите внимание, URL использует целочисленный параметр id
    # path('<int:pk>/update', article_update_view, name='article-update'),  # URL для отображения формы и редактирования статьи
    # path('<int:pk>/delete', article_delete_view, name='article-delete')  # URL для отображения формы подтверждения и удаления статьи
]
