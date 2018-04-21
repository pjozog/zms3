#!/usr/bin/env python3
# Copyright 2018 Paul Ozog.  All rights reserved.
"""Stage an event for upload to S3. This should run as a filter in Zoneminder
using the www-data user. Use zms3-upload (from another user) to upload to S3.

"""

import sys

def main():
    assert len(sys.argv) == 1

if __name__ == '__main__':
    sys.exit(main())
