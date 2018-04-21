#!/usr/bin/env python3
# Copyright 2018 Paul Ozog.  All rights reserved.
"""Upload all staged events to S3. This should be run in cron from a
aws-equipped user.

"""

import argparse
import fcntl
import os
import sys

S3_BUCKET = 'replace-me'
S3_FOLDER = 'replace-me'
LOCAL_ZONEMINDER_DIR = '/usr/share/zoneminder/www'

# These are used to ensure only one instance of this script is running.
_PID_FILE = '/tmp/zms3-upload.pid'
_fp = open(_PID_FILE, 'w')

class Zms3Upload:
    def __init__(self, stage_dir):
        self._stage_dir = stage_dir
        self._ensure_no_other_process()

    def _ensure_no_other_process(self):
        try:
            fcntl.lockf(_fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            print('Another instance is running; exiting.')
            sys.exit(0)

    def _get_seconds_dir(self, full_event_dir):
        split = full_event_dir.split('/')
        assert len(split) > 1
        return split[-1]


    def _get_without_seconds_dir(self, full_event_dir):
        split = full_event_dir.split('/')
        assert len(split) > 1
        return '/'.join(split[0:-1])


    def make_url(self, full_event_dir):
        """
        Create S3 url of the form 's3://<bucket>/<directory>'.
        """
        assert full_event_dir[0] == '/'

        # Strip LOCAL_ZONEMINDER_DIR from the beginning
        event_dir = os.path.relpath(full_event_dir, LOCAL_ZONEMINDER_DIR)

        event_seconds = self._get_seconds_dir(event_dir)
        event_without_seconds = self._get_without_seconds_dir(event_dir)

        return 's3://%s/%s/%s' % (S3_BUCKET, S3_FOLDER, event_without_seconds)


    def run(self):
        # For each
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', '--input', required=True, help='Path to input stage file')
    args = parser.parse_args()

    zms3 = Zms3Upload(args.input)
    print(zms3.make_url('/usr/share/zoneminder/www/events/8/18/04/21/14/35/40'))

if __name__ == '__main__':
    sys.exit(main())
