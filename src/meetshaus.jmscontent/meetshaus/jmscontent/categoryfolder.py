from five import grok
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from plone.directives import dexterity, form

from Products.CMFCore.utils import getToolByName

from meetshaus.jmscontent.contentpage import IContentPage

from meetshaus.jmscontent import MessageFactory as _


# Interface class; used to define content-type schema.

class ICategoryFolder(form.Schema):
    """
    A structural folder representing a site category
    """


class CategoryFolder(dexterity.Container):
    grok.implements(ICategoryFolder)


class View(grok.View):
    grok.context(ICategoryFolder)
    grok.require('zope2.View')
    grok.name('view')

    def update(self):
        self.has_pages = len(self.contained_pages()) > 0
        if self.has_pages and self.anonymous():
            first_page_url = self.first_page()
            return self.request.response.redirect(first_page_url)

    def first_page(self):
        pages = self.contained_pages()
        first_page = pages[0]
        url = first_page.getURL()
        return url

    def contained_pages(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IContentPage.__identifier__,
                          path=dict(query='/'.join(context.getPhysicalPath()),
                                    depth=1),
                          review_state='published',
                          sort_on='getObjPositionInParent')
        return results

    def authenticated(self):
        return not self.anonymous()

    def anonymous(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request),
                                       name=u'plone_portal_state')
        return portal_state.anonymous()
