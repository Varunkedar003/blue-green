pipeline {
    agent any

    environment {
        IMAGE_NAME = "varunmb/blue-green-app"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Varunkedar003/blue-green.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME ./app'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {

                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Switch Traffic to Green') {
            steps {
                sh '''
                ssh -i /var/jenkins_home/ci-cd.pem ubuntu@13.201.192.75 << EOF
                sudo sed -i 's/15.206.149.116/65.0.19.164/g' /etc/nginx/sites-available/default
                sudo nginx -t
                sudo systemctl reload nginx
                EOF
                '''
          }
        }
    }
}
