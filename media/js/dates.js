$(function(){
    $("#id_arrival_date").datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: new Date(2011, 08, 24),
        maxDate: new Date(2011, 08, 27)
    });
    $("#id_departure_date").datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: new Date(2011, 08, 27),
        maxDate: new Date(2011, 08, 29)
    });
    /*if($("#id_departure_date").datepicker( "getDate" )) {
        $('#id_arrival_date').datepicker('option', 'maxDate', $("#id_departure_date").datepicker('getDate'));
    }
    if($("#id_departure_date").datepicker( "getDate" )) {
        $('#de_la').datepicker('option', 'minDate', $("#id_departure_date").datepicker('getDate'));
    }*/
});
