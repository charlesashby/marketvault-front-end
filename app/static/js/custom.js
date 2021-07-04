//CUSTOM-JS

$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-top').fadeIn();
			
        } else {
            $('.back-top').fadeOut();
        }
    });

    // scroll body to 0px on click
    $('.back-top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 1600);
        return false;
    });
});
$(window).scroll(function() {    
    var scroll = $(window).scrollTop();

    if (scroll >= 50) {
        $("header").addClass("fixed-theme");
    } else {
        $("header").removeClass("fixed-theme");
    }
});

$('#main-srch').focus(function () { $('#search-f').addClass('open');})

$('#main-srch').blur(function () {$('#search-f').removeClass('open'); $('.srch-icon').hide();});
$( document ).on( 'keydown', function ( e ) {
    if ( e.keyCode === 27 ) {
        $('#search-f').removeClass('open');
		$('.srch-icon').hide();
    }
});
$('#main-srch').click(function(event){event.preventDefault();
	$('#search-f').addClass('open');
	$('.srch-icon').show();
});
$("#main-srch").keyup(function(){
    if($(this).val()) {
        $(".clear-box").show();
    } 
        
});


$("#reset-btn").click(function(){
	$(".clear-box").hide();
	$('.srch-icon').hide();
});
$(".search-btn").click(function(){
	$(".clear-box").hide();
});


$(document).ready(function(){
  $(".clear-box").hide();
}); 


$(".myloginpage").click(function(){
	$('#lost-modal').modal('hide');
	$('#register-modal').modal('hide');
    $("#login-modal").modal('show');
 });
   $(".myloginpage1").click(function(){
	$('#lost-modal').modal('hide');
	$('#login-modal').modal('hide');
    $("#register-modal").modal('show');
 });

   $(".lostform").click(function(){
	$('#register-modal').modal('hide');
	$('#login-modal').modal('hide');
    $("#lost-modal").modal('show');
 });


