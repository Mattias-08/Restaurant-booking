$(document).ready(function() {
    const checkTableAvailability = (date, timeSlot) => {
        $.ajax({
            url: "{% url 'get_available_tables' %}",
            type: "GET",
            data: {
                date: date,
                time_slot: timeSlot
            },
            success: function(response) {
                $("#id_table").empty(); // Clear existing options
                $("#id_table").append('<option disabled selected value="">-- Select Table --</option>');

                if (response.tables.length > 0) {
                    $.each(response.tables, function(index, tableId) {
                        $("#id_table").append(`<option value="${tableId}">Table ${tableId}</option>`);
                    });
                } else {
                    $("#table-availability-message").text("No tables available for this time slot.");
                    $("#id_table").prop("disabled", true); // Disable table selection
                }
            },
            error: function(error) {
                console.error("Error checking table availability:", error);
            }
        });
    };

    $('#id_date, #id_time_slot').on('change', () => {
        const selectedDate = $('#id_date').val();
        const selectedTimeSlot = $('#id_time_slot').val();
        checkTableAvailability(selectedDate, selectedTimeSlot);
    });

    const initialDate = $('#id_date').val();
    const initialTimeSlot = $('#id_time_slot').val();
    checkTableAvailability(initialDate, initialTimeSlot);
});