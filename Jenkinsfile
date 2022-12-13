pipeline{
	agent any
	environment {
		TAG_NAME = 'latest';
		REPO = 'randomguy090/testing';
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
					echo "echo building";

					def command = 'print("building python")';
					command = "python3 -c '${command}'"
					sh  "${command}" ;
					sh 'docker build -t randomguy090/testing:latest .';
					def img = image("xD");
				}
			}
		}
		stage("test"){
			steps{
				script {
					echo "echo testing";

					def command = 'print("testing python")';
					command = "python3 -c '${command}'"
					sh  "${command}" ;
				}
			}
		}

		stage("deploy"){
			steps{	
				script {
					echo "echo deploying";

					def command = 'print("testing python")';
					command = "python3 -c '${command}'"
					sh  "${command}" ;
				}
			}
		}
		stage('Docker Push') {
			      steps {
				      script{
					      
					      withCredentials([usernamePassword(credentialsId: "f0713cc8-1b33-42bb-8611-b151f7db8717", passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
							sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
						      sh "docker push $REPO:$TAG_NAME";
						}
					}
			    } 
		}
	}
}
