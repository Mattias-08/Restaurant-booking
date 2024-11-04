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
               time_slot: timeSlot  // Ensure it's consistent here
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

   // Populate initial reservation list from Django-rendered HTML
   const populateReservationList = () => {
       const reservationList = $('#reservation-list');
       const initialReservations = reservationList.data('reservations'); // Read reservations from data attribute

       if (initialReservations && initialReservations.length > 0) {
           initialReservations.forEach(reservation => {
               reservationList.append(`
                   <li>
                       Date: ${reservation.date}<br>
                       Time: ${reservation.time_slot}<br>
                       Table: ${reservation.table}
                   </li>
               `);
           });
           $('#no-reservations').hide();
       } else {
           $('#no-reservations').show();
       }
   };

   // Page-specific logic
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

       // Populate reservation list
       populateReservationList();
   }