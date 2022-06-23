from django.urls import path

from . import views

urlpatterns=[
    path("",views.index, name="home"),
    path("generator/",views.entries_view, name="generator"),
    path("generated/",views.generated_view, name="generated"),
    path("stories/",views.story_view, name="stories"),
    path("storiesDatabase/",views.storiesDatabase, name="storiesDatabase"),
    path("history/",views.generatedHistory, name="history")
]