from src.extract import WeatherExtractor
from src.transform import WeatherTransformer
from src.load import WeatherLoader

extractor = WeatherExtractor()
transformer = WeatherTransformer()
loader = WeatherLoader()

raw_data = extractor.extract()

weather_df = transformer.transform(raw_data)

loader.save_to_csv(weather_df)

print(weather_df.head())