devdns
======

Simple Development DNS Server written in Python.
This server will route all whatever \*.dev domain names to 127.0.0.1.
So you can quickly start a new project without touching your system's host file.

## Installation

Clone this repo.

```bash
git clone https://github.com/ball6847/devdns.git
cd devdns
```

Setup environment and dependencies, you need python virtualenv or virtualenvwrapper.

```bash
mkvirtualenv devdns 
pip install -r requirements.txt
```

Start devdns

```bash
sudo twistd -y devdns.py
```

And there you go.

For any reason you need to run this server in `non-daemonize` mode eg. running under Supervisor.
You can start server using `-ny` options like this.

```bash
sudo twistd -ny devdns.py
```

One last step. Edit `/etc/resolv.conf` to make your system using localhost as a DNS.
Just open `/etc/resolv.conf` with your preferred text editor (you may need super user privilege)

```text
nameserver 127.0.0.1
```

## Todo

- Provide instruction for Windows
- Provide instruction on disabling dnsmasq in Ubuntu NetworkManager
- Use twisted application module
- Simple configuration file
- Auto backup/restore `/etc/resolv.conf` upon server start or stop
- DNS caching

## Credit

This script inspired by this gist [https://gist.github.com/johnboxall/1147973](https://gist.github.com/johnboxall/1147973), written by [John Boxall](https://github.com/johnboxall)