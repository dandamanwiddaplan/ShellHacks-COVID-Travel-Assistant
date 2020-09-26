from google.cloud import bigquery as bq

def stateQuery(state) :

    client = bigquery.client
    query_job = client.query(
        """
        SELECT *
        FROM `bigquery-public-data.covid19_public_forecasts.state_14d`
        WHERE state_name = @state
        """
     return(query_job)


def countyQuery(county, state) :
    client = bigquery.client
    query_job = client.query(
        """
        SELECT *
        FROM `bigquery-public-data.covid19_public_forecasts.state_14d`
        WHERE state_name = @state 
        """
    return(query_job))