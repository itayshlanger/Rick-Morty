# Rick and Morty API Application

## Overview
This project interacts with the Rick and Morty API to fetch character data and expose it through a Flask based REST API. The project also includes Dockerization, Kubernetes, and a Helm chart for deployment.

## Features
1. Fetches and filters character data based on:
   - Species: Human
   - Status: Alive
   - Origin: Earth
2. Saves the data to a CSV file (Example located at /app/rick_and_morty_characters.csv).
3. Exposes a REST API to:
   - /characters: Returns the data as JSON.
   - /healthcheck: Verifies application health.

## REST API Endpoints
1. /characters:
   - Description: Returns all filtered characters as JSON.
   - Example Response:
    ```
    [
      {
        "Name": "Rick Sanchez",
        "Location": "Earth",
        "Image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg"
      },
      ...
    ]
    ```

2. /healthcheck:
   - Description: Confirms the API is healthy.
   - Example Response:
    ```
    { "status": "healthy" }
    ```

## Setup and Usage

### 1. Docker Deployment
- App files located at /app

- Build the Docker image:
 ```
 docker build -t rick-and-morty-api .
 ```
- Run the container:
 ```
 docker run -d -p 5000:5000 rick-and-morty-api
 ```
- Test container
 ```
 127.0.0.1:5000/<desired-api-endpoint>
 ```

### 2. Kubernetes Deployment
- Kubernetes YAML files are located in the yamls/ directory:
  - Deployment.yaml
  - Service.yaml
  - Ingress.yaml

### Deploy Steps:
1. Start Minikube and Enable Ingress Addon:
    ``` 
    minikube start
    ```
    ```
    minikube addons enable ingress
    ```
2. Apply yamls:
    ```
    kubectl apply -f yamls/
    ```
3. Check status
    ```
    kubectl get all
    ```
4. Add Host to /etcd/hosts
    ```txt
    127.0.0.1 rick-and-morty.local
    ```
    ( Can be changed at yamls/ingress.yaml )

5. Access with minikube tunnel
    ```
    minikube tunnel
    ```
    
    Test at -

    ```
    http://<your-host>/<desired-api-endpoint>
    ```

### 3. Helm Deployment
- Helm chart is located in the rick-and-morty-api/ directory.

### Deploy Steps:
1. Install Helm chart:
    ```
    helm install rick-and-morty ./rick-and-morty-api
    ```
2. Check deployment status:
    ```
    kubectl get all
    ```
