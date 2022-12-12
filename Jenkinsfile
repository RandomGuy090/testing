pipeline{
	agent { dockerfile true }
	
	 environment { 

		registry = "randomguy090/testing" 

		registryCredential = credentials('f0713cc8-1b33-42bb-8611-b151f7db8717') 

		dockerImage = '' 

    	}

	stages{
		stage("prepare"){
			steps{
				script{
					sh "python3 -m pip install -r requirements.txt";
				}
			}
		}
		stage("build"){
			steps{
				script {
					echo "echo building";
						
					def command = 'print("building python")';
					command = "python -c '${command}'"
					sh  "${command}" ;
					sh 'docker build -t randomguy090/testing:latest .';
				}
			}
		}
		stage("test"){
			steps{
				script {
					echo "echo testing";
					
					def command = 'print("testing python")';
					command = "python -c '${command}'"
					sh  "${command}" ;
				}
			}
		}
		
		stage("deploy"){
			steps{	
				script {
					echo "echo deploying";
					
					def command = 'print("testing python")';
					command = "python -c '${command}'"
					sh  "${command}" ;
				}
			}
		}
		stage('Docker Push') {
			agent any
			      steps {
					withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
						sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
				  	sh 'docker pushrandomguy090/testing:latest'
					}
			    } 
		}
	}
}
