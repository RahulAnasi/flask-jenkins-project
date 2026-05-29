pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-demo"
    }

    stages {

        stage('GitHub Checkout') {
            steps {
                sh 'echo "Code pulled from GitHub"'
            }
        }

        stage('Environment Check') {
            steps {
                sh 'python3 --version'
                sh 'docker --version'
            }
        }

        stage('Project Files') {
            steps {
                sh 'ls -la'
            }
        }
    }
}
