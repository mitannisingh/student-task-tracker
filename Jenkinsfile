pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Student Task Tracker'
                sh 'python3 -m venv .jenkins-venv'
                sh '.jenkins-venv/bin/pip install -r requirements.txt'
                sh 'mkdir -p build'
                sh 'tar -czf build/student-task-tracker-${BUILD_NUMBER}.tar.gz app.py templates requirements.txt'
                archiveArtifacts artifacts: 'build/*.tar.gz', fingerprint: true
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                sh '.jenkins-venv/bin/python -m pytest'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Checking code quality'
                sh '.jenkins-venv/bin/python -m flake8 app.py'
            }
        }

        stage('Security') {
            steps {
                echo 'Running security scan'
                sh '.jenkins-venv/bin/python -m bandit -r app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Student Task Tracker'
                sh 'docker build -t student-task-tracker:${BUILD_NUMBER} .'
            }
        }

        stage('Release') {
            steps {
                echo "Creating release ${BUILD_NUMBER}"
                sh 'docker tag student-task-tracker:${BUILD_NUMBER} student-task-tracker:latest'
            }
        }

    }
}