// pipeline {
//     agent any

//     environment {
//         PYTHONPATH = "${env.WORKSPACE}"
//     }

//     stages {
//         stage('Clone Repo') {
//             steps {
//                 git 'https://github.com/mystikyatra/automation-test-web-python.git'
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 bat 'pip install -r requirements.txt'
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 bat 'pytest tests/ --maxfail=1 --disable-warnings'
//             }
//         }

//         stage('Archive Logs') {
//             steps {
//                 archiveArtifacts artifacts: 'logs/*.log', allowEmptyArchive: true
//             }
//         }

//         stage('Archive Video') {
//             steps {
//                 archiveArtifacts artifacts: 'videos/test_run.mp4', fingerprint: true, allowEmptyArchive: true
//             }
//         }
//     }
// }
pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
        BASE_URL = 'https://www.saucedemo.com/v1/'
        // Inject USERNAME and PASSWORD from Jenkins credentials store
        USERNAME = credentials('login-credentials').username
        PASSWORD = credentials('login-credentials').password
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

        stage('Archive Video') {
            steps {
                archiveArtifacts artifacts: 'videos/test_run.mp4', fingerprint: true, allowEmptyArchive: true
            }
        }
    }
}
