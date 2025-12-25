pipeline {						
    agent any						
						
    tools {						
        jdk 'jdk17'        // hoặc jdk8 / jdk11 tùy project						
    }						
						
    stages {						
						
        stage('Checkout Source') {						
            steps {						
                echo '🔄 Checkout Source Code'					
            }						
        }						
						
        stage('Build & Test') {						
            steps {						
                					
            }						
        }						
										
    }						
						
    post {						
        success {						
            archiveArtifacts artifacts: 'target/*.jar', fingerprint: true						
            echo '✅ Build JAR SUCCESS'						
        }						
						
        failure {						
            echo '❌ Build FAILED'						
        }						
    }						
}						
