Usage instructions
==================

* Get an Ubuntu 13.04 box
* $ sudo add-apt-repository ppa:zkrynicki/vagrant
* $ sudo apt-get update
* $ sudo apt-get install vagrant bzr git python-bzrlib
* $ mkdir -p ~/.config
* $ git clone git://github.com/checkbox/tarmac-configs.git ~/.config/tarmac
* $ git clone git://github.com/checkbox/tarmac.git ~/tarmac
* $ cd ~/tarmac
* $ PYTHONPATH=. ./bin/tarmac authenticate
* $ ./run.sh # This will run forever
