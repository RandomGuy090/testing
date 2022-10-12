pipeline{
	agent any

	stages{
		stage("build"){
			steps{
				echo "echo building"
				sh "uname -a"
			}
		}
		stage("test"){
			steps{
				echo "echo testing"
			}

		}
		stage("deploy"){
			steps{
				echo "echo deploying"
			}
		}
	}
}