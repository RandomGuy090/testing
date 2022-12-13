pipeline{
	
	
	
	
	agent any
	environment {

		TAG_NAME = 'latest';
		REPO_USER = "${scm.getUserRemoteConfigs()[0].getUrl().tokenize('/')[-2].toLowerCase()}";
		REPO_NAME = "${scm.getUserRemoteConfigs()[0].getUrl().tokenize('/').last().split("\\.")[0]}";
		
		REPO = "$REPO_USER/$REPO_NAME";

	}

	stages{
		stage("Preparing"){
			steps{
				script{

					echo "$env.BRANCH_NAME";
					if( env.BRANCH_NAME != "main" ) {
						currentBuild.result = 'SUCCESS'
						return
					}


					sh "apt update && apt upgrade -y ";
					sh "apt install python3-pip -y ";
					
					sh "python3 -m pip install -r requirements.txt";
					sh "apt install docker -y ";

					echo "build tag ${env.BUILD_TAG}";
					echo "repo name: ${scm.getUserRemoteConfigs()[0].getUrl()}"
				}
			}
		}
		stage("Building"){
			steps{
				script {
					echo "---------------building---------------";
					echo "building docker image via built in function";
					IMG = docker.build("$REPO:$TAG_name");
					echo "build image: $IMG";

				}
			}
		}
		stage("Testing"){
			steps{
				script {
					echo "---------------testing---------------";
					echo "list all images built";
					sh "docker images";
					echo "$IMG";
				}
			}
		}
		stage('Docker Push') {
			      steps {
				      script{
						echo "---------------pushing to docker hub---------------";

					      withCredentials([usernamePassword(credentialsId: "f0713cc8-1b33-42bb-8611-b151f7db8717", passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
							echo "deploying: $IMG";
							IMG.push(TAG_NAME);
							sh "docker rmi $IMG.id"
						}
					}
			    } 
		}
		

		stage("deploy"){
			steps{	
				script {
					echo "---------------deploying---------------";

				}
			}
		}
		
	}
}
