$(document).ready(function() {

    
    $(document).on('click', '.action-btn', function(event) {
        event.preventDefault();
        
        const cafeId = $(this).parent().data('cafe');
        if ($(this).hasClass('like-btn')) {
            location.replace("/like/" + cafeId + "/?next=" + location.href);
        } else if ($(this).hasClass('mark-btn')) {
            location.replace("/mark/" + cafeId + "/?next=" + location.href);
        }
        
    });
});
