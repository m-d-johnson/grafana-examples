from grafanalib.core import (
    Alert, AlertCondition, BarGauge, Dashboard, Graph, GaugePanel,
    GreaterThan, OP_AND, OPS_FORMAT, Row, RTYPE_SUM, SECONDS_FORMAT,
    SHORT_FORMAT, single_y_axis, Target, TimeRange, YAxes, YAxis
)


dashboard = Dashboard(
    title="My Home Dashboard",
    rows=[
        Row(panels=[
          GaugePanel(
            title="Load Gauge (Holly)",
            dataSource='Prometheus',
            targets=[
                Target(
                  expr='node_load5{instance="holly.kuub.org:9100",job="prometheus"}',
                  refId='A',
                  ), 
                ]
            ),
          Graph(
            title="MyGraphPanel",
            dataSource='Prometheus',
            targets=[
                Target(
                  expr='node_load5{instance="holly.kuub.org:9100",job="prometheus"}',
                  refId='A',
                  legendFormat="Load on {{instance}}",
                  ), 
                ],
            yAxes=single_y_axis(
              format=None, 
              decimals=2
              ),
            ),
          BarGauge(
            title="My BarGaugePanel",
            dataSource="Prometheus",
              targets=[
                Target(
                  expr='node_load5{instance="holly.kuub.org:9100",job="prometheus"}',
                  refId='A',
                  legendFormat="Load on {{instance}}",
                  ), 
                ],
            )
        ])
    ]
).auto_panel_ids()
