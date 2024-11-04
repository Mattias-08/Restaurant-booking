document.addEventListener('DOMContentLoaded', function() {
    const dateField = document.getElementById('id_date');
    const timeSlotField = document.getElementById('id_time_slot');
    const tableField = document.getElementById('id_table');
    const tableAvailabilityMessage = document.getElementById('table-availability-message');

    console.log('dateField:', dateField);
    console.log('timeSlotField:', timeSlotField);
    console.log('tableField:', tableField);
    console.log('tableAvailabilityMessage:', tableAvailabilityMessage);

    if (dateField && timeSlotField && tableField && tableAvailabilityMessage) {
        const getTablesUrl = "/get_available_tables/";

        const checkTableAvailability = () => {
            const date = dateField.value;
            const timeSlot = timeSlotField.value;

            if (date && timeSlot) {
                fetch(`${getTablesUrl}?date=${date}&time_slot=${timeSlot}`)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.text();
                    })
                    .then(html => {
                        tableField.innerHTML = ''; // Clear existing options
                        tableField.innerHTML = '<option disabled selected value="">-- Select Table --</option>';
                        const tables = JSON.parse(html).tables;
                        if (tables.length > 0) {
                            tables.forEach(tableId => {
                                tableField.innerHTML += `<option value="${tableId}">Table ${tableId}</option>`;
                            });
                            tableField.disabled = false;
                            tableAvailabilityMessage.textContent = '';
                        } else {
                            tableAvailabilityMessage.textContent = "No tables available for this time slot.";
                            tableField.disabled = true; // Disable table selection
                        }
                    })
                    .catch(error => console.error('Error checking table availability:', error));
            }
        };

        dateField.addEventListener('change', checkTableAvailability);
        timeSlotField.addEventListener('change', checkTableAvailability);
    } else {
        console.error("One or more form elements are missing.");
    }
});
