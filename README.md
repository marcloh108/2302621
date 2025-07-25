# Docker Web Server Project

This project sets up a simple web server using Nginx and Docker Compose. It serves static files and includes basic authentication.

## Project Structure

```
docker-webserver-project
├── nginx
│   ├── nginx.conf        # Configuration file for Nginx
│   └── html
│       └── index.html    # Default HTML file served by Nginx
├── docker-compose.yml     # Docker Compose configuration
├── .env                   # Environment variables for authentication
└── README.md              # Project documentation
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```
   cd docker-webserver-project
   ```

3. Create a `.env` file with the following content:
   ```
   USERNAME=admin
   PASSWORD=2302621@sit.singaporetech.edu.sg
   ```

### Running the Project

To start the web server, run the following command in the project directory:

```
docker-compose up
```

This command will build the Nginx container and start the web server.

### Accessing the Web Server

Open your web browser and go to `http://localhost`. You should see the content of `index.html`.

### Stopping the Project

To stop the running containers, press `CTRL+C` in the terminal where the containers are running, or run:

```
docker-compose down
```

### Notes

- Ensure that the ports specified in `docker-compose.yml` are not in use by other applications.
- Modify the `nginx.conf` and `index.html` files as needed to customize your web server.