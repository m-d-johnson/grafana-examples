from grafanalib.core import (
    Alert, 
    AlertCondition, 
    BarGauge, 
    Dashboard, 
    Graph, 
    GaugePanel,
    GreaterThan, 
    OP_AND, 
    OPS_FORMAT, 
    Row, 
    RTYPE_SUM, 
    SECONDS_FORMAT,
    SHORT_FORMAT, 
    single_y_axis,
    Table, 
    Target, 
    TimeRange, 
    YAxes, 
    YAxis
)


dashboard = Dashboard(
    title="My Home Dashboard",
    rows=[
        Row(
          title="Statistics",

          panels=[

          GaugePanel(
            title="GaugePanel: Load Gauge (Holly)",
            dataSource='Prometheus',
            targets=[
                Target(
                  expr='node_load5{instance="holly.kuub.org:9100",job="prometheus"}',
                  refId='A',
                  ), 
                ]
            ),
          BarGauge(
            title="BarGauge: 5 min Load (Holly)",
            dataSource="Prometheus",
              targets=[
                Target(
                  expr='node_load5{instance="holly.kuub.org:9100",job="prometheus"}',
                  refId='A',
                  legendFormat="Load on {{instance}}",
                  ), 
                ],
            ),
          BarGauge(
            title="BarGauge: 5 min Load (Hilly)",
            dataSource="Prometheus",
              targets=[
                Target(
                  expr='node_load5{instance="hilly.kuub.org:9100",job="prometheus"}',
                  refId='A',
                  legendFormat="Load on {{instance}}",
                  ), 
                ],
            ),
          Table(
            title="Table: 5 Min Load (Servers)",
            dataSource="Prometheus",
            targets=[
              Target(
                expr='node_load5{job="prometheus"}',
                refId='A',
                legendFormat="Load on {{instance}}",
                ),
                ], 
              ),]
            ),
        Row(
          title="Graphs",
          panels=[
          # There is a helper function available in grafanalib which can be used to graph data returned
          # by Prometheus, but this is just an example of using the base Graph object.
          # https://grafanalib.readthedocs.io/en/latest/api/grafanalib.html#module-grafanalib.prometheus
            Graph(
              title="Graph: 5 min Load (Servers)",
              dataSource='Prometheus',
              targets=[
                  Target(
                    expr='node_load5{job="prometheus"}',
                    refId='A',
                    legendFormat="{{instance}} 5-min Load",
                    ), 
                  ],
              yAxes=single_y_axis(
                format=None, 
                decimals=2,
                ),
               ),
          ])
        
        ],
    
).auto_panel_ids()
