# k8-CICD
# Kubernetes CI/CD Example

This repository contains an example of a CI/CD pipeline for deploying a Node.js application to a Kubernetes cluster using AWS services.

## Project Structure

├── app.js 
├── buildspec.yml 
├── deployment.yaml 
├── Dockerfile 
├── package.json 
├── pipeline.json 
├── README.md 
└── lambda-deploy/lambda_function.py

## Files

- **app.js**: The main Node.js application file.
- **buildspec.yml**: The build specification file for AWS CodeBuild.
- **deployment.yaml**: The Kubernetes deployment and service configuration.
- **Dockerfile**: The Dockerfile for building the application image.
- **package.json**: The Node.js package configuration file.
- **pipeline.json**: The AWS CodePipeline configuration file.
- **lambda-deploy/lambda_function.py**: The AWS Lambda function for updating the Kubernetes deployment.

## CI/CD Pipeline

The CI/CD pipeline is defined in `pipeline.json` and consists of three stages:

1. **Source**: Retrieves the source code from AWS CodeCommit.
2. **Build**: Builds the Docker image using AWS CodeBuild.
3. **Deploy**: Deploys the Docker image to the Kubernetes cluster using an AWS Lambda function.

## Deployment

The deployment is defined in `deployment.yaml` and includes a Kubernetes Deployment and Service. The Deployment runs two replicas of the Node.js application, and the Service exposes the application using a LoadBalancer.

## Lambda Function

The Lambda function (`lambda-deploy/lambda_function.py`) updates the Kubernetes deployment with the new Docker image. It is triggered by the CodePipeline after the build stage.

## Running Locally

To run the application locally:

1. Install dependencies:
    ```sh
    npm install
    ```

2. Start the application:
    ```sh
    npm start
    ```

The application will be available at `http://localhost:3000`.

## License

This project is licensed under the MIT License.