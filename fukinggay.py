import os 
import subprocess
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="𝐋𝐈𝐎𝐍 𝐔𝐁 %(asctime)s ✘ - ⫸ %(name)s ⫷ - ⛝ %(levelname)s ⛝ - ║ %(message)s ║", level=INFO)
LOGS = getLogger("Helper")
os.system("git clone https://github.com/Mdnoor786/Lion lion")
os.chdir("lion")
process = subprocess.Popen(
        ["python3", "-m", "Lion"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    LOGS.warning(er.decode())
print("::::::::::::::")
if out:
    LOGS.info(out.decode())
