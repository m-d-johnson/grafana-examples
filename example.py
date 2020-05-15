from grafanalib.core import (
    Alert, AlertCondition, Dashboard, Graph, GaugePanel,
    GreaterThan, OP_AND, OPS_FORMAT, Row, RTYPE_SUM, SECONDS_FORMAT,
    SHORT_FORMAT, single_y_axis, Target, TimeRange, YAxes, YAxis
)


dashboard = Dashboard(
    title="Frontend Stats",
    rows=[
        Row(panels=[
          GaugePanel(
            title="Power Consumption",
            dataSource='prometheus',
            targets=[
                Target(
                  expr='_mqtt:instantaneous_power_house',
                  legendFormat="Consumption Now",
                  refId='A',
                  ), 
                ]
            )
        ])
    ]
).auto_panel_ids()
