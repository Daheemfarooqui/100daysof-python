import numpy as np


def calculate_grade(df):

    df["Grade"] = np.where(
        df["Marks"] >= 80,
        "A",
        np.where(
            df["Marks"] >= 60,
            "B",
            np.where(
                df["Marks"] >= 40,
                "C",
                "Fail"
            )
        )
    )

    return df


def process_students(df):

    df["Name"] = df["Name"].str.strip().str.title()

    return df