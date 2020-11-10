from google.cloud import bigquery
from rule_engine import get_client, get_job_config, rule_engine, run_query, create_table_name

def transformation_2(project, dataset, table_prefix):
    sql = rule_engine(2)
    table_name = "start_end_temp"
    output = create_table_name(project, dataset, table_prefix, table_name)
    run_query(bigquery, sql, output)