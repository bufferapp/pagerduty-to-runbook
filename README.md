#Pagerduty to Runbook

This is a simple project that will take data sent in from a pagerduty webhook when an incident is
triggered and using that data, decide what the most relevant runbook URL is to be used. At this
stage it will be a simple link to a google document/dropbox paper/wiki/service of your choice. 

## Future goals

One of the goal in the future is to have it come with its own CMS/wiki that will be intelligent
enough to guide any user through the steps required to rectify an issue. So if one of the steps is
"SSH into x box" the system will be intelligent enough to help you link to the steps to the document
"how to ssh into x box"

A second goal will be to act as an intermediary to pagerduty to help transform data coming in from
services like New Relic into messages that PAgerduty truly understands (so that it can make the most
use of features like incident key)

## Get up and running (dev environment only)

The app is designed to get up and running with minimal involvement. But there is still a little that needs to be done. Some steps will be removed along the way, while others will be moved into a run once script


* Run the following commands in the root of this repo. This assumes you have sqlite3 installed already
  `mkdir data logs && touch data/data.db && sqlite3 data/data.db`

* Inside the sqlite db, run the query:
  `CREATE TABLE runbooks (incident_key TEXT, runbook_url TEXT);`

* Run `docker-compose build`

* Run `cp src/sampleconfig.ini src/config.ini`
  * you will need to set the secret key for your flask application. The endpoint to give to pagerduty, and the slack endpoint to send messages to. 
  * For your flask application secret key run `docker run --rm -it python:3.5. In the python terminal that opens, run the following:
    * `import os`
    * `os.urandom(21)`
    * copy the result (without the b' and the ending ')
  * for the endpoint to give pagerduty, you can come up with any string you like that has numbers and letters in it. 
* Finally run the following command:
  `docker-compose -f docker-compose.yml -f docker-compose-dev.yml up -d`

