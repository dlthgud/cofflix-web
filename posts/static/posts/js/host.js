$(document).ready(function() {

    $('.tag-box input').click(function() {
        $(this).toggleClass('active');

        getContent();
    });
});