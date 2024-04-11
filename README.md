# Pass Without Trace
Sample malicious unit tests for pipeline code injection and data exfiltration spiced with D&D themed stuff.

## About 
This repository is a proof of concept for SAST/DAST abuse and pipeline hijacking by leveraging arbitrary code execution through PyTests. 

The whole execution can be simulated using Github Actions and SonarCloud or any other CI/CD and Code Scanner tool and the objective is to exfiltrate container configurations, credentials, secrets and even obtaining a shell inside the runner container.

## TODO

* Implement reverse shell with pytests
* Implement exfil options with pytests
* Implement sample mockaroo data for DLP testing 
* Include sample Github Actions yml file and tutorial for simulating 

