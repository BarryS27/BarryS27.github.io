/*
document.addEventListener("DOMContentLoaded", () => {
    
    gsap.registerPlugin(ScrollTrigger);

    // --- 1. iOS Style "Snappy" Entry Animation ---
    const tl = gsap.timeline();

    tl.to(".navbar", {
        x: 0,
        opacity: 0.3,
        duration: 1.2,
        ease: "expo.out"
    })
    
    .to(".hero-content, .section-label, .card, .footer", {
        y: 0,
        opacity: 1,
        duration: 1,
        stagger: 0.08,
        ease: "expo.out",
        clearProps: "all"
    }, "-=1.0");


    // --- 2. iOS Control Center 3D Tilte ---
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const xRotation = -((y - rect.height / 2) / 25); 
            const yRotation = (x - rect.width / 2) / 25;
            
            gsap.to(card, {
                transform: `perspective(1000px) rotateX(${xRotation}deg) rotateY(${yRotation}deg) scale(1.01)`,
                duration: 0.1,
                ease: "power1.out",
                overwrite: "auto"
            });
        });

        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                transform: "perspective(1000px) rotateX(0) rotateY(0) scale(1)",
                duration: 0.6,
                ease: "elastic.out(1, 0.6)"
            });
        });
    });


    // --- 3. Magnetic Button Press ---
    const buttons = document.querySelectorAll('a.portfolio-btn, a.contact-button, a.project-link-button, .view-work-btn, .navbar a');

    buttons.forEach(btn => {
        btn.addEventListener('mousedown', () => {
            gsap.to(btn, { scale: 0.94, duration: 0.1, ease: "power1.out" });
        });

        btn.addEventListener('mouseup', () => {
            gsap.to(btn, { scale: 1, duration: 0.2, ease: "back.out(1.7)" });
        });
        
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, { scale: 1, duration: 0.2 });
        });
    });

});
