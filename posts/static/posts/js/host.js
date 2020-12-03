$(document).ready(function() {

    $('.tag-box input').click(function() {
        $(this).toggleClass('active');
    });
    
    $('.btn-signup').click(function() {
        let tags = [];
        $('.tag-box input.active').each(function() {
            tags.push($(this).val());
        });
        $('#tags').val(tags.join(','));
        $('#regist').submit();
    });
});

$(document).on("keyup", ".tel-number", function() {
    let telWithHypen = $(this).val();
    telWithHypen = telWithHypen.replace(/[^0-9]/g, "").replace(/(^02.{0}|^01.{1}|[0-9]{3})([0-9]+)([0-9]{4})/, "$1-$2-$3");
    $(this).val(telWithHypen);
});