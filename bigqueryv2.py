'''
- Go to https://console.developers.google.com/apis/credentials
- Pick an existing project or create a new project
- Select New credentials > Service account key and select a New service account. (Fill in any name and account ID)
- Ensure that the environment variable GOOGLE_APPLICATION_CREDENTIALS points to the downloaded credentials file
- Replace project_id in this program with the project_id from your downloaded credentials
'''

from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
import pandas as pd

class BigQuery(object):
    def __init__(self):
        self.credentials = GoogleCredentials.get_application_default()
        self.bigquery = build('bigquery', 'v2', credentials=self.credentials)

    def query(self, project_id, query):
        jobs = self.bigquery.jobs()
        response = jobs.query(projectId=project_id, body={'query': query}).execute()
        data = pd.DataFrame([cell['v'] for cell in row['f']] for row in response['rows'])
        data.columns = [col['name'] for col in response['schema']['fields']]
        for col in response['schema']['fields']:
            col_name = col['name']
            if col['type'] == 'INTEGER':
                data[col_name] = data[col_name].dropna().astype(int)
            elif col['type'] == 'BOOLEAN':
                data[col_name] = data[col_name].dropna().astype(bool)
            elif col['type'] == 'FLOAT':
                data[col_name] = data[col_name].dropna().astype(float)
        return data

if __name__ == '__main__':
    # Fill the project_id from your credentials json file
    project_id = 'ferrous-thought-120112'
    query = "SELECT year, state, is_male, child_race, avg(plurality) as pl FROM publicdata:samples.natality " \
            "GROUP BY year, state, is_male, child_race, plurality"
    con = BigQuery()
    data = con.query(project_id, query)
    data.to_csv('natality.csv')
