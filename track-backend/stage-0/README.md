## Stage-0
**Task Description**  
Develop a public API that returns the following information in JSON format:  

1.  **Your registered email address**  (used to register on the HNG12 Slack workspace).
2.  **The current datetime**  as an ISO 8601 formatted timestamp.
3.  **The GitHub URL**  of the project's codebase.

**Requirements**  

1.  Technology Stack:
2.  **Programming Language/Framework:**  Use any of the following: See Sharp (C#), PHP, Python, Go, Java, JavaScript/TypeScript.
3.  **Deployment:**  The API must be deployed to a publicly accessible endpoint.
4.  **CORS Handling:**  Ensure the API handles Cross-Origin Resource Sharing (CORS) appropriately.
5.  **Response Format:**  All responses must be in JSON format.

**API Specification**  

-   Endpoint:  `GET** <your-url>`
-   Required JSON Response Format (200 OK):
	```
	{ "email": "your-email@example.com", "current_datetime": "2025-01-30T09:30:00Z", "github_url": "<[https://github.com/yourusername/your-repo](https://github.com/yourusername/your-repo)>" }
	```

