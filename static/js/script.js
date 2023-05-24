/* Menu icon functionality */
$(document).ready(function(){
    $("#mobile-menu-trigger").click(function(){
        $("body").toggleClass("mobile-menu-open");
        $("#mobile-menu-trigger").toggleClass("is-clicked");
    });
});

/* About Us dropdown button functionality */
$("#about-us-dropdown-btn").click(function(e){
    e.preventDefault();
    $("#about-us-dropdown").slideToggle();
});
$('#about-us-dropdown-btn').blur(function() {
    $('#about-us-dropdown').hide("slow");
});
$("#about-us-dropdown-mobile-btn").click(function(e){
    e.preventDefault();
    $("#about-us-dropdown-mobile").slideToggle();
});

/* Events dropdown button functionality */
$("#events-dropdown-btn").click(function(e){
    e.preventDefault();
    $("#events-dropdown").slideToggle();
});
$('#events-dropdown-btn').blur(function() {
    $('#events-dropdown').hide(1000);
});
$("#events-dropdown-mobile-btn").click(function(e){
    e.preventDefault();
    $("#events-dropdown-mobile").slideToggle();
});

/* Cart icon functionality */
$("#cart-btn").click(function(event){
    event.preventDefault();
    $(".cart-box").slideToggle();
});
$('#cart-btn').blur(function() {
    $('.cart-box').hide("slow");
});
$("#mobile-cart-btn").click(function(event){
    event.preventDefault();
    $(".cart-box").slideToggle();
});

window.onscroll = function () { scrollFunction() };
function scrollFunction() {
    if (document.body.scrollTop > 60 || document.documentElement.scrollTop > 60) {
        document.getElementById('header').classList.add("minimize");
    } else {
        document.getElementById('header').classList.remove("minimize");
    }

    // if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
    //     document.getElementsByClassName('back-to-top')[0].classList.add("is-visible");
    // } else {
    //     document.getElementsByClassName('back-to-top')[0].classList.remove("is-visible");
    // }
}

contact_btn = document.getElementById("contact-badge");
contact_menu = document.getElementById("contact-badge-menu");
contact_btn.addEventListener("click", function(e) {
    e.preventDefault();
    if (contact_menu.style.visibility == "hidden") {
        contact_menu.style.visibility = "visible";
        contact_menu.style.opacity = "1";
        contact_btn.style.backgroundColor = "#440659";
        contact_btn.style.color = "#ffffff";
        contact_btn.innerHTML = '<i class="fa-solid fa-x"></i>';
    } else {
        contact_menu.style.visibility = "hidden";
        contact_menu.style.opacity = "0";
        contact_btn.style.backgroundColor = "#D9D9D9";
        contact_btn.style.color = "#440659";
        contact_btn.innerHTML = '<i class="fa-regular fa-comment-dots"></i>';
    }
});
contact_btn.addEventListener("blur", function() {
    contact_menu.style.visibility = "hidden";
    contact_menu.style.opacity = "0";
    contact_btn.style.backgroundColor = "#D9D9D9";
        contact_btn.style.color = "#440659";
        contact_btn.innerHTML = '<i class="fa-regular fa-comment-dots"></i>';
});

// const minusItem = document.getElementById('minus-item');
// const plusItem = document.getElementById('plus-item');
// const totalItems = document.getElementById('total-items');
// const onePrice = document.getElementById('one-price');
// const totalPrice = document.getElementById('total-price');
// const total = document.getElementById('total');
// const subtotal = document.getElementById('subtotal');
// const shipping = document.getElementById('shipping');
// minusItem.addEventListener('click', (e) => {
// 	if (totalItems.innerHTML == 0) {
// 		return;
// 	}
// 	totalItems.innerHTML = Number(totalItems.innerHTML) - 1;
// 	totalPrice.innerHTML = Number(totalPrice.innerHTML) - Number(onePrice.innerHTML);
// 	subtotal.innerHTML = totalPrice.innerHTML;
// 	total.innerHTML = Number(totalPrice.innerHTML) + Number(shipping.innerHTML);
//     e.preventDefault();
// });
// plusItem.addEventListener('click', (e) => {
// 	totalItems.innerHTML = Number(totalItems.innerHTML) + 1;
// 	totalPrice.innerHTML = Number(totalPrice.innerHTML) + Number(onePrice.innerHTML);
// 	subtotal.innerHTML = totalPrice.innerHTML;
// 	total.innerHTML = Number(totalPrice.innerHTML) + Number(shipping.innerHTML);
//     e.preventDefault();
// });