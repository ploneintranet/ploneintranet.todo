from zope.component import getUtility
from plone.uuid.interfaces import IUUID

from .interfaces import ITodoUtility
from .interfaces import MUST_READ
from .behaviors import IMustRead


def mark(obj, evt):
    """The event handler that marks this object as mustread.
    """
    todos = getUtility(ITodoUtility)
    obj_uuid = IUUID(obj)
    behavior = IMustRead(obj)
    # Verify if it has been booked in the utility
    present = todos.query(
        content_uids=[obj_uuid],
        verbs=[MUST_READ]
    )
    if not behavior.mustread and len(present) > 0:
        # Ok, so it was present but somehow we don't want it to be "must read"
        # anymore, so we complete the actions (ugh)
        todos.complete_action(
            content_uid=obj_uuid,
            verb=MUST_READ
        )
    if behavior.mustread and len(present) == 0:
        todos.add_action(
            content_uid=obj_uuid,
            verb=MUST_READ
        )


def on_delete(obj, evt):
    """Complete actions for objects marked as must read that have been deleted
    """
    todos = getUtility(ITodoUtility)
    obj_uuid = IUUID(obj)
    todos.complete_action(
        content_uid=obj_uuid,
        verb=MUST_READ
    )