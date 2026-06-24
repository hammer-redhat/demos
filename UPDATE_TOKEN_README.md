# OpenShift Token Update Playbook

This playbook generates a new OpenShift service account token and updates an AAP credential with that token.

## Prerequisites

1. Install required collections:
```bash
ansible-galaxy collection install -r requirements.yml
```

   Or install from Automation Hub if you have access:
   ```bash
   ansible-galaxy collection install ansible.controller
   ansible-galaxy collection install kubernetes.core
   ```

2. Set environment variables:
```bash
export OCP_ADMIN_TOKEN="your-openshift-admin-token"
export AAP_PASSWORD="your-aap-admin-password"
```

## Configuration

Edit the `vars` section in `update_ocp_token.yml`:

- **OpenShift settings:**
  - `ocp_api_url`: Your OpenShift cluster API URL
  - `ocp_namespace`: Namespace where the service account exists
  - `ocp_service_account`: Name of the service account
  - `token_duration`: Token validity duration (default: 1 year)

- **AAP settings:**
  - `aap_host`: Your AAP instance URL (already set to your instance)
  - `aap_username`: AAP admin username
  - `aap_credential_name`: Name of the credential to update in AAP
  - `aap_organization`: Organization in AAP

## Usage

Run the playbook:
```bash
ansible-playbook update_ocp_token.yml
```

## What the playbook does

1. Ensures the service account exists in OpenShift
2. Deletes any existing token secret (to force regeneration)
3. Creates a new token secret for the service account
4. Waits for the token to be generated
5. Extracts and decodes the token
6. Updates the AAP credential with the new token
7. Tests the new token to verify it works

## Notes

- The playbook uses the traditional service account token secret method which works in OpenShift 4.x
- For OpenShift 4.11+, you might need to use TokenRequest API for short-lived tokens
- The credential type in AAP must be "OpenShift or Kubernetes API Bearer Token"
- Make sure the service account has appropriate RBAC permissions for your automation needs

## Service Account Permissions

You may need to create a ClusterRole or Role binding for the service account. Example:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: automation-sa-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: automation-sa
  namespace: default
```

Apply with: `oc apply -f service-account-rbac.yml`
