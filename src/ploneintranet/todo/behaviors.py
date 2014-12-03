from plone.directives import form
from zope.interface import alsoProvides, Interface
from zope.schema import Bool

from . import _


class IMustRead(form.Schema):
    """MustRead schema
    """

    form.fieldset(
        'settings',
        label=_(u'Settings'),
        fields=('mustread',),
    )

    mustread = Bool(
        title=_(u"Must read"),
        description=_(u"""Mark the content as "Must read" for all users."""),
        default=False,
        required=False,
    )

alsoProvides(IMustRead, form.IFormFieldProvider)


class IMustReadMarker(Interface):
    """Marker interface that will be provided by instances using the
    IMustRead behavior.
    """
