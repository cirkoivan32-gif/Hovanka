(function () {
    const USERS_KEY = "codevanta_users";
    const SESSION_KEY = "codevanta_session";
    readSiteData();

    initializeReveals();
    initializeBotTabs();
    initializeFaq();
    initializeModals();
    initializeAuthForms();
    initializeSessionUi();
    initializeLogout();
})();

function readSiteData() {
    const node = document.getElementById("site-data");
    if (!node) {
        return {};
    }

    try {
        return JSON.parse(node.textContent || "{}");
    } catch (error) {
        return {};
    }
}

function initializeReveals() {
    const items = document.querySelectorAll(".reveal");
    if (!items.length) {
        return;
    }

    if (!("IntersectionObserver" in window)) {
        items.forEach((item) => item.classList.add("is-visible"));
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
        { threshold: 0.12 }
    );

    items.forEach((item) => observer.observe(item));
}

function initializeBotTabs() {
    const tabs = Array.from(document.querySelectorAll("[data-bot-target]"));
    const panels = Array.from(document.querySelectorAll("[data-bot-panel]"));
    if (!tabs.length || !panels.length) {
        return;
    }

    tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            const target = tab.dataset.botTarget;
            tabs.forEach((item) => item.classList.toggle("is-active", item === tab));
            panels.forEach((panel) => {
                panel.classList.toggle("is-active", panel.dataset.botPanel === target);
            });
        });
    });
}

function initializeFaq() {
    const items = Array.from(document.querySelectorAll(".faq-item"));
    items.forEach((item) => {
        const button = item.querySelector(".faq-trigger");
        if (!button) {
            return;
        }

        button.addEventListener("click", () => {
            const willOpen = !item.classList.contains("is-open");
            items.forEach((entry) => {
                const entryButton = entry.querySelector(".faq-trigger");
                entry.classList.remove("is-open");
                if (entryButton) {
                    entryButton.setAttribute("aria-expanded", "false");
                }
            });

            item.classList.toggle("is-open", willOpen);
            button.setAttribute("aria-expanded", willOpen ? "true" : "false");
        });
    });
}

function initializeModals() {
    const layer = document.querySelector("[data-modal-layer]");
    if (!layer) {
        return;
    }

    document.querySelectorAll(".js-open-register").forEach((button) => {
        button.addEventListener("click", () => {
            if (getCurrentUser()) {
                window.location.href = "/app/";
                return;
            }

            openModal("register");
        });
    });

    document.querySelectorAll(".js-open-login").forEach((button) => {
        button.addEventListener("click", () => openModal("login"));
    });

    layer.querySelectorAll("[data-close-modal]").forEach((button) => {
        button.addEventListener("click", closeModal);
    });

    layer.querySelectorAll("[data-switch-modal]").forEach((button) => {
        button.addEventListener("click", () => openModal(button.dataset.switchModal));
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeModal();
        }
    });
}

function initializeAuthForms() {
    document.querySelectorAll("[data-auth-form]").forEach((form) => {
        form.addEventListener("submit", async (event) => {
            event.preventDefault();
            const action = form.dataset.authForm;
            if (action === "register") {
                await handleRegister(form);
                return;
            }

            if (action === "login") {
                await handleLogin(form);
            }
        });
    });
}

function initializeSessionUi() {
    const user = getCurrentUser();
    if (document.body.dataset.page === "app") {
        hydrateApp(user);
        if (!user) {
            openModal("login");
        }
        return;
    }

    if (!user) {
        return;
    }

    document.querySelectorAll(".js-open-register").forEach((button) => {
        button.textContent = "Open workspace";
    });
}

function initializeLogout() {
    document.querySelectorAll("[data-logout-button]").forEach((button) => {
        button.addEventListener("click", () => {
            localStorage.removeItem(SESSION_KEY);
            window.location.href = "/";
        });
    });
}

