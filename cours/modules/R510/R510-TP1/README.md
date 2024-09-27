# R510-TP1 - bases de Kubernetes

## 1 - Compétences à acquérir lors du TP

## 2 - "Crash course" sur Kubernetes

## 3 - Installation du cluster Kubernetes avec Kind

- On installe Go:

  ```sh
  wget https://go.dev/dl/go1.23.1.linux-amd64.tar.gz
  tar -xf go1.23.1.linux-amd64.tar.gz -C /usr/local/
  export PATH=$PATH:/usr/local/go/bin
  go version
  ```

- On installe Kubectl:

  ```sh
  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
  echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
  sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
  kubectl version --client
  ```

- On installe Kind:

  ```sh
  [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.24.0/kind-linux-amd64
  chmod +x ./kind
  sudo mv ./kind /usr/local/bin/kind
  ```

- On clone le dépôt Git:

  ```sh
  git clone https://github.com/pushou/substrat-labs-k8s.git && cd substrat-labs-k8s
  ```

- On lance le script pour créer le cluster:

  ```sh
  ./creation-cluster-kind/creation-kind-cluster-with-ec.sh
  ```

- On installe FZF:

  ```sh
  apt install fzf
  ~/.fzf/install
  ```

On fait:

```sh
kubectl get nodes -o json | jq ".items[] | {name:.metadata.name} + .status.capacity"
```

ce qui nous donne:

```json
{
  "name": "tp1k8s-control-plane",
  "cpu": "4",
  "ephemeral-storage": "47918820Ki",
  "hugepages-1Gi": "0",
  "hugepages-2Mi": "0",
  "memory": "4008700Ki",
  "pods": "110"
}
{
  "name": "tp1k8s-worker",
  "cpu": "4",
  "ephemeral-storage": "47918820Ki",
  "hugepages-1Gi": "0",
  "hugepages-2Mi": "0",
  "memory": "4008700Ki",
  "pods": "110"
}
{
  "name": "tp1k8s-worker2",
  "cpu": "4",
  "ephemeral-storage": "47918820Ki",
  "hugepages-1Gi": "0",
  "hugepages-2Mi": "0",
  "memory": "4008700Ki",
  "pods": "110"
}
{
  "name": "tp1k8s-worker3",
  "cpu": "4",
  "ephemeral-storage": "47918820Ki",
  "hugepages-1Gi": "0",
  "hugepages-2Mi": "0",
  "memory": "4008700Ki",
  "pods": "110"
}
```

- Ajout de l'auto-complétion bash:

  ```bashrc
  #### Kubectl alias
  alias k=kubectl
  source <(kubectl completion bash)
  complete -F __start_kubectl k
  ```

  On fait aussi:

  ```sh
  kubectl completion bash >/etc/bash_completion.d/kubectl
  ```

  afin de l'activer sur le système.

- Test avec une application Python:

  ```sh
  docker pull registry.iutbeziers.fr/pythonapp:latest
  kind load docker-image registry.iutbeziers.fr/pythonapp:latest --name tp1k8s
  ```

  ce qui nous donne:

  ```sh
  latest: Pulling from pythonapp
  756975cb9c7e: Pull complete 
  d77915b4e630: Pull complete 
  5f37a0a41b6b: Pull complete 
  96b2c1e36db5: Pull complete 
  c495e8de12d2: Pull complete 
  33382189822a: Pull complete 
  414ebfa5f45b: Pull complete 
  dd860911922e: Pull complete 
  ac1f7f2faf6e: Pull complete 
  ac38a92df562: Pull complete 
  4d71fc4753b5: Pull complete 
  b477a50490a1: Pull complete 
  4f4fb700ef54: Pull complete 
  2c5d93e6dff2: Pull complete 
  Digest: sha256:b23c278eab01274a6f41878fd06da9c05e8902e4b7af5e3b2c6e52cb4b86303c
  Status: Downloaded newer image for registry.iutbeziers.fr/pythonapp:latest
  registry.iutbeziers.fr/pythonapp:latest
  Image: "registry.iutbeziers.fr/pythonapp:latest" with ID "sha256:20b638827c2b93109a5aacfe73e0aa1bcf5363402197cf941d3d742e2033b208" not yet present on node "tp1k8s-worker", loading...
  Image: "registry.iutbeziers.fr/pythonapp:latest" with ID "sha256:20b638827c2b93109a5aacfe73e0aa1bcf5363402197cf941d3d742e2033b208" not yet present on node "tp1k8s-control-plane", loading...
  Image: "registry.iutbeziers.fr/pythonapp:latest" with ID "sha256:20b638827c2b93109a5aacfe73e0aa1bcf5363402197cf941d3d742e2033b208" not yet present on node "tp1k8s-worker3", loading...
  Image: "registry.iutbeziers.fr/pythonapp:latest" with ID "sha256:20b638827c2b93109a5aacfe73e0aa1bcf5363402197cf941d3d742e2033b208" not yet present on node "tp1k8s-worker2", loading...
  ```

