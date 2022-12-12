pipeline{
	agent { dockerfile true }

	stages{
		stage("prepare"){
			steps{
				
				sh "python3 -m pip install -r requirements.txt";
			}
		}
		stage("build"){
			steps{
				echo "echo building";
				def comm = "print('building')"
				sh  "python3 -c com" ;
			}
		}
		stage("test"){
			steps{
				echo "echo testing";
				sh "python3 -m pytest tests.py";
			}

		}
		stage("deploy"){
			steps{
				echo "echo deploying";
			}
		}
	}
}
