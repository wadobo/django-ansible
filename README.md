django-ansible
==============

simple django deploy with nginx+uwsgi+postgresql using ansible and vagrant


How to use
==========

 * Change the playbook.yml settings your project vars
 * Change the repo.yml file and adapt it to your project

Vagrant
-------
 * $ vagrant up
 * Wait to finish
 * Open the browser http://localhost:8080
 * Profit!

Remote Machine
--------------

This stuff is for ubuntu, to use in other distro, please, fix this shit and send me a patch.

To run in a remote machine:
 * Create an inventory file with one server ip or domain per line
 * $ ansible-playbook playbook.yml -i inventory
 * Take a look to the doc to know more about ansible inventory files http://docs.ansible.com/intro_inventory.html
 * Profit!

Warning!
========

This deployment copies your .ssh directory to the remote host to be able to
download the repo. So if you don't control the remote server change the user.yml
to copy other ssh directory with repo download privileges.
