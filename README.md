# how to check mac adress

```commandline
ip addr show
```

# How to change the MAC address
```commandline
sudo ifconfig eth0 down
sudo ifconfig eth0 hw ether 00:11:22:33:44:55
sudo ifconfig eth0 up
```
