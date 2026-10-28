import os, re
IS_WINDOWS = os.name == "nt"
COMMANDS = [
{"id":"mkdir","title":"Create a folder","keywords":["folder banao","naya folder","directory banao","create folder","make a folder","new folder"],"examples":["folder banao","make a new folder"],"linux":"mkdir <folder_name>","windows":"mkdir <folder_name>","windows_argv":None,"explanation":"Creates a directory using the name chosen by the user. The tool asks for a name before showing the final command.","risk":"low","aliases":["mkdir notes"],"runnable":True},
{"id":"list","title":"List files including hidden files","keywords":["files dikhao","saari files","show files","list files","hidden files"],"examples":["files dikhao","show hidden files"],"linux":"ls -la","windows":"Get-ChildItem -Force","windows_argv":["cmd","/c","dir","/a"] if IS_WINDOWS else None,"explanation":"Lists files and directories, including hidden entries.","risk":"low","aliases":["ls -la","get-childitem -force","dir /a"],"runnable":True},
{"id":"pwd","title":"Show current directory","keywords":["current location","where am i","current directory","meri location","path batao","present working directory"],"examples":["current location batao","where am I"],"linux":"pwd","windows":"Get-Location","windows_argv":["cmd","/c","cd"] if IS_WINDOWS else None,"explanation":"Prints the current working directory path.","risk":"low","aliases":["pwd","get-location","cd"],"runnable":True},
{"id":"git-status","title":"Check Git changes","keywords":["git status","git changes","changes check","git ki status","working tree"],"examples":["git status check karo","show git changes"],"linux":"git status","windows":"git status","windows_argv":["git","status"],"explanation":"Shows changed, staged, and untracked files in the repository.","risk":"low","aliases":["git status"],"runnable":True},
{"id":"git-log","title":"Show five latest commits","keywords":["last commits","recent commits","last 5 commits","git history","commit history"],"examples":["last 5 commits","show recent commits"],"linux":"git log -5 --oneline","windows":"git log -5 --oneline","windows_argv":["git","log","-5","--oneline"],"explanation":"Displays five recent commits in compact format.","risk":"low","aliases":["git log -5 --oneline"],"runnable":True},
{"id":"git-branch","title":"Show current branch","keywords":["current branch","branch name","git branch","meri branch","which branch"],"examples":["show current branch","meri branch batao"],"linux":"git branch --show-current","windows":"git branch --show-current","windows_argv":["git","branch","--show-current"],"explanation":"Prints the current branch name.","risk":"low","aliases":["git branch --show-current"],"runnable":True},
{"id":"find-txt","title":"Find text files","keywords":["find txt","search txt","text files","find files","txt files"],"examples":["find txt files","search for text files"],"linux":"find . -type f -name '*.txt'","windows":"Get-ChildItem -Recurse -File -Filter *.txt","windows_argv":["cmd","/c","where","/r",".","*.txt"] if IS_WINDOWS else None,"explanation":"Searches the current directory tree for .txt files.","risk":"low","aliases":["find . -type f -name '*.txt'"],"runnable":True},
{"id":"disk","title":"Show disk space","keywords":["disk space","storage space","disk usage","kitni space","free space"],"examples":["show disk space","disk usage"],"linux":"df -h","windows":"Get-PSDrive -PSProvider FileSystem","windows_argv":None,"explanation":"Shows disk capacity/available space; Windows uses a different command.","risk":"low","aliases":["df -h"],"runnable":False},
{"id":"largest","title":"Find largest files","keywords":["biggest files","largest files","large files","badi files","files size"],"examples":["show biggest files","find largest files"],"linux":"du -ah . | sort -rh | head -10","windows":"Get-ChildItem -File -Recurse | Sort-Object Length -Descending | Select-Object -First 10 Name,Length","windows_argv":None,"explanation":"Finds large files; recursive scans may be slow.","risk":"medium","aliases":[],"runnable":False},
{"id":"git-diff","title":"Summarize unstaged changes","keywords":["git diff","diff summary","changed lines","code changes summary"],"examples":["summarize code changes","git diff summary"],"linux":"git diff --stat","windows":"git diff --stat","windows_argv":["git","diff","--stat"],"explanation":"Summarizes unstaged changes without printing the full diff.","risk":"low","aliases":["git diff --stat"],"runnable":True}
]
BUNDLES = {
"git-summary":{"title":"Git project summary","commands":[
{"title":"Working tree status","command":["git","status","--short","--branch"],"tip":"Run this inside a Git repository."},
{"title":"Current branch","command":["git","branch","--show-current"]},
{"title":"Latest five commits","command":["git","log","-5","--oneline"]},
{"title":"Unstaged change summary","command":["git","diff","--stat"]}]},
"system-summary":{"title":"System and developer tools summary","commands":[
{"title":"Python version","command":["python","--version"]},
{"title":"Git version","command":["git","--version"],"tip":"Install Git for Windows if missing."}]}
}
def normalize(text):
    text=text.lower().strip()
    text=re.sub(r"[^\w\s./*'-]"," ",text)
    return " ".join(text.split())
def match_request(request):
    target=normalize(request); best=None; best_score=0
    for item in COMMANDS:
        score=0
        for phrase in item["keywords"]+item["examples"]:
            p=normalize(phrase)
            if p and p in target:
                score=max(score,len(p.split())*10+len(p))
        if score>best_score: best,best_score=item,score
    return best
def find_command(command_text):
    target=normalize(command_text)
    for item in COMMANDS:
        if any(target==normalize(c) for c in [item["linux"],item["windows"]]+item["aliases"]):
            return item
    return None
