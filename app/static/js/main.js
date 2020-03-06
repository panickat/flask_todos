$(document).ready(function(){

  $("#search_user").submit(function(e){
    e.preventDefault();
  });

  $("#listSearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();

    $("#myList li").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
    
    user = get_user();
    if (user) {        
      $("#under").prop("disabled",false)
      $("#over").prop("disabled",false)
    }else{
      $("#under").prop("disabled",true)
      $("#over").prop("disabled",true)
    }      
  });

  $( "#under" ).on( "click", function() { 
    set_action("under")
  });

  $( "#over" ).on( "click", function() {
    set_action("over")
  });

  function set_action(action){
    user = get_user();
    if (user) {
      $("#"+action+"_frm").attr( "action", '/daily/update_qualify/'+ action +'/'+ user );
    }else{
      event.preventDefault();
    }      
  }

  function get_user() {
    var total_fields = 0;
    var nones = 0;
    var user = '';
    
    $( "#myList li" ).each(function( index ) {
        total_fields += 1;
        ($(this).css("display") == 'none') ? nones += 1 : user = $(this).text();
      });

    if (total_fields - nones != 1) {user=''}
    return user.trim()
  }
  }); 