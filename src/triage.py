"""Deterministic ticket triage rules suitable for automation workflows."""

from __future__ import annotations


RULES = (
    ("security", ("phishing", "acesso indevido", "malware", "vazamento"), "P1"),
    ("availability", ("fora do ar", "indisponível", "indisponivel", "queda"), "P1"),
    ("payments", ("pagamento", "cobrança", "cobranca", "transação", "transacao"), "P2"),
    ("access", ("senha", "login", "permissão", "permissao"), "P3"),
)


def classify_ticket(description: str) -> dict[str, str]:
    """Classify a ticket by category, priority, and suggested queue."""
    if not description or not description.strip():
        raise ValueError("description must not be empty")
    text = description.casefold()
    for category, keywords, priority in RULES:
        if any(keyword in text for keyword in keywords):
            return {"category": category, "priority": priority, "queue": f"support-{category}"}
    return {"category": "general", "priority": "P3", "queue": "support-general"}


def summarize_queue(tickets: list[dict[str, str]]) -> dict[str, int]:
    """Count tickets by priority for an operations dashboard."""
    summary = {"P1": 0, "P2": 0, "P3": 0}
    for ticket in tickets:
        priority = ticket.get("priority")
        if priority in summary:
            summary[priority] += 1
    return summary
