// This function ensures that when the Chess Ending option is acted on, more options appear
$(".submenu").click(function(){
  //.slideToggle () is used to show or hide a sliding element
  $(this).children("ul").slideToggle();
})

//This function ensures that the moment the Chess Ending option is activated and more options appear,
//it causes that event to end at that moment
$("ul").click(function(p){
  p.stopPropagation();
})
