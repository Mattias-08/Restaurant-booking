$(document).ready(function() {
    // General constants
    const reservationUrl = "/make_reservation/";
    const getTablesUrl = "/get_available_tables/";
    const dateField = $('#id_date');
    const timeSlotField = $('#id_time_slot');
    const tableField = $('#id_table');
    const tableAvailabilityMessage = $("#table-availability-message");

    // Functions
    const checkTableAvailability = (date, timeSlot) => {
        $.ajax({
            url: getTablesUrl,
            type: "GET",
            data: {
                date: date,
                time_slot: timeSlot
            },
            success: function(response) {
                tableField.empty(); // Clear existing options
                tableField.append('<option disabled selected value="">-- Select Table --</option>');

                if (response.tables.length > 0) {
                    $.each(response.tables, function(index, tableId) {
                        tableField.append(`<option value="${tableId}">Table ${tableId}</option>`);
                    });
                } else {
                    tableAvailabilityMessage.text("No tables available for this time slot.");
                    tableField.prop("disabled", true); // Disable table selection
                }
            },
            error: function(error) {
                console.error("Error checking table availability:", error);
            }
        });
    };

    // Page-specific logic for make_reservation page
    if (window.location.pathname === reservationUrl) {
        dateField.on('change', () => {
            const selectedDate = dateField.val();
            const selectedTimeSlot = timeSlotField.val();
            checkTableAvailability(selectedDate, selectedTimeSlot);
        });

        timeSlotField.on('change', () => {
            const selectedDate = dateField.val();
            const selectedTimeSlot = timeSlotField.val();
            checkTableAvailability(selectedDate, selectedTimeSlot);
        });

        const initialDate = dateField.val();
        const initialTimeSlot = timeSlotField.val();
        checkTableAvailability(initialDate, initialTimeSlot);
    }
});