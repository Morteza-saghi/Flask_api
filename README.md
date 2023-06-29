# Flask_api
here is small api using flask in python
--------------------------------------------------------------------------------------------------
api stands for Application programming interface.
An application programming interface is a way for two or more computer programs to communicate with each other.

here are some things i learned on the way...


URI stands for Uniform Resource Identifier
URL stands for Uniform Resource Locator



REST API stands for Representational State Transfer Application Programming Interface.


API methods:

GET: to retrieve data from a server. For example, when you use a search engine to look up information, it's likely using a GET request to retrieve the data you're looking for.

POST: to send data to a server. When you fill out a form on a website and click "submit," that data is usually sent using a POST request.

PUT: to update existing data on a server. For example, if you edit your profile information on a social media site and save the changes, that data is likely sent using a PUT request.

DELETE:to delete data from a server. For example, if you remove a post or comment on a social media site, that action is likely triggered by a DELETE request.




RESTful principles:

Client-server architecture: The client and server parts of the application must be separated, allowing them to evolve independently.

Statelessness: Each request from a client to the server must contain all the necessary information for the server to understand the request, without requiring the server to keep any context about the client.

Cacheability: Responses from the server must define themselves as cacheable or non-cacheable, to allow clients to reuse responses.

Layered system: A layered system means that the client can only see one layer at a time (usually the API layer), without having any knowledge of the underlying layers.

Uniform interface: The uniform interface is the most important constraint in REST. It defines a standard way of interacting with resources through HTTP methods (GET, POST, PUT, DELETE) and resource URIs.

Code on demand (optional): This constraint allows servers to extend the functionality of clients by transferring executable code, such as JavaScript.
