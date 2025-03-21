from pathlib import Path

from icecream import ic

DIR_PATH = Path(__file__).resolve().parents[1]
SRC_PATH = DIR_PATH / "src"
DATA_PATH = DIR_PATH / "data"
RAW_DATA_PATH = DATA_PATH / "raw"
INTERIM_DATA_PATH = DATA_PATH / "interim"
PROCESSED_DATA_PATH = DATA_PATH / "processed"
FIG_PATH = DIR_PATH / "fig"


def generate_dir():
    for path in [
        SRC_PATH,
        DATA_PATH,
        RAW_DATA_PATH,
        INTERIM_DATA_PATH,
        PROCESSED_DATA_PATH,
        FIG_PATH,
    ]:
        path.mkdir(exist_ok=True)


if __name__ == "__main__":
    generate_dir()
    ic(DIR_PATH)
