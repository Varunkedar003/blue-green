pipeline {
    agent any

    environment {
        IMAGE_NAME = "varunmb/blue-green-app"
        BLUE_IP = "15.206.149.116"
        GREEN_IP = "65.0.19.164"
        LB_IP = "13.201.192.75"
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

        stage('Detect Active Environment') {
            steps {
                script {

                    def active = sh(
                        script: """
                        ssh -i /var/jenkins_home/ci-cd.pem ubuntu@$LB_IP \
                        "grep server /etc/nginx/sites-available/app.conf"
                        """,
                        returnStdout: true
                    ).trim()

                    if (active.contains(BLUE_IP)) {
                        env.TARGET_IP = GREEN_IP
                        env.TARGET = "GREEN"
                    } else {
                        env.TARGET_IP = BLUE_IP
                        env.TARGET = "BLUE"
                    }

                    echo "Current active: ${active}"
                    echo "Deploying to: ${TARGET}"
                }
            }
        }

        stage('Deploy to Target Server') {
            steps {
                sh """
                ANSIBLE_HOST_KEY_CHECKING=False \
                ansible-playbook ansible/deploy-green.yml \
                -i ansible/inventory.ini \
                --limit ${TARGET_IP} \
                --private-key=/var/jenkins_home/ci-cd.pem
                """
            }
        }

        stage('Health Check') {
            steps {
                sh """
                echo Checking health of ${TARGET_IP}
                curl -f http://${TARGET_IP}:5000/health
                """
            }
        }

        stage('Switch Traffic') {
            steps {
                sh """
                ssh -i /var/jenkins_home/ci-cd.pem ubuntu@$LB_IP \
                "sudo sed -i 's/${BLUE_IP}/${TARGET_IP}/g' /etc/nginx/sites-available/app.conf && sudo sed -i 's/${GREEN_IP}/${TARGET_IP}/g' /etc/nginx/sites-available/app.conf && sudo systemctl reload nginx"
                """
            }
        }
    }
}
