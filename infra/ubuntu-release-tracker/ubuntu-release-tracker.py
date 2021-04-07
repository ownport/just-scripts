#!/usr/bin/env python3

import re
import sys
import time
import urllib

from urllib import request
from datetime import datetime
import urllib

RE_URL_DISTRO = re.compile(r'<a href="(ubuntu.+?)".+?>')
RE_URL_RELEASE_NUMBER = re.compile(r'<a href="(\d+\.\d+.+?)".+?>')

def print_releases_list() -> None:
    ''' print out the releases list
    '''
    page = request.urlopen(f'http://releases.ubuntu.com/').read()
    for version in RE_URL_RELEASE_NUMBER.findall(str(page)):
        print(version.replace('/', ''))


def check_release(release:str, exclude_patterns:list, period:int=0) -> None:
    ''' check when release is available
    '''
    if exclude_patterns is None:
        exclude_patterns = list()

    try:
        while True:
            
            now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
            URL_RELEASE=f'http://releases.ubuntu.com/{release}/'

            try:
                page = request.urlopen(URL_RELEASE).read()
            except urllib.error.HTTPError as err:
                print(f'[ERROR] {err}, url: {URL_RELEASE}')
                sys.exit(1)

            matches = []
            for filename in RE_URL_DISTRO.findall(str(page)):
                skip_file=False
                for exclude_pattern in exclude_patterns:
                    if re.search(exclude_pattern, filename):
                        skip_file = True
                        break
                if not skip_file:
                    matches.append(filename)
            
            if not matches:
                print(f'[{now}] The requested release {release} is not available yet')
                if period == 0:
                    break
                time.sleep(period)
            else:
                print(f'[{now}] The requested release {release} is ready for dowload!')
                for filename in set(matches):
                    print(f'- {filename}')
                break
    
    except KeyboardInterrupt as err:
        print("Interrupted by user")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--list-releases', action='store_true',
                        help='Check available releases')
    parser.add_argument('--check-release', type=str, dest='release',
                        help="Release number, for example: 21.04")
    parser.add_argument('--exclude', type=str, action='append',
                        help="Exclude filter, for example, exlude 'beta' releases")
    parser.add_argument('--check-period', type=int, default=0,
                        help="Check period in seconds, default: 0 secs (no periodical checks)")
    args = parser.parse_args()

    if args.list_releases:
        print_releases_list()

    elif args.release:
        check_release(args.release, args.exclude, args.check_period)
    
    else:
        parser.print_help()

