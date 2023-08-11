from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Sum
from income.models import Income
from expense.models import Expense

def savings_table(request):
    income_expenses = []

    income_by_month = Income.objects.values('date__year', 'date__month').annotate(total_income=Sum('amount'))
    expense_by_month = Expense.objects.values('date__year', 'date__month').annotate(total_expense=Sum('amount'))

    for income in income_by_month:
        year = income['date__year']
        month = income['date__month']
        total_income = income['total_income']

        expense_entry = expense_by_month.filter(date__year=year, date__month=month).order_by('total_expense').first()    
        total_expense = expense_entry['total_expense'] if expense_entry else 0

        savings_amount = total_income - total_expense

        if total_income == 0 and total_expense > 0:
            savings_amount = -total_expense

        income_expenses.append({'year': year, 'month': month, 'savings_amount': savings_amount})

    for expense in expense_by_month:
        year = expense['date__year']
        month = expense['date__month']
        if not any(entry['year'] == year and entry['month'] == month for entry in income_expenses):
            total_expense = expense['total_expense']
            savings_amount = -total_expense
            income_expenses.append({'year': year, 'month': month, 'savings_amount': savings_amount})

    income_expenses.sort(key=lambda x: (x['year'], x['month']))

    paginator = Paginator(income_expenses, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'savings/savings_table.html', context)
