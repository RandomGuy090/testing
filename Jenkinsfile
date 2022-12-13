pipeline{
	agent any
	environment {
		TAG_NAME = 'latest';
		REPO = 'randomguy090/testing';
		IMG = "";
	}

	stages{
		stage("prepare"){
			steps{
				script{
					sh "apt update && apt upgrade -y ";
					sh "apt install python3-pip -y ";
					
					sh "python3 -m pip install -r requirements.txt";
					sh "apt install docker -y ";

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
					echo "build image: $build_res";

				}
			}
		}
		stage("test"){
			steps{
				script {
					echo "---------------testing---------------";
					echo "list all images built";
					sh "docker images ls";
					echo "$IMG";
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
		stage('Docker Push') {
			      steps {
				      script{
						echo "---------------pushing to docker hub---------------";
					      
					      withCredentials([usernamePassword(credentialsId: "f0713cc8-1b33-42bb-8611-b151f7db8717", passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
							sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
						      sh "docker push $REPO:$TAG_NAME";
						}
					}
			    } 
		}
	}
}
