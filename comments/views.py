import re

from django.db.models import Q
from django.shortcuts import render

from commentsearch import settings
from comments.models import Comment

def index(request):
    comment_matches = []
    success_submit = False

    if request.method == 'POST':
        if request.POST.get('search-terms').strip():
            search_terms = [term.strip() for term in request.POST.get('search-terms').split(',')]

            # Original implementation, unsure if in violation of Criteria point #2 (uses Django ORM framework for SQL generation)
            # comment_matches = Comment.objects.filter(reduce(lambda x, y: x | y, [Q(body__icontains=term) for term in search_terms]))
    
            # To play it safe, here is my own implementation
            # Splits strings up based on: whitespace | hyphen | forward slash | period | ampersand | comma
            # Done for substring matching purposes
            comment_matches = set([comment for comment in Comment.objects.all() for term in search_terms if term.lower() in [word.lower().strip('.?!:"(){}[],') for word in re.split('\s|-|,|/|\.|&|,', comment.body)]])

            success_submit = True

    context = {'success_submit': success_submit, 'comment_matches': comment_matches, 'link': settings.REVIEW_ARTICLE_LINK}
    return render(request, 'comments/index.html', context)
