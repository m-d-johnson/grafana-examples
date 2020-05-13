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
            title="My GaugePanel",
            dataSource='My Prometheus',
            targets=[
                Target(
                  expr='histogram_quantile(0.5, sum(irate(nginx_http_request_duration_seconds_bucket{job="default/frontend"}[1m])) by (le))',
                  legendFormat="0.5 quantile",
                  refId='A',
                  ), 
                ]
            )
        ])
    ]
).auto_panel_ids()
