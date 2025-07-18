pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-repo/my-python-project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    pytest tests/
                '''
            }
        }

        stage('Build or Package') {
            steps {
                echo 'Build step here (optional for Python)'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploy step here (e.g., copy files, upload to server, etc.)'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up'
        }
    }
}