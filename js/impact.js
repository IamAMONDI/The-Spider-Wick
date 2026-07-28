// ==========================================================
// Impact Page — Interactions (Vanilla JS)
// ==========================================================

document.addEventListener("DOMContentLoaded", () => {
    
    // Select all elements that have the 'fade-in' class
    const fadeElements = document.querySelectorAll('.fade-in');

    // Create an Intersection Observer
    // This watches elements to see when they enter the viewport
    const observer = new IntersectionObserver((entries, observer) => {
        
        entries.forEach(entry => {
            // If the element has crossed into the viewport
            if (entry.isIntersecting) {
                // Add the 'visible' class to trigger the CSS transition
                entry.target.classList.add('visible');
                
                // Once it's visible, we don't need to observe it anymore
                observer.unobserve(entry.target);
            }
        });

    }, {
        // Trigger when 15% of the element is visible
        threshold: 0.15,
        // Start triggering slightly before it actually comes into view
        rootMargin: "0px 0px -50px 0px"
    });

    // Attach the observer to every fade element
    fadeElements.forEach(element => {
        observer.observe(element);
    });

});
