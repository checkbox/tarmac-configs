Usage instructions
==================

1. Get an Ubuntu 13.04 box
2. Install a few packages and clone tarmac and the tarmac configs (this!):

        $ sudo add-apt-repository ppa:zkrynicki/vagrant
        $ sudo apt-get update
        $ sudo apt-get install vagrant bzr git python-bzrlib pastebinit
        $ mkdir -p ~/.config
        $ git clone git://github.com/checkbox/tarmac-configs.git ~/.config/tarmac
        $ git clone git://github.com/checkbox/tarmac.git ~/tarmac
        $ sudo cp ~/.config/tarmac/tarmac-lander.conf /etc/init

4. Set the user that tarmac will use on launchpad:

        $ bzr launchpad-login <your-launchpad-login>. 

5. Tarmac needs to be able to access launchpad with its own ssh key, so generate
   an ssh key for the user:

        $ ssh-keygen -O source-address=your_external_ip_address
        (select no passphrase)
   then add .ssh/id_rsa.pub to [your launchpad authorized keys](https://launchpad.net/~/+editsshkeys)

6. As the tarmac-running user, or globally, do <code>bzr branch lp:some-project</code>, this is so that
   launchpad's ssh host keys are known to the user, otherwise an Invalid host key error will appear.
 
7. Edit configurations to suit your needs:

    * Edit .config/tarmac and set branch_root to the location for your 
      tarmac local branches.
    * Edit /etc/init/tarmac-lander.conf and set HOME, PYTHONPATH, TARMAC_DIR
      and TARMAC_CONFIG to the appropriate values.

8. Authenticate tarmac to launchpad:

        $ cd ~/tarmac
        $ PYTHONPATH=. ./bin/tarmac authenticate

Now you're ready to start running tarmac.  

* To run once, do

        sudo start tarmac-lander

* To run periodically, set up a cron entry that does the above as often as you want. Example:

        $ echo "*/10 * * * * root /sbin/start tarmac-lander >/dev/null" | sudo tee /etc/cron.d/tarmac-lander

    Or if you want to run hourly:

        $ echo "/sbin/start tarmac-lander >/dev/null" | sudo tee /etc/cron.hourly/tarmac-lander

Optional refinements
====================

To speed up frequent testing, use apt-cacher-ng to cache downloaded packages:

    $ sudo apt-get install apt-cacher-ng

Then add the following to /etc/init/tarmac-lander.conf, along with the other
environment variables:

    env VAGRANT_APT_CACHE=http://<your ip address>:3142

To put the virtual machines on ramdisk:

About 1.5 GB RAM are needed for a VM's virtual disk, plus about 1 GB for the
host and VM RAM. VMs are destroyed after each use, so the ramdisk space can be
reused. To be entirely safe, 3 GB total RAM are recommended if you want to use
this, to allow for some breathing room.

1. Add this to /etc/fstab:

        tmpfs /ramdisk tmpfs defaults,size=2000m,uid=ubuntu 0 0

2. Create /ramdisk:

        $ mkdir /ramdisk

3. Mount /ramdisk:

        $ sudo mount -a

5. Edit ~/.VirtualBox/VirtualBox.xml, look for SystemProperties and change 
the defaultMachineFolder to something under /ramdisk:

        <SystemProperties 
        defaultMachineFolder="/ramdisk/vms" defaultHardDiskFormat="VDI" 
        VRDEAuthLibrary="VBoxAuth" webServiceAuthLibrary="VBoxAuth" 
        LogHistoryCount="3"/>
