

# LibreElec config for windows

This repo contains scripts and help to set a libreelec OS on a  raspi zero 2w. 

The raspi is focused on playing videos on a vertical screen inside of a HYTE Y60. 

Scripts included here are for automating this labor.

1. Generate/Save Public and Private Keys (.pub and .ppk) with PuttyGen (Included with Putty)

2. Copy Public Key (.pub) to LE (/storage/.ssh) (Connect via samba \\IP\Videos) and run:

```
cp key.pub /storage/.ssh/
```

3. Use Putty to Run the following commands in SSH session:

```
ssh-keygen -i -f ~/.ssh/key.pub > ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

4. Change the ip
```
connmanctl services
#Check service with * (Something like wifi_e45f01f5b780_46616d696c6961204365726f6e_managed_psk)
connmanctl config <entry_with_asterisk> --ipv4 manual 192.168.0.240 255.255.255.0 192.168.0.1
```

5. Configure/Save new Putty Session:

    Enter Host\IP
    Navigate to 'Connection\Data' and enter 'root' for 'Auto-login username'
    Navigate to 'Connection\SSH\Auth' and click 'Browse' to select previously generate private key (.ppk)
    Navigate back to 'Session' and specify a Session Name before clicking 'Save'

6. Video autoplay, run:
```
crontab -e
```

7. Add the following line:
```
*/5 * * * * kodi-send -a "PlayMedia(/storage/videos/)"
```