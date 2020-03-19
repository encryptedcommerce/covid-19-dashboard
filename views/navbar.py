import dash_core_components as dcc
import dash_html_components as html


def create_navbar(current_page: str = 'confirmed'):
    links = {
        '/': 'Summary Dashboard',
        '/confirmed':  'Confirmed',
        '/deaths': 'Deaths',
        '/recovered': 'Recovered',
    }
    nav_items = []
    for link, title in links.items():
        if current_page == link:
            class_name = 'active'
        else:
            class_name = ''
        link_id = title.lower().replace(' ', '-')
        nav_items.append(dcc.Link(title, id=link_id, href=link, className=class_name))

    nav_bar = html.Nav(id='nav-bar', children=nav_items)

    return nav_bar
