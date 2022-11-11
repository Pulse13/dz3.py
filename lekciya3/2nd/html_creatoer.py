from UI import temperature_view
from UI import wind_speed_view
from UI import pressure_view

def create(device=1):
    style = 'stule = "front-size:30px;"'
    html = '<html>\n  <head><head>\n   <body>\n'
    html+= '    <p{}>Temperature:{} c<\p>\n'\
        .format(style, temperature_view(device))
    html+= '    <p{}>Temperature:{} m/s<\p>\n'\
        .format(style, wind_speed_view(device))
    html+= '    <p{}>Temperature:{} mmHg<\p>\n'\
        .format(style, pressure_view(device))
    html+= '   </body>\n<?html>'

    with open('index.html', 'w') as page:
        page.write(html)

def new_create(data,devise=1):
    t,p,w = data
    style = 'stule = "front-size:30px;"'
    html = '<html>\n  <head><head>\n   <body>\n'
    html+= '    <p{}>Temperature:{} c<\p>\n'\
        .format(style, t)
    html+= '    <p{}>Temperature:{} m/s<\p>\n'\
        .format(style, w)
    html+= '    <p{}>Temperature:{} mmHg<\p>\n'\
        .format(style, p)
    html+= '   </body>\n<?html>'

    with open('index.html', 'w') as page:
        page.write(html)