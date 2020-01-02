#!/usr/bin/env python3

import os
import yaml
import logging
import urllib.request


logger = logging.getLogger(__name__)


def download(url: str, target_dir: str = None) -> str:
    ''' download file
    '''
    _url, filepath = os.path.split(url)
    if target_dir:
        filepath = os.path.join(target_dir, filepath)
    logging.info('Fetching the file, url: {}, target file: {}'.format(url, filepath))
    urllib.request.urlretrieve(url, filepath)
    return _url, filepath

def dump(index_file_url: str, target_dir: str) -> None: 
    ''' dump helm charts repo by index file url
    '''
    _url, filename = download(index_file_url, target_dir)

    with open(filename) as _file:
        _index = yaml.load(_file)
        for component, artifacts in _index.get('entries', {}).items():
            for artifact in artifacts:
                for artifact_url in artifact.get('urls', []):
                    download(os.path.join(_url, artifact_url), target_dir)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--index-file-url', type=str, required=True,
                            help='Helm charts index file url')
    parser.add_argument('--target-dir', type=str, 
                            help='the path to directory where store files')
    parser.add_argument('-l', '--log-level', default='INFO',
                            help='Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL')
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level,
                            format="%(asctime)s.%(msecs)03d (%(name)s) [%(levelname)s] %(message)s",
                            datefmt='%Y-%m-%dT%H:%M:%S')
    
    if args.target_dir:
        args.target_dir = os.path.abspath(args.target_dir)
        if not os.path.isdir(args.target_dir):
            logger.info('The path to target directory does not exist, creating the path: {}'.format(args.target_dir))
            os.makedirs(args.target_dir)

    dump(args.index_file_url, args.target_dir)
