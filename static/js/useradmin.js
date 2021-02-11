(function($) {
    $(function() {
        var selectField = $('#id_permission'),
            verified = $('.field-companies');

        function toggleVerified(value) {
            value == 'CS' ? verified.show() : verified.hide();
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);