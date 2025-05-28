pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
        GENERIC_URL = "https://the-internet.herokuapp.com/"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/mystikyatra/automation-test-web-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'login-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    writeFile file: '.env', text: """
                        BASE_URL=${env.GENERIC_URL}
                        USERNAME=${USERNAME}
                        PASSWORD=${PASSWORD}
                    """
                    // Run tests, generate JUnit XML report
                    bat 'pytest tests/ --disable-warnings --junitxml=reports/test-results.xml -v'
                }
            }
        }
    }

    post {
        always {
            // Publish test results to Jenkins UI
            junit 'reports/test-results.xml'

            // Archive logs and videos
            archiveArtifacts artifacts: 'logs/*.log', allowEmptyArchive: true
            archiveArtifacts artifacts: 'videos/test_run.mp4', fingerprint: true, allowEmptyArchive: true
        }
    }
}