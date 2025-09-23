# schema.py

SECTIONS = [
    {
        "slug": "merchant_and_services",
        "title": "Merchant & Products/Services",
        "fields": [
            {"type": "text","label": "Merchant Legal Name","mapping_ref": "VASPA.MERCHANT.LEGAL_NAME","required": True},
            {"type": "multicheck","label": "What type of services do you offer?","mapping_ref": "VASPA.SERVICES.OFFERED",
             "options": [
                {"label": "Exchange between cryptocurrency and fiat currency","value": "exchange_crypto_fiat","option_mapping_ref": "VASPA.SERVICES.OFFERED.EXCHANGE_CRYPTO_FIAT"},
                {"label": "Exchange between one or more forms of cryptocurrency","value": "exchange_crypto_to_crypto","option_mapping_ref": "VASPA.SERVICES.OFFERED.EXCHANGE_CRYPTO_CRYPTO"},
                {"label": "Transfer of cryptocurrency","value": "transfer_crypto","option_mapping_ref": "VASPA.SERVICES.OFFERED.TRANSFER"},
                {"label": "Holding custody of cryptocurrency or administration of instruments that enable custody","value": "custody","option_mapping_ref": "VASPA.SERVICES.OFFERED.CUSTODY"},
                {"label": "Participation in financial services related to an issuer’s offer or sale of cryptocurrency","value": "issuer_related_services","option_mapping_ref": "VASPA.SERVICES.OFFERED.ISSUER_FIN_SERVICES"},
                {"label": "Funds deposit or withdrawal via ATM","value": "atm","option_mapping_ref": "VASPA.SERVICES.OFFERED.ATM"}
             ]},
            {"type": "text","label": "Other services (if so, please describe)","mapping_ref": "VASPA.SERVICES.OTHER_DESC","placeholder": "Describe other services if any"},
            {"type": "select","label": "Do you offer cross border payments?","mapping_ref": "VASPA.SERVICES.CROSS_BORDER","required": True,
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SERVICES.CROSS_BORDER.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SERVICES.CROSS_BORDER.NO"}
             ]},
            {"type": "textarea","label": "Please describe your customer base (geographic regions, customer types, industry sectors)","mapping_ref": "VASPA.CUSTOMER.BASE_DESC"},
            {"type": "textarea","label": "Which cryptocurrencies do you deal with?","mapping_ref": "VASPA.CRYPTO.CURRENCIES"},
            {"type": "select","label": "Do you deal with any anonymous cryptocurrencies?","mapping_ref": "VASPA.CRYPTO.ANONYMOUS",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.CRYPTO.ANONYMOUS.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.CRYPTO.ANONYMOUS.NO"}
             ]},
            {"type": "textarea","label": "If yes, what measures are in place to mitigate risks associated with anonymous cryptocurrencies?","mapping_ref": "VASPA.CRYPTO.ANON_CONTROLS"},
            {"type": "textarea","label": "What is the crypto purchase/sale model and process? (brokerage, exchange, peer-to-peer, etc.)","mapping_ref": "VASPA.CRYPTO.MODEL_PROCESS"},
            {"type": "select","label": "Do you accept funds from or for Gambling sites?","mapping_ref": "VASPA.SERVICES.GAMBLING_FUNDS",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SERVICES.GAMBLING_FUNDS.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SERVICES.GAMBLING_FUNDS.NO"}
             ]},
            {"type": "textarea","label": "If yes (gambling), please provide controls to mitigate the associated risks.","mapping_ref": "VASPA.SERVICES.GAMBLING_CONTROLS"}
        ]
    },
    {
        "slug": "wallets",
        "title": "Wallet Services",
        "fields": [
            {"type": "multicheck","label": "What type of wallets do you offer?","mapping_ref": "VASPA.WALLET.TYPES",
             "options": [
                {"label": "Hosted / Custodial wallets","value": "hosted","option_mapping_ref": "VASPA.WALLET.TYPES.HOSTED"},
                {"label": "Self-hosted / Non-custodial wallets","value": "self_hosted","option_mapping_ref": "VASPA.WALLET.TYPES.SELF_HOSTED"}
             ]},
            {"type": "textarea","label": "If offering both hosted/custodial and self-hosted/non-custodial wallets, describe how you differentiate and manage risks.","mapping_ref": "VASPA.WALLET.BOTH_RISK_MGMT"},
            {"type": "textarea","label": "How do you assess wallet risk?","mapping_ref": "VASPA.WALLET.RISK_ASSESSMENT"},
            {"type": "select","label": "Do you use Blockchain analytics tools to assess wallet risk?","mapping_ref": "VASPA.WALLET.BLOCKCHAIN_ANALYTICS",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.WALLET.BLOCKCHAIN_ANALYTICS.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.WALLET.BLOCKCHAIN_ANALYTICS.NO"}
             ]},
            {"type": "select","label": "Can you top up a wallet with a high-risk payment type (fiat cards, third-party payments)?","mapping_ref": "VASPA.WALLET.TOPUP_HIGH_RISK",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.WALLET.TOPUP_HIGH_RISK.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.WALLET.TOPUP_HIGH_RISK.NO"}
             ]},
            {"type": "select","label": "Are you engaged in ICO of cryptos (Initial Coin Offering)?","mapping_ref": "VASPA.ICO.ENGAGED",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.ICO.ENGAGED.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.ICO.ENGAGED.NO"}
             ]},
            {"type": "textarea","label": "If Yes (ICO), describe your controls around this risk.","mapping_ref": "VASPA.ICO.CONTROLS"},
            {"type": "select","label": "Can customers make payouts to accounts other than those in their own name?","mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_ALLOWED",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_ALLOWED.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_ALLOWED.NO"}
             ]},
            {"type": "textarea","label": "If yes, explain why this functionality is allowed.","mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_JUSTIFICATION"},
            {"type": "select","label": "Can customers make payouts to different accounts under their own name that are not the original funding account?","mapping_ref": "VASPA.PAYOUTS.ALTERNATE_OWN_ACCTS",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.PAYOUTS.ALTERNATE_OWN_ACCTS.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.PAYOUTS.ALTERNATE_OWN_ACCTS.NO"}
             ]},
            {"type": "textarea","label": "If yes, what controls ensure that the alternative account belongs to the same account holder?","mapping_ref": "VASPA.PAYOUTS.ALTERNATE_OWN_ACCTS_CONTROLS"},
            {"type": "multicheck","label": "Controls to mitigate risks associated with third-party payouts","mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_CONTROLS",
             "options": [
                {"label": "Automated name matching","value": "auto_name_match","option_mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_CONTROLS.AUTO_NAME_MATCH"},
                {"label": "Manual review","value": "manual_review","option_mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_CONTROLS.MANUAL_REVIEW"},
                {"label": "Transaction limits","value": "txn_limits","option_mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_CONTROLS.TXN_LIMITS"},
                {"label": "Documentation verification (proof of account ownership)","value": "doc_verify","option_mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_CONTROLS.DOC_VERIFY"},
                {"label": "Other (please specify)","value": "other","option_mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_CONTROLS.OTHER"}
             ]},
            {"type": "text","label": "If 'Other', please specify","mapping_ref": "VASPA.PAYOUTS.THIRD_PARTY_CONTROLS.OTHER_DESC"},
            {"type": "select","label": "Do you allow payouts to e-wallets or prepaid cards?","mapping_ref": "VASPA.PAYOUTS.EWALLET_PREPAID",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.PAYOUTS.EWALLET_PREPAID.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.PAYOUTS.EWALLET_PREPAID.NO"}
             ]},
            {"type": "textarea","label": "If yes, what additional controls are in place?","mapping_ref": "VASPA.PAYOUTS.EWALLET_PREPAID_CONTROLS"}
        ]
    },
    {
        "slug": "licensing_legal",
        "title": "Licensing & Legal Compliance",
        "fields": [
            {"type": "list","label": "List all jurisdictions where you are licensed to operate and provide services","mapping_ref": "VASPA.LICENSING.JURISDICTIONS","placeholder": "Add jurisdiction (e.g., Cyprus – VASP license 1234)"},
            {"type": "select","label": "Does your license allow services to users from your targeted countries?","mapping_ref": "VASPA.LICENSING.TARGETED_ALLOWED",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.LICENSING.TARGETED_ALLOWED.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.LICENSING.TARGETED_ALLOWED.NO"}
             ]},
            {"type": "file","label": "If yes, upload legal opinion confirming ability to conduct VASP services in other jurisdictions","mapping_ref": "VASPA.LICENSING.LEGAL_OPINION_FILE","multiple": False},
            {"type": "textarea","label": "How do you ensure compliance with local laws and regulations in each jurisdiction?","mapping_ref": "VASPA.LICENSING.LOCAL_COMPLIANCE_METHODS"},
            {"type": "select","label": "Do you have a dedicated legal/compliance team for multi-jurisdiction requirements?","mapping_ref": "VASPA.LICENSING.DEDICATED_TEAM",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.LICENSING.DEDICATED_TEAM.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.LICENSING.DEDICATED_TEAM.NO"}
             ]},
            {"type": "textarea","label": "If yes, provide details on team structure and responsibilities","mapping_ref": "VASPA.LICENSING.DEDICATED_TEAM_DETAILS"}
        ]
    },
    {
        "slug": "monitoring_screening",
        "title": "Monitoring & Screening",
        "fields": [
            {"type": "textarea","label": "What is your transaction monitoring process?","mapping_ref": "VASPA.MON.TM_PROCESS"},
            {"type": "text","label": "Do you use a transaction monitoring tool? If so, who is the provider?","mapping_ref": "VASPA.MON.TM_PROVIDER"},
            {"type": "select","label": "Do you operate automated, manual, or hybrid transaction monitoring?","mapping_ref": "VASPA.MON.TM_MODE",
             "options": [
                {"label": "Automated","value": "automated","option_mapping_ref": "VASPA.MON.TM_MODE.AUTOMATED"},
                {"label": "Manual","value": "manual","option_mapping_ref": "VASPA.MON.TM_MODE.MANUAL"},
                {"label": "Hybrid","value": "hybrid","option_mapping_ref": "VASPA.MON.TM_MODE.HYBRID"}
             ]},
            {"type": "textarea","label": "How do you monitor customer IP addresses?","mapping_ref": "VASPA.MON.IP_METHOD"},
            {"type": "select","label": "Do you monitor device IDs?","mapping_ref": "VASPA.MON.DEVICE_ID",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.MON.DEVICE_ID.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.MON.DEVICE_ID.NO"}
             ]},
            {"type": "select","label": "Do you monitor non-residential activity (address vs. account location differ)?","mapping_ref": "VASPA.MON.NON_RESIDENTIAL",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.MON.NON_RESIDENTIAL.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.MON.NON_RESIDENTIAL.NO"}
             ]},
            {"type": "textarea","label": "What kind of Transaction Monitoring controls do you have in place? Please describe.","mapping_ref": "VASPA.MON.TM_CONTROLS_DESC"},
            {"type": "select","label": "Transactions Screening (Sanctions) - real time","mapping_ref": "VASPA.SCREEN.SANCTIONS_TXN_REALTIME",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SCREEN.SANCTIONS_TXN_REALTIME.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SCREEN.SANCTIONS_TXN_REALTIME.NO"}
             ]},
            {"type": "select","label": "Sanctions Name Screening during onboarding","mapping_ref": "VASPA.SCREEN.SANCTIONS_ONBOARDING",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SCREEN.SANCTIONS_ONBOARDING.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SCREEN.SANCTIONS_ONBOARDING.NO"}
             ]},
            {"type": "select","label": "Sanctions Name Screening ongoing","mapping_ref": "VASPA.SCREEN.SANCTIONS_ONGOING",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SCREEN.SANCTIONS_ONGOING.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SCREEN.SANCTIONS_ONGOING.NO"}
             ]},
            {"type": "select","label": "PEP Name Screening during onboarding","mapping_ref": "VASPA.SCREEN.PEP_ONBOARDING",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SCREEN.PEP_ONBOARDING.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SCREEN.PEP_ONBOARDING.NO"}
             ]},
            {"type": "select","label": "PEP Name Screening ongoing","mapping_ref": "VASPA.SCREEN.PEP_ONGOING",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SCREEN.PEP_ONGOING.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SCREEN.PEP_ONGOING.NO"}
             ]},
            {"type": "select","label": "Adverse Media Screening during onboarding","mapping_ref": "VASPA.SCREEN.AM_ONBOARDING",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SCREEN.AM_ONBOARDING.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SCREEN.AM_ONBOARDING.NO"}
             ]},
            {"type": "select","label": "Adverse Media Screening ongoing","mapping_ref": "VASPA.SCREEN.AM_ONGOING",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.SCREEN.AM_ONGOING.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.SCREEN.AM_ONGOING.NO"}
             ]},
            {"type": "textarea","label": "Controls to detect mixers / tumblers","mapping_ref": "VASPA.MON.MIXER_TUMBLER_CONTROLS"}
        ]
    },
    {
        "slug": "sanctions",
        "title": "Sanctions",
        "fields": [
            {"type": "textarea","label": "What sanctions regimes do you follow?","mapping_ref": "VASPA.SANCTIONS.REGIMES"},
            {"type": "textarea","label": "What controls do you have to address sanctions risk?","mapping_ref": "VASPA.SANCTIONS.CONTROLS"}
        ]
    },
    {
        "slug": "kyc_kyb",
        "title": "KYC / KYB",
        "fields": [
            {"type": "textarea","label": "Describe your onboarding and KYC/KYB process (Initial, EDD, Ongoing).","mapping_ref": "VASPA.KYC.PROCESS_DESC"},
            {"type": "select","label": "Do you perform full ID&V for Authorized Signatories and UBO (incl. digital ID verification)?","mapping_ref": "VASPA.KYC.FULL_IDV_AS_UBO",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.KYC.FULL_IDV_AS_UBO.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.KYC.FULL_IDV_AS_UBO.NO"}
             ]},
            {"type": "select","label": "Do you gather information on Source of Funds, Source of Wealth, or Source of Crypto?","mapping_ref": "VASPA.KYC.SOF_SOW_SOC",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.KYC.SOF_SOW_SOC.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.KYC.SOF_SOW_SOC.NO"}
             ]},
            {"type": "textarea","label": "Customer Risk Assessment process – factors and methodology","mapping_ref": "VASPA.KYC.CRA_PROCESS"},
            {"type": "textarea","label": "List of prohibited and high-risk business activities","mapping_ref": "VASPA.KYC.PROHIBITED_ACTIVITIES"}
        ]
    },
    {
        "slug": "governance_reporting",
        "title": "Governance & Reporting",
        "fields": [
            {"type": "textarea","label": "Filing process to the required local regulator (SAR, Sanctions, Fraud)","mapping_ref": "VASPA.GOV.FILING_PROCESS"},
            {"type": "textarea","label": "When are onboarding/monitoring decisions escalated for approval?","mapping_ref": "VASPA.GOV.ESCALATION_CRITERIA"},
            {"type": "textarea","label": "Company progress in addressing MiCA / Travel Rule regulations","mapping_ref": "VASPA.GOV.MICA_TRAVEL_PROGRESS"},
            {"type": "textarea","label": "Customer exit process and triggers","mapping_ref": "VASPA.GOV.CUSTOMER_EXIT"},
            {"type": "number","label": "How many customers do you currently have?","mapping_ref": "VASPA.GOV.CUSTOMER_COUNT","min": 0},
            {"type": "textarea","label": "Risk rating distribution between customers (%)","mapping_ref": "VASPA.GOV.RISK_DISTRIBUTION"},
            {"type": "textarea","label": "Size, structure, and setup of your Compliance / AML department","mapping_ref": "VASPA.GOV.AML_DEPT"},
            {"type": "select","label": "Process in place to comply with Payment Transparency?","mapping_ref": "VASPA.GOV.PAYMENT_TRANSPARENCY_PROCESS",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.GOV.PAYMENT_TRANSPARENCY_PROCESS.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.GOV.PAYMENT_TRANSPARENCY_PROCESS.NO"}
             ]},
            {"type": "multicheck","label": "Standards compliance","mapping_ref": "VASPA.GOV.STANDARDS",
             "options": [
                {"label": "Wolfsberg Group Payment Transparency Standards","value": "wolfsberg","option_mapping_ref": "VASPA.GOV.STANDARDS.WOLFSBERG"},
                {"label": "FATF Recommendation 16","value": "fatf16","option_mapping_ref": "VASPA.GOV.STANDARDS.FATF16"},
                {"label": "FinCEN Travel Rule","value": "fincen_travel","option_mapping_ref": "VASPA.GOV.STANDARDS.FINCEN_TRAVEL"},
                {"label": "European Wire Transfer Regulations","value": "eu_wire","option_mapping_ref": "VASPA.GOV.STANDARDS.EU_WIRE"},
                {"label": "Local Payment Transparency Regulations","value": "local_payment_transparency","option_mapping_ref": "VASPA.GOV.STANDARDS.LOCAL_PAYMENT_TRANSPARENCY"}
             ]},
            {"type": "file","label": "UK entities: Upload FCA P11 Notification covering Crypto-asset promotion rules","mapping_ref": "VASPA.GOV.FCA_P11_FILE","multiple": False},
            {"type": "textarea","label": "Non-UK entities: Describe your approach to UK FCA Financial Promotion Regulations","mapping_ref": "VASPA.GOV.FCA_NON_UK_APPROACH"},
            {"type": "select","label": "Do you have a legitimate third-party approver for financial promotions?","mapping_ref": "VASPA.GOV.FCA_TP_APPROVER",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.GOV.FCA_TP_APPROVER.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.GOV.FCA_TP_APPROVER.NO"}
             ]},
            {"type": "textarea","label": "If yes, provide details on the third-party approver","mapping_ref": "VASPA.GOV.FCA_TP_APPROVER_DETAILS"}
        ]
    },
    {
        "slug": "fraud",
        "title": "Fraud Controls & Metrics",
        "fields": [
            {"type": "textarea","label": "Parts of the business vulnerable to fraudsters (products, services, channels)","mapping_ref": "VASPA.FRAUD.VULNERABLE_PARTS"},
            {"type": "textarea","label": "Is fraud included in your business-wide risk assessment? Areas of high residual risk?","mapping_ref": "VASPA.FRAUD.BWRA"},
            {"type": "textarea","label": "Assigned risk owner for fraud; team responsible for monitoring","mapping_ref": "VASPA.FRAUD.OWNER_TEAM"},
            {"type": "textarea","label": "Management information collected (refunds, losses, chargebacks, etc.)","mapping_ref": "VASPA.FRAUD.MI"},
            {"type": "textarea","label": "Onboarding controls to mitigate fraud risks (incl. impersonation)","mapping_ref": "VASPA.FRAUD.ONBOARD_CONTROLS"},
            {"type": "textarea","label": "Fraud screening controls in place","mapping_ref": "VASPA.FRAUD.SCREEN_CONTROLS"},
            {"type": "textarea","label": "Activity-based rules (access attempts, IP/device monitoring, etc.)","mapping_ref": "VASPA.FRAUD.ACTIVITY_RULES"},
            {"type": "textarea","label": "Controls to identify both victims and perpetrators of fraud","mapping_ref": "VASPA.FRAUD.VICTIMS_PERPS_CONTROLS"},
            {"type": "select","label": "Does new-joiner and annual refresher training include fraud?","mapping_ref": "VASPA.FRAUD.TRAINING_INCLUDED",
             "options": [
                {"label": "Yes","value": "yes","option_mapping_ref": "VASPA.FRAUD.TRAINING_INCLUDED.YES"},
                {"label": "No","value": "no","option_mapping_ref": "VASPA.FRAUD.TRAINING_INCLUDED.NO"}
             ]},
            {"type": "textarea","label": "Enhanced controls to monitor wallets with known/suspected fraud","mapping_ref": "VASPA.FRAUD.ENHANCED_WALLET_MONITORING"},
            {"type": "textarea","label": "Controls to prevent exited fraudulent individuals from re-onboarding","mapping_ref": "VASPA.FRAUD.REENTRY_CONTROLS"},
            {"type": "textarea","label": "Most common fraud types (last 6 months) – summary","mapping_ref": "VASPA.FRAUD.COMMON_TYPES"},
            {"type": "textarea","label": "Mitigation actions taken (e.g., enhanced monitoring, stricter KYC, system changes)","mapping_ref": "VASPA.FRAUD.MITIGATION_ACTIONS"},
            {"type": "table","label": "Fraud Incidents (last 6 months)","mapping_ref": "VASPA.FRAUD.MONTHLY_TABLE",
             "columns": [
                {"key": "month_label","label": "Month (e.g., 2025-07)"},
                {"key": "confirmed_incidents","label": "Number of Confirmed Fraud Incidents"},
                {"key": "fraud_volume_pct","label": "Fraud Volume % of all Transactions"},
                {"key": "fraud_amount_eur","label": "Fraud Amount (EUR)"},
                {"key": "fraud_losses_eur","label": "Fraud Losses (EUR)"},
                {"key": "chargeback_rate_pct","label": "Chargeback Rate (%)"},
                {"key": "detection_rate_pct","label": "Fraud Detection Rate (%)"}
             ],
             "rows": 6}
        ]
    },
    {
        "slug": "documents_submit",
        "title": "Documents & Submission",
        "fields": [
            {"type": "file","label": "Upload AML Policy (5AMLD-aligned)","mapping_ref": "VASPA.DOCS.AML_POLICY","multiple": False},
            {"type": "file","label": "Upload Fraud Policy","mapping_ref": "VASPA.DOCS.FRAUD_POLICY","multiple": False},
            {"type": "file","label": "Example KYC Pack (2–3 customers)","mapping_ref": "VASPA.DOCS.KYC_PACK","multiple": True},
            {"type": "file","label": "CV of MLRO (upload)","mapping_ref": "VASPA.DOCS.MLRO_CV","multiple": False},
            {"type": "file","label": "AML Audit Report (upload)","mapping_ref": "VASPA.DOCS.AML_AUDIT_REPORT","multiple": False},
            {"type": "date","label": "Date","mapping_ref": "VASPA.SUBMISSION.DATE"},
            {"type": "text","label": "Completed by (Name & Surname)","mapping_ref": "VASPA.SUBMISSION.COMPLETED_BY"},
            {"type": "text","label": "Position","mapping_ref": "VASPA.SUBMISSION.POSITION"}
        ]
    }
]

SECTION_SLUGS = [s["slug"] for s in SECTIONS]
