from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="expense"),
    path('add-expense/', views.add_expense, name="add-expense"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('search-expense/', csrf_exempt(views.search_expenses),
         name="search_expenses"),
    path('expense_category_summary/', views.expense_category_summary,
         name="expense_category_summary"),
    path('expensestats/', views.expensestats_view,
         name="expensestats")
]