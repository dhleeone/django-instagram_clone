from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # feed에 있는 모든 데이터를 가져온다.(쿼리셋 = select * from content_feed)

        return render(request, "leestagram/main.html", context=dict(feeds=feed_list))

