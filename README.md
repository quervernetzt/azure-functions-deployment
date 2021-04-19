# Deployment of a Python Azure Function

- This solution serves as example on how to deploy a Python Azure Function (running on Premium Plan) using an Azure DevOps YAML pipeline

# Prerequisites

- `.\deployment\templates\variables\global.yml` updated with the required values

- Azure DevOps Project

- A service connection between Azure DevOps and an Azure Subscription

- The code available in a repo in the project and a pipeline pointing to `./deployment/pipeline/main.yml`



# Resources

[Continuous delivery by using Azure DevOps](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops?tabs=python)