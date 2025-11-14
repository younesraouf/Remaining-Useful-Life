import os
import pandas as pd


def convert_txt_to_csv(input_path: str, output_path: str):
    """
    Convertit un fichier NASA CMAPSS (.txt) en CSV propre.
    - Enlève la colonne vide extra
    - Supprime les espaces multiples
    """
    print(f"Converting: {input_path}")

    df = pd.read_csv(
        input_path,
        sep=r"\s+",
        header=None,
        engine="python"
    )

    # Certaines versions ont une colonne vide → suppression
    if df.columns[-1] == df.columns[-1]:
        if df.iloc[:, -1].isna().all() or (df.iloc[:, -1] == 0).all():
            df = df.iloc[:, :-1]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Saved: {output_path}")


def convert_all_raw_files(raw_folder: str, ingested_folder: str):
    """
    Convertit tous les .txt de data/raw/ en .csv dans data/ingested/
    """
    os.makedirs(ingested_folder, exist_ok=True)

    for filename in os.listdir(raw_folder):
        if filename.endswith(".txt"):
            input_file = os.path.join(raw_folder, filename)
            output_file = os.path.join(
                ingested_folder,
                filename.replace(".txt", ".csv")
            )

            convert_txt_to_csv(input_file, output_file)

    print("\n✔ Conversion terminée pour tous les fichiers NASA CMAPSS.\n")


if __name__ == "__main__":
    RAW_DIR = "data/raw/"
    INGESTED_DIR = "data/ingested/"

    convert_all_raw_files(RAW_DIR, INGESTED_DIR)
