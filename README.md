1. instead rhc app create "satchmo" django create from openshift web-site with git https://github.com/eparst/django-example/
2. go to ssh-openshift and:
$OPENSHIFT_HOMEDIR/python/virtenv/bin/python setup.py install #/var/lib/openshift/51d5b51d4382ecf1c30002a5/python/virtenv/bin/python setup.py install
$OPENSHIFT_HOMEDIR/python/virtenv/bin/python /home/user/src/satchmo-trunk/scripts/clonesatchmo.py
