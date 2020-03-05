$(document).ready(function(){
    $("#listSearch").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myList li").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });

    $( "body" ).click(function() {
        var total_fields = 0;
        var nones = 0;
        var user = '';
        
        $( "#myList li" ).each(function( index ) {
            total_fields += 1;
            ($(this).css("display") == 'none') ? nones += 1 : user = $(this).text();
          });
        if (total_fields - nones == 1) {
            console.log(user)
        }
      });

  }); 