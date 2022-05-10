new tempusDominus.TempusDominus(document.getElementById('enabledDisabled'), {
    display: {
        viewMode: 'clock',
        sideBySide: false,
        icons: {
            time: 'bi bi-calendar',
            date: 'bi bi-clock',
            up: 'bi bi-arrow-up',
            down: 'bi bi-arrow-down',
            previous: 'bi bi-chevron-left',
            next: 'bi bi-chevron-right',
            today: 'bi bi-calendar-check',
            clear: 'bi bi-trash',
            close: 'bi bi-x',
        },
        buttons: {
            today: false,
            clear: true,
            close: true,
        },
        components: {
            decades: false,
            year: true,
            month: true,
            date: true,
            hours: true,
            minutes: false,
            seconds: false,
            useTwentyfourHour: true,
        }
    },
    restrictions: {
        daysOfWeekDisabled: [0, 6],
        disabledHours: [1, 2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22, 23, 24]
    }
});