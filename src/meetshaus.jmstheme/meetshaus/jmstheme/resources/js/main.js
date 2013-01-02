/*jslint white:false, onevar:true, undef:true, nomen:true, eqeqeq:true, plusplus:true, bitwise:true, regexp:true, newcap:true, immed:true, strict:false, browser:true */
/*global jQuery:false, document:false, window:false, location:false */

(function ($) {
    $(document).ready(function () {
        if (jQuery.browser.msie && parseInt(jQuery.browser.version, 10) < 7) {
            // it's not realistic to think we can deal with all the bugs
            // of IE 6 and lower. Fortunately, all this is just progressive
            // enhancement.
            return;
        }
        $('#banner-scrollable').scrollable({
            circular: true
        }).autoscroll(6000).navigator();
    
        $("a[rel=prettyPhoto]").prettyPhoto();
    
        var $sameHeightDivs = $("div[data-appui='leveled']");
        var maxHeight = 0;
        $sameHeightDivs.each(function () {
            maxHeight = Math.max(maxHeight, $(this).outerHeight());
        });
        $sameHeightDivs.css({ height: maxHeight + 'px' });
    });
}(jQuery));
