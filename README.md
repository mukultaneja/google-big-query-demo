Google Big Query Database Interaction Demo


Table of contents

1. What is BigQuery
2. BigQuery Authentication
    A. What is service account
    B. Creating a service account
3. Public/Private Key Pair
4. Code Walk-through


What is BigQuery

Querying massive datasets can be time consuming and expensive without the right hardware and infrastructure. Google BigQuery
solves this problem by enabling super-fast, SQL queries against append-only tables, using the processing power of Google's
infrastructure. Google gives us the ability where we can move our data into BigQuery and then it handles all the hard work
on its own. We can control access to both the project and our data based on our business needs, such as giving others the ability
to view or query our data.

We can access BigQuery by using a web UI or a command-line tool, or by making calls to the BigQuery REST API using a
variety of client libraries such as Java, .NET or Python. There are also a variety of third-party tools that we can use
to interact with BigQuery, such as visualizing the data or loading the data.


BigQuery Authentication

The BigQuery API requires all requests to be authenticated as a user or a service account. This guide describes how to
perform authentication through service account using Google OAuth 2.0 authentication service.

    What is service account

        The Google OAuth 2.0 system supports server-to-server interactions such as those between a web application and a Google service.
        Service account is the medium by which we can make this interaction happen. It is an account which belongs to the web application
        instead of to an individual end user. The application calls Google APIs on behalf of the service account, so users aren't directly
        involved. This scenario is sometimes called "two-legged OAuth," or "2LO." (The related term "three-legged OAuth" refers to scenarios
        in which the application calls Google APIs on behalf of end users, and in which user consent is sometimes required.)

        Typically, an application uses a service account when the application uses Google APIs to work with its own data rather than a
        user's data. For example, an application that uses Google Cloud Datastore for data persistence would use a service account to
        authenticate its calls to the Google Cloud Datastore API.

        To support server-to-server interactions, first create a service account for a project in the Developers Console.
        Then, the application prepares to make authorized API calls by using the service account's credentials to
        request an access token from the OAuth 2.0 auth server.Finally, the application can use the access token to call Google APIs.


    Creating a service account

        A service account's credentials include a generated email address that is unique and at least one public/private key pair.
        If the application runs on Google App Engine, a service account is set up automatically when we create our project.
        If the application runs on Google Compute Engine, a service account is also set up automatically when we create our project,
        but we must specify the scopes that the application needs access to when we create a Google Compute Engine instance.
        If the application doesn't run on Google App Engine or Google Compute Engine, we can get these credentials in the
        Google Developers Console. To generate service-account credentials, or to view the public credentials that you've
        already generated, do the following:

        1. Login into Google Developer Console using google email address and password.
        2. Go to https://console.developers.google.com/permissions which is Developers Console's Permissions page. If we dont have a
           project then it asks for making a new project otherwise it will direct to the permission page.
        3. Open the Service accounts section of the Developers Console's Permissions page.
        4. Click Create service account.
        5. In the Create service account window, type a name for the service account and select Furnish a new private key. Then, click Create.


        A new public/private key pair is generated and downloaded to local machine; it serves as the only copy of this key and should be responsibly
        stored for security purpose.

    Public/Private Key Pair

        After creating the service account a new public/private key pair has been generated. These pairs can be stored in two different formats
        which are JSON and P12. JSON is the preferable format over P12. The main difference which should be highlighted apart from their encodings
        is that we do not need to read JSON file for the credentials in our programs. Instead of reading the file we can use an environment variable
        'GOOGLE_APPLICATION_CREDENTIALS' which will store the path for JSON file and read it automatically when is needed. It is more manageable option
        that is why JSON format is a recommending to store credentials.

    Code Walk-through

        There are two files named 'bigqueryv1.py' and 'bigqueryv2.py' which works as an application and authenticates itself over the
        bigquery database servers using service account. You all can create a service account with the above steps and change the account
        and project details in the program according to your own details.

        The version 1 of bigquery python file is using credentials stored in P12 format file so as earlier I described for this format our
        program should be able to read the file and fetch the key from it.

        The version 2 of bigquery python file is using credentials stored in JSON format file where we need not to read the file to fetch the
        key instead we have to add an environment variable 'GOOGLE_APPLICATION_CREDENTIALS' which will store the path of the JSON file.
