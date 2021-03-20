$(document).ready(function() {
    let i = 0;

    var imageBtn = $('.image-btn').children('button');
    imageBtn.on('click', function() {
        if ($(this).hasClass('right')) {
            i++;
            if (i >= 5) {
                i = 0;
            }
        } else {
            i--;
            if (i < 0) {
                i = 4;
            }
        }
        $('.image-list').animate({
            marginLeft: -100 * i + "%"
        });
    })
});
