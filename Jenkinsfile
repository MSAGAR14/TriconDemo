pipeline {
    agent any
    parameters {
        string(name: 'NUMBER1', defaultValue: '5', description: 'First number')
        string(name: 'NUMBER2', defaultValue: '21', description: 'Second number')
    }
 
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/MSAGAR14/TriconDemo', branch: 'main'
            }
        }
 
        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install pytest
                '''
            }
        }
 
        stage('Run Tests') {
            steps {
                sh 'pytest test_main.py'
            }
        }
        
        
    
    }
 
    post {
        always {
            echo 'Build finished'
        }
    }
}
