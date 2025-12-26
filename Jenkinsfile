pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh 'docker build -t py-app .'
                }
            }
        }

        stage('Run Unit Tests in Docker') {
            steps {
                script {
                    sh 'docker run --rm py-app'
                }
            }
        }
    }

    post {
        success {
            echo '🎉 CI PASSED — Build và test thành công!'
        }
        failure {
            echo '❌ CI FAILED — Kiểm tra lại code hoặc test!'
        }
    }
}
