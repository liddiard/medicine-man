$(document).ready(function(){
    $('.artwork, .plaque, .view-item').hide();
    var piece = $('.artwork').first();
    showPiece($('.artwork:visible'), piece);
    $('.next').click(function(){
        var current = $('.artwork:visible');
        var next = current.next().length == 0 ? $('.artwork').first() : current.next();
        showPiece(current, next);
    });
    $('.prev').click(function(){
        var current = $('.artwork:visible');
        var next = current.prev().length == 0 ? $('.artwork').last() : current.prev();
        showPiece(current, next);
    });
});

function showPiece(prev, current) {
    prev.fadeOut(1000);
    prev.find('.plaque, .view-item').fadeOut(500);
    current.fadeIn(1000);
    setTimeout(function(){
        current.find('.plaque').fadeIn(2000);
    }, 2000);
    setTimeout(function(){
        current.find('.view-item').fadeIn(1000);
    }, 4000);
}
