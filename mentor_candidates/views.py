from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Mentor

def detail(request, mentor_id):
    mentor = get_object_or_404(Mentor, pk=mentor_id)
    # try:
    #     mentor = Mentor.objects.get(pk=mentor_id)
    # except Mentor.DoesNotExist:
    #     raise Http404("Mentor does not exist")
    return render(request, 'mentor_candidates/detail.html', {'mentor': mentor})

def opinion(request, opinion_id):
    return HttpResponse("You're voting on opinion %s." % opinion_id)



def index(request):
    mentor_list = Mentor.objects.all()
    # template = loader.get_template('mentor_candidates/index.html')
    context = {
        'mentor_list': mentor_list,
    }
    return render(request, 'mentor_candidates/index.html', context)
    # return HttpResponse(template.render(context, request))