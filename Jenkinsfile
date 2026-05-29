pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-demo"
        CONTAINER_NAME = "flask-app"
    }

    stages {

        stage('Verify Environment') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
            }
        }

        stage('Deploy New Container') {
            steps {
                sh '''
                docker run -d \
                --name $CONTAINER_NAME \
                -p 5000:8000 \
                $IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
                sh 'curl localhost:5000'
            }
        }
    }
}
