let isProcessing = false;
function drawCafeItem(num = 0) {
    return new Promise(function(resolve, reject) {
        if(num < 1) {
            reject();
        } else {
            if(!isProcessing) {
                isProcessing = true;
                $.ajax({
                    url: "/rcmd",
                    data: { num },
                    type: 'get',
                    dataType: 'json',
                    success: function(data) {
                        // console.log(data);
                        if(data.result) {
                            const cafe = data.cafe[0];
                            // console.log(cafe);
                            let str = '';
                            str += '<li class="cafe-item">';
                            str += '<a href="" class="cafe">';
                            str += '<div class="cafe-content">';
                            str += '<div class="cafe-img">';
                            str += '<img id="' + cafe['id'] + '" src="/static/posts/images/logo-2.png">';
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
                            str += '<div class="cafe-text">';
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
                            resolve(str);
                        } else {
                            reject('end');
                        }
                    },
                    error: function(err) {
                        reject(err);
                    },
                    complete: function() {
                        isProcessing = false;
                    }
                })
            } else {
                reject();
            }
        }
    })
}

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

    let offset = 4;
    let num = 1;

    $('.page-btn button').click(async function() {
        if($(this).hasClass('prev-btn')) {
            if(num < 2) {
                return;
            }
            try {
                const result = await drawCafeItem(num - 1);
                if(result !== null) {
                    $('.cafe-item').last().remove();
                    $('.cafe-list').prepend(result);
                    num -= 1;
                }
                if($('.next-btn').css('display') === 'none') {
                    $('.next-btn').css('display', 'block');
                }
            } catch (err) {}
        } else {
            try {
                const result = await drawCafeItem(num + offset);
                if(result !== null) {
                    $('.cafe-item').first().remove();
                    $('.cafe-list').append(result);
                    num += 1;
                }
            } catch (err) {
                // console.error(err);
                if(err === 'end') {
                    $('.next-btn').css('display', 'none');
                }
            }
        }
        if(num > 1 && $('.prev-btn').css('display') === 'none') {
            $('.prev-btn').css('display', 'block');
        } else if (num < 2 && $('.prev-btn').css('display') === 'block') {
            $('.prev-btn').css('display', 'none');
        }
        // console.log(num);
    });
});
