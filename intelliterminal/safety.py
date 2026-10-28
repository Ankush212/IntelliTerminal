import re

PATTERNS = [
    (r"\brm\s+-rf\b", "recursive permanent deletion"),
    (r"\bgit\s+reset\s+--hard\b", "discarding Git changes"),
    (r"\bgit\s+clean\s+-[a-z]*f", "deleting untracked files"),
    (r"\bsudo\b", "elevated privileges"),
    (r"\bformat\b", "disk formatting"),
    (r"\bchmod\s+-R\b", "recursive permission changes"),
    (r"\bcurl\b.*\|\s*(sh|bash)", "running a remote script"),
    (r"\bshutdown\b", "system shutdown"),
]


def classify_risk(command):
    for pattern, reason in PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return "HIGH — " + reason
    return "LOW — no known destructive pattern detected; not a guarantee of safety"


def is_allowed_to_run(item):
    return bool(item and item.get("runnable") and item.get("risk") == "low")


def folder_name_error(name):
    """Return an error message if a folder name is unsafe/invalid on Windows."""
    if not name or not name.strip():
        return "Folder name cannot be empty."
    if name in {".", ".."}:
        return "Please enter a normal folder name, not '.' or '..'."
    if any(ord(char) < 32 for char in name):
        return "Folder name cannot contain control characters."
    if any(char in '<>:"/\\|?*' for char in name):
        return 'Avoid these characters in a Windows folder name: < > : " / \\ | ? *'
    if name.endswith((" ", ".")):
        return "A Windows folder name cannot end with a space or dot."
    reserved = {"CON", "PRN", "AUX", "NUL"}
    reserved.update(f"COM{i}" for i in range(1, 10))
    reserved.update(f"LPT{i}" for i in range(1, 10))
    if name.split(".", 1)[0].upper() in reserved:
        return "That name is reserved by Windows. Choose another name."
    return None
