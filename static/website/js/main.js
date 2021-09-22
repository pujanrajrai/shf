// Begin FAQ Section
let li = document.querySelectorAll(".faq-text li");
for (var i = 0; i < li.length; i++) {
  li[i].addEventListener("click", (e)=>{
    let clickedLi;
    if(e.target.classList.contains("question-arrow")){
      clickedLi = e.target.parentElement;
    }else{
      clickedLi = e.target.parentElement.parentElement;
    }
   clickedLi.classList.toggle("showAnswer");
  });
}
// End FAQ Section
//  Begin Login-Register JS
let container = document.getElementById('container')

toggle = () => {
  container.classList.toggle('sign-in')
  container.classList.toggle('sign-up')
}

setTimeout(() => {
  container.classList.add('sign-in')
}, 200)
// End Login-Register JS

// // Begin FAQ Section
// let li = document.querySelectorAll(".faq-text li");
// for (var i = 0; i < li.length; i++) {
//   li[i].addEventListener("click", (e)=>{
//     let clickedLi;
//     if(e.target.classList.contains("question-arrow")){
//       clickedLi = e.target.parentElement;
//     }else{
//       clickedLi = e.target.parentElement.parentElement;
//     }
//    clickedLi.classList.toggle("showAnswer");
//   });
// }
// // End FAQ Section

// Start Product Section (Index Page)
$(document).ready(function () {
    $("#product-slider").owlCarousel({
        items: 6,
        itemsDestop: [1199, 2],
        itemsDestopSmall: [980, 2],
        itemsMoile: [700, 1],
        pagination: false,
        navigation: true,
        navigationText: ["", ""],
        autoPlay: 1500  //sliding speed 1.5s
    });
});
//   End Product Section

// Start Product Detail Section (Product Detail Page)
var MainImg = document.getElementById('MainImg');
var smallimg = document.getElementsByClassName('small-img');
smallimg[0].onclick = function () {
    MainImg.src = smallimg[0].src;
}
smallimg[1].onclick = function () {
    MainImg.src = smallimg[1].src;
}
smallimg[2].onclick = function () {
    MainImg.src = smallimg[2].src;
}
smallimg[3].onclick = function () {
    MainImg.src = smallimg[3].src;
}
// End Product Detail Section

// Start Scroll Up Section
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    // scroll body to 0px on click
    $('#back-to-top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 400);
        return false;
    });
});
// End Scroll Up Section