# Snippets

## Minikube info


```
$ minikube version    
minikube version: v1.25.1
commit: 3e64b11ed75e56e4898ea85f96b2e4af0301f43d

$ minikube status   
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

$ minikube node list  
minikube        192.168.64.10
```
## Kubeconfig files 

```shell
[ansible@ansible Chapter-11]$ ls -l ~/.kube/ 
total 16 
-rw-r--r--. 1 ansible ansible 1111 Apr 25 14:03 ca.crt 
-rw-r--r--. 1 ansible ansible 1147 Apr 25 14:03 client.crt 
-rw-------. 1 ansible ansible 1675 Apr 25 14:03 client.key 
-rw-rw-r--. 1 ansible ansible  824 Apr 25 13:58 minikube-config 
```

## repo for kubectl

```shell
[ansible@ansible Chapter-11]$ cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo 
[kubernetes] 
name=Kubernetes 
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64 
enabled=1 
gpgcheck=1
repo_gpgcheck=1 
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg 
EOF 
```
## Cluster nodes

```shell
[ansible@ansible Chapter-11]$ ansible-playbook k8s-details.yaml
...<output omitted>..
ames': ['k8s.gcr.io/kube-scheduler@sha256:8be4eb1593cf9ff2d91b44596633b7815a3753696031a1eb4273d1b39427fa8c', 'k8s.gcr.io/kube-scheduler:v1.23.1'], 'sizeBytes': 53488305}, {'names': ['k8s.gcr.io/ingress-nginx/kube-webhook-certgen@sha256:64d8c73dca984af206adf9d6d7e46aa550362b1d7a01f3a0a91b20cc67868660'], 'sizeBytes': 47736388}, {'names': ['k8s.gcr.io/coredns/coredns@sha256:5b6ec0d6de9baaf3e92d0f66cd96a25b9edbce8716f5f15dcd1a616b3abd590e', 'k8s.gcr.io/coredns/coredns:v1.8.6'], 'sizeBytes': 46829283}, {'names': ['kubernetesui/metrics-scraper@sha256:36d5b3f60e1a144cc5ada820910535074bdf5cf73fb70d1ff1681537eef4e172', 'kubernetesui/metrics-scraper:v1.0.7'], 'sizeBytes': 34446077}, {'names': ['gcr.io/k8s-minikube/storage-provisioner@sha256:18eb69d1418e854ad5a19e399310e52808a8321e4c441c1dddad8977a0d7a944', 'gcr.io/k8s-minikube/storage-provisioner:v5'], 'sizeBytes': 31465472}]}, 'apiVersion': 'v1', 'kind': 'Node'}) => {
    "msg": "minikube"
}

PLAY RECAP ****************************************************************************************************
localhost                  : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Figure 11.16 – Kubernetes namespace created using Ansible 

```shell
[ansible@ansible Chapter-11]$ kubectl get namespace todoapp-ns
NAME         STATUS   AGE
todoapp-ns   Active   6s
```

## 

```shell
[ansible@ansible Chapter-11]$ kubectl -n todoapp-ns get all
NAME                           READY   STATUS    RESTARTS   AGE
pod/todo-app-546b5b58d-bhhnz   1/1     Running   0          5m36s

NAME                  TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/todoapp-svc   NodePort   10.98.213.33   <none>        3000:30080/TCP   5m35s

NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/todo-app   1/1     1            1           5m36s

