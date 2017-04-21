DenyHostsMySQL
=========

DenyHostsMySQL is a port of the DenyHosts utility developed by Phil Schwartz and maintained by a
number of developers which was aimed to thwart sshd (ssh server) brute force attacks.  DenyHostsMySQL modified DenyHosts to thwart attacks against MySQL

Please refer to https://github.com/tmmdata/denyhostsmysql for more information.

Installation
============


Requirements
------------

The DenyHostsMySQL software depends on the "ipaddr" Python module,
which is available in most Linux and BSD repositories.



Source Distribution
-------------------

If you downloaded the source distribution file (DenyHostsMySQL-#.#-tar.gz)
then:

    $ tar zxvf DenyHostsMySQL-3.1.tar.gz 

    $ cd denyhostsmysql

as root:

    # python setup.py install

This will install the DenyHosts modules into python's site-packages
directory.

Binary Distribution (rpm, deb, etc)
-----------------------------------

It is assumed that you are familiar with installing a binary package
on your particular operating system. If you are unsure how to do
this, you may wish to install from source instead.


All Distributions
-----------------

DenyHostsMySQL requires that a configuration file be created before
it can function.  The sample configuration file denyhostsmysql.conf
contains most of the possible settings and should be copied and
then edited as such:

    # cp denyhostsmysql.conf /etc

    # nano /etc/denyhostsmysql.conf

(nano is a simple text editor. Feel free to use your own favourite
text editor such as emacs, vi, etc)

The sample configuration file contains informational comments that
should help you quickly configure DenyHostsMySQL.  After you have
edited your configuration file, save it.

Next, if you intend to run DenyHostsMySQL in daemon mode (recommended)
copy the sample daemon-control.dist script as such:

    # cp daemon-control-dist daemon-control-dhmysql

Edit the daemon-control file.  You should only need to edit this section
near the top:

    ###############################################
    #### Edit these to suit your configuration ####
    ###############################################

    DENYHOSTSMYSQL_BIN   = "/usr/bin/denyhostsmysql.py"
    DENYHOSTSMYSQL_LOCK  = "/var/lock/subsys/denyhostsmysql"
    DENYHOSTSMYSQL_CFG   = "/etc/denyhostsmysql.conf"


These defaults should be reasonable for many systems.  You
should customize these settings to match your particular
system.

Once you have edited the configuration and daemon control files
make sure that the daemon control script it executable (by root).

    # chown root daemon-control-dhmysql

    # chmod 700 daemon-control-dhmysql


Starting DenyHostsMySQL Manually
===========================

Assuming you have configured DenyHostsMySQL to run as a daemon, you
can use the daemon-control-dhmysql script to control it:

    # daemon-control-dhmysql start

You should refer to the daemon log (typically /var/log/denyhostsmysql)
to ensure that DenyHostsMySQL is running successfully.

Another way to start DenyHostsMySQL manually is to run it from the command
line, usually supply a few common parameters. Usually, when running
DenyHostsMySQL from the command line (or from the /etc/rc.local script) we
can launch the program by running

     # python /usr/local/bin/denyhostsmysql --config /etc/denyhostsmysql.conf --daemon

The above command launches DenyHostsMySQL and runs it in the background. DenyHostsMySQL
will use the /etc/denyhostsmysql.conf configuration file to dictate its behavour.


Starting DenyHostsMySQL Automatically
================================

Method 1 (preferred)
--------------------

Create a symbolic link from /etc/init.d such as:

    # cd /etc/init.d
    # ln -s /usr/share/denyhostsmysql/daemon-control-dhmysql denyhostsmysql

If you have chkconfig installed you can then use it to
ensure that DenyHostsMySQL runs at boot time:

    # chkconfig --add denyhostsmysql

If you do not have chkconfig (or similar) installed you can either manually
create the symlinks in /etc/rc2.d, /etc/rc3.d, /etc/rc5.d but that is beyond
the scope of this document.

Method 2
--------

Add an entry into the /etc/rc.local file:

    /usr/share/denyhostsmysql/daemon-control-dhmysql start

Method 3
--------

Add an entry into crontab:

    @reboot /usr/share/denyhostsmysql/daemon-control-dhmysql start

