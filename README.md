# **Quokka QR Engine App**

A simple web application built with Flask for generating QR codes

## **Table of Contents**
- [**Quokka QR Engine App**](#quokka-qr-engine-app)
  - [**Table of Contents**](#table-of-contents)
  - [**Project Description**](#project-description)
  - [**Getting Started**](#getting-started)
    - [**Prerequisites**](#prerequisites)
    - [**Installation**](#installation)
  - [**Usage**](#usage)
  - [**Deployment**](#deployment)
  - [**Built With**](#built-with)
  - [**License**](#license)
  - [**Acknowledgements**](#acknowledgements)

## **Project Description**

Originally a Tkinter app, this QR generator was used to generate QR codes for lab inspections, as the online lab form inspections used in the company I used to work for did not have a built in QR code generator. 

Lab technicians and scientists also did not want to bookmark all the different labs with their custom form logic on their mobile devices, and while the use of QR codes was up for discussion, many people did not trust the free QR code generators available on the internet for various reasons.

This Tkinter app has since evolved into a web application that allows users of the site to generate QR codes. The functionality and interface is simple, where they can enter a link name and URL, after which the application generates a QR code that can be downloaded, screenshotted, etc for use.

## **Getting Started**

To run the project locally, follow the steps below:

### **Prerequisites**
- Python 3.x
- Flask

Install Flask by running the following command:

```pip install Flask```

### **Installation**
1. Clone the repository:

   ```git clone https://github.com/your-username/quokka-qr-code-generator.git```
2. Navigate to the project directory:

    ```cd quokka-qr-code-generator```
3. Set up a virtual environment(recommended but not required):

    ```python3 -m venv venv```

    ```source venv/bin/activate```
4. Install the project dependencies:

    ```pip install -r requirements.txt```
## **Usage**
5. Start the Flask development server:

    ```flask run```
6. Open a web browser and navigate to 'http://localhost:8080' to access the application
7. Enter the link name and URL in the form fields
8. Click the "Generate QR Code"
9. The QR code image will be displayed on the screen. At this point you can either right click on the image and choose "Save Image As" to download it or you can use a screenshotting tool to save it and later crop.
## **Deployment**
10. Set up a GKE cluster and make sure you have the necessary permissions and credentials to deploy to it.
11. Create a Docker image of the application using the provided Dockerfile.
    
    ```docker build -t quokka-qr-code-generator```
    * Note: The tag can be named anything
12. Push the Docker image to a container registry (ie. Docker Hub, Google Container Registry, Amazon Elastic Container Registry, Azure Container Registry)
    
    ```docker tag quokka-qr-code-generator gcr.io/<project-name-here>/quokka-qr-code-generator```

    ```docker push gcr.io/<project-name-here>/quokka-qr-code-generator```
13. Deploy the application to GKE using the provided Kubernetes deployment configuration file ('quokka-engine.yaml')

    ```kubectl apply -f quokka-engine.yaml```
14. Expose the deployed service to an external IP address.

    ```kubectl expose deployment quokka-qr-gke --type=LoadBalancer --port=80 --target-port=8080```

15. Access the application using the assigned external IP address.

## **Built With**
- Flask - Web framework used for the application
- Google Cloud Platform - Cloud platform used for hosting and deployment
- Google Cloud Build - CI/CD pipeline integrated with Github to streamline deployment and minimize manual input (see: cloudbuild.yaml)

## **License**
This project is licensed under the MIT License.
## **Acknowledgements**
- QR code generation library: pyqrcode

Additionally, I would like to thank the open-source community and developers of the libraries, frameworks, and tools that were used in this project. Their hard work have been instrumental in making this project possible.