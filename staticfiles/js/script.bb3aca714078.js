// Set active navigation link based on current page
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-links a');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === currentPath || 
            (currentPath === '/' && link.getAttribute('href').includes('home'))) {
            link.classList.add('active');
        }
    });

    // Form submission handling
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;
            
            // Create mailto link
            const mailtoLink = `mailto:dr.sakthivel@university.edu?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(`From: ${name} (${email})\n\n${message}`)}`;
            
            window.location.href = mailtoLink;
            
            // Clear form
            contactForm.reset();
            
            // Show success message
            showNotification('Message prepared. Your default email client will open.');
        });
    }

    // Add scroll animation for elements
    observeElements();

    // Initialize gallery glance effect
    initGalleryGlance();

    // Initialize full-screen gallery modal
    initGalleryModal();
});

// Initialize Gallery Glance Effect
function initGalleryGlance() {
    const galleryGrid = document.querySelector('.gallery-grid');
    if (!galleryGrid) return;

    const galleryItems = document.querySelectorAll('.gallery-item');
    
    // Add staggered animation to each item
    galleryItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
    });

    // Optional: Start auto-glance cycling through items on hover
    // Disable on touch devices
    if (window.matchMedia("(hover: hover)").matches) {
        galleryGrid.addEventListener('mouseenter', function() {
            startGalleryGlance();
        });

        galleryGrid.addEventListener('mouseleave', function() {
            stopGalleryGlance();
        });
    }
}

let glanceInterval = null;
let currentGlanceIndex = 0;

function startGalleryGlance() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    if (galleryItems.length === 0) return;

    // Clear any existing interval
    if (glanceInterval) clearInterval(glanceInterval);

    glanceInterval = setInterval(() => {
        // Add glance animation effect
        galleryItems.forEach((item, index) => {
            if (index === currentGlanceIndex % galleryItems.length) {
                item.style.transform = 'scale(1.05) translateY(-8px)';
                item.style.filter = 'brightness(1.2)';
            } else {
                item.style.transform = '';
                item.style.filter = '';
            }
        });
        currentGlanceIndex++;
    }, 500);
}

function stopGalleryGlance() {
    if (glanceInterval) {
        clearInterval(glanceInterval);
        glanceInterval = null;
    }
    // Reset all items
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.style.transform = '';
        item.style.filter = '';
    });
}

// Initialize Full-Screen Gallery Modal
let currentModalIndex = 0;
let galleryImages = [];

function initGalleryModal() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const modal = document.getElementById('galleryModal');
    const modalClose = document.querySelector('.modal-close');
    const modalPrev = document.querySelector('.modal-prev');
    const modalNext = document.querySelector('.modal-next');

    // Store gallery data
    galleryImages = Array.from(galleryItems).map(item => ({
        src: item.querySelector('img').src,
        alt: item.querySelector('img').alt,
        caption: item.querySelector('.gallery-overlay-text')?.textContent || ''
    }));

    // Open modal on gallery item click
    galleryItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            currentModalIndex = index;
            openGalleryModal(currentModalIndex);
        });
        // Add cursor pointer
        item.style.cursor = 'pointer';
    });

    // Close modal
    modalClose.addEventListener('click', closeGalleryModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeGalleryModal();
        }
    });

    // Navigation
    modalPrev.addEventListener('click', () => {
        currentModalIndex = (currentModalIndex - 1 + galleryImages.length) % galleryImages.length;
        updateModalImage(currentModalIndex);
    });

    modalNext.addEventListener('click', () => {
        currentModalIndex = (currentModalIndex + 1) % galleryImages.length;
        updateModalImage(currentModalIndex);
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (modal.classList.contains('active')) {
            if (e.key === 'ArrowLeft') {
                currentModalIndex = (currentModalIndex - 1 + galleryImages.length) % galleryImages.length;
                updateModalImage(currentModalIndex);
            } else if (e.key === 'ArrowRight') {
                currentModalIndex = (currentModalIndex + 1) % galleryImages.length;
                updateModalImage(currentModalIndex);
            } else if (e.key === 'Escape') {
                closeGalleryModal();
            }
        }
    });

    // Touch/Swipe navigation for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    modal.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    });

    modal.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });

    function handleSwipe() {
        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;

        if (Math.abs(diff) > swipeThreshold && modal.classList.contains('active')) {
            if (diff > 0) {
                // Swiped left - show next image
                currentModalIndex = (currentModalIndex + 1) % galleryImages.length;
                updateModalImage(currentModalIndex);
            } else {
                // Swiped right - show previous image
                currentModalIndex = (currentModalIndex - 1 + galleryImages.length) % galleryImages.length;
                updateModalImage(currentModalIndex);
            }
        }
    }
}

function openGalleryModal(index) {
    const modal = document.getElementById('galleryModal');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    updateModalImage(index);
}

function closeGalleryModal() {
    const modal = document.getElementById('galleryModal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function updateModalImage(index) {
    const modalImage = document.getElementById('modalImage');
    const modalCaption = document.getElementById('modalCaption');
    
    if (galleryImages[index]) {
        modalImage.src = galleryImages[index].src;
        modalImage.alt = galleryImages[index].alt;
        modalCaption.textContent = galleryImages[index].caption;
    }
}

// Intersection Observer for scroll animations
function observeElements() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'slideInUp 0.6s ease-out forwards';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe achievement and award cards
    document.querySelectorAll('.achievement-card, .award-item').forEach(element => {
        observer.observe(element);
    });
}

// Notification function
function showNotification(message) {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: rgba(0, 255, 65, 0.2);
        border: 1px solid rgba(0, 255, 65, 0.5);
        color: #00ff41;
        padding: 15px 25px;
        border-radius: 10px;
        z-index: 10000;
        font-size: 0.95rem;
        backdrop-filter: blur(10px);
        animation: slideInRight 0.3s ease-out;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideInRight 0.3s ease-out reverse';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add slideInUp animation to stylesheet
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Smooth scroll behavior */
    html {
        scroll-behavior: smooth;
    }

    /* Add glow effect on hover for profile image */
    .profile-image img:hover {
        animation: imageGlow 0.3s ease-out;
    }

    @keyframes imageGlow {
        0% {
            filter: drop-shadow(0 0 30px rgba(0, 255, 65, 0.4));
        }
        100% {
            filter: drop-shadow(0 0 50px rgba(0, 255, 65, 0.8));
        }
    }
`;
document.head.appendChild(style);

// Mouse tracking effect for interactive elements
document.addEventListener('mousemove', function(e) {
    const mouseX = e.clientX / window.innerWidth;
    const mouseY = e.clientY / window.innerHeight;

    // Optional: Add parallax effect if needed
    const profileImage = document.querySelector('.profile-image img');
    if (profileImage) {
        profileImage.style.transform = `scale(1.05) translateY(-10px) rotateY(${mouseX * 5}deg) rotateX(${mouseY * -5}deg)`;
    }
});

// Add loading animation
window.addEventListener('load', function() {
    document.body.style.opacity = '1';
});

// Prevent form default submission and show alert
document.addEventListener('submit', function(e) {
    if (e.target.classList.contains('contact-form')) {
        // Already handled above
        return;
    }
}, true);

// Add keyboard navigation support
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        // Close any open modals or notifications (for future enhancement)
    }
});

console.log('Portfolio interactive features loaded successfully!');
