import questionary

from lib import keymgmt

# Style
style = questionary.Style([])


# If search has any results
def validKey(text):
    if len(keymgmt.listKeys(keymgmt.ctx, text)) == 0:
        return "No search results"
    else:
        return True


def askKeys(multipule: bool = False, question: str = "Select a key:"):
    # Search
    query = questionary.text("Search Keys |", qmark="", validate=validKey).ask()
    searchResult = keymgmt.listKeys(keymgmt.ctx, query)

    # Single Result
    if len(searchResult) == 1:
        return searchResult[0]

    # Mutliple Results
    for i in range(len(searchResult)):
        print(keymgmt.getFingerprint(searchResult[i], 0))