NAME                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/todo-app-546b5b58d   1         1         1       5m36s
```

## Figure 11.19 – Exposed service details in a minikube cluster 

```shell
$ minikube service list
|---------------|------------------------------------|--------------|----------------------------|
|   NAMESPACE   |                NAME                | TARGET PORT  |            URL             |
|---------------|------------------------------------|--------------|----------------------------|
| default       | kubernetes                         | No node port |
| ingress-nginx | ingress-nginx-controller           | http/80      | http://192.168.64.10:31729 |
|               |                                    | https/443    | http://192.168.64.10:30711 |
| ingress-nginx | ingress-nginx-controller-admission | No node port |
| kube-system   | kube-dns                           | No node port |
| kube-system   | metrics-server                     | No node port |
| todoapp-ns    | todoapp-svc                        |         3000 | http://192.168.64.10:30080 |
|---------------|------------------------------------|--------------|----------------------------|
```

## install
## ingress task
```
    - name: Create ingress resource
      kubernetes.core.k8s:
        kubeconfig: "{{ kubeconfig_file }}"
        state: present
        src: todo-app-ingress.yaml
        namespace: "{{ namespace_name }}"
```

## Scaling application using kubectl

```shell
$ kubectl -n todoapp-ns scale deployment/todo-app --replicas=3 
deployment.apps/todo-app scaled 
```

## Application scaled to 3 replicas

```shell
[ansible@ansible Chapter-11]$ kubectl -n todoapp-ns get all
NAME                           READY   STATUS    RESTARTS   AGE
pod/todo-app-546b5b58d-bhhnz   1/1     Running   0          16m
pod/todo-app-546b5b58d-hk6zz   1/1     Running   0          21s
pod/todo-app-546b5b58d-lkmlt   1/1     Running   0          21s

NAME                  TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/todoapp-svc   NodePort   10.98.213.33   <none>        3000:30080/TCP   16m

NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/todo-app   3/3     3            3           16m

NAME                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/todo-app-546b5b58d   3         3         3       16m
```

## 

```shell
[ansible@ansible Chapter-11]$ kubectl -n todoapp-ns describe service/todoapp-svc
Name:                     todoapp-svc
Namespace:                todoapp-ns
Labels:                   <none>
Annotations:              <none>
Selector:                 app=todo
Type:                     NodePort
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.98.213.33
IPs:                      10.98.213.33
Port:                     <unset>  3000/TCP
TargetPort:               3000/TCP
NodePort:                 <unset>  30080/TCP
Endpoints:                172.17.0.10:3000,172.17.0.11:3000,172.17.0.9:3000
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

## Figure 11.28 – Pod replicas after scaling

```shell
[ansible@ansible Chapter-11]$ kubectl -n todoapp-ns get pods
NAME                       READY   STATUS    RESTARTS   AGE
todo-app-546b5b58d-5j8nj   1/1     Running   0          28s
todo-app-546b5b58d-7sr8j   1/1     Running   0          28s
todo-app-546b5b58d-bhhnz   1/1     Running   0          24m
todo-app-546b5b58d-r9nmz   1/1     Running   0          28s
```

## Figure 11.34 – Curl command output for todoapp-svc 


```shell
[ansible@ansible Chapter-11]$ ansible-playbook curl-app-deploy.yaml 
...<ouput omitted>...

TASK [Display service check output] ***************************************************************************
ok: [localhost] => {
    "msg": [
        "",
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "    <meta charset=\"utf-8\" />",
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no, maximum-scale=1.0, user-scalable=0\" />",
        "    <link rel=\"stylesheet\" href=\"css/bootstrap.min.css\" crossorigin=\"anonymous\" />",
        "    <link rel=\"stylesheet\" href=\"css/font-awesome/all.min.css\" crossorigin=\"anonymous\" />",
        "    <link href=\"https://fonts.googleapis.com/css?family=Lato&display=swap\" rel=\"stylesheet\" />",
        "    <link rel=\"stylesheet\" href=\"css/styles.css\" />",
        "    <title>Todo App</title>",
        "</head>",
        "<body>",
        "    <div id=\"root\"></div>",
        "    <script src=\"js/react.production.min.js\"></script>",
        "    <script src=\"js/react-dom.production.min.js\"></script>",
        "    <script src=\"js/react-bootstrap.js\"></script>",
        "    <script src=\"js/babel.min.js\"></script>",
        "    <script type=\"text/babel\" src=\"js/app.js\"></script>",
        "</body>",
        "</html>"
    ]
}

...<ouput omitted>...
```