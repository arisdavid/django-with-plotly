from django.shortcuts import render
import random


def bar_chart_view(request):
    """
    Bar chart
    :param request:
    :return:
    """
    # Generate a list of random numbers
    x = list(range(1, 6))
    y = [random.randint(100, 600) for _ in range(6)]

    # Bar chart colors
    colors = ['limegreen', ] * 5

    # Create a trace json to hold graph data
    trace = {
        'x': x,
        'y': y,
        'type': 'bar',
        'name': x,
        'marker': {'color': colors}

    }

    # Configure the chart's layout
    layout = {'title': {'text': 'Bar Chart',
                        'font': {
                            'color': '#ffffff'}
                        },
              'xaxis': {'title': 'X-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'false'},
              'yaxis': {'title': 'Y-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'true'},
              'plot_bgcolor': 'black', 'paper_bgcolor': 'black', 'bordercolor': '#ffffff'}

    # Pass trace and layout in the context
    context = {"trace": trace,
               "layout": layout,
               "title": "Bar Chart"}

    return render(request, "chart.html", context)


def scatter_chart_view(request):
    """
    Scatter Chart
    :param request:
    :return:
    """
    # Generate a list of random numbers
    x = list(range(1, 6))
    y = [random.randint(100, 600) for _ in range(6)]

    # Create a trace json to hold graph data
    trace = {
        'x': x,
        'y': y,
        'type': 'scatter',

    }

    # Configure the chart's layout
    layout = {'title': {'text': 'Scatter Chart',
                        'font': {
                            'color': '#ffffff'}
                        },
              'xaxis': {'title': 'X-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'false'},
              'yaxis': {'title': 'Y-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'true'},
              'plot_bgcolor': 'black', 'paper_bgcolor': 'black', 'bordercolor': '#ffffff'}

    # Pass trace and layout in the context
    context = {"trace": trace,
               "layout": layout,
               "title": "Scatter Chart"}

    return render(request, "chart.html", context)


def pie_chart_view(request):
    """
    Pie Chart
    :param request:
    :return:
    """

    # Create a trace json to hold graph data
    trace = {
        'values': [19, 26, 55],
        'labels': ['Residential', 'Non-Residential', 'Utility'],
        'type': 'pie'


    }

    # Configure the chart's layout
    layout = {'title': {'text': 'Pie Chart',
                        'font': {
                            'color': '#ffffff'}
                        },
              'plot_bgcolor': 'black', 'paper_bgcolor': 'black', 'bordercolor': '#ffffff'}

    # Pass trace and layout in the context
    context = {"trace": trace,
               "layout": layout,
               "title": "Pie Chart"}

    return render(request, "chart.html", context)


def scatter_chart_view(request):
    """
    Scatter Chart
    :param request:
    :return:
    """
    # Generate a list of random numbers
    x = list(range(1, 6))
    y = [random.randint(100, 600) for _ in range(6)]

    # Create a trace json to hold graph data
    trace = {
        'x': x,
        'y': y,
        'type': 'scatter',

    }

    # Configure the chart's layout
    layout = {'title': {'text': 'Scatter Chart',
                        'font': {
                            'color': '#ffffff'}
                        },
              'xaxis': {'title': 'X-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'false'},
              'yaxis': {'title': 'Y-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'true'},
              'plot_bgcolor': 'black', 'paper_bgcolor': 'black', 'bordercolor': '#ffffff'}

    # Pass trace and layout in the context
    context = {"trace": trace,
               "layout": layout,
               "title": "Scatter Chart"}

    return render(request, "chart.html", context)


def bubble_chart_view(request):
    """
    Bubble Chart
    :param request:
    :return:
    """

    # Create a trace json to hold graph data
    trace = {
          'x': [1, 2, 3, 4],
          'y': [10, 11, 12, 13],
          'mode': 'markers',
          'marker': {
            'size': [40, 60, 80, 100]
          }


    }

    # Configure the chart's layout
    layout = {'title': {'text': 'Bubble Chart',
                        'font': {
                            'color': '#ffffff'}
                        },
              'xaxis': {'title': 'X-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'false'},
              'yaxis': {'title': 'Y-axis', 'color': '#DCDCDC', 'mirror': 'true', 'showline': 'true'},
              'plot_bgcolor': 'black', 'paper_bgcolor': 'black', 'bordercolor': '#ffffff'}

    # Pass trace and layout in the context
    context = {"trace": trace,
               "layout": layout,
               "title": "Bubble Chart"}

    return render(request, "chart.html", context)

