beets-noimport
==============

Adds directories to the incremental import "do not import" list

Install
-------

To install this plugin, run

```
pip install beets-noimport
```

and add `noimport` to the `plugins` list in your beets config file.

Usage
-----

To use this plugin, simply use the `beet noimport` command like you would use the `beet import` command.
To add all the directories in your current directory, run

```
$ beet noimport .
Added 384 paths to the skip list
```

License
-------

This plugin is licensed under the MIT license.
For the complete license, read the `LICENSE` file.