import pytest

from users import get_users


pw1 = """
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
"""
pw2 = """
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
"""
pw3 = """
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
Debian-exim:x:101:103::/var/spool/exim4:/bin/false
statd:x:102:65534::/var/lib/nfs:/bin/false
sshd:x:103:65534::/var/run/sshd:/usr/sbin/nologin
ftp:x:104:65534::/home/ftp:/bin/false
messagebus:x:105:106::/var/run/dbus:/bin/false
"""
pw4 = """
mysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false
avar:x:1000:1000::/home/avar:/bin/bash
chad:x:1001:1001::/home/chad:/bin/bash
git-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash
gerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash
avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
"""


@pytest.mark.parametrize("input_, expected", [
    (pw1, {'root': 'root', 'daemon': 'daemon', 'bin': 'bin',
           'sys': 'sys', 'sync': 'sync', 'games': 'games',
           'man': 'man', 'lp': 'lp'}),
    (pw2, {'mail': 'mail', 'news': 'news', 'uucp': 'uucp',
           'proxy': 'proxy', 'www-data': 'www-data',
           'backup': 'backup', 'list': 'Mailing List Manager'}),
    (pw3, {'irc': 'ircd', 'gnats': 'Gnats Bug-Reporting System (admin)',
           'nobody': 'nobody', 'libuuid': 'unknown', 'Debian-exim': 'unknown',
           'statd': 'unknown', 'sshd': 'unknown', 'ftp': 'unknown',
           'messagebus': 'unknown'}),
    (pw4, {'mysql': 'MySQL Server', 'avar': 'unknown', 'chad': 'unknown',
           'git-svn-mirror': 'Git mirror', 'gerrit2': 'Gerrit User',
           'avahi': 'Avahi mDNS daemon', 'postfix': 'unknown',
           'ssh-rsa': 'unknown', 'artagnon': 'Ramkumar R Git GSOC'}),
])
def test_users(input_, expected):
    assert get_users(input_) == expected
