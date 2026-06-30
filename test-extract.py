from src.extract import WeatherExtractor

extractor = WeatherExtractor()

weather = extractor.extract()

print(f"Total Records: {len(weather)}")

print(weather[0])