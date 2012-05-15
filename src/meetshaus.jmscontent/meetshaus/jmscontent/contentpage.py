from five import grok
from plone.directives import dexterity, form
from zope import schema

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage

from plone.app.textfield import RichText

from meetshaus.jmscontent import MessageFactory as _


class IContentPage(form.Schema, IImageScaleTraversable):
    """
    A cdocument/page type inlcuding preview images
    """
    headline = schema.TextLine(
        title=_(u"Headline"),
        description=_(u"Enter an alternative headline for this page. Leave "
                      u"empty to use the standard document title"),
        required=False,
    )
    text = RichText(
        title=_(u"Body Text"),
        required=True,
    )
    image = NamedBlobImage(
        title=_(u"Preview Image"),
        description=_(u"Please upload the main image for this content page."
                      u"Note: the image will automatically be scaled and the"
                      u"original scale will be available via a popover view"),
        required=False,
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
