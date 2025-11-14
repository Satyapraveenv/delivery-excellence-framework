"""
Delivery Excellence Metrics Dashboard
Interactive visualization of program delivery, quality, and team performance metrics

Usage:
    python delivery_metrics.py

Then navigate to http://localhost:8050 in your browser
"""

import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import json

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Delivery Excellence Dashboard"

# Sample Data Generation (Replace with your actual data source)
def generate_sample_data():
    """Generate sample metrics data for demonstration"""
    
    # Date range: Last 6 months
    dates = pd.date_range(end=datetime.now(), periods=26, freq='W')
    
    # On-Time Delivery Metrics
    delivery_data = pd.DataFrame({
        'Week': dates,
        'Committed': [45, 48, 42, 50, 47, 45, 52, 48, 50, 46, 48, 51, 47, 49, 45, 50, 48, 52, 47, 49, 51, 48, 50, 46, 49, 51],
        'Completed': [43, 46, 41, 49, 47, 44, 51, 47, 49, 45, 47, 50, 46, 48, 44, 49, 47, 51, 46, 48, 50, 47, 49, 45, 48, 50],
        'OnTime_Rate': [95.6, 95.8, 97.6, 98.0, 100.0, 97.8, 98.1, 97.9, 98.0, 97.8, 97.9, 98.0, 97.9, 98.0, 97.8, 98.0, 97.9, 98.1, 97.9, 98.0, 98.0, 97.9, 98.0, 97.8, 98.0, 98.0]
    })
    
    # Customer Satisfaction (CSAT)
    csat_data = pd.DataFrame({
        'Month': pd.date_range(end=datetime.now(), periods=12, freq='M'),
        'CSAT': [92, 93, 94, 95, 96, 95, 96, 97, 95, 96, 97, 98],
        'NPS': [45, 48, 52, 55, 58, 56, 60, 62, 58, 61, 64, 68]
    })
    
    # Quality Metrics
    quality_data = pd.DataFrame({
        'Week': dates,
        'Defects_Found_QE': [23, 19, 21, 18, 20, 17, 22, 19, 18, 20, 16, 21, 19, 17, 20, 18, 19, 16, 21, 18, 17, 19, 18, 20, 17, 16],
        'Defects_Escaped': [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        'Automation_Coverage': [65, 67, 68, 70, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89]
    })
    
    # Risk Metrics
    risk_data = pd.DataFrame({
        'Risk_Category': ['Technical', 'Resource', 'Schedule', 'Quality', 'Compliance'],
        'Critical': [2, 1, 0, 1, 0],
        'High': [5, 3, 2, 3, 1],
        'Medium': [8, 6, 5, 4, 3],
        'Low': [12, 10, 8, 7, 5]
    })
    
    # Team Velocity
    velocity_data = pd.DataFrame({
        'Sprint': [f'Sprint {i}' for i in range(1, 13)],
        'Planned': [45, 48, 47, 50, 49, 52, 48, 50, 51, 49, 52, 50],
        'Actual': [43, 46, 47, 49, 49, 51, 47, 49, 50, 48, 51, 50],
        'Velocity': [43, 44.5, 45.3, 46.8, 47.4, 48.6, 48.0, 48.3, 49.0, 48.7, 49.5, 49.7]
    })
    
    return delivery_data, csat_data, quality_data, risk_data, velocity_data

# Load data
delivery_df, csat_df, quality_df, risk_df, velocity_df = generate_sample_data()

# Calculate KPIs
current_ontime_rate = delivery_df['OnTime_Rate'].iloc[-4:].mean()
current_csat = csat_df['CSAT'].iloc[-1]
current_nps = csat_df['NPS'].iloc[-1]
defect_escape_rate = (quality_df['Defects_Escaped'].sum() / quality_df['Defects_Found_QE'].sum()) * 100
automation_coverage = quality_df['Automation_Coverage'].iloc[-1]
avg_velocity = velocity_df['Velocity'].iloc[-4:].mean()

# Dashboard Layout
app.layout = html.Div([
    html.Div([
        html.H1("Delivery Excellence Dashboard", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 10}),
        html.P("Real-time metrics for strategic program delivery", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'marginBottom': 30})
    ]),
    
    # KPI Cards Row
    html.Div([
        # On-Time Delivery
        html.Div([
            html.Div([
                html.H3("On-Time Delivery", style={'color': '#7f8c8d', 'fontSize': 14, 'marginBottom': 5}),
                html.H2(f"{current_ontime_rate:.1f}%", 
                       style={'color': '#27ae60' if current_ontime_rate >= 95 else '#e74c3c', 
                              'fontSize': 32, 'marginBottom': 5}),
                html.P("Target: 95%+", style={'color': '#95a5a6', 'fontSize': 12})
            ], style={'padding': 20, 'backgroundColor': '#ecf0f1', 'borderRadius': 8})
        ], style={'width': '18%', 'display': 'inline-block', 'margin': '0 1%'}),
        
        # CSAT
        html.Div([
            html.Div([
                html.H3("Customer Satisfaction", style={'color': '#7f8c8d', 'fontSize': 14, 'marginBottom': 5}),
                html.H2(f"{current_csat}%", 
                       style={'color': '#27ae60' if current_csat >= 90 else '#e74c3c', 
                              'fontSize': 32, 'marginBottom': 5}),
                html.P(f"NPS: +{current_nps}", style={'color': '#95a5a6', 'fontSize': 12})
            ], style={'padding': 20, 'backgroundColor': '#ecf0f1', 'borderRadius': 8})
        ], style={'width': '18%', 'display': 'inline-block', 'margin': '0 1%'}),
        
        # Defect Escape Rate
        html.Div([
            html.Div([
                html.H3("Defect Escape Rate", style={'color': '#7f8c8d', 'fontSize': 14, 'marginBottom': 5}),
                html.H2(f"{defect_escape_rate:.2f}%", 
                       style={'color': '#27ae60' if defect_escape_rate < 1 else '#e74c3c', 
                              'fontSize': 32, 'marginBottom': 5}),
                html.P("Target: <1%", style={'color': '#95a5a6', 'fontSize': 12})
            ], style={'padding': 20, 'backgroundColor': '#ecf0f1', 'borderRadius': 8})
        ], style={'width': '18%', 'display': 'inline-block', 'margin': '0 1%'}),
        
        # Automation Coverage
        html.Div([
            html.Div([
                html.H3("Automation Coverage", style={'color': '#7f8c8d', 'fontSize': 14, 'marginBottom': 5}),
                html.H2(f"{automation_coverage}%", 
                       style={'color': '#27ae60' if automation_coverage >= 70 else '#f39c12', 
                              'fontSize': 32, 'marginBottom': 5}),
                html.P("Target: 70%+", style={'color': '#95a5a6', 'fontSize': 12})
            ], style={'padding': 20, 'backgroundColor': '#ecf0f1', 'borderRadius': 8})
        ], style={'width': '18%', 'display': 'inline-block', 'margin': '0 1%'}),
        
        # Team Velocity
        html.Div([
            html.Div([
                html.H3("Avg Velocity (4wk)", style={'color': '#7f8c8d', 'fontSize': 14, 'marginBottom': 5}),
                html.H2(f"{avg_velocity:.1f}", 
                       style={'color': '#3498db', 'fontSize': 32, 'marginBottom': 5}),
                html.P("Story Points", style={'color': '#95a5a6', 'fontSize': 12})
            ], style={'padding': 20, 'backgroundColor': '#ecf0f1', 'borderRadius': 8})
        ], style={'width': '18%', 'display': 'inline-block', 'margin': '0 1%'}),
    ], style={'marginBottom': 30}),
    
    # Charts Row 1: Delivery & CSAT
    html.Div([
        html.Div([
            dcc.Graph(id='delivery-trend')
        ], style={'width': '48%', 'display': 'inline-block', 'margin': '0 1%'}),
        
        html.Div([
            dcc.Graph(id='csat-trend')
        ], style={'width': '48%', 'display': 'inline-block', 'margin': '0 1%'}),
    ], style={'marginBottom': 20}),
    
    # Charts Row 2: Quality & Risk
    html.Div([
        html.Div([
            dcc.Graph(id='quality-metrics')
        ], style={'width': '48%', 'display': 'inline-block', 'margin': '0 1%'}),
        
        html.Div([
            dcc.Graph(id='risk-heatmap')
        ], style={'width': '48%', 'display': 'inline-block', 'margin': '0 1%'}),
    ], style={'marginBottom': 20}),
    
    # Charts Row 3: Velocity
    html.Div([
        html.Div([
            dcc.Graph(id='velocity-trend')
        ], style={'width': '98%', 'display': 'inline-block', 'margin': '0 1%'}),
    ]),
    
    # Footer
    html.Div([
        html.P("Delivery Excellence Framework | Satya Praveen Vemuri", 
               style={'textAlign': 'center', 'color': '#95a5a6', 'marginTop': 30})
    ])
], style={'padding': 30, 'backgroundColor': '#ffffff', 'fontFamily': 'Arial, sans-serif'})

