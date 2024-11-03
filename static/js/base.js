$(document).ready(function() {
    $('#id_date, #id_time_slot').on('change', function() {
        const selectedDate = $('#id_date').val();
        const selectedTimeSlot = $('#id_time_slot').val();

        $.ajax({
            url: '/get_available_tables/',
            data: {
                date: selectedDate,
                time_slot: selectedTimeSlot
            },
            success: function(response) {
                $('#id_table').empty();
                $.each(response.tables, function(index, tableId) {
                    $('#id_table').append(`<option value="${tableId}">Table ${tableId}</option>`);
                });
            }
        });
    });
});