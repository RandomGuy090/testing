pipeline{
	agent {
		docker { image 'python:slim' }

	}

	stages{
		stage("prepare"){
			steps{
				sh "python3 -m pip install -r requirements.txt"
			}
		}
		stage("build"){
			steps{
				echo "echo building"
				sh "uname -a"
				sh "ls --all"
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