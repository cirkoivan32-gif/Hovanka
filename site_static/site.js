const USERS_KEY = "codevanta_users";
const SESSION_KEY = "codevanta_session";
const LANGUAGE_KEY = "codevanta_locale";
const SUPPORTED_LOCALES = ["en", "uk", "ru", "pl", "de", "fr", "es", "it", "pt", "tr"];
const TRANSLATIONS = {
    en: {
        language_label: "Language",
        nav_bots: "Bots",
        nav_workflow: "Workflow",
        nav_pricing: "Pricing",
        nav_faq: "FAQ",
        open_app_text: "Open app",
        register_button_text: "Register",
        open_workspace_text: "Open workspace",
        hero_badge: "AI-guided crypto automation workspace",
        hero_title: "Codevanta builds calmer trading flows out of chaotic crypto markets.",
        hero_lead: "Launch bot strategies, score setups before you commit, and run your daily market routine from one focused control surface instead of five noisy tabs.",
        hero_primary_text: "Create Workspace",
        hero_secondary_text: "See Bot Modes",
        hero_status: "Live sandbox preview",
        hero_console_title: "Operator Console",
        hero_console_copy: "Adaptive scoring, protection layers, and ready-to-run bot modes in one workspace.",
        signal_score_label: "Signal score",
        market_mode_label: "Market mode",
        risk_band_label: "Risk band",
        selected_bot_label: "Selected bot",
        session_checkpoints_label: "Session checkpoints",
        bots_heading: "Five trading modes built for different market behavior",
        advantages_heading: "Less tab chaos. More repeatable decisions.",
        workflow_heading: "From idea to execution in a clean four-step loop",
        comparison_heading: "What changes when you move from manual trading to Codevanta",
        connectors_heading: "Built around the exchange stack traders already know",
        quotes_heading: "What the workspace changes for active crypto traders",
        plans_heading: "Start free, then scale into deeper automation",
        faq_heading: "Questions traders usually ask before they commit",
        cta_heading: "Build a Codevanta workspace and test your flow before risking size.",
        cta_primary_text: "Register Free",
        cta_secondary_text: "Open Sandbox App",
        footer_text: "Codevanta is designed as a crypto automation workspace and decision-support environment. It is not a guarantee of returns.",
        instant_workspace_access: "Instant workspace access",
        register_title: "Create your Codevanta workspace",
        login_title: "Return to your operator desk",
        welcome_back: "Welcome back",
        workspace_access: "Workspace access",
        open_saved_sandbox: "Open your saved sandbox",
        workspace_label: "Sandbox workspace",
        app_title: "Your operator dashboard",
        app_copy: "A fast workspace to review market posture, bot readiness, watchlist priorities, and the next actions for the session.",
        back_to_site_text: "Back to site",
        switch_account_text: "Switch account",
        log_out_text: "Log out",
        need_account_first: "Need an account first?",
        register_on_main: "Register on the main page",
        name_label: "Name",
        email_label: "Email",
        password_label: "Password",
        focus_label: "Focus",
        create_local_workspace: "Create local workspace",
        already_registered: "Already registered?",
        log_in_text: "Log in",
        need_new_account: "Need a new account?",
        register_text: "Register",
        guest_operator: "Guest operator",
        not_connected: "Not connected",
        default_focus: "Mixed routine",
        name_placeholder: "Your operator name",
        email_placeholder: "you@example.com",
        password_placeholder: "At least 8 characters",
        saved_password_placeholder: "Your saved password"
    },
    uk: {
        language_label: "Мова",
        nav_bots: "Боти",
        nav_workflow: "Процес",
        nav_pricing: "Тарифи",
        open_app_text: "Відкрити app",
        register_button_text: "Реєстрація",
        open_workspace_text: "Відкрити простір",
        hero_badge: "AI-простір для криптоавтоматизації",
        hero_title: "Codevanta збирає спокійний торговий процес із хаотичного крипторинку.",
        hero_lead: "Запускай бот-стратегії, оцінюй сетапи до входу і веди процес з однієї панелі замість п'яти шумних вкладок.",
        hero_primary_text: "Створити простір",
        hero_secondary_text: "Переглянути режими",
        bots_heading: "П'ять режимів торгівлі під різні сценарії ринку",
        advantages_heading: "Менше хаосу у вкладках. Більше повторюваних рішень.",
        workflow_heading: "Від ідеї до запуску в чіткому чотирикроковому циклі",
        comparison_heading: "Що змінюється після переходу на Codevanta",
        connectors_heading: "Побудовано навколо біржевого стеку, який трейдери вже знають",
        quotes_heading: "Що цей простір змінює для активних криптотрейдерів",
        plans_heading: "Почни безкоштовно, а потім масштабуй автоматизацію",
        faq_heading: "Питання, які трейдери ставлять перед стартом",
        cta_heading: "Створи простір Codevanta і протестуй процес до того, як ризикувати більше.",
        cta_primary_text: "Зареєструватись",
        cta_secondary_text: "Відкрити sandbox app",
        register_title: "Створи свій простір Codevanta",
        login_title: "Повернись до панелі оператора",
        welcome_back: "З поверненням",
        workspace_access: "Доступ до простору",
        open_saved_sandbox: "Відкрити збережений sandbox",
        workspace_label: "Sandbox-простір",
        app_title: "Твоя панель оператора",
        app_copy: "Швидкий простір для перегляду режиму ринку, готовності ботів і наступних дій.",
        back_to_site_text: "Назад на сайт",
        switch_account_text: "Змінити акаунт",
        log_out_text: "Вийти"
    },
    ru: {
        language_label: "Язык",
        nav_bots: "Боты",
        nav_workflow: "Процесс",
        nav_pricing: "Тарифы",
        open_app_text: "Открыть app",
        register_button_text: "Регистрация",
        open_workspace_text: "Открыть пространство",
        hero_badge: "AI-пространство для криптоавтоматизации",
        hero_title: "Codevanta собирает спокойный торговый процесс из хаотичного крипторынка.",
        hero_lead: "Запускай бот-стратегии, оценивай сетапы до входа и веди процесс с одной панели вместо пяти шумных вкладок.",
        hero_primary_text: "Создать пространство",
        hero_secondary_text: "Смотреть режимы",
        bots_heading: "Пять режимов торговли под разные сценарии рынка",
        advantages_heading: "Меньше хаоса во вкладках. Больше повторяемых решений.",
        workflow_heading: "От идеи до запуска в четком цикле из четырех шагов",
        comparison_heading: "Что меняется после перехода на Codevanta",
        cta_heading: "Создай пространство Codevanta и протестируй процесс до большего риска.",
        cta_primary_text: "Зарегистрироваться",
        cta_secondary_text: "Открыть sandbox app",
        register_title: "Создай свое пространство Codevanta",
        login_title: "Вернись к панели оператора",
        workspace_label: "Sandbox-пространство",
        app_title: "Твоя панель оператора",
        back_to_site_text: "Назад на сайт",
        switch_account_text: "Сменить аккаунт",
        log_out_text: "Выйти"
    },
    pl: {
        language_label: "Język",
        nav_bots: "Boty",
        nav_workflow: "Proces",
        nav_pricing: "Cennik",
        open_app_text: "Otwórz app",
        register_button_text: "Rejestracja",
        open_workspace_text: "Otwórz workspace",
        hero_badge: "AI workspace do automatyzacji krypto",
        hero_title: "Codevanta zamienia chaos rynku krypto w spokojniejszy workflow.",
        hero_primary_text: "Utwórz workspace",
        hero_secondary_text: "Zobacz tryby",
        bots_heading: "Pięć trybów tradingowych dla różnych scenariuszy rynku",
        advantages_heading: "Mniej chaosu w kartach. Więcej powtarzalnych decyzji.",
        workflow_heading: "Od pomysłu do wykonania w czystej pętli czterech kroków",
        cta_heading: "Zbuduj workspace Codevanta i przetestuj proces przed większym ryzykiem.",
        cta_primary_text: "Zarejestruj się",
        cta_secondary_text: "Otwórz sandbox app",
        app_title: "Twój panel operatora",
        back_to_site_text: "Powrót do strony",
        switch_account_text: "Zmień konto",
        log_out_text: "Wyloguj"
    },
    de: {
        language_label: "Sprache",
        nav_workflow: "Ablauf",
        nav_pricing: "Preise",
        open_app_text: "App öffnen",
        register_button_text: "Registrieren",
        open_workspace_text: "Workspace öffnen",
        hero_badge: "AI-Workspace für Krypto-Automatisierung",
        hero_title: "Codevanta macht aus chaotischen Kryptomärkten einen ruhigeren Workflow.",
        hero_primary_text: "Workspace erstellen",
        hero_secondary_text: "Modi ansehen",
        bots_heading: "Fünf Trading-Modi für unterschiedliche Marktphasen",
        advantages_heading: "Weniger Tab-Chaos. Mehr wiederholbare Entscheidungen.",
        workflow_heading: "Von der Idee zur Ausführung in einer klaren Vier-Schritt-Schleife",
        cta_heading: "Baue einen Codevanta-Workspace und teste deinen Ablauf vor größerem Risiko.",
        cta_primary_text: "Registrieren",
        cta_secondary_text: "Sandbox-App öffnen",
        back_to_site_text: "Zurück zur Seite",
        switch_account_text: "Konto wechseln",
        log_out_text: "Abmelden"
    },
    fr: {
        language_label: "Langue",
        nav_workflow: "Processus",
        nav_pricing: "Tarifs",
        open_app_text: "Ouvrir l'app",
        register_button_text: "Inscription",
        open_workspace_text: "Ouvrir l'espace",
        hero_badge: "Espace IA pour l'automatisation crypto",
        hero_title: "Codevanta transforme le chaos du marché crypto en workflow plus calme.",
        hero_primary_text: "Créer un espace",
        hero_secondary_text: "Voir les modes",
        bots_heading: "Cinq modes de trading pour différents scénarios de marché",
        advantages_heading: "Moins de chaos dans les onglets. Plus de décisions répétables.",
        workflow_heading: "De l'idée à l'exécution dans une boucle claire en quatre étapes",
        cta_heading: "Crée un espace Codevanta et teste ton process avant de risquer plus gros.",
        cta_primary_text: "S'inscrire",
        cta_secondary_text: "Ouvrir la sandbox app",
        back_to_site_text: "Retour au site",
        switch_account_text: "Changer de compte",
        log_out_text: "Déconnexion"
    },
    es: {
        language_label: "Idioma",
        nav_workflow: "Proceso",
        nav_pricing: "Precios",
        open_app_text: "Abrir app",
        register_button_text: "Registro",
        open_workspace_text: "Abrir espacio",
        hero_badge: "Espacio IA para automatización cripto",
        hero_title: "Codevanta convierte el caos cripto en un flujo más calmado.",
        hero_primary_text: "Crear espacio",
        hero_secondary_text: "Ver modos",
        bots_heading: "Cinco modos de trading para diferentes escenarios de mercado",
        advantages_heading: "Menos caos de pestañas. Más decisiones repetibles.",
        workflow_heading: "De la idea a la ejecución en un ciclo limpio de cuatro pasos",
        cta_heading: "Crea un espacio Codevanta y prueba tu flujo antes de arriesgar más.",
        cta_primary_text: "Registrarse",
        cta_secondary_text: "Abrir sandbox app",
        back_to_site_text: "Volver al sitio",
        switch_account_text: "Cambiar cuenta",
        log_out_text: "Salir"
    },
    it: {
        language_label: "Lingua",
        nav_workflow: "Processo",
        nav_pricing: "Prezzi",
        open_app_text: "Apri app",
        register_button_text: "Registrazione",
        open_workspace_text: "Apri workspace",
        hero_badge: "Workspace AI per l'automazione crypto",
        hero_title: "Codevanta trasforma il caos del mercato crypto in un flusso più calmo.",
        hero_primary_text: "Crea workspace",
        hero_secondary_text: "Vedi modalità",
        bots_heading: "Cinque modalità di trading per diversi scenari di mercato",
        advantages_heading: "Meno caos tra le schede. Più decisioni ripetibili.",
        workflow_heading: "Dall'idea all'esecuzione in un ciclo chiaro di quattro passi",
        cta_heading: "Crea un workspace Codevanta e testa il flusso prima di rischiare di più.",
        cta_primary_text: "Registrati",
        cta_secondary_text: "Apri sandbox app",
        back_to_site_text: "Torna al sito",
        switch_account_text: "Cambia account",
        log_out_text: "Esci"
    },
    pt: {
        language_label: "Idioma",
        nav_workflow: "Processo",
        nav_pricing: "Preços",
        open_app_text: "Abrir app",
        register_button_text: "Cadastro",
        open_workspace_text: "Abrir workspace",
        hero_badge: "Workspace IA para automação cripto",
        hero_title: "Codevanta transforma o caos do mercado cripto em um fluxo mais calmo.",
        hero_primary_text: "Criar workspace",
        hero_secondary_text: "Ver modos",
        bots_heading: "Cinco modos de trading para diferentes cenários de mercado",
        advantages_heading: "Menos caos de abas. Mais decisões repetíveis.",
        workflow_heading: "Da ideia à execução em um ciclo limpo de quatro etapas",
        cta_heading: "Monte um workspace Codevanta e teste seu fluxo antes de arriscar mais.",
        cta_primary_text: "Cadastrar",
        cta_secondary_text: "Abrir sandbox app",
        back_to_site_text: "Voltar ao site",
        switch_account_text: "Trocar conta",
        log_out_text: "Sair"
    },
    tr: {
        language_label: "Dil",
        nav_bots: "Botlar",
        nav_workflow: "Süreç",
        nav_pricing: "Fiyatlar",
        open_app_text: "App aç",
        register_button_text: "Kayıt",
        open_workspace_text: "Workspace aç",
        hero_badge: "Kripto otomasyonu için AI workspace",
        hero_title: "Codevanta, kaotik kripto piyasasını daha sakin bir akışa dönüştürür.",
        hero_primary_text: "Workspace oluştur",
        hero_secondary_text: "Modları gör",
        bots_heading: "Farklı piyasa senaryoları için beş trading modu",
        advantages_heading: "Daha az sekme kaosu. Daha fazla tekrar edilebilir karar.",
        workflow_heading: "Fikirden uygulamaya temiz bir dört adımlı döngü",
        cta_heading: "Codevanta workspace kur ve daha büyük risk almadan önce sürecini test et.",
        cta_primary_text: "Kaydol",
        cta_secondary_text: "Sandbox app aç",
        back_to_site_text: "Siteye dön",
        switch_account_text: "Hesap değiştir",
        log_out_text: "Çıkış"
    }
};
let siteData = {};
let currentLocale = "en";

