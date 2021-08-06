#!/usr/bin/env groovy
// pipeline {
//     agent any
//     stages {
//         stage('P0-Test') {
//             when {
//                 expression {
//                     env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'jenkins-pipeline'
//                 }
//             }
//             steps {
//                 echo "Success on $env.BRANCH_NAME"
//             }
//         }
//     }
// }
node {
    stage('P0-Test') {
        if (env.BRANCH_NAME == 'master') {
            echo 'Success on master branch'
        } 
        else {
            echo "Branch: $env.BRANCH_NAME"
        }
    }
}