document.addEventListener('DOMContentLoaded', function() {
    const dateField = document.getElementById('id_date');
    const timeSlotField = document.getElementById('id_time_slot');
    const tableField = document.getElementById('id_table');
    const tableAvailabilityMessage = document.getElementById('table-availability-message');
    const getTablesUrl = "/get_available_tables/";

    // Clear table dropdown on load
    tableField.innerHTML = '<option disabled selected value="">-- Select Table --</option>';

    const checkTableAvailability = () => {
        const date = dateField.value;
        const timeSlot = timeSlotField.value;

        if (date && timeSlot) {
            const url = `${getTablesUrl}?date=${date}&time_slot=${timeSlot}`;
            console.log('Fetching URL:', url); // Log the URL for debugging

            fetch(url)
                .then(response => response.text())
                .then(data => {
                    console.log('Fetch data:', data); // Log the data for debugging
                    const tableIds = data.split(',');
                    tableField.innerHTML = '<option disabled selected value="">-- Select Table --</option>';
                    if (tableIds[0]) {
                        tableIds.forEach(tableId => {
                            tableField.innerHTML += `<option value="${tableId}">Table ${tableId}</option>`;
                        });
                        tableField.disabled = false;
                        tableAvailabilityMessage.textContent = '';
                    } else {
                        tableAvailabilityMessage.textContent = "No tables available for this time slot.";
                        tableField.disabled = true;
                    }
                })
                .catch(error => console.error('Error checking table availability:', error));
        }
    };

    dateField.addEventListener('change', checkTableAvailability);
    timeSlotField.addEventListener('change', checkTableAvailability);
});
