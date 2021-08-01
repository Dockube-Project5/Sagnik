# Sagnik
Flask docker app deployed on k8s

![alt text](https://github.com/Dockube-Project5/Sagnik/blob/master/Screenshot/app_screenshot.JPG)

# Building an image
```
docker build -t <folder-name> .
```
```
docker images
```
```
docker run <image-id>
```
```
docker run -p <portname>:<portname> <image name>
```

# Kubernetes Deployment
```
kubectl get pods
```
![alt text](https://github.com/Dockube-Project5/Sagnik/blob/master/Screenshot/app_pods.JPG)
```
kubectl get services
```
![alt text](https://github.com/Dockube-Project5/Sagnik/blob/master/Screenshot/app_services.JPG)
```
kubectl port-forward service/<service name> <browser port>:<port>
```
```
curl http://localhost:<port-name>
```
![alt text](https://github.com/Dockube-Project5/Sagnik/blob/master/Screenshot/kubernetes_deployment.JPG)


