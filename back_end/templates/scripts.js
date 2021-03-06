$( function() {
            function log( message ) {
              $( "<div>" ).text( message ).prependTo( "#log" );
              $( "#log" ).scrollTop( 0 );
            }

            $( "#search" ).autocomplete({
              source: function( request, response ) {
                $.ajax( {
                  url: "search.php",
                  dataType: "jsonp",
                  data: {
                    term: request.term
                  },
                  success: function( data ) {
                    response( data );
                  }
                } );
              },
              minLength: 2,
              select: function( event, ui ) {
                log( "Selected: " + ui.item.value + " aka " + ui.item.id );
              }
            } );
          } );

function addToPlanList() {
  temp = document.getElementById("search").value;
  document.getElementById("planList").innerHTML += temp + "<br>";
}
function addToCompletedList() {
  temp = document.getElementById("search").value;
  document.getElementById("completedList").innerHTML += temp + "<br>";
}
