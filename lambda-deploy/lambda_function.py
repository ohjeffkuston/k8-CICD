import json
import os
from kubernetes import client, config

def lambda_handler(event, context):
    # Load image URI from CodeBuild artifact
    image_uri = event['Records'][0]['s3']['object']['key']
    with open('/tmp/imageDetail.json', 'r') as f:
        image_data = json.load(f)
    new_image = image_data['ImageURI']

    # Load kubeconfig from environment or default
    config.load_incluster_config()  # Assumes Lambda runs in EKS with proper IAM role
    v1 = client.AppsV1Api()

    # Update deployment
    deployment = v1.read_namespaced_deployment("kubernetes-cd-example", "default")
    deployment.spec.template.spec.containers[0].image = new_image
    v1.patch_namespaced_deployment("kubernetes-cd-example", "default", deployment)

    return {
        'statusCode': 200,
        'body': json.dumps(f"Updated deployment with image: {new_image}")
    }