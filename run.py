"""
Application Entry Point
"""

from src.main import WeatherETLPipeline

if __name__ == "__main__":
    pipeline = WeatherETLPipeline()
    pipeline.run()