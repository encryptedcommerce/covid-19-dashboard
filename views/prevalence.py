from controllers import prevalence as controller
from views import common


layout = common.get_tabs_layout('prevalence')


def get_chart_layout():
    return common.get_chart_layout('prevalence', controller, scale_toggle=True)


def get_table_layout():
    return common.get_table_layout('prevalence', controller)

