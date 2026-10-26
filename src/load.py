import pandas as pd
from sqlalchemy import create_engine


def load_gold_to_postgres():
    # Read cleaned CSV data into DataFrame
    df = pd.read_csv("data/processed/weather_cleaned.csv")

    # Establish database connection engine
    engine = create_engine(
        "postgresql+psycopg2://itversity_retail_user:itversity@localhost:5432/itversity_retail_db"
    )

    # Load DataFrame into PostgreSQL table
    df.to_sql("weather_summary", engine, if_exists="replace", index=False)
    print("Success! Data loaded into PostgreSQL database table 'weather_summary'.")


if __name__ == "__main__":
    load_gold_to_postgres()