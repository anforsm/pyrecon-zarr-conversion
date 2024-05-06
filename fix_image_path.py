import json
import tempfile
from pathlib import Path

def fix_image_path(series_path):
    with open(series_path, "r") as f:
        jser = json.load(f)
    
    new_image_path = jser["series"]["src_dir"].split("/")[-1]
    base_path = series_path.split("traces")[0]
    new_image_path = f"{base_path}images/{new_image_path}"
    jser["series"]["src_dir"] = Path(new_image_path).absolute().as_posix()

    # open tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as f:
        new_jser_path = f.name
        with open(new_jser_path, "w") as f:
            json.dump(jser, f)

    return new_jser_path
    


if __name__ == "__main__":
    print(fix_image_path("../source/BBCHZ/traces/BBCHZ-2024-03-27-phpcuration.jser"))
