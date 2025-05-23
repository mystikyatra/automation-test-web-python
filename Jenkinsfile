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
//                 withCredentials([usernamePassword(credentialsId: 'login-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
//                     bat """
//                         set BASEURL=https://www.saucedemo.com/v1/
//                         set USERNAME=%USERNAME%
//                         set PASSWORD=%PASSWORD%
//                         pytest tests/ --maxfail=1 --disable-warnings
//                     """
//                 }
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
                withCredentials([usernamePassword(credentialsId: 'login-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat """
                        set BASEURL=https://www.saucedemo.com/v1/
                        set USERNAME=%USERNAME%
                        set PASSWORD=%PASSWORD%
                        pytest tests/ -n 2 --maxfail=1 --disable-warnings
                    """
                }
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
