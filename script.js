document.addEventListener("DOMContentLoaded", () => {
    
    // Register GSAP ScrollTrigger
    gsap.registerPlugin(ScrollTrigger);

    // --- 1. iOS Style Staggered Entry Animation (Loading) ---
    const tl = gsap.timeline();

    tl.from(".navbar", {
        x: -50,
        opacity: 0,
        duration: 1,
        ease: "power3.out"
    })
    .from(".hero-content", {
        y: 30,
        opacity: 0,
        duration: 0.8,
        ease: "back.out(1.7)"
    }, "-=0.5")
    .from(".card:not(.hero-section)", {
        y: 50,
        opacity: 0,
        duration: 0.8,
        stagger: 0.2,
        ease: "power2.out",
        scrollTrigger: {
            trigger: ".container",
            start: "top 80%",
        }
    }, "-=0.6");


    // --- 2. 3D Tilt Effect on Hover ---
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Calculate rotation based on mouse position
            const xRotation = -((y - rect.height / 2) / 20); 
            const yRotation = (x - rect.width / 2) / 20;
            
            // Apply the transformation
            gsap.to(card, {
                transform: `perspective(1000px) rotateX(${xRotation}deg) rotateY(${yRotation}deg) scale(1.02)`,
                duration: 0.1,
                ease: "power1.out"
            });
        });

        // Reset card position when mouse leaves
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                transform: "perspective(1000px) rotateX(0) rotateY(0) scale(1)",
                duration: 0.5,
                ease: "elastic.out(1, 0.5)"
            });
        });
    });


    // --- 3. Interactive Button "Press" Effect ---
    const buttons = document.querySelectorAll('.portfolio-btn, .medium-btn, .contact-button, .view-work-btn');

    buttons.forEach(btn => {
        btn.addEventListener('mousedown', () => {
            gsap.to(btn, { scale: 0.95, duration: 0.1 });
        });

        btn.addEventListener('mouseup', () => {
            gsap.to(btn, { scale: 1, duration: 0.1 });
        });
        
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, { scale: 1, duration: 0.3 });
        });
    });

});
