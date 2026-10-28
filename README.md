# IntelliTerminal — Intelligent Terminal Assistant

**Subject:** Linux, Git & Developer Workflow | **Language:** Python 3.10+ | **Platform:** Windows 10/11

IntelliTerminal is an independent educational project inspired by the concepts in the Shelldon README shared for this assignment. It suggests commands from plain-English/Hinglish requests, explains known commands, combines related developer checks, and includes a safety-first allowlist.

## Features
- Offline keyword-based natural-language suggestions.
- Linux/macOS command and Windows equivalent.
- Command explanations.
- `git-summary`: combines Git status, current branch, five recent commits and diff statistics.
- `system-summary`: combines Python and Git version checks.
- Optional local AI fallback using Ollama (disabled by default).
- Explicit confirmation before running a supported command.
- Unit tests using Python's standard `unittest` library.
- No third-party Python dependencies for core features.

## Project structure
```text
intelliterminal_complete/
├── main.py
├── README.md
├── .gitignore
├── intelliterminal/
│   ├── __init__.py
│   ├── catalog.py
│   └── safety.py
└── tests/
    ├── __init__.py
    └── test_catalog.py
```

## Setup
1. Install Python 3.10+ and Git for Windows.
2. Extract the ZIP and open the folder in VS Code.
3. Open PowerShell in the project root and check:
```powershell
python --version
git --version
```
No `pip install` is required for core features.

## Commands
```powershell
python main.py --help
python main.py suggest "folder banao"
python main.py suggest "files dikhao"
python main.py suggest "current location batao"
python main.py suggest "git status check karo"
python main.py suggest "last 5 commits"
python main.py explain "git status"
python main.py commands
python main.py doctor
python main.py bundle git-summary
python main.py bundle system-summary
python main.py run "git status"
```

`run` accepts only exact catalog commands that are marked safe and asks the user to type `YES`. Suggested or AI-generated text is never executed. Bundles use fixed argument lists and do not accept arbitrary shell input.

## Optional local AI with Ollama
The default assistant is offline keyword matching. For more flexible requests, install Ollama separately and pull a model such as `llama3.2:3b`. Start Ollama, then in PowerShell:
```powershell
$env:INTELLITERMINAL_AI = "ollama"
$env:OLLAMA_MODEL = "llama3.2:3b"
$env:OLLAMA_URL = "http://localhost:11434"
python main.py suggest "I want to inspect my project's recent history"
```
To disable the fallback in the current PowerShell session:
```powershell
Remove-Item Env:INTELLITERMINAL_AI
```
The optional AI request goes to the local Ollama service. Model output is untrusted text and is never executed.

## Tests
```powershell
python -m unittest discover -s tests -v
```

## Safety and limitations
- No `shell=True`; subprocesses receive argument lists.
- The program does not execute AI output.
- Bundles are fixed read-only diagnostics.
- Risk checks are best-effort, not a guarantee of safety.
- Keyword matching cannot understand every phrase/language variation.
- Some Linux commands are shown for learning but have no runnable Windows mapping.
- Git-specific reports should be run inside a Git repository.

## Future improvements
Add more command mappings, better Hinglish synonyms, error explanation (`why`), local history with secret redaction, and GitHub Actions CI.

## Learning outcomes
Python modules, dictionaries, regular expressions, `argparse`, `subprocess`, Git workflow, cross-platform commands, safety policies, and unit testing.
