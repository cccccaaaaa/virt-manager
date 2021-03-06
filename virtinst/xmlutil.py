#
# Copyright 2006, 2013 Red Hat, Inc.
#
# This work is licensed under the GNU GPLv2 or later.
# See the COPYING file in the top-level directory.
#


def listify(l):
    if l is None:
        return []
    elif not isinstance(l, list):
        return [l]
    else:
        return l


def xml_escape(xml):
    """
    Replaces chars ' " < > & with xml safe counterparts
    """
    if xml:
        xml = xml.replace("&", "&amp;")
        xml = xml.replace("'", "&apos;")
        xml = xml.replace("\"", "&quot;")
        xml = xml.replace("<", "&lt;")
        xml = xml.replace(">", "&gt;")
    return xml


def get_prop_path(obj, prop_path):
    """Return value of attribute identified by `prop_path`

    Look up the attribute of `obj` identified by `prop_path`
    (separated by "."). If any component along the path is missing an
    `AttributeError` is raised.

    """
    parent = obj
    pieces = prop_path.split(".")
    for piece in pieces[:-1]:
        parent = getattr(parent, piece)

    return getattr(parent, pieces[-1])


def set_prop_path(obj, prop_path, value):
    """Set value of attribute identified by `prop_path`

    Set the attribute of `obj` identified by `prop_path` (separated by
    ".") to `value`. If any component along the path is missing an
    `AttributeError` is raised.
    """
    parent = obj
    pieces = prop_path.split(".")
    for piece in pieces[:-1]:
        parent = getattr(parent, piece)

    return setattr(parent, pieces[-1], value)


def raise_programming_error(cond, msg):
    """
    Small helper to raise a consistent error message for coding issues
    """
    if cond:
        raise RuntimeError("programming error: %s" % msg)
