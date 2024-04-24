/*!
 * Bootstrap v3.4.1 (https://getbootstrap.com/)
 * Copyright 2011-2023 Twitter, Inc.
 * Licensed under the MIT license
 */

if("undefined"==typeof jQuery)throw new Error("Bootstrap's JavaScript requires jQuery");+function(t){"use strict";var e=t.fn.jquery.split(" ")[0].split(".");if(e[0]<2&&e[1]<9||1==e[0]&&9==e[1]&&e[2]<1||e[0]>3)throw new Error("Bootstrap's JavaScript requires jQuery version 1.9.1 or higher, but lower than version 4")}(jQuery),+function(t){"use strict";function e(e){var o=e.attr("data-target");o||(o=e.attr("href"),o=o&&/#[A-Za-z]/.test(o)&&o.replace(/.*(?=#[^\s]*$)/,""));var i="#"!==o?t(document).find(o):null;return i&&i.length?i:e.parent()}function o(o){o&&3===o.which||(t(n).remove(),t(s).each(function(){var i=t(this),n=e(i),s={relatedTarget:this};n.hasClass("open")&&(o&&"click"==o.type&&/input|textarea/i.test(o.target.tagName)&&t.contains(n[0],o.target)||(n.trigger(o=t.Event("hide.bs.dropdown",s)),o.isDefaultPrevented()||(i.attr("aria-expanded","false"),n.removeClass("open").trigger(t.Event("hidden.bs.dropdown",s)))))}))}function i(e){return this.each(function(){var o=t(this),i=o.data("bs.dropdown");i||o.data("bs.dropdown",i=new a(this)),"string"==typeof e&&i[e].call(o)})}var n=".dropdown-backdrop",s='[data-toggle="dropdown"]',a=function(e){t(e).on("click.bs.dropdown",this.toggle)};a.VERSION="3.4.1",a.prototype.toggle=function(i){var n=t(this);if(!n.is(".disabled, :disabled")){var s=e(n),a=s.hasClass("open");if(o(),!a){"ontouchstart"in document.documentElement&&!s.closest(".navbar-nav").length&&t(document.createElement("div")).addClass("dropdown-backdrop").insertAfter(t(this)).on("click",o);var r={relatedTarget:this};if(s.trigger(i=t.Event("show.bs.dropdown",r)),i.isDefaultPrevented())return;n.trigger("focus").attr("aria-expanded","true"),s.toggleClass("open").trigger(t.Event("shown.bs.dropdown",r))}return!1}},a.prototype.keydown=function(o){if(/(38|40|27|32)/.test(o.which)&&!/input|textarea/i.test(o.target.tagName)){var i=t(this);if(o.preventDefault(),o.stopPropagation(),!i.is(".disabled, :disabled")){var n=e(i),a=n.hasClass("open");if(!a&&27!=o.which||a&&27==o.which)return 27==o.which&&n.find(s).trigger("focus"),i.trigger("click");var r=" li:not(.disabled):visible a",d=n.find(".dropdown-menu"+r);if(d.length){var l=d.index(o.target);38==o.which&&l>0&&l--,40==o.which&&l<d.length-1&&l++,~l||(l=0),d.eq(l).trigger("focus")}}}};var r=t.fn.dropdown;t.fn.dropdown=i,t.fn.dropdown.Constructor=a,t.fn.dropdown.noConflict=function(){return t.fn.dropdown=r,this},t(document).on("click.bs.dropdown.data-api",o).on("click.bs.dropdown.data-api",".dropdown form",function(t){t.stopPropagation()}).on("click.bs.dropdown.data-api",s,a.prototype.toggle).on("keydown.bs.dropdown.data-api",s,a.prototype.keydown).on("keydown.bs.dropdown.data-api",".dropdown-menu",a.prototype.keydown)}(jQuery),+function(t){"use strict";function e(e,i){return this.each(function(){var n=t(this),s=n.data("bs.modal"),a=t.extend({},o.DEFAULTS,n.data(),"object"==typeof e&&e);s||n.data("bs.modal",s=new o(this,a)),"string"==typeof e?s[e](i):a.show&&s.show(i)})}var o=function(e,o){this.options=o,this.$body=t(document.body),this.$element=t(e),this.$dialog=this.$element.find(".modal-dialog"),this.$backdrop=null,this.isShown=null,this.originalBodyPad=null,this.scrollbarWidth=0,this.ignoreBackdropClick=!1,this.fixedContent=".navbar-fixed-top, .navbar-fixed-bottom",this.options.remote&&this.$element.find(".modal-content").load(this.options.remote,t.proxy(function(){this.$element.trigger("loaded.bs.modal")},this))};o.VERSION="3.4.1",o.TRANSITION_DURATION=300,o.BACKDROP_TRANSITION_DURATION=150,o.DEFAULTS={backdrop:!0,keyboard:!0,show:!0},o.prototype.toggle=function(t){return this.isShown?this.hide():this.show(t)},o.prototype.show=function(e){var i=this,n=t.Event("show.bs.modal",{relatedTarget:e});this.$element.trigger(n),this.isShown||n.isDefaultPrevented()||(this.isShown=!0,this.checkScrollbar(),this.setScrollbar(),this.$body.addClass("modal-open"),this.escape(),this.resize(),this.$element.on("click.dismiss.bs.modal",'[data-dismiss="modal"]',t.proxy(this.hide,this)),this.$dialog.on("mousedown.dismiss.bs.modal",function(){i.$element.one("mouseup.dismiss.bs.modal",function(e){t(e.target).is(i.$element)&&(i.ignoreBackdropClick=!0)})}),this.backdrop(function(){var n=t.support.transition&&i.$element.hasClass("fade");i.$element.parent().length||i.$element.appendTo(i.$body),i.$element.show().scrollTop(0),i.adjustDialog(),n&&i.$element[0].offsetWidth,i.$element.addClass("in"),i.enforceFocus();var s=t.Event("shown.bs.modal",{relatedTarget:e});n?i.$dialog.one("bsTransitionEnd",function(){i.$element.trigger("focus").trigger(s)}).emulateTransitionEnd(o.TRANSITION_DURATION):i.$element.trigger("focus").trigger(s)}))},o.prototype.hide=function(e){e&&e.preventDefault(),e=t.Event("hide.bs.modal"),this.$element.trigger(e),this.isShown&&!e.isDefaultPrevented()&&(this.isShown=!1,this.escape(),this.resize(),t(document).off("focusin.bs.modal"),this.$element.removeClass("in").off("click.dismiss.bs.modal").off("mouseup.dismiss.bs.modal"),this.$dialog.off("mousedown.dismiss.bs.modal"),t.support.transition&&this.$element.hasClass("fade")?this.$element.one("bsTransitionEnd",t.proxy(this.hideModal,this)).emulateTransitionEnd(o.TRANSITION_DURATION):this.hideModal())},o.prototype.enforceFocus=function(){t(document).off("focusin.bs.modal").on("focusin.bs.modal",t.proxy(function(t){document===t.target||this.$element[0]===t.target||this.$element.has(t.target).length||this.$element.trigger("focus")},this))},o.prototype.escape=function(){this.isShown&&this.options.keyboard?this.$element.on("keydown.dismiss.bs.modal",t.proxy(function(t){27==t.which&&this.hide()},this)):this.isShown||this.$element.off("keydown.dismiss.bs.modal")},o.prototype.resize=function(){this.isShown?t(window).on("resize.bs.modal",t.proxy(this.handleUpdate,this)):t(window).off("resize.bs.modal")},o.prototype.hideModal=function(){var t=this;this.$element.hide(),this.backdrop(function(){t.$body.removeClass("modal-open"),t.resetAdjustments(),t.resetScrollbar(),t.$element.trigger("hidden.bs.modal")})},o.prototype.removeBackdrop=function(){this.$backdrop&&this.$backdrop.remove(),this.$backdrop=null},o.prototype.backdrop=function(e){var i=this,n=this.$element.hasClass("fade")?"fade":"";if(this.isShown&&this.options.backdrop){var s=t.support.transition&&n;if(this.$backdrop=t(document.createElement("div")).addClass("modal-backdrop "+n).appendTo(this.$body),this.$element.on("click.dismiss.bs.modal",t.proxy(function(t){return this.ignoreBackdropClick?void(this.ignoreBackdropClick=!1):void(t.target===t.currentTarget&&("static"==this.options.backdrop?this.$element[0].focus():this.hide()))},this)),s&&this.$backdrop[0].offsetWidth,this.$backdrop.addClass("in"),!e)return;s?this.$backdrop.one("bsTransitionEnd",e).emulateTransitionEnd(o.BACKDROP_TRANSITION_DURATION):e()}else if(!this.isShown&&this.$backdrop){this.$backdrop.removeClass("in");var a=function(){i.removeBackdrop(),e&&e()};t.support.transition&&this.$element.hasClass("fade")?this.$backdrop.one("bsTransitionEnd",a).emulateTransitionEnd(o.BACKDROP_TRANSITION_DURATION):a()}else e&&e()},o.prototype.handleUpdate=function(){this.adjustDialog()},o.prototype.adjustDialog=function(){var t=this.$element[0].scrollHeight>document.documentElement.clientHeight;this.$element.css({paddingLeft:!this.bodyIsOverflowing&&t?this.scrollbarWidth:"",paddingRight:this.bodyIsOverflowing&&!t?this.scrollbarWidth:""})},o.prototype.resetAdjustments=function(){this.$element.css({paddingLeft:"",paddingRight:""})},o.prototype.checkScrollbar=function(){var t=window.innerWidth;if(!t){var e=document.documentElement.getBoundingClientRect();t=e.right-Math.abs(e.left)}this.bodyIsOverflowing=document.body.clientWidth<t,this.scrollbarWidth=this.measureScrollbar()},o.prototype.setScrollbar=function(){var e=parseInt(this.$body.css("padding-right")||0,10);this.originalBodyPad=document.body.style.paddingRight||"";var o=this.scrollbarWidth;this.bodyIsOverflowing&&(this.$body.css("padding-right",e+o),t(this.fixedContent).each(function(e,i){var n=i.style.paddingRight,s=t(i).css("padding-right");t(i).data("padding-right",n).css("padding-right",parseFloat(s)+o+"px")}))},o.prototype.resetScrollbar=function(){this.$body.css("padding-right",this.originalBodyPad),t(this.fixedContent).each(function(e,o){var i=t(o).data("padding-right");t(o).removeData("padding-right"),o.style.paddingRight=i?i:""})},o.prototype.measureScrollbar=function(){var t=document.createElement("div");t.className="modal-scrollbar-measure",this.$body.append(t);var e=t.offsetWidth-t.clientWidth;return this.$body[0].removeChild(t),e};var i=t.fn.modal;t.fn.modal=e,t.fn.modal.Constructor=o,t.fn.modal.noConflict=function(){return t.fn.modal=i,this},t(document).on("click.bs.modal.data-api",'[data-toggle="modal"]',function(o){var i=t(this),n=i.attr("href"),s=i.attr("data-target")||n&&n.replace(/.*(?=#[^\s]+$)/,""),a=t(document).find(s),r=a.data("bs.modal")?"toggle":t.extend({remote:!/#/.test(n)&&n},a.data(),i.data());i.is("a")&&o.preventDefault(),a.one("show.bs.modal",function(t){t.isDefaultPrevented()||a.one("hidden.bs.modal",function(){i.is(":visible")&&i.trigger("focus")})}),e.call(a,r,this)})}(jQuery),+function(t){"use strict";function e(e){return this.each(function(){var i=t(this),n=i.data("bs.tab");n||i.data("bs.tab",n=new o(this)),"string"==typeof e&&n[e]()})}var o=function(e){this.element=t(e)};o.VERSION="3.4.1",o.TRANSITION_DURATION=150,o.prototype.show=function(){var e=this.element,o=e.closest("ul:not(.dropdown-menu)"),i=e.data("target");if(i||(i=e.attr("href"),i=i&&i.replace(/.*(?=#[^\s]*$)/,"")),!e.parent("li").hasClass("active")){var n=o.find(".active:last a"),s=t.Event("hide.bs.tab",{relatedTarget:e[0]}),a=t.Event("show.bs.tab",{relatedTarget:n[0]});if(n.trigger(s),e.trigger(a),!a.isDefaultPrevented()&&!s.isDefaultPrevented()){var r=t(document).find(i);this.activate(e.closest("li"),o),this.activate(r,r.parent(),function(){n.trigger({type:"hidden.bs.tab",relatedTarget:e[0]}),e.trigger({type:"shown.bs.tab",relatedTarget:n[0]})})}}},o.prototype.activate=function(e,i,n){function s(){a.removeClass("active").find("> .dropdown-menu > .active").removeClass("active").end().find('[data-toggle="tab"]').attr("aria-expanded",!1),e.addClass("active").find('[data-toggle="tab"]').attr("aria-expanded",!0),r?(e[0].offsetWidth,e.addClass("in")):e.removeClass("fade"),e.parent(".dropdown-menu").length&&e.closest("li.dropdown").addClass("active").end().find('[data-toggle="tab"]').attr("aria-expanded",!0),n&&n()}var a=i.find("> .active"),r=n&&t.support.transition&&(a.length&&a.hasClass("fade")||!!i.find("> .fade").length);a.length&&r?a.one("bsTransitionEnd",s).emulateTransitionEnd(o.TRANSITION_DURATION):s(),a.removeClass("in")};var i=t.fn.tab;t.fn.tab=e,t.fn.tab.Constructor=o,t.fn.tab.noConflict=function(){return t.fn.tab=i,this};var n=function(o){o.preventDefault(),e.call(t(this),"show")};t(document).on("click.bs.tab.data-api",'[data-toggle="tab"]',n).on("click.bs.tab.data-api",'[data-toggle="pill"]',n)}(jQuery);

/*
* Project: Bootstrap Notify = v3.1.5
* Description: Turns standard Bootstrap alerts into "Growl-like" notifications.
* Author: Mouse0270 aka Robert McIntosh
* License: MIT License
* Website: https://github.com/mouse0270/bootstrap-growl
*/

/* global define:false, require: false, jQuery:false */

!function(t){"function"==typeof define&&define.amd?define(["jquery"],t):"object"==typeof exports?t(require("jquery")):t(jQuery)}(function(o){var i={element:"body",position:null,type:"info",allow_dismiss:!0,allow_duplicates:!0,newest_on_top:!1,showProgressbar:!1,placement:{from:"top",align:"right"},offset:20,spacing:10,z_index:1031,delay:5e3,timer:1e3,url_target:"_blank",mouse_over:null,animate:{enter:"animated fadeInDown",exit:"animated fadeOutUp"},onShow:null,onShown:null,onClose:null,onClosed:null,onClick:null,icon_type:"class",template:'<div data-notify="container" class="col-xs-11 col-sm-4 alert alert-{0}" role="alert"><button type="button" aria-hidden="true" class="close" data-notify="dismiss">&times;</button><span data-notify="icon"></span> <span data-notify="title">{1}</span> <span data-notify="message">{2}</span><div class="progress" data-notify="progressbar"><div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div></div><a href="{3}" target="{4}" data-notify="url"></a></div>'};function e(t,s,e){var n,a,s={content:{message:"object"==typeof s?s.message:s,title:s.title||"",icon:s.icon||"",url:s.url||"#",target:s.target||"-"}};e=o.extend(!0,{},s,e),this.settings=o.extend(!0,{},i,e),this._defaults=i,"-"===this.settings.content.target&&(this.settings.content.target=this.settings.url_target),this.animations={start:"webkitAnimationStart oanimationstart MSAnimationStart animationstart",end:"webkitAnimationEnd oanimationend MSAnimationEnd animationend"},"number"==typeof this.settings.offset&&(this.settings.offset={x:this.settings.offset,y:this.settings.offset}),!this.settings.allow_duplicates&&(this.settings.allow_duplicates||(n=this,a=!1,o('[data-notify="container"]').each(function(t,s){var e=o(s),i=e.find('[data-notify="title"]').html().trim(),s=e.find('[data-notify="message"]').html().trim(),i=i===o("<div>"+n.settings.content.title+"</div>").html().trim(),s=s===o("<div>"+n.settings.content.message+"</div>").html().trim(),e=e.hasClass("alert-"+n.settings.type);return i&&s&&e&&(a=!0),!a}),a))||this.init()}String.format=function(){var s=arguments;return arguments[0].replace(/(\{\{\d\}\}|\{\d\})/g,function(t){if("{{"===t.substring(0,2))return t;t=parseInt(t.match(/\d/)[0]);return s[t+1]})},o.extend(e.prototype,{init:function(){var a=this;this.buildNotify(),this.settings.content.icon&&this.setIcon(),"#"!=this.settings.content.url&&this.styleURL(),this.styleDismiss(),this.placement(),this.bind(),this.notify={$ele:this.$ele,update:function(t,s){var e,i={};for(e in"string"==typeof t?i[t]=s:i=t,i)switch(e){case"type":this.$ele.removeClass("alert-"+a.settings.type),this.$ele.find('[data-notify="progressbar"] > .progress-bar').removeClass("progress-bar-"+a.settings.type),a.settings.type=i[e],this.$ele.addClass("alert-"+i[e]).find('[data-notify="progressbar"] > .progress-bar').addClass("progress-bar-"+i[e]);break;case"icon":var n=this.$ele.find('[data-notify="icon"]');"class"===a.settings.icon_type.toLowerCase()?n.removeClass(a.settings.content.icon).addClass(i[e]):(n.is("img")||n.find("img"),n.attr("src",i[e])),a.settings.content.icon=i[t];break;case"progress":n=a.settings.delay-a.settings.delay*(i[e]/100);this.$ele.data("notify-delay",n),this.$ele.find('[data-notify="progressbar"] > div').attr("aria-valuenow",i[e]).css("width",i[e]+"%");break;case"url":this.$ele.find('[data-notify="url"]').attr("href",i[e]);break;case"target":this.$ele.find('[data-notify="url"]').attr("target",i[e]);break;default:this.$ele.find('[data-notify="'+e+'"]').html(i[e])}s=this.$ele.outerHeight()+parseInt(a.settings.spacing)+parseInt(a.settings.offset.y);a.reposition(s)},close:function(){a.close()}}},buildNotify:function(){var t=this.settings.content;this.$ele=o(String.format(this.settings.template,this.settings.type,t.title,t.message,t.url,t.target)),this.$ele.attr("data-notify-position",this.settings.placement.from+"-"+this.settings.placement.align),this.settings.allow_dismiss||this.$ele.find('[data-notify="dismiss"]').css("display","none"),(this.settings.delay<=0&&!this.settings.showProgressbar||!this.settings.showProgressbar)&&this.$ele.find('[data-notify="progressbar"]').remove()},setIcon:function(){"class"===this.settings.icon_type.toLowerCase()?this.$ele.find('[data-notify="icon"]').addClass(this.settings.content.icon):this.$ele.find('[data-notify="icon"]').is("img")?this.$ele.find('[data-notify="icon"]').attr("src",this.settings.content.icon):this.$ele.find('[data-notify="icon"]').append('<img src="'+this.settings.content.icon+'" alt="Notify Icon" />')},styleDismiss:function(){this.$ele.find('[data-notify="dismiss"]').css({position:"absolute",right:"10px",top:"5px",zIndex:this.settings.z_index+2})},styleURL:function(){this.$ele.find('[data-notify="url"]').css({backgroundImage:"url(data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)",height:"100%",left:0,position:"absolute",top:0,width:"100%",zIndex:this.settings.z_index+1})},placement:function(){var e=this,t=this.settings.offset.y,s={display:"inline-block",margin:"0px auto",position:this.settings.position||("body"===this.settings.element?"fixed":"absolute"),transition:"all .5s ease-in-out",zIndex:this.settings.z_index},i=!1,n=this.settings;switch(o('[data-notify-position="'+this.settings.placement.from+"-"+this.settings.placement.align+'"]:not([data-closing="true"])').each(function(){t=Math.max(t,parseInt(o(this).css(n.placement.from))+parseInt(o(this).outerHeight())+parseInt(n.spacing))}),!0===this.settings.newest_on_top&&(t=this.settings.offset.y),s[this.settings.placement.from]=t+"px",this.settings.placement.align){case"left":case"right":s[this.settings.placement.align]=this.settings.offset.x+"px";break;case"center":s.left=0,s.right=0}this.$ele.css(s).addClass(this.settings.animate.enter),o.each(Array("webkit-","moz-","o-","ms-",""),function(t,s){e.$ele[0].style[s+"AnimationIterationCount"]=1}),o(this.settings.element).append(this.$ele),!0===this.settings.newest_on_top&&(t=parseInt(t)+parseInt(this.settings.spacing)+this.$ele.outerHeight(),this.reposition(t)),o.isFunction(e.settings.onShow)&&e.settings.onShow.call(this.$ele),this.$ele.one(this.animations.start,function(){i=!0}).one(this.animations.end,function(){e.$ele.removeClass(e.settings.animate.enter),o.isFunction(e.settings.onShown)&&e.settings.onShown.call(this)}),setTimeout(function(){i||o.isFunction(e.settings.onShown)&&e.settings.onShown.call(this)},600)},bind:function(){var e,i=this;this.$ele.find('[data-notify="dismiss"]').on("click",function(){i.close()}),o.isFunction(i.settings.onClick)&&this.$ele.on("click",function(t){t.target!=i.$ele.find('[data-notify="dismiss"]')[0]&&i.settings.onClick.call(this,t)}),this.$ele.mouseover(function(){o(this).data("data-hover","true")}).mouseout(function(){o(this).data("data-hover","false")}),this.$ele.data("data-hover","false"),0<this.settings.delay&&(i.$ele.data("notify-delay",i.settings.delay),e=setInterval(function(){var t,s=parseInt(i.$ele.data("notify-delay"))-i.settings.timer;("false"===i.$ele.data("data-hover")&&"pause"===i.settings.mouse_over||"pause"!=i.settings.mouse_over)&&(t=(i.settings.delay-s)/i.settings.delay*100,i.$ele.data("notify-delay",s),i.$ele.find('[data-notify="progressbar"] > div').attr("aria-valuenow",t).css("width",t+"%")),s<=-i.settings.timer&&(clearInterval(e),i.close())},i.settings.timer))},close:function(){var t=this,s=parseInt(this.$ele.css(this.settings.placement.from)),e=!1;this.$ele.attr("data-closing","true").addClass(this.settings.animate.exit),t.reposition(s),o.isFunction(t.settings.onClose)&&t.settings.onClose.call(this.$ele),this.$ele.one(this.animations.start,function(){e=!0}).one(this.animations.end,function(){o(this).remove(),o.isFunction(t.settings.onClosed)&&t.settings.onClosed.call(this)}),setTimeout(function(){e||(t.$ele.remove(),o.isFunction(t.settings.onClosed)&&t.settings.onClosed.call(this))},600)},reposition:function(t){var s=this,e='[data-notify-position="'+this.settings.placement.from+"-"+this.settings.placement.align+'"]:not([data-closing="true"])',i=this.$ele.nextAll(e);!0===this.settings.newest_on_top&&(i=this.$ele.prevAll(e)),i.each(function(){o(this).css(s.settings.placement.from,t),t=parseInt(t)+parseInt(s.settings.spacing)+o(this).outerHeight()})}}),o.notify=function(t,s){return new e(0,t,s).notify},o.notifyDefaults=function(t){return i=o.extend(!0,{},i,t)},o.notifyClose=function(t){o(void 0===t||"all"===t?"[data-notify]":"success"===t||"info"===t||"warning"===t||"danger"===t?".alert-"+t+"[data-notify]":t?t+"[data-notify]":'[data-notify-position="'+t+'"]').find('[data-notify="dismiss"]').trigger("click")},o.notifyCloseExcept=function(t){("success"===t||"info"===t||"warning"===t||"danger"===t?o("[data-notify]").not(".alert-"+t):o("[data-notify]").not(t)).find('[data-notify="dismiss"]').trigger("click")}});