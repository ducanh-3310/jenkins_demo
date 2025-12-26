pipeline {
    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Unit Tests (Python)') {
            steps {
                sh 'python3 -m unittest -v unit_test.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t py-app .'
            }
        }

        stage('Run Docker Image') {
            steps {
                sh '''
                docker rm -f py-app-container || true
                docker run -d -p 8080:5000 --name py-app-container py-app
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 SUCCESS: Pipeline completed'
        }
        failure {
            echo '❌ FAILED: Pipeline error, check logs'
        }
    }
}
