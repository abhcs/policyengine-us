from policyengine_us.data.datasets.cps.enhanced_cps.calibrate import (
    get_snapshot,
)
from policyengine_us.data.storage import STORAGE_FOLDER
import pandas as pd


def main():
    YEARS = ["2023", "2024", "2025"]
    DATASETS = ["puf_2023", "cps_2023", "enhanced_cps_2023"]

    dfs = []

    for year in YEARS:
        for dataset in DATASETS:
            df = get_snapshot(dataset, year)
            df["time_period"] = year
            df["dataset"] = dataset
            dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)

    df.to_csv(
        STORAGE_FOLDER / "dataset_losses.csv.gz",
        index=False,
        compression="gzip",
    )


if __name__ == "__main__":
    main()
