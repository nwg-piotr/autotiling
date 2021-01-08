v1.3 (2021-01-08)
- added `--workspaces` argument to restrict autotiling to certain workspaces @riscie
- code formatting and arguments cleanup

v1.2 (2021-01-04)
- added --version argument @nschloe
- allowed autotiling to be run as a script directly @Lqp1

v1.1 (2020-07-21)
- added proper Python package structure so that could be published on PyPi 
[#14](https://github.com/nwg-piotr/autotiling/pull/14) @nschloe

v1.0 (2020-07-19)
- changed fullscreen mode detection to reflect changes in sway 1.5 
[#11](https://github.com/nwg-piotr/autotiling/pull/11) @ammgws
78
v0.9 (2020-04-08)
- bug in debugging fixed [#6](https://github.com/nwg-piotr/autotiling/pull/6)

v0.8 (2020-03-21)
- `--debug` option added [#5](https://github.com/nwg-piotr/autotiling/pull/5) @ammgws

v0.7 (2020-02-20)
- Only run command if absolutely necessary [#3](https://github.com/nwg-piotr/autotiling/pull/3) @ammgws

v0.5 (2020-02-19)
- Check if con exists before querying submembers [#2](https://github.com/nwg-piotr/autotiling/pull/2) @ammgws

v0.4 (2019-12-11)
- ignoring stacked layouts added [#1](https://github.com/nwg-piotr/autotiling/pull/1) @travankor

v0.3 (2019-09-26)
- unnecessary Event.WINDOW_NEW subscription removed

v0.2 (2019-09-25)
- tabbed layouts and full screen mode excluded
- fullscreen_mode detection diversified for i3 and sway
