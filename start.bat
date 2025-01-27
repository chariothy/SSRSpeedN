::conda create -n ssrspeed
::conda activate ssrspeed
python -m pip install --upgrade pip
pip3 install -r requirements.txt
::pip3 install requests
::pip3 install pyyaml
::pip3 install Pillow
::pip3 install pysocks
::pip3 install aiohttp
::pip3 install aiohttp_socks
::pip3 install requests[socks]
::pip3 install flask
::pip3 install flask-cors

echo.
echo Usage: main.py [options] arg1 arg2...
echo.
echo Options:
echo.
echo  --version                              show program's version number and exit
echo  -h, --help                             show this help message and exit
echo  -c GUICONFIG, --config=GUICONFIG       Load config generated by shadowsocksr-csharp.
echo  -u URL, --url=URL                      Load ssr config from subscription url.
echo  -m TEST_METHOD, --method=TEST_METHOD   Select test method in Select test method in [speedtestnet, fast, socket, stasync].
echo  -M TEST_MODE, --mode=TEST_MODE         Select test mode in [all,pingonly,wps].
echo  --include                              Filter nodes by group and remarks using keyword.
echo  --include-remark                       Filter nodes by remarks using keyword.
echo  --include-group                        Filter nodes by group name using keyword.
echo  --exclude                              Exclude nodes by group and remarks using keyword.
echo  --exclude-group                        Exclude nodes by group using keyword.
echo  --exclude-remark                       Exclude nodes by remarks using keyword.
echo  --use-ssr-cs                           Replace the ShadowsocksR-libev with the ShadowsocksR-C# (Only Windows)
echo  -g GROUP                               Manually set group.
echo  -y, --yes                              Skip node list confirmation before test.
echo  -C RESULT_COLOR, --color=RESULT_COLOR  Set the colors when exporting images..
echo  -S SORT_METHOD, --sort=SORT_METHOD     Select sort method in [speed,rspeed,ping,rping],default not sorted.
echo  -i IMPORT_FILE, --import=IMPORT_FILE   Import test result from json file and export it.
echo  --skip-requirements-check              Skip requirements check.
echo  --debug                                Run program in debug mode.
echo.
echo  Test Modes
echo  Mode                 Remark
echo  TCP_PING             Only tcp ping, no speed test
echo  WEB_PAGE_SIMULATION  Web page simulation test
echo  ALL                  Full speed test (exclude web page simulation)
echo.
echo  Test Methods
echo  Methods              Remark
echo  ST_ASYNC             Asynchronous download with single thread
echo  SOCKET               Raw socket with multithreading
echo  SPEED_TEST_NET       Speed Test Net speed test
echo  FAST                 Fast.com speed test
echo.

pause

set /p a=Input subscription URL:
if "%a%"=="" (
goto :end
) else (
goto :jx1
)
:jx1
echo python main.py -u "%a%"
echo.
python main.py -u "%a%"
pause
set a=

:end
exit /B
