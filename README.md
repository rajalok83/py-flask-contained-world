# Docker commands
## Docker machine commands
* Start a docker machine

`docker-machine start [optional_one_or_more_machine_name]`

* Stop a docker machine

`docker-machine stop [optional_one_or_more_machine_name]`

* List all docker machines running

`#docker-machine ls`

* Display or set environment variable 

`docker-machine env [optional_machine_name]`

## Docker image commands

* Build docker image

`docker build --rm -t <tag_name> .`

`docker build --rm -t <tag_name> --file <path_to_Dockerfile> .`

* List docker images

`docker images -a`

`docker images`

* Delete docker images

`docker rmi <image_id>`

`docker images -a | grep -e "none" -e "image_tag_name_to_exclude" | awk '{print $3}' | xargs docker rmi`

`docker images -a -q | grep -v "image_id_to_exlude" | xargs docker rmi`

`use -f option to force remove the images`

## Docker container commands

* Start a container

`docker run --rm --network host --name <container_name> <image_tag_name:optional_version>`

* List contianers

`docker ps -a`

`docker ps -a  -q`

* Stop containers

`docker stop <contianer_id>`

`docker ps -a | grep -e "container_to_exclude_name" | awk '{print $1}' | xargs docker stop`

`docker ps -a -q | grep -e "container_to_exclude_id" | xargs docker stop`

* Remove containers

`docker ps -a -q | xargs docker rm -f `

# Kubernetes/minikube commands

## minikube commands

* Start a minikube

`minikube start`

* Check minikube version

`minikube version`

* Start minikube dashboard

`minikube dashboard`

* Get minikuube ip

`minikube ip`

* Get minikube environment

`minikube env`

* Make a local docker

`minikube docker-env #Run the command generated`

# kubectl commands

* Check kubectl version

`kubectl version`

*  Check cluster information

`kubectl cluster-info`

* Check nodes in the cluster

`kubectl get nodes`

* Describe nodes

`kubectl describe node`

## Namespaces

* Create namespace

`kubectl create namespace <namespace-name>`

* Get list of namespaces

`kubectl get namespace`

* Set namespace for all your commands

`kubectl config set-context --current --namespace=<namespace>`

* Validate current namespace

`kubectl config view --minify`

* Resources in a namespace

`kubectl api-resources --namespaced=true`

* Resources not in a namespace

`kubectl api-resources --namespaced=false`

* Delete a namespace

`kubectl delete namespaces <namespace_name>`

## kubectl deployment commands

* Create deployment

`kubectl create deployment <deployment_name> --image=<image_path> created`

* Getting deployments

`kubectl get deployments`

* Describe deployments

`kubectl describe deployment`

* Start proxy

`kubectl proxy`

## kubectl pods commands

* Getting pods

`kubectl get pods`

* Getting pods from label

`kubectl get pods -l <label_key_value>`

* Getting all replicas of the deployment

`kubectl get pods -o wide`

* Describe pods

`kubectl describe pod <pod_name>`

* Set label on pod

`kubectl label pod <pod_name> <label_key_value>`

* Get logs from pods

`kubectl logs <pod_name>`

* Executing command under container on a pod

`kubectl exec <pod_name> <command>` 

* Opening a shell under container on a pod

`kubectl exec -ti <pod_name> bash`

## kubectl service commands

* Types of services

  * ClusterIP
 
  * NodePort

  * LoadBalancer

  * External

* Getting services

`kubectl get services`

* Getting services from label

`kubectl get services -l <label_key_value>`

* Creating services

`kubectl expose deployment/<deployment_name> --type=[ClusterIP|NodePort|LoadBalancer|]`

* Describe service

`kubectl describe services/<service_name>`

* Delete a service

`kubectl delete service <service_name>`

* Delete a service using label

`kubectl delete service -l <label_key_value>`

##Replication and scale

* Get replication set

`kubectl get rs`

* Scale application

`kubectl scale deployments/<deployment_name> --replicas=<num_of_replicas>`

## Upgrade application

`kubectl set image deployments/<deployment_name> <image_path>`

## Rollback application

`kubectl rollout undo deployments/<deployment_name>`

## Logging
* See logs of pod

`kubernetes get logs pods/<pod_name>`

* See logs of a particular container

`kubernetes get logs pods/<pod_name> -c <container_name> #Get container name from deployment yml or describe pod command`  

# skaffold commands

## Initialize a skaffold project

`skaffold init #After having kubernetes yml in the project and Dockerfile`

## Continous monitoring and new build and deploy on local

`skaffold dev`

## Build one time

`skaffold build`

## Run one time

`skaffold run`