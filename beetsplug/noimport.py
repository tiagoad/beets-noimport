"""
add directories to the incremental import skip list
"""

import logging
import os.path

from beets import plugins, ui, importer
from beets.util import syspath, normpath, displayable_path

# Global logger.
log = logging.getLogger('beets')

class NoImportPlugin(plugins.BeetsPlugin):
    def __init__(self):
        super(NoImportPlugin, self).__init__()

        self._command = ui.Subcommand(
            'noimport',
            help='add directories to the incremental import skip list')

        self._command.parser.add_option(
            '-r', '--reverse', action='store_true', dest='reverse', default=None,
            help="remove directories from the skip list"
        )

    def commands(self):
        def func(lib, opts, args):
            # to match "beet import" function
            paths = args
            if not paths:
                raise ui.UserError('no path specified')

            self.noimport_files(lib, paths, opts)

        self._command.func = func
        return [self._command]

    def noimport_files(self, lib, paths, opts):
        # Check the user-specified directories.
        for path in paths:
            if not os.path.exists(syspath(normpath(path))):
                raise ui.UserError(u'no such file or directory: {0}'.format(
                    displayable_path(path)))

        # Open the state file
        state = importer._open_state()

        # Create the 'taghistory' set if it doesn't exist
        if 'taghistory' not in state:
            state['taghistory'] = set()

        # For every path...
        for path in paths:
            added = 0
            # ...get the list of albums in that path...
            for dirs, paths_in_dir in importer.albums_in_dir(path):
                dirs_tuple = tuple(map(normpath, dirs))

                # ...check if they're not already in the 'taghistory' set
                if not opts.reverse:
                    if dirs_tuple not in state['taghistory']:
                        state['taghistory'].add(dirs_tuple)
                        added += 1

                elif dirs_tuple in state['taghistory']:
                    state['taghistory'].remove(dirs_tuple)
                    added += 1

        # Save the state file
        importer._save_state(state)

        if not opts.reverse:
            log.info(u'Added {0} paths to the skip list', added)
        else:
            log.info(u'Removed {0} paths from the skip list', added)