pipeline{
	agent any
	environment {

		TAG_NAME = 'latest';
		REPO_USER = "${scm.getUserRemoteConfigs()[0].getUrl().tokenize('/')[-2].toLowerCase()}";
		REPO_NAME = "${scm.getUserRemoteConfigs()[0].getUrl().tokenize('/').last().split("\\.")[0]}";
		
		REPO = "$REPO_USER/$REPO_NAME";


	}

	stages{
		stage("prepare"){
			steps{
				script{
					sh "apt update && apt upgrade -y ";
					sh "apt install python3-pip -y ";
					
					sh "python3 -m pip install -r requirements.txt";
					sh "apt install docker -y ";

					echo "build tag ${env.BUILD_TAG}";
					echo "repo name: ${scm.getUserRemoteConfigs()[0].getUrl()}"
				}
			}
		}
		stage("build"){
			steps{
				script {
					echo "---------------building---------------";

					// echo "building docker image via shell";
					// sh 'docker build -t randomguy090/testing:latest .';
					echo "building docker image via built in function";
					// IMG = docker.image("xD");
					// echo "id of container: ${IMG}";
					IMG = docker.build("$REPO:$TAG_name");
					echo "build image: $IMG";

				}
			}
		}
		stage("test"){
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
							// sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
						    //   sh "docker push $REPO:$TAG_NAME";
							$IMG.push($TAG_NAME)
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
