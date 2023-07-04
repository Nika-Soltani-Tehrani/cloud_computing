# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: redis-deplyment-app
# spec:
#   selector:
#     matchLabels:
#       app: redis
#   replicas: 1
#   template:
#     metadata:
#       labels:
#         app: redis
#     spec:
#       containers:
#         - name: redis
#           image: nikast/redis:1.0
#           imagePullPolicy: IfNotPresent
#           ports:
#             - containerPort: 6379
#           resources:
#             limits:
#               memory: 512Mi
#               cpu: "1"
#             requests:
#               memory: 256Mi
#               cpu: "0.2"