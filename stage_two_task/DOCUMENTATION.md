## API Documentation

This documentation provides an overview of the API endpoints, the standard formats for requests and responses, sample usage, and instructions for setting up and deploying the API. 

The API allows adding, fetching, updating, and deleting person records.

Endpoints

1. **Create Endpoint**

    * URL: /api
    * Method: POST
    * Description: Adds a new person to the database.
    * Request Format:
   
       *  Content-Type: application/json or query parameter name
   
        * Body (JSON): json
```
    {
      "name": "John Doe"
    }

```
Response Format:

    Content-Type: application/json
    Body (Successful Response):
    json

    {
      "user_id": 1,
      "name": "John Doe"
    }

    Status Code: 201 (Created)

Possible Errors:

    Status Code: 400 (Bad Request)
        Body:json

    {
      "message": "Name is required"
    }

Status Code: 405 (Method Not Allowed)

    Body: json

            {
              "message": "Incorrect HTTP verb"
            }

2. **Read, Update, Delete Endpoint**

    * URL: /api
    * Methods: GET, PUT, DELETE
    * Description:
        * GET: Fetches details of a person by user ID or name.
        * PUT: Modifies details of a person by user ID or name.
        * DELETE: Removes a person by user ID or name.
   *  Request Format:
   
        Content-Type: application/json or query parameters user_id or name
   *  Response Format:
      Content-Type: application/json
    * Possible Errors:
      * Status Code: 401 (Unauthorized)
              Body: json

    ``` 
        {
            "message": "Person matching these values does not exist."
        }
   ```

   * Status Code: 400 (Bad Request)

       Body: json
        ```
            {
         "message": "Person does not exist"
       }
     ```

    * Status Code: 405 (Method Not Allowed)
    
      Body: json
```
            {
              "message": "Incorrect HTTP verb"
            }
 ```

##### **Sample Usage**
1. **Create Endpoint**

**Request:** POST /api

**Content-Type:** 
application/json

```{
  "name": "John Doe"
}
```

**Response:** http

HTTP/1.1 201 Created

**Content-Type:** 
application/json

```{
  "user_id": 1,
  "name": "John Doe"
}
```

2. **Read Endpoint**

**Request:** GET /api?user_id=1

**Response:** http

HTTP/1.1 200 OK

**Content-Type:** 
application/json

```{
  "user_id": 1,
  "name": "John Doe"
}
```

**Update Endpoint**

**Request:** PUT /api?user_id=1

**Content-Type:**
application/json

```{
  "name": "Jane Smith"
}
```

**Response:**
http

HTTP/1.1 200 OK

**Content-Type:** application/json

```{
  "user_id": 1,
  "name": "Jane Smith"
}
```
**Delete Endpoint**

**Request:**
DELETE /api?user_id=1

**Response:**
http

HTTP/1.1 202 Accepted

**Content-Type:** application/json

```
{
  "message": "Person has been successfully deleted."
}
```

**Limitations and Assumptions**

    - The API assumes the usage of a relational database (SQLite in the provided example) and relies on SQLAlchemy as the ORM.
    - The API assumes that the Person model has been defined properly with necessary constraints.
    - The API assumes that the database connection and configuration are set up correctly.
    - The API does not provide authentication or authorization mechanisms. It assumes that the endpoints are accessible to all users.
    - The API does not handle validation for input parameters beyond basic checks (e.g., checking for the existence of a name).
    - The API does not implement pagination for fetching multiple person records.

**Setting Up and Deploying the API**

To set up and deploy the API locally or on a server, follow these steps:

    - Ensure you have Python installed (version 3.6 or higher).
    - Create a virtual environment (optional but recommended).
    - Install the required dependencies by running pip install -r requirements.txt.
    - Set the FLASK_APP environment variable to app.py (e.g., export FLASK_APP=app.py).
    - Create the SQLite database by running the command flask db_create.
    - (Optional) Seed the database with sample data by running the command flask db_seed.
    - Startthe API by running flask run.
    - The API should now be accessible at http://localhost:5000/api for local development.

**Note:**

If you plan to deploy the API to a server, you will need to configure the server environment and update the necessary settings (e.g., database connection) accordingly.