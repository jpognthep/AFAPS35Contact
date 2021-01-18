from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def test_vue(request):
    return render(request, 'abc.html')
