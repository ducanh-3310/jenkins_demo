pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }

         stage('run deno.py') {
            steps {
                sh 'python3 deno.py'
            }
        }
    }
}
