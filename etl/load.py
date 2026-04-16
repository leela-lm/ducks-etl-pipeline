from google.cloud import bigquery

def load_to_bigquery(records, table_id):
    client = bigquery.Client()

    query = f"TRUNCATE TABLE `{table_id}`"
    client.query(query).result()


    errors = client.insert_rows_json(table_id, records)

    if errors:
        print("Insert errors:", errors)
        raise Exception("BigQuery insert failed")