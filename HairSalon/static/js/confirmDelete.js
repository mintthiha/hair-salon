document.addEventListener("DOMContentLoaded", function () {
    var deleteButtonsMember = document.querySelectorAll('.delete-member');
    var deleteButtonsReport = document.querySelectorAll('.delete-report');
    var deleteButtonsAppoint = document.querySelectorAll('.delete-appointment');

    deleteButtonsMember.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            var userResponse = confirm('Are you sure?');
            if (userResponse) {
                user_id = button.id;
                window.location.href = '/administration/user/members/delete/' + user_id
            } else {
                alert('You have stopped deletion!');
            }
        });
    });

    deleteButtonsReport.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            var userResponse = confirm('Are you sure?');
            if (userResponse) {
                report_id = button.id;
                window.location.href = '/administration/reports/delete/' + report_id
            } else {
                alert('You have stopped deletion!');
            }
        });
    });

    deleteButtonsAppoint.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            var userResponse = confirm('Are you sure?');
            if (userResponse) {
                appoint_id = button.id;
                window.location.href = '/administration/appointments/delete/' + appoint_id
            } else {
                alert('You have stopped deletion!');
            }
        });
    });
});