# Callbacks for interactive charts
@app.callback(
    Output('delivery-trend', 'figure'),
    Input('delivery-trend', 'id')
)
def update_delivery_chart(_):
    fig = go.Figure()
    
    # Target line
    fig.add_trace(go.Scatter(
        x=delivery_df['Week'],
        y=[95] * len(delivery_df),
        mode='lines',
        name='Target (95%)',
        line=dict(color='#e74c3c', dash='dash', width=2)
    ))
    
    # Actual on-time delivery
    fig.add_trace(go.Scatter(
        x=delivery_df['Week'],
        y=delivery_df['OnTime_Rate'],
        mode='lines+markers',
        name='On-Time Delivery',
        line=dict(color='#27ae60', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='On-Time Delivery Trend (Weekly)',
        xaxis_title='Week',
        yaxis_title='On-Time Rate (%)',
        yaxis=dict(range=[90, 100]),
        hovermode='x unified',
        template='plotly_white'
    )
    
    return fig

@app.callback(
    Output('csat-trend', 'figure'),
    Input('csat-trend', 'id')
)
def update_csat_chart(_):
    fig = go.Figure()
    
    # CSAT
    fig.add_trace(go.Scatter(
        x=csat_df['Month'],
        y=csat_df['CSAT'],
        mode='lines+markers',
        name='CSAT',
        line=dict(color='#3498db', width=3),
        marker=dict(size=10),
        yaxis='y'
    ))
    
    # NPS
    fig.add_trace(go.Scatter(
        x=csat_df['Month'],
        y=csat_df['NPS'],
        mode='lines+markers',
        name='NPS',
        line=dict(color='#9b59b6', width=3),
        marker=dict(size=10),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title='Customer Satisfaction Metrics (Monthly)',
        xaxis_title='Month',
        yaxis=dict(title='CSAT (%)', range=[85, 100]),
        yaxis2=dict(title='NPS', overlaying='y', side='right', range=[40, 75]),
        hovermode='x unified',
        template='plotly_white'
    )
    
    return fig

@app.callback(
    Output('quality-metrics', 'figure'),
    Input('quality-metrics', 'id')
)
def update_quality_chart(_):
    fig = go.Figure()
    
    # Defects found in QE
    fig.add_trace(go.Bar(
        x=quality_df['Week'],
        y=quality_df['Defects_Found_QE'],
        name='Defects Found (QE)',
        marker_color='#3498db',
        yaxis='y'
    ))
    
    # Defects escaped to production
    fig.add_trace(go.Scatter(
        x=quality_df['Week'],
        y=quality_df['Defects_Escaped'],
        mode='lines+markers',
        name='Defects Escaped',
        line=dict(color='#e74c3c', width=3),
        marker=dict(size=10),
        yaxis='y'
    ))
    
    # Automation coverage
    fig.add_trace(go.Scatter(
        x=quality_df['Week'],
        y=quality_df['Automation_Coverage'],
        mode='lines',
        name='Automation Coverage (%)',
        line=dict(color='#27ae60', width=2),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title='Quality Engineering Metrics',
        xaxis_title='Week',
        yaxis=dict(title='Defect Count'),
        yaxis2=dict(title='Automation Coverage (%)', overlaying='y', side='right', range=[0, 100]),
        hovermode='x unified',
        template='plotly_white',
        barmode='group'
    )
    
    return fig

@app.callback(
    Output('risk-heatmap', 'figure'),
    Input('risk-heatmap', 'id')
)
def update_risk_heatmap(_):
    # Prepare data for heatmap
    risk_matrix = risk_df.set_index('Risk_Category')[['Critical', 'High', 'Medium', 'Low']].T
    
    fig = go.Figure(data=go.Heatmap(
        z=risk_matrix.values,
        x=risk_matrix.columns,
        y=risk_matrix.index,
        colorscale=[[0, '#27ae60'], [0.3, '#f39c12'], [0.7, '#e67e22'], [1, '#e74c3c']],
        text=risk_matrix.values,
        texttemplate='%{text}',
        textfont={"size": 16},
        colorbar=dict(title="Risk Count")
    ))
    
    fig.update_layout(
        title='Risk Distribution by Category & Severity',
        xaxis_title='Risk Category',
        yaxis_title='Severity',
        template='plotly_white'
    )
    
    return fig

@app.callback(
    Output('velocity-trend', 'figure'),
    Input('velocity-trend', 'id')
)
def update_velocity_chart(_):
    fig = go.Figure()
    
    # Planned vs Actual
    fig.add_trace(go.Bar(
        x=velocity_df['Sprint'],
        y=velocity_df['Planned'],
        name='Planned',
        marker_color='#95a5a6'
    ))
    
    fig.add_trace(go.Bar(
        x=velocity_df['Sprint'],
        y=velocity_df['Actual'],
        name='Actual',
        marker_color='#3498db'
    ))
    
    # Velocity trend line
    fig.add_trace(go.Scatter(
        x=velocity_df['Sprint'],
        y=velocity_df['Velocity'],
        mode='lines+markers',
        name='Velocity (Trend)',
        line=dict(color='#27ae60', width=3),
        marker=dict(size=10),
        yaxis='y'
    ))
    
    fig.update_layout(
        title='Team Velocity & Sprint Performance',
        xaxis_title='Sprint',
        yaxis_title='Story Points',
        hovermode='x unified',
        template='plotly_white',
        barmode='group'
    )
    
    return fig

if __name__ == '__main__':
    print("Starting Delivery Excellence Dashboard...")
    print("Navigate to http://localhost:8050 in your browser")
    app.run_server(debug=True, port=8050)
