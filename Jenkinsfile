pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Varunkedar003/blue-green.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t blue-green-app ./app'
            }
        }

    }
}
