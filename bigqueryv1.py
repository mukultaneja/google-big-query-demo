
import httplib2
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd

class BigQueryConnector(object):

    def __init__(self):
        # these details should be changed according to service account
        self.PROJECT_NUMBER = '458519335866'
        self.SERVICE_ACCOUNT_EMAIL = 'mukul253@ferrous-thought-120112.iam.gserviceaccount.com'
        self.PROJECT_ID = 'ferrous-thought-120112'
        self.SERVICE_SCOPE = 'https://www.googleapis.com/auth/bigquery'

        # reading the P12 format file to fetch key
        with open('My Project-8ddc2329ab50.p12', 'rb') as f:
            self.KEY = f.read()

    def get_service_authentication(self):
        credentials = SignedJwtAssertionCredentials(self.SERVICE_ACCOUNT_EMAIL, self.KEY, scope=self.SERVICE_SCOPE)
        # creating http request object
        http = httplib2.Http()
        # request for authentication to server
        http = credentials.authorize(http)
        return build('bigquery', 'v2', http=http)

    def get_natality_query(self):
        query = 'SELECT year, state, is_male, child_race, avg(plurality) as pl FROM publicdata:samples.natality GROUP BY' \
                ' year, state, is_male, child_race, plurality'
        return {
            'query': query,
            'timeoutMs': 200
        }

    def get_response(self):
        try:
            service = self.get_service_authentication()
            query_data = self.get_natality_query()
            job_object = service.jobs()
            response = job_object.query(projectId=self.PROJECT_ID, body=query_data).execute(num_retries=5)
            if response:
                return self.convert_response_to_csv(response)
            return response

        except KeyError as e:
            raise KeyError(e.__str__())
        except Exception as e:
            raise Exception(e.__str__())

    def convert_response_to_csv(self, response):
        try:
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

            data.to_csv('natility.csv', encoding='utf-8')
            return True

        except KeyError as e:
            raise KeyError(e.__str__())

if __name__ == '__main__':
    conn = BigQueryConnector()
    try:
        response = conn.get_response()
    except Exception as e:
        print ('Error : ' + e.__str__())
        exit()

