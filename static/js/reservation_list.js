document.addEventListener('DOMContentLoaded', function() {
    const getReservationsUrl = "/api/reservations/";

    const fetchReservations = () => {
        fetch(getReservationsUrl)
            .then(response => response.json())
            .then(data => {
                const reservationList = document.getElementById('reservation-list');
                reservationList.innerHTML = ''; // Clear existing list
                if (data.length > 0) {
                    data.forEach(reservation => {
                        const { date, time_slot, table } = reservation.fields;
                        const listItem = `
                            <li>
                                Date: ${date}<br>
                                Time: ${time_slot}<br>
                                Table: ${table}
                            </li>
                        `;
                        reservationList.innerHTML += listItem;
                    });
                    document.getElementById('no-reservations').style.display = 'none';
                } else {
                    document.getElementById('no-reservations').style.display = 'block';
                }
            })
            .catch(error => console.error('Error fetching reservations:', error));
    };

    // Call fetchReservations on page load
    fetchReservations();
});