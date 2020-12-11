# Note that once we’ve done this in all these views,
# we no longer need to import loader and HttpResponse
# (you’ll want to keep HttpResponse if you still have
# the stub methods for detail, results, and vote).

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# There’s also a get_list_or_404() function,
# which works just as get_object_or_404()
# – except using filter() instead of get().
# It raises Http404 if the list is empty.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)