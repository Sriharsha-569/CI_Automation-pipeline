/*
 * Study Project: DevOps & Continuous Integration
 * Tool: Jenkins
 * Purpose: Demonstrate a CI workflow with Jenkins (Checkout → Build → Test → Report → Deploy)
 *
 * Author: Sri Harsha Deep Chilakalapudi
 * Seminar: Concepts & Tools for Application Development
 * Date: 02 July 2025
 */


pipeline {
    agent any

    environment {
        APP_NAME = "Weather App"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out ${APP_NAME} code from GitHub..."
                git branch: 'main', url: 'https://github.com/Sriharsha-569/Weather_A.git'
            }
        }

        stage('Build') {
            steps {
                echo "Building ${APP_NAME}..."
                // Simulate a build step
                sh 'echo Building files...'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests for ${APP_NAME}..."
                // Simulate test execution
                sh 'echo Running unit tests...'
            }
        }
        
       stage('Report') {
            steps {
               echo "Generating test report for ${APP_NAME}..."
               sh 'echo Test report generated successfully!'
            }
        }
       stage('Deploy') {
            steps {
                echo "Deploying ${APP_NAME} update..."
                // Simulate deployment
                sh 'echo Deploying to production server...'
            }
        }
    }

    post {
        success {
            echo "${APP_NAME} update pipeline completed successfully!"
        }
        failure {
            echo "Something went wrong with ${APP_NAME} update pipeline!"
        }
    }
}
