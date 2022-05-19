# RHCSA Yum & Repo Objectives

## Repos
### - checking enabled repos, config file location
### - yum/subscription-manager
### - /etc/yum.repos.d/

```
subscription-manager repos --list
subscription-manager repos --list-enabled
subscription-manager repos --enable <repo_id>
subscription-manager repos --disable <repo_id>
```

### - Using a local repo or http repo on another host.
```
touch /etc/yum.repos.d/http.repo
vim /etc/yum.repos.d/http.repo


#EXAMPLE REPO CONFIG
[http-repo-for-rhcsa-workgroup]
name = http-example-repo-on-another-server
enabled = 1
gpgcheck = 0
baseurl = http://ip_address_of_http_server/directory/for/repository/ #HTTP repo example
baseurl = file:///path/to/repo/locally/on/host  # Local file repo
```


## Yum
### yum - Yellowdog Updater Modified
```
yum list (available/installed/all/<package>)
yum info <package>
yum provides <command>
yum repolist all/enabled/disabled
yum install <package>
yum update
yum update <package>
yum downgrade <package>
yum reinstall <package>
yum remove/erase <package>
yum grouplist 
yum groupinstall "Web server"
```

### Yum popular options:
```
-y "Assume yes if prompted"
--assumeno "assume no if prompted"
-q quiet
-v debugging output
--downloadonly "downloads packages to /var/cache/yum/* but doesn't install them."
```

### Yum troubleshooting (yum-utils required)
```
yum-complete-transaction
needs-restarting (shows processes requiring restart after update)
```
