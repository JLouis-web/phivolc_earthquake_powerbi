from pylindol import PhivolcsEarthquakeInfoScraper
import pandas as pd

# Initialize scraper
scraper = PhivolcsEarthquakeInfoScraper()

# Run scraper (latest available data)
df = scraper.run()

# Preview data
print(df.head())

# Save to CSV
# df.to_csv("phivolcs_earthquake_data.csv", index=False)

# print("CSV file saved successfully!")
