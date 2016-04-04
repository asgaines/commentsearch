import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from commentsearch import settings
from comments.models import Comment


class Command(BaseCommand):
    help = 'Collects the comments on the page linked and stores in database'

    def handle(self, *args, **kwargs):
        # Feed HTML from web page into parser
        soup = BeautifulSoup(requests.get(settings.REVIEW_ARTICLE_LINK).text, 'html.parser')

        # Clear old comments
        for comment in Comment.objects.all():
            comment.delete()

        # Loop through all comments on page and feed into database
        for comment in soup.find_all(attrs={'class': 'comment'}):
            try:
                # Id set by site comment system ensures uniqueness and updating after editing
                id = int(comment['id'].split('-')[-1])
            except Exception as e:
                raise CommandError('{0}, {1}'.format(e.message, e.args))

            try:
                author = comment.find('cite').text
            except Exception as e:
                raise CommandError('{0}, {1}'.format(e.message, e.args))

            try:
                body = comment.find(attrs={'class': 'comment-body'}).text
            except Exception as e:
                raise CommandError('{0}, {1}'.format(e.message, e.args))

            # Build new comment object from scraped data
            c = Comment(pk=id, author=author, body=body)
            
            try:
                c.save()
            except Exception as e:
                raise CommandError('{0}, {1}'.format(e.message, e.args))

        self.stdout.write(self.style.SUCCESS('{0} comments successfully collected to database'.format(Comment.objects.count())))
