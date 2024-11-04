pipeline {
    agent any
 
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/MSAGAR14/TriconDemo', branch: 'main'
            }
        }
 
        // stage('Install Dependencies') {
        //     steps {
        //         sh '''
        //             pip install pytest
        //         '''
        //     }
        // }
 
        // stage('Run Tests') {
        //     steps {
        //         sh 'pytest test_main.py'
        //     }
        // }
        
        stage('Addition') {
            steps {
                script {
                    
                    def num1 = params.NUMBER1.toInteger()
                    def num2 = params.NUMBER2.toInteger()
                    
                    
                    def sum = num1 + num2
                    
                    
                    echo "The sum of ${num1} and ${num2} is: ${sum}"
                }
            }
        }
    
    }
 
    post {
        always {
            echo 'Build finished'
        }
    }
}
