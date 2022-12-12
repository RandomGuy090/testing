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
					def comm = "print('building')"
					sh  'python3 -c "com"' ;
				}
			}
		}
		stage("test"){
			steps{
				script {
					echo "echo testing";
					def comm = "print('testing')"
					sh  'python3 -c "com"' ;
				}
			}

		}
		stage("deploy"){
			steps{	
				script {
					echo "echo deploying";
					def comm = "print('deploying')"
					sh  'python3 -c "com"' ;
				}
			}
		}
	}
}
