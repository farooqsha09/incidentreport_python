class IncidentReport:
    def __init__(self, report_id, description, status="Submitted"):
        self.report_id = report_id
        self.description = description
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Report ID: {self.report_id}, Description: {self.description}, Status: {self.status}"
    def __repr__(self):
            return f"IncidentReport(report_id={self.report_id},title={self.title},description={self.description},status={self.status})"

class IncidentReportManager:
    def __init__(self):
        self.reports = {}

    def submit_incident_report(self, report_id, description):
        if report_id in self.reports:
            raise ValueError("Report ID already exists.")
        report = IncidentReport(report_id, description)
        self.reports[report_id] = report

    def review_submitted_reports(self):
        return [str(report) for report in self.reports.values()]

    def update_report(self, report_id, new_description=None, new_status=None):
        if report_id not in self.reports:
            raise ValueError("Report ID not found.")
        report = self.reports[report_id]
        if new_description:
            report.description = new_description
        if new_status:
            report.update_status(new_status)

    def delete_report(self, report_id):
        if report_id not in self.reports:
            raise ValueError("Report ID not found.")
        del self.reports[report_id]
    



import unittest

class TestIncidentReporting(unittest.TestCase):
    def setUp(self):
        self.manager = IncidentReportManager()

    def test_submit_incident_report(self):
        self.manager.submit_incident_report(1, "Test incident")
        self.assertEqual(len(self.manager.reports), 1)
        self.assertEqual(self.manager.reports[1].description, "Test incident")

    def test_review_submitted_reports(self):
        self.manager.submit_incident_report(1, "Test incident")
        self.manager.submit_incident_report(2, "Another incident")
        reports = self.manager.review_submitted_reports()
        self.assertEqual(len(reports), 2)

    def test_update_report(self):
        self.manager.submit_incident_report(1, "Test incident")
        self.manager.update_report(1, new_description="Updated incident", new_status="Reviewed")
        report = self.manager.reports[1]
        self.assertEqual(report.description, "Updated incident")
        self.assertEqual(report.status, "Reviewed")

    def test_delete_report(self):
        self.manager.submit_incident_report(1, "Test incident")
        self.manager.delete_report(1)
        self.assertEqual(len(self.manager.reports), 0)

    def test_delete_non_existent_report(self):
        with self.assertRaises(ValueError):
            self.manager.delete_report(999)

if __name__ == "__main__":
    unittest.main()
