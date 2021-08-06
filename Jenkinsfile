node {
    stage('P1-Test') {
        if (env.BRANCH_NAME == 'master') {
            echo 'Success on master branch'
        } else {
            echo "Fail: $env.BRANCH_NAME"
        }
    }
}