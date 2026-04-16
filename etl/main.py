from etl.extract import fetch_chapters
from etl.transform import transform_chapters
from etl.load import load_to_bigquery
from etl.logger import logger

TABLE_ID = "ducks-etl-project.ducks_dataset.ducks_chapters_raw"


def run_pipeline():
    try:
        logger.info("Starting ETL pipeline")

        data = fetch_chapters()
        logger.info("Extract step completed")

        transformed = transform_chapters(data)
        logger.info(f"Transformed {len(transformed)} records")

        load_to_bigquery(transformed, TABLE_ID)
        logger.info(f"Loaded {len(transformed)} records into BigQuery")

        logger.info("ETL pipeline finished successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()
