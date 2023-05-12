 var messages = document.querySelectorAll('.alert');
        if (messages.length > 0) {
            messages.forEach(function (message) {
                message.style.display = 'block';
                setTimeout(function () {
                    message.style.display = 'none';
                }, 3000);
            });
        }