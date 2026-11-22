pipeline {
    agent any

    environment {
        IMAGE_NAME = "workout-boredom-buster"
        CONTAINER_NAME = "workout-app"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/cygday/boredom-buster.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                // Scans the image and fails the build if CRITICAL vulnerabilities are found
                sh 'trivy image --exit-code 1 --severity CRITICAL ${IMAGE_NAME}:${BUILD_NUMBER}'
            }
        }

        stage('Deploy Container') {
            steps {
                // Stop and remove old container if it exists, then start the new one
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }
    }
}
