pipeline {
    agent any
    stages {
        stage('P0-Test') {
            when {
                expression {
                    env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'jenkins-pipeline'
                }
            }
            steps {
                echo "Success on $env.BRANCH_NAME"
            }
        }
    }
}