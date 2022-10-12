pipeline{
	agent any

	stages{
		stage("build"){
			steps{
				echo "echo building"
				sh "uname -a"
				sh "ls --all"
				sh "python -m pip install -r requirements.txt"
			}
		}
		stage("test"){
			steps{
				echo "echo testing"
				sh "python3 -m pytest tests.py"
			}

		}
		stage("deploy"){
			steps{
				echo "echo deploying"
			}
		}
	}
}