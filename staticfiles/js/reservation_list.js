document.addEventListener('DOMContentLoaded', function() {
    const reservationList = document.getElementById('reservation-list');
    const noReservationsMessage = document.getElementById('no-reservations');

    if (reservationList && noReservationsMessage) {
        const reservations = Array.from(document.querySelectorAll('.reservation-item'));

        if (reservations.length > 0) {
            reservations.forEach(reservation => {
                reservationList.appendChild(reservation);
            });
            noReservationsMessage.style.display = 'none';
        } else {
            noReservationsMessage.style.display = 'block';
        }
    } else {
        console.error("One or more reservation list elements are missing.");
    }
});