(function () {
    siteData = readSiteData();
    currentLocale = detectInitialLocale();
    initializeLanguageSwitchers();
    applyTranslations(currentLocale);

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

function detectInitialLocale() {
    const stored = localStorage.getItem(LANGUAGE_KEY);
    if (stored && SUPPORTED_LOCALES.includes(stored)) {
        return stored;
    }

    const browserLocale = (navigator.language || "en").slice(0, 2).toLowerCase();
    if (SUPPORTED_LOCALES.includes(browserLocale)) {
        return browserLocale;
    }

    return "en";
}

function initializeLanguageSwitchers() {
    document.querySelectorAll("[data-language-switcher]").forEach((select) => {
        select.value = currentLocale;
        select.addEventListener("change", () => {
            currentLocale = select.value;
            localStorage.setItem(LANGUAGE_KEY, currentLocale);
            applyTranslations(currentLocale);
        });
    });
}

function translate(key) {
    const localeMap = TRANSLATIONS[currentLocale] || {};
    const englishMap = TRANSLATIONS.en || {};
    return localeMap[key] || englishMap[key] || "";
}

function applyTranslations(locale) {
    currentLocale = locale;
    document.documentElement.lang = locale;

    document.querySelectorAll("[data-language-switcher]").forEach((select) => {
        select.value = locale;
    });

    document.querySelectorAll("[data-i18n]").forEach((node) => {
        const value = translate(node.dataset.i18n);
        if (value) {
            node.textContent = value;
        }
    });

    document.querySelectorAll("[data-i18n-placeholder]").forEach((node) => {
        const value = translate(node.dataset.i18nPlaceholder);
        if (value) {
            node.placeholder = value;
        }
    });

    refreshLocalizedDynamicData();
}

function refreshLocalizedDynamicData() {
    const user = getCurrentUser();

    if (document.body.dataset.page === "app") {
        hydrateApp(user);
    }

    if (document.body.dataset.page !== "app" && user) {
        document.querySelectorAll(".js-open-register").forEach((button) => {
            button.textContent = translate("open_workspace_text");
        });
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
        button.textContent = translate("open_workspace_text");
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
        name: translate("guest_operator") || "Guest operator",
        email: translate("not_connected") || "Not connected",
        focus: translate("default_focus") || "Mixed routine",
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
