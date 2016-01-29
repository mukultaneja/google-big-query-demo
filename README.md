Google Big Query Database Interaction Demo

Table of contents

* What is BigQuery
* BigQuery Authentication
* Public/Private Key Pair
* Code Walk-through

What is BigQuery

Refer below link to know about BigQuery.

https://cloud.google.com/bigquery/what-is-bigquery

BigQuery Authentication

The BigQuery API requires all requests to be authenticated as a user or a service account. This guide describes how to perform authentication through service account using Google OAuth 2.0 authentication service.

Please refer below link to know about ‘What is a service account?’ and ‘How to create a service account?’

https://developers.google.com/identity/protocols/OAuth2ServiceAccount

Public/Private Key Pair

After creating the service account a new public/private key pair has been generated. This pair can be stored in two different formats which are JSON and P12. JSON is the preferable format over P12 and the main difference which should be highlighted apart from their encodings is that we do not need to read 
JSON file for the credentials in our programs. Instead of reading the file we can use an environment variable named 'GOOGLE_APPLICATION_CREDENTIALS' which will store the path for JSON file and read it automatically when is needed. It is more manageable option that is why JSON format is a recommending to store credentials.

Code Walk-through

There are two files named 'bigqueryv1.py' and 'bigqueryv2.py' which works as an application and authenticates itself over the BigQuery Database servers using service account. You all can create a service account with the above steps and change the account and project details in the program according to your own details.

The version 1 of bigquery python file is using credentials stored in P12 format file. As earlier I described for this format our program should be able to read the file and fetch the key from it.

The version 2 of bigquery python file is using credentials stored in JSON format file where we need not to read the file to fetch the key instead we have to add an environment variable 'GOOGLE_APPLICATION_CREDENTIALS' which will store the path of the JSON file.
