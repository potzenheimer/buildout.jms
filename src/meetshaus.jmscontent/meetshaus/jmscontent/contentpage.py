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


# Interface class; used to define content-type schema.

class IContentPage(form.Schema, IImageScaleTraversable):
    """
    A cdocument/page type inlcuding preview images
    """
    text = RichText(
        title=_(u"Body Text"),
        required=True,
    )
    image = NamedBlobImage(
        title=_(u"Preview Image"),
        description=_(u"Please upload the main image for this content page."
                      u"Note: the image will automatically be scaled and the"
                      u"original scale will be available via a popover view"),
        required=True,
    )
    caption = schema.TextLine(
        title=_(u"Image Caption"),
        description=_(u"Enter a short description of the image content used"
                      u"as an image caption"),
        required=False,
    )


class ContentPage(dexterity.Item):
    grok.implements(IContentPage)


class View(grok.View):
    grok.context(IContentPage)
    grok.require('zope2.View')
    grok.name('view')
