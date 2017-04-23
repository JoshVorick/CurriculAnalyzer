/**
 * @file
 * js base functions
 *
 * Includes js behaviors for various toggles and switches
 *
 */
$(function() {

    // Slide out menu
    $('#primary-menus-toggle, #primary-menus-close').click(function(){
        $('#primary-menus-off-canvas').toggleClass('reveal');
        return false;
    });

    // Site search toggle
    $('#site-search-container-switch').click(function(){
        $('#site-search-container').toggle();
        $('#q').focus();
        return false;
    });

    // Site search local/gt toggle
    $('#search-local-selection').click(function(){
        $(this).addClass('checked');
        $('#search-local').show();
        $('#search-gt').hide();
        if ($('#search-gt-selection').hasClass('checked')){
            $('#search-gt-selection').removeClass('checked');
        }
        return false;
    });
    $('#search-gt-selection').click(function(){
        $(this).addClass('checked');
        $('#search-local').hide();
        $('#search-gt').show();
        if ($('#search-local-selection').hasClass('checked')){
            $('#search-local-selection').removeClass('checked');
        }
        return false;
    });

    // adding hover-active class to parent main menu <li>
    $("#main-menu-wrapper > ul.menu > li").hover(
        function () {
            $(this).addClass('hover-active');
        },
        function () {
            $(this).removeClass('hover-active');
        }
    );

    // Main menu functionality
    $("#main-menu-wrapper ul li a").on('touchstart click', function(event) {
        // if toggle button for menu is visible then we're in a mobile viewport, so add accordion behaviors
        if($('#primary-menus-toggle').is(':visible')){
            if($(this).hasClass('been-clicked') || !$(this).parent('li').children('ul').length > 0) {
                // fix for IOS requiring triple-click to navigate to expanded menu item
                window.location.href = $(this).attr('href');
                return true;
            } else {
                event.preventDefault();
                $(this).addClass('been-clicked');
                $(this).parent('li').children('ul').addClass('show');
                return false;
            }
            // else in desktop viewports
        } else {
            // in standard drop-down only make second click necessary for top level items,
            // unless parent <li> has the "hover-active" class, which means we're not in a touch environment
            if(!$(this).hasClass('been-clicked') && $(this).parent('li').parent('ul').index() == 0) {
                if ($(this).parent('li').children('ul').length > 0) {
                    $(this).addClass('been-clicked');
                    // return true if hover class exists (cause we're not in touch environment)
                    if ($(this).parent('li').hasClass('hover-active')) {
                        return true;
                    } else {
                        return false;
                    }
                } else {
                    return true;
                }
            } else {
                return true;
            }
        }
    });

    // Main menu functionality addendum for "nolink" parent <li> items
    // that are constructed via special menu items module
    $("#main-menu-wrapper > ul.menu > li > span.nolink").click(function() {
        // if toggle button for menu is visible then we're in a mobile viewport, so add accordion behaviors
        if($('#primary-menus-toggle').is(':visible')){
            if($(this).hasClass('been-clicked')) {
                $(this).removeClass('been-clicked');
                $(this).parent('li').children('ul').removeClass('show');
            } else {
                $(this).addClass('been-clicked');
                $(this).parent('li').children('ul').addClass('show');
            }
        }
    });

    // Superfooter main display toggle
    $('.js__superfooter-trigger').click(function(){
        var h = $('#superfooter > .row').outerHeight();
        if($(this).hasClass('collapsed')) {
            $(this).removeClass('collapsed');
            // TODO: figure out some easing that works in all viewports
            if ($(window).width() > '815') {
                $('#superfooter').animate({height: h + "px"}, 250, 'swing');
            } else {
                $('#superfooter').removeClass('collapsible');
            }
        } else {
            $(this).addClass('collapsed');
            // TODO: figure out some easing that works in all viewports
            if ($(window).width() > '815') {
                $('#superfooter').animate({height: "0px"}, 250, 'swing');
            } else {
                $('#superfooter').addClass('collapsible');
            }
        }
        return false;
    });

    // Superfooter links toggle
    $('.superfooter-resource-links .title').click(function(){
        if($(this).next().is('ul')){
            $(this).next().toggle();
            if ($(this).hasClass('open')){
                $(this).removeClass('open').addClass('closed');
            } else {
                $(this).removeClass('closed').addClass('open');
            }
            return false;
        }
        return true;
    });

    //code ends

});