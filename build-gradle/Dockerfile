FROM image-registry.openshift-image-registry.svc:5000/openshift/java:latest
COPY build/libs/*.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]