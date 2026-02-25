# Da Ma Cai Scraper

Da Ma Cai is a lottery in Malaysia. This project scrapes draw results, organizes them, and makes them consumable by applications.

## Features
- Scrapes draw results from the Da Ma Cai website.
- Saves results in organized JSON files by year and draw date.
- Avoids redundant downloads by checking existing results.

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
