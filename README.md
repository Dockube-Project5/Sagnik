# Sagnik
Flask docker app deployed on k8s

![alt text](https://github.com/Dockube-Project5/Sagnik/blob/master/Flaskapp_screenshot.JPG)

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
```
kubectl get services
```
```
kubectl port-forward service/<service name> <browser port>:<port>
```
```
curl http://localhost:<port-name>
```

