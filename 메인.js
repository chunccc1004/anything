jQuery(document).ready(function () {
    var _ = jQuery;
    _body = _('body');

    // 메인 banner
    var _mainBanner = $('.main_banner').bxSlider({
        auto: true, // 자동, 수동 = false
        autoHover: true,
        speed: 500, // 슬라이드 속도 500 = 0.5초
        pause: 5000, // 멈춰있는 시간 3000 = 3초
        controls: true,
        useCSS: false,
        pagerCustom: '#mainSliderPager',
        nextText: '<i class="xi-angle-right-thin"></i>',
        prevText: '<i class="xi-angle-left-thin"></i>',
        onSliderLoad: function () {
            _('.mainSliderWrap').css({
                'height': 'auto', 'overflow': 'visible'
            });
        },
        onSlideBefore: function () {
            _mainBanner.stopAuto();
        },
        onSlideAfter: function () {
            _mainBanner.startAuto();
        }
    });
    //메인 tabProduct
    var newCateProd = _('.newCate_prod'), newCateSlider = newCateProd.find('.newCateSlider').bxSlider({
        autoHover: true,
        pagerCustom: '#newCatePageThumb',
        auto: true,
        stopAutoOnClick: true,
        speed: 400,
        controls: false,
        useCSS: true,
        mode: 'fade',
        onSliderLoad: function () {
            jQuery('#tabProduct ').css("visibility", "visible");
        }
    });
    newCateProd.find('.slideList').on('mouseenter', function () {
        return newCateSlider.stopAuto();
    });
    newCateProd.find('.slideList').on('mouseleave', function () {
        return newCateSlider.startAuto();
    });
    //메인 newCateProd 내부 hover 처리
    newCateProd.find(".item-cont li").mouseenter(function () {
        _(this).find(".prd-info-bx").fadeIn();
    }).mouseleave(function () {
        _(this).find(".prd-info-bx").fadeOut();
    });
});

var target = document.querySelectorAll('.ready'); // 클릭할 버튼요소를 변수 처리

// 팝업 열기
for (var i = 0; i < target.length; i++) {
    target[i].addEventListener('click', function () {
        event.preventDefault(); // 기본 동작을 막습니다.
        alert("준비 중인 페이지입니다.")
    });
}