## 4 - Premiers pas avec Kubernetes

### 4.1 - Configuration des objets en mode déclaratif et impératif

1. Adaptez à votre contexte et passez les commandes suivantes pour vous familiariser avec Kubernetes
  et son mode impératif:

  ```sh
  kubectl run nginx-pod --image nginx
  kubectl exec -it nginx-pod -- sh
  kubectl create deployment hello-nginx --image nginx
  kubectl scale deployment hello-nginx --replicas 2
  kubectl expose deployment hello-nginx --type=LoadBalancer --port 80 --target-port 80
  ```

2. Visualisez les objets Kubernetes générés avec les commandes suivantes:

  ```sh
  k get nodes -o wide --show-labels
  k describe "ressources=node,pods,deploy,service..."
  k logs "pods"
  ```

  - ```sh
    k get nodes -o wide --show-labels
    ```

    nous donne:

    ```sh
    NAME                   STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                         KERNEL-VERSION   CONTAINER-RUNTIME     LABELS
    tp1k8s-control-plane   Ready    control-plane   28m   v1.31.0   172.18.0.3    <none>        Debian GNU/Linux 12 (bookworm)   6.1.0-25-amd64   containerd://1.7.18   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,ingress-ready=true,kubernetes.io/arch=amd64,kubernetes.io/hostname=tp1k8s-control-plane,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node.kubernetes.io/exclude-from-external-load-balancers=,run=haproxy-ingress
    tp1k8s-worker          Ready    <none>          27m   v1.31.0   172.18.0.4    <none>        Debian GNU/Linux 12 (bookworm)   6.1.0-25-amd64   containerd://1.7.18   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=tp1k8s-worker,kubernetes.io/os=linux
    tp1k8s-worker2         Ready    <none>          27m   v1.31.0   172.18.0.5    <none>        Debian GNU/Linux 12 (bookworm)   6.1.0-25-amd64   containerd://1.7.18   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=tp1k8s-worker2,kubernetes.io/os=linux
    tp1k8s-worker3         Ready    <none>          27m   v1.31.0   172.18.0.6    <none>        Debian GNU/Linux 12 (bookworm)   6.1.0-25-amd64   containerd://1.7.18   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=tp1k8s-worker3,kubernetes.io/os=linux
    ```

  - ```sh
    k describe "ressources=node,pods,deploy,service..."
    ```

    - `node`: Voir [k-desc-node.txt](./src/k-desc-node.txt)
    - `pods`: Voir [k-desc-pods.txt](./src/k-desc-pods.txt)
    - `deploy`: Voir [k-desc-deploy.txt](./src/k-desc-deploy.txt)
    - `service`: Voir [k-desc-service.txt](./src/k-desc-service.txt)


3. Utilisez la commande 

  ```sh
  kubectl create --dry-run=client -o yaml "objet"
  ```

  afin de générer les manifests des objets créés en mode impératif précédemment.

4. Créer via la commande Kubectl et l'option `--from-literal` une `configmap` nommée
  `maconfigmap` avec les couples clefs/valeurs suivants:

  - `k8s=lepresent`
  - `virt=legacy`

  Affichez ensuite les valeurs.


5. Créer de même un secret nommé `monsecret` avec la valeur `mdp=torototo` et 
  affichez le "décodé" (il est en base 64).
