from src.extract import WeatherExtractor
from src.transform import WeatherTransformer

extractor = WeatherExtractor()
transformer = WeatherTransformer()

raw_weather = extractor.extract()

weather_df = transformer.transform(raw_weather)

print(weather_df)