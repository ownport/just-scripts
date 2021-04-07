# Ubuntu Release Tracker

The script for checking when Ubuntu Release is available

## How to use

```sh
/ubuntu-release-tracker.py 
usage: ubuntu-release-tracker.py [-h] [--list-releases] [--check-release RELEASE] [--exclude EXCLUDE] [--check-period CHECK_PERIOD]

optional arguments:
  -h, --help            show this help message and exit
  --list-releases       Check available releases
  --check-release RELEASE
                        Release number, for example: 21.04
  --exclude EXCLUDE     Exclude filter, for example, exlude 'beta' releases
  --check-period CHECK_PERIOD
                        Check period in seconds, default: 0 secs (no periodical checks)

```

to get the list of releases
```sh
./ubuntu-release-tracker.py --list-releases
12.04.5
12.04
14.04.6
14.04
16.04.6
16.04.7
16.04
18.04.4
18.04.5
18.04
20.04.2.0
20.04.2
20.04
20.10
21.04
```

to get the list of available files for specific release
```sh
./ubuntu-release-tracker.py --check-release 21.04
[2021-04-07 10:23:09] The requested release 21.04 is ready for dowload!
- ubuntu-21.04-beta-desktop-amd64.iso
- ubuntu-21.04-beta-live-server-amd64.iso
- ubuntu-21.04-beta-desktop-amd64.iso.torrent
- ubuntu-21.04-beta-desktop-amd64.iso.zsync
- ubuntu-21.04-beta-desktop-amd64.list
- ubuntu-21.04-beta-desktop-amd64.manifest
- ubuntu-21.04-beta-live-server-amd64.iso
- ubuntu-21.04-beta-live-server-amd64.iso.torrent
- ubuntu-21.04-beta-live-server-amd64.iso.zsync
- ubuntu-21.04-beta-live-server-amd64.list
- ubuntu-21.04-beta-live-server-amd64.manifest
```

to exclude certain files
```sh
./ubuntu-release-tracker.py --check-release 21.04 --exclude desktop 
[2021-04-07 10:25:04] The requested release 21.04 is ready for dowload!
- ubuntu-21.04-beta-live-server-amd64.iso
- ubuntu-21.04-beta-live-server-amd64.iso.zsync
- ubuntu-21.04-beta-live-server-amd64.list
- ubuntu-21.04-beta-live-server-amd64.iso.torrent
- ubuntu-21.04-beta-live-server-amd64.manifest
```

periodical check
```sh
/ubuntu-release-tracker.py --check-release 21.04 --exclude beta --check-period 20
[2021-04-07 10:26:31] The requested release 21.04 is not available yet
[2021-04-07 10:26:51] The requested release 21.04 is not available yet
^CInterrupted by user
```
