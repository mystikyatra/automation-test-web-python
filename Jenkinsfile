pipeline {
    agent any
    environment {
        PATH = "${env.PATH}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/mystikyatra/automation-test-web-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest tests/ --maxfail=1 --disable-warnings'
            }
        }

        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: 'logs/*.log', allowEmptyArchive: true
            }
        }
    }
}