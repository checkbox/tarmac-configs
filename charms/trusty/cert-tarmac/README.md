Certification team Tarmac service.
==================================

This charm takes care of deploying tarmac according to the certification team's
desired setup.

This is basically an automation of the steps described in the top-level
README.md file for [the branch containing the tarmac configuration and
scripts][1], behavior is best described on that file but roughly it's as
follows:

- Tarmac runs via cron every 10 minutes. An upstart service file launches
  tarmac, this takes care of avoiding two simultaneous instances.
- On each run, the upstart script will try to pull changes to tarmac
  configuration from a specific branch on github, that way deploying changes to
  tarmac's list of branches to consider can be done by pushing changes to that
  github branch and waiting.
- Assumptions are made about location of the tarmac source itself, the location
  of the tarmac configuration as described above, and locations of files in the
  server running this. This non-tunability reflects the very purpose-specific
  nature of this charm. It's NOT meant to be a generic tarmac deployment.
- The only needed additional configuration is that related to Launchpad
  authentication:
    1. Launchpad id (username) of the user under which Tarmac will access
      Launchpad.
    2. Launchpad credentials, obtained under the above user. A helper script is
      provided for this.
    3. SSH keys (public and private) for tarmac to be able to push code to
      Launchpad.

How to deploy this charm:

1. The first thing is to decide is which Launchpad user to run tarmac as. The
   first config option is the username of this user.

2. You also need ssh private and public key parts that are registered on
   Launchpad for that user. Generate these with `ssh-keygen -f tarmac-keys`,
   setting no passphrase so Tarmac can run unattended. Two files, `tarmac-keys`
   and `tarmac-keys.pub`, will be created, with the private and public keys,
   respectively.

3. To get the Launchpad oauth credentials for that user you can run the
   create_launchpad_credentials.py script included in the charm. This will
   create a `credentials` file.

Once you have all of these create a file called `tarmac-config.yaml`
containing::

    cert-tarmac:
        launchpad-id: <USERNAME>
        launchpad-public-key: ssh-rsa AAAAA...
        launchpad-private-key: |
            -----BEGIN RSA PRIVATE KEY-----
            MII....
            ...
            -----END RSA PRIVATE KEY-----
        launchpad-credentials: |
            [1]
            consumer_key = tarmac
            consumer_secret =
            access_token = 1232...
            access_secret = AAA...

Then you can deploy tarmac with (assuming you're in `tarmac-configs`):

    juju deploy --constraints "mem=6G arch=amd64" --repository charms local:trusty/cert-tarmac --config tarmac-config.yaml

passing the filename of the file you just created.

[1]: https://github.com/checkbox/tarmac-configs
