Usage instructions
==================

* Get an Ubuntu 13.04 box
* $ sudo apt-get install vagrant bzr git
* $ mkdir -p ~/.config
* $ git clone git://github.com/checkbox/tarmac-configs.git ~/.config/tarmac
* $ git clone git://github.com/checkbox/tarmac.git ~/tarmac
* $ cd ~/tarmac
* $ PYTHONPATH=. ./bin/tarmac authenticate
* $ ./run.sh # This will run forever
