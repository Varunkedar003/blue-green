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

        stage('Deploy to Green Server') {
            steps {
                sh '''
                ANSIBLE_HOST_KEY_CHECKING=False \
                ansible-playbook ansible/deploy-green.yml \
                -i ansible/inventory.ini \
                --private-key=/var/jenkins_home/ci-cd.pem
                '''
            }
        }

        stage('Switch Traffic to Green') {
    steps {
        sh '''
        ssh -i /var/jenkins_home/ci-cd.pem ubuntu@13.201.192.75 "sudo ln -sf /etc/nginx/conf.d/green.conf /etc/nginx/sites-enabled/default && sudo nginx -t && sudo systemctl reload nginx"
        '''
    }
}
    }
}
