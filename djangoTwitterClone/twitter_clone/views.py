from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.loader import get_template

from twitter_clone.models import Tweet
from twitter_clone.forms import TweetForm

class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class TimelineView(View):
    template_name = 'timeline.html'

    def get(self, request, *args, **kwargs):
        tweets = Tweet.objects.filter(user_id=request.user.id).order_by('-created_at')
        return render(request, self.template_name, { 'tweets': tweets })


@method_decorator(login_required, name='dispatch')
class NewTweetView(View):
    template_name = 'new_tweet.html'
    model = Tweet

    def get(self, request, *args, **kwargs):
        form = TweetForm()
        return render(request, self.template_name, { 'form': form })

    def post(self, request, * args, **kwargs):
        Tweet(text=request.POST['text'], user_id=request.user.id).save()
        return HttpResponseRedirect('/timeline')
