django-ansible
==============

simple django deploy with nginx+uwsgi+postgresql using ansible and vagrant


How to use
==========

 * Change the playbook.yml settings your project vars
 * Change the repo.yml file and addapt it to your project

Warning!
========

This deployment copies your .ssh directory to the remote host to be able to
download the repo. So if you don't control the remote server change the user.yml
to copy other ssh directory with repo download privileges.
