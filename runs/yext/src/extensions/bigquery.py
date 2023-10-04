from google.cloud import bigquery
from src.operators.reader import read, get_config


def format_schema(schema):
    formatted_schema = []
    for row in schema:
        if row["type"] == "RECORD":
            fields = format_schema(row["fields"])
            formatted_schema.append(bigquery.SchemaField(row['name'], row['type'], mode=row['mode'], fields=fields))
        else:
            formatted_schema.append(bigquery.SchemaField(row['name'], row['type'], mode=row['mode']))   
    return formatted_schema


def write(json_object):
    config = get_config()
    table_schema = read("static/schemas/store_hours.json")

    project_id = config["bigquery"]["project"]
    dataset_id = config["bigquery"]["dataset"]
    table_id = config["bigquery"]["table"]

    client  = bigquery.Client(project = project_id)
    dataset  = client.dataset(dataset_id)
    table = dataset.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.schema = format_schema(table_schema)
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    job = client.load_table_from_json(json_object, table, job_config = job_config)

    print(job.result())