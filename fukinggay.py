import os 
import subprocess
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="𝐋𝐈𝐎𝐍 𝐔𝐁 %(asctime)s ✘ - ⫸ %(name)s ⫷ - ⛝ %(levelname)s ⛝ - ║ %(message)s ║", level=INFO)
LOGS = getLogger("Helper")
os.system("git clone https://github.com/Mdnoor786/Lion-X lion-x")
os.chdir("lion-x")
process = subprocess.Popen(
        ["python3", "-m", "Lion"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    LOGS.warning(er.decode())
print("𝙶𝙾𝚃 𝙰𝙽 𝙴𝚁𝚁𝙾𝚁 𝚁𝙴𝙿𝙾𝚁𝚃 𝙸𝚃 𝚃𝙾 𝙾𝚄𝚁 𝙰𝙳𝙼𝙸𝙽𝚂")
if out:
    LOGS.info(out.decode())
