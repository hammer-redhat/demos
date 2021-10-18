# Ansible: Variables, Facts and Conditionals
## Chris Hammer, Senior Consultant, Red Hat
---


## Objectives:
##    1: Variables
    - Declaring variables 
    - Calling Variables
    - Variable Precedence
        Lowest:  -Configuration Settings - ansible.cfg
                 -Command-line options
                 -Playbook keywords play(most general) and tasks(most specific)
        Highest: -Variables vars/vars_files
        Trumps all: --extra-vars or -e. 
    ![](image.PNG)
    
## 2: Facts
        - Generate host facts: CLI/Playbook
        - Generate service facts: Playbook
        - Using facts as variables
        - Filtering Facts (demo'd in Conditionals)
    
## 3: Conditionals 
        - Register
        - When
        - Including/filtering facts


