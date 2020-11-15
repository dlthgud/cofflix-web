$(document).ready(function() {
    $('.filter').click(function() {
        const keyword = $(this).find('.filter-text span').text();
        location.href = '/lists/?keywords[]=' + keyword;
    });
});