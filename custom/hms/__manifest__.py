{
    "name": "HMS",
    "version": "1.0",
    "summary": "Hospital Management System",
    "category": "Healthcare",
    "author": "Your Name",
    "depends": ["base", "mail"],
    "description": """
        Hospital management system module.
    """,
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/doctor_views.xml",
        "views/department_views.xml",
        "views/patient_status_report.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
