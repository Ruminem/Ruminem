### VS Code extensions

**[cmake-link-explorer](https://github.com/Ruminem/cmake-link-explorer)**
For the moments a CMake project stops you over linking: what to link to use a
header, who links a given target, what is eating the binary size and the build
time, and which macros a file is really compiled with. Reads what CMake's File
API, the linker map and ninja's build log already hold rather than parsing
`CMakeLists.txt`.

**[hover-decode](https://github.com/Ruminem/hover-decode)**
For the values in code and logs that mean nothing at a glance: hover over a Windows
error code, an epoch timestamp, a duration, a hex number, a base64 string or an HTTP
status code to see what it is. Error codes come back with Windows' own message, and the
terminal gets the same rows through link tooltips. Your own terms go in a personal
dictionary that lives outside any repository, your team's in one committed with the
project.

**[native-toolbelt](https://github.com/Ruminem/native-toolbelt)**
For the native build that runs on your machine and nowhere else: it reads an `.exe` or
`.dll` and says which DLLs it needs, where Windows would find each one, and which ones
it would not find at all. Delay-loaded imports count too, and a DLL sitting next to the
binary but off the search path is named with its path. The list comes out of the PE file
itself, so no Visual Studio and no `dumpbin`.

**[terminal-toast](https://github.com/Ruminem/terminal-toast)**
For the long build you stop watching: when a terminal command or task that took a
while ends and the VS Code window is in the background, a Windows toast says what
ran, how long it took and whether it failed. Shell integration and the task API
already report this, so nothing has to be wrapped or prefixed.

**[vscode-assist](https://github.com/Ruminem/vscode-assist)**
Navigation shortcuts VS Code does not ship, bound to keys it does not use. The
main one is a round trip: `Alt+G` on a declaration goes to the definition and
back again, with overrides and base virtuals in C++.

**[vscode-neon-glow](https://github.com/Ruminem/vscode-neon-glow)**
Neon glow for syntax highlighting that derives itself from the active theme's own
token colours, so it works with whatever colour theme is already in use.

All six are plain JavaScript with no build step and no dependencies.

### Other

**[kakaotalk-theme](https://github.com/Ruminem/kakaotalk-theme)**
KakaoTalk themes for iOS (`.ktheme`) and Android (`.apk`). Every colour lives in
one palette table, and the CSS, `colors.xml`, images and previews are all
generated from it.

**[hdr-auto-toggle](https://github.com/Ruminem/hdr-auto-toggle)**
A PowerShell script that turns Windows HDR on while a registered game has a
window open and off once they are all closed, so screenshots outside games do
not bloom.

**[cursor-playground](https://github.com/Ruminem/cursor-playground)**
For dressing up the Windows mouse pointer: 120 pixel-art pointer schemes, 20 animated
ones included. Try them as your cursor on a [preview page](https://ruminem.github.io/cursor-playground/win-cursor/preview.html),
then recolour it with a hue slider or swap the arrow silhouette between four shapes,
and apply it to Windows, resize it or roll back with a button after a one-line
setup. Also has a pixel cat that follows the cursor around the desktop and falls
asleep when it stops. Everything is drawn as text and built with the Python
standard library.

**[vsx-tools](https://github.com/Ruminem/vsx-tools)**
For keeping several home-made VS Code extensions in step: one table shows each
one's version, installed version and git state, and one command builds and
installs them all. A single Node script with no dependencies, plus an
[install page](https://ruminem.github.io/vsx-tools/?lang=en) for setting up a new machine.

---

### VS Code 익스텐션

**[cmake-link-explorer](https://github.com/Ruminem/cmake-link-explorer)** —
CMake 프로젝트에서 링크 때문에 막힐 때 씀. 이 헤더를 쓰려면 무엇을 링크해야 하는지,
**누가 이 타겟을 링크하는지**, 바이너리 크기와 빌드 시간을 무엇이 잡아먹는지, 이
파일이 실제로 어떤 매크로로 컴파일되는지 보여줌. `CMakeLists.txt`를 파싱하지 않고
CMake File API·링커 맵·ninja 빌드 로그에 이미 있는 것을 읽음.

**[hover-decode](https://github.com/Ruminem/hover-decode)** —
코드나 로그에서 한눈에 뜻을 알 수 없는 값을 볼 때 씀. Windows 에러 코드, epoch
타임스탬프, 기간, 16진수, base64 문자열, HTTP 상태 코드에 마우스를 올리면 그게
무엇인지 보여줌. 에러 코드는 Windows가 가진 메시지까지 같이 보여 주고, 터미널에서는
링크 풀이로 같은 내용이 뜸. 내 용어는 저장소 밖에 있는 개인 사전에, 팀 용어는
프로젝트에 같이 커밋하는 사전에 넣어 둠.

**[native-toolbelt](https://github.com/Ruminem/native-toolbelt)** —
내 PC에서만 안 도는 네이티브 빌드를 볼 때 씀. `.exe`나 `.dll`을 읽어 어떤 DLL이
필요한지, 윈도우가 그걸 어디서 찾을지, 아예 못 찾는 게 무엇인지 알려 줌. 지연 로드
임포트도 같이 세고, 바이너리 옆에 있지만 검색 경로 밖인 DLL은 그 경로를 적어 줌.
목록을 PE 파일에서 직접 읽으므로 Visual Studio도 `dumpbin`도 필요 없음.

**[terminal-toast](https://github.com/Ruminem/terminal-toast)** —
오래 걸리는 빌드를 지켜보지 않고 딴 일 할 때 씀. 한참 걸린 터미널 명령이나 태스크가
끝났는데 VS Code 창이 백그라운드면 무엇이 돌았고 얼마나 걸렸고 실패했는지를 윈도우
토스트로 띄움. 셸 통합과 태스크 API가 이미 알려 주는 것을 읽으므로 명령을 감싸거나
앞에 무언가 붙일 필요 없음.

**[vscode-assist](https://github.com/Ruminem/vscode-assist)** —
VS Code에 없는 탐색 단축키를 VS Code가 안 쓰는 키에 묶음. 핵심은 왕복 이동 —
선언에서 `Alt+G`를 누르면 정의로, 다시 누르면 선언으로 돌아옴. C++에서는 오버라이드와
베이스 가상 함수까지 챙김.

**[vscode-neon-glow](https://github.com/Ruminem/vscode-neon-glow)** —
문법 강조에 네온 글로우를 입힘. 팔레트를 박아두지 않고 **지금 쓰는 테마의 토큰
색에서 글로우를 유도**하므로 어떤 색 테마와도 맞음.

여섯 다 순수 JavaScript고 빌드 단계도 의존성도 없음.

### 그 밖에

**[kakaotalk-theme](https://github.com/Ruminem/kakaotalk-theme)** —
iOS(`.ktheme`)·안드로이드(`.apk`) 카카오톡 테마. 색은 팔레트 표 한 곳에서만
관리하고 CSS·`colors.xml`·이미지·미리보기가 전부 거기서 생성됨.

**[hdr-auto-toggle](https://github.com/Ruminem/hdr-auto-toggle)** —
등록한 게임 창이 열리면 Windows HDR을 켜고 모두 닫히면 다시 끄는 PowerShell
스크립트. 게임 밖에서 캡처할 때 밝은 부분이 번지지 않게 함.

**[cursor-playground](https://github.com/Ruminem/cursor-playground)** —
윈도우 마우스 포인터를 꾸밀 때 씀. 움직이는 커서 20종을 포함한 픽셀아트 포인터 구성표
120종. [시안 페이지](https://ruminem.github.io/cursor-playground/win-cursor/preview.html)에서
커서로 먼저 써 보고 색조 슬라이더로 색을 바꾸거나 화살표 모양을 네 가지 중에서 고름.
한 줄 설치해 두면 버튼으로 윈도우에 적용·크기 조정·원래대로를 함. 바탕화면에서 커서를 따라다니다 멈추면 잠드는 픽셀 고양이도
있음. 전부 텍스트로 그리고 Python 표준 라이브러리로 만듦.

**[vsx-tools](https://github.com/Ruminem/vsx-tools)** —
직접 만든 VS Code 확장 여러 개를 함께 관리할 때 씀. 확장마다 버전, 설치된 버전, git
상태를 한 표로 보여주고 명령 하나로 전부 빌드·설치함. 의존성 없는 Node 스크립트 하나.
새 PC 에서는 [설치 페이지](https://ruminem.github.io/vsx-tools/?lang=ko)에서 확장을 골라 설치함.
