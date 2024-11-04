document.addEventListener('DOMContentLoaded', function() {
    const reservationList = document.getElementById('reservation-list');
    const noReservationsMessage = document.getElementById('no-reservations');

    // Check if reservations exist and handle display
    if (reservationList) {
        const reservations = Array.from(document.querySelectorAll('.reservation-item'));

        if (reservations.length > 0) {
            console.log('empty')
            noReservationsMessage.style.display = 'none';
        } else {
            console.log('none')
            noReservationsMessage.style.display = 'block';
        }
    }
});
