# abbreviated schema with the final 'documents_submit' to ensure end-to-end
SECTIONS = [
    {
        "slug": "merchant_and_services",
        "title": "Merchant & Products/Services",
        "fields": [
            {"type":"text","label":"Merchant Legal Name","mapping_ref":"VASPA.MERCHANT.LEGAL_NAME","required":True}
        ]
    },
    {
        "slug": "documents_submit",
        "title": "Documents & Submission",
        "fields": [
            {"type":"file","label":"CV of MLRO (upload)","mapping_ref":"VASPA.DOCS.MLRO_CV","multiple":False},
            {"type":"date","label":"Date","mapping_ref":"VASPA.SUBMISSION.DATE"},
            {"type":"text","label":"Completed by (Name & Surname)","mapping_ref":"VASPA.SUBMISSION.COMPLETED_BY"}
        ]
    }
]
SECTION_SLUGS = [s["slug"] for s in SECTIONS]
