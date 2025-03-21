import polars as pl

from config import *


def read_df():
    raw_df = pl.read_csv(RAW_DATA_PATH / "test_prestige_sd.csv")
    return raw_df.select(
        [
            "participant.code",
            "participant.payoff",
            "player.id_in_group",
            "player.payoff",
            "player.contribution",
            "player.show_payoff",
            "player.show_contribution",
            "group.total_contribution",
            "subsession.round_number",
            "session.code",
        ]
    )


# `next_contribution` を計算する関数を適用
def add_next_contribution(df: pl.DataFrame):
    # ソート（`session.code` と `participant.code` ごとに `subsession.round_number` を昇順）
    df = df.sort(
        ["session.code", "participant.code", "subsession.round_number"]
    ).with_columns(
        pl.col("player.contribution")
        .shift(-1)
        .over(["session.code", "participant.code"])
        .alias("next_contribution")
    )

    return df


def process_df(raw_df):
    df = raw_df
    df = add_next_contribution(df)
    return df


def write_res_df(df: pl.DataFrame):
    df.write_csv(PROCESSED_DATA_PATH / "test_prestige_sd.csv")


if __name__ == "__main__":
    raw_df = read_df()
    processed_df = process_df(raw_df)
    write_res_df(processed_df)
