# Copyright 2018 Paul Ozog.  All rights reserved.

import os
import glob
import random
import string
import sys

class StageQueue:
    """Stage events for upload using a directory in /tmp. Every 'push' simply
    creates a file in this directory corresponding to a Zoneminder event.

    Every 'pop' returns the contents of one of these files (in undefined
    order), and deletes the file.
    """

    DIR = '/tmp/zms3-stage'
    EVENT_FILE_EXT = '.sevent'

    def __init__(self, stage_dir=DIR):
        """If stage_dir exists, it must be writeable.
        """
        self._dir = stage_dir
        print('Stage directory: ', self._dir)
        if not os.path.exists(self._dir):
            os.makedirs(self._dir)

    def push(self, event_dir_name):
        """Add a new stage event file in DIR corresponding to this event.
        """
        filename = self._next_upload_event_filename()
        f = open(filename, "w", encoding='utf-8')
        f.write(event_dir_name)
        f.close()

    def pop(self):
        """Get a file in DIR, read its contents, delete the file, and return the
        contents.

        Return None if no file exists or is empty.
        """
        filenames = glob.glob(os.path.join(self._dir, "*" +
                              StageQueue.EVENT_FILE_EXT))
        if len(filenames) == 0:
            return None

        content = open(filenames[0], "r").readlines()
        os.remove(filenames[0])

        if len(content) != 1:
            return None

        event_dir = content[0].strip()
        return event_dir

    def _next_upload_event_filename(self):
        return os.path.join(self._dir, self._random_string(32) +
                            StageQueue.EVENT_FILE_EXT)

    def _random_string(self, n):
        return ''.join(random.choice(string.ascii_lowercase + string.digits)
                       for _ in range(n))
