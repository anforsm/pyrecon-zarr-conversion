from glob import glob
from pathlib import Path

def get_most_recent_series(series_path):
    path = Path(series_path) / Path("traces")
    print(path)
    path = path.as_posix()
    series = glob(f"{path}/BBCHZ-*-*.jser")
    print(series)
    most_recent_series = sorted(series)[-1]
    return most_recent_series

if __name__ == "__main__":
    most_recent_series = get_most_recent_series()
    print(most_recent_series)
