from django.shortcuts import render, redirect
from charts.views import bar_chart_view


def home_view(request):
    """
    Redirect to Bar chart
    :param request:
    :return:
    """


    return redirect(bar_chart_view)

