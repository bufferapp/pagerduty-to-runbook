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
