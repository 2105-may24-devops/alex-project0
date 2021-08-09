node {
    stage('P0-Test') {
        echo "This is a Test."
    }
    stage('Ansible-Playbook') {
        ansiblePlaybook colorized: true, 
        installation: 'ansible0', 
        inventory: '**/inventory', 
        playbook: '**/install-packages.yaml'
    }
    stage('Discord-Message') {
        discordSend description: "```Build Number: ${env.BUILD_ID} \nBuild Node: ${env.NODE_NAME} \nBuild Location: ${env.WORKSPACE} \nBuild Duration: ${currentBuild.durationString}```", 
        footer: 'Jenkins v2.289.1, Discord Notifier v1.4.14', 
        image: '', 
        link: env.BUILD_URL, 
        result: currentBuild.currentResult, 
        thumbnail: '', 
        title: 'Alex-P0-Jenkins', 
        webhookURL: 'https://discord.com/api/webhooks/856587514218545203/OmVq23OAAKWh6VQGfoiFE-DRlGwtDst19OLHedR9HaQ7eONnVdlBJlc1i8OiAUpz4hqd'
    }
}