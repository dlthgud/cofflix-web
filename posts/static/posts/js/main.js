$(document).ready(function() {
    $('.filter').click(function() {
        const keyword = $(this).find('.filter-text span').text();
        location.href = '/lists/?keywords[]=' + keyword;
    });

    $('.activity-wrap a').click(function(e) {
        e.preventDefault();
        $('.activity-popup').css('display', 'block');
    });

    $('.close-btn').click(function() {
        $('.activity-popup').css('display', 'none');
    });
});
