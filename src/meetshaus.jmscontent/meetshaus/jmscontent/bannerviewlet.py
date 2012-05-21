from five import grok
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets.interfaces import IPortalHeader
from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.interfaces import IContentish
from meetshaus.jmscontent.banner import IBanner
from meetshaus.jmscontent.landingpage import ILandingPage


class BannerViewlet(grok.Viewlet):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('meetshaus.jmscontent.BannerViewlet')
    grok.viewletmanager(IPortalHeader)

    def update(self):
        self.has_banners = len(self.banner_content()) > 0
        self.display_banner_nav = len(self.banner_content()) > 1

    def banners(self):
        banners = []
        for banner in self.banner_content():
            obj = banner.getObject()
            if obj.text:
                body = obj.text.output
            else:
                body = '<p>&nbsp;</p>'
            banners.append({
                'url': obj.absolute_url(),
                'image_tag': self.contruct_image_tag(obj),
                'text': body,
                'banner_class': obj.position,
            })
        return banners

    def banner_content(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        if IFolderish.providedBy(context):
            query_path = '/'.join(context.getPhysicalPath())
        else:
            parent = context.__parent__
            query_path = '/'.join(parent.getPhysicalPath())
        results = catalog(object_provides=IBanner.__identifier__,
                          path=dict(query=query_path,
                                    depth=1),
                          review_state='published',
                          sort_on='getObjPositionInParent')
        return results

    def contruct_image_tag(self, obj):
        scales = getMultiAdapter((obj, self.request), name='images')
        scale = scales.scale('image', scale='preview')
        imageTag = None
        if scale is not None:
            imageTag = scale.tag()
        return imageTag


class FrontpageBannerViewlet(grok.Viewlet):
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.name('meetshaus.jmscontent.FrontpageBannerViewlet')
    grok.viewletmanager(IPortalHeader)

    def update(self):
        self.has_banners = len(self.banner_content()) > 0
        self.display_banner_nav = len(self.banner_content()) > 1

    def banners(self):
        banners = []
        for banner in self.banner_content():
            obj = banner.getObject()
            banners.append({
                'url': obj.absolute_url(),
                'image_tag': self.contruct_image_tag(obj),
                'text': obj.text.output,
                'banner_class': obj.position,
            })
        return banners

    def banner_content(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        if IFolderish.providedBy(context):
            query_path = '/'.join(context.getPhysicalPath())
        else:
            parent = context.__parent__
            query_path = '/'.join(parent.getPhysicalPath())
        results = catalog(object_provides=IBanner.__identifier__,
                          path=dict(query=query_path,
                                    depth=1),
                          review_state='published',
                          sort_on='getObjPositionInParent')
        return results

    def contruct_image_tag(self, obj):
        scales = getMultiAdapter((obj, self.request), name='images')
        scale = scales.scale('image', scale='preview')
        imageTag = None
        if scale is not None:
            imageTag = scale.tag()
        return imageTag
