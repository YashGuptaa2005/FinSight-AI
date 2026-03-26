import pandas as pd
import os

def load_news_data():
    folder_path = "data/news"
    all_files = []

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            print(f"Loading: {file}")
            df = pd.read_csv(file_path)
            all_files.append(df)

    combined_df = pd.concat(all_files, ignore_index=True)
    return combined_df


if __name__ == "__main__":
    df = load_news_data()
    print(df.head())