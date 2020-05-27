from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import BookModelFormset
from .models import Book

from django.shortcuts import render, redirect

from .forms import BookModelFormset

def create_book_model_form(request):
    template_name = 'create_normal.html'
    heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        # we don't want to display the already saved model instances
        formset = BookModelFormset(queryset=Book.objects.none())
    elif request.method == 'POST':
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('name'):
                    form.save()
            return redirect('testform:book_list')
    return render(request, template_name, {
            'formset': formset,
            'heading': heading_message,
            })
