# Octopus BI Intern Assessment

This repository contains a Django application integrated with Docker for easy deployment and development. The Django app is designed to manage school data.

## Prerequisites

Make sure you have the following installed on your system:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/chrk-Dev/Octopus-BI-Intern-Assessment.git
    ```

2. Navigate to the project directory:

    ```bash
    cd schoolData
    ```

3. Build the Docker containers:

    ```bash
    docker-compose build
    ```

4. Start the Docker containers:

    ```bash
    docker-compose up -d
    ```

5. Access the Django application in your web browser at [http://localhost:8000](http://localhost:8000).
