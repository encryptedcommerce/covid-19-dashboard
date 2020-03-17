from controllers import deaths as controller
from views import common


layout = common.get_tabs_layout('deaths')


def get_chart_layout():
    return common.get_chart_layout('deaths', controller)


def get_table_layout():
    return common.get_table_layout('deaths', controller)

