from controllers import recovered as controller
from views import common


layout = common.get_tabs_layout('recovered')


def get_chart_layout():
    return common.get_chart_layout('recovered', controller)


def get_table_layout():
    return common.get_table_layout('recovered', controller)

