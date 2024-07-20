document.addEventListener('DOMContentLoaded', function() {
    const progressCircles = document.querySelectorAll('.progress-circle');

    progressCircles.forEach(circle => {
        const value = circle.getAttribute('data-value');
        const progress = circle.querySelector('.progress');
        const radius = progress.r.baseVal.value;
        const circumference = 2 * Math.PI * radius;
        const offset = circumference - (value / 100) * circumference;

        progress.style.strokeDashoffset = offset;
    });
});
