# Ansible Automation Platform: Configuration as Code
## Chris Hammer, Senior Architect, Financial Services - Launch Team | <img src="redhat-logo.png" style="width:100px;"/>
---
## Objectives:
- Review prerequisites for Infrastructure and Configuration as Code deployment.
    - Collections: infra.aap_utilities & ansible.controller.
    - Hosts: Provisioned and running (Bastion, Controller, Automation Hub and Database).
    - Network: Firewall rules and traffic allowed for cluster.
- Demonstrate the following: 
    - Uploading the manifest/license.
    - Create credentials
    - Create a project from Git.
    - Create an inventory
    - Populate hosts in the newly created inventory.
    - Build a job template from the Git project created earlier. 