document.addEventListener('DOMContentLoaded', function() {
    const reservationUrl = "/make_reservation/";
    const getTablesUrl = "/get_available_tables/";
    const dateField = document.getElementById('id_date');
    const timeSlotField = document.getElementById('id_time_slot');
    const tableField = document.getElementById('id_table');
    const tableAvailabilityMessage = document.getElementById('table-availability-message');

    const checkTableAvailability = (date, timeSlot) => {
        fetch(`${getTablesUrl}?date=${date}&time_slot=${timeSlot}`)
            .then(response => response.json())
            .then(data => {
                tableField.innerHTML = '<option disabled selected value="">-- Select Table --</option>';
                if (data.tables.length > 0) {
                    data.tables.forEach(tableId => {
                        const option = document.createElement('option');
                        option.value = tableId;
                        option.textContent = `Table ${tableId}`;
                        tableField.appendChild(option);
                    });
                } else {
                    tableAvailabilityMessage.textContent = "No tables available for this time slot.";
                    tableField.disabled = true; // Disable table selection
                }
            })
            .catch(error => console.error("Error checking table availability:", error));
    };

    if (window.location.pathname === reservationUrl) {
        dateField.addEventListener('change', () => {
            const selectedDate = dateField.value;
            const selectedTimeSlot = timeSlotField.value;
            checkTableAvailability(selectedDate, selectedTimeSlot);
        });

        timeSlotField.addEventListener('change', () => {
            const selectedDate = dateField.value;
            const selectedTimeSlot = timeSlotField.value;
            checkTableAvailability(selectedDate, selectedTimeSlot);
        });

        const initialDate = dateField.value;
        const initialTimeSlot = timeSlotField.value;
        checkTableAvailability(initialDate, initialTimeSlot);
    }
});
