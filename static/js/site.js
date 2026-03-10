document.addEventListener("DOMContentLoaded", () => {
    initializeFaq();
    initializeReveals();
});

function initializeFaq() {
    document.querySelectorAll(".faq-trigger").forEach((button) => {
        button.addEventListener("click", () => {
            const item = button.closest(".faq-item");
            if (!item) {
                return;
            }

            const list = item.parentElement;
            if (list) {
                list.querySelectorAll(".faq-item").forEach((entry) => {
                    const trigger = entry.querySelector(".faq-trigger");
                    if (entry !== item) {
                        entry.classList.remove("is-open");
                        if (trigger) {
                            trigger.setAttribute("aria-expanded", "false");
                        }
                    }
                });
            }

            const isOpen = item.classList.toggle("is-open");
            button.setAttribute("aria-expanded", isOpen ? "true" : "false");
        });
    });
}

function initializeReveals() {
    const nodes = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window) || !nodes.length) {
        nodes.forEach((node) => node.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.16,
        },
    );

    nodes.forEach((node) => observer.observe(node));
}
