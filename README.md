A PoC showing injection of additional packages for the alpine image via `build-args`

For instance, if you build an image using the `pandas` module in python, it will fail because of the lack of native libraries in the base alpine image. You'll see something like the following error message on build.

```
    RuntimeError: Broken toolchain: cannot link a simple C program
```

By adding a `ARG` in the `Dockerfile` and letting one inject additional packages, the built image could include additional packages and lead to a successful build.

```
# build with additional packages required by pandas
faas-cli build --build-arg 'ADDITIONAL_PACKAGE=make automake gcc g++ subversion python3-dev'

# deploy
faas-cli deploy

# invoke
echo '' |faas invoke faas-pandas
{"A":{"1356998400000":0.7141047827,"1357084800000":0.1363116581,"1357171200000":0.6025874047,"1357257600000":-0.9151811418,"1357344000000":-0.335473092,"1357430400000":0.4021770176},"B":{"1356998400000":-0.8583147783,"1357084800000":0.2183210089,"1357171200000":0.9400280865,"1357257600000":-0.0560025869,"1357344000000":0.9899218939,"1357430400000":-0.4704440479},"C":{"1356998400000":1.2526469043,"1357084800000":-0.9468157998,"1357171200000":-1.9264357788,"1357257600000":0.4827442627,"1357344000000":0.0032829625,"1357430400000":-0.7745142946},"D":{"1356998400000":-0.097564495,"1357084800000":0.7604999532,"1357171200000":-0.3399715634,"1357257600000":1.0363703792,"1357344000000":-1.3265440567,"1357430400000":-1.1893725234}}
```
