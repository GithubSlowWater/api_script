#!groovy
pipeline {
	agent any

	stages {

		stage('清空文件') {
			steps {
				echo "start clean report"
				dir('/opt/api/jenkins/jobs/blockchain/api_script/reports/') {
					deleteDir()
				}

			}
		}

		stage('运行自动化脚本'){
			steps {
				echo "start run api_test"
				dir('/opt/api/jenkins/jobs/blockchain/api_script/') {
					sh '/usr/local/bin/hrun testcase'
				}
			}
		}

		stage('发送测试报告'){
			steps {
				echo "start send emaill"
				dir('/opt/api/jenkins/jobs/blockchain/api_script/') {
					sh 'python report_mail.py'
				}
			}
		}
	}
}