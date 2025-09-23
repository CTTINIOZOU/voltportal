SECTIONS = [
    {
        "slug": "merchant_and_services",
        "title": "Merchant & Products/Services",
        "fields": [
            {"type":"text","label":"Merchant Legal Name","mapping_ref":"VASPA.MERCHANT.LEGAL_NAME","required":True},
            {"type":"multicheck","label":"What type of services do you offer?","mapping_ref":"VASPA.SERVICES.OFFERED",
             "options":[
                 {"label":"Exchange between cryptocurrency and fiat currency","value":"exchange_crypto_fiat","option_mapping_ref":"VASPA.SERVICES.OFFERED.EXCHANGE_CRYPTO_FIAT"},
                 {"label":"Exchange between one or more forms of cryptocurrency","value":"exchange_crypto_to_crypto","option_mapping_ref":"VASPA.SERVICES.OFFERED.EXCHANGE_CRYPTO_CRYPTO"}
             ]}
        ]
    },
    {
        "slug": "documents_submit",
        "title": "Documents & Submission",
        "fields": [
            {"type":"date","label":"Date","mapping_ref":"VASPA.SUBMISSION.DATE"},
            {"type":"text","label":"Completed by (Name & Surname)","mapping_ref":"VASPA.SUBMISSION.COMPLETED_BY"}
        ]
    }
]
SECTION_SLUGS = [s["slug"] for s in SECTIONS]
