import unittest

from src.triage import classify_ticket, summarize_queue


class TriageTests(unittest.TestCase):
    def test_security_incident_is_critical(self):
        result = classify_ticket("Suspeita de phishing e acesso indevido")
        self.assertEqual(result["priority"], "P1")
        self.assertEqual(result["category"], "security")

    def test_password_request_is_low_priority(self):
        result = classify_ticket("Preciso redefinir minha senha")
        self.assertEqual(result["priority"], "P3")
        self.assertEqual(result["category"], "access")

    def test_queue_summary_counts_priorities(self):
        tickets = [
            classify_ticket("sistema fora do ar"),
            classify_ticket("erro no pagamento"),
            classify_ticket("dúvida sobre senha"),
        ]
        self.assertEqual(summarize_queue(tickets), {"P1": 1, "P2": 1, "P3": 1})


if __name__ == "__main__":
    unittest.main()
