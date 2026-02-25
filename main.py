import json
import time
from pathlib import Path
import requests
import re
def main():
    """Start the result scrapping process.
    Results are stored in `results/` folder, relative to this script.
    Refer to https://tech.mrleong.net/scrapping-da-ma-cai-4d-results for scrapping technique.
    """

    print("Getting draw dates...")
    draw_dates = get_draw_dates()
    has_new_result = False

    for draw_date in draw_dates:
        if has_saved_result(draw_date):
            continue

        has_new_result = True
        print("Getting result for draw date: " + draw_date)
        result = get_result(draw_date)
        print("Saving result for draw date: " + draw_date)
        save_result(result, draw_date)

        # Avoid rate limiting.
        time.sleep(0.2)
    
    if has_new_result:
        print("Saving draw dates")
        save_draw_dates(draw_dates)

def save_draw_dates(dates: list[str]) -> None:
    """Save draw dates to file, overwriting existing file.
    The file is located relative to current script directory: `results/draw_dates.json`
    """

    dates.sort()
    data = {
        "last_draw_date": dates[-1],
        "draw_dates": dates
    }

    draw_dates_file = Path(__file__).parent / "results" / "draw_dates.json"
    draw_dates_file.write_text(json.dumps(data))

def get_draw_dates() -> list[str]:
    """Get all draw dates.
    Example date: "20050205"
    """

    url = "https://www.damacai.com.my/ListPastResult"
    response = requests.get(url)

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Could not decode JSON from the response.")
        print("Response content:", response.text)
    
    dates = data['drawdate'].split()
    # Expecting each date to be exactly 8 digits: YYYYMMDD
    dates = [d for d in dates if re.fullmatch(r'\d{8}', d)]

    return dates

def get_result_link(draw_date: str) -> str:
    """Get temporary link for result of given draw date. 
    Link is signed, and expires in 1 hour.
    Example: https://prddmcremt1.blob.core.windows.net/drawresult/DrawDate/20260222.json?sv=2014-02-14&sr=b&sig=ofBjsm76v00Jh8OooyFnJvFnsuzIR5h0%2B6FVh2vFrHk%3D&st=2026-02-25T11:26:59Z&se=2026-02-25T12:36:59Z&sp=r
    """

    url = f"https://www.damacai.com.my/callpassresult?pastdate={draw_date}"
    response = requests.get(url, headers={ 'cookiesession': '504' })

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Could not decode JSON from the response.")
        print("Response content:", response.text)

    return data['link']

def get_result(draw_date: str):
    url = get_result_link(draw_date)
    response = requests.get(url)

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Could not decode JSON from the response.")
        print("Response content:", response.text)

    return data

def save_result(result, draw_date: str) -> None:
    """Save result to file, overwriting existing file.
    Result is JSON encoded.
    """

    # Using `result_file_path`, check if folder exists. If not, create it.
    result_path = result_file_path(draw_date)
    if not result_path.parent.is_dir():
        result_path.parent.mkdir(parents=True, exist_ok=True)
    
    result_path.write_text(json.dumps(result))


def has_saved_result(draw_date: str) -> bool:
    """Check if result file exists."""

    return result_file_path(draw_date).is_file()

def result_file_path(draw_date: str) -> Path:
    """Resolve the path to the result file.
    The file is located relative to current script directory: `results/{year}/{draw_date}.json`
    """

    year = draw_date[:4]
    return Path(__file__).parent / "results" / year / f"{draw_date}.json"

if __name__ == "__main__":
    main()
