$(document).ready(function() {
    let url = decodeURI(decodeURIComponent(location.href));
    let param = url.split('?')[1];
    let keyword = param.split('=')[1];
    $('.tag-box input[value="'+keyword+'"]').addClass('active');
    
    $('.all').click(function() {
       $('.tag-box input').removeClass('active');
        
        getContent();
    });

    $('.tag-box input').click(function() {
        $(this).toggleClass('active');

        getContent();
    });
});

function getContent() {
    let keywords = [];
    $('.tag-box input.active').each(function() {
        keywords.push($(this).val());
    });

    $.ajax({
        // url: "{% url 'posts:main' %}",
        url: "/lists",
        data: { "keywords": keywords },
        type: 'get',
        dataType: 'json',
        success: function(data) {
            var str = '';
            // console.log(data);
            $.each(data.cafes, function(idx, cafe) {
                // console.log(cafe);
                str += '<li class="filter-item">';
                str += '<a href="" class="filter">';
                str += '<div class="filter-content">';
                str += '<div class="filter-img">';
                str += '<img id="' + cafe['id'] + '" src="' + cafe['img'] + '">';
                $.ajax({
                    url: "/image",
                    data: { "cafe": cafe['id'] },
                    type: 'get',
                    dataType: 'json',
                    success: function(data) {
                        if(data.image) {
                            $('#' + cafe['id']).attr('src', data.image);
                        } else {
                            $('#' + cafe['id']).attr('src', '/static/posts/images/logo-2.png');
                        }
                    }
                })
                str += '</div>';
                str += '<div class="filter-text">';
                str += '<div class="info">';
                str += '<span>' + cafe['name'] + '</span>';
                str += '</div>';
                str += '<div class="etc">';
                str += cafe['address'];
                str += '</div>';
                str += '</div>';
                str += '</div>';
                str += '</a>';
                str += '</li>';
            });
            $('.filter-list').html(str);
        },
    });
}