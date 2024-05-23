FROM FROM image-registry.openshift-image-registry.svc:5000/01-1/httpd:original
RUN chmod 777 mountain.jpg
COPY mountain.jpg /var/www/html
COPY index.html /var/www/html
