pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-demo"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub'
            }
        }

        stage('Verify Environment') {
            steps {
                sh 'python3 --version'
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images'
            }
        }
    }
}
