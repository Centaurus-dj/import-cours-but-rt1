# R510-TP1 - bases de Kubernetes

## 1 - Compétences à acquérir lors du TP

## 2 - "Crash course" sur Kubernetes

## 3 - Installation du cluster Kubernetes avec Kind

- On installe Go:

  ```sh
  wget https://go.dev/dl/go1.23.1.linux-amd64.tar.gz /tmp
  tar -xf /tmp/go1.23.1.linux-amd64.tar.gz -C /usr/local/
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

   - On fait un `deployment`:

     ```sh
     k create deployment --dry-run=client -o yaml --image nginx nginx  
     ```

     donne:

     ```yml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       creationTimestamp: null
       labels:
         app: nginx
       name: nginx
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: nginx
       strategy: {}
       template:
         metadata:
           creationTimestamp: null
           labels:
             app: nginx
         spec:
           containers:
           - image: nginx
             name: nginx
             resources: {}
     status: {}
     ```

4. Créer via la commande Kubectl et l'option `--from-literal` une `configmap` nommée
  `maconfigmap` avec les couples clefs/valeurs suivants:

     - `k8s=lepresent`
     - `virt=legacy`

     Affichez ensuite les valeurs.

     - Pour créer la configmap, on fait:

       ```sh
       k create configmap maconfigmap --from-literal=k8s=lepresent --from-literal=virt=legacy
       ```

     - Pour voir notre configmap, on fait:

       ```sh
       k get configmap maconfigmap -o jsonpath='{.data}'
       ```

       Ce qui nous donne:

       ```json
       {"k8s":"lepresent","virt":"legacy"}
       ```

5. Créer de même un secret nommé `monsecret` avec la valeur `mdp=torototo` et
  affichez le "décodé" (il est en base 64).

   - Pour créer un secret, on fait :

      ```sh
      k create secret generic monsecret --from-literal=mdp=torototo
      ```

   - Pour le voir, on fait :

      ```sh
      k get secret monsecret -o jsonpath='{.data}'
      ```

      ce qui nous donne:

      ```json
      {"mdp":"dG9yb3RvdG8="}
      ```

   - Pour le décoder, on fait:

      ```sh
      echo 'dG9yb3RvdG8=' | base64 --decode
      ```

      qui nous donne:

      ```txt
      torototo
      ```

   - En une seule fois, on peut faire:

      ```sh
      k get secret monsecret -o jsonpath='{.data.mdp}' | base64 --decode
      ```

      qui nous donne:

      ```txt
      torototo
      ```

### 4.2 - Les "PODS" l'unité atomique de Kubernetes

#### 4.2.1 - Opérations basiques sur les PODS

1. Générez la configuration d'un pod debian à l'aide de la commande suivante:

    ```sh
    k run --dry-run=client debianpod --image=registry.iutbeziers.fr/debianiut:latest -o yaml > monpremierpod.yml
    ```

    qui nous donne:

    ```yml
    apiVersion: v1
    kind: Pod
    metadata:
      creationTimestamp: null
      labels:
        run: debianpod
      name: debianpod
    spec:
      containers:
      - image: registry.iutbeziers.fr/debianiut:latest
        name: debianpod
        resources: {}
      dnsPolicy: ClusterFirst
      restartPolicy: Always
    status: {}
    ```

    - Créez ce manifest sur votre cluster afin de créer votre premier pod avec "kubectl create".

      On fait:

      ```sh
      k create -f monpremierpod.yml
      ```

      On peut vérifier qu'il existe bien en faisant:

      ```sh
      k get pods debianpod
      ```

      ce qui nous donne:

      ```sh
      NAME        READY   STATUS              RESTARTS   AGE
      debianpod   0/1     ContainerCreating   0          10s
      ```

2. Vérifiez l'état de votre pod

    On peut vérifier son état en faisant:

    ```sh
    k get pods debianpod -o wide
    ```

    ```sh
    NAME        READY   STATUS    RESTARTS   AGE    IP           NODE            NOMINATED NODE   READINESS GATES
    debianpod   1/1     Running   0          2m2s   10.244.2.3   tp1k8s-worker   <none>           <none>
    ```

3. Sur quel noeud votre pod s'exécute-t-il ?

    Il s'exécute sur le noeud: `tp1k8s-worker`.

4. Dans quel NameSpace votre Pod s'exécute-t-il ?

    On peut récupérer notre namespace en faisant:

    ```sh
    k get pods debianpod -o json | jq ".metadata.namespace"
    ```

    ou

    ```sh
    k get pods debianpod -o jsonpath='{.metadata.namespace}'
    ```

    Il s'exécute dans le namespace: `default`.

5. Accédez au container en utilisant "kubectl exec".
  Démarrez un server apache dans le container

    On fait:

    ```sh
    k exec -it debianpod -- /bin/bash
    apt install -y apache2
    service apache2 start
    ```

6. Pouvez-vous accéder au serveur web Apache qui s'exécute dans ce Pod ?
  Accéder au serveur Apache depuis votre client Kubernetes en utilisant
  `kubectl port-forward`. Quel est le principe de cette commande ?

    On ne peut normalement pas accéder au serveur en dehors du pod.

    - Avec un cURL sur le pod:

      ```sh
      curl -I http://localhost:80
      ```

      donne:

      ```http
      HTTP/1.1 200 OK
      Date: Fri, 27 Sep 2024 15:36:21 GMT
      Server: Apache/2.4.62 (Debian)
      Last-Modified: Fri, 27 Sep 2024 15:32:39 GMT
      ETag: "29cd-6231b90b69e04"
      Accept-Ranges: bytes
      Content-Length: 10701
      Vary: Accept-Encoding
      Content-Type: text/html
      ```

    - Avec un cURL sur la machine:

      ```sh
      curl -I http://10.244.2.3:80 -vv
      ```

      donne:

      ```http
      *   Trying 10.244.2.3:80...
      ^C
      ```

    On forward le port de la manière suivante:

    ```sh
    k port-forward <host-port>:<pod-port>
    ```

    ce qui fait:

    ```sh
    k port-forward 8080:80 &
    ```

    nous permettant d'obtenir les résultats suivant, en faisant:

    ```sh
    curl -I http://localhost:8080
    ```

    nous donnant:

    ```http
    HTTP/1.1 200 OK
    Date: Fri, 27 Sep 2024 15:41:07 GMT
    Server: Apache/2.4.62 (Debian)
    Last-Modified: Fri, 27 Sep 2024 15:32:39 GMT
    ETag: "29cd-6231b90b69e04"
    Accept-Ranges: bytes
    Content-Length: 10701
    Vary: Accept-Encoding
    Content-Type: text/html
    ```

#### 4.2.2 - Manipulation des Pods

1. Supprimez le pod et recréez-le cette fois-ci en utilisant un `kubectl apply -f votre-manifeste`.
  Quelle est la différence entre "apply" et "create" ?

    On fait:

    ```sh
    k delete pods debianpod
    k apply -f monpremierpod.yml
    ```

     - Apply

       > Apply a configuration to a resource by file name or stdin. The resource name must be specified. \
       > This resource will be created if it doesn't exist yet. \
       > To use 'apply', always create the resource initially with either 'apply' or 'create --save-config'

     - Create

       > Create a resource from a file or from stdin.

     | Apply                                                                                    | Create                                                        |
     | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
     | Crée à partir d'un fichier ou de `stdin` si la ressource n'existe pas, sinon mets à jour | Crée dans tous les cas, peu importe s'il existe une ressource |

2. Recréer le POD avec en sus[^1] un container issu d'une image busybox. Rattachez-vous au pod via
  "kubectl exec" en précisant avec l'option -c le container nom donné au container busybox

    On ajoute à notre fichier YAML:

    ```yml
    - image: registry.iutbeziers.fr/busybox:latest
      name: busypod
      resources: {}
    ```

    ce qui fait:

    ```yml
    apiVersion: v1
    kind: Pod
    metadata:
      creationTimestamp: null
      labels:
        run: debianpod
      name: debianpod
    spec:
      containers:
      - name: debianpod
        image: registry.iutbeziers.fr/debianiut:latest
        resources: {}
      - name: busypod
        image: registry.iutbeziers.fr/busybox:latest
        resources: {}
        stdin: true
        tty: true
      dnsPolicy: ClusterFirst
      restartPolicy: Always
    status: {}
    ```

    > [!NOTE]
    > `stdin: true` et `tty: true` sont tous les deux nécessaires afin que busybox fonctionne
    > sous k8s.

    On peut les recréer:

    ```sh
    k delete pods debianpod
    k apply -f monpremierpod.yml
    ```

    On fait ensuite:

    ```sh
    k exe -it debianpod -c busypod -- /bin/sh
    ```

    [^1]: "En sus" = "En plus"

3. Modifiez le manifeste du pod afin de limiter le cpu et la mémoire consommer par ce pod via des "limits"

    Nous modifions notre manifeste comme ceci:

    ```yml
    apiVersion: v1
    kind: Pod
    metadata:
      creationTimestamp: null
      labels:
        run: debianpod
      name: debianpod
    spec:
      containers:
      - name: debianpod
        image: registry.iutbeziers.fr/debianiut:latest
        resources:
          limits:
            memory: "512Mi"
            cpu: "500m"
      - name: busypod
        image: registry.iutbeziers.fr/busybox:latest
        resources:
          limits:
            memory: "512Mi"
            cpu: "250m"
        stdin: true
        tty: true
      dnsPolicy: ClusterFirst
      restartPolicy: Always
    status: {}
    ```

    On applique ensuite la nouvelle configuration:

    ```sh
    k create -f monpremierpod.yml
    ```

    Si l'on fait:

    ```sh
    k get pods debianpod -o json | jq ".spec.containers[] | {name: .name, resources: .resources}"
    ```

    on obtient:

    ```json
    {
      "name": "debianpod",
      "resources": {
        "limits": {
          "cpu": "500m",
          "memory": "512Mi"
        },
        "requests": {
          "cpu": "500m",
          "memory": "512Mi"
        }
      }
    }
    {
      "name": "busypod",
      "resources": {
        "limits": {
          "cpu": "250m",
          "memory": "512Mi"
        },
        "requests": {
          "cpu": "250m",
          "memory": "512Mi"
        }
      }
    }
    ```

4. Générer un autre pod sur un autre "node" K8s et effectuez un traceroute entre les deux pods.
  Quelles différences constatez-vous avec la gestion réseaux des containers Docker ?

    - Nous avons notre premier noeud:

      ```sh
      k get pods debianpod -o json | jq ' . as $parent | .spec.containers[] | {name: .name, node: $parent.spec.nodeName, resources: .resources}'
      ```

      qui nous donne:

      ```json
      {
        "name": "debianpod",
        "node": "tp1k8s-worker3",
        "resources": {
          "limits": {
            "cpu": "500m",
            "memory": "512Mi"
          },
          "requests": {
            "cpu": "500m",
            "memory": "512Mi"
          }
        }
      }
      {
        "name": "busypod",
        "node": "tp1k8s-worker3",
        "resources": {
          "limits": {
            "cpu": "250m",
            "memory": "512Mi"
          },
          "requests": {
            "cpu": "250m",
            "memory": "512Mi"
          }
        }
      }
      ```

    - Nous avons nos noeuds disponibles:

      ```sh
      k get node -o json | jq '.items[] | {name: .metadata.name, addresses: .status.addresses}'
      ```

      qui nous donne:

      ```json
      {
        "name": "tp1k8s-control-plane",
        "addresses": [
          {
            "address": "172.18.0.5",
            "type": "InternalIP"
          },
          {
            "address": "tp1k8s-control-plane",
            "type": "Hostname"
          }
        ]
      }
      {
        "name": "tp1k8s-worker",
        "addresses": [
          {
            "address": "172.18.0.2",
            "type": "InternalIP"
          },
          {
            "address": "tp1k8s-worker",
            "type": "Hostname"
          }
        ]
      }
      {
        "name": "tp1k8s-worker2",
        "addresses": [
          {
            "address": "172.18.0.4",
            "type": "InternalIP"
          },
          {
            "address": "tp1k8s-worker2",
            "type": "Hostname"
          }
        ]
      }
      {
        "name": "tp1k8s-worker3",
        "addresses": [
          {
            "address": "172.18.0.3",
            "type": "InternalIP"
          },
          {
            "address": "tp1k8s-worker3",
            "type": "Hostname"
          }
        ]
      }
      ```

  On peut alors déployer notre pod sur le noeud `tp1k8s-worker` ou `tp1k8s-worker2`.

  - On crée donc un `deployment` de pods `debianpod` avec la configuration suivante:

    ```yml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: debianpod-deployment
      labels:
        app: debianpod
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: debianpod
      template:
        metadata:
          creationTimestamp: null
          labels:
            run: debianpod
          name: debianpod
        spec:
          containers:
          - name: debianpod
            image: registry.iutbeziers.fr/debianiut:latest
            resources:
              limits:
                memory: "512Mi"
                cpu: "500m"
          - name: busypod
            image: registry.iutbeziers.fr/busybox:latest
            resources:
              limits:
                memory: "512Mi"
                cpu: "250m"
            stdin: true
            tty: true
          dnsPolicy: ClusterFirst
          restartPolicy: Always
          nodeName: tp1k8s-worker
        status: {}
    ```

  - Ensuite, on récupère les addresses IPs des pods:$*

    ```sh
    k get pods -o json | jq '. as $parent | .items[] | {pod: .metadata.name, nodeIPs: .status.hostIPs, podIPs: .status.podIPs}'
    ```

    ce qui nous donne:

    ```json
    {
      "pod": "debianpod",
      "nodeIPs": [
        {
          "ip": "172.18.0.3"
        }
      ],
      "podIPs": [
        {
          "ip": "10.244.3.3"
        }
      ]
    }
    {
      "pod": "debianpod-deployment-5944f7f555-b4nl8",
      "nodeIPs": [
        {
          "ip": "172.18.0.2"
        }
      ],
      "podIPs": [
        {
          "ip": "10.244.1.3"
        }
      ]
    }
    {
      "pod": "debianpod-deployment-5944f7f555-djv7v",
      "nodeIPs": [
        {
          "ip": "172.18.0.2"
        }
      ],
      "podIPs": [
        {
          "ip": "10.244.1.2"
        }
      ]
    }
    ```

  - On accède au shell de notre pod de départ `debianpod`:

    ```sh
    k exec -it debianpod -- /bin/bash
    ```

  - On fait un traceroute:

    ```sh
    traceroute 10.244.1.2
    ```

    qui nous donne:

    ```sh
    traceroute to 10.244.1.2 (10.244.1.2), 64 hops max
    1   10.244.3.1  0,003ms  0,001ms  0,001ms
    2   172.18.0.2  0,001ms  0,001ms  0,001ms
    3   10.244.1.2  0,001ms  0,002ms  0,001ms
    ```

  On constate que l'on accède aux pods via les noeuds sur lesquels ils se situent,
  contrairement à Docker où tous les containers se trouvent dans le même réseau.


