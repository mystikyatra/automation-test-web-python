pipeline {
    agent any
    environment {
        PATH = "${env.PATH}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/yourusername/saucedemo_automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --maxfail=1 --disable-warnings'
            }
        }

        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: 'logs/*.log', allowEmptyArchive: true
            }
        }
    }
}
