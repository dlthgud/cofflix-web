$(document).ready(function() {
    $('.tag-box input').click(function() {
        $(this).toggleClass('active');

        let keywords = [];
        $('.tag-box input.active').each(function() {
            keywords.push($(this).val());
        });

        $.ajax({
            // url: "{% url 'posts:main' %}",
            url: "/",
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
                    str += '<img src="' + cafe['img'] + '">';
                    str += '</div>';
                    str += '<div class="filter-text">';
                    str += '<div class="info">';
                    str += '<span>' + cafe['name'] + '</span>';
                    str += '</div>';
                    str += '<div class="etc">';
                    str += cafe['desc'];
                    str += '</div>';
                    str += '</div>';
                    str += '</div>';
                    str += '</a>';
                    str += '</li>';
                });
                $('.filter-list').html(str);
            },
        });
    });
});
