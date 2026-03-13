pipeline {
    agent any

    environment {
        IMAGE_NAME = "varunmb/blue-green-app"
        BLUE_IP = "15.206.149.116"
        GREEN_IP = "65.0.19.164"
        LOAD_BALANCER = "13.201.192.75"
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
                    ACTIVE = sh(
                        script: "ssh -i /var/jenkins_home/ci-cd.pem ubuntu@${LOAD_BALANCER} \"grep server /etc/nginx/sites-available/app.conf\"",
                        returnStdout: true
                    ).trim()

                    if (ACTIVE.contains(env.BLUE_IP)) {
                        env.TARGET = env.GREEN_IP
                        env.OLD = env.BLUE_IP
                    } else {
                        env.TARGET = env.BLUE_IP
                        env.OLD = env.GREEN_IP
                    }

                    echo "Deploying to ${env.TARGET}"
                }
            }
        }

        stage('Deploy New Version') {
            steps {
                sh '''
                ANSIBLE_HOST_KEY_CHECKING=False \
                ansible-playbook ansible/deploy-green.yml \
                -i ansible/inventory.ini \
                --private-key=/var/jenkins_home/ci-cd.pem
                '''
            }
        }

        stage('Health Check') {
            steps {
                script {
                    sh """
                    echo "Checking health of ${env.TARGET}"
                    curl -f http://${env.TARGET}:5000/health
                    """
                }
            }
        }

        stage('Switch Traffic') {
            steps {
                sh """
                ssh -i /var/jenkins_home/ci-cd.pem ubuntu@${LOAD_BALANCER} \
                "sudo sed -i 's/${env.OLD}/${env.TARGET}/' /etc/nginx/sites-available/app.conf && sudo systemctl reload nginx"
                """
            }
        }
    }
}
