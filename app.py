from flask import Flask, render_template
from flask_ask import Ask, statement
import jenkins
app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('JenkinsIntent')
def hello(app):
  server = jenkins.Jenkins('http://jenkins:8080', username='admin', password='admin')
  if str(app) == "deploy-bnp":
  back = server.build_job('deploy-bnp')
  print back
  print "deploying Business Network Portal"
  if str(app) == "test-bnp":
  print "Testing Business Network Portal"

return statement("Running {0}".format(app))

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
