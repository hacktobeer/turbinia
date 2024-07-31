How to develop against a remote GKE cluster.

Follow the develop-minikube.md setup guide, but substitute the "Start minikube cluster" with the below.

* Login into Cloud Code (VSCode bottom left)
* Choose a GCP project (VSCode bottom left)
   * Enable the Artifact Repository API in your GCP project
* Create Service Account with Storage Admin role and download the credentials file to `kaniko-secret` (we use this for the Artifact Repo push)
* Create a GKE cluster (VSCode Cloud Code icon left sidebar -> Kubernetes -> Click "+")
   * Make sure you choose a Node size with 64GB minumum (eg n2-standard-16)

Follow the develop-minikube.md setup guide again but substitute the skaffold commands with
* `skaffold build -f skaffold-gke.yaml`
* `skaffold dev -f skaffold-gke.taml`
