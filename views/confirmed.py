from controllers import confirmed as controller
from views import common


layout = common.get_tabs_layout('confirmed')


def get_chart_layout():
    return common.get_chart_layout('confirmed', controller, scale_toggle=True)


def get_table_layout():
    return common.get_table_layout('confirmed', controller)

