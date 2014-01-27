$(document).ready(function(){
    $('.artwork, .plaque, .view-item').hide();
    var first = $('.artwork').first();
    var current = $('.artwork:visible') // we need to give showPiece an empty selector
    showPiece(current, first, true);
});


var bindArrows = function() {
    $('.next').click(function(){
        var current = $('.artwork:visible');
        var next = current.next().length == 0 ? $('.artwork').first() : current.next();
        showPiece(current, next, true);
    });
    $('.prev').click(function(){
        var current = $('.artwork:visible');
        var next = current.prev().length == 0 ? $('.artwork').last() : current.prev();
        showPiece(current, next, false);
    });
    $('.next, .prev').removeClass('disabled');
}

function showPiece(prev, current, forward) {
    // [jQuery obj] prev: artworks that should be hidden
    // [jQuery obj] current: artworks that should be shown
    // [boolean] forward: moving forward or backward? 
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
}
