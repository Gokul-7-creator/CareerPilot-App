import requests


def validate_company(company):

    company = company.strip()

    if not company:
        return False

    try:

        response = requests.get(
            f"https://autocomplete.clearbit.com/v1/companies/suggest?query={company}",
            timeout=5
        )

        if response.status_code != 200:
            return False

        data = response.json()

        return len(data) > 0

    except Exception:

        return False