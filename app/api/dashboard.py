from dash import Dash, html
import os

def run_dashboard():
    app = Dash(__name__)
    app.layout = html.Div([
        html.H1("🧘 NaMoNexus Dharma Console"),
        html.P("Dashboard is active and connected to the API Gateway.")
    ])
    port = int(os.getenv("DASHBOARD_PORT", 8050))
    app.run_server(host="0.0.0.0", port=port)

if __name__ == "__main__":
    run_dashboard()
