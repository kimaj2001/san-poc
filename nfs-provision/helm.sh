tar xzvf helm-v3.15.0-linux-amd64.tar.gz
mv linux-amd64/helm ~/bin/ 

oc create namespace nfs-provisioner
oc create -f custom-priv-scc.yaml
helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
    --set nfs.server=172.16.47.103 \
    --set nfs.path=/nfs/projects/pv -n nfs-provisioner
