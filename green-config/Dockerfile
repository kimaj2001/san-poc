FROM FROM image-registry.openshift-image-registry.svc:5000/04/httpd:original

RUN chmod 777 green.jpg

COPY green.jpg /var/www/html
COPY index.html /var/www/html
