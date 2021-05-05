$(document).ready(function() {

    var loading = false;
    
    var page = 2;
    var offset = 4;
    
    let url = decodeURI(decodeURIComponent(location.href));
    let param = url.split('?')[1];
    if (typeof param !== 'undefined') {
        let keyword = param.split('=')[1];
        $('.tag-box input[value="'+keyword+'"]').addClass('active');
    }
        
    $('.all').click(function() {
       $('.tag-box input').removeClass('active');
        
        page = 1;
        
        getContent();
    });

    $('.tag-box input').click(function() {
        $(this).toggleClass('active');
        
        page = 1;

        getContent();
    });

    $(window).on('scroll', function() {        
        var scrollHeight = $(document).height();
        var scrollPosition = $(window).height() + $(window).scrollTop();

        if ((scrollPosition > scrollHeight - 500) && loading == false) {
            loading = true;

            getContent(true);
        }
    });
    
    $(document).on('click', '.action-btn', function(event) {
        event.preventDefault();
        
        const cafeId = $(this).parent().data('cafe');
        if ($(this).hasClass('like-btn')) {
            location.replace("/like/" + cafeId + "/?next=" + location.href);
        } else if ($(this).hasClass('mark-btn')) {
            location.replace("/mark/" + cafeId + "/?next=" + location.href);
        }
        
    });

    function getContent(scroll = false) {

        let keywords = [];
        $('.tag-box input.active').each(function() {
            keywords.push($(this).val());
        });

        $.ajax({
            // url: "{% url 'posts:main' %}",
            url: "/lists",
            data: {
                "keywords": keywords,
                "page": page,
                "offset": offset,
            },
            type: 'get',
            dataType: 'json',
            success: function(data) {
                var str = '';
                // console.log(data);
                if (data.cafes) {
                    page++;
                }
                loading = false;
                
                if (!scroll) {
                    $('.filter-list').html('');
                }
                
                $.each(data.cafes, function(idx, cafe) {
                    // console.log(cafe);
                    
                    let $item = $(".filter-item.template").clone();
                    $item.removeClass('template');
                    $item.find('.filter').attr("href", "/" + cafe['id']);
                    $item.find('.swiper-wrapper').attr("id", cafe['id']);
                    
                    $.ajax({
                        url: "/image",
                        data: { "cafe": cafe['id'] },
                        type: 'get',
                        dataType: 'json',
                        success: function(data) {
                            // console.log(data);
                            if(data.images) {
                                data.images.forEach(image => {
                                    let slide = '<div class="swiper-slide">';
                                    slide += '<img src="' + image + '">';
                                    slide += '</div>';
                                    $('#' + cafe['id']).append(slide);
                                });
                                initSwiper();
                            } else {
                                let slide = '<div class="swiper-slide">';
                                    slide += '<img src="/static/posts/images/logo-2.png">';
                                    slide += '</div>';
                            }
                        }
                    })
                    
                    $item.find('.btn-wrap').attr('data-cafe', cafe['id']);
                    if (cafe.liked_users.includes(data.user)) {
                        $item.find('.like-btn img').addClass('active');
                    }
                    if (cafe.marked_users.includes(data.user)) {
                        $item.find('.mark-btn img').addClass('active');
                    }
                    
                    $item.find('.info span').text(cafe['name']);
                    $item.find('.etc').text(cafe['address']);
                    
                    $('.filter-list').append($item);
                });
            },
        });
    }
});


function initSwiper() {
    var swiper = new Swiper(".swiper-container", {
          slidesPerView: 'auto',
          // Optional parameters
          direction: 'horizontal',
          // loop: true,
          lazyLoading: true,

      });
}