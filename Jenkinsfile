pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('test echo') {
      steps {
        sh 'echo dupa'
      }
    }

    stage('building container') {
      steps {
        sh 'docker build --tag testing_docker .'
      }
    }

    stage('run container') {
      steps {
        sh 'docker run -d -p 5009:5009 testing_docker'
      }
    }

  }
}