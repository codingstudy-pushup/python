from typing import List


class Solution:
    def uniqueEmails(self, emails: List[str]) -> int:
        strSet = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            strSet.add(local + '@' + domain)
        return len(strSet)


if __name__ == "__main__":
    print(Solution().uniqueEmails([
        "test.email+james@coding.com",
        "test.e.mail+toto.jane@cod.ing.com",
        "testemail+tom@cod.ing.com"]))
