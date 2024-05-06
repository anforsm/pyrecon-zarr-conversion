from pathlib import Path
from fix_image_path import fix_image_path
from get_recent_series import get_most_recent_series
import os
import subprocess
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        series_path = os.path.abspath("../source/BBCHZ/")
        print("No series path provided, using default path: ", series_path)
    else:
        series_path = sys.argv[1]

    output_dir = Path(series_path.split("source")[0] + "target") / Path(series_path).name / Path("output.zarr")
    os.makedirs(output_dir, exist_ok=True)

    most_recent_series = get_most_recent_series(series_path)
    print("This is the most recent series", most_recent_series)
    new_jser_path = fix_image_path(most_recent_series)
    print("This file has the fixed src dir", new_jser_path)

    env = os.environ.copy()
    env["QT_QPA_PLATFORM"] = "offscreen"
    subprocess.run(f"python jser_to_zarr.py {new_jser_path} -o {output_dir} -g {' '.join(['neurons', 'axons', 'dendrites', 'spines'])}".split(" "), env=env)
