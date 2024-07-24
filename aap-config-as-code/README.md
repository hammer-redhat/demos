# Ansible Automation Platform: Configuration as Code
## Chris Hammer, Senior Architect, Financial Services - Launch Team | <img src="files/redhat-logo.png" style="width:100px;"/>
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
---
- Lab Environment:  

| Function    | Hostname |
| :--------: | :-------: |
| Bastion:   |  bastion.lan  |
| Automation Controller:  | aap.lan  |
| Automation Hub: | pah.lan  |
| Database:  |  db.lan  |

---
## How to use:
- Deploying AAP:
    - Navigate to the `inventory_vars/variables.yml` file and update it according to your environment.
    - After the `variables.yml` is updated save the file and run the playbook command below. 
    - Run: `ansible-playbook deploy_aap.yml`
- Config as Code:  
    - To prepare for the Configuration as Code example you will need to download an AAP manifest from access.redhat.com or provide the `ansible.controller.license` module with username/password credentials.   
    - Next you will need to populate the `files/controller_auth` file with your controller url and admin credentials.   
    - Finally if you wish to use ssh key auth you can upload a private key to `files/id_rsa` to be used as credentials in AAP.   
    - Run: `ansible-playbook configure_aap.yml`
    
