from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from .models import Transaction

def home(request):
    User = get_user_model()
    user_count = User.objects.count()
    return render(request, 'tracker/home.html', {'user_count': user_count})


@login_required
def expense_dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('expense_dashboard')
    else:
        form = TransactionForm()
    return render(request, 'tracker/expense_dashboard.html', {'form': form, 'transactions': transactions})