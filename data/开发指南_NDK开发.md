# 合并文件
合并时间: 2025-04-30 06:34:51

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ndk-development-overview-V14
爬取时间: 2025-04-30 06:12:40
来源: Huawei Developer
NDK（Native Development Kit）是HarmonyOS SDK提供的Native API、相应编译脚本和编译工具链的集合，方便开发者使用C或C++语言实现应用的关键功能。NDK只覆盖了HarmonyOS一些基础的底层能力，如C运行时基础库libc、图形库、窗口系统、多媒体、压缩库、面向ArkTS/JS与C跨语言的Node-API等，并没有提供ArkTS/JS API的完整能力。
运行态，开发者可以使用NDK中的Node-API接口，访问、创建、操作JS对象；也允许JS对象使用Native动态库。
NDK适用场景
适合使用NDK的场景：应用涉及如下场景时，适合采用NDK开发
-  性能敏感的场景，如游戏、物理模拟等计算密集型场景。
-  需要复用已有C或C++库的场景。
-  需要针对CPU特性进行专项定制库的场景，如Neon加速。
不建议使用NDK的场景：应用涉及如下场景时，不建议采用NDK开发
-  纯C或C++的应用。
-  希望在尽可能多的HarmonyOS设备上保持兼容的应用。
NDK必备基础知识
为顺利进行NDK开发，开发者需要先掌握必要的基本概念及基础知识。
NDK基本概念
-  Node-API 曾用名NAPI，是HarmonyOS中提供ArkTS/JS与C/C++跨语言调用的接口，是NDK接口中的一部分。该接口是在Node.js提供的Node-API基础上扩展而来，但与Node.js中的Node-API不完全兼容。
-  C API HarmonyOS NDK的曾用名，不再使用。
前置知识
-  Linux C语言编程知识 内核、libc基础库基于POSIX等标准扩展而来，掌握基本的Linux C编程知识能够更好的帮助理解HarmonyOS NDK开发。
-  CMake使用知识 CMake是HarmonyOS默认支持的构建系统。请先通过CMake官方文档了解基础用法。
-  Node Addons开发知识 ArkTS采用Node-API作为跨语言调用接口，熟悉基本的Node Addons开发模式，可以更好理解NDK中Node-API的使用。
-  Clang/LLVM编译器使用知识 具备一定的Clang/LLVM编译器基础知识，能够帮助开发者编译出更优的Native动态库。
NDK目录简介
-  build目录：放置预定义的toolchain脚本文件ohos.toolchain.cmake CMake编译时需要读取该文件中的默认值，比如编译器架构、C++库链接方式等，因此在编译时会通过CMAKE_TOOLCHAIN_FILE指出该文件的路径，便于CMake在编译时定位到该文件。
-  build-tools文件夹：放置NDK提供的编译工具
-  llvm文件夹：放置NDK提供的编译器
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165811.82977044494199813274008326763921:50001231000000:2800:3DD61820FF02FA85E6E80FCEE4C761CC6A120745F587AB89849D66FA4C622465.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165811.71822256822135215440051155871645:50001231000000:2800:E504D664D71608C6736F9FB94EC55B34074FF00DCEC9A593ABE023CE45799755.png)
NDK常用模块
下表介绍了NDK的常用模块。
| 模块 | 模块简介 |
| --- | --- |
| 标准C库 | 以musl为基础提供的标准C库接口。 |
| 标准C++库 | C++运行时库libc++_shared。 |
| 日志 | 打印日志到系统的HiLog接口。 |
| Node-API | 当需要实现ArkTS/JS和C/C++之间的交互时，可以使用Node-API。 |
| FFRT | 基于任务的并发编程框架。 |
| libuv | 三方异步IO库。 |
| zlib | zlib库，提供基本的数据压缩、解压接口。 |
| Rawfile | 应用资源访问接口，可以读取应用中打包的各种资源。 |
| XComponent | ArkUI XComponent组件提供surface与触屏事件等接口，方便开发者开发高性能图形应用。 |
| Drawing | 系统提供的2D图形库，可以在surface进行绘制。 |
| OpenGL | 系统提供的OpenGL 3D图形接口。 |
| OpenSL ES | 用于2D、3D音频加速的接口库。 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/create-with-ndk-V14
爬取时间: 2025-04-30 06:12:53
来源: Huawei Developer
下面通过DevEco Studio的NDK工程模板，来演示如何创建一个NDK工程。
不同DevEco Studio版本的向导界面、模板默认参数等会有所不同，请根据实际工程需要，创建工程或修改工程参数。
1.  通过如下两种方式，打开工程创建向导界面。
2.  根据工程创建向导，选择Native C++工程模板，然后单击Next。
3.  在工程配置页面，根据向导配置工程的基本信息后，单击Finish，工具会自动生成示例代码和相关资源，等待工程创建完成。 在工程entry/src/main目录下会包含cpp目录，该目录文件的详细介绍请参见C++工程目录结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165811.04329556132948807319968877509558:50001231000000:2800:E479E768771A279B3105655D52D47F4B1B41A5E36E926B79DA191358953691D9.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165811.94826161061725330943651613489224:50001231000000:2800:8BD469D854FA1DB2A0B72A368968DDDE4861E182EB8D91ACD73EAEB4A1B99004.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/build-with-ndk-V14
爬取时间: 2025-04-30 06:13:06
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/build-with-ndk-overview-V14
爬取时间: 2025-04-30 06:13:20
来源: Huawei Developer
HarmonyOS NDK默认使用CMake作为构建系统，随包提供了符合HarmonyOS工具链的基础配置文件ohos.toolchain.cmake，用于预定义CMake变量来简化开发者配置。
常用的NDK工程构建方式有：
-  从源码构建 源码构建也有不同方式：
-  使用预构建库构建
本章节将通过具体示例介绍如何在Native工程中使用NDK，以及如何编写CMake脚本来构建NDK工程。
ohos.toolchain.cmake简介
ohos.toolchain.cmake是HarmonyOS NDK提供给CMake的toolchain脚本，里面预定义了编译HarmonyOS应用需要设置的编译参数，如交叉编译设备的目标、C++运行时库的链接方式等；这些参数在调用CMake命令时，可以从命令行传入，来改变默认编译链接行为。此文件中的常用参数见下表。
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| OHOS_STL | c++_shared/c++_static | libc++的链接方式。默认为c++_shared。 c++_shared表示采用动态链接libc++_shared.so；c++_static表示采用静态链接libc++_static.a。 由于C++运行时中存在一些全局变量，因此同一应用中的全部Native库需要采用相同的链接方式。  |
| OHOS_ARCH | armeabi-v7a/arm64-v8a/x86_64 | 设置当前Native交叉编译的目标架构，当前支持的架构为armeabi-v7a/arm64-v8a/x86_64。 |
| OHOS_PLATFORM | OHOS | 选择平台。当前只支持HarmonyOS平台。 |
libc++的链接方式。默认为c++_shared。
c++_shared表示采用动态链接libc++_shared.so；c++_static表示采用静态链接libc++_static.a。
由于C++运行时中存在一些全局变量，因此同一应用中的全部Native库需要采用相同的链接方式。
上述参数最终会控制Clang的交叉编译命令，产生合适的命令参数。
-  --target={arch}-linux-ohos参数，通知编译器生成相应架构下符合HarmonyOS ABI的二进制文件。
-  --sysroot={ndk_root}/sysroot参数，告知编译器HarmonyOS系统头文件的所在位置。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/build-with-ndk-ide-V14
爬取时间: 2025-04-30 06:13:33
来源: Huawei Developer
NDK通过CMake和Ninja编译应用的C/C++代码，编译过程如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.41489301199236220413594819709132:50001231000000:2800:124046EAFB3B90941B130B1733A1EDF24AC68A8DAAE7F253AA457190CEC9F2EA.png)
核心编译过程如下：
1.  根据CMake配置脚本以及build-profile.json5中配置的externalNativeOptions构建参数，与缓存中的配置比对后，生成CMake命令并执行CMake。
2.  执行Ninja，按照makefile执行编译和链接，将生成的.so以及运行时依赖的.so同步到输出目录，完成构建过程。
通过DevEco Studio提供的应用模板，可以快速生成CMake构建脚本模板，并在build-profile.json5中指定相关编译构建参数。
CMakeLists.txt
通过DevEco Studio模板工程创建的NDK工程中，包含默认生成的CMakeLists.txt脚本，如下所示：
默认的CMakeLists.txt脚本中添加了编译所需的源代码、头文件以及三方库，开发者可根据实际工程添加自定义编译参数、函数声明、简单的逻辑控制等。
externalNativeOptions
模块级build-profile.json5中externalNativeOptions参数是NDK工程C/C++文件编译配置的入口，可以通过path指定CMake脚本路径、arguments配置CMake参数、cppFlags配置C++编译器参数、abiFilters配置编译架构等。
externalNativeOptions具体参数说明如下表所示。
| 配置项 | 类型 | 说明 |
| --- | --- | --- |
| path | string | CMake构建脚本地址，即CMakeLists.txt文件地址。 |
| abiFilters | array | 本机的ABI编译环境，包括： - arm64-v8a - x86_64 如不配置该参数，编译时默认编译出arm64-v8a架构相关so。  |
| arguments | string | CMake编译参数。 |
| cppFlags | string | C++编译器参数。 |
本机的ABI编译环境，包括：
- arm64-v8a
- x86_64
如不配置该参数，编译时默认编译出arm64-v8a架构相关so。
更多关于build-profile.json5中参数的说明，请参考build-profile.json5。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/build-with-ndk-cmake-V14
爬取时间: 2025-04-30 06:13:46
来源: Huawei Developer
在很多复杂应用工程中，C++代码工程是通过CMake等构建系统以命令行方式来编译构建的，接下来介绍如何把已有的CMake工程切换到HarmonyOS工具链中，从而使用命令行CMake构建该工程。
下载NDK开发包
NDK开发相关工具位于$DevEco Studio安装目录/sdk/default/openharmony/native路径下。
解压NDK开发包
下载完成后，将压缩包放入创建好的文件夹下解压。
windows/linux 使用 SDK 包解压完成效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.13414352011422565190316129131390:50001231000000:2800:0F7849F2A19A442910811E2ECBF23D5D927F7BD5014BF51F63C36849D44E217F.png)
mac使用 SDK 包解压完成效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.06095987742138107543096268675522:50001231000000:2800:6A4C0F6F4ED8A2CCD802E16D707874FD8ED8FD3758A2B3A88EFAA184AA0A30E1.png)
配置环境变量
如果只是在DevEco Studio中使用，跳过以下步骤：
-  配置 linux 系统下环境变量
-  配置 mac 系统下环境变量
-  配置 windows 下的环境变量 右键点击我的电脑，在下拉框中选择我的电脑，点击高级系统设置，点击环境变量，点击Path后点编辑，点击新建，将路径添加进去，之后保存退出，打开cmd（若下一步不能够实现，请重启电脑尝试）。 打开命令框，输入{cmake实际安装路径}\cmake.exe -version，命令行正确回显cmake的版本号，说明环境变量配置完成。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.86090241509776762091385456602641:50001231000000:2800:C148342627BBDDE55C9BBB6FE939387F5463F331456AC51BFF863CAAC74DE1D1.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.12024417286919815643082912337508:50001231000000:2800:695C414BA4709E2BCCC5C0D73CE2CBC8275EFE4DB0254405E3B08C52A920D0DA.png)
1.  linux 和 mac 系统环境下 windows 系统环境下，cmake 安装路径为自己所配置的环境变量路径 通过 我的电脑->高级系统设置->环境变量->在 Path 对象中查看
2.  linux 和 mac 系统环境下
3.  windows 系统环境下，cmake 安装路径为自己所配置的环境变量路径 通过 我的电脑->高级系统设置->环境变量->在 Path 对象中查看
-  linux 和 mac 系统环境下
-  windows 系统环境下，cmake 安装路径为自己所配置的环境变量路径 通过 我的电脑->高级系统设置->环境变量->在 Path 对象中查看
使用NDK开发包编译Native程序
应用开发者可以通过NDK开发包快速的开发出Native动态库、静态库与可执行文件。NDK开发包提供CMake编译构建工具脚本，下面通过编写一个C/C++ demo工程来演示适配过程。
demo工程内容
下面是一个CMake的demo工程内容，此工程包含两个目录，include目录包含此库的头文件，src目录包含全部源码；src目录包含两个文件，sum.cpp的算法文件，以及main.cpp的调用算法的主入口文件，目标是编译成一个可执行程序，以及一个算法动态库。
demo目录图
根目录CMakeLists.txt内容
内部CMakeLists.txt内容
源码内容
hello.cpp源码
sum.h源码
sum.cpp源码
编译构建demo工程
linux 和 mac 系统环境下
在工程目录下，创建build目录，用来放置CMake构建时产生的中间文件。注意: ohos-sdk是下载下来的SDK的根目录，开发者需要自行替换成实际的下载目录。
1.  采用OHOS_STL=c++_shared动态链接c++库方式构建工程，如不指定，默认采用c++_shared；DOHOS_ARCH参数可根据系统架构来决定具体值。
```shell
>mkdir build && cd build
>cmake -DOHOS_STL=c++_shared -DOHOS_ARCH=armeabi-v7a -DOHOS_PLATFORM=OHOS -DCMAKE_TOOLCHAIN_FILE={ohos-sdk}/linux/native/build/cmake/ohos.toolchain.cmake ..
>cmake --build .
```
2.  采用OHOS_STL=c++_static静态链接c++库方式构建工程。 命令中，OHOS_ARCH与OHOS_PLATFORM两个变量最终会生成clang++的--target命令参数，在此例子中就是--target=arm-linux-ohos --march=armv7a两个参数。 CMAKE_TOOLCHAIN_FILE指定了toolchain文件，在此文件中默认给clang++设置了--sysroot={ndk_sysroot目录}，告诉编译器查找系统头文件的根目录。
```shell
>mkdir build && cd build
>cmake -DOHOS_STL=c++_static -DOHOS_ARCH=armeabi-v7a -DOHOS_PLATFORM=OHOS -DCMAKE_TOOLCHAIN_FILE={ohos-sdk}/linux/native/build/cmake/ohos.toolchain.cmake ..
>cmake --build .
```
windows系统环境下
在windows下使用cmake进行编译，与linux下不同的是，使用cmake要加入参数 -G 选择使用的生成器，直接回车会列出下面的生成器。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.22412056177063758671771647651753:50001231000000:2800:788E93B1D8D8AA739918F834A9B22A3814A74A394EB8DAB96309BA22C977BFCF.png)
这里使用的是cmake .. -G "Ninja" 引号里面跟的参数就是上图查看的环境所支持的生成器，这里ndk中自带的生成器是Ninja。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.02180018013101139445034131224115:50001231000000:2800:5BCBAA9266B7F68C14991C16865A3B0BF270DD6C60763BC37A78549BAC13FABB.png)
Step 1. 同样在工程目录下创建 build 文件夹并执行以下指令：
注：如需debug调试，增加参数 -D CMAKE_BUILD_TYPE=normal；cmake路径和编译工具链ohos.toolchain.cmake路径都是下载好的ndk路径。
执行结果如下图：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.00772664450144029671868593158638:50001231000000:2800:D0E6F55E3DCAD06A3B84B23C48D3AB24ECF968F8A762B15E0E98D8BB1953FC54.png)
这里生成的build.ninja文件就是我们需要的 。
Step 2. 让我们用ninja指令来编译生成目标文件，其位置如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.49046266043226572993348539460864:50001231000000:2800:7D11932E20526DF35D68A2E0EE94EC98462A7BA77B15F0B4EAE4F7DDEDDEF19F.png)
ninja -f build.ninja 或者用 cmake --build . 执行结果如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.58483872088619422408485628205758:50001231000000:2800:F510DCF8F78C3D7EF9A12AC08B04675FB32E6C0D876009A3D7BA9594744571C7.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/build-with-ndk-prebuilts-V14
爬取时间: 2025-04-30 06:14:00
来源: Huawei Developer
在NDK工程中，可以通过CMake语法规则引入并使用预构建库。在引用预构建库时，模块libs目录中的预构建库，以及在CMakeList.txt编译脚本中声明的预构建库都会被打包。
直接引入预构建库
可以通过直接将预构建的库文件复制到项目文件中, 来使用预构建库。例如在项目中需要使用预构建库libavcodec_ffmpeg.so，其开发态存放路径如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.08265445435673658368659120915427:50001231000000:2800:1E21E16DF06998678CF27B6960BC1C1F1444CB805AC8659AB9CFE3E302390938.png)
在模块的CMakeLists.txt编译脚本中通过add_library添加所需的预构建库，并声明预构建库路径等信息后，可以在target_link_libraries中声明链接该预构建库，脚本示例如下所示：
在模块的CMakeLists.txt编译脚本中添加include_directories：
当在HAR中使用预构建库时，当前编译的库和链接所需预构建库会打包到HAR中的libs目录下，如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165812.69158599576300006796550988918250:50001231000000:2800:82E9D1E0D5AAA0BAF2E4EBFA20A4B20418F5AD38F0E28F352C4ECE2120466913.png)
预构建库的SONAME问题
请确保引入的预构建动态库（so）正确设置了SONAME。
如果预构建so没有SONAME，链接器将会将so的绝对路径插入到依赖这个so的二进制文件的dynamic section中。当这些二进制文件随hap包发布运行时，动态加载器（dynamic loader）可能最终无法找到这个so而导致错误。
可以使用llvm-readelf工具查看so文件是否设置了SONAME。llvm-readelf工具路径为：${DevEco Studio安装目录}/sdk/default/openharmony/native/llvm/bin或者${command-line-tools安装目录}/sdk/default/openharmony/native/llvm/bin/llvm-readelf。
示例如下：
若预构建so使用cmake进行构建，则所有的so默认会设置SONAME（只要目标平台支持）。
若预构建so使用其他构建工具，可以通过配置ldflags来设置。
使用远程依赖HAR中集成的预构建库
当使用远程依赖HAR中集成的预构建库时，CMakeLists.txt文件中引用脚本如下所示：
使用本地HAR中集成的预构建库
当使用本地HAR中集成的预构建库时，CMakeLists.txt文件中引用脚本如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/bisheng-compiler-V14
爬取时间: 2025-04-30 06:14:13
来源: Huawei Developer
毕昇编译器简介
毕昇编译器是基于LLVM开源软件开发的一款用于C/C++等语言的native编译器，能将C/C++代码工程编译链接成可以在设备上运行的二进制。在无需改动用户代码的条件下，相比业界主流的开源LLVM或GCC编译器，毕昇编译器能提供更强大的优化能力，使编译链接出来的二进制的运行时长更短、指令数更少，帮助提升应用在设备上的运行流畅度。
能力范围
毕昇编译器提供将C/C++代码工程编译链接成可以在设备上运行的二进制的基本能力，主要包括以下三方面：
亮点特征
毕昇编译器相对于LLVM/GCC编译器有以下特点。
针对循环相关的编译优化，毕昇编译器在场景识别、结构变换等方面做了改进和增强。例如在社区LLVM已有的Loop Distribution优化上，毕昇编译器相比开源LLVM编译器，能额外识别出循环内不同代码块间数据依赖关系、以及不同代码块运行的迭代次数差别，从而能对更多的循环进行loop distribution优化。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.61073952664265345902569591925394:50001231000000:2800:248A62AB15CE235D6BE02447823BAD9987B91E7542A0F20F5E955C89238CA572.png)
Figure 1 毕昇编译器Loop Distribution优化增强示例
毕昇编译器在矢量化优化方面，相比开源LLVM编译器，不仅能将更多的循环做矢量化转换，还在矢量化指令选择上更高效。例如下面示例中，开源LLVM编译器虽然做了矢量化，但使用了5条矢量指令；而毕昇编译器只需要使用2条矢量指令，最终产生的二进制效率更优。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.88948712879521471461769583863067:50001231000000:2800:375647E2990706354BFFC4E8218D4281ED69311004808944FD3440F6B2548BB4.png)
Figure 2 毕昇编译器矢量化优化增强示例
毕昇编译器使用指导
在DevEco Studio 中使用毕昇编译器：
开发者可以获取DevEco Studio 5.0.3.402及以上的版本，在HarmonyOS应用的工程级build-profile.json5中简单配置即可使用毕昇编译器：在runtimeOS为HarmonyOS的时候，设置nativeCompiler为BiSheng，即可使用毕昇编译器构建HarmonyOS工程的C/C++代码。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.62113833349269927644457485770385:50001231000000:2800:3579BB5DB8464747792F4F37D3EB8A13C7D36AA821F2C31CF34809AEFE859E38.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/coding-V14
爬取时间: 2025-04-30 06:14:26
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/develop-code-overview-V14
爬取时间: 2025-04-30 06:14:40
来源: Huawei Developer
HarmonyOS NDK提供多个开放能力库，如图形图像、内存管理、设备管理等，供开发者实现代码逻辑；同时提供业界标准库，如libc标准库、标准C++库、Node-API等。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/c-cpp-V14
爬取时间: 2025-04-30 06:14:53
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/c-cpp-overview-V14
爬取时间: 2025-04-30 06:15:06
来源: Huawei Developer
HarmonyOS NDK提供业界标准库libc标准库、标准C++库，本文用于介绍C/C++标准库在HarmonyOS中的机制，开发者了解这些机制有助于在NDK开发过程中避免相关问题。
1. C++兼容性
在HarmonyOS系统中，系统库与应用Native库都在使用C++标准库（参考libc++版本），系统库依赖的C++标准库随镜像版本升级，而应用Native库依赖的C++标准库随编译使用的SDK版本升级，两部分依赖的C++基础库会跨多个大版本，产生ABI兼容性问题。为了解决此问题，HarmonyOS上把两部分依赖的C++标准库进行了区分。
两个库使用的C++命名空间不一样，libc++.so使用__h作为C++符号的命名空间，libc++_shared.so使用__n1作为C++符号的命名空间。
系统和应用使用的C++标准库不能进行混用，Native API接口当前只能是C接口，可以通过这个接口隔离两边的C++运行环境。因此在使用共享库HAR包构建应用时，如果HAR包含的libc++_shared.so不同于应用使用的libc++_shared.so版本，那么只有其中一个版本会安装到应用里，可能会导致不兼容问题，可以使用相同的SDK版本更新HAR包解决此问题。
已知C++兼容性问题：
应用启动或者dlopen时hilog报错symbol not found, s=__emutls_get_address，原因是API9及之前版本SDK中的libc++_shared.so无此符号，而API11之后版本SDK的libc++_shared.so是有此符号的。解决此问题需要更新应用或者共享库HAR包的SDK版本。
2. musl libc动态链接器
动态库加载命名空间隔离
动态库加载命名空间（namespace，下面统称为ns）是动态链接器设计的一个概念（区别于C++语言中的命名空间），其设计的主要目的是为了在进程中做native库资源访问的管控，以达到安全隔离的目的。例如系统native库允许加载系统目录（/system/lib64;/vendor/lib64等）下的native库，但是普通应用native库仅允许加载普通应用native库和ndk库，而不允许直接加载系统native库。
动态链接器无论是在加载编译依赖（DT_NEEDED）中指定的共享库，还是调用dlopen加载指定的共享库，都需要关联到具体的ns。
HarmonyOS中动态库加载namespace配置的情况
-  default ns：动态链接器启动时默认创建的ns，它可以搜索/system/lib{abi};/vendor/lib{abi}等系统目录路径下的so。
-  ndk ns：动态链接器启动时默认创建的ns，它可以搜索/system/lib{abi}/ndk目录下的so，主要是暴露了NDK接口的so。
-  app ns: 应用启动时创建的ns，它的搜索路径一般是应用的安装路径(可能为沙箱路径)，即可加载应用的so。
当前这一套命名空间机制主要限制了应用native库和系统native库之间的调用，如图所示，具体规则为：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.56336324388409447879088416507151:50001231000000:2800:8D7EC3ACC4F588471A044CB812DB5E4E3EC4CBF5AA68F45512480563ACBB02BB.png)
rpath机制
rpath（run-time path）是在运行时指定共享库搜索路径的机制。该机制允许在可执行文件或共享库中嵌入一个用于在运行时指定库的搜索路径的信息。
由于上文介绍的命名空间隔离机制，应用仅允许加载对应安装目录拼接native库路径下（例如arm64平台上为libs/arm64）的应用native库，当应用程序涉及加载较多的native库，期望创建多个native库加载路径方便管理，但是会导致无法加载新创建目录下的native库，这种情况可以通过rpath机制编译时指定搜索路径。
例如，应用安装目录lib/arm64下的libhello.so依赖新创建路径lib/arm64/module下的libworld.so，那么在应用的CMakeList.txt里设置上rpath编译选项后编译，使用readelf查看libhello.so的rpath配置如图所示，$ORIGIN为libhello.so所在路径，运行时即可正常加载module目录下的libworld.so。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.43045009055993058462593833389700:50001231000000:2800:122A3A4D7B6FC1142D4EFBDE9AC0481938359DFCB45B120A6B71A7A17B103E2B.png)
支持dlclose
支持使用dlclose真实卸载动态库的能力。
支持symbol-version机制
symbol-version是libc在动态链接-符号重定位阶段的符号检索机制，支持不同版本的符号重定位，也可以帮助解决重复符号的问题。可参考LD Version Scripts (GNU Gnulib)。
网络接口select支持fd fortify检测
宏定义FD_SET/FD_CLR新增fd有效值检查，当传入的fd不在区间[0, 1024)中会触发abort crash。
宏定义FD_ISSET新增fd有效值检查，当传入的fd不在区间[0, 1024)中会返回false。
全球化支持
自API12起，newlocale及setlocale接口支持将locale设置C、C.UTF-8、en_US、en_US.UTF-8、zh_CN及zh_CN.UTF-8。新增在zh_CN及zh_CN.UTF-8的locale设置下对strtod_l、wcstod_l和localeconv的支持。注意strtod_l及wcstod_l不支持对十六进制及十六进制小数的转换。
fdsan功能
fdsan使用指导可以帮助检测文件的重复关闭和关闭后使用问题。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/fdsan-V14
爬取时间: 2025-04-30 06:15:20
来源: Huawei Developer
1. 功能介绍
fdsan针对的操作对象是文件描述符，主要用于检测不同使用者对相同文件描述符的错误操作，包括多次关闭（double-close）和关闭后使用（use-after-close)。这些文件描述符可以是操作系统中的文件、目录、网络套接字和其他I/O设备等，在程序中，打开文件或套接字会生成一个文件描述符，如果此文件描述符在使用后出现反复关闭、或者关闭后使用等场景，就会造成内存泄露、文件句柄泄露等安全隐患问题。该类问题非常隐蔽，且难以排查，为了更好地检测此类问题，因此引入了此种针对文件描述符错误操作的检测工具fdsan。
2. 实现原理
设计思路：当打开已有文件或创建一个新文件的时候，在得到返回fd后，设置一个关联的tag，来标记fd的属主信息；关闭文件前，检测fd关联的tag，判断是否符合预期(属主信息一致)，符合就继续走正常文件关闭流程；如果不符合就是检测到异常，根据设置，调用对应的异常处理。
tag由两部分组成，最高位的8-bit构成type，后面的56-bit构成value。
type，标识fd通过何种封装形式进行管理，例如 FDSAN_OWNER_TYPE_FILE就表示fd通过普通文件进行管理，type类型在 fdsan_owner_type进行定义。
value，则用于标识实际的owner tag。
tag构成图示
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.85184338128190403097112101194771:50001231000000:2800:9E2FB0EFFAEF44180589206D068DC9241C2584D63A30AC603E3F38B779C911BF.png)
3. 接口说明
fdsan_set_error_level
描述：可以通过fdsan_set_error_level设定error_level，error_level用于控制检测到异常后的处理行为。默认error_level为FDSAN_ERROR_LEVEL_WARN_ALWAYS。
参数：fdsan_error_level
| 名称 | 说明 |
| --- | --- |
| FDSAN_ERROR_LEVEL_DISABLED | disabled，此level代表什么都不处理。 |
| FDSAN_ERROR_LEVEL_WARN_ONCE | warn-once，第一次出现错误时在hilog中发出警告，然后将级别降低为disabled(FDSAN_ERROR_LEVEL_DISABLED)。 |
| FDSAN_ERROR_LEVEL_WARN_ALWAYS | warn-always，每次出现错误时都在hilog中发出警告。 |
| FDSAN_ERROR_LEVEL_FATAL | fatal，出现错误时调用abort异常退出。 |
返回值：返回旧的error_level。
fdsan_get_error_level
描述：可以通过fdsan_get_error_level获取error level。
返回值：当前的error_level。
fdsan_create_owner_tag
描述：通过传入的type和tag字段，拼接成一个有效的文件描述符的关闭tag。
参数：fdsan_owner_type
| 名称 | 说明 |
| --- | --- |
| FDSAN_OWNER_TYPE_GENERIC_00 | 默认未使用fd对应的type值 |
| FDSAN_OWNER_TYPE_GENERIC_FF | 默认非法fd对应的type值 |
| FDSAN_OWNER_TYPE_FILE | 默认普通文件对应的type值，使用fopen或fdopen打开的文件具有该类型 |
| FDSAN_OWNER_TYPE_DIRECTORY | 默认文件夹对应的type值，使用opendir或fdopendir打开的文件具有该类型 |
| FDSAN_OWNER_TYPE_UNIQUE_FD | 默认unique_fd对应的type值，保留暂未使用 |
| FDSAN_OWNER_TYPE_ZIPARCHIVE | 默认zip压缩文件对应的type值，保留暂未使用 |
返回值：返回创建的tag，可以用于fdsan_exchange_owner_tag函数的输入。
fdsan_exchange_owner_tag
描述：修改文件描述符的关闭tag。
通过fd所以找到对应的FdEntry，判断close_tag值与expected_tag是否一致，一致说明符合预期，可以用new_tag值重新设定对应的FdEntry。
如果不符合，则说明检测到了异常，后续则进行对应的异常处理。
参数：
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| fd | int | fd句柄，作为FdEntry的索引 |
| expected_tag | uint64_t | 期望的ownership tag值 |
| new_tag | uint64_t | 设置新的ownership tag值 |
fdsan_close_with_tag
描述：根据tag描述符关闭文件描述符。
通过fd找到匹配的FdEntry。如果close_tag与tag相同，则符合预期，可以继续执行文件描述符关闭流程，否则意味着检测到异常。
参数：
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| fd | int | 待关闭的fd句柄 |
| tag | uint64_t | 期望的ownership tag |
返回值：0或者-1，0表示close成功，-1表示close失败。
fdsan_get_owner_tag
描述：根据文件描述符获取tag信息。
通过fd找到匹配的FdEntry，并获取其对应的close_tag。
参数：
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| tag | uint64_t | ownership tag |
返回值：返回对应fd的tag。
fdsan_get_tag_type
描述：根据tag计算出对应的type类型。
通过获取到的tag信息，通过计算获取对应tag中的type信息。
参数：
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| tag | uint64_t | ownership tag |
返回值：返回对应tag的type。
fdsan_get_tag_value
描述：根据tag计算出对应的owner value。
通过获取到的tag信息，通过偏移计算获取对应tag中的value信息。
参数：
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| tag | uint64_t | ownership tag |
返回值：返回对应tag的value。
4. 使用示例
如何使用fdsan？这是一个简单的double-close问题：
上述代码中的good_write函数会打开一个文件并写入一些字符串而bad_close函数中也会打开一个文件同时包含double-close问题，这两个线程同时运行那么程序的执行情况会是这样的。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.18134768089166170608181378675273:50001231000000:2800:5F309D8F7544D678A3A3531C7C90DBF983A4B8A4ADC9283393C92FB6C8BA5066.png)
由于每次open返回的fd是顺序分配的，在进入主函数后第一个可用的fd是43，bad_close函数中第一次open返回的fd是43，在关闭之后，43就变成了可用的fd，在good_write函数中open返回了第一个可用的fd，即43，但是由于bad_close函数中存在double-close问题，因此错误的关闭了另一个线程中打开的文件，导致写入失败。
在fdsan引入之后，有两种方法可以检测这类问题：使用标准库接口或实现具有fdsan的函数接口。
使用标准库接口
标准库接口中fopen，fdopen，opendir，fdopendir都已经集成了fdsan，使用前述接口而非直接使用open可以帮助检测问题。在前述案例中可以使用fopen替代open：
日志信息
使用fopen打开的每个文件描述符都需要有一个与之对应的 tag 。fdsan 在 close 时会检查关闭的 fd 是否与 tag 匹配，不匹配就会默认提示相关日志信息。下面是上述代码的日志信息：
从这里的错误信息中可以看出FILE接口体的文件被其他人错误的关闭了，FILE接口体的地址可以协助进一步定位。
此外，可以在代码中使用fdsan_set_error_level设置错误等级error_level，设置为Fatal之后如果fdsan检测到错误会提示日志信息同时crash生成堆栈信息用于定位。下面是error_level设置为Fatal之后生成的crash堆栈信息：
此时，从crash信息中可以看到是bad_close中存在问题，同时crash中也包含了所有打开的文件，协助进行定位，提升效率。
```shell
OpenFiles:
0->/dev/null native object of unknown type 0
1->/dev/null native object of unknown type 0
2->/dev/null native object of unknown type 0
3->socket:[28102] native object of unknown type 0
4->socket:[28103] native object of unknown type 0
5->anon_inode:[eventpoll] native object of unknown type 0
6->/sys/kernel/debug/tracing/trace_marker native object of unknown type 0
7->anon_inode:[eventpoll] native object of unknown type 0
8->anon_inode:[eventpoll] native object of unknown type 0
9->/dev/console native object of unknown type 0
10->pipe:[95598] native object of unknown type 0
11->pipe:[95598] native object of unknown type 0
12->socket:[18542] native object of unknown type 0
13->pipe:[96594] native object of unknown type 0
14->socket:[18545] native object of unknown type 0
15->pipe:[96594] native object of unknown type 0
16->anon_inode:[eventfd] native object of unknown type 0
17->/dev/binder native object of unknown type 0
18->/data/storage/el1/bundle/entry.hap native object of unknown type 0
19->anon_inode:[eventpoll] native object of unknown type 0
20->anon_inode:[signalfd] native object of unknown type 0
21->socket:[29603] native object of unknown type 0
22->anon_inode:[eventfd] native object of unknown type 0
23->anon_inode:[eventpoll] native object of unknown type 0
24->anon_inode:[eventfd] native object of unknown type 0
25->anon_inode:[eventpoll] native object of unknown type 0
26->anon_inode:[eventfd] native object of unknown type 0
27->anon_inode:[eventpoll] native object of unknown type 0
28->anon_inode:[eventfd] native object of unknown type 0
29->anon_inode:[eventpoll] native object of unknown type 0
30->anon_inode:[eventfd] native object of unknown type 0
31->anon_inode:[eventpoll] native object of unknown type 0
32->anon_inode:[eventfd] native object of unknown type 0
33->anon_inode:[eventpoll] native object of unknown type 0
34->anon_inode:[eventfd] native object of unknown type 0
35->socket:[97409] native object of unknown type 0
36->socket:[94716] native object of unknown type 0
38->socket:[94720] native object of unknown type 0
40->/data/storage/el1/bundle/entry_test.hap native object of unknown type 0
41->socket:[95617] native object of unknown type 0
42->/sys/kernel/debug/tracing/trace_marker native object of unknown type 0
43->/dev/null FILE* 4155724704
44->socket:[94737] native object of unknown type 0
45->pipe:[95634] native object of unknown type 0
46->pipe:[95634] native object of unknown type 0
47->pipe:[95635] native object of unknown type 0
49->pipe:[95636] native object of unknown type 0
50->pipe:[95636] native object of unknown type 0
```
实现具有fdsan的函数接口
除了直接使用具有fdsan功能的标准库函数之外，还可以实现具有fdsan的函数接口。fdsan机制主要通过两个接口实现：fdsan_exchange_owner_tag和fdsan_close_with_tag，fdsan_exchange_owner_tag可以设置对应fd的tag，而fdsan_close_with_tag可以在关闭文件时检查对应的tag是否正确。
下面是一个具有fdsan的函数接口实现实例：
这里的实现中使用fdsan_exchange_owner_tag在开始时将fd与结构体对象地址绑定，然后在关闭文件时使用fdsan_close_with_tag进行检测，预期tag是结构体对象地址。
在实现了具有fdsan的函数接口之后，可以使用该接口包装fd：
此时运行该程序可以检测到另一个线程的double-close问题，详细信息可以参考日志。同样也可以设置error_level为fatal，这样可以使fdsan在检测到crash之后主动crash以获取更多信息。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/using-napi-interaction-with-cpp-V14
爬取时间: 2025-04-30 06:15:33
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/napi-introduction-V14
爬取时间: 2025-04-30 06:15:46
来源: Huawei Developer
场景介绍
HarmonyOS Node-API是基于Node.js 12.x LTS的Node-API规范扩展开发的机制，为开发者提供了ArkTS/JS与C/C++模块之间的交互能力。它提供了一组稳定的、跨平台的API，可以在不同的操作系统上使用。
本文中如无特别说明，后续均使用Node-API指代HarmonyOS Node-API能力。
HarmonyOS Node-API与Node.js 12.x LTS的Node-API规范的接口异同点，详见Node-API参考
一般情况下HarmonyOS应用开发使用ArkTS/JS语言，但部分场景由于性能、效率等要求，比如游戏、物理模拟等，需要依赖使用现有的C/C++库。Node-API规范封装了I/O、CPU密集型、OS底层等能力并对外暴露ArkTS/JS接口，从而实现ArkTS/JS和C/C++的交互。主要场景如下：
-  系统可以将框架层丰富的模块功能通过ArkTS/JS接口开放给上层应用。
-  应用开发者也可以选择将一些对性能、底层系统调用有要求的核心功能用C/C++封装实现，再通过ArkTS/JS接口使用，提高应用本身的执行效率。
Node-API的组成架构
图1Node-API的组成架构
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.78578232680274396965161429555496:50001231000000:2800:5CE705D8FA2D947AED6011166933BD6B791AA3E4A3D12CADC70F725A18F71913.png)
-  Native Module：开发者使用Node-API开发的模块，用于在ArkTS侧导入使用。
-  Node-API：实现ArkTS与C/C++交互的逻辑。
-  ModuleManager：Native模块管理，包括加载、查找等。
-  ScopeManager：管理napi_value的生命周期。
-  ReferenceManager：管理napi_ref的生命周期。
-  NativeEngine：ArkTS引擎抽象层，统一ArkTS引擎在Node-API层的接口行为。
-  ArkCompiler ArkTS Runtime：ArkTS运行时。
Node-API的关键交互流程
图2Node-API的关键交互流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165813.98294693256409137238697675507575:50001231000000:2800:AEBE3847A594938B1B67159FB87E483DE01C21F24F39B084ACAF65DCEE677E5A.png)
ArkTS和C++之间的交互流程，主要分为以下两步：
1.  初始化阶段：当ArkTS侧在import一个Native模块时，ArkTS引擎会调用ModuleManager加载模块对应的so及其依赖。首次加载时会触发模块的注册，将模块定义的方法属性挂载到exports对象上并返回该对象。
2.  调用阶段：当ArkTS侧通过上述import返回的对象调用方法时，ArkTS引擎会找到并调用对应的C/C++方法。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/napi-data-types-interfaces-V14
爬取时间: 2025-04-30 06:16:00
来源: Huawei Developer
Node-API的数据类型
napi_status
是一个枚举数据类型，表示Node-API接口返回的状态信息。
每当调用一个Node-API函数，都会返回该值，表示操作成功与否的相关信息。
napi_extended_error_info
一个结构体，在调用函数不成功时存储了较为详细的错误信息。
napi_value
napi_value是一个C的结构体指针，表示一个JavaScript对象的引用。napi_value持有了JS对象，同时，napi_value受handle_scope管理，scope中napi_value持有的JS对象不会被释放；出scope后，napi_value将失效，不再持有对应的JS对象。
napi_env
-  用于表示Node-API执行时的上下文，Native侧函数入参，并传递给函数中的Node-API接口。
-  napi_env与JS线程绑定，JS线程退出后，napi_env将失效。
-  禁止缓存napi_env，禁止在不同Worker中传递napi_env。
napi_threadsafe_function
napi_threadsafe_function用来创建一个线程安全的JavaScript函数，可以在不同的线程中调用。可以用于将异步操作的结果传递给JavaScript环境，例如从另一个线程中读取数据或执行计算密集型操作。此外，它还可以用于从JavaScript环境中调用C++代码中的函数，以便在另一个线程中执行。通过使用napi_threadsafe_function，可以实现JavaScript和C++之间的高效通信，同时保持线程安全性。
napi_threadsafe_function_release_mode
该枚举类型定义了两个常量，用于指定在何时释放线程安全函数的回调函数。
该值会传给napi_release_threadsafe_function。
-  mode值为napi_tsfn_release时：表示当前线程不再调用此tsfn。
-  mode值为napi_tsfn_abort时：表示除了当前线程，其他线程不能再调用此tsfn。 如果设置为napi_tsfn_abort，利用napi_call_threadsafe_function接口调用此tsfn时将返回napi_closing，tsfn函数并不会被放入queue中。
napi_threadsafe_function_call_mode
该枚举类型定义了两个常量，用于指定线程安全函数的调用模式。
数据结构如下所示：
-  napi_tsfn_nonblocking：napi_call_threadsafe_function是非阻塞的，如果队列已满，则返回napi_queue_full，从而阻止数据添加到队列中。
-  napi_tsfn_blocking：napi_call_threadsafe_function是阻塞的，直至队列中有空间可用。
内存管理类型
Node-API包含以下内存管理类型：
napi_handle_scope
napi_handle_scope数据类型是用来管理JavaScript对象的生命周期的。它允许JavaScript对象在一定范围内保持活动状态，以便在JavaScript代码中使用。在创建napi_handle_scope时，所有在该范围内创建的JavaScript对象都会保持活动状态，直到结束。这样可以避免在JavaScript代码中使用已经被释放的对象，从而提高代码的可靠性和性能。
napi_escapable_handle_scope
-  由napi_open_escapable_handle_scope接口创建，由napi_close_escapable_handle_scope接口关闭。
-  表示一种特殊类型的句柄范围，用于将在escapable_handle_scope范围内创建的值返回给父scope。
-  用于napi_escape_handle接口，将escape_handle_scope提升到JS对象，以便在外部作用域使用。
napi_ref
指向napi_value，允许用户管理JavaScript值的生命周期。
napi_type_tag
该结构体定义了一个包含两个无符号64位整数的类型标签，用于标识一个Node-API值的类型信息。
-  存储了两个无符号64位整数的128位值，用它来标记JavaScript对象，确保它们属于某种类型。
-  比napi_instanceof更强的类型检查，如果对象的原型被操纵，napi_instanceof可能会报告误报。
-  type_tag与napi_wrap结合非常有用，因为它确保从包装对象检索的指针可以安全地转换为与先前应用于JavaScript对象的类型标记相对应的Native类型。
napi_async_cleanup_hook_handle
napi_async_cleanup_hook_handle用于注册异步操作的回调函数。它主要用于在异步操作完成或被取消时执行清理操作，例如释放资源或撤销操作。使用napi_async_cleanup_hook_handle可以确保在异步操作完成或被取消时，相关资源得到正确的释放和清理，从而避免内存泄漏等问题。
回调类型
Node-API包含以下回调类型：
napi_callback_info
Native侧获取JS侧参数信息，传递给napi_get_cb_info，用于获取JS侧入参信息。
napi_callback
表示用户定义的Native函数，暴露给JavaScript，即JS侧调用的接口；一般不在此callback中创建handle或者callback scope。
基本用法如下：
napi_finalize
函数指针，用于传入napi_create_threadsafe_function和napi_set_instance_data接口。napi_finalize在对象被回收时会被调用。
napi_async_execute_callback
函数指针，用于napi_create_async_work接口。
-  异步执行的Native函数，从工作池线程调用，可与主事件循环线程并行执行。
-  函数实现中必须避免执行JavaScript或与JavaScript对象交互的Node-API调用。
-  Node-API调用可以在napi_async_complete_callback中执行。
napi_async_complete_callback
napi_async_complete_callback用于异步操作完成后的回调。当需要进行异步操作时，可以使用napi_create_async_work函数创建一个异步操作任务，并指定一个napi_async_complete_callback回调函数，在异步操作完成后会自动调用该回调函数，以便进行后续的处理。该回调函数的参数包括当前异步操作任务的状态和返回值等信息，可以根据这些信息进行相应的处理。
napi_threadsafe_function_call_js
函数指针，在主线程中与独立线程中的JavaScript代码进行交互，从而实现更加复杂的功能，用于napi_create_threadsafe_function(napi_env env,…,napi_threadsafe_function_call_js call_js_cb,...)接口。
napi_cleanup_hook
函数指针，用于napi_add_env_cleanup_hook接口，当环境销毁时会被执行。
napi_async_cleanup_hook
函数指针，用于napi_add_async_cleanup_hook接口，当环境销毁时会被执行。
调度优先级
QoS决定了线程调度的优先级，等级定义如下：
| QoS等级 | 适用场景 |
| --- | --- |
| napi_qos_background | 低等级，用户不可见任务，例如数据同步、备份。 |
| napi_qos_utility | 中低等级，不需要立即看到响应效果的任务，例如下载或导入数据。 |
| napi_qos_default | 默认。 |
| napi_qos_user_initiated | 高等级，用户触发并且可见进展，例如打开文档。 |
事件循环模式
napi提供了运行底层事件循环的两种模式, 其定义如下：
| 事件循环运行模式 | 解释说明 |
| --- | --- |
| napi_event_mode_default | 阻塞式的运行底层事件循环，直到循环中没有任何任务时退出事件循环。 |
| napi_event_mode_nowait | 非阻塞式的运行底层事件循环，尝试去处理一个任务，处理完之后退出事件循环；如果事件循环中没有任务，立刻退出事件循环。 |
线程安全任务优先级
napi提供了线程安全任务的优先级, 底层任务队列中的任务会根据其优先级被依次执行, 优先级的定义如下：
| 任务优先级 | 解释说明 |
| --- | --- |
| napi_priority_immediate | 该优先级的级别最高。 |
| napi_priority_high | 该优先级的级别低于napi_priority_immediate。 |
| napi_priority_low | 该优先级的级别低于napi_priority_immediate和napi_priority_high。 |
| napi_priority_idle | 该优先级的级别最低。 |
支持的Node-API接口
Node-API接口在Node.js提供的原生模块基础上扩展，目前支持部分接口，具体可见下文。
异步安全线程相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_threadsafe_function | 创建线程安全函数。 |
| napi_get_threadsafe_function_context | 获取线程安全函数中的context。 |
| napi_call_threadsafe_function | 调用线程安全函数。 |
| napi_acquire_threadsafe_function | 指示线程安全函数可以开始使用。 |
| napi_release_threadsafe_function | 指示线程安全函数将停止使用。 |
| napi_ref_threadsafe_function | 指示在主线程上运行的事件循环在线程安全函数被销毁之前不应退出。 |
| napi_unref_threadsafe_function | 指示在主线程上运行的事件循环可能会在线程安全函数被销毁之前退出。 |
buffer相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_buffer | 创建并获取一个指定大小的JS Buffer。 |
| napi_create_buffer_copy | 创建并获取一个指定大小的JS Buffer，并以给定数据进行初始化。 |
| napi_create_external_buffer | 创建并获取一个指定大小的JS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 |
| napi_get_buffer_info | 获取JS Buffer底层data及其长度。 |
| napi_is_buffer | 判断给定JS value是否为Buffer对象。 |
| napi_create_external_arraybuffer | 分配一个附加有外部数据的JS ArrayBuffer。 |
string相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_string_utf16 | 通过UTF16编码的C字符串数据创建JS String。 |
| napi_get_value_string_utf16 | 获取给定JS vaule对应的UTF16编码的字符串。 |
| napi_create_string_latin1 | 通过ISO-8859-1编码的C字符串数据创建JS String。 |
| napi_create_string_utf8 | 通过UTF8编码的C字符串数据创建JS String。 |
| napi_get_value_string_latin1 | 获取给定JS vaule对应的ISO-8859-1编码的字符串。 |
| napi_get_value_string_utf8 | 获取给定JS vaule对应的UTF8编码的字符串。 |
date相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_date | 通过一个C的double数据创建JS Date。 |
| napi_get_date_value | 获取给定JS Date对应的C double值。 |
| napi_is_date | 判断给定JS value是否为JS Date对象。 |
arraybuffer相关
| 接口 | 功能说明 |
| --- | --- |
| napi_get_arraybuffer_info | 获取ArrayBuffer的底层data buffer及其长度。 |
| napi_is_arraybuffer | 判断给定JS value是否为ArrayBuffer。 |
| napi_detach_arraybuffer | 分离给定ArrayBuffer的底层数据。 |
| napi_is_detached_arraybuffer | 判断给定的ArrayBuffer是否已被分离。 |
| napi_create_arraybuffer | 创建并获取一个指定大小的JS ArrayBuffer。 |
module相关
| 接口 | 功能说明 |
| --- | --- |
| napi_module_register | native模块注册接口。 |
生命周期相关
| 接口 | 功能说明 |
| --- | --- |
| napi_open_handle_scope | 创建一个上下文环境使用。需要使用napi_close_handle_scope进行关闭。 |
| napi_close_handle_scope | 关闭传入的上下文环境，关闭后，全部在其中声明的引用都将被关闭。 |
| napi_open_escapable_handle_scope | 创建出一个可逃逸的handle scope，可将范围内声明的值返回到父作用域。需要使用napi_close_escapable_handle_scope进行关闭。 |
| napi_close_escapable_handle_scope | 关闭传入的可逃逸的handle scope。 |
| napi_escape_handle | 提升传入的JS Object的生命周期到其父作用域。 |
| napi_create_reference | 为Object创建一个reference，以延长其生命周期。调用者需要自己管理reference生命周期。 |
| napi_delete_reference | 删除传入的reference。 |
| napi_reference_ref | 增加传入的reference的引用计数，并获取新的计数。 |
| napi_reference_unref | 减少传入的reference的引用计数，并获取新的计数。 |
| napi_get_reference_value | 获取与reference相关联的JS Object。 |
| napi_add_finalizer | 当js Object中的对象被垃圾回收时调用注册的napi_finalize回调。 |
promise相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_promise | 创建一个promise对象。 |
| napi_resolve_deferred | 对promise关联的deferred对象进行resolve。 |
| napi_reject_deferred | 对promise关联的deferred对象进行reject。 |
| napi_is_promise | 判断给定napi_value是否为promise对象。 |
array相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_array | 创建并获取一个JS Array。 |
| napi_create_array_with_length | 创建并获取一个指定长度的JS Array。 |
| napi_get_array_length | 获取array的length。 |
| napi_is_array | 判断给定JS value是否为array。 |
| napi_set_element | 在给定Object的指定索引处，设置元素。 |
| napi_get_element | 获取给定Object指定索引处的元素。 |
| napi_has_element | 若给定Object的指定索引处拥有属性，获取该元素。 |
| napi_delete_element | 尝试删除给定Object的指定索引处的元素。 |
| napi_create_typedarray | 通过现有的ArrayBuffer创建一个JS TypeArray。 |
| napi_is_typedarray | 判断给定JS value是否为TypeArray。 |
| napi_get_typedarray_info | 获取给定TypedArray的各种属性。 |
| napi_create_dataview | 通过现有的ArrayBuffer创建一个JS DataView。 |
| napi_is_dataview | 判断给定JS value是否为DataView。 |
| napi_get_dataview_info | 获取给定DataView的各种属性。 |
primitive相关
| 接口 | 功能说明 |
| --- | --- |
| napi_get_boolean | 根据给定的C boolean值，获取JS Boolean对象。 |
| napi_get_global | 获取global对象。 |
| napi_get_null | 获取null对象。 |
| napi_get_undefined | 获取undefined对象。 |
| napi_coerce_to_bool | 将给定的JS value强转成JS Boolean。 |
| napi_coerce_to_number | 将给定的JS value强转成JS Number。 |
| napi_coerce_to_object | 将给定的JS value强转成JS Object。 |
| napi_coerce_to_string | 将给定的JS value强转成JS String。 |
class相关
| 接口 | 功能说明 |
| --- | --- |
| napi_new_instance | 通过给定的构造函数，构建一个实例。 |
| napi_get_new_target | 获取构造函数调用的new.target。 |
| napi_define_class | 定义与C++类相对应的JavaScript类。 |
| napi_wrap | 在ArkTS对象上绑定一个Node-API模块对象实例。这个函数通常在将Node-API模块对象与ArkTS对象进行绑定时使用，以便在ArkTS中使用本地对象的方法和属性。 |
| napi_unwrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例。 |
| napi_remove_wrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例，并解除绑定。 |
object相关
| 接口 | 功能说明 |
| --- | --- |
| napi_get_prototype | 获取给定JS Object的prototype。 |
| napi_create_object | 创建一个默认的JS Object。 |
| napi_object_freeze | 冻结给定的对象。 |
| napi_object_seal | 密封给定的对象。 |
| napi_typeof | 获取给定JS value的JS Type。 |
| napi_instanceof | 判断给定object是否为给定constructor的实例。 |
| napi_type_tag_object | 将tag指针的值与Object关联。 |
| napi_check_object_type_tag | 判断给定的tag指针是否被关联到了JS Object上。 |
| napi_create_symbol | 创建一个JS Symbol对象。 |
| napi_create_external | 用于创建一个JS外部对象，该对象可以用于将C/C++中的自定义数据结构或对象传递到JS中，并且可以在JS中访问其属性和方法。 |
| napi_get_value_external | 用于获得napi_create_external创建的绑定了外部数据的JS值，此函数可以在JS和C/C++之间传递数据。 |
基本数据类型相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_int32 | 通过一个C的int32数据创建JS number。 |
| napi_create_uint32 | 通过一个C的uint32数据创建JS number。 |
| napi_create_int64 | 通过一个C的int64数据创建JS number。 |
| napi_create_double | 通过一个C的double数据创建JS number。 |
| napi_get_value_int32 | 获取给定JS number对应的C int32值。 |
| napi_get_value_uint32 | 获取给定JS number对应的C uint32值。 |
| napi_get_value_int64 | 获取给定JS number对应的C int64值。 |
| napi_get_value_double | 获取给定JS number对应的C double值。 |
| napi_get_value_bool | 获取给定js Boolean对应的C bool值。 |
bigint相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_bigint_int64 | 通过一个C的int64数据创建JS BigInt。 |
| napi_create_bigint_uint64 | 通过一个C的uint64数据创建JS BigInt。 |
| napi_create_bigint_words | 通过一个C的uint64数组创建单个JS BigInt。 |
| napi_get_value_bigint_int64 | 获取给定JS BigInt对应的C int64值。 |
| napi_get_value_bigint_uint64 | 获取给定JS BigInt对应的C uint64值。 |
| napi_get_value_bigint_words | 获取给定JS BigInt对应的信息，包括符号位、64位小端序数组和数组中的元素个数。 |
异常和错误相关
| 接口 | 功能说明 |
| --- | --- |
| napi_throw | 抛出一个JS value。 |
| napi_throw_error | 用于抛出一个带文本信息的ArkTS Error。 |
| napi_throw_type_error | 抛出一个带文本信息的JS TypeError。 |
| napi_throw_range_error | 抛出一个带文本信息的JS RangeError。 |
| napi_is_error | 判断napi_value是否表示为一个error对象。 |
| napi_create_error | 创建并获取一个带文本信息的JS Error。 |
| napi_create_type_error | 创建并获取一个带文本信息的JS TypeError。 |
| napi_create_range_error | 创建并获取一个带文本信息的JS RangeError。 |
| napi_get_and_clear_last_exception | 获取并清除最近一次出现的异常。 |
| napi_is_exception_pending | 判断是否出现了异常。 |
| napi_fatal_error | 引发致命错误以立即终止进程。 |
| napi_get_last_error_info | 获取napi_extended_error_info结构体，其中包含最近一次出现的error信息。 |
| napi_fatal_exception | 抛出一个致命异常并终止进程, 同时产生相应的crash日志。 |
属性相关
| 接口 | 功能说明 |
| --- | --- |
| napi_get_property_names | 以字符串数组的形式获取对象的可枚举属性的名称。 |
| napi_set_property | 对给定Object设置属性。 |
| napi_get_property | 获取给定Object的给定属性。 |
| napi_has_property | 判断给定对象中是否存在给定属性。 |
| napi_delete_property | 尝试从给定Object中删除给定key属性。 |
| napi_has_own_property | 判断给定Object中是否有名为key的own property。 |
| napi_set_named_property | 对给定Object设置一个给定名称的属性。 |
| napi_get_named_property | 获取给定Object中指定名称的属性。 |
| napi_has_named_property | 判断给定Object中是否有给定名称的属性。 |
| napi_define_properties | 批量的向给定Object中定义属性。 |
| napi_get_all_property_names | 获取一个数组，其中包含此对象过滤后的属性名称。 |
异步任务相关
| 接口 | 功能说明 |
| --- | --- |
| napi_create_async_work | 创建一个异步工作对象。 |
| napi_delete_async_work | 释放先前创建的异步工作对象。 |
| napi_queue_async_work | 将异步工作对象加到队列，由底层去调度执行。 |
| napi_cancel_async_work | 取消入队的异步任务。 |
自定义异步操作
| 接口 | 功能说明 |
| --- | --- |
| napi_async_init | 创建一个异步资源上下文环境（不支持与async_hook相关能力）。 |
| napi_make_callback | 在异步资源上下文环境中回调JS函数（不支持与async_hook相关能力）。 |
| napi_async_destroy | 销毁先前创建的异步资源上下文环境（不支持与async_hook相关能力）。 |
| napi_open_callback_scope | 创建一个回调作用域（不支持与async_hook相关能力）。 |
| napi_close_callback_scope | 关闭先前创建的回调作用域（不支持与async_hook相关能力）。 |
uv相关
| 接口 | 功能说明 |
| --- | --- |
| napi_get_uv_event_loop | 获取当前libuv loop实例。 |
函数调用
| 接口 | 功能说明 |
| --- | --- |
| napi_call_function | 在C/C++侧调用JS方法。 |
| napi_get_cb_info | 从给定的callback info中获取有关调用的详细信息，如参数和this指针。 |
扩展能力
Node-API组件扩展的符号列表
| 接口 | 功能说明 |
| --- | --- |
| napi_queue_async_work_with_qos | 将异步工作对象加到队列，由底层根据传入的qos优先级去调度执行。 |
| napi_run_script_path | 运行指定abc文件。 |
| napi_load_module | 将abc文件作为模块加载，返回模块的命名空间。 |
| napi_load_module_with_info | 将abc文件作为模块加载，返回模块的命名空间，可在新创建的ArkTS基础运行时环境中使用。 |
| napi_create_object_with_properties | 使用给定的napi_property_descriptor创建js Object。descriptor的键名必须为 string，且不可转为number。 |
| napi_create_object_with_named_properties | 使用给定的napi_value和键名创建js Object。键名必须为 string，且不可转为number。 |
| napi_coerce_to_native_binding_object | 强制将js Object和Native对象绑定。 |
| napi_create_ark_runtime | 创建基础运行时环境。 |
| napi_destroy_ark_runtime | 销毁基础运行时环境。 |
| napi_run_event_loop | 触发底层的事件循环。 |
| napi_stop_event_loop | 停止底层的事件循环。 |
| napi_serialize | 将ArkTS对象转换为native数据。 |
| napi_deserialize | 将native数据转为ArkTS对象。 |
| napi_delete_serialization_data | 删除序列化数据。 |
| napi_call_threadsafe_function_with_priority | 将指定优先级和入队方式的任务投递到ArkTS主线程。 |
| napi_is_sendable | 判断给定JS value是否是Sendable的。 |
| napi_define_sendable_class | 创建一个sendable类。 |
| napi_create_sendable_object_with_properties | 使用给定的napi_property_descriptor创建一个sendable对象。 |
| napi_create_sendable_array | 创建一个sendable数组。 |
| napi_create_sendable_array_with_length | 创建一个指定长度的sendable数组。 |
| napi_create_sendable_arraybuffer | 创建一个sendable ArrayBuffer。 |
| napi_create_sendable_typedarray | 创建一个sendable TypedArray。 |
| napi_wrap_sendable | 包裹一个native实例到ArkTS对象中。 |
| napi_wrap_sendable_with_size | 包裹一个native实例到ArkTS对象中并指定大小。 |
| napi_unwrap_sendable | 获取ArkTS对象包裹的native实例。 |
| napi_remove_wrap_sendable | 移除并获取ArkTS对象包裹的native实例。 |
napi_queue_async_work_with_qos
用法同napi_queue_async_work，但可以指定QoS等级。
napi_run_script_path
napi_load_module
napi_create_object_with_properties
napi_create_object_with_named_properties
napi_coerce_to_native_binding_object
napi_run_event_loop
napi_stop_event_loop
napi_serialize
napi_deserialize
napi_delete_serialization_data
napi_call_threadsafe_function_with_priority
napi_is_sendable
napi_define_sendable_class
napi_create_sendable_object_with_properties
napi_create_sendable_array
napi_create_sendable_array_with_length
napi_create_sendable_arraybuffer
napi_create_sendable_typedarray
napi_wrap_sendable
napi_wrap_sendable_with_size
napi_unwrap_sendable
napi_remove_wrap_sendable
环境生命周期
| 接口 | 功能说明 |
| --- | --- |
| napi_set_instance_data | 绑定与当前运行的环境相关联的数据项。 |
| napi_get_instance_data | 检索与当前运行的环境相关联的数据项。 |
对象生命周期管理
| 接口 | 功能说明 |
| --- | --- |
| napi_add_env_cleanup_hook | 注册环境清理钩子函数。 |
| napi_remove_env_cleanup_hook | 取消环境清理钩子函数。 |
| napi_add_async_cleanup_hook | 注册清理异步钩子函数。 |
| napi_remove_async_cleanup_hook | 取消清理异步钩子函数。 |
ArkTS基础运行时环境
| 接口 | 功能说明 |
| --- | --- |
| napi_create_ark_runtime | 创建基础运行时环境。 |
| napi_destroy_ark_runtime | 销毁基础运行时环境。 |
其他实用工具
| 接口 | 功能说明 |
| --- | --- |
| napi_get_version | 获取Node运行时支持的最高 NAPI 版本。 |
| node_api_get_module_file_name | 用于获取加载项加载位置的绝对路径。 |
| napi_strict_equals | 在某些情况下，希望确保两个值不仅具有相同的值，还具有相同的类型——例如正在处理一些需要特定类型的数据结构或算法——使用napi_strict_equals可以确保数据的一致性。 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/napi-guidelines-V14
爬取时间: 2025-04-30 06:16:13
来源: Huawei Developer
获取JS传入参数及其数量
【规则】当传入napi_get_cb_info的argv不为nullptr时，argv的长度必须大于等于传入argc声明的大小。
当argv不为nullptr时，napi_get_cb_info会根据argc声明的数量将JS实际传入的参数写入argv。如果argc小于等于实际JS传入参数的数量，该接口仅会将声明的argc数量的参数写入argv；而当argc大于实际参数数量时，该接口会在argv的尾部填充undefined。
错误示例
正确示例
生命周期管理
【规则】合理使用napi_open_handle_scope和napi_close_handle_scope管理napi_value的生命周期，做到生命周期最小化，避免发生内存泄漏问题。
每个napi_value属于特定的HandleScope，HandleScope通过napi_open_handle_scope和napi_close_handle_scope来建立和关闭，HandleScope关闭后，所属的napi_value就会自动释放。
正确示例：
上下文敏感
【规则】多引擎实例场景下，禁止通过Node-API跨引擎实例访问JS对象。
引擎实例是一个独立运行环境，JS对象创建访问等操作必须在同一个引擎实例中进行。若在不同引擎实例中操作同一个对象，可能会引发程序崩溃。引擎实例在接口中体现为napi_env。
错误示例：
所有的JS对象都隶属于具体的某一napi_env，不可将env1的对象，设置到env2中的对象中。在env2中一旦访问到env1的对象，程序可能会发生崩溃。
异常处理
【建议】Node-API接口调用发生异常需要及时处理，不能遗漏异常到后续逻辑，否则程序可能发生不可预期行为。
正确示例：
如上示例中，步骤1或者步骤2出现异常时，步骤3都不会正常进行。只有当方法的返回值是napi_ok时，才能保持继续正常运行；否则后续流程可能会出现不可预期的行为。
异步任务
【规则】当使用uv_queue_work方法将任务抛到JS线程上面执行的时候，对JS线程的回调方法，一般情况下需要加上napi_handle_scope来管理回调方法创建的napi_value的生命周期。
使用uv_queue_work方法，不会走Node-API框架，此时需要开发者自己合理使用napi_handle_scope来管理napi_value的生命周期。
本规则旨在强调napi_value生命周期情况，若只想往JS线程抛任务，不推荐使用uv_queue_work方法。如有抛任务的需要，请使用napi_threadsafe_function系列接口。
正确示例：
对象绑定
【规则】使用napi_wrap接口，如果最后一个参数result传递不为nullptr，需要开发者在合适的时机调用napi_remove_wrap函数主动删除创建的napi_ref。
napi_wrap接口定义如下：
当最后一个参数result不为空时，框架会创建一个napi_ref对象，指向js_object。此时开发者需要自己管理js_object的生命周期，即需要在合适的时机调用napi_remove_wrap删除napi_ref，这样GC才能正常释放js_object，从而触发绑定C++对象native_object的析构函数finalize_cb。
一般情况下，根据业务情况最后一个参数result可以直接传递为nullptr。
正确示例：
高性能数组
【建议】存储值类型数据时，使用ArrayBuffer代替JSArray来提高应用性能。
使用JSArray作为容器储存数据，支持几乎所有的JS数据类型。
使用napi_set_element方法对JSArray存储值类型数据（如int32）时，同样会涉及到与运行时的交互，造成不必要的开销。
ArrayBuffer进行增改是直接对缓冲区进行更改，具有远优于使用napi_set_element操作JSArray的性能表现。
因此此种场景下，更推荐使用napi_create_arraybuffer接口创建的ArrayBuffer对象。
示例：
napi_create_arraybuffer等同于JS代码中的new ArrayBuffer(size)，其生成的对象不可直接在TS/JS中进行读取，需要将其包装为TyppedArray或DataView后方可进行读写。
基准性能测试结果如下：
以下数据为千次循环写入累计数据，为更好的体现出差异，已对设备核心频率进行限制。
| 容器类型 | Benchmark数据（us） |
| --- | --- |
| JSArray | 1566.174 |
| ArrayBuffer | 3.609 |
数据转换
【建议】尽可能的减少数据转换次数，避免不必要的复制。
模块注册与模块命名
【规则】
nm_register_func对应的函数需要加上修饰符static，防止与其他so里的符号冲突。
模块注册的入口，即使用__attribute__((constructor))修饰函数的函数名需要确保与其他模块不同。
模块实现中.nm_modname字段需要与模块名完全匹配，区分大小写。
错误示例
以下代码为模块名为nativerender时的错误示例
正确示例：
以下代码为模块名为nativerender时的正确示例
正确的使用napi_create_external系列接口创建的JS Object
【规则】napi_create_external系列接口创建出来的JS对象仅允许在当前线程传递和使用，跨线程传递（如使用worker的post_message）将会导致应用crash。若需跨线程传递绑定有Native对象的JS对象，请使用napi_coerce_to_native_binding_object接口绑定JS对象和Native对象。
错误示例
```typescript
// index.d.ts
export const createMyExternal: () => Object;
// 应用代码
import testNapi from 'libentry.so';
import worker from '@ohos.worker';
const mWorker = new worker.ThreadWorker('../workers/Worker');
{
const mExternalObj = testNapi.createMyExternal();
mWorker.postMessage(mExternalObj);
}
// 关闭worker线程
// 应用可能在此步骤崩溃, 或在后续引擎进行GC的时候崩溃
mWorker.terminate();
// Worker的实现为默认模板，此处省略
```
防止重复释放获取的buffer
【规则】使用napi_get_arraybuffer_info等接口，参数data资源开发者不允许释放，data的生命周期受引擎管理。
这里以napi_get_arraybuffer_info为例，该接口定义如下：
data获取的是ArrayBuffer的Buffer头指针，开发者只可以在范围内读写该Buffer区域，不可以进行释放操作。该段内存由引擎内部的ArrayBuffer Allocator管理，随JS对象ArrayBuffer的生命周期释放。
错误示例：
| Node-API中受当前规则约束的接口有： |
| --- |
| napi_create_arraybuffer |
| napi_create_sendable_arraybuffer |
| napi_get_arraybuffer_info |
| napi_create_buffer |
| napi_get_buffer_info |
| napi_get_typedarray_info |
| napi_get_dataview_info |
其他
【建议】合理使用napi_object_freeze和napi_object_seal来控制对象以及对象属性的可变性。
napi_object_freeze等同于Object.freeze语义，freeze后对象的所有属性都不可能以任何方式被修改；napi_object_seal等同于Object.seal语义，对象不可增删属性。两者的主要区别是，freeze不能改属性的值，seal还可以改属性的值。
开发者使用以上语义时，需确保约束条件是自己需要的，一旦违背以上语义严格模式下就会抛出Error（默认严格模式）。
参考文档
Native侧子线程与UI主线程通信开发;
如何在Native侧C++子线程直接调用ArkTS接口，不用通过ArkTS侧触发回调;
napi_env、napi_value实例是否可以跨worker线程共享;
Native如何创建子线程，有什么约束，与主线程如何通信.

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-process-V14
爬取时间: 2025-04-30 06:16:27
来源: Huawei Developer
使用Node-API实现跨语言交互，首先需要按照Node-API的机制实现模块的注册和加载等相关动作。
-  ArkTS/JS侧：实现C++方法的调用。代码比较简单，import一个对应的so库后，即可调用C++方法。
-  Native侧：.cpp文件，实现模块的注册。需要提供注册lib库的名称，并在注册回调方法中定义接口的映射关系，即Native方法及对应的JS/ArkTS接口名称等。
此处以在ArkTS/JS侧实现add()接口、在Native侧实现Add()接口，从而实现跨语言交互为例，呈现使用Node-API进行跨语言交互的流程。
创建Native C++工程
-  在DevEco Studio中New > Create Project，选择Native C++模板，点击Next，选择API版本，设置好工程名称，点击Finish，创建得到新工程。
-  创建工程后工程结构可以分两部分，cpp部分和ets部分，工程结构具体介绍可见C++工程目录结构。
Native侧方法的实现
-  设置模块注册信息 ArkTS侧import native模块时，会加载其对应的so。加载so时，首先会调用napi_module_register方法，将模块注册到系统中，并调用模块初始化函数。 napi_module有两个关键属性：一个是.nm_register_func，定义模块初始化函数；另一个是.nm_modname，定义模块的名称，也就是ArkTS侧引入的so库的名称，模块系统会根据此名称来区分不同的so。
注：以上代码无须复制，创建Native C++工程以后在napi_init.cpp代码中已配置好。
-  模块初始化 实现ArkTS接口与C++接口的绑定和映射。
-  在index.d.ts文件中，提供JS侧的接口方法。
```typescript
// entry/src/main/cpp/types/libentry/index.d.ts
export const callNative: (a: number, b: number) => number;
export const nativeCallArkTS: (cb: (a: number) => number) => number;
```
-  在oh-package.json5文件中将index.d.ts与cpp文件关联起来。
-  在CMakeLists.txt文件中配置CMake打包参数。
-  实现Native侧的CallNative以及NativeCallArkTS接口。具体代码如下：
ArkTS侧调用C/C++方法实现
ArkTS侧通过import引入Native侧包含处理逻辑的so来使用C/C++的方法。
```typescript
// entry/src/main/ets/pages/Index.ets
// 通过import的方式，引入Native能力。
import nativeModule from 'libentry.so'
@Entry
@Component
struct Index {
@State message: string = 'Test Node-API callNative result: ';
@State message2: string = 'Test Node-API nativeCallArkTS result: ';
build() {
Row() {
Column() {
// 第一个按钮，调用add方法，对应到Native侧的CallNative方法，进行两数相加。
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
this.message += nativeModule.callNative(2, 3);
})
// 第二个按钮，调用nativeCallArkTS方法，对应到Native的NativeCallArkTS，在Native调用ArkTS function。
Text(this.message2)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
this.message2 += nativeModule.nativeCallArkTS((a: number)=> {
return a * 2;
});
})
}
.width('100%')
}
.height('100%')
}
}
```
Node-API的约束限制
SO命名规则
导入使用的模块名和注册时的模块名大小写保持一致，如模块名为entry，则so的名字为libentry.so，napi_module中nm_modname字段应为entry，ArkTS侧使用时写作：import xxx from 'libentry.so'。
注册建议
-  nm_register_func对应的函数（如上述Init函数）需要加上static，防止与其他so里的符号冲突。
-  模块注册的入口，即使用__attribute__((constructor))修饰的函数的函数名（如上述RegisterDemoModule函数）需要确保不与其它模块重复。
多线程限制
每个引擎实例对应一个JS线程，实例上的对象不能跨线程操作，否则会引起应用crash。使用时需要遵循如下原则：
-  Node-API接口只能在JS线程使用。
-  Native接口入参env与特定JS线程绑定只能在创建时的线程使用。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/napi-use-V14
爬取时间: 2025-04-30 06:16:40
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-extension-V14
爬取时间: 2025-04-30 06:16:54
来源: Huawei Developer
简介
扩展能力接口进一步扩展了Node-API的功能，提供了一些额外的接口，用于在Node-API模块中与ArkTS进行更灵活的交互和定制，这些接口可以用于创建自定义ArkTS对象等场景。
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
模块加载
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_load_module | 用于在Node-API模块中将abc文件作为模块加载，返回模块的命名空间，适用于需要在运行时动态加载模块或资源的应用程序，从而实现灵活的扩展和定制。 |
| napi_load_module_with_info | 用于在Node-API中进行模块的加载，当模块加载出来之后，可以使用函数napi_get_property获取模块导出的变量，也可以使用napi_get_named_property获取模块导出的函数，该函数可以在新创建的ArkTS基础运行时环境中使用。 |
| napi_module_register | 有些功能可能需要通过Node-API模块来实现以获得更好的性能，通过将这些功能实现为自定义模块并注册到ArkTS环境中，可以在一定程度上提高整体的性能。 |
使用示例
napi_load_module
使用Node-API接口在主线程中进行模块加载
napi_load_module_with_info
使用Node-API接口进行模块加载
napi_module_register
在ArkTS代码环境中使用Node-API模块编写的代码来实现特定的功能，可以将这部分功能封装成自定义模块，然后通过napi_module_register将其注册到ArkTS代码环境中，以实现功能的扩展和复用。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const add: (a: number, b: number) => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API 2 + 3 = %{public}d', testNapi.add(2, 3));
```
ArkTS Object相关
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_create_object_with_properties | 用于在Node-API模块中使用给定的napi_property_descriptor创建ArkTS Object。descriptor的键名必须为string，且不可转为number。 |
| napi_create_object_with_named_properties | 用于在Node-API模块中使用给定的napi_value和键名创建ArkTS Object。键名必须为string，且不可转为number。 |
使用示例
napi_create_object_with_properties
用给定的napi_property_descriptor作为属性去创建一个ArkTS对象，并且descriptor的键名必须为string，且不可转为number。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createObjectWithProperties: (data: string) => Object;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.createObjectWithProperties('createObject');
hilog.info(0x0000, 'testTag', 'Node-API napi_create_object_with_properties:%{public}s', JSON.stringify(value));
```
napi_create_object_with_named_properties
用于使用给定的napi_value和键名创建一个ArkTS对象，并且给定的键名必须为string，且不可转为number。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createObjectWithNameProperties: (data: string) => string | { name: string };
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.createObjectWithNameProperties('ls');
hilog.info(0x0000, 'testTag', 'Node-API napi_create_object_with_named_properties:%{public}s', JSON.stringify(value));
```
运行指定abc文件
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_run_script_path | 用于在Node-API模块中运行指定abc文件。 |
使用示例
napi_run_script_path
在Node-API模块中运行abc文件。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const runScriptPath: () => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
// 在此处执行错误返回false，成功就返回true
hilog.info(0x0000, 'testTag', 'Test Node-API napi_run_script_path: %{public}s', testNapi.runScriptPath());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_run_script_path errorMessage: %{public}s', error.message);
}
```
test.js代码，将js代码编成.abc文件，步骤如下：
放入指定路径中：/entry/resources/rawfile
异步工作对象加入队列并指定优先级
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_queue_async_work_with_qos | 用于将异步工作对象加入队列，让开发者能够根据QoS优先级来管理和调度异步工作的执行，从而更好地满足程序的性能和响应需求。 |
使用示例
napi_queue_async_work_with_qos
将异步工作对象加到队列，由底层根据传入的qos优先级去调度执行。
给ArkTS对象绑定回调和回调所需的参数
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_coerce_to_native_binding_object | 用于给ArkTS对象绑定回调和回调所需的参数，其作用是为了给ArkTS对象携带Native信息。 |
使用示例
napi_coerce_to_native_binding_object
用于给ArkTS Object绑定回调和回调所需的参数，给ArkTS Object携带Native信息。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getAddress: () => number;
export const getSetSize: () => number;
export const store: (a: number) => void;
export const erase: (a: number) => void;
export const clear: () => void;
```
ArkTS侧示例代码
```typescript
// index.ets
import testNapi from 'libentry.so';
import taskpool from '@ohos.taskpool';
@Concurrent
function getAddress() {
let address: number = testNapi.getAddress();
console.info("taskpool:: address is " + address);
}
@Concurrent
function store(a:number, b:number, c:number) {
let size:number = testNapi.getSetSize();
console.info("set size is " + size + " before store");
testNapi.store(a);
testNapi.store(b);
testNapi.store(c);
size = testNapi.getSetSize();
console.info("set size is " + size + " after store");
}
@Concurrent
function erase(a:number) {
let size:number = testNapi.getSetSize();
console.info("set size is " + size + " before erase");
testNapi.erase(a);
size = testNapi.getSetSize();
console.info("set size is " + size + " after erase");
}
@Concurrent
function clear() {
let size:number = testNapi.getSetSize();
console.info("set size is " + size + " before clear");
testNapi.clear();
size = testNapi.getSetSize();
console.info("set size is " + size + " after clear");
}
async function test01(): Promise<void> {
let address:number = testNapi.getAddress();
console.info("host thread address is " + address);
let task1 = new taskpool.Task(getAddress);
await taskpool.execute(task1);
let task2 = new taskpool.Task(store, 1, 2, 3);
await taskpool.execute(task2);
let task3 = new taskpool.Task(store, 4, 5, 6);
await taskpool.execute(task3);
let task4 = new taskpool.Task(erase, 3);
await taskpool.execute(task4);
let task5 = new taskpool.Task(erase, 5);
await taskpool.execute(task5);
let task6 = new taskpool.Task(clear);
await taskpool.execute(task6);
}
test01();
```
注意事项
对ArkTS对象A调用napi_coerce_to_native_binding_object将开发者实现的detach/attach回调和native对象信息加到A上，再将A跨线程传递。跨线程传递需要对A进行序列化和反序列化，在当前线程thread1序列化A得到数据data，序列化阶段执行detach回调。然后将data传给目标线程thread2，在thread2中反序列化data，执行attach回调，最终得到ArkTS对象A。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165814.25734857632567789798718574401436:50001231000000:2800:3FF6D289B2202B4EC7A00104160235BC5C35C89A28B17EEB0F768E144293FAEE.png)
事件循环
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_run_event_loop | 触发底层的事件循环。 |
| napi_stop_event_loop | 停止底层的事件循环。 |
使用示例
napi_run_event_loop、napi_stop_event_loop
使用扩展的Node-API接口在异步线程中运行和停止事件循环
ArkTS基础运行时环境
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_create_ark_runtime | 创建基础运行时环境。 |
| napi_destroy_ark_runtime | 销毁基础运行时环境。 |
使用示例
napi_create_ark_runtime、napi_destroy_ark_runtime
使用Node-API接口创建ArkTS运行时环境
序列化和反序列化
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_serialize | 将ArkTS对象转换为native数据。第一个参数env是接口执行的ArkTS环境；第二个参数object是待序列化的ArkTS对象；第三个参数transfer_list是存放需要以transfer传递的arrayBuffer的array，如不涉及可传undefined；第四个参数clone_list是存放需要克隆传递的Sendable对象的array，如不涉及可传undefined；第五个参数result是序列化结果。 |
| napi_deserialize | 将native数据转为ArkTS对象。第一个参数env是接口执行的ArkTS环境；第二个参数buffer是序列化数据；第三个参数object是反序列化得到的结果。 |
| napi_delete_serialization_data | 删除序列化数据。 |
使用示例
napi_serialize、napi_deserialize、napi_delete_serialization_data
用于将ArkTS对象转换为native数据、将native数据转为ArkTS对象、删除序列化数据等操作。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const aboutSerialize: (obj: Object) => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
class Obj {
numKey:number = 0;
}
let obj: Obj = { numKey: 500 };
hilog.info(0x0000, 'testTag', ' Node-API aboutSerialize: %{public}d', testNapi.aboutSerialize(obj));
```
根据任务指定的优先级和入队方式进行处理异步线程向ArkTS线程投递的任务
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_call_threadsafe_function_with_priority | 将指定优先级和入队方式的任务投递到ArkTS主线程。 |
使用示例
napi_call_threadsafe_function_with_priority
使用Node-API接口从异步线程向ArkTS线程投递指定优先级和入队方式的的任务
Sendable相关
接口描述
| 接口 | 描述 |
| --- | --- |
| napi_is_sendable | 判断给定ArkTS value是否是Sendable的。 |
| napi_define_sendable_class | 创建一个sendable类。 |
| napi_create_sendable_object_with_properties | 使用给定的napi_property_descriptor创建一个sendable对象。 |
| napi_create_sendable_array | 创建一个sendable数组。 |
| napi_create_sendable_array_with_length | 创建一个指定长度的sendable数组。 |
| napi_create_sendable_arraybuffer | 创建一个sendable ArrayBuffer。 |
| napi_create_sendable_typedarray | 创建一个sendable TypedArray。 |
| napi_wrap_sendable | 包裹一个native实例到ArkTS对象中。 |
| napi_wrap_sendable_with_size | 包裹一个native实例到ArkTS对象中并指定大小。 |
| napi_unwrap_sendable | 获取ArkTS对象包裹的native实例。 |
| napi_remove_wrap_sendable | 移除并获取ArkTS对象包裹的native实例。 |
使用示例
napi_is_sendable
判断给定ArkTS value是否是Sendable的。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isSendable: <T>(a: T) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.isSendable('createObject');
hilog.info(0x0000, 'testTag', 'Node-API napi_is_sendable: %{public}s', JSON.stringify(value));
```
napi_define_sendable_class
创建一个sendable类。
cpp部分代码
接口声明
```typescript
// index.d.ts
@Sendable
export class SendableClass {
static staticStr: string;
static staticFunc(): string;
str: string;
func(): string;
}
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = new testNapi.SendableClass();
hilog.info(0x0000, 'testTag', 'Node-API napi_define_sendable_class: %{public}s', value.str);
```
napi_create_sendable_object_with_properties
使用给定的napi_property_descriptor创建一个sendable对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getSendableObject: () => { x: true };
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.getSendableObject();
hilog.info(0x0000, 'testTag', 'Node-API napi_create_sendable_object_with_properties: %{public}s', JSON.stringify(value));
```
napi_create_sendable_array
创建一个sendable数组。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getSendableArray: () => [];
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.getSendableArray();
hilog.info(0x0000, 'testTag', 'Node-API napi_create_sendable_array: %{public}s', JSON.stringify(value));
```
napi_create_sendable_array_with_length
创建一个指定长度的sendable数组。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getSendableArrayWithLength: () => [];
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.getSendableArrayWithLength();
hilog.info(0x0000, 'testTag', 'Node-API napi_create_sendable_array_with_length: %{public}s', JSON.stringify(value.length));
```
napi_create_sendable_arraybuffer
创建一个sendable ArrayBuffer。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getSendableArrayBuffer: () => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
testNapi.getSendableArrayBuffer();
```
napi_create_sendable_typedarray
创建一个sendable TypedArray。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getSendableTypedArray: () => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
testNapi.getSendableTypedArray();
```
napi_wrap_sendable
包裹一个native实例到ArkTS对象中。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const wrapSendable: () => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
testNapi.wrapSendable();
```
napi_wrap_sendable_with_size
包裹一个native实例到ArkTS对象中并指定大小。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const wrapSendableWithSize: () => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
testNapi.wrapSendableWithSize();
```
napi_unwrap_sendable
获取ArkTS对象包裹的native实例。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const unwrapSendable: () => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
testNapi.unwrapSendable();
```
napi_remove_wrap_sendable
移除并获取ArkTS对象包裹的native实例。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const removeWrapSendable: () => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
testNapi.removeWrapSendable();
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-array-V14
爬取时间: 2025-04-30 06:17:08
来源: Huawei Developer
简介
使用Node-API接口进行array相关开发时，调用相关接口可以在Node-API模块中直接操作和处理ArkTS中的数组。
基本概念
使用Node-API接口进行数组（array）相关开发时，涉及的基本概念主要包括数组的创建、访问、修改、遍历以及与数组相关的操作。这些概念对于理解如何在Node-API模块中与ArkTS数组交互非常重要。以下是一些关键概念：
场景和功能介绍
使用Node-API接口进行数组相关开发时，可以处理各种涉及ArkTS数组的操作和交互场景。以下是几个具体的使用场景介绍：
| 接口 | 描述 |
| --- | --- |
| napi_create_array | 用于在Node-API模块中向ArkTS层创建一个ArkTS数组对象。 |
| napi_create_array_with_length | 用于在Node-API模块中向ArkTS层创建指定长度的ArkTS数组时。 |
| napi_get_array_length | 用于在Node-API模块中获取ArkTS数组对象的长度。 |
| napi_is_array | 用于在Node-API模块中判断一个napi_value值是否为数组。 |
| napi_set_element | 用于在Node-API模块中对ArkTS数组对象的特定索引处设置一个值。 |
| napi_get_element | 用于在Node-API模块中从ArkTS数组对象的特定索引处获取一个值。 |
| napi_has_element | 用于在Node-API模块中判断ArkTS数组对象请求索引处是否包含元素。 |
| napi_delete_element | 用于在Node-API模块中从ArkTS数组对象中删除请求索引对应的元素。 |
| napi_create_typedarray | 用于在Node-API模块中创建指定类型的TypedArray，例如Uint8Array、Int32Array等，通常用于将Node-API模块中的数据转换为ArkTS中的TypedArray，以便进行高性能的数据处理操作。 |
| napi_is_typedarray | 用于在Node-API模块中判断一个给定的napi_value是否为TypedArray对象。 |
| napi_get_typedarray_info | 用于在Node-API模块中获得某个TypedArray的各种属性。 |
| napi_create_dataview | 用于在Node-API模块中创建一个DataView对象，可以访问和操作二进制数据。 |
| napi_is_dataview | 用于在Node-API模块中判断给定的napi_value是否为ArkTS中的DataView对象。 |
| napi_get_dataview_info | 用于在Node-API模块中获得某个DataView的各种属性。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。具体使用见示例。
napi_create_array
用于在Node-API模块中创建一个ArkTS数组。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createArray: () => number[];
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_array:%{public}s', JSON.stringify(testNapi.createArray()));
```
napi_create_array_with_length
用于在Node-API模块中创建一个具有指定长度的ArkTS数组。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createArrayWithLength: (length: number) => void[];
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let array = testNapi.createArrayWithLength(6);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_array_with_length:%{public}d', array.length);
```
napi_get_array_length
获取给定array的长度。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getArrayLength: (arr: Array<any>) => number | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
const arr = [0, 1, 2, 3, 4, 5];
hilog.info(0x0000, 'testTag', 'Test Node-API get_array_length:%{public}d', testNapi.getArrayLength(arr));
```
napi_is_array
判断给定ArkTS值是否为数组。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isArray: <T>(data: Array<T> | T) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
let value = new Array<number>(1);
let data = "123";
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_array: %{public}s', testNapi.isArray<number>(value));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_array: %{public}s', testNapi.isArray<string>(data));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_array error: %{public}s', error.message);
}
```
napi_set_element
用于在ArkTS数组中设置指定索引位置的元素。
对于以索引值为键的object，可以使用napi_set_element来设置属性值。
cpp部分代码
接口声明
```typescript
export const napiSetElement: <T>(arr: Array<T>, index: number, value: T) => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let arr = [10, 20, 30];
testNapi.napiSetElement<number | string>(arr, 1, 'newElement');
testNapi.napiSetElement<number | string>(arr, 2, 50);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_element arr: %{public}s', arr.toString());
hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_element arr[3]: %{public}s', arr[3]);
interface MyObject {
first: number;
second: number;
}
let obj: MyObject = {
first: 1,
second: 2
};
testNapi.napiSetElement<number | string | Object>(arr, 4, obj);
let objAsString = JSON.stringify(arr[4]);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_element arr[4]: %{public}s', objAsString);
```
napi_get_element
用于从ArkTS数组中获取请求索引位置的元素值。请求索引值应在数组的有效范围内，如果索引超出数组长度，函数会返回undefined。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiGetElement: <T>(arr: Array<T>, index: number) => number | string | Object | boolean | undefined;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
interface MyObject {
first: number;
second: number;
}
let obj: MyObject = {
first: 1,
second: 2
};
let arr = [10, 'hello', null, obj];
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[0]: %{public}d', testNapi.napiGetElement<number | string | null | Object>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[1]: %{public}s', testNapi.napiGetElement<number | string | null | Object>(arr, 1));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[2]: %{public}s', testNapi.napiGetElement<number | string | null | Object>(arr, 2));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[3]: %{public}s', testNapi.napiGetElement<number | string | null | Object>(arr, 3));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[4]: %{public}s', JSON.stringify(testNapi.napiGetElement(arr, 4)));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[null]: %{public}s', testNapi.napiGetElement<number | string | null | Object>(arr, 5));
```
napi_has_element
用于判断ArkTS数组是否具有指定索引的元素。如果索引超出了对象的有效范围，函数返回false，表示没有元素。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiHasElement: <T>(arr: Array<T>, index: number) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let arr = [10, 'hello', null, 'world'];
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_element arr[0]: %{public}s', testNapi.napiHasElement<number | string | null>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_element arr[7]: %{public}s', testNapi.napiHasElement<number | string | null>(arr, 7));
```
napi_delete_element
用于从ArkTS数组对象中删除请求索引的元素。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiDeleteElement: <T>(arr: Array<T>, index: number) => boolean;
```
ArkTS侧示例代码
```typescript
// 需要同时导入前文示例代码中的napiHasElement、napiGetElement接口
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let arr = [10, 'hello', null, 'world'];
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_element arr[0]: %{public}s', testNapi.napiHasElement<number | string | null>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_delete_element arr[0]: %{public}s', testNapi.napiDeleteElement<number | string | null>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_element deleted arr[0]: %{public}s', testNapi.napiHasElement<number | string | null>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[0]: %{public}d', testNapi.napiGetElement<number | string | null>(arr, 0));
```
napi_create_typedarray
用于在Node-API模块中通过现有的ArrayBuffer创建指定类型的ArkTS TypedArray。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const enum TypedArrayTypes {
INT8_ARRAY = 0,
UINT8_ARRAY,
UINT8_CLAMPED_ARRAY,
INT16_ARRAY,
UINT16_ARRAY,
INT32_ARRAY,
UINT32_ARRAY,
FLOAT32_ARRAY,
FLOAT64_ARRAY,
BIGINT64_ARRAY,
BIGuINT64_ARRAY,
}
export const createTypedArray: <T>(type: TypedArrayTypes) => T;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 传递要创建的类型值
let typedArray = testNapi.createTypedArray<Int8Array>(testNapi.TypedArrayTypes["INT8_ARRAY"]);
if (typedArray instanceof Int8Array) {
hilog.info(0x0000, 'testTag', ' Node-API napi_create_typedarray: Int8Array');
}
let uint8Array = testNapi.createTypedArray<Uint8Array>(testNapi.TypedArrayTypes["UINT8_ARRAY"]);
if (uint8Array instanceof Uint8Array) {
hilog.info(0x0000, 'testTag', ' Node-API napi_create_typedarray: Uint8Array');
}
```
需要对use-napi-process.md中的模块初始化部分进行修改，具体见如下：
napi_is_typedarray
用于在Node-API模块中判断ArkTS侧给定的napi_value是否为TypedArray对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isTypedarray: (data: Object) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
let value = new Uint8Array([1, 2, 3, 4]);
let data = "123";
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_typedarray: %{public}s', testNapi.isTypedarray(value));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_typedarray: %{public}s', testNapi.isTypedarray(data));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_typedarray error: %{public}s', error.message);
}
```
napi_get_typedarray_info
获取给定TypedArray的各种属性。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getTypedarrayInfo: <T>(typeArray: T, infoType: number) => ArrayBuffer | number | boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 传入TypedArray类型数据。TypedArray是一种用来描述二进制数据的类数组数据视图，没有直接构造器，可以用其子类构造类数组
// TypedArray的子类有: Int8Array Uint8Array Uint8ClampedArray Int16Array Int32Array等
let int8Array = new Int8Array([15, 7]);
// 定义枚举类型 这些都是TypedArray的属性
enum InfoType {
TYPE = 1, // 传入的TypedArray的类型
LENGTH = 2, // 传入的TypedArray的长度
ARRAY_BUFFER = 3, // TypedArray下的ArrayBuffer
BYTE_OFFSET = 4 // 数组的第一个元素所在的基础原生数组中的字节偏移量
};
let arrbuff = testNapi.getTypedarrayInfo(int8Array, InfoType.ARRAY_BUFFER) as ArrayBuffer;
// 将arraybuffer转为数组
let arr = new Array(new Int8Array(arrbuff));
hilog.info(0x0000, 'Node-API', 'get_typedarray_info_arraybuffer: %{public}s', arr.toString());
hilog.info(0x0000, 'Node-API', 'get_typedarray_info_isIn8Array: %{public}s', testNapi.getTypedarrayInfo(int8Array, InfoType.TYPE).toString());
hilog.info(0x0000, 'Node-API', 'get_typedarray_info_length: %{public}d', testNapi.getTypedarrayInfo(int8Array, InfoType.LENGTH));
hilog.info(0x0000, 'Node-API', 'get_typedarray_info_byte_offset: %{public}d', testNapi.getTypedarrayInfo(int8Array, InfoType.BYTE_OFFSET));
```
napi_create_dataview
创建dataview对象，便于访问和操作二进制数据，需要提供一个指向二进制数据的缓冲区，并指定要包含的字节数。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createDataView: (arraybuffer:ArrayBuffer) => DataView | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
const arrayBuffer = new ArrayBuffer(16);
const dataView = testNapi.createDataView(arrayBuffer) as DataView;
hilog.info(0x0000, 'testTag', 'Test Node-API dataView：%{public}d', dataView.byteLength);
hilog.info(0x0000, 'testTag', 'Test Node-API dataView第一个数据：%{public}d', dataView.getInt8(0));
```
napi_is_dataview
用于在Node-API模块中判断ArkTS侧给定的napi_value是否为DataView。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isDataView: (date: DataView | string) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
let buffer = new ArrayBuffer(16);
let dataView = new DataView(buffer);
let data = "123";
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_dataview: %{public}s', testNapi.isDataView(dataView));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_dataview: %{public}s', testNapi.isDataView(data));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_dataview error: %{public}s', error.message);
}
```
napi_get_dataview_info
获取给定DataView的各种属性。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getDataViewInfo: (dataView: DataView, infoType: number) => ArrayBuffer | number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 创建一个ArrayBuffer
let arrayBuffer = new Int8Array([2, 5]).buffer;
// 使用arrayBuffer创建一个dataView
let dataView = new DataView(arrayBuffer);
// 定义一个枚举类型
enum InfoType {
BYTE_LENGTH = 0,
ARRAY_BUFFER = 1,
BYTE_OFFSET = 2,
};
// 传入DataView类型参数查询DataView的字节数
hilog.info(0x0000, 'Node-API', 'get_dataview_info_bytelength %{public}d', testNapi.getDataViewInfo(dataView, InfoType.BYTE_LENGTH));
// 传入DataView类型参数查询DataView的ArrayBuffer
let arrbuff = testNapi.getDataViewInfo(dataView, InfoType.ARRAY_BUFFER) as ArrayBuffer;
// 将arraybuffer转为数组
let arr = Array.from(new Int8Array(arrbuff));
hilog.info(0x0000, 'Node-API', 'get_dataview_info_arraybuffer %{public}s', arr.toString());
// 传入DataView类型参数查询DataView开始投影的数据缓冲区中的字节偏移量
hilog.info(0x0000, 'Node-API', 'get_dataview_info_byteoffset %{public}d', testNapi.getDataViewInfo(dataView, InfoType.BYTE_OFFSET));
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-arraybuffer-V14
爬取时间: 2025-04-30 06:17:21
来源: Huawei Developer
简介
ArrayBuffer是ArkTS中的一种数据类型，用于表示通用的、固定长度的原始二进制数据缓冲区。它提供了一种在ArkTS中有效地表示和操作原始二进制数据的方式。
基本概念
场景和功能介绍
以下Node-API接口通常在Node-API模块中操作ArrayBuffer类型的数据。以下是一些可能的使用场景：
| 接口 | 描述 |
| --- | --- |
| napi_is_arraybuffer | 检查一个值是否为ArrayBuffer，以确保正在处理正确的数据类型。需要注意的是，此函数只能判断一个值是否为ArrayBuffer，而不能判断一个值是否为TypedArray。如果需要判断一个值是否为TypedArray，可以使用napi_is_typedarray函数。 |
| napi_get_arraybuffer_info | 获取给定的ArrayBuffer对象的相关信息，包括数据指针和数据长度。 |
| napi_detach_arraybuffer | 在某些情况下，当需要频繁地访问ArrayBuffer的底层数据缓冲区时，将其分离可以提高性能。分离后可以直接在C/C++中操作数据，而无需通过Node-API接口进行数据访问。 |
| napi_is_detached_arraybuffer | 判断给定的ArrayBuffer是否已经被分离。 |
| napi_create_arraybuffer | 用于在Node-API模块中创建一个具有指定字节长度的ArkTS ArrayBuffer对象。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_is_arraybuffer
判断给定ArkTS value是否为ArrayBuffer。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isArrayBuffer: <T>(arrayBuffer: T) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
let value = new ArrayBuffer(1);
let data = "123";
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_arraybuffer: %{public}s', testNapi.isArrayBuffer(value));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_arraybuffer: %{public}s', testNapi.isArrayBuffer(data));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_arraybuffer error: %{public}s', error.message);
}
```
napi_get_arraybuffer_info
获取ArrayBuffer的底层数据缓冲区和长度。
cpp部分代码
接口声明
```typescript
// index.d.ts
export class ArrayBufferInfo {
byteLength: number;
buffer: Object;
}
export const getArrayBufferInfo: (data: ArrayBuffer) => ArrayBufferInfo | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
const buffer = new ArrayBuffer(10);
hilog.info(0x0000, 'testTag', 'Test Node-API get_arrayBuffer_info:%{public}s ', JSON.stringify(testNapi.getArrayBufferInfo(buffer)));
```
napi_detach_arraybuffer
分离给定ArrayBuffer的底层数据。
napi_is_detached_arraybuffer
判断给定的ArrayBuffer是否已被分离。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const detachedArrayBuffer: (buffer:ArrayBuffer) => ArrayBuffer;
export const isDetachedArrayBuffer: (arrayBuffer: ArrayBuffer) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
const bufferArray = new ArrayBuffer(8);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_detached_arraybuffer one: %{public}s', testNapi.isDetachedArrayBuffer(bufferArray));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_detached_arraybuffer two: %{public}s ', testNapi.isDetachedArrayBuffer(testNapi.detachedArrayBuffer(bufferArray)));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_detached_arraybuffer error: %{public}s', error.message);
}
```
napi_create_arraybuffer
用于在C/C++中创建一个具有指定字节长度的ArkTS ArrayBuffer对象，如果调用者想要直接操作缓冲区，则可以选择将底层缓冲区返回给调用者。要从ArkTS写入此缓冲区，需要创建类型化数组或DataView对象。
napi_create_arraybuffer在byte_length为0或超大值时，data返回值将为nullptr。因此在对data进行使用前，有必要对其进行判空。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createArrayBuffer: (size: number) => ArrayBuffer;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_arraybuffer:%{public}s', testNapi.createArrayBuffer(10).toString());
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-bigint-V14
爬取时间: 2025-04-30 06:17:35
来源: Huawei Developer
简介
BigInt是ArkTS中用于表示任意精度整数的数据类型，它能够处理比Number类型更大范围的整数值。通过Node-API提供的接口，可以在Node-API模块中创建、获取和操作BigInt类型值，从而实现与BigInt相关的功能扩展。
基本概念
在使用Node-API接口操作BigInt类型值时，需要理解以下基本概念：
场景和功能介绍
| 接口 | 描述 |
| --- | --- |
| napi_create_bigint_int64 | 用于创建64位带符号整数（int64）的BigInt对象的函数。 |
| napi_create_bigint_uint64 | 用于创建64位无符号整数（uint64）的BigInt对象的函数。 |
| napi_create_bigint_words | 用于根据提供的64位无符号（uint64）字节数据创建BigInt对象的函数。 |
| napi_get_value_bigint_int64 | 用于从BigInt对象中获取64位带符号整数（int64）值的函数。 |
| napi_get_value_bigint_uint64 | 用于从BigInt对象中获取64位无符号整数（uint64）值的函数。 |
| napi_get_value_bigint_words | 用于从BigInt对象中获取底层的64位无符号（uint64）字节数据。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_create_bigint_int64
这个函数用于在给定的Node-API环境中依据一个带有符号的64位整数创建一个ArkTS的BigInt对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createBigintInt64t: () => bigint;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_bigint_int64: %{public}d', testNapi.createBigintInt64t());
```
napi_create_bigint_uint64
这个函数用于在给定的Node-API环境中依据一个无符号的64位整数创建一个ArkTS的BigInt对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createBigintUint64t: () => bigint;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_bigint_uint64: %{public}d', testNapi.createBigintUint64t());
```
napi_create_bigint_words
这个函数用于在给定的Node-API环境中由一系列无符号64位整数创建一个ArkTS的BigInt对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createBigintWords: () => bigint | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_bigint_words: %{public}d', testNapi.createBigintWords());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
}
```
napi_get_value_bigint_int64
用于从传入的参数中提取64位整数的BigInt数据，以供后续处理。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueBigintInt64t: (bigInt64: bigint) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let bigInt = BigInt(-5555555555555555);
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_value_bigint_int64: %{public}s',
JSON.stringify(testNapi.getValueBigintInt64t(bigInt)));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
}
```
napi_get_value_bigint_uint64
用于从传入的参数中提取无符号64位整数的BigInt数据，以供后续处理。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueBigintUint64t: (bigUint64: bigint) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let bigUint = BigInt(5555555555555555);
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_value_bigint_uint64: %{public}s',
JSON.stringify(testNapi.getValueBigintUint64t(bigUint)));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
}
```
napi_get_value_bigint_words
用于获取ArkTS的BigInt对象底层的64位无符号（uint64）二进制字节数据。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueBigintWords: (bigIntWords: bigint) => bigint | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let bigInt = BigInt(-5555555555555555);
let bigUint = BigInt(5555555555555555);
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_value_bigint_words signBit is: %{public}d', testNapi.getValueBigintWords(bigInt));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_value_bigint_words signBit is: %{public}d', testNapi.getValueBigintWords(bigUint));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
}
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-buffer-V14
爬取时间: 2025-04-30 06:17:48
来源: Huawei Developer
简介
在ArkTS中，Buffer是一种用于处理二进制数据的数据类型。
基本概念
使用Node-API接口进行buffer相关开发时，使用Buffer对象与ArkTS代码之间进行二进制数据的有效交互，以便在Node-API模块创建、操纵和传递Buffer对象到ArkTS，从而处理和传递二进制数据，比如文件I/O、网络传输等。
场景和功能使用
以下这些接口用于有效地与ArkTS层进行交互，这使Node-API模块能够更好地处理ArkTS层的二进制数据，比如处理文件I/O、网络传输等操作：
| 接口 | 描述 |
| --- | --- |
| napi_create_buffer | 用于创建并获取一个指定大小的ArkTS Buffer。 |
| napi_create_buffer_copy | 用于创建并获取一个指定大小的ArkTS Buffer，并以给定的入参数据对buffer的缓冲区进行初始化。 |
| napi_create_external_buffer | 用于创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 |
| napi_get_buffer_info | 获取ArkTS Buffer底层数据缓冲区及其长度。 |
| napi_is_buffer | 判断给定ArkTS value是否为Buffer对象。 |
| napi_create_external_arraybuffer | 用于分配一个附加有外部数据的ArkTS ArrayBuffer。外部ArrayBuffer是一个特殊类型的ArrayBuffer，它持有对外部数据的引用而不实际拥有数据存储。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_create_buffer
此接口用于创建Buffer对象。Buffer对象是用于在Node-API模块中操作二进制数据的一种特殊类型。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createBuffer: () => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_buffer: %{public}s', testNapi.createBuffer().toString());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_buffer error');
}
```
napi_create_buffer_copy
本接口是Node-API中用于创建并复制数据到Buffer对象的函数。它可以在Node-API模块中创建一个新的Buffer对象，并将指定的数据复制到该Buffer对象中。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createBufferCopy: () => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_buffer_copy: %{public}s', testNapi.createBufferCopy().toString());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_buffer_copy error');
}
```
napi_create_external_buffer
当希望在ArkTS中使用现有的Node-API模块内存块，而不需要额外的拷贝时，可以使用napi_create_external_buffer。这将允许ArkTS层直接访问并操作该内存，避免额外的内存分配和拷贝操作。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createExternalBuffer: () => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_external_buffer: %{public}s', testNapi.createExternalBuffer()
.toString());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_external_buffer error');
}
```
napi_get_buffer_info
在ArkTS中需要对Buffer对象中的数据执行特定的操作时，可以使用此接口来获取指向数据的指针和数据长度。这样可以在Node-API模块直接对数据进行操作，而无需进行数据的拷贝。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getBufferInfo: () => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_buffer_info: %{public}s', testNapi.getBufferInfo().toString());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_buffer_info error');
}
```
napi_is_buffer
判断给定ArkTS value是否为Buffer对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isBuffer: () => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_buffer: %{public}s', JSON.stringify(testNapi.isBuffer()));
} catch (error) {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_buffer error');
}
```
napi_create_external_arraybuffer
分配一个附加有外部数据的ArkTS ArrayBuffer。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createExternalArraybuffer: () => ArrayBuffer | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Node-API createExternalArraybuffer: %{public}s',
JSON.stringify(testNapi.createExternalArraybuffer()));
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-basic-data-types-V14
爬取时间: 2025-04-30 06:18:01
来源: Huawei Developer
简介
ArkTS的Number类型是一个双精度64位二进制格式IEEE 754值。只有在-2^53+1到2^53-1范围内（闭区间）的整数才能在不丢失精度的情况下被表示，在超过该取值范围的情况下，需要使用BigInt对应的NPI接口来处理更大范围的整数。
基本概念
当使用Node-API接口进行数值类型的创建和获取时，有一些基本概念需要了解：
场景和功能介绍
以下Node-API函数通常在开发ArkTS的Node-API模块时使用，以便处理数值类型值，帮助开发人员在Node-API模块中和JavaScrip数值进行交互：
| 接口 | 描述 |
| --- | --- |
| napi_get_value_uint32 | 将ArkTS环境中number类型数据转为Node-API模块中的uint32类型数据。 |
| napi_get_value_int32 | 将ArkTS环境中获取的number类型数据转为Node-API模块中的int32类型数据。 |
| napi_get_value_int64 | 将ArkTS环境中获取的number类型数据转为Node-API模块中的int64类型数据。 |
| napi_get_value_double | 将ArkTS环境中获取的number类型数据转为Node-API模块中的double类型数据。 |
| napi_create_int32 | 将Node-API模块中的int32_t类型转换为ArkTS环境中number类型。 |
| napi_create_uint32 | 将Node-API模块中的uint32_t类型转换为ArkTS环境中number类型。 |
| napi_create_int64 | 将Node-API模块中的int64_t类型转换为ArkTS环境中number类型。 |
| napi_create_double | 将Node-API模块中的double类型转换为ArkTS环境中number类型。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_get_value_uint32
用于从ArkTS环境中获取32位无符号整数值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueUint32: <T>(data: T) => number | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.getValueUint32<number>(111111111111);
let data = testNapi.getValueUint32<string>("sssss");
hilog.info(0x0000, 'Node-API', 'get_value_uint32_number %{public}d', value);
// 传入非数字"sssss"时函数返回undefined
hilog.info(0x0000, 'Node-API', 'get_value_uint32_number %{public}s', data);
// 传入uint32范围内的数字100时函数返回原数字
hilog.info(0x0000, 'Node-API', 'get_value_uint32_number %{public}d', testNapi.getValueUint32<number>(100));
```
napi_get_value_int32
将ArkTS value转为Node-API模块中的int32类型数据。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueInt32: (value: number | string) => number | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 传入非数字“ss”时函数返回undefined
hilog.info(0x0000, 'Node-API', 'get_value_int32_not_number %{public}s', testNapi.getValueInt32('ss'));
// 传入int32范围内的数字100时函数返回原数字
hilog.info(0x0000, 'Node-API', 'get_value_int32_number %{public}d', testNapi.getValueInt32(100));
// 传入68719476735，此数字的二进制为111111111111111111111111111111111111，在int32类型中此二进制代表数字-1
hilog.info(0x0000, 'Node-API', 'get_value_int32_oversize %{public}d', testNapi.getValueInt32(68719476735));
// 大于2的31次-1的数字且不是二进制为111111111111111111111111111111111111这样的在int32中有特殊含义的数字也会溢出，导致数值发生改变，返回值按后32位二进制编码解码
hilog.info(0x0000, 'Node-API', 'get_value_int32_oversize %{public}d', testNapi.getValueInt32(687194767355));
// 传入NAN（not a number）、+Infinity（正无穷）或-Infinity（负无穷），会返回数字0
hilog.info(0x0000, 'Node-API', 'get_value_int32_number_NAN %{public}d', testNapi.getValueInt32(NaN));
hilog.info(0x0000, 'Node-API', 'get_value_int32_number_+Infinity %{public}d', testNapi.getValueInt32(+Infinity));
hilog.info(0x0000, 'Node-API', 'get_value_int32_number_-Infinity %{public}d', testNapi.getValueInt32(-Infinity));
```
napi_get_value_int64
将ArkTS value转为Node-API模块中的int64类型数据。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueInt64: (value: number | string) => number | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 输入不超过int64表示范围的数字，会返回该数字
hilog.info(0x0000, 'Node-API', 'get_value_int64_number %{public}d', testNapi.getValueInt64(80));
// 传入非数字“ss”，获得函数返回的值应为undefined
hilog.info(0x0000, 'Node-API', 'get_value_int64_not_number %{public}s', testNapi.getValueInt64('sAs'));
// 输入超过int64表示范围的数字会溢出，失去精度，导致输入数字与返回数字不相等
hilog.info(0x0000, 'Node-API', 'get_value_int64_number_oversize %{public}d', testNapi.getValueInt64(9223372036854775809));
// 传入NAN（not a number）、+Infinity（正无穷）或-Infinity（负无穷）接口返回数字0
hilog.info(0x0000, 'Node-API', 'get_value_int64_number_NAN %{public}d', testNapi.getValueInt64(NaN));
hilog.info(0x0000, 'Node-API', 'get_value_int64_number_+Infinity %{public}d', testNapi.getValueInt64(+Infinity));
hilog.info(0x0000, 'Node-API', 'get_value_int64_number_-Infinity %{public}d', testNapi.getValueInt64(-Infinity));
```
napi_get_value_double
将ArkTS value转为Node-API模块中的double类型数据。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getDouble: (value: number | string) => number | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 输入数字，返回该数字
hilog.info(0x0000, 'Node-API', 'get_value_double_number %{public}d', testNapi.getDouble(80.885));
// 传入非数字，获得函数返回的值应为undefined
hilog.info(0x0000, 'Node-API', 'get_value_double_not_number %{public}s', testNapi.getDouble('sAs'));
```
napi_create_int32
用于创建一个ArkTS数字（int32类型）的值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createInt32: () => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag','Test Node-API napi_create_int32：' + testNapi.createInt32());
```
napi_create_uint32
用于创建一个ArkTS数字（uint32类型）的值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createUInt32: () => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag','Test Node-API napi_create_uint32: ' + testNapi.createUInt32());
```
napi_create_int64
用于创建一个ArkTS数字（int64类型）的值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createInt64: () => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag','Test Node-API napi_create_int64: ' + testNapi.createInt64());
```
napi_create_double
用于创建一个ArkTS数字（double类型）的值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createDouble: () => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag','Test Node-API napi_create_double: ' + testNapi.createDouble());
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-class-V14
爬取时间: 2025-04-30 06:18:15
来源: Huawei Developer
简介
使用Node-API接口进行class相关开发，处理ArkTS中的类，例如定义类、构造实例等。
基本概念
在使用Node-API接口进行class相关开发时，需要理解以下基本概念：
场景和功能介绍
以下Node-API接口主要用于处理class。他们的使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_new_instance | 需要通过给定的构造函数构建一个实例时，可以使用这个函数。 |
| napi_get_new_target | 使用此函数获取构造函数调用的new.target。 |
| napi_define_class | 在Node-API模块定义与ArkTS类相对应的类。这个函数允许将Node-API模块类绑定到ArkTS类。 |
| napi_wrap | 在ArkTS对象上绑定一个Node-API模块对象实例。这个函数通常在将Node-API模块对象与ArkTS对象进行绑定时使用，以便在ArkTS中使用本地对象的方法和属性。 |
| napi_unwrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例。 |
| napi_remove_wrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例，并解除绑定。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_new_instance
通过给定的构造函数实例化一个对象，将这个对象返回ArkTS侧使用。
参数constructor不是function类型则返回napi_function_expected。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const newInstance: (obj: Object, param: string) => Object;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
class Fruit {
name: string;
constructor(name: string) {
this.name = name;
}
}
// 调用函数，用变量obj接收函数返回的实例化对象
let obj = testNapi.newInstance(Fruit, 'test');
// 打印实例化对象obj的信息
hilog.info(0x0000, 'Node-API', 'napi_new_instance %{public}s', JSON.stringify(obj));
```
napi_get_new_target
用于获取构造函数的new.target值。在ArkTS中，new.target是一个特殊的元属性，用于在构造函数中判断是否通过new关键字调用了该构造函数。
示例代码可以参考链接：
Native与ArkTS对象绑定
napi_define_class
用于定义一个ArkTS类。该函数允许在Node-API模块中创建一个ArkTS类，并将类的方法和属性与相应的Node-API模块关联起来。
示例代码可以参考链接：
Native与ArkTS对象绑定
napi_wrap
在ArkTS object上绑定一个native对象实例。
参数js_object不为object类型或function类型时返回napi_object_expected。
napi_unwrap
从一个被包装的对象中解除包装并获取与之关联的数据指针。
参数js_object不为object类型或function类型时返回napi_object_expected。
napi_remove_wrap
从ArkTS object上获取先前绑定的native对象实例，并解除绑定。
参数js_object不为object类型或function类型时返回napi_object_expected。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const wrap: (obj: Object) => Object;
export const unWrap: (obj: Object) => void;
export const removeWrap: (obj: Object) => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Obj {}
let obj: Obj = {};
testNapi.wrap(obj)
testNapi.unWrap(obj)
testNapi.removeWrap(obj)
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API error: %{public}s', error.message);
}
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-cleanuphook-V14
爬取时间: 2025-04-30 06:18:28
来源: Huawei Developer
简介
使用Node-API接口在进程退出时处理未释放资源，在Node-API模块注册清理钩子，一旦当前环境退出，这些钩子就会运行，使所有资源都被正确释放。
基本概念
Node-API提供了注册和取消注册清理钩子函数的功能，以下是相关概念：
以上这些基本概念是理解和使用Node-API接口注册环境清理钩子的基础，下面将介绍具体的接口和使用示例。
场景和功能介绍
以下Node-API接口用于注册和取消不同类型的清理钩子。他们的使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_add_env_cleanup_hook | 注册一个环境清理钩子函数，该函数将在Node-API环境退出时被调用。 |
| napi_remove_env_cleanup_hook | 取消之前注册的环境清理钩子函数，避免其在环境清理时执行。 |
| napi_add_async_cleanup_hook | 注册一个异步清理钩子函数，该函数将在Node-API进程退出时异步执行。 |
| napi_remove_async_cleanup_hook | 取消之前注册的异步清理钩子函数，确保在不需要时不会执行相关的清理工作。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_add_env_cleanup_hook
用于注册一个环境清理钩子函数，该函数将在环境退出时执行。这是确保资源在环境销毁前得到清理的重要机制。
napi_remove_env_cleanup_hook
用于取消之前注册的环境清理钩子函数。在某些情况下，需要在插件卸载或资源被重新分配时取消钩子函数。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiEnvCleanUpHook: () => Object | void;
```
ArkTS侧示例代码
```typescript
// index.ets
import hilog from '@ohos.hilog'
import worker from '@ohos.worker'
let wk = new worker.ThreadWorker("entry/ets/workers/worker.ts");
// 发送消息到worker线程
wk.postMessage("test NapiEnvCleanUpHook");
// 处理来自worker线程的消息
wk.onmessage = (message) => {
hilog.info(0x0000, 'testTag', 'Test Node-API message from worker: %{public}s', JSON.stringify(message));
wk.terminate();
};
```
```typescript
// worker.ts
import hilog from '@ohos.hilog'
import worker from '@ohos.worker'
import testNapi from 'libentry.so'
let parent = worker.workerPort;
// 处理来自主线程的消息
parent.onmessage = function(message) {
hilog.info(0x0000, 'testTag', 'Test Node-API message from main thread: %{public}s', JSON.stringify(message));
// 发送消息到主线程
parent.postMessage('Test Node-API worker:' + testNapi.napiEnvCleanUpHook());
}
```
worker相关开发配置和流程参考以下链接：
使用Worker进行线程间通信
napi_add_async_cleanup_hook
这个接口用于注册一个异步清理钩子函数，该函数将在环境退出时异步执行。与同步钩子不同，异步钩子允许在进程退出时进行更长时间的操作，而不会阻塞进程退出。
napi_remove_async_cleanup_hook
这个接口用于取消之前注册的异步清理钩子函数。与取消同步钩子类似，这通常是在不再需要钩子函数时进行的操作。
cpp部分代码
由于需要包含“uv.h”库，所以需要在CMakeLists文件中添加配置：
接口声明
```typescript
// index.d.ts
export const napiAsyncCleanUpHook: () => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_add_async_cleanup_hook: %{public}s', testNapi.napiAsyncCleanUpHook());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_add_async_cleanup_hook error.message: %{public}s', error.message);
}
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-date-V14
爬取时间: 2025-04-30 06:18:42
来源: Huawei Developer
简介
Node-API中date相关接口用于处理ArkTS Date对象，并在Node-API模块和ArkTS代码之间进行日期数据的转换和处理。这对于在Node-API模块中处理时间和日期相关逻辑非常有用。
基本概念
在Node-API的中，ArkTS Date对象的数据表示从UTC时间1970年1月1日0时0分0秒起至现在的总毫秒数。
ArkTS Date对象提供了一种在ArkTS中表示和操作日期和时间的方式。它们允许您创建表示特定时刻的日期对象，执行各种日期和时间相关的计算（如添加或减去时间间隔），以及格式化日期为字符串以供显示。
在Node-API中，通过提供与Date对象交互的函数，Node-API模块能够更紧密地与ArkTS环境集成，执行更复杂的日期和时间相关操作。
场景和功能介绍
以下Node-API函数通常在开发Node-API模块中与ArkTS的Date对象进行交互时使用，来处理和操作日期数据。以下是一些可能的使用场景：
| 接口 | 描述 |
| --- | --- |
| napi_create_date | 在需要根据当前系统时间或特定计算生成一个Date对象时，可通过使用此接口创建表示这些时间的ArkTS Date对象，然后将其传递给ArkTS代码进行进一步处理。 |
| napi_get_date_value | 在Node-API模块中接收到一个ArkTS的Date对象，并且需要获取其对应的时间戳或日期值时，可以使用此接口。 |
| napi_is_date | 在需要确定一个ArkTS对象是否为Date对象时，可使用此接口判断给定的值是否为Date对象。例如，在接收函数参数时，需要验证参数是否为Date对象以确保正确的数据类型。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_create_date
通过一个C++的double数据创建ArkTS的Date。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createDate: () => Date;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_date: %{public}s', testNapi.createDate().toString());
```
napi_get_date_value
获取给定ArkTS Date对应的C++ double值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getDateValue: (date: Date) => number | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
const date = new Date();
hilog.info(0x0000, 'testTag', 'Node-API: output the Unix Time Stamp: %{public}d', date.getTime());
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_date_value: %{public}d', testNapi.getDateValue(date));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_date_value error: %{public}s', error.message);
}
```
napi_is_date
判断给定ArkTS value是否为ArkTS Date对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isDate: <T>(date: T) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
let now: Date = new Date();
let date = "123";
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_date: %{public}s', testNapi.isDate(now));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_date: %{public}s', testNapi.isDate(date));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_date error: %{public}s', error.message);
}
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-error-V14
爬取时间: 2025-04-30 06:18:55
来源: Huawei Developer
简介
使用Node-API接口进行错误处理开发，使得在Node-API模块中能够更好地管理和响应错误情况。通过合理使用这些函数，可以提高模块的稳定性和可靠性。
基本概念
在ArkTS编程中，异常和错误是常见的概念。异常表示发生了某种意外情况，而错误则指示程序无法正确执行某些操作。Node-API提供了一系列方法来帮助开发者在Node-API模块中处理ArkTS中的异常和错误。下面是一些基本概念：
这些基本概念在异常和错误处理中非常重要，开发者需要通过适当的方法来捕获、处理或向用户报告这些异常和错误，以确保程序的稳定性和正确性。Node-API提供的方法可以帮助开发者在Node-API模块中处理ArkTS中的异常和错误。
场景和功能介绍
以下Node-API接口主要用于与ArkTS交互时处理错误和异常情况。他们的使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_create_error、napi_create_type_error、napi_create_range_error | 在C/C++中需要创建一个错误对象时，可以使用这些函数。创建的错误对象可以使用napi_throw抛出到ArkTS。 |
| napi_throw | 当在C/C++中出现了错误或异常情况时，通过使用napi_create_error或napi_get_last_error_info方法创建或获取ArkTS Error对象，使用该方法抛出已有的ArkTS Error对象。 |
| napi_throw_error、napi_throw_type_error、napi_throw_range_error | 当在C/C++中出现了错误或异常情况时，可以使用这些函数来抛出ArkTS中的异常。 |
| napi_is_error | 检查一个napi_value是否代表一个错误对象时，可以使用这个函数。 |
| napi_get_and_clear_last_exception | 当你需要获取最近一次出现的异常，并将异常队列清空时，可以使用这个函数。 |
| napi_is_exception_pending | 当你需要判断是否有未处理的异常时，可以使用这个函数。 |
| napi_fatal_error | 当遇到严重错误或不可恢复的情况时，可以使用这个函数引发致命错误来立即终止进程。 |
| napi_fatal_exception | 抛出一个致命异常并终止进程, 同时产生相应的crash日志。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_get_last_error_info
用于获取最后一次发生的错误信息，包括错误码、错误消息以及错误进栈信息，即使存在挂起的ArkTS异常，也可以调用此API。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getLastErrorInfo: (str: string) => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_last_error_info: %{public}s', testNapi.getLastErrorInfo('message'));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_last_error_info error: %{public}s', error);
}
```
napi_create_type_error
创建并获取一个带文本信息的ArkTS TypeError。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createTypeError: () => Error;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
throw testNapi.createTypeError();
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_type_error errorCode: %{public}s, errorMessage %{public}s', error.code, error.message);
}
```
napi_create_range_error
创建并获取一个带文本信息的ArkTS RangeError。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createRangeError: () => Error;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
throw testNapi.createRangeError();
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_range_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
```
napi_create_error
创建并获取一个带文本信息的ArkTS Error。
napi_throw
用于在Node-API模块中抛出ArkTS异常的函数。当在本机代码中发生错误或检测到不符合预期的情况时，可以使用此接口来抛出一个ArkTS异常，使其能够被捕获并处理。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiThrow: () => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
testNapi.napiThrow();
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_throw errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
```
napi_throw_error
用于抛出一个带文本信息的ArkTS Error。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiThrowErrorMessage: () => void;
export const napiThrowError: (dividend: number, divisor: number) => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
testNapi.napiThrowErrorMessage();
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_throw_error error code: %{public}s , message: %{public}s', error.code, error.message);
}
try {
testNapi.napiThrowError(5, 0);
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_throw_error errorCode: %{public}s , errorManager: %{public}s', error.code, error.message);
}
```
napi_throw_type_error
创建并获取一个带文本信息的ArkTS TypeError。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const throwTypeErrorMessage: () => void;
export const throwTypeError: (message: string) => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
testNapi.throwTypeErrorMessage();
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_throw_type_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
try {
testNapi.throwTypeError('str');
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_throw_type_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
```
napi_throw_range_error
创建并获取一个带文本信息的ArkTS RangeError。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const throwRangeErrorMessage: () => void;
export const throwRangeError: (num: number) => number | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
testNapi.throwRangeErrorMessage();
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_throw_range_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
try {
testNapi.throwRangeError(1);
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_throw_range_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
```
napi_is_error
用于判断给定的napi_value是否表示一个error对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiIsError: <T>(obj: T) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
throw new Error("throwing an error");
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_error error: %{public}s', testNapi.napiIsError(error)
.toString());
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_error error: %{public}s', testNapi.napiIsError(1)
.toString());
}
```
napi_get_and_clear_last_exception
用于获取并清除最近一次出现的异常。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getAndClearLastException: () => Error | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 这里获取到最后一个未处理的异常
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_and_clear_last_exception, error.message: %{public}s',
testNapi.getAndClearLastException());
```
napi_is_exception_pending
用于判断是否出现了异常。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isExceptionPending: () => Object | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
interface MyObject {
code: string;
message: string;
}
try {
let result = testNapi.isExceptionPending() as MyObject;
hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_exception_pending, error.Code: %{public}s, error.message: %{public}s',
result.code, result.message);
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_exception_pending error');
}
```
napi_fatal_error
用于引发致命错误以立即终止进程。在调用napi_fatal_error函数后，导致应用程序终止，因此应该慎重使用，避免在正常操作中频繁调用该函数。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const fatalError: () => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
testNapi.fatalError();
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_fatal_error error');
}
```
napi_fatal_exception
在主线程的上下文环境中调用napi_fatal_exception函数后，抛出一个致命异常，导致应用程序终止，同时会生成相应的crash日志。因此应该慎重使用，避免在正常操作中频繁调用该函数。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const fatalException: (err: Error) => void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
const err = new Error("a fatal exception occurred");
testNapi.fatalException(err);
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-environmental-life-cycle-V14
爬取时间: 2025-04-30 06:19:09
来源: Huawei Developer
简介
在Node-API模块中，我们可以使用Node-API接口将特定数据与当前的环境相关联，并在需要时检索该数据。
基本概念
在Node-API中的关联数据是指将自定义的C++数据结构的生命周期与当前环境的生命周期相关联，这意味着只要当前运行环境存在，关联数据就会保持有效。
场景和功能介绍
以下接口可以帮助我们在Node-API模块中更方便地管理对象实例所需的状态信息、引用计数或其他自定义数据，他们的使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_set_instance_data | 绑定与当前运行的环境相关联的数据项。 |
| napi_get_instance_data | 检索与当前运行的环境相关联的数据项。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_set_instance_data
将需要绑定的数据与当前运行的环境相关联。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const setInstanceData: (data: number) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let data = 5;
let value = testNapi.setInstanceData(data);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_instance_data:%{public}s', value);
```
napi_get_instance_data
检索出与当前运行的环境相关联的数据项。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getInstanceData: () => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let data = 5;
testNapi.setInstanceData(data);
let value = testNapi.getInstanceData();
hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_instance_data:%{public}d', value);
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-function-V14
爬取时间: 2025-04-30 06:19:22
来源: Huawei Developer
简介
函数调用允许开发者从Node-API模块中调用ArkTS函数，并传递参数进行调用，或者直接在Node-API模块中创建一个ArkTS方法。
基本概念
函数是一种非常重要的编程概念，可以执行特定的任务或操作、提高代码的可读性、把复杂任务简化、提高代码复用性以及支持代码的组织与管理。每个函数可以负责不同的功能，提供一种将代码模块化和组织结构化的方式，使其更易于理解、维护和重用。
场景和功能介绍
| 接口 | 描述 |
| --- | --- |
| napi_get_cb_info | 当需要从给定的callback info中获取有关调用的参数信息和this指针时，可使用此接口。 |
| napi_call_function | 当需要在Node-API模块中对ArkTS侧函数进行调用时，可使用此接口。 |
| napi_create_function | 当需要将C/C++函数创建一个ArkTS函数时，可以使用此接口。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。napi_create_function方法除外，具体使用见示例。
napi_get_cb_info
获取有关函数调用的详细信息。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getCbArgs: <T>(arg: T) => T;
// getCbArgQuantity的入参由用户自定义，在此用例中，我们用两个入参，一个是string，一个是number
export const getCbArgQuantity: (str: string, num: number) => number;
export const getCbContext: () => Object;
```
ArkTS 侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
function summation(arr: Array<number>) {
let sum: number = 0;
for (let i = 0; i < arr.length; i++) {
sum += arr[i];
}
return sum;
}
const str = 'message';
const arr = [0, 1, 2, 3, 4, 5];
const num = 526;
class Student {
name: string;
age: number;
score: number;
constructor(name: string, age: number, score: number) {
this.name = name;
this.age = age;
this.score = score;
}
}
let student = new Student('Alice', 18, 100);
// 获取参数
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get string arg:%{public}s', testNapi.getCbArgs(str));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get array arg:%{public}s ', testNapi.getCbArgs(arr).toString());
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get num arg:%{public}d ', testNapi.getCbArgs(num));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get undefined arg:%{public}s ', testNapi.getCbArgs(undefined));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get object arg:%{public}s ', JSON.stringify(testNapi.getCbArgs(student)));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get function arg:%{public}d ', testNapi.getCbArgs(summation(arr)));
// 获取参数个数
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get arg quantity:%{public}d ', testNapi.getCbArgQuantity(str, num));
// 获取上下文
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get thisArg:%{public}s ', testNapi.getCbContext().toString());
```
napi_call_function
在C/C++侧对ArkTS函数进行调用。
注意事项：napi_call_function传入的argv的长度必须大于等于argc声明的数量，且被初始化成nullptr。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const callFunction: (func: Function) => number;
export const objCallFunction: (obj: Object, func: Function) => number;
```
ArkTS 侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
function returnNumber() {
return 10;
}
class Person {
age(): number {
return 11;
}
}
const person = new Person();
hilog.info(0x0000, 'testTag', 'Test Node-API call_function:%{public}d', testNapi.callFunction(returnNumber));
hilog.info(0x0000, 'testTag', 'Test Node-API call_function:%{public}d', testNapi.objCallFunction(person,person.age));
```
napi_create_function
将一个C/C++函数包装为可在ArkTS中调用的函数，并返回一个表示该函数的napi_value。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const calculateArea: (width: number, height: number) => number;
```
ArkTS 侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API create_function:%{public}d ', testNapi.calculateArea(1.2, 4));
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-life-cycle-V14
爬取时间: 2025-04-30 06:19:35
来源: Huawei Developer
简介
在Node-API中，napi_value是一个表示ArkTS值的抽象类型，它可以表示任何ArkTS值，包括基本类型（如数字、字符串、布尔值）和复杂对象类型（如数组、函数、对象等）。
napi_value的生命周期与其在ArkTS中的对应值的生命周期紧密相关。当ArkTS值被垃圾回收时，与之关联的napi_value也将不再有效。重要的是不要在ArkTS值不再存在时尝试使用napi_value。
框架层的scope通常用于管理napi_value的生命周期。在Node-API中，可以使用napi_open_handle_scope和napi_close_handle_scope函数来创建和销毁scope。通过在scope内创建napi_value，可以确保在scope结束时自动释放napi_value，避免内存泄漏。
napi_ref是一个Node-API类型，用于管理napi_value的生命周期。napi_ref允许您在napi_value的生命周期内保持对其的引用，即使它已经超出了其原始上下文的范围。这使得您可以在不同的上下文中共享napi_value，并确保在不再需要时正确释放其内存。
基本概念
Node-API提供了一组功能，使开发人员能够在Node-API模块中创建和操作ArkTS对象，管理引用和生命周期，并注册垃圾回收回调函数等。下面是一些基本概念：
这些基本概念使开发人员能够在Node-API模块中安全且有效地操作ArkTS对象，并确保正确管理对象的生命周期。
场景和功能介绍
以下Node-API接口主要用于ArkTS对象的引用管理，并确保在Node-API模块代码中正确地处理ArkTS对象的生命周期。使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_open_handle_scope、napi_close_handle_scope | 主要用于管理ArkTS对象的生命周期，确保在Node-API模块代码中使用ArkTS对象时能够正确地进行内存管理。当在Node-API模块中处理ArkTS对象时，需要创建一个临时的作用域来存储对象的引用，以便在执行期间正确访问这些对象，并在执行结束后关闭这个handle scope。 |
| napi_open_escapable_handle_scope、napi_close_escapable_handle_scope | 当在Node-API模块中编写函数实现，需要将函数在ArkTS中返回的对象从函数的作用域正确地返回到函数被调用的外部作用域中。 |
| napi_escape_handle | 需要将ArkTS对象的生命周期提升到父作用域中，避免对象被意外释放。 |
| napi_create_reference、napi_delete_reference | 主要用于在Node-API模块代码中管理ArkTS对象的引用，以确保对象的生命周期符合插件的需求。 |
| napi_reference_ref、napi_reference_unref | 主要用于管理ArkTS对象引用的引用计数，以确保在多个地方共享引用时引用计数能够正确地增加和减少。 |
| napi_get_reference_value | 主要用于在Node-API模块代码中获取与引用相关联的ArkTS对象，以便在Node-API模块中对其进行操作。 |
| napi_add_finalizer | 在需要在ArkTS对象被垃圾回收前执行一些清理或释放资源的情况下，确保资源的正确释放和管理。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_open_handle_scope、napi_close_handle_scope
通过接口napi_open_handle_scope创建一个上下文环境使用。需要使用napi_close_handle_scope进行关闭。用于管理ArkTS对象的生命周期确保在Node-API模块代码处理ArkTS对象时能够正确地管理其句柄，以避免出现对象错误回收的问题。
需要注意的是合理使用napi_open_handle_scope和napi_close_handle_scope管理napi_value的生命周期，做到生命周期最小化，避免发生内存泄漏问题。
代码部分也可参考下面链接：
生命周期管理
cpp部分代码
接口声明
```typescript
// index.d.ts
export const handleScopeTest: () => string;
export const handleScope: () => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API handleScopeTest: %{public}s', testNapi.handleScopeTest());
hilog.info(0x0000, 'testTag', 'Test Node-API handleScope: %{public}s', testNapi.handleScope());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API handleScopeTest errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
```
napi_open_escapable_handle_scope、napi_close_escapable_handle_scope、napi_escape_handle
通过接口napi_open_escapable_handle_scope创建出一个可逃逸的handel scope，可将范围内声明的值返回到父作用域。需要使用napi_close_escapable_handle_scope进行关闭。napi_escape_handle用于提升传入的ArkTS对象的生命周期到其父作用域。
通过上述接口可以更灵活的使用管理传入的ArkTS对象，特别是在处理跨作用域的值传递时非常有用。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const escapableHandleScopeTest: () => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API EscapableHandleScopeTest: %{public}s', testNapi.escapableHandleScopeTest());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API EscapableHandleScopeTest errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
```
napi_create_reference、napi_delete_reference
为Object创建一个reference，以延长其生命周期。调用者需要自己管理reference生命周期。可以调用napi_delete_reference删除传入的reference。
napi_reference_ref、napi_reference_unref
增加/减少传入的reference的引用计数，并获取新的计数。
napi_get_reference_value
获取与reference相关联的ArkTS Object。
由于弱引用（引用计数为0的napi_ref）的释放与gc回收js对象并非同时发生。
因此可能在弱引用被释放前，js对象已经被回收。
这意味着你可能在napi_ref有效的情况下，通过本接口获取到一个空指针。
napi_add_finalizer
当ArkTS Object中的对象被垃圾回收时调用注册的napi_add_finalizer回调。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createReference: () => Object | void;
export const useReference: () => Object | void;
export const deleteReference: () => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API createReference: %{public}s', JSON.stringify(testNapi.createReference()));
hilog.info(0x0000, 'testTag', 'Test Node-API useReference: %{public}s', JSON.stringify(testNapi.useReference()));
hilog.info(0x0000, 'testTag', 'Test Node-API deleteReference: %{public}s', testNapi.deleteReference());
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API ReferenceTest errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-object-V14
爬取时间: 2025-04-30 06:19:49
来源: Huawei Developer
简介
使用Node-API接口进行object相关开发，处理ArkTS对象的基本操作的功能，例如创建对象、获取原型、冻结和密封对象，检查对象的类型等。这些操作是在处理ArkTS对象时非常常见的，提供了一种与ArkTS对象交互的方式。
基本概念
在Node-API接口开发中，经常需要定义和操作对象。例如，创建一个API接口，该接口接受一个对象作为输入参数，对该对象执行某些操作，并返回一个结果对象。在这个过程中，需要确保接口的定义清晰、规范，并且与对象的属性和方法相兼容。
场景和功能介绍
以下Node-API接口主要用于操作和管理ArkTS对象，使用场景介绍：
| 接口 | 描述 |
| --- | --- |
| napi_get_prototype | 当需要获取一个ArkTS对象的原型时，可以使用这个接口。通过这个接口可以在C/C++中获取到这个原型对象。 |
| napi_create_object | 在Node-API模块中创建一个默认的ArkTS对象。 |
| napi_object_freeze | 当需要确保一个对象不会被修改时（immutable），可以使用这个接口来冻结该对象，使其属性不可更改。 |
| napi_object_seal | 类似于napi_object_freeze，napi_object_seal用于密封给定的对象，使其属性不可添加或删除，但可以修改属性的值。 |
| napi_typeof | 在处理传入的ArkTS值时，可以使用这个接口来获取其类型，以便进行相应的处理。 |
| napi_instanceof | 当需要在Node-API模块中确定一个对象是否为特定构造函数的实例时，可以使用这个接口。 |
| napi_type_tag_object | 可以将指针的特定值与ArkTS对象关联起来，这对于一些自定义的内部对象标记非常有用。 |
| napi_check_object_type_tag | 使用此接口可以检查给定的对象上是否关联了特定类型的标记。 |
| napi_create_symbol | 创建一个ArkTS Symbol对象。 |
| napi_create_external | 用于创建一个ArkTS外部对象，该对象可以用于将C/C++中的自定义数据结构或对象传递到ArkTS中，并且可以在ArkTS中访问其属性和方法。 |
| napi_get_value_external | 用于获得napi_create_external创建的绑定了外部数据的ArkTS值，此函数可以在ArkTS和C/C++之间传递数据。 |
这些接口为开发人员提供了在Node-API模块中处理ArkTS对象的灵活性和功能性，可以实现从创建对象到管理对象属性以及类型检查等多种操作。
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_get_prototype
可以获得给定ArkTS对象的prototype。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getPrototype: (object: Object) => Object;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 定义一个类
class Person {
// 属性
name: string;
age: number;
// 构造函数
constructor(name: string, age: number) {
this.name = name;
this.age = age;
}
}
// 创建类的实例
const person = new Person('Alice', 30);
// 传入实例对象，获取该对象的原型
let applePrototype = testNapi.getPrototype(person);
// 判断通过testNapi.getPrototype()函数获取到的原型是不是apple的原型
// 在DevEco Studio 4.1及以后的版本中，由于ArkTS没有原型的概念，因此尝试进行原型赋值或相关操作时，将会触发错误提示'Prototype assignment is not supported (arkts-no-prototype-assignment)'，以下代码需在ts文件中执行
if (applePrototype === Person.prototype) {
hilog.info(0x0000, 'Node-API', 'get_prototype_success');
} else {
hilog.info(0x0000, 'Node-API', 'get_prototype_fail');
}
```
napi_create_object
用于在Node-API模块中创建一个空的ArkTS对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createObject: () => { name: string };
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
const myObject = testNapi.createObject();
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_object: %{public}s', myObject.name);
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_object errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
```
napi_object_freeze
用于冻结给定的ArkTS对象。冻结对象后，无法再向对象添加新的属性或方法，也无法修改已有属性或方法的值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export interface Obj {
data: number
message: string
}
export const objectFreeze: (objFreeze: Object) => Obj;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Obj {
data: number = 0
message: string = ""
}
let obj: Obj = {data: 0, message: "hello world"};
let objFreeze = testNapi.objectFreeze(obj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_freeze: %{public}s', (objFreeze.data = 1));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_object_freeze error: %{public}s', error.message);
}
```
napi_object_seal
封闭一个对象后，无法向其添加新的属性，也无法删除或修改现有属性的可配置性。但是，可以继续修改已有属性的值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export interface Obj {
data: number
message: string
id: number
}
export const objectSeal : (objSeal: Object) => Obj;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Obj {
data: number = 0
message: string = ""
// 可选属性
address?: number = 0
}
let obj: Obj = { data: 0, message: "hello world"};
let objSeal = testNapi.objectSeal(obj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}s', objSeal.message);
objSeal.data = 1;
hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}d', objSeal.data);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}d', (objSeal.id = 1));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_object_seal error: %{public}s', error.message);
}
```
napi_typeof
获取给定ArkTS value的ArkTS Type。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiTypeOf : <T>(value: T) => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
let varUndefined: undefined;
hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varUndefined));
let varNull: null = null;
hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varNull));
let varTrue= true;
hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varTrue));
let varNum = 1;
hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varNum));
let varString = "str";
hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varString));
class Obj {
id: number = 0
name: string = ""
}
let varObject: Obj = {id: 1, name: "LiLei"};
hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varObject));
const addNum = (a: number, b: number): number => a * b;
hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(addNum));
let varBigint = BigInt("1234567890123456789012345678901234567890");
hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varBigint));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_typeof error: %{public}s', error.message);
}
```
napi_instanceof
用于检查一个对象是否是指定构造函数的实例。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiInstanceOf: (date: Object, construct: Object) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Person {
name: string;
age: number;
constructor(name: string, age: number) {
this.name = name;
this.age = age;
}
}
const person = new Person("Alice", 30);
class Obj {
data: number = 0
message: string = ""
}
let obj: Obj = { data: 0, message: "hello world"};
hilog.info(0x0000, 'testTag', 'Test Node-API napi_instanceof: %{public}s', testNapi.napiInstanceOf(person, Person));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_instanceof: %{public}s', testNapi.napiInstanceOf(obj, Person));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_instanceof error: %{public}s', error.message);
}
```
napi_type_tag_object
使用类型标签type_tag来标记ArkTS对象，后续可以更精确地识别ArkTS对象。
napi_check_object_type_tag
验证一个ArkTS对象是否带有特定类型标签。
类型标签提供了一种在Node-API模块和ArkTS对象之间建立强类型关联的机制，使得原生代码能够更准确地识别和处理特定的ArkTS对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const setTypeTagToObject: (obj: Object, index: number) => boolean | void;
export const checkObjectTypeTag: (obj: Object, index: number) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
class Obj {
data: number = 0
message: string = ""
}
let objA: Obj = { data: 0, message: "hello world"};
let objB: Obj = { data: 10, message: "typeTag"};
hilog.info(0x0000, 'testTag', 'Test Node-API napi_type_tag_object objA -> 0: %{public}s', testNapi.setTypeTagToObject(objA, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_type_tag_object objB -> 0: %{public}s', testNapi.setTypeTagToObject(objB, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_check_object_type_tag objA -> 0: %{public}s', testNapi.checkObjectTypeTag(objA, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_check_object_type_tag objB -> 1: %{public}s', testNapi.checkObjectTypeTag(objB, 1));
```
napi_create_external
创建包装自定义的C/C++对象并将其公开给ArkTS代码。这种情况下，我们可以使用napi_create_external来创建一个包含指向自定义对象的指针的Node-API值，以便让ArkTS代码能够访问和操作该对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createExternal: () => Object;
export const getExternalType: (externalData: Object) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
const externalData = testNapi.createExternal();
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_external:%{public}s', testNapi.getExternalType(externalData));
```
napi_get_value_external
napi_create_external可以创建包装自定义的C/C++对象并将其公开给ArkTS代码，而napi_get_value_external就是用来获得napi_create_external所创建的外部对象的。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueExternal: () => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'Node-API', 'get_value_external:%{public}d', testNapi.getValueExternal());
```
napi_create_symbol
用于创建一个新的Symbol。Symbol是一种特殊的数据类型，用于表示唯一的标识符。与字符串或数字不同，符号的值是唯一的，即使两个符号具有相同的描述，它们也是不相等的。符号通常用作对象属性的键，以确保属性的唯一性。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createSymbol : () => symbol;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let varSymbol = testNapi.createSymbol();
hilog.info(0x0000, 'Node-API', 'createSymbol:%{public}s', typeof varSymbol);
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-other-practical-tools-V14
爬取时间: 2025-04-30 06:20:02
来源: Huawei Developer
简介
Node-API接口提供了一些实用接口，可以帮助开发者更好地进行Node-API相关开发。
基本概念
场景和功能介绍
| 接口 | 描述 |
| --- | --- |
| node_api_get_module_file_name | 获取加载项加载位置的绝对路径。 |
| napi_strict_equals | 在某些情况下，希望确保两个值不仅具有相同的值，还具有相同的类型。例如，如果正在处理一些需要特定类型的数据结构或算法，使用napi_strict_equals可以确保数据的一致性。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
node_api_get_module_file_name
用于获取加载项加载位置的绝对路径。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getModuleFileName: () => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let filename = testNapi.getModuleFileName();
hilog.info(0x0000, 'testTag', 'Test Node-API node_api_get_module_file_name:%{public}s', filename);
```
napi_strict_equals
判断给定的两个ArkTS value是否严格相等。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const strictEquals : (lhs: string, rhs: string | number) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
let lhs = "123";
let rhs = "123";
let str = "456";
let num = 123;
hilog.info(0x0000, 'testTag', 'Test Node-API napi_strict_equals: %{public}s', testNapi.strictEquals(lhs, rhs));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_strict_equals: %{public}s', testNapi.strictEquals(lhs, str));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_strict_equals: %{public}s', testNapi.strictEquals(lhs, num));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_strict_equals error: %{public}s', error.message);
}
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-primitive-V14
爬取时间: 2025-04-30 06:20:15
来源: Huawei Developer
简介
在使用Node-API接口时，开发人员可以实现在Node-API模块中与ArkTS对象的交互，并进行数据转换和获取特定对象的操作，它们在不同的场景中发挥着重要的作用，使开发人员能够更灵活地处理ArkTS值和对象。
基本概念
在使用Node-API操作ArkTS对象时，有一些基本概念需要了解：
场景和功能介绍
以下接口用于从C/C++代码中与ArkTS进行交互，传递数据并执行操作，它们的使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_coerce_to_bool | 用于将给定的ArkTS value强转成ArkTS boolean值。 |
| napi_coerce_to_number | 用于将给定的ArkTS value强转成ArkTS number。 |
| napi_coerce_to_object | 用于将给定的ArkTS value强转成ArkTS Object。 |
| napi_coerce_to_string | 用于将给定的ArkTS value强转成ArkTS string。 |
| napi_get_boolean | 用于根据给定的C boolean值，获取ArkTS boolean值。 |
| napi_get_value_bool | 用于根据给定的ArkTS boolean值，获取等价的C/C++布尔值。 |
| napi_get_global | 用于获取全局ArkTS对象，以便在C/C++中访问和操纵全局对象。 |
| napi_get_null | 用于获取ArkTS null。 |
| napi_get_undefined | 用于获取ArkTS undefined。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_coerce_to_bool
用于将给定的ArkTS value强转成ArkTS boolean值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const coerceToBool: <T>(data: T) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.coerceToBool<number>(0);
let str = testNapi.coerceToBool<string>('111111111');
let obj = new Object();
let res = testNapi.coerceToBool<Object>(obj);
let result = testNapi.coerceToBool<null>(null);
// false
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_bool:%{public}s', value);
// true
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_bool:%{public}s', str);
// true
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_bool:%{public}s', res);
// false
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_bool:%{public}s', result);
```
napi_coerce_to_number
用于将给定的ArkTS value强转成ArkTS number。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const coerceToNumber: <T>(data: T) => number;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.coerceToNumber<string>('2556');
let str = testNapi.coerceToNumber<string>('sssss');
let bool = testNapi.coerceToNumber<boolean>(true);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_number:%{public}d', value);
// 返回的为NAN
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_number:%{public}d', str);
// 返回的是1
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_number:%{public}d', bool);
```
napi_coerce_to_object
用于将给定的ArkTS value强转成ArkTS Object。
cpp部分代码：
接口声明
```typescript
// index.d.ts
export const coerceToObject: <T>(data: T) => Object;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.coerceToObject<string>('222222');
let result = testNapi.coerceToObject<number>(111);
hilog.info(0x0000, 'testTag', 'Node-API coerceToObject:%{public}s.', typeof result);
if (typeof value === 'object') {
hilog.info(0x0000, 'testTag', 'Node-API The value is an object.');
} else {
hilog.info(0x0000, 'testTag', 'Node-API The value is not an object.');
}
```
napi_coerce_to_string
用于将给定的ArkTS value强转成ArkTS string。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const coerceToString: <T>(data: T) => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.coerceToString<number>(212);
let obj = new Object();
let res = testNapi.coerceToString<Object>(obj);
let bool = testNapi.coerceToString<boolean>(false);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_string:%{public}s', value);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_string:%{public}s', typeof res);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_string:%{public}s', bool);
```
napi_get_boolean
用于根据给定的C boolean值，获取等价的ArkTS Boolean对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getBoolean: <T>(data: T, value: String) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.getBoolean<number>(1, '1');
let data = testNapi.getBoolean<string>('sss', '1');
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_boolean:%{public}s', value);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_boolean:%{public}s', data);
```
napi_get_value_bool
使用这个函数将ArkTS中的布尔值转为等价的C布尔值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueBool: (value: boolean | string) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 分别传入布尔值和非布尔值检测接口,传入布尔值将返回原布尔值,传入其他类型返回undefined
hilog.info(0x0000, 'Node-API', 'get_value_bool_not_bool %{public}s', testNapi.getValueBool('你好123'));
hilog.info(0x0000, 'Node-API', 'get_value_bool_true %{public}s', testNapi.getValueBool(true));
hilog.info(0x0000, 'Node-API', 'get_value_bool_false %{public}s', testNapi.getValueBool(false));
```
napi_get_global
用于获取全局ArkTS对象。该函数的主要作用是获取表示ArkTS全局对象的napi_value，使得C/C++模块能够与ArkTS运行时的全局对象进行交互。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getGlobal: () => Object;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let globalObj = testNapi.getGlobal();
// 判断获取的global是否具有global的自身属性
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_global:%{public}s', globalObj.hasOwnProperty!("undefined"));
```
napi_get_null
用于获取ArkTS中的null。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getNull: () => null;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = testNapi.getNull();
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_null:%{public}s', value);
```
napi_get_undefined
用于获取ArkTS中的undefined。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getUndefined: (value: undefined) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let data: undefined = undefined;
let value = testNapi.getUndefined(data);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_undefined:%{public}s', value);
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-promise-V14
爬取时间: 2025-04-30 06:20:29
来源: Huawei Developer
简介
使用Node-API接口处理异步操作。异步操作是指需要一定时间才能完成的操作，例如从网络下载数据或读取大型文件。与同步操作不同，异步操作不会阻塞主线程，而是会在后台执行。当异步操作完成后，事件循环将把它放入任务队列中，等待主线程空闲时执行。
基本概念
Promise是ArkTS中用来处理异步操作的对象，Promise有pending（待定）、fulfilled（已兑现）和rejected（已拒绝）三种状态，Promise的初始状态是pending，resolve函数可以使其状态从pending变为fulfilled（已兑现），reject函数可以使其状态从pending变为rejected(已拒绝)，一旦兑现或拒绝Promise的状态将不能更改。下面是一些基本概念：
这些基本概念在处理异步操作中非常重要，开发者需要通过适当的方法来处理异步操作，Promise可以链式调用多个异步操作，使代码清晰整洁，便于维护。Node-API提供的方法可以帮助开发者在C/C++应用中处理ArkTS中的异步操作。
场景和功能介绍
以下Node-API接口主要用于与ArkTS Promise对象进行交互。他们的使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_is_promise | 检查一个napi_value是否代表一个Promise对象时，可以使用这个函数。 |
| napi_create_promise | 需要创建一个Promise对象时，可以使用这个函数。 |
| napi_resolve_deferred | 当你需要对promise关联的deferred对象进行resolve，将其从挂起状态转换为已解决状态时，可以使用这个函数。 |
| napi_reject_deferred | 当你需要对promise关联的deferred对象进行reject，将其从挂起状态转换为已拒绝状态时，可以使用这个函数。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_is_promise
判断给定的napi_value是否表示一个Promise对象。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const isPromise: <T>(value: T) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let value = Promise.resolve();
// 传入的对象为Promise时，返回true，否则返回false
hilog.info(0x0000, 'Node-API', 'napi_is_promise %{public}s', testNapi.isPromise(value));
hilog.info(0x0000, 'Node-API', 'napi_is_promise string %{public}s', testNapi.isPromise(''));
```
napi_create_promise
napi_create_promise用于创建一个Promise对象。
使用该接口时应注意：
napi_resolve_deferred & napi_reject_deferred
用于对Promise关联的deferred对象进行解析，napi_resolve_deferred将其从挂起状态转换为已兑现状态，napi_reject_deferred将其从挂起状态转换为已拒绝状态。
为确保微任务能正确的被执行，ArkTS运行时在使用Node-API方法兑现Promise时，将会触发一次微任务的执行。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createPromise: () => boolean | void;
export const resolveRejectDeferred: (resolve: string, reject: string, status: boolean) => Promise<string> | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 创建promise如果创建成功返回true，创建失败返回false
hilog.info(0x0000, 'Node-API', 'napi_create_promise %{public}s', testNapi.createPromise());
// 调用resolveRejectDeferred函数设置resolve和reject的返回结果以及Promise状态
// Promise状态为true时设置resolve，返回结果在then函数中获得
let promiseSuccess: Promise<string> = testNapi.resolveRejectDeferred('success', 'fail', true) as Promise<string>;
promiseSuccess.then((res) => {
hilog.info(0x0000, 'Node-API', 'get_resolve_deferred resolve %{public}s', res)
}).catch((err: Error) => {
hilog.info(0x0000, 'Node-API', 'get_resolve_deferred reject %{public}s', err)
})
// Promise状态为false时设置reject，返回结果在catch函数中获得
let promiseFail: Promise<string> = testNapi.resolveRejectDeferred('success', 'fail', false) as Promise<string>;
promiseFail.then((res) => {
hilog.info(0x0000, 'Node-API', 'get_resolve_deferred resolve %{public}s', res)
}).catch((err: Error) => {
hilog.info(0x0000, 'Node-API', 'get_resolve_deferred reject %{public}s', err)
})
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-property-V14
爬取时间: 2025-04-30 06:20:42
来源: Huawei Developer
简介
使用Node-API接口获取和设置ArkTS对象的属性。通过合理使用这些函数，实现更复杂的功能和逻辑。
基本概念
在ArkTS对象属性的相关开发中，需要处理ArkTS对象属性，确保正确地访问、设置、删除属性，并了解属性的继承关系和枚举特性。以下是一些关键概念：
场景和功能介绍
以下Node-API接口提供了对ArkTS对象属性的基本操作，包括设置、获取、删除和检查属性是否存在。使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_get_property_names | 在进行对象操作或调试时，有时需要获取对象的属性和属性名。此接口可以帮助提取对象的属性名，用于动态获取对象的属性信息的场景。 |
| napi_set_property | 通过此接口可以动态地向对象添加属性。也可修改对象的属性值，满足动态属性值变更的需求。 |
| napi_get_property | 在调用Node-API模块的函数或方法时，可能需要将ArkTS对象的属性值作为参数传递。通过此接口可以获取属性值，并将其传递给其他函数进行处理。 |
| napi_has_property | 在进行属性访问之前，通常需要先检查对象中是否存在指定的属性。通过调用此接口可以判断给定对象是否包含特定的属性，从而避免访问不存在属性导致的异常或错误。 |
| napi_delete_property | 在需要删除一个ArkTS对象上的某个属性时，可以使用这个函数。 |
| napi_has_own_property | 在需要检查一个ArkTS对象是否直接拥有（而不是从其原型链上继承）某个属性时，可以使用这个函数。 |
| napi_set_named_property | 在需要将一个值赋给ArkTS对象的命名属性时，可以使用这个函数。 |
| napi_get_named_property | 在需要从ArkTS对象中获取一个命名属性的值时，可以使用这个函数。 |
| napi_has_named_property | 在需要检查一个ArkTS对象是否包含某个命名属性时，可以使用这个函数。 |
| napi_define_properties | 当需要在指定Object中自定义属性，并从ArkTS中访问和操作这些属性时，可以使用这个函数。 |
| napi_get_all_property_names | 当需要遍历一个对象的所有属性，并对其进行处理时，可以使用此接口获取所有属性名称的数组，然后检查数组中是否包含特定的属性名。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_get_property_names
以字符串数组的形式获取对象的可枚举属性的名称。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getPropertyNames: (obj: Object) => Array<string> | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Obj {
data: number = 0
message: string = ""
}
let obj: Obj = { data: 0, message: "hello world"};
let propertyNames = testNapi.getPropertyNames(obj);
if (Array.isArray(propertyNames) && propertyNames.length > 0) {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_property_names: %{public}s', propertyNames[0]);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_property_names: %{public}s', propertyNames[1]);
}
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_property_names error: %{public}s', error.message);
}
```
napi_set_property
将给定的属性与值设置入给定的Object。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const setProperty: (obj: Object, key: String, value: string) => Object | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Obj {
data: number = 0
message: string = ""
}
let obj: Obj = { data: 0, message: "hello world"};
let result = testNapi.setProperty(obj, "code", "hi");
hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_property: %{public}s', JSON.stringify(result));
} catch (error) {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_property error: %{public}s', error.message);
}
```
napi_get_property
获取object指定的属性的值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getProperty: (obj: Object, key: string) => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Obj {
data: number = 0
message: string = ""
}
let obj: Obj = { data: 0, message: "hello world"};
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_property: %{public}s', testNapi.getProperty(obj, "message"));
} catch (error) {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_property error: %{public}s', error.message);
}
```
napi_has_property
检查对象中是否存在指定的属性，可以避免访问不存在属性导致的异常或错误。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const hasProperty: (obj: Object, key: number | string) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Obj {
data: number = 0
message: string = ""
}
let obj: Obj = { data: 0, message: "hello world"};
let resultFalse = testNapi.hasProperty(obj, 0);
let resultTrue = testNapi.hasProperty(obj, "data");
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_property: %{public}s', JSON.stringify(resultFalse));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_property: %{public}s', JSON.stringify(resultTrue));
} catch (error) {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_property error: %{public}s', error.message);
}
```
napi_delete_property
尝试从给定的Object中删除由key指定的属性，并返回操作的结果。
如果对象是一个不可扩展的对象，或者属性是不可配置的，则可能无法删除该属性。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const deleteProperty: (obj: Object, key:string) => boolean;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
class Obj {
first: number = 0;
}
let obj: Obj = { first: 1};
hilog.info(0x0000, 'testTag', 'Test Node-API napi_delete_property first: %{public}s', testNapi.deleteProperty(obj, 'first'));
// 设置新的属性为不可配置
// 这里的Object.defineProperty方法在DevEco Studio 4.1.0.400及其以上版本不支持，需在ts使用
Object.defineProperty(obj, 'config', {
configurable: false,
value: "value"
})
hilog.info(0x0000, 'testTag', 'Test Node-API napi_delete_property config: %{public}s', testNapi.deleteProperty(obj, 'config'));
```
napi_has_own_property
用于检查传入的Object是否具有自己的命名属性，不包括从原型链上继承的属性。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiHasOwnProperty: (obj: Object, key:string) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let myObj = { 'myProperty': 1 };
let inheritedObj = { 'inheritedProperty': 2 };
// 这里的Object.setPrototypeOf方法在DevEco Studio 4.1.0.400及其以上版本不支持，需在ts使用
Object.setPrototypeOf(myObj, inheritedObj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_own_property my: %{public}s', testNapi.napiHasOwnProperty(myObj, 'myProperty'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_own_property inherited: %{public}s', testNapi.napiHasOwnProperty(myObj, 'inheritedProperty'));
```
napi_set_named_property
用于在传入的ArkTS对象上设置一个命名属性。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiSetNamedProperty: (key: string) => Object | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let obj = testNapi.napiSetNamedProperty('myProperty');
let objAsString = JSON.stringify(obj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_named_property: %{public}s', objAsString);
```
napi_get_named_property
用于从ArkTS对象中获取命名属性的值。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiGetNamedProperty: (obj: Object, key:string) => boolean | number | string | Object | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
interface NestedObj {
nestedStr: string;
nestedNum: number;
}
class Obj {
str: string = "";
num: number = 0;
bol: boolean = false;
nestedObj: NestedObj = { nestedStr: "", nestedNum: 0 };
}
let obj: Obj = {str: "bar", num: 42, bol: true,
nestedObj: { nestedStr: "nestedValue", nestedNum: 123 }};
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}s', testNapi.napiGetNamedProperty(obj, 'str'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}d', testNapi.napiGetNamedProperty(obj, 'num'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}s', testNapi.napiGetNamedProperty(obj, 'bol'));
let nestedObj = testNapi.napiGetNamedProperty(obj, 'nestedObj');
let objAsString = JSON.stringify(nestedObj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}s', objAsString);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}s', testNapi.napiGetNamedProperty(obj, 'null'));
```
napi_has_named_property
用于检查ArkTS对象中是否包含指定的命名属性。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const napiHasNamedProperty: (obj: Object, key:string) => boolean | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
interface NestedObj {
nestedStr: string;
nestedNum: number;
}
class Obj {
str: string = "";
num: number = 0;
bol: boolean = false;
nestedObj: NestedObj = { nestedStr: "", nestedNum: 0 };
}
let obj: Obj = {str: "bar", num: 42, bol: true,
nestedObj: { nestedStr: "nestedValue", nestedNum: 123 }};
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_named_property : %{public}s', testNapi.napiHasNamedProperty(obj, 'str'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_named_property : %{public}s', testNapi.napiHasNamedProperty(obj, 'nestedStr'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_named_property : %{public}s', testNapi.napiHasNamedProperty(obj, 'bol'));
```
napi_define_properties
用于定义对象的属性。
cpp部分代码
接口声明
```typescript
// index.d.ts
export class DefineMethodObj {
defineMethodPropertiesExample: Function;
}
export class DefineStringObj {
defineStringPropertiesExample: string;
}
export class DefineGetterSetterObj {
getterCallback: Function;
setterCallback: Function;
}
export const defineMethodProperties: () => DefineMethodObj;
export const defineStringProperties: () => DefineStringObj;
export const createStringWithGetterSetter: () => DefineGetterSetterObj;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 定义method类型的属性
hilog.info(0x0000, 'testTag', 'Test Node-API define_method_properties:%{public}d', testNapi.defineMethodProperties()
.defineMethodPropertiesExample());
// 定义string类型的属性
hilog.info(0x0000, 'testTag', 'Test Node-API define_string_properties::%{public}s ', testNapi.defineStringProperties()
.defineStringPropertiesExample);
// getter和setter
hilog.info(0x0000, 'testTag', 'Test Node-API get::%{public}s ', testNapi.createStringWithGetterSetter()
.getterCallback());
hilog.info(0x0000, 'testTag', 'Test Node-API setter::%{public}s ', testNapi.createStringWithGetterSetter()
.setterCallback('set data'));
```
napi_get_all_property_names
用于获取传入的ArkTS对象的所有属性名。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getAllPropertyNames : (obj: Object) => Array<string> | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
try {
class Obj {
data: number = 0
message: string = ""
}
let obj: Obj = { data: 0, message: "hello world"};
let propertyNames = testNapi.getAllPropertyNames(obj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_all_property_names: %{public}s', JSON.stringify(propertyNames));
} catch (error) {
hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_all_property_names error: %{public}s', error.message);
}
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-string-V14
爬取时间: 2025-04-30 06:20:56
来源: Huawei Developer
简介
使用Node-API关于string的六个接口，可以让Node-API模块和ArkTS字符串进行交互。
基本概念
string是编程中常用的数据类型之一。它可以存储和操作文本数据，用于表示和处理字符序列。还可用于构建用户界面元素，如标签、按钮和文本框，处理用户输入，验证和格式化输入数据。不同的编码支持不同的字符集和语言，以下是一些主要的编码方案及其区别：
场景和功能介绍
以下Node-API接口主要用于string的创建和获取，使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_get_value_string_utf8 | 需要将ArkTS的字符类型的数据转换为utf8编码的字符时使用这个函数。 |
| napi_create_string_utf8 | 需要通过UTF8编码的C字符串创建ArkTS string值时使用这个函数。 |
| napi_get_value_string_utf16 | 需要将ArkTS的字符类型的数据转换为utf16编码的字符时使用这个函数。 |
| napi_create_string_utf16 | 需要通过UTF16编码的C字符串创建ArkTS string值时使用这个函数。 |
| napi_get_value_string_latin1 | 需要将ArkTS的字符类型的数据转换为ISO-8859-1编码的字符时使用这个函数。 |
| napi_create_string_latin1 | 需要通过ISO-8859-1编码的字符串创建ArkTS string值时使用这个函数。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_get_value_string_utf8
将ArkTS的字符类型的数据转换为utf8编码的字符。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueStringUtf8: (param: string | number) => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 分别传入字符和非字符检测接口，传入字符串类型的数据将返回原字符串，传入其他类型返回undefined
hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_utf8_string %{public}s', testNapi.getValueStringUtf8('aaBC+-$%^你好123'));
hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_utf8_not_string %{public}s', testNapi.getValueStringUtf8(50));
```
napi_create_string_utf8
用于创建一个UTF-8编码的ArkTS字符串。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createStringUtf8: () => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_string_utf8:%{public}s', testNapi.createStringUtf8());
```
napi_get_value_string_utf16
将ArkTS的字符类型的数据转换为utf16编码的字符。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueStringUtf16: (data: string) => string;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
let result = testNapi.getValueStringUtf16('hello,');
hilog.info(0x0000,'testTag','Node-API napi_get_value_string_utf16:%{public}s', result);
```
napi_create_string_utf16
用于创建一个UTF-16编码的ArkTS字符串。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createStringUtf16: () => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_string_utf16:%{public}s ', testNapi.createStringUtf16());
```
napi_get_value_string_latin1
将ArkTS的字符类型的数据转换为ISO-8859-1编码的字符。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const getValueStringLatin1: (param: number | string) => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
// 传入非字符型数据，函数返回undefined
hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_latin1_not_string %{public}s', testNapi.getValueStringLatin1(10));
// ISO-8859-1编码不支持中文，传入中文字符会乱码
hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_latin1_string_chinese %{public}s', testNapi.getValueStringLatin1('中文'));
// 传入其他字符，不会乱码
hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_latin1_string %{public}s', testNapi.getValueStringLatin1('abo ABP=-&*/'));
```
napi_create_string_latin1
用于创建一个Latin1编码的ArkTS字符串。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const createStringLatin1: () => string | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
hilog.info(0x0000, 'testTag', 'Test Node-API  napi_create_string_latin1:%{public}s', testNapi.createStringLatin1());
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-about-custom-asynchronous-operations-V14
爬取时间: 2025-04-30 06:21:09
来源: Huawei Developer
简介
使用Node-API的自定义异步操作功能，可以使ArkTS的使用更加灵活和高效，可以处理那些可能阻塞事件循环的长时间运行任务，同时保持ArkTS应用的响应性和性能。
基本概念
Node-API支持异步操作，这对于处理IO密集型或计算密集型的任务非常重要，因为这些任务通常需要非阻塞的执行方式以避免阻塞主线程。以下是一些关于自定义异步操作的基本概念：
场景和功能介绍
这些Node-API接口可以在Node-API模块中执行异步操作、进行ArkTS回调以及管理相关资源的生命周期。通过使用这些函数，可以有效地与ArkTS环境进行交互，并实现复杂的异步操作。他们的使用场景如下：
| 接口 | 描述 |
| --- | --- |
| napi_async_init、napi_async_destroy | 用于创建和销毁异步资源上下文环境。这些函数可以用于处理长时间运行的异步操作，例如文件I/O操作、网络请求等。在这些情况下，创建异步资源上下文环境，执行必要的异步任务，然后销毁资源以释放相关的资源和内容。 |
| napi_make_callback | 用于在异步资源上下文环境中执行ArkTS回调函数。在处理异步操作的结果后，将结果传递回ArkTS代码。 |
| napi_open_callback_scope、napi_close_callback_scope | 用于创建和关闭回调作用域。在异步操作期间执行ArkTS代码并管理其上下文。 |
使用示例
Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。
napi_async_init、napi_async_destroy
在需要管理异步资源上下文环境的创建和销毁时，可以使用napi_async_init和napi_async_destroy来管理这些环境。需要注意的是，这些函数不支持与async_hook相关的能力，所以在使用时需要注意可能会存在的限制。
napi_make_callback
在编写Node-API模块时，需要在异步操作完成后调用ArkTS回调函数。可以使用napi_async_init创建异步资源上下文环境，然后使用napi_make_callback在该环境中执行ArkTS回调函数。
napi_open_callback_scope、napi_close_callback_scope
在需要创建一个回调作用域来确保异步操作期间ArkTS环境仍然可用时。可以使用napi_open_callback_scope创建回调作用域，然后在异步操作完成后使用napi_close_callback_scope关闭该作用域。
cpp部分代码
接口声明
```typescript
// index.d.ts
export const asynchronousWork: (object: Object, obj: Object, fun: Function, num: number) => number | void;
```
ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog'
import testNapi from 'libentry.so'
import process from '@ohos.process'
try {
hilog.info(0x0000, 'testTag', 'Test Node-API asynchronousWork: %{public}d', testNapi.asynchronousWork({}, process.ProcessManager, (num: number)=>{return num;}, 123));
} catch (error) {
hilog.error(0x0000, 'testTag', 'Test Node-API asynchronousWork error: %{public}s', error.message);
}
```
以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/napi-scenarios-V14
爬取时间: 2025-04-30 06:21:23
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-asynchronous-task-V14
爬取时间: 2025-04-30 06:21:36
来源: Huawei Developer
场景介绍
napi_create_async_work是Node-API接口之一，用于创建一个异步工作对象。可以在需要执行耗时操作的场景中使用，以避免阻塞主线程，确保应用程序的性能和响应性能。例如以下场景：
-  文件操作：读取大型文件或执行复杂的文件操作时，可以使用异步工作对象来避免阻塞主线程。
-  网络请求：当需要进行网络请求并等待响应时，使用异步工作对象可以确保主线程不被阻塞，从而提高应用程序的响应性能。
-  数据库操作：当需要执行复杂的数据库查询或写入操作时，使用异步工作对象可以确保主线程不被阻塞，从而提高应用程序的并发性能。
-  图像处理：当需要对大型图像进行处理或执行复杂的图像算法时，使用异步工作对象可以确保主线程不被阻塞，从而提高应用程序的实时性能。
异步调用支持callback方式和Promise方式，使用哪种方式由应用开发者决定，通过是否传递callback函数进行区分。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165815.09410687008205315217691720445997:50001231000000:2800:16CCD5F7784A9628FC3A9F94094CB96B005CC8B67A94AE15F3D4B8689EE989E6.png)
使用Promise方式示例
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165815.02966769689325389872828941027693:50001231000000:2800:68C995B753D195648DFEFA7C35598CDC1E417EFBA0688F7C1C8CC2A719EED66D.png)
1.  使用napi_create_async_work创建异步任务，并使用napi_queue_async_work将异步任务加入队列，等待执行。
2.  定义异步任务的第一个回调函数，该函数在工作线程中执行，处理具体的业务逻辑。
3.  定义异步任务的第二个回调函数，该函数在主线程执行，将结果传递给ArkTS侧。
4.  模块初始化以及ArkTS侧调用接口。
使用callback方式示例
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165815.10895344307105826325986797661318:50001231000000:2800:DD3EAE719A61DD06A5D52031800A0EBD0C5F2C4C57A27308407EE87892450F36.png)
1.  使用napi_create_async_work创建异步任务，并使用napi_queue_async_work将异步任务加入队列，等待执行。
2.  定义异步任务的第一个回调函数，该函数在工作线程中执行，处理具体的业务逻辑。
3.  定义异步任务的第二个回调函数，该函数在主线程执行，将结果传递给ArkTS侧。
4.  模块初始化以及ArkTS侧调用接口。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-thread-safety-V14
爬取时间: 2025-04-30 06:21:50
来源: Huawei Developer
场景介绍
napi_create_threadsafe_function是Node-API接口之一，用于创建一个线程安全的JavaScript函数。主要用于在多个线程之间共享和调用，而不会出现竞争条件或死锁。例如以下场景：
-  异步计算：如果需要进行耗时的计算或IO操作，可以创建一个线程安全的函数，将计算或IO操作放在另一个线程中执行，避免阻塞主线程，提高程序的响应速度。
-  数据共享：如果多个线程需要访问同一份数据，可以创建一个线程安全的函数，确保数据的读写操作不会发生竞争条件或死锁等问题。
-  多线程编程：如果需要进行多线程编程，可以创建一个线程安全的函数，确保多个线程之间的通信和同步操作正确无误。
使用示例
1.  在Native入口定义线程安全函数。
2.  在工作线程中调用ExecuteWork，并执行线程安全函数。
3.  在JS线程执行异步回调函数。
4.  任务执行完成后，进行资源清理回收。
5.  模块初始化以及ArkTS侧调用接口。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-object-wrap-V14
爬取时间: 2025-04-30 06:22:03
来源: Huawei Developer
场景介绍
通过napi_wrap将ArkTS对象与Native的C++对象绑定，后续操作时再通过napi_unwrap将ArkTS对象绑定的C++对象取出，并对其进行操作。
使用示例
1.  接口声明、编译配置以及模块注册 接口声明 编译配置 模块注册
```typescript
// index.d.ts
export class MyObject {
constructor(arg: number);
plusOne: () => number;
public get value();
public set value(newVal: number);
}
```
2.  在构造函数中绑定ArkTS与C++对象
3.  将ArkTS对象之前绑定的C++对象取出，并对其进行操作
4.  ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog';
import { MyObject } from 'libentry.so';
let object : MyObject = new MyObject(0);
object.value = 1023;
hilog.info(0x0000, 'testTag', 'MyObject value after set: %{public}d', object.value);
hilog.info(0x0000, 'testTag', 'MyObject plusOne: %{public}d', object.plusOne());
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-sendable-napi-V14
爬取时间: 2025-04-30 06:22:16
来源: Huawei Developer
场景介绍
通过napi_wrap_sendable将Sendable ArkTS对象与Native的C++对象绑定，后续操作时再通过napi_unwrap_sendable将ArkTS对象绑定的C++对象取出，并对其进行操作。
使用示例
1.  接口声明、编译配置以及模块注册 接口声明 编译配置 模块注册
```typescript
// index.d.ets
@Sendable
export class MyObject {
constructor(arg: number);
plusOne(): number;
public get value();
public set value(newVal: number);
}
```
2.  在构造函数中绑定Sendable ArkTS与C++对象
3.  将Sendable ArkTS对象之前绑定的C++对象取出，并对其进行操作
4.  ArkTS侧示例代码
```typescript
import hilog from '@ohos.hilog';
import { MyObject } from 'libentry.so';
let object : MyObject = new MyObject(0);
object.value = 1023;
hilog.info(0x0000, 'testTag', 'MyObject value after set: %{public}d', object.value);
hilog.info(0x0000, 'testTag', 'MyObject plusOne: %{public}d', object.plusOne());
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-ark-runtime-V14
爬取时间: 2025-04-30 06:22:30
来源: Huawei Developer
场景介绍
开发者通过pthread_create创建新线程后，可以通过napi_create_ark_runtime来创建一个新的ArkTS基础运行时环境，并通过该运行时环境加载ArkTS模块。当使用结束后，开发者需要通过napi_destroy_ark_runtime来销毁所创建的ArkTS基础运行时环境。
约束限制
一个进程最多只能创建16个运行时环境。
使用示例
1.  接口声明、编译配置以及模块注册。 接口声明 编译配置 在当前模块的build-profile.json5文件中进行以下配置： 模块注册
```typescript
// index.d.ts
export const createArkRuntime: () => object;
```
2.  新建线程并创建ArkTS基础运行时环境，加载自定义模块请参考napi_load_module_with_info。
3.  编写ArkTS侧示例代码。
```typescript
// ObjectUtils.ets
export function Logger() {
console.log("print log");
}
// ArkTS侧调用接口
import testNapi from 'libentry.so';
testNapi.createArkRuntime();
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-load-module-V14
爬取时间: 2025-04-30 06:22:43
来源: Huawei Developer
场景介绍
Node-API中的napi_load_module接口的功能是在主线程中进行模块的加载，当模块加载出来之后，可以使用函数napi_get_property获取模块导出的变量，也可以使用napi_get_named_property获取模块导出的函数，目前支持以下场景：
函数说明
| 参数 | 说明 |
| --- | --- |
| env | 当前的虚拟机环境 |
| path | 加载的文件路径或者模块名 |
| result | 加载的模块 |
使用限制
建议使用napi_load_module_with_info来进行模块加载，该接口支持了更多的场景。
加载系统模块使用示例
使用napi_load_module导出系统模块hilog，并调用info函数。
加载ArkTS文件中的模块使用示例
当加载文件中的模块时，如以下ArkTS代码：
1.  需要在工程的build-profile.json5文件中进行以下配置：
```json
{
"buildOption" : {
"arkOptions" : {
"runtimeOnly" : {
"sources": [
"./src/main/ets/Test.ets"
]
}
}
}
}
```
2.  使用napi_load_module加载Test文件，调用函数test以及获取变量value：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-event-loop-V14
爬取时间: 2025-04-30 06:22:56
来源: Huawei Developer
场景介绍
开发者在自己创建的ArkTS运行环境中调用异步的ArkTS接口时，可以通过使用Node-API中的扩展接口napi_run_event_loop和napi_stop_event_loop来运行和停止ArkTS实例中的事件循环。
调用异步的ArkTS接口示例
调用的ArkTS接口为异步接口时，需要通过扩展接口napi_run_event_loop将异步线程中的事件循环运行起来，底层事件队列中的异步任务将被处理执行。当前Node-API扩展了两种事件循环模式来运行异步线程的事件循环，分别为napi_event_mode_nowait模式和napi_event_mode_default模式。
如果使用napi_event_mode_nowait模式运行底层事件循环，系统会尝试从底层的事件队列中取出一个任务并处理，完成之后事件循环停止，如果底层的事件队列中没有任务，事件循环会立刻停止，当前的异步线程不会被阻塞；
如果使用napi_event_mode_default模式来运行底层事件循环，系统会阻塞当前的线程，同时会一直尝试从事件队列中获取任务并执行处理这些任务。如果不想当前线程继续被阻塞，可以使用扩展接口napi_stop_event_loop将正在运行的事件循环停止。
示例代码
-  模块注册
-  接口声明
```typescript
// index.d.ts
export const runEventLoop: (isDefault: boolean) => object;
```
-  编译配置
```json
{
"buildOption" : {
"arkOptions" : {
"runtimeOnly" : {
"sources": [
"./src/main/ets/pages/ObjectUtils.ets"
]
}
}
}
}
```
```typescript
// index.ets
import testNapi from 'libentry.so'
testNapi.runEventLoop(true);
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-load-module-with-info-V14
爬取时间: 2025-04-30 06:23:10
来源: Huawei Developer
Node-API中的napi_load_module_with_info接口的功能是进行模块的加载，当模块加载出来之后，可以使用函数napi_get_property获取模块导出的变量，也可以使用napi_get_named_property获取模块导出的函数，该函数可以在新创建的ArkTS基础运行时环境中使用。
函数说明
| 参数 | 说明 |
| --- | --- |
| env | 当前的虚拟机环境 |
| path | 加载的文件路径或者模块名 |
| module_info | bundleName/moduleName的路径拼接 |
| result | 加载的模块 |
napi_load_module_with_info支持的场景
| 场景 | 详细分类 | 说明 |
| --- | --- | --- |
| 本地工程模块 | 加载模块内文件路径 | 要求路径以moduleName开头 |
| 本地工程模块 | 加载HAR模块名 | - |
| 远程包 | 加载远程HAR模块名 | - |
| 远程包 | 加载ohpm包名 | - |
| API | 加载@ohos.或 @system. | - |
| 模块Native库 | 加载libNativeLibrary.so | - |
异常场景
使用示例
当加载文件中的模块时，如以下ArkTS代码：
1.  需要当前模块的build-profile.json5文件中进行以下配置：
```json
{
"buildOption" : {
"arkOptions" : {
"runtimeOnly" : {
"sources": [
"./src/main/ets/Test.ets"
]
}
}
}
}
```
2.  使用napi_load_module_with_info加载Test文件，调用函数test以及获取变量value。 开启useNormalizedOHMUrl后(即将工程目录中与entry同级别的应用级build-profile.json5文件中strictMode属性的useNormalizedOHMUrl字段配置为true)，加载模块内文件路径时：1、bundleName不会影响最终加载逻辑，会智能通过module名索引进程内对应的hap，例如：工程的bundleName为com.example.application，实际入参时填写为 com.example.application1，模块也能正常加载。2、路径需要以packageName开头，packageName指的是模块的oh-package.json5中配置的name字段。
HAR包Index.ets文件如下：
1.  在oh-package.json5文件中配置dependencies项：
```json
{
"dependencies": {
"library": "file:../library"
}
}
```
2.  在使用library的模块中，对build-profile.json5进行配置：
```json
{
"buildOption" : {
"arkOptions" : {
"runtimeOnly" : {
"packages": [
"library"
]
}
}
}
}
```
3.  用napi_load_module_with_info加载library，调用函数test以及获取变量value：
1.  在oh-package.json5文件中配置dependencies项：
```json
{
"dependencies": {
"@ohos/hypium": "1.0.16"
}
}
```
2.  在使用@ohos/hypium的模块中，对build-profile.json5进行配置：
```json
{
"buildOption" : {
"arkOptions" : {
"runtimeOnly" : {
"packages": [
"@ohos/hypium"
]
}
}
}
}
```
3.  用napi_load_module_with_info加载@ohos/hypium，获取DEFAULT变量：
1.  在oh-package.json5文件中配置dependencies项：
```json
{
"dependencies": {
"json5": "^2.2.3"
}
}
```
2.  在使用json5的模块中，对build-profile.json5进行配置：
```json
{
"buildOption" : {
"arkOptions" : {
"runtimeOnly" : {
"packages": [
"json5"
]
}
}
}
}
```
3.  用napi_load_module_with_info加载json5，调用函数stringify：
libentry.so的index.d.ts文件如下：
1.  在oh-package.json5文件中配置dependencies项：
```json
{
"dependencies": {
"libentry.so": "file:../src/main/cpp/types/libentry"
}
}
```
2.  在使用libentry.so的模块中，对build-profile.json5进行配置：
```json
{
"buildOption" : {
"arkOptions" : {
"runtimeOnly" : {
"packages": [
"libentry.so"
]
}
}
}
}
```
3.  用napi_load_module_with_info加载libentry.so，调用函数add：
场景为har1加载har2，har2中的Index.ets文件如下：
1.  在har1中的oh-package.json5文件中配置dependencies项：
```json
{
"dependencies": {
"har2": "file:../har2"
}
}
```
2.  在har1的build-profile.json5文件中进行配置：
```json
{
"buildOption" : {
"arkOptions" : {
"runtimeOnly" : {
"packages": [
"har2"
]
}
}
}
}
```
3.  在har1中用napi_load_module_with_info加载har2，调用函数test以及获取变量value：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-call-threadsafe-function-with-priority-V14
爬取时间: 2025-04-30 06:23:24
来源: Huawei Developer
Node-API中的napi_call_threadsafe_function_with_priority接口的功能是从异步线程向ArkTS线程投递任务，底层队列会根据任务的优先级和入队方式来处理任务。
函数说明
| 参数 | 说明 |
| --- | --- |
| func | 线程安全方法 |
| data | 异步线程期望传递给主线程的数据 |
| priority | 指定任务的优先级napi_task_priority |
| isTail | 指定任务的入队方式，true代表任务从队列的尾部入队，false代表任务从队列的头部入队。 |
场景介绍
异步线程向ArkTS主线程投递的任务需要根据任务指定的优先级和入队方式进行处理。
调用异步的ArkTS接口示例
示例代码
-  模块注册
-  接口声明
```typescript
// index.d.ts
export const callThreadSafeWithPriority: (cb: (a: number, b: number) => number) => void;
```
-  编译配置 CMakeLists.txt文件需要按照如下配置
-  ArkTS代码示例
```typescript
// index.ets
import testNapi from 'libentry.so'
let callback = (a: number, b: number) : number => {
console.info('result is ' + (a + b))
return a + b;
}
testNapi.callThreadSafeWithPriority(callback);
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-napi-faqs-V14
爬取时间: 2025-04-30 06:23:39
来源: Huawei Developer
ArkTS/JS侧import xxx from libxxx.so后，使用xxx报错显示undefined/not callable或明确的Error message
1.  排查.cpp文件在注册模块时的模块名称与so的名称匹配一致。 如模块名为entry，则so的名字为libentry.so，napi_module中nm_modname字段应为entry，大小写与模块名保持一致。
2.  排查so是否加载成功。 应用启动时过滤模块加载相关日志，重点搜索"dlopen"关键字，确认是否有相关报错信息；常见加载失败原因有权限不足、so文件不存在以及so已拉入黑名单等，可根据以下关键错误日志确认问题。其中，多线程场景(worker、taskpool等)下优先检查模块实现中nm_modname是否与模块名一致，区分大小写。
3.  排查依赖的so是否加载成功。 确定所依赖的其它so是否打包到应用中以及是否有权限打开。常见加载失败原因有权限不足、so文件不存在等，可根据以下关键错误日志确认问题。
4.  排查模块导入方式与so路径是否对应。 若JS侧导入模块的形式为： import xxx from '@ohos.yyy.zzz'，则该so将在/system/lib/module/yyy中找libzzz.z.so或libzzz_napi.z.so，若so不存在或名称无法对应，则报错日志中会出现dlopen相关日志。 注意，32位系统路径为/system/lib，64位系统路径为/system/lib64。
| 已知关键错误日志 | 修改建议 |
| --- | --- |
| module $SO is not allowed to load in restricted runtime. | $SO表示模块名。该模块不在受限worker线程的so加载白名单，不允许加载，建议用户删除该模块。 |
| module $SO is in blocklist, loading prohibited. | $SO表示模块名。受卡片或者Extension管控，该模块在黑名单内，不允许加载，建议用户删除该模块。 |
| load module failed. $ERRMSG. | 动态库加载失败。$ERRMSG表示加载失败原因，一般常见原因是so文件不存在、依赖的so文件不存在或者符号未定义，需根据加载失败原因具体分析。 |
| try to load abc file from $FILEPATH failed. | 通常加载动态库和abc文件为二选一：如果是要加载动态库并且加载失败，该告警可以忽略；如果是要加载abc文件，则该错误打印的原因是abc文件不存在，$FILEPATH表示模块路径。 |
| Error message | 修改建议 |
| --- | --- |
| First attempt: $ERRMSG. | 首先加载后缀不拼接'_napi'的模块名为'xxx'的so，如果加载失败会有该错误信息，$ERRMSG表示具体加载时的错误信息。 |
| Second attempt: $ERRMSG. | 第二次加载后缀拼接'_napi'的模块名为'xxx_napi'的so，如果加载失败会有该错误信息，$ERRMSG表示具体加载时的错误信息。 |
| try to load abc file from xxx failed. | 第三次加载名字为'xxx'的abc文件，如果加载失败会有该错误信息。 |
| module xxx is not allowed to load in restricted runtime. | 该模块不允许在受限运行时中使用，xxx表示模块名，建议用户删除该模块。 |
| module xxx is in blocklist, loading prohibited. | 该模块不允许在当前extension下使用，xxx表示模块名，建议用户删除该模块。 |
接口执行结果非预期，日志显示occur exception need return
部分Node-API接口在调用结束前会进行检查，检查虚拟机中是否存在JS异常。如果存在异常，则会打印出occur exception need return日志，并打印出检查点所在的行号，以及对应的Node-API接口名称。
解决此类问题有以下两种思路：
-  若该异常开发者不关心，可以选择直接清除。 可直接使用napi接口napi_get_and_clear_last_exception，清理异常。调用时机：在打印occur exception need return日志的接口之前调用。
-  将该异常继续向上抛到ArkTS层，在ArkTS层进行捕获。 发生异常时，可以选择走异常分支， 确保不再走多余的Native逻辑 ，直接返回到ArkTS层。
napi_value和napi_ref的生命周期有何区别
-  native_value由HandleScope管理，一般开发者不需要自己加HandleScope（uv_queue_work的complete callback除外）。
-  napi_ref由开发者自己管理，需要手动delete。
Node-API接口返回值不是napi_ok时，如何排查定位
Node-API接口正常执行后，会返回一个napi_ok的状态枚举值，若napi接口返回值不为napi_ok，可从以下几个方面进行排查。
-  Node-API接口执行前一般会进行入参校验，首先进行的是判空校验。在代码中体现为：
-  某些Node-API接口还有入参类型校验。比如napi_get_value_double接口是获取JS number对应的C double值，首先就要保证的是：JS value类型为number，因此可以看到相关校验。
-  还有一些接口会对其执行结果进行校验。比如napi_call_function这个接口，其功能是执行一个JS function，当JS function中出现异常时，Node-API将会返回napi_pending_exception的状态值。
-  还有一些状态值需要根据相应Node-API接口具体分析：确认具体的状态值，分析这个状态值在什么情况下会返回，再排查具体出错原因。
napi_threadsafe_function内存泄漏，应该如何处理
napi_threadsafe_function（下文简称tsfn）在使用时，常常会调用 napi_acquire_threadsafe_function 来更改tsfn的引用计数，确保tsfn不会意外被释放。但在使用完成后，应该及时使用 napi_tsfn_release 模式调用 napi_release_threadsafe_function 方法，以确保在所有调用回调都执行完成后，其引用计数能回归到调用 napi_acquire_threadsafe_function 方法之前的水平。当其引用计数归为0时，tsfn才能正确的被释放。
当在env即将退出，但tsfn的引用计数未被归零时，应该使用 napi_tsfn_abort 模式调用 napi_release_threadsafe_function 方法，确保在env释放后不再对tsfn进行持有及使用。在env退出后，继续持有tsfn进行使用，是一种未定义的行为，可能会触发崩溃。
如下代码将展示通过注册 env_cleanup 钩子函数的方式，以确保在env退出后不再继续持有tsfn。
以下内容为主线程逻辑，主要用作创建worker线程和通知worker执行任务
```typescript
// 主线程 Index.ets
import worker, { MessageEvents } from '@ohos.worker';
const mWorker = new worker.ThreadWorker('../workers/Worker');
mWorker.onmessage = (e: MessageEvents) => {
const action: string | undefined = e.data?.action;
if (action === 'kill') {
mWorker.terminate();
}
}
// 触发方式的注册已省略
mWorker.postMessage({action: 'tsfn-demo'})
```
以下内容为Worker线程逻辑，主要用以触发Native任务
```typescript
// worker.ets
import worker, { ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@ohos.worker';
import napiModule from 'libentry.so'; // libentry.so: napi 库的模块名称
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
const action: string | undefined = e.data?.action;
if (action === 'tsfn-demo') {
// 触发 c++ 层的 tsfn demo
napiModule.myTsfnDemo();
// 通知主线程结束 worker
workerPort.postMessage({action: 'kill'});
};
}
```
napi_get_uv_event_loop接口错误码说明
在HarmonyOS中，对使用非法的napi_env作为napi_get_uv_event_loop入参的行为加入了额外的参数校验，这一行为将直接反映到该接口的返回值上。该接口返回值详情如下：
常见错误场景示例如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-V14
爬取时间: 2025-04-30 06:23:53
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-introduction-V14
爬取时间: 2025-04-30 06:24:06
来源: Huawei Developer
场景介绍
HarmonyOS JSVM-API是基于标准JS引擎提供的一套稳定的API，为开发者提供了较为完整的JS引擎能力，包括创建和销毁引擎，执行JS代码，JS/C++交互等关键能力。
HarmonyOS JSVM-API是C语言接口，遵循C99标准。
通过JSVM-API，开发者可以在应用运行期间直接执行一段动态加载的JS代码。也可以选择将一些对性能、底层系统调用有较高要求的核心功能用C/C++实现并将C++方法注册到JS侧，在JS代码中直接调用，提高应用的执行效率。
本文中如无特别说明，后续均使用JSVM-API指代HarmonyOS JSVM-API能力。
JSVM-API的组成架构
图1JSVM-API的组成架构
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165816.04359300862327404367569498686297:50001231000000:2800:522847B29320FB5540BB10FD98459FDFDCE659953548889BD02F8486A0CF6376.png)
-  Native Module：开发者使用JSVM-API开发的模块，用于在Native侧使用。
-  VM Life Cycle Manager：管理JSVM_VM的生命周期。
-  JS Context Manager：管理JSVM_Env的生命周期。
-  Context Snapshot：上下文快照，可用以缩短JS Context的创建时间。
-  JS Code Execute：执行JS代码。
-  JS/C++ Interaction：连接JS层与C++层，用于支撑JS与C++之间的交互。
-  Code Cache：编译后的JS代码的缓存，能提升JS代码执行的启动速度。
-  Debugger：调试器，用于调试JS代码。
-  CPU Profiler：该工具能记录JS代码执行所用的时间，使用此工具能帮助开发者分析JS代码的性能瓶颈，为代码优化提供数据支撑。
-  Heap Snapshot：JS堆内存分析/调优工具，可以进行内存优化和发现内存泄漏问题。
-  Heap Statistics：JS堆统计信息，包括内存大小及上下文数量。
-  Memory Adjustment：调整外部内存大小、虚拟机内存压力，以加快触发GC。
-  VM Information：JSVM_VM的信息。
-  Standard JS Engine：标准JS引擎。
JSVM-API的关键交互流程
图2JSVM-API的关键交互流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165816.90322212846433383078144796947227:50001231000000:2800:03D61BD07152F70A6687BC56D42EB0ED61046E0BEAF8455672C5FC7E967590AA.png)
JSVM-API和Native模块之间的交互流程，主要分为以下两步：
1.  初始化阶段：在Native模块上初始化JSVM和JS上下文，并完成Native函数的注册。Native方法将会被挂载到JS执行环境的全局上下文即GlobalThis。
2.  调用阶段：当JS侧调用通过JSVM-API注册到JS全局上下文的方法时，JS引擎会找到并调用对应的C/C++方法。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-data-types-interfaces-V14
爬取时间: 2025-04-30 06:24:21
来源: Huawei Developer
JSVM-API 的数据类型
JSVM_Status
JSVM_ExtendedErrorInfo
一个结构体，在调用函数不成功时存储了较为详细的错误信息。
JSVM_Value
在C++代码中，表示一个JavaScript值。
JSVM_Env
-  用于表示JSVM-API执行时的上下文，Native侧函数入参，并传递给函数中的JSVM-API接口。
-  退出Native侧插件时，JSVM_Env将失效，该事件通过回调传递给OH_JSVM_SetInstanceData。
-  禁止缓存JSVM_Env，禁止在不同Worker中传递JSVM_Env。
-  在不同线程间共享JSVM_Env时，要保证在线程切换时在前一个线程中关闭env scope并在新的线程中打开新的env scope，以保证threadlocal变量的线程隔离。
JSVM_ValueType
JSVM_Value的类型。包含了ECMAScript语言规范中定义的类型，其中JSVM_EXTERNAL表示外部数据类型。
JSVM_TypedarrayType
TypedArray的基本二进制标量数据类型。
JSVM_RegExpFlags
正则表达式标志位。
编译选项相关类型
JSVM_CompileOptions
配合编译接口 OH_JSVM_CompileScriptWithOptions 使用，是其参数中 options 数组的元素类型。
其中：
id 的值和 content 的类型需要对应使用，详细对应关系参考下面对各个选项类型的介绍。
JSVM_CompileOptionId
JSVM_CompileOptions 中的 id 对应类型， 每个值都有其对应的 content 类型, 其中 JSVM_COMPILE_ENABLE_SOURCE_MAP 对应的类型为 bool，当同时传入的 JSVM_ScriptOrigin 中 sourceMapUrl 不为空时生效。
JSVM_CompileMode
当 id 为 JSVM_COMPILE_MODE，content 的类型，每个值代表一种编译模式：
JSVM_CodeCache
当 id 为 JSVM_COMPILE_CODE_CACHE 时，content 的类型：
JSVM_ScriptOrigin
当 id 为 JSVM_COMPILE_SCRIPT_ORIGIN 时，content 的类型，存放待编译脚本的源码信息：
JSVM
内存管理类型
JSVM-API包含以下内存管理类型：
JSVM_HandleScope
JSVM_HandleScope数据类型是用来管理JavaScript对象的生命周期的。它允许JavaScript对象在一定范围内保持活动状态，以便在JavaScript代码中使用。在创建JSVM_HandleScope时，所有在该范围内创建的JavaScript对象都会保持活动状态，直到结束。这样可以避免在JavaScript代码中使用已经被释放的对象，从而提高代码的可靠性和性能。
JSVM_EscapableHandleScope
-  由OH_JSVM_OpenEscapableHandleScope接口创建，由OH_JSVM_CloseEscapableHandleScope接口关闭。
-  表示一种特殊类型的句柄范围，用于将在JSVM_EscapableHandleScope范围内创建的值返回给父scope。
-  用于OH_JSVM_EscapeHandle接口，将JSVM_EscapableHandleScope提升到JavaScript对象，以便在外部作用域使用。
JSVM_Ref
指向JSVM_Value，允许用户管理JavaScript值的生命周期。
JSVM_TypeTag
该结构体定义了一个包含两个无符号64位整数的类型标签，用于标识一个JSVM-API值的类型信息。
-  存储了两个无符号64位整数的128位值，用它来标记JavaScript对象，确保它们属于某种类型。
-  比OH_JSVM_Instanceof更强的类型检查，如果对象的原型被操纵，OH_JSVM_Instanceof可能会报告误报。
-  JSVM_TypeTag 在与 OH_JSVM_Wrap 结合使用时最有用，因为它确保从包装对象检索的指针可以安全地转换为与先前应用于JavaScript对象的类型标记相对应的Native类型。
回调类型
JSVM-API包含以下回调类型：
JSVM_CallbackStruct
用户提供的 Native callback 的回调函数指针和数据，JSVM_CallbackStruct 将通过 JSVM-API 暴露给 JavaScript。例如，可以使用 OH_JSVM_CreateFunction 接口创建绑定到 Native callback 的 JS 函数，其中 Native callback 就是通过 JSVM_CallbackStruct 结构定义。除非在对象生命周期管理中有特殊要求，一般不在此 callback 中创建 handle 或者 callback scope。
JSVM_Callback
JSVM_CallbackStruct 指针类型的类型别名。
定义如下:
JSVM_CallbackInfo
用户定义的 Native callback，第一个参数类型是 JSVM_Env，第二个参数类型是 JSVM_CallbackInfo。JSVM_CallbackInfo 表示从 JS 侧调用到 Native 侧时携带的调用信息，如参数列表。在实现 Native callback 时，一般使用 OH_JSVM_GetCbInfo 接口从 JSVM_CallbackInfo 中提取调用信息。
JSVM_Finalize
函数指针，用于传入OH_JSVM_SetInstanceData、OH_JSVM_CreateExternal、OH_JSVM_Wrap等接口。JSVM_Finalize在对象被回收时会被调用，可用于在JavaScript对象被垃圾回收时释放Native对象。
写法如下：
JSVM_PropertyHandlerConfigurationStruct
当执行对象的getter、setter、deleter和enumerator作时，对应的的回调将会触发。
JSVM_PropertyHandlerCfg
包含属性监听回调的结构的指针类型。
基本用法如下:
支持的JSVM-API接口
标准JS引擎的能力通过JSVM-API提供。JSVM-API支持动态链接到不同版本的JS引擎库，从而为开发者屏蔽掉不同引擎接口的差异。JSVM-API提供引擎生命周期管理、JS context管理、JS代码执行、JS/C++互操作、执行环境快照、codecache等能力，具体可见下文。
使用 JSVM-API 接口创建引擎实例及 JS 执行上下文环境
场景介绍
执行JS代码需要先创建JavaScript VM，创建JS执行的上下文环境。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_Init | 初始化JavaScript引擎实例 |
| OH_JSVM_CreateVM | 创建JavaScript引擎实例 |
| OH_JSVM_DestroyVM | 销毁JavaScript引擎实例 |
| OH_JSVM_OpenVMScope | 打开一个新的VM scope，引擎实例只能在scope范围内使用，可以保证引擎实例不被销毁 |
| OH_JSVM_CloseVMScope | 关闭VM scope |
| OH_JSVM_CreateEnv | 创建一个新的JS执行上下文环境，并注册指定的Native函数 |
| OH_JSVM_DestroyEnv | 销毁一个JS执行上下文环境 |
| OH_JSVM_OpenEnvScope | 打开一个新的Env scope，Env只能在scope范围内使用 |
| OH_JSVM_CloseEnvScope | 关闭Env scope |
| OH_JSVM_OpenHandleScope | 打开一个Handle scope，确保scope范围内的JSVM_Value不被GC回收 |
| OH_JSVM_CloseHandleScope | 关闭Handle scope |
JSVM_InitOptions 的使用描述
通过传入 JSVM_InitOptions 可以初始化具备不同能力的 VM 平台。
场景示例：
常规模式下初始化 VM 平台
场景示例：
初始化低内存占用的 VM 平台
场景示例：
初始化低GC触发频次的 VM 平台
执行结果：
使用以上三个接口可以分别初始化具备不同能力的 VM 平台。初始化之后，可以创建 VM 实例，并执行 JavaScript 脚本。其中，
调用 LowGCFrequencyInit 接口进行 VM 平台初始化执行 JavaScript 脚本，相比调用 NormalInit 接口所触发的 GC 频次更低。调用 LowMemoryInit 接口进行 VM 平台初始化执行 JavaScript 脚本，相比调用 NormalInit 接口所占用内存更少。
创建 VM 实例
场景示例:
创建及销毁JavaScript引擎实例，包含创建及销毁JS执行上下文环境
使用 JSVM-API 接口编译及执行 JS 代码
场景介绍
编译及执行JS代码。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CompileScript | 编译JavaScript代码并返回绑定到当前环境的编译脚本 |
| OH_JSVM_CompileScriptWithOrigin | 编译JavaScript代码并返回绑定到当前环境的编译脚本，同时传入包括 sourceMapUrl 和源文件名在内的源代码信息，用于处理 source map 信息 |
| OH_JSVM_CompileScriptWithOptions | 通用的编译接口，通过传入 option 数组完成前面的 compile 接口全部功能，同时支持后续选项扩展 |
| OH_JSVM_CreateCodeCache | 为编译脚本创建code cache |
| OH_JSVM_RunScript | 执行编译脚本 |
场景示例：
编译及执行JS代码(创建vm，注册function，执行js，销毁vm)。
使用 JSVM-API WebAssembly 接口编译 wasm module
场景介绍
JSVM-API WebAssembly 接口提供了 wasm 字节码编译、wasm 函数优化、wasm cache 序列化和反序列化的能力。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CompileWasmModule | 将 wasm 字节码同步编译为 wasm module。如果提供了 cache 参数，先尝试将 cache 反序列为 wasm module，反序列化失败时再执行编译。 |
| OH_JSVM_CompileWasmFunction | 将 wasm module 中指定编号的函数编译为优化后的机器码，目前只使能了最高的优化等级，函数编号的合法性由接口调用者保证。 |
| OH_JSVM_IsWasmModuleObject | 判断传入的值是否是一个 wasm module。 |
| OH_JSVM_CreateWasmCache | 将 wasm module 中的机器码序列化为 wasm cache，如果 wasm module 不包含机器码，则会序列化失败。 |
| OH_JSVM_ReleaseCache | 释放由 JSVM 接口生成的 cache。传入的 cacheType 和 cacheData 必须匹配，否则会产生未定义行为。 |
场景示例
详见使用 JSVM-API WebAssembly 接口。
异常处理
场景介绍
获取、抛出、清理JS异常
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_Throw | 抛出一个JS值 |
| OH_JSVM_ThrowTypeError | 抛出一个JS TypeError |
| OH_JSVM_ThrowRangeError | 抛出一个JS RangeError |
| OH_JSVM_IsError | 判断JS值是否为JS异常 |
| OH_JSVM_CreateError | 创建一个JS异常 |
| OH_JSVM_CreateTypeError | 创建一个JS TypeError并返回 |
| OH_JSVM_CreateRangeError | 创建一个JS RangeError并返回 |
| OH_JSVM_ThrowError | 抛出一个JS异常 |
| OH_JSVM_GetAndClearLastException | 清理并返回最后一个JS异常 |
| OH_JSVM_IsExceptionPending | 判断当前是否有异常 |
| OH_JSVM_GetLastErrorInfo | 获取最后一个异常的信息 |
| OH_JSVM_ThrowSyntaxError | 抛出一个JS SyntaxError |
| OH_JSVM_CreateSyntaxError | 创建一个JS SyntaxError并返回 |
场景示例：
以TypeError为例。创建，判断，并抛出JS TypeError。
使用OH_JSVM_GetAndClearLastException后将异常信息以字符串形式打印
对象生命周期管理
在调用JSVM-API接口时，底层VM堆中的对象可能会作为JSVM_Values返回句柄。这些句柄必须在Native方法退出或主动释放掉前，使其关联的对象处于“活动”状态，防止被引擎回收掉。
当对象句柄被返回时，它们与一个“scope”相关联。默认作用域的生命周期与本机方法调用的生命周期相关联，这些句柄及关联的对象将在Native方法的生命周期内保持活动状态。
然而，在许多情况下，句柄必须保持有效的时间范围并不与Native方法的生命周期相同。下面将介绍可用于更改句柄的生命周期的JSVM-API方法。
对象生命周期管理接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_OpenHandleScope | 打开一个新的scope，在关闭该scope之前创建的对象在scope范围内不会被GC回收 |
| OH_JSVM_CloseHandleScope | 关闭一个scope，在此scope范围内创建的对象在关闭scope后可以被GC回收 |
| OH_JSVM_OpenEscapableHandleScope | 打开一个新的scope逃逸handle scope，在关闭该scope之前创建的对象与父作用域有相同的生命周期 |
| OH_JSVM_CloseEscapableHandleScope | 关闭一个scope，在此scope范围外创建的对象不受父作用域保护 |
| OH_JSVM_EscapeHandle | 将 JavaScript 对象的句柄提升到外部作用域，确保在外部作用域中可以持续地使用该对象 |
| OH_JSVM_CreateReference | 以指定的引用计数为JavaScript对象创建一个新的引用，该引用将指向传入的对象，引用允许在不同的上下文中使用和共享对象，并且可以有效地监测对象的生命周期 |
| OH_JSVM_DeleteReference | 释放由 OH_JSVM_CreateReference 创建的引用，确保对象在不再被使用时能够被正确地释放和回收，避免内存泄漏 |
| OH_JSVM_ReferenceRef | 增加由OH_JSVM_CreateReference 创建的引用的引用计数，以确保对象在有引用时不会被提前释放 |
| OH_JSVM_ReferenceUnref | 减少由OH_JSVM_CreateReference 创建的引用的引用计数，以确保没有任何引用指向该对象时能正确地释放和回收 |
| OH_JSVM_GetReferenceValue | 返回由 OH_JSVM_CreateReference 创建的引用的对象 |
| OH_JSVM_RetainScript | 持久化保存一个 JSVM_Script, 使其能够跨过当前 scope 使用 |
| OH_JSVM_ReleaseScript | 释放持久化保存过的 JSVM_Script，释放之后 JSVM_Script 不再可用，应当置为空 |
场景示例：
通过handlescope保护在scope范围内创建的对象在该范围内不被回收。
通过escapable handlescope保护在scope范围内创建的对象在父作用域范围内不被回收
通过CreateReference创建对象引用和释放
通过 RetainScript 持久化保存 JSVM_Script 并使用
创建JS对象类型和基本类型
场景介绍
创建JS对象类型和基本类型
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CreateArray | 创建一个新的 JavaScript 数组对象 |
| OH_JSVM_CreateArrayWithLength | 创建一个指定长度的 JavaScript 数组对象 |
| OH_JSVM_CreateArraybuffer | 创建一个指定大小的 ArrayBuffer 对象 |
| OH_JSVM_CreateDate | 创建了一个表示给定毫秒数的 Date 对象 |
| OH_JSVM_CreateExternal | 创建一个包装了外部指针的 JavaScript 对象 |
| OH_JSVM_CreateObject | 创建一个默认的JavaScript Object对象 |
| OH_JSVM_CreateSymbol | 根据给定的描述符创建一个 Symbol 对象 |
| OH_JSVM_SymbolFor | 在全局注册表中搜索具有给定描述的现有Symbol,如果该Symbol已经存在，它将被返回，否则将在注册表中创建一个新Symbol |
| OH_JSVM_CreateTypedarray | 在现有的 ArrayBuffer 上创建一个 JavaScript TypedArray 对象,TypedArray 对象在底层数据缓冲区上提供类似数组的视图，其中每个元素都具有相同的底层二进制标量数据类型 |
| OH_JSVM_CreateDataview | 在现有的 ArrayBuffer 上创建一个 JavaScript DataView 对象,DataView 对象在底层数据缓冲区上提供类似数组的视图 |
| OH_JSVM_CreateInt32 | 根据 Int32_t 类型对象创建 JavaScript number 对象 |
| OH_JSVM_CreateUint32 | 根据 Uint32_t 类型对象创建 JavaScript number 对象 |
| OH_JSVM_CreateInt64 | 根据 Int64_t 类型对象创建 JavaScript number 对象 |
| OH_JSVM_CreateDouble | 根据 Double 类型对象创建 JavaScript number 对象 |
| OH_JSVM_CreateBigintInt64 | 根据 Int64 类型对象创建 JavaScript Bigint 对象 |
| OH_JSVM_CreateBigintUint64 | 根据 Uint64 类型对象创建 JavaScript Bigint 对象 |
| OH_JSVM_CreateBigintWords | 根据给定的 Uint64_t 数组创建一个 JavaScript BigInt 对象 |
| OH_JSVM_CreateStringLatin1 | 根据 Latin-1 编码的字符串创建一个 JavaScript string 对象 |
| OH_JSVM_CreateStringUtf16 | 根据 Utf16 编码的字符串创建一个 JavaScript string 对象 |
| OH_JSVM_CreateStringUtf8 | 根据 Utf8 编码的字符串创建一个 JavaScript string 对象 |
| OH_JSVM_CreateMap | 创建一个新的 JavaScript Map对象 |
| OH_JSVM_CreateRegExp | 根据输入的字符串创建一个JavaScript 正则对象 |
| OH_JSVM_CreateSet | 创建一个新的 JavaScript Set对象 |
场景示例:
创建指定长度的数组。
创建typedarray，以Int32Array为例：
创建number和string:
创建Map:
创建RegExp:
创建Set:
从JS类型获取C类型&获取JS类型信息
场景介绍
从JS类型获取C类型&获取JS类型信息。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_GetArrayLength | 返回 Array 对象的长度 |
| OH_JSVM_GetArraybufferInfo | 检索 ArrayBuffer 的底层数据缓冲区及其长度 |
| OH_JSVM_GetPrototype | 获取给定 JavaScript 对象的原型 |
| OH_JSVM_GetTypedarrayInfo | 获取 TypedArray（类型化数组）对象的信息 |
| OH_JSVM_GetDataviewInfo | 获取 Dataview 对象的信息 |
| OH_JSVM_GetDateValue | 获取给定 JavaScript Date 的时间值的 Double 基础类型值 |
| OH_JSVM_GetValueBool | 获取给定 JavaScript Boolean 的 C 布尔基础类型值 |
| OH_JSVM_GetValueDouble | 获取给定 JavaScript number 的 Double 基础类型值 |
| OH_JSVM_GetValueBigintInt64 | 获取给定 JavaScript BigInt 的 Int64_t 基础类型值 |
| OH_JSVM_GetValueBigintUint64 | 获取给定 JavaScript BigInt 的 Uint64_t 基础类型值 |
| OH_JSVM_GetValueBigintWords | 获取给定 JavaScript BigInt 对象的底层数据，即 BigInt 数据的字词表示 |
| OH_JSVM_GetValueExternal | 获取先前传递给 OH_JSVM_CreateExternal 的外部数据指针 |
| OH_JSVM_GetValueInt32 | 获取给定 JavaScript number 的 Int32 基础类型值 |
| OH_JSVM_GetValueInt64 | 获取给定 JavaScript number 的 Int64 基础类型值 |
| OH_JSVM_GetValueStringLatin1 | 获取给定 JavaScript string 对象的 Latin1 编码字符串 |
| OH_JSVM_GetValueStringUtf8 | 获取给定 JavaScript string 对象的 Utf8 编码字符串 |
| OH_JSVM_GetValueStringUtf16 | 获取给定 JavaScript string 对象的 Utf16 编码字符串 |
| OH_JSVM_GetValueUint32 | 获取给定 JavaScript number 的 Uint32 基础类型值 |
| OH_JSVM_GetBoolean | 返回用于表示给定布尔值的 JavaScript 单例对象 |
| OH_JSVM_GetGlobal | 返回当前环境中的全局 global 对象 |
| OH_JSVM_GetNull | 返回 JavaScript null 对象 |
| OH_JSVM_GetUndefined | 返回 JavaScript Undefined 对象 |
场景示例：
创建64位的BigInt，并获取64位int值。
创建一个Int32Array，并获取其长度，byteoffset等信息。
创建utf8类型的String，并获取C字符串。
JS值操作和抽象操作
场景介绍
JS值操作和抽象操作。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CoerceToBool | 将目标值转换为 Boolean 类型对象 |
| OH_JSVM_CoerceToNumber | 将目标值转换为 Number 类型对象 |
| OH_JSVM_CoerceToObject | 将目标值转换为 Object 类型对象 |
| OH_JSVM_CoerceToString | 将目标值转换为 String 类型对象 |
| OH_JSVM_CoerceToBigInt | 将目标值转换为 BigInt 类型对象 |
| OH_JSVM_Typeof | 返回 JavaScript 对象的类型 |
| OH_JSVM_Instanceof | 判断一个对象是否是某个构造函数的实例 |
| OH_JSVM_IsArray | 判断一个 JavaScript 对象是否为 Array 类型对象 |
| OH_JSVM_IsArraybuffer | 判断一个 JavaScript 对象是否为 Arraybuffer 类型对象 |
| OH_JSVM_IsDate | 判断一个 JavaScript 对象是否为 Date 类型对象 |
| OH_JSVM_IsTypedarray | 判断一个 JavaScript 对象是否为 Typedarray 类型对象 |
| OH_JSVM_IsDataview | 判断一个 JavaScript 对象是否为 Dataview 类型对象 |
| OH_JSVM_IsUndefined | 此API检查传入的值是否为Undefined。这相当于JS中的value === undefined。 |
| OH_JSVM_IsNull | 此API检查传入的值是否为Null对象。这相当于JS中的value === null。 |
| OH_JSVM_IsNullOrUndefined | 此API检查传入的值是否为Null或Undefined。这相当于JS中的value == null。 |
| OH_JSVM_IsBoolean | 此API检查传入的值是否为Boolean。这相当于JS中的typeof value === 'boolean'。 |
| OH_JSVM_IsNumber | 此API检查传入的值是否为Number。这相当于JS中的typeof value === 'number'。 |
| OH_JSVM_IsString | 此API检查传入的值是否为String。这相当于JS中的typeof value === 'string'。 |
| OH_JSVM_IsSymbol | 此API检查传入的值是否为Symbol。这相当于JS中的typeof value === 'symbol'。 |
| OH_JSVM_IsFunction | 此API检查传入的值是否为Function。这相当于JS中的typeof value === 'function'。 |
| OH_JSVM_IsObject | 此API检查传入的值是否为Object。 |
| OH_JSVM_IsBigInt | 此API检查传入的值是否为BigInt。这相当于JS中的typeof value === 'bigint'。 |
| OH_JSVM_IsConstructor | 此API检查传入的值是否为构造函数。 |
| OH_JSVM_IsMap | 此API检查传入的值是否为Map。 |
| OH_JSVM_IsSet | 此API检查传入的值是否为Set。 |
| OH_JSVM_IsRegExp | 此API检查传入的值是否为RegExp。 |
| OH_JSVM_StrictEquals | 判断两个 JSVM_Value 对象是否严格相等 |
| OH_JSVM_Equals | 判断两个 JSVM_Value 对象是否宽松相等 |
| OH_JSVM_DetachArraybuffer | 调用 ArrayBuffer 对象的Detach操作 |
| OH_JSVM_IsDetachedArraybuffer | 检查给定的 ArrayBuffer 是否已被分离(detached) |
场景示例:
判断JS值是否为数组类型
将int32类型转换为string类型
将boolean类型转换为bigint类型
判断两个JS值类型是否严格相同：先比较操作数类型，操作数类型不同就是不相等，操作数类型相同时，比较值是否相等，相等才返回true。
判断两个JS值类型是否宽松相同：判断两个操作数的类型是否相同，若不相同，且可以转换为相同的数据类型，转换为相同的数据类型后，值做严格相等比较，其他的都返回false。
判断JS值是否为构造函数
判断JS值是否为map类型
判断JS值是否为Set类型
判断JS值是否为RegExp类型
JS属性操作
场景介绍
JS对象属性的增删获取和判断
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_GetPropertyNames | 获取给定对象的所有可枚举属性名称, 结果变量将存储一个包含所有可枚举属性名称的JavaScript数组。 |
| OH_JSVM_GetAllPropertyNames | 获取给定对象的所有可用属性名称, 结果变量将存储一个包含所有可枚举属性名称的JavaScript数组。 |
| OH_JSVM_SetProperty | 为给定对象设置一个属性。 |
| OH_JSVM_GetProperty | 用给定的属性的名称，检索目标对象的属性。 |
| OH_JSVM_HasProperty | 用给定的属性的名称，查询目标对象是否有此属性。 |
| OH_JSVM_DeleteProperty | 用给定的属性的名称，删除目标对象属性。 |
| OH_JSVM_HasOwnProperty | 检查目标对象是否具有指定的自有属性。 |
| OH_JSVM_SetNamedProperty | 用给定的属性的名称为目标对象设置属性，此方法等效于使用从作为 utf8Name 传入的字符串创建的 JSVM_Value 调用 OH_JSVM_SetProperty。 |
| OH_JSVM_GetNamedProperty | 用给定的属性的名称，检索目标对象的属性，此方法等效于使用从作为 utf8Name 传入的字符串创建的 JSVM_Value 调用 OH_JSVM_GetProperty。 |
| OH_JSVM_HasNamedProperty | 用给定的属性的名称，查询目标对象是否有此属性，此方法等效于使用从作为 utf8Name 传入的字符串创建的 JSVM_Value 调用 OH_JSVM_HasProperty。 |
| OH_JSVM_SetElement | 在给定对象的指定索引处设置元素。 |
| OH_JSVM_GetElement | 获取给定对象指定索引处的元素。 |
| OH_JSVM_HasElement | 若给定对象的指定索引处拥有属性，获取该元素。 |
| OH_JSVM_DeleteElement | 尝试删除给定对象的指定索引处的元素。 |
| OH_JSVM_DefineProperties | 批量的向给定对象中定义属性。 |
| OH_JSVM_ObjectFreeze | 冻结给定的对象,防止向其添加新属性，删除现有属性，防止更改现有属性的可枚举性、可配置性或可写性，并防止更改现有属性的值。 |
| OH_JSVM_ObjectSeal | 密封给定的对象。这可以防止向其添加新属性，以及将所有现有属性标记为不可配置。 |
| OH_JSVM_ObjectSetPrototypeOf | 为给定对象设置一个原型。 |
| OH_JSVM_ObjectGetPrototypeOf | 获取给定JavaScript对象的原型。 |
场景示例:
JS对象属性的增删获取和判断
JS函数操作
场景介绍
JS函数操作。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CallFunction | 在C/C++侧调用JS方法 |
| OH_JSVM_CreateFunction | 用于创建JavaScript函数,用于从JavaScript环境中调用C/C++代码中的函数 |
| OH_JSVM_GetCbInfo | 从给定的callback info中获取有关调用的详细信息，如参数和this指针 |
| OH_JSVM_GetNewTarget | 获取构造函数调用的new.target |
| OH_JSVM_NewInstance | 通过给定的构造函数，构建一个实例 |
| OH_JSVM_CreateFunctionWithScript | 根据传入的函数体和函数参数列表，创建一个新的 JavaScript Function对象 |
场景示例:
创建JavaScript函数操作
在C/C++侧获取并调用JS方法
创建Function:
对象绑定操作
场景介绍
对象绑定操作。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_DefineClass | 用于在JavaScript中定义一个类，并与对应的C类进行封装和交互。它提供了创建类的构造函数、定义属性和方法的能力，以及在C和JavaScript之间进行数据交互的支持。 |
| OH_JSVM_Wrap | 在 JavaScript 对象中封装原生实例。稍后可以使用 OH_JSVM_Unwrap() 检索原生实例。 |
| OH_JSVM_Unwrap | 使用 OH_JSVM_Wrap() 检索先前封装在 JavaScript 对象中的原生实例。 |
| OH_JSVM_RemoveWrap | 检索先前封装在 JavaScript 对象中的原生实例并移除封装。 |
| OH_JSVM_TypeTagObject | 将 type_tag 指针的值与 JavaScript 对象或外部对象相关联。 |
| OH_JSVM_CheckObjectTypeTag | 检查给定的类型标签是否与对象上的类型标签匹配。 |
| OH_JSVM_AddFinalizer | 为对象添加 JSVM_Finalize 回调，以便在 JavaScript 对象被垃圾回收时调用来释放原生对象。 |
| OH_JSVM_DefineClassWithPropertyHandler | 定义一个具有给定类名、构造函数、属性和回调处理程序的JavaScript类，并作为函数回调进行调用。属性操作包括getter、setter、deleter、enumerator等。 |
场景示例：
对象绑定操作。
场景示例：
对象绑定及监听拦截属性操作。
版本管理
场景介绍
获取当前版本信息。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_GetVersion | 返回JSVM运行时支持的最高JSVM API版本 |
| OH_JSVM_GetVMInfo | 返回虚拟机的信息 |
场景示例：
获取当前版本信息。
内存管理
场景介绍
内存管理
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_AdjustExternalMemory | 将因JavaScript对象而保持活跃的外部分配的内存大小及时通知给底层虚拟机，虚拟机后续触发GC时，就会综合内外内存状态来判断是否进行全局GC。即增大外部内存分配，则会增大触发全局GC的概率；反之减少。 |
| OH_JSVM_MemoryPressureNotification | 通知虚拟机系统内存压力层级，并有选择地触发垃圾回收。 |
| OH_JSVM_AllocateArrayBufferBackingStoreData | 申请一块 BackingStore 内存。 |
| OH_JSVM_FreeArrayBufferBackingStoreData | 释放 BackingStore 内存。 |
| OH_JSVM_CreateArrayBufferFromBackingStoreData | 基于申请的 BackingStore 内存创建 array buffer。 |
BackingStore 的使用属于高危操作，需要使用者自身保证内存的正确使用，请参考下方的正确示例，谨慎使用。
场景示例：
内存管理。
BackingStore 正确使用示例
Promise操作
场景介绍
Promise相关操作。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CreatePromise | 创建一个延迟对象和一个JavaScript promise |
| OH_JSVM_ResolveDeferred | 通过与之关联的延迟对象来解析JavaScript promise |
| OH_JSVM_RejectDeferred | 通过与之关联的延迟对象来拒绝JavaScript Promise |
| OH_JSVM_IsPromise | 查询Promise是否为原生Promise对象 |
场景示例：
Promise相关操作。
JSON操作
场景介绍
JSON操作。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_JsonParse | 解析JSON字符串，并返回成功解析的值 |
| OH_JSVM_JsonStringify | 将对象字符串化，并返回成功转换后的字符串 |
场景示例：
解析JSON操作。
创建和使用虚拟机的启动快照
场景介绍
创建和使用虚拟机的启动快照
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CreateSnapshot | 用于创建虚拟机的启动快照 |
| OH_JSVM_CreateEnvFromSnapshot | 基于启动快照创建jsvm环境 |
场景示例：
创建和使用虚拟机的启动快照。
检查传入的值是否可调用
场景介绍
检查传入的值是否可调用
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_IsCallable | 检查传入的值是否可调用 |
场景示例：
检查传入的值是否可调用
Lock操作
场景介绍
Lock操作
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_IsLocked | 判断当前线程是否持有指定环境的锁 |
| OH_JSVM_AcquireLock | 获取指定环境的锁 |
| OH_JSVM_ReleaseLock | 释放指定环境的锁 |
场景示例：
加锁解锁操作
设置与获取和当前运行的JSVM环境相关联的数据
场景介绍
检索通过OH_JSVM_SetInstanceData()与当前运行的JSVM环境相关联的数据
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_SetInstanceData | 设置与当前运行的JSVM环境相关联的数据 |
| OH_JSVM_GetInstanceData | 获取与当前运行的JSVM环境相关联的数据 |
场景示例：
设置并获取与当前运行的JSVM环境相关联的数据。
任务队列
场景介绍
在虚拟机内部启动任务队列的运行，检查是否有微任务在队列中等待，这个任务队列可以由外部事件循环执行
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_PumpMessageLoop | 启动任务队列的运行 |
| OH_JSVM_PerformMicrotaskCheckpoint | 执行任务队列里的微任务 |
场景示例：
启动任务队列，执行任务。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-jsvm-process-V14
爬取时间: 2025-04-30 06:24:34
来源: Huawei Developer
使用JSVM-API实现跨语言交互，首先需要按照JSVM-API的机制实现模块的注册和加载等相关动作。
-  ArkTS/JS侧：实现C++方法的调用。代码比较简单，import一个对应的so库后，即可调用C++方法。
-  Native侧：.cpp文件，实现模块的注册。需要提供注册lib库的名称，并在注册回调方法中定义接口的映射关系，即Native方法及对应的JS/ArkTS接口名称等。
此处以在ArkTS/JS侧实现RunJsVm()接口、在Native侧实现RunJsVm()接口，从而实现跨语言交互为例，呈现使用JSVM-API进行跨语言交互的流程。
创建Native C++工程
具体见创建NDK工程
Native侧方法的实现
-  设置模块注册信息 具体见设置模块注册信息
-  模块初始化 实现ArkTS接口与C++接口的绑定和映射。
-  在index.d.ts文件中，提供JS侧的接口方法。
```typescript
// entry/src/main/cpp/types/libentry/index.d.ts
export const runTest: () => void;
```
-  在oh-package.json5文件中将index.d.ts与cpp文件关联起来。
```json
{
"name": "libentry.so",
"types": "./index.d.ts",
"version": "",
"description": "Please describe the basic information."
}
```
-  在CMakeLists.txt文件中配置CMake打包参数。
-  实现Native侧的runTest接口。具体代码如下：
ArkTS侧调用C/C++方法实现
```typescript
import hilog from '@ohos.hilog'
// 通过import的方式，引入Native能力。
import napitest from 'libentry.so'
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
// runtest
napitest.runTest();
})
}
.width('100%')
}
.height('100%')
}
}
```
预期输出结果
```typescript
JSVM OH_JSVM_StrictEquals: success: 0
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-development-standards-V14
爬取时间: 2025-04-30 06:24:48
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-guidelines-V14
爬取时间: 2025-04-30 06:25:05
来源: Huawei Developer
生命周期管理
【规则】合理使用OH_JSVM_OpenHandleScope和OH_JSVM_CloseHandleScope管理JSVM_Value的生命周期，做到生命周期最小化，避免发生内存泄漏问题。
每个JSVM_Value属于特定的HandleScope，HandleScope通过OH_JSVM_OpenHandleScope和OH_JSVM_CloseHandleScope来建立和关闭，HandleScope关闭后，所属的JSVM_Value就会自动释放。
注意事项：
Scope关闭错误示例：
C++使用封装：
示例：
多引擎实例上下文敏感
【规则】多引擎实例（VM）场景下，禁止通过JSVM-API跨引擎实例访问JS对象。
引擎实例是一个独立运行环境，JS对象创建访问等操作必须在同一个引擎实例中进行。若在不同引擎实例中操作同一个对象，可能会引发程序崩溃。引擎实例在接口中体现为JSVM_Env。
错误示例：
所有的JS对象都隶属于具体的某一JSVM_Env，不可将env1的对象，设置到env2中的对象中。在env2中一旦访问到env1的对象，程序可能会发生崩溃。
多线程共享引擎实例
【规则】多线程同时使用同一个引擎实例的场景下，需要加锁使用。保证一个引擎实例在同一时刻只能在一个线程执行。多线程同一时刻同时使用引擎实例可能造成应用崩溃。
注意事项：
C++使用封装：
正确示例：
获取JS传入参数及其数量
【规则】当传入OH_JSVM_GetCbInfo的argv不为nullptr时，argv的长度必须大于等于传入argc声明的大小。
当argv不为nullptr时，OH_JSVM_GetCbInfo会根据argc声明的数量将JS实际传入的参数写入argv。如果argc小于等于实际JS传入参数的数量，该接口仅会将声明的argc数量的参数写入argv；而当argc大于实际参数数量时，该接口会在argv的尾部填充undefined。
错误示例：
正确示例：
异常处理
【建议】JSVM-API接口调用发生异常需要及时处理，不能遗漏异常到后续逻辑，否则程序可能发生不可预期行为。
根据主从类型，异常处理可以分为两类：
1.  JSVM 执行 C++ 回调函数（JS主，Native从）时发生 C++ 异常，需往 JSVM 中抛出异常，下面用例描述了3种情况下 C++ 回调函数的写法 注意事项：回调函数中调用JSVM-API失败，如要向JSVM中抛异常，需保证JSVM中无等待处理的异常，也可以不抛出异常，JS的try-catch块可以捕获回调函数调用API失败产生的JS异常，见NativeFunctionExceptionDemo3。
2.  C++调用JSVM-API（Native主，JS从）失败，需清理JSVM中等待处理的异常，避免影响后续JSVM-API的执行，并设置C++异常处理分支（或抛出C++异常）。
上下文绑定对象
【规则】：调用JSVM-API生成的JS函数、对象需绑定到上下文中才能从JS侧访问，OH_JSVM_CreateFunction接口中的const char *参数为创建函数的属性name，不代表上下文中指向该函数的函数名。调用JSVM-API生成的类、对象同理。
示例：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-frequently-questions-V14
爬取时间: 2025-04-30 06:25:19
来源: Huawei Developer
定位方法
程序崩溃类问题：通过C++崩溃时调用栈查询FAQ的方式定位代码问题
程序执行结果不符合预期类问题：需应用通过JSVM-API调用返回值定位到执行失败或执行结果不符合预期的位置，通过函数名查询FAQ
程序崩溃类
1.  Q：在OH_JSVM_RunScript或OH_JSVM_CallFunction时crash，调用栈顶层为SetReturnValue A：SetReturnValue用于设置js函数的返回值，在js完成注入的native函数调用后触发。需检查native函数的返回值是否正确，如返回值（类型JSVM_Value）是否未初始化就直接返回。
2.  Q：js执行虚拟机初始化注入的native函数时程序崩溃 A：检查JSVM_CallbackStruct是否为栈上变量，跨函数使用时需保证JSVM_CallbackStruct生命周期 >JSVM_Env的生命周期 样例中的代码结构如上，JS引擎实例在函数结束前被关闭，所以可以直接使用栈上的param。
3.  Q：OH_JSVM_ReferenceRef、OH_JSVM_ReferenceUnRef、OH_JSVM_CreateReference、OH_JSVM_DeleteReference时程序崩溃 A：检查是否同时有多个线程持有和释放JSVM_Ref，见多线程共享引擎实例
4.  Q：在虚拟机引擎实例中创建JS类型实例崩溃（如OH_JSVM_CreateDouble），调用栈如下 A：检查HandleScope的使用是否正确，见生命周期管理
JSVM-API执行失败类
1.  Q：OH_JSVM_GetCbInfo的无法获取JS函数参数 A：检查函数传递的参数是否正确，见获取JS传入参数及其数量
2.  Q：OH_JSVM_CreateFunction等函数调用失败，返回值为JSVM_PENDING_EXCEPTION A：JSVM_PENDING_EXCEPTION表明当前虚拟机环境中存在未处理的异常，可能是由于本次调用产生的JS异常，也可能是之前调用产生的未被清理的异常。可以通过在函数调用前插入OH_JSVM_GetAndClearLastException排查之前是否有未清除的异常。如果为之前的未清理异常，检查是否有JSVM接口调用未处理异常返回值；如未本次产生的异常，需清理异常，避免影响后续的函数调用。获取并清理异常的函数为OH_JSVM_GetAndClearLastException
3.  Q：JS执行时无法找到 OH_JSVM_DefineClass 定义的类 A：检查是否将定义的类绑定到上下文中，见上下文绑定对象

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-use-V14
爬取时间: 2025-04-30 06:25:32
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-jsvm-execute_tasks-V14
爬取时间: 2025-04-30 06:25:46
来源: Huawei Developer
简介
在虚拟机内部启动任务队列的运行，检查是否有微任务在队列中等待，这个任务队列可以由外部事件循环执行。
基本概念
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_PumpMessageLoop | 启动任务队列的运行 |
| OH_JSVM_PerformMicrotaskCheckpoint | 执行任务队列里的微任务 |
使用示例
JSVM-API接口开发流程参考使用JSVM-API实现JS与C/C++语言交互开发流程，本文仅对接口对应C++相关代码进行展示。
OH_JSVM_PumpMessageLoop && OH_JSVM_PerformMicrotaskCheckpoint
启动任务队列，执行任务。
cpp代码
预期输出结果
OH_JSVM_SetMicrotaskPolicy
修改微任务执行策略,通过该接口，用户可以将策略设置为 JSVM_MicrotaskPolicy::JSVM_MICROTASK_EXPLICIT 或 JSVM_MicrotaskPolicy::JSVM_MICROTASK_AUTO。默认模式下，微任务的执行策略为 JSVM_MicrotaskPolicy::JSVM_MICROTASK_AUTO。
微任务策略：
cpp 部分代码
预期输出结果

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-jsvm-create-snapshot-V14
爬取时间: 2025-04-30 06:26:00
来源: Huawei Developer
简介
JavaScript虚拟机（JSVM）的快照创建功能，将当前运行时的JavaScript程序状态保存为一个快照文件，这个快照文件包含了当前的堆内存、执行上下文、函数闭包等信息。
基本概念
创建虚拟机启动快照可以简化一些复杂的编程任务，使得在JSVM中管理和维护虚拟机更加便捷，使程序更加灵活与稳定。
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CreateSnapshot | 用于创建虚拟机的启动快照 |
| OH_JSVM_CreateEnvFromSnapshot | 基于虚拟机的起始快照，创建一个新的环境 |
使用示例
OH_JSVM_CreateSnapshot & OH_JSVM_CreateEnvFromSnapshot
用于创建和使用虚拟机的启动快照。
cpp部分代码
注意事项: 需要在OH_JSVM_Init的时候，将JSVM对外部的依赖注册到initOptions.externalReferences中。
ArkTS侧示例代码
```typescript
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
// runtest
napitest.runTest();
})
}
.width('100%')
}
.height('100%')
}
}
```
执行结果
在LOG中输出：Test JSVM RunVMSnapshot read file blobSize = : 300064

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-jsvm-about-wasm-V14
爬取时间: 2025-04-30 06:26:13
来源: Huawei Developer
简介
JSVM-API WebAssembly 接口提供了 WebAssembly 字节码编译、WebAssembly 函数优化、WebAssembly cache 序列化和反序列化的能力。
基本概念
接口说明
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_CompileWasmModule | 将 wasm 字节码同步编译为 wasm module。如果提供了 cache 参数，先尝试将 cache 反序列为 wasm module，反序列化失败时再执行编译。 |
| OH_JSVM_CompileWasmFunction | 将 wasm module 中指定编号的函数编译为优化后的机器码，目前只使能了最高的优化等级，函数编号的合法性由接口调用者保证。 |
| OH_JSVM_IsWasmModuleObject | 判断传入的值是否是一个 wasm module。 |
| OH_JSVM_CreateWasmCache | 将 wasm module 中的机器码序列化为 wasm cache，如果 wasm module 不包含机器码，则会序列化失败。 |
| OH_JSVM_ReleaseCache | 释放由 JSVM 接口生成的 cache。传入的 cacheType 和 cacheData 必须匹配，否则会产生未定义行为。 |
code cache 校验规格说明
| 规格 | 规格说明 |
| --- | --- |
| 完整性校验 | 由用户保证 |
| 兼容性校验 | 校验生成 cache 的 JSVM 版本与编译选项是否与当前一致 |
| 一致性校验 | 由用户保证 |
使用示例
JSVM-API 接口开发流程参考使用JSVM-API实现JS与C/C++语言交互开发流程，本文仅对接口对应 C++ 相关代码进行展示。
cpp 部分代码：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-scenarios-V14
爬取时间: 2025-04-30 06:26:27
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-debugger-cpuprofiler-heapsnapshot-V14
爬取时间: 2025-04-30 06:26:42
来源: Huawei Developer
JSVM，既标准JS引擎，是严格遵守Ecmascript规范的JavaScript代码执行引擎。 详情参考：JSVM。
基于JSVM的JS代码调试调优能力包括：Debugger、CPU Profiler、Heap Snapshot、Heap Statistics。涉及以下接口：
| 接口名 | 接口功能 |
| --- | --- |
| OH_JSVM_GetVM | 将检索给定环境的虚拟机实例。 |
| OH_JSVM_GetHeapStatistics | 返回一组虚拟机堆的统计数据。 |
| OH_JSVM_StartCpuProfiler | 创建并启动一个CPU profiler。 |
| OH_JSVM_StopCpuProfiler | 停止CPU profiler并将结果输出到流。 |
| OH_JSVM_TakeHeapSnapshot | 获取当前堆快照并将其输出到流。 |
| OH_JSVM_OpenInspector | 在指定的主机和端口上激活inspector，将用来调试JS代码。 |
| OH_JSVM_OpenInspectorWithName | 基于传入的 pid 和 name 激活 inspector。 |
| OH_JSVM_CloseInspector | 尝试关闭剩余的所有inspector连接。 |
| OH_JSVM_WaitForDebugger | 等待主机与inspector建立socket连接，连接建立后程序将继续运行。发送Runtime.runIfWaitingForDebugger命令。 |
本文将介绍调试、CPU Profiler、Heap Snapshot的使用方法。
调试能力使用方法
使用 OH_JSVM_OpenInspector
示例代码
JSVM-API接口开发流程参考使用JSVM-API实现JS与C/C++语言交互开发流程，本文仅对接口对应C++相关代码进行展示。
使用 OH_JSVM_OpenInspectorWithName
代码示例
对应的 enable inspector 替换为下面的即可
使用 Chrome inspect 页面进行调试
除了使用上述打开"devtoolsFrontendUrl"字段url的方法调试代码之外，也可以直接通过Chrome浏览器的 chrome://inspect/#devices 页面进行调试。方法如下：
1.  执行端口转发命令：hdc fport [开发者个人计算机侧端口号] [端侧端口号] 例如：hdc fport tcp:9227 tcp:9226
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165817.68821852561208605418105135625262:50001231000000:2800:BE6A522E9B209EEDF1592B2C21F0545C56BBD023D21E94B9D9745BB092B6A37C.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165817.14561628806407758151283178018808:50001231000000:2800:7FDD1732C749B77305959E6585B9B9174807E4BB505D9C718B47D7AE9DC7659B.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165817.05672750141164234122528123367783:50001231000000:2800:D2161EBD4D9DE9B270164DA0570308C1580062E6B34172845F6F9DCA4B5697BE.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165817.97301631762201504819648365914837:50001231000000:2800:10FA5428660EDB64B89F2534DEA9A662528204FD03E9BC12B1929AD194B603A3.png)
CPU Profiler及Heap Snapshot使用方法
CPU Profiler接口使用方法
Heap Snapshot接口使用方法
1.为分析某段JS代码的堆对象创建情况。可在执行JS代码前后，分别调用一次OH_JSVM_TakeHeapSnapshot。传入输出流回调及输出流指针。数据将会写入指定的输出流中。
2.输出数据可存入.heapsnapshot文件中。该文件类型可导入Chrome浏览器-DevTools-Memory工具中解析成内存分析视图。
示例代码
JSVM-API接口开发流程参考使用JSVM-API实现JS与C/C++语言交互开发流程，本文仅对接口对应C++相关代码进行展示。
// 样例测试JS

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-usage-examples-V14
爬取时间: 2025-04-30 06:26:55
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-jsvm-runtime-task-V14
爬取时间: 2025-04-30 06:27:09
来源: Huawei Developer
场景介绍
开发者通过createJsCore方法来创建一个新的JS基础运行时环境，并通过该方法获得一个CoreID，通过evaluateJS方法使用CoreID对应的运行环境来运行JS代码，在JS代码中创建promise并异步执行函数，最后使用releaseJsCore方法来释放CoreID对应的运行环境。
使用示例
JSVM-API接口开发流程参考使用JSVM-API实现JS与C/C++语言交互开发流程，本文仅对接口对应C++相关代码进行展示。
新建多个JS运行时环境并运行JS代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-jsvm-about-code-cache-V14
爬取时间: 2025-04-30 06:27:23
来源: Huawei Developer
code cache 简介
JSVM 提供了生成并使用 code cache 加速编译过程的方法，其获取和使用分为下面几个部分：
通过上述流程，将会在使用 code cache 的那次编译中，极大减少编译时间，其原理为将编译完成的 script 序列化，然后使用 code cache 编译时就不再需要重新解析/编译已经被序列化的函数，只需要进行一次反序列化即可，编译就简化为了一次数据读取。
code cache 校验规格说明
| 规格 | 规格说明 |
| --- | --- |
| 完整性校验 | 校验 cache 实际长度，是否与生成时一致 |
| 兼容性校验 | 校验生成 cache 的 JSVM 版本与编译选项是否与当前一致 |
| 一致性校验 | 校验生成 cache 的 js 源码，是否与当前输入源码长度一致 |
场景示例
下面的伪代码是一个典型的使用方法，其中第二次编译，如果 cacheRejected 为 true，那么说明 code cache 被拒绝无法生效，运行时间会与无 code cache 时间一致；为 false 则这次运行将会极大加快。
其中使用到的 JSVM-API 可以参考JSVM 数据类型与接口说明，这里仅展示调用的步骤。
外层跨语言交互的部分可以参考使用 JSVM-API 实现 JS 与 C/C++ 语言交互开发流程。
预期输出结果
注意事项
上述代码中使用了 code cache 进行编译: OH_JSVM_CompileScript(env, jsSrc, dataPtr, length, true, &cacheRejected, &script);
这个接口的传入参数中包含了 cacheRejected，其作用是接收实际的编译过程中，code cache 是否被拒绝的状态，这里包含了多种情况：
对于第一种情况，这个参数会被置为 true，而后两种情况都是 false，因此需要注意即使 reject 为 false，也不能说明 code cache 被接收了。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/jsvm-optimizations-V14
爬取时间: 2025-04-30 06:27:36
来源: Huawei Developer
JSVM 调用结构
小程序使用 JSVM 执行 JS 代码的过程大概可以分为 native，JSVM-API，JSVM 三层：
使用 JSVM 的过程中，可能由于各种原因产生一些不必要的开销导致启动变慢，其中的原因可以从以上三层的角度进行拆分。
提升启动速度
对于使用 JSVM 的应用启动场景，我们可以区分冷热启动用于分别进行不同的优化。
首先是冷启动，是没有任何 profile 或者 cache 可以用于优化的场景，通常是首次启动；
热启动则是已经充分预热，在多次启动之后获取了足量用于优化的 cache 的场景。
减少 JS 引擎层的开销
引擎层的开销很大的一部分来源于编译，通过合理调整调用 JSVM-API 时传入的选项，可以减少主线程上 JS 引擎的编译开销，
以下面的编译接口为例，其中 eagerCompile 这个参数的开关可以调控编译行为，通过在不同的启动场景打开这个选项可以实现优化效果。
同时 code cache 的生成和使用也会对编译产生影响，这部分可以参考使用 code cache 加速编译。
热启动：生成足够多的 code cache
热启动场景下，我们会在热启动前生成 code cache 以减少编译带来的开销。这个时候生成的 code cache 的覆盖率会影响 code cache 对热启动的优化效果。
有一个简单的策略可以生成足量的 code cache，就是在生成 code cache 前的那次编译打开 eager compile 选项，这样 v8 会在编译时进行全量的编译，这样生成 code cache 一定是全量的。
这个方法会带来额外的编译时间开销，可能影响冷启动的时间，这一点会在下面对 native 层的冷启动优化方法中提到。
冷启动：使用 lazy compile 代替 eager compile
在冷启动时，eager compile 会增加不必要的编译时间。这其中主要的原因是没有拿到 v8 lazy compile 优化效果：v8 会将不在必经路径上的函数推迟编译，在实际运行到的时候才进行编译，这样会减少一些不被运行到函数的编译，从而优化冷启动的时间。
因此在冷启动时，会阻塞主线程的部分可以关闭 eager compile 选项，从而拿到足够的冷启动优化效果。
在 native 层减少时间开销
冷启动：减少 code cache 的影响
上面在考虑减少 v8 层开销的时候，提到了为了热启动的性能可以开启 eager compile 进行编译，而为了冷启动性能却又需要关闭 eager compile 选项，看起来是矛盾的。为了解决这个矛盾，避免在冷热启动性能上的权衡，关键点是在 code cache 生成本身。
首先 code cache 的生成是需要前置的编译的，其次生成 code cache 本身也存在开销；
那么在 native 层，要解决冷启动和生成 code cache 之间的矛盾，首先我们可以另起一个线程用于生成 code cache，这样避免了生成 code cache 这个操作本身对冷启动的影响；
然后，有两个方法可以参考(下面的伪代码仅用于展示逻辑流程，不涉及真正的 api 调用):
使用更高效的 JSVM-API
在能达到相同效果时，使用更高效的 JSVM-API 是简单有效的性能优化方法，以下实践是在优化实践过程中发现的一些例子
使用 IsXXX 代替 TypeOf
过去发现，针对仅需要判断对象原生类型的场景，存在一种相对低效的使用方法：
从 OH_JSVM_TypeOf 接口获取对象类型后，再判断是否与某个类型相同。
这种方法需要先查询 object 的类型，这种方法相对于直接使用 is 方法会更慢，因此我们新增了针对基础类型的 IsXXX 系列方法，用更高效的接口代替了相对低效的接口。下面的示例中中使用到的 JSVM-API 可以参考JSVM 数据类型与接口说明，这里仅展示调用的步骤。
以某生态应用小程序场景为例，这个优化可以带来的性能收益端到端有 150ms，总占比约 5%。
直接使用 OH_JSVM_CreateReference，避免创建冗余的 object
过去存在这样一种创建 reference 的路径：
创建一个新的 object -> 设置 object 的值 -> 创建 object 的 reference。
这种在已经有值的情况下创建一个新的 object 的操作是冗余的，直接创建对值的引用即可。
下面的示例中中使用到的 JSVM-API 可以参考JSVM 数据类型与接口说明，这里仅展示调用的步骤。
同样以某生态应用小程序场景为例，这个改动减少了大量冗余的接口调用，最终带来的端到端时间收益有 100+ms，约 3%。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/openmp-V14
爬取时间: 2025-04-30 06:27:50
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/openmp-overview-V14
爬取时间: 2025-04-30 06:28:09
来源: Huawei Developer
OpenMP（Open Multi-Processing）是一套支持跨平台共享内存方式的多线程并发的编程API，由一套编译器指令、库和一些能够影响运行行为的环境变量构成，提供了对并行算法的高层抽象描述，适合在多核CPU机器上的并行程序设计。编译器根据程序中添加的pragma指令，自动将pragma指令标记的程序片段并行处理，使用OpenMP可以降低并行编程的复杂度。
使用场景
OpenMP广泛应用于科学计算、图像处理、机器学习、金融计算、生物信息学等需要高性能计算的领域，尤其适合解决计算密集型任务和数据并行问题。它通过简化多核并行化的开发流程，帮助开发者高效利用现代处理器的多核资源，解决了传统并行编程中线程管理复杂、任务负载不均、性能瓶颈等问题。借助OpenMP的灵活调度机制和跨平台支持，程序能够显著提升性能，同时保持代码的简洁性和可移植性，是提高开发效率和计算效率的关键工具。
版本说明
当前Openharmony中的OpenMP库采用llvm 15.0.4中的实现，对应OpenMP API版本请参考clang-OpenMPSupport。
Openharmony应用中使用OpenMP请参考OpenMP应用构建和运行指南。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/openmp-guideline-V14
爬取时间: 2025-04-30 06:28:22
来源: Huawei Developer
HarmonyOS NDK中提供了OpenMP的动态库和静态库文件，支持开发者在Native应用中使用OpenMP。本文用于指导开发者在DevEco Studio中调用库文件使用OpenMP的并行化能力，更详细的使用示例和API标准请查看官方文档clang-OpenMPSupport。
开发步骤
1. 创建Native C++工程
创建NDK工程
2. 添加依赖
OpenMP库的引入有静态链接和动态链接两种方式。
OMPT(OpenMP Tools Interface)工具目前仅支持静态链接时使用。
静态链接
（1）打开entry/src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加静态库libomp.a以及日志依赖libhilog_ndk.z.so。
```typescript
target_link_libraries(entry PUBLIC libomp.a libace_napi.z.so libhilog_ndk.z.so)
```
（2）打开entry/build-profile.json5，在buildOption->externalNativeOptions->cppFlags下添加编译参数"-static-openmp -fopenmp"。
动态链接
（1）打开entry/src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加动态库libomp.so以及日志依赖libhilog_ndk.z.so。
```typescript
target_link_libraries(entry PUBLIC libomp.so libace_napi.z.so libhilog_ndk.z.so)
```
（2）打开entry/build-profile.json5，在buildOption->externalNativeOptions->cppFlags下添加编译参数"-fopenmp"。
（3）打开Sdk安装目录，在“{Sdk安装目录}{版本号}\HarmonyOS\native\llvm\lib\aarch64-linux-ohos”目录下找到libomp.so动态库文件，并将其拷贝到工程目录entry/libs/arm64-v8a文件夹。
3. 修改源文件
（1）修改entry/src/main/cpp/napi_init.cpp，引入omp.h头文件，并添加OmpTest函数。
（2）修改entry/src/main/cpp/types/libentry/Index.d.ts，导出ompTest函数。
（3）Ts侧调用，修改entry/src/main/ets/pages/Index.ets，调用ompTest函数。
4. 运行并校验结果
运行前请检查设备连接并配置好Signature信息。直接点击右上角运行按钮，应用启动后设备进入“Hello OpenMP”界面，点击“Hello OpenMP”标签，打开Dev Eco下方“Log”查看页面，即可看到并行打印的“Hello OpenMP！”消息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165817.51133050269444131513805812187368:50001231000000:2800:EFCCF6E4874C3EC61719586756AD5D235334BF8ADBE702EE9B29C6F7F2374868.png)
OpenMP程序运行时，Hilog中会输出“dlopen_impl load library header failed for libarcher.so”的报错信息（如下图）。该报错信息中提到的libarcher.so，在OpenMP程序开启Tsan检测时才需要使用。目前HarmonyOS未支持OpenMP程序的Tsan检测能力，因此该错误信息可忽略，不影响程序正常运行。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165818.70691576422080454631686790629853:50001231000000:2800:A199345EF708E49AB8EB8D7C1FB8805EAF7D85F53A585A1F1E0ECC72B2BB8496.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/resource-management-V14
爬取时间: 2025-04-30 06:28:36
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/rawfile-guidelines-V14
爬取时间: 2025-04-30 06:28:50
来源: Huawei Developer
场景介绍
开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native Rawfile接口操作Rawfile目录和文件。功能包括文件列表遍历、文件打开、搜索、读取和关闭Rawfile。
64后缀相关接口属于新增接口，新接口支持打开更大的rawfile文件(超过2G以上建议使用)，具体请参考：Rawfile接口介绍。64相关的开发步骤和非64一致，将非64接口替换为64接口即可，例如：OH_ResourceManager_OpenRawFile替换为OH_ResourceManager_OpenRawFile64。
接口说明
| 接口名 | 描述 |
| --- | --- |
| NativeResourceManager *OH_ResourceManager_InitNativeResourceManager(napi_env env, napi_value jsResMgr) | 初始化native resource manager。 |
| RawDir *OH_ResourceManager_OpenRawDir(const NativeResourceManager *mgr, const char *dirName) | 打开指定rawfile目录。 |
| int OH_ResourceManager_GetRawFileCount(RawDir *rawDir) | 获取指定rawfile目录下的rawfile文件数量。 |
| const char *OH_ResourceManager_GetRawFileName(RawDir *rawDir, int index) | 获取rawfile名字。 |
| RawFile *OH_ResourceManager_OpenRawFile(const NativeResourceManager *mgr, const char *fileName) | 打开指定rawfile文件。 |
| long OH_ResourceManager_GetRawFileSize(RawFile *rawFile) | 获取rawfile文件大小。 |
| int OH_ResourceManager_SeekRawFile(const RawFile *rawFile, long offset, int whence) | 指定rawfile内偏移量。 |
| long OH_ResourceManager_GetRawFileOffset(const RawFile *rawFile) | 获取rawfile偏移量。 |
| int OH_ResourceManager_ReadRawFile(const RawFile *rawFile, void *buf, size_t length) | 读取rawfile文件内容。 |
| int64_t OH_ResourceManager_GetRawFileRemainingLength(const RawFile *rawFile) | 获取rawfile文件剩余长度。 |
| void OH_ResourceManager_CloseRawFile(RawFile *rawFile) | 释放rawfile文件相关资源。 |
| void OH_ResourceManager_CloseRawDir(RawDir *rawDir) | 释放rawfile目录相关资源。 |
| bool OH_ResourceManager_GetRawFileDescriptor(const RawFile *rawFile, RawFileDescriptor &descriptor) | 获取rawfile的fd。 |
| bool OH_ResourceManager_ReleaseRawFileDescriptor(const RawFileDescriptor &descriptor) | 释放rawfile的fd。 |
| void OH_ResourceManager_ReleaseNativeResourceManager(NativeResourceManager *resMgr) | 释放native resource manager相关资源。 |
| bool OH_ResourceManager_IsRawDir(const NativeResourceManager *mgr, const char *path) | 判断路径是否是rawfile下的目录。 |
详细的接口说明请参考rawfile函数说明。
开发步骤
以ArkTS侧获取rawfile文件列表、rawfile文件内容、rawfile描述符{fd, offset, length}三种调用方式为例。
1. 创建工程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165818.09206945199179210728087774984657:50001231000000:2800:0394667AE50339A55986ED86B443F0D356A517479767E4625B0379CCC3824080.png)
2. 添加依赖
创建完成后，DevEco Studio会在工程生成cpp目录，目录有libentry/index.d.ts、hello.cpp、CMakeLists.txt等文件。
1.  打开src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加资源的librawfile.z.so以及日志依赖libhilog_ndk.z.so。
2.  打开src/main/cpp/types/libentry/index.d.ts文件，此文件声明了应用侧函数getFileList、getRawFileContent、getRawFileDescriptor。
```typescript
import resourceManager from '@ohos.resourceManager';
export const getFileList: (resmgr: resourceManager.ResourceManager, path: string) => Array<String>;
export const getRawFileContent: (resmgr: resourceManager.ResourceManager, path: string) => Uint8Array;
export const getRawFileDescriptor: (resmgr: resourceManager.ResourceManager, path: string) => resourceManager.RawFileDescriptor;
export const isRawDir: (resmgr: resourceManager.ResourceManager, path: string) => Boolean;
```
3. 修改源文件
1.  打开src/main/cpp/hello.cpp文件，文件Init会对当前方法进行初始化映射，这里定义对外接口为getFileList、getRawFileContent、getRawFileDescriptor，映射C++接口分别为GetFileList、GetRawFileContent、GetRawFileDescriptor。
2.  把src/main/cpp/hello.cpp文件中，增加对应的三个方法，如下所示：
3.  在hello.cpp文件中获取Js的资源对象，并转为Native的资源对象，即可调用资源的Native接口，获取rawfile列表、rawfile文件内容以及rawfile描述符{fd, offset, length}三种调用方式示例代码如下：
4. Js侧调用
1.  打开src\main\ets\pages\index.ets, 导入"libentry.so"。
2.  资源获取包括获取本应用包资源、应用内跨包资源、跨应用包资源。 获取本应用包resourceManager对象，通过.context().resourceManager方法。 获取应用内跨包resourceManager对象，通过.context().createModuleContext().resourceManager 方法。 获取跨应用包resourceManager对象，通过.context.createModuleContext(bundleName:'bundleName name',moduleName:'module name').resourceManager方法，该方法仅支持系统应用使用。 Context的更多使用信息请参考应用上下文Context。
3.  调用Native接口getFileList即为src/main/cpp/types/libentry/index.d.ts中声明的接口，传入js的资源对象，以及rawfile文件夹的相对路径。 获取本应用包资源resourceManager对象的示例如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/thread-scheduling-V14
爬取时间: 2025-04-30 06:29:03
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/qos-guidelines-V14
爬取时间: 2025-04-30 06:29:17
来源: Huawei Developer
场景介绍
自多道程序及多任务操作系统问世以来，CPU、内存等有限的系统资源成为系统中所有任务的竞争对象。合理安排各个任务对系统的响应速度以及资源消耗都有非常重大的意义。相比操作系统，开发者更加清楚应用中各个任务的重要程度；根据重要程度对应用的任务进行分类，能帮助系统更好地进行任务的调度。通过本指导，开发者可以了解在HarmonyOS系统中，如何利用QoS特性及相关的接口调节任务在系统中的运行时间分配。
本文用于指导开发者基于QoS特性实现应用任务优先调度属性自定义。
基本概念
QoS
QoS(quality-of-service)，即服务质量，在HarmonyOS中QoS特性主要指任务的优先调度属性。开发者可以利用QoS对要执行的工作进行分类，以指示其与用户交互的关联程度；系统则可以根据任务设置的QoS安排各任务的运行时间和运行次序。例如，当系统中有多个任务需要同时执行时，一些与用户交互关联程度不高的后台下载任务可以推迟到更晚的时间执行，且每次执行时分配更少的时间；而用户感知明显的动效绘制等任务则需要立即执行，并分配更多的执行时间。
QoS等级定义
目前，HarmonyOS系统一共划分了如下6个QoS等级，从上到下与用户交互的关联程度依次递增，适用于多种不同的应用场景及负载特征情况。
| QoS等级 | 使用场景 | 负载特征 |
| --- | --- | --- |
| QOS_BACKGROUND | 后台且用户不可见任务，例如数据同步、备份。 | 任务完成需要几分钟甚至几小时。 |
| QOS_UTILITY | 不需要立即看到响应效果的任务，例如下载或导入数据。 | 任务完成需要几秒到几分钟。 |
| QOS_DEFAULT | 默认。 | 任务完成需要几秒钟。 |
| QOS_USER_INITIATED | 用户触发并且可见进展的任务，例如打开文档。 | 任务在几秒钟之内完成。 |
| QOS_DEADLINE_REQUEST | 越快越好的关键任务，如页面加载。 | 任务几乎是瞬间完成的。 |
| QOS_USER_INTERACTIVE | 用户交互任务（UI线程、刷新界面、动效）。 | 任务是即时的。 |
QoS等级定义为枚举类型QoS_Level，如上表所示；枚举值定义如下。
QoS_Level声明
功能效果
QoS等级更高的任务相对等级更低的可能被分配更多的CPU时间。
下面将展示合理使用QoS对程序执行的优化效果。
QoS对线程执行的优化
优化前
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165818.33898056133174554992391404677803:50001231000000:2800:B72BDC5586298AA74FEF1C314E1190D107C201EC3DE08D6ED2F2CFE8BDFA66D6.png)
线程1和线程2是某程序的两个关键线程，线程1在运行时会触发新任务线程2，等线程2执行完后会唤醒线程1继续执行。在未标记这两个线程的QoS等级之前，其优先执行顺序低于线程3和线程4；此时线程1和线程2的执行效果如上图所示：
1.  线程1等待被线程2唤醒，而线程2优先级低，长时间被抢占，导致线程1长时间睡眠；
2.  线程1优先级低，它被唤醒后等待运行时间长；
3.  线程1优先级低，运行过程中长时间被其它线程抢占。
优化后
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165818.93209553251502902328837488298980:50001231000000:2800:66BA8BC53386C1852A24A7745705451F8F17F7A9D3B427E70451DBA210CF7496.png)
合理标记线程1和线程2的QoS等级后，两个线程的执行优化效果如上图所示：
1.  线程2运行时间占比提高，线程1等待时间减少；
2.  线程1被线程2唤醒后，等待的时间减少；
3.  线程1运行实际占比提高，被抢占比例减少。
QoS对RN框架的优化
在RN框架中合理标记关键线程的QoS等级后，如下表所示，开源benchmark测试的性能提升了约13%。
| 验证场景 | 验证环境 | 总渲染时间 |
| --- | --- | --- |
| benchmark 1500view  | 无QoS优化 | 270.8 ms |
| benchmark 1500view  | 使用QoS优化 | 236.6 ms |
benchmark
1500view
benchmark
1500view
接口说明
| 接口名 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| OH_QoS_SetThreadQoS(QoS_Level level) | 设置当前任务的QoS等级。 | QoS_Level level | 0或-1 |
| OH_QoS_ResetThreadQoS() | 取消当前任务设置的QoS等级。 | 无 | 0或-1 |
| OH_QoS_GetThreadQoS(QoS_Level *level) | 获取当前任务的QoS等级。 | QoS_Level *level | 0或-1 |
使用限制
函数介绍
OH_QoS_SetThreadQoS
声明
参数
QoS_Level level
返回值
描述
为某个任务设置指定的QoS等级。
样例
OH_QoS_ResetThreadQoS
声明
参数
返回值
描述
取消某个任务设置的QoS等级。
样例
OH_QoS_GetThreadQoS
声明
参数
QoS_Level *level
返回值
描述
获取某个任务之前最近一次设置的QoS等级；如果之前未设置任何QoS等级，则返回-1。
样例
开发步骤
以下步骤描述了如何使用QoS特性提供的Native API接口，调整或查询任务的QoS等级。
1. 添加动态链接库
QoS特性的使用依赖相关的动态链接库：libqos.so；需要在目标应用或程序的编译环境中添加。
示例
使用DevEco Studio创建的模板NDK工程，会默认生成CMakeLists.txt脚本，在其中添加QoS相关动态链接库示例如下：
2. 引用头文件
在使用QoS特性的源代码中需要引用相关的头文件。
3. 调用QoS接口
开发者根据自身需求调用相应的QoS接口调整任务的QoS等级，或者查询任务的QoS等级。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/memory-management-V14
爬取时间: 2025-04-30 06:29:31
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/purgeable-memory-guidelines-V14
爬取时间: 2025-04-30 06:29:45
来源: Huawei Developer
场景介绍
HarmonyOS提供Purgeable Memory内存管理机制，开发者可以使用相关接口创建PurgeableMemory对象，从而管理purgeable内存。
开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native层相关接口操作purgeable内存。功能包括purgeable内存的申请、释放等。
针对Purgeable Memory内存管理机制，常见的开发场景如下：
接口说明
| 接口名 | 描述 |
| --- | --- |
| OH_PurgeableMemory *OH_PurgeableMemory_Create(size_t size, OH_PurgeableMemory_ModifyFunc func, void *funcPara) | 创建PurgeableMemory对象，每次调用都会产生一个新的PurgeableMemory对象。 |
| bool OH_PurgeableMemory_Destroy(OH_PurgeableMemory *purgObj) | 对PurgeableMemory对象进行析构操作。 |
| bool OH_PurgeableMemory_BeginRead(OH_PurgeableMemory *purgObj) | 对PurgeableMemory对象进行读访问。 |
| void OH_PurgeableMemory_EndRead(OH_PurgeableMemory *purgObj) | 读操作结束，将PurgeableMemory对象的引用计数减1，当引用计数为0的时候， 该PurgeableMemory对象可以被系统回收。 |
| bool OH_PurgeableMemory_BeginWrite(OH_PurgeableMemory *purgObj) | 对PurgeableMemory对象进行写访问。 |
| void OH_PurgeableMemory_EndWrite(OH_PurgeableMemory *purgObj) | 写操作结束，将PurgeableMemory对象的引用计数减1，当引用计数为0的时候，该PurgeableMemory对象可以被系统回收。 |
| void *OH_PurgeableMemory_GetContent(OH_PurgeableMemory *purgObj) | 获取PurgeableMemory对象内存数据。 |
| size_t OH_PurgeableMemory_ContentSize(OH_PurgeableMemory *purgObj) | 获取PurgeableMemory对象内存数据大小。 |
| bool OH_PurgeableMemory_AppendModify(OH_PurgeableMemory *purgObj, OH_PurgeableMemory_ModifyFunc func, void *funcPara) | 添加PurgeableMemory对象的修改方法。 |
Purgeable Memory应用开发步骤
以下步骤描述了在HarmonyOS中如何使用Purgeable Memory提供的NAPI接口，申请PurgeableMemory对象，并将内容写入PurgeableMemory对象后，对相应对象进行读写访问。
1.  声明PurgeableMemory对象创建规则。
2.  创建PurgeableMemory对象。
3.  读访问PurgeableMemory对象。
4.  写访问PurgeableMemory对象。
5.  销毁PurgeableMemory对象。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/device-management-V14
爬取时间: 2025-04-30 06:29:59
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/usb-ddk-guidelines-V14
爬取时间: 2025-04-30 06:30:13
来源: Huawei Developer
场景介绍
USB DDK（USB Driver Develop Kit）是为开发者提供的USB驱动程序开发套件，支持开发者基于用户态，在应用层开发USB设备驱动。提供了一系列主机侧访问设备的接口，包括主机侧打开和关闭接口、管道同步异步读写通信、控制传输、中断传输等。
约束与限制
-  USB DDK开放API支持USB接口非标外设扩展驱动开发场景。
-  USB DDK开放API使用范围内仅允许DriverExtensionAbility生命周期内使用。
-  使用USB DDK开放API需要在module.json5中声明匹配的ACL权限，例如ohos.permission.ACCESS_DDK_USB。
接口说明
| 名称 | 描述 |
| --- | --- |
| OH_Usb_Init(void) | 初始化DDK。 |
| OH_Usb_Release(void) | 释放DDK。 |
| OH_Usb_GetDeviceDescriptor(uint64_t deviceId, struct UsbDeviceDescriptor *desc) | 获取设备描述符。 |
| OH_Usb_GetConfigDescriptor(uint64_t deviceId, uint8_t configIndex, struct UsbDdkConfigDescriptor **const config) | 获取配置描述符。请在描述符使用完后使用OH_Usb_FreeConfigDescriptor()释放描述符，否则会造成内存泄露。 |
| OH_Usb_FreeConfigDescriptor(const struct UsbDdkConfigDescriptor *const config) | 释放配置描述符，请在描述符使用完后释放描述符，否则会造成内存泄露。 |
| OH_Usb_ClaimInterface(uint64_t deviceId, uint8_t interfaceIndex, uint64_t *interfaceHandle) | 声明接口。 |
| OH_Usb_SelectInterfaceSetting(uint64_t interfaceHandle, uint8_t settingIndex) | 激活接口的备用设置。 |
| OH_Usb_GetCurrentInterfaceSetting(uint64_t interfaceHandle, uint8_t *settingIndex) | 获取接口当前激活的备用设置。 |
| OH_Usb_SendControlReadRequest(uint64_t interfaceHandle, const struct UsbControlRequestSetup *setup, uint32_t timeout, uint8_t *data, uint32_t *dataLen) | 发送控制读请求，该接口为同步接口。 |
| OH_Usb_SendControlWriteRequest(uint64_t interfaceHandle, const struct UsbControlRequestSetup *setup, uint32_t, const uint8_t *data, uint32_t dataLen) | 发送控制写请求，该接口为同步接口。 |
| OH_Usb_ReleaseInterface(uint64_t interfaceHandle) | 释放接口。 |
| OH_Usb_SendPipeRequest(const struct UsbRequestPipe *pipe, UsbDeviceMemMap *devMmap) | 发送管道请求，该接口为同步接口。中断传输和批量传输都使用该接口发送请求。 |
| OH_Usb_CreateDeviceMemMap(uint64_t deviceId, size_t size, UsbDeviceMemMap **devMmap) | 创建缓冲区。请在缓冲区使用完后，调用OH_Usb_DestroyDeviceMemMap()销毁缓冲区，否则会造成资源泄露。 |
| OH_Usb_DestroyDeviceMemMap(UsbDeviceMemMap *devMmap) | 销毁缓冲区。请在缓冲区使用完后及时销毁缓冲区，否则会造成资源泄露。 |
名称
描述
OH_Usb_Init(void)
初始化DDK。
OH_Usb_Release(void)
释放DDK。
OH_Usb_GetDeviceDescriptor(uint64_t deviceId, struct UsbDeviceDescriptor *desc)
获取设备描述符。
OH_Usb_GetConfigDescriptor(uint64_t deviceId, uint8_t configIndex, struct UsbDdkConfigDescriptor **const config)
获取配置描述符。请在描述符使用完后使用OH_Usb_FreeConfigDescriptor()释放描述符，否则会造成内存泄露。
OH_Usb_FreeConfigDescriptor(const struct UsbDdkConfigDescriptor *const config)
释放配置描述符，请在描述符使用完后释放描述符，否则会造成内存泄露。
OH_Usb_ClaimInterface(uint64_t deviceId, uint8_t interfaceIndex, uint64_t *interfaceHandle)
声明接口。
OH_Usb_SelectInterfaceSetting(uint64_t interfaceHandle, uint8_t settingIndex)
激活接口的备用设置。
OH_Usb_GetCurrentInterfaceSetting(uint64_t interfaceHandle, uint8_t *settingIndex)
获取接口当前激活的备用设置。
OH_Usb_SendControlReadRequest(uint64_t interfaceHandle, const struct UsbControlRequestSetup *setup, uint32_t timeout, uint8_t *data, uint32_t *dataLen)
发送控制读请求，该接口为同步接口。
OH_Usb_SendControlWriteRequest(uint64_t interfaceHandle, const struct UsbControlRequestSetup *setup, uint32_t, const uint8_t *data, uint32_t dataLen)
发送控制写请求，该接口为同步接口。
OH_Usb_ReleaseInterface(uint64_t interfaceHandle)
释放接口。
OH_Usb_SendPipeRequest(const struct UsbRequestPipe *pipe, UsbDeviceMemMap *devMmap)
发送管道请求，该接口为同步接口。中断传输和批量传输都使用该接口发送请求。
OH_Usb_CreateDeviceMemMap(uint64_t deviceId, size_t size, UsbDeviceMemMap **devMmap)
创建缓冲区。请在缓冲区使用完后，调用OH_Usb_DestroyDeviceMemMap()销毁缓冲区，否则会造成资源泄露。
OH_Usb_DestroyDeviceMemMap(UsbDeviceMemMap *devMmap)
销毁缓冲区。请在缓冲区使用完后及时销毁缓冲区，否则会造成资源泄露。
详细的接口说明请参考USB DDK。
开发步骤
以下步骤描述了如何使用USB DDK开发USB驱动：
添加动态链接库
CMakeLists.txt中添加以下lib。
头文件
1.  获取设备描述符。 使用usb_ddk_api.h的OH_Usb_Init接口初始化DDK，并使用OH_Usb_GetDeviceDescriptor获取到设备描述符。
2.  获取配置描述符及声明接口。 使用usb_ddk_api.h的OH_Usb_GetConfigDescriptor接口获取配置描述符config，并使用 OH_Usb_ClaimInterface 声明"认领"接口。
3.  获取当前激活接口的备用设置及激活备用设置。 使用usb_ddk_api.h的OH_Usb_GetCurrentInterfaceSetting获取备用设置，并使用OH_Usb_SelectInterfaceSetting激活备用设置。
4.  发送控制读请求、发送控制写请求。 使用usb_ddk_api.h的OH_Usb_SendControlReadRequest发送控制读请求，或者使用OH_Usb_SendControlWriteRequest发送控制写请求。
5.  创建内存映射缓冲区及发送请求。 使用usb_ddk_api.h的OH_Usb_CreateDeviceMemMap接口创建内存映射缓冲区devMmap，并使用OH_Usb_SendPipeRequest发送请求。
6.  释放资源。 在所有请求处理完毕，程序退出前，使用usb_ddk_api.h的OH_Usb_DestroyDeviceMemMap接口销毁缓冲区。使用OH_Usb_ReleaseInterface释放接口。使用OH_Usb_Release释放USB DDK。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hid-ddk-guidelines-V14
爬取时间: 2025-04-30 06:30:27
来源: Huawei Developer
场景介绍
HID DDK（HID Driver Develop Kit）是为开发者提供的HID设备驱动程序开发套件，支持开发者基于用户态，在应用层开发HID设备驱动。提供了一系列主机侧访问设备的接口，包括创建设备、向设备发送事件、销毁设备。
约束与限制
-  HID DDK开放API支持非标HID类外设扩展驱动开发场景。
-  HID DDK开放API使用范围内仅允许DriverExtensionAbility生命周期内使用。
-  使用HID DDK开放API需要在module.json5中声明匹配的ACL权限，例如ohos.permission.ACCESS_DDK_HID。
接口说明
| 名称 | 描述 |
| --- | --- |
| OH_Hid_CreateDevice(Hid_Device *hidDevice, Hid_EventProperties *hidEventProperties) | 创建HID设备。请在设备使用完后使用OH_Hid_DestroyDevice销毁设备 |
| OH_Hid_EmitEvent(int32_t deviceId, const Hid_EmitItem items[], uint16_t length) | 向指定deviceId的HID设备发送事件。 |
| OH_Hid_DestroyDevice(int32_t deviceId) | 销毁指定deviceId的HID设备。 |
名称
描述
OH_Hid_CreateDevice(Hid_Device *hidDevice, Hid_EventProperties *hidEventProperties)
创建HID设备。请在设备使用完后使用OH_Hid_DestroyDevice销毁设备
OH_Hid_EmitEvent(int32_t deviceId, const Hid_EmitItem items[], uint16_t length)
向指定deviceId的HID设备发送事件。
OH_Hid_DestroyDevice(int32_t deviceId)
销毁指定deviceId的HID设备。
详细的接口说明请参考HID DDK。
开发步骤
以下步骤描述了如何使用HID DDK开发HID设备驱动：
添加动态链接库
CMakeLists.txt中添加以下lib。
头文件
1.  创建设备。 使用hid_ddk_api.h的OH_Hid_CreateDevice接口创建HID设备，成功返回设备deviceId（非负数），失败返回错误码（负数）。
2.  向指定deviceId的HID设备发送事件。 使用hid_ddk_api.h的OH_Hid_EmitEvent向指定的deviceId的设备发送事件。
3.  释放资源。 在所有请求处理完毕，程序退出前，使用hid_ddk_api.h的OH_Hid_DestroyDevice接口销毁HID设备。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/bundle-management-V14
爬取时间: 2025-04-30 06:30:40
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/native-bundle-guidelines-V14
爬取时间: 2025-04-30 06:31:34
来源: Huawei Developer
场景介绍
开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native Bundle接口获取应用自身相关信息。
接口说明
| 接口名 | 描述 |
| --- | --- |
| OH_NativeBundle_GetCurrentApplicationInfo | 获取应用自身相关信息。 |
| OH_NativeBundle_GetAppId | 获取自身应用的appId信息。 |
| OH_NativeBundle_GetAppIdentifier | 获取自身应用的appIdentifier信息。 |
| OH_NativeBundle_GetMainElementName | 获取自身应用入口的信息。 |
| OH_NativeBundle_GetCompatibleDeviceType | 获取自身应用适用的设备类型。 |
开发步骤
1. 创建工程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165818.97191582610764167764323285435105:50001231000000:2800:14A32FFB7F78D743FD8CD359C530CADE559A2F9DDEB9A3C39F5879F246071846.png)
2. 添加依赖
创建完成后，DevEco Studio会在工程生成cpp目录，目录有types/libentry/index.d.ts、napi_init.cpp、CMakeLists.txt等文件。
1.  打开src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加包管理的libbundle_ndk.z.so。
2.  打开src/main/cpp/napi_init.cpp文件，添加头文件。
3. 修改源文件
1.  打开src/main/cpp/napi_init.cpp文件，文件Init会对当前方法进行初始化映射，这里定义对外接口为getCurrentApplicationInfo。
2.  在src/main/cpp/napi_init.cpp文件中，增加对应的方法，如下所示：
3.  在src/main/cpp/napi_init.cpp文件中获取Native的包信息对象，并转为js的包信息对象，即可在js测获取应用的信息：
4. js侧调用
1.  打开src\main\ets\pages\index.ets, 导入"libentry.so"。
2.  调用Native接口getCurrentApplicationInfo即可获取应用信息。示例如下：
关于包管理NDK开发，可参考Bundle模块介绍。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/debugging-profiling-V14
爬取时间: 2025-04-30 06:31:48
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/debug-performance-profiling-overview-V14
爬取时间: 2025-04-30 06:32:02
来源: Huawei Developer
通过NDK开发C/C++程序不可避免会遇到Native程序常见的异常、性能等问题，NDK随包提供了常用的调试调优工具，方便开发者定位问题。
已提供如下方式进行调试和性能分析：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/debug-ide-V14
爬取时间: 2025-04-30 06:32:15
来源: Huawei Developer
DevEco Studio提供了丰富的调试能力，在NDK开发过程中可以利用这些能力检测并修复程序中的错误。调试能力包括：
-  使用真机进行调试：将应用/服务运行到真机设备上并进行调试，具体请参见使用真机进行调试。 在调试过程中，如果本地编译设备so文件的源码路径和当前配置的C++源码路径不一致，可以分为以下两种场景处理： 建立文件间映射关系：参考三方源码调试，当Step Into进入汇编代码后，会弹出源码关联的提示，请点击“Select file”，选择本地对应C++源码进行关联。 建议路径间映射关系：选择Run > Edit Configurations，选择模块后，切换到Debugger页签，选择Native类型，在LLDB Startup Commands页签中，新增“settings set target.source-map "/buildbot/path" "/my/path"”命令建立映射关系，其中参数一为编译环境中的源码路径，参数二为本地源码路径。
-  建立文件间映射关系：参考三方源码调试，当Step Into进入汇编代码后，会弹出源码关联的提示，请点击“Select file”，选择本地对应C++源码进行关联。
-  建议路径间映射关系：选择Run > Edit Configurations，选择模块后，切换到Debugger页签，选择Native类型，在LLDB Startup Commands页签中，新增“settings set target.source-map "/buildbot/path" "/my/path"”命令建立映射关系，其中参数一为编译环境中的源码路径，参数二为本地源码路径。
-  C/C++反向调试：在调试过程中可以回退到历史行和历史断点，查看相关变量信息，具体请参见C/C++反向调试。
-  建立文件间映射关系：参考三方源码调试，当Step Into进入汇编代码后，会弹出源码关联的提示，请点击“Select file”，选择本地对应C++源码进行关联。
-  建议路径间映射关系：选择Run > Edit Configurations，选择模块后，切换到Debugger页签，选择Native类型，在LLDB Startup Commands页签中，新增“settings set target.source-map "/buildbot/path" "/my/path"”命令建立映射关系，其中参数一为编译环境中的源码路径，参数二为本地源码路径。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165819.51321718068383306151121259230147:50001231000000:2800:293CBF7516AEB1AAD53DF8EB2539283D49FA11AE4BEA8BE678E899622665C858.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165819.75900351741916876409939704705598:50001231000000:2800:76250C7ADEA5CFA62C3888F99F7508C27FC1D06694936F90272365CBB8094C29.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/debug-lldb-V14
爬取时间: 2025-04-30 06:32:29
来源: Huawei Developer
概述
LLDB（Low Level Debugger）是新一代高性能调试器。详细说明参考LLDB官方文档。
当前HarmonyOS中的LLDB工具是在llvm15.0.4基础上适配演进出来的工具，是HUAWEI DevEco Studio工具中默认的调试器，支持调试C和C++应用。
工具获取
可通过HUAWEI DevEco Studio下载SDK获取LLDB调试工具。
以Windows平台为例，lldb.exe的存放路径为sdk\[HarmonyOS版本]\openharmony\native\llvm\bin。例如“sdk\HarmonyOS-NEXT-DP1\openharmony\native\llvm\bin”。
| 路径  | 说明  |
| --- | --- |
| sdk\[HarmonyOS版本]\hms\native\lldb\aarch64-linux-ohos\lldb-server  | 适用于aarch64-linux-ohos架构的lldb-server  |
| sdk\[HarmonyOS版本]\hms\native\lldb\arm-linux-ohos\lldb-server  | 适用于arm-linux-ohos架构的lldb-server  |
| sdk\[HarmonyOS版本]\hms\native\lldb\x86_64-linux-ohos\lldb-server  | 适用于x86_64-linux-ohos架构的lldb-server  |
路径
说明
sdk\[HarmonyOS版本]\hms\native\lldb\aarch64-linux-ohos\lldb-server
适用于aarch64-linux-ohos架构的lldb-server
sdk\[HarmonyOS版本]\hms\native\lldb\arm-linux-ohos\lldb-server
适用于arm-linux-ohos架构的lldb-server
sdk\[HarmonyOS版本]\hms\native\lldb\x86_64-linux-ohos\lldb-server
适用于x86_64-linux-ohos架构的lldb-server
功能列表
此处列举LLDB调试器支持的部分功能，更多命令参考：LLDB工具使用指导和LLDB官网手册。Windows、Linux x86_64和Mac平台的LLDB工具有些许差异，以实际应用为准。
-  记录日志
-  断点管理
-  观察点管理
-  表达式处理
-  查看变量
-  进程/线程管理
-  汇编处理
-  源码信息获取
-  信号处理
-  进程启动
-  attach进程
应用场景
-  Linux x86_64本地调试。 LLDB支持在Linux x86_64环境上调试C和C++应用。 Mac桌面本地调试。 LLDB支持在Mac桌面（包括Mac x86_64和M1系统）调试C和C++应用。
-  Linux x86_64本地调试。 LLDB支持在Linux x86_64环境上调试C和C++应用。
-  Mac桌面本地调试。 LLDB支持在Mac桌面（包括Mac x86_64和M1系统）调试C和C++应用。
-  基于HUAWEI DevEco Studio的远程调试。 LLDB支持基于HUAWEI DevEco Studio在Windows和Mac桌面连接HarmonyOS设备或模拟器远程调试Native C++应用，即使用HUAWEI DevEco Studio的Debug调试功能。 桌面连接HarmonyOS设备远程调试。 HarmonyOS设备为root镜像，SELinux关闭：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试C和C++应用以及可执行二进制。 HarmonyOS设备为root镜像，SELinux开启：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试C和C++应用以及可执行二进制，但是lldb-server和要调试的应用或可执行二进制只能放在/data/local/tmp/debugserver目录内。 HarmonyOS设备是user镜像，SELinux开启：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试基于HUAWEI DevEco Studio编译的带签名的debug版本的hap包，目前仅支持此类调试。 root镜像：使用hdc shell id命令查询到“uid=0(root)”，或执行hdc shell进入交互命令环境，提示符为“#”。 user镜像：使用hdc shell id命令查询到“uid=2000(shell)”，或执行hdc shell进入交互命令环境，提示符为“$”。 SELinux开启模式：使用hdc shell getenforce命令查询到“Enforcing”。 SELinux关闭模式：使用hdc shell getenforce命令查询到“Permissive”。
-  基于HUAWEI DevEco Studio的远程调试。 LLDB支持基于HUAWEI DevEco Studio在Windows和Mac桌面连接HarmonyOS设备或模拟器远程调试Native C++应用，即使用HUAWEI DevEco Studio的Debug调试功能。
-  桌面连接HarmonyOS设备远程调试。 HarmonyOS设备为root镜像，SELinux关闭：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试C和C++应用以及可执行二进制。 HarmonyOS设备为root镜像，SELinux开启：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试C和C++应用以及可执行二进制，但是lldb-server和要调试的应用或可执行二进制只能放在/data/local/tmp/debugserver目录内。 HarmonyOS设备是user镜像，SELinux开启：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试基于HUAWEI DevEco Studio编译的带签名的debug版本的hap包，目前仅支持此类调试。 root镜像：使用hdc shell id命令查询到“uid=0(root)”，或执行hdc shell进入交互命令环境，提示符为“#”。 user镜像：使用hdc shell id命令查询到“uid=2000(shell)”，或执行hdc shell进入交互命令环境，提示符为“$”。 SELinux开启模式：使用hdc shell getenforce命令查询到“Enforcing”。 SELinux关闭模式：使用hdc shell getenforce命令查询到“Permissive”。
-  Linux x86_64本地调试。 LLDB支持在Linux x86_64环境上调试C和C++应用。
-  Mac桌面本地调试。 LLDB支持在Mac桌面（包括Mac x86_64和M1系统）调试C和C++应用。
-  基于HUAWEI DevEco Studio的远程调试。 LLDB支持基于HUAWEI DevEco Studio在Windows和Mac桌面连接HarmonyOS设备或模拟器远程调试Native C++应用，即使用HUAWEI DevEco Studio的Debug调试功能。
-  桌面连接HarmonyOS设备远程调试。 HarmonyOS设备为root镜像，SELinux关闭：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试C和C++应用以及可执行二进制。 HarmonyOS设备为root镜像，SELinux开启：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试C和C++应用以及可执行二进制，但是lldb-server和要调试的应用或可执行二进制只能放在/data/local/tmp/debugserver目录内。 HarmonyOS设备是user镜像，SELinux开启：LLDB支持在Windows、Mac桌面和Linux x86_64环境直连HarmonyOS设备远程调试基于HUAWEI DevEco Studio编译的带签名的debug版本的hap包，目前仅支持此类调试。 root镜像：使用hdc shell id命令查询到“uid=0(root)”，或执行hdc shell进入交互命令环境，提示符为“#”。 user镜像：使用hdc shell id命令查询到“uid=2000(shell)”，或执行hdc shell进入交互命令环境，提示符为“$”。 SELinux开启模式：使用hdc shell getenforce命令查询到“Enforcing”。 SELinux关闭模式：使用hdc shell getenforce命令查询到“Permissive”。
使用指导-本地调试
Linux x86_64或Mac本地调试步骤一致。
使用LLDB工具启动并调试应用
此处以在Linux x86_64环境调试一个使用clang编译器生成的带有调试信息的可执行文件a.out为例。
源文件：hello.cpp
编译：
使用LLDB工具调试已经启动的应用
此处以在Mac环境调试一个使用clang编译器生成的带有调试信息和用户输入的可执行文件a.out为例。
源文件：hello.cpp
编译：
步骤attach应用和设置断点可以调换顺序执行。
使用指导-远程调试
root镜像远程调试
源文件：hello.cpp
编译：
user镜像远程调试
FAQ

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/debug-asan-V14
爬取时间: 2025-04-30 06:33:23
来源: Huawei Developer
为追求C/C++的更优性能，编译器和OS(Windows/Linux/Mac)运行框架不会对内存操作进行安全检测。针对该场景，DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。
关于ASan的使用说明请参见C/C++内存错误检测。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hardware-compatibility-V14
爬取时间: 2025-04-30 06:33:36
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hw-guide-V14
爬取时间: 2025-04-30 06:33:50
来源: Huawei Developer
使用C/C++开发HarmonyOS应用原生库时，需要感知到硬件特性；HarmonyOS系统会运行在多种架构、多厂商的设备上，对于使用了HarmonyOS原生库的应用，如何保证其在不同设备上的兼容性以及体验的一致性是一个很大的挑战。
本章节将介绍HarmonyOS应用二进制接口（Application Binary Interface，简称ABI），定义了当前HarmonyOS系统支持的ABI标准；同时也提供了如何使用CPU扩展特性的指导，方便应用在不破坏兼容性的基础上更好的利用CPU硬件特性。最后通过一些简单的示例演示如何更好的使用ARM Neon特性。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ohos-abi-V14
爬取时间: 2025-04-30 06:34:05
来源: Huawei Developer
HarmonyOS系统支持丰富的设备形态，支持多种架构指令集，支持多种操作系统内核；HarmonyOS遵循“OHOS”ABI定义，保持与社区ABI的一致性。
本文定义了"OHOS" ABI（Application Binary Interface）的基础标准，包含如下方面。
字节序和字宽
"OHOS" ABI始终采用little-endian，32位系统采用ILP32，64位系统采用LP64。
过程调用规范
过程调用规范（Procedure Call Standard）定义了函数调用的参数传递方式，寄存器使用规则，栈操作规则等；不同C++编译器，不同操作系统，不同架构都有可能采用不同的调用规则。详细内容请参考《不同C++编译器和操作系统的调用规范》。架构相关的函数调用规范，请参考：
-  ARM相关的调用规范请参考《ARM32过程调用标准》。
-  ARM64相关的调用规范请参考《ARM64过程调用标准》。
C++ ABI
HarmonyOS系统采用llvm项目中的libc++作为C++运行时库，在系统侧使用libc++.so库来承载，应用侧使用libc++_shared.so来承载，两侧共用一套代码，采用不同的C++命名空间。C++的符号重整规则请参考《Itanium C++ ABI》。
浮点格式
采用IEEE754作为浮点编码格式，针对long double的格式定义，将在支持架构ABI具体说明。
可执行文件格式
HarmonyOS系统采用ELF文件格式作为全系统的二进制文件格式，具体格式详情，请参考《System V Application Binary Interface》。CPU架构相关的格式定义，参考下面对应架构说明。
-  arm相关的elf文件格式定义请参考《arm架构elf文件格式》。
-  arm64相关elf文件格式定义请参考《arm64架构elf文件格式》。
支持架构ABI
下面介绍下当前“OHOS” ABI中支持的架构以及差异点。
armeabi-v7a
此ABI是以《ARM架构应用二进制接口》为基础制定，适用于32位armv7a架构的cpu，支持的核心包括Cortex-A5，Cortex-A7，Cortex-A8，Cortex-A9，Cortex-A12，Cortex-A15，以及Cortex-A17，支持arm32，thumb-2，VFPv3-D16指令。
此ABI使用-mfloat-cpu=softfp作为强制浮点数调用规则，本身不影响实际指令是否使用硬件浮点指令。Neon指令等其他扩展在此ABI中是可选的，为了更好的兼容性，建议应用开发者采用-mfpu=softvfp来编译native库 。
此ABI使用64位long double(IEEE binary64)。
当前通过DevEco Studio构建NDK工程时，不支持armeabi-v7a编译环境。如需要在HarmonyOS中使用该编译环境，需要通过CMake方式构建。
arm64-v8a
此ABI是以《ARM架构应用二进制接口》为基础制定，支持AArch64指令集，默认支持neon特性。
此ABI使用-mfloat-cpu=softfp作为强制浮点数调用规则。
此ABI使用128位long double(IEEE binary128)。
x86_64
此ABI是以Intel64和IA-32 ABI为基础，支持MMX、SSE、SSE2、SSE3、SSSE3、SSE4.1等指令，与x86相关的规范参考《System V Application Binary Interface》、《AMD64 Architecture Processor Supplement》。
此ABI使用128位long double(IEEE binary128)，x86架构上很多平台采用float80格式，HarmonyOS仍然采用128bit形式。
在编译架构中指定ABI
DevEco Studio中设置
在HarmonyOS的C++工程中，找到C++代码所在项目build-profile.json5文件buildOption/externalNativeOptions字段，添加abiFilters字段：
```json
{
“abiType”: 'stageMode',
“buildOption”： {
“externalNativeOptions”: {
"path": "./src/main/cpp/CMakeLists.txt",
"arguments": "",
"abiFilters": [
"armeabi-v7a",
"arm64-v8a"
]
}
}
}
```
cmake中设置
通过SDK CAPI开发native代码的时候，在build/cmake/ohos.toolchain.cmake中定义了HarmonyOS系统一些交叉编译常用的环境变量设置。其中OHOS_ARCH变量定义了当前目标编译的ABI，可以设置下面三个ABI中的一种，arm64-v8a，armeabi-v7a，x86_64。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/cpu-features-V14
爬取时间: 2025-04-30 06:34:19
来源: Huawei Developer
CPU特性是CPU提供的一些硬件扩展。开发者可以通过调用指令，设置特殊寄存器来使用这些CPU特性，例如ARMv7a架构上的VFP-v32d32、NEON、IDIV、AES等CPU特性。很多CPU特性是可选的，不同厂商的CPU通常有不同的特性。
在HarmonyOS原生库开发中，如何使用CPU特性？如何在代码中处理CPU特性相关的代码？本章节将提供一些方法，以便帮助开发者开发出既能保持兼容性，又能利用CPU特有能力的应用。
HarmonyOS系统当前没有提供获取CPU特性的接口，开发者可以导入现有开源社区的库函数，具体可以参考如下的例子；也可直接读取/proc/cpuinfo，或者调用libc getauxval(AT_HWCAP)接口来获取设备的CPU特性。
使用建议
1.  在HarmonyOS系统C++工程中引入开源库，下载cpu_features库，解压到工程的cpp目录下。如下以IDE C++模版示例应用举例：
2.  在代码中加入判断CPU特性支持能力语句，如下以支持ARM与AARCH64两种架构举例： cpu_features库实际上是通过/proc/cpuinfo，与getauxval接口从内核中读取对应的CPU特性信息，有可能由于应用沙盒的原因导致无法读取对应的信息，注意错误处理。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/neon-guide-V14
爬取时间: 2025-04-30 06:34:32
来源: Huawei Developer
ARM Neon是ARM架构的SIMD（Single Instruction Multiple Data）扩展实现，提供一条指令处理多个数据的并行处理能力，广泛用于多媒体编解码、2D/3D图形处理等领域，提高执行性能。
Neon扩展从ARMv7开始被采用，目前在Cortex-A7、Cortex-A12、Cortex-A15处理器中被设置为默认选项，但在其余的ARMv7 Cortex-A系列中是可选项。具体技术细节请参考《Introducing NEON Development Article》。
ARMv8a架构CPU默认集成Neon扩展，在AArch64与AArch32两种状态下都支持，详细请参考ARM官方文档《Learn the architecture - Introducing Neon》。
HarmonyOS架构支持情况
在HarmonyOS系统中，arm64-v8a ABI下默认已经开启了对Neon扩展的支持；在armeabi-v7a ABI下，为了能够尽可能的支持ARMv7a架构设备，默认不开启Neon扩展。
在HarmonyOS SDK的LLVM工具链中，为armeabi-v7a ABI提供了对多种配置的预编译运行时库的支持，供开发者根据不同的配置进行选择。具体目录结构如下，native-root表示NDK所在的native包解压根目录。
其中hard、soft、softfp是float-abi，未指定默认采用softfp；neon-vfpv4就是-mfpu指定的参数类型，LLVM工具链根据相应编译参数选择依赖不同架构配置的二进制库。
如何使用
使用Neon扩展的主要通过如下几种方式：
-  使用LLVM的Auto-Vectorization特性，由编译器来生成对应指令，默认开启，可以通过-fno-vectorize关闭，具体参考《Auto-Vectorization in LLVM》。
-  使用Neon intrinsics库，方便开发者直接操作低阶Neon指令。
-  手工写Neon汇编指令。
详细可以参考《Arm Neon架构》。
举例说明
下面举例说明在一个armeabi-v7a HarmonyOS C++工程中如何使用Neon intrinsics。
1.  使用Neon intrinsics需要在源码包含arm_neon.h头文件，由于该特性与CPU架构强相关，在包含该头文件时，推荐用cpu features等宏括起来。
2.  在函数实现处，根据CPU特性调用对应的实现函数。
3.  在CMakeLists.txt文件中添加对应选项。
上述步骤完成后，开发者即可在工程中使用Neon intrinsics指令。

