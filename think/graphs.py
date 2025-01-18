import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
from .models import UserInput

class GraphGenerator:
    def __init__(self, data):
        self.data = data

    def _validate_data(self, required_columns):
        if not self.data or len(self.data) == 0:
            raise ValueError("No data available")
        
        # Convert QuerySet to DataFrame using values()
        df = pd.DataFrame.from_records(self.data.values())
        
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise KeyError(f"Missing required columns: {', '.join(missing_cols)}")
        return df

    def sleep_analysis_graph(self, start_date=None, end_date=None):
        try:
            required_columns = ['sleep', 'wake']
            df = self._validate_data(required_columns)
            
            df['sleep_duration'] = (pd.to_datetime(df['wake']) - 
                                  pd.to_datetime(df['sleep'])).dt.total_seconds() / 3600
            df['date'] = pd.to_datetime(df['sleep']).dt.date

            if start_date:
                df = df[df['date'] >= start_date]
            if end_date:
                df = df[df['date'] <= end_date]

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=df['date'],
                y=df['sleep_duration'],
                name='Sleep Duration (hours)'
            ))
            fig.update_layout(
                title='Sleep Duration Analysis',
                xaxis_title='Date',
                yaxis_title='Hours of Sleep',
                template='plotly_white'
            )
            return fig.to_html()
            
        except Exception as e:
            return f"<p>Error generating sleep analysis graph: {str(e)}</p>"

    def exercise_analysis_graph(self, start_date=None, end_date=None):
        try:
            required_columns = ['exercise_start', 'exercise_end', 'exercise_type']
            df = self._validate_data(required_columns)
            
            df['exercise_duration'] = (pd.to_datetime(df['exercise_end']) - 
                                     pd.to_datetime(df['exercise_start'])).dt.total_seconds() / 3600
            df['date'] = pd.to_datetime(df['exercise_start']).dt.date

            if start_date:
                df = df[df['date'] >= start_date]
            if end_date:
                df = df[df['date'] <= end_date]

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=df['date'],
                y=df['exercise_duration'],
                name='Exercise Duration (hours)'
            ))
            fig.update_layout(
                title='Exercise Duration Analysis',
                xaxis_title='Date',
                yaxis_title='Hours of Exercise',
                template='plotly_white'
            )
            return fig.to_html()
            
        except Exception as e:
            return f"<p>Error generating exercise analysis graph: {str(e)}</p>"

    def sunlight_analysis_graph(self, start_date=None, end_date=None):
        try:
            required_columns = ['sunlight_start', 'sunlight_end']
            df = self._validate_data(required_columns)
            
            df['sunlight_duration'] = (pd.to_datetime(df['sunlight_end']) - 
                                     pd.to_datetime(df['sunlight_start'])).dt.total_seconds() / 3600
            df['date'] = pd.to_datetime(df['sunlight_start']).dt.date

            if start_date:
                df = df[df['date'] >= start_date]
            if end_date:
                df = df[df['date'] <= end_date]

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=df['date'],
                y=df['sunlight_duration'],
                name='Sunlight Exposure (hours)'
            ))
            fig.update_layout(
                title='Daily Sunlight Exposure',
                xaxis_title='Date',
                yaxis_title='Hours of Sunlight',
                template='plotly_white'
            )
            return fig.to_html()
            
        except Exception as e:
            return f"<p>Error generating sunlight analysis graph: {str(e)}</p>"
