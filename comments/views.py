from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from commentsearch import settings
from comments.models import Comment

def index(request):
    comment_matches = []
    if request.method == 'POST':
        search_terms = [term.strip() for term in request.POST.get('search-terms').split(',')]
        comment_matches = Comment.objects.filter(reduce(lambda x, y: x | y, [Q(body__icontains=term) for term in search_terms]))
    context = {'method': request.method, 'comment_matches': comment_matches, 'link': settings.REVIEW_ARTICLE_LINK}
    return render(request, 'comments/index.html', context)
