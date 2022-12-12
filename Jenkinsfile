pipeline{
	agent { dockerfile true }

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
					dockerImage = docker.build("randomguy090/testing:latest")
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
		 stage('Push image') {
			 steps{
				 script {
					withDockerRegistry([ credentialsId: "randomguy090", url: "" ]) {
					dockerImage.push()
					}
				}
			 }
		    }    
	}
}
