from pathlib import Path
import csv
import json

# Robust project root resolution
CURRENT_DIR = Path.cwd()
PROJECT_ROOT = CURRENT_DIR if (CURRENT_DIR / "data").exists() else CURRENT_DIR.parent
DATA_DIR = PROJECT_ROOT / "data" / "sample"

def load_prices(filepath=DATA_DIR / "prices.csv"):
    """Load market observations from CSV into a list of dictionaries."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

prices = load_prices()


def load_instruments(filepath=DATA_DIR / "instruments.json"):
    """Load and parse JSON metadata file into a Python dictionary."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)

instruments = load_instruments()



def display_market_summary(asset, prices, show_currency=True):
    """
    Display a standardized market summary for any instrument or benchmark.
    
    Args:
        asset (dict): Metadata dictionary (containing 'ticker', 'name', 'currency').
        prices (list): Filtered observation dictionaries.
        show_currency (bool): Whether to append the currency code to prices.
    """
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)
    currency_suffix = f" {asset.get('currency', '')}" if show_currency else ""

 

def run_td02_market_snapshot():
    """Simulate the complete main() workflow for TD02."""
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print("Period   : 1 month")
    print("Interval : Daily")
    print()
    print("Instrument")
    display_market_summary(instrument, instrument_prices, show_currency=True)
    print()
    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)

# Execute full simulation
run_td02_market_snapshot()