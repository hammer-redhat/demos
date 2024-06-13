# Ansible Automation Platform: Configuration as Code
## Chris Hammer, Senior Architect, Financial Services - Launch Team | <img src="redhat-logo.png" style="width:100px;"/>
---
## Objectives:
- Review prerequisites for Infrastructure and Configuration as Code deployment.
    - Collections: infra.aap_utilities & ansible.controller.
    - Hosts: Provisioned and running (Bastion, Controller, Automation Hub and Database).
    - Network: Firewall rules and traffic allowed for cluster.
- Demonstrate the following Using Config As Code: 
    - Uploading the manifest/license file.
    - Create credentials to sync a project from Github and connect to hosts. 
    - Create a project and sync from Github.
    - Create an inventory to run our playbooks against.
    - Populate hosts in the newly created inventory.
    - Build a job template to run our playbook from the Github project created and synced earlier. 

- Lab Environment:  

| Function    | Hostname |
| :--------: | :-------: |
| Automation Controller:  | aap.lan  |
| Automation Hub: | pah.lan  |
| Execution Node:  | exec-node.lan  |
| Database:  |  db.lan  |