
def get_client(client, location='EU'):
    return client.Client(location=location)

def get_job_config(client, output_table):
    return client.QueryJobConfig(destination=output_table, write_disposition='WRITE_TRUNCATE')

#Really crude rules engine. Just to build out architecture prototype!!
def rule_engine(switch):
    if switch == 1:
        return "select rental_id, end_station_id, start_station_id, temporary as end_temp from `bigquery-public-data.london_bicycles.cycle_hire` a left join `bigquery-public-data.london_bicycles.cycle_stations` b on a.end_station_id = b.id"
    if switch == 2:
        return "select rental_id, end_station_id, start_station_id, end_temp, temporary as start_temp from `udemy-course-292015.design_test.end_temp` a left join `bigquery-public-data.london_bicycles.cycle_stations` b on a.start_station_id = b.id"

def run_query(bigquery, sql, output):
    client = get_client(bigquery)

    job_config = get_job_config(bigquery, output)

    # Start the query, passing in the extra configuration.
    query_job = client.query(sql, job_config=job_config)  # Make an API request.
    query_job.result()  # Wait for the job to complete.

    print("Query pre-prod results loaded to the table {}".format(output))


def create_table_name(project, dataset, table_prefix, table_name):
    return f"{project}.{dataset}.{table_prefix}_{table_name}"
