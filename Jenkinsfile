pipeline {
    agent any

    stages {

        stage('Build') {
    steps {
        echo 'Building Student Task Tracker'
        sh 'python3 -m venv .jenkins-venv'
        sh '.jenkins-venv/bin/python -m pip install --upgrade pip'
        sh '.jenkins-venv/bin/pip install -r requirements.txt'
        sh 'mkdir -p build'
        sh 'tar -czf build/student-task-tracker-${BUILD_NUMBER}.tar.gz app.py templates requirements.txt'
        archiveArtifacts artifacts: 'build/*.tar.gz', fingerprint: true
    }
}

        stage('Test') {
            steps {
                echo 'Running tests with coverage'
                sh '.jenkins-venv/bin/python -m pytest --cov=app --cov-report=term-missing --cov-fail-under=80'
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
        sh '/usr/local/bin/docker build -t student-task-tracker:${BUILD_NUMBER} .'
        sh '/usr/local/bin/docker rm -f student-task-tracker-app || true'
        sh '/usr/local/bin/docker run -d --name student-task-tracker-app -p 5002:5000 student-task-tracker:${BUILD_NUMBER}'
        sh 'sleep 3'
        sh 'curl -f http://localhost:5002/'
    }
}

stage('Release') {
    steps {
        echo "Creating release ${BUILD_NUMBER}"
        sh '/usr/local/bin/docker tag student-task-tracker:${BUILD_NUMBER} student-task-tracker:v1.0.${BUILD_NUMBER}'
        sh '/usr/local/bin/docker tag student-task-tracker:${BUILD_NUMBER} student-task-tracker:latest'
    }
}

    }
}