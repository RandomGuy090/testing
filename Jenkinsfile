pipeline{
	agent any
	environment {
		TAG_NAME = '0.1';

		REPO = 'randomguy090/testing';
		IMG = "";
		LAST_TAG = "";

	}

	stages{
		stage("prepare"){
			steps{
				script{
					sh "apt update && apt upgrade -y ";
					sh "apt install python3-pip -y ";
					
					sh "python3 -m pip install -r requirements.txt";
					sh "apt install docker -y ";
					$LAST_TAG = sh (
						script: "docker images | grep ${REPO} | tr -s ' ' | cut -f2 -d' '", 
						returnStdout: true
					).split("-")
					
					echo $LAST_TAG;
					echo $LAST_TAG.getClass();
					echo $LAST_TAG[0];
					$LAST_TAG = $LAST_TAG[0];
					$LAST_TAG = Float.valueOf($LAST_TAG);
					$LAST_TAG = $LAST_TAG + 0.1;
					$LAST_TAG = $LAST_TAG.round(2)
					echo "LAST_TAG $LAST_TAG"

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
							// $IMG.push("${REPO}:${TAG_NAME}")
						}
					}
			    } 
		}
	}
}
