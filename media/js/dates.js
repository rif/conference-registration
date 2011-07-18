$(function(){
    $("#id_arrival_date").datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: new Date(2011, 08, 10),
        maxDate: new Date(2011, 08, 20)
    });
    $("#id_departure_date").datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: new Date(2011, 08, 10),
        maxDate: new Date(2011, 08, 20)
    });
    /*if($("#id_departure_date").datepicker( "getDate" )) {
        $('#id_arrival_date').datepicker('option', 'maxDate', $("#id_departure_date").datepicker('getDate'));
    }
    if($("#id_departure_date").datepicker( "getDate" )) {
        $('#de_la').datepicker('option', 'minDate', $("#id_departure_date").datepicker('getDate'));
    }*/
});
