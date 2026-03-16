pipeline {
    agent any

    environment {
        APP_NAME = 'CI_Automation-pipeline'
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out ${APP_NAME}..."
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Checking code syntax...'
                sh 'python3 -m py_compile src/calculator.py'
                echo 'Syntax check passed.'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    pytest tests/ \
                        --verbose \
                        --cov=src \
                        --cov-report=term-missing
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t ${APP_NAME}:latest -f docker/Dockerfile .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'docker run --rm ${APP_NAME}:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed. All tests passed.'
        }
        failure {
            echo 'Pipeline failed. Check test results.'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
