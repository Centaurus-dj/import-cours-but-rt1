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
