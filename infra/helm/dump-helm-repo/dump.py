#!/usr/bin/env python3

import os
import yaml
import urllib.request

def download(url: str) -> str:
    ''' download file
    '''
    _url, filename = os.path.split(url)
    urllib.request.urlretrieve(url, filename)
    return _url, filename

def dump(repo_url: str) -> None: 
    ''' dump helm charts repo by url
    '''
    _url, filename = download(repo_url)

    with open(filename) as _file:
        _index = yaml.load(_file)
        for component, artifacts in _index.get('entries', {}).items():
            for artifact in artifacts:
                for artifact_url in artifact.get('urls', []):
                    download(os.path.join(_url, artifact_url))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-url', required=True,
                            help='Helm charts repo url')
    args = parser.parse_args()

    dump(args.repo_url)
