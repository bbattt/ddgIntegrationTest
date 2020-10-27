import pytest
import requests

url = "https://api.duckduckgo.com"


def test_ddg_presidents():
    response = requests.get(url + "/?q=presidents+of+the+united+states&format=json")

    response_json = response.json()

    known_presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson",
                        "Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce",
                        "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur",
                        "Cleveland", "Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson",
                        "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy",
                        "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump"]
    known_presidents = set(known_presidents)
    found_presidents = []

    for r in response_json["RelatedTopics"]:
        # found_presidents.append(r["Text"])

        end_of_title = r["Text"].find(" -")
        found_presidents.append(r["Text"][:end_of_title])

    for found_index in range(len(found_presidents)):
        for known in known_presidents:
            if found_presidents[found_index].find(known) != -1:
                known_presidents.remove(known)
                found_presidents[found_index] = ""
                break

    # print(*known_presidents, sep = "\n")
    # print(*found_presidents, sep = "\n")

    assert len(known_presidents) == 0
