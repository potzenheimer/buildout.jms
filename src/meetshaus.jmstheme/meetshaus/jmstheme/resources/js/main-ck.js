/*jslint white:false, onevar:true, undef:true, nomen:true, eqeqeq:true, plusplus:true, bitwise:true, regexp:true, newcap:true, immed:true, strict:false, browser:true *//*global jQuery:false, document:false, window:false, location:false */(function(e){e(document).ready(function(){if(jQuery.browser.msie&&parseInt(jQuery.browser.version,10)<7)return;e("#banner-scrollable").scrollable({circular:!0}).autoscroll(6e3).navigator();e("a[rel=prettyPhoto]").prettyPhoto();var t=e("div[data-appui='leveled']"),n=0;t.each(function(){n=Math.max(n,e(this).outerHeight())});t.css({height:n+"px"})})})(jQuery);