async function handleRegister(form) {
    const status = getStatusNode("register");
    setStatus(status, "Creating workspace...", "pending");

    const formData = new FormData(form);
    const name = (formData.get("name") || "").toString().trim();
    const email = normalizeEmail(formData.get("email"));
    const password = (formData.get("password") || "").toString();
    const focus = (formData.get("focus") || "").toString().trim() || "Mixed routine";

    if (!name || !email || password.length < 8) {
        setStatus(status, "Enter a valid name, email, and password.", "error");
        return;
    }

    const users = readUsers();
    if (users[email]) {
        setStatus(status, "This email already has a local workspace. Log in instead.", "error");
        return;
    }

    const passwordHash = await hashValue(password);
    users[email] = {
        name,
        email,
        focus,
        passwordHash,
        createdAt: new Date().toISOString(),
    };
    writeUsers(users);
    setSession(email);
    setStatus(status, "Workspace created. Opening app...", "success");
    form.reset();
    window.setTimeout(() => {
        window.location.href = "/app/";
    }, 350);
}

async function handleLogin(form) {
    const status = getStatusNode("login");
    setStatus(status, "Checking access...", "pending");

    const formData = new FormData(form);
    const email = normalizeEmail(formData.get("email"));
    const password = (formData.get("password") || "").toString();

    if (!email || password.length < 8) {
        setStatus(status, "Enter your email and password.", "error");
        return;
    }

    const users = readUsers();
    const user = users[email];
    if (!user) {
        setStatus(status, "No local workspace found for this email.", "error");
        return;
    }

    const passwordHash = await hashValue(password);
    if (user.passwordHash !== passwordHash) {
        setStatus(status, "Password does not match this local workspace.", "error");
        return;
    }

    setSession(email);
    setStatus(status, "Access granted. Opening workspace...", "success");

    if (document.body.dataset.page === "app") {
        closeModal();
        hydrateApp(user);
        form.reset();
        return;
    }

    window.setTimeout(() => {
        window.location.href = "/app/";
    }, 300);
}

function hydrateApp(user) {
    const safeUser = user || {
        name: "Guest operator",
        email: "Not connected",
        focus: "Mixed routine",
    };

    setText("[data-session-name]", safeUser.name);
    setText("[data-profile-name]", safeUser.name);
    setText("[data-profile-email]", safeUser.email);
    setText("[data-profile-focus]", safeUser.focus);
    setText("[data-session-focus]", safeUser.focus);
}

function openModal(name) {
    const layer = document.querySelector("[data-modal-layer]");
    if (!layer) {
        return;
    }

    layer.hidden = false;
    document.body.classList.add("modal-open");
    layer.querySelectorAll("[data-modal]").forEach((modal) => {
        modal.hidden = modal.dataset.modal !== name;
    });
}

function closeModal() {
    const layer = document.querySelector("[data-modal-layer]");
    if (!layer) {
        return;
    }

    layer.hidden = true;
    document.body.classList.remove("modal-open");
    layer.querySelectorAll("[data-modal]").forEach((modal) => {
        modal.hidden = true;
    });
}

function getStatusNode(name) {
    return document.querySelector(`[data-form-status="${name}"]`);
}

function setStatus(node, message, type) {
    if (!node) {
        return;
    }

    node.textContent = message;
    node.dataset.state = type;
}

function setText(selector, value) {
    const node = document.querySelector(selector);
    if (node) {
        node.textContent = value;
    }
}

function normalizeEmail(value) {
    return (value || "").toString().trim().toLowerCase();
}

function readUsers() {
    try {
        return JSON.parse(localStorage.getItem(USERS_KEY) || "{}");
    } catch (error) {
        return {};
    }
}

function writeUsers(users) {
    localStorage.setItem(USERS_KEY, JSON.stringify(users));
}

function setSession(email) {
    localStorage.setItem(
        SESSION_KEY,
        JSON.stringify({
            email,
            updatedAt: new Date().toISOString(),
        })
    );
}

function getCurrentUser() {
    try {
        const raw = JSON.parse(localStorage.getItem(SESSION_KEY) || "null");
        if (!raw || !raw.email) {
            return null;
        }

        const users = readUsers();
        return users[raw.email] || null;
    } catch (error) {
        return null;
    }
}

async function hashValue(value) {
    if (window.crypto && window.crypto.subtle) {
        const bytes = new TextEncoder().encode(value);
        const digest = await window.crypto.subtle.digest("SHA-256", bytes);
        return Array.from(new Uint8Array(digest))
            .map((byte) => byte.toString(16).padStart(2, "0"))
            .join("");
    }

    return btoa(value);
}
