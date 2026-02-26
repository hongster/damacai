# Da Ma Cai API & Scraper

A lightweight, JSON-based API service for historical and latest Da Ma Cai lottery results. Hosted on GitHub for 100% uptime and zero latency.

## Features
- Static JSON files served via high-speed CDN ensures your application gets data instantly.
- Simple RESTful structure. No API keys, no rate limits, just simple HTTP GET requests.
- Automated scrapers ensure the latest draw results are pushed to the repository immediately.

## API

Get all draw dates
```bash
curl https://damacai.hongineer.com/results/draw_dates.json
```

Sample result
```json
{
  "last_draw_date": "20260225",
  "draw_dates": [
    "20050101",
    "20050102",
    "20050104",
    "20050105",
    "20050108"
   ]
}
```

Draw result is retrievable at `https://damacai.hongineer.com/results/<YEAR>/<YYYYMMDD>.json`
```bash
curl https://damacai.hongineer.com/results/2026/20260225.json
```

## Prerequisites
- Python 3.14 or higher
- `requests` library (automatically installed via dependencies)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:hongster/damacai.git
   ```

2. Navigate to the project directory:
   ```bash
   cd damacai
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

Run the scraper using the following command:
```bash
uv run main.py
```

The results will be saved in the `results/` directory, organized by year and draw date.

## Project Structure
- `main.py`: The main script to scrape and save results.
- `results/`: Directory where scraped results are stored.
- `pyproject.toml`: Project metadata and dependencies.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References
- [Scraping Da Ma Cai 4D Results](https://tech.mrleong.net/scrapping-da-ma-cai-4d-results)

## Disclaimer
- This project is an independent open-source initiative. It is neither affiliated with, nor endorsed by Pan Malaysian Pools Sdn. Bhd. (Da Ma Cai). All trademarks, logos, and brand names are the property of their respective owners. 
- This API and the associated scraper are provided strictly for educational and research purposes to demonstrate web data extraction and static API hosting techniques. 
- The data is provided "as-is" without any guarantees of accuracy, completeness, or timeliness. Use this data at your own risk. The developer is not responsible for any financial losses or damages resulting from the use of this service. 
- Lottery involves financial risk. This service does not encourage gambling. If you or someone you know has a gambling problem, please seek professional help. 
