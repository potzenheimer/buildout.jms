from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from meetshaus.jmscontent import MessageFactory as _


positions = SimpleVocabulary(
    [SimpleTerm(value=u'topleft', title=_(u'Top Left')),
     SimpleTerm(value=u'topright', title=_(u'Top Right')),
     SimpleTerm(value=u'bottomleft', title=_(u'Bottom Left')),
     SimpleTerm(value=u"bottomright", title=_(u"Bottom Right"))]
    )


class IBanner(form.Schema, IImageScaleTraversable):
    """
    A banner used as a tile inside the scrollable
    """
    image = NamedBlobImage(
        title=_(u"Banner Image"),
        description=_(u"Upload image used as a background for the top "
                      u"scrollable. Note: the dimensions should already fit "
                      u"the available frame for best quality display"),
        required=False,
    )
    text = RichText(
        title=_(u"Teaser Text"),
        description=_(u"Enter teaser text for this banner"),
        required=False,
    )
    position = schema.Choice(
        title=_(u"Teaser Text Position"),
        vocabulary=positions,
        required=False,
        default=u"topleft",
    )
    video = schema.Bool(
        title=_(u"Has Video Content"),
        description=_(u"Please select, if this banner has video content. "
                      u"Image content will be ignored and the teaser text "
                      u"will be used as a full width tile"),
        required=False,
    )


class Banner(dexterity.Item):
    grok.implements(IBanner)


class View(grok.View):
    grok.context(IBanner)
    grok.require('zope2.View')
    grok.name('view')
