TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Django context processors
                "django.template.context_processors.i18n",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Django CMS context processors
                "cms.context_processors.cms_settings",
                # Third-party context processors
                "sekizai.context_processors.sekizai",
            ],
        },
    },
]

CMS_TEMPLATES = [
    ("home.html", "Home page template"),
]
