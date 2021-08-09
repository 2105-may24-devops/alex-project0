node {
    stage('P0-Test') {
        if (env.BRANCH_NAME == 'master') {
            echo 'Success on master branch'
        } 
        else {
            echo "Branch: ${env.BRANCH_NAME}"
        }
    }
    stage('Discord-Message') {
        discordSend description: "```Build Number: ${env.BUILD_ID} \nBuild Branch: ${env.BRANCH_NAME} \nBuild Location: ${env.WORKSPACE} \nBuild Duration: ${currentBuild.durationString}```", 
        footer: 'Jenkins v2.289.1, Discord Notifier v1.4.14', 
        image: '', 
        link: env.BUILD_URL, 
        result: currentBuild.currentResult, 
        thumbnail: '', 
        title: 'Alex-P0-Jenkins', 
        webhookURL: 'https://discord.com/api/webhooks/856587514218545203/OmVq23OAAKWh6VQGfoiFE-DRlGwtDst19OLHedR9HaQ7eONnVdlBJlc1i8OiAUpz4hqd'
    }
}