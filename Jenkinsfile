@Library('my-shared-library') _

pipeline{

    agent any
    //agent { label 'Demo' }

    parameters{

        choice(name: 'action', choices: 'create\ndelete', description: 'Choose create/Destroy')
        string(name: 'ImageName', description: "name of the docker build", defaultValue: 'snakeapp')
        string(name: 'ImageTag', description: "tag of the docker build", defaultValue: 'v1')
        string(name: 'DockerHubUser', description: "name of the Application", defaultValue: 'esanvsh')
    }

    stages{
         
        stage('Git Checkout'){
                    when { expression {  params.action == 'create' } }
            steps{
            gitCheckout(
                branch: "main",
                url: "https://github.com/esanvsh/PY_PKG_TEMPLATE3.git"
            )
            }
        }
        //  stage('Unit Test pytest'){
         
        //  when { expression {  params.action == 'create' } }

        //     steps{
        //        script{
                   
        //            mvnTest()
        //        }
        //     }
        // }
        //  stage('Integration Test pytest'){
        //  when { expression {  params.action == 'create' } }
        //     steps{
        //        script{
                   
        //            mvnIntegrationTest()
        //        }
        //     }
        // }
    //     stage('Static code analysis: Sonarqube'){
    //      when { expression {  params.action == 'create' } }
    //         steps{
    //            script{
                   
    //                def SonarQubecredentialsId = 'sonarqube-api'
    //                statiCodeAnalysis(SonarQubecredentialsId)
    //            }
    //         }
    //    }
    //    stage('Quality Gate Status Check : Sonarqube'){
    //      when { expression {  params.action == 'create' } }
    //         steps{
    //            script{
                   
    //                def SonarQubecredentialsId = 'sonarqube-api'
    //                QualityGateStatus(SonarQubecredentialsId)
    //            }
    //         }
    //    }
        // stage('Maven Build : maven'){
        //  when { expression {  params.action == 'create' } }
        //     steps{
        //        script{
                   
        //            mvnBuild()
        //        }
        //     }
        // }
        stage('Docker Compose'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                sh 'sudo docker-compose up -d'
               }
            }
        }
        // stage('Docker Image Build'){
        //  when { expression {  params.action == 'create' } }
        //     steps{
        //        script{
                   
        //            dockerBuild("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
        //        }
        //     }
        // }
        //  stage('Docker Image Scan: trivy '){
        //  when { expression {  params.action == 'create' } }
        //     steps{
        //        script{
                   
        //            dockerImageScan("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
        //        }
        //     }
        // }
        // stage('Docker Image Push : DockerHub '){
        //  when { expression {  params.action == 'create' } }
        //     steps{
        //        script{
                   
        //            dockerImagePush("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
        //        }
        //     }
        // }   
        // stage('Docker Image Cleanup : DockerHub '){
        //  when { expression {  params.action == 'create' } }
        //     steps{
        //        script{
                   
        //            dockerImageCleanup("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
        //        }
        //     }
        // }
    }
}
