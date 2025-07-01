# UmamusumeAutoTrainer

Uma Musume Pretty Derby (Chinese Server) Automatic Training Tool

## Features

1. Supports automatic completion of training scenarios for all Uma Musume
2. Customize training target attributes, racing tactics, additional races, and skill learning for easier three-star factor farming and improving Uma Musume inheritance compatibility \


## Usage Instructions

### Download

##### Clone Repository

```commandline
git clone https://github.com/shiokaze/UmamusumeAutoTrainer
```
##### Install Dependencies

1. Install Python 3.10.9, [Download Link](https://www.python.org/downloads/release/python-3109/)
2. Double-click to run install.ps1. If it opens in Notepad, right-click the file and select "Open with PowerShell". Ensure there is no venv folder in the current directory when starting. (If not in mainland China or don't need domestic mirrors, you can modify line 32 to `pip install --upgrade -r requirements.txt`)


### 2. Configuration

Modify the config.yaml file content

```
bot:
  auto:
    adb:
      device_name: "127.0.0.1:16384" # Change to emulator's ADB port
      delay: 0
    cpu_alloc: 4 # Number of CPUs to allocate
```
Common emulator ports:\
(Recommended) MuMu12: 127.0.0.1:16384 \
LDPlayer/BlueStacks: emulator-5554
#### BlueStacks emulator port changes each restart (Hyper-V)
Find the bluestacks.conf file in BlueStacks data directory
- International version default path: C:\ProgramData\BlueStacks_nxt\bluestacks.conf
- China mainland version default path: C:\ProgramData\BlueStacks_nxt_cn\bluestacks.conf
```
bot:
  auto:
    adb:
      device_name: "127.0.0.1:16384" # Change to emulator's ADB port
      delay: 0
      bluestacks_config_path: "C:\\ProgramData\\BlueStacks_nxt\\bluestacks.conf" # bluestacks.conf 파일 경로
      bluestacks_config_keyword: "bst.instance.Rvc64.status.adb_port" # 해당 에뮬레이터의 포트 키, Rvc64는 에뮬레이터 이름으로 다를 수 있음 (Rvc64_1, Pie64 등), bluestacks.conf 파일에서 adb_port를 검색하여 찾을 수 있음
    cpu_alloc: 4 # 할당할 CPU 개수
```

### 3. 에뮬레이터 설정

에뮬레이터 해상도를 720 * 1280, DPI 180 (세로 모드)로 설정하세요
MuMu 에뮬레이터는 백그라운드 유지 기능을 활성화할 수 없습니다


### 4. 실행

Double-click to run run.ps1

Console displays the following content indicating successful launch
```commandline
UAT running on http://127.0.0.1:8071
```

Copy to browser to access and configure tasks through WebUI to start the script

<img alt="LOGO" src="docs/1.png" width="680" height="565" />

## Important Notes

1. In-game graphics settings must be set to Standard version, not Simple version
2. If the Uma Musume training phase includes optional races or races with fan count requirements (such as Oguri Cap's 2 G1 races in the third year and Urara's fan count targets), you need to use the corresponding Uma Musume preset or configure which races to participate in through custom race schedule
3. Target attributes should match the proportion of support card types you carry. Don't bring 3 Intelligence + 3 Speed cards while setting high Stamina and Power targets
4. Currently does not support selecting training Uma Musume and stallion. At launch, it will use the last trained Uma Musume and stallion saved in the game. If there's no saved record, manually select them first before launching
5. Friend cards are not recommended because there's currently no specific strategy for friend card outings, making them less effective than other support card types
6. When launching the script, you should be in the main menu or any training interface

### If Exceptions Occur

1. If emulator connection fails or "connection reset" errors occur, close running accelerators (such as UU Accelerator) and use Task Manager to close adb.exe, then restart both the emulator and script program
2. If recognition errors cause program crashes, entering unexpected interfaces, or getting stuck on an interface, manually operate to enter the next turn and reset the task in WebUI before restarting. You can save screenshots of stuck interfaces and attach error logs when submitting issues.


## FAQ

#### 1. install.ps1 or run.ps1 crashes on execution
Open console first then run PowerShell script, so you can see the error reason when it occurs.
#### 2. System prohibits running PowerShell scripts
Reference: https://www.jianshu.com/p/4eaad2163567
#### 3. Script reports error on startup
Check if user folder name contains Chinese characters\
Reference: https://github.com/shiokaze/UmamusumeAutoTrainer/issues/18 \
https://github.com/shiokaze/UmamusumeAutoTrainer/issues/24
#### 4. Launch successful but WebUI won't open, with browser console errors
If error message is: Failed to load module script: Expected a JavaScript module script but the server responded with a MIME type of "text/plain". Strict MIME type checking is enforced for module scripts per HTML spec. \
Reference: https://github.com/shiokaze/UmamusumeAutoTrainer/issues/9
https://github.com/shiokaze/UmamusumeAutoTrainer/issues/25


### TODO

- [ ] Scheduled task execution
- [ ] AI logic optimization during training
- [ ] Event configuration options support
- [ ] Auto-complete daily coins/support points/JJC


### Contributing to Development

If you think the current code has shortcomings, feel free to submit PRs

