$(document).ready(function() {
    const getReservationsUrl = "/api/reservations/"; // API endpoint for fetching reservations

    // Fetch reservations
    const fetchReservations = () => {
        console.log("Fetching reservations...");
        $.ajax({
            url: getReservationsUrl,
            type: "GET",
            success: function(response) {
                console.log("Reservations fetched:", response);
                const reservationList = $('#reservation-list');
                reservationList.empty(); // Clear existing list
                const reservations = JSON.parse(response);

                if (reservations.length > 0) {
                    reservations.forEach(reservation => {
                        const data = reservation.fields;
                        reservationList.append(`
                            <li>
                                Date: ${data.date}<br>
                                Time: ${data.time_slot}<br>
                                Table: ${data.table}
                                <button class="edit-reservation" data-id="${reservation.pk}">Edit</button>
                                <button class="delete-reservation" data-id="${reservation.pk}">Delete</button>
                            </li>
                        `);
                    });
                    $('#no-reservations').hide();
                } else {
                    $('#no-reservations').show();
                }
            },
            error: function(error) {
                console.error("Error fetching reservations:", error);
            }
        });
    };

    // Call fetchReservations on page load
    fetchReservations();
});
