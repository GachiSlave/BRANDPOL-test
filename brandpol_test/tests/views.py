from django.shortcuts import render, redirect
from .models import Tests, Questions
from .forms import TestsForm, QuestForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.


def tests_home(request):
    tests = Tests.objects.all()
    return render(request, 'tests/tests_home.html', {'tests': tests})

def create_quest(request, pk):
    error = ''
    if request.method == 'POST':
        #a = Questions.objects.get(test=pk)
        #form = QuestForm(request.POST, instance=a)
        #a = Questions(test_id=pk, question_text=request.POST['question_text'])
        Questions.objects.create(question_text=request.POST['question_text'], test_id = pk)
    form = QuestForm()
    data = {
        'form': form,
        'test_id': pk,
        'error': error
    }
    return render(request, 'tests/create_question.html', data)
class TestDetailView(DetailView):
    model = Tests
    template_name = 'tests/details_view.html'
    context_object_name = 'test'

class TestUpdateView(UpdateView):
    model = Tests
    template_name = 'tests/create_test.html'

    form_class = TestsForm

class TestDeleteView(DeleteView):
    model = Tests
    success_url = '/tests/'
    template_name = 'tests/test_delete.html'

def create_test(request):
    error = ''
    if request.method == 'POST':
        form = TestsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'
    form = TestsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tests/create_test.html', data)