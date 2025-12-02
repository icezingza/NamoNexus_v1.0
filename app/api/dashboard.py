"""Optional Dash dashboard for NaMoNexus monitoring."""
from __future__ import annotations

try:
    import dash  # type: ignore
    from dash import Dash, Input, Output, dcc, html
except ImportError:  # pragma: no cover - optional dependency
    dash = None
    Dash = None
    Input = None
    Output = None
    dcc = None
    html = None

from app.api.monitoring import get_metrics


def create_dashboard() -> Dash | None:
    if dash is None or Dash is None or html is None or dcc is None or Input is None or Output is None:
        return None

    app = Dash(__name__)
    app.layout = html.Div(
        children=[
            html.H1("NaMo Nexus Dashboard"),
            dcc.Interval(id="interval", interval=3_000, n_intervals=0),
            html.Pre(id="metrics"),
        ]
    )

    @app.callback(Output("metrics", "children"), Input("interval", "n_intervals"))  # type: ignore
    def update_metrics(_: int):  # pragma: no cover - requires Dash runtime
        metrics = get_metrics()
        return f"{metrics}"

    return app
