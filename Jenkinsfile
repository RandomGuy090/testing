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
	}
}
