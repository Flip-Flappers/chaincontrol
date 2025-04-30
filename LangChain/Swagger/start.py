import subprocess
import sys

python_executable = sys.executable  # 获取当前 Python 解释器

files = ["selectbyreturn_0.py", "selectbyreturn_1.py", "return2api_2.py",
         "selecttagbyapiname_3.py", "selectbyapiname_4.py", "gettargetAPI_5.py",
         "searchJsonKeys_6.py"]

for file in files:
    result = subprocess.run([python_executable, file], stdout=subprocess.DEVNULL, text=True)
    print(f"{file} 结束")
    if result.returncode != 0:
        print(f"{file} 执行失败，退出码: {result.returncode}")
