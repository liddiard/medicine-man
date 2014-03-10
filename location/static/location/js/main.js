$(document).ready(function(){
    $('.artwork, .plaque, .view-item').hide();
    var first = $('.artwork').first();
    var current = $('.artwork:visible'); // we need to give showPiece an empty selector
    rotator_intervalid = showPiece(current, first, true);

    /* popups */
    $('body').click(function(){
        $('.popup').fadeOut('fast');
        $('.place').removeClass('active');
    });
    $('.popup').click(function(event){
        event.stopPropagation();
    });
    $('.place').click(function(event){
        event.stopPropagation();
        $('.place').removeClass('active');
        $('.popup').fadeOut('fast');
        var popup = $(this).find('.popup');
        popup.fadeToggle('fast');
        $(this).toggleClass('active');
        populatePlaceDetail(popup);
    });
});


var bindArrows = function() {
    $('.next').click(function(){
        nextSlide();
    });
    $('.prev').click(function(){
        prevSlide();
    });
    $('.next, .prev').removeClass('disabled');
}

function nextSlide() {
    var current = $('.artwork:visible');
    var next = current.next().length == 0 ? $('.artwork').first() : current.next();
    rotator_intervalid = showPiece(current, next, true);
}

function prevSlide() {
    var current = $('.artwork:visible');
    var next = current.prev().length == 0 ? $('.artwork').last() : current.prev();
    rotator_intervalid = showPiece(current, next, false);
}

function showPiece(prev, current, forward) {
    // [jQuery obj] prev: artworks that should be hidden
    // [jQuery obj] current: artworks that should be shown
    // [boolean] forward: moving forward or backward? 
    if (typeof rotator_intervalid != 'undefined') clearInterval(rotator_intervalid);
    $('.next, .prev').unbind('click').addClass('disabled'); // disable buttons while we're transitioning
    if (forward) {
        prev.animate({'background-position-x': '-=50', 'opacity': 0}, 1000).hide(1000);
        current.css({'background-position-x': '50px', 'opacity': 0}).show().animate({'background-position-x': '-=50', 'opacity': 1}, 1000);
    } else {
        prev.animate({'background-position-x': '+=50', 'opacity': 0}, 1000).hide(1000);
        current.css({'background-position-x': '-50px', 'opacity': 0}).show().animate({'background-position-x': '+=50', 'opacity': 1}, 1000);
    }
    prev.find('.plaque, .view-item').fadeOut(500);
    setTimeout(function(){
        current.find('.plaque').fadeIn(2000);
    }, 2000);
    setTimeout(function(){
        current.find('.view-item').fadeIn(1000);
        bindArrows(); // rebind next/prev buttons
    }, 4000);

    return setInterval(function(){ nextSlide() }, 10000);
}

function populatePlaceDetail(elem) {
    if (elem.data('fetched'))
        return; // don't re-request the data if it's already populated
    var reference = elem.data('reference');
    ajaxGet(
        {reference: reference}, 
        '/api/location/place_detail/', 
        function(response){ 
            console.log(response);
            var detail = response.detail;
            elem.find('.phone').text(detail.phone);
            elem.find('.website').text(detail.host).prop('href', detail.url);
            elem.find('.website').text(detail.host).prop('href', detail.url);
            elem.find('.map').prop('src', detail.map);
            elem.find('.map-link').prop('href', detail.map_link);
            if (detail.host.length > 0 && detail.phone.length > 0)
                elem.find('.separator').text(' | ');
            elem.find('.loading').hide();
            elem.data('fetched', true);
        }
    );
}


/* utility functions */

function ajaxGet(params, endpoint, callback_success) {
    $.ajax({
        type: "GET",
        url: endpoint,
        data: params,
        crossDomain: true,
        success: callback_success,
        error: function(xhr, textStatus, errorThrown) {
            if (xhr.status != 0)
                console.error('Oh no! Something went wrong. Please report this error: \n'+errorThrown+xhr.status+xhr.responseText);
        }
    }); 
}
