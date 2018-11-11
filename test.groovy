#!groovy
pipeline {
	agent any

	stages {

		stage('清空文件') {
			steps {
				echo "start clean report"
				dir('/opt/apitest/BC/reports/') {
					deleteDir()
				}

			}
		}

		stage('运行自动化脚本'){
			steps {
				echo "start run api_test"
				dir('/opt/apitest/BC') {
					sh '/usr/local/bin/hrun testsuites'
				}
			}
		}

		stage('发送测试报告'){
			steps {
				echo "start send emaill"
				dir('/opt/apitest/BC/') {
					sh 'python c5.py'
				}
			}
		}
	}
}