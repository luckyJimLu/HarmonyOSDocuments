# 合并文件
合并时间: 2025-04-30 21:23:02

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-tools-overview-V14
爬取时间: 2025-04-30 06:36:24
来源: Huawei Developer
该文档匹配DevEco Studio5.0.2 Release（5.0.7.210）版本。
概述
HUAWEI DevEco Studio（获取工具请单击链接下载，以下简称DevEco Studio）是基于IntelliJ IDEA Community开源版本打造，为运行在HarmonyOS系统上的应用和元服务（以下简称应用/元服务）提供一站式的开发平台。
作为一款开发工具，除了具有基本的代码开发、编译构建及调测等功能外，DevEco Studio还具有如下特点：
应用/元服务开发流程
使用DevEco Studio，只需要按照如下几步，即可轻松开发一个应用/元服务。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161811.62892157669582882328857541908651:50001231000000:2800:B49BEAA394DAD44E3B3DE91636299C0BCBB6B7E34B6F96AD5C92EEF140053526.png?needInitFileName=true?needInitFileName=true)
一、开发准备
获取HUAWEI DevEco Studio请单击链接下载，完成开发工具的安装。
DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。部分企业网络受限的情况下，需要配置代理信息。
二、开发应用/元服务
DevEco Studio集成了Phone、Tablet、2in1、Car等设备的典型场景模板，可以通过工程向导轻松的创建一个新的工程。
接下来还需要定义应用/元服务的UI、开发业务功能等编码工作，可以根据HarmonyOS应用开发概述来查看具体的开发过程，通过查看API接口文档查阅需要调用的API接口。
在开发代码的过程中，可以使用预览器查看应用/元服务效果，支持实时预览、动态预览、双向预览等功能，使编码的过程更高效。
三、运行、调试和测试应用/元服务
应用/元服务开发完成后，可以使用真机进行调试（需要申请调测证书进行签名），支持单步调试、跨语言调试等调试手段，使得应用/元服务调试更加高效。
HarmonyOS应用/元服务开发完成后，在发布到应用/元服务市场前，还需要对应用进行测试，主要包含Instrument Test、Local Test，确保HarmonyOS应用/元服务纯净、安全，给用户带来更好的使用体验。
四、发布应用/元服务
HarmonyOS应用/元服务开发、测试完成后，需要将应用/元服务发布至应用市场，以便应用市场对应用/元服务进行分发，普通消费者可以通过应用市场获取到对应的HarmonyOS应用/元服务。需要注意的是，发布到华为应用市场的HarmonyOS应用/元服务，必须使用应用市场颁发的发布证书进行签名。
文档声明
HUAWEI DevEco Studio使用指南配套DevEco Studio5.0.2 Release版本。如使用DevEco Studio其它版本，可能存在文档与产品功能界面、操作不一致的情况，请以实际功能界面为准。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-quick-start-V14
爬取时间: 2025-04-30 06:36:59
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-software-download-V14
爬取时间: 2025-04-30 06:37:34
来源: Huawei Developer
请前往下载中心，登录华为账号后下载DevEco Studio，并根据下载中心页面工具完整性指导进行完整性校验。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-software-install-V14
爬取时间: 2025-04-30 06:38:08
来源: Huawei Developer
DevEco Studio支持Windows和macOS系统，下面将针对两种操作系统的软件安装方式分别进行介绍。
Windows环境
运行环境要求
为保证DevEco Studio正常运行，建议电脑配置满足如下要求：
安装DevEco Studio
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.24168415982265803574331600242644:50001231000000:2800:876F6DF9B5ED7AA447977C302E0D2813F2937BE6ECDB1D205E2455DDC643F25B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.67038181701135982498706356425300:50001231000000:2800:A545FAB8227F4F6E75287DAEEA9EDB98B0C64BD38E797939C2A08C29B6D8D632.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.99309838389675078614094538021146:50001231000000:2800:A1544E62B8F829919A96D7ADDA97D5B2A55D64331D71D9F020786CAB5761277F.png?needInitFileName=true?needInitFileName=true)
macOS环境
运行环境要求
为保证DevEco Studio正常运行，建议电脑配置满足如下要求：
安装DevEco Studio
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.97614668326577816596405607250697:50001231000000:2800:7959B4671B9677D34C3E58E9D32E2C831ABFDDD698C004FE39A78011C5A2C50F.png?needInitFileName=true?needInitFileName=true)
诊断开发环境
为了您开发应用/元服务的良好体验，DevEco Studio提供了开发环境诊断的功能，帮助您识别开发环境是否完备。您可以在欢迎页面单击Diagnose进行诊断。如果您已经打开了工程开发界面，也可以在菜单栏单击Help > Diagnostic Tools > Diagnose Development Environment进行诊断。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.11728039059024973675935737305323:50001231000000:2800:74A1BFBB285690115EDEFCCA19633D9E37485BA0047AFDA3CF94F5548A93462B.png?needInitFileName=true?needInitFileName=true)
DevEco Studio开发环境诊断项包括电脑的配置、网络的连通情况、依赖的工具是否安装等。如果检测结果为未通过，请根据检查项的描述和修复建议进行处理。
启用中文化插件
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.12462555784555664258922177300133:50001231000000:2800:1907EACE8A13D3580D69E32BC02D1A8F02F21DF3008AFC4977E6224BAB85DBF8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.47810490519470014306920434875467:50001231000000:2800:7D7AD422D20318F57418339DB58F2EEFA03D20B22786A9F9471EB3DBE8211A7C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hello-world-V14
爬取时间: 2025-04-30 06:38:43
来源: Huawei Developer
DevEco Studio安装完成后，可以通过运行Hello World工程来验证环境设置是否正确。接下来以创建一个支持Phone设备的工程为例进行介绍。
创建一个新工程
1.
2.  工程创建完成后，DevEco Studio会自动进行工程的同步。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.38964624316562542414314162184454:50001231000000:2800:2B6C97AF5967E2D1EFE85949C05AA4274895A3EF61BA8123E7A19C534DD54075.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.49535065152189871071589389316734:50001231000000:2800:7AF257EB48AB98C66E0375359CDCBC2150843DE78A2DC739E2BD6F2564A4E1A0.png?needInitFileName=true?needInitFileName=true)
运行Hello World
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.11575536872636360087640039189034:50001231000000:2800:CFFE5DEA0AC7E5255102BCFCB60A47F390ED1A45F9BECBE7F0934971E2B03D86.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.90627587862353681318919616577740:50001231000000:2800:1F1CCE393B430997B23CDDC6385959C540F0C4740242D863862AA005085D614F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.29844204052854422808324910287561:50001231000000:2800:D8884607FF5E3532CA8A453C79AF31B5B6A66A91962A3B161A3B8565EE1436B4.png?needInitFileName=true?needInitFileName=true)
至此，您已成功运行了第一个应用，接下来可以通过一个简单的DEMO工程示例，来详细了解应用的开发过程，具体请参见HarmonyOS应用开发快速入门。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-no-network-V14
爬取时间: 2025-04-30 06:39:18
来源: Huawei Developer
如果开发者所使用的电脑处于完全无网络的环境中，需要先在一台可访问网络的电脑上准备好以下文件，将这些文件拷贝到无网络电脑中。
安装hypium
工程模板的工程级oh-package.json5文件中默认配置了hypium依赖，因此需要安装hypium，如果配置了其他依赖，也可参考以下步骤安装。
先配置环境变量，再打开命令行工具，执行 ohpm install 命令，会生成oh_modules文件夹和oh-package-lock.json5文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150611.87518594666653775024851016769996:50001231000000:2800:BF9D469598E81CF9EB2808B4937E06C894A82F4EB70E36CA934DFC6401C7F8FB.png?needInitFileName=true?needInitFileName=true)
将oh_modules文件夹和oh-package-lock.json5文件拷贝到无网络电脑的工程根目录下。
有网环境和无网环境下使用的ohpm版本需保持一致，否则可能导致oh-package-lock.json5文件不生效。
安装三方库
-  打开命令行工具，执行 ohpm install 命令，会生成oh_modules文件夹和oh-package-lock.json5文件。 将oh_modules文件夹和oh-package-lock.json5文件拷贝到无网络电脑的工程根目录下。 使用方法二时，需要确保可访问网络的电脑与无网络电脑中ohpm版本是一致的，以避免因oh-package-lock.json5文件版本不匹配而导致oh-package-lock.json5文件失效的问题。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.37116624532180526769785135998511:50001231000000:2800:BE52A0F3D309185F0E0BC6E410BF3296CD8B1A028EF7BA7314CEC328D5D08CD5.png?needInitFileName=true?needInitFileName=true)
无网络流水线搭建
如果开发者使用的电脑处于完全无网络的环境中，可参考本文搭建流水线环境，关于应用的构建、运行等请参考搭建流水线。
安装pnpm插件
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.36173497800794096595747326458434:50001231000000:2800:74C9F9A9D0327E25A92185FC4699AB13BDBD0D26BC71E8E8EB5855867265AC1E.png?needInitFileName=true?needInitFileName=true)
安装npm依赖插件
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.12333279357228847546690534210674:50001231000000:2800:D1BE482591DEF8B5CDF2885BB2ED43740026539495B5A93D9A505EB6A61B88EA.png?needInitFileName=true?needInitFileName=true)
安装ohpm依赖插件
请参考安装三方库。
安装libGL1库
在linux系统的构建场景下，使用纹理压缩功能需要安装libGL1库。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-project-V14
爬取时间: 2025-04-30 06:39:52
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-project-overview-V14
爬取时间: 2025-04-30 06:40:27
来源: Huawei Developer
APP包结构
在进行应用/元服务开发前，开发者应该掌握应用/元服务的逻辑结构。
应用/元服务发布形态为APP Pack（Application Package），它是由一个或多个HAP（Harmony Ability Package）包以及描述APP Pack属性的pack.info文件组成。
一个HAP在工程目录中对应一个Module，它是由代码、资源、三方库及应用/元服务配置文件组成，HAP可以分为Entry和Feature两种类型。
-  Entry：应用的主模块，作为应用的入口，提供了应用的基础功能。
-  Feature：应用的动态特性模块，作为应用能力的扩展，可以根据用户的需求和设备类型进行选择性安装。
基于Stage模型和FA模型开发的应用，应用程序包结构并不相同。
Stage模型应用程序包结构如下图所示。更多说明请参见应用开发基础知识中的Stage模型应用程序包结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.95474248011845310201050568790781:50001231000000:2800:A7D12862BF3BAE86A6FF1B9E77186058862D715159DDB4065B00C8AAA3CA5F4F.png?needInitFileName=true?needInitFileName=true)
FA模型应用程序包结构如下图所示。更多说明请参见应用开发基础知识中的FA模型应用程序包结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.63251096061109552493320573229504:50001231000000:2800:C3EED786807A4E7DF0C1E0B38BF5534093EB2FE1613047C0B521F77506D27A07.png?needInitFileName=true?needInitFileName=true)
切换工程视图
DevEco Studio工程目录结构提供工程视图和Ohos视图。工程视图（Project）展示工程中实际的文件结构，Ohos视图会隐藏一些编码中不常用到的文件，并将常用到的文件进行重组展示，方便开发者查询或定位所需编辑的模块或文件。
工程创建或打开后，默认显示工程视图，如果要切换到Ohos视图，在左上角单击Project>Ohos进行切换。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.51915262697921087749156885488023:50001231000000:2800:97BD28A622C5848952EC848FF2CCD0CDE55AD203A51443E8C19D8AD4DE2E00FA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-project-structure-V14
爬取时间: 2025-04-30 06:41:01
来源: Huawei Developer
ArkTS工程目录结构（Stage模型）
ArkTS Stage模型支持API Version 10及以上版本，其工程目录结构如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.80280155696827713743311652149681:50001231000000:2800:9FC9BB6AA8F52D2306756CECAF54E77EC6D7DFDC487A01D6188047E6AB5E903A.png?needInitFileName=true?needInitFileName=true)
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
| 资源目录  | 资源文件说明  |
| --- | --- |
| base>element  | 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： boolean.json：布尔型color.json：颜色float.json：浮点型intarray.json：整型数组integer.json：整型pattern.json：样式plural.json：复数形式strarray.json：字符串数组string.json：字符串值  |
| base>media  | 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。  |
| rawfile  | 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。  |
C++工程目录结构（Stage模型）
C++ Stage模型支持API Version 10以上版本，支持使用ArkTS+C++进行开发，其工程目录结构如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.07764977920562522257502253429840:50001231000000:2800:63891CC512DB2FCBEF6A5EDDE3F981712538BA92D8C45ECA96511A9747270F4A.png?needInitFileName=true?needInitFileName=true)
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
| 资源目录  | 资源文件说明  |
| --- | --- |
| base>element  | 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： boolean.json：布尔型color.json：颜色float.json：浮点型intarray.json：整型数组integer.json：整型pattern.json：样式plural.json：复数形式strarray.json：字符串数组string.json：字符串值。  |
| base>media  | 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。  |
| rawfile  | 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。  |
JS工程目录结构（FA模型）
JS工程只支持FA模型，其工程目录结构如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.92558539282237765900900919332236:50001231000000:2800:E02ECA0DC9F2B2C32B3C680DC45F9101D24F415B489164AAAB7DE98BFE887DF3.png?needInitFileName=true?needInitFileName=true)
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
-  资源目录 资源文件说明 base>element 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： base>media 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。 rawfile 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。
| 资源目录  | 资源文件说明  |
| --- | --- |
| base>element  | 包括字符串、整型数、颜色、样式等资源的json文件。每个资源均由json格式进行定义，例如： boolean.json：布尔型color.json：颜色float.json：浮点型intarray.json：整型数组integer.json：整型pattern.json：样式plural.json：复数形式strarray.json：字符串数组string.json：字符串值  |
| base>media  | 多媒体文件，如图形、视频、音频等文件，支持的文件格式包括：.png、.gif、.mp3、.mp4等。  |
| rawfile  | 用于存储任意格式的原始资源文件。rawfile不会根据设备的状态去匹配不同的资源，需要指定文件路径和文件名进行引用。  |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-template-V14
爬取时间: 2025-04-30 06:41:35
来源: Huawei Developer
DevEco Studio支持多种品类的应用/元服务开发，预置丰富的工程模板，可以根据工程向导轻松创建适应于各类设备的工程，并自动生成对应的代码和资源模板。同时，DevEco Studio还提供了多种编程语言供开发者进行应用/元服务开发，包括ArkTS、JS和C/C++。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.05125475584949852294192511705080:50001231000000:2800:021A95B403C4FD7BB4D046B0BE135DF18D6EE3D4D8B35A0CC1B5B49685914A43.png?needInitFileName=true?needInitFileName=true)
工程模板支持的开发语言及模板说明如下表所示：
| 模板名称  | 说明  |
| --- | --- |
| Empty Ability   | 用于Phone、Tablet、2in1、Car设备的模板，展示基础的Hello World功能。  |
| Native C++  | 用于Phone、Tablet、2in1、Car设备的模板，作为应用调用C++代码的示例工程，界面显示“Hello World”。  |
| [CloudDev]Empty Ability  | 端云一体化开发通用模板。更多信息请参见端云一体化开发。  |
| [Lite]Empty Ability  | 用于Lite Wearable设备的模板，展示了基础的Hello World功能。可基于此模板，修改设备类型及RuntimeOS，进行小型嵌入式设备开发。  |
| Flexible Layout Ability  | 用于创建跨设备应用开发的三层工程结构模板。三层工程结构包含common（公共能力层）、features（基础特性层）、products（产品定制层）。  |
| Embeddable Ability  | 用于开发支持被其他应用嵌入式运行的元服务的工程模板。  |
模板名称
说明
Empty Ability
用于Phone、Tablet、2in1、Car设备的模板，展示基础的Hello World功能。
Native C++
用于Phone、Tablet、2in1、Car设备的模板，作为应用调用C++代码的示例工程，界面显示“Hello World”。
[CloudDev]Empty Ability
端云一体化开发通用模板。更多信息请参见端云一体化开发。
[Lite]Empty Ability
用于Lite Wearable设备的模板，展示了基础的Hello World功能。可基于此模板，修改设备类型及RuntimeOS，进行小型嵌入式设备开发。
Flexible Layout Ability
用于创建跨设备应用开发的三层工程结构模板。三层工程结构包含common（公共能力层）、features（基础特性层）、products（产品定制层）。
Embeddable Ability
用于开发支持被其他应用嵌入式运行的元服务的工程模板。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-create-new-project-V14
爬取时间: 2025-04-30 06:42:10
来源: Huawei Developer
当您开始开发一个应用/元服务时，首先需要根据工程创建向导，创建一个新的工程，工具会自动生成对应的代码和资源模板。
在运行DevEco Studio工程时，建议每一个运行窗口有2GB以上的可用内存空间。
创建和配置新工程
DevEco Studio提供了基础的工程模板资源，不同模板支持的设备类型、API Version可能不同，在创建新工程前，请提前了解各模板的相关信息，具体请参考工程模板介绍。
创建HarmonyOS工程
1.
2.
3.  应用包名要求：
4.  应用包名要求：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.55149727100582368910755550142979:50001231000000:2800:31636D2BC29322CBB9CD7EA0469F7BE3B24512494F9C25362B6E3A1257173A23.png?needInitFileName=true?needInitFileName=true)
-  应用包名要求：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150612.34062754476338546950526530960977:50001231000000:2800:DE85E62A7A4F3392F06A8D8DBE7F3EFE73145D01D95B4C53B145730BFE78768A.png?needInitFileName=true?needInitFileName=true)
创建OpenHarmony工程
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150613.60726551773205805728787734589706:50001231000000:2800:73DB4ADF3BCA0B31A94DB985D15931A2708A5C9AA28264D1B2DF27B641D0262A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150613.91579647384306496045299324967547:50001231000000:2800:B4C27142AF4B901417AD2910BEB0E0E1FE2B3AA571EF19620AD44C2A6A5831DD.png?needInitFileName=true?needInitFileName=true)
若选择Native C++模板创建OpenHarmony应用，且应用需要在RK开发板上运行，则需在对应Native模块的build-profile.json5文件buildOption/externalNativeOptions字段下，新增abiFilters字段并赋值为"armeabi-v7a"。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-project-migration-V14
爬取时间: 2025-04-30 06:42:45
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-integrated-project-migration-V14
爬取时间: 2025-04-30 06:43:19
来源: Huawei Developer
DevEco Studio从 NEXT Developer Beta1版本开始，提供开箱即用的开发体验，将SDK、Node.js、Hvigor、OHPM等工具链进行合一打包，简化DevEco Studio安装配置流程；并提供一体化的历史工程迁移能力，帮助开发者快速完成工程转换。
为了避免数据丢失，迁移前请对工程进行备份。
本次一体化变更点如下：
| 变更点  | 详细说明  |
| --- | --- |
| 删除compileSdkVersion字段  | 删除工程级build-profile.json5中的compileSdkVersion配置。编译所用的SDK版本即为配套的SDK版本。 说明由于targetSdkVersion未配置时值默认与compileSdkVersion的值一致，如果之前未配置targetSdkVersion，targetSdkVersion的值将与配套的SDK版本保持一致；如果之前配置过targetSdkVersion，targetSdkVersion的值不变。若工程为Openharmony工程，则无需执行此步骤。   |
| 删除部分hvigor文件 & 删除冗余hvigor配置  | 删除hvigor-wrapper.json。删除hvigorw、hvigorw.bat。删除hvigor-config.json5中的hvigorVersion字段，并删除dependencies中@ohos/hvigor-ohos-plugin及rollup字段。  |
| 删除HarmonyOS SDK配置  | 删除local.properties中的HarmonyOS SDK配置。若工程为Openharmony工程，则忽略此步骤。  |
| 增加开发态配置  | 在hvigor-config.json5中增加开发态配置版本号modelVersion。在工程级的oh-package.json5中增加开发态配置版本号modelVersion。  |
变更点
详细说明
删除compileSdkVersion字段
删除工程级build-profile.json5中的compileSdkVersion配置。编译所用的SDK版本即为配套的SDK版本。
删除部分hvigor文件 & 删除冗余hvigor配置
删除HarmonyOS SDK配置
删除local.properties中的HarmonyOS SDK配置。若工程为Openharmony工程，则忽略此步骤。
增加开发态配置
自动迁移
1.  可以通过菜单栏Tools > Migrate Assistant，进入迁移助手页面。
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143407.30688682356006771683192013217948:50001231000000:2800:547E61B173B75DFFB1B8E298E73AB0E18C883771C3A3D5062C2F69EB4589D9B8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143407.69815691969764688369212179359488:50001231000000:2800:8CD18B29B72800E497057FCCB9CDCDF2222AA55829AF97FF9661978091E0ABB7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143407.11130032202917904961496271740045:50001231000000:2800:9592E3579D037FE1F18A5AFCF212F9D596A417774A64086E560648BE5967B8BB.png?needInitFileName=true?needInitFileName=true)
若您的工程是NPM管理的API 8/9工程，请先按照适配OHPM包管理完成升级，再通过菜单栏Tools > Migrate Assistant，进入迁移助手页面，完成一体化工程自动迁移。
手动迁移
API 10及以上历史工程迁移
如自动化迁移不成功或希望进行手动迁移，迁移前同样需对工程进行备份。手动迁移流程如下：
1.
2.
3.
4.
5.
6.
7.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143407.67695938218804950590267250605707:50001231000000:2800:DB5E941C32BECC99E465EF46C91D1F8813ECDF097D7E890998A0A2C53D13276B.png?needInitFileName=true?needInitFileName=true)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143407.87096588171761720376245408554407:50001231000000:2800:FCCA8F0FA945C83B09236EC663CB9E68F86120B27ACCDB82A45D816DFA5D0797.png?needInitFileName=true?needInitFileName=true)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.47038891917970305622868183506714:50001231000000:2800:BC0C1F39C5C6C95D58FE720F86DF6A93BC2BE256FE4E720077E2832C25662489.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.57722778873388433287109947798804:50001231000000:2800:5B54108C6917A310FEF423FCDF377BA0D86A35D86181CAEB820973FF0BEAE3C2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.49299744773188517395583149065749:50001231000000:2800:EC9B475E86C32B30285F052967074269DC62C476F813EB1646386CC7B781C150.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.63087511243184683875347960999855:50001231000000:2800:DD1A338CEB341EC270D2633ACCF307AC55D878554B0FE656A75AB839B8C27E8C.png?needInitFileName=true?needInitFileName=true)
API 9历史工程迁移
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.93010934759054479527505811206828:50001231000000:2800:4D9DEC3DE5283B8625DC9E8842669236BAD76AF55537BA99CF656B9B28CA96FC.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.43422940502137624651091822776576:50001231000000:2800:274BA7501015ABE923D95444C6ECC249BD7859122D13683A4E78A7E67C04D9FB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.39313455890455391081158930273559:50001231000000:2800:FBC30D2449AE307AA483DDED450378C4F81725BD776DEBA10DFF106B66751145.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.93927138702848096651669711216863:50001231000000:2800:E84F1B9BDB7112F0B65E484122A769ED37B659FA9CA677C3D2CF9D8BE898D25E.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-historical-project-migration-V14
爬取时间: 2025-04-30 06:43:55
来源: Huawei Developer
OHPM CLI（OpenHarmony Package Manager Command-line Interface） 作为鸿蒙生态三方库的包管理工具，支持共享包的发布、安装和依赖管理。
在DevEco Studio 3.1 Release及更高版本上新建API 9及以上版本的工程将使用ohpm作为默认包管理器。
仅使用npm包管理的API 8/9历史工程需进行迁移。
整体迁移流程如下：
1.  将工程和模块下npm包管理相关配置文件package.json或.npmrc，迁移为oh-package.json5或.ohpmrc文件。具体操作请参阅迁移步骤二。 若原工程中无.npmrc文件，则无需迁移为.ohpmrc文件。
2.  在工程中新增hvigor相关的wrapper文件，包括hvigorw、hvigorw.bat、hvigor-config.json5、hvigor-wrapper.js配置文件。具体操作请参阅迁移步骤三。
3.  包含package.json、package-lock.json、.npmrc、node_modules，工程和模块级别下均需进行删除处理。具体操作请参阅迁移步骤四。
|   |   |
| --- | --- |
| 迁移前文件目录  | 迁移后文件目录  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150614.12133822311207534780045851507961:50001231000000:2800:9BF2B49CADC069788F095ABDEFC4E45645DF09861F2C3B1D4FEE915772B58701.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150614.12323610125415894051315383574038:50001231000000:2800:BB9D0EC98D670FC3CD27536FBA569933817C8573B27D70E9E4A00CD97C55F03F.png?needInitFileName=true?needInitFileName=true)
迁移前文件目录
迁移后文件目录
历史工程手动迁移
迁移前需对工程进行备份。
具体迁移流程如下：
1.  若历史工程为C++工程，src>main>cpp目录下包含package.json或.npmrc，需做相同处理。
2.  oh-package.json5包含字段 字段说明 迁移/新增字段 原package.json字段 说明 name 软件包名称 迁移字段 name 必选字段，若package.json文件中未指明，需在oh-package.json5添加补齐 version 软件包版本 迁移字段 version 必选字段，若package.json文件中未指明，需在oh-package.json5添加补齐 description 软件包简介 迁移字段 description 必选字段，若package.json文件中未指明，需在oh-package.json5添加补齐 keywords 软件包关键字 迁移字段 keywords - homepage 主页链接 迁移字段 homepage - license 开源协议 迁移字段 license - author 软件包作者 迁移字段 author - main 软件包入口 迁移字段 main - repository 仓库地址 迁移字段 repository - dependencies 生产依赖 迁移字段 dependencies 该字段处理方式请参阅下方说明内容 devDependencies 开发依赖 迁移字段 devDependencies - types 类型定义 迁移字段 types - artifactType 共享包类型 新增字段，非必选配置项 - 可选项： .npmrc字段 字段释义 .ohpmrc对应字段 registry 仓库地址 registry @${scope}:registry 指定仓库 @${group}:registry cache 缓存路径 cache noproxy 不使用proxy代理 no_proxy proxy http代理 http_proxy https-proxy https代理 https_proxy strict-ssl ssl校验 strict_ssl cafile ca证书路径 ca_files loglevel 日志级别 log_level
3.
4.
5.
| oh-package.json5包含字段  | 字段说明  | 迁移/新增字段  | 原package.json字段  | 说明  |
| --- | --- | --- | --- | --- |
| name  | 软件包名称  | 迁移字段  | name  | 必选字段，若package.json文件中未指明，需在oh-package.json5添加补齐  |
| version  | 软件包版本  | 迁移字段  | version  | 必选字段，若package.json文件中未指明，需在oh-package.json5添加补齐  |
| description  | 软件包简介  | 迁移字段  | description  | 必选字段，若package.json文件中未指明，需在oh-package.json5添加补齐  |
| keywords  | 软件包关键字  | 迁移字段  | keywords  | -  |
| homepage  | 主页链接  | 迁移字段  | homepage  | -  |
| license  | 开源协议  | 迁移字段  | license  | -  |
| author  | 软件包作者  | 迁移字段  | author  | -  |
| main  | 软件包入口  | 迁移字段  | main  | -  |
| repository  | 仓库地址  | 迁移字段  | repository  | -  |
| dependencies  | 生产依赖  | 迁移字段  | dependencies  | 该字段处理方式请参阅下方说明内容  |
| devDependencies  | 开发依赖  | 迁移字段  | devDependencies  | -  |
| types  | 类型定义  | 迁移字段  | types  | -  |
| artifactType  | 共享包类型  | 新增字段，非必选配置项  | -  | 可选项： original：源码，即发布源码(.ts/.ets)。obfuscation：混淆代码，即源码经过混淆之后发布上传。  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150614.87003976995615219937281640205914:50001231000000:2800:615DE8734C281D2A3A5F10DD6FA8DD5D56F26C789CC584CB5FDF3EEEA20B6F03.png?needInitFileName=true?needInitFileName=true)
| .npmrc字段  | 字段释义  | .ohpmrc对应字段  |
| --- | --- | --- |
| registry  | 仓库地址  | registry  |
| @${scope}:registry  | 指定仓库  | @${group}:registry  |
| cache  | 缓存路径  | cache  |
| noproxy  | 不使用proxy代理  | no_proxy  |
| proxy  | http代理  | http_proxy  |
| https-proxy  | https代理  | https_proxy  |
| strict-ssl  | ssl校验  | strict_ssl  |
| cafile  | ca证书路径  | ca_files  |
| loglevel  | 日志级别  | log_level  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150614.06575456123140449556995253214585:50001231000000:2800:A9E0D02832F5E54E53A2935B1CD322439F6DAC2C83E90BFCA068C40BAAA683B7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150614.29037920073879831598575044138732:50001231000000:2800:56CC3D1698BC5C60EB11550B72F8F2A3D36D191FADC5DAB3F9B1A9BBDD52779E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150614.15158587575695369858158986464619:50001231000000:2800:EEC9B1D620A4C345DB84303C4CE0768389B62B1EE5F32024D2A854F74ABC7256.png?needInitFileName=true?needInitFileName=true)
若同步时报错提示“Install failed FetchPackageInfo：hypium failed”，请参见对应解决方案。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-module-management-V14
爬取时间: 2025-04-30 06:44:29
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-add-new-module-V14
爬取时间: 2025-04-30 06:45:03
来源: Huawei Developer
Module是应用/元服务的基本功能单元，包含了源代码、资源文件、第三方库及应用/元服务配置文件，每一个Module都可以独立进行编译和运行。一个应用/元服务通常会包含一个或多个Module，因此，可以在工程中创建多个Module，每个Module分为Ability和Library两种类型。Module支持entry、feature、har、shared四种类型，具体请参考module.json5配置文件。
在工程中添加Module
创建新的Module
1.  当前暂不支持在AppScope、hvigor、oh_modules、build、点开头的目录（如：.hvigor、.idea）下通过单击鼠标右键创建module。
2.  当前暂不支持在AppScope、hvigor、oh_modules、build、点开头的目录（如：.hvigor、.idea）下通过单击鼠标右键创建module。
3.
4.
5.
-  当前暂不支持在AppScope、hvigor、oh_modules、build、点开头的目录（如：.hvigor、.idea）下通过单击鼠标右键创建module。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250124180251.92317964142449137798310479513910:50001231000000:2800:123470B689EDBF0E5891B41D974214260592E8249B87287A6A140FC3F25276B3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250124180251.37810333766916371937737262052507:50001231000000:2800:DCA7A96C13F9EAEA6F9FAAACAA57DB75F6EC17CA15DE365DE52B525ABE7D03D6.png?needInitFileName=true?needInitFileName=true)
导入Module
HarmonyOS工程支持导入其它HarmonyOS模块的功能。当前仅支持FA模型的模块导入到FA模型，Stage模型的模块导入到Stage模型。不支持FA模型的模块导入到Stage模型，或Stage模型的模块导入到FA模型。
DevEco Studio支持引用当前工程目录之外，即其他工程下的Module。除Import Module方式导入模块外，可通过在build-profile.json5文件中srcPath字段下配置工程外Module的相对路径导入。通过srcPath方式导入工程，仅引用Module相关信息，不会将Module代码完全复制至本地。
1.
2.  在指定路径下，选择导入的模块，单击OK。导入的模块可以为文件夹，也可以为zip格式。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250124180252.08804579474770196355119130086092:50001231000000:2800:DC42B294E50CB590DCE0711934B7A7DCBBF3D948EAEBE25B906A1105FBC65E2A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250124180252.66876604023899495594711880104420:50001231000000:2800:7A4BED46CBE7CE7180AAE8D17B35FE1CBFF79E92FB48BFD4DCB49789A8468A91.png?needInitFileName=true?needInitFileName=true)
配置distroFilter/distributionFilter分发规则
同一类型的设备（Phone、Wearable、Lite Wearable等）可能在系统API版本（apiVersion）、屏幕形状（screenShape）、窗口分辨率（screenWindow）上存在差异。针对这些差异，开发者需要针对同一类型设备的不同型号进行适配开发，然后在应用市场实现精准的分发，以便不同设备的用户能获得更好的使用体验。为了实现应用市场的精准分发，需要在一个工程中，针对同一类型设备添加多个Entry模块来适配不同型号的设备，然后再配置不同的分发规则。具体规则如下：
screenWindow标签的policy取值只能为include。
Stage模型配置分发规则
1.
2.
FA模型分发规则配置
在同一个工程中，如果同一个设备存在多个Entry模块，需要在每一个Entry模块的config.json文件中，配置distroFilter分发规则。FA模型配置字段请参见distroFilter对象的内部结构。
删除Module
在工程目录中选中要删除的模块，单击鼠标右键，选中Delete，并在弹出的对话框中单击Delete。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-add-new-ability-V14
爬取时间: 2025-04-30 06:45:38
来源: Huawei Developer
Ability是应用/元服务所具备的能力的抽象，一个Module可以包含一个或多个Ability。应用/元服务先后提供了两种应用模型：
-  Stage模型包含两种Ability组件类型：
Stage模型添加UIAbility
在模块中添加UIAbility
选中对应的模块，单击鼠标右键，选择New > Ability。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.84775517812642044588680556259838:50001231000000:2800:D528AB5C229C3F4B04D3B5B23A37EAA85FE652ADFC8F600B446E23B06A4DE745.png?needInitFileName=true?needInitFileName=true)
在模块中添加Extension Ability
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.05362980624597770622073649334894:50001231000000:2800:58C4933E51B52E4EAAC4FB9697FF586F6FBF635EB640E9DD75F180C538E26489.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.75698201109874981943631721885271:50001231000000:2800:C54EDF5077BFEBA2E219DA5996C85503A5FBB9250414EF9E8B790D8D11C535F5.png?needInitFileName=true?needInitFileName=true)
FA模型添加Ability
ArkTS工程与JS工程在FA模型中添加Ability的操作方式一致，本节内容以ArkTS工程为例介绍在模块中添加Ability。
创建Particle Ability
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.51844000163195736839011540433694:50001231000000:2800:A5C8AF72C46CF786C7FAD47C73EB2EB7427077B0ED15E63C36A657F0ADC409FB.png?needInitFileName=true?needInitFileName=true)
创建Feature Ability
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.75466193131595596865493440735791:50001231000000:2800:90DBAA37141C78A82B9A6BCA4647468947A315717C17CFDF102E757EAC7DE808.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-service-widget-V14
爬取时间: 2025-04-30 06:46:12
来源: Huawei Developer
概述
服务卡片可将元服务/应用的重要信息以卡片的形式展示在桌面，用户可通过快捷手势使用卡片，通过轻量交互行为实现服务直达、减少层级跳转的目的。
不同的SDK版本提供的卡片模板不同：
-  模板名称 支持的设备 支持的开发语言 模板描述 Hello World Phone、Tablet、2in1 ArkTS、JS HelloWorld卡片，用于高效直观地构建UI。当前Hello World卡片模板支持使用6*4尺寸。 Image With Information（图文卡片模板） Phone、Tablet、2in1 ArkTS、JS 图文卡片模板主要在于展现图片和一定数量文本的搭配，在这种布局下，图片和文本属于同等重要的信息。在不同尺寸下，图片大小和文本数量会发生一定变化，用于凸显关键信息。 Immersive Information（沉浸图文卡片模板） Phone、Tablet、2in1 ArkTS、JS 沉浸式卡片的装饰性较强，能够较好的提升卡片品质感并起到装饰桌面的作用，合理的去布局信息与背景图片之间的空间比例，可以提升用户的个性化使用体验。 List Phone、Tablet、2in1 ArkTS 提供基本的列表功能。当前仅动态卡片支持在API 11及以上工程创建List卡片模板。 Control Button Phone、Tablet、2in1 ArkTS 操控类型的卡片，展示文本信息与按钮操作，点击按钮响应事件。当前仅静态卡片支持API 11及以上工程创建Control Button卡片模板。 Control Search Phone、Tablet、2in1 ArkTS 操控类型的卡片，适用于搜索场景。当前仅静态卡片支持API 11及以上工程创建Control Search卡片模板。
| 模板名称  | 支持的设备  | 支持的开发语言  | 模板描述  |
| --- | --- | --- | --- |
| Hello World  | Phone、Tablet、2in1  | ArkTS、JS  | HelloWorld卡片，用于高效直观地构建UI。当前Hello World卡片模板支持使用6*4尺寸。  |
| Image With Information（图文卡片模板）  | Phone、Tablet、2in1  | ArkTS、JS  | 图文卡片模板主要在于展现图片和一定数量文本的搭配，在这种布局下，图片和文本属于同等重要的信息。在不同尺寸下，图片大小和文本数量会发生一定变化，用于凸显关键信息。  |
| Immersive Information（沉浸图文卡片模板）  | Phone、Tablet、2in1  | ArkTS、JS  | 沉浸式卡片的装饰性较强，能够较好的提升卡片品质感并起到装饰桌面的作用，合理的去布局信息与背景图片之间的空间比例，可以提升用户的个性化使用体验。  |
| List  | Phone、Tablet、2in1  | ArkTS  | 提供基本的列表功能。当前仅动态卡片支持在API 11及以上工程创建List卡片模板。  |
| Control Button  | Phone、Tablet、2in1  | ArkTS  | 操控类型的卡片，展示文本信息与按钮操作，点击按钮响应事件。当前仅静态卡片支持API 11及以上工程创建Control Button卡片模板。  |
| Control Search  | Phone、Tablet、2in1  | ArkTS  | 操控类型的卡片，适用于搜索场景。当前仅静态卡片支持API 11及以上工程创建Control Search卡片模板。  |
使用约束
创建服务卡片
创建一个工程后，可以通过如下方法进行创建服务卡片：
1.
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.00321712416362134304754937944110:50001231000000:2800:6D45D7E7412F9A840130AB8EEAEC423BCB47034A6767BF6B5EEBF572CA20AAA2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.12058858881968834722994112507488:50001231000000:2800:B92440D3AF30C744522FEBC9EDCF2CA9CA8759D43475E0FD83C7725A8E7F26CA.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.97515149449007614412347796760180:50001231000000:2800:6CBEB217C9931968B515B3502FFCC8C85CA42CA60D6CD321F4441812A409B2B2.png?needInitFileName=true?needInitFileName=true)
创建动态/静态卡片
DevEco Studio支持创建静态/动态卡片。动态卡片支持自定义交互、动效、滑动等功能，功能丰富但内存占用较大；静态卡片内存占用较小，有助实现整机内存优化，可实现静态信息展示、刷新和点击跳转。
当前仅API 10及以上Stage模型支持开发静态卡片。
创建服务卡片后，在form_config.json文件中，可修改isDynamic参数配置。isDynamic置空或为"true"，则该卡片为动态卡片；若赋值为"false"，则该卡片为静态卡片。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.56860276214719070037737308943478:50001231000000:2800:35B344F99917F173BFC51ADBD76C459F8FBB0CD2E0755EC4A132DFE8F56FEAC9.png?needInitFileName=true?needInitFileName=true)
预览服务卡片
在开发服务卡片过程中，支持对卡片进行实时预览。服务卡片通过ArkTS、JS文件进行布局设计，在开发过程中，可以对布局文件进行实时预览，只要在布局文件中保存了修改的源代码，在预览器中就可以实时查看布局效果。在Phone和Tablet服务卡片的预览效果中，每个尺寸的服务卡片提供3种场景的预览效果，分别为极窄（Minimum）、默认（Default）、极宽(Maximum)，开发者应确保三种尺寸的显示效果均正常，以便适应不同屏幕尺寸的设备。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150615.75910730079301956634641524775272:50001231000000:2800:CEC62049BDD24626FFBB8373DA3FE4A747E292B118268A147BF3EF3060823550.png?needInitFileName=true?needInitFileName=true)
关于预览器的使用详细说明请参考界面预览。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-add-page-V14
爬取时间: 2025-04-30 06:46:46
来源: Huawei Developer
在ArkTS语言的工程中，支持添加Page。Page是表示应用/元服务的一个页面。应用/元服务可以设计为多个功能页面，每个页面进行单独的文件管理，并通过路由API实现页面的调度管理，以实现应用内功能的解耦。ArkTS语言的工程添加Page后，会在pages文件夹下生成一个新的ets文件。
1.  API 10工程中仅支持创建Page，展示基础的Hello World功能；如需使用场景化Page模板，请将工程切换为API 11及以上后进行开发。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.20401570996704182976110108199286:50001231000000:2800:53F71B23053B291200EFCA4A39F82CF47B57BA4FBBC82C9A8901961A91E31A8E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.38027059291925240380473309835989:50001231000000:2800:5434AC555042EBE86BDC005072222D5BB43B7C7A121C4FC192242B70C10C336D.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-import-sample-V14
爬取时间: 2025-04-30 06:47:20
来源: Huawei Developer
DevEco Studio支持Sample工程的导入功能，通过对接Gitee开源社区中的Sample资源，可一键导入Sample工程到DevEco Studio中。
下面介绍导入Sample的方法。
1.  在打开工程的情况下，可以单击File > Settings进入设置界面。
2.
3.
4.  在打开工程的情况下，可以单击File > New > Import > Import Sample来进行导入。
5.
6.  如果网络受限，导入时会提示“Failed to connect to gitee.com port 443: Time out”连接超时错误，请配置Git代理信息。
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.52436900257693478478467898662352:50001231000000:2800:C3C60867B290ADFC1E20C83D2B6EF7C30BB93556BDDDDD4E1C1BBE44E48314C7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.26762783190426582264152555972543:50001231000000:2800:F72B193E6C48CB8A0C76E5957FC049A261DAFCB3CFE79C5F24172D57E70F8B45.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.00643749338025487438718810586949:50001231000000:2800:1C33D6AF1BF73E3ADE0BA6D77C9153E0FA4C366A412ABAA72157AE1EDA6698FD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.82261190283918017394748654864948:50001231000000:2800:04A8D6D9546E60FE1C4B1510BA69F944FFD48CFDAC1769C9D49A6A01EA490CF4.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-intent-V14
爬取时间: 2025-04-30 06:47:54
来源: Huawei Developer
DevEco Studio支持创建意图框架，帮助应用理解用户意图，并提供相应的服务和体验。
使用约束
使用方式
1.  PlayMusic和PlayMusicList不支持同时关闭，请至少选择开启一个意图。
2.  PlayMusic和PlayMusicList不支持同时关闭，请至少选择开启一个意图。
3.
-  PlayMusic和PlayMusicList不支持同时关闭，请至少选择开启一个意图。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.03637350887855280232965807357524:50001231000000:2800:3B731AD2B57CA5A7E4547B745A93869D126F1CAA68499287CBBBEBA315547DBF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.25795071100367045584936853170562:50001231000000:2800:82089A99D304E97F54EA904B5C2F1098F27CAE6B50B56AC24049EDA5AF11A2CE.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-code-edit-V14
爬取时间: 2025-04-30 06:48:29
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-editer-overview-V14
爬取时间: 2025-04-30 06:49:03
来源: Huawei Developer
DevEco Studio支持使用多种语言进行应用/元服务的开发，包括ArkTS、JS和C/C++。在编写应用/元服务阶段，可以通过掌握代码编写的各种常用技巧，来提升编码效率。
代码高亮
支持对代码关键字、运算符、字符串、类、标识符、注释等进行高亮显示，您可以打开File >Settings（macOS为DevEco Studio > Preferences）面板，在Editor > Color Scheme自定义各字段的高亮显示颜色。默认情况下，您可以在Language Defaults中设置源代码中的各种高亮显示方案，该设置将对所有语言生效；如果您需要针对具体语言的源码高亮显示方案进行定制，可以在左侧边栏选择对应的语言，然后取消“Inherit values from”选项后设置对应的颜色即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.19616362008697411251757334221098:50001231000000:2800:6257EA79214B45FE7FF72C1D4DA4C288016A67B80B40F28BC16027C54C64D61E.png?needInitFileName=true?needInitFileName=true)
代码跳转
在编辑器中，可以按住Ctrl键（macOS为Command键），鼠标单击代码中引用的类、方法、参数、变量等名称，自动跳转到定义处。若单击定义处的类、变量等名称，当仅有一处引用时，可直接跳转到引用位置；若有多处引用，在弹窗中可以选择想要查看的引用位置。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.29393750180285601516672987728279:50001231000000:2800:A83712C9DE9A2DCF83F11F0DCC857C98B01C11126CFBAA5C5BB856AA44AB8AC6.gif?needInitFileName=true?needInitFileName=true)
跨语言跳转
DevEco Studio支持在声明或引用了Native接口的文件中（如d.ts）跨语言跳转其对应的C/C++函数，从而提升混合语言开发时的开发效率。您可以选中接口名称单击右键，在弹出的菜单中选择Go To > Implementation(s)（或使用快捷键Ctrl+Alt+B，macOS为Command+Option+B）实现跨语言跳转。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150616.93849886345769892436621341665137:50001231000000:2800:FD5F8460EC46C9A7A1F33BB2A9FA60B93E42C01A4883534B5CF450A78D640E27.png?needInitFileName=true?needInitFileName=true)
代码格式化
代码格式化功能可以帮助您快速的调整和规范代码格式，提升代码的美观度和可读性。默认情况下，DevEco Studio已预置了代码格式化的规范，您也可以个性化的设置各个文件的格式化规范，设置方式如下：在File > Settings > Editor > Code Style（macOS为DevEco Studio > Preferences >Editor>Code Style）下，选择需要定制的文件类型，如ArkTS，然后自定义格式化规范即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.63866424987089788440265408873279:50001231000000:2800:EAE7930F83F78E35388F28BFC27FA1C2C53248582207B9B691013E2A0EFD1E80.png?needInitFileName=true?needInitFileName=true)
在使用代码格式化功能时，您可以使用快捷键Ctrl + Alt + L（macOS为Option+Command +L） 可以快速对选定范围的代码进行格式化。
如果在进行格式化时，对于部分代码片段不需要进行自动的格式化处理，可以通过如下方式进行设置：
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.11289854719662225575597595950419:50001231000000:2800:4EA0CEF8EFD8FD33DC2B944895C424DFA4BE22EB132B3DCF2D0497CF0651090D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.03735845818915589501559818464619:50001231000000:2800:F998763361758D708F0DE4E321B174B0801B76F44C5DFF81C15F6EC02C74A1C7.png?needInitFileName=true?needInitFileName=true)
若工程已配置code-linter.json5文件，选中code-linter.json5文件右键选择Apply CodeLinter Style Rules，代码格式化规则将与已配置的code-linter.json5文件中相关规则保持一致。code-linter.json5文件配置请参考配置代码检查规则。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.70857392543392566150691178898249:50001231000000:2800:803EFBE1135413832B675D0B83BB8CAA1A00238627A2D9ADEDA0D577088A16F0.png?needInitFileName=true?needInitFileName=true)
代码折叠
支持对代码块的快速折叠和展开，既可以单击编辑器左侧边栏的折叠和展开按钮对代码块进行折叠和展开操作，还可以对选中的代码块单击鼠标右键选择折叠方式，包括折叠、递归折叠、全部折叠等操作。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.33303554193135809698608208875693:50001231000000:2800:F9A40072F960AE2B85A6672E2FDCD191B1F363803CF64AD48D3839CEA79F9D8C.gif?needInitFileName=true?needInitFileName=true)
代码快速注释
支持对选择的代码块进行快速注释，使用快捷键Ctrl+/（macOS为Command+/）进行快速注释。对于已注释的代码块，再次使用快捷键Ctrl+/（macOS为Command+/）取消注释。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.16643021123363803626247094051266:50001231000000:2800:42842B24B2AB4D1A12337C476B710817DE1681667C1640EE5AFA2EA69E9AB9A7.gif?needInitFileName=true?needInitFileName=true)
代码结构树
使用快捷键Alt + 7 / Ctrl + F12（macOS为Command+7）打开代码结构树，快速查看文件代码的结构树，包括全局变量和函数，类成员变量和方法等，并可以跳转到对应代码行。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.07689579776026428284439321972551:50001231000000:2800:C3CDE1B442C1224C0D20B1239C464E488FB1E0E183FD7ECB8B5F37E23A349CFA.png?needInitFileName=true?needInitFileName=true)
代码引用查找
提供Find Usages代码引用查找功能，帮助开发者快速查看某个对象(变量、函数或者类等)被引用的地方，用于后续的代码重构，可以极大的提升开发者的开发效率。
使用方法：在要查找的对象上，单击鼠标右键 > Find Usages或使用快捷键Alt +F7（macOS为Option +F7）。可点击图标查看变量赋值位置，点击图标查看变量引用情况。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.92681061977955313410623757569527:50001231000000:2800:5EBA5EBD1CDC81813F9173051C3A51E06FD9E371427F94B081331B1DB558585B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.99472435046719335463177132983610:50001231000000:2800:E8AC5B3E35C9F40E3AD72C28C7160F645EA54DECDE858171273A42A5A95E600A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.92648615907210964216244472070565:50001231000000:2800:99AE68E7F1F5099FB2564F54F365663542CF46D92F92711BE2085073957ED16C.png?needInitFileName=true?needInitFileName=true)
函数注释生成
DevEco Studio支持在函数定义处，快速生成对应的注释。在函数定义的代码块前，输入“/**”+回车键，快速生成注释信息。
C++文件同时支持使用“//!”+回车键快速生成注释。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.51248220013545584736211722418142:50001231000000:2800:769F47AD47FEE10464EBD0CD29DD928738894F95375B3271C4FFF0044E87984D.gif?needInitFileName=true?needInitFileName=true)
代码查找
通过对符号、类或文件的即时导航来查找代码。检查调用或类型层次结构，轻松地搜索工程里的所有内容。通过连续点击两次Shift快捷键，打开代码查找界面，在搜索框中输入需要查找内容，下方窗口实时展示搜索结果。双击查找的结果可以快速打开所在文件的位置。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.66820703790215512956511138541741:50001231000000:2800:895D96DA64575767914C0D7E16DC3D416AF2CC5B5588851092E78900571AC931.png?needInitFileName=true?needInitFileName=true)
快速查阅API接口及组件参考文档
在编辑器中调用ArkTS/JS API或组件时，支持在编辑器中快速、精准调取出对应的参考文档。
可在编辑器中，鼠标悬停在需要查阅的接口或组件，弹窗将显示当前接口/组件在不同API版本下的参数等信息，单击弹窗右下角Show in API Reference，或选中接口或组件，右键点击Show in API Reference，可以快速查阅更详细的API文档。
DevEco Studio集成了离线版API参考类文档，最新版本请参考官网HarmonyOS API参考。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.42864970212127176839600331645567:50001231000000:2800:1D6330C5C580A4B605A3E1D4713E12F5CE604F1AACC9BFBE496544B59FEF9FC7.gif?needInitFileName=true?needInitFileName=true)
在弹窗中可以查看：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.32962472044696792354404899853862:50001231000000:2800:E9B4E8A74ACA6BAF68DBC333D92A33E95BFA849A72429BEF22AFF1F82B9F7784.png?needInitFileName=true?needInitFileName=true)
Optimize Imports功能
使用编辑器提供的Optimize Imports，可以快速清除未使用的import，并根据设置的规则对import进行合并或排序。选择文件或目录，使用快捷键Ctrl+Alt+O（macOS为Control+Option+O），或单击菜单栏Code > Optimize Imports。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150617.48220835435190447718179062051463:50001231000000:2800:8135C4F609E7A244EB86E83F827ABDD61BD6B142844CBBD63093FEE3ED90E1D3.gif?needInitFileName=true?needInitFileName=true)
如需修改优化配置，进入File > Settings... > Editor > Code Style，选择开发语言（当前以ArkTS为例），在Imports标签页中，可选择在优化时是否需合并来自同一模块的import，是否需要对同一条import语句导入的元素进行排序，或对多条import语句按模块排序。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.87455100287346903145869930249255:50001231000000:2800:FF863969C86DF123842DE3796B4A16A393E6633F2C513AB84F30ED7F3EF9E1BD.png?needInitFileName=true?needInitFileName=true)
父/子类快速跳转
编辑器支持快速跳转至当前接口、类、方法、属性的子类/父类。点击代码编辑区域左侧的Gutter Icons（装订线图标）可以跳转到对应的父/子接口或类。如有多个继承关系，在弹窗的文件列表中选择需要查看的接口/类即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.76386346753581659651435982084557:50001231000000:2800:C4FC9B2C13730DFC59EEA612B81E9E2C211BB0A940515839A008A22A13AC880D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.63754028459051645379134399281862:50001231000000:2800:70D6467A87CF2CD90B322EF0522AE88BFC9DDD416F9B8BE8AAE289A251ADBEC7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.93033332059244899978678877316185:50001231000000:2800:00695B7FBCA9AF0C44BA12BC89B033742B3D993B1E10E7F3C254AA69C5306728.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.58138491933532137661978768411084:50001231000000:2800:D997CA1F9183645F250B9B96C391AD4EC37BCB8DA7DAB6A50D63FADFA9CC7050.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.06749963602533669648257815686612:50001231000000:2800:0DB3F7979EBA1858178818D182CD98E3EAA40BF0C20B28A9B60C4FE34E118E6F.png?needInitFileName=true?needInitFileName=true)
本功能默认开启，可以通过菜单栏进入File > Settings > Editor > General > Gutter Icons，通过勾选或取消勾选Implemented、Implementing、Overridden、Overriding四项可以开启或关闭该功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.71138250675332540935303686017644:50001231000000:2800:EE70FB36EF7BC6133A3B46DFE52A1B5AB1B947C43DE7D065FAB194683EAEB158.png?needInitFileName=true?needInitFileName=true)
查看接口/类的层次结构
编辑器支持查看当前接口/类父类或子类的层次结构。选中或将光标放置于类/接口名称处，使用快捷键Ctrl+H，或在菜单栏Navigate页签下选择Type Hierarchy，在弹出的Hierarchy窗口中查看接口/类的继承关系结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.93744071829120161676944884221294:50001231000000:2800:D1718EF2B54789F1B121BC43CEF0298328F77B72049A0CFA6D44CE15E10A9EB3.png?needInitFileName=true?needInitFileName=true)
Hierarchy窗口按钮功能：
| 图标  | 功能  |
| --- | --- |
|   | 显示所选类的父类和子类。 该功能不支持查看接口的继承关系。  |
|   | 显示当前类/接口的父类。  |
|   | 显示当前类/接口的子类。  |
|   | 按字母顺序对继承关系结构树中的所有同级元素进行排序。  |
|   | 更新显示所有的类/接口的继承关系结构。  |
|   | 默认双击结构树中类/接口名称时，编辑窗口将跳转至所选类/接口所在的代码位置。勾选该选项后，单击结构树中类/接口名称，即可跳转访问。  |
|    | 展开/折叠继承关系结构。  |
|   | 锁定当前Hierarchy窗口显示于编辑窗口上。  |
|   | 将类/接口的继承关系结构导出到文本文件中。  |
|   | 关闭工具窗口。  |
图标
功能
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.49002953432644137250515557577974:50001231000000:2800:9CAC3E8F7A9BE6CFCF28B57656DECD9613CA765ED87402C05CF8A0A09A210EA1.png?needInitFileName=true?needInitFileName=true)
显示所选类的父类和子类。
该功能不支持查看接口的继承关系。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.27270076465108329383771079788906:50001231000000:2800:55ED6AB15C9F4077A89F07A22F54EE53913183B2A56C865D0047BDCC1FF97CCB.png?needInitFileName=true?needInitFileName=true)
显示当前类/接口的父类。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.11358453043192343788037865851973:50001231000000:2800:E21AC4DB16C3BD9EA6A160FB7E4CEADF33B881B5B90682C2CC33C8FCA94B7E73.png?needInitFileName=true?needInitFileName=true)
显示当前类/接口的子类。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.11619793244757804164558724762899:50001231000000:2800:E6865C87CB9AF5DC6CEBE0DE8C2EA2E7B3098F58CB93BD8C135B589B8E9E1153.png?needInitFileName=true?needInitFileName=true)
按字母顺序对继承关系结构树中的所有同级元素进行排序。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.10274209927762107932947372053726:50001231000000:2800:2D977654DFBF5D52EFCB5EDF9C67A6E76A26617A85ECFD983AA217B84D64677F.png?needInitFileName=true?needInitFileName=true)
更新显示所有的类/接口的继承关系结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.26429338027728906762100699822023:50001231000000:2800:34E11DF6ACFF4A4FC2FF9EDE203C79AFDCC2027C4C87FBF1B4071796D472AF02.png?needInitFileName=true?needInitFileName=true)
默认双击结构树中类/接口名称时，编辑窗口将跳转至所选类/接口所在的代码位置。勾选该选项后，单击结构树中类/接口名称，即可跳转访问。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.56896780058810125414202915807508:50001231000000:2800:FB1FA857B833AED0D50A08E1E67277F3A59732728D5EBA7C62629F7D92B5DCE0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.10084081456521353979851849442266:50001231000000:2800:B90CCBF8F5373F132EECA69DF7AB90E878E4F63FFD0F87E95704B7472ED44363.png?needInitFileName=true?needInitFileName=true)
展开/折叠继承关系结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.31668299722304902329983114258107:50001231000000:2800:98D80B750388DF03F9A43170C4465D856AC4274C1D818CB938A2E0734BDADF0E.png?needInitFileName=true?needInitFileName=true)
锁定当前Hierarchy窗口显示于编辑窗口上。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.70687991796387269970887169434369:50001231000000:2800:2FC59EE3712F37889FB64B47506F0F69F35FE80EAABD0F546FD107A4E8D0F730.png?needInitFileName=true?needInitFileName=true)
将类/接口的继承关系结构导出到文本文件中。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150618.27845971821614527813268611860706:50001231000000:2800:CD04A7C3BA98429B11213351966F871AA7BEDC5B37356225E048CA834F055CB9.png?needInitFileName=true?needInitFileName=true)
关闭工具窗口。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-code-completion-V14
爬取时间: 2025-04-30 06:49:37
来源: Huawei Developer
代码自动补全
提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。
自动补齐功能默认按最短路径进行排序，如仅需按照最近使用过的类、方法、字段和关键字等名称提供补全内容排序，可以在File > Settings（MacOS为DevEco Studio > Preferences）> Editor > General > Code Completion中勾选“Sort suggestions by recently used”。
若已勾选代码补齐按最近使用排序但未生效，请检查Code Completion页面，确保“Sort suggestions alphabetically”已取消勾选。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.43789968260237849669533659781361:50001231000000:2800:7A2E1C7151F92FAED48C90EB4A19CFC66C19235DDB25852DC6C5B3F5B99A070F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.23563962667572496236442330426791:50001231000000:2800:430ABF5302AFEC9DA83D456CB3942A587DDB01782DB63660AA73A47FE7C11E3E.gif?needInitFileName=true?needInitFileName=true)
快速覆写父类
DevEco Studio提供Override Methods，辅助开发者根据父类模板快速生成子类方法，提升开发效率。将光标放于子类定义位置，使用快捷键Ctrl+O，或右键单击Generate...，选择Override Methods，指定需要覆写的对象（方法、变量等），点击OK将自动生成该对象的覆写代码。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.67035153404725050476510725580497:50001231000000:2800:929D0218A881DD30FDD6E0116152264B508F8806523C838837B4002B456F61C0.gif?needInitFileName=true?needInitFileName=true)
快速生成构造器
编辑器支持为类快速生成一个对应的构造函数。
在类中使用快捷键Alt+Insert，或单击鼠标右键选择Generate...，在弹窗中选择Constructor，选择一个或多个需要生成构造函数的参数，点击OK。若选择Select None，则生成不带参数的构造器。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.09557408847460225140821477052943:50001231000000:2800:E22FA0CCBCEB1C782FF3643956408ACE3F6A88CFC70833EEFCE09517A3782BDF.gif?needInitFileName=true?needInitFileName=true)
快速生成get/set方法
编辑器支持为类成员变量或对象属性快速生成get和set方法。
将光标放置在当前类中，单击右键选择Generate...>Getter and Setter，或者使用快捷键Alt+Insert，在菜单中选择Getter and Setter，完成方法快速生成。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.34099549003057003433760099712670:50001231000000:2800:351360E9F93B1DD149630F73F61ED1C5ED8A1007D57006630F6152307B40DBF6.gif?needInitFileName=true?needInitFileName=true)
快速生成声明信息到Index文件
编辑器支持将HSP和HAR模块中变量、方法、接口、类等需要对外暴露的信息，通过Generate...>Declarations功能，批量在Index.ets文件中进行声明，便于其他模块调用。
在HSP或HAR模块内的文件编辑界面，单击右键选择Generate...>Declarations，或者使用快捷键Alt+Insert，在菜单中选择Declarations，按住快捷键Ctrl并选择需要声明的变量名、方法名、接口名、类名等，即可在模块的Index.ets文件中批量生成相应的声明信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.55248617972271919022214374749301:50001231000000:2800:19521D7E368895B1783F992BD2D3946C38943E30FB3F9A6AC11AE4216E743305.gif?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-code-check-V14
爬取时间: 2025-04-30 06:50:11
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-realtime-check-V14
爬取时间: 2025-04-30 06:50:45
来源: Huawei Developer
实时检查
编辑器会实时的进行代码分析，如果输入的语法不符合编码规范，或者出现语义语法错误，将在代码中突出显示错误或警告，将鼠标放置在错误代码处，会提示详细的错误信息。
从DevEco Studio 4.0 Release版本开始，当compatibleSdkVersion≥10时，编辑器代码实时检查支持ArkTS性能语法规范检查。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.68869808011646334614130741315605:50001231000000:2800:A131C6FB14F3269303D33C908D1EB0D3BBD98E48AF51FD8A681EA781BDD7F633.png?needInitFileName=true?needInitFileName=true)
当前compileSDKVersion≥10且arkTSVersion≥1.1(默认)时ArkTS严格类型检查支持实时检查。
代码快速修复
DevEco Studio支持代码快速修复能力，辅助开发者快速修复ArkTS或C++代码问题。
查看告警信息：使用双击Shift快捷键打开文件查询框，输入problems打开问题工具面板；双击对应告警信息，可以查看告警的具体位置及原因。
快速修复：将光标放在错误告警的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式；单击More actions可查看更多修复方法。或是在页面出现灯泡图标时，可点击图标并根据相应建议，实现代码快速修复。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.11955571890960956623005107293392:50001231000000:2800:15C7B9C615D808D7D1D7DA97DF3AA65ABA07234E4069607C864E6F8313156375.png?needInitFileName=true?needInitFileName=true)
C++快速修复使用演示
下面通过示例展示C++代码中快速修复功能的使用方法。
填充switch语句
编辑器支持快速修复方式，对C++代码自动补齐switch条件表达式缺失的case条件，提升编码效率。
光标悬浮在switch表达式的条件变量处，点击灯泡图标，在下拉菜单中选择Create missing switch cases，完成缺失的case条件补充。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.02031773574057387398715854746891:50001231000000:2800:EC8FBA3342A39A524948799AF8003AC0CCF6BF958144299820DB23919FE8D2D4.gif?needInitFileName=true?needInitFileName=true)
使用auto替换类型
编辑器中可以用 auto 替换 iterator，new expression，cast expression的声明类型。光标悬浮在类型名称处，点击灯泡图标，在下拉菜单中选择Replace the type with 'auto'完成替换。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.15053908254626174381379389458205:50001231000000:2800:2DCCEABFB0B14123EB7391873B60CAE3A420E7F22B6A15B5FCD6D78B34EB3E35.gif?needInitFileName=true?needInitFileName=true)
用？：三元操作符替换if-else
编辑器中支持将if-else语句替换为？：三元操作符。光标放在if表达式的条件处，左侧出现黄色灯泡图标，点击灯泡图标，在下拉菜单中选择Replace 'if else' with '?:'完成替换。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.96021545902376902962615582444207:50001231000000:2800:5DD3AEF3721C9CA6F5C080C73734F991169C63E16C9567ECFD4DE4A461A0D1FE.gif?needInitFileName=true?needInitFileName=true)
从使用处生成构造函数
如使用了未定义的构造函数，可通过quickfix方式快速生成相应的构造函数定义。点击构造函数名称，左侧出现红色灯泡后，点击灯泡图标选择Create new constructor 'xxx'生成构造函数。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.24158449630704305745783056884313:50001231000000:2800:4CF122BA1AFEBC9A1D7E098B9EE6C0B9A9E68448DBB6AA03508F894FC63DD331.gif?needInitFileName=true?needInitFileName=true)
将变量拆分为声明和赋值
光标点击需要拆分的变量，左侧出现黄色灯泡后，点击灯泡图标选择Split into declaration and assignment，将变量的声明赋值语句拆分成声明语句和赋值语句。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150619.89915475808599032033532859683121:50001231000000:2800:B2A0D4F3C175410099DAF6572C58D09FC8E1F3C0F83D42D1265F0DE03B0E4166.gif?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-code-linter-V14
爬取时间: 2025-04-30 06:51:20
来源: Huawei Developer
Code Linter代码检查
Code Linter针对ArkTS/TS代码进行最佳实践/编程规范方面的检查。检查规则支持配置，配置方式请参考配置代码检查规则。
开发者可根据扫描结果中告警提示手工修复代码缺陷，或者执行一键式自动修复，在代码开发阶段，确保代码质量。
检查方法：
在已打开的代码编辑器窗口单击右键点击Code Linter，或在工程管理窗口中鼠标选中单个或多个工程文件/目录，右键选择Code Linter> Full Linter执行代码全量检查。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.82410560480101957545743216191519:50001231000000:2800:02BA6A5C87989520C72C5A7738894FBD595C3DD17CB60E879A5BB95A467EE5EB.png?needInitFileName=true?needInitFileName=true)
如只需对Git工程中增量文件（包含新增/修改/重命名）进行检查，可在commit界面右下角点击齿轮图标，选择Incremental Linter执行增量检查。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.49255328323984302014415822750040:50001231000000:2800:28DD93FA2FBA5495314BF90DEFC70F1243B56730AF52DCB1D095D9CD2B315F76.png?needInitFileName=true?needInitFileName=true)
配置代码检查规则
在工程根目录下创建code-linter.json5配置文件，可对于代码检查的范围及对应生效的检查规则进行配置，其中files和ignore配置项共同确定了代码检查范围，ruleSet和rules配置项共同确定了生效的规则范围。具体配置项功能如下：
files：配置待检查的文件名单，如未指定目录，将检查当前被选中的文件或文件夹中所有的.ets文件。
ignore：配置无需检查的文件目录，其指定的目录或文件需使用相对路径格式，相对于code-linter.json5所在工程根目录，例如：build/**/*。
ruleSet：配置检查使用的规则集，规则集支持一次导入多条规则。规则详情请参见Code Linter代码检查规则。目前支持的规则集包括：
rules：可以基于ruleSet配置的规则集，新增额外规则项，或修改ruleSet中规则默认配置，例如：将规则集中某条规则告警级别由warn改为error。
overrides：针对工程根目录下部分特定目录或文件，可配置定制化检查的规则。
查看/处理代码检查结果
扫描完成后，在底部工具面板查看检查结果。勾选Defects中不同告警等级，可分别查看对应告警级别的信息。双击某条告警结果，可以跳转到对应代码缺陷位置；选中告警结果时，可以在右侧Defect Description窗口查看告警对应的规则详细说明，其中包含正向和反向示例，并根据其中的建议修改代码；搜索规则时，可设定是否全词匹配和大小写敏感。
单击图标，查看可修复的代码规则，点击代码修复图标，可以一键式批量修复告警，并刷新检查结果。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.76149238430329808636527704936029:50001231000000:2800:CA08910CAD93B99FDE606AA947BBE1C60C16B36FF24BAE35FE2C0A957B3C64B5.jpg?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.10949004866023703329902976075772:50001231000000:2800:7E880A5E50D484900F341D8CA8478918D5D15033E78FF7E3E24296CBCB92391A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.90830417203621890618854090046925:50001231000000:2800:79A5415DDAAA7BE49DCE0321BE285A71059996DD5E26AF51E33FBA7F43A18F55.png?needInitFileName=true?needInitFileName=true)
屏蔽告警信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.70188711989488931041797155740172:50001231000000:2800:BE3C38AAAFD08FF855F25B1EE84DCADFC68BF14F28FEF9AFDE0E83B910CB12CC.jpg?needInitFileName=true?needInitFileName=true)
如需恢复忽略的报错信息，可以直接删除该行上方的注释，重新执行Code Linter检查。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.98532863155644901256075304093519:50001231000000:2800:61D13150381C62FF89D07F605E790A894F09A1384ED3D2CEFE38FEC8D1DBE1A9.png?needInitFileName=true?needInitFileName=true)
导出检查结果：点击工具面板左侧导出按钮，即可导出检查结果到excel文件，包含告警所在行，告警明细，告警级别等信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.57856054153828171155844751991818:50001231000000:2800:C084948BA119A7016B9156926118F749052C47F83EEB3932C04E48BCD4EC227D.jpg?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.01878768930727311647903598387368:50001231000000:2800:B3F8149590C38FCC8BFA44997BCA678CBAF6BB36E4C1718A2A0A484873BCF1BC.png?needInitFileName=true?needInitFileName=true)
实践说明
以@typescript-eslint/no-restricted-syntax（使用某类语法时，codelinter告警）、@typescript-eslint/naming-convention（命名风格校验）和@hw-stylistic/file-naming-convention（检查代码文件的命名风格）三个规则为例，介绍codelinter配置文件的使用方法。
示例1：调用类Foo下bar方法时，Code Linter告警
在配置文件中定义规则
在ArkTS工程中，pages/Index.ets文件下增加以下用例：
在工程根目录下新建code-linter.json5文件（文件名不可修改），新增以下配置：
如需在code-linter.json5文件中配置其他字段，请参见配置代码检查规则。
执行代码检查
对pages/Index.ets文件执行代码检查，检查结果如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.00564468659862096424903747008934:50001231000000:2800:4033A7C680A1E6618AF3D37359DB1C68F45846241D10467ACD35E24A9F545EEB.png?needInitFileName=true?needInitFileName=true)
示例2：对类名Foo的命名风格校验
在配置文件中定义规则
在ArkTS工程中，pages/Index.ets文件下增加以下用例：
在工程根目录下新建code-linter.json5文件，新增以下配置：
| 字段名称  | 参数说明  | 是否必选  | 类型  | 支持配置的参数  |
| --- | --- | --- | --- | --- |
| selector  | 配置要检查的语法  | 是  | 字符串、字符串数组  | variable：变量function：函数parameter：参数parameterProperty：参数属性accessor：get/set方法enumMember：枚举成员classMethod：类方法structMethod：自定义组件中的方法objectLiteralMethod：对象方法typeMethod：接口方法classProperty：类属性structProperty：自定义组件中的属性objectLiteralProperty：对象属性typeProperty：接口属性class：类struct：自定义组件interface：接口typeAlias：类型别名enum：枚举typeParameter：泛型参数default：包含以上所有的类型variableLike：包含variable，function，parametermemberLike：包含classProperty，structProperty，objectLiteralProperty，typeProperty，parameterProperty ，enumMember，classMethod，objectLiteralMethod，typeMethod，accessortypeLike：包含class，struct，interface，typeAlias，enum，typeParametermethod：包含classMethod，structMethod，objectLiteralMethod，typeMethodproperty：包含classProperty，objectLiteralProperty，typeProperty  |
| format  | 配置期望的命名风格  | 是  | 字符串数组  | camelCase：小驼峰命名风格，比如getName，getID（支持连续大写字母），不支持下划线strictCamelCase：严格小驼峰命名风格，除了不支持连续大写字母（getID），其他的和camelCase相同PascalCase：大驼峰命名风格，比如Foo，CC，除了要求第一个字母大写，其他的和camelCase相同StrictPascalCase：大驼峰命名风格，除了不支持连续大写字母（CC），其他的和PascalCase相同snake_case：小写字母+下划线+小写字母的命名风格，比如a_a，不支持_a，a_a_UPPER_CASE：大写字母+下划线+大写字母的命名风格，比如A_A，不支持_A，A_A_  |
| custom  | 配置用户自定义的命名风格  | 否  | 对象  | regex：属性必选，配置具体的正则match：属性必选，配置为true表示正则未命中时报错，配置为false表示正则命中时报错  |
| leadingUnderscore/trailingUnderscore  | 配置是否允许以下划线开头/以下划线结尾的命名风格  | 否  | 字符串  | allow：允许以一个下划线开头/结尾的命名风格，比如_nameallowDouble：允许以两个下划线开头/结尾的命名风格，比如__nameallowSingleOrDouble：允许以一个或者两个下划线开头/结尾的命名风格（allow+allowDouble）forbid：禁止以下划线开头/结尾的命名风格，比如_name，__namerequire：必须是以下划线开头/结尾的命名风格，比如_name，__namerequireDouble：必须是以两个下划线开头/结尾的命名风格，比如__name  |
| prefix/suffix  | 配置固定前缀/后缀的命名风格。如果前缀/后缀未匹配则报错  | 否  | 字符串数组  | 用户自定义前缀/后缀  |
| filter  | 过滤特定的命名风格，检查或者不检查正则命中的命名  | 否  | 对象  | 配置格式与custom相似 match：设置为true表示只检查正则命中的名字，设置为false表示不检查正则命中的名字 regex：设置过滤的正则 说明支持直接配置一个字符串，这个字符串配置的是regex，此时match相当于配置的是true。   |
| modifiers  | 匹配修饰符，只有包含特定修饰符的命名才会检查  | 否  | 字符串数组  | abstract：匹配abstract关键字override：匹配override关键字private：匹配private关键字protected：匹配protected关键字static：匹配static关键字async：匹配async关键字const：匹配const关键字destructured：匹配解构语法exported：匹配export关键字global：匹配全局声明#private：匹配私有符号#public：匹配public级别的访问修饰符requiresQuotes：匹配字符串类型的命名，并且 字符串中包含特殊字符unused：匹配未使用的声明  |
| types  | 匹配类型，只有特定类型的名字才会检查  | 否  | 字符串数组  | array：数组类型boolean：布尔类型function：函数类型number：数字类型string：字符串类型  |
字段名称
参数说明
是否必选
类型
支持配置的参数
selector
配置要检查的语法
是
字符串、字符串数组
format
配置期望的命名风格
是
字符串数组
custom
配置用户自定义的命名风格
否
对象
leadingUnderscore/trailingUnderscore
配置是否允许以下划线开头/以下划线结尾的命名风格
否
字符串
prefix/suffix
配置固定前缀/后缀的命名风格。如果前缀/后缀未匹配则报错
否
字符串数组
用户自定义前缀/后缀
filter
过滤特定的命名风格，检查或者不检查正则命中的命名
否
对象
配置格式与custom相似
match：设置为true表示只检查正则命中的名字，设置为false表示不检查正则命中的名字
regex：设置过滤的正则
支持直接配置一个字符串，这个字符串配置的是regex，此时match相当于配置的是true。
modifiers
匹配修饰符，只有包含特定修饰符的命名才会检查
否
字符串数组
types
匹配类型，只有特定类型的名字才会检查
否
字符串数组
以上配置的参数有校验优先级：filter > types > modifiers > validate leading underscore > validate trailing underscore > validate prefix > validate suffix > validate custom > validate format。
执行代码检查
对pages/Index.ets文件执行代码检查，检查结果如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.64510069612532156238402102565055:50001231000000:2800:2D69D299C69AE5A255AD881F24776366924A491B7AAF89D1F5DFC3E3C46E9285.png?needInitFileName=true?needInitFileName=true)
示例3：检查代码文件的命名风格
在配置文件中定义规则
在ArkTS工程中，pages目录下新建test.ets文件；
在工程根目录下新建code-linter.json5文件，新增以下配置：
如果selector属性不配置，默认检查代码文件和资源文件的命名风格。
执行代码检查
对pages/test.ets文件执行代码检查，检查结果如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150620.25077895974314236861688810116016:50001231000000:2800:C6440FC80C5A7B79BB7E6101DE319582D9191124AC5AEEE1EF1694BD87BA0323.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-code-refactoring-V14
爬取时间: 2025-04-30 06:51:54
来源: Huawei Developer
ArkTS/TS代码重构
Refactor-Extract代码提取
在编辑器中支持将函数内、类方法内等区域代码块或表达式，提取为新方法/函数（Method）、常量（Constant）、接口（Interface）、变量（Variable）或类型别名（Type Alias）。准确便捷的将所选区域代码从当前作用域内进行提取，提升编码效率。选中所需要提取的代码块，右键单击Refactor，选择需要提取的类型。
Refactor-Extract代码提取为类型别名（Type Alias）能力仅TS语言支持。
方法/函数（Method）支持选中代码块或完整语句进行提取：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.22592063191055890145548280295344:50001231000000:2800:0C38B7FBE4430DD3E7453F2A4B3B015753EB3677F7F94ABA3B25B640CA3B3BB7.gif?needInitFileName=true?needInitFileName=true)
在ArkTS语言中，支持将组件调用代码块提取为@Builder装饰器装饰的方法，组件属性调用表达式可提取为@Styles或@Extend装饰器装饰的方法。
使用方式：选中需要提取的组件或属性，右键单击Refactor，选择Extract Method...，组件私有属性可提取为@Extend装饰的方法，通用属性可提取为@Styles或@Extend装饰的方法。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.28046152285516500003891507370461:50001231000000:2800:3A6285DD38951A10CA8BC4E0D70B6217F4AB75D7CE5C67C57EBA6C214EA4FEE7.gif?needInitFileName=true?needInitFileName=true)
常量（Constant）支持选中单行表达式进行提取：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.99495228319030540974424903779427:50001231000000:2800:60E6CDE7E7263E613DB89F93A5E46CC53593E9D5EE466512AE574903CC00C682.gif?needInitFileName=true?needInitFileName=true)
接口（Interface）支持选中对象自变量进行提取：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.17855392358532059939088345145117:50001231000000:2800:E654464B6C4CF9784321D86C5CB8BB95760547706AA903F6AC5F6E851FDAAED6.gif?needInitFileName=true?needInitFileName=true)
支持选中表达式提取为变量（Variable）：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.73620430452624295375229466407726:50001231000000:2800:7E71249D6FC6F0CA129E637C3F9038F626EC88618D15266F9C1B4A016A36E652.gif?needInitFileName=true?needInitFileName=true)
Refactor-Convert代码转换
编辑器内提供Convert重构能力，支持Convert between named imports and namespace imports等高频转换操作，辅助开发者高效重构代码，提升代码质量。
| 功能  | 说明  | 使用方法  | 支持转换的源码类型  |
| --- | --- | --- | --- |
| Convert to class  | 将JS源码中的function转换为符合ES6标准的类  | 点击或选中function名，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。 说明若当前工程中已引用该方法，执行Convert to class后，在Find Usages中可查看引用的具体位置，点击Do Refactor可忽略冲突并执行转换；也可以逐条修改引用位置的代码后，重新执行上述操作。   | JS  |
| Convert to anonymous function  | 将箭头函数转换为匿名函数  | 选中箭头函数赋值变量，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  | JS/TS  |
| Convert to named function  | 将箭头函数转换为普通函数  | 选中箭头函数赋值变量，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  | JS/TS/ArkTS  |
| Convert to arrow function  | 将匿名函数转换为箭头函数  | 选中匿名函数赋值变量，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  | JS/TS/ArkTS  |
| Convert default export to named export  | 支持named export和default export相互转换   | 完整选中export default语句，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  | JS/TS/ArkTS   |
| Convert named export to default export  | 完整选中export语句，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  |
| Convert named imports to namespace import  | 支持在命名import和命名空间import形态间转换   | 完整选中import语句，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  | JS/TS/ArkTS   |
| Convert namespace import to named imports  | 完整选中命名空间import语句，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  |
| Convert to template string  | 将字符串转换为模板字面量  | 选中字符串或完整表达式，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  | JS/TS/ArkTS  |
| Convert to optional chain expression  | 将判空逻辑转换为可选链式调用  | 选中连续判空表达式，右键单击Refactor > Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。  | JS/TS/ArkTS  |
功能
说明
使用方法
支持转换的源码类型
Convert to class
将JS源码中的function转换为符合ES6标准的类
点击或选中function名，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
若当前工程中已引用该方法，执行Convert to class后，在Find Usages中可查看引用的具体位置，点击Do Refactor可忽略冲突并执行转换；也可以逐条修改引用位置的代码后，重新执行上述操作。
JS
Convert to anonymous function
将箭头函数转换为匿名函数
选中箭头函数赋值变量，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
JS/TS
Convert to named function
将箭头函数转换为普通函数
选中箭头函数赋值变量，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
JS/TS/ArkTS
Convert to arrow function
将匿名函数转换为箭头函数
选中匿名函数赋值变量，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
JS/TS/ArkTS
Convert default export to named export
支持named export和default export相互转换
完整选中export default语句，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
JS/TS/ArkTS
Convert named export to default export
完整选中export语句，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
Convert named imports to namespace import
支持在命名import和命名空间import形态间转换
完整选中import语句，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
JS/TS/ArkTS
Convert namespace import to named imports
完整选中命名空间import语句，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
Convert to template string
将字符串转换为模板字面量
选中字符串或完整表达式，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
JS/TS/ArkTS
Convert to optional chain expression
将判空逻辑转换为可选链式调用
选中连续判空表达式，右键单击Refactor>Convert，或使用快捷键Ctrl+Alt+Shift+R（MacOS为Option+Shift+Command+R），在弹窗中选择转换的方式。
JS/TS/ArkTS
Refactor-Rename代码重命名
代码编辑支持Rename功能，可以快速更改变量、方法、对象属性等相关标识符及文件、模块的名称，并同步到整个工程中对其进行引用的位置。
使用方式：选中需要重新命名的标识符（变量、类、接口、自定义组件等），右键单击Refactor，选择Rename...（或使用快捷键Shift+F6），在弹框中输入新的标识符名称，并在Scope中选择替换的范围，点击Refactor完成重新命名。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.78593351585052546987024896658227:50001231000000:2800:016BF67C3EA41DE5237C1A4D95FAA1396FBD088FECF90A267A0CCE1F4F99161A.png?needInitFileName=true?needInitFileName=true)
代码编辑支持筛选并过滤不需要rename的引用位置。在Rename...弹窗中点击Preview，在弹出预览窗口中，用户选中无需Rename的选项，单击右键菜单Exclude/Remove进行过滤/删除，完成筛选后点击左下角Do Refactor，重新执行Rename操作。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.36176751964330981162381495148361:50001231000000:2800:C2984FE0E01B8E1DF6B6BC64661A192BACEED875208A4F9CF08390A6B47CB9A0.png?needInitFileName=true?needInitFileName=true)
若ArkTS文件中存在C++接口调用，使用Rename进行重命名时，C++文件中涉及的函数名也会被重命名。
Move File
在文件中单击右键，选择Refactor > Move File...，在弹窗中输入或点击...选择指定的目录，点击Refactor，可将当前文件移动至该目录下。勾选Search for references，可查找并更新工程中对该文件的引用；勾选Open in editor，可在编辑器中查看移动的文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.44405091365919288321022637746238:50001231000000:2800:AE08F60BFF130D93710DB3ADF6677870DA6E3574F6AEDA31E988A0E383DAC3B6.png?needInitFileName=true?needInitFileName=true)
Safe Delete
编辑器支持Safe Delete功能，帮助您安全地删除代码中的标识符对象（变量、函数或类等）或删除指定文件。在删除前，编辑器将先在代码中搜索对该对象的引用，如果存在引用，编辑器将提示您进行必要的检查和调整。
使用方式：在编辑器内选中需要删除的标识符对象或在工程目录选择待删除的文件，右键单击Refactor，选择Safe Delete，单击OK将自动检查当前对象在代码中被引用的情况，点击View Usages可查看具体使用的代码内容，点击Delete Anyway将直接删除该对象的定义。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.82553101518738940194291673896979:50001231000000:2800:BDAA17AD7A5120D9F0AD7478A9F871665D410AC72E6417E84D437B0234BAA228.png?needInitFileName=true?needInitFileName=true)
C++代码重构
编辑器提供C++代码重构能力，当前支持展开宏、交换if分支、移动函数体到声明处等使用场景下的重构能力，提升开发效率。
展开宏
支持在当前宏引用处展开宏。将光标移动至需要展开的宏，右键单击Refactor，选择Inline，展开此处引用的宏。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.55946177130007316997877664803775:50001231000000:2800:5B10103F5989D7EB2D8C3269F113B1B12450A203C6E673687B19C676CB9BE175.gif?needInitFileName=true?needInitFileName=true)
交换if分支
编辑器支持在选中if-else完整代码块的情况下，实现对if-else代码块的位置交换，并对条件取反。
使用约束
使用方式
编辑器内选择需要转换的代码区域，右键单击Refactor，选择Swap If Branches，对原有if条件取反，并交换if-else原代码块顺序。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.53126187737768661925269631939705:50001231000000:2800:CFDFE4FD21159229A6767EFFAB9934A65BC67F4ADA1D8D233EF53723F419436C.gif?needInitFileName=true?needInitFileName=true)
移动函数体到声明处
编辑器支持将函数体从源文件移动到头文件中，提高代码可读性。编辑器内选中函数名，右键单击Refactor，选择Move to Declaration，源文件中的函数实现将移动至头文件中。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.07879586435537479793757917884842:50001231000000:2800:977A1201C589B4F99CD7D5B6E304D2F5F0E6C8F655F96FB617BEBD3844EC6626.gif?needInitFileName=true?needInitFileName=true)
移动函数体到实现处
在编辑器内将光标放在或选中函数名，右键单击Refactor，选择Move to Implementation，选择移动到的文件，将函数定义移动到该文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.09731692663209673846948027398742:50001231000000:2800:F95267718B204D87EFF7AB5E232CC9C4490BE136732E027DC126396F4C71D320.gif?needInitFileName=true?needInitFileName=true)
将语句转为原始字符串
编辑器提供重构能力，支持将带有 \n, \t, \", \\, \'五类转义字符的字符串转换为原始字符串。当前仅支持标准字符串，不支持 u8""等其他字符串。
在编辑器内选择字符串代码区域，右键单击Refactor，选择Convert To Raw String，将语句转换为原始字符串。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150621.92039183724694574844286412593961:50001231000000:2800:CC65267AD1741EA181842DC93434D22CCADC7EC9B15A273A42D609C10964F091.gif?needInitFileName=true?needInitFileName=true)
定义构造函数
编辑器提供重构能力，支持为类的成员变量生成默认的构造函数。
规格限制
使用方法：在类的定义的类名处，右键单击Generate...，选择Constructor，在弹框中点击Define，为成员变量定义一个构造函数。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.24751441864167144935981872209454:50001231000000:2800:4D21A99F0D38651AD288334FC6DB4A1BB85E362047A3F4D400763D1EFF044927.gif?needInitFileName=true?needInitFileName=true)
提取表达式到变量
在编辑器内，选中需要提取的表达式范围，右键单击Refactor，选择Extract Variable，支持提取表达式到变量。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.67051774894121579236198253596370:50001231000000:2800:A177583229888EAEE5BF22D376DF1AF2716D19B0E7DB6585B0CDC26FB2CF09D7.gif?needInitFileName=true?needInitFileName=true)
移除namespace
光标停留在需要移除的namespace处，右键单击Refactor，选择Remove Using Namespace进行移除，可以避免命名冲突，提高代码可读性。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.09482386644068724840164537504931:50001231000000:2800:28ED1F15527DE6C5A1335071961991318A1D6768C9874C00CD917A665F82A176.gif?needInitFileName=true?needInitFileName=true)
添加using声明
编辑器内，光标停留在需要添加using声明处，右键单击Refactor，选择Add Using完成使用using定义类型别名。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.11083752591702459451705327633768:50001231000000:2800:E3466921841B9F5ACC2996DBC9F86803DAB17DB382348664AB185117E054E620.gif?needInitFileName=true?needInitFileName=true)
auto自动展开
在auto关键字处右键单击Refactor，选择Expand Auto Type，可以使用推断类型替换auto类型。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.56833799537670713309859155256770:50001231000000:2800:05EE73BDD1486AABC2A4F09AE83989B9811B1E7F714EBF1A6B8A18BA593A6000.gif?needInitFileName=true?needInitFileName=true)
声明隐式成员
编辑器支持在类中声明隐式复制/移动成员。光标停留在需要生成的类处，右键单击Generate..., 选择Copy/Move Members。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.14971871713484048100704812611851:50001231000000:2800:6CF59AD99BF8583610E7CF665A1609F346C9885D9250AD2B7318E68E9AC73CB5.gif?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-arktsdoc-V14
爬取时间: 2025-04-30 06:52:29
来源: Huawei Developer
DevEco Studio支持通过Generate ArkTSDoc功能，将代码文件中变量、方法、接口、类等需要对外暴露的信息快速生成相应的参考文档。
ArkTSDoc生成步骤
1.
2.  生成的ArkTSDoc左侧文档目录和原工程目录结构一致，右侧可点击跳转到当前文件包含的某个变量、方法、接口或类的文档位置。 若没有勾选Open generated documentation in browser选项，在生成ArkTSDoc后，DevEco Studio右下角弹出对应提示框，可以点击Go to Folder跳转到生成的ArkTSDoc文件夹，用浏览器打开文件夹中index.html文件即可查看ArkTSDoc文档。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.63992864848041189489079841469055:50001231000000:2800:7902CB0D3A889986089B86394DF0DE59F8896DECE90C65AC2BEF799E8BA68048.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.80665797947457472502528754294596:50001231000000:2800:6FD6F4D6CBA3204D48D9B81B72F9F96C033422E63DD4886FCE50DD220E2F6E5B.png?needInitFileName=true?needInitFileName=true)
生成效果示例
代码示例：
ArkTSDoc文档生成结果：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.39565811153518820684516274371534:50001231000000:2800:5451186ED64C4F97435091930D42E609DAE9C4B1B520618B27E4FA97D81DA138.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-cross-language-code-editing-V14
爬取时间: 2025-04-30 06:53:03
来源: Huawei Developer
生成胶水代码函数框架
DevEco Studio提供跨语言代码编辑功能。当开发者需要使用NAPI封装暴露给ArkTS/JS的接口时，在Cpp头文件内，通过右键Generate > NAPI，快速生成当前函数或类的胶水代码函数框架。
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.61922514103357168177372072146252:50001231000000:2800:FB7C0EF1378AA347749E44E44EBD76A51571F919F26277B1B30A633283564521.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.63790102969344799602050291097027:50001231000000:2800:09304C5FB58350FE805C3702DB347727935B5CA4C1AC866C695F30EB22FFB219.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.36548284878185734980239644042314:50001231000000:2800:AE115E1A0987F03671AF80FD3C414EA1C5E62180D142F03231DF5BB3B124DFFA.png?needInitFileName=true?needInitFileName=true)
跨语言快速生成函数定义
当前支持在跨语言的d.ts文件中，通过Generate native implementation功能，一键生成C++文件中对应函数定义。
将光标悬浮在未定义的函数名处，在悬浮窗中点击Generate native implementation，或点击页面上出现的红色灯泡图标，选择Generate native implementation，生成函数定义。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150622.33013610050388543330444718756288:50001231000000:2800:E936E191A52C126AECCFABAB290A4CF7BE25C97B8FCBB45FE670DE3C5C6B3BFD.gif?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-01-V14
爬取时间: 2025-04-30 06:53:38
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-overview-V14
爬取时间: 2025-04-30 06:54:12
来源: Huawei Developer
DevEco Studio为开发者提供了UI界面预览功能，可以查看UI界面效果，方便开发者随时调整界面UI布局。预览器支持界面代码的实时预览，只需要将开发的源代码进行保存，就可以通过预览器实时查看组件/界面运行效果，方便开发者随时调整代码。
由于操作系统和真机设备的差异，在预览界面中可能出现字体、颜色等与真机设备运行的效果存在差异，预览效果仅作为组件/界面开发过程中的参考，实际最终效果请以真机设备运行效果为准。
为了更好的使用体验，建议先将DevEco Studio升级至最新版本。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-previewchecker-V14
爬取时间: 2025-04-30 06:54:45
来源: Huawei Developer
DevEco Studio启动预览时将执行PreviewChecker，检测通过后才可进行预览，以确保在使用预览器前识别到已知的不支持预览的场景，若存在不支持预览的场景，将给出优化提示，以便于开发者根据提示的建议进行代码优化。
@previewer/mandatory-default-value-for-local-initialization
对于所有将被预览到的组件，如果组件的属性支持本地初始化，则都应当设置一个合法的不依赖运行时的默认值，以确保异常调用到该组件时，即使入参不完整，也能正常运行渲染。
反例
正例
@previewer/no-unallowed-decorator-on-root-component
对于@Entry组件，不允许使用@Consume、@Link、@ObjectLink、@Prop注解；对于@Preview组件，建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件作为预览该组件的容器。
反例
正例
@previewer/paired-use-of-consume-and-provide
如果缺少@Provide定义，@Consume组件在预览时将无法获取有效值，且@Consume不支持本地初始化。建议被@Consume修饰的组件的祖先组件上应当有对应的@Provide属性，并且该属性应当有合法的不依赖运行时的默认值。
反例
正例
@previewer/no-page-method-on-preview-component
@Preview通常修饰在组件上，而非@Entry的页面入口。onPageShow、onPageHide、onBackPress仅在@Entry组件上生效。因此禁止在非路由组件上实例化onPageShow等页面级方法。
反例
正例
@previewer/no-page-import-unmocked-hsp
由于能力缺失，预览器无法确保HSP是可以正常运行的。界面代码调用HSP可能会在预览运行时无法按预期执行，未正确初始化的接口调用可能会导致运行异常，从而影响界面渲染结果。建议待预览的组件及其依赖的组件避免引用HSP，或为该HSP设置Mock实现。
反例
```typescript
import { add } from 'library'; // 该模块未配置自定义mock。
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Text(this.message)
.onClick(() => add(1, 2))
}
}
}
```
正例
```typescript
import { add } from 'library'; // 该模块已配置自定义mock，配置方法见下文。
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Text(this.message)
.onClick(() => add(1, 2))
}
}
}
```
自定义mock配置：
```typescript
// src/mock/myhsp.mock.ets
export function add(a: number, b: number): number {
return a + b;
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-arkts-js-V14
爬取时间: 2025-04-30 06:55:20
来源: Huawei Developer
预览器支持ArkTS/JS应用/元服务“实时预览”和“动态预览”。
-  开发者修改resources/base/profile目录下的配置文件（如main_pages.json/form_config.json），不支持触发实时预览，开发者需要点击重新加载。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.09624136661539844384494279827480:50001231000000:2800:F1676A45BA9C8E2E8C52806A8C6BD938886A5574AA244D4317A2E9EA897B8F6D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.57379079915426532045244054903439:50001231000000:2800:B52300694234729A1D5AE9821A433D272B87981061AB914459578909FAE46B4E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.85874387073106069693156067740758:50001231000000:2800:7E16B72313B3ED02FE218A7E3C74E62B2BFC889B1341B5B62186D554211DE84C.gif?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.41304791691585173880181995374026:50001231000000:2800:81432411047C9DE59A85A9D718E8BCD0E50EEF5B20D42C79DB78C2D0D9D777F4.gif?needInitFileName=true?needInitFileName=true)
以ArkTS为例，使用预览器的方法如下：
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.74272883344804787070588419746350:50001231000000:2800:FE9E429FDCCF5BBCB89A4349FCAEF648F34AB4FB1C744F7034AC969F20866B07.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-arkui-V14
爬取时间: 2025-04-30 06:55:53
来源: Huawei Developer
ArkUI预览支持页面预览与组件预览，下图中左侧图标为页面预览，右侧图标为组件预览。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.04135395680481403513471572833530:50001231000000:2800:FEE5A08B74FF544A6530A3A30E19C470789FEB6C6C4E5460D9B9F33FF1CF0BC1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.93649473586895192496919999327519:50001231000000:2800:7FFF9ED53A6943ABA5005202F750779127529FDB61597312C9F26577C71290DE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.36303257659236378087089581780462:50001231000000:2800:D1DAE3984074DFFA86704F84E65E44DAC30C6525D9C5CD616C9512B3696028EE.png?needInitFileName=true?needInitFileName=true)
页面预览
ArkTS应用/元服务支持页面预览。页面预览通过在工程的ets文件头部添加@Entry实现。
@Entry的使用参考如下示例：
组件预览
ArkTS应用/元服务支持组件预览。组件预览支持实时预览，不支持动态图和动态预览。组件预览通过在组件前添加注解@Preview实现，在单个源文件中，最多可以使用10个@Preview装饰自定义组件。
以上示例的组件预览效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.95246938421635406049624613313276:50001231000000:2800:D8AAE43206412DD0288CF5FB15A1DA053BC3E7AD295D27930A4B279C28B08615.gif?needInitFileName=true?needInitFileName=true)
请注意，如果被预览的组件是依赖参数注入的组件，建议的预览方式是：定义一个组件片段，在该片段中声明将要预览的组件，以及该组件依赖的入参，并在组件片段上标注@Preview注解，以表明将预览该片段中的内容。例如，要预览如下组件：
建议按如下方式预览：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-profile-manager-V14
爬取时间: 2025-04-30 06:56:27
来源: Huawei Developer
由于真机设备有丰富的设备型号，不同设备型号的屏幕分辨率可能不一样。因此，在HarmonyOS应用/元服务开发过程中，由于设备类型繁多，可能需要查看在不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以通过定义不同的预览设备Profile，查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。
定义设备后，可以在Previewer右上角，单击按钮，打开Profile管理器，切换预览设备。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.59563852323378392389391555760448:50001231000000:2800:64E1878EE750244D2195CFD3D41FA10BF90059E532D548746A623DB866361DF7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150623.55276915980864011175915369915562:50001231000000:2800:3DFE1CE9219FAAAE7A9E2AD75B9743857AAA460E0F7C99A9279C5750529A951E.png?needInitFileName=true?needInitFileName=true)
同时，Profile Manager还支持多设备预览功能，具体请参考查看多端设备预览效果。
下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150624.10038444118810546066688574541376:50001231000000:2800:F2231791C49A8C2655F9F3A4B89E45CDD2CEEB102C6ADF509122F62EA3F615B1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150624.68586108455697685126797778159102:50001231000000:2800:A07644FA432A89A1B9397BAB6B4C2622392C4E0866F38B2ADB4F2E75BA6005D7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150624.84665976019508634411127707786961:50001231000000:2800:5E0DDFAC9C6A13C0AF063BCFF15BBA5FC1BE8A64C4CED53712B697D71777DAEE.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-multi-profile-V14
爬取时间: 2025-04-30 06:57:01
来源: Huawei Developer
多端设备预览最多同时支持4个设备的预览。
前面介绍了DevEco Studio支持ArkTS、JS应用/元服务的预览器功能，多端设备预览器支持ArkTS、JS应用/元服务在不同设备上的同时预览。如果两个设备支持的编码语言不同，就不能使用多端设备预览功能。
下面以ArkTS应用/元服务为例，介绍多端设备预览器的使用方法，JS应用/元服务的多端设备预览器使用方法相同。
1.
2.  多端设备预览不支持动画的预览，如果需要查看动画在设备上的预览效果，请关闭Multi-device preview功能后在单设备预览界面进行查看。 多设备预览效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150624.88939451080808118989632914364737:50001231000000:2800:A8221C0698443F33CDE92B7E1593F5C884F9CE18420AEE1060F812E143DDF507.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150624.41519757554755679341523618328846:50001231000000:2800:AF7D0A6F42449A6E7B27EB11A3F1E06F38437E4D2BDCF35DDBC9BD8668ED1F5E.gif?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-inspector-V14
爬取时间: 2025-04-30 06:57:37
来源: Huawei Developer
DevEco Studio提供HarmonyOS应用/元服务的UI预览界面与源代码文件间的双向预览功能，支持ets文件与预览器界面的双向预览。使用双向预览功能时，需要在预览器界面单击图标打开双向预览功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150624.41495429468649185402505329148209:50001231000000:2800:2D5CCD6C3ED6B646634446A80AB22D2DEEA6BFBC8115A46FA700EE02364090C6.png?needInitFileName=true?needInitFileName=true)
不支持服务卡片的双向预览功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150624.33875354273226458440400893685580:50001231000000:2800:8DA4DE3645F086EC9B4956956A12DD6AEA97F7E70056B668CC648394E4193A7D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150624.58563781230020661796916747802022:50001231000000:2800:E450049C8C0C5D97C0C5FDC86B44578D8E02D087FAD65BF3040AD17711A089D6.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-mock-V14
爬取时间: 2025-04-30 06:58:11
来源: Huawei Developer
仅API 11及以上版本的Stage工程支持。
在预览场景中，由于代码的运行环境与真机设备上的运行环境不同，调用部分接口时无法获取到有效的返回值（例如获取电池电量信息等，在预览场景下batteryInfo.voltage返回的是一个固定的值0），这样开发者就无法在预览时查看到不同返回值带来的界面变化。因此，Hamock提供了预览场景的模拟功能，在不改变业务运行逻辑的同时，开发者可以模拟UI组件上的属性或方法，或模拟import的模块接口。
使用前提
使用Hamock在预览场景模拟，需要在工程或模块的oh-package.json5中添加该依赖，然后重新同步工程。
UI组件上的Mock
Hamock提供了@MockSetup用于修饰Mock方法，仅支持声明式范式的组件。当开发者预览该组件时，预览运行时将在组件初始化时执行被@MockSetup修饰的方法。因此，开发者可以在这个被修饰的方法内重定义组件的方法或重赋值组件的属性，其将在预览时生效。
@MockSetup修饰的方法仅在预览场景会自动触发，并先于组件的aboutToAppear执行。
UI组件的方法
1.
2.
```typescript
import { MockKit, when, MockSetup } from '@ohos/hamock';
@Entry
@Component
struct Index {
...
@MockSetup
randomName() {
let mocker: MockKit = new MockKit();
let mockfunc: Object = mocker.mockFunc(this, this.method1);
// mock 指定的方法在指定入参的返回值
when(mockfunc)('test').afterReturn(1);
}
...
// 业务场景调用方法
const result = this.method1('test'); // in previewer, result = 1
}
```
UI组件的属性
1.
2.
```typescript
import { MockSetup } from '@ohos/hamock';
@Component
struct Person {
@Prop species: string;
// 在@MockSetup片段中，定义对象属性
@MockSetup
randomName() {
this.species = 'primates'
}
...
// 业务场景调用属性（如果从初始化到调用期间，该属性无变化）
const result = this.species // in previewer, result = primates
}
```
模块的Mock
系统模块/依赖的模块
1.
2.
3.
本地模块
1.  其中CommonUtils.ets文件示例如下： 本地Module的Mock仅支持src/main/ets目录下的ArkTS或TS文件。
```typescript
// import local module
import LibDefaultExport from '../../../main/ets/utils/CommonUtils'; // get origin default export
import { methodA, ObjectB } from '../../../main/ets/utils/CommonUtils'; // get origin export on demand
class DefaultExportMock extends LibDefaultExport {
// 定义mock实现
public static getName(): String {
return "Mocked Name";
}
};
export {
methodA,
ObjectB,
}
export default DefaultExportMock;
```
2.
3.

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-api-list-V14
爬取时间: 2025-04-30 06:58:47
来源: Huawei Developer
组件
ArkTS组件
| 组件  | API  |
| --- | --- |
| 基础组件                                  | AlphabetIndexer  |
| Blank  |
| Button  |
| Checkbox  |
| CheckboxGroup  |
| DataPanel  |
| DatePicker  |
| Divider  |
| Gauge  |
| Image  |
| ImageAnimator  |
| ImageSpan  |
| LoadingProgress  |
| Marquee  |
| Menu  |
| MenuItem  |
| MenuItemGroup  |
| Navigation  |
| NavRouter  |
| NavDestination  |
| PatternLock  |
| Progress  |
| QRCode  |
| Radio  |
| Rating  |
| ScrollBar  |
| Search  |
| Select  |
| Slider  |
| Span  |
| Stepper  |
| StepperItem  |
| Text  |
| TextArea  |
| TextClock  |
| TextInput  |
| TextPicker  |
| TextTimer  |
| Toggle  |
| 容器组件  | Badge  |
| Column  |
| ColumnSplit  |
| Counter  |
| Flex  |
| FlowItem  |
| GridCol  |
| GridRow  |
| List  |
| ListItem  |
| ListItemGroup  |
| Navigator  |
| Panel  |
| Refresh  |
| RelativeContainer  |
| Row  |
| RowSplit  |
| Scroll  |
| SideBarContainer  |
| Stack  |
| Swiper  |
| Tabs  |
| TabContent  |
| WaterFlow  |
| 绘制组件         | Circle  |
| Ellipse  |
| Line  |
| Polyline  |
| Path  |
| Rect  |
| Shape  |
| 画布组件         | Canvas  |
| CanvasGradient  |
| CanvasPattern  |
| CanvasRenderingContext2D  |
| ImageBitmap  |
| ImageData  |
| Matrix2D  |
| OffscreenCanvasRenderingContext2D  |
| Path2D  |
组件
API
基础组件
AlphabetIndexer
Blank
Button
Checkbox
CheckboxGroup
DataPanel
DatePicker
Divider
Gauge
Image
ImageAnimator
ImageSpan
LoadingProgress
Marquee
Menu
MenuItem
MenuItemGroup
Navigation
NavRouter
NavDestination
PatternLock
Progress
QRCode
Radio
Rating
ScrollBar
Search
Select
Slider
Span
Stepper
StepperItem
Text
TextArea
TextClock
TextInput
TextPicker
TextTimer
Toggle
容器组件
Badge
Column
ColumnSplit
Counter
Flex
FlowItem
GridCol
GridRow
List
ListItem
ListItemGroup
Navigator
Panel
Refresh
RelativeContainer
Row
RowSplit
Scroll
SideBarContainer
Stack
Swiper
Tabs
TabContent
WaterFlow
绘制组件
Circle
Ellipse
Line
Polyline
Path
Rect
Shape
画布组件
Canvas
CanvasGradient
CanvasPattern
CanvasRenderingContext2D
ImageBitmap
ImageData
Matrix2D
OffscreenCanvasRenderingContext2D
Path2D
JS组件
| 组件  | API  |
| --- | --- |
| 基础组件                           | button  |
| chart  |
| divider  |
| image  |
| image-animator  |
| input  |
| label  |
| marquee  |
| menu  |
| option  |
| picker  |
| picker-view  |
| piece  |
| progress  |
| qrcode  |
| rating  |
| search  |
| select  |
| slider  |
| span  |
| switch  |
| text  |
| textarea  |
| toolbar  |
| toolbar-item  |
| toggle  |
| 容器组件                  | badge  |
| dialog  |
| div  |
| form  |
| list  |
| list-item  |
| list-item-group  |
| panel  |
| popup  |
| refresh  |
| stack  |
| stepper  |
| stepper-item  |
| swiper  |
| tabs  |
| tab-bar  |
| tab-content  |
| 画布组件          | canvas  |
| CanvasRenderingContext2D  |
| Image  |
| CanvasGradient  |
| ImageData  |
| Path2D  |
| ImageBitmap  |
| OffscreenCanvas  |
| OffscreenCanvasRenderingContext2D  |
| 栅格组件    | grid-container  |
| grid-row  |
| grid-col  |
| svg组件               | svg  |
| rect  |
| circle  |
| ellipse  |
| path  |
| line  |
| polyline  |
| polygon  |
| text  |
| tspan  |
| textPath  |
| animate  |
| animateMotion  |
| animateTransform  |
组件
API
基础组件
button
chart
divider
image
image-animator
input
label
marquee
menu
option
picker
picker-view
piece
progress
qrcode
rating
search
select
slider
span
switch
text
textarea
toolbar
toolbar-item
toggle
容器组件
badge
dialog
div
form
list
list-item
list-item-group
panel
popup
refresh
stack
stepper
stepper-item
swiper
tabs
tab-bar
tab-content
画布组件
canvas
CanvasRenderingContext2D
Image
CanvasGradient
ImageData
Path2D
ImageBitmap
OffscreenCanvas
OffscreenCanvasRenderingContext2D
栅格组件
grid-container
grid-row
grid-col
svg组件
svg
rect
circle
ellipse
path
line
polyline
polygon
text
tspan
textPath
animate
animateMotion
animateTransform
接口
UI界面
| 模块  | API  |
| --- | --- |
| @ohos.animator (动画)    | Animator  |
| AnimatorResult  |
| AnimatorOptions  |
| @ohos.mediaquery (媒体查询)    | matchMediaSync  |
| MediaQueryResult  |
| MediaQueryListener  |
| @ohos.promptAction (弹窗)          | showToast  |
| showDialog  |
| showActionMenu  |
| ShowToastOptions  |
| Button  |
| ShowDialogSuccessResponse  |
| ShowDialogOptions  |
| ActionMenuSuccessResponse  |
| ActionMenuOptions  |
| @ohos.router (页面路由)              | pushUrl  |
| replaceUrl  |
| back  |
| clear  |
| getLength  |
| getState  |
| enableAlertBeforeBackPage  |
| disableAlertBeforeBackPage  |
| getParams  |
| RouterMode  |
| RouterOptions  |
| RouterState  |
| EnableAlertOptions  |
模块
API
@ohos.animator (动画)
Animator
AnimatorResult
AnimatorOptions
@ohos.mediaquery (媒体查询)
matchMediaSync
MediaQueryResult
MediaQueryListener
@ohos.promptAction (弹窗)
showToast
showDialog
showActionMenu
ShowToastOptions
Button
ShowDialogSuccessResponse
ShowDialogOptions
ActionMenuSuccessResponse
ActionMenuOptions
@ohos.router (页面路由)
pushUrl
replaceUrl
back
clear
getLength
getState
enableAlertBeforeBackPage
disableAlertBeforeBackPage
getParams
RouterMode
RouterOptions
RouterState
EnableAlertOptions
网络管理
| 模块  | API  |
| --- | --- |
| @ohos.net.http (数据请求)  | http.createHttp 如果Http请求需要配置代理才能访问，API 12及以上的预览器支持使用系统的http_proxy/https_proxy/no_proxy环境变量。  |
模块
API
@ohos.net.http (数据请求)
http.createHttp
如果Http请求需要配置代理才能访问，API 12及以上的预览器支持使用系统的http_proxy/https_proxy/no_proxy环境变量。
数据管理
| 模块  | API  |
| --- | --- |
| @ohos.data.preferences (用户首选项)         | data_preferences.getPreferences  |
| data_preferences.deletePreferences  |
| data_preferences.removePreferencesFromCache  |
| Preferences  |
| ValueType  |
模块
API
@ohos.data.preferences (用户首选项)
data_preferences.getPreferences
data_preferences.deletePreferences
data_preferences.removePreferencesFromCache
Preferences
ValueType
文件管理
| 模块  | API  |
| --- | --- |
| @ohos.file.fs (文件管理)              | fs.open  |
| fs.close  |
| fs.fdatasync  |
| fs.fsync  |
| fs.read  |
| fs.write  |
| fs.mkdir  |
| fs.mkdtemp  |
| fs.rename  |
| fs.rmdir  |
| fs.unlink  |
| fs.stat  |
| fs.truncate  |
模块
API
@ohos.file.fs (文件管理)
fs.open
fs.close
fs.fdatasync
fs.fsync
fs.read
fs.write
fs.mkdir
fs.mkdtemp
fs.rename
fs.rmdir
fs.unlink
fs.stat
fs.truncate

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-develop-app-V14
爬取时间: 2025-04-30 06:59:23
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-creating-har-api9-V14
爬取时间: 2025-04-30 06:59:59
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-har-V14
爬取时间: 2025-04-30 07:00:36
来源: Huawei Developer
HAR(Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不同于HAP，不能独立安装运行在设备上，只能作为应用模块的依赖项被引用。
接下来，将简单介绍库模块的工程结构，如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.36017624807413442604785658086407:50001231000000:2800:69BDB5FFDCCC9DFE6DED45180F732C78643A08B77265CAAF5F5EC0EC9298782A.png?needInitFileName=true?needInitFileName=true)
相关字段的描述如下，其余字段与Entry或Feature模块相关字段相同，可参考工程介绍。
本文将介绍如何创建库模块、如何编译共享包、如何引用共享包资源，以及如何发布共享包。
创建库模块
1.
2.  创建完成后，会在工程目录中生成库模块及相关文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.81934028475671288782584069090171:50001231000000:2800:9DF10ED9958463E8D5479307434D2DE82E46619744104D822C1BCC51EAFFD861.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.26145780294283216079741433226343:50001231000000:2800:437884358E186C8578A3299B35291D68CA771D05DE35E30A50A268784F4FAC1F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.83878162491179470635079869774483:50001231000000:2800:F43D31AE9AB9703EBEA822238DCBAF5B85429995D27E8E8B2D1B6CD6FD4EC666.png?needInitFileName=true?needInitFileName=true)
编译库模块
开发完库模块后，选中模块名，然后通过DevEco Studio菜单栏的Build > Make Module ${libraryName}进行编译构建，生成HAR。HAR可用于工程其它模块的引用，或将HAR上传至ohpm仓库，供其他开发者下载使用。若部分源码文件不需要打包至HAR中，可通过创建.ohpmignore文件，配置打包时要忽略的文件/文件夹。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.97681537451797774533805531322733:50001231000000:2800:E4D3A93970CC5ECC19AF8E925DA4AFA6C8845524CD77568705E12E385AFDEED4.png?needInitFileName=true?needInitFileName=true)
编译构建的HAR可在模块下的build目录下获取，包格式为*.har。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.33520778918926027856878524734494:50001231000000:2800:0EE6CC6EDF4F37160B2A9558EFD9C7C30FAC405A9B390C291D2B584528AEEDB9.png?needInitFileName=true?needInitFileName=true)
在编译构建HAR时，请注意以下事项：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hsp-V14
爬取时间: 2025-04-30 07:01:12
来源: Huawei Developer
DevEco Studio支持开发动态共享包HSP（Harmony Shared Package）。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。
使用约束
开发动态共享包
创建HSP模块
1.
2.
3.  创建完成后，会在工程目录中生成库模块及相关文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.94789617872706710221492455336701:50001231000000:2800:E33BBC9176D2AE9E91199EF7322C4C3DAF1F0251BD26ADF0F1032346B40625A2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.31458232409709199464543842879994:50001231000000:2800:A84AB034450ABD1EAC4FBC724380F72695B91E6DB0D64057D3E7B264A818AF9E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.56401369298855453791544692116581:50001231000000:2800:53BB2506E41AAEECD74D041A5D2BF03FB3A6AB2923D179280E2E0526F3CEE1F8.png?needInitFileName=true?needInitFileName=true)
编译HSP模块
如果HSP未开启混淆，则后续HSP被集成使用时，将不会再对HSP包进行混淆。
参考应用内HSP开发指导开发完库模块后，选中模块名，然后通过DevEco Studio菜单栏的Build > Make Module ${libraryName}进行编译构建，生成HSP。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.50095710337221885191728141922929:50001231000000:2800:ED4526DEB4FE3E2A4276A8BA9342A521C1DA22D7A99AC6A3A69FFF3D156D9633.png?needInitFileName=true?needInitFileName=true)
打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到*.har和*.hsp。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.02762797528681012692390373682515:50001231000000:2800:B7106718785559DC795D735A98B23ABC85E2F9FBB3619B12447DF517358A2B72.png?needInitFileName=true?needInitFileName=true)
如需在应用内共享HSP，请将HSP共享包上传至私仓（请参考将三方库发布到 ohpm-repo），请先按以下操作编译生成*.tgz包。
1.
2.  构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150625.42497442750362368240146175165829:50001231000000:2800:FC3936588CA9CB2ED2C13EBC19973D8EC32E50ABAF4A3131DF5AF66E252566CB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150626.10586193391000713404779064353339:50001231000000:2800:703449CD3AC8BC6B0E098F3FC8F7F419840110CE81C84126C764B081C1B2BDA2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150626.83261398122663042317697166717486:50001231000000:2800:43B6D15E1CCB3424FE3BF79913CE3E59F0B29CF1133A914DB8C7927C1C13A30D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150626.30281926554378726309223411443510:50001231000000:2800:0CD08322DE571ADF47241046580E6E0F898E68D1CEFC4323BFFEC12C6D67C265.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-har-publish-V14
爬取时间: 2025-04-30 07:01:48
来源: Huawei Developer
发布打包的HAR，可供其他开发者安装和引用。接下来将介绍如何发布HAR共享包。
OpenHarmony三方库中心仓仅支持HAR共享包发布，不支持HSP共享包发布。如需在应用内共享HSP，可将HSP共享包发布至私仓使用，请参考ohpm私仓搭建工具。
1.
2.
3.
4.
5.
6.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150626.52975898271700235233239223822301:50001231000000:2800:CC741F9271E86227AC2966D6CA0C1ED10C0C0B0E090712E2965EE13F066DD1E2.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-har-import-V14
爬取时间: 2025-04-30 07:02:22
来源: Huawei Developer
引用三方HAR，包括从仓库进行安装、从本地文件夹和本地压缩包中进行安装三种方式。
-  说明：ohpm支持多个仓库地址，采用英文逗号分隔。 依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会安装到该模块的oh_modules目录下。
-  依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会安装到该模块的oh_modules目录下。
-  依赖设置完成后，需要执行ohpm install命令安装依赖包，模块foo的源码会安装在entry模块的oh_modules目录下。
-  依赖设置完成后，需要执行ohpm install命令安装依赖包，模块foo的源码会安装在entry模块的oh_modules目录下。
-  依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会安装到该模块的oh_modules目录下。
-  依赖设置完成后，需要执行ohpm install命令安装依赖包，模块foo的源码会安装在entry模块的oh_modules目录下。
-  代码片段中package.har为三方包文件名；"package"为引用该三方包所使用的依赖名称，建议与三方包包名，即三方包的oh-package.json5文件中的name字段保持一致。 依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会安装在该模块的oh_modules目录下。
-  代码片段中package.har为三方包文件名；"package"为引用该三方包所使用的依赖名称，建议与三方包包名，即三方包的oh-package.json5文件中的name字段保持一致。 依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会安装在该模块的oh_modules目录下。
-  代码片段中package.har为三方包文件名；"package"为引用该三方包所使用的依赖名称，建议与三方包包名，即三方包的oh-package.json5文件中的name字段保持一致。
-  代码片段中package.har为三方包文件名；"package"为引用该三方包所使用的依赖名称，建议与三方包包名，即三方包的oh-package.json5文件中的name字段保持一致。 依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会安装在该模块的oh_modules目录下。
-  代码片段中package.har为三方包文件名；"package"为引用该三方包所使用的依赖名称，建议与三方包包名，即三方包的oh-package.json5文件中的name字段保持一致。
-  代码片段中package.har为三方包文件名；"package"为引用该三方包所使用的依赖名称，建议与三方包包名，即三方包的oh-package.json5文件中的name字段保持一致。
另外，在安装或卸载共享包时，可在模块或工程的oh-package.json5文件中增加钩子设置，以管理install、uninstall命令的生命周期，配置示例如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-tgz-har-migrating-V14
爬取时间: 2025-04-30 07:02:57
来源: Huawei Developer
使用DevEco Studio 3.1 Release之前创建出的、使用npm包管理器的Hvigor工程，构建出的共享包为.tgz格式的HAR包。要将已有的.tgz格式的HAR包转换成使用ohpm包管理器的.har格式的HAR包，需要根据以下的流程手动进行转换：
1.  解压出来的文件会在解压路径的package文件夹中。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150626.69673332985981230659478799081199:50001231000000:2800:8FAD10980F6837447A09A4BE87B754E5DD9FD5AE611DF843C8D4E4A1EAA7F676.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150626.32186208336393762384076297062721:50001231000000:2800:8567E181FB6A64146A9D95DE43A09DCF71059B7CCADCFA094AEE5D1F2D1A3237.png?needInitFileName=true?needInitFileName=true)
转换后.har格式的HAR包可以使用ohpm包管理器进行安装与发布。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-apply-generated-icon-V14
爬取时间: 2025-04-30 07:03:31
来源: Huawei Developer
DevEco Studio支持Image Asset功能，帮助开发者生成适应不同设备、不同屏幕密度的图标，并展示图标在目录中的具体位置。
当前Image Asset功能支持为Phone、Tablet、2in1应用生成单层图标。
Image Asset支持生成以下两种类型图标：
1.  若在模块级目录（Entry或其他模块）下新建Image Asset，将创建Icon and start window icon类型图标，用于在module.json5文件中配置icon及startWindowIcon字段；在工程级目录（AppScope或其他目录）下新建Image Asset，将创建Icon类型图标，生成的图标可配置在app.json5文件的icon字段中。
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150626.40011133179892735981378654759238:50001231000000:2800:06B49E5208E82A03BFD4C29B500F2A673D5D569333A38C027775C5414C774BBE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150626.05076821157105282168251996453063:50001231000000:2800:33E0F4BEE4FA4CEB5BE9BB792C3D464B88F4DCC1F0692543F60EEBD06FEFA712.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150627.17357949088940252627631210665307:50001231000000:2800:B4AF2C9911A0F3A408861D6D0FE6050DE734F7226CB517DAD41A8DE25F8B9219.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150627.13390815691786648033354729505562:50001231000000:2800:D70FF0CE2B3C1603490EA14F7D1CF671773EBDE1169F57BFC9029BF3B7CA2774.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-kit-assistant-V14
爬取时间: 2025-04-30 07:04:06
来源: Huawei Developer
DevEco Studio提供Kit Assistant能力，支持通过拖拽方式将基础的场景化的控件/代码片段插入ArkTS工程中，减少高频场景代码的编写时间。
1.
2.
3.  若当前编辑器打开的文件或所在的模块，存在某些Kit能力不支持的设备类型/API版本/工程模型，或某些Kit能力或控件不支持在元服务工程中使用，则Kit Assistant目录中该Kit能力或控件将置灰并无法成功拖拽。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150627.65735944290922473987816151525152:50001231000000:2800:7CFE94461FA74014AC85EDE6B040840FEE2901E4447E2230C9B17CD0820A9D66.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150627.91587184520478936936803515617455:50001231000000:2800:F5B5A74B65B8B0008B2D299B569CA3DE47ED62F75FDB8BBAE52679554CAA325A.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddevguide-V14
爬取时间: 2025-04-30 07:04:41
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-view-V14
爬取时间: 2025-04-30 07:05:15
来源: Huawei Developer
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181215.94121897801933396578162506444856:50001231000000:2800:A0A4129FE845A3C14938669AF8CDF0682A5FA052F280D55CED3EE67C6D18A27B.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-overview-V14
爬取时间: 2025-04-30 07:05:50
来源: Huawei Developer
什么是端云一体化开发
为丰富HarmonyOS对云端开发的支持、实现端云联动，DevEco Studio以Cloud Foundation Kit（云开发服务）为底座、在传统的“端开发”基础上新增“云开发”能力，开发者在创建工程时选择合适的云开发工程模板，即可在DevEco Studio内同时完成HarmonyOS应用/元服务的端侧与云侧开发，体验端云一体化协同开发。
什么是云开发工程模板
云开发工程模板是为端云一体化开发工程构建的场景化模板，提供了常见场景的代码实现。使用云开发工程模板，您可根据工程向导轻松创建端云一体化开发工程，工程将自动加载模板内预置的代码和资源文件。
DevEco Studio目前预置了通用云开发模板，该模板当前使用Cloud Foundation Kit（云开发服务）搭建了基础的演示项目，不含业务属性。您可参考模板学习如何进行基础的端云工程开发，后续开发时可删除预置的页面代码。
点击此处了解通用云开发模板的更多信息。
端云一体化开发特性
端云一体化开发特性主要包含了如下功能。
| 主要功能  | 说明  |
| --- | --- |
| 端云一体化开发  | 您不仅可以在DevEco Studio中开发应用端侧的业务代码，还可以开发和调试应用云侧的服务代码、并在开发完成后将云侧工程一键部署至AGC云端。  |
| Cloud Foundation Kit  | 云侧工程接入Cloud Foundation Kit，按需为应用提供云函数、云数据库、云存储等云端服务，借助Cloud Foundation Kit开箱即用、一键部署、自动弹性伸缩、免运维等特点助力开发者降本增效。  |
主要功能
说明
端云一体化开发
您不仅可以在DevEco Studio中开发应用端侧的业务代码，还可以开发和调试应用云侧的服务代码、并在开发完成后将云侧工程一键部署至AGC云端。
Cloud Foundation Kit
云侧工程接入Cloud Foundation Kit，按需为应用提供云函数、云数据库、云存储等云端服务，借助Cloud Foundation Kit开箱即用、一键部署、自动弹性伸缩、免运维等特点助力开发者降本增效。
端云一体化开发的优势
相比于传统开发模式，端云一体化开发模式具备成本低、效率高、门槛低等优势，具体区别见下表。
| 区别点  | 传统开发模式  | 端云一体化开发模式  |
| --- | --- | --- |
| 开发工具  | 端侧与云侧各需一套开发工具，云侧需自建服务器，工具成本高。  | DevEco Studio一套开发工具即可支撑端侧与云侧同时开发，无需搭建服务器，工具成本低。  |
| 开发人员  | 端侧与云侧要求不同的开发语言，技能要求高。需多人投入，且开发人员之间需持续、准确沟通，人力与沟通成本高、效率低。  | 依托Cloud Foundation Kit开放的接口，端侧开发人员也能轻松开发云侧代码，大大降低开发门槛。开发人员数量少，降低人力成本，提高沟通效率。  |
| 运维  | 需自行构建运营与运维能力，成本高、负担重。  | 直接接入Cloud Foundation Kit，具有开箱即用、一键部署、自动弹性伸缩、免运维等特点，开发者可聚焦业务逻辑本身，实现降本增效。  |
区别点
传统开发模式
端云一体化开发模式
开发工具
端侧与云侧各需一套开发工具，云侧需自建服务器，工具成本高。
DevEco Studio一套开发工具即可支撑端侧与云侧同时开发，无需搭建服务器，工具成本低。
开发人员
运维
需自行构建运营与运维能力，成本高、负担重。
直接接入Cloud Foundation Kit，具有开箱即用、一键部署、自动弹性伸缩、免运维等特点，开发者可聚焦业务逻辑本身，实现降本增效。
工作原理
DevEco Studio支持开发者在本地完成云侧服务资源的开发与部署，并可在端侧工程中调用您开发的云侧代码，真正实现端云一体化开发。
1.  云侧与端侧工程的代码可并行开发，一般无先后顺序。但若需在端侧代码中调用云侧代码，云侧代码必须先部署到AGC云端，因此建议您先完成云侧代码的开发、调试与部署，再进行端侧代码开发与调试。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180210.95264043636859153775306326923114:50001231000000:2800:F13D62FBCB1609A30B80AAA4A94034AF94809E77C7B242724B2D4ECB3D2C02FD.jpg?needInitFileName=true?needInitFileName=true)
约束与限制
支持的设备
仅支持手机，且不支持使用模拟器运行调试。
支持的国家/地区
当前仅在中国境内（不包含中国香港、中国澳门、中国台湾）提供服务。
支持的签名方式
当前仅支持手动签名。
计费说明
使用端云一体化开发服务时，会开通并使用云函数、云数据库、云存储服务。华为为每个服务都提供了免费额度以供试用，具体的配额明细可以参考各服务的配额说明：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-prerequisite-V14
爬取时间: 2025-04-30 07:06:24
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-account-V14
爬取时间: 2025-04-30 07:06:58
来源: Huawei Developer
您需要拥有华为开发者账号，才能使用端云一体化开发功能。当前仅支持注册地为中国境内（不包含中国香港、中国澳门、中国台湾）的账号。
| 步骤  | 企业  | 个人  |
| --- | --- | --- |
| 1. 注册华为开发者联盟账号  | 注册账号  |
| 2. 实名认证  | 企业开发者实名认证  | 个人开发者实名认证  |
步骤
企业
个人
1. 注册华为开发者联盟账号
注册账号
2. 实名认证
企业开发者实名认证
个人开发者实名认证

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-setup-V14
爬取时间: 2025-04-30 07:07:32
来源: Huawei Developer
基于Cloud Foundation Kit（云开发服务）的端云一体化开发需要使用DevEco Studio NEXT Developer Beta1及以上版本，如果您尚未安装或者安装版本过低，请参考快速开始安装、下载、配置最新版本的DevEco Studio。
端云一体化开发工程在初始化时需要从npm仓库下载依赖，如果需要代理才能访问网络，请配置NPM代理。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-createproject-V14
爬取时间: 2025-04-30 07:08:06
来源: Huawei Developer
创建项目
项目是您在AppGallery Connect（以下简称AGC）资源的组织实体，您可以将一个应用的不同平台版本添加到同一个项目中。当您的应用需要使用华为服务时，您需要在AGC中创建您的项目。
创建HarmonyOS应用/元服务
如果您需要在华为应用市场发布您的HarmonyOS应用/元服务，或者使用AGC提供的各类服务，您需要先在AGC中创建HarmonyOS应用/元服务。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-devprocess-V14
爬取时间: 2025-04-30 07:08:41
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-devproject-V14
爬取时间: 2025-04-30 07:09:15
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-create-appproject-V14
爬取时间: 2025-04-30 07:09:50
来源: Huawei Developer
新建工程
前提条件
选择模板
1.  当前仅支持通用云开发模板（[CloudDev]Empty Ability）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.41211543675811636528708272780111:50001231000000:2800:148EEFD50FA8C373BAD0D5A5563758485D16101E23BF9D36B249851C755334C4.png)
配置工程信息
1.  参数 说明 Project name 工程的名称，由大小写字母、数字和下划线组成。 Bundle name 软件包名称，需保证唯一，且需与您在AGC创建的HarmonyOS应用的“应用包名”一致。 Save location 工程文件本地存储路径，由大小写字母、数字和下划线等组成，不能包含中文字符。 Compatible SDK 兼容的最低API Version。 使用基于Cloud Foundation Kit（云开发服务）的端云一体化开发功能，请选择5.0.0(12)或以上版本。 Module name 模块名称。 Device type 该工程模板支持的设备类型，目前仅支持手机设备。 Enable CloudDev 是否启用云开发。云开发模板默认启用且无法更改。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.34265519889788028691013658517166:50001231000000:2800:3FD304980BECD4821DAA052532EA5EF0545F5D1AA54B6AD6F1A1FC674644D608.png)
| 参数  | 说明  |
| --- | --- |
| Project name  | 工程的名称，由大小写字母、数字和下划线组成。  |
| Bundle name  | 软件包名称，需保证唯一，且需与您在AGC创建的HarmonyOS应用的“应用包名”一致。  |
| Save location  | 工程文件本地存储路径，由大小写字母、数字和下划线等组成，不能包含中文字符。  |
| Compatible SDK  | 兼容的最低API Version。 使用基于Cloud Foundation Kit（云开发服务）的端云一体化开发功能，请选择5.0.0(12)或以上版本。  |
| Module name  | 模块名称。  |
| Device type  | 该工程模板支持的设备类型，目前仅支持手机设备。  |
| Enable CloudDev  | 是否启用云开发。云开发模板默认启用且无法更改。  |
关联云开发资源
为工程关联云开发所需的资源，即将您账号团队在AGC创建的同包名应用关联到当前工程。具体操作如下：
1.  登录成功后，界面将展示账号昵称。
2.
3.  选中团队后，系统根据工程Bundle name在该团队中自动查询AGC上的同包名应用。 完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。
4.
5.
6.
7.
8.  完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。
9.  只有账号持有者和法务角色才有权限签署协议。
10.  若云侧执行“npm install”失败，请排查是否尚未配置npm运行环境。
11.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.35033649656542118610733224824288:50001231000000:2800:B051A630AD3F93B276EFA4A51CC02CEED7C5D23766186EAF059AC2EE4B881F72.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.07113227745833930334180095490285:50001231000000:2800:0107D4303553B0F782D8A76F95D61A7399C6D21422BBB0CE04757C21B8EBC0BA.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.00128863439168056318693571045377:50001231000000:2800:E47495EBD6C53BC8D0DAAE8FC19340405256C85BD6EE6E040E640166D70AFB05.png)
-
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.71333259708457162051310071485437:50001231000000:2800:2A2DAE9A4158A2F4033FCDE8A2A8E7D4D5080E5A15F87BE8CB7174B577D8DF24.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.29658066321360968850953295865404:50001231000000:2800:E769359A711B290B2CA7EDDAE47D9B6E89A54CB08A8BE397D3721D4E7F1016AB.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.67279256192907317896659131592990:50001231000000:2800:50971B1451108D9BE28E37ACFDA107E4981A17719F4AA03907C606631AA187E8.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.47297387119822940737805686237553:50001231000000:2800:C1710FF1C54514D87A69FF7A10F25BFB01B06C9E69D7E5D504B498809D93C99E.png)
-  完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.51894062198489698967769919446922:50001231000000:2800:A898DFB1CAE33DE4914F138C3A7EEB851876D578BA12CA2E4E123DCA64ADB175.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.35614202265193906245907356956554:50001231000000:2800:1BE917936E36EFA386F64A29F3630FFDA1FBF6940C9AEE6E31C420414AFE9940.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143410.49375202545813931581466797786939:50001231000000:2800:9C518A2F050426ABA8B04174691F7E5E7EE4E1D7605345F978B19F0E890BC4E0.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.81867096310412837518519723919930:50001231000000:2800:88FC0770D3B6427D54AF784A3AFFF985E76A31EC5128A5BE16E8A051F8B2A9C8.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.26460206232620608711099123953920:50001231000000:2800:14B66E103F4D3C332E2C27CC25DED685E6EEA7FF4E2AE77E7CBA5B38C67E253A.png)
工程初始化配置
当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。
自动开通云开发服务
DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。
端云一体化开发工程目录结构
端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。
端开发工程（Application）
端开发工程主要用于开发应用端侧的业务代码，通用云开发模板的端开发工程目录结构如下图所示。“Application/cloud_objects”模块用于存放云对象的端侧调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见工程目录结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.09447437843549993301757867867211:50001231000000:2800:7941130DFC0514DB70080288641CA879C8D6EBF68A38C9FF2D83569C02110983.png)
云开发工程（CloudProgram）
在云开发工程中，您可为您的应用开发云端代码，包括云函数和云数据库服务代码。通用云开发模板的云开发工程目录结构如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.71851931496019825111065558344665:50001231000000:2800:2F3B62A44FDC70AB619C4B3AE0F10D3D4167D25796AD370023A40FF38A66C68B.png)
-  该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。 该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.15527408872421303840205957662837:50001231000000:2800:96487DA04FAB30162C3DD45A1E69779AD3357685C653E374966CF4B8B18E428B.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.70733086128262388541614714054972:50001231000000:2800:5E82337FFF8B69EC736CB6EBD7915888597F94528786EBFF93F164CBDAEBA187.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.29921596887994095989704185940270:50001231000000:2800:90355E85E6B46B85F9525C510780305865E476BC787951E560BB2734A55958E1.png)
（可选）AGC应用管理
从DevEco Studio补充创建同包名应用
如创建工程时，发现尚未在AGC控制台创建与工程包名相同的应用，可进行补充创建。
1.
2.  参数 说明 应用类型 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。 应用名称 应用在华为应用市场详情页展示的名称。 应用包名 从DevEco Studio中带入自动填充，且不可更改。 应用分类 请选择普通应用或游戏类应用。 应用分类设置后不支持修改，请谨慎选择。
3.
4.  启用的数据处理位置必须包含中国站点。
5.  启用的数据处理位置必须包含中国站点。
6.
7.  启用的数据处理位置必须包含中国站点。
8.
9.
10.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.53948901704198409473752524453745:50001231000000:2800:2CAD951EDB774F1620451C45D206DE58E5A071560F77985894594770A5753E4C.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.57718253191773206713933864062466:50001231000000:2800:EA0773FB521BE1ED564538626B0940D2682EEF6B88B168647B7307FAE16D309C.png)
| 参数  | 说明  |
| --- | --- |
| 应用类型  | 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。  |
| 应用名称  | 应用在华为应用市场详情页展示的名称。  |
| 应用包名  | 从DevEco Studio中带入自动填充，且不可更改。  |
| 应用分类  | 请选择普通应用或游戏类应用。 说明应用分类设置后不支持修改，请谨慎选择。   |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.22936833361178471864926269097736:50001231000000:2800:A426B9C339EA25D4C45A41BCF8577CAD3FB11590B9F5F13404D2990C49AF1F94.png)
-  启用的数据处理位置必须包含中国站点。
-
-  启用的数据处理位置必须包含中国站点。
-
1.
2.  启用的数据处理位置必须包含中国站点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.45477131097380586707149865055973:50001231000000:2800:750256E295A5E69378AB58B08CF8C9A4A7C6C05E5D9C6A23AFAEC77A9CD44F1F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.39969628004262785729327217284308:50001231000000:2800:F7AEECC21B0BF4C238A85FA33F25FC13F2B192926046BF66DA79AB29A090F1B3.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143411.44569231889543283871122668260405:50001231000000:2800:C9685E7D9646FEC2F92D3352E3ED6822E4F47A5570DB74E6CEF5BF0E105C52EE.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.27521852260261351314114042036211:50001231000000:2800:BC2F476C791DF87246FA6ED6CEABAEA5F731C45E3B04201256104C81CBB0EBEC.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.54847095415470531273014153031751:50001231000000:2800:25B790797E8FABF9FF5199422373B4B5307ACEDE745D3AFBAC8B74DE7055B9DC.png)
将游离应用添加到AGC项目下
游离应用指未关联任何AGC项目的应用。创建工程时，如需要关联的AGC应用为游离应用，则您需要将该应用添加到您的AGC项目下。
应用与项目的关联关系一旦创建则无法再修改，请谨慎操作。
1.
2.
3.  如选择了已有项目，则忽略此步骤。
4.  启用的数据处理位置必须包含中国站点。
5.  启用的数据处理位置必须包含中国站点。
6.
7.  启用的数据处理位置必须包含中国站点。
8.
9.
10.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.39953598703861411535024935776760:50001231000000:2800:B133F52398AE54CDEB908830C9B4D98E966976A1AE44D4B6625BE7E235F04422.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.89892893724693687372401765717062:50001231000000:2800:B877F3110FEA0FB96C1D28943DCD07F3DDF2D41F27F6BE5F19C492266D85B82F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.16810084804566736976263509165178:50001231000000:2800:3E49BBC498D8E467664761D2F360492963A7067D03C0AB5BC8CAAA9A56008F0C.png)
-  启用的数据处理位置必须包含中国站点。
-
-  启用的数据处理位置必须包含中国站点。
-
1.
2.  启用的数据处理位置必须包含中国站点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.05642559718007705454589362737749:50001231000000:2800:87E717168D9772542ED4080EE1E61FF3A7618D41EFFE5153364E3DA736EE3C07.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.96254097557784926821717913691356:50001231000000:2800:39D088E3B570D1BFB895224F2DEFA00D1B0D9193830734D2F4A10602558793C5.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.38495272446353119987800640207502:50001231000000:2800:95DCDDC95A63D1BC93A9779B52F0D67F0A6FBA67AE2F842FB6B182594F05A767.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.91229736368099630010780653475238:50001231000000:2800:D38EADEF4D8360039FC166C15AD8084900360EBD1BADC4D82E116083BC1FF256.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.00956690541721280046405678859626:50001231000000:2800:7F2368E0F52FA2B8A891A399BAB2E11DACDC7C303477D8D5E14D747D8305001E.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-create-faproject-V14
爬取时间: 2025-04-30 07:10:24
来源: Huawei Developer
新建工程
前提条件
选择模板
1.  当前仅支持通用云开发模板（[CloudDev]Empty Ability）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.70821827345393694383540830727166:50001231000000:2800:584EDC3F0A808602DD29769C54151DC2105D8C71CA1C6936BF769A5840058F77.png)
关联云开发资源
为工程关联云开发所需的资源，即将您账号团队在AGC创建的元服务关联到待创建工程。具体操作如下：
1.  登录成功后，界面将展示账号昵称。
2.  元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。 创建成功后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，选择新生成的APP ID，点击“Next”即可。
3.  元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。
4.  创建成功后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，选择新生成的APP ID，点击“Next”即可。
5.
6.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.76554801103111491271708503423750:50001231000000:2800:211E3FA377CCCC6FD5B247D608C959029C9D9EFD25A6A8EA6FD2B8F6EA102619.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143412.35915736313350898660091141814150:50001231000000:2800:0ADFD0247206D5F755BD6A50C7FA472934B32C187617213613D7374B0D8E92F3.png)
-  元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.75292837195708070238730174520256:50001231000000:2800:7422DFECB773F24F2E814BDD1FB196DF3E429452CAA32E458EDF01F08DF116EF.png)
-  创建成功后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，选择新生成的APP ID，点击“Next”即可。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.55777155378262042510830018882245:50001231000000:2800:3F14E1FE11CDC79DF52717A5A030C9523B484D4B5DE001DE52E0161420218B7D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.90006489757000853349995784652400:50001231000000:2800:F137E0DDFDBE5B897E45A7F5050951A08EC41467993D3DF51E3F24E232EA58C6.png)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.24945825991204101993325584427208:50001231000000:2800:A76AE6E2E7229965EF7C13570447126738FDE7A6BDDE02D87369743D2D144E8E.png)
配置工程信息
1.  参数 说明 Project name 工程的名称，由大小写字母、数字和下划线组成。 Bundle name 创建元服务时自动生成，不支持手动修改。 Save location 工程文件本地存储路径，由大小写字母、数字和下划线等组成，不能包含中文字符。 Compatible SDK 兼容的最低API Version。 元服务使用基于Cloud Foundation Kit（云开发服务）的端云一体化开发功能，请选择5.0.0(12)或以上版本。 Module name 模块名称。 Device type 该工程模板支持的设备类型，目前仅支持手机设备。 Enable CloudDev 是否启用云开发。云开发模板默认启用且无法更改。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.22157561137022087241542263043659:50001231000000:2800:55D3BA30609298FD5B286B35B6A47C41BC4A635FB04A1024E41CD78AF2330CE2.png)
| 参数  | 说明  |
| --- | --- |
| Project name  | 工程的名称，由大小写字母、数字和下划线组成。  |
| Bundle name  | 创建元服务时自动生成，不支持手动修改。  |
| Save location  | 工程文件本地存储路径，由大小写字母、数字和下划线等组成，不能包含中文字符。  |
| Compatible SDK  | 兼容的最低API Version。 元服务使用基于Cloud Foundation Kit（云开发服务）的端云一体化开发功能，请选择5.0.0(12)或以上版本。  |
| Module name  | 模块名称。  |
| Device type  | 该工程模板支持的设备类型，目前仅支持手机设备。  |
| Enable CloudDev  | 是否启用云开发。云开发模板默认启用且无法更改。  |
1.  若云侧执行“npm install”失败，请排查是否尚未配置npm运行环境。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.22059711672705214239983468136951:50001231000000:2800:286A8EF98D76F6AC0BC112670D1B17D15F4E7464D8EB815DB9D8D95B41A6170C.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.46724718636120749183422192037111:50001231000000:2800:F8B8CD52E73E24C68792EF691B3E247182336DD3F7C24AC1BAE0F0DABDD6D963.png)
工程初始化配置
当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。
自动开通云开发服务
DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。
端云一体化开发工程目录结构
端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。
端开发工程（Application）
端开发工程主要用于开发应用端侧的业务代码，通用云开发模板的端开发工程目录结构如下图所示。“Application/cloud_objects”模块用于存放云对象的调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见工程目录结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.89245084404135394901193050752347:50001231000000:2800:B56CCCC0DC92B39DC68C7825A64D1B752A3AC8C4EB9C87AE13D0C0F088004519.png)
云开发工程（CloudProgram）
在云开发工程中，您可为您的元服务开发云端代码，包括云函数和云数据库服务代码。通用云开发模板的云开发工程目录结构如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.92256425991162444579035098763243:50001231000000:2800:1ED2B929F6960FF21590E5F92446F5E055B04E07EE4BC0F5C4D41A969B853D55.png)
-  该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。 该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。
-  该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.95611323276469034262230664995532:50001231000000:2800:050502488ACC8C7246BB4F706081B9E3D53C57285C3ECA5B2EDA36F209E918E5.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.93268190423806534403018062121899:50001231000000:2800:A24CA1EEA05F03134563537D280832B4B63D1C566D07339D86D0413921030E20.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143413.66045459433924860915739447448455:50001231000000:2800:E7C0507E6B06AADC8120EAD7C807F84648CAAC93234B20E832B2FD7D41476655.png)
（可选）AGC元服务管理
从DevEco Studio补充创建元服务
如创建元服务工程时，发现尚未在AGC控制台创建对应的元服务，可直接从DevEco Studio进行补充创建。
1.
2.  元服务包名会在元服务创建成功后自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。 参数 说明 应用类型 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。 应用名称 元服务在华为应用市场详情页展示的名称。 应用分类 元服务仅支持“应用”类型。 应用分类设置后不支持修改，请谨慎选择。
3.
4.  启用的数据处理位置必须包含中国站点。
5.  启用的数据处理位置必须包含中国站点。
6.
7.  启用的数据处理位置必须包含中国站点。
8.
9.
10.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.23422778040293394008429538945759:50001231000000:2800:1FF198AA9A50B095AFECA47437536D3208B60A5E13D1B881C8708DFC2E6B19A4.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.42835674146072958943464504230684:50001231000000:2800:70C43874E5A1271685FD9CD37714DA0635A16284BB8CB6FC35F5BD8215B79B02.png)
| 参数  | 说明  |
| --- | --- |
| 应用类型  | 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。  |
| 应用名称  | 元服务在华为应用市场详情页展示的名称。  |
| 应用分类  | 元服务仅支持“应用”类型。 说明应用分类设置后不支持修改，请谨慎选择。   |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.28504311531393217573925040580162:50001231000000:2800:99944B4B0AC39DCC5BE5A211A2111A255E17CDAF2FF404FBC6ECBDE4208D4F9D.png)
-  启用的数据处理位置必须包含中国站点。
-
-  启用的数据处理位置必须包含中国站点。
-
1.
2.  启用的数据处理位置必须包含中国站点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.33373262914033849627999418786135:50001231000000:2800:2DD279057916FE89FAB1598924655B55023AE47C0E5544073C9FA0A2E72D72B1.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.42127285908057880054786258994117:50001231000000:2800:2CB48247E260CB3E375B11A78298746E8902CBFE93D7793B0EAD66E5C44E648C.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.71835070894218080674710755039618:50001231000000:2800:0963A676701B188260F19C1381CB4E82465B3B309A4FCEACDA325B0DBE486242.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.17687182351852893255153680004126:50001231000000:2800:1D11884C821B5F19364CAFFB4CB1B08F2DE8C79528AA0061B105254665E2BD5B.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.36141865192181603716948997662724:50001231000000:2800:217F43D3FA58C061EACE8976E186DFF870EE174823B6017130E1464A36A9A9CA.png)
将游离元服务添加到AGC项目下
游离元服务指未关联任何AGC项目的元服务。创建工程时，如需要关联的AGC元服务为游离状态，则您需要将该元服务添加到您的AGC项目下。
元服务与项目的关联关系一旦创建则无法再修改，请谨慎操作。
1.
2.
3.  如选择了已有项目，则忽略此步骤。
4.  启用的数据处理位置必须包含中国站点。
5.  启用的数据处理位置必须包含中国站点。
6.
7.  启用的数据处理位置必须包含中国站点。
8.
9.
10.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.90641564649958935197785712862060:50001231000000:2800:57FD73258F432292F19F1DB90D954E3C49474A99582AC3DB213E66B1B546B564.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.73231184347484011299717319127519:50001231000000:2800:7D8192795913BB8166CFA9E697C95D343DCEBA7832A6C1780E239E4CB7A50082.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.66281567745970465539976435311796:50001231000000:2800:803F1F839741EA3B4622414BEED361B2D3D24113C19F8FADED4242FC9CFE9BCE.png)
-  启用的数据处理位置必须包含中国站点。
-
-  启用的数据处理位置必须包含中国站点。
-
1.
2.  启用的数据处理位置必须包含中国站点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.55287009734029505356385133054230:50001231000000:2800:6B3BE995A463143419C0FF49E8E022B1094BDC11E2CFA6D5C6E212D2977C0D5D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143414.12016537990335822192612955659819:50001231000000:2800:E71143726A5C3FCF758902093A24A9CB80406248E688355DD673B656741E7F04.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143415.06573084026263439583680499184865:50001231000000:2800:45C77FCEBEC2ABB3A19612EE1759511C519FA181504713C01FB36EFA5933F582.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143415.60242466157013409785220102789098:50001231000000:2800:7E2C6C3E9273D25EA093E94025D314E5E1BD6D17EB60CA1E850BA659DC6621D5.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250407143415.03216290030121582918458083381980:50001231000000:2800:85B1E892586AD306A8ADA493F571C2FE218EC6E4743ED023BFC7F237A2D7C6B4.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-project-migration-V14
爬取时间: 2025-04-30 07:10:59
来源: Huawei Developer
如您此前已经创建了非端云一体化开发工程，希望直接转换为端云一体化开发工程，可执行如下操作：
DevEco Studio NEXT Beta1版本之前的非端云一体化历史工程，在转换前需先进行一体化工程迁移。
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150633.75570794473473590723010260163812:50001231000000:2800:A9D113E727D47A152ACFC45941612FC60B3EB0097727169FF912D665D544E7E0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150633.02983853841059904880030091881650:50001231000000:2800:DDC0B96ADC5462F7EB592D75C510616A0467CE1792F30A70EEF950E485F8C7DE.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-develop-V14
爬取时间: 2025-04-30 07:11:33
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-cloudfunctions-V14
爬取时间: 2025-04-30 07:12:08
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-functionprocess-V14
爬取时间: 2025-04-30 07:12:42
来源: Huawei Developer
云函数是一项Serverless计算服务，可以根据函数的实际流量对函数进行弹性收缩。您只需聚焦业务逻辑，开发与上传业务模块相关的函数，云函数即可为您自动完成资源分配、代码部署、负载均衡等工作，既提高了开发和上线函数的速度，也保证了函数的高可用性。
云函数当前分为传统云函数和云对象两种类型，本章节仅介绍传统云函数，了解云对象详情请参考开发云对象。
使用DevEco Studio在端云一体化云侧工程下开发云函数，总体流程如下。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.86150571182600034038978551998063:50001231000000:2800:2EFEC44BF1146D178DB8B47B90D9D695CA215CCAC742D643CBDD9CBB5DC59399.png?needInitFileName=true?needInitFileName=true)
一般建议先将函数调试无误后再部署至云端，但某些业务场景下需要先部署函数才能进行调试。请根据实际业务需要操作。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-createfunc-V14
爬取时间: 2025-04-30 07:13:17
来源: Huawei Developer
您可直接在DevEco Studio创建函数、为函数配置调用的触发器等。
创建函数
1.
2.  函数名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。 “cloudfunctions”目录下生成新建的“my-cloud-function”函数目录，目录下主要包含如下文件：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.50641263684170709285352422962492:50001231000000:2800:DAFA7A79EB0C2CF015C7E64088618E800681AD7DD2E1DAE84EA34ED0224AC4B8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.05307109752893505457889551101315:50001231000000:2800:03FD77AA7FA274DED187BD61DFC379CB7614FFDF95E5EB0BDA61EF1539304A85.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.94687428526943816240588071231680:50001231000000:2800:333F9ADC9CFDC2F4BCD3C67EAB1C8EF53F46166150E424EA425F6DF94E397899.png?needInitFileName=true?needInitFileName=true)
配置函数
函数创建完毕后，您可在配置文件“function-config.json”的“triggers”下配置触发器，通过触发器暴露的触发条件来实现函数调用。
“functionType”表示函数类型，“0”表示云函数，“1”表示云对象。“functionType”的值为创建时自动生成，不可手动修改，否则将导致云函数部署失败。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.48946465605783189111621485646820:50001231000000:2800:3700BBF012DB879560F61E4823374002F33D9FCEDD3992CBF4FE5A14A21EBCA5.png?needInitFileName=true?needInitFileName=true)
云函数当前仅支持HTTP触发器， “function-config.json”文件中已为您自动完成HTTP触发器配置。配置了HTTP触发器的函数被部署到云端后，您的应用即可通过Cloud Foundation Kit调用函数。关于如何使用HTTP触发器调用函数，请参见调用函数。
如您需在函数部署完成后更新触发器，请先删除之前的触发器配置，再添加新的触发器配置，否则您的更新将不生效。
-  参数 说明 enableUrlDecode 通过HTTP触发器触发函数时，对于contentType为“application/x-www-form-urlencoded”的触发请求，是否使用URLDecoder对请求body进行解码再转发到函数中。 authFlag 是否鉴权，默认为true。 authAlgor 鉴权算法，默认为HDA-SYSTEM。 authType HTTP触发器的认证类型。
| 参数  | 说明  |
| --- | --- |
| enableUrlDecode  | 通过HTTP触发器触发函数时，对于contentType为“application/x-www-form-urlencoded”的触发请求，是否使用URLDecoder对请求body进行解码再转发到函数中。 true：启用。false：不启用。  |
| authFlag  | 是否鉴权，默认为true。  |
| authAlgor  | 鉴权算法，默认为HDA-SYSTEM。  |
| authType  | HTTP触发器的认证类型。 apigw-client：端侧网关认证，适用于来自APP客户端侧（即本地应用或者项目）的函数调用。cloudgw-client：云侧网关认证，适用于来自APP服务器侧（即云函数）的函数调用。  |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-funccoding-V14
爬取时间: 2025-04-30 07:13:51
来源: Huawei Developer
函数创建并配置完成后，您便可以开始编写函数业务代码了。
1.  此处我们以函数“my-cloud-function”为例，构造一个用于返回时间戳的函数。 云函数与云函数之间是相互独立的，部署至云侧时，只会部署所选云函数目录下的文件，不可在一个云函数中通过import '../anotherDirectory/xxx'的方式引入依赖。如果有多个云函数公共的配置，建议存储在云数据库中，通过云数据库Server API类查询出公共配置；也可以将多个云函数整合成一个云对象，将公共配置变成云对象的私有配置。
1.  右击“package.json”文件，选择“Run 'npm install'”菜单，也可以实现依赖包安装。 所有安装的依赖包都会存储在当前函数的“node_modules”目录下。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.34071718236067610885636419421209:50001231000000:2800:9D0D7F72BA2BCCE29B507D442F8E12558F5DAA3B2CCC5CD4355EF932E1D96265.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.12568940612488471546381252128746:50001231000000:2800:CA1689AF73ED0AF614653A94D475FD060AC6C8863C9AD7EADEDF81EB8485F99D.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-debugfunc-V14
爬取时间: 2025-04-30 07:14:26
来源: Huawei Developer
函数开发完成后，您可以对函数进行调试，以验证函数代码运行是否正常。
目前DevEco Studio函数调试支持本地调用和远程调用，请根据实际场景选择使用：
前提条件
通过本地调用方式调试函数
您可在DevEco Studio调试本地开发好的函数，支持单个调试和批量调试，并支持Run和Debug两种模式。
下文以Debug模式下调试单个函数“my-cloud-function”为例，介绍如何在DevEco Studio调试本地函数。
1.
2.
3.  设置断点后，调试能够在断点处中断，并高亮显示该行。
4.
5.
6.  点击右上角可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。
7.  “Result”框右侧的“Logs”面板仅供通过远程调用方式调试函数时使用。
8.  如下图，函数“my-cloud-function”配置了环境变量“env1”，可成功访问环境变量“env1”的值“value1”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.22835513785678150633841141534165:50001231000000:2800:54200E6B8813989AE27F59DA3C0276C05918807825F371C8DD76FAB7E908A5D4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.88809921660975246266060398980257:50001231000000:2800:C469F072A95DE37C61CC6D3837FD2E47DB237619BA05784A41E7B31ACCA41626.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.24060719732761371368857083998690:50001231000000:2800:E5C6466341D355E0F1628C8D6FAA1E496A1FED6D6D7FD9B892112A8DA01E82A1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150634.67950735820431177047343322400953:50001231000000:2800:0A606B4F0D5E200C11E4D870CCC23C1E957CFE3636068E5458EBF8A96F6B1BA2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.60298752885610924292862561495473:50001231000000:2800:BA510A2CDF26A978608B89FEC47C212E735F9547F67B616EA20CC5C07C159C14.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.88626520478512469368258553349799:50001231000000:2800:67D2C4ECE5BD7511C9418B751D6F82E0B9891E60474F14BD741FFA30FE0C942A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.76437183120555868166397706253369:50001231000000:2800:2FE1DAEDBB2932BED4271AC7AD3F1434F51713427F56CB82AB405EC8A648239C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.50617701756088380609090704418612:50001231000000:2800:227E0C01466EC538F4D0945BD9D0DEB11827A793C0571031FC78A1DDF71914E1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.68610935102291824575090003196689:50001231000000:2800:4A8C546FBB80C3F39AA6BEA034DB80ECF09B7EBBED50C7CB58B1B1198CF1A512.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.77581738074843104671036484871112:50001231000000:2800:EE884C7866F3DBCDB516B268EC60A5BEE7AA376BAA09C7C0B308BE7BE66CA5F8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.09818301933319190970079947749763:50001231000000:2800:3E596068B28E152347680C98EC98880CE10EB437B53A99D7DBB9185BB531FB27.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.16815950733493355905851848475888:50001231000000:2800:BB0B09C7AC900C6544E4C3CDB94E11CF9BE7B553AC12DD0D6FD10218240176B6.png?needInitFileName=true?needInitFileName=true)
通过远程调用方式调试函数
您还可以将函数部署至AGC云端，然后在DevEco Studio调用云端函数，以测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。
1.
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.58730782744600881550132848651598:50001231000000:2800:37FD1B4D5A7684A4836F7C230EC1539902E80571785A17EB720B20E8C84F33D8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.36575250700716075765644936009318:50001231000000:2800:1924F4614C64BDA69A0510F32D27BDD2701E18B7FC51D2D13C2A9775DAC0BB31.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.76735193790260212358394177363298:50001231000000:2800:66C08FE496291B3F0CFAB8451C511ABD586BB85B50B0AD8DA08ABC079BB1E3EB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.84152458479939278705681993797629:50001231000000:2800:6F4808BD25098C3EA0932672969A136D315ED42EA1AB68B728AC2E4BEC155543.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.30333178791550956865047336913302:50001231000000:2800:5DA5F03432CE970FE355BC2AB5872E69B2022D1DD9E4312803030F8AC95B7534.png?needInitFileName=true?needInitFileName=true)
（可选）自定义Run/Debug配置
直接启动函数调试采用的是默认的Run/Debug配置。如有特殊需求，您也可使用自定义Run/Debug配置项来进行调试。
1.
2.
3.  如当前暂不使用自定义配置，可点击“OK”保存配置。后续有需要时再选择自定义配置，分别点击或进行Run或Debug。 点击“Edit environment variables”按钮，在“Environment Variables”弹窗中点击“+”添加一个环境变量，然后点击“OK”。添加成功后，您便可以将变量配置信息传入到函数执行环境中，用于函数运行时读取。
4.  点击“Edit environment variables”按钮，在“Environment Variables”弹窗中点击“+”添加一个环境变量，然后点击“OK”。添加成功后，您便可以将变量配置信息传入到函数执行环境中，用于函数运行时读取。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.34501876782993680670789594500899:50001231000000:2800:A9416BD99C016E56DD6FCB03D97119CAEBE4666BCA2334E9CAC41FF65461075A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.70317256164086419070476321485253:50001231000000:2800:BC56B37A41C5D8BD7FAA763312ADA1B31FBA15B75A45E422E522DBA95737A8BD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150635.65061042497830223500442033778863:50001231000000:2800:0CDDB7B17410A92E3BB7EF850640EEE27CDA32B25E11CFAA80303BDB444F2C0E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.52696407280770227524629960671332:50001231000000:2800:67809B630B2E422CE3BA69E39B67CF12895BF9C2AA9150A44984EB6D002CCC37.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.01853859187194076788283678364776:50001231000000:2800:5312E52FE90AF1C18446C53FB012AD5CFAB576BEBDC2836A5D1101EB5A6C458D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.83021875561102975434636668634046:50001231000000:2800:BEC8782D7672B99B6DB74650D7C0886E519734C18C5BC80A3E029339D2A45ACF.png?needInitFileName=true?needInitFileName=true)
-  点击“Edit environment variables”按钮，在“Environment Variables”弹窗中点击“+”添加一个环境变量，然后点击“OK”。添加成功后，您便可以将变量配置信息传入到函数执行环境中，用于函数运行时读取。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.03233463682350782662772584093174:50001231000000:2800:D1D31558F59D386338694AEACC1BCD824342A8BFF0039C2FEEC0FED0BD974D6D.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-deployfunc-V14
爬取时间: 2025-04-30 07:15:00
来源: Huawei Developer
完成函数代码开发后，您可将函数部署到AGC云端，支持单个部署和批量部署。
单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到AGC云端。
下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。
1.  如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到AGC云端。
2.  请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。
3.
4.
5.  部署成功后，您便可以从端侧调用云函数了，具体请参见在端侧调用云函数。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.13527535401396169861281057954234:50001231000000:2800:7C4E4DAC4C7ED9146ADC67BB63F8E47212A15019BD9EA74C2E2CB1281657C401.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.43459826685153001448922399909517:50001231000000:2800:279A07A7BC6A2C1E06E5B475A2B75EF56DB94A1C2FCA5D6E0A676785EE4A0D12.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.93390299416650967444310147023547:50001231000000:2800:4A0DDF86FCCA728F9DC487655EE374821605BA893BD863231E42050F5196C5E7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.70355807026356194612227872829713:50001231000000:2800:DD83495A782BD6374B6B9F31143DB1CD72C85369EA05BE0FAFA42BF7E5482784.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.30925820587940673390302748691087:50001231000000:2800:1056CCF025D0D9439CAFC2549B5C62034FC5ABD64B4369FC41A5DFE70B018A37.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-cloudobj-V14
爬取时间: 2025-04-30 07:15:35
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-cloudobjprocess-V14
爬取时间: 2025-04-30 07:16:10
来源: Huawei Developer
除去传统的云函数，您还可在端云一体化云侧工程下开发云对象。云对象是一种特殊的云函数，本质是对云函数的一种封装，客户端可通过导入一个云对象来直接使用这个对象的方法，为您提供在端侧直接调用云侧代码的开发体验。相对普通云函数方式，云对象代码更精简、逻辑更清晰，大多数场景下推荐使用云对象代替传统云函数。开发流程大致如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.20142112538576670179503746432405:50001231000000:2800:1A644A2E0AA9CE0F0CA2CC09EB5769E1C73C3A91935F6306004E79BB0AF55EC1.png?needInitFileName=true?needInitFileName=true)
一般建议先将云对象调试无误后再部署至云端，但某些业务场景下需要先部署云对象才能进行调试。请根据实际业务需要操作。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-createcloudobj-V14
爬取时间: 2025-04-30 07:16:44
来源: Huawei Developer
首先您需要在云侧工程下创建云对象。
1.
2.  与云函数名一样，云对象名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。 云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。
3.  云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150636.00445948687394081509148596382930:50001231000000:2800:442C16B271F74DE11528D6D16E9BA87FA1A90EB1ADB50B0A689DF30EC1B3AE2B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150637.96609129424126651309128414484417:50001231000000:2800:A075238B0F55986DC7DC18EE07300080AEE65CE5DFA56B591B37985F18E22864.png?needInitFileName=true?needInitFileName=true)
-  云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150637.67446784359090142061027179517855:50001231000000:2800:0669E7C44B52A0C9D645821E2CAF54A5E03C70F2A1D69D6AB1FBCDB127B28B24.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150637.74208992006574937223355111260369:50001231000000:2800:6CDC4B47190A8A5FED0A057A634119047CD9BC41CFB7B263184CC1B9483BC64A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150637.48874613012244703417713642396269:50001231000000:2800:A0A5BDDF630A9ECC9B8387EA4DD00A0ACDA49169151F4EFBB7CFB97DE8792CA4.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-cloudobj-coding-V14
爬取时间: 2025-04-30 07:17:19
来源: Huawei Developer
云对象创建完成后，您便可以直接在云对象中编写需要实现的方法。例如，通过云对象实现add与subtract两个方法。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150637.60280210960547961373064742657587:50001231000000:2800:128FA984D65C5DCEBA68D6D8CD74C6874F707F5E8FD61165A60AFFD6B29EF530.png?needInitFileName=true?needInitFileName=true)
1.  右击“package.json”文件，选择“Run 'npm install'”菜单，也可以实现依赖包安装。 所有安装的依赖包都会存储在当前云对象的“node_modules”目录下。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150637.40587022574602893519667813874827:50001231000000:2800:A592EA84FCFFD0A44EE12AC34987177D7F073CC74D8061748422895D3EDBAA16.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150637.04941503730369814692665849502525:50001231000000:2800:12684E2F1FEC70C4446AE0A2965A6F19673476CC9EF1354407DF9A960D131953.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-debugcloudobj-V14
爬取时间: 2025-04-30 07:17:53
来源: Huawei Developer
云对象开发完成后，您可以对其进行调试，以验证云对象代码运行是否正常。
目前DevEco Studio云对象调试支持本地调用和远程调用，请根据实际场景选择使用：
前提条件
通过本地调用方式调试云对象
您可在DevEco Studio调试本地开发好的云对象，支持单个调试和批量调试，并支持Run和Debug两种模式。
下文以Debug模式下调试单个云对象“my-cloud-object”为例，介绍如何在DevEco Studio调试本地云对象。
1.
2.
3.  设置断点后，调试能够在断点处中断，并高亮显示该行。
4.
5.  如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号'['，外层的方括号表示参数列表。
6.  如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号'['，外层的方括号表示参数列表。
7.  点击右上角可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。
8.  “Result”框右侧的“Logs”面板仅供通过远程调用方式调试云对象时使用。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180215.58504026825891451782835412311446:50001231000000:2800:22390ED296226D44A0FBBB2741BCAB5D67486B6F8B1DB99EEAB5BCA51C6F3DD3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180215.38324409943848324156495422252241:50001231000000:2800:81F6DD6D383DE3EB27155000ED83DD4D98622BD77A104EB81269C6D6EB2EED01.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180215.19768688783550807385010359518634:50001231000000:2800:0FB751C69E464E23CF164F35255AE9806C889B99E8087223EE5A61E7AA585D36.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180215.32237189898595853018512332068875:50001231000000:2800:C89369631641BF71F2F6CC143A38BFBD76C5953C46FC8485061E062578C3D994.png?needInitFileName=true?needInitFileName=true)
-  如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号'['，外层的方括号表示参数列表。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180215.04675553617086984920925860000096:50001231000000:2800:D22C05EE6A0CD003BE2F23AF4F10B435B4DCAF7340FE72D502169A82A896CBA1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180215.23415994888341760743255391730751:50001231000000:2800:8E75C024F3700089D7FCA25A2307334F19351AE365BD17B5F9705F8744D2C21F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.60011605229944737519003438397999:50001231000000:2800:E6BFCB1DE0D2DB833FF7C996F02404C766EABE5D13D7C9A4174B1E42E0F8A114.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.99020904967789460287659869778571:50001231000000:2800:EE02A113E786E3CBB012A47DDC37B871E38D9289DE2AA2615EB0A5D94F355A3E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.36419119373890891061293729334001:50001231000000:2800:53F4F3CF14930AA6FCB8FCA95915EEEA8E9954F7F006023E0CA33041216CF7AE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.10069799621234137344511410705263:50001231000000:2800:C654A02A82932FAAB0D02F657BA25A5144C076EACE56F5503E0AA1A643C50138.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.40299067880691621904981797405764:50001231000000:2800:2D636F6FFB2993DF850093419AFEAE432A061195B27B4CDAE01B0D942CDCCE19.png?needInitFileName=true?needInitFileName=true)
通过远程调用方式调试云对象
您还可以将云对象部署至AGC云端，然后在DevEco Studio调用云端云对象，以测试云对象在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。
1.
2.  如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号，如'[[1, 2], 3]'，外层的方括号表示参数列表。
3.  如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号，如'[[1, 2], 3]'，外层的方括号表示参数列表。
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.74195720237983544741453449997559:50001231000000:2800:CEDF6580FE41098AF70FE3DA605D2FC46ECF0C657D187933EE70ADFBE3C21DBF.png?needInitFileName=true?needInitFileName=true)
-  如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号，如'[[1, 2], 3]'，外层的方括号表示参数列表。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.00320256478620852149966115675681:50001231000000:2800:59D00F3FBDFF5A930A25D111159E2ADB55CC17C8B032A72A2688F5E6248AF7CE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.98359175110820687563796413100645:50001231000000:2800:656DCEEC75825F44C318F2F664470427FD9594017B4055722B0701811D723ECA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-deploycloudobj-V14
爬取时间: 2025-04-30 07:18:28
来源: Huawei Developer
完成云对象代码开发后，您可将云对象部署到AGC云端，支持单个部署和批量部署。
单个部署仅部署选中的云对象，批量部署则会将整个“cloudfunctions”目录下的所有云对象同时部署到AGC云端。
下文以部署单个云对象“my-cloud-object”为例，介绍如何部署云对象。
1.  如需批量部署多个云对象，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有云对象。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到AGC云端。
2.  请您耐心等待，直至出现“Deploy successfully”消息，表示当前云对象已成功部署。
3.
4.
5.  部署成功后，您便可以从端侧调用云对象了，具体请参见在端侧调用云对象。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150638.98849838286003586598253200519362:50001231000000:2800:730B4381A9D5E0A3179720086434754879963573B7748F4132E4810BC3D68317.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150638.46868967996720115109845221345366:50001231000000:2800:A878AC3A742ADF431DED5A12DA01273FBB8BED2AE653C29C2C9A85828FE3CCD7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150638.31057409615149973053971585265105:50001231000000:2800:654AFBA0358EC59132D14FD844CF6CFF9E2CA7D1A93100EB776544E37D7B362A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.26568738431797710872877191956245:50001231000000:2800:E66A8D1AD82904BA67C5955F11627041F18075D7ED439FCCD945925455CAA8DE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.81687799115773968706391334754790:50001231000000:2800:F1AB1FA5DFE540FEBC23A0DD0B6A6EBE3156958757E46AC415D35B9B40FD575D.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-clouddb-V14
爬取时间: 2025-04-30 07:19:02
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-dbprocess-V14
爬取时间: 2025-04-30 07:19:37
来源: Huawei Developer
| 云数据库是一款端云协同的数据库产品，提供端云数据的协同管理、统一的数据模型和丰富的数据管理API接口等能力。云数据库采用基于对象模型的数据存储结构。数据以对象（Object）的形式存储在不同的存储区中，每一个对象，都是一条完整的数据记录。对象类型（ObjectType）用于定义存储对象的集合，不同的对象类型对应的不同数据结构。存储区（Zone）是一个独立的数据存储区域，每个存储区拥有完全相同的对象类型定义。 更多云数据库服务信息，请参考Cloud Foundation Kit开发指南（云数据库）。  |   |
| --- | --- |
云数据库是一款端云协同的数据库产品，提供端云数据的协同管理、统一的数据模型和丰富的数据管理API接口等能力。云数据库采用基于对象模型的数据存储结构。数据以对象（Object）的形式存储在不同的存储区中，每一个对象，都是一条完整的数据记录。对象类型（ObjectType）用于定义存储对象的集合，不同的对象类型对应的不同数据结构。存储区（Zone）是一个独立的数据存储区域，每个存储区拥有完全相同的对象类型定义。
更多云数据库服务信息，请参考Cloud Foundation Kit开发指南（云数据库）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.23127062573067523492970734025310:50001231000000:2800:D51C83846331A2A9B8C542CE5A688F3684BA5A1EC0AA3A65F7144577C8B9790D.png?needInitFileName=true?needInitFileName=true)
您可以使用DevEco Studio在端云一体化云侧工程下开发云数据库，总体流程如下。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.20785014880478289601190085548292:50001231000000:2800:AA6CB86CD3E756AABEE220408FD41947A6B3DE5A769FD5A98769EB2020B34FCC.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-objecttype-V14
爬取时间: 2025-04-30 07:20:11
来源: Huawei Developer
对象类型（ObjectType）用于定义存储对象的集合，不同的对象类型对应的不同数据结构。每创建一个对象类型，云数据库会在每个存储区实例化一个与之结构相对应的对象类型，用于存储对应的数据。
创建对象类型的操作如下：
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.05730801647070625619368162740961:50001231000000:2800:E191C7679782A00FC88C9742FFCEF68935E8CAB8F37D2F53FDA4D34617E6921C.png?needInitFileName=true?needInitFileName=true)
1.  对象类型名称必须符合如下规范： “clouddb/objecttype”目录下生成并打开新建的对象类型JSON文件“objecttype1.json”。
2.  参数 必选(M)/可选(O) 说明 fieldName M 字段名称。 输入要求具体如下： 当前Cloud Foundation Kit暂不支持自增类型字段IntAutoIncrement或LongAutoIncrement。 fieldType M 字段的数据类型。 当前支持的数据类型：String、Boolean、Byte、Short、Integer、Long、Float、Double、ByteArray、Text、Date。 belongPrimaryKey O 设置该字段是否为对象类型的主键，默认值为false。 notNull O 设置字段值是否为非空，默认值为false。 isNeedEncrypt O 设置字段是否需要加密，开启全程加密数据管理功能，默认值为false。 选择加密后，该字段对应的数据会加密存储在存储区中。 isSensitive O 设置字段是否为敏感字段，默认值为false。 选择敏感后，该字段对应的数据会加密存储在存储区中。 defaultValue O 字段为非空时，必须设置默认值。 例如，我们可为“objecttype1”对象类型配置如下字段。 fieldName fieldType belongPrimaryKey notNull isNeedEncrypt defaultValue author String true true - - shadowFlag Boolean - true - true bookName String - - - - id Integer - - - - price Double - - - - publishTime Date - - - -
3.  参数 必选(M)/可选(O) 说明 indexName M 索引名称。 输入要求具体如下： indexList > fieldName M 索引包含的字段。 支持设置组合索引，由多个字段组合成为索引，一个组合索引包含的字段不超过5个。 indexList > sortType M 索引包含的字段的排序方式，支持升序或降序。 例如，我们可为“objecttype1”对象类型配置如下两个索引。 indexName fieldName sortType id_Index id ASC price_Index price DESC
4.  参数 必选(M)/可选(O) 说明 role M 用户角色，包括： rights M 授予角色的权限，包括Read、Upsert（包含新增和修改）和Delete权限。 各角色只能完成对应权限的操作，超出权限范围的操作云侧将返回“permission denied”错误。由于端云一体化工程的初始化代码未配置AccessToken，故“CloudProgram/clouddb/objecttype/Post.json”中给World角色添加了Upsert和Delete权限。 例如，我们可按下表为各个角色配置“objecttype1”对象类型的权限。 角色 Read Upsert Delete World √ – – Authenticated √ √ – Creator √ √ √ Administrator √ √ √
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.77613144451476000612183111444386:50001231000000:2800:9B6F6FE44C24E1B0A78A33FB3770548246373C0B204211C05431C3268CF09541.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.72395428059673986698741202369593:50001231000000:2800:9B4B25DC6183DFE6E3CF4EF7A6A748DC36C5CD456A233A1BDE41DF4064918D0B.png?needInitFileName=true?needInitFileName=true)
| 参数  | 必选(M)/可选(O)  | 说明  |
| --- | --- | --- |
| fieldName  | M  | 字段名称。 输入要求具体如下： 字段的名称长度必须大于或等于1个字符，小于或等于30个字符，只能包含以下3种类型，并且至少包含“字母”类型：字母（A-Z或a-z）数字（0-9）特殊字符：_ 字段名称必须以字母开头，以字母或者数字结尾。字段名称中不区分字母的大小写。修改对象类型时，支持删除字段。字段名称不允许使用系统保留字段名称： naturalbase_version、naturalbase_deleted、naturalbase_operationtype、naturalbase_creator、naturalbase_accesstime、naturalbase_operationtime、naturalbase_syncstatus、naturalbase_changedfieldsbitmap、naturalbase_lastmodifier、cmin、cmax、xmin、xmax、ctid、oid、tableoid、xc_node_id、tablebucketid、rowid。 说明当前Cloud Foundation Kit暂不支持自增类型字段IntAutoIncrement或LongAutoIncrement。   |
| fieldType  | M  | 字段的数据类型。 当前支持的数据类型：String、Boolean、Byte、Short、Integer、Long、Float、Double、ByteArray、Text、Date。  |
| belongPrimaryKey  | O  | 设置该字段是否为对象类型的主键，默认值为false。 至少设置一个字段为主键。支持设置复合主键，由多个字段组合成为主键，一个复合主键包含的字段小于等于5个，复合主键字段顺序与字段的顺序一致。数据类型为ByteArray、Text、Date、Double、Float和Boolean的字段不支持设置为主键。主键的值不允许更改。  |
| notNull  | O  | 设置字段值是否为非空，默认值为false。 数据类型为ByteArray和Date的字段不支持设置为非空。主键默认非空，且不允许更改。设置为非空的字段不支持加密和敏感。  |
| isNeedEncrypt  | O  | 设置字段是否需要加密，开启全程加密数据管理功能，默认值为false。 选择加密后，该字段对应的数据会加密存储在存储区中。 主键字段不支持加密。加密的字段不支持设置为非空。加密的字段不支持设置为敏感字段。一个对象类型中包含的加密字段和敏感字段的总数需小于或等于5个。字段设置为加密后，不支持导出该字段的数据值。数据类型为ByteArray、Text的字段不支持加密。对象类型创建成功后，不支持修改加密属性。  |
| isSensitive  | O  | 设置字段是否为敏感字段，默认值为false。 选择敏感后，该字段对应的数据会加密存储在存储区中。 敏感字段不支持设置为主键。敏感字段不支持设置为非空。敏感字段不支持设置为加密。敏感字段不支持设置为默认值。对象类型创建成功后，不支持修改敏感属性。仅支持数据类型为Byte、Short、Integer、Long、Float、Double、String和Date的字段设置为敏感字段。敏感字段不支持设置为索引。一个对象类型中包含的加密字段和敏感字段的总数需小于或等于5个。  |
| defaultValue  | O  | 字段为非空时，必须设置默认值。 主键不支持设置默认值。加密字段和敏感字段不支持设置默认值。数据类型为ByteArray、Date不支持为其设置默认值。数据类型为Text的字段设置默认值时，默认值的长度小于或等于200个字符。  |
| fieldName  | fieldType  | belongPrimaryKey  | notNull  | isNeedEncrypt  | defaultValue  |
| --- | --- | --- | --- | --- | --- |
| author  | String  | true  | true  | -  | -  |
| shadowFlag  | Boolean  | -  | true  | -  | true  |
| bookName  | String  | -  | -  | -  | -  |
| id  | Integer  | -  | -  | -  | -  |
| price  | Double  | -  | -  | -  | -  |
| publishTime  | Date  | -  | -  | -  | -  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.20865220900071198702846813140497:50001231000000:2800:B6626795D20DB27263C27266A87F016F8B97372EB40E84E2E7E2F3084B9EEA9B.png?needInitFileName=true?needInitFileName=true)
| 参数  | 必选(M)/可选(O)  | 说明  |
| --- | --- | --- |
| indexName  | M  | 索引名称。 输入要求具体如下： 索引的名称长度必须大于或等于1个字符，小于或等于30个字符，只能包含以下3种类型，并且至少包含“字母”类型：字母（A-Z或a-z）数字（0-9）特殊字符：_ 索引名称必须以字母开头。索引名称中不区分字母的大小写。修改对象类型时，仅支持新增或者删除索引。当删除索引后，本次提交前不允许新增同名索引。每个对象类型可以设置小于或等于16个索引。数据类型为ByteArray和Text的字段不支持设置为索引。  |
| indexList > fieldName  | M  | 索引包含的字段。 支持设置组合索引，由多个字段组合成为索引，一个组合索引包含的字段不超过5个。  |
| indexList > sortType  | M  | 索引包含的字段的排序方式，支持升序或降序。  |
| indexName  | fieldName  | sortType  |
| --- | --- | --- |
| id_Index  | id  | ASC  |
| price_Index  | price  | DESC  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.40206619248440923604801503674046:50001231000000:2800:57D1309FFB2F2608D0B5C305123E794B8E89AC22B37EFB4C0F7F865D54860A6A.png?needInitFileName=true?needInitFileName=true)
| 参数  | 必选(M)/可选(O)  | 说明  |
| --- | --- | --- |
| role  | M  | 用户角色，包括： World：代表所有用户，包含认证和非认证用户。该角色默认拥有Read权限，可自定义配置Upsert和Delete权限。但是，不建议将Upsert和Delete权限配置给所有人角色。当对象类型中设置了加密字段之后，表示开启全程加密功能，此时所有人角色将不会拥有Read、Upsert和Delete权限，且不允许修改。Authenticated：经过AGC登录认证的用户。该角色默认拥有Read权限，可自定义配置Upsert和Delete权限。当对象类型中设置了加密字段之后，表示开启全程加密功能，此时认证用户角色将不会拥有Read、Upsert和Delete权限，且不允许修改。Creator：经过认证的数据创建用户。该角色默认拥有所有权限，且可自定义配置所有权限。每条数据都有其对应的数据创建人（即应用用户），每个数据创建者仅可以Upsert或者Delete自己创建的数据，不能Upsert或者Delete他人创建的数据。数据创建者的信息保存在数据记录的系统表中。Administrator：应用开发者，主要是指通过AGC控制台或FaaS（Function as a Service，函数即服务）侧访问云数据库的角色。该角色默认拥有所有权限，且可自定义配置所有权限。Administrator可以管理并配置其他角色的权限。  |
| rights  | M  | 授予角色的权限，包括Read、Upsert（包含新增和修改）和Delete权限。  |
| 角色  | Read  | Upsert  | Delete  |
| --- | --- | --- | --- |
| World  | √  | –  | –  |
| Authenticated  | √  | √  | –  |
| Creator  | √  | √  | √  |
| Administrator  | √  | √  | √  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.25958639347540086584111744124828:50001231000000:2800:4253BC98323CD42A70B836153F0522B508460928315E26BECD0064B6E05D3099.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-dataentry-V14
爬取时间: 2025-04-30 07:20:46
来源: Huawei Developer
创建完对象类型后，您可在对象类型内添加数据条目（DataEntry），并配置数据所在的存储区。
支持手动创建和自动生成数据条目文件。
手动创建数据条目文件
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.38746008567409086807245532851518:50001231000000:2800:4028BE03EF2C4DB55B905A3659D9F2C9D88959317DB0FB14932EA6FA24CDA7F1.png?needInitFileName=true?needInitFileName=true)
1.  例如，选择刚刚创建的对象类型“objecttype1”，数据条目文件取默认名“d_objecttype1”。 如下图，“clouddb/dataentry”目录下生成并打开新建的数据条目JSON文件“d_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。
2.  字段 数据条目1 数据条目2 author Nancy Peter shadowFlag true false bookName My Favorite Book Your First English Book id 10 20 price 10.5 20.5 publishTime 19961007 19961007
3.  字段 数据条目1 数据条目2 author Nancy Peter shadowFlag true false bookName My Favorite Book Your First English Book id 10 20 price 10.5 20.5 publishTime 19961007 19961007
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.26141849086810538865566772533805:50001231000000:2800:EF0E6C7664EC94D375512B8CEB0506A07A18E10C63DD44B0B11532781893E6AA.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150639.19795927107750353852302455792528:50001231000000:2800:CA2B547A330760CC409B4296CF2533B6D901DC56B9504EAA30DC49B3F3D077BE.png?needInitFileName=true?needInitFileName=true)
-  字段 数据条目1 数据条目2 author Nancy Peter shadowFlag true false bookName My Favorite Book Your First English Book id 10 20 price 10.5 20.5 publishTime 19961007 19961007
| 字段  | 数据条目1  | 数据条目2  |
| --- | --- | --- |
| author  | Nancy  | Peter  |
| shadowFlag  | true  | false  |
| bookName  | My Favorite Book  | Your First English Book  |
| id  | 10  | 20  |
| price  | 10.5  | 20.5  |
| publishTime  | 19961007  | 19961007  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.37383529457332258586807682952833:50001231000000:2800:AB5A9F1D7F2A72DCA214D18EB5428BCA7CFA83FDCEDE8333A9181CEF840AA526.png?needInitFileName=true?needInitFileName=true)
自动生成数据条目文件
1.  依旧以对象类型“objecttype1”为例，其包含了“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”六个字段。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.61246312770371841265774624494849:50001231000000:2800:5B76A05FD2C0661ED3984F64409AA4B524582D8EF9AEA5C76D0A47789CC9156A.png?needInitFileName=true?needInitFileName=true)
1.  如下图，“clouddb/dataentry”目录下自动为对象类型“objecttype1”生成数据条目文件“d_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。
2.  字段 数据条目1 数据条目2 author Nancy Peter shadowFlag true false bookName My Favorite Book Your First English Book id 10 20 price 10.5 20.5 publishTime 19961007 19961007
3.  字段 数据条目1 数据条目2 author Nancy Peter shadowFlag true false bookName My Favorite Book Your First English Book id 10 20 price 10.5 20.5 publishTime 19961007 19961007
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.34917483065352598130964886622637:50001231000000:2800:1CA6AB29EDF7C2C7947EE5C290A923D119E36833F3CCA81912E669A91CFA1808.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.44906337720826982254483782286650:50001231000000:2800:CB214682EBD06F6D49F9F994FC76BD2072BF05AFB040C25AC580F24C2F23C225.png?needInitFileName=true?needInitFileName=true)
-  字段 数据条目1 数据条目2 author Nancy Peter shadowFlag true false bookName My Favorite Book Your First English Book id 10 20 price 10.5 20.5 publishTime 19961007 19961007
| 字段  | 数据条目1  | 数据条目2  |
| --- | --- | --- |
| author  | Nancy  | Peter  |
| shadowFlag  | true  | false  |
| bookName  | My Favorite Book  | Your First English Book  |
| id  | 10  | 20  |
| price  | 10.5  | 20.5  |
| publishTime  | 19961007  | 19961007  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.94529861334025301046860659266651:50001231000000:2800:D45F53A8B2D7E82F553AD4DCD14002E4418A0843EB10CEA5A78C195EA46994EB.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-deploydatabase-V14
爬取时间: 2025-04-30 07:21:20
来源: Huawei Developer
完成数据条目创建后，您可以直接部署该数据条目。您也可以等所有对象类型和数据条目开发完成后，再统一批量部署到AGC云端。
部署云数据库的操作如下：
1.
2.  请您耐心等待，直至出现“Deploy successfully”消息，表示云数据库已成功部署。 云数据库部署成功后，DevEco Studio将自动从云侧下载云数据库的schema文件至“AppScope/resources/rawfile/schema.json”路径，该文件是云数据库端侧API必须引入的配置文件。
3.
4.
5.  部署成功后，您便可以从端侧访问云数据库了，具体请参见在端侧访问云数据库。 您还可以在AGC控制台继续编辑以上部署的云数据库资源，具体操作请参考管理数据库。 对象类型“Post”与“objecttype1”: 对象类型“Post”所属存储区“Demo”、“objecttype1”所属存储区“cloudDBZoneName1”： “d_Post.json”内的数据条目、“d_objecttype1.json”内的数据条目： 部署对象类型或数据条目JSON文件，实际是部署JSON文件内包含的对象类型或数据条目。因此，您在AGC控制台查看到的将是一个个对象类型或者一条条数据，而非JSON文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.94460686027220747890455889659368:50001231000000:2800:130B70B04F4549FACE384BB7C389088AC222C0EFE4D10823A56B23EFFB439B90.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.15207432299181690442532809915121:50001231000000:2800:2D0EC7D23F0F43CAD7C94C742D5A1A398B4E69575B61177453718E00C9941342.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.38047583437136621165565207074292:50001231000000:2800:2384CCFF7911A39F45D45B369A87098F0A55521E382CBEF283FA2476B08871C0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.67144179890997769016706680392168:50001231000000:2800:543899DA86D9C32A931ABBFBE6FE001181863AF5830E238FE8075B812721E34F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.34809714650321231410632230176932:50001231000000:2800:9E5C06C5068D08A4F86CECCDA7D1D06211FA29FFAF9E40C460DFEC685165C074.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.31834180725566478624109186704360:50001231000000:2800:012904F5D0E20AA7C3C390F69B9A4E9D1DCEB502AF1771F7376D9973B2B5A85C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.47146501981494569659974325544911:50001231000000:2800:1278E24223929EF466C1BE21118443E4EB221FFE568828668F5A3A8AD32A7D60.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150640.60673271816622999351131519848478:50001231000000:2800:1584173DA99A2275A43FECF629BB3E87BD309AD624D9BF24B5BBFF1EA2595BF4.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-modelclass-V14
爬取时间: 2025-04-30 07:21:55
来源: Huawei Developer
云数据库支持从端侧或者云侧云函数访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。DevEco Studio当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数开发时引用。
生成Server Model
1.
2.
3.  指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。
4.  如果定义的云数据库表字段中包含ByteArray或Date类型的字段，在插入或者更新云数据库时需要使用Server Model的parseFrom方法将入参转化成API识别的类型，例如上述示例中的BookInfo.parseFrom方法。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.99360357122913478873712842814303:50001231000000:2800:746208C11563C5861046C6CAA6E2689D0EB90F45DD8FD0FCFBFC7F7B205350E4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.42448599811050101650058743463775:50001231000000:2800:F319A562696CD47FC441FE94D8E316A22195DB29276310C5EAB76B53A7A274EE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.50418973625620171708879881322812:50001231000000:2800:488856100419D743A73FF319F595A6094038126EA052565433470DCBB2B16357.png?needInitFileName=true?needInitFileName=true)
生成Client Model
1.
2.
3.  指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.98806341032506712495460402813387:50001231000000:2800:3162AAE90800C1E0AF8DA50E7204C8594C381131E9146EA6E6BEA83F56B57B00.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.41645121972273747516617319219364:50001231000000:2800:94CD98DE419DD551AD7F3CC6CA19399BE328F9743F966BB6F8B495C2E30217CE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.69174339469292166962956158562946:50001231000000:2800:133E067B6B3C66F05C7412329D35EDCF2F8F005403212351A20AC374481DC9BD.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-deploy-V14
爬取时间: 2025-04-30 07:22:30
来源: Huawei Developer
您也可选择在云函数和云数据库全部开发完成后，将整个云工程资源统一部署到AGC云端。
1.
2.  请您耐心等待，直至出现“Deploy successfully”消息，表示云工程已成功部署。
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.92289215922827537625666523820695:50001231000000:2800:D104C41D6E051D9B661753D9F0C52C3B1CD41E4935B2F72AA4F9036E3B0E211F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.12753655999517450427109304843206:50001231000000:2800:92BCABC74BB30D1B3B7B0457712B5296023EBC3A41B4A42CBD0B1D9F312DF938.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.69287828947603973023558887147022:50001231000000:2800:9FC14BA44AFDA9EEDE7F1EFD616CC2E59AC75F41B14385E542AA44BB21857C7C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.14454629651734400858841694011072:50001231000000:2800:0EC1AFCEA8AED4E6D7880C53B79F4CF073CB418FFF2632697C7A69581EB308E0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.61821686723104493288883851212877:50001231000000:2800:FC82F8B49720364E1A70637D7F0460BFA0C84061F74BD25A72A2D9BB5217678D.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-sync-V14
爬取时间: 2025-04-30 07:23:04
来源: Huawei Developer
DevEco Studio还支持您将AGC云端当前项目下的代码同步至本地工程，包括之前从本地部署到AGC云端的代码、以及在AGC云端编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。
云端代码同步目前支持以下模式：仅同步云函数/云对象、仅同步云数据库、一键同步云侧代码。
同步云函数/云对象
对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。
同步单个云函数/云对象
云函数/云对象部署到AGC云端后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。
1.
2.
3.  后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.60718709646193421542067653183181:50001231000000:2800:C7F619697E4ACCA6CF7994766CEC83B4746A4D12E8CDD6DAFFF7FB53EA295BDD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.94197351211292651185964349195797:50001231000000:2800:FD2BB276B3E47060A06F05F6CE49A202F720786F4244F7B8AEADBF6498433F2B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150641.45705187409076364379217847681787:50001231000000:2800:D9618747D912133EDB6E0354C0A73D438567D986C6E1A06844053A486CA2E731.png?needInitFileName=true?needInitFileName=true)
批量同步云函数/云对象
批量同步云函数/云对象即将AGC云端当前项目下的所有云函数/云对象同步至本地工程。
1.
2.
3.  如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。
4.  如下图，“cloudfunctions”目录下新增了云端同步下来的云对象“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-备份时间.backup”。 后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.44801682976013088969746140445806:50001231000000:2800:B54E8381BF1F2BCCF81FBC0579735558287E8E13CD8C1D806F5879409C19AB5B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.56175318050958505630980624475452:50001231000000:2800:C3395007C5CE272B57C1A537680E640FA151E7319C18459D91F85BCE75362A43.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.52513612344085942203749666788767:50001231000000:2800:9205267C2B558A81F269EAD8C3FB1EEF3BDAC71912B1481260C95ABB88D745F0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.64266332350218048576852283132359:50001231000000:2800:40AA98065C78A810AB3C4669DE644BDB414B713BD9CDB7B5BE49E5EDBB1D0D88.png?needInitFileName=true?needInitFileName=true)
同步云数据库
目前仅支持同步对象类型。
同步单个对象类型
对象类型部署到AGC云端后，如又发生了新改动，您可再将云端的对象类型同步到本地。
1.
2.
3.  后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.37184829351290062002746855715969:50001231000000:2800:E94EAE643CAC5EC0B6AFA8550BF28FA7DC2F6DAE3957E8FC50FBAF3150BCF4EB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.93159587609066100409952095464237:50001231000000:2800:7BE752F43F41CE5EB77CD5353304B4DBF7BF2E93C37FEC968028853C726A2B75.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.62002799943467512736583759372396:50001231000000:2800:725B5F8588AD6D6566B1A91A91A4A920EE00BAF6DBF69E6E5A53B7BC90204F5A.png?needInitFileName=true?needInitFileName=true)
批量同步对象类型
您可以将AGC云端当前项目下所有的对象类型一键同步至本地。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.69339510366735929286195902015755:50001231000000:2800:31392D0203DE33061F4F036BA0DAB4BF1F6C1262213F25542D24DF3F87BC516E.png?needInitFileName=true?needInitFileName=true)
1.
2.  如下图，“objecttype”目录下新增了云端同步下来的“test_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
3.  后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.96390878033850087234514245365444:50001231000000:2800:D5527F02C5608AE8177B8762410DFD7B8581CAAAEE783715443D142CC3CB5917.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.96063003136239800566644166145694:50001231000000:2800:E7B3D7A399096AE0D190C78617BA49579B6050E6DFE6BF81D302CDBDFA164D22.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.43312687536920331295525184731326:50001231000000:2800:A33B5BE64C6A9CF04DFE9D5BDD7FB6124D06939FCBA080C04E889AF25F926FE3.png?needInitFileName=true?needInitFileName=true)
一键同步云侧代码
对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。
1.
2.
3.  如下图：
4.  如下图： 后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
5.  后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150642.40478417487828387817957863347332:50001231000000:2800:59E9CC87F79A47FF299E13CB07435273F865F7CAEDAE79551DB93322C2C6061C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.34792752460858959468667587873671:50001231000000:2800:822BACDDE0775AB8F51C963C10946658FCBFEFBB9C9F3900D636E19E16B6C6AD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.06286050513638207197355654643311:50001231000000:2800:941AB350F32DFB395391BD93EA4B8AA222B12BCEDE932C4F2493FA9B01EB8C6C.png?needInitFileName=true?needInitFileName=true)
-  后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.18962509547679159777786884776727:50001231000000:2800:3A52AE50B2560CBC9F3D0AC8BE86E8F3A4A49715380EB2C83C828E7170501517.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-appdevelop-V14
爬取时间: 2025-04-30 07:23:38
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-invokecloudcode-V14
爬取时间: 2025-04-30 07:24:13
来源: Huawei Developer
在通用云开发模板工程中，端侧“pages”目录下的ets页面文件代码实现了在端侧调用云侧代码。您可以参考这些文件内的代码实现，在自己的代码文件中进行开发。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-invokecloudfunc-V14
爬取时间: 2025-04-30 07:24:47
来源: Huawei Developer
前提条件
请确保云函数已正确开发并部署。
操作步骤
1.  例如，调用云侧函数“my-cloud-function”，以返回一个时间戳。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-invokecloudobj-V14
爬取时间: 2025-04-30 07:25:22
来源: Huawei Developer
云对象开发完成后，您可以为其生成端侧调用接口类，供后续端侧工程调用云对象使用。
前提条件
请确保云对象已正确开发并部署。
操作步骤
1.
2.
3.
4.  由于“Generate Invoke Interface”时已经生成所需要的模型以及importObject方法，因此在编码时可以很方便地使用联想、自动引入等DevEco Studio提供的高阶能力，如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.39944836536860447212280804802832:50001231000000:2800:658B426B67BC4D2CB7484F0C950C3C2F179B1B3C49FF2FE4B8D3C2EAAE7A37B7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.56122742363511166897447403994439:50001231000000:2800:295600B170C36A32D241820DD593F41C0EAF68BFDDB9B0F44E126D2058694F46.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.97101116298209827527722285801065:50001231000000:2800:812584A79D51A02384216B516099FD1CDB5DE91427DCD0B031C7EB9804BAA31D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.89288589468297460900265051595025:50001231000000:2800:8EA95E74B4F821728EBB2198B3CFF3F50366D8475DB040C20248BAF5D13E0065.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-invokeclouddatabase-V14
爬取时间: 2025-04-30 07:25:56
来源: Huawei Developer
前提条件
-  云数据库部署成功后，DevEco Studio将自动从云侧下载云数据库的schema文件至“AppScope/resources/rawfile/schema.json”路径，该文件是云数据库端侧API必须引入的配置文件。
操作步骤
1.
```typescript
...
async updateLikeCount(item: Post) {
let likes: string[] = JSON.parse(item.likes)
let userId: string = this.userId;
let index: number = likes.indexOf(userId);
if (index >= 0) {
likes = likes.filter((item: string) => item !== userId)
item.likeCount = likes.length
item.likes = JSON.stringify(likes)
} else {
likes.push(userId);
item.likeCount = likes.length
item.likes = JSON.stringify(likes)
}
try {
await this.agcDataBase?.upsert(item)
} catch (err) {
}
...
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.91686482558360778422969826410199:50001231000000:2800:AFF483154A38FFC91318B08AD9C20BBD9F7CD2CF9C627471B1444BAD450E83EF.png?needInitFileName=true?needInitFileName=true)
```typescript
...
async updateLikeCount(item: Post) {
let likes: string[] = JSON.parse(item.likes)
let userId: string = this.userId;
let index: number = likes.indexOf(userId);
if (index >= 0) {
likes = likes.filter((item: string) => item !== userId)
item.likeCount = likes.length
item.likes = JSON.stringify(likes)
} else {
likes.push(userId);
item.likeCount = likes.length
item.likes = JSON.stringify(likes)
}
try {
await this.agcDataBase?.upsert(item)
} catch (err) {
}
...
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-invokecloudstorage-V14
爬取时间: 2025-04-30 07:26:31
来源: Huawei Developer
前提条件
操作步骤
1.
```typescript
...
bucket.uploadFile(getContext(this), {
localPath: cacheFilePath,
cloudPath: cloudPath,
}).then(task => {
// add task event listener
this.addEventListener(task, this.onUploadCompleted(cloudPath, cacheFilePath));
// start task
task.start();
}).catch((err: BusinessError) => {
hilog.error(HILOG_DOMAIN, TAG, 'uploadFile failed, error code: %{public}d, message: %{public}s',
err.code, err.message);
this.isUploading = false;
});
...
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-console-V14
爬取时间: 2025-04-30 07:27:06
来源: Huawei Developer
DevEco Studio为您提供了CloudDev云开发管理面板。该面板集成了AGC云开发子控制台、文档和社区入口，方便您直达AGC云开发子控制台进行服务和资源管理，并且可轻松跳转至各指导文档和社区论坛来获取技术支持，为您提供开发、调试、部署、管理与技术支持的端到端体验。
1.
2.  如尚未登录，请点击“Sign in”登录您的华为开发者账号。 其中，AGC云开发子控制台如下图所示，您可按需进入对应菜单进行服务或资源管理。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.48323223923230364630198136638624:50001231000000:2800:A04DA3E6D18D64E79AA03C5341F01A85F85A5547FB170678DE0CB60B7657FCD2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.23182111408352172626011897028716:50001231000000:2800:EE4DA0E2219F7173A2BB57A576347F20DB399BFAB634A55345926E9D77B4BC93.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150643.25131569402648711232477103841529:50001231000000:2800:70666EA9840D73258BC9AFEA801F5800C6F22185E6F00168878FB5AF016818CE.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-compile-V14
爬取时间: 2025-04-30 07:27:40
来源: Huawei Developer
端云两侧工程代码全部开发完成后，建议您在本地进行调试，以查看和验证应用/元服务运行效果，减少发布过程中可能遇到的问题，具体请参见应用/服务调试。
当前API12的端云一体化开发工程仅支持手动签名。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-release-V14
爬取时间: 2025-04-30 07:28:14
来源: Huawei Developer
调试完毕后，将工程打包成APP，提交至AGC申请上架。具体请参见HarmonyOS应用/服务发布。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-faq-V14
爬取时间: 2025-04-30 07:28:49
来源: Huawei Developer
使用DevEco Studio打开端云一体化项目文件夹，左侧的项目列表不显示云侧工程
问题现象
开发者使用DevEco Studio打开端云一体化项目文件夹，左侧的项目列表不显示云侧工程“CloudProgram”。
解决措施
端云一体化工程根目录下只允许有“Application”与“CloudProgram”文件夹，不能有其他文件。否则，DevEco Studio会把该工程当成纯端侧工程，不显示云侧工程“CloudProgram”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.63001966098063573234420679877249:50001231000000:2800:3B5893DC07459C2A0C3B3EB2A8AAD2F78F125915F2F08AC4706F49A2F3F4BEDE.png?needInitFileName=true?needInitFileName=true)
部署云数据库时，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”
问题现象
部署云数据库失败，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”
解决措施
出现此错误，表示AGC云端的存储区数量超过最大限制。
部署到AGC云端的存储区数量不得超过4个，否则会导致部署失败。如AGC云端当前已存在4个存储区，请将数据部署到已有的存储区，或者删除已有存储区后再部署新的存储区。
需要注意的是，删除存储区，该存储区内的数据也将一并删除，且不可恢复。
部署云数据库时，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”
问题现象
部署云数据库失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.59281076015397185935687353960811:50001231000000:2800:E0620BAA4FDA1AC7C1529344E7C7BAFA47A20A4EF842EAAE3B2D805EDA6D5A34.png?needInitFileName=true?needInitFileName=true)
解决措施
出现此错误，可能是您在本地对象类型内做了与云端不兼容的修改。
对象类型中的fieldType等字段信息，部署到AGC云端后，请勿在本地再做修改。例如，fieldType设置为String，对象类型部署成功后，又在本地修改fieldType为Integer，再次部署将失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”错误。如需更改fieldType等字段信息，请先删除云端部署的对象类型。
需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。
体验端云一体化模板APP功能时，云存储上传图片失败，Hilog中打印“on response {"version":"HTTP/1.1","statusCode":403,"reason":"Forbidden","headers":{}}”
问题现象
体验端云一体化模板APP功能时，云存储上传图片失败，Hilog中打印“on response {"version":"HTTP/1.1","statusCode":403,"reason":"Forbidden","headers":{}}”。
解决措施
出现此错误，是由于使用云存储功能需要获取用户凭据。请先配置AccessToken。
体验端云一体化模板APP功能时，云数据库界面不展示数据，Hilog中打印“schemaJson_ is empty”
问题现象
体验端云一体化模板APP功能时，云数据库界面不展示数据，Hilog中打印“schemaJson_ is empty”。
解决措施
请检查resources/rawfile目录下是否存在schema文件。schema文件是云数据库功能依赖的必要文件，部署云数据库成功时会自动产生。如schema文件不存在，请重新部署云数据库，或从AGC控制台导出。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.09688221202563024744788154162025:50001231000000:2800:6CB6B22CCFF295FA381BF40E03D7B4A48F3638B384E489E4C8D513843FA1E2F4.png?needInitFileName=true?needInitFileName=true)
云数据库无法新建数据条目，Hilog中打印“2001015:permission denied”
问题现象
云数据库无法新建数据条目，Hilog中打印“2001015:permission denied”。
解决措施
出现此错误，是因为APP操作者的角色权限不足，请检查操作的对象类型的权限配置。
云函数调用失败，error message包含“404:160404:Trigger not exist”
问题现象
云函数调用失败，error message包含“404:160404:Trigger not exist”。
解决措施
出现此错误，是因为云函数未部署。error message中的404是服务端返回的HTTP状态码，表示找不到对应的函数。
云函数调用失败，error message包含“hmos auth app doesn't have permission”
问题现象
云函数调用失败，error message包含“hmos auth app doesn't have permission”。
解决措施
出现此错误，是因为当前云侧认证还不支持自动签名。请使用手动签名。
云函数部署失败，提示“The function type cannot be changed”
问题现象
云函数部署失败，错误信息中提示“The function type cannot be changed”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.12354973716311160002285225407631:50001231000000:2800:4192862DB58B865238E70A030A42E0F507B4B107861D155F693804618B4E535A.png?needInitFileName=true?needInitFileName=true)
解决措施
出现此错误，是因为云函数分为传统云函数类型和云对象类型。一种类型的云函数在部署到AGC云端后，不允许再变更成另一种类型。您可以前往AGC控制台的云函数服务页面，手动删除之前已部署的同名云函数/云对象，然后重新在DevEco Studio执行部署操作。
在云函数中调用云函数失败，提示“mismatched authType”
问题现象
在云函数中调用云函数失败，错误信息中提示“mismatched authType”。
解决措施
出现此错误，是因为被调用的云函数的HTTP触发器的认证类型须配置为云侧网关认证，即“authType”字段须配置为“cloudgw-client”。修改被调用云函数的“function-config.json”文件中的“authType”字段值，然后重新部署被调用的云函数即可。
端云一体化开发工程同步失败，失败步骤为npm install failed
问题现象
端云一体化开发工程同步失败，失败步骤是npm install failed。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.10532655390403613874916977291376:50001231000000:2800:8DCBA2D7BD1179E2031544C592C3E4787065C1B76D1C3DE7A31104E160D9BBB8.png?needInitFileName=true?needInitFileName=true)
解决措施
出现此错误，是因为端云一体化开发的云侧工程是通过npm管理依赖，同步时需要通过npm去下载对应依赖。请参考配置NPM代理检查npm代理和网络情况。
使用云存储上传文件失败，提示“404:Product does not exist”
问题现象
使用云存储上传文件失败，HiLog提示“404:Product does not exist”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180216.55840203989027995315548268570555:50001231000000:2800:C18ABFB46EF36263C65462B6E4EE556508DE38FC5919878E6DFC035E48B523BD.png?needInitFileName=true?needInitFileName=true)
解决措施
云存储服务端返回的错误，出现此错误是因为云存储服务未开通。请在顶部菜单栏选择“Tools > CloudDev”，进入CloudDev云开发管理面板，点击“Cloud Storage”服务下的“Go to console”快捷进入AGC服务菜单进行手动开通。
使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
问题现象
使用云存储上传文件失败，出现如下错误提示：
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.45484896926081449468670164492240:50001231000000:2800:5E1287A2443206D557CA8639E13239528210A2C19C5FE72D362E2550FF63AEA7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.78191554122044958683733898570080:50001231000000:2800:1EA0383ACC4F0958AD9941FD591D40237F01E736833DDDC45A196B38F4194E1D.png?needInitFileName=true?needInitFileName=true)
解决措施
使用云存储服务，需要通过AuthProvider获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。请参考AuthProvider获取用户凭据。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-template-V14
爬取时间: 2025-04-30 07:29:23
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agc-harmonyos-clouddev-emptyability-V14
爬取时间: 2025-04-30 07:29:58
来源: Huawei Developer
适用范围
| 模板名称  | 通用云开发模板（[CloudDev]Empty Ability）  |
| --- | --- |
| 模板说明  | DevEco Studio内预置的端云一体化开发模板。当前使用Cloud Foundation Kit（云开发服务，包括云函数、云数据库和云存储）搭建了基础的演示项目，不含业务属性。您可参考模板学习如何进行基础的端云工程开发，后续开发时可删除预置的页面代码。  |
| 支持的应用类型  | HarmonyOS应用元服务  |
模板名称
通用云开发模板（[CloudDev]Empty Ability）
模板说明
DevEco Studio内预置的端云一体化开发模板。当前使用Cloud Foundation Kit（云开发服务，包括云函数、云数据库和云存储）搭建了基础的演示项目，不含业务属性。您可参考模板学习如何进行基础的端云工程开发，后续开发时可删除预置的页面代码。
支持的应用类型
效果图
以下为通用云开发模板主要功能模块的效果图。
| 功能模块  | 效果图  | 功能说明  |
| --- | --- | --- |
| 云函数  |   | 点击“Generate Global Unique ID”时，调用云函数SDK执行部署在AGC云端的云对象“id-generator”，生成UUID。  |
| 云数据库  |   | 点击“New”创建数据，可在AGC云端查看到创建的数据。  |
| 云存储  |   | 点击“Upload Image”上传本地图片，成功后可获取图片链接。  |
功能模块
效果图
功能说明
云函数
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.98715458433003894359863766165673:50001231000000:2800:9439118022636AFB21DA0D16E99F9126D90AA475AE93B2C6B3B4019B43025ECB.png?needInitFileName=true?needInitFileName=true)
点击“Generate Global Unique ID”时，调用云函数SDK执行部署在AGC云端的云对象“id-generator”，生成UUID。
云数据库
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.48640586095111139814384783376201:50001231000000:2800:E52A95CFCB009B0581986C8321B3BDC3C048B1C053795C6E1350C2579E2E54E2.png?needInitFileName=true?needInitFileName=true)
点击“New”创建数据，可在AGC云端查看到创建的数据。
云存储
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.71956547509621616041247796587707:50001231000000:2800:A04FD404B6AEB7AC22486241E92AA22B56EAED9436E2DD0A6898C15ECA42246D.png?needInitFileName=true?needInitFileName=true)
点击“Upload Image”上传本地图片，成功后可获取图片链接。
体验模板
如您希望在设备上亲自体验该模板的功能和页面效果，可按如下流程操作：
当前Cloud Foundation Kit不支持模拟器，请使用真机体验。
1.  当前端云一体化开发工程仅支持手动签名。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-V14
爬取时间: 2025-04-30 07:30:32
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-V14
爬取时间: 2025-04-30 07:31:07
来源: Huawei Developer
编译构建工具DevEco Hvigor（以下简称Hvigor）是一款基于TS实现的构建任务编排工具，主要提供任务管理机制，包括任务注册编排、工程模型管理、配置管理等关键能力，提供专用于构建和测试应用的流程和可配置设置。
DevEco Studio使用构建工具Hvigor来自动执行和管理构建流程，实现应用/元服务构建任务流的执行，完成HAP/APP的构建打包。
Hvigor可独立于DevEco Studio运行，这意味着，你可以在DevEco Studio内、命令行工具或是集成服务器上构建应用。无论您从命令行工具或是DevEco Studio上构建项目，构建过程的输出都将相同。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-life-cycle-V14
爬取时间: 2025-04-30 07:31:42
来源: Huawei Developer
本文档对Hvigor编译构建系统结构及生命周期进行简要讲解，首先介绍Hvigor对工程结构模型的定义，随后介绍什么是任务（Task），最后会介绍Hvigor的构建生命周期以及它是如何依赖hvigor-ohos-plugin一起完成自动化编译构建流程的。
工程结构定义
Hvigor将工程解析为一个树形结构，项目为树的根节点，项目中的每个模块为树的叶子节点，树最多为两层，模块中不能包含其他模块，在Hvigor的定义中统称项目或模块为一个node(节点)。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150644.29972514467797971431196246794563:50001231000000:2800:55AF9B1C6171CF226FED0D4E9537C204187B76ECDE5CE1E75A6E00D8022F9BDD.png?needInitFileName=true?needInitFileName=true)
在构建最开始的初始化阶段，会通过hvigorconfig.ts文件以及工程级build-profile.json5文件中的配置来构造出一个树形结构存储项目的工程结构，工程级build-profile.json5文件和hvigorconfig.ts文件均可以配置多模块。
Hvigor脚本文件
构建的生命周期中Hvigor使用两个脚本文件来完成插件、任务以及生命周期hook的注册：
任务与任务依赖图
Hvigor是基于任务对您的项目进行自动化构建的，任务（Task）是Hvigor构建过程中的基本工作单元，它定义了构建项目时需要执行的具体工作。任务可以完成多种操作，比如源码编译任务，打包任务或签名任务等。每一种任务的执行逻辑由插件（plugin）提供，插件可以是由hvigor-ohos-plugin提供的默认任务逻辑，也可由您个性化定制。
需要注意的一点是，任务是存在依赖关系的，Hvigor在执行任何任务之前会构建任务依赖图，所有任务会形成一个有向无环图（DAG），如下示例图，任务之间的依赖关系用箭头进行表示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150644.04335581739752801833757374981367:50001231000000:2800:B31431CDB0FF3EA1045E347D4E2D02E5C32738824831AD637F3BD56D9B7B316E.png?needInitFileName=true?needInitFileName=true)
hvigor插件（hvigor-ohos-plugin）和hvigorfile.ts文件中的构建脚本都将通过任务依赖机制对任务依赖图做出影响。
hvigor-ohos-plugin
hvigor-ohos-plugin是默认的构建插件，为任务（Task）的完成提供业务逻辑支持，比如为Hvigor提供Hap、Har和Hsp打包服务等任务，每一种任务的具体执行逻辑由本模块中不同的插件来提供。
Hvigor与hvigor-ohos-plugin的关系
概述部分提到了Hvigor提供任务注册编排以及配置管理等任务管理机制，它负责控制任务的执行流程，但是并不包含每一个任务的具体业务逻辑，具体逻辑是由hvigor-ohos-plugin提供的。
Hvigor和hvigor-ohos-plugin的关系可以通过下图来说明，Hvigor接受任务的注册并编排任务执行顺序，并按照顺序依次调用hvigor-ohos-plugin中的插件来执行任务。如果您定制了自己的任务逻辑插件并将其注册，hvigor-ohos-plugin也会调用您的个性化插件来完成编译构建流程。
在Hvigor执行构建的过程中，hvigor-ohos-plugin会向Hvigor进行任务的注册，Hvigor会根据构建的任务执行有向图依次调用对应的插件来执行相应任务，在完成编译、打包、签名等一系列任务后，Hvigor也就正式完成了构建。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150644.20507718269397159449354502527895:50001231000000:2800:4E35BAE53F1530D1C440DAD281BA4AEA716562228918E7997474451000642493.png?needInitFileName=true?needInitFileName=true)
Hvigor生命周期
生命周期展示了Hvigor编译构建系统如何进行一次完整的编译构建流程。Hvigor的编译构建过程有三个不同的阶段，分为初始化、配置和执行，Hvigor会按顺序运行这些阶段。
初始化
此阶段主要目的为初始化项目的编译参数，构造出项目结构的树形数据模型，每个node为一个HvigorNode对象。
配置
此阶段开始时，所有的node都已经加载完毕，但每个node中还没有加载插件（plugin）、任务（task）和DAG图，此阶段的主要目的就是加载出这些内容。
执行
生命周期及hook点
在Hvigor的生命周期中，以下多个hook点可供您使用，便于您在对应的时机调用某些逻辑。
在下图中所有绿色标记的线框为可以使用的hook点。每个hook点的使用方式请参考基础构建能力。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150645.55103317909689494512474011993309:50001231000000:2800:AAFFAF633573E245FD667D2E37C06D2B91CE90EA1D5E4B01EC2BE5A098893118.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-configuration-file-V14
爬取时间: 2025-04-30 07:32:16
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-set-options-V14
爬取时间: 2025-04-30 07:32:51
来源: Huawei Developer
Hvigor提供hvigor-config.json5文件，以指定开发态版本号、构建依赖以及构建行为的配置参数。
| 参数  | 是否必填  | 类型  | 说明  |
| --- | --- | --- | --- |
| modelVersion  | 是  | string  | 开发态版本号。  |
| dependencies  | 是  | object  | 当前工程执行构建任务时，依赖的构建插件及版本，为npm源组件。  |
| execution  | 否  | object  | 执行构建的相关配置参数。  |
|    | analyze  | 否  | string | boolean  | 构建分析模式。 normal（默认值）：普通模式，通过简单打点数据进行分析。原default模式已废弃。advanced：进阶模式，通过更加详细的打点数据进行分析。如果需要更详细的任务耗时数据，请选择该模式。原verbose模式已废弃。false：不启用构建分析。  |
| daemon  | 否  | boolean  | 是否启用守护进程编译。 true（缺省默认值）：启用。false：不启用。  |
| incremental  | 否  | boolean  | 是否启用增量编译。 true（缺省默认值）：启用。false：不启用。  |
| parallel  | 否  | boolean  | 是否启用并行编译。 true（缺省默认值）：启用。false：不启用。  |
| typeCheck  | 否  | boolean  | 是否启用构建脚本hvigorfile.ts文件的类型检查，启用后构建效率可能会有所降低。 true：启用。false（缺省默认值）：不启用。  |
| logging  | 否  | object  | 日志相关配置参数。  |
|    | level  | 否  | string  | 构建时打印日志的级别。 debug：调测日志。info（缺省默认值）：基本信息日志。warn：告警日志。error：错误日志。  |
| debugging  | 否  | object  | 调测相关配置参数。  |
|    | stacktrace  | 否  | boolean  | 是否启用堆栈跟踪。 true：启用。false（缺省默认值）：不启用。  |
| nodeOptions  | 否  | object  | Node相关配置参数。  |
|    | maxOldSpaceSize  | 否  | integer  | 启用守护进程编译时，守护进程老生代内存大小，单位为MB。当工程代码量较大出现JS内存溢出时，可以调整该参数。 启用守护进程编译但未配置该参数时，将使用Node默认的内存大小配置。  |
|    | exposeGC  | 否  | boolean  | 是否启用GC（Garbage Collection，内存回收），启用后会优化编译过程的峰值内存。 true（缺省默认值）：启用。false：不启用。  |
| javaOptions  | 否  | object  | java相关配置参数。  |
|    | Xmx  | 否  | integer  | 设置JVM最大堆内存，单位为MB，默认为512MB。  |
| properties  | 否  | object  | 额外配置参数。  |
|    | hvigor.cacheDir  | 否  | string  | 指定项目根目录下的.hvigor缓存文件夹的存放路径。 说明同名的不同工程不可指定相同的存放位置。   |
| ohos.buildDir  | 否  | string  | 指定项目的构建产物目录（build目录）存放位置。 说明同名的不同工程不可指定相同的存放位置。   |
| enableSignTask  | 否  | boolean  | 是否启用HAP或HSP签名任务。 true（缺省默认值）：启用。false：不启用。  |
| ohos.arkCompile.maxSize  | 否  | integer  | 指定编译ArkTS线程的数量，默认为5。  |
| hvigor.pool.maxSize  | 否  | integer  | 指定编译过程中的线程数量，相比ohos.arkCompile.maxSize增加签名、打包等任务的线程。默认值为“工程的模块数”和“电脑虚拟核数-1”两者的较小值。  |
| ohos.pack.compressLevel  | 否  | string  | 设置打包hap（压缩so）或app（压缩hap）时的压缩率等级。压缩率越高，压缩速度越慢。 fast（缺省默认值）：最低等级的压缩率，压缩速度最快。standard：适中等级的压缩率，压缩速度适中。ultimate：最高等级的压缩率，压缩速度最慢。  |
| hvigor.analyzeHtml  | 否  | boolean  | 是否生成构建可视化html文件。 true：生成构建可视化html文件。生成的html文件存放在工程的.hvigor/report目录下，该文件可直接在浏览器中打开。false（缺省默认值）：不生成构建可视化html文件。  |
| hvigor.dependency.useNpm  | 否  | boolean  | 指定是否使用npm下载hvigor依赖。 若未配置该字段，当Node.js版本 ≥ 16时，默认使用pnpm下载依赖。在某些特定场景，可以通过配置该字段指定使用npm下载依赖。 true：对于任意Node版本，都使用npm下载依赖。false（缺省默认值）：Node.js版本 ≥ 16时，使用pnpm下载依赖；Node.js版本 ＜ 16时，使用npm下载依赖。  |
| ohos.compile.lib.entryfile  | 否  | boolean  | 指定是否从入口文件开始编译： true：表示从模块的入口文件开始编译，将编译入口文件及被引用的文件，没被引用的文件不会参与编译流程。false（缺省默认值）：表示将src/main/ets下的ets和ts文件进行全量编译，涉及到以下场景：构建HSP时，存在于src/main/ets下的ets和ts文件都会被编译到产物中。release模式对HAR混淆或构建字节码HAR时，存在于src/main/ets下的ets和ts文件都会被编译到产物中。构建HAP/HSP时，存在于动态依赖的HAR模块src/main/ets下的ets和ts文件都会被编译到产物中。   |
| ohos.align.target  | 否  | string  | 指定本次构建任务所有涉及到的模块及其依赖的模块的target。详情请参考多产物构建target。  |
| ohos.fallback.target  | 否  | array  | 指定本次构建任务所有涉及到的模块及其依赖模块的fallback target，fallback target是一个特定优先级的target，各target的优先级顺序：align target > 命令行指定target > 被依赖的父模块target > fallback target > default target。详情请参考多产物构建target。  |
| ohos.arkCompile.sourceMapDir  | 否  | string  | 指定sourceMap文件的生成路径，方便开发者进行堆栈的回栈与错误信息的定位，当前仅支持Stage模型。若没有指定路径，默认生成在build/{productName}/outputs/{targetName}/mapping下。 说明从API 12开始支持。   |
| ohos.collect.debugSymbol  | 否  | boolean  | 是否将sourceMap、nameCache和带调试信息的so文件归档到产物路径下，根据选择的构建模式，如果是构建HAP/HSP/HAR，会归档到模块的build/{productName}/outputs/{targetName}/symbol的release或debug目录下；如果是构建APP，会将HAP/HSP模块的文件归档到工程的build/outputs/{productName}/symbol的release或debug目录下。 true：归档。false：不归档。 说明如果不配置，release模式时默认值为true，debug模式时默认值为false。仅支持Stage模型。nameCache文件仅在release模式下且开启混淆后才会生成，release模式下不开启混淆以及debug模式下均不生成这个文件。   |
| hvigor.enableMemoryCache  | 否  | boolean  | 是否开启缓存，开启缓存会加快增量编译速度，关闭缓存能够节省内存占用，但是会增加增量编译时间。 true（缺省默认值）：开启。false：不开启。  |
| hvigor.memoryThreshold  | 否  | integer  | 内存管理阈值，单位为MB，当编译构建占用内存超过此阈值时，新加入的编译任务会等待，直到正在进行的编译任务结束，新的编译任务才能开始，此配置将导致编译时间延长。 说明配置该字段后，即使hvigor.enableMemoryCache配置为true，也不进行缓存。该字段配置为很小的值时，构建任务会串行执行，等效于配置ohos.arkCompile.maxSize:1；配置为很大的值时，与不配置没有差异。   |
| ohos.nativeResolver  | 否  | boolean  | ArkTS编译过程中是否使用高性能插件进行依赖寻址，使用高性能插件可以降低编译过程的峰值内存，加快编译速度。 true（缺省默认值）：使用。false：不使用。  |
| ohos.arkCompile.noEmitJs  | 否  | boolean  | ArkTS编译过程中是否生成js中间产物，不生成js中间产物可以降低编译过程的峰值内存，加快编译速度。 true：不生成。false（缺省默认值）：生成。 说明以下场景均不支持该字段，配置后也会生成js中间产物： FA模型。覆盖率测试。在release模式下，开启混淆构建包含js中间码的HAR。LiteWearable设备对应的工程。   |
| ohos.sign.har  | 否  | boolean  | 是否启用HAR签名任务。详情请参考构建签名HAR。 true：启用。false（缺省默认值）：不启用。  |
| hvigor.keepDependency  | 否  | boolean  | 是否保持hsp中的所有依赖。如果保持则不对依赖进行处理，如果不保持，则只会保留hsp模块中的hsp相关依赖。 true（缺省默认值）：保持。false：不保持。  |
参数
是否必填
类型
说明
modelVersion
是
string
开发态版本号。
dependencies
是
object
当前工程执行构建任务时，依赖的构建插件及版本，为npm源组件。
execution
否
object
执行构建的相关配置参数。
analyze
否
string | boolean
构建分析模式。
daemon
否
boolean
是否启用守护进程编译。
incremental
否
boolean
是否启用增量编译。
parallel
否
boolean
是否启用并行编译。
typeCheck
否
boolean
是否启用构建脚本hvigorfile.ts文件的类型检查，启用后构建效率可能会有所降低。
logging
否
object
日志相关配置参数。
level
否
string
构建时打印日志的级别。
debugging
否
object
调测相关配置参数。
stacktrace
否
boolean
是否启用堆栈跟踪。
nodeOptions
否
object
Node相关配置参数。
maxOldSpaceSize
否
integer
启用守护进程编译时，守护进程老生代内存大小，单位为MB。当工程代码量较大出现JS内存溢出时，可以调整该参数。
启用守护进程编译但未配置该参数时，将使用Node默认的内存大小配置。
exposeGC
否
boolean
是否启用GC（Garbage Collection，内存回收），启用后会优化编译过程的峰值内存。
javaOptions
否
object
java相关配置参数。
Xmx
否
integer
设置JVM最大堆内存，单位为MB，默认为512MB。
properties
否
object
额外配置参数。
hvigor.cacheDir
否
string
指定项目根目录下的.hvigor缓存文件夹的存放路径。
同名的不同工程不可指定相同的存放位置。
ohos.buildDir
否
string
指定项目的构建产物目录（build目录）存放位置。
同名的不同工程不可指定相同的存放位置。
enableSignTask
否
boolean
是否启用HAP或HSP签名任务。
ohos.arkCompile.maxSize
否
integer
指定编译ArkTS线程的数量，默认为5。
hvigor.pool.maxSize
否
integer
指定编译过程中的线程数量，相比ohos.arkCompile.maxSize增加签名、打包等任务的线程。默认值为“工程的模块数”和“电脑虚拟核数-1”两者的较小值。
ohos.pack.compressLevel
否
string
设置打包hap（压缩so）或app（压缩hap）时的压缩率等级。压缩率越高，压缩速度越慢。
hvigor.analyzeHtml
否
boolean
是否生成构建可视化html文件。
hvigor.dependency.useNpm
否
boolean
指定是否使用npm下载hvigor依赖。
若未配置该字段，当Node.js版本 ≥ 16时，默认使用pnpm下载依赖。在某些特定场景，可以通过配置该字段指定使用npm下载依赖。
ohos.compile.lib.entryfile
否
boolean
指定是否从入口文件开始编译：
ohos.align.target
否
string
指定本次构建任务所有涉及到的模块及其依赖的模块的target。详情请参考多产物构建target。
ohos.fallback.target
否
array
指定本次构建任务所有涉及到的模块及其依赖模块的fallback target，fallback target是一个特定优先级的target，各target的优先级顺序：align target > 命令行指定target > 被依赖的父模块target > fallback target > default target。详情请参考多产物构建target。
ohos.arkCompile.sourceMapDir
否
string
指定sourceMap文件的生成路径，方便开发者进行堆栈的回栈与错误信息的定位，当前仅支持Stage模型。若没有指定路径，默认生成在build/{productName}/outputs/{targetName}/mapping下。
从API 12开始支持。
ohos.collect.debugSymbol
否
boolean
是否将sourceMap、nameCache和带调试信息的so文件归档到产物路径下，根据选择的构建模式，如果是构建HAP/HSP/HAR，会归档到模块的build/{productName}/outputs/{targetName}/symbol的release或debug目录下；如果是构建APP，会将HAP/HSP模块的文件归档到工程的build/outputs/{productName}/symbol的release或debug目录下。
hvigor.enableMemoryCache
否
boolean
是否开启缓存，开启缓存会加快增量编译速度，关闭缓存能够节省内存占用，但是会增加增量编译时间。
hvigor.memoryThreshold
否
integer
内存管理阈值，单位为MB，当编译构建占用内存超过此阈值时，新加入的编译任务会等待，直到正在进行的编译任务结束，新的编译任务才能开始，此配置将导致编译时间延长。
ohos.nativeResolver
否
boolean
ArkTS编译过程中是否使用高性能插件进行依赖寻址，使用高性能插件可以降低编译过程的峰值内存，加快编译速度。
ohos.arkCompile.noEmitJs
否
boolean
ArkTS编译过程中是否生成js中间产物，不生成js中间产物可以降低编译过程的峰值内存，加快编译速度。
以下场景均不支持该字段，配置后也会生成js中间产物：
ohos.sign.har
否
boolean
是否启用HAR签名任务。详情请参考构建签名HAR。
hvigor.keepDependency
否
boolean
是否保持hsp中的所有依赖。如果保持则不对依赖进行处理，如果不保持，则只会保留hsp模块中的hsp相关依赖。
hvigor-config.json5的示例如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-build-profile-V14
爬取时间: 2025-04-30 07:33:25
来源: Huawei Developer
build-profile.json5文件分为工程级与模块级，其中buildOption在工程级文件和模块级文件均可配置，其中相同字段以模块级的字段为准，不同字段模块级的buildOption配置会继承工程级配置。
工程级
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| app | object | 是 | 编译配置信息。 |
|    | signingConfigs | array | 否 | 签名方案信息，可配置多个。 |
|    | name | string | 是 | 签名方案的名称，不允许为空字符串。 |
| material | object | 是 | 签名方案相关材料，如密码、证书等，详情请参见表2。 |
| type | string | 否 | 签名类型：  HarmonyOS OpenHarmony  |
| products | array | 否 | 产品品类，可配置多个。如需配置多个，相关说明请参见配置多目标产物章节。 |
|    | name | string | 是 | 产品的名称，必须存在name为"default"的product。 |
| signingConfig | string | 否 | 产品的签名方案名称，即signingConfigs中配置的某个签名方案名称。 |
| bundleName | string | 否 | 产品的包名。 |
| buildOption | object | 否 | 产品的编译构建配置，详情请参见表3。 |
| runtimeOS | string | 否 | 产品的运行环境：  HarmonyOS OpenHarmony  |
| arkTSVersion | string | 否 | ArkTS语法检查工具的版本号：1.0，1.1。 默认为当前ArkTS语法检查工具支持的最新版本。 仅API 11及以上版本工程支持。 |
| compileSdkVersion | string/integer | 否 | 标识编译应用/元服务所使用的SDK版本。  运行环境是HarmonyOS时，字段类型为string，配置示例：5.0.2(14) 运行环境是OpenHarmony时，字段类型为integer，配置示例：14  说明 从DevEco Studio NEXT Developer Beta1（5.0.3.403）版本开始，该字段不需要显性配置，编译时默认使用配套的SDK版本。如果配置，只能配置为当前DevEco Studio配套的SDK版本，不允许配置为其他SDK版本。  |
| compatibleSdkVersion | string/integer | 是 | 标识应用/元服务运行所需兼容的最低SDK版本，应用/元服务不能安装在低于该版本的设备。 |
| targetSdkVersion | string/integer | 否 | 标识应用/元服务运行所需目标SDK版本，是系统提供的前向兼容手段。如果新SDK版本中API行为发生变更，将应用/元服务安装到新系统后，可通过该字段提供向前兼容手段，在新系统版本保持老的API行为。如未配置，默认与compileSdkVersion保持一致。 |
| bundleType | string | 否 | 包的类型：  app：应用 atomicService：元服务 shared：共享包  |
| label | string | 否 | 应用/元服务名称。配置示例："$string:app_name"。 配置products中的label、icon、versionCode、versionName、resource字段后，编译构建时将根据此处的配置替换 app.json5中的相关配置，常用于应用和元服务可分可合构建打包场景。 |
| icon | string | 否 | 应用图标。配置示例："$media:application_icon"。 |
| versionCode | integer | 否 | 版本号。配置示例：1000000。 |
| versionName | string | 否 | 版本名称。配置示例："1.0.0"。 |
| resource | object | 否 | 名称和图标对应的资源所在目录。详情请参见表4。 |
| output | object | 否 | 定制产品生成的应用包的配置，详情请参见表5 output。 |
| vendor | string | 否 | 供应商。 |
| buildModeSet | array | 否 | 构建模式合集，可配置多个。 |
|    | name | string | 是 | 构建模式名称。默认生成debug，release和test三个名称，支持开发者自定义，其中test模式仅在执行ohosTest测试套件时使用。 |
| buildOption | object | 否 | 构建模式使用的具体配置信息，详情请参见表3。关于buildOption的优先级请参考定制编译模式。 |
| multiProjects | boolean | 否 | 当前工程是否支持多工程构建：  true：支持。 false（缺省默认值）：不支持。  |
| modules | array | 是 | 工程中所包含模块的信息，包含工程中所有的模块。数组长度至少为1。 |
|    | name | string | 是 | 模块的名称。该名称需与module.json5文件中的module.name保持一致。 在FA模型中，对应的文件为config.json。 |
| srcPath | string | 是 | 模块的源码路径，为模块根目录相对工程根目录的相对路径，允许模块根目录不在当前工程下，详情请参考导入Module。 说明 当前支持引用其他工程下的HAR和HSP模块。  |
| targets | array | 否 | 模块的target信息，用于定制多目标构建产物。 更多关于多目标构建产物的内容，请参见配置多目标产物章节。 |
|    | name | string | 是 | target名称，在各个模块级build-profile.json5中的targets字段定义。HAR模块无需配置。 |
| applyToProducts | array | 否 | target关联的product。HAR模块无需配置。 |
配置项
类型
是否必填
说明
app
object
是
编译配置信息。
signingConfigs
array
否
签名方案信息，可配置多个。
name
string
是
签名方案的名称，不允许为空字符串。
material
object
是
签名方案相关材料，如密码、证书等，详情请参见表2。
type
string
否
签名类型：
products
array
否
产品品类，可配置多个。如需配置多个，相关说明请参见配置多目标产物章节。
name
string
是
产品的名称，必须存在name为"default"的product。
signingConfig
string
否
产品的签名方案名称，即signingConfigs中配置的某个签名方案名称。
bundleName
string
否
产品的包名。
buildOption
object
否
产品的编译构建配置，详情请参见表3。
runtimeOS
string
否
产品的运行环境：
arkTSVersion
string
否
ArkTS语法检查工具的版本号：1.0，1.1。
默认为当前ArkTS语法检查工具支持的最新版本。
仅API 11及以上版本工程支持。
compileSdkVersion
string/integer
否
标识编译应用/元服务所使用的SDK版本。
从DevEco Studio NEXT Developer Beta1（5.0.3.403）版本开始，该字段不需要显性配置，编译时默认使用配套的SDK版本。如果配置，只能配置为当前DevEco Studio配套的SDK版本，不允许配置为其他SDK版本。
compatibleSdkVersion
string/integer
是
标识应用/元服务运行所需兼容的最低SDK版本，应用/元服务不能安装在低于该版本的设备。
targetSdkVersion
string/integer
否
标识应用/元服务运行所需目标SDK版本，是系统提供的前向兼容手段。如果新SDK版本中API行为发生变更，将应用/元服务安装到新系统后，可通过该字段提供向前兼容手段，在新系统版本保持老的API行为。如未配置，默认与compileSdkVersion保持一致。
bundleType
string
否
包的类型：
label
string
否
应用/元服务名称。配置示例："$string:app_name"。
配置products中的label、icon、versionCode、versionName、resource字段后，编译构建时将根据此处的配置替换 app.json5中的相关配置，常用于应用和元服务可分可合构建打包场景。
icon
string
否
应用图标。配置示例："$media:application_icon"。
versionCode
integer
否
版本号。配置示例：1000000。
versionName
string
否
版本名称。配置示例："1.0.0"。
resource
object
否
名称和图标对应的资源所在目录。详情请参见表4。
output
object
否
定制产品生成的应用包的配置，详情请参见表5 output。
vendor
string
否
供应商。
buildModeSet
array
否
构建模式合集，可配置多个。
name
string
是
构建模式名称。默认生成debug，release和test三个名称，支持开发者自定义，其中test模式仅在执行ohosTest测试套件时使用。
buildOption
object
否
构建模式使用的具体配置信息，详情请参见表3。关于buildOption的优先级请参考定制编译模式。
multiProjects
boolean
否
当前工程是否支持多工程构建：
modules
array
是
工程中所包含模块的信息，包含工程中所有的模块。数组长度至少为1。
name
string
是
模块的名称。该名称需与module.json5文件中的module.name保持一致。
在FA模型中，对应的文件为config.json。
srcPath
string
是
模块的源码路径，为模块根目录相对工程根目录的相对路径，允许模块根目录不在当前工程下，详情请参考导入Module。
当前支持引用其他工程下的HAR和HSP模块。
targets
array
否
模块的target信息，用于定制多目标构建产物。
更多关于多目标构建产物的内容，请参见配置多目标产物章节。
name
string
是
target名称，在各个模块级build-profile.json5中的targets字段定义。HAR模块无需配置。
applyToProducts
array
否
target关联的product。HAR模块无需配置。
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| storePassword | string | 是 | 密钥库密码，以密文形式呈现。 通过File > Project Structure... > Project > Signing Configs界面，进行自动签名后，material节点中的各配置项会自动填充。 |
| certpath | string | 是 | 调试或发布证书文件地址，文件后缀为.cer。 |
| keyAlias | string | 是 | 密钥别名信息。 |
| keyPassword | string | 是 | 密钥密码，以密文形式呈现。 |
| profile | string | 是 | 调试或发布证书Profile文件地址，文件后缀为.p7b。 |
| signAlg | string | 是 | 密钥库signAlg参数。当前可配置值SHA256withECDSA。 |
| storeFile | string | 是 | 密钥库文件地址，文件后缀为.p12。 |
配置项
类型
是否必填
说明
storePassword
string
是
密钥库密码，以密文形式呈现。
通过File > Project Structure... > Project > Signing Configs界面，进行自动签名后，material节点中的各配置项会自动填充。
certpath
string
是
调试或发布证书文件地址，文件后缀为.cer。
keyAlias
string
是
密钥别名信息。
keyPassword
string
是
密钥密码，以密文形式呈现。
profile
string
是
调试或发布证书Profile文件地址，文件后缀为.p7b。
signAlg
string
是
密钥库signAlg参数。当前可配置值SHA256withECDSA。
storeFile
string
是
密钥库文件地址，文件后缀为.p12。
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| packOptions | object | 否 | 打包相关配置项。 |
|    | buildAppSkipSignHap | boolean | 否 | 是否跳过生成签名HAP：  true：跳过，即不生成签名HAP。 false（缺省默认值）：不跳过，即生成签名HAP。  编译构建APP时，无需生成签名HAP，可将此参数修改为true，从而提升编译构建性能。 |
| debuggable | boolean | 否 | 当前编译产物是否为可调试模式：  true（缺省默认值）：可调试。 false：不可调试。  当使用release的编译模式时，默认为false。工程级别buildOption配置会与模块级别的buildOption进行合并，具体合并规则请参考合并编译选项规则。 |
| resOptions | object | 否 | 资源编译配置项。 |
|    | compression | object | 否 | 对工程预置图片资源进行纹理压缩的编译配置参数。详情请参见表12 compression。 |
| externalNativeOptions | object | 否 | Native编译配置项。 |
|    | path | string | 否 | CMake构建脚本地址，即CMakeLists.txt文件地址。 |
| abiFilters | array | 否 | HarmonyOS当前支持的ABI编译环境，包括：  arm64-v8a x86_64  如不配置该参数，编译时默认为arm64-v8a。 |
| arguments | string/array | 否 | CMake编译参数。 |
| cppFlags | string | 否 | C++编译器参数。 |
| sourceOption | object | 否 | 源码相关配置。使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。 |
|    | workers | array | 否 | 指定使用node.js工作器的JS/TS源代码，源代码在构建过程中单独处理。 |
| nativeLib | object | 否 | Native 库（.so）相关配置。 |
|    | filter | object | 否 | Native 库（.so）文件的筛选选项。配置后优先级高于napiLibFilterOption。 |
|    | excludes | array | 否 | 根据正则表达式排除匹配到的.so文件，匹配到的so文件将不会被打包。 |
| pickFirsts | array | 否 | 按照.so文件的优先级顺序，打包最高优先级的.so文件。详情请参见关于库文件so的优先级。 |
| pickLasts | array | 否 | 按照.so文件的优先级顺序，打包最低优先级的.so文件。详情请参见关于库文件so的优先级。 |
| enableOverride | boolean | 否 | 是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：  true：允许。 false（缺省默认值）：不允许。  |
| select | array | 否 | select提供native产物的精准选择能力，根据包名、版本、产物名称等选择或排除，select的优先级高于excludes、pickFirsts等配置项。详情请参见关于select的使用。 |
| select/package | string | 否 | 包名。 |
| select/version | string | 否 | 包版本。 |
| select/include | array | 否 | 选择打包的native产物。 |
| select/exclude | array | 否 | 排除的native产物。 |
| debugSymbol | object | 否 | 移除.so文件中的符号表、调试信息。 |
|    | strip | boolean | 否 | 是否移除.so文件中的符号表、调试信息。  true（缺省默认值）：移除。 false：不移除。  说明 从DevEco Studio NEXT Developer Beta2（5.0.3.502）版本开始，缺省默认值由false改为true。  |
| exclude | array | 否 | 不对.so文件执行strip的正则表达式规则集。 |
| headerPath | string/array | 否 | 指向包含要导出到此模块的依赖项的标头的目录的路径。 |
| collectAllLibs  | boolean | 否 | 对libs目录收集打包时，是否收集所有后缀的文件。  true：不限制后缀，即收集所有文件（包括无后缀文件）。 false（缺省默认值）：限制后缀为.so，即只收集后缀为.so的文件。  |
| excludeFromHar | boolean | 否 | 是否排除依赖HAR模块中的so，排除时，依赖HAR模块的so不会被打包到本模块产物中。  true（缺省默认值）：排除。 false：不排除。  说明 仅针对HAR模块生效。  |
| excludeSoFromInterfaceHar | boolean | 否 | 编译HSP模块时，打包的HAR产物是否排除so文件，减少.tgz包体积大小。  true：排除。HAR产物不包含so文件，HSP产物包含so文件。 false（缺省默认值）：不排除。HAR产物和HSP产物都包含so文件。  说明  仅针对HSP模块生效。 当HSP模块的工程级或模块级build-profile.json5文件中配置headerPath字段时，excludeSoFromInterfaceHar字段不生效。   |
| napiLibFilterOption  | object | 否 | NAPI库（.so）文件的筛选选项。标记为废弃，不建议使用，推荐使用nativeLib/filter。 |
|    | excludes | array | 否 | 排除的.so文件。罗列的NAPI库将不会被打包。 |
| pickFirsts | array | 否 | 按照.so文件的优先级顺序，打包最高优先级的.so文件。 |
| pickLasts | array | 否 | 按照.so文件的优先级顺序，打包最低优先级的.so文件。 |
| enableOverride | boolean | 否 | 是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：  true：允许。 false（缺省默认值）：不允许。  |
| arkOptions | object | 否 | ArkTS 编译配置。 |
|    | apPath | string | 否 |  说明 API 11及以上版本不再支持，即该字段配置后不再生效。  应用热点信息文件路径。 |
| buildProfileFields | object | 否 | 用于ArkTS的构建配置。自定义类型，key可由数字、英文和下划线、中划线组成，value类型仅可以为string、number、boolean。 |
| hostPGO | boolean | 否 | 是否启用配置文件引导优化功能：  true：启用。 false（缺省默认值）：不启用。  从API 10开始废弃，由于partial模式可能存在兼容性问题，请使用Target AOT能力，不建议使用Host AOT。 |
| types | array | 否 | 自定义类型，可配置包名或d.ts/d.ets文件路径。 |
| tscConfig | object | 否 | 与编译TS语法相关的配置选项。 |
|    | targetESVersion | string | 否 | 指定TS语法编译产物的目标运行时EcmaScript版本，包括：  ES2017 ES2021（缺省默认值）。  |
| autoLazyImport | boolean | 否 | 编译时是否自动将符合lazy-import语法规范的import语句添加"lazy"关键字。仅支持在源码中添加"lazy"关键字，不包含依赖的字节码HAR包或HSP。关于lazy-import的介绍及相关影响请参考延迟加载（lazy import）。  true：添加。 false（缺省默认值）：不添加。  说明 如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。  |
| strictMode | object | 否 | 严格模式。 |
|    | noExternalImportByPath | boolean | 否 | 是否严格检查绝对路径导入方式和相对路径跨模块导入方式。  true：严格检查。 false：不严格检查。  说明 从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当工程级build-profile.json5中useNormalizedOHMUrl配置为true时，noExternalImportByPath缺省默认值为true；当useNormalizedOHMUrl配置为false时，noExternalImportByPath缺省默认值为false。  |
| useNormalizedOHMUrl | boolean | 否 | 是否使用标准化的OHMUrl（OHMUrl的定义参考以下说明）格式，标准化的OHMUrl统一了原有OHMUrl的格式。使用集成态HSP和字节码HAR需使用标准化的OHMUrl格式。  true：使用标准化的OHMUrl格式。 false（缺省默认值）：不使用标准化的OHMUrl格式。  说明  从API 12开始支持。 一个ets文件在编译后会成为安装包的一部分，这个ets文件对应的字节码称为一个字节码段，OHMUrl是用来定位一个字节码段的标识。 若工程引用了HAR/HSP，需确保工程的useNormalizedOHMUrl配置和HAR/HSP的useNormalizedOHMUrl配置保持一致，同时配置为true或false。 从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当useNormalizedOHMUrl设置为true时，不允许通过相对路径跨模块或绝对路径导入文件，oh-package.json5中依赖的包使用的别名需要和依赖包的oh-package.json5的name保持一致，具体的适配指导请参考变更说明。   |
| caseSensitiveCheck | boolean | 否 | 导入文件是否严格校验大小写，支持相对路径和软链接。  true：严格校验。 false（缺省默认值）：不严格校验。  |
| duplicateDependencyCheck | boolean | 否 | 是否校验本地HSP模块有无依赖相同的HAR。仅在Build App(s)起效。  true：如果本地HSP模块依赖了相同的HAR（包括本地/远程、直接/间接），则编译报错。（注意：当依赖链中存在远程HSP，则该远程HSP及其依赖链不参与校验）。 false（默认缺省值）：不启用校验。  |
| harLocalDependencyCheck | boolean | 否 | 是否对HAR产物启用本地依赖校验。  true：如果oh-package.json中的dependencies、dynamicDependencies存在本地依赖，则编译报错。 false（默认缺省值）：不启用校验。  说明 除HAR模块外，HSP模块编译时也会生成HAR产物，该配置同样生效。  |
| nativeCompiler | string | 否 | 指定Native编译时使用的编译器，包括：  Original（缺省默认值）：原有的OpenHarmony Native编译器。 BiSheng：使用毕昇编译器进行Native编译。  说明  从API 12开始支持。   |
配置项
类型
是否必填
说明
packOptions
object
否
打包相关配置项。
buildAppSkipSignHap
boolean
否
是否跳过生成签名HAP：
编译构建APP时，无需生成签名HAP，可将此参数修改为true，从而提升编译构建性能。
debuggable
boolean
否
当前编译产物是否为可调试模式：
当使用release的编译模式时，默认为false。工程级别buildOption配置会与模块级别的buildOption进行合并，具体合并规则请参考合并编译选项规则。
resOptions
object
否
资源编译配置项。
compression
object
否
对工程预置图片资源进行纹理压缩的编译配置参数。详情请参见表12 compression。
externalNativeOptions
object
否
Native编译配置项。
path
string
否
CMake构建脚本地址，即CMakeLists.txt文件地址。
abiFilters
array
否
HarmonyOS当前支持的ABI编译环境，包括：
如不配置该参数，编译时默认为arm64-v8a。
arguments
string/array
否
CMake编译参数。
cppFlags
string
否
C++编译器参数。
sourceOption
object
否
源码相关配置。使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。
workers
array
否
指定使用node.js工作器的JS/TS源代码，源代码在构建过程中单独处理。
nativeLib
object
否
Native 库（.so）相关配置。
filter
object
否
Native 库（.so）文件的筛选选项。配置后优先级高于napiLibFilterOption。
excludes
array
否
根据正则表达式排除匹配到的.so文件，匹配到的so文件将不会被打包。
pickFirsts
array
否
按照.so文件的优先级顺序，打包最高优先级的.so文件。详情请参见关于库文件so的优先级。
pickLasts
array
否
按照.so文件的优先级顺序，打包最低优先级的.so文件。详情请参见关于库文件so的优先级。
enableOverride
boolean
否
是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：
select
array
否
select提供native产物的精准选择能力，根据包名、版本、产物名称等选择或排除，select的优先级高于excludes、pickFirsts等配置项。详情请参见关于select的使用。
select/package
string
否
包名。
select/version
string
否
包版本。
select/include
array
否
选择打包的native产物。
select/exclude
array
否
排除的native产物。
debugSymbol
object
否
移除.so文件中的符号表、调试信息。
strip
boolean
否
是否移除.so文件中的符号表、调试信息。
从DevEco Studio NEXT Developer Beta2（5.0.3.502）版本开始，缺省默认值由false改为true。
exclude
array
否
不对.so文件执行strip的正则表达式规则集。
headerPath
string/array
否
指向包含要导出到此模块的依赖项的标头的目录的路径。
collectAllLibs
boolean
否
对libs目录收集打包时，是否收集所有后缀的文件。
excludeFromHar
boolean
否
是否排除依赖HAR模块中的so，排除时，依赖HAR模块的so不会被打包到本模块产物中。
仅针对HAR模块生效。
excludeSoFromInterfaceHar
boolean
否
编译HSP模块时，打包的HAR产物是否排除so文件，减少.tgz包体积大小。
napiLibFilterOption
object
否
NAPI库（.so）文件的筛选选项。标记为废弃，不建议使用，推荐使用nativeLib/filter。
excludes
array
否
排除的.so文件。罗列的NAPI库将不会被打包。
pickFirsts
array
否
按照.so文件的优先级顺序，打包最高优先级的.so文件。
pickLasts
array
否
按照.so文件的优先级顺序，打包最低优先级的.so文件。
enableOverride
boolean
否
是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：
arkOptions
object
否
ArkTS 编译配置。
apPath
string
否
API 11及以上版本不再支持，即该字段配置后不再生效。
应用热点信息文件路径。
buildProfileFields
object
否
用于ArkTS的构建配置。自定义类型，key可由数字、英文和下划线、中划线组成，value类型仅可以为string、number、boolean。
hostPGO
boolean
否
是否启用配置文件引导优化功能：
从API 10开始废弃，由于partial模式可能存在兼容性问题，请使用Target AOT能力，不建议使用Host AOT。
types
array
否
自定义类型，可配置包名或d.ts/d.ets文件路径。
tscConfig
object
否
与编译TS语法相关的配置选项。
targetESVersion
string
否
指定TS语法编译产物的目标运行时EcmaScript版本，包括：
autoLazyImport
boolean
否
编译时是否自动将符合lazy-import语法规范的import语句添加"lazy"关键字。仅支持在源码中添加"lazy"关键字，不包含依赖的字节码HAR包或HSP。关于lazy-import的介绍及相关影响请参考延迟加载（lazy import）。
如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。
strictMode
object
否
严格模式。
noExternalImportByPath
boolean
否
是否严格检查绝对路径导入方式和相对路径跨模块导入方式。
从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当工程级build-profile.json5中useNormalizedOHMUrl配置为true时，noExternalImportByPath缺省默认值为true；当useNormalizedOHMUrl配置为false时，noExternalImportByPath缺省默认值为false。
useNormalizedOHMUrl
boolean
否
是否使用标准化的OHMUrl（OHMUrl的定义参考以下说明）格式，标准化的OHMUrl统一了原有OHMUrl的格式。使用集成态HSP和字节码HAR需使用标准化的OHMUrl格式。
caseSensitiveCheck
boolean
否
导入文件是否严格校验大小写，支持相对路径和软链接。
duplicateDependencyCheck
boolean
否
是否校验本地HSP模块有无依赖相同的HAR。仅在Build App(s)起效。
harLocalDependencyCheck
boolean
否
是否对HAR产物启用本地依赖校验。
除HAR模块外，HSP模块编译时也会生成HAR产物，该配置同样生效。
nativeCompiler
string
否
指定Native编译时使用的编译器，包括：
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| directories | array | 是 | 资源地址路径。配置示例： 
"directories": [    './AppScope/resource'] |
配置项
类型
是否必填
说明
directories
array
是
资源地址路径。配置示例：
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| artifactName | string | 是 | 自定义产品生成的应用包名称，可由数字、英文字母、中划线、下划线和英文句号（.）组成，支持输入版本号。 |
配置项
类型
是否必填
说明
artifactName
string
是
自定义产品生成的应用包名称，可由数字、英文字母、中划线、下划线和英文句号（.）组成，支持输入版本号。
模块级
下表为"Ability"类型的Module（HAP）对应的模块级build-profile.json5中配置项包含的字段，"Library"类型的Module（HAR和HSP）对应的模块级build-profile.json5中配置项为下表罗列范围的子集。
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| apiType | string | 否 | API模型类型：  stageMode：Stage模型，后续长期演进的模型，推荐使用该模型。 faMode：FA模型。  |
| targets | array | 否 | 定义的target，可配置多个；若配置，数组长度至少为1。 |
|    | name | string | 是 | target名称。 |
| runtimeOS | string | 否 | target的目标运行环境：  HarmonyOS OpenHarmony  |
| config | object | 否 | target相关配置。 |
|    | distroFilter | object | 否 | 应用市场分发规则。在FA模型中使用。详情请参见distroFilter。 |
| distributionFilter | object | 否 | 应用市场分发规则。在Stage模型中使用。详情请参见distributionFilter。 |
| deviceType | array | 否 | target支持的设备范围，具体配置项同module.json5中的deviceTypes。 在FA模型中，对应的文件为config.json。 |
| buildOption | object | 否 | 模块在构建过程中的相关配置，详情请参见表8。关于buildOption的优先级请参考定制编译模式。 |
| atomicService | object | 否 | 元服务相关配置，详情请参见表9，仅支持在Stage模型中配置。 |
| source | object | 否 | target的源码范围。 |
|    | abilities | array | 否 | FA模型工程中支持对Ability源码目录下的page页面进行定制，详情参见表11。配置示例： 
"source": {     "abilities": [      {        "name": ".MainAbility",        "pages": [          "pages/index"        ]      }    ]} |
| pages | array | 否 | Stage模型工程中支持对pages源码目录的page页面进行定制，数组长度至少为1。配置示例： 
"source": {    "pages": [      "pages/Index"    ]} |
| sourceRoots | array | 否 | Stage模型工程中支持对差异化代码空间进行定制，数组长度至少为1。数组中的值有以下限制：  必须唯一； 必须为相对路径； 类型必须为文件夹； 文件夹必须真实存在； 文件夹必须与src/main同级；  当数组中存在多个值时，寻址的优先级为数组中值的顺序。配置示例： 
"source": {  "sourceRoots": [    "./src/default"  ]} |
| resource | object | 否 | target包含的资源目录。 |
|    | directories | array | 否 | 资源目录地址。 |
| output | object | 否 | 定制产品生成的应用包的配置 |
|    | artifactName | string | 是 | 自定义产品生成的应用包名称，可由数字、英文字母、中划线、下划线和英文句号（.）组成，支持输入版本号。 |
| showInServiceCenter | boolean | 否 | 是否显示在服务中心：  true：显示。 false（缺省默认值）：不显示。  |
| buildOption | object | 否 | 模块在构建过程中的相关配置，详情请参考表8，关于buildOption的优先级请参考定制编译模式。 其中仅支持配置resOptions，externalNativeOptions，sourceOption，nativeLib，napiLibFilterOption和arkOptions字段。 其中在FA模型中，arkOptions配置中仅支持配置types字段。 |
| buildOptionSet | array | 否 | 表8构建配置集，其中name字段必填，每个配置都是当前支持的编译过程中所有可用工具的通用配置选项集。关于buildOption的优先级请参考定制编译模式。 |
| buildModeBinder | array | 否 | 构建模式（debug、release 等）与构建配置（buildOption）的关联配置。通过该配置可以将不同的构建配置和target进行组合，并绑定到对应的构建模式上，其中构建模式需要在工程级别的构建模式列表中已定义。 |
|    | buildModeName | string | 否 | 构建模式名称。 |
| mappings | array | 否 | 关联关系。 |
|    | targetName | string | 否 | target名称。 |
| buildOptionName | string | 否 | 构建配置buildOption名称。 |
| entryModules | array | 否 | Feature类型模块所关联的入口模块。 |
配置项
类型
是否必填
说明
apiType
string
否
API模型类型：
targets
array
否
定义的target，可配置多个；若配置，数组长度至少为1。
name
string
是
target名称。
runtimeOS
string
否
target的目标运行环境：
config
object
否
target相关配置。
distroFilter
object
否
应用市场分发规则。在FA模型中使用。详情请参见distroFilter。
distributionFilter
object
否
应用市场分发规则。在Stage模型中使用。详情请参见distributionFilter。
deviceType
array
否
target支持的设备范围，具体配置项同module.json5中的deviceTypes。
在FA模型中，对应的文件为config.json。
buildOption
object
否
模块在构建过程中的相关配置，详情请参见表8。关于buildOption的优先级请参考定制编译模式。
atomicService
object
否
元服务相关配置，详情请参见表9，仅支持在Stage模型中配置。
source
object
否
target的源码范围。
abilities
array
否
FA模型工程中支持对Ability源码目录下的page页面进行定制，详情参见表11。配置示例：
pages
array
否
Stage模型工程中支持对pages源码目录的page页面进行定制，数组长度至少为1。配置示例：
sourceRoots
array
否
Stage模型工程中支持对差异化代码空间进行定制，数组长度至少为1。数组中的值有以下限制：
当数组中存在多个值时，寻址的优先级为数组中值的顺序。配置示例：
resource
object
否
target包含的资源目录。
directories
array
否
资源目录地址。
output
object
否
定制产品生成的应用包的配置
artifactName
string
是
自定义产品生成的应用包名称，可由数字、英文字母、中划线、下划线和英文句号（.）组成，支持输入版本号。
showInServiceCenter
boolean
否
是否显示在服务中心：
buildOption
object
否
模块在构建过程中的相关配置，详情请参考表8，关于buildOption的优先级请参考定制编译模式。
其中仅支持配置resOptions，externalNativeOptions，sourceOption，nativeLib，napiLibFilterOption和arkOptions字段。
其中在FA模型中，arkOptions配置中仅支持配置types字段。
buildOptionSet
array
否
表8构建配置集，其中name字段必填，每个配置都是当前支持的编译过程中所有可用工具的通用配置选项集。关于buildOption的优先级请参考定制编译模式。
buildModeBinder
array
否
构建模式（debug、release 等）与构建配置（buildOption）的关联配置。通过该配置可以将不同的构建配置和target进行组合，并绑定到对应的构建模式上，其中构建模式需要在工程级别的构建模式列表中已定义。
buildModeName
string
否
构建模式名称。
mappings
array
否
关联关系。
targetName
string
否
target名称。
buildOptionName
string
否
构建配置buildOption名称。
entryModules
array
否
Feature类型模块所关联的入口模块。
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| apiVersion | object | 否 | 支持的apiVersion范围。 |
|    | policy | string | 是 | 取值规则：  include：需要包含的value属性。 exclude：需要排除的value属性。  |
| value | array | 是 | 支持的取值为API Version存在的整数值，例如10。 |
| screenShape | object | 否 | 屏幕形状的支持策略。 |
|    | policy | string | 是 | 取值规则：  include：需要包含的value属性。 exclude：需要排除的value属性。  |
| value | array | 是 | 支持的取值范围：  circle：圆形 rect：矩形  |
| screenWindow | object | 否 | 应用运行时窗口的分辨率支持策略。 |
|    | policy | string | 是 | 取值规则：  include：需要包含的value属性。  |
| value | array | 是 | 单个字符串的取值格式为“宽 * 高”，取值为整数像素值，例如"454 * 454"。 |
| screenDensity | object | 否 | 屏幕的像素密度支持策略。 |
|    | policy | string | 是 | 取值规则：  include：需要包含的value属性。 exclude：需要排除的value属性。  |
| value | array | 是 | 取值范围：  sdpi：小规模的屏幕密度（Small-scale Dots per Inch），适用于dpi取值为(0,120]的设备。 mdpi：中规模的屏幕密度（Medium-scale Dots Per Inch），适用于dpi取值为(120,160]的设备。 ldpi：大规模的屏幕密度（Large-scale Dots Per Inch），适用于dpi取值为(160,240]的设备。 xldpi：大规模的屏幕密度（Extra Large-scale Dots Per Inch），适用于dpi取值为(240,320]的设备。 xxldpi：大规模的屏幕密度（Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(320，480]的设备。 xxxldpi：表示大规模的屏幕密度（Extra Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(480, 640]的设备。  |
| countryCode | object | 否 | 应用需要分发的国家地区码。 |
|    | policy | string | 是 | 取值规则：  include：需要包含的value属性。 exclude：需要排除的value属性。  |
| value | array | 是 | 国家地区码取值，具体值以ISO-3166-1标准为准。支持多个国家和地区枚举定义。 |
配置项
类型
是否必填
说明
apiVersion
object
否
支持的apiVersion范围。
policy
string
是
取值规则：
value
array
是
支持的取值为API Version存在的整数值，例如10。
screenShape
object
否
屏幕形状的支持策略。
policy
string
是
取值规则：
value
array
是
支持的取值范围：
screenWindow
object
否
应用运行时窗口的分辨率支持策略。
policy
string
是
取值规则：
value
array
是
单个字符串的取值格式为“宽 * 高”，取值为整数像素值，例如"454 * 454"。
screenDensity
object
否
屏幕的像素密度支持策略。
policy
string
是
取值规则：
value
array
是
取值范围：
countryCode
object
否
应用需要分发的国家地区码。
policy
string
是
取值规则：
value
array
是
国家地区码取值，具体值以ISO-3166-1标准为准。支持多个国家和地区枚举定义。
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| name  | string | 否 | 构建配置方案buildOption的名称。 |
| debuggable  | boolean | 否 | 当前编译产物是否为可调试模式(debug)：  true（缺省默认值）：可调试。 false：不可调试。  当使用release的构建模式时，默认为false。 |
| copyFrom  | string | 否 | 从同模块中已有的buildOption复制配置，配置已定义的buildOption名称。 |
| resOptions  | object | 否 | 资源编译配置项。 |
|    | compression | object | 否 | 对模块预置图片资源进行纹理压缩的编译配置参数。详情请参见表12 compression。 |
| externalNativeOptions  | object | 否 | Native编译配置项。 |
|    | path  | string | 否 | CMake构建脚本地址，即CMakeLists.txt文件地址。 |
| abiFilters  | array | 否 | HarmonyOS当前支持的ABI编译环境，包括：  arm64-v8a x86_64  如不配置该参数，编译时默认为arm64-v8a。若配置，则数组长度至少至少1。 |
| cppFlags  | string | 否 | C++编译器参数。 |
| cFlags  | string | 否 | C编译参数。 |
| arguments  | string/array | 否 | CMake编译参数。 |
| targets  | array | 否 | 指定hvigor应构建的CMake项目中的库和可执行目标。 |
| sourceOption  | object | 否 | 源码相关配置。使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。 |
|    | workers  | array | 否 | 指定使用node.js工作器的JS/TS源代码，源代码在构建过程中单独处理。 |
| nativeLib | object | 否 | Native 库（.so）相关配置。 |
|    | filter  | object | 否 | Native 库（.so）文件的筛选选项。 |
|    | excludes | array | 否 | 根据正则表达式排除匹配到的.so文件，匹配到的so文件将不会被打包。 |
| pickFirsts | array | 否 | 按照.so文件的优先级顺序，打包最高优先级的.so文件。详情请参见关于库文件so的优先级。 |
| pickLasts | array | 否 | 按照.so文件的优先级顺序，打包最低优先级的.so文件。详情请参见关于库文件so的优先级。 |
| enableOverride | boolean | 否 | 是否允许当.so重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：  true：允许。 false（缺省默认值）：不允许。  |
| select | array | 否 | select提供native产物的精准选择能力，根据包名、版本、产物名称等选择或排除，select的优先级高于excludes、pickFirsts等配置项。详情请参见关于select的使用。 |
| select/package | string | 否 | 包名。 |
| select/version | string | 否 | 包版本。 |
| select/include | array | 否 | 选择打包的native产物。 |
| select/exclude | array | 否 | 排除的native产物。 |
| debugSymbol   | object | 否 | 移除.so文件中的符号表、调试信息。 |
|    | strip | boolean | 否 | 是否移除.so文件中的符号表、调试信息。  true（缺省默认值）：移除。 false：不移除。  说明 从DevEco Studio NEXT Developer Beta2（5.0.3.502）版本开始，缺省默认值由false改为true。  |
| exclude | array | 否 | 不对.so文件执行strip的正则表达式规则集。 |
| headerPath | string/array | 否 | 指向包含要导出到此模块的依赖项的标头的目录的路径。 |
| collectAllLibs | boolean | 否 | 对libs目录收集打包时，是否收集所有后缀的文件。  true：不限制后缀，即收集所有文件（包括无后缀文件）。 false：限制后缀为.so，即只收集后缀为.so的文件。  |
| librariesInfo | array | 否 | 声明so的透传依赖信息。具体可参考依赖透传。 |
|    | name | string | 是 | 本模块so库的名称。 |
| linkLibraries | array | 是 | so库的依赖信息，格式为"依赖包名::依赖so名称"。 |
| excludeFromHar | boolean | 否 | 是否排除依赖HAR模块中的so，排除时，依赖HAR模块的so不会被打包到本模块产物中。  true（缺省默认值）：排除。 false：不排除。  说明 仅针对HAR模块生效。  |
| excludeSoFromInterfaceHar | boolean | 否 | 编译HSP模块时，打包的HAR产物是否排除so文件，减少.tgz包体积大小。  true：排除。HAR产物不包含so文件，HSP产物包含so文件。 false（缺省默认值）：不排除。HAR产物和HSP产物都包含so文件。  说明  仅针对HSP模块生效。 当HSP模块的工程级或模块级build-profile.json5文件中配置headerPath字段时，excludeSoFromInterfaceHar字段不生效。   |
| napiLibFilterOption | object | 否 | NAPI库（.so）文件的筛选选项。标记为废弃，不建议使用，推荐使用nativeLib/filter。 |
|    | excludes | array | 否 | 排除的.so文件。罗列的NAPI库将不会被打包。 |
| pickFirsts | array | 否 | 按照.so文件的优先级顺序，打包最高优先级的.so文件。 |
| pickLasts | array | 否 | 按照.so文件的优先级顺序，打包最低优先级的.so文件。 |
| enableOverride | boolean | 否 | 是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：  true：允许。 false（缺省默认值）：不允许。  |
| ignoreArchitectures | array | 否 | 忽略运行系统CPU架构的.so文件。 |
| arkOptions | object | 否 | ArkTS编译配置。 |
|    | runtimeOnly | object | 否 | 配置动态import的文件和依赖的包名，仅支持在Stage模型中配置。 runtimeOnly为非必选配置，当工程需要以变量方式动态import文件、目录的相对路径或三方包时，需要通过配置runtimeOnly来确保其加入编译流程。详情请参考动态import变量表达式。 |
|    | sources | array | 否 | 配置动态import的文件/文件夹的相对路径。 配置的文件/文件夹必须在工程中真实存在，且文件的后缀只能为ets或ts。 |
| packages | array | 否 | 配置动态import依赖的包名。 该包名需要和工程级/模块级oh-package.json5的dependencies中的名字保持一致。 |
| apPath | string | 否 |  说明 API 11及以上版本不再支持，即该字段配置后不再生效。  应用热点信息文件路径。 |
| hostPGO | boolean | 否 | 是否启用配置文件引导优化功能：  true：启用。 false（缺省默认值）：不启用。  从API 10开始废弃。 |
| types | array | 否 | 自定义类型，可配置包名或d.ts/d.ets文件路径。 |
| obfuscation | object | 否 | 代码混淆配置，详情请参见表10。 代码混淆仅针对Release模式打包生效。 更多关于代码混淆的内容，请参见代码混淆。 |
| buildProfileFields | object | 否 | 运行时可获取的自定义构建参数，支持键值对配置，仅支持在Stage模型中配置，配置示例： 
"arkOptions": {    "buildProfileFields": {      "buildOptionSetData": "BuildOptionSetDataRelease",      "data": "DataRelease"    }} 当前支持配置string/number/boolean类型的自定义参数。 更多关于如何在运行时获取编译构建参数的内容，请参见获取自定义编译参数。 |
| integratedHsp | boolean | 否 | 是否为集成态HSP。  true：是。 false（缺省默认值）：否。  说明  从API 12开始支持。 需在工程级build-profile.json5中配置useNormalizedOHMUrl为true后使用。 该字段仅在HSP模块中配置后生效。   |
| transformLib | string | 否 | 字节码插桩插件配置，允许开发者在编译时对字节码进行插桩修改，仅支持Stage模型，格式为相对路径，不同系统要求的文件类型如下，文件内容需要在对应平台生成，不能拷贝修改后缀名混用。详情请参考编译期自定义修改方舟字节码。  Windows：.dll文件。 Linux/Mac：.so文件。  说明  Mac环境下添加配置后插桩未生效的问题请参考FAQ。 HAR模块仅字节码HAR配置生效，非字节码HAR配置不生效。   |
| branchElimination | boolean | 否 | 是否启用代码分支裁剪，减少编译产物大小，开启后，在release编译模式下，不会被执行到的代码分支会被裁剪掉，示例如下： 
# 编译生成的BuildProfile文件export const DEBUG = false;export const VERSION_CODE = 100;# 开发者自定义的ets文件import { DEBUG } from 'BuildProfile';import { VERSION_CODE } from 'BuildProfile';if (DEBUG)  {XXX} // 该分支会被裁剪掉else  {XXX}if (VERSION_CODE){XXX} // 该语法发生了类型转换，不支持代码裁剪。if (VERSION_CODE === 100){XXX} // 若需要裁剪代码，使用该方式，显式指定判断条件为boolean类型。  true：启用（将导致使用"ApplyChanges"功能时，对const声明的常量的值进行的修改可能不生效）。 false（缺省默认值）：不启用。  说明  仅支持API 11及以上的Stage模型。 仅支持const声明的bool类型常量和const声明的string/number类型常量的判断表达式。 不支持间接导入，例如A文件中定义const变量A1，B文件导入A1，导出B1，ets导入B1进行判断，无法进行裁剪。   |
| byteCodeHar | boolean | 否 | 是否支持字节码HAR，仅在HAR模块中配置后生效。详情请参考构建字节码HAR。  true：支持。 false：不支持。  说明  从API 12开始支持。 从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当工程级build-profile.json5中useNormalizedOHMUrl配置为true时，byteCodeHar缺省默认值为true；当useNormalizedOHMUrl配置为false时，byteCodeHar缺省默认值为false。   |
| bundledDependencies | boolean | 否 | 是否支持将多个源码HAR（本地+远程）打包成一个字节码HAR。字节码HAR、HSP、npm不会被打包进去，仅会合并源码HAR。  true：支持。 false（缺省默认值）：不支持。  说明  仅支持字节码HAR配置该字段。 从API 12开始支持。 仅支持Stage模型。   |
| autoLazyImport | boolean | 否 | 编译时是否自动将符合lazy-import语法规范的import语句添加"lazy"关键字。仅支持在源码中添加"lazy"关键字，不包含依赖的字节码HAR包或HSP。关于lazy-import的介绍及相关影响请参考延迟加载（lazy import）。  true：添加。 false（缺省默认值）：不添加。  说明 如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。  |
配置项
类型
是否必填
说明
name
string
否
构建配置方案buildOption的名称。
debuggable
boolean
否
当前编译产物是否为可调试模式(debug)：
当使用release的构建模式时，默认为false。
copyFrom
string
否
从同模块中已有的buildOption复制配置，配置已定义的buildOption名称。
resOptions
object
否
资源编译配置项。
compression
object
否
对模块预置图片资源进行纹理压缩的编译配置参数。详情请参见表12 compression。
externalNativeOptions
object
否
Native编译配置项。
path
string
否
CMake构建脚本地址，即CMakeLists.txt文件地址。
abiFilters
array
否
HarmonyOS当前支持的ABI编译环境，包括：
如不配置该参数，编译时默认为arm64-v8a。若配置，则数组长度至少至少1。
cppFlags
string
否
C++编译器参数。
cFlags
string
否
C编译参数。
arguments
string/array
否
CMake编译参数。
targets
array
否
指定hvigor应构建的CMake项目中的库和可执行目标。
sourceOption
object
否
源码相关配置。使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。
workers
array
否
指定使用node.js工作器的JS/TS源代码，源代码在构建过程中单独处理。
nativeLib
object
否
Native 库（.so）相关配置。
filter
object
否
Native 库（.so）文件的筛选选项。
excludes
array
否
根据正则表达式排除匹配到的.so文件，匹配到的so文件将不会被打包。
pickFirsts
array
否
按照.so文件的优先级顺序，打包最高优先级的.so文件。详情请参见关于库文件so的优先级。
pickLasts
array
否
按照.so文件的优先级顺序，打包最低优先级的.so文件。详情请参见关于库文件so的优先级。
enableOverride
boolean
否
是否允许当.so重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：
select
array
否
select提供native产物的精准选择能力，根据包名、版本、产物名称等选择或排除，select的优先级高于excludes、pickFirsts等配置项。详情请参见关于select的使用。
select/package
string
否
包名。
select/version
string
否
包版本。
select/include
array
否
选择打包的native产物。
select/exclude
array
否
排除的native产物。
debugSymbol
object
否
移除.so文件中的符号表、调试信息。
strip
boolean
否
是否移除.so文件中的符号表、调试信息。
从DevEco Studio NEXT Developer Beta2（5.0.3.502）版本开始，缺省默认值由false改为true。
exclude
array
否
不对.so文件执行strip的正则表达式规则集。
headerPath
string/array
否
指向包含要导出到此模块的依赖项的标头的目录的路径。
collectAllLibs
boolean
否
对libs目录收集打包时，是否收集所有后缀的文件。
librariesInfo
array
否
声明so的透传依赖信息。具体可参考依赖透传。
name
string
是
本模块so库的名称。
linkLibraries
array
是
so库的依赖信息，格式为"依赖包名::依赖so名称"。
excludeFromHar
boolean
否
是否排除依赖HAR模块中的so，排除时，依赖HAR模块的so不会被打包到本模块产物中。
仅针对HAR模块生效。
excludeSoFromInterfaceHar
boolean
否
编译HSP模块时，打包的HAR产物是否排除so文件，减少.tgz包体积大小。
napiLibFilterOption
object
否
NAPI库（.so）文件的筛选选项。标记为废弃，不建议使用，推荐使用nativeLib/filter。
excludes
array
否
排除的.so文件。罗列的NAPI库将不会被打包。
pickFirsts
array
否
按照.so文件的优先级顺序，打包最高优先级的.so文件。
pickLasts
array
否
按照.so文件的优先级顺序，打包最低优先级的.so文件。
enableOverride
boolean
否
是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：
ignoreArchitectures
array
否
忽略运行系统CPU架构的.so文件。
arkOptions
object
否
ArkTS编译配置。
runtimeOnly
object
否
配置动态import的文件和依赖的包名，仅支持在Stage模型中配置。
runtimeOnly为非必选配置，当工程需要以变量方式动态import文件、目录的相对路径或三方包时，需要通过配置runtimeOnly来确保其加入编译流程。详情请参考动态import变量表达式。
sources
array
否
配置动态import的文件/文件夹的相对路径。
配置的文件/文件夹必须在工程中真实存在，且文件的后缀只能为ets或ts。
packages
array
否
配置动态import依赖的包名。
该包名需要和工程级/模块级oh-package.json5的dependencies中的名字保持一致。
apPath
string
否
API 11及以上版本不再支持，即该字段配置后不再生效。
应用热点信息文件路径。
hostPGO
boolean
否
是否启用配置文件引导优化功能：
从API 10开始废弃。
types
array
否
自定义类型，可配置包名或d.ts/d.ets文件路径。
obfuscation
object
否
代码混淆配置，详情请参见表10。
代码混淆仅针对Release模式打包生效。
更多关于代码混淆的内容，请参见代码混淆。
buildProfileFields
object
否
运行时可获取的自定义构建参数，支持键值对配置，仅支持在Stage模型中配置，配置示例：
当前支持配置string/number/boolean类型的自定义参数。
更多关于如何在运行时获取编译构建参数的内容，请参见获取自定义编译参数。
integratedHsp
boolean
否
是否为集成态HSP。
transformLib
string
否
字节码插桩插件配置，允许开发者在编译时对字节码进行插桩修改，仅支持Stage模型，格式为相对路径，不同系统要求的文件类型如下，文件内容需要在对应平台生成，不能拷贝修改后缀名混用。详情请参考编译期自定义修改方舟字节码。
branchElimination
boolean
否
是否启用代码分支裁剪，减少编译产物大小，开启后，在release编译模式下，不会被执行到的代码分支会被裁剪掉，示例如下：
byteCodeHar
boolean
否
是否支持字节码HAR，仅在HAR模块中配置后生效。详情请参考构建字节码HAR。
bundledDependencies
boolean
否
是否支持将多个源码HAR（本地+远程）打包成一个字节码HAR。字节码HAR、HSP、npm不会被打包进去，仅会合并源码HAR。
autoLazyImport
boolean
否
编译时是否自动将符合lazy-import语法规范的import语句添加"lazy"关键字。仅支持在源码中添加"lazy"关键字，不包含依赖的字节码HAR包或HSP。关于lazy-import的介绍及相关影响请参考延迟加载（lazy import）。
如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| preloads | array | 否 | 定义当前模块运行时预加载的模块。 |
|    | moduleName | string | 否 | 预加载的模块名称。 |
配置项
类型
是否必填
说明
preloads
array
否
定义当前模块运行时预加载的模块。
moduleName
string
否
预加载的模块名称。
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| ruleOptions | object | 否 | 混淆规则配置。 |
|    | enable | boolean | 是 | 是否启用代码混淆：  true：启用。 false（默认值）：不启用。  说明 从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认值由true改为false。  |
| files | array | 否 | 配置混淆规则文件的相对路径，默认使用obfuscation-rules.txt文件。文件中配置的混淆规则仅在本模块编译时生效（包含依赖代码）。 说明  规则文件中支持配置所有混淆规则。 支持配置多个文件，文件名称支持自定义，当存在多个混淆规则文件时，规则合并以及合并后的作用范围可参考混淆规则合并策略。   |
| consumerFiles | string/array | 否 | 仅HAR模块可配置，配置传递给集成方的混淆规则文件的相对路径，支持配置多个文件，文件名称支持自定义。 说明  为保证HAR模块可被正确集成使用，若有不希望被集成方混淆的内容，建议在规则文件中配置对应的保留选项，例如HAR模块中导出的变量或函数。   规则文件中配置的混淆选项会与集成方的混淆规则进行合并，进而影响集成方的编译混淆，因此，建议仅配置保留选项。   |
配置项
类型
是否必填
说明
ruleOptions
object
否
混淆规则配置。
enable
boolean
是
是否启用代码混淆：
从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认值由true改为false。
files
array
否
配置混淆规则文件的相对路径，默认使用obfuscation-rules.txt文件。文件中配置的混淆规则仅在本模块编译时生效（包含依赖代码）。
consumerFiles
string/array
否
仅HAR模块可配置，配置传递给集成方的混淆规则文件的相对路径，支持配置多个文件，文件名称支持自定义。
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| abilities | array | 否 | 自定义目标的能力范围。 |
|    | name | string | 是 | 指定目标选择的能力的名称。 |
| pages | array | 否 | 指定目标选择的能力的页面。 |
| res | array | 否 | 指定资源目录。 |
| icon | string | 否 | 指定能力图标文件的索引，格式为"$media:ability_icon"。 |
| label | string | 否 | 指定对用户可见的性能名称。标签值设置为该名称的资源索引，以支持多语言。 |
| launchType | string | 否 | 指定能力的启动模式：  multiton：多实例模式，每次启动创建一个新实例。   standard：同multiton，建议使用multiton替代。 singleton（缺省默认值）：单实例模式，仅第一次启动创建新实例。 specified：指定实例模式，运行时由开发者决定是否创建新实例。  |
配置项
类型
是否必填
说明
abilities
array
否
自定义目标的能力范围。
name
string
是
指定目标选择的能力的名称。
pages
array
否
指定目标选择的能力的页面。
res
array
否
指定资源目录。
icon
string
否
指定能力图标文件的索引，格式为"$media:ability_icon"。
label
string
否
指定对用户可见的性能名称。标签值设置为该名称的资源索引，以支持多语言。
launchType
string
否
指定能力的启动模式：
| 配置项 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| media | object | 否 | 对资源目录下media目录的图片进行纹理压缩的配置参数。 |
|    | enable | boolean | 否 | 是否对media图片启用纹理压缩。  true：启用。 false（缺省默认值）：不启用。  说明  在linux系统的构建场景下，请确认系统环境已安装libGL1库。 对图片进行纹理压缩会改变文件名称和内容，在分层图标以及二次编辑的场景下会引起图片显示异常，请进一步使用filters排除掉这部分文件。   |
| filters | array | 否 | 文件过滤配置参数。 说明 编译过程中会依次遍历图片文件，并与filters条件进行匹配，一旦匹配成功，则完成该图片的处理。当工程级和模块级同时配置时，先按照模块级的过滤条件匹配，一旦匹配成功，则忽略工程级的过滤条件；如果模块级的没有匹配成功，继续按工程级的条件进行匹配。  |
|    | method | object | 是 | 纹理压缩的方式。 |
|    | type | string | 是 | 转换类型。  astc（Adaptive Scalable Texture Compression）：自适应可变纹理压缩，一种对GPU友好的纹理格式，可在设备侧更快地显示，有更少的内存占用。 sut（SUper compression for Texture） ：纹理超压缩，可在设备侧更快地显示，有更少的内存占用，相比astc具备更大压缩率和更少ROM占用。  |
| blocks | string | 是 | astc/sut转换类型的扩展参数，决定画质和压缩率，当前仅支持"4x4"。 |
| files | object | 否 | 指定用来参与压缩的文件，与exclude字段配合使用。 |
|    | path | array | 否 | 指定“按路径匹配”的过滤条件，符合glob规范，格式为相对路径，配置示例： 
"path": [  "./entry/src/main/resources/base/media/big_picture.png"] |
| size | array | 否 | 二维数组，指定“按大小匹配”的过滤条件，格式为[min,max]，闭区间，表示大小从min到max之间的文件，配置示例： 
"size"：[  [0, '1k'],      // 0 ~ 1*1024  ['1024', '2k'], // 1024 ~ 2*1024  ['3K']          // 3*1024 ~ 无限大]  每个数值可以填数字、字符串或字符串中带单位(大小写均可)。 单位K/k=1024，M/m=1024*1024，G/g=1024*1024*1024。 区间最大值可省略，表示无限大。  |
| resolution | array | 否 | 二维数组，指定“按分辨率匹配”的过滤条件，配置示例： 
resolution:[  [    { width:32, height:32 },   // 最小宽高    { width:64, height:64 },   // 最大宽高  ],                           // 分辨率在32*32到64*64之间的图片  [    { width:200, height:200 }, // 最小宽高    // 此处第2个不填表示最大宽高是无限大  ],                           // 分辨率大于200*200的图片]  width和height只能是数字。 最大宽高可以省略，表示无限大。  |
| exclude | object | 否 | 从files中剔除掉不需要压缩的文件。 |
|    | path | array | 否 | 同files/path。 |
| size | array | 否 | 同files/size。 |
| resolution | array | 否 | 同files/resolution。 |
配置项
类型
是否必填
说明
media
object
否
对资源目录下media目录的图片进行纹理压缩的配置参数。
enable
boolean
否
是否对media图片启用纹理压缩。
filters
array
否
文件过滤配置参数。
编译过程中会依次遍历图片文件，并与filters条件进行匹配，一旦匹配成功，则完成该图片的处理。当工程级和模块级同时配置时，先按照模块级的过滤条件匹配，一旦匹配成功，则忽略工程级的过滤条件；如果模块级的没有匹配成功，继续按工程级的条件进行匹配。
method
object
是
纹理压缩的方式。
type
string
是
转换类型。
blocks
string
是
astc/sut转换类型的扩展参数，决定画质和压缩率，当前仅支持"4x4"。
files
object
否
指定用来参与压缩的文件，与exclude字段配合使用。
path
array
否
指定“按路径匹配”的过滤条件，符合glob规范，格式为相对路径，配置示例：
```json
"path": [
"./entry/src/main/resources/base/media/big_picture.png"
]
```
size
array
否
二维数组，指定“按大小匹配”的过滤条件，格式为[min,max]，闭区间，表示大小从min到max之间的文件，配置示例：
resolution
array
否
二维数组，指定“按分辨率匹配”的过滤条件，配置示例：
exclude
object
否
从files中剔除掉不需要压缩的文件。
path
array
否
同files/path。
size
array
否
同files/size。
resolution
array
否
同files/resolution。
模块级build-profile.json5的示例如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-task-process-V14
爬取时间: 2025-04-30 07:34:00
来源: Huawei Developer
本章节将对构建的任务进行说明，可以更直观得了解到构建的任务流程。
任务流程图
HAP基础任务流程图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150645.19405040143676346606036287199204:50001231000000:2800:3D8498D1215446E8426CDCB16B516A970250D7105FABD1EEA32971FD46DA47AD.png?needInitFileName=true?needInitFileName=true)
HSP基础任务流程图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150645.46386710883619124603580206290717:50001231000000:2800:7B99CB362853ECD0793FCC7AA7AD44934673E528AF785D787B75CDD8DF9FD71B.png?needInitFileName=true?needInitFileName=true)
HAR基础任务流程图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150645.55715192862666012544774455728964:50001231000000:2800:C980D384B0D8AAB3293DF056A5E967FACBF1A5CB8B47349DD224A1EB5FDDC6EB.png?needInitFileName=true?needInitFileName=true)
使用命令查看任务
在DevEco Studio中可以通过以下命令获得任务相关的信息
获取任务树时会根据工程中的模块将模块中注册的任务树以下图形式输出：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150645.24766855293536560633194072772669:50001231000000:2800:81A384B2BAD0131D44D42DDD4FBB8E5EE9312251A3B269B6C0E39DC212114FEF.png?needInitFileName=true?needInitFileName=true)
执行顺序举例说明：如图所示，assembleHap依赖signHap，signHap依赖于packageHap；则任务执行顺序则为packageHap->signHap->assembleHap。
任务详细说明
根据任务职能的不同主要分为以下几个类型的任务。
| 任务类别  | 任务说明  |
| --- | --- |
| Hook  | hook任务  |
| ArkTS  | ArkTS编译相关任务  |
| JS  | JS编译相关任务  |
| Resources  | 资源编译、处理、链接、合并相关的任务  |
| Package  | 打包相关的任务  |
| Sign  | 签名相关的任务  |
| Verification  | 验证项目或者依赖项设置等相关的任务  |
| Generate  | 生成和转换前置文件等相关的任务  |
| Config  | 生成，合并，处理配置文件等相关的任务  |
| Native  | Native编译等相关的任务  |
| Help  | 查询hvigor帮助信息的相关任务  |
| Other  | 未分类的任务  |
任务类别
任务说明
Hook
hook任务
ArkTS
ArkTS编译相关任务
JS
JS编译相关任务
Resources
资源编译、处理、链接、合并相关的任务
Package
打包相关的任务
Sign
签名相关的任务
Verification
验证项目或者依赖项设置等相关的任务
Generate
生成和转换前置文件等相关的任务
Config
生成，合并，处理配置文件等相关的任务
Native
Native编译等相关的任务
Help
查询hvigor帮助信息的相关任务
Other
未分类的任务
Hook
ArkTS
JS
Resources
Package
Sign
Verification
Generate
Config
Native
Help
Other
Sync
Init
该任务类型与Sync下的init不同，该过程中无具体任务，主要负责执行调用hvigor前的准备工作。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-compile-build-V14
爬取时间: 2025-04-30 07:34:35
来源: Huawei Developer
HAP/HSP构建产物说明
以HAP为例，release模式的构建产物一般包含以下文件：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150645.84078042060271428080857621704675:50001231000000:2800:43F9683B7A9E10A77CDD4A3B02B097262188580DDAF02C6B47C499875E9F694F.png?needInitFileName=true?needInitFileName=true)
HAR构建产物说明
详情请参考构建HAR。
App构建产物说明
APP构建产物如下，其中包名取决于个人项目中的模块名，与下图可能不同：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150645.38267455774883132441481320668328:50001231000000:2800:FAD345FFEEBEA72F90549F1484D72F8236DD720BB1094D871002E1E8AD89795C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-configuration-V14
爬取时间: 2025-04-30 07:35:09
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-multi-module-V14
爬取时间: 2025-04-30 07:35:43
来源: Huawei Developer
模块是应用/元服务的基本功能单元，包含了源代码、资源文件、第三方库及应用/元服务配置文件，Hvigor支持工程多模块管理。您可在工程下的build-profile.json5配置文件中增加对应模块信息，即可对模块进行工程绑定和管理，或在hvigorconfig.ts脚本中动态添加或排除某个模块。同时也支持分模块配置、编译和打包。
多模块配置
静态配置模块
工程级build-profile.json5配置文件中"modules"字段，用于记录工程下的模块信息，主要包含模块名称、模块的源码路径以及模块的 target 信息。target信息主要用于定制多目标构建产物，更多详细信息可参考配置多目标产物章节。
例如以下目录中存在两个模块目录，您可在工程下的build-profile.json5配置文件，添加模块信息，使得模块与工程进行绑定：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150645.38843214917872737808065941054949:50001231000000:2800:19D89232F2B5479E141E4BCDF86E3C144C85BDBEE58E14410A8F06B592AB301B.png?needInitFileName=true?needInitFileName=true)
其他配置文件：
工程下的build-profile.json5文件中模块配置示例：
动态配置模块
Hvigor支持在hvigorconfig.ts脚本中动态添加或排除某个模块，具体API及示例可参考HvigorConfig。
分模块编译
Hvigor支持分模块编译和打包。您可以通过以下两种方式进行分模块构建：
更多构建HAR/HSP包命令，可参考命令行工具章节。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-dependencies-V14
爬取时间: 2025-04-30 07:36:18
来源: Huawei Developer
应用/元服务支持通过包管理工具ohpm来安装、共享、分发代码，管理项目的依赖关系。本文介绍了在您的项目中如何添加依赖项。
您可在工程或模块下的oh-package.json5文件中的dependencies（生产依赖）/devDependencies（开发依赖）字段中指定依赖项，以上两种依赖字段均支持引用远程三方包、本地文件夹和本地HAR/HSP三种方式。oh-package.json5文件中的dynamicDependencies（动态依赖）仅限于动态依赖HSP的使用场景。以下配置以dependencies为例。
远程三方包
本地文件夹
本地HAR/HSP包
依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会存储在对应模块的oh_modules目录下。
更多关于oh-package.json5文件说明，请参考oh-package.json5。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-customized-multi-targets-and-products-V14
爬取时间: 2025-04-30 07:36:53
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-customized-multi-targets-and-products-guides-V14
爬取时间: 2025-04-30 07:37:27
来源: Huawei Developer
通常情况下，应用厂商会根据不同的部署环境，不同的目标人群，不同的运行环境等，将同一个应用定制为不同的版本，如国内版、国际版、普通版、VIP版、免费版、付费版等。针对以上场景，DevEco Studio支持通过少量的代码配置以实例化不同的差异版本，在编译构建过程中实现一个应用构建出不同的目标产物版本，从而实现源代码、资源文件等的高效复用。
在了解HarmonyOS应用的多目标构建产物如何定制前，先了解target和product的概念：
定制HAP多目标构建产物
每一个Entry/Feature模块均支持定制不同的target，通过在模块中的build-profile.json5文件中实现差异化定制，当前支持HAP包名、设备类型（deviceType）、源码集（source）、资源（resource）、buildOption配置项（如C++依赖的.so、混淆配置、abi类型、cppFlags等）、分发规则（distributionFilter）的定制。
定义目标产物target
每一个target对应一个定制的HAP，因此，在定制HAP多目标构建产物前，应提前规划好需要定制的target名称。例如，以ArkTS Stage模型为例，定义一个免费版和付费版，模块级build-profile.json5文件示例如下：
按照上述target的定义，在编译构建时，会同时打包生成default、free和pay三个不同的HAP。
定义产物的HAP包名
每一个target均可以指定产物命名。
如果已配置签名，target产物对应的HAP包名为开发者定制的名称；如果未配置签名，target产物对应的HAP包名为开发者定制的名称+unsigned。
定义产物的deviceType
每一个target均可以指定支持的设备类型deviceType，也可以不定义。如果不定义，则该target默认支持config.json或module.json5中定义的设备类型。
同时，在定义每个target的deviceType时，支持的设备类型必须在config.json或module.json5中已经定义。例如，在上述定义的3个target中，分别定义default默认支持所有设备类型，free和pay版本只支持phone设备。
定义产物的distributionFilter
在未定义target的分发规则distributionFilter时，以module配置distroFilter/distributionFilter分发规则为准。
针对多target存在相同设备类型deviceType的场景，相同设备类型的target需要指定分发规则distributionFilter。
如果是FA工程，请将distributionFilter字段替换为distroFilter。
定义产物preloads的分包
对于元服务，每一个target均可以指定preloads的分包，也可以不定义。如果不定义，则以module.json5中的配置为准。
定义产物的source源码集-pages
对于source源码集的定制，由于Stage模型和FA模型的差异，Stage模型支持对pages源码目录的page页面进行定制，FA模型则支持对Ability源码目录下的page页面进行定制。
定义产物的source源码集-sourceRoots
在模块的主代码空间（src/main）下，承载着开发者编写的公共代码。如果开发者需要实现不同target之间的差异化逻辑，可以使用差异化代码空间（sourceRoots）。配合差异化代码空间的能力，可以在主代码空间中代码不变的情况下，针对不同的target，编译对应的代码到最终产物中。
概念说明
例如以下工程目录：
规格限制
1. import xxx from '<packageName>/sourcePath/sourceFileName' ：通过packageName的方式，省略sourceRoot，可以实现不同target下的差异化构建。
2. 支持hap、hsp、har（请注意：开启文件/文件夹名称混淆的har模块需要使用-keep-file-name指定sourceRoot，sourcePath，sourceFileName对应的文件/文件夹名称不被混淆）。
3. 不支持跨模块引用。
4. 不支持动态import。
编译时模块target的选择优先级说明
在模块编译的过程中，该模块使用的sourceRoots由当前模块编译时的target来决定。当前模块编译时选择target的优先级则为：命令行显式指定 > 直接引用方target > default。
如以下示例：
hap -> hsp -> har（->表示依赖）
其中hap和hsp存在三个target：default、custom、static，而har存在两个target：default、static。
-  hap: custom，命令行显式指定； hsp: custom，命令行没有显式指定，则基于直接引用方查找，hsp的直接引用方为hap，hap的target为custom，hsp存在该target，则hsp的target为custom； har: default，命令行没有显式指定，则基于直接引用方查找，har的直接引用方为hsp，hsp的target为custom，har不存在该target，则har的target为default；
-  hap: custom，命令行显式指定； hsp: static，命令行显式指定； har: static，命令行没有显式指定，则基于直接引用方查找，har的直接引用方为hsp，hsp的target为static，har存在该target，则har的target为static。
示例
1. 在entry模块的build-profile.json5中添加sourceRoots：
2. 在src目录下新增default/Test.ets和custom/Test.ets，新增后的模块目录结构：
3. 在default/Test.ets中写入代码：
4. 在custom/Test.ets中写入代码：
5. 修改src/main/ets/pages/Index.ets的代码：
```typescript
import { getName } from 'entry/Test'; // 其中entry为模块级的oh-package.json5中的name字段的值
@Entry
@Component
struct Index {
@State message: string = getName();
build() {
RelativeContainer() {
Text(this.message)
}
.height('100%')
.width('100%')
}
}
```
6. 在工程级的build-profile.json5中配置targets：
7. Sync完成后，选择entry的target为default，点击Run，界面展示default；选择entry的target为custom，点击Run，则界面展示custom。
定义产物的资源
每个target使用的资源文件可能存在差异，在开发过程中，开发者可以将每个target所使用的资源存放在不同的资源目录下。其中，ArkTS工程支持对main目录下的资源文件目录（resource）进行定制；JS工程支持对main目录下的资源文件目录（resource）及 Ability下的资源文件目录（res）进行定制。如下为ArkTS工程的资源文件目录定制示例：
请注意，如果target引用的多个资源文件目录下，存在同名的资源，则在构建打包过程中，将按照配置的资源文件目录顺序进行选择。例如，上述付费版target引用的资源中，resource_default和resource_pay中存在同名的资源文件，则resource_default中的资源会被打包到HAP中。
定义产物的icon、label、launchType
针对每一个的target的ability，均可以定制不同的icon、label和launchType。如果不定义，则该target采用module.json5中module.abilities配置的icon、label，launchType默认为"singleton"。示例如下所示：
定义C++工程依赖的.so文件
在 C++ 工程中，可以对每个target依赖的.so文件进行定制。例如某模块依赖了function1.so、function2.so和function3.so三个文件，其中target为default的产物依赖了function1.so和function2.so；其中target为vip的产物依赖了function1.so和 function3.so，则示例代码如下所示：
定制HAR多目标构建产物
每一个HAR模块均支持定制不同的target，通过在模块中的build-profile.json5文件中实现差异化定制，当前支持设备类型（deviceType）、资源（resource）、buildOption配置项（如C++依赖的.so、混淆配置、abi类型、cppFlags等）、源码集（source）的定制。
当前版本，在DevEco Studio中编译时，仅支持编译target为default的模块。若需指定其他target，需通过命令行来指定，并通过命令行来编译。
例如构建指定的自定义target:free的har，可参考执行以下命令：
定义产物的deviceType
每一个target均可以指定支持的设备类型deviceType，也可以不定义。如果不定义，则该target默认支持config.json或module.json5中定义的设备类型。
同时，在定义每个target的deviceType时，支持的设备类型必须在config.json或module.json5中已经定义。例如，在上述定义的2个target中，分别定义default默认支持所有设备类型，free版本只支持2in1设备。
定义C++工程依赖的.so文件
在 C++ 工程中，可以对每个target依赖的.so文件进行定制。例如某模块依赖了function1.so、function2.so和function3.so三个文件，其中target为default的产物依赖了function1.so和function2.so；其中target为vip的产物依赖了function1.so和 function3.so，则示例代码如下所示：
定义产物的资源
每个target使用的资源文件可能存在差异，在开发过程中，开发者可以将每个target所使用的资源存放在不同的资源目录下。其中，ArkTS工程支持对main目录下的资源文件目录（resource）进行定制；JS工程支持对main目录下的资源文件目录（resource）及 Ability下的资源文件目录（res）进行定制。如下为ArkTS工程的资源文件目录定制示例：
定义产物的source源码集-sourceRoots
请参考定义产物的source源码集-sourceRoots。
配置APP多目标构建产物
APP用于应用/元服务上架发布，针对不同的应用场景，可以定制不同的product，每个product中支持对bundleName、bundleType、签名信息、icon和label以及包含的target进行定制。
定义目标产物product
每一个product对应一个定制的APP包，因此，在定制APP多目标构建产物前，应提前规划好需要定制的product名称。例如，定义productA和productB。工程级build-profile.json5文件示例如下：
在定制product时，必须存在"default"的product，否则编译时会出现错误。
定义产物的APP包名和供应商名称
每一个product均可以指定产物命名和供应商名称。
如果已配置签名，product产物对应的APP包名为开发者定制的名称；如果未配置签名，product产物对应的APP包名为开发者定制的名称+unsigned。
定义product的bundleName
针对每个定义的product，均可以定制不同的bundleName，如果product未定义bundleName，则采用工程默认的bundleName。示例如下所示：
定义product的bundleType
针对每个定义的product，均可以定制不同的bundleType。开发者可以通过定义每个product的bundleType，分别定义产物类型：
如果product未定义bundleType，则采用工程的bundleType（即创建工程时选择的Application/Atomic Service）。示例如下所示：
定义product的签名配置信息
针对每个定义的product，均可以定制不同的signingConfig签名文件，如果product未定义signingConfig，则构建生成未签名的APP包。
通常情况下，您首先需要在签名配置界面或工程的build-profile.json5文件中配置签名信息。例如在File > Project Structure > Project > Signing Configs界面，分别配置default、productA和productB的签名信息，如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.76242374233577972579713009604895:50001231000000:2800:9D10C2B437C4049283C812D9D4AE046075E3A2D41F3674E03EA2CDBA72F62F8D.png?needInitFileName=true?needInitFileName=true)
签名信息配置完成后，再添加各个product对应的签名文件，示例如下所示：
您也可以提前在product中定义签名文件信息，然后在签名界面对每个product进行签名，确保配置的product签名文件与签名界面配置的签名文件保持一致即可。
定义product的icon和label
针对每个定义的product，均可以定制不同的icon和label，如果product未定义icon和label，则采用工程默认的icon和label。示例如下所示：
products中的icon和label字段在编译时会替换app.json5中对应的字段，app.json5和module.json5均可以配置这两个字段，如果都配置，优先级顺序请参考应用/组件级配置。
定义product中包含的target
开发者可以选择需要将定义的target分别打包到哪一个product中，每个product可以指定一个或多个target。
同时每个target也可以打包到不同的product中，但是同一个module的不同target不能打包到同一个product中（除非该module的不同target配置了不同的deviceType或distributionFilter/distroFilter）。
例如，前面定义了default、free和pay三个target，现需要将default target打包到default product中；将free target打包到productA中；将pay target打包到productB中，对应的示例代码如下所示：
构建定义的目标产物
每个target对应一个HAP，每个product对应一个APP包，在编译构建时，如果存在多product或多target时，您可以指定编译具体的包。
单击右上角的图标，指定需要打包的Product及Target，然后单击Apply保存。例如选择"ProductA"中，entry模块对应的"free" Target。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.76264862134593062102293105330377:50001231000000:2800:92BF357CC346A209530E0DE6525B0F88599CEA69C5C8F7F5BAB0BCD296E59064.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.48116833333706704187287784838693:50001231000000:2800:54CC45F6091BB1689AFF51C485C8D90055B4B7C79D9BBE1E0293F41727EF3C9C.png?needInitFileName=true?needInitFileName=true)
然后执行编译构建APP/HAP的任务：
如果您想将某个模块下的指定target打包生成HAP，可以在工程目录中，单击模块名，然后再单击Build > Make Module‘模块名’，此时DevEco Studio将构建生成模块下指定target对应的包。例如，按照上述配置，此时DevEco Studio将构建生成entry模块下free的HAP，不会生成default的HAP。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.86135695111852839947682605632812:50001231000000:2800:82E7A369DE6478CA199B67560EA7F614629E0CBD272492DAE1C9779D0C9F6890.png?needInitFileName=true?needInitFileName=true)
调试和运行指定的Target
使用DevEco Studio调试或运行应用/元服务时，每个模块只能选择其中的一个target运行，可以通过单击右上角的图标，指定需要调试或运行的Product下对应的Module Target，然后单击Apply保存。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.70448014853236880172597572960790:50001231000000:2800:586CF685A84A02FBC24D42F1C7B8F26627380C97656F1C19B67737C0B54A5388.png?needInitFileName=true?needInitFileName=true)
在选择需要调试或运行的target时，需要注意选择该target所属的Product，否则将找不到可调试和运行的target。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.95548959189899261685182909582850:50001231000000:2800:F584C5DD4B6C34B3CE0DB7FD56BC08C701ED5EFD852FDEF727A5F4E5D46022D9.png?needInitFileName=true?needInitFileName=true)
多产物构建target
-  编译构建时，优先级最高的target。工程配置align target后，如果模块中存在align target，那么将自动选择align target进行构建。align target作用范围是整个工程，只能配置一个，支持命令行和配置文件两种方式。
-  当模块不存在指定的target时会选用default进行构建，但如果不想用default进行构建，那么可以配置fallback target，当找不到指定target时，如果模块中存在fallback target，则使用fallback target进行构建。fallback target作用范围是整个工程，可配置多个，配置多个时按数组顺序先命中的生效。
多个target的优先级顺序为：align target > 命令行指定模块target > 父级模块target > fallback target > default。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.23415362750605908092585963858091:50001231000000:2800:D342C46DFD7370E9CD16E25F547D4BCF07992757EE1F50D916E9C2EEB58D6FE1.png?needInitFileName=true?needInitFileName=true)
举例说明：
工程依赖entry->lib1->lib2，需要构建多个产品A、B、C，工程中target配置如下：
entry: A、B、default
lib1: B、C、default
lib2: A、C、default
指定align target为A，fallback target为C。那么构建hap时的编译命令为：
编译的target选择就是：entry@A, lib1@C, lib2@A。
以上所有说明仅针对非ohosTest模式。在ohosTest模式下，依赖的target固定为default，其他target均不生效。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-customized-multi-targets-and-products-sample-V14
爬取时间: 2025-04-30 07:38:02
来源: Huawei Developer
某对外发布应用共有两个版本：
1. Community社区版本，免费，向个人开发者用户提供该应用绝大部分基础功能，但是不提供部分定制化限定功能及技术支持。
2. Ultimate终极版本，收费，向个人、政企等开发者用户提供该应用全部基础功能，同时提供定制化限定功能及技术支持。
可以看出在Community版本与Ultimate版本之间，部分功能存在重合，同时也存在某些特定功能，所以期望通过一次开发以实现差异化，根据不同配置完成多种特定运行环境的开发、预览、打包、调试等功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.55604803056595737467139810703859:50001231000000:2800:7875918B5818587A57A3126AFB47B57A06EEC3E6B7207F0F4D62E070232E9EAB.png?needInitFileName=true?needInitFileName=true)
1. 两个不同版本的软件，可能存在差异：如不同的应用标题、应用图标、版本声明。我们可以在工程级build-profile.json5->app{}->products[]中，可以对两种不同的外发版本进行差异化定制，新增两个product：Community和Ultimate。根据已支持的字段进行定制修改。
2. 应用软件部分功能可能针对特定场景存在定制场景：如ultimate版本的功能A在phone设备类型上免费，在TV设备类型上需要收费；再如community版本的功能B在2in1设备类型上的启动页与在wearable设备类型上呈现效果存在差异。在模块级build-profile.json5->targets[]中新增2个 target：vip和free。
3. 新增product、target后，需要指定关联关系，在工程级build-profile.json5->modules[]->targets[]->applyToProducts中。此处表示当前模块的target具体应用到工程product的配置。
由上配置：
4. 在实际构建中，可通过可视化窗口灵活选择product-target的关联关系以构建出需要的APP/HAP包。
例：用户需要构建Ultimate版本的且具有vip特性的应用，可以选择product：Ultimate，target：vip，apply之后执行构建。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.92025941757846693603783585091682:50001231000000:2800:615AFB936365489D9E4CF004A5DB8D81A8825D2B198771B8950A12E189116BBC.png?needInitFileName=true?needInitFileName=true)
查看构建产物
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.69525593776533966426328095569645:50001231000000:2800:FB8320ECD339B66863DA45E65C7174570D14D7787814B5BA0B06A7D3623E8BC9.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-cpp-V14
爬取时间: 2025-04-30 07:38:36
来源: Huawei Developer
Hvigor集成cmake，ninja为cpp代码的构建工具。在初始状态下，您无需额外配置，为了定制您的cpp代码编译，您可通过以下配置添加自定义配置。
在模块的build-profile.json5中，存在以下配置项：
通过自定义externalNativeOptions参数，可修改cpp编译表现。nativeLib/headerPath声明了模块的c/cpp接口文件，并通过打包暴露给依赖模块。而通过debugSymbol、filter等配置，可修改so产物的体积与打包规则。
关于库文件so的优先级
库文件so的优先级选择，可以通过pickFirsts，pickLasts选项来选择，其中pickFirsts选择高优先级的库文件，pickLasts选择低优先级的库文件。
这个优先级是由本模块所依赖模块或三方包的收集顺序决定的，本模块依赖声明在oh-package.json5文件的dependencies配置项中，收集顺序按照广度优先的遍历方式来收集依赖。
如下图，优先级顺序为current > library0 > library1 > library5 > library2 > library3 > library4。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150646.46461992037231230265924455136284:50001231000000:2800:B4F72AD9700577F2A929732E8DD4E9BD1FF57FCB415FE27D812425C273626068.png?needInitFileName=true?needInitFileName=true)
关于select的使用
select提供native产物的精准选择能力，根据包名，版本，产物名称等，选择打包或排除native产物到hap/hsp/har产物。
例如本模块依赖的libcurl.so所在的har包为@ohos/curl，并且存在多个版本的libcurl.so，需要打包1.3.5版本，那可以通过以下配置，精确打包这个so到产物中。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-build-har-V14
爬取时间: 2025-04-30 07:39:10
来源: Huawei Developer
构建模式：DevEco Studio默认提供debug和release两种构建模式，同时支持开发者自定义构建模式。
产物格式：构建出的HAR包产物分为包含源码的HAR、包含js中间码的HAR以及包含字节码的HAR三种产物格式。
debug构建模式时，从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，默认产物是字节码HAR，用于开发者进行本地调测，可提升编译构建效率；同时支持构建包含源码的HAR。
release构建模式时，从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认不开启混淆，构建产物和debug模式相同；开启混淆后，构建产物是包含js中间码的HAR，用于发布到ohpm中心仓；同时支持配置产物格式为字节码HAR，用于提升发布产物的安全性。
使用约束
创建模块
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153008.40185831777070333466741180008072:50001231000000:2800:6398FD4CEED8B4E7693F6F7367BEEDA97FE554D1621528952B634F94074DF2A1.png?needInitFileName=true?needInitFileName=true)
构建HAR
以debug模式构建HAR
产物是包含源码的HAR包，其中包含源码、资源文件以及配置文件等，方便开发者进行本地调测，不包含build、node_modules、oh_modules、.cxx、.previewer、.hvigor、.gitignore、.ohpmignore、.gitignore/.ohpmignore中配置的文件、cpp工程的CMakeLists.txt。
1.  使用DevEco Studio NEXT Beta1（5.0.3.800）之前的版本，工程级build-profile.json5的useNormalizedOHMUrl字段默认值为false，无需执行本步骤。
2.
3.
4.  构建完成后，build目录下生成HAR包产物。 HAR包产物解压后，结构如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.71101147539817664969209351448991:50001231000000:2800:D69E35A72114E3FFDBA5DA378F7F633819B49C28364FF6EE7E077E8EC789346B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.56232361354086768811447774604443:50001231000000:2800:68E8A1F4C223E786E56FA3D8112D3F02E70A29A3B0ED8820010B3D241C7BF996.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.26639236018284382332776481832923:50001231000000:2800:3BF3D936FCA0A6F448E8EBB74B64F5FA327BFE92E4583D1675C57A8BB271996C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.59574012235274990623585242802929:50001231000000:2800:51F7315E6EFCD21738987652AAD1E7015D312650B8B7D09A1C0ED68A22B405F4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.86225107190251344091402462694650:50001231000000:2800:D9FDD108059B597FFD96A02B602A8CE0AAADC2340BBBC8E82AE3422E0CB669DB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.44572279827668210981197740083021:50001231000000:2800:E006F95FCA20D9150492D159CCCF5362F4905D7317651CC50106D7C56E29D18D.png?needInitFileName=true?needInitFileName=true)
以release模式构建HAR
从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认不开启混淆，构建产物和debug模式相同，请参考以debug模式构建HAR。
开启混淆后，构建产物是包含js中间码的HAR包，其中包含源码混淆后生成的js中间码文件、资源文件、配置文件、readme、changelog声明文件、license证书文件，用于发布到ohpm中心仓。
1.
2.
3.  使用DevEco Studio NEXT Beta1（5.0.3.800）之前的版本，工程级build-profile.json5的useNormalizedOHMUrl字段默认值为false，无需执行本步骤。
4.  构建完成后，build目录下生成HAR包产物。 HAR包产物解压后，结构如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.80215300571578456620292271996320:50001231000000:2800:63DAD1427AA946ACAF6E261DC517D9BECC5EE6DB226E1D69663C840EEAD3219E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.45753895754198548051802623861118:50001231000000:2800:E38A460E664AFC1EF2E07E4AACD8C48B3AAC5B85F290D7F4F3B450581700AF99.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.81089084310656973923507514391925:50001231000000:2800:7E1DF53EFFDDC0D018E212C6AF125A6CF3FE985551608A758F749BD93E770DD6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.48044825922956449143336475828541:50001231000000:2800:619A69680122E5D4DC30BA900F118E096D02A376CEB344C5B6A6E83CF4D2D69D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.26084008089751739641612898891229:50001231000000:2800:44693C4691314AAE08EBD2E533B6222DE68815CD6A8CF0C40876632A825FC7AF.png?needInitFileName=true?needInitFileName=true)
构建字节码格式的HAR
默认产物是包含字节码的HAR包，其中包含abc字节码、资源文件、配置文件、readme、changelog声明文件、license证书文件，提升发布到ohpm中心仓产物的安全性。
由于字节码HAR包中包含的是编译后的abc字节码，因此当字节码HAR被其他应用模块(HAP/HSP)依赖时，在执行应用模块的编译构建时，不需要再对依赖的HAR中的代码进行语法检查和编译等操作，相比包含源码的HAR和包含js中间码的HAR，可以有效提升应用模块的编译构建效率。
1.  从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，工程级build-profile.json5中useNormalizedOHMUrl字段默认为true，byteCodeHar缺省默认值为true，无需执行步骤1和2。
2.
3.  构建完成后，build目录下生成HAR包产物。 HAR包产物解压后，结构如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.54040107348842047714315903980219:50001231000000:2800:0B2D7FB6F49605789F411CB7FF945BA3997E38464C105124A29066F8FF16BAF7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.47955389687872737025043897622988:50001231000000:2800:CCD94DD4703A24BCE4683EE7087CF8E917F61C97777337051A477E231086FBD2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.62892681001801894205046994203313:50001231000000:2800:FF9D1032470110CCD21CA91B4D488C611C5CC161E435AED051862E3810E6C60C.png?needInitFileName=true?needInitFileName=true)
对HAR进行签名
DevEco Studio在构建HAR流程的基础上，支持对HAR进行签名。签名后的HAR包后续可用于接入生态市场，接入流程请参考SDK类商品接入说明。
1. 该能力只在Compatible SDK 5.0.0(12)及以上版本的SDK中支持。
2. 该能力需开启Hvigor的Daemon能力，请确保当前工程开启了Daemon，打开Settings > Build,Execution,Deployment > Build Tools > Hvigor，勾选字段Enable the Daemon for tasks。
1.
2.  构建完成后，build目录下生成签名HAR包产物。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.73720703378232026592866625277463:50001231000000:2800:DA899591A2CCBA6FA52DFF4D0DF548706C019979025339C6E795E84C3C09EE00.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153009.54820243413591174925796099670346:50001231000000:2800:18533730D801C1479677A5C99A1A1A44DCA156855B95B4C7980C746176549E5D.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-multi-projects-V14
爬取时间: 2025-04-30 07:39:45
来源: Huawei Developer
为降低大型应用多个团队协作开发的复杂度，提供多工程开发模式，提高协作开发效率。多工程开发能力支持将大型应用拆分为多个模块，每个模块对应一个单独工程。在每个工程分别编译生成HAP后，需统一打包生成一个APP，用于上架应用市场。
1.
2.

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-verification-rule-V14
爬取时间: 2025-04-30 07:40:19
来源: Huawei Developer
HAP是应用安装的基本单位，在DevEco Studio工程目录中，一个HAP对应一个Module。应用打包时，每个Module生成一个.hap文件。
应用如果包含多个Module，在应用市场上架时，会将多个.hap文件打包成一个.app文件（称为Bundle），但在云端分发和端侧安装时，仍然是以HAP为基本单位。
为了能够正常分发和安装应用，需要保证一个应用安装到设备时，Module的名称、Ability的名称不重复，并且只有一个Entry类型的Module与目标设备相对应。
DevEco Studio会在编译构建时，对HAP进行上述唯一性校验，如果校验不通过，将会编译失败或给出告警。
Module校验逻辑
校验目的：同一目标设备上Module唯一。
1.  deviceType不相交是指两个Module的deviceType中配置了完全不同的设备，例如： deviceType相交是指两个Module的deviceType中包含了相同的设备，例如：
```json
//Module1和Module2配置了完全不同的设备，deviceType不相交。
//Module1
{
"deviceType": ["tv", "tablet"]
}
//Module2
{
"deviceType": ["car", "router"]
}
```
2.  distributionFilter中包含属性apiVersion、screenShape、screenWindow、screenDensity和countryCode。相交的相关含义如下： 例如，两 Module 中的apiVersion、screenShape、screenWindow、screenDensity都相交，但countryCode不相交，则可以区分两个Module，校验通过。
Ability校验逻辑
校验目的：同一目标设备上Ability唯一。
1.  例如，两个Ability的Name相同，但其所属Module的deviceType不相交，校验通过。
2.  例如，两个Ability的Name相同，其所属Module的deviceType也相交，但其所属Module的distributionFilter不相交，校验通过。
Entry校验逻辑
校验目的：目标设备只有一个Entry类型的Module与之对应，Feature类型的Module经过deviceType及distributionFilter指明的目标设备都需要存在Entry类型的Module。
1.  例如，Bundle中存在一个Entry类型Module1，其支持设备为tablet和wearable，其分发规则为circle和rect形状的屏幕，同时存在一个Feature类型的Module2，通过分发规则可知，其可以分发到rect形状的tablet和wearable设备上，而rect形状的tablet和wearable设备上存在Entry类型的Module1，校验通过。
2.  例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType不相交，可以有效区分两个Module，校验通过。 例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType相交，但两者的distributionFilter不相交，可以有效区分两个Module，校验通过。
3.  例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType不相交，可以有效区分两个Module，校验通过。
4.  例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType相交，但两者的distributionFilter不相交，可以有效区分两个Module，校验通过。
1.  例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType不相交，可以有效区分两个Module，校验通过。
2.  例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType相交，但两者的distributionFilter不相交，可以有效区分两个Module，校验通过。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-path-V14
爬取时间: 2025-04-30 07:40:54
来源: Huawei Developer
.hvigor目录默认位于用户目录下：
若默认目录的磁盘空间不足，开发者需要自定义.hvigor目录路径，可通过以下方式自行配置。
该功能从DevEco Studio 5.0 Canary1版本开始支持。
-  在系统或者用户的变量中，添加自定义.hvigor目录的绝对路径。 变量名：HVIGOR_USER_HOME 变量值：自定义存放.hvigor目录的绝对路径。如D:\HvigorUserHome
-  该设置方式在重启电脑后将失效。 在macOS上设置系统变量的方式因系统版本不同而存在多种差异，以下仅为在macOS上为DevEco Studio设置系统变量的一种示例，具体设置方式以系统版本为准。 在/etc/launchd.conf（若该文件不存在，可自行创建）中添加如下内容。 设置完成后，重启电脑后才可生效。
-  该设置方式在重启电脑后将失效。
-  在macOS上设置系统变量的方式因系统版本不同而存在多种差异，以下仅为在macOS上为DevEco Studio设置系统变量的一种示例，具体设置方式以系统版本为准。 在/etc/launchd.conf（若该文件不存在，可自行创建）中添加如下内容。 设置完成后，重启电脑后才可生效。
-  打开终端工具，执行以下命令。 保存并关闭文件，使用source命令重新加载.bashrc配置文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150648.40644196918590009842641706191346:50001231000000:2800:50B6D4CA52217B4B9C807DEE9C9638D387EC4CF94B7CC3F282E0400A1702FB42.png?needInitFileName=true?needInitFileName=true)
-  该设置方式在重启电脑后将失效。
-  在macOS上设置系统变量的方式因系统版本不同而存在多种差异，以下仅为在macOS上为DevEco Studio设置系统变量的一种示例，具体设置方式以系统版本为准。 在/etc/launchd.conf（若该文件不存在，可自行创建）中添加如下内容。 设置完成后，重启电脑后才可生效。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-customization-V14
爬取时间: 2025-04-30 07:41:29
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-compilation-options-customizing-V14
爬取时间: 2025-04-30 07:42:04
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-compilation-options-customizing-guide-V14
爬取时间: 2025-04-30 07:42:38
来源: Huawei Developer
Hvigor支持灵活定制编译，即支持定制编译模式。当您创建新工程时，DevEco Studio会自动创建"debug" 、"release"和"test" 编译模式。"test"模式虽然没有出现在工程级build-profile.json5配置文件中，但是利用测试框架开启测试时会自动使用"test"编译模式。
指定编译模式
界面设置
DevEco Studio支持界面配置Build Mode配置选项，点击右上角图标选择编译模式：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153010.93604864889946732813272369777957:50001231000000:2800:89C2494F0AADA5A9B23848015C7841FD2065B80715497B4BEA05AF935BB3846B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153010.25435290924766586904460233706393:50001231000000:2800:FE878D86D3FEFCF57EC71BD54B3DFF72928CE7D7C0E191A94D52F076968CBCC8.png?needInitFileName=true?needInitFileName=true)
内置三个选项：<Default>，debug，release。
如果开发者在build-profile.json5文件中，自定义了其他编译模式，Build Mode配置界面会提供对应选项。
命令行设置
当未指定编译模式时，构建APP包，默认release模式；构建HAP/HSP/HAR包时，默认debug模式。
定制编译模式
Hvigor支持定制编译模式，采用buildOption字段声明编译选项，并通过buildModeBinder来绑定target、 buildOption以及buildMode三者之间的组合关系。
定义编译选项
工程级build-profile.json5文件：
| 字段  | 类型  | 是否必填  | 说明  |
| --- | --- | --- | --- |
| buildModeSet  | array  | 否  | 构建模式合集，可配置多个。  |
|    | name  | string  | 是  | 构建模式名称。 内置三种类型，此三项无需用户显性配置： debug：开发、调试推荐选项release：打包、发布推荐选项test：运行ohosTest测试套件推荐选项说明1. 项目中全局唯一，不区分大小写 2. 仅允许在工程级build-profile.json5中声明、定义 3. 相同的buildMode会被覆盖，按照配置顺序，后者覆盖前者 4. 三种模式均支持开发者自定义    |
| buildOption  | object  | 否  | 构建模式使用的具体配置信息，详情请参见表3。  |
| products  | array  | 否  | 产品品类，可配置多个。如需配置多个，相关说明请参见配置多目标产物章节。  |
|    | buildOption  | object  | 否  | 产品的编译构建配置，详情请参见表3。 说明product的buildOption会对buildMode的buildOption继承覆写，即相同配置项product的优先级更高。   |
字段
类型
是否必填
说明
buildModeSet
array
否
构建模式合集，可配置多个。
name
string
是
构建模式名称。
内置三种类型，此三项无需用户显性配置：
-  1. 项目中全局唯一，不区分大小写 2. 仅允许在工程级build-profile.json5中声明、定义 3. 相同的buildMode会被覆盖，按照配置顺序，后者覆盖前者 4. 三种模式均支持开发者自定义
buildOption
object
否
构建模式使用的具体配置信息，详情请参见表3。
products
array
否
产品品类，可配置多个。如需配置多个，相关说明请参见配置多目标产物章节。
buildOption
object
否
产品的编译构建配置，详情请参见表3。
product的buildOption会对buildMode的buildOption继承覆写，即相同配置项product的优先级更高。
模块级build-profile.json5文件：
| 字段  | 类型  | 是否必填  | 说明  |
| --- | --- | --- | --- |
| buildOption  | object  | 否  | 构建模式使用的具体配置信息，详情请参见表8，其中仅支持配置resOptions，externalNativeOptions，sourceOption，nativeLib，napiLibFilterOption和arkOptions字段。  |
| buildOptionSet  | array  | 否  | buildOption的集合，定义可用的底层配置选项集。  |
|    | name  | string  | 是  | buildOption的名称。 当前模块级build-profile.json5中已有顶层独立的buildOption配置，buildOptionSet优先级比buildOption更高。 说明同模块中唯一，不区分大小写。相同的名称会被覆盖，按照配置顺序，后者覆盖前者。内置三种：default、debug、release。   |
| copyFrom  | string  | 否  | 配置已定义的buildOption的name，表示从本模块已有的buildOption复制配置，然后再覆写。 说明仅限在同一模块的build-profile.json5中复制。目标buildOption不存在时，构建告警，回落为从内置的default选项中复制。   |
| buildModeBinder  | array  | 否  | 为某一buildMode建立target与buildOption之间的映射关系。  |
|    | buildModeName  | string  | 是  | 指定待建立映射的buildMode。 说明模块级中无法定义buildMode，此处名称须在工程级的buildModeSet中选取。对于系统内置的三种buildMode（debug / release / test）, Hvigor会分配默认绑定：debug mode：优先分配debug buildOption，测试包（ohosTest）分配default buildOption。release mode：优先分配release buildOption，测试包（ohosTest）分配 default buildOption。test mode：【测试套使用】测试包（ohosTest）分配default buildOption，主包分配debug buildOption。    |
| mappings  | array  | 否  | 绑定target使用的buildOption。  |
|    | targetName  | string  | 是  | 指定待绑定的target。 说明仅在本模块选择。   |
| buildOptionName  | string  | 是  | 指定待绑定的buildOption。 说明仅在本模块选择。   |
| targets  | config  | buildOption  | object  | 否  | 构建模式使用的具体配置信息，详情请参见表6，优先级比buildOptionSet更高。  |
字段
类型
是否必填
说明
buildOption
object
否
构建模式使用的具体配置信息，详情请参见表8，其中仅支持配置resOptions，externalNativeOptions，sourceOption，nativeLib，napiLibFilterOption和arkOptions字段。
buildOptionSet
array
否
buildOption的集合，定义可用的底层配置选项集。
name
string
是
buildOption的名称。
当前模块级build-profile.json5中已有顶层独立的buildOption配置，buildOptionSet优先级比buildOption更高。
copyFrom
string
否
配置已定义的buildOption的name，表示从本模块已有的buildOption复制配置，然后再覆写。
buildModeBinder
array
否
为某一buildMode建立target与buildOption之间的映射关系。
buildModeName
string
是
指定待建立映射的buildMode。
mappings
array
否
绑定target使用的buildOption。
targetName
string
是
指定待绑定的target。
仅在本模块选择。
buildOptionName
string
是
指定待绑定的buildOption。
仅在本模块选择。
targets
config
buildOption
object
否
构建模式使用的具体配置信息，详情请参见表6，优先级比buildOptionSet更高。
合并编译选项规则
编译选项继承覆写关系示意图
优先级：命令行配置>targets配置>buildOptionSet配置>buildOption配置>products配置>buildModeSet配置
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153010.82322229213822007396144023505816:50001231000000:2800:78E792CDE949BB47637BCCB84A5A1C2EA3FD414E6FA48BF4AE7DFEE453F6AE5D.jpg?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-compilation-options-customizing-sample-V14
爬取时间: 2025-04-30 07:43:12
来源: Huawei Developer
应用正式对外布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。
假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能debug调试。
示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下（模块）：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.44865673164584830878935797834409:50001231000000:2800:F10329EB670607BF63CA2D66324BFB9B553A7E87B76C07F7B8AC4D0743D13C3C.png?needInitFileName=true?needInitFileName=true)
工程级build-profile.json5示例
模块级build-profile.json5示例
entry模块
指定构建模式
命令行
示例1：构建APP时，构建产物为default，指定构建模式为debug，可执行如下命令：
编译产物示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.60082438645214988341627380826124:50001231000000:2800:DCCF501A84F23E08FA970F17EB2F2B789E1B86AC3E287E4040F911D540164156.png?needInitFileName=true?needInitFileName=true)
示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：
编译产物示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.15119265348568845584958739635496:50001231000000:2800:701E235E3C4022A86ACE38FBDBCA26FA523DF65C330ADC4482CFB7374DF1A638.png?needInitFileName=true?needInitFileName=true)
DevEco Studio界面
在DevEco Studio界面进行可视化配置，Build Mode下拉选择对应配置选项debug后，点击Build -> Build Hap(s)/APP(s) -> Build APP(s) ，构建编译模式为debug，构建产物为default的APP包。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250228180217.93476111819966708487213302412522:50001231000000:2800:6499C4CD4EA5E5789D1B668E8DF98C5D42BEEBDAC6C753024662BE69CF56B525.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-get-build-profile-para-V14
爬取时间: 2025-04-30 07:43:48
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-get-build-profile-para-guide-V14
爬取时间: 2025-04-30 07:44:23
来源: Huawei Developer
在编译构建时，Hvigor会生成BuildProfile类，开发者可以通过该类在运行时获取编译构建参数，也可以在build-profile.json5中通过buildProfileFields增加自定义字段，从而在运行时获取自定义的参数。
使用说明
buildProfileFields的优先级：模块级target > 模块级buildOptionSet > 模块级buildOption > 工程级product > 工程级buildModeSet
HAP/HSP运行时获取编译构建参数
生成BuildProfile类文件
当前有以下几种方式可以生成BuildProfile类文件：
执行完上述操作后，将在“${moduleName} / build / ${productName} / generated / profile / ${targetName} ”目录下生成BuildProfile.ets文件。示例如下所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153010.81066634510097515080863214882832:50001231000000:2800:6CA28C28CA7109949C8A5B5D4730EB442AB707EA7A2D7443A0DC2778DE91D564.png?needInitFileName=true?needInitFileName=true)
在代码中获取构建参数
在HSP中使用import BuildProfile from 'BuildProfile'在跨包集成HSP的时候可能会产生编译错误，推荐使用import BuildProfile from '${packageName}/BuildProfile'。
通过如下方式获取到构建参数：
默认参数
生成BuildProfile类文件时，Hvigor会根据当前工程构建的配置信息生成一部分默认参数，开发者可以在代码中直接使用。
| 参数名  | 类型  | 说明  |
| --- | --- | --- |
| BUNDLE_NAME  | string  | 应用的Bundle名称。  |
| BUNDLE_TYPE  | string  | 应用的Bundle类型。  |
| VERSION_CODE  | number  | 应用的版本号。  |
| VERSION_NAME  | string  | 应用版本号的文字描述。  |
| TARGET_NAME  | string  | Target名称。  |
| PRODUCT_NAME  | string  | Product名称。  |
| BUILD_MODE_NAME  | string  | 编译模式。  |
| DEBUG  | boolean  | 应用是否可调试。  |
参数名
类型
说明
BUNDLE_NAME
string
应用的Bundle名称。
BUNDLE_TYPE
string
应用的Bundle类型。
VERSION_CODE
number
应用的版本号。
VERSION_NAME
string
应用版本号的文字描述。
TARGET_NAME
string
Target名称。
PRODUCT_NAME
string
Product名称。
BUILD_MODE_NAME
string
编译模式。
DEBUG
boolean
应用是否可调试。
自定义参数
开发者可以在模块级的build-profile.json5文件中增加自定义参数，在生成BuildProfile类文件后，在代码中使用自定义参数。
自定义参数可以在buildOption、buildOptionSet、targets节点下的arkOptions子节点中通过增加buildProfileFields字段实现，自定义参数通过key-value键值对的方式配置，其中value取值仅支持number、string、boolean类型。
配置示例如下所示：
HAR运行时获取编译构建参数
生成BuildProfile类文件
当前有以下几种方式可以生成BuildProfile类文件：
执行完上述操作后，将在模块根目录下生成BuildProfile.ets文件（该文件可放置在.gitignore文件中进行忽略）。示例如下所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.89591844963696570394620659028201:50001231000000:2800:321257348C91998F62B749B95292E4BEBC44CB9160F013C7C6FBD3EE85FB9C96.png?needInitFileName=true?needInitFileName=true)
在代码中获取构建参数
生成BuildProfile类文件后，在代码中可以通过相对路径引入该文件，如在HAR模块的Index.ets文件中使用该文件：
通过如下方式获取到构建参数：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.26619850865558088131523295014971:50001231000000:2800:3F2AC04B54C2C3BBE841DA4B59B3B3B5DCF64961F565C5C38EA91885547FD7A9.png?needInitFileName=true?needInitFileName=true)
默认参数
生成BuildProfile类文件时，Hvigor会根据当前工程构建的配置信息生成一部分默认参数，开发者可以在代码中直接使用。
| 参数名  | 类型  | 说明  |
| --- | --- | --- |
| HAR_VERSION  | string  | HAR版本号。  |
| BUILD_MODE_NAME  | string  | 编译模式。  |
| DEBUG  | boolean  | 应用是否可调试。  |
| TARGET_NAME  | string  | 目标名称。  |
参数名
类型
说明
HAR_VERSION
string
HAR版本号。
BUILD_MODE_NAME
string
编译模式。
DEBUG
boolean
应用是否可调试。
TARGET_NAME
string
目标名称。
自定义参数
开发者可以在模块级的build-profile.json5文件中增加自定义参数，在生成BuildProfile类文件后，在代码中使用自定义参数。
自定义参数可以在buildOption、buildOptionSet节点下的arkOptions子节点中通过增加buildProfileFields字段实现，自定义参数通过key-value键值对的方式配置，其中value取值仅支持number、string、boolean类型。
配置示例如下所示：
工程级配置自定义构建参数
开发者可以在工程级的build-profile.json5文件中增加自定义参数，该自定义参数会生成到所有模块的BuildProfile类文件，在代码中使用自定义参数。
自定义参数可以在工程级products、buildModeSet中的buildOption节点下的arkOptions子节点中通过增加buildProfileFields字段实现，自定义参数通过key-value键值对的方式配置，其中value取值仅支持number、string、boolean类型。
配置示例如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-get-build-profile-para-sample-V14
爬取时间: 2025-04-30 07:44:57
来源: Huawei Developer
示例：配置工程级和模块级的自定义参数并通过切换product来展示不同的message。
新建工程并创建一个har模块
在工程级别的build-profile.json5使用以下配置，目的是为了实现在所有模块中都可以使用到productMessage自定义参数。
通过切换不同的product从而使用到对应的productMessage值。
在har模块的MainPage.ets中添加以下代码。
在hap的oh-package.json5中引用本地的har模块。
在hap的Index.ets文件中用引用该har包并且使用MainPage方法。
执行预览或签名后推包到设备调试
点击har模块执行以下按钮。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.80842245041490016740329005110232:50001231000000:2800:86CECA31DC5DD76A3A8F265079A80F181BF3D5BB9E2380002A492EEE33BE0ED2.png?needInitFileName=true?needInitFileName=true)
default模式下初始化的message为defaultMessage。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.03390221637987380886691074692271:50001231000000:2800:3E86A5E45CA5DCFC894BC844DBF5D2D75D1E3BF2CFA84DC41AF2C89E7C491FB1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.66509909223009646538015420740850:50001231000000:2800:4C6641E17DF42F62F27E14A1B73EC856949891DA264F17BC8EAEAFB18E4BE4A3.png?needInitFileName=true?needInitFileName=true)
通过切换不同的product可以使用不同的自定义参数用来初始化message。
切换product为mirror。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.55166762546082134016813523781482:50001231000000:2800:7D3B428BBE7049CEAA9854B365B751C3C266044421947CABEB6CAF10BA9FBED3.png?needInitFileName=true?needInitFileName=true)
可以观察到初始化参数为mirrorMessage：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.50049242859656469572048601554101:50001231000000:2800:BB62B40F1C0A83B62DD5EEA9649B4242BA7EA3CAC257F5ADE388CDFBA9B3CA9E.png?needInitFileName=true?needInitFileName=true)
点击不同的Button可以改变message为对应的自定义参数：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.86234684131676633139913025820359:50001231000000:2800:98822069C6A2C584ED75A71429AFC334EA8FE0D0B863A341D517971BA4D53731.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.91896100714805712347543080873984:50001231000000:2800:545EE8EE82C23B18794FA461B3B390F1AF1E66B875E9CF20F9B49528DB1FBC5A.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-config-ohos-V14
爬取时间: 2025-04-30 07:45:32
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-config-ohos-guide-V14
爬取时间: 2025-04-30 07:46:07
来源: Huawei Developer
Hvigor支持在hvigorfile.ts里接收部分编译配置，以实现动态配置构建配置、并使能到构建的过程与结果中。
此能力现有两种方式实现：
通过hook以及插件上下文实现动态配置
Hvigor支持stage模型在hvigor hook中操作从硬盘上读取的以下配置文件：
目前可以通过hvigor对象提供的上下文直接获取和修改配置以实现动态配置构建配置、并使能到构建的过程与结果中。
在hvigorfile.ts或hvigorconfig.ts文件中，可以使用Hvigor提供的API接口来实现此能力。
相比于下面的overrides的能力来说，通过hook以及插件上下文来动态修改签名和编译配置更为灵活和易于理解，功能也更为全面，推荐使用此种方式。具体使用方式请参考通过hook以及插件上下文动态配置构建配置(推荐使用)。
在hvigorfile.ts中通过overrides关键字导出动态配置
在hvigorfile.ts中，我们约定在导出的对象中的config.ohos属性里接收编译的配置：
目前可以在工程级的hvigorfile.ts的config.ohos中配置的字段：
目前可以在模块级的hvigorfile.ts的config.ohos中配置的字段：
配置在overrides项中的参数，其优先级会高于在配置项中的对应字段。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-config-ohos-sample-V14
爬取时间: 2025-04-30 07:46:41
来源: Huawei Developer
通过hook以及插件上下文动态配置构建配置(推荐使用)
修改每个hvigorNode中的build-profile.json5
此处只举例为单个node注册hook并修改build-profile.json5的信息。
例如需要修改根目录下的build-profile.json5的签名信息，则在项目根目录下的hvigorfile.ts中添加如下内容：
修改module.json5中的配置信息
可以通过hvigor对象的hook能力快捷为所有的node创建hook，此处先举例为单一的node创建一个hook并修改其中的module.json5的配置信息。
例如此处需要修改entry下的module.json5配置，则在entry下的hvigorfile.ts中添加如下内容：
修改app.json5中的配置信息
在项目的根目录下的hvigorfile.ts中添加如下代码内容：
修改oh-package.json5中的依赖
通过overrides动态配置签名材料和版本信息(不推荐使用)
通过在hvigorfile.ts里使用函数方法，动态配置签名材料和版本号、版本名等信息：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-optimized-V14
爬取时间: 2025-04-30 07:47:16
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-build-analyzer-V14
爬取时间: 2025-04-30 07:47:50
来源: Huawei Developer
使用Build Analyzer工具可以显示编译构建过程的重要信息，开发者可以可视化分析排查构建过程中的性能问题。
进入Build Analyzer
Build Analyzer会在每次构建应用时默认生成一份报告，并在Build Analyzer窗口进行展示。
可以在构建完成后通过以下方式打开Build Analyzer窗口：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.77329296116355377933236643146067:50001231000000:2800:3D97948EC3F6DD243A859A79A16D6CF743FAD66C0D0DD5611B6AEAF116EAE00C.png?needInitFileName=true?needInitFileName=true)
查看构建历史记录
Build Analyzer左侧的Build History窗口中按时间顺序显示构建历史记录，包括本工程的构建历史数据和导入的日志数据。点击构建历史记录可以显示对应概览和可视化图谱界面。
本工程的构建历史数据保存在./hvigor/report目录下，超过10条记录后，最久的历史数据将会被自动清理。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.08630739560451671707875487143986:50001231000000:2800:D1475BD86DE8CB6AF8C83ADB7EA6AA9478A4398BE41135810918892CC9C60055.png?needInitFileName=true?needInitFileName=true)
查看构建任务时间图谱
完成构建后首次打开Build Analyzer 时，窗口会显示构建分析概览，如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.25827978514931452760470307845845:50001231000000:2800:C7B270A9046FE6CB5EB21D9BA3119787DAD5B36DDD2A38BD430E138B81F2F795.png?needInitFileName=true?needInitFileName=true)
如需查看构建任务时间图谱，请从下拉菜单中点击Tasks，默认进入时间图谱界面。该界面会分块显示构建历史记录、构建任务时长图谱、构建日志以及对应的日志详情信息，如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.87832592480824524698962199600770:50001231000000:2800:C77386DA428B076B582E10B3A816B4E60BE1BF6A674BEFFEC0837EACB296C3C7.png?needInitFileName=true?needInitFileName=true)
图谱中的构建任务展示按照各个任务总时长占比，以相对长度进行展示。可以对时间块进行缩小放大，查看具体的任务名称及耗时信息。
图谱中构建子任务默认是折叠的，可点击Build TimeLine的节点信息，展开查看子任务的构建时长图谱。
图谱与日志信息是联动的，可点击图谱中的任务信息，即可联动对应的日志以及日志详情；相同的，点击日志时，也可联动对应的上方图谱信息。
Build Analyzer不会全部显示构建操作中的所有任务，而是重点显示决定构建总时长的任务。
图谱下方日志模块，展示每次构建的所有日志信息，并按日志级别（Info、Debug、Warn、Error）进行区分，并提供日志搜索功能。
点击日志，可与上方图谱和右侧Details模块，进行联动显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.72598990740972487622808764793224:50001231000000:2800:55BF8BD3C61058C857FEE83003251D5F36BBD1239D0384D9E0B6665AA4B5C42E.png?needInitFileName=true?needInitFileName=true)
查看构建任务占比图谱
如需查看决定着构建时长的任务的占比细分数据，请点击概览页面上的Common views into this build下方链接 ，您也可以从下拉菜单中选择Tasks并确认您要的任务分组类别。任务以模块、业务类别、目标以及同一模块下的目标、同一模块下的业务类别和同一目标下的业务类别进行分组。图表中任务按照时间占比从大到小排列，点击子任务可详细了解其执行情况。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.09760802013592743120669943116520:50001231000000:2800:804AE10E35A06128CFA541091FE936C58133609B281E198C43B8B3E9BA31DFA8.png?needInitFileName=true?needInitFileName=true)
1. 由于并行线程的存在，分类任务计算时间可能会比实际总时间长；
2. 饼图中Configuration代表未记录的任务占比。
导出日志
如需查看本次构建日志，您可以点击导出按钮进行日志导出。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.40786628721717961611208216018093:50001231000000:2800:E7A8110358BDED7D422FB13D117FB23CCBCEC93AF596E85EE9F486B065A8E7F2.png?needInitFileName=true?needInitFileName=true)
导出内容有：
导入日志
如需查看历史或其他工程的构建日志，您可以点击导入按钮导入report.json文件，导入的文件保存在工程./hvigor/report/upload目录下，导入后可在Build Analyzer左侧的Build History窗口中查看。upload目录下最多保存10条记录，超过10条记录后，最久的历史数据将会被自动清理。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.42836058161841451082791197089663:50001231000000:2800:91E81930B4687A668BB23B89EEB6250252DE301F4896254C0A5C0280306A472F.png?needInitFileName=true?needInitFileName=true)
设置构建分析模式
进入File > Settings > Build, Execution, Deployment > Build Tools > Hvigor下，查看Use build analysis mode选项：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150650.47615675140619774709115575108786:50001231000000:2800:E968C871B55C265FF83E4A3417C83E7A3BCB65EDCD7D3B6924026D5EB325B25E.png?needInitFileName=true?needInitFileName=true)
生成构建可视化html文件
执行以上命令后，在工程的.hvigor/report目录下生成对应的html文件，该文件可直接在浏览器中打开。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-optimized-performance-V14
爬取时间: 2025-04-30 07:48:24
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-improve-performance-V14
爬取时间: 2025-04-30 07:48:59
来源: Huawei Developer
构建性能对生产力至关重要，完成构建所需时间越长，开发效率就越低。构建花费时间越少，您对新问题的反应效率就越快，并且可以频繁地进行验证。
这意味着投入一些精力使您的构建尽可能快，是有意义的。本节提供了几种加快构建速度的方法，此外，您还将找到有关导致构建性能下降的原因以及如何避免这种情况的详细信息。
启用守护进程
请参考Hvigor守护进程启用守护进程。
启用并行执行
大部分工程都包含了多个子工程，其中一些子工程是相互独立的，也就是说，它们之间没有状态共享。在大多数情况下，通过并行构建可以有效地减少多个子工程的整体构建时间。然而，在特定的情况下，如子工程之间存在大量的依赖关系，可能无法显著缩短构建时间。节省的具体时间取决于您的工程结构和子工程之间的依赖关系。
默认情况下，Hvigor会开启并行执行。您可以通过parallel标志控制是否启用并行：
您也可以配置hvigor-config.json5中execution.parallel选项来控制是否启用并行执行。
启用增量构建
增量构建是Hvigor执行任务的一种优化，如果在两次执行任务工程中，执行任务的输入和输出没有更改，Hvigor会跳过该任务的执行。
Hvigor自定义任务要与增量构建兼容，需指定输入和输出，有关更多的增量构建，请查看增量构建章节。
Hvigor默认启用增量构建，您可以使用以下标志设置增量构建开关：
您也可以配置hvigor-config.json5中execution.incremental选项来控制是否启用增量构建。开启增量构建后，您应该会在增量执行场景下看到显著的性能改进。
增加守护进程内存大小
请参考设置守护进程内存增加守护进程内存大小。
构建能力分析
在任何更改之前，请使用分析构建能力来检查您的构建。正确的构建检查可以帮助您了解：
检查提供了一个比较点，您可以更好的了解本节建议对构建时长的影响。该能力已集成在DevEco Studio中，您可参考分析构建性能章节获取更多能力信息。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-daemon-V14
爬取时间: 2025-04-30 07:49:34
来源: Huawei Developer
守护进程是作为后台进程运行而不是在交互式用户的直接控制下运行的计算机程序。Hvigor守护进程是一个持续存在的后台进程，可以减少运行构建所需的时间。
了解守护进程
Hvigor客户端发送Daemon构建信息，如命令行参数、工程目录和环境变量等，以便于运行构建。客户端和守护进程之间的通信通过本地套接字进行连接，正在运行守护进程同时最多开启8个，状态为非停止或中断的守护进程最多开启6个。
启用禁用守护进程
Hvigor默认启用守护进程，您可以使用以下标志设置守护进程开关：
您也可以配置hvigor-config.json5中execution.daemon选项来控制是否启用守护进程。
设置守护进程内存
守护进程默认内存是8192 MB，对绝大多数构建来说已经足够了。如果您想自定义守护进程的内存，可以通过以下两种方式修改，建议您参考本地剩余内存进行调整设置。其中命令行方式优先级高于hvigor-config.json5配置文件。
检查守护进程状态
如果您想获取正在运行的守护进程及其状态的列表，可以使用以下命令查看：
```shell
> hvigor PID    STATUS  PORT    ROOT_PATH
> hvigor 11072  idle    45001   D:\Demo1
> hvigor 18836  stopped 45000   D:\Demo2
```
| 守护进程状态  | 状态描述  |
| --- | --- |
| idle  | 闲置  |
| half_busy  | 半忙碌  |
| busy  | 忙碌  |
| canceled  | 取消  |
| stopReq  | 停止请求  |
| stopped  | 停止  |
| broken  | 中断  |
守护进程状态
状态描述
idle
闲置
half_busy
半忙碌
busy
忙碌
canceled
取消
stopReq
停止请求
stopped
停止
broken
中断
停止守护进程
在更改关于守护进程内存设置或调试故障时，重启守护进程是必要的。
您可用以下命令停止运行守护进程，这将停止该工程下的守护进程：
如果您想停止所有守护进程，您可以使用以下命令：
性能影响
当您重复构建同一项目时，守护进程可以将构建时间缩短。多次构建时，守护进程只会将hvigor一次性加载到内存中，而不是每一次构建。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-incremental-build-V14
爬取时间: 2025-04-30 07:50:08
来源: Huawei Developer
任何构建工具的一个重要部分是能够避免重复执行已经执行完成的工作。在重复编译时，如果之前的源文件已经被编译过，除非发生了影响输入输出的更改，那么该文件就不需要重新编译。编译过程本身就会耗费大量时间，因此跳过此种任务的编译，将会节省大量时间。
Hvigor自然支持此种增量构建行为。当您执行任务且控制台输出任务被标记为UP-TO-DATE，这意味着增量构建正在工作。
任务的输入和输出
在正常情况下，任务根据一些输入生成一些输出。作为增量构建的一部分，Hvigor记录上次构建的任何任务的输入和输出情况，对比当次构建的输入和输出，如果没有发生更改，那么Hvigor将认为该任务没有更改，从而跳过该任务的执行。因此也请注意，尽管任务在通常情况下至少有一个输入，但是在定义任务时，请至少定义一个输出，否则增量构建将无法工作。
对此定义增量任务，您只需告诉Hvigor哪些任务属性是输入，哪些任务属性是输出。如果任务属性影响了输出，请务必将其注册为输入，否则任务将可能被视为最新，与预期效果不一致。相反，如果任务属性不影响输出，请不要将其注册为输入，否则任务将可能会在不需要时被执行。另请注意非确定性任务不应配置为增量任务，因为这些任务可能为完全相同的输入生成不同的输出，导致最新检查不起作用。
它是如何工作的
在第一次执行之前，Hvigor会获取输入的快照信息，该信息包括输入文件名称、路径、大小、最后修改时间以及对应的哈希值。任务执行成功之后，Hvigor会获取输出的快照信息，该信息包括输出文件名称、路径、大小、最后修改时间以及对应的哈希值。当然，Hvigor对任务本身也进行了快照存储。Hvigor会在下次执行任务时会保留这两个快照信息。
此后每次执行任务之前，Hvigor都会获取输入和输出的新快照信息。如果新快照信息与之前的快照信息相同，Hvigor就会认为输出已经是最新的并且跳过该任务的执行。如果它们不相同，Hvigor就会执行该任务，执行成功之后，输入和输出的新快照信息将被存储。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-esmodule-compile-V14
爬取时间: 2025-04-30 07:50:42
来源: Huawei Developer
应用模块化编译是指基于ESModule的Bundleless编译模式，使用原生ES Module规则构建源码。API 10及以上版本的Stage工程默认开启模块化编译，可有效缩短增量编译时间、减小编译后的包体积。
当前已知模块化编译如果存在re-export语法、引用了没有对应声明文件 (.d.ts) 的 native 文件 (.so)、使用export * from 'x.js'导出js文件中的符号等情况将导致工程报错，若原有工程在升级DevEco Studio至3.1 Beta2版本后出现编译错误，请查看FAQ进行修改。
FA 模板创建的工程依然使用基于bundle打包的构建方式。
模块化编译解决了Bundle编译打包模式引入的如下问题：
模块化编译模式有以下价值：
使用规格约束

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-aot-V14
爬取时间: 2025-04-30 07:51:16
来源: Huawei Developer
AOT（Ahead Of Time）即预先编译，在程序运行前，预先编译成高性能机器码，让程序在首次运行就能通过执行高性能机器码获得性能收益（关于具体的性能收益分析，可以使用性能分析工具进行前后对比分析，工具说明及指导请参见性能分析）。
方舟AOT编译器实现了PGO (Profile-Guided-Optimization）编译优化，即通过结合预先profiling的运行时类型等信息和静态类型信息，预先静态地生成高性能优化机器代码。
在方舟AOT编译器中，记录预先profiling运行时类型等信息的文件称为ap(ark profiler)文件。
对性能有高要求的开发者可以使用AOT编译提升应用运行性能。
使用约束
前置操作
打开ap采集开关(设备重启后，开关恢复默认关闭状态)。
操作步骤
1.  当采集阶段执行到的js函数个数少于一定阈值时，无法生成ap文件。
2.  输入如下命令，待命令返回后，表示编译完成。 编译任务受整机资源状态管控，为提高编译成功率，请在设备熄屏状态下进行编译，并在避免设备发烫情况下开启编译。
3.  执行以下命令，通过aotCompileStatus字段查看该应用下每个module的编译状态。 状态值 意义 常见场景 0 尚未进行AOT编译 没有生成ap文件，或待进行AOT编译 1 AOT编译成功 AOT编译成功 2 AOT编译失败 AOT编译器内部错误
4.  使用过程中如出现应用闪退、界面不一致、手机功耗异常增加等不稳定情况，可按照本步骤清除AOT产物。
| 状态值  | 意义  | 常见场景  |
| --- | --- | --- |
| 0  | 尚未进行AOT编译  | 没有生成ap文件，或待进行AOT编译  |
| 1  | AOT编译成功  | AOT编译成功  |
| 2  | AOT编译失败  | AOT编译器内部错误  |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-so-V14
爬取时间: 2025-04-30 07:51:52
来源: Huawei Developer
在工程中使用依赖模块时，如果希望使用依赖模块中native相关的so库与接口文件（.h/.hpp），Hvigor提供了快速链接功能。
头文件
-  在共享包中include目录下如存在.h等接口文件，Hvigor会自动将此目录添加到CMake接口目录中，无需手动添加。
预构建库
在工程中引用了共享包/本地依赖模块中的so库，编译时，Hvigor会生成cmakeConfig-file Packages，自动通过cmakefind_package引入这些so。开发者只需根据此依赖模块的模块名、so库名，在CMakeLists.txt脚本中以${moduleName::soName}库名称的形式来声明链接。
例如工程依赖了curl共享包，共享包中存在libcurl.so，在oh-package.json5中添加依赖。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150651.90221975844902525867414795778485:50001231000000:2800:E8F94B68960C6CCF7909487AA12F61915834960A751CE88146CDE4BDD557947B.png?needInitFileName=true?needInitFileName=true)
在工程的CMakeLists.txt脚本中声明链接：
对于本地模块，HAR仅暴露本模块构建的so库，HSP暴露本模块构建及所依赖的so库。
依赖透传
如果需要声明库之间的依赖关系，例如entry依赖curl，可在模块内build-profile.json5中配置librariesInfo。
当其他模块依赖声明了依赖透传的模块并使用libentry.so时，libentry.so会将依赖curl::curl添加到参数INTERFACE_LINK_LIBRARIES，开发者无需关注它的依赖。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-expanding-V14
爬取时间: 2025-04-30 07:52:26
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-task-V14
爬取时间: 2025-04-30 07:53:03
来源: Huawei Developer
了解任务
任务是Hvigor构建过程中的执行基本单元，任务中通常包含一段编译过程处理的可执行代码；一个任务可以依赖其他多个任务。Hvigor任务调度执行时通过解析依赖关系确定任务执行时序。
UP-TO-DATE
任务标识，表示任务未实际执行。Hvigor任务增量跳过机制，在二次执行任务时检测任务输入输出条件未发生变化，则任务跳过执行提高构建效率。
示例：
Finished
任务执行完成标识，表示任务已执行完成。
示例：
注册任务
使用HvigorNode节点对象注册任务。
1.
2.
3.  使用hvigor命令行工具执行任务：
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150651.89923253514189486202215821351844:50001231000000:2800:32232E3A6FC5D4BFDFBB44822E26D0AAB11B9B059CA52C24BCBDF209E8894734.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-plugin-V14
爬取时间: 2025-04-30 07:53:38
来源: Huawei Developer
Hvigor允许开发者实现自己的插件，开发者可以定义自己的构建逻辑，并与他人共享。
Hvigor主要提供了两种方式来实现插件：基于hvigorfile脚本开发插件、基于typescript项目开发。
下面的章节中，将以HarmonyOS应用为示例，逐一介绍。
基于hvigorfile脚本开发
基于hvigorfile.ts脚本开发的方式，其优点是可实现快速开发，直接编辑工程或模块下hvigorfile.ts即可编写插件代码，不足之处是在多个项目中，无法方便的进行插件代码的复用和共享分发。
1.
2.
3.
4.  执行Hvigor命令时，在Hvigor生命周期配置阶段执行插件中的apply方法。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150651.09858863203651220602841436629050:50001231000000:2800:8F8C570A77639B717BB46A9414249BB7C2D06B11708CCE4DBF9BF9D5AD04DB91.png?needInitFileName=true?needInitFileName=true)
基于typescript项目开发
基于typescript项目开发较好地弥补了上一小节中使用hvigorfile脚本方式编写插件代码不易复用和共享分发的问题。因此通常情况下推荐此方式开发。
初始化typescript项目
1.  在命令行工具中使用cd命令进入空目录下。
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150651.16880310381850600914326197406301:50001231000000:2800:1C4AF18346618BC25C073D9D6E9B09A43B590D5E544599AD698879FBB13B21F3.png?needInitFileName=true?needInitFileName=true)
开发插件
1.  在用户目录下创建或打开.npmrc文件，配置如下信息：
2.  打开package.json添加devDependencies配置。
3.
4.  创建custom-plugin.ts文件，编写插件代码，更多接口请参考扩展构建API。
5.  创建index.ts文件，并在该文件中声明插件方法的导出。
发布插件
typescript项目本质上是一种npm项目，插件发布流程遵循npm发布规范。详情请查询npm官方资料。
发布npm包流程：
1.  在用户目录下创建.npmrc文件，配置您需要发布的镜像仓库。
2.  执行如下命令，注册并登录npm仓库，在用户目录下.npmrc文件中自动生成token信息。
3.  执行如下命令，将npm项目打包并发布至镜像仓库。
使用插件
1.
2.
3.  根据插件编写时基于的node节点，确定导入的节点所在的hvigorfile.ts文件，在hvigorfile.ts中导入插件。
4.

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-apis-V14
爬取时间: 2025-04-30 07:54:12
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-api-V14
爬取时间: 2025-04-30 07:54:47
来源: Huawei Developer
Hvigor预置对象
"hvigor"对象是一个预定义的Hvigor对象，表示当前正在执行的Hvigor构建引擎的实例，通过"hvigor"对象可以获得有关构建的一些信息和操作。
导入模块
| 成员  | 声明  | 说明  | 开始支持的版本  |
| --- | --- | --- | --- |
| getRootNode  | getRootNode(): HvigorNode  | 获取根项目的节点  | Hvigor 4.3.0  |
| getAllNodes  | getAllNodes(): HvigorNode[]  | 获取包含所有节点的数组  | Hvigor 4.3.0  |
| getNode  | getNode(scriptPath: string): HvigorNode  | 根据hvigorfile.ts路径获取当前节点  | Hvigor 4.0.2  |
| getNodeByName  | getNodeByName(nodeName: string): HvigorNode | undefined  | 根据节点的名字获取节点  | Hvigor 4.3.0  |
| getHvigorConfig  | getHvigorConfig(): HvigorConfig  | 获取hvigorConfig对象  | Hvigor 4.3.0  |
| getParameter  | getParameter(): Parameter  | 获取Parameter对象  | Hvigor 4.3.0  |
| configEvaluated  | configEvaluated(fn: (HvigorConfig) => {})  | 添加一个config文件评估完成的回调函数  | Hvigor 4.3.0  |
| beforeNodeEvaluate  | beforeNodeEvaluate(fn: (HvigorNode) => {})  | 为所有的node添加一个node评估前的回调函数  | Hvigor 4.3.0  |
| afterNodeEvaluate  | afterNodeEvaluate(fn: (HvigorNode) => {})  | 为所有的node添加一个node评估后的回调函数  | Hvigor 4.3.0  |
| nodesInitialized  | nodesInitialized(fn: (Hvigor) => {})  | 添加一个node初始化完成的回调函数  | Hvigor 4.3.0  |
| nodesEvaluated  | nodesEvaluated(fn: (Hvigor) => {}): void  | 添加一个nodes解析完成的回调函数  | Hvigor 4.0.2  |
| taskGraphResolved  | taskGraphResolved(fn: (Hvigor) => {})  | 添加一个任务图解析完毕的回调函数  | Hvigor 4.3.0  |
| buildFinished  | buildFinished(fn: (BuildResult) => {})  | 添加一个构建结束的回调函数  | Hvigor 4.3.0  |
| getCommandEntryTask  | getCommandEntryTask(): string[] | undefined  | 获取构建的入口任务名字符串数组  | Hvigor 4.3.0  |
| isCommandEntryTask  | isCommandEntryTask(taskName: string): boolean  | 判断是否是命令入口任务  | Hvigor 4.3.0  |
成员
声明
说明
开始支持的版本
getRootNode
getRootNode(): HvigorNode
获取根项目的节点
Hvigor 4.3.0
getAllNodes
getAllNodes(): HvigorNode[]
获取包含所有节点的数组
Hvigor 4.3.0
getNode
getNode(scriptPath: string): HvigorNode
根据hvigorfile.ts路径获取当前节点
Hvigor 4.0.2
getNodeByName
getNodeByName(nodeName: string): HvigorNode | undefined
根据节点的名字获取节点
Hvigor 4.3.0
getHvigorConfig
getHvigorConfig(): HvigorConfig
获取hvigorConfig对象
Hvigor 4.3.0
getParameter
getParameter(): Parameter
获取Parameter对象
Hvigor 4.3.0
configEvaluated
configEvaluated(fn: (HvigorConfig) => {})
添加一个config文件评估完成的回调函数
Hvigor 4.3.0
beforeNodeEvaluate
beforeNodeEvaluate(fn: (HvigorNode) => {})
为所有的node添加一个node评估前的回调函数
Hvigor 4.3.0
afterNodeEvaluate
afterNodeEvaluate(fn: (HvigorNode) => {})
为所有的node添加一个node评估后的回调函数
Hvigor 4.3.0
nodesInitialized
nodesInitialized(fn: (Hvigor) => {})
添加一个node初始化完成的回调函数
Hvigor 4.3.0
nodesEvaluated
nodesEvaluated(fn: (Hvigor) => {}): void
添加一个nodes解析完成的回调函数
Hvigor 4.0.2
taskGraphResolved
taskGraphResolved(fn: (Hvigor) => {})
添加一个任务图解析完毕的回调函数
Hvigor 4.3.0
buildFinished
buildFinished(fn: (BuildResult) => {})
添加一个构建结束的回调函数
Hvigor 4.3.0
getCommandEntryTask
getCommandEntryTask(): string[] | undefined
获取构建的入口任务名字符串数组
Hvigor 4.3.0
isCommandEntryTask
isCommandEntryTask(taskName: string): boolean
判断是否是命令入口任务
Hvigor 4.3.0
getNode4.0.2+
getNode(scriptPath: string): HvigorNode
传入hvigorfile.ts脚本文件路径获取当前节点对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| scriptPath  | string  | 是  | hvigorfile.ts脚本全路径  |
参数名
类型
必填
说明
scriptPath
string
是
hvigorfile.ts脚本全路径
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNode  | hvigor节点对象  |
类型
说明
HvigorNode
hvigor节点对象
示例：获取当前节点对象。
getRootNode4.3.0+
getRootNode(): HvigorNode
返回根项目的节点对象。
注意：在node初始化后才能使用，否则会报错。
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNode  | hvigor根节点对象  |
类型
说明
HvigorNode
hvigor根节点对象
示例：获取根节点对象。
getAllNodes4.3.0+
getAllNodes(): HvigorNode[]
返回所有节点的数组。
注意：在node初始化后才能使用，否则会报错。
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNode[]  | hvigor所有节点对象的数组  |
类型
说明
HvigorNode[]
hvigor所有节点对象的数组
示例：获取所有节点对象的数组。
getNodeByName4.3.0+
getNodeByName(nodeName: string): HvigorNode | undefined
根据节点名称获取节点对象。
注意：在node初始化后才能使用，否则会报错。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| nodeName  | string  | 是  | 节点的名称  |
参数名
类型
必填
说明
nodeName
string
是
节点的名称
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNode | undefined  | 根据名称找到的节点对象，如果不存在则返回undefined  |
类型
说明
HvigorNode | undefined
根据名称找到的节点对象，如果不存在则返回undefined
示例：通过节点名称获取节点对象。
getHvigorConfig4.3.0+
getHvigorConfig(): HvigorConfig
返回HvigorConfig对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorConfig  | HvigorConfig对象  |
类型
说明
HvigorConfig
HvigorConfig对象
示例：获取当前HvigorConfig对象。
getParameter4.3.0+
getParameter(): Parameter
返回Parameter对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| Parameter  | Parameter对象  |
类型
说明
Parameter
Parameter对象
示例：获取当前Parameter对象。
configEvaluated4.3.0+
configEvaluated(fn: (HvigorConfig) => {}): void
添加一个config文件评估完成的回调函数。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (HvigorConfig) => {}  | 是  | 一个入参为空或者为hvigorConfig的方法  |
参数名
类型
必填
说明
fn
(HvigorConfig) => {}
是
一个入参为空或者为hvigorConfig的方法
此API写在hvigorconfig.ts文件中才会生效，在构建生命周期的初始化阶段被执行。
示例：注册configEvaluated hook。
beforeNodeEvaluate4.3.0+
beforeNodeEvaluate(fn: (HvigorNode) => {}): void
为所有的node添加一个node评估前的回调函数。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (HvigorNode) => {}  | 是  | 一个入参为空或者为HvigorNode的方法  |
参数名
类型
必填
说明
fn
(HvigorNode) => {}
是
一个入参为空或者为HvigorNode的方法
此API写在hvigorconfig.ts文件中才会生效，在构建生命周期的初始化阶段被执行。
示例：注册beforeNodeEvaluate hook。
afterNodeEvaluate4.3.0+
afterNodeEvaluate(fn: (HvigorNode) => {}): void
为所有的node添加一个node评估后的回调函数。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (HvigorNode) => {}  | 是  | 一个入参为空或者为HvigorNode的方法  |
参数名
类型
必填
说明
fn
(HvigorNode) => {}
是
一个入参为空或者为HvigorNode的方法
示例：注册afterNodeEvaluate hook。
nodesInitialized4.3.0+
nodesInitialized(fn: (Hvigor) => {}): void
添加一个node初始化完成的回调函数。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (HvigorNode) => {}  | 是  | 一个入参为空或者为Hvigor对象的方法  |
参数名
类型
必填
说明
fn
(HvigorNode) => {}
是
一个入参为空或者为Hvigor对象的方法
此API写在hvigorconfig.ts文件中才会生效，在构建生命周期的初始化阶段被执行。
示例：注册nodesInitialized hook。
nodesEvaluated4.0.2+
nodesEvaluated(fn: (Hvigor) => {}): void
添加hvigor配置阶段完成之后执行的回调函数，此函数在配置阶段结束之前使用方可有效。在配置阶段中接口使用场景例如节点插件上下文信息延迟获取、任务延迟注册等。添加的回调函数是以队列的形式存储，遵循先进先出原则，先添加的回调会先被执行。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (Hvigor) => {}  | 是  | 一个入参为空或者为Hvigor对象的方法  |
参数名
类型
必填
说明
fn
(Hvigor) => {}
是
一个入参为空或者为Hvigor对象的方法
示例：工程节点获取子节点插件上下文信息。
taskGraphResolved4.3.0+
taskGraphResolved(fn: (Hvigor) => {}): void
添加一个任务图解析完毕的回调函数。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (Hvigor) => {}  | 是  | 一个入参为空或者为Hvigor对象的方法  |
参数名
类型
必填
说明
fn
(Hvigor) => {}
是
一个入参为空或者为Hvigor对象的方法
buildFinished4.3.0+
buildFinished(fn: (BuildResult) => {}): void
添加一个任务图解析完毕的回调函数。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (BuildResult) => {}  | 是  | 一个入参为空或者为BuildResult对象的方法  |
参数名
类型
必填
说明
fn
(BuildResult) => {}
是
一个入参为空或者为BuildResult对象的方法
getCommandEntryTask4.3.0+
getCommandEntryTask(): string[] | undefined
获取构建的入口任务名字符串数组。
返回值:
| 类型  | 说明  |
| --- | --- |
| string[]  | 构建的入口任务名字符串数组  |
类型
说明
string[]
构建的入口任务名字符串数组
isCommandEntryTask4.3.0+
isCommandEntryTask(taskName: string): boolean
判断是否是命令入口任务。
返回值:
| 类型  | 说明  |
| --- | --- |
| boolean  | 是否是入口任务  |
类型
说明
boolean
是否是入口任务
BuildResult
代表构建结果的对象，如果是异常结束则会包含异常的信息。
| 成员  | 声明  | 说明  | 开始支持的版本  |
| --- | --- | --- | --- |
| getError  | getError(): Error | null  | 获取异常信息。没有异常则返回null  | Hvigor 4.3.0  |
| getReportJson  | getReportJson(): any  | 获取本次构建的可视化记录report.json结果  | Hvigor 5.0.10  |
成员
声明
说明
开始支持的版本
getError
getError(): Error | null
获取异常信息。没有异常则返回null
Hvigor 4.3.0
getReportJson
getReportJson(): any
获取本次构建的可视化记录report.json结果
Hvigor 5.0.10
getError4.3.0+
getError(): Error | null
获取异常信息。没有异常则返回null。
返回值:
| 类型  | 说明  |
| --- | --- |
| Error | null  | 异常信息。没有异常则为null。  |
类型
说明
Error | null
异常信息。没有异常则为null。
getReportJson5.0.10+
getReportJson(): any
获取本次构建的可视化记录report.json结果。
返回值:
| 类型  | 说明  |
| --- | --- |
| any  | 本次构建的可视化记录report.json结果。  |
类型
说明
any
本次构建的可视化记录report.json结果。
report.json结构说明。不同类型的构建事件具有不同结构，以下为典型结构示例：
HvigorConfig
HvigorConfig对象是在node对象被创建之前用来保存每个节点的描述信息的对象。
| 成员  | 声明  | 说明  | 开始支持的版本  |
| --- | --- | --- | --- |
| getRootNodeDescriptor  | getRootNodeDescriptor(): HvigorNodeDescriptor  | 获取RootNode的描述对象  | Hvigor 4.3.0  |
| getAllNodeDescriptors  | getAllNodeDescriptors(): HvigorNodeDescriptor[]  | 获取所有的node描述对象的数组  | Hvigor 4.3.0  |
| getNodeDescriptorByName  | getNodeDescriptorByName(name: string): HvigorNodeDescriptor  | 根据节点名称获取node描述对象  | Hvigor 4.3.0  |
| includeNode  | includeNode(name: string, srcPath: string, extraOptions?: Record<string, any>): void  | 添加一个node(节点)  | Hvigor 5.4.0  |
| excludeNodeByName  | excludeNodeByName(name: string): void  | 排除一个node(节点)  | Hvigor 5.4.0  |
成员
声明
说明
开始支持的版本
getRootNodeDescriptor
getRootNodeDescriptor(): HvigorNodeDescriptor
获取RootNode的描述对象
Hvigor 4.3.0
getAllNodeDescriptors
getAllNodeDescriptors(): HvigorNodeDescriptor[]
获取所有的node描述对象的数组
Hvigor 4.3.0
getNodeDescriptorByName
getNodeDescriptorByName(name: string): HvigorNodeDescriptor
根据节点名称获取node描述对象
Hvigor 4.3.0
includeNode
includeNode(name: string, srcPath: string, extraOptions?: Record<string, any>): void
添加一个node(节点)
Hvigor 5.4.0
excludeNodeByName
excludeNodeByName(name: string): void
排除一个node(节点)
Hvigor 5.4.0
getRootNodeDescriptor4.3.0+
getRootNodeDescriptor(): HvigorNodeDescriptor
获取RootNode的描述对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNodeDescriptor  | 根节点的节点描述对象  |
类型
说明
HvigorNodeDescriptor
根节点的节点描述对象
getAllNodeDescriptor4.3.0+
getAllNodeDescriptor(): HvigorNodeDescriptor[]
获取所有的node描述对象的数组。
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNodeDescriptor[]  | 所有节点的节点描述对象  |
类型
说明
HvigorNodeDescriptor[]
所有节点的节点描述对象
getNodeDescriptorByName4.3.0+
getNodeDescriptorByName(name: string): HvigorNodeDescriptor
根据节点名称获取node描述对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| name  | string  | 是  | 根据此name查找NodeDescriptor  |
参数名
类型
必填
说明
name
string
是
根据此name查找NodeDescriptor
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNodeDescriptor  | 根据名称获取的节点描述对象  |
类型
说明
HvigorNodeDescriptor
根据名称获取的节点描述对象
includeNode5.4.0+
includeNode(name: string, srcPath: string, extraOptions?: Record<string, any>): void
添加一个node。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| name  | string  | 是  | 要添加的node的name  |
| srcPath  | string  | 是  | 要添加的node的srcPath  |
| extraOptions  | Record<string, any>  | 否  | 可以通过此参数传入额外的配置信息，会被解析成为此node的targets  |
参数名
类型
必填
说明
name
string
是
要添加的node的name
srcPath
string
是
要添加的node的srcPath
extraOptions
Record<string, any>
否
可以通过此参数传入额外的配置信息，会被解析成为此node的targets
返回值: 无
此API写在hvigorconfig.ts文件中才会生效，在构建生命周期的初始化阶段被执行。
excludeNodeByName5.4.0+
excludeNodeByName(name: string): void
通过name排除一个Node。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| name  | string  | 是  | 要排除的node的name  |
参数名
类型
必填
说明
name
string
是
要排除的node的name
返回值: 无
此API写在hvigorconfig.ts文件中才会生效，在构建生命周期的初始化阶段被执行。
HvigorNodeDescriptor4.3.0+
此对象为hvigor的节点描述对象，hvigor在构建时会通过此对象来构造出hvigorNode对象。
| 成员  | 声明  | 说明  | 开始支持的版本  |
| --- | --- | --- | --- |
| name  | name: string  | 节点的名称  | Hvigor 4.3.0  |
| srcPath  | srcPath: string  | 节点的src路径  | Hvigor 4.3.0  |
| extraOptions  | extraOptions:  Map<string, any>  | 拓展属性，用来保存传递数据  | Hvigor 4.3.0  |
| getChildNode  | getChildNode(): HvigorNodeDescriptor[] | undefined  | 获取所有的子节点描述对象，不存在子节点则返回undefined  | Hvigor 4.3.0  |
| getRootNode  | getRootNode(): HvigorNodeDescriptor  | 获取根节点的节点描述对象  | Hvigor 4.3.0  |
成员
声明
说明
开始支持的版本
name
name: string
节点的名称
Hvigor 4.3.0
srcPath
srcPath: string
节点的src路径
Hvigor 4.3.0
extraOptions
extraOptions:  Map<string, any>
拓展属性，用来保存传递数据
Hvigor 4.3.0
getChildNode
getChildNode(): HvigorNodeDescriptor[] | undefined
获取所有的子节点描述对象，不存在子节点则返回undefined
Hvigor 4.3.0
getRootNode
getRootNode(): HvigorNodeDescriptor
获取根节点的节点描述对象
Hvigor 4.3.0
Parameter4.3.0+
“Parameter”是hvigor中的命令配置参数对象，可以通过hvigor.getParameter()方法获取。
| 成员  | 声明  | 说明  | 开始支持的版本  |
| --- | --- | --- | --- |
| getProperty  | getProperty(key: string): any | undefined  | 获取properties对象指定key值的value值  | Hvigor 4.1.2  |
| getProperties  | getProperties(): Properties  | 获取properties配置对象  | Hvigor 4.1.2  |
| getExtParam  | getExtParam(key: string): string | undefined  | 获取指定key值的-p扩展参数value值  | Hvigor 4.1.2  |
| getExtParams  | getExtParams(): Record<string, string>  | 获取全部的-p 扩展参数对象  | Hvigor 4.1.2  |
| getStartParams  | getStartParams(): StartParam  | 获取hvigor启动参数  | Hvigor 4.1.2  |
| getWorkspaceDir  | getWorkspaceDir(): string  | 获取hvigor工作空间路径  | Hvigor 4.1.2  |
| setProperty  | setProperty(key: string, value: any): void  | 设置properties对象指定key值的value值  | Hvigor 5.10.3  |
成员
声明
说明
开始支持的版本
getProperty
getProperty(key: string): any | undefined
获取properties对象指定key值的value值
Hvigor 4.1.2
getProperties
getProperties(): Properties
获取properties配置对象
Hvigor 4.1.2
getExtParam
getExtParam(key: string): string | undefined
获取指定key值的-p扩展参数value值
Hvigor 4.1.2
getExtParams
getExtParams(): Record<string, string>
获取全部的-p 扩展参数对象
Hvigor 4.1.2
getStartParams
getStartParams(): StartParam
获取hvigor启动参数
Hvigor 4.1.2
getWorkspaceDir
getWorkspaceDir(): string
获取hvigor工作空间路径
Hvigor 4.1.2
setProperty
setProperty(key: string, value: any): void
设置properties对象指定key值的value值
Hvigor 5.10.3
getProperty4.1.2+
getProperty(key: string): any | undefined
获取properties配置指定key值的value值，若不存在配置时返回undefined。
示例：获取properties配置中指定key值的value值。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| key  | string  | 是  | properties配置中key  |
参数名
类型
必填
说明
key
string
是
properties配置中key
返回值:
| 类型  | 说明  |
| --- | --- |
| any  | properties配置中指定key对应的value值（string，number, boolean类型）  |
类型
说明
any
properties配置中指定key对应的value值（string，number, boolean类型）
示例：
在hvigorfile.ts中添加代码。
执行命令hvigorw --sync -c properties.key=hello，控制台打印：
getProperties4.1.2+
getProperties(): Properties
获取properties所有配置的对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| Properties  | Properties配置对象  |
类型
说明
Properties
Properties配置对象
示例：
在hvigorfile.ts中添加代码
执行命令hvigorw --sync -c properties.key=hello，控制台打印：
getExtParam4.1.2+
getExtParam(key: string): string | undefined
获取指定key值的-p扩展参数value值，若不存在配置时返回undefined。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| key  | string  | 是  | 命令行参数-p配置中的key  |
参数名
类型
必填
说明
key
string
是
命令行参数-p配置中的key
返回值:
| 类型  | 说明  |
| --- | --- |
| string | undefined  | 指定key值对应的-p参数对应的value，配置不存在时undefined  |
类型
说明
string | undefined
指定key值对应的-p参数对应的value，配置不存在时undefined
示例：
执行命令hvigorw --sync -p key=hello，控制台打印：
getExtParams4.1.2+
getExtParams(): Record<string, string>
获取全部的-p扩展参数对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| Record<string, string>  | 命令行中所有配置的-p参数集合对象  |
类型
说明
Record<string, string>
命令行中所有配置的-p参数集合对象
示例：
执行命令hvigorw --sync -p key=hello，控制台打印：
getStartParams4.1.2+
getStartParams(): StartParam
获取hvigor启动参数：例如daemon开关，并行功能开关，增量功能开关，日志级别等。
返回值:
| 类型  | 属性  | 说明  |
| --- | --- | --- |
| StartParams  | daemon: boolean  | 守护进程启用状态，true开启（默认开启）、false关闭  |
| StartParams  | parallel: boolean  | 并行编译能力启用状态，true开启（默认开启）、false关闭  |
| StartParams  | incremental: boolean  | 增量编译能力启用状态，true开启（默认开启）、false关闭  |
| StartParams  | logLevel: string  | 当前日志级别，info、debug、warn、error等  |
| StartParams  | typeCheck: boolean  | hvigorfile.ts的类型检查，true开启、false关闭（默认关闭）  |
类型
属性
说明
StartParams
daemon: boolean
守护进程启用状态，true开启（默认开启）、false关闭
StartParams
parallel: boolean
并行编译能力启用状态，true开启（默认开启）、false关闭
StartParams
incremental: boolean
增量编译能力启用状态，true开启（默认开启）、false关闭
StartParams
logLevel: string
当前日志级别，info、debug、warn、error等
StartParams
typeCheck: boolean
hvigorfile.ts的类型检查，true开启、false关闭（默认关闭）
示例：
执行命令hvigorw --sync，控制台打印：
getWorkspaceDir4.1.2+
getWorkspaceDir(): string
获取hvigor工作空间路径。工作空间是指当前工程对应的hvigor插件安装在磁盘的位置。
示例：
执行命令hvigorw --sync，控制台打印当前工程hvigor安装的工作路径：
setProperty5.10.3+
setProperty(key: string, value: any): void
设置properties对象指定key值的value值。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| key  | string  | 是  | hvigor-config.json5配置文件中properties字段的key值  |
| value  | any  | 是  | hvigor-config.json5配置文件中properties字段的key值对应的value值  |
参数名
类型
必填
说明
key
string
是
hvigor-config.json5配置文件中properties字段的key值
value
any
是
hvigor-config.json5配置文件中properties字段的key值对应的value值
返回值：无
在模块级hvigorfile.ts中调用该API不生效，请在工程级hvigorfile.ts中调用。
示例：
在工程级hvigorfile.ts中添加代码。
执行命令hvigorw --sync，控制台打印：
HvigorNode
"HvigorNode"是hvigor中的节点模型接口，Hvigor工程中都有一个根模块对应的节点对象和每个子模块对应的节点对象，节点对象均为HvigorNode接口的实现。节点对象包含了该模块的配置，属性和任务等。
导入模块
| 成员  | 声明  | 描述  | 开始支持的版本  |
| --- | --- | --- | --- |
| registerTask  | registerTask: (task: HvigorTask) => void  | 注册任务  | Hvigor 4.0.2  |
| getTaskByName  | getTaskByName: (taskName: string) => Task | undefined  | 根据taskName获取Task对象  | Hvigor 4.0.2  |
| getNodeName  | getNodeName: () => string  | 获取当前节点名称  | Hvigor 4.0.2  |
| getNodePath  | getNodePath: () => string  | 获取当前节点路径  | Hvigor 4.0.2  |
| getParentNode  | getParentNode: () => HvigorNode | undefined  | 获取父级节点对象  | Hvigor 4.0.2  |
| subNodes  | subNodes: (callbackfn: (node: HvigorNode) => void) => void  | 所有子节点回调函数  | Hvigor 4.0.2  |
| getSubNodeByName  | getSubNodeByName: (nodeName: string) => HvigorNode | undefined  | 根据节点名称获取节点对象  | Hvigor 4.0.2  |
| getContext  | getContext: (pluginId: string) => any  | 根据pluginId获取当前节点上指定插件的上下文接口信息  | Hvigor 4.0.2  |
| getAllPluginIds  | getAllPluginIds: () => string[]  | 获取当前节点已加载的pluginId集合  | Hvigor 4.0.2  |
| nodeDir  | nodeDir: NormalizedFile  | 当前节点的根目录的NormalizedFile对象  | Hvigor 4.3.0  |
| getNodeDir  | getNodeDir: () => NormalizedFile  | 获取当前节点的根目录的NormalizedFile对象  | Hvigor 4.3.0  |
| addExtraOption  | addExtraOption: (key: string, value: any) => void  | 为当前的node添加一个拓展属性  | Hvigor 4.3.0  |
| getExtraOption  | getExtraOption: (key: string) => any  | 通过key获取一个拓展属性  | Hvigor 4.3.0  |
| beforeNodeEvaluate  | beforeNodeEvaluate(fn: (HvigorNode) => {})  | 为当前的node添加一个node评估前的回调函数  | Hvigor 4.3.0  |
| afterNodeEvaluate  | afterNodeEvaluate(fn: (HvigorNode) => {})  | 为当前的node添加一个node评估后的回调函数  | Hvigor 4.3.0  |
成员
声明
描述
开始支持的版本
registerTask
registerTask: (task: HvigorTask) => void
注册任务
Hvigor 4.0.2
getTaskByName
getTaskByName: (taskName: string) => Task | undefined
根据taskName获取Task对象
Hvigor 4.0.2
getNodeName
getNodeName: () => string
获取当前节点名称
Hvigor 4.0.2
getNodePath
getNodePath: () => string
获取当前节点路径
Hvigor 4.0.2
getParentNode
getParentNode: () => HvigorNode | undefined
获取父级节点对象
Hvigor 4.0.2
subNodes
subNodes: (callbackfn: (node: HvigorNode) => void) => void
所有子节点回调函数
Hvigor 4.0.2
getSubNodeByName
getSubNodeByName: (nodeName: string) => HvigorNode | undefined
根据节点名称获取节点对象
Hvigor 4.0.2
getContext
getContext: (pluginId: string) => any
根据pluginId获取当前节点上指定插件的上下文接口信息
Hvigor 4.0.2
getAllPluginIds
getAllPluginIds: () => string[]
获取当前节点已加载的pluginId集合
Hvigor 4.0.2
nodeDir
nodeDir: NormalizedFile
当前节点的根目录的NormalizedFile对象
Hvigor 4.3.0
getNodeDir
getNodeDir: () => NormalizedFile
获取当前节点的根目录的NormalizedFile对象
Hvigor 4.3.0
addExtraOption
addExtraOption: (key: string, value: any) => void
为当前的node添加一个拓展属性
Hvigor 4.3.0
getExtraOption
getExtraOption: (key: string) => any
通过key获取一个拓展属性
Hvigor 4.3.0
beforeNodeEvaluate
beforeNodeEvaluate(fn: (HvigorNode) => {})
为当前的node添加一个node评估前的回调函数
Hvigor 4.3.0
afterNodeEvaluate
afterNodeEvaluate(fn: (HvigorNode) => {})
为当前的node添加一个node评估后的回调函数
Hvigor 4.3.0
registerTask
registerTask: (task: HvigorTask) => void
在当前节点注册任务，在Hvigor生命周期中的配置阶段中执行。注册任务需完成HvigorTask的实现作为入参对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| task  | HvigorTask  | 是  | HvigorTask的实现  |
参数名
类型
必填
说明
task
HvigorTask
是
HvigorTask的实现
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNode  | hvigor节点对象  |
类型
说明
HvigorNode
hvigor节点对象
示例：自定义任务注册。
getTaskByName
getTaskByName: (taskName: string) => Task | undefined
获取当前节点中已注册的Task对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| taskName  | string  | 是  | 任务名称  |
参数名
类型
必填
说明
taskName
string
是
任务名称
返回值:
| 类型  | 说明  |
| --- | --- |
| Task | undefined  | Task对象或undefined。当前节点未找到指定taskName的已注册任务时，返回值为undefined。  |
类型
说明
Task | undefined
Task对象或undefined。当前节点未找到指定taskName的已注册任务时，返回值为undefined。
示例：
getNodeName
getNodeName: () => string
获取当前节点名称。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 节点名称  |
类型
说明
string
节点名称
getNodePath
getNodePath: () => string
获取当前节点路径。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 节点路径  |
类型
说明
string
节点路径
getParentNode
getParentNode: () => HvigorNode | undefined
获取父级节点对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNode | undefined  | 节点对象或undefined  |
类型
说明
HvigorNode | undefined
节点对象或undefined
subNodes
subNodes: (callbackfn: (node: HvigorNode) => void) => void
遍历当前节点下的子节点执行回调函数。可通过此接口在工程节点操作节点对象。
补充：工程节点比模块节点优先加载，若需操作子节点，需使用hvigor.nodesEvaluated接口等待全部节点加载完成，才能操作子节点对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| callbackfn  | (node: HvigorNode) => void  | 是  | 入参类型为HvigorNode，返回类型为void的函数  |
参数名
类型
必填
说明
callbackfn
(node: HvigorNode) => void
是
入参类型为HvigorNode，返回类型为void的函数
getSubNodeByName
getSubNodeByName: (nodeName: string) => HvigorNode | undefined
根据节点名称获取节点对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| nodeName  | string  | 是  | 节点名称  |
参数名
类型
必填
说明
nodeName
string
是
节点名称
返回值:
| 类型  | 说明  |
| --- | --- |
| HvigorNode | undefined  | 节点对象或undefined  |
类型
说明
HvigorNode | undefined
节点对象或undefined
getContext
getContext: (pluginId: string) => any
根据pluginId获取当前节点上指定插件的上下文接口信息。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| pluginId  | string  | 是  | 插件ID  |
参数名
类型
必填
说明
pluginId
string
是
插件ID
返回值:
| 类型  | 说明  |
| --- | --- |
| any  | 支持自定义返回值类型  |
类型
说明
any
支持自定义返回值类型
getAllPluginIds
getAllPluginIds: () => string[]
获取当前节点已加载的pluginId集合。
返回值:
| 类型  | 说明  |
| --- | --- |
| string[]  | 当前已加载的插件ID集合  |
类型
说明
string[]
当前已加载的插件ID集合
nodeDir4.3.0+
nodeDir: NormalizedFile
当前节点的根目录的NormalizedFile对象。
getNodeDir4.3.0+
getNodeDir: () => NormalizedFile
获取当前节点的根目录的NormalizedFile对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| NormalizedFile  | 当前节点的根目录的NormalizedFile对象  |
类型
说明
NormalizedFile
当前节点的根目录的NormalizedFile对象
addExtraOption4.3.0+
addExtraOption: (key: string, value: any) => void
为当前的node添加一个拓展属性。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| key  | string  | 是  | 要添加的拓展属性的key  |
| value  | any  | 是  | 要添加的拓展属性的value  |
参数名
类型
必填
说明
key
string
是
要添加的拓展属性的key
value
any
是
要添加的拓展属性的value
getExtraOption4.3.0+
getExtraOption: (key: string) => any
根据节点名称获取节点对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| key  | string  | 是  | 拓展属性的key  |
参数名
类型
必填
说明
key
string
是
拓展属性的key
返回值:
| 类型  | 说明  |
| --- | --- |
| any  | 拓展属性的value  |
类型
说明
any
拓展属性的value
beforeNodeEvaluate4.3.0+
beforeNodeEvaluate(fn: (HvigorNode) => {}): void
为当前的node添加一个node评估前的回调函数。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (HvigorNode) => {}  | 是  | 一个入参为空或者为HvigorNode的方法  |
参数名
类型
必填
说明
fn
(HvigorNode) => {}
是
一个入参为空或者为HvigorNode的方法
示例：为名称为entry的node注册一个beforeNodeEvaluate hook并打印出node的信息。
afterNodeEvaluate4.3.0+
afterNodeEvaluate(fn: (HvigorNode) => {}): void
为当前的node添加一个node评估后的回调函数。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | (HvigorNode) => {}  | 是  | 一个入参为空或者为HvigorNode的方法  |
参数名
类型
必填
说明
fn
(HvigorNode) => {}
是
一个入参为空或者为HvigorNode的方法
示例：为名称为entry的node注册一个afterNodeEvaluate hook并打印出node的信息。
HvigorPlugin
该接口定义了Hvigor开发插件的基本范式。开发Hvigor插件需实现此接口。
导入模块
| 成员  | 声明  | 描述  |
| --- | --- | --- |
| pluginId  | pluginId: string  | 插件唯一标识  |
| context  | context?: (() => any) | any  | 插件上下文定义，在hvigor配置的生命周期调用  |
| apply  | apply: (node: HvigorNode) => void | Promise<void>  | 插件主体函数，用于定义插件实现逻辑(例如任务注册等); 在hvigor的生命周期配置阶段调用  |
成员
声明
描述
pluginId
pluginId: string
插件唯一标识
context
context?: (() => any) | any
插件上下文定义，在hvigor配置的生命周期调用
apply
apply: (node: HvigorNode) => void | Promise<void>
插件主体函数，用于定义插件实现逻辑(例如任务注册等); 在hvigor的生命周期配置阶段调用
pluginId
pluginId: string
插件唯一标识属性。
context
context?: (() => any) | any
插件上下文实现接口，可选实现；实现此函数后，其他插件可通过node.getContext('插件ID'）获取插件中定义的上下文接口。
返回值:
| 类型  | 说明  |
| --- | --- |
| (() => any) | any  | 自定义返回类型的Function或自定义任一返回类型  |
类型
说明
(() => any) | any
自定义返回类型的Function或自定义任一返回类型
apply
apply: (node: HvigorNode) => void | Promise<void>
插件主体函数，用于定义插件实现逻辑(例如任务注册等); 在Hvigor的生命周期配置阶段调用。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| node  | HvigorNode  | 是  | hvigor节点对象  |
参数名
类型
必填
说明
node
HvigorNode
是
hvigor节点对象
返回值:
| 类型  | 说明  |
| --- | --- |
| (node: HvigorNode) => void | Promise<void>  | 入参类型HvigorNode、返回类型为void的函数，或Promise<void>类型  |
类型
说明
(node: HvigorNode) => void | Promise<void>
入参类型HvigorNode、返回类型为void的函数，或Promise<void>类型
HvigorTask
Hvigor任务实现的接口类型，定义了任务的实现范式，在创建任务时需实现此接口。
导入模块
| 成员  | 声明  | 描述  |
| --- | --- | --- |
| name  | name: string  | 任务名称定义  |
| context  | context?: (() => any) | any  | 定义任务中局部共享的数据对象  |
| input  | input?: (input: TaskInput) => void  | 实现任务增量输入条件定义  |
| output  | output?: (output: TaskOutput) => void  | 实现任务增量输出条件定义  |
| beforeRun  | beforeRun?: (taskContext: HvigorTaskContext) => void | Promise<void>  | 在run函数执行前被执行  |
| afterRun  | afterRun?: (taskContext: HvigorTaskContext) => void | Promise<void>  | 在run函数执行后被执行  |
| run  | run: (taskContext: HvigorTaskContext) => void | Promise<void>  | 任务执行逻辑主体函数  |
| dependencies  | dependencies?: (() => string[]) | string[]  | 配置前置依赖任务  |
| postDependencies  | postDependencies?: (() => string[]) | string[]  | 配置后置依赖任务  |
成员
声明
描述
name
name: string
任务名称定义
context
context?: (() => any) | any
定义任务中局部共享的数据对象
input
input?: (input: TaskInput) => void
实现任务增量输入条件定义
output
output?: (output: TaskOutput) => void
实现任务增量输出条件定义
beforeRun
beforeRun?: (taskContext: HvigorTaskContext) => void | Promise<void>
在run函数执行前被执行
afterRun
afterRun?: (taskContext: HvigorTaskContext) => void | Promise<void>
在run函数执行后被执行
run
run: (taskContext: HvigorTaskContext) => void | Promise<void>
任务执行逻辑主体函数
dependencies
dependencies?: (() => string[]) | string[]
配置前置依赖任务
postDependencies
postDependencies?: (() => string[]) | string[]
配置后置依赖任务
name
name: string
任务名称定义。
类型:
| 类型  | 说明  |
| --- | --- |
| string  | 任务名称  |
类型
说明
string
任务名称
context
context?: (() => any) | any
任务中的局部内数据共享的对象定义。实现此函数中定义的对象将在任务注册时被注入到this.context属性上，在input、output、run函数中可使用直接this.context调用context函数中定义的对象和属性。
返回值:
| 类型  | 说明  |
| --- | --- |
| (() => any) | any  | 自定义返回类型的Function或自定义任一返回类型  |
类型
说明
(() => any) | any
自定义返回类型的Function或自定义任一返回类型
input
input?: (input: TaskInput) => void
实现任务增量输入条件定义。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| input  | TaskInput  | 是  | 控制任务增量的输入条件实现对象  |
参数名
类型
必填
说明
input
TaskInput
是
控制任务增量的输入条件实现对象
output
output?: (output: TaskOutput) => void
实现任务增量输出条件定义。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| output  | TaskOutput  | 是  | 控制任务增量的输出条件实现对象  |
参数名
类型
必填
说明
output
TaskOutput
是
控制任务增量的输出条件实现对象
run
run: (taskContext: HvigorTaskContext) => void | Promise<void>
任务执行逻辑主体函数。您可以在此函数实现中定义您所需的任务处理逻辑。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| taskContext  | HvigorTaskContext  | 否  | 接口中默认注入的公共信息类型  |
参数名
类型
必填
说明
taskContext
HvigorTaskContext
否
接口中默认注入的公共信息类型
返回值:
| 类型  | 说明  |
| --- | --- |
| (taskContext: HvigorTaskContext) => void | Promise<void>  | 入参类型为HvigorTaskContext、返回类型为void的函数，或Promise<void>类型  |
类型
说明
(taskContext: HvigorTaskContext) => void | Promise<void>
入参类型为HvigorTaskContext、返回类型为void的函数，或Promise<void>类型
beforeRun
beforeRun?: (taskContext: HvigorTaskContext) => void | Promise<void>
run函数的前置处理函数。在任务执行阶段，任务中的run函数执行前此函数被调用执行。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| taskContext  | HvigorTaskContext  | 否  | 接口中默认注入的公共信息  |
参数名
类型
必填
说明
taskContext
HvigorTaskContext
否
接口中默认注入的公共信息
返回值:
| 类型  | 说明  |
| --- | --- |
| (taskContext: HvigorTaskContext) => void | Promise<void>  | 入参类型为HvigorTaskContext、返回类型为void的函数，或Promise<void>类型  |
类型
说明
(taskContext: HvigorTaskContext) => void | Promise<void>
入参类型为HvigorTaskContext、返回类型为void的函数，或Promise<void>类型
afterRun
afterRun?: (taskContext: HvigorTaskContext) => void | Promise<void>
run函数的后置处理函数。在任务执行阶段，任务中的run函数执行后此函数被调用执行。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| taskContext  | HvigorTaskContext  | 否  | 接口中默认注入的公共信息类型  |
参数名
类型
必填
说明
taskContext
HvigorTaskContext
否
接口中默认注入的公共信息类型
返回值:
| 类型  | 说明  |
| --- | --- |
| (taskContext: HvigorTaskContext) => void | Promise<void>  | 入参类型为HvigorTaskContext、返回类型为void的函数，或Promise<void>类型  |
类型
说明
(taskContext: HvigorTaskContext) => void | Promise<void>
入参类型为HvigorTaskContext、返回类型为void的函数，或Promise<void>类型
dependencies
dependencies?: (() => string[]) | string[]
配置前置任务依赖。
补充：前置任务依赖是指当前任务依赖另一个任务，执行顺序是前置任务 -> 当前任务 -> 后置任务。
返回值:
| 类型  | 说明  |
| --- | --- |
| (() => string[]) | string[]  | 返回类型为string[]的函数或string[]类型  |
类型
说明
(() => string[]) | string[]
返回类型为string[]的函数或string[]类型
postDependencies
postDependencies?: (() => string[]) | string[]
配置任务的后置任务依赖。
说明：后置任务依赖是指另一个任务依赖当前任务，执行顺序是前置任务 -> 当前任务 -> 后置任务。
返回值:
| 类型  | 说明  |
| --- | --- |
| (() => string[]) | string[]  | 返回类型为string[]的函数或string[]类型  |
类型
说明
(() => string[]) | string[]
返回类型为string[]的函数或string[]类型
TaskInput
任务增量执行判断的输入对象实现类型，提供添加任务输入条件的基本函数。
导入模块
| 接口成员  | 声明  | 成员描述  |
| --- | --- | --- |
| property  | property(key: string, value: TaskInputValue): TaskInput  | 添加键值对作为Task增量输入条件  |
| file  | file(path: string): TaskInput  | 添加单个文件/文件夹路径作为Task增量输入  |
| files  | files(paths: string[]): TaskInput  | 添加多个文件/文件夹路径作为Task增量输入  |
接口成员
声明
成员描述
property
property(key: string, value: TaskInputValue): TaskInput
添加键值对作为Task增量输入条件
file
file(path: string): TaskInput
添加单个文件/文件夹路径作为Task增量输入
files
files(paths: string[]): TaskInput
添加多个文件/文件夹路径作为Task增量输入
property
property(key: string, value: TaskInputValue): TaskInput
添加键值对作为Task增量输入条件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| key  | string  | 是  | 条件名称  |
| value  | TaskInputValue  | 是  | 支持基本数组类型number、string、boolean及对应的数组类型的参数  |
参数名
类型
必填
说明
key
string
是
条件名称
value
TaskInputValue
是
支持基本数组类型number、string、boolean及对应的数组类型的参数
file
file(path: string): TaskInput
添加单个目录或文件路径作为任务增量输入条件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| path  | string  | 是  | 目录或文件路径  |
参数名
类型
必填
说明
path
string
是
目录或文件路径
返回值:
| 类型  | 说明  |
| --- | --- |
| TaskInput  | 当前控制任务增量的输入条件对象，用于链式调用  |
类型
说明
TaskInput
当前控制任务增量的输入条件对象，用于链式调用
files
files(paths: string[]): TaskInput
添加多个目录或文件路径作为任务增量输入条件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| paths  | string  | 是  | 目录或文件路径列表  |
参数名
类型
必填
说明
paths
string
是
目录或文件路径列表
返回值:
| 类型  | 说明  |
| --- | --- |
| TaskInput  | 当前控制任务增量的输入条件对象，用于链式调用  |
类型
说明
TaskInput
当前控制任务增量的输入条件对象，用于链式调用
TaskOutput
任务增量执行判断的输出对象实现类型，提供添加任务输出条件的基本函数。
导入模块
| 成员  | 声明  | 描述  |
| --- | --- | --- |
| file  | file(path: string): TaskOutput  | 添加单个目录或文件路径作为输出条件  |
| files  | files(paths: string[]): TaskOutput  | 添加多个目录或文件路径作为输出条件  |
成员
声明
描述
file
file(path: string): TaskOutput
添加单个目录或文件路径作为输出条件
files
files(paths: string[]): TaskOutput
添加多个目录或文件路径作为输出条件
file
file(path: string): TaskOutput
添加单个目录或文件路径作为任务的增量输出条件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| path  | string  | 是  | 目录或文件路径  |
参数名
类型
必填
说明
path
string
是
目录或文件路径
返回值:
| 类型  | 说明  |
| --- | --- |
| TaskOutput  | 当前控制任务增量的输出条件对象，用于支持链式调用  |
类型
说明
TaskOutput
当前控制任务增量的输出条件对象，用于支持链式调用
files
files(paths: string[]): TaskOutput
添加多个目录或文件路径作为任务的增量输出条件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| paths  | string[]  | 是  | 目录或文件路径列表  |
参数名
类型
必填
说明
paths
string[]
是
目录或文件路径列表
返回值:
| 类型  | 说明  |
| --- | --- |
| TaskOutput  | 控制任务增量的输出条件对象，用于支持链式调用  |
类型
说明
TaskOutput
控制任务增量的输出条件对象，用于支持链式调用
Task
HvigorTask的外置对象。您可以使用此对象访问任务的属性、 操作任务提供的接口函数。
导入模块
| 成员  | 声明  | 描述  |
| --- | --- | --- |
| getName  | getName: () => string  | 获取任务名称  |
| getDependencies  | getDependencies: () => string[]  | 获取当前任务依赖的任务名称列表  |
| setEnable  | setEnable: (enable: boolean) => void  | 设置任务的启动状态  |
| beforeRun  | beforeRun: (fn: Function) => void  | 添加任务执行之前的钩子函数  |
| afterRun  | afterRun: (fn: Function) => void  | 添加任务执行之后的钩子函数  |
成员
声明
描述
getName
getName: () => string
获取任务名称
getDependencies
getDependencies: () => string[]
获取当前任务依赖的任务名称列表
setEnable
setEnable: (enable: boolean) => void
设置任务的启动状态
beforeRun
beforeRun: (fn: Function) => void
添加任务执行之前的钩子函数
afterRun
afterRun: (fn: Function) => void
添加任务执行之后的钩子函数
getName
getName: () => string
获取任务名称。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 任务名称  |
类型
说明
string
任务名称
getDependencies
getDependencies: () => string[]
获取当前任务依赖的前置任务名称列表。
返回值:
| 类型  | 说明  |
| --- | --- |
| string[]  | 任务的依赖的任务名称列表  |
类型
说明
string[]
任务的依赖的任务名称列表
setEnable
setEnable: (enable: boolean) => void
设置任务的启用状态，当任务被禁用时，任务仍然在任务依赖图中存在，仅跳过了任务的执行不会破坏原来设定的任务依赖关系。任务被注册时任务状态默认是启用的。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| enable  | boolean  | 是  | true：启用任务， false: 禁用任务  |
参数名
类型
必填
说明
enable
boolean
是
true：启用任务， false: 禁用任务
beforeRun
beforeRun: (fn: Function) => void
添加任务执行之前的钩子函数。钩子函数以栈结构存储，遵循先进后出原则，后添加的函数先被执行。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | Function  | 是  | 回调函数  |
参数名
类型
必填
说明
fn
Function
是
回调函数
afterRun
afterRun: (fn: Function) => void
添加任务执行完成之后的钩子函数。钩子函数以堆结构存储，遵循先进先出原则，先添加的函数先被执行。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| fn  | Function  | 是  | 回调函数  |
参数名
类型
必填
说明
fn
Function
是
回调函数
NormalizedFile4.3.0+
hvigor API中的文件类。您可以通过此对象来进行一些基本的文件操作。
| 成员  | 声明  | 描述  | 开始支持的版本  |
| --- | --- | --- | --- |
| filePath  | filePath: string  | 当前对象的路径信息  | Hvigor 4.3.0  |
| getPath  | getPath: () => string  | 获取当前对象路径信息  | Hvigor 4.3.0  |
| file  | file: (_path: string) => NormalizedFile  | 在原有的NormalizedFile对象的路径链式拼接，获取它的NormalizedFile对象  | Hvigor 4.3.0  |
| asFileList  | asFileList: () => NormalizedFile[]  | 获取到NormalizedFile对象下深层递归的目录与文件NormalizedFile[]，包含它本身  | Hvigor 4.3.0  |
成员
声明
描述
开始支持的版本
filePath
filePath: string
当前对象的路径信息
Hvigor 4.3.0
getPath
getPath: () => string
获取当前对象路径信息
Hvigor 4.3.0
file
file: (_path: string) => NormalizedFile
在原有的NormalizedFile对象的路径链式拼接，获取它的NormalizedFile对象
Hvigor 4.3.0
asFileList
asFileList: () => NormalizedFile[]
获取到NormalizedFile对象下深层递归的目录与文件NormalizedFile[]，包含它本身
Hvigor 4.3.0
filePath4.3.0+
filePath: string
当前对象的路径信息。
getPath4.3.0+
getPath: () => string
获取当前路径信息。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 当前对象的路径信息  |
类型
说明
string
当前对象的路径信息
file4.3.0+
file: (_path: string) => NormalizedFile
在原有的目录路径链式拼接路径，获取它的NormalizedFile对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| _path  | string  | 是  | 需要拼接路径字符串  |
参数名
类型
必填
说明
_path
string
是
需要拼接路径字符串
返回值:
| 类型  | 说明  |
| --- | --- |
| NormalizedFile  | 在原有的NormalizedFile对象的路径链式拼接所得到NormalizedFile对象  |
类型
说明
NormalizedFile
在原有的NormalizedFile对象的路径链式拼接所得到NormalizedFile对象
asFileList4.3.0+
asFileList: () => NormalizedFile[]
获取到NormalizedFile对象下深层递归的目录与文件NormalizedFile[]，包含它本身。
返回值:
| 类型  | 说明  |
| --- | --- |
| NormalizedFile[]  | NormalizedFile对象下深层递归的目录与文件NormalizedFile[]，包含它本身  |
类型
说明
NormalizedFile[]
NormalizedFile对象下深层递归的目录与文件NormalizedFile[]，包含它本身
当前只能通过node节点的 node.nodeDir 或者 node.node.getNodeDir() 获取该node节点的根路径的NormalizedFile对象，再通过NormalizedFile.file(_path: string)方法拼接后续路径来获取到新的NormalizedFile对象，工程级hvigorfile.ts示例：
FileUtil4.3.0+
文件操作工具类，支持一些基本的文件操作。
导入模块
| 成员  | 声明  | 描述  | 开始支持的版本  |
| --- | --- | --- | --- |
| exist  | exist: (filePath: string) => boolean  | 判断文件路径是否存在  | Hvigor 4.3.0  |
| isDictionary  | isDictionary: (file: string | NormalizedFile) => boolean  | 判断文件路径或NormalizedFile对象是否是目录  | Hvigor 4.3.0  |
| isFile  | isFile: (file: string | NormalizedFile) => boolean  | 判断文件路径或NormalizedFile对象是否是文件  | Hvigor 4.3.0  |
| ensureDirSync  | ensureDirSync: (dirPath: string) => void  | 确保目录存在，不存在就创建  | Hvigor 4.3.0  |
| ensureFileSync  | ensureFileSync: (filePath: string) => void  | 确保文件存在，不存在就创建  | Hvigor 4.3.0  |
| readJson5  | readJson5: (file: string | NormalizedFile) => JSON  | 读取Json5文件  | Hvigor 4.3.0  |
| readFileSync  | readFileSync: (file: string | NormalizedFile) => Buffer  | 同步读取文件  | Hvigor 4.3.0  |
| readFile  | readFile: (file: string | NormalizedFile) => Promise<Buffer>  | 异步读取文件  | Hvigor 4.3.0  |
| writeFileSync  | writeFileSync: (file: string | NormalizedFile, content: any) => void  | 同步写入文件  | Hvigor 4.3.0  |
| writeFile  | writeFile: (file: string | NormalizedFile, content: any) => Promise<void>  | 异步写入文件  | Hvigor 4.3.0  |
| copyFileSync  | copyFileSync: (file: string | NormalizedFile, dest: string) => void  | 同步复制文件  | Hvigor 4.3.0  |
| copyFile  | copyFile: (file: string | NormalizedFile, dest: string) => Promise<void>  | 异步复制文件  | Hvigor 4.3.0  |
| pathResolve  | pathResolve: (...paths: string[]) => string  | 拼接路径方法类  | Hvigor 4.3.0  |
成员
声明
描述
开始支持的版本
exist
exist: (filePath: string) => boolean
判断文件路径是否存在
Hvigor 4.3.0
isDictionary
isDictionary: (file: string | NormalizedFile) => boolean
判断文件路径或NormalizedFile对象是否是目录
Hvigor 4.3.0
isFile
isFile: (file: string | NormalizedFile) => boolean
判断文件路径或NormalizedFile对象是否是文件
Hvigor 4.3.0
ensureDirSync
ensureDirSync: (dirPath: string) => void
确保目录存在，不存在就创建
Hvigor 4.3.0
ensureFileSync
ensureFileSync: (filePath: string) => void
确保文件存在，不存在就创建
Hvigor 4.3.0
readJson5
readJson5: (file: string | NormalizedFile) => JSON
读取Json5文件
Hvigor 4.3.0
readFileSync
readFileSync: (file: string | NormalizedFile) => Buffer
同步读取文件
Hvigor 4.3.0
readFile
readFile: (file: string | NormalizedFile) => Promise<Buffer>
异步读取文件
Hvigor 4.3.0
writeFileSync
writeFileSync: (file: string | NormalizedFile, content: any) => void
同步写入文件
Hvigor 4.3.0
writeFile
writeFile: (file: string | NormalizedFile, content: any) => Promise<void>
异步写入文件
Hvigor 4.3.0
copyFileSync
copyFileSync: (file: string | NormalizedFile, dest: string) => void
同步复制文件
Hvigor 4.3.0
copyFile
copyFile: (file: string | NormalizedFile, dest: string) => Promise<void>
异步复制文件
Hvigor 4.3.0
pathResolve
pathResolve: (...paths: string[]) => string
拼接路径方法类
Hvigor 4.3.0
exist4.3.0+
exist: (filePath: string) => boolean
判断文件路径是否存在。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| filePath  | string  | 是  | 文件路径字符串  |
参数名
类型
必填
说明
filePath
string
是
文件路径字符串
返回值:
| 类型  | 说明  |
| --- | --- |
| boolean  | true: 文件路径存在，false: 文件路径不存在  |
类型
说明
boolean
true: 文件路径存在，false: 文件路径不存在
isDictionary4.3.0+
isDictionary: (file: string | NormalizedFile) => boolean
判断文件路径或NormalizedFile对象是否是目录。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | 文件路径字符串或者是NormalizedFile对象  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
文件路径字符串或者是NormalizedFile对象
返回值:
| 类型  | 说明  |
| --- | --- |
| boolean  | true: 是目录，false: 不是目录  |
类型
说明
boolean
true: 是目录，false: 不是目录
isFile4.3.0+
isFile: (file: string | NormalizedFile) => boolean
判断文件路径或NormalizedFile对象是否是文件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | 文件路径字符串或者是NormalizedFile对象  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
文件路径字符串或者是NormalizedFile对象
返回值:
| 类型  | 说明  |
| --- | --- |
| boolean  | true: 是文件，false: 不是文件  |
类型
说明
boolean
true: 是文件，false: 不是文件
ensureDirSync4.3.0+
ensureDirSync: (dirPath: string) => void
确保目录存在，不存在就创建。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| dirPath  | string  | 是  | 目标目录地址  |
参数名
类型
必填
说明
dirPath
string
是
目标目录地址
ensureFileSync4.3.0+
ensureFileSync: (filePath: string) => void
确保文件存在，不存在就创建。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| filePath  | string  | 是  | 目标文件地址  |
参数名
类型
必填
说明
filePath
string
是
目标文件地址
readJson54.3.0+
readJson5: (file: string | NormalizedFile) => JSON
同步读取Json5文件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | json5文件路径或者NormalizedFile对象  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
json5文件路径或者NormalizedFile对象
返回值:
| 类型  | 说明  |
| --- | --- |
| JSON  | 读取出的JSON格式数据  |
类型
说明
JSON
读取出的JSON格式数据
readFileSync4.3.0+
readFileSync: (file: string | NormalizedFile) => Buffer
同步读取文件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | 文件路径字符串或者是NormalizedFile对象  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
文件路径字符串或者是NormalizedFile对象
返回值:
| 类型  | 说明  |
| --- | --- |
| Buffer  | 读取的Buffer数据  |
类型
说明
Buffer
读取的Buffer数据
readFile4.3.0+
readFile: (file: string | NormalizedFile) => Promise<Buffer>
异步读取文件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | 文件路径字符串或者是NormalizedFile对象  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
文件路径字符串或者是NormalizedFile对象
返回值:
| 类型  | 说明  |
| --- | --- |
| Promise  | Promise<Buffer>  |
类型
说明
Promise
Promise<Buffer>
writeFileSync4.3.0+
writeFileSync: (file: string | NormalizedFile, content: any) => void
同步写入文件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | 文件路径字符串或者是NormalizedFile对象  |
| content  | any  | 是  | 需要写入文件的内容  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
文件路径字符串或者是NormalizedFile对象
content
any
是
需要写入文件的内容
writeFile4.3.0+
writeFile: (file: string | NormalizedFile, content: any) => Promise<void>
异步写入文件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | 文件路径字符串或者是NormalizedFile对象  |
| content  | any  | 是  | 需要写入文件的内容  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
文件路径字符串或者是NormalizedFile对象
content
any
是
需要写入文件的内容
返回值:
| 类型  | 说明  |
| --- | --- |
| Promise  | Promise<void>  |
类型
说明
Promise
Promise<void>
copyFileSync4.3.0+
copyFileSync: (file: string | NormalizedFile, dest: string) => void
同步复制文件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | 文件路径字符串或者是NormalizedFile对象  |
| dest  | string  | 是  | 目标文件路径  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
文件路径字符串或者是NormalizedFile对象
dest
string
是
目标文件路径
copyFile4.3.0+
copyFile: (file: string | NormalizedFile, dest: string) => Promise<void>
异步复制文件。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| file  | string | NormalizedFile  | 是  | 文件路径字符串或者是NormalizedFile对象  |
| dest  | string  | 是  | 目标文件路径  |
参数名
类型
必填
说明
file
string | NormalizedFile
是
文件路径字符串或者是NormalizedFile对象
dest
string
是
目标文件路径
返回值:
| 类型  | 说明  |
| --- | --- |
| Promise  | Promise<void>  |
类型
说明
Promise
Promise<void>
pathResolve4.3.0+
pathResolve: (...paths: string[]) => string
拼接路径。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| ...paths  | string[]  | 是  | 文件路径信息数组  |
参数名
类型
必填
说明
...paths
string[]
是
文件路径信息数组
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 拼接后得到的路径信息  |
类型
说明
string
拼接后得到的路径信息

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-expanding-project-model-V14
爬取时间: 2025-04-30 07:55:22
来源: Huawei Developer
Product
HarmonyOS应用工程级配置中的Product信息接口。
导入模块
Product:
| 成员  | 声明  | 描述  |
| --- | --- | --- |
| getProductName  | getProductName: () => string  | 获取product名称  |
| getBundleType  | getBundleType: () => string  | 获取product使用的bundleType信息  |
| getBundleName  | getBundleName: () => string  | 获取product使用的bundleName信息  |
成员
声明
描述
getProductName
getProductName: () => string
获取product名称
getBundleType
getBundleType: () => string
获取product使用的bundleType信息
getBundleName
getBundleName: () => string
获取product使用的bundleName信息
getProductName
getProductName: () => string
获取product名称。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | product名称  |
类型
说明
string
product名称
getBundleType
getBundleType: () => string
获取product使用的bundleType信息。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | bundleType值  |
类型
说明
string
bundleType值
getBundleName
getBundleName: () => string
获取product使用的bundleName信息。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | bundleName值  |
类型
说明
string
bundleName值
Target
HarmonyOS应用模块级配置中的Target信息接口。
导入模块
| 成员  | 声明  | 描述  |
| --- | --- | --- |
| getCurrentProduct  | getCurrentProduct: () => Product  | 获取当前Target配置的Product。  |
| getBuildTargetOutputPath  | getBuildTargetOutputPath: () => string  | 获取当前target构建产物输出路径。  |
| getTargetName  | getTargetName: () => string  | 获取target名称。  |
成员
声明
描述
getCurrentProduct
getCurrentProduct: () => Product
获取当前Target配置的Product。
getBuildTargetOutputPath
getBuildTargetOutputPath: () => string
获取当前target构建产物输出路径。
getTargetName
getTargetName: () => string
获取target名称。
getCurrentProduct
getCurrentProduct: () => Product
获取当前Target配置的Product。
返回值:
| 类型  | 说明  |
| --- | --- |
| Product  | 当前构建target应用的Product对象  |
类型
说明
Product
当前构建target应用的Product对象
getBuildTargetOutputPath
getBuildTargetOutputPath: () => string
获取当前target构建产物输出路径。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 当前target构建产物输出路径  |
类型
说明
string
当前target构建产物输出路径
getTargetName
getTargetName: () => string
获取target名称。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | target名称  |
类型
说明
string
target名称

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-expanding-context-V14
爬取时间: 2025-04-30 07:55:57
来源: Huawei Developer
OhosPluginId
本组件是hvigor-ohos-plugin插件id常量类。
导入模块
常量:
| 常量名  | 类型  | 描述  |
| --- | --- | --- |
| OHOS_APP_PLUGIN  | string  | AppPlugin插件ID  |
| OHOS_HAP_PLUGIN  | string  | HapPlugin插件ID  |
| OHOS_HSP_PLUGIN  | string  | HspPlugin插件ID  |
| OHOS_HAR_PLUGIN  | string  | HarPlugin插件ID  |
常量名
类型
描述
OHOS_APP_PLUGIN
string
AppPlugin插件ID
OHOS_HAP_PLUGIN
string
HapPlugin插件ID
OHOS_HSP_PLUGIN
string
HspPlugin插件ID
OHOS_HAR_PLUGIN
string
HarPlugin插件ID
OhosAppContext
本组件是appTasks插件对外提供的上下文扩展接口，包括工程信息、product信息等。
导入模块
getProjectName
getProjectName: () => string
获取工程名称。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 工程名称  |
类型
说明
string
工程名称
getProjectPath
getProjectPath: () => string
获取工程路径。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 工程路径  |
类型
说明
string
工程路径
getBuildRootPath
getBuildRootPath: () => string
获取构建目录根路径。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 构建根路径  |
类型
说明
string
构建根路径
getBuildProductOutputPath
getBuildProductOutputPath: () => string
获取当前product构建的打包输出路径。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 当前product构建的打包输出路径  |
类型
说明
string
当前product构建的打包输出路径
getCurrentProduct
getCurrentProduct: () => Product
获取当前构建指定的product对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| Product  | 当前构建指定的product对象  |
类型
说明
Product
当前构建指定的product对象
getBuildMode
getBuildMode: () => string
获取当前构建指定的BuildMode。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 当前构建指定的BuildMode  |
类型
说明
string
当前构建指定的BuildMode
getAppJsonOpt
getAppJsonOpt: () => any
获取当前构建的app.json5文件中内容的obj对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| any  | 当前构建的app.json5文件中内容的obj对象  |
类型
说明
any
当前构建的app.json5文件中内容的obj对象
setAppJsonOpt
setAppJsonOpt: (appJsonOpt) => void
修改当前构建的app.json5文件中内容的obj对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| appJsonOpt  | any  | 是  | 设置当前构建的app.json5文件解析出来的obj对象  |
参数名
类型
必填
说明
appJsonOpt
any
是
设置当前构建的app.json5文件解析出来的obj对象
在工程级hvigorfile.ts中编写示例代码：
setAppJsonOpt会进行schema校验，如果传入的对象不符合校验规则则会抛出异常。
getBuildProfileOpt
getBuildProfileOpt: () => any
获取当前构建的根目录下build-profile.json5文件中内容的obj对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| any  | 当前构建的根目录下build-profile.json5文件中内容的obj对象  |
类型
说明
any
当前构建的根目录下build-profile.json5文件中内容的obj对象
setBuildProfileOpt
setBuildProfileOpt: (buildProfileOpt) => any
设置当前构建的build-profile.json5文件中内容的obj对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| buildProfileOpt  | any  | 是  | 设置当前构建的根目录下build-profile.json5文件中内容的obj对象  |
参数名
类型
必填
说明
buildProfileOpt
any
是
设置当前构建的根目录下build-profile.json5文件中内容的obj对象
setBuildProfileOpt会进行schema校验，如果传入的对象不符合校验规则则会抛出异常。
getOhpmDependencyInfo5.0.0+
getOhpmDependencyInfo: () => Record<string, OhpmDependencyInfo> | object
获取工程下oh-package.json5中配置的依赖信息。
返回值:
| 类型  | 说明  |
| --- | --- |
| Record<string, OhpmDependencyInfo> | object  | oh-package.json5中配置的依赖信息  |
类型
说明
Record<string, OhpmDependencyInfo> | object
oh-package.json5中配置的依赖信息
在工程级hvigorfile.ts中编写示例代码：
执行hvigorw --sync输出示例：
getOhpmRemoteHspDependencyInfo5.6.2+
getOhpmRemoteHspDependencyInfo: (signed) => Record<string, OhpmDependencyInfo> | object
获取工程下oh-package.json5中配置的hsp包依赖信息。
参数值:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| signed  | boolean  | 否  | 是否获取签名的hsp包路径，默认为false  |
参数名
类型
必填
说明
signed
boolean
否
是否获取签名的hsp包路径，默认为false
返回值:
| 类型  | 说明  |
| --- | --- |
| Record<string, OhpmDependencyInfo> | object  | 工程下oh-package.json5中配置的hsp包依赖信息  |
类型
说明
Record<string, OhpmDependencyInfo> | object
工程下oh-package.json5中配置的hsp包依赖信息
在工程级hvigorfile.ts中编写示例代码：
执行hvigorw assembleHap输出示例：
getDependenciesOpt5.0.10+
getDependenciesOpt: () => object
获取工程下oh-package.json5中配置的dependencies依赖。
返回值:
| 类型  | 说明  |
| --- | --- |
| object  | 获取工程级别下oh-package.json5中dependencies信息  |
类型
说明
object
获取工程级别下oh-package.json5中dependencies信息
在工程级hvigorfile.ts中编写示例代码：
setDependenciesOpt5.0.10+
setDependenciesOpt: (:any) => any
设置工程下oh-package.json5中的dependencies依赖。
参数值:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| dependencies  | any  | 是  | 设置当前工程下oh-package.json5中dependencies依赖  |
参数名
类型
必填
说明
dependencies
any
是
设置当前工程下oh-package.json5中dependencies依赖
getDevDependenciesOpt5.0.10+
getDevDependenciesOpt: () => object
获取工程下oh-package.json5中配置的devDependencies依赖。
返回值:
| 类型  | 说明  |
| --- | --- |
| object  | 获取工程级别下oh-package.json5中devDependencies信息  |
类型
说明
object
获取工程级别下oh-package.json5中devDependencies信息
在工程级hvigorfile.ts中编写示例代码：
setDevDependenciesOpt5.0.10+
setDevDependenciesOpt: (:any) => any
设置工程下oh-package.json5中的devDependencies依赖。
参数值:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| devDependencies  | any  | 是  | 设置当前工程下oh-package.json5中devdependencies依赖  |
参数名
类型
必填
说明
devDependencies
any
是
设置当前工程下oh-package.json5中devdependencies依赖
getDynamicDependenciesOpt5.0.10+
getDynamicDependenciesOpt: () => object
获取工程下oh-package.json5中配置的dynamicDependencies依赖。
返回值:
| 类型  | 说明  |
| --- | --- |
| object  | 获取工程级别下oh-package.json5中DynamicDependencies信息  |
类型
说明
object
获取工程级别下oh-package.json5中DynamicDependencies信息
在工程级hvigorfile.ts中编写示例代码：
setDynamicDependenciesOpt5.0.10+
setDynamicDependenciesOpt: (:any) => any
设置工程下oh-package.json5中的dynamicDependencies依赖。
参数值:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| dynamicDependencies  | any  | 是  | 设置当前工程下oh-package.json5中dynamicDependencies依赖  |
参数名
类型
必填
说明
dynamicDependencies
any
是
设置当前工程下oh-package.json5中dynamicDependencies依赖
getOverrides5.10.3+
getOverrides:()=>object
获取工程下oh-package.json5中配置的overrides字段。
返回值：
| 类型  | 说明  |
| --- | --- |
| object  | 获取工程下oh-package.json5中配置的overrides字段  |
类型
说明
object
获取工程下oh-package.json5中配置的overrides字段
在工程级hvigorfile.ts中编写示例代码：
setOverrides5.10.3+
setOverrides:(overrides: any)=>void
设置工程下oh-package.json5中的overrides字段。
参数值：
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| overrides  | any  | 是  | 设置工程下oh-package.json5中的overrides字段  |
参数名
类型
必填
说明
overrides
any
是
设置工程下oh-package.json5中的overrides字段
在工程级hvigorfile.ts中编写示例代码：
OhosHapContext
hap模块Plugin提供的上下文接口，在hap模块的hvigor节点中可通过getContext方法传入OhosPluginId.OHOS_HAP_PLUGIN_ID获取该接口，接口中主要包含了hap模块中module、target信息。
导入模块
示例：获取hap模块上下文接口信息。
getModuleName
getModuleName: () => string
获取模块名称。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 模块名称  |
类型
说明
string
模块名称
getModulePath
getModulePath: () => string
获取模块路径。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 模块路径  |
类型
说明
string
模块路径
getModuleType
getModuleType: () => string
获取模块类型，取值来自模块配置文件module.json5中moduleTyp字段。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 模块类型  |
类型
说明
string
模块类型
getBuildProductRootPath
getBuildProductRootPath: () => string
获取模块基于product构建根路径。
返回值:
| 类型  | 说明  |
| --- | --- |
| string  | 模块基于product构建根路径  |
类型
说明
string
模块基于product构建根路径
targets
targets: (callbackfn: (target: Target) => void) => void
当前需构建的target对象回调方法
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| callback  | (target: Target) => void  | 是  | 入参类型为Target，返回类型为void的函数  |
参数名
类型
必填
说明
callback
(target: Target) => void
是
入参类型为Target，返回类型为void的函数
getModuleJsonOpt
getModuleJsonOpt: () => any
获取当前模块的module.json5文件中内容的obj对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| any  | 当前模块的module.json5文件中内容的obj对象  |
类型
说明
any
当前模块的module.json5文件中内容的obj对象
setModuleJsonOpt
setModuleJsonOpt: (moduleJsonOpt) => void
修改当前构建的module.json5文件中内容的obj对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| moduleJsonOpt  | any  | 是  | 设置当前模块的module.json5文件解析出来的obj对象  |
参数名
类型
必填
说明
moduleJsonOpt
any
是
设置当前模块的module.json5文件解析出来的obj对象
setModuleJsonOpt会进行schema校验，如果传入的对象不符合校验规则则会抛出异常。
getBuildProfileOpt
getBuildProfileOpt: () => any
获取当前模块的build-profile.json5文件中内容的obj对象。
返回值:
| 类型  | 说明  |
| --- | --- |
| any  | 当前模块的build-profile.json5文件中内容的obj对象  |
类型
说明
any
当前模块的build-profile.json5文件中内容的obj对象
setBuildProfileOpt
setBuildProfileOpt: (buildProfileOpt) => any
设置当前模块的build-profile.json5文件中内容的obj对象。
参数:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| buildProfileOpt  | any  | 是  | 设置当前模块的build-profile.json5文件中内容的obj对象  |
参数名
类型
必填
说明
buildProfileOpt
any
是
设置当前模块的build-profile.json5文件中内容的obj对象
setBuildProfileOpt会进行schema校验，如果传入的对象不符合校验规则则会抛出异常。
getVersion
getVersion: () => string
获取模块oh-package.json5中配置的版本号。
返回值：
| 类型  | 说明  |
| --- | --- |
| string  | 模块oh-package.json5中配置的版本号  |
类型
说明
string
模块oh-package.json5中配置的版本号
在工程级hvigorfile.ts中编写示例代码：
执行hvigorw --sync输出示例：
setVersion
setVersion: (version: string) => void
修改模块oh-package.json5中的版本号。
参数：
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| version  | string  | 是  | 修改模块oh-package.json5中的版本号  |
参数名
类型
必填
说明
version
string
是
修改模块oh-package.json5中的版本号
在工程级hvigorfile.ts中编写示例代码：
执行hvigorw --sync输出：
getOhpmDependencyInfo5.0.0+
getOhpmDependencyInfo: () => Record<string, OhpmDependencyInfo> | object
获取模块下oh-package.json5中配置的依赖信息。
返回值:
| 类型  | 说明  |
| --- | --- |
| Record<string, OhpmDependencyInfo> | object  | oh-package.json5中配置的依赖信息  |
类型
说明
Record<string, OhpmDependencyInfo> | object
oh-package.json5中配置的依赖信息
在工程级hvigorfile.ts中编写示例代码：
执行hvigorw --sync输出示例：
getOhpmRemoteHspDependencyInfo5.6.2+
getOhpmRemoteHspDependencyInfo: (signed) => Record<string, OhpmDependencyInfo> | object
获取模块下oh-package.json5中配置的hsp包依赖信息。
参数值:
| 参数名  | 类型  | 必填  | 说明  |
| --- | --- | --- | --- |
| signed  | boolean  | 否  | 是否获取签名的hsp包路径，默认为false  |
参数名
类型
必填
说明
signed
boolean
否
是否获取签名的hsp包路径，默认为false
返回值:
| 类型  | 说明  |
| --- | --- |
| Record<string, OhpmDependencyInfo> | object  | 模块下oh-package.json5中配置的hsp包依赖信息  |
类型
说明
Record<string, OhpmDependencyInfo> | object
模块下oh-package.json5中配置的hsp包依赖信息
执行hvigorw assembleHap输出示例：
getDependenciesOpt5.0.10+
与OhosAppContext中的getDependenciesOpt方法一致，请参考上文中getDependenciesOpt接口描述。
setDependenciesOpt5.0.10+
与OhosAppContext中的setDependenciesOpt方法一致，请参考上文中getDependenciesOpt接口描述。
getDevDependenciesOpt5.0.10+
与OhosAppContext中的getDevDependenciesOpt方法一致，请参考上文中getDependenciesOpt接口描述。
setDevDependenciesOpt5.0.10+
与OhosAppContext中的setDevDependenciesOpt方法一致，请参考上文中getDependenciesOpt接口描述。
getDynamicDependenciesOpt5.0.10+
与OhosAppContext中的getDynamicDependenciesOpt方法一致，请参考上文中getDependenciesOpt接口描述。
setDynamicDependenciesOpt5.0.10+
与OhosAppContext中的setDynamicDependenciesOpt方法一致，请参考上文中getDependenciesOpt接口描述。
OhosHspContext
Hsp模块上下文接口信息与OhosHapContext一致，请参考上文中OhosHapContext接口描述。
OhosHarContext
Har模块上下文接口信息与OhosHapContext一致，请参考上文中OhosHapContext接口描述。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-expanding-sample-V14
爬取时间: 2025-04-30 07:56:32
来源: Huawei Developer
示例：在工程级hvigorfile.ts文件中分别注册工程级与模块级任务。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-reinforcement-V14
爬取时间: 2025-04-30 07:57:07
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-build-obfuscation-V14
爬取时间: 2025-04-30 07:57:42
来源: Huawei Developer
DevEco Studio原先默认开启代码混淆功能，会对API 10及以上的Stage工程，且编译模式是release时，自动进行简单的代码混淆，仅对参数名和局部变量名进行混淆。
从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，新建工程及模块默认关闭代码混淆功能，如果在模块级build-profile.json5配置文件中开启代码混淆，则混淆规则配置文件obfuscation-rules.txt中默认开启推荐的混淆规则，包含-enable-property-obfuscation、-enable-toplevel-obfuscation、-enable-filename-obfuscation、-enable-export-obfuscation四项混淆项，开发者可进一步在obfuscation-rules.txt文件中选择开启的混淆项，关于混淆项的介绍请查看配置混淆规则。
使用约束
字段说明
可在模块级build-profile.json5文件中进行代码混淆相关配置。obfuscation字段说明如下：
| 配置项  | 类型  | 是否必填  | 说明  |
| --- | --- | --- | --- |
| ruleOptions  | object  | 否  | 混淆规则配置。  |
|    | enable  | boolean  | 是  | 是否启用代码混淆： true：启用。false（默认值）：不启用。 说明从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认值由true改为false。   |
| files  | array  | 否  | 配置混淆规则文件的相对路径，默认使用obfuscation-rules.txt文件。文件中配置的混淆规则仅在本模块编译时生效（包含依赖代码）。 说明规则文件中支持配置所有混淆规则。支持配置多个文件，文件名称支持自定义，当存在多个混淆规则文件时，规则合并可参考混淆规则合并策略，合并后的规则作用范围可参考开启代码混淆。   |
| consumerFiles  | string/array  | 否  | 仅HAR模块可配置，配置传递给集成方的混淆规则文件的相对路径，支持配置多个文件，文件名称支持自定义。 说明为保证HAR模块可被正确集成使用，若有不希望被集成方混淆的内容，建议在规则文件中配置对应的保留选项，例如HAR模块中导出的变量或函数。 规则文件中配置的混淆选项会与集成方的混淆规则进行合并，进而影响集成方的编译混淆，因此，建议仅配置保留选项。   |
配置项
类型
是否必填
说明
ruleOptions
object
否
混淆规则配置。
enable
boolean
是
是否启用代码混淆：
从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认值由true改为false。
files
array
否
配置混淆规则文件的相对路径，默认使用obfuscation-rules.txt文件。文件中配置的混淆规则仅在本模块编译时生效（包含依赖代码）。
consumerFiles
string/array
否
仅HAR模块可配置，配置传递给集成方的混淆规则文件的相对路径，支持配置多个文件，文件名称支持自定义。
使能混淆
为保护代码资产，建议开启混淆，您可以在模块级的build-profile.json5配置文件中开启代码混淆功能：
从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，开启混淆后，混淆规则配置文件obfuscation-rules.txt中默认开启推荐的混淆规则，包含-enable-property-obfuscation、-enable-toplevel-obfuscation、-enable-filename-obfuscation、-enable-export-obfuscation四项混淆项。
使用release模式编译发布时，建议开启混淆，需要正确配置混淆规则，否则可能会有运行时问题。
使能高阶混淆
在开启混淆后，若您需要更高阶的混淆能力，可以通过以下操作配置高阶混淆规则。
配置所有混淆规则
1.  当存在多个混淆规则文件时，规则合并可参考混淆规则合并策略，合并后的规则作用范围可参考开启代码混淆。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150652.07326272214794243892655522321938:50001231000000:2800:812C2CD9F6D4E43ABE97B0571F891502E3C7B044F5A383A043B81352A569867E.png?needInitFileName=true?needInitFileName=true)
HAR配置保留选项
为保证HAR模块可被正确集成使用，若有不希望被集成方混淆的内容，建议在规则文件中配置对应的保留选项，例如HAR模块中导出的变量或函数。
1.  当存在多个混淆规则文件时，规则合并可参考混淆合并策略，合并后的规则作用范围可参考开启代码混淆。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150652.10911394010545157069380643967106:50001231000000:2800:20FA1360B32E9669CD75F6129A7B57A1490CDBE74E0AA4D7A6ACEC1B4B9B2AA2.png?needInitFileName=true?needInitFileName=true)
通过混淆助手配置保留选项
开启混淆后，代码中的方法、属性或路径被混淆，但运行的时候访问的是未混淆的方法、属性或路径，可能导致功能不可用，因此需要将对应的字段配置保留选项。关于保留选项的排查场景及配置方式请参考配置混淆规则。
需要排查的场景和配置的字段有很多，因此DevEco Studio提供了混淆助手工具（ObfuscationHelper），可以根据模块和场景对源码进行扫描，快速识别需要配置的保留选项和白名单字段，开发者可以一键生成白名单混淆规则文件。由于某些场景是动态访问名称、属性，需要在运行的时候才能确定的字段，ObfuscationHelper会识别该类场景，开发者需要根据业务进一步排查识别白名单后进行配置。
扫描代码
1.
2.
3.
4.
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150652.62579803690860148735868704116251:50001231000000:2800:7CCC5C29CE0245983A57C24F5F4C11461A111B5425E40CF2B9608DF7ED337691.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150652.77752080290384244116017545611232:50001231000000:2800:DF22339EC40E3319A3EAA359A227CE9DA7FFF0691854E3EDEC2CD1E39155732A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150652.42121829384712881792028203008868:50001231000000:2800:03DA8BC72A34BE92818D2B7ACE2BC6BF7339B1DF51D58C3A81B9E8CE7FB5A419.png?needInitFileName=true?needInitFileName=true)
配置推荐白名单
在推荐白名单配置页面，可以查看扫描出来的推荐配置的保留选项和白名单字段，并一键生成白名单混淆规则文件。
1.  选中一个扫描任务，在页面下方会按照以下的树状结构，显示推荐的保留选项和白名单字段。
2.
3.
4.  如entry模块下生成推荐白名单文件：
5.
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150652.53064052217919375772154789183901:50001231000000:2800:C8DFBE6144DC62E18E431743315E1A8188BD1B2B1D359F9C7E3A1D27E1A17E99.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150652.75139497686464964292819336885441:50001231000000:2800:1A7116382B145E5DE8E6346846EE61C379DB01AC16E3E3D97A24A1CB8A64C166.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.41123861472926474918520392946538:50001231000000:2800:4DB4083E04478481D58F982270735B7C053AAE2FB641A9E75FFCA0B8DD37D19E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.10301716012267205743976980858857:50001231000000:2800:15F88F0CFBBEE69AA1F45AE854F5762E228590E4428D81DA3FD0B50F4DA21B4F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.50763168684816113798190362388177:50001231000000:2800:672F9B52A9132D1E5E947CBA694B1C1C9C3FC17F800982FFE79FE4E55F6154D9.png?needInitFileName=true?needInitFileName=true)
配置待排查白名单
在待排查白名单配置页面，可以查看扫描出来的关键代码，需要开发者根据业务进一步排查，识别白名单字段并配置到文件中。
1.  选中一个扫描任务，在页面下方会按照“关键代码 --> 代码所在文件: 代码行”的结构，显示待排查的代码。点击关键代码，可以跳转到代码所在的文件和代码行。
2.
3.  如entry模块下生成排查白名单文件：
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.57165122250202251188836392304359:50001231000000:2800:8A1352541843F683B0A4700FE48D79756C7468002094FEAEC33F17EF07C1FB83.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.34934229720707828569651979388036:50001231000000:2800:DA88C35817AAD4801759854E2F325A35B93FB72247DDA458EA4C9ADF0A31780B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.71569294694664020806892097097308:50001231000000:2800:66357DAA201006FEE3DDF2F7EB5B5D39D129F51EE91C1A1E597CB1908A7F922F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.96427154859409781248704516777593:50001231000000:2800:7CF2415BDDBB274940689D5E19DDEA06EC4251AEE73FC3459B2E1196F09FC5CD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.49682469441225226488447831778708:50001231000000:2800:7EBAE7E4D462ADDE5C435A1E4853BF8670EACE2178E063E55967DC29BB3A5603.png?needInitFileName=true?needInitFileName=true)
查看历史记录
点击生成推荐白名单或者待排查白名单后，会生成一条历史记录，方便开发者后续查看和继续排查白名单。
在ObfuscationHelper的首页，点击底部的历史记录按钮，可查看所有的历史记录。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.49575218094016322755479668913017:50001231000000:2800:8DE44B59FBBD3EE96EB5E6F783B662571CE62CFCAE367BAA6F52C6EBF936FA97.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.13644277211258595002745056630099:50001231000000:2800:E5CBDFFDBD434A36303AA74CFCBD5ADF09098C85A8C8A8C1B44B807C0B9958D3.png?needInitFileName=true?needInitFileName=true)
扫描任务
属性混淆
-  JSON数据解析及对象序列化时，需要保留使用到的字段，详细内容请参考保留选项的-keep-property-name。
-  通过字符串访问的对象属性需要被保留，详细内容请参考保留选项的-keep-property-name。
-  开发者需要根据C++接口来排查与其相关的ArkTS中的属性字符串，并手动加入白名单中，涉及的C++接口参考使用Node-API接口设置ArkTS对象的属性。
-  数据库键值对类型（ValuesBucket）中的属性需要被保留，详细内容请参考保留选项的-keep-property-name。
-  自定义装饰器修饰的成员变量、方法、参数需要被保留，详细内容请参考保留选项的-keep-property-name。
顶层作用域名称混淆
-  namespace中导出的名称需要被保留，详细内容请参考保留选项的-keep-global-name。
文件名名称混淆
-  动态导入的路径名需要被保留，详细内容请参考保留选项的-keep-file-name。
-  传递给动态路由的路径名需要被保留，详细内容请参考保留选项的-keep-file-name。
导入/导出名称混淆
-  从so库中导入的接口及其点式调用的属性，需要被保留。
```typescript
// 导出的常量
export const LOCAL_NUM = 100  // LOCAL_NUM加入keep-global-name
// 导出的方法
export function harFun() {    // harFun加入keep-global-name
}
// 导出的类名及其属性(包括该类的父类和属性)，如果属性也是一个类，该类也需要以同样的方式保留。
class FatherClass {
prop4: string = "bbb"
}
class SubClass {
prop3: string = "bbb"
}
export class HSPClass extends FatherClass{    // 类名称HSPClass加入到-keep-global-name
prop1: string = "aaa"
prop2: SubClass = new SubClass()    // 属性prop1,prop2,prop3,prop4加入到-keep-property-name
}
// 导出的namespace，包括其中的方法、常量、类(保留方式同上)、子namespace
export namespace NmSpace {
export const NUM_NAME_SPACE = 100   // 常量NUM_NAME_SPACE加入-keep-global-name
export class classNameSpace {       // 类名称classNameSpace加入-keep-global-name
prop: string = "bbb"             // 类属性prop加入-keep-property-name
}
export function funNameSpace() {    // 方法funNameSpace加入-keep-global-name
}
}
// 将入口文件相对路径,如 ./index.ets加入keep保留选项。
// 将入口文件名如index.ets加入keep-file-name保留选项。
```
-  从hsp中导入的接口及其点式调用的属性，需要被保留。
-  参考hsp对外暴露的接口。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-faq-V14
爬取时间: 2025-04-30 07:58:17
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-log-V14
爬取时间: 2025-04-30 07:58:51
来源: Huawei Developer
日志是构建工具的主要对外显示的部分，如果日志过于冗长，真正的告警和异常将更容易被隐藏；而另一方面，当出现问题时，你也需要相关的信息来定位问题。Hvigor定义了四种日志级别，如下日志级别所示。
日志级别
| 日志级别  | 日志信息  |
| --- | --- |
| ERROR  | 错误信息  |
| WARN  | 告警信息  |
| INFO  | 正常信息  |
| DEBUG  | 调试信息  |
日志级别
日志信息
ERROR
错误信息
WARN
告警信息
INFO
正常信息
DEBUG
调试信息
选择日志级别
您可以使用命令行中的日志选项开关来控制输出不同的日志级别，还可通过配置hvigor-config.json5中日志选项logging.level来设置。在stacktrace命令选项中，您可以找到影响堆栈跟踪记录的命令开关，当然，你也可以通过配置hvigor-config.json5中日志选项debugging.stacktrace来设置堆栈跟踪日志开关。
日志级别命令行选项
| 日志选项  | 输出日志级别  |
| --- | --- |
| -e 或 --error  | 错误且更高级别  |
| -w 或 --warn  | 告警且更高级别  |
| -i 或 --info  | 信息且更高级别  |
| -d 或 --debug  | 调试且更高级别（即所有日志信息）  |
日志选项
输出日志级别
-e 或 --error
错误且更高级别
-w 或 --warn
告警且更高级别
-i 或 --info
信息且更高级别
-d 或 --debug
调试且更高级别（即所有日志信息）
堆栈跟踪命令行选项
--stacktrace
控制台将打印完整的堆栈跟踪信息。
--no-stacktrace
如果出现构建错误（例如编译错误），则不会将堆栈跟踪信息打印到控制台。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-faqs-V14
爬取时间: 2025-04-30 07:59:29
来源: Huawei Developer
如何解决编译过程内存过高
问题现象
编译构建时，内存或CPU占用过高，导致出现DevEco Studio运行卡顿、延迟等现象。
解决措施
-  可以在hvigor-config.json5中添加配置。 当配置项"hvigor.pool.maxSize"和"ohos.arkCompile.maxSize"的值改小，"hvigor.enableMemoryCache"改为false后，可能会导致编译时长增加，请耐心等待。
-  使用非并行模式编译，内存占用会减少，但可能会导致编译时长增加，请耐心等待。
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.97480824971292812332751531322580:50001231000000:2800:0D1C769D392BF9F879119C372F1F3219F50BEF111F01C5838F4344565227F99D.png?needInitFileName=true?needInitFileName=true)
构建报错“Cannot read properties of undefined(reading 'xxx')”
问题现象
编译构建时，出现报错“Cannot read properties of undefined(reading 'xxx')”。
解决措施
打开堆栈信息排查hvigorconfig.ts文件和hvigorfile.ts文件里的代码，里面是否使用了未定义的属性。
堆栈打开方法：项目根目录/hvigor/hvigor-config.json5文件中配置如下内容：
如果上述文件中并未排查出问题，请及时向我们提单反馈。
请按照如下步骤进行操作：提单链接，在线提单->HarmonyOS NEXT->开发工具->DevEco Studio。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.56126438105233702356381461028799:50001231000000:2800:2FC399A403D3FE7F078F9141FC648BB372A5D284C6366EF174C73F1F200B5844.png?needInitFileName=true?needInitFileName=true)
构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”
问题现象
编译构建时，出现报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”。
问题原因是构建时存在不同版本的同名so文件。比如将har模块产物里的so文件拷贝到entry模块的libs目录下，这时har模块里有一个libhar.so，entry模块里也有一个libhar.so，再配置entry依赖har，构建entry就会出现报错。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150653.18080802459100128713154756562253:50001231000000:2800:38CFF46394286F5B26538577D237F54BCFD117C7995D06B586C379F62D099D13.png?needInitFileName=true?needInitFileName=true)
解决措施
使用select、pickFirsts、pickLasts等配置选中要使用的so文件; select提供native产物的精准选择能力，优先级高于excludes、pickFirsts等配置项。pickFirsts、pickLasts按照.so文件的优先级顺序，打包最高优先级的.so文件，优先级顺序是指依赖收集的顺序，越晚被收集优先级越高。
具体可参考：配置文件说明 > build-profile.json5。
基于上面的例子，可以在entry的build-profile.json5中添加配置select选中har模块中的so文件，package选中包名为“har”的模块, include选中“libhar.so”文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.89910355096011251599121471314063:50001231000000:2800:4D6C6BF9B4C0BE304CFE35E4550818A9191547966FC22E24F505A56A84238CE0.png?needInitFileName=true?needInitFileName=true)
构建报错“input module releaseType is different”
问题现象
打包APP时，提示“input module releaseType is different”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.36980840211764741482361668796327:50001231000000:2800:297381B5F199702D6B8D7C85387E8BEB2560F856E2794A644B1B248F149B6E75.png?needInitFileName=true?needInitFileName=true)
解决措施
根据报错日志的Warning信息所提示的模块名称，检查模块间的apiReleaseType字段是否一致。
该apiReleaseType字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中。如下图所示，首先确认各模块间该字段是否一致，如果存在不一致的情况，需要将应用的各个模块，使用相同版本的SDK重新打包，然后打包APP。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.41375504923461734897699361162116:50001231000000:2800:F67774508F1E04F0BECF2EC63D2A79D3A9C6376B26F4ED180FD32F5D3D4EC861.png?needInitFileName=true?needInitFileName=true)
构建报错“debug is different”
问题现象
打包APP时，提示“debug is different”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.58306320620023294530923938487923:50001231000000:2800:5CEC09449E2BDE957A7964D7F041D42404112477D03AC0041D25A73F6120013A.png?needInitFileName=true?needInitFileName=true)
解决措施
根据报错日志的Warning信息所提示的模块名称，检查模块间的debug字段是否一致，尤其需要关注本地模块和外部引用模块之间是否一致。
1.该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.45199578886140539096947771294275:50001231000000:2800:15FA86F36BCC7874D2EF965E0668342C7E42AA0D2E7E16BB0BFE0ED79105E925.png?needInitFileName=true?needInitFileName=true)
2.编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.21453212789467460277529700436316:50001231000000:2800:5CAB91E06E321A9509396EC2FEFB572461546BD881F7977D6407504EF2588EA5.png?needInitFileName=true?needInitFileName=true)
构建报错“proxy data is duplicated”
问题现象
打包APP时，提示“uri datashareproxy://bundleName/** in proxy data is duplicated”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.65194214548144707089213091147681:50001231000000:2800:694A3E3C71FD1C19B60B44149CDD5D4AD459D25DB0DEBCB89D122B4913D2D04B.png?needInitFileName=true?needInitFileName=true)
解决措施
proxyData标识模块提供的数据代理列表，只允许entry和feature配置，不同的proxyData中配置的URI不可重复。遇到此问题，检查模块间是否配置了相同uri的proxyData。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.91063708918293156050857522527618:50001231000000:2800:C7A39162569D88801A9A6161C5C56F26B571367D0005C8BF09BB5EEB93816340.png?needInitFileName=true?needInitFileName=true)
编译报错“Init keystore failed: parseAlgParameters failed: ObjectIdentifier()”
问题现象
编译构建时，出现错误：Init keystore failed: parseAlgParameters failed: ObjectIdentifier()。
错误原因
使用高版本JDK生成密钥对(p12)，再使用低版本的JDK执行签名命令时，会因为不兼容导致解析p12失败，从而签名失败。
场景
解决方案
请检查当前使用的JDK版本和生产密钥对使用的JDK版本，使用版本匹配的JDK执行签名命令。
编译报错“generate SignerBlock failed”
问题现象
编译构建时，出现错误：message:generate SignerBlock failed。
错误原因
签名用的公私钥对不匹配，使用私钥签名后，用公钥验签失败。需保证私钥(keyalias)和公钥(appCertPath)配对使用。
场景
解决方案
请选择正确、配对的keyalias和appCertPath文件。
编译报错“java.io.IOException: DerValue.getOID, not an OID 49”
问题现象
编译构建时，出现错误：java.io.IOException: DerValue.getOID, not an OID 49。
报错原因
证书文件解析失败，找不到证书的OID。
场景
解决方案
请检查证书文件是否正确。
编译报错“JS heap out of memory”
问题现象
编译构建时，出现报错“JS heap out of memory“。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.88867540285566147445140901891152:50001231000000:2800:503CD862EDCBA85DC41E2A8381443F10291D64C307B771FD8E65C2E21717514D.png?needInitFileName=true?needInitFileName=true)
解决措施
出现该报错的原因是Hvigor运行时内存不足，在使用3.1.0及以上版本的Hvigor时，可通过以下方式修改Hvigor运行时内存的最大值。
勾选Enable the Daemon for tasks：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.17446428867885860121594133343157:50001231000000:2800:7550222871EC7B142E31D0A99954E0DB6F9CD7766D54AEF07C89DEAAC4EC8E68.png?needInitFileName=true?needInitFileName=true)
在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程的大小，适当将其增大（如设置为8192）：
Linux环境下编译报错“JS heap out of memory”
问题现象
在Linux环境下，系统内存有64G，Hvigorw脚本中配置--max-old-space-size=40960，在编译构建时，实际在使用内存未达到配置的内存（例如使用到20G左右）就出现报错“JS heap out of memory“。
问题原因
vm.max_map_count是一个与内核虚拟内存子系统相关的参数，用于控制进程可以拥有的内存映射区域的最大数量。它通常用于限制一个进程可以打开的文件数量，特别是在使用大量内存映射文件的情况下。
在Linux系统上，vm.max_map_count参数的默认值通常是较小的数值，例如65530。然而，对于一些需要大量内存映射的应用程序或者特定的使用场景，可能需要增加该参数的值，以便支持更多的内存映射区域。
解决措施
修改vm.max_map_count的值：
-  保存文件后，使用以下命令使更改生效：
编译报错“Cannot find module XXX or its corresponding type declarations”
-  问题现象 Stage模板工程编译引用native文件(.so) 提示 "Cannot find module XXX or its corresponding type declarations."。 处理措施 当前Stage工程在编译构建阶段新增对native文件(.so)导出符号的语法校验，如果引用了没有对应声明文件(.d.ts)的native文件(.so)的现有工程在编译构建阶段，语法校验工具便会报错提示找不到对应的声明文件。 如果出现类似问题，可尝试通过如下方式进行解决：
-
-
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.17283029492496031224562588365353:50001231000000:2800:468405F76A9B61BDF68A2CB38823891C4530B515241716C9F8D48C80D30D63B8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.67817218977150097863621725874264:50001231000000:2800:5ADC4F1B6361E0556B3E8AD2E9771DF223A809598E89BE8ABA865E9CD2FC8DFF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.91990359878960903009042270525244:50001231000000:2800:95450EF806524ECFED6A2B32C0907095FC280FF38370609E7BCD38D261CCED4D.png?needInitFileName=true?needInitFileName=true)
-  问题现象 引用三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。 处理措施 进入对应模块级oh-package.json5文件或工程级oh-package.json5文件中查看三方包是否已安装，若未安装，需执行ohpm install安装；若已安装，需查看“main”字段是否配置正确，若未配置或配置错误，需配置为正确的入口文件。
-  问题现象 引用的包路径被混淆，代码中又是在引用包后面拼接了路径，导致模块引用不到而报错。 例如： 代码中这样引用 这样引用会找不到模块，导致报错。 处理措施 修改引用方式，改为推荐的引用方式
-  问题现象 被引用模块oh_package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。 被引用模块的 oh_package.json5 中配置了错误的types字段。 该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。 处理措施 如果该包中没有d.ets声明，则这个字段可以删除。配置不存在或者错误，会导致报错。
-  问题现象 oh_package.json5 中 dependencies 中引入模块的 名称 和 实际使用时 import 的 不一致。 例如 在 oh_package.json5 中这样引入： 但是实际上在代码中import 的时候是 大写 HAR 或者其他而不是 dependencies 里面配置的 ‘har’ 的值，要注意保持完全一致。（目前windows 没有问题，linux会报错模块找不到） 处理措施 引入和使用改成一致。
-  问题现象 引用模块的 oh_package.json5 中 main 字段值和实际的文件名称大小写不一致。 处理措施 将main字段和实际文件名称的大小写改为一致。
-  问题现象 Stage模板工程编译构建失败，提示 "Cannot find module '@bundle:rollup_plugin_ignore_empty_module_placeholder' or its corresponding type declarations"。 解决措施 该问题是由于工程引用了无对应实现文件的.d.ts声明文件： 在输入栏中输入rollup_plugin_ignore_empty_module_placeholder，找到问题模块的中间文件。
```typescript
export type {T} from './type';
```
-  在输入栏中输入rollup_plugin_ignore_empty_module_placeholder，找到问题模块的中间文件。
-
```typescript
export type {T} from './type';
```
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.54196080651566421082881413962304:50001231000000:2800:22727735AFD692AA821D0DAAF8D644057660E1807020E8D28F278F1180E72610.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.26742518506906019282860482255229:50001231000000:2800:CA5211ADA172DEF03975F9EE8D3DA12AD61EEB5F8B480C6EB2B85526DC3D0862.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150654.85668130015808422865087364999275:50001231000000:2800:1ECFCE26D290B66C2EFCE0C2EBBADB3E767D81D48741265F2B1483777DDDB21A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.09989553772673513222012103746590:50001231000000:2800:BBFFD8E447F3EB6B4135781AFCDE97DBEC6B8EFBD2FDF223B1510AD055309209.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.41643922464407634430647833561254:50001231000000:2800:4B4B1BD23D73BF96E83E0CAA5D97B83DDF3390C5DE3378110D7F5B77F9293FC2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.75546738696194618404424249565084:50001231000000:2800:44F74D6CDA0C78725A1A4A2DFD5FF9F8E8AA7F3534F85F63A83F04662124D7A4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.37911922964323408642675756314464:50001231000000:2800:F8EE84ED5890335154C783524D66A7780EBEEFEBBE0B25FC68D2A261D6459485.png?needInitFileName=true?needInitFileName=true)
1.  在输入栏中输入rollup_plugin_ignore_empty_module_placeholder，找到问题模块的中间文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.75955944099720830465224439639286:50001231000000:2800:059F65C39FE1652BAD20C2E51068FF5686337B5B6435E5F9AA961FF41248EB8E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.76246635087397636197845055560927:50001231000000:2800:707711C27206144C949E99659B5B1E6054578175F95FD81441FF2D78B4B59E6C.png?needInitFileName=true?needInitFileName=true)
1.
```typescript
export type {T} from './type';
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.88272791683045798185155882101722:50001231000000:2800:51AC6A4DB85BB948BC838CB8C1DE26E80950DE9529428D90DE1E942B3F6A498B.png?needInitFileName=true?needInitFileName=true)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.75157331753683507132104615852098:50001231000000:2800:C765D70DFE46C9C9C87665C6538833767A17532D74ACB5626BC5CFB3583FEA1A.png?needInitFileName=true?needInitFileName=true)
编译报错“Module 'xxx' has no exported member 'yyy'”
问题现象
Stage模板工程编译构建失败，提示 "Module 'xxx' has no exported member 'yyy'" 并且"yyy"符号是由export * from 'x.js'语法从js文件中导出。
处理措施
当前Stage工程编译构建期的语法校验工具对js文件不作检查，因此当使用export * from 'x.js'导出js文件中的符号时，符号引用处便会提示"Module 'xxx' has no exported member 'yyy'"的错误信息。
如果出现类似问题，可尝试通过如下方式进行解决：
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.16323855852528378269526110652570:50001231000000:2800:BFF7BDBCB8C931F30E402515596B483EA75BCBF5F25D2CDA004835662DFE2F6D.png?needInitFileName=true?needInitFileName=true)
编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”
问题现象
Stage模板工程编译构建失败，提示 "ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded"。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.56466863681350176099097268078834:50001231000000:2800:A67B8E8871426E1BA2BB2CDF1731E633E195C94054043A2BC80ADA9C58C9DB2B.png?needInitFileName=true?needInitFileName=true)
处理措施
该问题是由于file1为当前工程外的代码：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.67853878715840941921333882389017:50001231000000:2800:FE639C0550FE3D8623E3013EDF4D40A9A3E0304606D692CFDCD652142DA7E5F8.png?needInitFileName=true?needInitFileName=true)
请新建Static Library模块，并将工程外的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。
编译报错“Failed to get a resolved OhmUrl by filepath xx”
-  问题现象 三方包在配置依赖时，配置到devDependencies，源码中又有引用依赖中的API时，编译失败。如以下示例：三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/grs的API时，编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.12463973194109838112716019492456:50001231000000:2800:575CC4A24B007EB05132E7EB2FF38985163CF5BDC009A7093196D8C5AD2C8438.png?needInitFileName=true?needInitFileName=true)
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.97321277191664035813898868810111:50001231000000:2800:9A734D164B723F34A00089B32D331A830460873D5E2E3F361D7257FC1BABB83A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.41016170340629787146015625394937:50001231000000:2800:4AC2082088F4037F625DA3DDF656ABCF22A2FAFD5C6F0A1475EDD2738A758C0B.png?needInitFileName=true?needInitFileName=true)
-  问题现象 DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。 问题确认 查看工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与真实路径不相同，是否存在大小写不一致问题。 处理措施 将工程目录下的build-profile.json5文件中modules字段配置的srcPath路径与真实路径保持一致。
-  问题现象 工程A以相对路径引用了工程B的模块，这种引用会导致报错。 处理措施
-  问题现象 DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor_ignore_xxxxx' imported by xxx”。 处理措施 如果hvigor_ignore_xxxxx所在的模块是一个har模块，需要排查oh_package.json5中是否存在"packageType": "InterfaceHar"，如果存在，请删除"packageType": "InterfaceHar"。
-  问题现象 DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for 'xxx' imported by 'yyy'”。 问题确认 处理措施
-
-  请确认当前使用的DevEco Studio和SDK版本是配套的，点击菜单栏Help > About DevEco Studio，Help > About HarmonyOS SDK分别查看配套的DevEco Studio和SDK版本。
-  问题现象： DevEco Studio编译失败，提示 "ERROR:  ArkTS:ERROR failed to execute es2abc ERROR:  ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx"。 处理措施 该问题是由于在工程中引用了非工程标准模块目录（即目录内无模块描述文件module.json5），如下图utils目录所示：请新建Static Library模块，并将utils/common里面的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.39617173861727852145655255396409:50001231000000:2800:96CE4BF61548B9D87DCF1FEC467AB7F1FF8888AA36A3D1BC5353AE8D578DAB19.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150655.82728382886043337648074508995990:50001231000000:2800:B3AF4AB7376FDBB4611533195DB09A84A7D03483B573D6497C04B504142F1CCE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.86543731269866886092787897612336:50001231000000:2800:FFDB89AD4F58334298EF00E015B5EA9288F0CEFD84CF10B643BD6C2806965C73.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.79337854842981383404001046819897:50001231000000:2800:A325F45898B7D2C6701D5EE6660DEBE1C8C8B2078432BFB884C8ED28ECA0D02D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.84244639966782065946145449983164:50001231000000:2800:4C712723A31DE683442A5EA1463A6178FADC098A93D23F965FE43AA7C107B8E6.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.24251703320637831092407311593164:50001231000000:2800:C6B053669F876D4A87C67A49CA1A88F353EFBA77C0718BA16F91B0A0FA3D7275.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.36708697059224395864096412758001:50001231000000:2800:162AAC4420C654FF1B8BAE183CEE3DFF24F9CFCA5ACDA4A7792499E9B74A45A9.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.73981350544615158578283099914799:50001231000000:2800:C15484A654B40DF984076807F6C2861C97D39380D599A6E9541B388DF5C8140F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.23485882070036949406604119051107:50001231000000:2800:36457EF3EF475738EFD81CB236BB9AB5D211AC05A1A911B42D99BC92A6FFB2C9.png?needInitFileName=true?needInitFileName=true)
编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”
问题现象1
使用了自定义参数BuildProfile，编译态无异常但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.46472884399603150576050592354545:50001231000000:2800:99CBC252A1AFDA170F5585684CC5E3A3574877448141697346CD65D55326E815.png?needInitFileName=true?needInitFileName=true)
处理措施
检查在当前模块下build-profile.json5中的targets > buildProfileFields配置的自定义参数中key值是否相同，如果不同请将targets内所有buildProfileFields中的key值保持相同。
以下为导致编译报错的错误配置示例：
请将targets内所有buildProfileFields中的key值修改一致，如以下示例：
问题现象2
使用了自定义参数BuildProfile并且编译器标红且构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.17697420113802075483581721198176:50001231000000:2800:1B2D5298C8D6D45BF3B98BFCBEC495171C45BC8094843F697C31D23A9BCBBA7F.png?needInitFileName=true?needInitFileName=true)
处理措施
请检查当前模块下build-profile.json5中buildProfileFields内是否添加了所使用的自定义参数，请确保该自定义参数已配置在buildProfileFields内。
C++工程编译导致电脑卡顿的处理建议
问题现象
在执行代码规模较大的C++工程的编译时，由于C++编译时的CPU占用率较高，可能出现电脑卡顿、反应迟缓等现象。
处理措施
如果出现类似问题，可尝试通过如下方式进行解决：
需要说明的是，修改了compile和link的值，可能会导致编译时长增加，请耐心等待。
CPP编译报错"A 'undefined symbol' error has occurred"
问题现象
在编译HarmonyOS C++ 项目时，报错提示"A 'undefined symbol' error has occurred"。
解决措施
"undefined symbol"错误通常表示链接器找不到特定符号的定义。这通常是因为源文件没有正确编译或链接，或者因为缺少必要的库文件。以下是如何定位和解决这个问题的步骤：
1. 确保所有源文件都已包含在 CMake 构建中。
首先，检查您的 CMakeLists.txt 文件，确保所有相关的源文件都已包含在项目中。
2. 确认源文件的符号定义。
确保在所有相关的源文件中正确定义了符号。例如，检查 myLibrary.cpp 是否包含 myFunction 的定义：
myLibrary.cpp
myLibrary.h
3. 检查编译和链接顺序。
确保所有源文件和库文件按照正确的顺序进行编译和链接。CMake 和 Ninja 通常会处理这个问题，但在手动编译时可能会出现问题。
4. 清理和重新生成构建文件。
有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：
或手动删除模块下.cxx目录。
5. 检查库路径和链接器标志。
如果使用三方库，确保 CMakeLists.txt 中正确配置了库路径和链接器标志。例如：
6. 启用详细编译和链接输出。
为了解详细的编译和链接过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：
7. 检查 Ninja 输出日志。
Ninja 默认生成 .ninja_log 文件，其中包含构建过程的详细信息。您可以检查这个日志文件以了解构建过程中的问题。
检查编译日志中是否存在符号所在的源文件或头文件。
8. 使用 nm 工具检查符号。
使用 nm 工具检查目标文件和库文件中的符号，确保符号定义存在。
可使用sdk中内置的nm工具：sdk/default/openharmony/native/llvm/bin/llvm-nm。
检查目标文件
检查三方库文件
结论
通过上述步骤，您可以定位和解决 error: undefined symbol 问题。在使用 CMake、Ninja 和 LLVM 编译 C++ 项目时，确保所有源文件和库文件正确包含在项目中，并正确配置编译和链接选项是关键。如果问题依旧存在，详细的编译和链接输出日志通常能提供更多线索，帮助您找到具体的原因。
CPP编译报错"A 'unknown type name' error has occurred"
问题现象
在编译HarmonyOS C++ 项目时，报错提示"A 'unknown type name' error has occurred"。
解决措施
在编译HarmonyOS C++ 项目时，遇到"unknown type name"错误通常表示编译器无法识别某个类型。这可能是因为类型未定义、未包含相关的头文件，或者包含的头文件路径不正确。以下是定位和解决这个问题的步骤：
1. 检查是否包含头文件。
确保所有必要的头文件都已正确包含在源文件中。例如，如果您正在使用某个自定义类型或库提供的类型，请确保在使用该类型的文件中包含了相关的头文件。
示例：
2. 检查头文件路径。
确保 CMakeLists.txt 中正确设置了头文件的搜索路径。可以通过 include_directories 添加头文件目录。
示例 CMakeLists.txt：
3. 清理和重新生成构建文件。
有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：
或手动删除模块下.cxx目录。
4. 启用详细编译输出。
为了解详细的编译过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：
5. 检查编译输出日志。
Ninja 默认生成 .ninja_log 文件，其中包含构建过程的详细信息。你可以检查这个日志文件以了解构建过程中的问题。
6. 使用 CMake 的 message 函数调试。
可以在 CMakeLists.txt 文件中添加 message 函数来打印一些调试信息，以确保路径和变量正确设置。
示例：
结论
通过上述步骤，您可以定位和解决 unknown type name 问题。在使用 CMake、Ninja 和 LLVM 编译 C++ 项目时，确保所有头文件正确包含并设置正确的头文件路径是关键。如果问题依旧存在，详细的编译输出日志通常能提供更多线索，帮助您找到具体的原因。
JDK版本不匹配导致编译失败
问题现象
通过命令行方式构建HarmonyOS应用或元服务过程中出现构建失败，现象如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.75516603291919733245861394086603:50001231000000:2800:AAD3FF8BF093E906F889D988E4DB0C3A782BD9CB357C6D798CB855459E453395.png?needInitFileName=true?needInitFileName=true)
解决措施
该问题是由于JDK版本不匹配导致，当前配套的版本为JDK 17。因此，请根据如下方法进行修正：
LABEL_VALUE_ERROR处理指导
问题现象
在工程同步、编译构建过程中，提示LABEL_VALUE_ERROR错误信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.96198820159708686998002027356540:50001231000000:2800:7F5EF0049CA77BC3D1F384DC2EAA8F5D4200F22E55BF8B2FA3A9506C0C672A1A.png?needInitFileName=true?needInitFileName=true)
解决措施
该问题是由于config.json文件的资源引用规则变更导致，需要将“label”字段的取值，修改为资源引用方式。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.24538549211413041202410660614802:50001231000000:2800:646592F182D10BBDCAE144B03774222567F81994C1F8F79C7B689CEB8C1B9BCE.png?needInitFileName=true?needInitFileName=true)
应用/元服务的启动界面信息缺失，提示"Schema validate failed"报错
问题现象
在工程同步或者编译构建时出现错误，提示“Schema validate failed”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.71423002454728283585964997150960:50001231000000:2800:0B950B1C1DFC4B967BBD5AF13349DB180EC256B37F72004BCC2FABB901D3ECBC.png?needInitFileName=true?needInitFileName=true)
解决措施
在开发应用/元服务时，可以设置应用/元服务的启动界面的图标及背景颜色，创建工程后自动设置了默认的启动界面信息，但若开发者误删其中某个字段后将导致报错。下面以重新设置启动界面信息为例，开发者可自定义启动界面的图标及背景颜色。
在开发应用/元服务时，为了提升应用/元服务冷启动的性能，您可以通过如下方式设置应用/元服务的启动界面的图标及背景颜色。
1.
2.  创建完成后，color.json文件如下图所示：
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.53778348800191048418731183759068:50001231000000:2800:04B958E5D1F2B892626DB3BE3B1A1C1A2A61FA2619E33BC752137F3F6FB6413E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150656.25690452332341808269424759628852:50001231000000:2800:3C9D722391EE0AF980D930130184E3331DB264B7C89C8530C6742F7121854209.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.49403530560394193923539279243472:50001231000000:2800:9E94838E920FD68B507E15D421CEB0D1E8FB87258E12A6FE46C4D06E80D155F8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.82267680773491528636564928872338:50001231000000:2800:C9D701716A2156DE1AB227EDFEEC8231E3ACC19B629F197A4C7E591868383B8A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.17634825265002972683075991285931:50001231000000:2800:ECFBE7CE0B2B647199DC6DAC859787F791E8C3835251F94FA9EAF29D6005CBD2.png?needInitFileName=true?needInitFileName=true)
编译报错“Schema validate failed”
问题现象
DevEco Studio编译时出现错误，提示“Schema validate failed”错误信息。
解决措施
出现该问题的原因是配置文件中字段缺失或拼写错误，可根据报错的详细信息进行问题定位。
如将module.json5文件中abilities标签中的“name”错写为“nam”，报错信息如下：
以上述报错为例，说明报错中关键词的含义，便于开发者理解报错信息，完成问题定位及修改。
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.25118239626780501855557968134569:50001231000000:2800:B294E589351BB6CC472A5A10BB911FAC3FC2857ABA82B64C5A8DF442F4432B13.png?needInitFileName=true?needInitFileName=true)
编译报错“No available entry module found”
问题现象
DevEco Studio编译时出现错误，提示“No available entry module found”错误信息。
解决措施
feature模块中需要配置依赖的entry模块，DevEco Studio在编译时会校验feature模块所依赖的entry模块是否存在，出现该问题的原因可能为以下情况：
编译报错“keystore password was incorrect”
问题现象
DevEco Studio编译时出现错误，提示“ERROR - hap-sign-tool: error: ACCESS_ERROR, code: 109. Details: Init keystore failed: keystore password was incorrect”错误信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.40744159938823364412557503746930:50001231000000:2800:653FED952ED1AC578327E09DD50BE94DCEC2DF1C0297D842DB047FAE8C374790.png?needInitFileName=true?needInitFileName=true)
报错原因
密钥库(p12)密码错误。
密钥库密码和密钥密码是在创建p12文件时由开发者自行输入的，请牢记该密码。DevEco Studio工程的build-profile.json5文件中有记录密码的密文，但签名工具需要输入密码明文，不能直接将build-profile.json5中的值用到签名工具中。
常见场景
解决措施
出现该问题的原因是签名文件中签名密码错误。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.63240997660589816586261464694832:50001231000000:2800:AEC84D8965BEC008046024EC1C937D407131B7EA75AC268CABA840A674556CE5.png?needInitFileName=true?needInitFileName=true)
开发者可通过重新自动签名解决该问题：
1. 点击File > Project Structure > Project > Signing Configs，打开签名配置页面。
2. 勾选“Automatically generate signing”（如果是HarmonyOS工程，需同时勾选“Support HarmonyOS”），等待重新签名，然后点击OK即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.00837284591497757327748356160701:50001231000000:2800:E6C44C21B46D5F5357BFA4B5A1C81DC8110C50C97F03B6DC3F8F501FB8BDF5C9.png?needInitFileName=true?needInitFileName=true)
编译报错“please check deviceType or distroFilter of the module”
问题现象
DevEco Studio编译时出现错误，出现如下提示之一：
-
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.16449569744340797974212314564001:50001231000000:2800:65BA0E08399D70B1A77854FB88883BF15492BDB15B9FA6B960BA31FE823EC736.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.04019134169071278334886643376374:50001231000000:2800:24F101722145FF3121503CBEB061C0B0CB4DBF4E4802D3CC889279586C066ACF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.82028058250062701669610101782365:50001231000000:2800:8CDF2BA78A072B0D1637DA4BCA9A61873143F6E971C87775365580670F17CB83.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.33222779235972730859998730968834:50001231000000:2800:7F792D96CD017824BACC5E5A049DFD5F1E68EDAF30D72613A2F47BE43FD09AD3.png?needInitFileName=true?needInitFileName=true)
解决措施
出现该问题的原因是打包时工程未满足HAP唯一性校验逻辑，请根据HAP唯一性校验逻辑修改工程，满足校验逻辑即可正常打包。
编译报错“Failed to generate test project build system”
问题现象
执行多模块native模块构建时，提示“Failed to generate test project build system.”错误信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.09536091901427136014413552918248:50001231000000:2800:5BEA139E7CA55E82157B16B93A722E72035E580CA9B163C8E85F4200899B9E96.png?needInitFileName=true?needInitFileName=true)
解决措施
请删除报错模块下的.cxx文件夹，然后选中需要构建的模块，执行Make Module${moduleName}完成单独构建，避免同时构建多个模块。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150657.04662346528604805431930646418351:50001231000000:2800:96C32464772BC981AFE5791057C6D7B12EBCD826A721B16C22FF9656693349D9.png?needInitFileName=true?needInitFileName=true)
C/C++项目三方依赖库未打包入HAP
问题现象
C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中。
解决措施
当前DevEco Studio对C/C++项目三方so的寻址方式有限，如出现三方so未打包到HAP中，请尝试修改so引入方式。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.80074898179564745854241162679446:50001231000000:2800:6FDA91E278729FAC741936640B42BC4BCF32112C6D14F4A8BA9C71237D1E14AF.png?needInitFileName=true?needInitFileName=true)
Static Library模块中src/main/cpp目录下的文件未打包进HAR
问题现象
点击Build > Make Module ${libraryName}编译构建生成HAR后，发现构建产物中未出现cpp目录下的文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.24325256543155768170375705399032:50001231000000:2800:1328E4A793930D62EA9CB40388C4EA10CA5462856F224A0B29F5C54A47492893.png?needInitFileName=true?needInitFileName=true)
解决措施
如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，只会将dependencies内处于本模块路径下的本地依赖也打包进.har文件中，devDependencies里的依赖不会打包进.har文件中。
请将相应的本地依赖移至dependencies中后重新编译。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.65854945364336122978270658847409:50001231000000:2800:F9D5072F6FD11093C0DCB0F148190EA9E99A85C5DE6B0DCAD4BE73551F72D94A.png?needInitFileName=true?needInitFileName=true)
工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”
问题现象
工程构建时，提示“ArkTS:WARN: For details about ArkTS syntax errors, see FAQs”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.24710114179039322343021405023548:50001231000000:2800:05CD4BD38C350B31198E673A3210075E05D6E4C7EC20AF8894B774EDAA4BE653.png?needInitFileName=true?needInitFileName=true)
解决措施
出现该告警说明当前工程存在不符合ArkTS语法规范的写法，请根据ERROR报错中括号内的语法规则如(arkts-no-var)，查看从TypeScript到ArkTS的适配规则中对应的说明，修改为ArkTS规范写法。
编译报错“ninja: error: mkdir(xxx): No such file or directory”
问题现象
Native工程编译报错，同时出现以下告警和报错信息。
出现工程目录长度超过250字符的告警，示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.29344028717859240823946311160251:50001231000000:2800:2BD1DB3714FCE189B838813252350DFEFEB22C41372A47827DAA80A4781809EF.png?needInitFileName=true?needInitFileName=true)
出现编译报错“ninja: error: mkdir(xxx): No such file or directory”，示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.05896212148083791255153997799225:50001231000000:2800:3FAE852B798AEB8C9CB1D8DCEEF9B89321AB3EB8D5EA1AE896DD0AA1C12141AB.png?needInitFileName=true?needInitFileName=true)
解决措施
CMAKE_OBJECT_PATH_MAX默认大小为250，如果工程中object file实际路径长度超出该大小，将导致编译报错。
开发者需要根据object file实际路径长度在工程CMakeLists.txt中设置CMAKE_OBJECT_PATH_MAX大小，具体方法如下：
-  示例中告警文件为TextMeasureCache.cpp.obj，长度为24字符，在默认值250的基础上增加24，即设置set(CMAKE_OBJECT_PATH_MAX 274)
-  计算公式：CMAKE_OBJECT_PATH_MAX = 总路径长度 - object file中目录部分长度 + cmake哈希值字符数（固定为32） 代入示例中的长度后，计算可得：CMAKE_OBJECT_PATH_MAX = 297 - 74 + 32 = 255，即设置set(CMAKE_OBJECT_PATH_MAX 255)
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.97406096081451190594636379811875:50001231000000:2800:1BA5702A415F95552908098D012FF881E091838216FB71D55A5420FD0D3AE52A.png?needInitFileName=true?needInitFileName=true)
编译报错“(is the command line too long?)”
问题现象
Native工程编译报错，同时出现以下告警和报错信息。
出现工程目录长度超过250字符的告警，示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.31827016755639728751311505972731:50001231000000:2800:4E278E57A622C59257D364AFA3339F3E3EF5996216780259C9B9004575C15EE6.png?needInitFileName=true?needInitFileName=true)
出现编译报错“(is the command line too long?)”，示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.73806573218357488873339576546175:50001231000000:2800:073D64DEE034B262BEDC407E2BBC741F4C0E57925D487A1130786EAAD6882397.png?needInitFileName=true?needInitFileName=true)
解决措施
CMAKE_OBJECT_PATH_MAX默认大小为250，如果工程中object file实际路径长度超出该大小，将导致编译报错。
开发者需要根据object file实际路径长度在工程CMakeLists.txt中设置CMAKE_OBJECT_PATH_MAX大小，具体方法如下：
-  示例中告警文件为TextMeasureCache.cpp.obj，长度为24字符，在默认值250的基础上增加24，即设置set(CMAKE_OBJECT_PATH_MAX 274)
-  计算公式：CMAKE_OBJECT_PATH_MAX = 总路径长度 - object file中目录部分长度 + cmake哈希值字符数（固定为32） 代入示例中的长度后，计算可得：CMAKE_OBJECT_PATH_MAX = 297 - 74 + 32 = 255，即设置set(CMAKE_OBJECT_PATH_MAX 255)
-
-  设置CMAKE_OBJECT_PATH_MAX后，cmake会将长路径转换为32字符的哈希值以缩短路径长度，如果转换后的路径依然过长，只能缩短工程的存放路径。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.23944688751930067559836844886819:50001231000000:2800:84F6F28B899ADAAF95A8095B39E73844C8B3AFB577F671F38AC48979E0889ED6.png?needInitFileName=true?needInitFileName=true)
编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”
问题现象
Native工程中使用find_path时出现以下报错信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.69066657438546182714752591106938:50001231000000:2800:88BA18E82998BCF433E5B0BF38E5FD3FB678F1784D8D370DD977EFC3E09B7203.png?needInitFileName=true?needInitFileName=true)
解决措施
OpenHarmony SDK提供的CMake交叉编译配置文件（ohos.toolchain.cmake）中，限制了搜索路径为CMAKE_SYSROOT。
如果开发者需要添加搜索路径，可在CMakeList.txt中使用list接口添加自定义路径，如将"D:demo"添加至搜索路径：
添加后，即可使用find_path查找"D:demo"目录下的文件。
编译报错 “Unknown resource name”
问题现象
工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.98903974079188591517012901532291:50001231000000:2800:6CD0E2E30861A54A38D7C29CB7545347810A1DBDD9C7457B37C563735219D21A.png?needInitFileName=true?needInitFileName=true)
解决措施
请确保符合以下条件：
问题现象
引用模块的方式不对，如果引用的是一个其他模块的代码，也会报资源找不到。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.79074789130755656228667186317613:50001231000000:2800:CFED6B9A9018035F41046731C52E943F87C66EE29ADFC5F34EFA2EB0A814AEC4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150658.84005993494318786763987300198932:50001231000000:2800:7CD4E58689CF616115932F52917FACD9A4346A9A7FDB909B7E8BD546F319F2F8.png?needInitFileName=true?needInitFileName=true)
解决措施
在oh_package.json5中引入该模块。通过定义的模块名称来引用。
如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.81136048517816365063918618843492:50001231000000:2800:C8FA8C2AD943495DA8E9B59282F767154E15679F24D25B5595EF0585631AB799.png?needInitFileName=true?needInitFileName=true)
问题现象
HSP A 申请了某个权限，这个权限进行了资源的引用，在所有依赖A的组件进行构建时，报错 A 引用的资源找不到。
解决措施
手动在引用方配置对应资源可以解决此问题。
构建报错“ERROR: Task xxx was not found in the project xxx”
问题现象
命令行手动执行构建命令时，构建失败，提示“ERROR: Task xxx was not found in the project xxx”
问题确认
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.73217520565519413901340107730533:50001231000000:2800:44C960662EFE94442E0FB91B2564F3BEA1A13E65E8BCCEDB7B962A7097C443CA.png?needInitFileName=true?needInitFileName=true)
解决措施
编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”
问题现象
DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user_grant permissions”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.85364576921555086778232619655502:50001231000000:2800:B3FF1576FC836A113978465C13A5BC0C4E8E19B0CC08B7423E6EFC201B677940.png?needInitFileName=true?needInitFileName=true)
问题原因
从DevEco Studio NEXT Developer Preview2版本开始新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定(可以缺省为空，若非空则name必填,user_grant权限则必填reason、usedScene字段)。
解决措施
进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：
编译报错“Only one default card can be configured in the form_config.json file”
问题现象
DevEco Studio编译失败，提示“Only one default card can be configured in the form_config.json file”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.27648049744682313834401397443148:50001231000000:2800:A247138E98963308AF575B7CB99958989DAF3135C93032864252FE38E91E546B.png?needInitFileName=true?needInitFileName=true)
问题原因
从DevEco Studio NEXT Developer Preview2版本开始新增规则：卡片的配置文件中isDefault不可缺省，每个UIAbility有且只有一个默认卡片。
解决措施
进入对应module.json5文件中，选择唯一默认卡片，将其他卡片的isDefault字段设置为false。
编译报错“In the form_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”
问题现象
DevEco Studio编译失败，提示“In the form_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty.”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.21312868225096304918260498810877:50001231000000:2800:54F55C183F0AC9CF52542DB9ECCDDFE795AE9D3A22F9F9B65656B36C1E2834CB.png?needInitFileName=true?needInitFileName=true)
问题原因
从DevEco Studio NEXT Developer Preview2版本开始新增规则：卡片的配置文件中updateEnabled不可缺省，为true时可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，当两者同时配置时，定时刷新优先生效。
解决措施
进入对应module.json5文件中，按照需求，选择配置updateEnabled为false，或者增加定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式配置。
编译报错“The path XX is not writable. please choose a new location”
问题现象
在mac上，通过直接打开dmg中的DevEco Studio，构建报错 The path XX is not writable. please choose a new location.”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.87425745655108724939148811951055:50001231000000:2800:B0AE7929DF71BF1EB1FAEEB0E0D513644C66FC23AC881C714B3B7EC84095B7A1.png?needInitFileName=true?needInitFileName=true)
问题原因
在mac上直接打开dmg 中的DevEco Studio，是会以只读的方式打开的，内置到DevEco Studio里面的文件是没有写权限的。
解决措施
将“DevEco-Studio.app”拖拽到“Applications”中，先安装再使用。
编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”
问题现象
本地HSP模块对外提供的接口中使用了HAP未定义的自定义参数BuildProfileFileds，且HAP引用了HSP中的该接口，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.44500201678613221034289272844582:50001231000000:2800:9B6B6BED514D2A49BF874D2B62A47BBD360B08D8C05E334EA7B65FF9BB090138.png?needInitFileName=true?needInitFileName=true)
解决措施
可采用以下两种方式解决该问题：
编译报错“The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match”
问题现象
编译报错“The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match”。
解决措施
useNormalizedOHMUrl为true的时候ohmurl使用的是新的拼接和解析方式，不能和旧的ohmurl混用，会导致运行时无法识别。
可采用以下两种方式解决该问题：
如果修改了useNormalizedOHMUrl仍无法解决，表明当前hsp包是本地包，需要以本地hsp包的形式引入，请在工程下的build-profile.json5中的modules中添加报错hsp模块，示例如下：
如何配置oh-package.json5动态依赖
oh-package.json5文件中：
示例如下，详细内容可参考oh-package.json5文件和添加依赖项。
如何解决SDK与镜像不匹配导致abc文件无法正常运行的问题
问题现象
当SDK版本与镜像版本不匹配时，应用将会闪退，出现jscrash，同时hilog出现日志。
解决措施
现象根本原因是SDK工具与镜像版本不匹配。推荐使用匹配的SDK与镜像版本。
查看SDK版本方法：
在DevEco Studio安装路径下的sdk路径中，执行 {sdk.dir}/openharmony/ets/build-tools/ets-loader/bin/ark/build-win/bin/es2abc.exe --bc-version可查看SDK版本号。用于检验SDK与镜像版本是否匹配。
如何解决编译报错“Could not resolve 'xxx' from”，但'xxx'目录存在的问题
问题现象
编译报错：“Could not resolve 'xxx' from”，但'xxx'目录存在，目录下存在Index文件。
问题原因
在引用目录时，编译时自动拼接小写的index文件，而目录中是大写的Index文件，在编译大小写敏感时，找不到index文件，则报错。
解决措施
在引用'xxx'目录时，明确写明引用到'xxx/Index'文件。
用户目录下没有npmrc文件
问题现象
新建项目报错 Error: The hvigor depends on the npmrc file. Configure the npmrc file first。
问题原因
在用户目录下没有 .npmrc 文件。
解决措施
在用户目录下创建.npmrc文件，配置如下信息：
如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题
问题现象
编译报错“ Error: 'icon' value `$media:icons` invalid value”。
报错原因
引用的资源不存在时，编译报错指向的文件路径是build目录。
常见场景
解决方案
根据报错的资源id全局搜索，查看报错的资源是否存在。
如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题
问题现象
编译报错“Error: cJSON_Parse failed, please check the JSON file”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.82457108357925769433700779518940:50001231000000:2800:BC13C5A2FA8764684E0C12496870AEF898185B5F314001080720296F3624B066.png?needInitFileName=true?needInitFileName=true)
报错原因
module.json文件格式不正确。
常见场景
1. json文件内末尾多了逗号。
2. 根标签不是大括号{}。
解决方案
检查报错指向的json文件格式，比如是否末尾多了逗号，根标签是否为大括号{}。
如何解决编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9_].”的问题
问题现象
编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9_]”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.23882113720904350027736688793349:50001231000000:2800:F9E2100B9C1DE731C7266881510F03F0DB6F96ABA20222F4728E23C94D7D323F.png?needInitFileName=true?needInitFileName=true)
解决方案
检查文件名是否合法，文件名只能包含大小写字母、数字、下划线。
如何解决三方包require语句报错
问题现象
当引入三方包时编译报错。
报错原因
部分三方包由npm迁移而来，其开发环境为node， 其中的require语法arkcompiler不完全支持，出现运行报错情况。
场景1：
需修改为：
场景2：
需修改为：
场景3：
编译出现warning信息：
解决方案
修改rollup 配置文件，rollup.config.js中修改 preferBuiltins 字段：
场景4：
需修改为：
如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题
问题现象
动态调用类或者接口的字段，导致编译报错出现：Indexed access is not supported for fields(arkts-no-props-by-index)。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.63364700615823372610851426418936:50001231000000:2800:293660EF4E1F2527DA6A866E7A1566F2E95C67853286C2B7E2D22A4DBB4BD2DD.png?needInitFileName=true?needInitFileName=true)
解决方案
修改代码：
如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
问题现象
在不同的文件中声明相同变量或者interface、enum等类型，DevEco Studio不报错，但是编译报错。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.16384167125808599872161969592097:50001231000000:2800:ED1E87060F7CEDDE423D424681A16E0E90443496C2AD68B467CA7C577624A850.png?needInitFileName=true?needInitFileName=true)
解决方案
如果文件中不包含export关键字，该文件将视作全局命名空间的一部分，相当于两个文件实质为同一个文件。请添加export关键字使其成为独立命名空间，或者将声明的内容添加到自定义的命名空间中。
如何解决编译报错“ The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary.”的问题
问题现象
编译报错"The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary"。
问题原因
HSP会生成.d.ts声明文件，由于原始文件中未注明类型，导致生成的.d.ts文件缺少类型注解。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.49240878999527317728958685399420:50001231000000:2800:CC7CB04568334EE769C7B9892E31B005119F508B067715B017FBED376E031B1E.png?needInitFileName=true?needInitFileName=true)
解决方案
报错位置添加类型注解。
如何解决编译报错"arkts-no-any-unknown" 和 "Cannot find module 'xx' or its corresponding type declarations"的问题
问题现象
编译报错"arkts-no-any-unknown" 和 "Cannot find module 'xx' or its corresponding type declarations"。
问题原因
大小写敏感导致模块找不到。常见于图片中的两种错误同时出现，且仅在Linux系统出现，win/mac不报错。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.89616713689822916079790810957455:50001231000000:2800:C74A29C1C1882332FA545E8872F46F9F522B87CB9FABBD8CD8740E4040022D36.png?needInitFileName=true?needInitFileName=true)
解决方案
解决引用中的大小写问题。
如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”的问题
问题现象
编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”。
问题原因
由于获取SDK的方式是从网络上下载，mac的安全设置会给可执行文件添加来源于网络的标识（com.apple.quarantine），导致无法执行。
解决方案
执行命令删除可执行文件的com.apple.quarantine标识。
如何解决编译报错“Cannot add xxxx items to index”的问题
问题现象
编译报错“Cannot add xxxx items to index”。
问题原因
被编译文件中某函数内部有大量object literal, array iteral和string，导致item的数量超过了上限（65536）。
解决方案
排查相关文件，将存在上述原因的函数进行拆分。
编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
问题现象
在升级DevEco Studio至5.0.3.403版本后，打开旧工程概率性报错：resource busy or locked, open 'xxx\outputs\build-logs\build.log'。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.41500597168132094406723911002668:50001231000000:2800:9F35CCC498C193B2D3528785C81DB6ADF5FD1BF8CF32C1F38D1724DBFA4D76C2.png?needInitFileName=true?needInitFileName=true)
问题原因
初始化时日志写入存在冲突，.hvigor目录中的build-log文件被占用导致了该报错。
解决方案
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150659.62908678590454838231044885251284:50001231000000:2800:5D72E773652CCC0FC0D2240A8C0D3637AEF67EB51C952D767199CF9518563084.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.80240874377348669583592757146490:50001231000000:2800:6375CC025CA2A484DF9936569FE08FF3A9C79BD72022A94CFDA26A3704A9F640.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.71646274277797061222227792813241:50001231000000:2800:916B24E9530A38B5EF02CC89E910AADAF40EBD4773FFBCA23FBDFCC3D22B51AF.png?needInitFileName=true?needInitFileName=true)
Mac环境下加载动态库，签名拦截导致未生效
问题现象
Mac环境下，在DevEco项目开发时，build-profile.json中添加了如下的插桩配置，但是插桩功能未生效。
```json
"transformLib": "<相对模块根路径的动态库路径，以./开头>"
```
判断与验证
解决方案
执行下列命令，将es2abc文件的签名替换成和动态库文件一样的用户签名。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-signing-V14
爬取时间: 2025-04-30 08:00:04
来源: Huawei Developer
针对应用/元服务的签名，DevEco Studio为开发者提供了自动签名方案，帮助开发者高效进行调试。也可选择手动签名对应用/元服务进行签名。
自动签名
使用自动签名前，请确保本地系统时间与北京时间（UTC/GMT +8.00）保持一致。如果不一致，将导致签名失败。
操作步骤
1.
2.  签名完成后，如下图所示，并在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b），数字证书在AppGallery Connect网站的“证书、APP ID和Profile”页签中可以查看。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.15380861216856391949077178569776:50001231000000:2800:8186A5C11A7BEB1B4590740B97027AD4AECB2B0AD021907576E2E243DCB783EE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.26690919960274580227384762782921:50001231000000:2800:50F606A8A760AA90179A8A824BAC0EC0F54A5D94B0B4A88E239DDA4A7396BED8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.52708319525820070665139228819801:50001231000000:2800:0928F2DCE5217259699A5661DF55CB1A710843E015E0E3B01AC9C5069F6AF806.png?needInitFileName=true?needInitFileName=true)
支持ACL权限
从DevEco Studio 4.0 Release版本起，若您的应用需要使用受限开放权限，可以在调测阶段通过自动签名快速申请。
当前支持通过自动签名申请需要ACL权限的清单如表1所示。
| API版本  | 支持的ACL权限  |
| --- | --- |
| API Version ＝ 10  | ohos.permission.READ_CONTACTSohos.permission.WRITE_CONTACTSohos.permission.READ_AUDIOohos.permission.WRITE_AUDIOohos.permission.READ_IMAGEVIDEOohos.permission.WRITE_IMAGEVIDEOohos.permission.SYSTEM_FLOAT_WINDOW  |
| API Version = 11  | ohos.permission.READ_CONTACTSohos.permission.WRITE_CONTACTSohos.permission.READ_AUDIOohos.permission.WRITE_AUDIOohos.permission.READ_IMAGEVIDEOohos.permission.WRITE_IMAGEVIDEOohos.permission.SYSTEM_FLOAT_WINDOWohos.permission.READ_PASTEBOARDohos.permission.ACCESS_DDK_USBohos.permission.ACCESS_DDK_HIDohos.permission.FILE_ACCESS_PERSIST  |
| API Version ≥ 12  | ohos.permission.READ_CONTACTSohos.permission.WRITE_CONTACTSohos.permission.READ_AUDIOohos.permission.WRITE_AUDIOohos.permission.READ_IMAGEVIDEOohos.permission.WRITE_IMAGEVIDEOohos.permission.SYSTEM_FLOAT_WINDOWohos.permission.READ_PASTEBOARDohos.permission.ACCESS_DDK_USBohos.permission.ACCESS_DDK_HIDohos.permission.FILE_ACCESS_PERSIST ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEOohos.permission.INPUT_MONITORINGohos.permission.INTERCEPT_INPUT_EVENT  |
API版本
支持的ACL权限
API Version ＝ 10
API Version = 11
API Version ≥ 12
执行操作步骤后，DevEco Studio将校验当前配置的ACL权限是否在上述列表内，然后通过应用市场（AGC）申请对应的Profile文件，用于签名打包，从而避免繁琐的手动签名步骤。
如果使用的DevEco Studio版本低于4.0 Release，在开发过程中使用了需要ACL的权限，则仍需要采用手动签名。
手动签名
HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请数字证书和Profile文件前，首先需要通过DevEco Studio来生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。然后，申请调试数字证书和调试Profile文件。最后，将密钥（.p12）文件、数字证书（.cer）文件和Profile（.p7b）文件配置到工程中。
生成密钥和证书请求文件
1.  如果本地已有对应的密钥，无需新生成密钥，可以在Generate Key界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2.
3.
4.
5.
6.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.07968327350080012446213033219125:50001231000000:2800:06B61AB41C0ED03BDA14E2CA2AFC2DCA66BC36C3DA28C20F8D00AC12544425B8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.58988124153359842493722326136924:50001231000000:2800:B6C5D5DAC47680DBA439A1F0D9011D170D94C7CF706DEE07A6049192F98CEB1B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.62485516723879675391679468473182:50001231000000:2800:88C848A9BAFEAA090339659E511B9F328691962B3146FDD15ED8C722A2FBD97E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.65973539810811028405948235130932:50001231000000:2800:DDE3583B9A7F71F777950B951466EFAE748AA10BE70C4B1134F88FC5B17C58A4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150700.19891078911248986597260170765002:50001231000000:2800:72E5C1D8FFD5E6B0D08A36829BD930AFB9914E7EFC61FBD40067AE05E5E55204.png?needInitFileName=true?needInitFileName=true)
申请调试证书和调试Profile文件
手动配置签名信息
在DevEco Studio中配置密钥（.p12）文件、申请的调试证书（.cer）文件和调试Profile（.p7b）文件。
Store file，Profile file，Certpath file三个字段支持配置相对路径，以项目根目录为起点，配置文件所在位置的路径名称。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.26728775016696679975314131384731:50001231000000:2800:2CC6B2A20E022A522099D28F26A963B65C61DCA453B4F1BE9A28004FBA4DF8F1.png?needInitFileName=true?needInitFileName=true)
配置完成后，进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.45177830948336273531803449660907:50001231000000:2800:9434959F3930F0BD2C9FFA363B5CB8A6309B19E3D4F218C31F022381522B1B5A.png?needInitFileName=true?needInitFileName=true)
使用ACL的签名配置指导
如果应用需要使用受限权限，请先审视是否符合受限开放权限的使用场景，并根据以下流程申请。
1.  请将APP ID、申请使用的受限开放权限、使用该权限的场景和功能信息，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放权限使用的名单，审核周期一个工作日，请耐心等待。
2.
3.  在“Signing”下分别配置密钥(.p12文件)、Profile(.p7b文件)和数字证书(.cer文件)的路径等信息。 勾选“Show restricted permissions”，即可看到配置成功的权限。 配置完毕后，点击“Apply”。
4.
5.  在“Signing”下分别配置密钥(.p12文件)、Profile(.p7b文件)和数字证书(.cer文件)的路径等信息。 勾选“Show restricted permissions”，即可看到配置成功的权限。 配置完毕后，点击“Apply”。
6.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.43103363920312656547706395265092:50001231000000:2800:9204DA1CA71C6AEF843F7C91F71502077193ADF92DEED490B178B3A5350F3288.png?needInitFileName=true?needInitFileName=true)
1.
2.  在“Signing”下分别配置密钥(.p12文件)、Profile(.p7b文件)和数字证书(.cer文件)的路径等信息。 勾选“Show restricted permissions”，即可看到配置成功的权限。 配置完毕后，点击“Apply”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.96913849745213220037724003713993:50001231000000:2800:C0CDE9FEE59018E97FCFAF45422B58A72C3D81DACC121AD326B1DFE9841BD1BF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.28497115573532675810238202924826:50001231000000:2800:6F4D51D1A1134DF8FFC7A34F8F6D3CC569AD15A87A1E5ECA6A237E1508B1FA27.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.02711604926523856375532127413517:50001231000000:2800:B2F779505BF5FCEF60821E2CED3B4752EF86032329908528A305DD7AD5BB73FE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.20042766457855895673775165325863:50001231000000:2800:FB43667CBC5A852D14EE4C7676A613A5F2913A73E2B591F30C11CF90F97A2F58.png?needInitFileName=true?needInitFileName=true)
常见问题
元服务签名时，提示"Invalid AppId in the bundle name."
问题原因
元服务的包名采用固定前缀和APP ID组合方式（com.atomicservice.[appid]）命名。开发者需先在AppGallery Connect中新建元服务并获取其包名，并将包名填写至工程的bundleName字段中。若上传的元服务包的包名和AGC中的包名不一致，则会导致元服务上架失败。
不合法包名包括：
解决措施
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.18056644843117110786466231661936:50001231000000:2800:1969E13DBBA0453B77C12ED04CCA0BD2AAB1E821B9779F2075629A8CCFFE13DB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150701.71436236176161828720525463344247:50001231000000:2800:1B12E3C5FC7E2C6B932CF13D2D7BE6B59CA0607E41197A4BC24402F1EE34CA25.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-running-app-V14
爬取时间: 2025-04-30 08:00:39
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-run-device-V14
爬取时间: 2025-04-30 08:01:14
来源: Huawei Developer
在Phone和Tablet中运行HarmonyOS应用/元服务的操作方法一致，可以采用USB连接方式或者无线调试的连接方式。
前提条件
使用USB连接方式
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.20676512834344800187915344819887:50001231000000:2800:F9F0FA97D816DD3FF8E3F6DE1B7F29FC5F337E384E7FCAF51465135B6EEE3E12.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.07638153246295306680401287118192:50001231000000:2800:93CEB0FEAA381856346184E9EC89847E5639034F57EED7C914AD07FBF4861120.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.71224770077895561895060255741043:50001231000000:2800:77D6C4EBECEC215C8CD75B2FC6C43907F1E9625AEE6E97083990758DC6F0E69F.png)
设备连接后，如果DevEco Studio无法识别到设备，显示“No device”，请参考设备连接后，无法识别设备的处理指导。
使用无线调试连接方式
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.10468384535586059468292879938227:50001231000000:2800:03BAF2BCE0D4265448F0770802CECECCC42EC7BAA5E388ECFD022A46F1871987.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.45817135922514779986995354157549:50001231000000:2800:9DF223CA6EB259EBE2D2B791A01BBAAD9FF7785722F01DF41B283D322A7A0D30.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.42681639315244053534816751661738:50001231000000:2800:9925EB213A3591486646C3C6EBC72B016BBCBB00B15A8BB103F6F640C1E6D3E6.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-run-emulator-V14
爬取时间: 2025-04-30 08:01:49
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-overview-V14
爬取时间: 2025-04-30 08:02:24
来源: Huawei Developer
DevEco Studio提供了模拟器（Emulator），为开发者提供了运行和调试HarmonyOS应用/元服务的便捷途径。模拟器还原了真实设备的基本功能，如屏幕旋转、音量调节、模拟的硬件传感器和指定设备的位置等。这使得您无需拥有不同类型的物理设备，就可以在各种虚拟环境中轻松测试您的应用程序。在某些情况下，在模拟器上进行应用测试，相比于在实际物理设备上的测试，有着更快速、更高效的体验。例如，模拟器提供了摇一摇的操作模拟，让您能够轻松触发摇一摇功能。总的来说，无论是快速原型验证还是功能测试，模拟器都是满足您测试需求的最佳选择。通过DevEco Studio提供的模拟器，您可以更灵活、更高效地进行应用开发和调试，提升您的开发体验与效率。
当前模拟器在不同系统上支持的设备类型见下表。
| 系统类型  | 设备类型  |
| --- | --- |
| Windows(X86)  | 手机（包括折叠屏）、平板  |
| macOS(ARM)  | 手机（包括折叠屏）、平板  |
系统类型
设备类型
Windows(X86)
手机（包括折叠屏）、平板
macOS(ARM)
手机（包括折叠屏）、平板
模拟器主要用于开发和调试HarmonyOS应用，为保护您的个人数据，请勿将模拟器用作其他用途。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-requirements-V14
爬取时间: 2025-04-30 08:02:58
来源: Huawei Developer
模拟器在本地计算机上创建和运行，在运行和调试应用/元服务时可以保持良好的流畅性和稳定性，但是需要耗费一定的计算机资源，具体的运行环境要求为：
| 系统类型  | 运行环境要求  |
| --- | --- |
| Windows(X86)  | Windows 10 企业版、专业版或教育版及以上，且操作系统版本不低于10.0.18363。具有二级地址转换 (SLAT) 的 64 位处理器。CPU支持AES指令集。CPU 支持 VM 监视器模式扩展（Intel CPU 的 VT-c 技术）。系统内存16GB及以上。不支持在虚拟机系统中运行模拟器。系统OpenGL版本4.1及以上。屏幕分辨率1280*800像素以上。  |
| macOS(ARM)  | macOS系统为12.5及以上版本。系统内存8GB及以上。不支持在虚拟机系统中运行模拟器。系统OpenGL版本4.1及以上。屏幕分辨率1280*800像素以上。  |
系统类型
运行环境要求
Windows(X86)
macOS(ARM)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-specification-V14
爬取时间: 2025-04-30 08:03:33
来源: Huawei Developer
与真机相比，模拟器暂时只支持部分Kit，以下是模拟器对各种Kit的支持情况。
使用x86模拟器时，C++工程及三方库需要编译出x86_64版本的so，请在build-profile.json5中externalNativeOptions/abiFilters的值中增加"x86_64"，具体编译配置请参见externalNativeOptions。
应用框架
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Ability Kit  | 部分支持  | 部分支持  | 不支持拉起文件处理类应用  |
| Accessibility Kit  | 是  | 是  | -  |
| ArkData  | 部分支持  | 部分支持  | 不支持分布式能力  |
| ArkTS  | 是  | 是  | -  |
| ArkUI  | 部分支持  | 部分支持  | 不支持heif类型的图片  |
| ArkWeb  | 是  | 是  | -  |
| Background Tasks Kit  | 是  | 是  | -  |
| Core File Kit  | 部分支持  | 部分支持  | 不支持分布式能力、AudioViewPicker  |
| Form Kit  | 部分支持  | 部分支持  | 不支持分布式能力  |
| IME Kit  | 是  | 是  | -  |
| IPC Kit  | 是  | 是  | -  |
| Localization Kit  | 是  | 是  | -  |
| UI Design Kit  | 否  | 否  | -  |
Kit名称
ARM版本
X86版本
备注
Ability Kit
部分支持
部分支持
不支持拉起文件处理类应用
Accessibility Kit
是
是
-
ArkData
部分支持
部分支持
不支持分布式能力
ArkTS
是
是
-
ArkUI
部分支持
部分支持
不支持heif类型的图片
ArkWeb
是
是
-
Background Tasks Kit
是
是
-
Core File Kit
部分支持
部分支持
不支持分布式能力、AudioViewPicker
Form Kit
部分支持
部分支持
不支持分布式能力
IME Kit
是
是
-
IPC Kit
是
是
-
Localization Kit
是
是
-
UI Design Kit
否
否
-
安全
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Asset Store Kit  | 是  | 是  | -  |
| Crypto Architecture Kit  | 是  | 是  | -  |
| Data Protection Kit  | 否  | 否  | -  |
| Device Certificate Kit  | 是  | 是  | -  |
| Device Security Kit  | 否  | 否  | -  |
| Enterprise Data Guard Kit  | 否  | 否  | -  |
| Online Authentication Kit  | 否  | 否  | -  |
| Universal Keystore Kit  | 是  | 是  | -  |
| User Authentication Kit  | 部分支持  | 部分支持  | 支持口令认证  |
Kit名称
ARM版本
X86版本
备注
Asset Store Kit
是
是
-
Crypto Architecture Kit
是
是
-
Data Protection Kit
否
否
-
Device Certificate Kit
是
是
-
Device Security Kit
否
否
-
Enterprise Data Guard Kit
否
否
-
Online Authentication Kit
否
否
-
Universal Keystore Kit
是
是
-
User Authentication Kit
部分支持
部分支持
支持口令认证
网络
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Connectivity Kit  | 部分支持  | 部分支持  | 支持wifi相关能力  |
| Distributed Service Kit  | 否  | 否  | -  |
| Network Kit  | 部分支持  | 部分支持  | 支持桥接本地计算机网络  |
| Network Boost Kit  | 否  | 否  | -  |
| Remote Communication Kit  | 是  | 是  | -  |
| Service Collaboration Kit  | 否  | 否  | -  |
| Telephony Kit  | 否  | 否  | -  |
Kit名称
ARM版本
X86版本
备注
Connectivity Kit
部分支持
部分支持
支持wifi相关能力
Distributed Service Kit
否
否
-
Network Kit
部分支持
部分支持
支持桥接本地计算机网络
Network Boost Kit
否
否
-
Remote Communication Kit
是
是
-
Service Collaboration Kit
否
否
-
Telephony Kit
否
否
-
基础功能
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Basic Services Kit  | 部分支持  | 部分支持  | 不支持usb、热管理、设备认证获取ODID前，需要先配置签名，可在模拟器上自动签名。  |
| Function Flow Runtime Kit  | 是  | 是  | -  |
| Input Kit  | 是  | 是  | -  |
| MDM Kit  | 否  | 否  | -  |
| Status Bar Extension Kit  | 否  | 否  | -  |
Kit名称
ARM版本
X86版本
备注
Basic Services Kit
部分支持
部分支持
Function Flow Runtime Kit
是
是
-
Input Kit
是
是
-
MDM Kit
否
否
-
Status Bar Extension Kit
否
否
-
硬件
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Car Kit  | 否  | 否  | -  |
| Driver Development Kit  | 否  | 否  | -  |
| Multimodal Awareness Kit  | 否  | 否  | -  |
| Pen Kit  | 否  | 否  | -  |
| Sensor Service Kit  | 部分支持  | 部分支持  | 支持部分传感器，参见虚拟传感器  |
| Wear Engine Kit  | 否  | 否  | -  |
Kit名称
ARM版本
X86版本
备注
Car Kit
否
否
-
Driver Development Kit
否
否
-
Multimodal Awareness Kit
否
否
-
Pen Kit
否
否
-
Sensor Service Kit
部分支持
部分支持
支持部分传感器，参见虚拟传感器
Wear Engine Kit
否
否
-
调测调优
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Performance Analysis Kit  | 否  | 否  | -  |
| Test Kit  | 是  | 是  | -  |
Kit名称
ARM版本
X86版本
备注
Performance Analysis Kit
否
否
-
Test Kit
是
是
-
媒体
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Audio Kit  | 是  | 是  | -  |
| AVCodec Kit  | 部分支持  | 部分支持  | 支持音频编解码、H264视频软解码  |
| AVSession Kit  | 否  | 否  | -  |
| Camera Kit  | 否  | 否  | -  |
| DRM Kit  | 否  | 否  | -  |
| Image Kit  | 是  | 是  | -  |
| Media Kit  | 部分支持  | 部分支持  | 不支持录像、拍照/扫码和屏幕录制  |
| Media Library Kit  | 部分支持  | 部分支持  | 不支持分布式能力  |
| Scan Kit  | 否  | 否  | -  |
| Ringtone Kit  | 否  | 否  | -  |
Kit名称
ARM版本
X86版本
备注
Audio Kit
是
是
-
AVCodec Kit
部分支持
部分支持
支持音频编解码、H264视频软解码
AVSession Kit
否
否
-
Camera Kit
否
否
-
DRM Kit
否
否
-
Image Kit
是
是
-
Media Kit
部分支持
部分支持
不支持录像、拍照/扫码和屏幕录制
Media Library Kit
部分支持
部分支持
不支持分布式能力
Scan Kit
否
否
-
Ringtone Kit
否
否
-
图形
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| AR Engine  | 否  | 否  | -  |
| ArkGraphics 2D  | 部分支持  | 部分支持  | 不支持OpenGL ES 3.0以上接口视频仅支持RGBA格式的像素  |
| ArkGraphics 3D  | 否  | 否  | -  |
| Graphics Accelerate Kit  | 否  | 否  | -  |
| XEngine Kit  | 否  | 否  | -  |
Kit名称
ARM版本
X86版本
备注
AR Engine
否
否
-
ArkGraphics 2D
部分支持
部分支持
ArkGraphics 3D
否
否
-
Graphics Accelerate Kit
否
否
-
XEngine Kit
否
否
-
应用服务
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Account Kit  | 是  | 否  | -  |
| Ads Kit  | 否  | 否  | -  |
| Calendar Kit  | 是  | 是  | -  |
| Call Kit  | 否  | 否  | -  |
| Cloud Foundation Kit  | 否  | 否  | -  |
| Contacts Kit  | 否  | 否  | -  |
| Game Service Kit  | 否  | 否  | -  |
| Health Service Kit  | 否  | 否  | -  |
| IAP Kit  | 否  | 否  | -  |
| Live View Kit  | 否  | 否  | -  |
| Location Kit  | 是  | 部分支持  | X86版本不支持地理逆编码  |
| Map Kit  | 否  | 否  | -  |
| Notification Kit  | 是  | 是  | -  |
| Payment Kit  | 否  | 否  | -  |
| PDF Kit  | 否  | 否  | -  |
| Preview Kit  | 否  | 否  | -  |
| Push Kit  | 部分支持  | 部分支持  | 支持getToken、deleteToken、getAAID、deleteAAID、bindAppProfileId、unbindAppProfileId支持推送通知消息、推送卡片刷新消息、推送后台消息使用Push Kit之前需要先配置签名，可在模拟器上自动签名  |
| Scenario Fusion Kit  | 否  | 否  | -  |
| Share Kit  | 否  | 否  | -  |
| Store Kit  | 否  | 否  | -  |
| Wallet Kit  | 否  | 否  | -  |
| Weather Service Kit  | 否  | 否  | -  |
Kit名称
ARM版本
X86版本
备注
Account Kit
是
否
-
Ads Kit
否
否
-
Calendar Kit
是
是
-
Call Kit
否
否
-
Cloud Foundation Kit
否
否
-
Contacts Kit
否
否
-
Game Service Kit
否
否
-
Health Service Kit
否
否
-
IAP Kit
否
否
-
Live View Kit
否
否
-
Location Kit
是
部分支持
X86版本不支持地理逆编码
Map Kit
否
否
-
Notification Kit
是
是
-
Payment Kit
否
否
-
PDF Kit
否
否
-
Preview Kit
否
否
-
Push Kit
部分支持
部分支持
Scenario Fusion Kit
否
否
-
Share Kit
否
否
-
Store Kit
否
否
-
Wallet Kit
否
否
-
Weather Service Kit
否
否
-
AI
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| Core Speech Kit  | 否  | 否  | -  |
| Core Vision Kit  | 否  | 否  | -  |
| HiAI Foundation Kit  | 否  | 否  | -  |
| Intents Kit  | 否  | 否  | -  |
| MindSpore Lite Kit  | 否  | 否  | -  |
| Natural Language Kit  | 否  | 否  | -  |
| Neural Network Runtime Kit  | 否  | 否  | -  |
| Speech Kit  | 否  | 否  | -  |
| Vision Kit  | 否  | 否  | -  |
Kit名称
ARM版本
X86版本
备注
Core Speech Kit
否
否
-
Core Vision Kit
否
否
-
HiAI Foundation Kit
否
否
-
Intents Kit
否
否
-
MindSpore Lite Kit
否
否
-
Natural Language Kit
否
否
-
Neural Network Runtime Kit
否
否
-
Speech Kit
否
否
-
Vision Kit
否
否
-
NDK开发
| Kit名称  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- |
| NDK  | 支持  | 部分支持  | X86版本不支持libjsvm  |
Kit名称
ARM版本
X86版本
备注
NDK
支持
部分支持
X86版本不支持libjsvm
其他
除Kit外，在其他场景下，模拟器和真机的能力也存在差异，具体如下表：
| 场景  | 能力  | ARM版本  | X86版本  | 备注  |
| --- | --- | --- | --- | --- |
| 预置应用      | 小艺输入法  | 是  | 是  | -  |
| 文件管理  | 部分支持  | 部分支持  | ARM/X86版本不支持.pdf/.pptx/.xlsx/.docx文件格式预览X86版本不支持文件删除  |
| 设置  | 是  | 是  | -  |
| 图库  | 是  | 是  | -  |
| 浏览器  | 是  | 否  | -  |
| 三方框架    | React Native  | 否  | 否  | -  |
| Taro  | 否  | 否  | -  |
| Flutter  | 部分支持  | 否  | ARM版本不支持视频播放  |
| 元服务   | 域名管控（配置服务器域名）  | 模拟器元服务域名访问不管控，不需要配置服务器域名  | -  |
| 账号登录管理  | 模拟器无需登录华为账号可以直接调试元服务  | -  |
场景
能力
ARM版本
X86版本
备注
预置应用
小艺输入法
是
是
-
文件管理
部分支持
部分支持
设置
是
是
-
图库
是
是
-
浏览器
是
否
-
三方框架
React Native
否
否
-
Taro
否
否
-
Flutter
部分支持
否
ARM版本不支持视频播放
元服务
域名管控（配置服务器域名）
模拟器元服务域名访问不管控，不需要配置服务器域名
-
账号登录管理
模拟器无需登录华为账号可以直接调试元服务
-

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-management-V14
爬取时间: 2025-04-30 08:04:08
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-create-V14
爬取时间: 2025-04-30 08:04:46
来源: Huawei Developer
操作步骤
1.
2.  在模拟器配置界面，可以选择一个默认的设备模板，首次使用时会提示“Download the system image first”，请点击设备右侧的下载模拟器镜像，您也可以在该界面更新或删除不同设备的模拟器镜像。单击Edit可以设置镜像文件的存储路径。Mac默认存储在~/Library/Huawei/Sdk下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Sdk下。
3.
4.
5.
6.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150702.59354491660345004403859035826396:50001231000000:2800:23AC62C2D271544F8170BCED706CE4ECA44E073C52251417D59097D3A2CECF55.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150702.52709101883548999044010663993875:50001231000000:2800:46D7C4D4F06FAFBBD0D6B63EEC46D1505BE0DBA50E4595302004DA29FCCA44A3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150702.11580098232606140323244733613547:50001231000000:2800:F8A5FAFC91C53A64D14F48BCEACF2495C7DB28A1C852A25126543C43AC5644E2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150702.78044772272677352961292943670545:50001231000000:2800:9F7685CAEFB62510553C9FFEEDDA882777A4F863EE9179496A7FCC2373823A81.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150702.75159760532174263463263659257482:50001231000000:2800:73B696CF4AA83F1CD6EA81A63E5064FFE7CC0A59B952FDAF79FE1D2264F5B16F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150702.89154111495334428046560680858212:50001231000000:2800:2AEEE2DAE31EA518D1B7ADBBFB9C73930B664F322C3E0EFFF9BD1579186C08C0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.06327485754790987728411395587848:50001231000000:2800:FDE90CB160BFAED756F1632B6300B97B6881A5B9DEC59B0FA7092DD8F5BF2211.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.02732765482496544497231012353093:50001231000000:2800:24B2449B83011882A70D282D6B355D81148BDC699C4225DD1FE25D81F87BA9E3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.47698297272092765150998562074090:50001231000000:2800:4DFCE4A87FEE97769ECF69D32C4C79B872B9CCDF07568202257855EA7D7A6085.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-start-and-close-V14
爬取时间: 2025-04-30 08:05:21
来源: Huawei Developer
在设备管理器页面，单击即可启动模拟器。模拟器启动时会默认携带上一次运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除上一次运行时的用户数据，点击Actions >> Wipe User Data。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.98446128671365710958282686461669:50001231000000:2800:FCE73697BF397D8C305A7729BBE43036090C65A9A84226E60511A825374AEF28.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.56884880912616630739047112201124:50001231000000:2800:75BC61C5CB0F370FDA9451ED76860404883CCA11CD60C23BF3ACC5325322E0B2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.42007477642740062943064685139571:50001231000000:2800:B7C42EC51AE42B65EDFF5B0C560DD9927DCEAFE5156F99955171624DCA1CAECC.png?needInitFileName=true?needInitFileName=true)
在模拟器运行期间，可以点击Actions >> Show on Disk显示模拟器在本地生成的用户数据。点击Actions >> Generate logs可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行时的模拟器，可以在设备管理器页面点击，或者点击模拟器工具栏上的关闭按钮。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.23061333206766725183997857339084:50001231000000:2800:194CD8E35BA75BAC544390A7E6E8787A4B426E9A0A87377ADFBA3CF2634A7375.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.13685556969315026063688641688712:50001231000000:2800:65827923A3C1C727A82D7DA72E6A34495A78DD8BF8826EA61EA0F7D6D5367230.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.34845157823017362731339950450393:50001231000000:2800:C5722970F9DB4997CD68546AA2CF7FCD5196278A346FC3D8FB4493AA7090122F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.33501353062330335640122465499737:50001231000000:2800:69D0FF369D17DE52E8935F7E6F262329A33B9CAA387504366DA9ACF45F94A8F7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.99822429955375849516243392033392:50001231000000:2800:1B1ED3361CA8E72A7457769DE87398D5F0C2AC89A217D5DAF876B2A517C54C7D.png?needInitFileName=true?needInitFileName=true)
模拟器关闭后，点击Actions >> Delete可以删除模拟器，并清除模拟器的用户数据和配置信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.60825520876197674648698844576699:50001231000000:2800:114BB7C9C9C031A5F459E3AAC79CBB2405705581FAEE2C0AF6DD2B47E4449D2A.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-use-V14
爬取时间: 2025-04-30 08:05:55
来源: Huawei Developer
模拟器界面由两部分构成：设备屏幕和工具栏。设备屏幕部分模拟了真实设备的显示屏，让开发者可以在模拟环境中对应用进行调试和测试。通过模拟器，开发者可以在不依赖于物理设备的情况下进行开发工作，节省了设备和资源成本。工具栏则提供了各种调试工具和控制选项，帮助开发者模拟不同的场景和操作，以提高用户的调试效率。本章节将向您介绍如何使用模拟器。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-control-screen-V14
爬取时间: 2025-04-30 08:06:30
来源: Huawei Developer
当模拟器运行时，您可以使用鼠标来模拟手指和设备屏幕进行交互，同时可以结合键盘来实现高级的屏幕操作，对应关系如下：
| 常用操作  | 描述  |
| --- | --- |
| 滑动屏幕  | 将鼠标放置屏幕上方，按住鼠标左键，在屏幕上轻扫，然后释放。  |
| 拖动项目  | 将鼠标放置屏幕中的项目上方, 按住鼠标左键，移动项目，然后释放。  |
| 单击屏幕  | 将鼠标放置屏幕上方，按住鼠标左键，然后释放。  |
| 双击屏幕  | 将鼠标放置屏幕上方，快速双击鼠标左键，然后释放。  |
| 长按屏幕  | 指向屏幕上的一个项目，按下鼠标左键，保持一段时间，然后释放。  |
| 输入文字  | 鼠标点击输入域，随后您可以使用计算机键盘或屏幕上弹出的软键盘在模拟器中键入文字。  |
| 双指缩放  | Windows系统按下Control键（macOS上的Command）会弹出一个捏合手势多点触控界面。单击鼠标左键模拟按住双指，并释放鼠标左键模拟松开双指。鼠标充当第一个手指，穿过锚点是第二个手指。拖动光标以移动第一个点。  |
| 垂直滑动  | 在屏幕上打开一个垂直菜单，使用鼠标滚轮滚动菜单项。单击菜单项可进行选择。  |
| 复制粘贴  | 在计算机上复制一段文本后，您可以在模拟器屏幕的文本输入框内进行粘贴。可支持复制的最大文本长度为30000英文字符，超过该长度会对文本进行截断。  |
常用操作
描述
滑动屏幕
将鼠标放置屏幕上方，按住鼠标左键，在屏幕上轻扫，然后释放。
拖动项目
将鼠标放置屏幕中的项目上方, 按住鼠标左键，移动项目，然后释放。
单击屏幕
将鼠标放置屏幕上方，按住鼠标左键，然后释放。
双击屏幕
将鼠标放置屏幕上方，快速双击鼠标左键，然后释放。
长按屏幕
指向屏幕上的一个项目，按下鼠标左键，保持一段时间，然后释放。
输入文字
鼠标点击输入域，随后您可以使用计算机键盘或屏幕上弹出的软键盘在模拟器中键入文字。
双指缩放
Windows系统按下Control键（macOS上的Command）会弹出一个捏合手势多点触控界面。单击鼠标左键模拟按住双指，并释放鼠标左键模拟松开双指。鼠标充当第一个手指，穿过锚点是第二个手指。拖动光标以移动第一个点。
垂直滑动
在屏幕上打开一个垂直菜单，使用鼠标滚轮滚动菜单项。单击菜单项可进行选择。
复制粘贴
在计算机上复制一段文本后，您可以在模拟器屏幕的文本输入框内进行粘贴。可支持复制的最大文本长度为30000英文字符，超过该长度会对文本进行截断。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-toolbar-V14
爬取时间: 2025-04-30 08:07:04
来源: Huawei Developer
工具栏上集成了模拟器的各种调试工具和控制选项，其中的扩展菜单栏包含了更加丰富的扩展功能。注意，部分工具栏按键需要在模拟器开机亮屏后才能使用。以下对工具栏的各个按键功能作简要说明：
| 按键  | 功能描述  |
| --- | --- |
| 关闭  | 关闭模拟器  |
| 最小化  | 最小化模拟器窗口  |
| 更多  | 打开侧边扩展菜单  |
| 置顶  | 将模拟器置于所有打开窗口的顶层  |
| 左旋转  | 将设备屏幕逆时针旋转90度  |
| 右旋转  | 将设备屏幕顺时针旋转90度  |
| 增大音量  | 调高设备音量，长按可持续调高设备音量  |
| 减小音量  | 调低设备音量，长按可持续调低设备音量  |
| 截屏  | 生成当前屏幕的截图，并将图片保存在本地计算机  |
| 返回  | 返回上一屏幕或关闭对话框、选项菜单、通知面板或屏幕键盘  |
| 主屏  | 返回Home界面  |
| 最近  | 点按可打开最近使用过的应用的缩略图列表。要打开某个应用，请点按其缩略图。要从列表中删除缩略图，请向上滑动缩略图  |
| 摇一摇  | 触发设备摇一摇操作，详情参考摇一摇  |
| 电池  | 打开电池模拟面板，详情参考电池  |
| GPS  | 打开GPS模拟面板，详情参考GPS定位  |
| 虚拟传感器  | 打开虚拟传感器面板，详情参考虚拟传感器  |
| 网络代理  | 打开网络代理面板，详情参考网络代理  |
| 设置  | 打开设置面板。可设置模拟器主题、截屏保存路径、模拟器使用语言  |
| Bug报告  | 打开Bug报告面板。可以保存Bug日志到本地。点击发送可前往官网在线提单  |
| 关于  | 打开关于面板。可以查看模拟器相关信息及许可证  |
| 展开  | 仅支持可折叠设备。切换设备形态至展开态  |
| 悬停  | 仅支持可折叠设备。切换设备形态至悬停态，并显示折痕避让区  |
| 折叠  | 仅支持可折叠设备。切换设备形态至折叠态  |
按键
功能描述
关闭
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.91071147279109688655961931788078:50001231000000:2800:FE1CFE086C989B722E6D7C235F5271464EE56E606BB89E5A340669297B729FFF.png?needInitFileName=true?needInitFileName=true)
关闭模拟器
最小化
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150703.87915306317329153131725288724929:50001231000000:2800:F089C59D89FD3F72DA36122551EA9FE8F4DABF14DC4FFBE9FA8597089B0D5662.png?needInitFileName=true?needInitFileName=true)
最小化模拟器窗口
更多
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.50057063874474834162229074889598:50001231000000:2800:1D68846EAD29A7C33004CA2C98F0CE0228BF25F936385CFDEEA06103DD8EC0D8.png?needInitFileName=true?needInitFileName=true)
打开侧边扩展菜单
置顶
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.47781648789851469709004732502343:50001231000000:2800:A8405E19FE34147B0871AB6E18CACD5803E3019530207FF3C91C064F39D5B78E.png?needInitFileName=true?needInitFileName=true)
将模拟器置于所有打开窗口的顶层
左旋转
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.32341447345218097591873990525570:50001231000000:2800:1FEFA9D3D2780D35651406515E16805772A68645E64CE5E50B1F118D5DB23182.png?needInitFileName=true?needInitFileName=true)
将设备屏幕逆时针旋转90度
右旋转
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.70875596173614735536243950788255:50001231000000:2800:15F39748879B157C9267FD2A142EAE709DFB465B0CC6C6DA0B691C495724B90F.png?needInitFileName=true?needInitFileName=true)
将设备屏幕顺时针旋转90度
增大音量
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.04471891081121477583961240640900:50001231000000:2800:E7AFBDB0A037819FBA23BE24338C8211C38653CBEBE64AB1BC447C69661BB138.png?needInitFileName=true?needInitFileName=true)
调高设备音量，长按可持续调高设备音量
减小音量
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.43592293226406826252492636830370:50001231000000:2800:3E1B35D9C124335AEEF1C3C4F0B901A5ADE43EB0D45983C3D7370DFC4CD66EEA.png?needInitFileName=true?needInitFileName=true)
调低设备音量，长按可持续调低设备音量
截屏
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.20189445754159937884839677550058:50001231000000:2800:AB8F9FE1F2F303C624609D62C27696F6E4B91D189AF5D9D7DAD7CCC853A484E5.png?needInitFileName=true?needInitFileName=true)
生成当前屏幕的截图，并将图片保存在本地计算机
返回
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.32143033473812040396446090337182:50001231000000:2800:7ECC7C7AFD92B8DFA85BF772F143F1E4C6A78BD0E79A2066F73290813F397612.png?needInitFileName=true?needInitFileName=true)
返回上一屏幕或关闭对话框、选项菜单、通知面板或屏幕键盘
主屏
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.51427838909839467227891364376828:50001231000000:2800:DC206CA62553EEF7B06E53F5E3D8ECB3EBE47D010768871FF17CC8A81C43F6A0.png?needInitFileName=true?needInitFileName=true)
返回Home界面
最近
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.86666040335792522214968556833214:50001231000000:2800:9CD76D84852112459E3F261DE7AF6CE84315343568027AEA17A9C2D098BF9E96.png?needInitFileName=true?needInitFileName=true)
点按可打开最近使用过的应用的缩略图列表。要打开某个应用，请点按其缩略图。要从列表中删除缩略图，请向上滑动缩略图
摇一摇
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.77363989456814684537228349834400:50001231000000:2800:5C0CC4A2165DA6637737A69DE1652EBEFC64B6D42F514533F824525680855887.png?needInitFileName=true?needInitFileName=true)
触发设备摇一摇操作，详情参考摇一摇
电池
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.89511422451543506353170977360513:50001231000000:2800:427F83E5124CBA63DCED0F78A201EBED955BC4382ED57EB9935F78806227CD05.png?needInitFileName=true?needInitFileName=true)
打开电池模拟面板，详情参考电池
GPS
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.88631229494267255082199213119912:50001231000000:2800:CBE98CB3A927F3CDBE1E8559E8013C98E98AE0F7F54D44F083C803DF5D9301B9.png?needInitFileName=true?needInitFileName=true)
打开GPS模拟面板，详情参考GPS定位
虚拟传感器
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.13832390840020065005929063876394:50001231000000:2800:F2851B61CFAEBB61AD6847B9CAF589A7F72025281C88B15642077CD17DE626A3.png?needInitFileName=true?needInitFileName=true)
打开虚拟传感器面板，详情参考虚拟传感器
网络代理
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.26573284972018888327266746225024:50001231000000:2800:D5F8FC18FF4F05F804209A9EE7C8F4AB8D947D2A70F28619A2F92D69C8F59EAC.png?needInitFileName=true?needInitFileName=true)
打开网络代理面板，详情参考网络代理
设置
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.54140053646215197304043630256028:50001231000000:2800:99026A93C33ABABA92CDB9B0EBC61AC1B59697E994E15344A2A9D957C6ADD3B5.png?needInitFileName=true?needInitFileName=true)
打开设置面板。可设置模拟器主题、截屏保存路径、模拟器使用语言
Bug报告
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.52325286027476141944699738895633:50001231000000:2800:E21DE6CF2B5F52B025C5605ADBFB0E5BD472A18A8B931EB7204EAF5E269A97FF.png?needInitFileName=true?needInitFileName=true)
打开Bug报告面板。可以保存Bug日志到本地。点击发送可前往官网在线提单
关于
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.32383109012409984781388716758127:50001231000000:2800:650899CE85B9BBA1D3D47A11CD3FE82FFE2B0391C46CC11ADC7CE5E38AACF251.png?needInitFileName=true?needInitFileName=true)
打开关于面板。可以查看模拟器相关信息及许可证
展开
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.47621695657766022057546658670893:50001231000000:2800:FE78B4BC8188942EE44B8DC2B0883E53F2FE2E759116EAB2D3F28585D51D529E.png?needInitFileName=true?needInitFileName=true)
仅支持可折叠设备。切换设备形态至展开态
悬停
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150704.57387293897087416385595189802686:50001231000000:2800:7EAE258C9DA31209CFE99A897E1032F91B9623FFEA21BFD9500BE5FA4982546F.png?needInitFileName=true?needInitFileName=true)
仅支持可折叠设备。切换设备形态至悬停态，并显示折痕避让区
折叠
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.44922240361623982402079006390695:50001231000000:2800:14203FF308769CB2BFA2448664DB4005213CFB12D3DCB17A4272322DCD9EBC16.png?needInitFileName=true?needInitFileName=true)
仅支持可折叠设备。切换设备形态至折叠态

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-move-and-zoom-V14
爬取时间: 2025-04-30 08:07:39
来源: Huawei Developer
-  您可以使用鼠标拖动模拟器到屏幕的指定位置。首先将鼠标放在屏幕边缘，当鼠标变成样式，按住鼠标左键并移动即可拖动模拟器。当模拟器被拖动到期望位置后，松开鼠标左键即可停止拖动。
-  如需改变模拟器大小，将鼠标放到屏幕四角的任意一处，当鼠标变成，按住鼠标左键并移动即可缩放模拟器。当模拟器被缩放到期望大小后，松开鼠标左键即可完成缩放。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.41508333219397140343247133282899:50001231000000:2800:36DE80D3853BF801595D8A14137E603B885DA375F4DCB74D2FE4A11452CBE7E2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.94128966983559907143709398652102:50001231000000:2800:47D35A393590394A39C0B02EB63CE2909CAD64EAA03906700B1CFC08F9DDE5A2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.99024442978309880481066078125311:50001231000000:2800:59F3F685293C5FA4180A002E4CA59D28DDAF56426157CE066CBA2E1E730CB418.gif?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-access-network-V14
爬取时间: 2025-04-30 08:08:13
来源: Huawei Developer
模拟器访问互联网
模拟器可以通过本地计算机的网络直接访问互联网。
如果连接失败请参考：模拟器无法连接网络和使用模拟器发起https请求时如何安装数字证书。
由于模拟器的虚拟以太网一直处于连接状态，断开本地计算机的网络或模拟器内的WiFi，无法使模拟器进入网络完全断开的状态。
模拟器访问本机网络
在本地计算机上建立网络服务端，模拟器可以通过10.0.2.2:<localPort>访问本地计算机服务端，其中10.0.2.2为模拟器的默认网关。
两个模拟器实现互相访问
如果两个模拟器需要进行通信互联，请按如下步骤进行设置。
1.  该命令中127.0.0.1:5555为模拟器B的HDC服务端口号，可通过hdc list targets命令查询。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.69228142418559479882247812580725:50001231000000:2800:7041616BCB94174653FF77F413DAF623E1751DF05BC415CD003F3A12AB53D9B7.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-install-upload-V14
爬取时间: 2025-04-30 08:08:48
来源: Huawei Developer
-  您可以将本地的HAP包安装到模拟器上，只需要将本地的HAP包拖动到屏幕上即可进行安装，支持一次性拖拽安装多个HAP包。模拟器也支持安装包含HSP文件的应用，只需要将HSP和HAP一起拖动到屏幕上即可进行安装。也可以在命令行窗口进入Deveco Studio安装目录的sdk\default\openharmony\toolchains目录下，使用hdc app install命令安装包。安装完成后，可在应用列表里查看已安装的应用。
-  您可以将本地文件上传到模拟器中，只需要将文件拖动至模拟器屏幕上即可。模拟器支持批量上传文件，上传的文件存放在虚拟设备的/storage/media/100/local/files/Docs/Download/目录下。您可以在模拟器上打开文件管理 > 我的手机 > 下载查看上传的文件。 此外，您也可以在命令行窗口进入Deveco Studio安装目录的sdk\default\openharmony\toolchains目录下，使用hdc file send命令上传文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.97943401419386959152329464327502:50001231000000:2800:C68CC26187634B42A0BCCFB8650F73F760F8DAC982AC1ECC9A6DF8FDC8D1965E.gif?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-more-features-V14
爬取时间: 2025-04-30 08:09:22
来源: Huawei Developer
电池
您可以在模拟器上模拟不同电池状态。在扩展菜单栏上点击打开电池模拟界面。在该界面，您可以手动输入或拖动滑块来改变电量百分比，也可以点击切换电池的充电/放电状态。电池具有以下三种充电状态：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.54313671488377461037722675660086:50001231000000:2800:E077EBE093D76DED7E80A15829B56D861912EB9F4864D9D33837F6B24CD9E77C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.67765909916024651066874354647177:50001231000000:2800:683F7C2D528780892A6C224BF54F3E64002D80E12C301AAC6C9694469B7410BB.png?needInitFileName=true?needInitFileName=true)
在应用中，您可以通过@ohos.batteryInfo模块查询模拟器的剩余电量以及充电状态。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.07862658375427420561739726802067:50001231000000:2800:6E0EF968B9547FAD5D117E5B4173D20C60167A7668DB0A2CE2C4188A9E6F0883.gif?needInitFileName=true?needInitFileName=true)
GPS定位
模拟器可以模拟设备所处的位置。您可以打开扩展菜单，并点击进行位置信息的设置。模拟器提供以下三种方式的GPS位置模拟：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.31954064797121246010711169252361:50001231000000:2800:1714DC694D4B2ABF88F4009DE620B1BBF1BA9B59B0C8692CB3EA3462058ABB2C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.51945783048256391904058371095020:50001231000000:2800:EB6612EC5714B7BBD44C3868E0C18CB2D0E214D7425577E4EEB02B272537A102.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.65860305901208909455134536280941:50001231000000:2800:53FABCA5F034B9FC04CE9D58F29E023AC05EC74DC3715B8A8B1552131ED6EF8E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.52140672797045698911899488576650:50001231000000:2800:7DA981C02F2A98F26DE6033BB661216D1B4EDA979D42CEBC0326B591DA6A11A9.png?needInitFileName=true?needInitFileName=true)
在应用中，您可以通过@ohos.geoLocationManager模块获取模拟器的位置信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.89157277129460536321422675040162:50001231000000:2800:96FCC11AEE0C9F8BF7FDE7FAA2397E7FF44D60023EFE30D85CC190AA5F97A9A7.gif?needInitFileName=true?needInitFileName=true)
虚拟传感器
模拟器提供了虚拟传感器来模拟硬件传感器的能力。在扩展菜单上点击打开虚拟传感器界面。在该界面，您可以调节不同的传感器来测试您的应用，使用@ohos.sensor模块监听传感器值的变化。模拟器提供以下虚拟传感器：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150705.39850818427793900770651603068780:50001231000000:2800:7CFBDB3E9E72242F34EB3296F63FE11E06308D14521B15C74E3AB70B1AC62693.png?needInitFileName=true?needInitFileName=true)
您可以拖动滑动条或者直接在文本框输入来改变不同传感器的值。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150706.84969609181777181669093226089344:50001231000000:2800:21D31B5ACA2A89CD5DCF5D8624776018FC59F1B86DF4BCF0394D4CC63382F3A1.png?needInitFileName=true?needInitFileName=true)
网络代理
模拟器可以将网络请求代理到代理服务器，利用代理服务器去请求目标服务器。从而满足以下开发场景：
您可以打开扩展菜单，并点击进行代理的配置。模拟器提供以下三种代理模式：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150706.00756585945123325108771791135292:50001231000000:2800:75CF5044DE56661C3E91F37775A41CD8C3B114A4CDCFAC20217E4CB872DFBF7D.png?needInitFileName=true?needInitFileName=true)
以上的代理配置需要点击按钮生效，同时可以通过点击按钮对当前的代理配置进行校验。在发起https请求时，需要安装网站的数字证书，请参考使用模拟器发起https请求时如何安装数字证书。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150706.05459511519298566660584677749480:50001231000000:2800:3520B1681DF6CE70EC216639433E173682F5EF35A1E8FD5D6E8D06FA31DDE600.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150706.52315484074435141713369875912109:50001231000000:2800:170DBB7022DCEE2BB9BB3D63AA58F56B971116598CD8FE613043F6B660284875.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150706.15169621833672531280051374727330:50001231000000:2800:B64F4AFA0487875B935EC350E915248E73330A7AFB9983E1390D6B4526D6D2EE.png?needInitFileName=true?needInitFileName=true)
摇一摇
模拟器可以模拟用户对设备的摇一摇操作。点击工具栏上的，您可以模拟时长为1s的摇一摇操作。您的应用可以通过@ohos.sensor模块监听加速度传感器变化，当加速度传感器的变化量达到设定阈值时，触发摇一摇对应的业务逻辑。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150706.87032979820396204281823096758417:50001231000000:2800:49922FCCAB7076DE8E483B5B604919A35C7D108B503851175EEB2F62B97CE61A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150706.73685144132325284957347634078495:50001231000000:2800:6668D99C20BEA41C66EDCF08A5BCB9FB35BD348D6F8753B08639117169FD97AB.gif?needInitFileName=true?needInitFileName=true)
音频输入
模拟器当前仅支持Audio Kit（音频服务）提供的音频输入能力，您可以使用本地计算机上的麦克风设备向模拟器中传输音频数据。使用步骤如下：
模拟器上的应用在调用相关API时，推荐使用如下格式的音频流信息格式，以保证清晰流畅的音质。
| 音频流信息  | 推荐值  |
| --- | --- |
| samplingRate（采样率）  | 48000Hz  |
| channels（通道数）  | 2  |
| sampleFormat（采样格式）  | 带符号的16位整数  |
| encodingType（编码格式）  | PCM编码  |
音频流信息
推荐值
samplingRate（采样率）
48000Hz
channels（通道数）
2
sampleFormat（采样格式）
带符号的16位整数
encodingType（编码格式）
PCM编码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-emulator-faqs-V14
爬取时间: 2025-04-30 08:09:57
来源: Huawei Developer
当模拟器运行出现错误时，您可以向我们提交错误信息。在扩展菜单栏打开Bug报告界面，在该界面您可以查看模拟器的上下文信息（包括本地操作系统信息，模拟器版本信息，镜像版本信息)，界面左侧展示了Bug出现时的设备截屏。您可以输入Bug的再现步骤来帮助我们更快的解决此问题，同时选择Bug信息中是否包含日志（日志中可能包含代码堆栈）以及屏幕截图。点击Save按钮将Bug的相关信息保存至本地。点击Send按钮可自动跳转到HarmonyOS Developer网站在线提交错误。在提交错误信息时，请在附件里上传保存的Bug信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.44286335749065020104576389847764:50001231000000:2800:5D9FBBF02E0DE2355EFE39D4C04DFF3CF6E10E6142571EA6059FE871E406B254.png?needInitFileName=true?needInitFileName=true)
模拟器应用运行时崩溃退出
问题现象
在启动调试或运行过程中应用异常退出。
解决措施
模拟器使用OpenGLES指令绘制图像，可能与真机存在色差
由于本地计算机所使用的OpenGL图形驱动与真机的图形驱动存在差异，部分图形接口的绘制效果无法与真机保持一致。同时，不同的显示设备也可能呈现出不同的显示效果，存在色差、饱和度的差异。
macOS上活动监视器中显示模拟器内存偏高
配置模拟器内存为4GB并使用一段时间，您可能会在活动监视器中发现模拟器进程占用了超过6GB的内存（如下图所示）。需要明确的是，图中的6.49GB并不代表模拟器进程实际使用的物理内存（即Dirty内存），而是指其占用的phys_footprint内存。在Mac系统中，针对虚拟化平台（如模拟器），普遍存在phys_footprint内存远高于Dirty内存的情况。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.40287125990364610625467117811298:50001231000000:2800:10989BD99AC8C7E8873976036D1C0F1697BBEFB8873F55A010679EE909986ADA.png?needInitFileName=true?needInitFileName=true)
想要查看模拟器的Dirty内存，首先打开活动监视器，查看Emulator的进程号（PID）。然后通过 `footprint -vmObjectDirty 进程号` 命令可以查看Dirty内存大小。
如何增加模拟器运行内存
问题现象
模拟器默认内存为4G，运行过程中内存不足时，可能会出现模拟器卡顿或者闪退。
解决措施
建议在创建模拟器时增加模拟器的运行内存（RAM）大小，请参考创建模拟器。
Windows x86模拟器三方C/C++库使用限制
x86模拟器支持已x86化的C/C++三方库调试运行，未x86化的三方库开发者可以自行编译x86版本。
目前已经x86化的三方库如下：
| 三方库  | 备注  |
| --- | --- |
| @ohos/mmkv  | 自2.0.4-rc.4版本开始支持x86编译。  |
| @ohos/imageknife  | 自2.1.1版本开始支持x86编译。已经是2.1.1版本请重新安装imageknife再进行编译。  |
| @ohos/videocompressor  | 自1.0.3版本开始支持x86编译。  |
| @ohos/coap  | 自2.0.5版本开始支持x86编译。  |
| @ohos/unrar  | 自2.0.2版本开始支持x86编译。  |
| @ohos/commons-compress  | 自2.0.2-rc.0版本开始支持x86编译。  |
| @ohos/socketio  | 自2.0.0版本开始支持x86编译。  |
| @ohos/smack  | 自2.0.1-rc.0版本开始支持x86编译。  |
| @ohos/ijkplayer  | 自2.0.3-rc.0版本开始支持x86编译。  |
| @ohos/mqtt  | 自2.0.5版本开始支持x86编译。  |
| @ohos/mars  | 自2.0.1-rc.1版本开始支持x86编译。  |
| @ohos/mp4parser  | 自2.0.2-rc.0版本开始支持x86编译。  |
三方库
备注
@ohos/mmkv
自2.0.4-rc.4版本开始支持x86编译。
@ohos/imageknife
自2.1.1版本开始支持x86编译。已经是2.1.1版本请重新安装imageknife再进行编译。
@ohos/videocompressor
自1.0.3版本开始支持x86编译。
@ohos/coap
自2.0.5版本开始支持x86编译。
@ohos/unrar
自2.0.2版本开始支持x86编译。
@ohos/commons-compress
自2.0.2-rc.0版本开始支持x86编译。
@ohos/socketio
自2.0.0版本开始支持x86编译。
@ohos/smack
自2.0.1-rc.0版本开始支持x86编译。
@ohos/ijkplayer
自2.0.3-rc.0版本开始支持x86编译。
@ohos/mqtt
自2.0.5版本开始支持x86编译。
@ohos/mars
自2.0.1-rc.1版本开始支持x86编译。
@ohos/mp4parser
自2.0.2-rc.0版本开始支持x86编译。
Windows x86模拟器安装HAP时失败
问题现象
在启动调试或运行C++应用/元服务时，安装HAP出现错误，提示“error: install parse native so failed”错误信息。
解决措施
请参考安装HAP时提示“code:9568347 error: install parse native so failed”错误。
模拟器无法连接网络
问题现象
开发者打开了模拟器中的WLAN选项并已成功连接到VirtWifi，但是在模拟器中仍然无法访问网站。
解决措施
是否连接VirtWifi与模拟器能否访问互联网无关。VirtWifi仅用于在模拟器中判断WLAN的连接状态。模拟器访问网络实际上利用的是本地计算机的以太网或者WLAN，与本地计算机共享同一网络资源。如出现无法连接网络的情况，请开发者确认本地网络访问是否受到了限制（如使用公司内网）。如果对网络访问进行了限制，则需要在模拟器上配置网络代理。参见网络代理。
使用模拟器发起https请求时如何安装数字证书
问题现象
在使用网络代理发送https请求时，有时需要安装网站服务器的数字证书。
解决措施
模拟器上安装证书的过程分为两步：
1、将证书拖拽上传至模拟器中，“文件管理-我的手机-下载”目录下可查看上传的文件。
2、在本机命令行窗口中使用以下命令打开证书管理。
选择“从存储设备安装“，选择pem格式证书进行安装。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.57218140781940852710832637568384:50001231000000:2800:9808E6ABC9CB06CA9CC0A7CB568EDCFE9BBD7D30C1B1F96140F2B174D71F07A8.png?needInitFileName=true?needInitFileName=true)
在模拟器中卸载应用显示成功，但实际未卸载成功
问题现象
通过桌面菜单卸载应用，显示卸载成功，但实际未卸载成功。
解决措施
出现该问题的原因是模拟器的磁盘空间已满，无法正常卸载应用。一般在频繁使用hdc file send local remote命令向模拟器中推送文件后可能会出现该问题。
请尝试通过如下两种方式解决：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.30866340450284331074150120920631:50001231000000:2800:F996FD1DE8519597F6E771F4035B74B60BEAC4F341D60E90061219F6F808EC2A.png?needInitFileName=true?needInitFileName=true)
运行工程到模拟器，提示“Failed to get the device apiVersion”
问题现象
模拟器已启动后，运行工程到模拟器，提示“Failed to get the device apiVersion”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.23177789033264462943256725240650:50001231000000:2800:28C1F4DDF507662D47EC88C0F85E9227CF7D2F5A989242C3D5EF04B6278E1146.png?needInitFileName=true?needInitFileName=true)
解决措施
可以通过如下方式重新运行工程：
模拟器播放本地音频文件偶现卡顿
问题现象
部分场景下，模拟器播放音频文件可能出现卡顿情况：
场景一：模拟器启动后，立即播放音频；
场景二：长时间使用模拟器播放音频。
解决措施
在模拟器启动稳定后再进行音频场景测试，对于需要长时间验证音频播放的场景，建议使用真机设备。
模拟器时间与系统时间不一致
问题现象
模拟器长时间运行后，可能出现显示的时间与当前实际的系统时间不一致。
解决措施
在设置中打开自动设置时间，联网情况下时间会自动同步，也可以手动设置时间。重启模拟器后时间会同步。
模拟器启动后，设备无法识别
问题现象
场景一：调试运行过程中，安装HAP失败，提示“Device not founded or connected”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.95148757316695195936459594507062:50001231000000:2800:97864FFF0BE53B5E03AAA2A8F20F2ACF3F74773B41B2BE6F46E08A72BD0BC9DC.png?needInitFileName=true?needInitFileName=true)
场景二：DevEco Studio无法识别到已连接的设备，显示“No device”。
解决措施
参考设备连接后，无法识别设备的处理指导。
在应用中如何区分真机和模拟器
问题现象
在调试应用代码时，有时需要判断当前运行的设备是真机还是模拟器，如何进行区分？
解决措施
在应用中，您可以使用@ohos.deviceInfo模块的productModel属性来区分真机和模拟器。在模拟器上productModel的值为emulator。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.68449030341726213563916164179636:50001231000000:2800:AC61041A59DBF851A3E70BD4FBCD0F5FBF925021566A8A10D9204AC8D3FB6311.png?needInitFileName=true?needInitFileName=true)
设备管理点击新建模拟器无响应
问题现象
在设备管理界面点击New Emulator按钮没有反应，无法新建模拟器。
解决措施
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.04472951290543078063461123582608:50001231000000:2800:A12858665A22F5BEF3609C919DD75E578E67C893CFFB2C605DDFABB080A3EB3B.png?needInitFileName=true?needInitFileName=true)
在Windows电脑上启动模拟器，提示未开启Hyper-V
问题现象
启动模拟器时，弹窗提示“未开启Hyper-V”或“Hyper-V not enabled”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.06309038717878755506860792027710:50001231000000:2800:B62750B612B7A0225A2FD8A0DF096301E4811E5056D01B945AA5CAAE682CE8BD.png?needInitFileName=true?needInitFileName=true)
解决措施
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161817.76818009257263454286391586397815:50001231000000:2800:F768B2D72C1662B13601A12249B627E010712E80D800016E3ADF649DA0CDCE00.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.28520314042801388784606519505205:50001231000000:2800:C13E413ED8909995A0114FD858B3831466A9EA2537A412A8053979F18D0F29AA.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.77641457432503357856271117871551:50001231000000:2800:BF38C7BE5A4C22D06257B7E5D141112D63AC00E38B110075466E886F07B7B4E6.png?needInitFileName=true?needInitFileName=true)
更多关于Hyper-V安装请参考在 Windows 上安装 Hyper-V和Hyper-V 系统要求。
Windows x86模拟器卡在开机界面，无法进入桌面
查看本机CPU支持的指令集（如使用业界CPU-Z工具等）。模拟器需要电脑的CPU支持AES指令集，若电脑不支持则无法使用模拟器。
Windows X86模拟器启动后无法亮屏
问题现象
更新DevEco Studio后首次启动Windows X86模拟器，模拟器无法亮屏。
解决措施
建议清除模拟器中的用户数据后重新启动。关于如何清除用户数据，请参考启动和关闭模拟器。
模拟器使用物理键盘无法输入中文
问题现象
点击输入框后使用物理键盘无法输入中文。
解决措施
在X86或macOS(ARM)模拟器上点击输入框时会弹出软键盘，可以使用软键盘进行中文输入。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.75443257157753667838848581161194:50001231000000:2800:0CAA48DD6D10FE7B77E8A89251B073A26572C6FE626A4A50E1D1F4FF8E98E684.png?needInitFileName=true?needInitFileName=true)
启动模拟器，提示镜像文件缺失
问题现象
启动模拟器失败，提示“system-image文件缺失”或“The system-image file is missing.”，模拟器镜像文件缺失。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.30497410933084386684602876152706:50001231000000:2800:C61919414DEFF5E37A7859C8E0A671EA92FFBB55B56FD0879C94689399563EC1.png?needInitFileName=true?needInitFileName=true)
解决措施
请通过以下两种方式解决：
启动模拟器，提示SDK路径已更改
问题现象
启动模拟器失败，提示“系统识别到的新的sdk路径...”或“Sdk Path has been changed to xxx”，SDK路径已修改。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.84079658046715494119928881462011:50001231000000:2800:A961D9925DFF05887B2BD09822862462CA355C1003C00ECEFA942419B7B34607.png?needInitFileName=true?needInitFileName=true)
解决措施
可以尝试通过如下两种方式进行解决：
模拟器中如何管理应用的权限
进入设置>应用和元服务，点击对应的应用，即可管理应用的权限。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.16437952558496770284520012037496:50001231000000:2800:B6CA127979068BE1DF0536FDA847D4903A0BD09B5A79033556C40567A546736D.png?needInitFileName=true?needInitFileName=true)
在模拟器上运行应用，应用生成的文件在哪个目录下
问题现象
在模拟器上运行应用，应用的沙箱路径和真实的物理路径不一致，导致找不到应用文件。
解决措施
在模拟器中，应用的沙箱路径和真实物理路径存在对应关系，该对应关系和真机保持一致，具体可参见应用沙箱路径和真实物理路径的对应关系。
播放音频的过程中拔插耳机后，无法继续播放音频
问题现象
模拟器播放音频过程中，先拔掉USB接口的耳机，随后再将耳机插上，导致音频播放功能不可用。
解决措施
模拟器不支持耳机的热插拔，请不要在播放音频的过程中拔插耳机。如果插拔耳机后无法播放音频，请重启模拟器。也可以使用圆孔接口耳机来避免此问题。
模拟器上某些视频无法正常播放
问题现象
模拟器播放视频过程中，有时候会出现视频有声音无画面，或播放卡顿的现象。
解决措施
由于模拟器目前仅支持RGBA格式的像素显示，请确保视频解码格式正确。此外，由于模拟器只支持软件解码，如果视频解码器依赖硬件解码能力，也可能导致视频无法正常播放。
Windows X86模拟器使用过程中调整系统屏幕缩放比，模拟器显示异常
问题现象
打开模拟器，在Windows的设置选项中调整屏幕缩放比例，模拟器屏幕出现黑边，工具栏布局混乱。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.59765975791640602055644498169705:50001231000000:2800:20C1C460D85A62D056FEE444E74547366D3B6170B8875E6254326EF1FB390E69.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.18518132134930129428236945754125:50001231000000:2800:2A074FAF56A8D9A2A18D70BD32299D4EA538E7D91D082C8A75CDEEFAB0000DEC.png?needInitFileName=true?needInitFileName=true)
解决措施
手动缩放模拟器即可恢复，缩放方式参见移动和缩放模拟器。
模拟器中应用卸载失败
问题现象
当模拟器存储空间不足时，无法卸载应用，提示卸载失败。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.26469231557563053571391502247716:50001231000000:2800:F258EE25AAD011436F677A9C1294B385DC5E543E060516DB505C0AE7F5ABA243.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.61569855254189495102742573156343:50001231000000:2800:A69EB586D518A2B24E92950978FA99D3DC116FF2401002CC5BD0F0B562458F0A.png?needInitFileName=true?needInitFileName=true)
解决措施
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161818.21726762263383442575443240082248:50001231000000:2800:DEC700A11266D5D18C5D7299F4437C7D102ACC0BD1491A7815336886EB628CE0.png?needInitFileName=true?needInitFileName=true)
Windows电脑上启动模拟器，提示可申请内存不足
问题现象
Windows电脑上启动模拟器时，弹窗提示“当前系统可申请的内存不足”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161819.19540231457624548287362743229658:50001231000000:2800:CFDF27D275AB1620ABDFC7456A7F03A397FC0773FCB709427A8F5EAF087C2259.png?needInitFileName=true?needInitFileName=true)
解决措施
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161819.15030557889097248991725102743785:50001231000000:2800:8940CDE1C8ACA186EA4DAE9A905B62679DF3C97636D4D733B2129A7A618027D4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161819.64773442565751261770595687616074:50001231000000:2800:7896FF27AEB53FC6D3313525B4448A814C1AB2D270D8786AF74BD5F79D541EF6.png?needInitFileName=true?needInitFileName=true)
设备管理获取模板数据、下载模拟器镜像，提示网络异常
问题现象
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161819.87544405150263010535408493260380:50001231000000:2800:36FFFB079405CE313E90617CB39C3746455BF15F17BF505A23A8E93EF75C52C1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250217161819.84758163794508575326223703155956:50001231000000:2800:8F4844D979F3AB325DBA2E126E1582C13524CADCB43B159A7DA3B7854E7C811C.png?needInitFileName=true?needInitFileName=true)
解决措施
尝试修改本机网络环境后进行重试，例如：设置代理、连接手机热点。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-app-V14
爬取时间: 2025-04-30 08:10:32
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-device-V14
爬取时间: 2025-04-30 08:11:07
来源: Huawei Developer
DevEco Studio提供了丰富的HarmonyOS应用/元服务调试能力，支持JS、ArkTS、C/C++单语言调试和ArkTS/JS+C/C++跨语言调试能力，并且支持三方库源码调试，帮助开发者更方便、高效地调试应用/元服务。
HarmonyOS应用/元服务调试支持使用真机设备、模拟器、预览器调试。接下来以使用真机设备为例进行说明，详细的调试流程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150708.75241694495358792875529102311920:50001231000000:2800:1D094618345332B9D51B2D6F8E269321312A43F60652D5F8189A4DD60EE886E5.png?needInitFileName=true?needInitFileName=true)
使用预览器调试的特别说明
使用真机或模拟器进行调试时，修改后的代码需要经过较长时间的编译和安装过程，才能刷新至调试环境。使用预览器进行调试，可快速地修改代码和运行应用，在DevEco Studio中直接查看修改后的界面显示效果。
开发者可以使用预览器运行调试Ability生命周期代码和界面代码，预览器调试支持基础Debug能力，包括断点、调试执行、变量查看等。
预览器调试使用约束：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-run-debug-configurations-V14
爬取时间: 2025-04-30 08:11:41
来源: Huawei Developer
设置调试代码类型
点击Run > Edit Configurations > Debugger，选择相应模块，设置Debug type即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150708.46854966134770458436914293171975:50001231000000:2800:8D1E4958ADA97FF28AF7130131712DEEC0BDDC8F6C2CD1F166E5AF7FAD8451F9.png?needInitFileName=true?needInitFileName=true)
| 调试类型  | 调试代码  |
| --- | --- |
| Detect Automatically  | 新建工程默认调试器选项。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。  |
| ArkTS/JS  | 调试ArkTS代码调试JS代码  |
| Native  | 仅调试C/C++代码  |
| Dual(ArkTS/JS + Native)  | 调试C/C++工程的ArkTS/JS和C/C++代码  |
调试类型
调试代码
Detect Automatically
新建工程默认调试器选项。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。
ArkTS/JS
Native
仅调试C/C++代码
Dual(ArkTS/JS + Native)
调试C/C++工程的ArkTS/JS和C/C++代码
设置HAP安装方式
在调试阶段，HAP在设备上的安装方式有2种，可以根据实际需要进行设置。
-  从DevEco Studio 4.1 Canary2版本开始，支持当代码无变化时，不进行推包安装。即根据模块有无变化来判断是否重新推送安装模块包，在运行调试时仅将有变化的模块及依赖它的模块重新推送安装至设备上。如entry依赖了HSP模块，当HSP模块有变化，运行调试时将同时推送安装HSP模块和entry模块。
设置方法如下：
单击Run > Edit Configurations，设置指定模块的HAP安装方式，勾选“Keep Application Data”，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
从DevEco Studio NEXT Developer Beta1开始，默认勾选“Keep Application Data”。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.46874826179242825875926023843710:50001231000000:2800:50BFF8972B07C45C563694D2F6341D349D14734FC850F7CBE816C5EFE71251A0.png?needInitFileName=true?needInitFileName=true)
配置自定义调试参数
如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在“Installation Options”和“Launch Options”下进行配置。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.55198169284364993932128525492468:50001231000000:2800:915EDBA04C41B1387569A23F1433581070D2C684E77770E55CC17C25C816DFCF.png?needInitFileName=true?needInitFileName=true)
-  您可以在工程中添加ExtensionAbility，如需了解开发ExtensionAbility，请参阅ExtensionAbility开发指导。 如果您的工程中包含ExtensionAbility，可以选择Specified Ability，在Ability指定您希望调试的ExtensionAbility进行调试。
-  您可以在工程中添加ExtensionAbility，如需了解开发ExtensionAbility，请参阅ExtensionAbility开发指导。 如果您的工程中包含ExtensionAbility，可以选择Specified Ability，在Ability指定您希望调试的ExtensionAbility进行调试。
-
-
-  您可以在工程中添加ExtensionAbility，如需了解开发ExtensionAbility，请参阅ExtensionAbility开发指导。 如果您的工程中包含ExtensionAbility，可以选择Specified Ability，在Ability指定您希望调试的ExtensionAbility进行调试。
-  您可以在工程中添加ExtensionAbility，如需了解开发ExtensionAbility，请参阅ExtensionAbility开发指导。 如果您的工程中包含ExtensionAbility，可以选择Specified Ability，在Ability指定您希望调试的ExtensionAbility进行调试。
-
-
-  您可以在工程中添加ExtensionAbility，如需了解开发ExtensionAbility，请参阅ExtensionAbility开发指导。 如果您的工程中包含ExtensionAbility，可以选择Specified Ability，在Ability指定您希望调试的ExtensionAbility进行调试。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.86331049628941989357620219282213:50001231000000:2800:D541446BB728BA4E8D57F321CD5B54912182F50A28E8899F0A3879B43913C7F7.png?needInitFileName=true?needInitFileName=true)
-
-
-  您可以在工程中添加ExtensionAbility，如需了解开发ExtensionAbility，请参阅ExtensionAbility开发指导。 如果您的工程中包含ExtensionAbility，可以选择Specified Ability，在Ability指定您希望调试的ExtensionAbility进行调试。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.02840417175949494207904549131953:50001231000000:2800:78646C5F113424A66EC9FFAAE90162F1CB8FCD5BCBD7EE241E182B1BF4D4B241.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.77733622936764565095686689547399:50001231000000:2800:2995DAD6857A4C7F9D06574868AF155E53BCD508FFD9D34BE3806548A356C84B.png?needInitFileName=true?needInitFileName=true)
配置环境变量
如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可在“Environment Variables”下配置环境变量。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.72362204460724104828716190494744:50001231000000:2800:CEF5C7C47D73C37D3853D1B47B1370F55883873E38A3D83D97FD87FFAB6AC1A4.png?needInitFileName=true?needInitFileName=true)
点击按钮，新增一行配置项。当前支持以下配置项：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.43155288187792149718075999317647:50001231000000:2800:6D9CD524AA2041F84768CDBF6E876113E7459C75E7659E3CF2961BE0332A28FF.png?needInitFileName=true?needInitFileName=true)
当配置Environment Variables后，“Keep Application Data”覆盖安装不生效。
环境变量配置完成后，需确保环境变量已勾选，勾选后点击Apply才可生效。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.16501478992934382200501483348211:50001231000000:2800:0F85A5110AE9DE2FC3144F0FBFAE2DDC57AEC62B914B81256DC4EE832B0BDB15.png?needInitFileName=true?needInitFileName=true)
开启异常检测
如需开启异常检测相关能力，请点击Diagnostics。当前支持Runtime Sanitization，勾选Address Sanitizer表示启用ASan功能，具体请参见ASan检测。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.48663514991739663955909008687959:50001231000000:2800:E49CA6D9112755EC9CF621A80DA3D5E4726E39E36AB8F775BC396A5EC33466ED.png?needInitFileName=true?needInitFileName=true)
多模块调试
安装多个模块
如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在Deploy Multi Hap中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。
从DevEco Studio V3.1 Release开始支持。
设置方法如下：
单击Run > Edit Configurations，在Deploy Multi Hap中，勾选Deploy Multi Hap Packages，选择多个模块。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.41308927654300331847825376962796:50001231000000:2800:DF5C52A01ECA1E46E2C74DA85D5FA19D7B046FBEA3C4435C0B97F7B9691514B4.png?needInitFileName=true?needInitFileName=true)
自动安装依赖
如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以设置Auto Dependencies，启动调试时会自动将所有依赖的模块都安装到设备上。
从DevEco Studio 4.1 Canary1版本开始支持。
设置方法如下：
单击Run > Edit Configurations，在General中，勾选Auto Dependencies。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.92936411478128800187346285553724:50001231000000:2800:850E508EAB6EB80A950E14CBCF7E364EAFD661918DEDB439D56CE1E704AD44CC.png?needInitFileName=true?needInitFileName=true)
在Before launch窗格中，您可以点击添加应用启动前的任务。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.80081799904756899146905679014962:50001231000000:2800:DF5A9B4BDC5514E4F4830EB16267C2BAF7B15A02320020E4D3EB8197ABDACE19.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.70567336433681735528119278564394:50001231000000:2800:C7EA5F9C77DB41501C68E225BC7CC38E4FA9D6795605563B1DCC37D19662BE03.png?needInitFileName=true?needInitFileName=true)
也可以点击移除任务。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150709.36475356186216259109907951227787:50001231000000:2800:D41CED8B03E4F5DA2B9D6AC81B15F42A22CDFBD1268AD5B1F0A42F48FDDC9B23.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.57274944429814596211673935029177:50001231000000:2800:DAEA03D82AD7ECFA6D7ED82FBFC813B42E868AAACC3B0FE8D1FED5DA915E29E0.png?needInitFileName=true?needInitFileName=true)
在勾选Auto Dependencies后，可以同时勾选Deploy Multi Hap Packages，从而达到推送所有包的效果。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-code-debugging-V14
爬取时间: 2025-04-30 08:12:16
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-V14
爬取时间: 2025-04-30 08:12:50
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-debug-V14
爬取时间: 2025-04-30 08:13:25
来源: Huawei Developer
可以按照如下方式启动调试会话。
1.  设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2.
3.
4.  或者在工具栏中Run中选择Debug。
5.  如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.27459483259131506284695201190578:50001231000000:2800:C2DC21EC32CAF309DF39AFA114879BFD28E4376D5EEF667986586658BD83AA1D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.19924653427166815143640685638255:50001231000000:2800:A429EDB6DDFE632F57D5C335422A6EDEEB320F0E2ACEF54BCE57481733CCE8B1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.51319274641979668359282352220525:50001231000000:2800:E8EA8586444E00856704054D30A11BEFF9FF0CAA637CF4AFD9FF39438CA03D7A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.27646183820612542209619127669601:50001231000000:2800:F6C5CD00A359AA088698C327B9BCFC4450B265C8D3FAC8FC0D3344A7CAEA607D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.14234036224494841376828796488297:50001231000000:2800:F8B940E81FA4DB8D1CA51968856A9DB9A7850936C5DD86972997C84291BCFD2C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.63197009497407103646789269218816:50001231000000:2800:23DBBE20C02F5119780E354714C438ABBB60E6E5D71A4742E268457FA2CB3FF6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.43951076805479816800557349294728:50001231000000:2800:6C3415C218F87EF2748FD420D365E0FBBCC420F08188253D9C7E2019F7CE7073.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-attach-V14
爬取时间: 2025-04-30 08:13:59
来源: Huawei Developer
开发者也可以通过将调试程序attach到已运行的应用进行调试。
Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。
前提条件
当前设备上被attach的应用代码和本地代码一致，且已提前进行构建生成必要的sourcemap文件。
使用约束
attach不支持的场景：
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.67198702487865936959616449025144:50001231000000:2800:58505CC59DFC3C656FD20A309B14854B083D004D21B4E9C6BDE32F335CA2E51B.png?needInitFileName=true?needInitFileName=true)
操作步骤
1.
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.63833829854604098396650255261916:50001231000000:2800:AFEAD6819D17584FD9966D5D6B133FD119C27E152C5D9485CA6F68CC1C6F865F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.79355349412331429876561162789231:50001231000000:2800:01106571D2506116BD2E949D59670AB61D7677784080965BF2CEBD2D7FD6E8B8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.82941340669376951088562004700378:50001231000000:2800:5556C63F3CA07E1C30BB4C4912E9FBA43D07C3AC9C57B2D65E83128195602ADB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150710.69193213875752032930024305189594:50001231000000:2800:212A36A168954C174748A09B96EF03A2B8ED9FD7D81FB5ED8AFA3A2F4CC657A2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.63915190552882430730602222439794:50001231000000:2800:A9A59E29729BE82DCAB302FD065F8DB7FB282FE9011C867ED2E668C55B25914B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.26778246165152725977369912890547:50001231000000:2800:1A823588C4E44BBA7B1BF196A13DBCDE16DEC63063A33CBF200D34533F2EE0B1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.97268440107508084871486399492688:50001231000000:2800:6C1F4275D292200B4C97D62B74ADE2AC29F1459FBF3C9C2590718EDE49CA9C8E.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-attach-to-process-V14
爬取时间: 2025-04-30 08:14:33
来源: Huawei Developer
开发者可以通过将某个应用设置为“等待调试模式”，然后当开发者需要对应用进行调试时，拉起应用即可快速进入调试。
操作步骤
1.
2.  此时会在DevEco Studio底部显示一个等待进度条，在应用被拉起之前，将一直处于等待状态。可通过进度条右侧的取消按钮进行取消。
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.50467809097121075301617112011391:50001231000000:2800:03F7B0CB31DBF19AC949D86DD184EED6FA8AAC106EDC11DEB722AB59A14F8F23.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.94937722564317353284947920966744:50001231000000:2800:870FD8F94A9C1F1E328EF423F4CC98C591C627CACD1D15468DCCE985460DD173.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.37806393977100004926769401102491:50001231000000:2800:274473BD242073955F5AE605119CE9B950295AD49E50F8622E591406ED46827F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.53753309928277428579747821623458:50001231000000:2800:6A44E712A0FF11565E33D5EF211CD9728088983AF31421F5CBDE0D5C46CCC837.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.90388705846393313859566170128995:50001231000000:2800:6ECA0073912B7CE1087C99436BAC9AE2F189A1539E68CA7E051E10639DC8AF79.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-breakpoint-V14
爬取时间: 2025-04-30 08:15:08
来源: Huawei Developer
DevEco Studio ArkTS支持行断点和异常断点，这些断点可以触发不同的操作。
行断点
行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，您可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。
异常断点
异常断点会在应用执行时发生异常的地方暂停应用。
行断点
如需添加行断点，请按以下步骤操作：
1.  当您设置断点时，相应的代码行旁边会出现一个红点，如图。 在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅会在满足特定条件时才会暂停应用。
2.  当应用运行到代码处，会在代码处停住，并高亮显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.98673930679183061227692793027376:50001231000000:2800:F33531773DCC5CA53F72ADAFD88CB9B3C1A6AB59E01B511C5314A41908E43F09.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.54810300089430998311271388294391:50001231000000:2800:056F03CFC0CCEB8E1D9C02F60F6802637982F0A50FBD6641505692A2F5A42943.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.02498023273891334046627751416690:50001231000000:2800:69FBAD37C649FFC45A4BBC6EE2B7963A8D2EE65C061659FB0C0F9F0835A60C77.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.10799766843966808794405635363042:50001231000000:2800:906E9729F5262C7C6CA7BF91E4C4A98CCDF51EEB7ADC56608FF1CEA14076944E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.66700738983056970728213565902170:50001231000000:2800:B83C4B4A4C83EFC5B191362AEEC511AA7EF35D957D64133923C2174C4825511C.png?needInitFileName=true?needInitFileName=true)
异常断点
在BreakPoints中，勾选ArkTS/Js Exception Breakpoints，开启异常断点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.96010684992879259050097903874188:50001231000000:2800:ED88356C14A4D82AEA086ECA7330B95A6BD9175C335D2820A295CCDE71D5AA43.png?needInitFileName=true?needInitFileName=true)
当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有标志，并展示当前Frames和Variable，以及错误信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150711.20307926683318927914682199389010:50001231000000:2800:9B46FDC23646925F1E0303B5D9C13744A20FFC281C6B5A079B033AD78451E898.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.02180366014024532197210211463663:50001231000000:2800:2EB06C0EBCD978DCE4B4C10AA80E34920B36AF9A139BD613847CFBAEFF9D1283.png?needInitFileName=true?needInitFileName=true)
断点管理
在设置的程序断点红点处，单击鼠标右键。然后单击More或按快捷键Ctrl+Shift+F8（macOS为Shift+Command+F8），可以管理断点。
或者在点击“Debug”窗口中点击View Breakpoints图标。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.96746903285375617432811704861067:50001231000000:2800:85955603672B93719D897938DCE15BDDA8168F7006A12F48A604C6795DAC1D39.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.91343253642282490697152538446619:50001231000000:2800:B91C85BBC5DDDE754D0ED51D681C742CC672C82FFFAB070B79346093C5B599A1.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-variables-V14
爬取时间: 2025-04-30 08:15:42
来源: Huawei Developer
当应用停止在某个断点处时，您可以在"Debugger"窗中查看当前的变量信息。当您在"Frame"窗格中择某个帧之后，您可以在"Variable"窗格中检查变量。此外您还可以通过对变量进行计算。
如需向"Watches"列表中添加变量或表达式，请按以下步骤操作：在"Watches"空格中输入表达式，然后点击Add to Watches 图标。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.51413147455298389603729297214970:50001231000000:2800:B0EC2F41C6EDEE306FC95C3228BCF37EBC9D34B04113AA1096EB91363A39E059.png?needInitFileName=true?needInitFileName=true)
如需从"Watches"列表中移除某一项，点击鼠标右键，选择Remove Watches。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.31911754298259248321391456562913:50001231000000:2800:5BA33894B39F30EC73830697B705BE5FDEE4D4102DEB678179DA0EC86BD2CF46.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-debugger-V14
爬取时间: 2025-04-30 08:16:17
来源: Huawei Developer
调试窗口
Debug界面有两个tab页，分别是“entry”和“entry(PandaDebugger)”。
通常第一个tab页“entry”用于展示推包安装过程。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.93456619142951363830716547705590:50001231000000:2800:C5E19336EF29907F52A7DFCAF808328797F76836A6EF09EA9D77ACA7EDDB08D8.png?needInitFileName=true?needInitFileName=true)
第二个tab页“entry(PandaDebugger)”是调试器，用于调试Debugger功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.19734572923314740888314363944945:50001231000000:2800:58F484C1FF9A19157CA33579666ECBDDB0A6EB9744BB0C657A5682F05054D6D7.png?needInitFileName=true?needInitFileName=true)
-  Debugger显示两个独立的窗格： 按钮 名称 快捷键 功能 Resume Program F9（macOS为Option+Command+R） 当程序执行到断点时停止执行，单击此按钮程序继续执行。 Step Over F8（macOS为F8） 在单步调试时，直接前进到下一行（如果在函数中存在子函数时，不会进入子函数内单步执行，而是将整个子函数当作一步执行）。 Step Into F7（macOS为F7） 在单步调试时，遇到子函数后，进入子函数并继续单步执行。 Force Step Into Alt+Shift+F7（macOS为Option+Shift+F7） 在单步调试时，强制进入方法。 Step Out Shift+F8（macOS为Shift+F8） 在单步调试执行到子函数内时，单击Step Out会执行完子函数剩余部分，并跳出返回到上一层函数。 Stop Ctrl+F2（macOS为Command+F2） 停止调试任务。 Run To Cursor Alt+F9（macOS为Option+F9） 断点执行到鼠标停留处。 代码进入add方法的定义处。
-
-
-  代码进入add方法的定义处。
-
-
-  用于展示已加载的ets/js。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.15630005227969985834927772898576:50001231000000:2800:102D4A3DC6785ED683D2911E1DD333A12AA59D86F225B097DD950FDA8CEA3A28.png?needInitFileName=true?needInitFileName=true)
| 按钮  | 名称  | 快捷键  | 功能  |
| --- | --- | --- | --- |
|   | Resume Program  | F9（macOS为Option+Command+R）  | 当程序执行到断点时停止执行，单击此按钮程序继续执行。  |
|   | Step Over  | F8（macOS为F8）  | 在单步调试时，直接前进到下一行（如果在函数中存在子函数时，不会进入子函数内单步执行，而是将整个子函数当作一步执行）。  |
|   | Step Into  | F7（macOS为F7）  | 在单步调试时，遇到子函数后，进入子函数并继续单步执行。  |
|   | Force Step Into  | Alt+Shift+F7（macOS为Option+Shift+F7）  | 在单步调试时，强制进入方法。  |
|   | Step Out  | Shift+F8（macOS为Shift+F8）  | 在单步调试执行到子函数内时，单击Step Out会执行完子函数剩余部分，并跳出返回到上一层函数。  |
|   | Stop  | Ctrl+F2（macOS为Command+F2）  | 停止调试任务。  |
|   | Run To Cursor  | Alt+F9（macOS为Option+F9）  | 断点执行到鼠标停留处。  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.09536682306690288870039803424346:50001231000000:2800:3ECE098097464551F53E8925EC99A5B320B78E45E4129D2F8D7309768926C393.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.19650466659775296404563217853064:50001231000000:2800:50204C0462E023408BD0F221E5FED4D5736B6DF49B2B52D88034CBF9EA65463F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.48192331691533527414267725930293:50001231000000:2800:89088332C07E3849A8E80420BADA5DF99FEF63F3F1BC8A960208EFD7E088D182.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.91018435118343872597981289821471:50001231000000:2800:F8F09896906CE97EE60528C2DBD91FC95E4FA231940769A2961458F10C5F237F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.91971672854184703786306377947484:50001231000000:2800:FF27E04AE51F9C35F4B5EDED0BA4BBEA1AE5EA386C8204263F1B736F3C1F2499.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.22133080654304301814903671272391:50001231000000:2800:C87ECCC9571EF277F98F800D119686A443973B08A044006E76F5B9E7A05DDD6C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.66012488700021458610884503577962:50001231000000:2800:AA8B1AC2D5FB540BE8AA723C4EDC8B4D62D2FFD5CB245E3D368B6D20890EAC72.png?needInitFileName=true?needInitFileName=true)
-
-
-  代码进入add方法的定义处。
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150712.76723978836952052627869102124857:50001231000000:2800:8C77F2E7BC5A680ADFD23F7471C9080C35394E3517CF7F0059A9267453CD564E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.68845420669868233532368541179331:50001231000000:2800:FEB703446294B2D5E3F88C0193FC53A31E4F68D35047F19130E41E5D054F0070.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.41391084699648178340823250292388:50001231000000:2800:58D98109A1C1329EB4F45A164E2DEBDA76262B980A5ACBB5F7F2F8D73E4DD0C9.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.31603151910046533215614746868416:50001231000000:2800:D842B6DFF1605438A6A41E4A441DA0D34E4C5BEBE5ECCF98E929CA5DD1EBD402.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.33365489053639246207070184594916:50001231000000:2800:1E778472245A47034E9CFC23E5A4AE1F52C8B62CC549E2083E5494049D953588.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.36286512907007965165658171078526:50001231000000:2800:BD8DF6E496FEDEC6AC43F9D52DEAF2EC7EE0DCE1E6DD864B92E53B15557DE1F2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.89625418279063664730579413698795:50001231000000:2800:0051698D99246E49907918776DB632E88D36D37294687801638E6796698A57E7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.18960064928311278100706747898612:50001231000000:2800:FF48227C8A43CE77F9133FB8D372F2292F306524110753526DF7C2A65FE9D362.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.00023286057190891183173662999802:50001231000000:2800:7C922E90011684A3DD311587A0801A6579C563A8B17149509800E984406CE32D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.13670128673703391774332637000094:50001231000000:2800:A701B846FBF2B7A1999548426754409BCCB96B8EC4E853C269513C8B3576AEA6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.12013723877923914374610893119085:50001231000000:2800:B0CED7F4946847F6C2100AABC16C92611EED3C1017D810E4524D8514253F0565.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.77397553900508695248341024472517:50001231000000:2800:C0D122B6F17FFAD46C5A44F7DE7412FF229BBC0CC8D46BA3E6D3584EE7540627.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.61688621356226615507933435838595:50001231000000:2800:08936A15E97DF1AB3D5CCE205BBD1D15CCDD1CE7F750BE489C4C54E87FA165B1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.01303502951224007527523150308209:50001231000000:2800:B63170709959C7DE64B6FC5D38CB0ECCD74C65FC1459DC5283E5DD8CC0CB6993.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-reverse-V14
爬取时间: 2025-04-30 08:16:52
来源: Huawei Developer
DevEco Studio提供了反向调试的能力，供开发者进行调用栈回退，当前仅支持ArkTS调试模式。
程序中断时，在调用栈窗口右键单击，选择Restart Frame，可以回退到上一个调用栈。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.92990195585097571645060697958633:50001231000000:2800:05AE8F279B4FFC6358404A0492EE2163A725800AA0FCC2C891BE92BAE1002221.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-extension-V14
爬取时间: 2025-04-30 08:17:26
来源: Huawei Developer
开发者可通过两种方式对Extension Ability生命周期函数进行调试。
等待调试方式
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.08059949707588132434082528367687:50001231000000:2800:15778F607D445CDA26AA2A0C76AE74E72F1E83E8D66D179A80C94CF900221995.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.30364638826366288742430476626223:50001231000000:2800:B17881F6D277835189D59756DD951B1335B4F34D272BB258E913ED0E20B8B9F9.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150713.80572355607468899543420277728796:50001231000000:2800:2F06B28AD372F183DF4A3F6DD945F121B7C6C7F98856FD678738B909E88A47A6.png?needInitFileName=true?needInitFileName=true)
修改运行配置方式
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.54592197321831188794119693720536:50001231000000:2800:A3E733A25F49C18A81121483B941507A351944713DB817CD9F5A001D0E0497D4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.75292364506652394838890796182706:50001231000000:2800:FA3DFA26DFF89A7F62DF7C857F0A5EC758C1A72A08E5A346604846251F095873.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.42851990567006126387004969487869:50001231000000:2800:8836BD2D7EB6D4A5D437F28C8AD796AE9258E1C337A175D087F9305FE5B3C54B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.11987934331196746647663204389184:50001231000000:2800:690FAB3932679EA29CCFE3F8B8E42AF346AC0619A8FD90C69B2CD0FC4C803E2F.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-worker-taskpool-V14
爬取时间: 2025-04-30 08:18:01
来源: Huawei Developer
开发者可通过在worker或taskpool代码上设置断点，对worker/taskpool进行断点调试。
worker 调试
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.29368582202654167491078660193235:50001231000000:2800:586535E3B23259EE503D12F637D5D29E10828B352378BDB22D5580C4B2AB25A4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.34515495797964237561342914838314:50001231000000:2800:26387A04DD08A06441D63530B9581F51308BA53F57AEB5AED6C4CD95279287B6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.43000479716706277940783547993181:50001231000000:2800:73C23B64FF6AEA1C8E5F506464A98C23A44179CE7277E79E433694D052F7A192.png?needInitFileName=true?needInitFileName=true)
taskpool 调试
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.32962569558623439844296490564388:50001231000000:2800:BCFDE1E58B1EB4305BED2820082F0982706ED8F79696D8DBA1EADD073AF0E806.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.20856790028701707097474277591314:50001231000000:2800:3FD9FEE62F3F2A2486BC5A95F2BD7F27A2DBF57B296D9D4EDEDC1DED2D1CB203.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-evaluate-log-V14
爬取时间: 2025-04-30 08:18:36
来源: Huawei Developer
开发者可以通过 Evaluate and log 能力在代码执行到断点行时打印开发者指定的表达式。
操作步骤
1.
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.21152065731601371637319654755230:50001231000000:2800:33039686BF81EF1A7DB5CF3EB696A330C3C522E71175AE376E268F9B469E78D4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.23577974983734453586434294675120:50001231000000:2800:FF10A8FE168A8A167FECF659BEEA5EFA2491C97DB2AA1415E0967BD0DB68BAA6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.42618345216447671998867215613766:50001231000000:2800:E82944F35401FBC1696C7B99E11761D5AFE75FAEC727B8977C24DA4DAEEB4172.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.34674146415344680139069384450210:50001231000000:2800:BA00E12E7DED7B556C184F6A2D5C93D83866A71D576E22E22939E4AEF4C9895D.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-arkts-smart-step-into-V14
爬取时间: 2025-04-30 08:19:10
来源: Huawei Developer
当编辑器上一行存在多个函数嵌套或调用时，开发者可以通过Smart Step Into的能力来步入到想要调试的函数内，如果在调试时想跳过某些文件，也可以自定义需要跳过的文件列表。
智能步入
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.24819904419498284725935622480992:50001231000000:2800:C5C9702FBA3C01465266B174661665609F9D3B171BD31FAF78E1CA1EA47D11E7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.10690436969157781748573211356331:50001231000000:2800:A9C20B6B9F38579354E2C5FF3E0D7024F472E0ED4ABFE58E1C4122C5D6E191D2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150714.38850794837589004689866181276765:50001231000000:2800:7FCEDEA0CD6676A767428514954BD97E8E5F57CA8FC2AB3752F54AD8066CAB65.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.46488833458522576103888471140247:50001231000000:2800:339044B9FED17025BFD342943EDF4ABB3CF8330BC91FDB6A27DF8D3238BA0E57.png?needInitFileName=true?needInitFileName=true)
过滤脚本文件
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.78500736345432024242625340835349:50001231000000:2800:0A9349091A25E65AD4D70E727D61B8349AE843F776AF89FF839DF9741B96AC51.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.72188359766413565858416938164691:50001231000000:2800:BC1C7160A10D5A3CF7BC6EA40FD0818F9423F53DECC1AD4D24CC65C622CE32C3.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-V14
爬取时间: 2025-04-30 08:19:47
来源: Huawei Developer
Native代码调试依赖 LLDB 调试器，进行调试之前请确保已安装 SDK 中的 native 包。
新建模板工程
在DevEco Studio中，点击File > New > Create Project，选择Native C++创建Native应用模板工程。
开始调试
设备连接状态正常，开始调试。调试配置详细设置参考启动调试章节。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.97719129999925344265532418508906:50001231000000:2800:11751C0DFBF8AB066B7113B05030EFD6C6DD5418CAD3E958FD4B9E5EEE3F49D1.png?needInitFileName=true?needInitFileName=true)
设置断点
在相应代码行设置断点进行断点调试。断点详细使用方式参考使用断点章节。
程序控制
可以使用DevEco Studio上的按钮或快捷键在调试过程中进行程序控制。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.91228024323522623959005681856728:50001231000000:2800:556EB9D1CF9CC8DE1280E152787C5E5A295E39495DBE2A831D1D931E2C7450B7.png?needInitFileName=true?needInitFileName=true)
调试信息查看
每次停在断点或由于其他原因导致程序中断，在堆栈列表展示当前线程状态，在Variable变量列表展示变量值。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.24810122152925863729762984475773:50001231000000:2800:C51A6B9093F1073344600951A3C4DFAA41CACAB22604D167AA466600B8979887.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-enable-V14
爬取时间: 2025-04-30 08:20:25
来源: Huawei Developer
支持 debug 和 attach 模式启动调试，启动调试前选择对应的设备进行调试，可参考debug启动调试或attach启动调试章节。
在调试配置中将 Debug type 选择为 Dual (ArkTS/JS + Native) 、Native 或 Detect Automatically，在启动调试前进行配置并在下一次调试生效。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.20272868475027657613875016061924:50001231000000:2800:A65D31DF856C0CFE78D4156DDC421B834354A16EC30E72F2B952B87865C6C041.png?needInitFileName=true?needInitFileName=true)
查看静态/全局变量
在 native 调试配置界面中勾选“Show static/global variables in the Variables Pane”，调试过程中变量列表会展示静态/全局变量。
符号表路径
在 native 调试配置界面中的“Symbol Directories”页签，点击“+”，可以添加符号表路径。这里指的是带有调试信息的 so 库。例如，您可以先编译带有调试信息的 so 库，然后将其调试信息裁减掉，在设备侧运行无调试信息的 so 库，调试时将带有调试信息的 so 库路径添加在这里，可以实现对该 so 库的调试。
预设调试器命令
在 native 调试配置界面中的“LLDB Startup Commands”页签和“LLDB Post Attach Commands”页签中预设lldb命令。
在 “LLDB Startup Commands”页签中的命令会在 LLDB 调试器启动之后立即执行，在“LLDB Post Attach Commands”页签中的命令会在 LLDB 调试器成功 attach 到进程之后执行。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-breakpoint-V14
爬取时间: 2025-04-30 08:21:00
来源: Huawei Developer
点击View Breakpoints图标可以打开断点管理界面，您可以在断点管理界面查看或更改您的断点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.41931365765309611117759847160323:50001231000000:2800:CFF6BF9BEF18F2AF08928DE8AA828D0271FD7BF0DB1475075BFE2E156BABFF1F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.45607081999264548376577113286163:50001231000000:2800:051774A9FEA4C1BD43C6A2135414206012398F7638C98A629D30A1FA60B0D395.png?needInitFileName=true?needInitFileName=true)
条件断点
在某个断点的配置中，勾选 Condition ，并设置表达式作为条件，使程序运行到断点且满足设置的条件时才会中断进程。
日志断点
在某个断点的配置中，勾选以下类型的log，可以使进程运行到断点时在 console 窗口打印相应 log。
未勾选 Enable 的断点不会打印日志，未勾选 Suspend execution 的断点会打印日志，不满足所设置的 Condition 的断点不会打印日志。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.33962532031953422426074461395048:50001231000000:2800:39C2C76E0755D309BFED177ACA8F675C1AF48924F573C27C13346CD7516E586B.png?needInitFileName=true?needInitFileName=true)
临时断点
在某个断点的配置中，勾选 Remove  once hit，该断点只生效一次，生效后该断点会被删除。
函数断点
也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。
在断点管理界面汇总点击“+”->“Cpp Symbolic Breakpoints”，在弹出窗口中填写函数名和模块名（模块名可缺省），添加函数断点
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.42561636668361824047991518433205:50001231000000:2800:B4DB5F68181293D2BB314B0D6A8480BF26A6F721FD2E39DA9AEEBE10E7A71578.png?needInitFileName=true?needInitFileName=true)
异常断点
异常断点可以使程序运行到抛异常或捕获异常的代码处停住。
其他系统异常，如 SIGSEGV 等信号量异常会默认捕获并中断进程。
在断点管理界面中点选 “Cpp Exception Breakpoint” 下的 “Any exception”，勾选 Enable 使能异常断点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.17048858079190673158266000821496:50001231000000:2800:C257DEB743C61687E785D46E9A4799DAE272C2CFBAFF0EB107B059EE7C915D4F.png?needInitFileName=true?needInitFileName=true)
数据断点
支持三种类型的数据断点，即变量被读、被写、被读写时中断进程。
在变量列表中对某一个变量右键，在菜单中选择添加数据断点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.99630013626840161621639645160379:50001231000000:2800:2BC95078CEE479D4B05BD0F7848EAFE5BFD9FB11C4BEED8FB16F700AAFBE205A.png?needInitFileName=true?needInitFileName=true)
在断点管理界面进行查看和修改。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150715.62619923614664100112766218114362:50001231000000:2800:8FEE00DD33B7A818E71378CDF5CF261E13EE0E1822FC130304A8C84BFC12D322.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-variables-V14
爬取时间: 2025-04-30 08:21:35
来源: Huawei Developer
调试时，在“Variables”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。
查看全局/静态变量
点击“Edit Configrations...”打开调试配置，在 native 调试配置界面中勾选“Show static/global variables in the Variables Pane”，调试过程中变量列表会展示全局/静态变量。
Simplify STL
在菜单栏点击“File > Settings > Build, Execution, Deployment > Debugger > C++ Debugger”，通过勾选“Display STL variables as visualization in the Variables Pane”在变量列表中展示简化后的 STL 变量值，或去掉勾选以展示其原始结构。
变量监视
通过在 Watches 页面点击 “+”，或在某个变量右键菜单中的“Add to Watches”添加监视的表达式，在每次程序停住之后会计算表达式的值。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.73661505190273446284888821881788:50001231000000:2800:12CF16AD78F71C278622B72FCC324F49B43D9714971D532C78AAC30C2BA68104.png?needInitFileName=true?needInitFileName=true)
表达式求值
通过点击“Evaluate Expression...”按钮，或Watches 页面中的输入行中，输入表达式进行计算。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.86204319851179578057789133178780:50001231000000:2800:DEB335A87B19C54C1040478A1FF17DE1B6B8A7A6FD37C07C29FD64B76253959D.png?needInitFileName=true?needInitFileName=true)
查看十六进制视图
在“Variables”页面点击鼠标右键，弹出框中选择“Show As Hex Values”，此时页面中的整型变量会以十六进制进行展示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.86109912230316393885497843618064:50001231000000:2800:8A1AE69FA14B13945AD1AD084DAE2B5E9194E98B3B5B95C01B14B3337404C0C6.png?needInitFileName=true?needInitFileName=true)
查看函数返回值
当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.66666974225063970068668960228943:50001231000000:2800:86D6871BE067A5CFB0F1334D4BE45C73B313F5EF503B9AAA4B391CBCF3D8538B.png?needInitFileName=true?needInitFileName=true)
其他说明
对于特性类型的变量，还支持查看bitmap预览、查看较长的字符串等功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.97804354031455778068586080956565:50001231000000:2800:9177812B950DAC52144EAD608F1D7F70BE9685C1A1E71F7C20E6DFEA0983D7BA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-disassembly-V14
爬取时间: 2025-04-30 08:22:09
来源: Huawei Developer
支持查看汇编和汇编代码调试，此外，当程序中断到没有源码的位置时（如 stepin 到一个没有调试信息的函数中），DevEco Studio 会打开汇编视图，让您了解程序当前停住的地址及对应的汇编码。
汇编视图
在某一个堆栈处右键，在弹出菜单中选择“Disassemble Frame”，可以查看该栈帧对应的汇编码。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.15341708690363176204887280508594:50001231000000:2800:0BE72ADA0B80C94B56B819BE33F8EC9FEB4B72C071F9BAD099ACA7E02785F97A.png?needInitFileName=true?needInitFileName=true)
支持在汇编视图中展示源码、函数名，可以跳转到对应源代码，汇编视图如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.19269553571316787434082672529498:50001231000000:2800:2C58E9F29890346D36FE6A8DB2F23332B4712DB1B6FF8F9A587A609BBD20B244.png?needInitFileName=true?needInitFileName=true)
汇编断点
可以在汇编视图设置断点，程序运行到对应地址时中断。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.37595585340804242916023748039361:50001231000000:2800:7153EE23F6F640BA62C642C761A4591D8BB12E300BB53A1906368DB7968A4089.png?needInitFileName=true?needInitFileName=true)
单步调试
汇编视图下，单步按钮默认以汇编指令级别进行单步调试。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.31183767234816452788731099586759:50001231000000:2800:8E3D71D9402030AC6E37C98F0DE77F4B04DCFB5B558F9B751C5E16488B9B3BA0.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-memory-view-V14
爬取时间: 2025-04-30 08:22:43
来源: Huawei Developer
在 native 调试窗口中，点击“Layout Settings”，勾选 Memory View ，打开内存查看窗口。
查看指定地址内存
在内存视图中，填写地址，点击“view”按钮，查看对应地址处的内存。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.85830781969499579057369026902271:50001231000000:2800:EFB7F1761DFB678E9F61D5AB393DB39398DFDC59E053C08F905D21160D2F2ECB.png?needInitFileName=true?needInitFileName=true)
点击“Settings”按钮，设置进制、偏移量和内存数量。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.23541349457778936919681786183937:50001231000000:2800:5D258B94BF8E495BD19EE29D28A46BB3EF6E5B089906E8DA34C239776A7F298F.png?needInitFileName=true?needInitFileName=true)
内存转换
通过点击某一个内存格子，右侧会动将内存内容转换成各种类型的值。您也可以按住并拖动，从而选中多个内存格，以显示这部分内存的 ASCII 码转换结果。
查看变量内存
在“Variables”变量列表中的某一个变量处右键，在弹出菜单中选择“Inspect Memory”，自动跳转到内存视图展示变量存储地址处的内存。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.04774924680885895093269655997760:50001231000000:2800:9528DB3F7454C9C5858987CDB40E46EA88675F45A67A52D8974A96DB5D0EBEE5.png?needInitFileName=true?needInitFileName=true)
内存修改
您可以在内存格上双击，键入您想要修改的内存来修改对应地址处的内存值；您也可以在右侧的数据转换结果框中输入数据，从而修改该数据对应类型的长度的内存值。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-lldb-V14
爬取时间: 2025-04-30 08:23:17
来源: Huawei Developer
在调试过程中，您可以在 native 调试窗口的 lldb 页面中执行 lldb 原生命令。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.63837505828350636618195929285111:50001231000000:2800:2D8E58E31603B367C7C8915811775AABE5B34E13A67EE56BB85947F354D3EB2E.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-reverse-V14
爬取时间: 2025-04-30 08:23:52
来源: Huawei Developer
针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。
反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：
前提条件
在File > Settings > Build,Execution,Deployment > Debugger > C++ Debugger设置界面，勾选Enable time travel debug开启C++反向调试开关。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150716.21642633423623201489991815990510:50001231000000:2800:BB004B201C6B7887B411E835D92ECDC028620002BFA877110E823C8809F602A5.png?needInitFileName=true?needInitFileName=true)
操作步骤
1.  需要查看历史调试信息时，点击“Open Time Travel Debug”按钮进入反向调试模式，您可以在此模式下进行调试。 其中，操作按钮说明如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.72692510354058511162943438108517:50001231000000:2800:BE7679A76BACC569DABCCF9328B733F2AE642A05D49C23EC8F90BD15ABDFF83B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.56365420377926360741127866894734:50001231000000:2800:D5FF9619140DD58AB1B13F7F7F8DF6B373F044213D4AFDDC99833959441479A7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.26873759166663400836697617057999:50001231000000:2800:C9C2B1938110AFC97E44EDEA1BCD267DFCA588832C994584AA13930D951897B3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.19929952108038410780859690600396:50001231000000:2800:EA04D659D8418E8C1D8E18D524EA9D1F7C070A164EDEE4F472CB0660486735E7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.50389677474699549688045527740859:50001231000000:2800:1492BBB61C981C417074B2273AA6C22916AD3A1617F043639AE55B640BBF1EC4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.35243002639543313307240735541585:50001231000000:2800:F63FFB68B62D1D982D944EB04D5ECA0B598A7219CFC1BC6601C39A864AE73F06.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.49299570956852557290007341839632:50001231000000:2800:16E8E40DD7EB77EC9E6141189F7F82AAAC0A99993EB871A661DE1353DB7CCD6C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.14928681358479909577567982191177:50001231000000:2800:D921627014DFFE09ACF2DC62254773BF4DDB81AB50B5C6D4095516B01359EDB3.png?needInitFileName=true?needInitFileName=true)
某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-parallel-stacks-V14
爬取时间: 2025-04-30 08:24:26
来源: Huawei Developer
在native调试窗口中，点击“Layout Settings”，勾选Parallel Stacks，打开并行栈视图。
在程序停住时，并行栈视图可以同时展示多个线程的调用栈信息，合并重复调用栈，帮助您更好地理解程序的并发执行情况，以及发现潜在的多线程问题。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.78166748585901794679977535317202:50001231000000:2800:32FE49353E87BAF2E6C281DC782A3C644E1B3BF5A89DF3703B1B1F5EB91E8188.png?needInitFileName=true?needInitFileName=true)
调用栈跳转
您可以在视图上对某一个调用栈双击来跳转到对应堆栈，Frames页签中会随之跳转，此时可以查看该堆栈的变量等信息。
线程信息查看
在多个线程合并的位置处鼠标悬浮，可以显示这些线程的具体信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.48048672002047150855785359782403:50001231000000:2800:0B5A0A20AE51357FB30B36D3B745070705586025D417E17CFB21783B7F1FDAEC.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-so-V14
爬取时间: 2025-04-30 08:25:01
来源: Huawei Developer
在native调试窗口中，点击“Layout Settings”，勾选Modules，打开模块视图。
在native调试期间，“Modules”窗口会列出并显示有关应用使用的so信息。点击各属性可按升序/降序来排序，支持升序和降序；支持字符串匹配搜索。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.86004967671211799339687480716235:50001231000000:2800:6443C995E0064B8F51D25C4D5E608BDC703F38D48580C2CD658958ABD99B0EE7.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-native-exection-point-V14
爬取时间: 2025-04-30 08:25:35
来源: Huawei Developer
开发者可以通过“设置执行点”在调试会话期间跳转到编辑器中的任意代码行，并在对应位置设置执行点，跳过当前位置到目标位置之间的所有代码。
此操作适用于线性和非线性执行路径，用于中断和跳过循环，或者在if-else子句表达式或switch-case语句中选择另一个分支。例如，如果要检查另一个分支而不重新启动调试会话，可使用该功能。
操作步骤
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.36117787737703089933496479106735:50001231000000:2800:6A7BDE3721CC01091895062443607D3412678D4D8E6284973683AE8725A1D283.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150717.80388957917381778172740715693527:50001231000000:2800:E68A52AAAF2C84CF4369FE6C65A5B42228E2882144D73C89A9A66C2F2852C898.png?needInitFileName=true?needInitFileName=true)
使用“设置执行点”时，仅修改了程序计数器的值，未修改其他寄存器的值，这可能会导致不可预知的错误，例如：
此外，还有一些其他不符合预期的问题，例如变量值错乱、堆栈信息异常等。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-smart-step-into-V14
爬取时间: 2025-04-30 08:26:10
来源: Huawei Developer
进行C++调试时，当前代码行有多个函数调用时，开发者可以使用Smart Step Into功能直接Step Into到其中某一个函数的实现中
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.71286115216694415227188670562310:50001231000000:2800:CE7282E9E040B5071C9044DDCADF69003C4D644690DD55CDD0970FD5741B7B1F.png?needInitFileName=true?needInitFileName=true)
操作步骤
通过点击调试窗口“entry-Native”调试器下的Debugger窗格中的按钮（或使用快捷键Shift+F7）触发Smart Step Into功能后，DevEco Studio会将当前代码中可以进行跳转的函数进行高亮显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.05994898339490644687448177949789:50001231000000:2800:2A13F79CA81CE394FCBB37973C275436ECB1FF0F3A6D894B7388A474E776DB71.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.86793859544135111209027488359698:50001231000000:2800:36468697C4F136E64574C42C86AE11C8113AF70C99C1A7C64BFDCF0F4F7901FD.png?needInitFileName=true?needInitFileName=true)
开发者点击需要跳转的函数，程序会运行到目标函数的实现内。
已经执行完毕的函数不会高亮显示。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-cross-language-debugging-V14
爬取时间: 2025-04-30 08:26:44
来源: Huawei Developer
DevEco Studio支持C++和ArkTS的跨语言调试，可以同时调试这两种语言。整体操作体验与单一语言调试一致，无需额外在对应语言去手动添加断点，避免了在此过程过多的手工操作，提升了使用两种语言混合开发的调试效率。
开启跨语言调试
1.
2.
3.  ArkTS调用C++方法之后的代码存在断点时，点击Resume可以回到ArkTS断点的代码行，继续进行Arkts代码调试。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.54066259176559659991870784710719:50001231000000:2800:32E3F46FFDC0DC56CA815B7946AB5FE156DB360D53D309FFF056C4D4BB90474F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.39461518744549382637352276757534:50001231000000:2800:9C48BA409725CAC11418DB09C94876AA967BE46B8CE0EC0A433B9E41704DE596.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.85393252624571547386828251191399:50001231000000:2800:DEFE494AD8406B4938991AF3A7562B39FF559C6BD0DAB18FB0FDF42CC6EB3159.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.72098088227245637930746521645288:50001231000000:2800:D5CC8D1782EF24A6CD6363968ECC320FE74AE0FB2C489A4669BA67A57688A696.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.82280898154989060886450041627651:50001231000000:2800:0E604F1556BB7281A82C7B8831559F916F9B47C8921210FD969FBFA4E136CC3C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-source-code-debugging-V14
爬取时间: 2025-04-30 08:27:18
来源: Huawei Developer
三方共享包分为静态共享包HAR和动态共享包HSP，两种共享包的源码调试方式有所区别，具体请查看以下指导。
HAR源码调试
HAR包的引用存在两个模式，对应的源码调试也有差异：
-  源码调试：关联本地模块源码进行调试，此时在对应module源码上进行调试。
-  源码调试： 如果工程依赖了远程仓库的HAR包，本地也有相应的源代码，可以通过修改前缀配置进行attach调试。 如下图所示，工程依赖了远程HAR包（也可以是本地的HAR包）。 此时可以在Run/Debug Configurations中通过如下配置来进行attach调试。 点击Run > Edit Configurations > Debugger，点击，填写remoteUrl和localUrl。 remoteUrl和localUrl的获取方式如下： 由于本地HAR工程不会产生sourceMap，所以需要一个入口。通常是新建一个工程，将HAR的源代码作为本地模块进行依赖。 然后build工程生成新的sourceMap，打开sourceMap并找到本地源码的key值前缀，该前缀即为localUrl。 启动attach调试，在debug窗口获取程序加载时的前缀，该前缀即为remoteUrl。 配置完成后，再进行attach调试，此时便可在源码中断点命中及打断点。
-  如果工程依赖了远程仓库的HAR包，本地也有相应的源代码，可以通过修改前缀配置进行attach调试。 如下图所示，工程依赖了远程HAR包（也可以是本地的HAR包）。 此时可以在Run/Debug Configurations中通过如下配置来进行attach调试。 点击Run > Edit Configurations > Debugger，点击，填写remoteUrl和localUrl。 remoteUrl和localUrl的获取方式如下： 由于本地HAR工程不会产生sourceMap，所以需要一个入口。通常是新建一个工程，将HAR的源代码作为本地模块进行依赖。 然后build工程生成新的sourceMap，打开sourceMap并找到本地源码的key值前缀，该前缀即为localUrl。 启动attach调试，在debug窗口获取程序加载时的前缀，该前缀即为remoteUrl。 配置完成后，再进行attach调试，此时便可在源码中断点命中及打断点。
-  如果工程依赖了远程仓库的HAR包，本地也有相应的源代码，可以通过修改前缀配置进行attach调试。 如下图所示，工程依赖了远程HAR包（也可以是本地的HAR包）。 此时可以在Run/Debug Configurations中通过如下配置来进行attach调试。 点击Run > Edit Configurations > Debugger，点击，填写remoteUrl和localUrl。 remoteUrl和localUrl的获取方式如下： 由于本地HAR工程不会产生sourceMap，所以需要一个入口。通常是新建一个工程，将HAR的源代码作为本地模块进行依赖。 然后build工程生成新的sourceMap，打开sourceMap并找到本地源码的key值前缀，该前缀即为localUrl。 启动attach调试，在debug窗口获取程序加载时的前缀，该前缀即为remoteUrl。 配置完成后，再进行attach调试，此时便可在源码中断点命中及打断点。
-
-
-
-  如果工程依赖了远程仓库的HAR包，本地也有相应的源代码，可以通过修改前缀配置进行attach调试。 如下图所示，工程依赖了远程HAR包（也可以是本地的HAR包）。 此时可以在Run/Debug Configurations中通过如下配置来进行attach调试。 点击Run > Edit Configurations > Debugger，点击，填写remoteUrl和localUrl。 remoteUrl和localUrl的获取方式如下： 由于本地HAR工程不会产生sourceMap，所以需要一个入口。通常是新建一个工程，将HAR的源代码作为本地模块进行依赖。 然后build工程生成新的sourceMap，打开sourceMap并找到本地源码的key值前缀，该前缀即为localUrl。 启动attach调试，在debug窗口获取程序加载时的前缀，该前缀即为remoteUrl。 配置完成后，再进行attach调试，此时便可在源码中断点命中及打断点。
-  如果工程依赖了远程仓库的HAR包，本地也有相应的源代码，可以通过修改前缀配置进行attach调试。 如下图所示，工程依赖了远程HAR包（也可以是本地的HAR包）。 此时可以在Run/Debug Configurations中通过如下配置来进行attach调试。 点击Run > Edit Configurations > Debugger，点击，填写remoteUrl和localUrl。 remoteUrl和localUrl的获取方式如下： 由于本地HAR工程不会产生sourceMap，所以需要一个入口。通常是新建一个工程，将HAR的源代码作为本地模块进行依赖。 然后build工程生成新的sourceMap，打开sourceMap并找到本地源码的key值前缀，该前缀即为localUrl。 启动attach调试，在debug窗口获取程序加载时的前缀，该前缀即为remoteUrl。 配置完成后，再进行attach调试，此时便可在源码中断点命中及打断点。
-
-
-
-  如果工程依赖了远程仓库的HAR包，本地也有相应的源代码，可以通过修改前缀配置进行attach调试。 如下图所示，工程依赖了远程HAR包（也可以是本地的HAR包）。 此时可以在Run/Debug Configurations中通过如下配置来进行attach调试。 点击Run > Edit Configurations > Debugger，点击，填写remoteUrl和localUrl。 remoteUrl和localUrl的获取方式如下： 由于本地HAR工程不会产生sourceMap，所以需要一个入口。通常是新建一个工程，将HAR的源代码作为本地模块进行依赖。 然后build工程生成新的sourceMap，打开sourceMap并找到本地源码的key值前缀，该前缀即为localUrl。 启动attach调试，在debug窗口获取程序加载时的前缀，该前缀即为remoteUrl。 配置完成后，再进行attach调试，此时便可在源码中断点命中及打断点。
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.22666980583779148107202648212503:50001231000000:2800:D1FDFB4390D4FD12BCDF40F14C154703B99C692E3208B22E73E01F4FF123927B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.23777382214184046040745717157054:50001231000000:2800:4EAFA5273BDD5A0627459FFC001868F5820955AE0715B6F452E8B10B3A87558B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.94520400228962712133370229275179:50001231000000:2800:ED6B05331E881F8AF5BCE0CD95087B75F4DC4DE0C7871638CD2B91B3EE742C70.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.22525712494494592997851890267005:50001231000000:2800:FF11B4BE2B07BFF717F09E6D77846AF402A84A27A83CBCE84D771ED20C98A6E6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.27894105413372461609545686139034:50001231000000:2800:1AEB42177806372315661021B692743C2ECC6F85D13A972615C828A0DEAFD5EF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150718.39924541438531610116231096508045:50001231000000:2800:249F38B810D8F4F76860141B3EE5B8263D34C7644330EF209A7FA238424696ED.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.78722745352247166253665288684495:50001231000000:2800:671296C4C72CD695C1F72DCA15A1C7B3AE42D057FC24BB3658BBBB0E2ACC5197.png?needInitFileName=true?needInitFileName=true)
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.88945597802741743088578138513646:50001231000000:2800:648A6470B63CC5AEFBC56EAFD9F11A1F5DB8B797F594E09006D4C2A14D7B1BD4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.89529899037329747704839812524557:50001231000000:2800:959A8AB59223DE3BBD5227146056B13FF3D861C8FC18EF11113A7E87C2FECF37.png?needInitFileName=true?needInitFileName=true)
字节码HAR调试
C++代码调试
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.29954760422345678444851097933952:50001231000000:2800:22386D986E71C6866E2841D622632E57D9E58FA1116972D8EC4B4FDF6E0999FA.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.72699717623248966316913472374770:50001231000000:2800:F2D4F5CC2A4A87479E8C817E2582A0043539E2CAFA0D8FFB5ED4E4A6040BC8AF.png?needInitFileName=true?needInitFileName=true)
ArkTS源码调试
HSP源码调试
如果要调试HSP源码，需要将源码置于本地工程模块下，以引用本地工程的module方式进行调试。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-incremental-debugging-V14
爬取时间: 2025-04-30 08:27:53
来源: Huawei Developer
对于大型应用来说，每次修改代码后需要重新构建、推包、安装，整个流程耗时较长。针对该场景，在DevEco Studio和命令行场景中分别提供增量运行调试功能，支持开发者在真机上调试应用时，修改代码后，会识别出代码差异，构建增量包，增量运行调试时只推送增量包，减少大型应用调试推包时间。
C++代码增量调试支持API Version 11及以上版本Stage模型的工程；ArkTS代码增量调试仅支持API Version 12及以上版本Stage模型工程的资源文件修改。
使用DevEco Studio增量调试
调试C++代码
1.  点击Apply Changes按钮后，DevEco Studio启动构建的增量构建任务，构建出增量包hqf。增量包构建完成后，将推送安装至设备。 当前增量运行Apply Changes功能，不支持新建和删除代码文件，不支持在代码中修改装饰器相关，不支持在代码文件中使用import新增引用文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.17449138247838222203373264915534:50001231000000:2800:DC1A88DA1BA43FA12B7B4C3E672419E149249D42C06DC130266F9F7AAA3A76C5.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.47348957537993277985207301063534:50001231000000:2800:26D398CC6135F96DB2FF2A5B44223F879A094E7BB6B41A8B140CB7D188F29941.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.60385041824732727502355768465160:50001231000000:2800:7BC06974B25559BFE9977F13FE17EE7B3512549B856DED834C1AC87433AC7E7C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.04151894253103997344426862777746:50001231000000:2800:4CADD9A5431397FFFBD9A28B6062E02FDA8B51F6B63A1C8E78274703D31619BA.png?needInitFileName=true?needInitFileName=true)
调试resfile资源
1.  当前对resfile资源的增量调试，仅支持代码中直接调用的资源文件。
2.  点击Apply Changes按钮后，DevEco Studio启动构建的增量构建任务，构建出增量包hqf。增量包构建完成后，将推送安装至设备。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.88130115839124506812273066496166:50001231000000:2800:82675A62244F195205DE0C1CE6B07E890DE926968F2534B1B695BBE2E77C21BB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.79663630605372809488805119239125:50001231000000:2800:BC8CE3593BB3EC27AD6E89AC71126EF541D9C2DC4A6957CBDB8A2538C967E318.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.20679622178423775928065180116824:50001231000000:2800:CBC3EE55A32FB920E11A369CE88DF3C3B49577380EACDB8CD3F86688C4495B33.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150719.76428773935824125228742058700167:50001231000000:2800:61AD7ADA5DAA794A9C0187EEC32DC89CDC20DBC4CE5DE4C360A923CF53BD3F09.png?needInitFileName=true?needInitFileName=true)
使用命令行增量调试（C++代码）
通过hvigorw构建hqf包
1.  关于命令行的使用指导请参考hvigorw。
2.
```shell
$ hdc shell mkdir data/local/tmp/99c24fdc44694c05be12491d0a48e139
$ hdc file send library-default-signed.hsp "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
$ hdc file send entry-default-signed.hap "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
$ hdc shell bm install -p "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
```
3.
4.
```shell
$ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
$ hdc file send library-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
$ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
$ bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
```
通过SDK工具构建hqf包
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.11044846043608577678848412688854:50001231000000:2800:3FE0C897794D121F408504EC4C8AD1BCA70D15CDA2EBD1F093B11AB41F97B36B.png?needInitFileName=true?needInitFileName=true)
1.
2.  可以从工程的build-profile.json5文件中获取到对应的签名文件。
3.
4.  --mode：打包模式hqf，必填。 --json-path：指定增量包信息patch.json，必选，参考步骤4。 --lib-path：指定希望构建打包的so目录，参考步骤2。 --out-path：指定输出hqf包路径。
5.  关于该命令中需要修改的参数说明如下，其余参数不需要修改：
6.
常见问题
在其他的开发工具中修改打包so库文件，无法使用DevEco Studio的增量调试功能
问题现象
如果开发者在其他的开发工具中修改打包so库文件，在使用DevEco Studio 4.1 Canary2版本的增量调试功能时，出现无法使用增量调试功能的现象。
解决措施
导致这个问题的原因是在DevEco Studio 4.1 Canary2版本上，对于超过16KB的Native文件，在命中其中的断点后，LLDB调试器会默认持有文件句柄，导致调试过程中无法修改保存该文件。
开发者可通过以下两种方式处理：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-debug-multi-process-V14
爬取时间: 2025-04-30 08:28:28
来源: Huawei Developer
开发者可通过修改编译构建配置项来让指定 Ability 以独立进程的方式运行并进行调试。
编译构建配置
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.75582706187208268661701567463186:50001231000000:2800:6B0B4C129F6353B656B81335EA9830A2C50066A5DA329519A966B10CCBB9143C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.51013360591269595447784653018136:50001231000000:2800:C9F207A154FDAB5FFBF3E512754A8515ED725AF3AF9289CE27EBEC6794DD0C45.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.07564164558680930835461754738510:50001231000000:2800:FE7067B8FE9B1F9F82B1BC9684E5AF16115DE6E2A5A228603B031F5170AFC69B.png?needInitFileName=true?needInitFileName=true)
调试
1.
2.  跳转到以独立进程启动的 UI Ability 时将会新启动一个调试会话窗口。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.67908147412198659235016982921745:50001231000000:2800:381236FB47EC627FF4FCD1894DF0DD17C8E6AE188EB68A379ECE4F873FA888F4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.89049013791558390817567072461991:50001231000000:2800:A98050413FC72D78A6BB92C62B987F3F2E0B24659BB908A4F30753F11287FBA1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.63972525396800037272203033511747:50001231000000:2800:B8FBF4394D7C5AE846E19CE4F4E53CBDF61C4F98C9D8C37665DFF0B4BC8A0AB0.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hot-reload-V14
爬取时间: 2025-04-30 08:29:02
来源: Huawei Developer
DevEco Studio提供Hot Reload（热重载）能力，支持开发者在真机或模拟器上运行/调试应用时，修改代码并保存后无需重启应用，在真机或模拟器上即可使用最新的代码，帮助开发者更快速地进行调试。
Hot Reload支持Stage模型的ArkTS工程，不支持ArkTS卡片相关工程，不建议在hotReload模式下执行与ArkTS卡片的相关操作。
使用约束
| 代码场景  | API 12  | 限制条件  |
| --- | --- | --- |
| UI代码修改  | 支持  | -  |
| UI相应事件  | 支持  | -  |
| 多文件修改  | 支持  | -  |
| 类/接口/枚举  | 部分支持  | @Entry入口文件内class成员函数新增不支持；@Entry入口文件内枚举修改不支持。  |
| 匿名函数  | 支持  | -  |
| Lambda函数  | 支持  | -  |
| 类继承  | 部分支持  | 继承类和被继承类都不可以放在@Entry入口文件内。  |
| 成员方法和成员变量  | 部分支持  | @Entry入口文件struct Index内成员变量、成员函数不支持。  |
| 闭包函数  | 支持  | -  |
| 闭包变量  | 部分支持  | 不支持@Entry闭包变量修改。  |
| import和export  | 部分支持  | 不支持import引入未加载的模块；只修改export default会导致热重载失效。  |
| 自定义组件  | 支持  | @Component自定义组件要放在非@Entry入口文件，使用import方式引入，且不能保留自定义组件热重载之前状态。  |
| 代码文件（新增和删除）  | 不支持  | -  |
代码场景
API 12
限制条件
UI代码修改
支持
-
UI相应事件
支持
-
多文件修改
支持
-
类/接口/枚举
部分支持
@Entry入口文件内class成员函数新增不支持；@Entry入口文件内枚举修改不支持。
匿名函数
支持
-
Lambda函数
支持
-
类继承
部分支持
继承类和被继承类都不可以放在@Entry入口文件内。
成员方法和成员变量
部分支持
@Entry入口文件struct Index内成员变量、成员函数不支持。
闭包函数
支持
-
闭包变量
部分支持
不支持@Entry闭包变量修改。
import和export
部分支持
不支持import引入未加载的模块；只修改export default会导致热重载失效。
自定义组件
支持
@Component自定义组件要放在非@Entry入口文件，使用import方式引入，且不能保留自定义组件热重载之前状态。
代码文件（新增和删除）
不支持
-
对上面表格的解释说明：
操作步骤
1.
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.75883558681431836204676294434433:50001231000000:2800:5E27855BD158820CFD044CDA78B713FF8C0754723356BB93DAFE522E6DCB182B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.03511285523742810719646926132715:50001231000000:2800:D4B7656D37486090689E5B3EA41EC0C1FBBE07B364B82233812CC678F601669F.png?needInitFileName=true?needInitFileName=true)
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.19763214648400886845497217837098:50001231000000:2800:AE7EA04833E992C69E973B58F81BAE5CEAA9FAE8416F0EA44440A638D0908073.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.29090476446772604270966646956834:50001231000000:2800:D306C1574AB65ADD70EE865887E0B3C16FD19A9BC99EA6EEAC3034CC393F5612.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.56619122712130919496821724887758:50001231000000:2800:45F12B4C31AC9A54275F308AC97BCA0322541B237E98B82B02370437872AB226.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-developer-mode-V14
爬取时间: 2025-04-30 08:29:36
来源: Huawei Developer
HarmonyOS系统上的“设置”包含开发者选项的界面，用于辅助HarmonyOS应用程序开发、测试及优化，面向开发人员提供商业发行版之外的功能（如API能力），提供更多的调试选项及能力；您可在该界面中通过配置选项来帮助您分析和调试应用，例如，您可以通过启用USB/无线调试进行应用调试、开启DFX稳定性相关选项获取更多应用的故障及性能信息、开启过度绘制等选项快速发现性能问题等等。
启用开发者选项
在Phone或Tablet上查看设置 > 系统中开发者选项是否存在，如果不存在，可在设置 >设备名称中，连续七次单击“版本号”，直到提示“开启开发者选项”，点击确认开启后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
禁用开发者选项
在Phone或Tablet上点击设置 > 系统> 开发者选项，关闭开发者选项开关，弹出提示框后点击确认关闭，设备会自动重启。
常规选项
调试
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.77738792475896893255467584871779:50001231000000:2800:47BEB31434D9B42E4403FEC6B61D1975A408B4C59377603398E30C7F2569E160.png?needInitFileName=true?needInitFileName=true)
DFX稳定性配置选项包括：
其他调试选项包括：
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.30906495052414438170048893007558:50001231000000:2800:2C3F98C23A66F632C0BCEAB1F5AB69491BE0782F14434FEE947A4D8D8616FCE9.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150720.14647630853658992033618081533966:50001231000000:2800:B71BCC4E36986DD8A6B05ECE2301E6F1FD882976250C179A39405AF5510A726F.png?needInitFileName=true?needInitFileName=true)
输入
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.67461679036313087376359251672200:50001231000000:2800:27C65FCE4831B9D81846072364DB8CBE5ECFFD91DF91980D504CF2A385588884.png?needInitFileName=true?needInitFileName=true)
绘图
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.03498755687111342529549477009685:50001231000000:2800:4851E3F3517EDF4D1A53B82B66291A006581A6D91FD13F4D7D3273729A52EBFD.png?needInitFileName=true?needInitFileName=true)
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.40831122495253392707879869644007:50001231000000:2800:A70914ACAF593EA80421296060EC09F03B2E29284F4327595E5D8890DD240190.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.34263850207970746597072956863658:50001231000000:2800:2D15A8CC1B4E4D6C25EEA2B1EFB0D08EE7E19D2021600D5063F055FB90E6F2C5.png?needInitFileName=true?needInitFileName=true)
应用

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-setup-hilog-V14
爬取时间: 2025-04-30 08:30:12
来源: Huawei Developer
打印日志请查看使用HiLog打印日志。
DevEco Studio提供了“Log > HiLog”窗口查看设备当前所有应用实时打印的日志信息。HiLog默认显示的日志为以下6个部分。
| 第一列  | 第二列  | 第三列  | 第四列  | 第五列  | 第六列  |
| --- | --- | --- | --- | --- | --- |
| Timestamp  | PID-TID  | Domain/Processname/Tag  | PackageName  | LogLevel  | Message  |
| 时间戳  | 进程ID和线程ID  | 日志标签  | 应用包名  | 日志级别  | 日志内容  |
第一列
第二列
第三列
第四列
第五列
第六列
Timestamp
PID-TID
Domain/Processname/Tag
PackageName
LogLevel
Message
时间戳
进程ID和线程ID
日志标签
应用包名
日志级别
日志内容
开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。
HiLog窗口左侧各个按钮的作用为：
：单击该按钮可以向上翻页，日志窗口取消自动滚动。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.91715655117753032693378116815139:50001231000000:2800:327C38B13BF1A11A5D30A8A89E2D27361B11F12F01888B5CBB5FF831B8F8F172.png?needInitFileName=true?needInitFileName=true)
：单击该按钮可以向下翻页，日志窗口取消自动滚动。如果翻页已到底部，日志窗口自动滚动。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.43665903489841588632697452817009:50001231000000:2800:364740563A6048DB2966FD5E680B08C7A2C816F2B901D0893819DEB93DC47E83.png?needInitFileName=true?needInitFileName=true)
：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.33530594753102820371777306048733:50001231000000:2800:8132F16E1AFD7EF8D86E98EE848BD6E3D62A4DD27C4CB2C3A6FD46CC27314004.png?needInitFileName=true?needInitFileName=true)
：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.73508182634912913996108860323438:50001231000000:2800:4DF10231CDF757FDC16DBE6538F99076DC942C85BC2D3BC7DD8A5A7D7AC60498.png?needInitFileName=true?needInitFileName=true)
：单击该按钮可以重新开启日志接收，会重新加载设备缓存日志。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.74086987860595571904063520919797:50001231000000:2800:F9A4FAA5A1DDAF695442495B1E429D2ED3B36294FDDA8E44B34FC658EC6DABBE.png?needInitFileName=true?needInitFileName=true)
：单击该按钮可以选择清空窗口日志或清空设备缓存。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.76247914217628519071402529899494:50001231000000:2800:74F3B52FE200F7234C6961D1389B9AECC1C077421A74D83914BCA3D544112F37.png?needInitFileName=true?needInitFileName=true)
:  单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.14074924793071896144616595736364:50001231000000:2800:11CA7A79EBABCEA42353497F687E5DDE0E8A14FD3BC2907E26F3FFF27F8DE432.png?needInitFileName=true?needInitFileName=true)
:  单击该按钮可以对当前选择的设备进行录屏，并保存在本地。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.47925586935862667572876892353396:50001231000000:2800:810D5B8D64C0BAE1A72CA5A6570127128D0D918DA5918F8C6657B1BB3D973311.png?needInitFileName=true?needInitFileName=true)
：单击该按钮可以保存日志缓存到指定文件（在线日志）或保存离线日志文件（离线日志）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.61708353520895826701122330219312:50001231000000:2800:CA09BC80958F99E4D2FC5DBEC858562849D1DD883AEE192651E46FAF9C5F53D5.png?needInitFileName=true?needInitFileName=true)
：单击该按钮可以自动选择和切换已连接的设备。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.12755816798860564835508804068940:50001231000000:2800:AFBDC75C88F6B56D6FF14FD25DFB487DC40E4368DE00E53BC0637D2DF5963692.png?needInitFileName=true?needInitFileName=true)
：单击该按钮可以切换日志视图以及自定义日志格式。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150721.13647485355008652351782952417201:50001231000000:2800:5A3BFA039129C25D891AC84A69500E6D29A9BB504C4DD6FF3ED62BDE29B0FCF7.png?needInitFileName=true?needInitFileName=true)
：单击该按钮可以关闭当前日志窗口。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.92663295427829826257056836552761:50001231000000:2800:7C1B3999F82E00F2B377F583EF82DD54F685CCC530D784B321CE8E43DAC8C819.png?needInitFileName=true?needInitFileName=true)
：单击该按钮可以跳转到HiLog日志相关的在线帮助文档。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.42066283843046918624988646507664:50001231000000:2800:7515BEB9AEBEAE23175F4AB944E9978A4FB0DD820C0B7785713D190A8A581C20.png?needInitFileName=true?needInitFileName=true)
过滤日志
按关键字过滤日志
在HiLog搜索框中输入希望过滤的信息，即可过滤显示所有包含此信息的日志。
按钮表示过滤是否区分大小写，按钮表示是否按照正则表达式匹配过滤。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.40857782985471810366556407029624:50001231000000:2800:466249CF71B9328DFAEDBD4381A6201C2BEF4361424B0E52093F94DBF0C35D09.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.46158090683671049490936625855950:50001231000000:2800:BF9863BE7B3749EBD426DE63DD58E12845B1B226A0629D6272CB4AD15FFC3B93.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.26653176395618123808825483860579:50001231000000:2800:5976BD0A5F270EB1C468F6F7FABEA0CAA62C3DB938686585B0B5FB95FFCF322C.png?needInitFileName=true?needInitFileName=true)
使用默认提供的过滤配置
HiLog提供多种默认的过滤模式，开发者不需要反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.35300886333668941903310333754575:50001231000000:2800:535B95FAD22CFA39397A3B7E66E684E4527C161F0CD474D9F882BB70AB855CFB.png?needInitFileName=true?needInitFileName=true)
当选择All logs of selected app或User logs of selected app时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。
由于设备启动时，USB调试开关没有开启，部分系统应用没注册上，Hilog进程列表无法显示未注册上的系统应用，如需查看此部分的日志，可以按关键字过滤查看，或者保持USB调试开关打开的状态，重启设备。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.03822128252546058754700719664736:50001231000000:2800:02A39E6396E4D5AB83B1D44C589464DCC1FB5B55180B1BA569E289DF7EB53924.png?needInitFileName=true?needInitFileName=true)
进程选择窗口可输入PID或应用名的关键字搜索要过滤的进程。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.91118542470439025418235556194421:50001231000000:2800:7315C04378DCEAF8FBF6DBE0980FA1377BDB687E5FA631A682153D2A3D6E519F.png?needInitFileName=true?needInitFileName=true)
按日志级别过滤日志
HiLog提供日志级别过滤以过滤某一级别及以上的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.97613347830785254846819466008994:50001231000000:2800:98770BBA9FF9FA9AD48BA496FE5D0AE6B051E0C8F5E6699114BF97F42C7F3F77.png?needInitFileName=true?needInitFileName=true)
如选择Warn级别，则过滤展示Warn级别与Warn级别以上的日志信息，即展示Warn、Error、Fatal3个级别。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.94662224280633435733118838104271:50001231000000:2800:9FDF5F2470A17A5372CAA24D9C96E061BD87F44BC992417A2D34ED4A14130CE9.png?needInitFileName=true?needInitFileName=true)
按自定义过滤项过滤日志
除默认过滤项外，Hilog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。
点击Config custom filter时将弹出自定义过滤配置窗口。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.66910231198219844902509513409984:50001231000000:2800:96AF22675FB8937C47D314B421C3506CE60A2B46D6CE3ECE12A1C204841D1F56.png?needInitFileName=true?needInitFileName=true)
先前介绍的过滤选项此处均可配置，同时增加了Package name和Set to all projects配置项。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.42229339218657560877621301959776:50001231000000:2800:17BF4E3BBD021F309BD349C291274276C658B4F979E192AE072E7137AE5A191B.png?needInitFileName=true?needInitFileName=true)
当配置完后将自动切换至此过滤配置。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.42098744271327510539345244525677:50001231000000:2800:9CB5CCA4461E09377E3E21BBFA6B47C4C446997F7F87C9DDC0A21A3EF88D4060.png?needInitFileName=true?needInitFileName=true)
切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。
自定义日志显示格式
开发者可以通过配置自定义格式，限制每条日志只显示用户关注的信息。
点击左侧图标，将弹出自定义格式窗口。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.41209581625050919340446870844124:50001231000000:2800:2BFF694A91B77638F5434B9DDEB0B6C3CC655E94B0AEBD824F5267074AE42A64.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.27984545833741827008339471140090:50001231000000:2800:6F6BDAA30152E8F75CA0CFA0F6A04073FBE91AC4E130136BDCC72B497D95B1B5.png?needInitFileName=true?needInitFileName=true)
在“Hilog Format”中自定义日志格式：
-  Format：Datetime/Time 显示日期时间/只显示时间。
-  Include thread id：是否显示TID。
-  Tag column width：domain/processname/tags列的最大宽度，超长信息将会缩略显示并以ToolTip形式显示完整信息。
-  Package column width：包名列的最大宽度，超长信息将会缩略显示并以ToolTip形式显示完整信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150722.43685151747690550605628696934921:50001231000000:2800:2E6588051B5C80325B702ABE5FF0033358C1030B7D86D6A6D2AEEE96A7CBA29B.png?needInitFileName=true?needInitFileName=true)
超长日志自动换行
当日志的消息过长时，日志窗口可能不能完整显示日志消息，需要拖动滚动条查看信息。此时开发者可以点击Soft-Warp按钮控制日志消息自动换行。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.14828467968034101257249670261647:50001231000000:2800:BC3015F2936A6312A690319820015D1B085622B543A72D5AB8CF781F110BADD7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.59468664301023837955612221248438:50001231000000:2800:363A8DC13ABEBCF93F9B960C344D2F58C15815D313A86E23E8CFCC996FA0A03A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.66485096986206053748077326653433:50001231000000:2800:BA2F1306533C1C459EB90FD6DB7D36482F97C97CC83B17ED36ABEB0E1EC20A77.png?needInitFileName=true?needInitFileName=true)
显示最新日志
设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击Scroll to End按钮使Hilog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.16250304840335474795342208961366:50001231000000:2800:ABA33FA56ECD864E7F01D270735DFD366138EA93A0E14139C7FD3B7DDC5CB0C1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.54838487488931654764750642956556:50001231000000:2800:79EF018C44923AAC12A7634FB97EF4C4DDCE11539559B64D6E6B2E8742C6067E.gif?needInitFileName=true?needInitFileName=true)
导出日志信息
用户可将经上述步骤过滤后的关键日志信息保存到本地，以便后续的进一步分析。
点击Export HiLog按钮，在弹出的Export HiLog To窗口中选择保存路径。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.89368333568297052701903396432878:50001231000000:2800:BCBB98F7351FF1B88850F66455CFF55A97F574D17DCD9362DEF33337FEE09B47.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.15117093143978543817150745845875:50001231000000:2800:BB79061DDE8BC91577FFB01CB16AA380CE8F45109DEF22F6E5A39EAB8E81429B.png?needInitFileName=true?needInitFileName=true)
清除日志缓存
与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。
HiLog显示日志信息的流程为：
点击Clear按钮，将弹出两个选项Clear Console Log、Clear Device Log。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.75376708061570296561015291742982:50001231000000:2800:954D10F38FA60BCDB7B080D9241CC3422E92D3A91645355EBB1745DB3AA5B3CE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.78803421228181620550128794083006:50001231000000:2800:805800AA44F1A57E3111C4A6C84757EE2760FEACCCB9A8FCA886931255DDF32F.png?needInitFileName=true?needInitFileName=true)
-  此操作只清空HiLog窗口缓存，Log组件将重新从设备端日志缓存读取日志消息，因而执行清除操作前已保存在设备端日志缓存的日志消息会显示到HiLog窗口中。
-  此操作将清除设备端日志缓存和HiLog窗口缓存。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.43605811499874638450994257674184:50001231000000:2800:35A3FFC4D540DA3E1D15B2EEB92B7A1B88E1984B0CF7BFFF1C797B55CB0CB101.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.82779541430245041733330470830509:50001231000000:2800:06BE489510B7D5A5EE66E4DD19FF124F27D885DF27736381B3BC58579E05EB19.png?needInitFileName=true?needInitFileName=true)
设置HiLog窗口缓存
HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。
点击Settings > Buffer，进入缓存设置窗口。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.57569302194120400195847336147225:50001231000000:2800:9E76CDD695C230849A1E16632A666A7C3DE0AA15205E33AE3E232778CF9B1C13.png?needInitFileName=true?needInitFileName=true)
默认缓存大小为4096K，变更缓存大小需重启HiLog窗口后生效。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150723.58444334392842083774748673073654:50001231000000:2800:ECD58590BD53B27BDDBFFD986F9877CECDDA47DF1BF98B33FE6DCC3E46850A80.png?needInitFileName=true?needInitFileName=true)
重启HiLog窗口操作：先点击下方的按钮，再点击上方的按钮中的Online Log即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.61779514276271268966396754859691:50001231000000:2800:0858FB4DE6F6ADABC2703A035960DB79F26C71FE4619C89B6959781B7FACF357.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.55745151656142844436234470498553:50001231000000:2800:19D68967E8C86A4F897789F14637648AA5D74A038E12CACA478B62E0C106D3A8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.36471211392541575433593395187371:50001231000000:2800:D4B9AE9C6227CFB5564F5DBAD88335F92994E111330B59B0707800DC7B94266D.png?needInitFileName=true?needInitFileName=true)
当日志量超出缓存时，顶部的旧日志不断被清除，因而顶部日志信息处于不停滚动的状态。此时若想查看此处的日志信息，可在窗口点击右键，勾选Pause Output暂停窗口打印，查看完后再取消勾选，重新开始打印日志。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.94134584080685282737600513699313:50001231000000:2800:86B652C201A99D0220E8245132B4C0F0263103A313791FE03975F70EFF9499B4.png?needInitFileName=true?needInitFileName=true)
设置设备端日志缓存
使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存，默认为256K。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.14401209687845014226924408188865:50001231000000:2800:766E1E3EB89566E2DB773957770855DCD648850EC584335093D348380123BD25.png?needInitFileName=true?needInitFileName=true)
使用hdc shell hilog -G命令可更改设备端日志缓存大小。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.94816815227080450719313679155308:50001231000000:2800:93B63FBCF2185520666A6A497DF3D7248638D7F1C4EC6CFA6A3261E0FD46DBBE.png?needInitFileName=true?needInitFileName=true)
配合-t参数可单独设置某一类型的日志缓存大小。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.39477465049012298876419587901710:50001231000000:2800:84BD935DFF60EF70C6DC167E3562BC2761982FE9F055EFE1523331FE5F2B63C3.png?needInitFileName=true?needInitFileName=true)
超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。
查看/导出设备离线日志
DevEco Studio提供查看设备离线日志的功能，支持查看设备中/data/log/hilog路径中的日志，离线日志窗口中展示的是经过解析和DevEco Studio格式化之后的日志。
点击HiLog窗口左上角New，随后点击Offline Log即可打开离线日志窗口。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.23266274570333082723268507095040:50001231000000:2800:7751A804B90755851845FA5D205834E220BA84AFFC30C5BA9B28709F0E68249C.png?needInitFileName=true?needInitFileName=true)
离线日志窗口左边工具栏中的按钮、日志级别下拉框和搜索框和在线日志的功能一致，设备下拉框仅支持选择真机和模拟器。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.89573225557473828459235300773805:50001231000000:2800:8C0CB0B06A6F8EB2F0056E41EDA4288467FF3ECBEFB64B105C949E15F897E7A8.png?needInitFileName=true?needInitFileName=true)
离线日志支持通过时间筛选设备上的日志文件，默认时间范围为打开窗口时的前三十分钟，除显示格式外，也支持通过键入yyyyMMddHHmm后回车进行时间输入。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.17745765101988467673714833570407:50001231000000:2800:0C142346A5CBF75B05D3189C1306B45FCAE9548D56D6EE9B8AC6C488D560FD06.png?needInitFileName=true?needInitFileName=true)
在输入时间之后，日志文件下拉框会进行刷新，点击文件会从设备端下载并自动解析后输出到离线日志窗口。
由于最新的日志文件内容还在更新中，在达到设定的大小前，内容会不断增多。如果重新打开离线日志窗口或者修改时间，日志文件列表都会刷新，会从设备端重新下载最新的日志文件，解析的内容会更多。
离线日志窗口能输出的文本量可参考设置HiLog窗口缓存进行设置，设置较小可能无法显示选择文件的所有日志，推荐设置6M(6144K)。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.38329094194151424197603813416607:50001231000000:2800:7C45BAB891DD4E7A33EFE6707342A6C5955BACC6B9B1E3D52D9F1C4FD0D9C764.png?needInitFileName=true?needInitFileName=true)
通过设置窗口的缓存大小可能无法展示完整的日志，可点击左侧工具栏的保存按钮导出离线日志，支持导出解析后未经DevEco Studio格式化的原始日志文件，导出的文件可以看到完整日志。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.54597952480419242198953319309920:50001231000000:2800:5D5E2B51F39864806816AB68B1CC72E806BA85690DC3415A7989EF98E87DD4D6.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-fault-analysis-V14
爬取时间: 2025-04-30 08:30:46
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-fault-log-V14
爬取时间: 2025-04-30 08:31:21
来源: Huawei Developer
当应用运行发生错误使应用进程终止时，应用将会抛出错误日志以通知应用崩溃的原因，开发者可通过查看错误日志分析应用崩溃的原因及引起崩溃的代码位置。
若需定位应用中的C++代码导致的内存问题如数组越界、内存泄露、释放已释放的地址等问题，需要在运行调试配置界面勾选Address Sanitizer以打开ASan功能再推包运行，具体请查看ASan检测。
FaultLog由系统自动从设备进行收集，包括如下几类故障信息：
调试模式（debug和attach）下，DevEco Studio会屏蔽当前工程的App Freeze和System Freeze等超时检测，避免调试过程出现超时检测影响开发者调试。
当前支持屏蔽的App Freeze故障类型：
当前支持屏蔽的System Freeze故障类型：
查看FaultLog日志
查看设备历史抛出的FaultLog日志
打开FaultLog窗口，将显示当前选中设备抛出的所有FaultLog日志。
FaultLog故障信息左侧按照应用/元服务包名 > 故障类型 > 故障时间结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.36517706571581117050147629915543:50001231000000:2800:8DB586D0B9EBF92B1E021B535E2BDD200C2A342FF9FFD85CEBCE997E06BEF926.png?needInitFileName=true?needInitFileName=true)
查看设备实时抛出的FaultLog日志
当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，开发者点击Jump to Log即可跳转至FaultLog窗口查看日志信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.01730660071938861175671458565403:50001231000000:2800:B5A7E383E155D779D0AD47C49FAE9F3F8DC065ECAAC19DA574DF5495C1FDFFAA.png?needInitFileName=true?needInitFileName=true)
跳转至引起错误的代码行
若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.90594487312133520962471218913195:50001231000000:2800:438A2783DE47082BCF20D7B2F27B1B9E0F02E90BA23CBEC6FF44A9C763213812.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150724.74879957979621597082544684824266:50001231000000:2800:EFDF32D0587E4301242E45AF21536AE69988B28954CF5F57F4D1F26E80F055B6.png?needInitFileName=true?needInitFileName=true)
导出日志
开发者可将当前显示的日志信息保存到本地，以便后续的进一步分析。开发者可根据需要选择保存当前选中节点的日志或保存所有日志。
-
-
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.60347399382845935422066198859671:50001231000000:2800:F288FC05A249937884F1B4DC610A6B3A2F95FAEE319FEFD33FA90EEB20B40582.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.28646036369705231845760037188737:50001231000000:2800:12A3121D69026A9FB363774897B86FC91CF45EA30986400ECEDFBE9F5043693F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.74437192756246619966818474131993:50001231000000:2800:5DF22F726769C1F6927F8DB154F75C54C95ABAA2BF6D0176125070B41D2A0A02.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.98544567064369897234598413934450:50001231000000:2800:671E1D0FB1244C20F9BBDEF536323D26F2A3288C4364B4FFE2A0E4966BD92F09.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-release-app-stack-analysis-V14
爬取时间: 2025-04-30 08:31:56
来源: Huawei Developer
对于发布的应用（Release应用），为减小应用程序大小，提高运行效率，会对代码进行优化，去除其中的debug信息。因此无法直接通过Release应用的堆栈信息定位到源码的具体文件和行位置，不易于开发者快速定位解决问题。
针对该场景，DevEco Studio提供了Release应用堆栈解析功能，开发者可以利用构建产物中包含Debug信息的文件（so文件、sourcemap文件、nameCache文件等），对Release应用中C++堆栈、ArkTS堆栈以及ArkTS堆栈中混淆的方法名和文件名进行还原。
Release应用堆栈解析功能操作方法如下：
1.
2.
3.  如果当前工程不是堆栈所在应用对应的工程，则需要配置应用对应构建产物：勾选Unscramble stack trace, 在下方的文件选择框中，分别添加应用对应的sourcemap文件、so文件以及nameCache文件，点击Start Analyze进行转换。 DevEco Studio将解析后的堆栈信息显示在右侧的输出框中。 在构建Release应用时，so文件是默认不包含符号表信息的，如果需要在构建Release应用时生成包含符号表的so文件，需要在工程的模块级build-profile.json5文件的buildOption属性中，配置如下信息： 如果引用release Har包中native方法产生了异常堆栈，解析时请勾选Unscramble stack trace, 并选择har模块中编译出的带有符号信息的so文件，引用方build产物中的har模块so不带有符号信息。so文件在模块中相对路径为build/default/intermediates/libs/default/{cpu类型}/libxxx.so。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.72693266349421744494710320539104:50001231000000:2800:FB1DEBA9A91FE3D118604C7855635BCC863CC721850E4A9F0024E9EAE7EB7685.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.08104946018910149782742396681749:50001231000000:2800:7F943315968506D5C2379CFEF29E18D6F4E7A14557DE0C47C3FD50D5DB9CAFCA.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.72262549051098129319048972355448:50001231000000:2800:FF1339E9EF1E7F973DBC07DB729D0AFAEDE9848E28F2A0D925ED01FBCE4B5999.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-exception-stack-parsing-principle-V14
爬取时间: 2025-04-30 08:32:30
来源: Huawei Developer
构建产物介绍
ArkTS调试产物sourcemap
release模式编译产物，产物位置：{ProjectPath}/{ModuleName}/build/{product}/cache/default/default@CompileArkTS/esmodule/release/sourceMaps.map
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.44765079721359971653354821805739:50001231000000:2800:3F4D0EC3B42C066904273FDE4163B67C09D4FEC3FC083F8F75BBA75CB34B09BA.png?needInitFileName=true?needInitFileName=true)
C++调试产物debug so
带debug信息的so数据，产物位置：{ProjectPath}/{ModuleName}/build/{product}/intermediates/libs
配置方式请参考release编译带debug信息的so。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.70244390387367127082177522624592:50001231000000:2800:0C3C5927C0B7F4202DBC1A862FB00A1605B7E76B0DB59B0363B7803CC0945A7D.png?needInitFileName=true?needInitFileName=true)
代码混淆产物nameCache
反混淆映射表，release模式编译产物，产物位置：{ProjectPath}/{ModuleName}/build/{product}/cache/default/default@CompileArkTS/esmodule/release/obfuscation
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.13394156432152534416401937478156:50001231000000:2800:B4824C8AF994EA18C086B097777B53DEA088FD3D39A055490377089A258C5940.png?needInitFileName=true?needInitFileName=true)
C++堆栈解析原理
编译选项差异
release编译带debug信息的so
通常release的so会经过strip，strip后的so中的符号表、调试信息会被剥离。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.28209398482886463477770058634670:50001231000000:2800:A47D8E39A54222CA7E979E1BE41863E67903FC6F540C00ACFCFEF09ECB16FFA2.png?needInitFileName=true?needInitFileName=true)
若需要保留so文件中的符号表、调试信息，需要在build-profile.json5的buildOption/externalNativeOptions中配置参数："arguments":"-DCMAKE_BUILD_TYPE=RelWithDebInfo"。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.07466098810386916164557173876010:50001231000000:2800:0F6AC1D67FDD2DE3AB9A10515C22364B1A402F627638C3D0250BE2502C8D997D.png?needInitFileName=true?needInitFileName=true)
C++堆栈解析流程
llvm-addr2line（获取llvm-addr2line工具）是将函数地址解析成文件名或行号的工具。
给出一个可执行文件中的地址或一个可重定位对象中的偏移部分的地址，使用调试信息来找出与之相关的文件名和行号。
常用参数：
| 参数  | 用途  |
| --- | --- |
| -a  | 以十六进制形式显示地址  |
| -C  | 将符号名解码为用户级别的名字  |
| -e  | 设置需要转换地址的可执行文件名  |
| -f  | 显示文件名、行号和函数名信息  |
| -F  | 显示函数名及文件行号  |
| -j  | 读取指定部分的偏移量，而不是绝对地址  |
| -p  | 每个地址信息单独占一行  |
参数
用途
-a
以十六进制形式显示地址
-C
将符号名解码为用户级别的名字
-e
设置需要转换地址的可执行文件名
-f
显示文件名、行号和函数名信息
-F
显示函数名及文件行号
-j
读取指定部分的偏移量，而不是绝对地址
-p
每个地址信息单独占一行
参考示例：
查看文件名、行号和函数名相关信息：
查找指定的地址所对应的代码位置：
例如：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.30839356926246252820015531141508:50001231000000:2800:5800DE4A38103AFBC184C850195E0EDC80B488F748171BD6FDD8522792486C6C.png?needInitFileName=true?needInitFileName=true)
ASan堆栈解析：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.07747554880574198000066561779309:50001231000000:2800:25F87EA9D78E12D02FBCBD1CD1692B552261F28FB6F230333F478E91CFD80325.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150725.24331451440573880626424422135860:50001231000000:2800:098415D87666C2626420FC25CB4E2740DCEBE0501BAC3A1489FBE587852BAC36.png?needInitFileName=true?needInitFileName=true)
常见问题
-  每一个可执行程序都有一个build UUID来唯一标识。Crash日志包含发生crash的这个应用（app）的build UUID以及crash发生时应用加载的所有库文件的build UUID。
-  在DevEco Studio安装目录/deveco-studio/sdk/default/openharmony/native/llvm/bin下即可找到llvm-addr2line.exe。
ArkTS堆栈解析原理
sourcemap格式
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150726.25978965082379512455590492349362:50001231000000:2800:CD1C70B21596608B5290FF8FF0206EA94CCC1764E8512EB8192797AF1CBAF5A7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150726.65886817396588001583652749948896:50001231000000:2800:E85FE554185C297F6DAEA69FEA8F86D1161FB58D6121995C88CCA1F720D45164.png?needInitFileName=true?needInitFileName=true)
实际代码映射关系：
70->29
71->30
72->31
73->32
sourcemap结构：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150726.09860352648705955498652248873488:50001231000000:2800:87451C895008B297F9E1F8235B593774D4DBDA884BAAB72FBE5BBF53B161C7D4.png?needInitFileName=true?needInitFileName=true)
单个module构建产物sourceMaps.map为merge文件，实际包含该模块的所有文件的映射关系；每个json中key以编译构建产物的唯一路径作为主键，运行程序的abc中保留了对应的key信息，当运行时异常代码归属到该文件时输出信息为该key，sources为实际源码文件信息，用于异常堆栈还原源码；mappings为编码后的行列号映射表，每个文件有独立的映射关系。
sourcemap解析流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150726.82011855550487839838124724377119:50001231000000:2800:F0613B708C2F7F5677D2EB272F93646A5C971B9CC8D40CCA370FAB78AACC0ABD.png?needInitFileName=true?needInitFileName=true)
反混淆解析原理
代码混淆配置请参考代码混淆。
代码混淆产物介绍
混淆映射表：$ProjectPath\$ModuleName\build\$product\cache\default\default@CompileArkTS\esmodule\release\obfuscation\nameCache.json
```json
"obfName": "home/src/main/ets/pages/a.ts"
```
-  变量名分为两类：普通变量、类方法变量。 普通变量映射关系的格式如下： 类方法变量映射关系的格式如下：
-  开启属性混淆时，成员方法映射关系的格式如下： 未开启属性混淆时，成员方法映射关系的格式如下：
-  属性名映射关系格式如下：
代码混淆解析
异常堆栈如下：
1.  a.ts通过sourcemap还原为tool.ts。
2.  查看混淆映射表：$ProjectPath\$ModuleName\build\$product\cache\default\default@CompileArkTS\esmodule\release\obfuscation\nameCache.json 该字段的IdentifierCache与MemberMethodCache中保存了方法名混淆前后的映射关系，对应格式为："源码方法名:该方法起始行号:该方法结束行号":"混淆后方法名"。 源码方法名中的"源码方法名"代表上下级关系，故匹配后可以通过"#"保留最后名称。 第一条堆栈混淆后的方法名为"g2"，若存在多个"g2"则需要通过行号范围过滤，故利用上述字段对该方法名进行还原：
```json
"#testObfuscation:6:9": "g2"
```
```json
"#testObfuscation:6:9": "g2"
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-asan-V14
爬取时间: 2025-04-30 08:33:05
来源: Huawei Developer
为追求C/C++的极致性能，编译器和OS(Windows/Linux/Mac)运行框架不会对内存操作进行安全检测。针对该场景，DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。
使用约束
配置参数
ASAN_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等。常用参数请查看表1。
ASAN_OPTIONS支持在app.json5中配置，也支持在Run/Debug Configurations中配置。app.json5的优先级较高，即两种方式都配置后，以app.json5中的配置为准。
在app.json5中配置环境变量
打开AppScope > app.json5文件，添加配置示例如下。
在Run/Debug Configurations中配置环境变量
具体请查看配置环境变量。
| 参数  | 默认值  | 是否必填  | 含义  |
| --- | --- | --- | --- |
| log_exe_name  | true  | 是  | 不可修改。指定内存错误日志中是否包含执行文件的名称。  |
| log_path  | /dev/asanlog/asan.log  | 否  | ROM版本小于NEXT.0.0.68时必填，值不可修改；NEXT.0.0.68及以上版本不再需要该参数。  |
| abort_on_error  | 0  | 是  | 指定在打印错误报告后调用abort()或_exit()。 false(0)：打印错误报后使用_exit()结束进程true(1)：打印错误报后使用abort()结束进程  |
| strip_path_prefix  | -  | 否  | 内存错误日志的文件路径中去除所配置的前缀。 如：/data/storage/el1  |
| detect_stack_use_after_return  | 0  | 否  | 指定是否检查“访问被释放栈空间”的行为。 true(1)：检查。false(0)：不检查。  |
| halt_on_error  | 0  | 否  | 检测内存错误后是否继续运行。 0表示继续运行。1表示结束运行。  |
| malloc_context_size  | -  | 否  | 内存错误发生时，显示的调用栈层数。  |
| suppressions  | ""  | 否  | 屏蔽文件名。  |
| handle_segv  | -  | 否  | 检查段错误。  |
| handle_sigill  | -  | 否  | 检查SIGILL信号。  |
| quarantine_size_mb  | 256  | 否  | 指定检测访问指向已被释放的栈空间错误的隔离区大小。  |
参数
默认值
是否必填
含义
log_exe_name
true
是
不可修改。指定内存错误日志中是否包含执行文件的名称。
log_path
/dev/asanlog/asan.log
否
ROM版本小于NEXT.0.0.68时必填，值不可修改；NEXT.0.0.68及以上版本不再需要该参数。
abort_on_error
0
是
指定在打印错误报告后调用abort()或_exit()。
strip_path_prefix
-
否
内存错误日志的文件路径中去除所配置的前缀。
如：/data/storage/el1
detect_stack_use_after_return
0
否
指定是否检查“访问被释放栈空间”的行为。
halt_on_error
0
否
检测内存错误后是否继续运行。
malloc_context_size
-
否
内存错误发生时，显示的调用栈层数。
suppressions
""
否
屏蔽文件名。
handle_segv
-
否
检查段错误。
handle_sigill
-
否
检查SIGILL信号。
quarantine_size_mb
256
否
指定检测访问指向已被释放的栈空间错误的隔离区大小。
更多可配置参数请参见asan_flags。
使能ASan
可通过以下两种方式使能ASan。
方式一
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.50171067071450953798123604571044:50001231000000:2800:C243E25CF0A6683805150D27602496110D7B39DDC5D0BC47D40CC8D47BE2D4CE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.93465178813773711191550496242032:50001231000000:2800:19445F4E5D6882EA08643C3DD17442633FBCD21BFB06791569E0E3E9C9433DF9.png?needInitFileName=true?needInitFileName=true)
方式二
1.
```json
"asanEnabled": true
```
2.  在需要使能ASan的模块中，通过添加构建参数开启ASan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数： 该参数未配置不会报错，但是除包含malloc和free函数等少数内存错误外，出现其他需要插桩检测的内存错误时，ASan无法检测到错误。
```json
"arguments": "-DOHOS_ENABLE_ASAN=ON"
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153011.59228072804589615031752825194467:50001231000000:2800:6744871E94F8D6141AB022465D13DF57AFBCD660E495F22098E0036252FB8C70.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153012.37955529884005654038530250506995:50001231000000:2800:95A1DCD4B6FF62E0164D7FA13FCA980D46447614A7F44EA55E85832B32A0981C.png?needInitFileName=true?needInitFileName=true)
启用ASan
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153012.05467907181858212237647461477113:50001231000000:2800:DC25452A6DE237B9D64B73CDE79581E89704AB19D8D5EC887CD49F91B66FED3A.png?needInitFileName=true?needInitFileName=true)
ASan检测异常码
当前提供案例在debug应用中可产生ASan，release应用因为在编译构建期间会进行代码优化，不一定会产生异常。
heap-buffer-overflow
背景/原理
访问越界。
错误代码实例
影响/报错
导致程序存在安全漏洞，并有崩溃风险。
开启ASan检测后，触发demo中的函数，应用闪退报ASan，包含字段：AddressSanitizer:heap-buffer-overflow
定位思路
如果有工程代码，直接开启ASan检测，debug模式运行后复现该错误，可以触发ASan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。
如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。
修改方法
注意数组容量不要访问越界。
推荐建议
已知大小的集合注意访问不要越界，位置大小的集合访问前先判断大小。
stack-buffer-underflow
背景/原理
访问越下界。
错误代码实例
影响/报错
导致程序存在安全漏洞，并有崩溃风险。
开启ASan检测后，触发demo中的函数，应用闪退报ASan，包含字段：AddressSanitizer:stack-buffer-underflow
定位思路
如果有工程代码，直接开启ASan检测，debug模式运行后复现该错误，可以触发ASan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。
如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。
修改方法
访问索引不应小于下界。
推荐建议
访问索引不应小于下界。
stack-use-after-scope
背景/原理
栈变量在作用域之外被使用。
错误代码实例
影响/报错
导致程序存在安全漏洞，并有崩溃风险。
开启ASan检测后，触发demo中的函数，应用闪退报ASan，包含字段：AddressSanitizer:stack-use-after-scope
定位思路
如果有工程代码，直接开启ASan检测，debug模式运行后复现该错误，可以触发ASan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。
如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。
修改方法
在作用域内使用该变量。
推荐建议
注意变量的作用域。
attempt-free-nonallocated-memory
背景/原理
尝试释放了非堆对象（non-heap object）或未分配内存。
错误代码实例
影响/报错
导致程序存在安全漏洞，并有崩溃风险。
开启ASan检测后，触发demo中的函数，应用闪退报ASan，包含字段：
AddressSanitizer: attempting free on address which was not malloc()-ed
定位思路
如果有工程代码，直接开启ASan检测，debug模式运行后复现该错误，可以触发ASan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。
如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。
修改方法
不要对非堆对象或未分配的内存使用free函数。
推荐建议
不要对非堆对象或未分配的内存使用free函数。
double-free
背景/原理
重复释放内存。
错误代码实例
影响/报错
导致程序存在安全漏洞，并有崩溃风险。
开启ASan检测后，触发demo中的函数，应用闪退报ASan，包含字段：AddressSanitizer: attempting double-free
定位思路
如果有工程代码，直接开启ASan检测，debug模式运行后复现该错误，可以触发ASan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。
如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。
修改方法
已经释放一次的指针，不要再重复释放。
推荐建议
变量定义声明时初始化为NULL，释放内存后也应立即将变量重置为NULL，这样每次释放之前都可以通过判断变量是否为NULL来判断是否可以释放。
heap-use-after-free
背景/原理
当指针指向的内存被释放后，仍然通过该指针访问已经被释放的内存，就会触发heap-use-after-free。
错误代码实例
影响/报错
导致程序存在安全漏洞，并有崩溃风险。
开启ASan检测后，触发demo中的函数，应用闪退报ASan，显示reason为AddressSanitizer:heap-use-after-free
定位思路
如果有工程代码，直接开启ASan检测，debug模式运行后复现该错误，可以触发ASan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。
如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。
修改方法
已经释放的指针不要再使用，将指针设置为NULL/nullptr。
推荐建议
实现一个free()的替代版本或者 delete析构器来保证指针的重置。
Other categories
未知的错误类型，持续更新中。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-tsan-V14
爬取时间: 2025-04-30 08:33:39
来源: Huawei Developer
TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。
功能介绍
应用场景
TSan能够检测出如下问题：
-  数据竞争（Data Race）是指两个或多个线程在没有适当的同步机制情况下同时访问相同的内存位置，其中至少有一个线程在写入。数据竞争是导致多线程程序行为不可预测的主要原因之一。
-  TSan 不仅能检测数据竞争，还能检测与锁相关的错误：
-  条件变量用于线程之间的通信和同步，常见错误包括：
错误报告
当 TSan 检测到错误时，它会生成详细的报告，包括：
使用约束
使能TSan
可通过以下两种方式使能TSan。
方式一
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153012.19674397451367350169689459313134:50001231000000:2800:0970ACAB66845982E446EF32234FD1A0BE10A24F86C609D2C60E4106B15B844C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153012.70681997746751677329868559413152:50001231000000:2800:BFAC12A4D69446710B89EAEF59ED39ED7571BD1664A0B52D53061311C3F04AE4.png?needInitFileName=true?needInitFileName=true)
方式二
1.
```json
"tsanEnabled": true
```
2.  在需要使能TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：
```json
"arguments": "-DOHOS_ENABLE_TSAN=ON"
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153012.90047564367073403893146115804971:50001231000000:2800:FF5973ED91347BD7F1B3DB13B4BD372992C5D157160C64498CEB883EC5448139.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153012.30993806349027323039652736035748:50001231000000:2800:9A5D93FCE19B56A886F28FF6E6FF07FA86C59D3DB9D836941B551B3BC6001A1D.png?needInitFileName=true?needInitFileName=true)
启用TSan
1.  当前使用call_once接口会存在TSan误报的现象，开发者可以在调用该接口的函数前添加__attribute__((no_sanitize("thread")))来屏蔽该问题。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153012.35640738418058122419064848481420:50001231000000:2800:7043A3A8C7C96D9188D3FA39C9274EDEBA3AB46426D52B4E394A9B55D2918A3D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250208153012.79992724101716883926893417718560:50001231000000:2800:14FAFF6DD8E3A12643BF9526D9322B4EF4F0F1866D6FA5308E773381C3C3B2E7.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hwasan-V14
爬取时间: 2025-04-30 08:34:13
来源: Huawei Developer
HWASan（Hardware-Assisted Address Sanitizer）是一款类似于ASan的内存错误检测工具。 与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的清理。
功能介绍
与ASan相比，HWASan具有如下特征：
HWASan能检测到ASan所能检测到的同一系列错误：
和ASan相比，HWASan具有以下优点：
约束条件
使能HWASan
方式一
点击Run > Edit Configurations >Diagnostics，勾选Hardware-Assisted Address Sanitizer开启检测。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250207111608.15547479135468381990208394262272:50001231000000:2800:9BCFA17F9D3E4C83A80BA88B78A80729ECFDA8873DFBF89B77FEBB5B88F7035D.png?needInitFileName=true?needInitFileName=true)
方式二
1.
```json
"hwasanEnabled": true
```
2.
```json
"arguments": "-DOHOS_ENABLE_HWASAN=ON"
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250207111608.66603614763137494406820117827041:50001231000000:2800:DC2A168015FAB873842F88692A79EE2207887DAA88666512CAF8AFD1EB681DD7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250207111608.88843477898629194506048389391743:50001231000000:2800:C039F3AA130D29CD222D5B1650C85958278DA554C7E3FE754BA0210839E441A6.png?needInitFileName=true?needInitFileName=true)
启用HWASan
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250207111608.82911896212911728192620997572699:50001231000000:2800:9A844CF52DB2EEF97C2127228C8755739F68C9F4502EEB75C7D25974B780FE3E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250207111608.63193801082259365316596424013643:50001231000000:2800:01A97BE58B8E38259374E7142310F07D87D1E01F5E3208CFE32AB5F153F6EE20.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-multi-thread-check-V14
爬取时间: 2025-04-30 08:34:49
来源: Huawei Developer
方舟多线程检测
在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript本身是单线程的，对JS对象的任何操作都必须在创建该JS线程的原始线程上进行。如果违反了这一规则，就会导致多线程安全问题。以下是关于如何判断和处理这些问题的一些详细说明。
原理介绍
-  JavaScript是单线程执行的语言，这意味着它一次只能在一个线程上执行代码。任何JavaScript对象都只能在创建它们的线程上进行操作。
-  N-API接口直接涉及到JavaScript对象的操作。绝大多数N-API接口（约95%）只能在创建这些对象的JavaScript线程上调用。
-  多线程检测机制会检测当前线程和正在使用的JS虚拟机环境（vm/env）中的JS线程ID是否一致。如果不一致，就表明虚拟机环境被跨线程使用，存在多线程安全问题。
常见多线程安全问题
-  非JavaScript线程尝试调用N-API接口，可能会导致未定义的行为或崩溃。
-  一个线程尝试使用另一个线程创建的env（JavaScript环境），这也会导致多线程安全问题。
如何判断是否发生了多线程安全问题
其中，thread:3096 表示创建并拥有这个JavaScript环境的线程ID。currentThread:3550 表示当前正在尝试操作这个JavaScript环境的线程ID。
当前线程号为3550，而使用的JavaScript线程是由3096线程创建的，这表明虚拟机环境（vm/env）被跨线程使用，从而导致了多线程安全问题。
使用约束
方舟多线程检测通过命令行参数开启，点击桌面图标无效。
使能方舟多线程检测
可通过以下两种方式使能方舟多线程检测。
-  点击Run > Edit Configurations >Diagnostics，勾选Multi Thread Check。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.31107583541876239970037836893319:50001231000000:2800:346A85A3C6D0AD730BC3410F861489912FB382C4075E9C224B44E1F37D629760.png?needInitFileName=true?needInitFileName=true)
-  通过命令行开启。
启用方舟多线程检测
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.57384479425698032478893818399329:50001231000000:2800:684BADE18202CBC4ACB32FF4657766D06A97DDD1329D88DC80FDB7833B95039D.png?needInitFileName=true?needInitFileName=true)
方舟native模块加载异常信息增强
在进行ArkTs项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTs项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。
使能方舟native模块加载异常信息增强
可以通过以下两种方式使能方舟native模块加载异常信息增强。
-  点击Run > Edit Configurations >Diagnostics，勾选Enhanced Error Info。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.58870990167951457025040306551161:50001231000000:2800:5F3DB62F5D3D320B281CEC61658F75698A281AA74D8F66BF220D35CFD96C4C47.png?needInitFileName=true?needInitFileName=true)
-  通过命令行开启。
启用方舟native模块加载异常信息增强
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.16417610853937804105651843957415:50001231000000:2800:0200F82FCCE283BCEE69EB61F202489ADD0D620723FDCAE85A1D357D810BC19A.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-arkui-inspector-V14
爬取时间: 2025-04-30 08:35:24
来源: Huawei Developer
开发者可以使用ArkUI Inspector，在DevEco Studio上查看应用在真机上的UI显示效果，并通过查看多次操作后的界面状态，快速分析定位UI界面存在的问题。
ArkUI Inspector支持的功能包括：
使用场景
针对界面较复杂的应用：
使用约束
操作步骤
1.
2.
3.  点击，勾选组件树信息的配置项Show Tree Statistics，可显示组件树节点信息。
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.43151814858647181669202795260623:50001231000000:2800:8D1308C3B7676D72FFAC4CB064E4BACF929C39C3745B470AAECC043557DB1882.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.56946859685680925633471663433056:50001231000000:2800:9EFB311C45302D77E19E401A590E26A62FD597545D83E14A78838E258ED0B453.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.30185978011326151276634972775644:50001231000000:2800:26B8A13F17A8D1FCD095B13055345DB8B8362F2A404509ADB3861189D32898F0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.79595575335101977886499288410382:50001231000000:2800:B97951B48DE6EE5F116EB3FD0BB6BBBF5953B49339EC502F113C8C787C4FC8D4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150727.23587396364953181065363117066062:50001231000000:2800:D3019237857FBFE3569E5C331B64EA4E6708D8160A26B090A41FFF6549BBE7AB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.51092399267907641323012753220807:50001231000000:2800:B1AF96259893D54C4F199C363A8641494AE6A394834B210A851D608F20753DD4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.27916385287128746063085765808093:50001231000000:2800:62F113898458278DCFE0D464F13974E25DB24B90F87F1EF274D3688D4A3C3609.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.07221158876417495977762618576078:50001231000000:2800:7425E5A6EB0E7F155BAAEF91B0A592FA8E6F875E5211A505275DECA7E9426125.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.54811224041545617171484541561368:50001231000000:2800:9B793A502649ADEEA9461FC51C38D7506347D89FAB516871235FBF472572ABE1.png?needInitFileName=true?needInitFileName=true)
UI界面快照
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.63533889589889454973039596176172:50001231000000:2800:2291BE35847B1D33CAEB9AE27A4DEC3135D1F350148DE155E28CA17E5A365D57.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.92895141097010999347958454768968:50001231000000:2800:46221DA8C8F627A0F0B60934718448EBC4164313219FA9288B1531D85E29939E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.68567296425086936738515984048472:50001231000000:2800:6BBF43FCBC7DF903164938865B6B5BEBABE0199BBFEB532EE373EFA59372E185.png?needInitFileName=true?needInitFileName=true)
UI组件源码跳转
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.04055819804600144444986625265178:50001231000000:2800:4434CBCB4312135ABBF8B18C67DED2214C4B8589637AE79DFD18BB373D2411DE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.67239338380163349762565239068174:50001231000000:2800:D5A9F2D70653C82CB8BE8D87DB1EA8A7662DCB338AC870EB3FACF79FE8011F90.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.26535712316172598493435285746408:50001231000000:2800:C92EBAD7C3A5A04CF7B1138358C0E9F4E52904704BF1F2D7A907CD17B3AC90FC.png?needInitFileName=true?needInitFileName=true)
显示布局边框
在UI显示设置上，勾选“Show Component Border”，可显示当前页面所有组件的布局信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.82292600283733143317507746830707:50001231000000:2800:C84CEC1F2C407BD6D39433FCEFD6AFC2A023178E7B91DA3E59106AAA6BDFDC8D.png?needInitFileName=true?needInitFileName=true)
查看UI组件的状态变量
点击自定义组件，可以查看自定义组件定义状态变量，以及状态变量影响的下一层组件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.28552474479541937549899082698142:50001231000000:2800:702E9A73C65BA58B8090407074E2CB8A08CA190DACBE87F70B83DFA8CF8966A7.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-device-file-explorer-V14
爬取时间: 2025-04-30 08:35:59
来源: Huawei Developer
开发者可以使用Device File Browser，在DevEco Studio上如PC端操作一样，进行文件新建、删除、上传、下载等操作，而无需使用命令行，提升开发效率，当前支持普通文件视图与应用沙箱视图两种模式。
使用场景
使用约束
操作步骤
1.
2.  如果需要查看数据库文件，可以通过该方式将数据库文件（路径举例：data > app > el2 > 100 > database >项目名称 > entry > rdb > 数据库文件）下载到PC上，再通过其他工具进行可视化查看。
3.  如果需要查看数据库文件，可以通过该方式将数据库文件（路径举例：data > app > el2 > 100 > database >项目名称 > entry > rdb > 数据库文件）下载到PC上，再通过其他工具进行可视化查看。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.37790205371978016988665280399406:50001231000000:2800:EFFC25EEC4063924DF6BBA4B9507EBB04D97DD5C5F12CC4E4C99964C652B6B28.png?needInitFileName=true?needInitFileName=true)
1.  如果需要查看数据库文件，可以通过该方式将数据库文件（路径举例：data > app > el2 > 100 > database >项目名称 > entry > rdb > 数据库文件）下载到PC上，再通过其他工具进行可视化查看。
普通文件视图
普通文件视图将按照设备的真实物理路径显示当前设备上的文件结构。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.73990000106042000577068340084577:50001231000000:2800:37EA3267D396CC95120431664DA23D50EC91BE487AC81F976F4532A70284A140.png?needInitFileName=true?needInitFileName=true)
公共目录
以下公共目录支持访问、文件上传与下载。
```shell
$ hdc file send test.txt /storage/media/100/local/files/Docs/test.txt // 往Docs目录里推送文件
$ hdc file recv /storage/media/100/local/files/Docs/test.txt test.txt // 将Docs目录下的文件下载到本地
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.67522966785886882594702827585549:50001231000000:2800:91D7E5FBFAF85B10D733F6D3567BA4BDB3BAC8B96D5DCE202D7741D27A2644DA.png?needInitFileName=true?needInitFileName=true)
应用沙箱视图
沙箱视图基于FTP协议，当需要以沙箱视图查看应用的文件结构时，需在module.json5文件内配置ohos.permission.INTERNET开启网络权限。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150728.99475159915185403924052754919997:50001231000000:2800:88B14CA57D32DA369B3D6B7FD5F4974EF24B1E1E64B5DB8A8FBBC0775DA00803.png?needInitFileName=true?needInitFileName=true)
应用沙箱视图将按照应用的沙箱文件路径显示应用的沙箱文件结构，支持数据目录的文件目录读写操作。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.17057638797089197606365601219359:50001231000000:2800:6BB7406FA724B145AA9F98AE485A0356CFC2C8C15B780EFB336343F821D3B75D.png?needInitFileName=true?needInitFileName=true)
命令行方式访问应用沙箱
真机设备中内置了bftpd二进制软件，可以通过命令行的方式访问debug应用的沙箱目录。
1.
2.
3.
```shell
$ ftpget -p {port} -P guest -u anonymous localhost -l /data/storage/el2/base           // 查看应用沙箱下/el2/base目录文件（返回文件全部信息）
$ ftpget -p {port} -P guest -u anonymous localhost -L /data/storage/el2/base           // 查看应用沙箱下/el2/base目录文件（仅返回文件名）
$ ftpget -p {port} -P guest -u anonymous localhost -M /data/storage/el2/base/test      // 在应用沙箱下/el2/base目录下创建test目录
$ ftpget -p {port} -P guest -u anonymous localhost -d /data/storage/el2/base/test.txt  // 在应用沙箱下/el2/base目录下删除test.txt文件
$ ftpget -p {port} -P guest -u anonymous localhost -D /data/storage/el2/base/test      // 在应用沙箱下/el2/base目录下删除test目录（仅支持删除空目录）
```
4.

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-screenshot-V14
爬取时间: 2025-04-30 08:36:34
来源: Huawei Developer
在调试过程中，可以通过多种方式截取屏幕截图。
通过DevEco Studio截屏
1.  截图的图片将直接显示在DevEco Studio中。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.94229761128534406507874604784575:50001231000000:2800:5C3FD35028EA57EF1EDF7AD54DB657444396EC6540AAD7704B2AE5540E428E34.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.87806044850604587189912836527368:50001231000000:2800:3B89E1EBCDF619AF48B97F111B0A435A3945C16D9114F7B08D9942B9233D541A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.29334981883103423250885639952732:50001231000000:2800:F620414CD6CAE0A69E82E5100573BB390588F68DCE9D8E760A6242F71F2BA78A.png?needInitFileName=true?needInitFileName=true)
通过命令行方式截屏
hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见hdc工具使用指导。
方式一：hdc shell snapshot_display
方式二：hdc shell wukong special -p
wukong是系统稳定性测试工具，通过指定参数-p可以实现截图功能。更多关于稳定性测试工具wukong的说明请参见wukong工具使用指导。
命令执行效果如下图所示，其中Report currentTestDir为结果存储路径，包含截屏图片。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250120143408.39568663175612818533223831804443:50001231000000:2800:EA43C82D4FFFF8F741870E751B945D52C147140EFEEFA2CB645860F1E7BC75E7.png?needInitFileName=true?needInitFileName=true)
通过hdc命令可以将该路径文件发送到本地，示例如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-screen-recording-V14
爬取时间: 2025-04-30 08:37:08
来源: Huawei Developer
在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。
使用约束
通过DevEco Studio录屏
1.
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.47567611846981399052891500009101:50001231000000:2800:EC1954C8259A470236F07D4DDA4C2A32409547BA363E801092077ECFAE406D8F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.75414661252284934090151987015763:50001231000000:2800:C90352D0694FCE39C309C26458EF233E4321856EFB0BA8A79FF4F66E4BF1A826.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.40621782223770361627735082051392:50001231000000:2800:B891D2428C9441C12A7C7FBD229695F1186B0842A1995778FDD4693870F1E3E5.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.34464390155634488171717941878102:50001231000000:2800:76ADE1700696FE8B1B44A41BDB97A9A80A8F02BF975D40C1AD9B836714EC747B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.28971959681741243546104942687225:50001231000000:2800:04E5BFE85BE59B612756C26231FF24AF3B2D8E0CAA4CF350BFFF8DA7E3FDCA39.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.90290786790095561318765194337995:50001231000000:2800:1051B9D2DDAE25BE6182483478CD793B2372B3482764FFED434918BF42EEEBB5.png?needInitFileName=true?needInitFileName=true)
设置录屏自定义路径
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.70923837858339113021545836031290:50001231000000:2800:F73AA1F477F7827E491DD2443E636B2C59B64A91435E8E9F2AB5AE44654D1EEA.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.38577795207862612297848651318770:50001231000000:2800:FEDF6FB7D757A914C2BE58D6345AD96BAA25E097AC2ACF009C7A0A67DAB1E6BF.png?needInitFileName=true?needInitFileName=true)
通过命令行方式录屏
hdc是可以用于调试的命令行工具，通过该工具可以实现录屏功能。更多关于命令行工具hdc的说明请参见hdc工具使用指导。
1.
2.
3.  需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。 命令返回值第二行即为录屏文件路径{RecordFile}。
4.  需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。 命令返回值第二行即为录屏文件路径{RecordFile}。
5.
6.
-  需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。 命令返回值第二行即为录屏文件路径{RecordFile}。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.96570164646399593487819256719715:50001231000000:2800:BE5374308BD9152B989396A67A5D26713B9D242B04F5A4D4F03D07DEE49A67DC.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150729.37856316362085243109020487794695:50001231000000:2800:368FF8264B00935E3C11DE9F83DDB589D4A869FC623C623614443E6BA7943056.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.28901789985164825163042789202977:50001231000000:2800:684D5F0DC7A173C6CDEDB966C3E01384E985EE3BFA88C5E852294AF22A2CEA86.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-V14
爬取时间: 2025-04-30 08:37:43
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-description-V14
爬取时间: 2025-04-30 08:38:17
来源: Huawei Developer
应用或元服务运行期间可能出现响应速度慢、动画播放不流畅、列表拖动卡顿、应用崩溃或耗电量过高、发烫、交互延迟等现象，这些现象表明应用或元服务可能存在性能问题。造成性能问题的原因可能是业务逻辑、应用代码对系统API的误用、对ArkTS对象的不合理持有导致内存泄露等，引起对系统资源不合理使用，包括对CPU、内存、网络、文件、GPU、以及其他外设等器件的冗余占用，进而引发性能问题。
通常，进行性能优化主要围绕关键点“降负载”来入手，这包括：
1）永久降负载。即将原本不合理的冗余处理进行彻底清理；
2）临时降负载。即避免在关键时间段内扎堆产生负载。可以考虑采用懒加载等延迟处理机制，错峰运行。
在遇到这些问题时，首先需要对应用的运行情况以及设备的资源消耗进行监测，以初步确定可能存在的性能问题以及问题出现的位置，进而有针对性的降低负载。
DevEco Profiler提供实时监控（Realtime Monitor）能力，提供全方位的设备资源监测，覆盖系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率以及能耗等多个维度的数据，自顶向下逐层展开分析，并可借助DevEco Profiler跳转到代码位置，结合代码进行白盒分析，明确不合理的负载出现位置，帮助识别性能瓶颈，定界问题所在，提高解决问题的效率。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-V14
爬取时间: 2025-04-30 08:38:53
来源: Huawei Developer
为了帮助开发者更高效地进行性能问题的分析，DevEco Studio提供了场景化调优工具DevEco Profiler，希望为开发者带来高效、直通代码行的调优体验。
开发者可以使用DevEco Profiler完成不同应用模型和场景下的完整性能数据采集，通过简单的工具操作即可完成数据采集，这些数据将帮助开发者洞悉应用在相应场景下的运行细节。
工具的整体设计也遵循了Top-Down的设计理念和数据展示范式。被采集的数据经由工具分析，会由浅到深的以一条条泳道的形式直观地呈现到界面上，DevEco Profiler提供深入具体函数运行热点、CPU调度细节的分析能力，帮助用户搭建HarmonyOS应用性能模型。
DevEco Profiler聚焦性能分析靶心，围绕着Top-Down的思路深入展开分析；各个局部功能具备高度的整体一致性，方便开发者快速上手其他场景下的类似功能。
您可以通过如下三种方式打开Profiler：
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.70065083645573107798198028924277:50001231000000:2800:AFB56E13964FF7DB48EA3EF5106BA23A9EDA5BB8B0F24C68815F62BC23F9D9AF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-layout-V14
爬取时间: 2025-04-30 08:39:27
来源: Huawei Developer
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.43548026783071762770261823706413:50001231000000:2800:64EDC39F7BE507723B2919847A655B65589E578FBAE51BBC7D8AA84529DD25A3.png?needInitFileName=true?needInitFileName=true)
DevEco Profiler工具的界面分为两大区域：
①会话区：负责调优会话的管理。会话区提供了性能实时监控工具Realtime Monitor来帮助开发者先明确问题场景，完成问题的发现和初步定界。开发者可以在会话区选择待调优的设备、应用及当前应用进程，当前已创建的调优分析任务将在下方以列表的形式展示。
每个会话是一份独立完整的性能数据单位，是由开发者通过一次录制得到的，同一个会话中的各种数据经过工具的处理可以互相关联，而不同会话间的数据，由于来自不同时间段的录制，不会具备关联关系。实时监控本质上也是一种会话，是由实时监控这个场景模板创造而成的。录制会话时需要注意，确保场景复现完整后再结束该次会话的录制。
同时会话区提供Launch、Frame等一系列场景化分析任务类型，帮助开发者有针对性的采集并展示更多更详细的数据，这些数据将会还原对应场景下的应用运行状况。
②数据区：负责性能数据的可视化呈现。包含工具控制栏、时间轴、泳道区域、详情区域，通过不同泳道展示，直观展示调优详情。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-session-V14
爬取时间: 2025-04-30 08:40:01
来源: Huawei Developer
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.45582283084567749650095386520678:50001231000000:2800:19A297448BD56F37815342141478C92037D2BFE5B1DA725FE758A5F434EAA4C3.png?needInitFileName=true?needInitFileName=true)
DevEco Profiler左侧为会话区，可以分为三个部分：
① 调优目标选择区域：选择设备及要分析的应用和进程。
选定被调优的设备、应用包及应用进程作为后续调优会话的分析对象。依次点击设备、应用、进程列表完成选择。选择完成后，若目标正在运行，将自动开启实时监控进行指标的观测。
② 会话列表区域：列出当前已创建的调优分析会话。
单击列表中的会话后，界面右侧数据区将显示其数据内容。选择设备应用和进程后，此处默认显示“Realtime Monitor”任务。
会话区将记录当前所有的会话。每一个会话都会包含：会话的名称(图例中的"Launch")、会话当前状态(图例中的"Recorded")、会话对应的录制时长信息(图例中的"9s 302ms")。会话支持拖拽方式调整顺序。
录制/删除会话：通过鼠标悬停在名称后方的信息图标上，会话所要观测的调优对象的基本信息将会以Tooltip的形式展示。点击会话的右侧的/按钮，开启/停止会话录制，此时工具开始抓取性能数据，开发者可以操作应用复现性能劣化场景；点击将删除该会话。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.39624463378981639071330762415417:50001231000000:2800:4C23C634D3E44B9038E5799F001713D61280C019ED5CC58DF49FD302F932DEB0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.84042879701097492966848283216421:50001231000000:2800:E90DDA3945856909997F5926BD6B522997D51DF4B9BAAB9E497C72E3E6084D61.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.06399152424577675978458646903899:50001231000000:2800:500ABF25A73A1B56756CE7CD7D6925AA028B24E18ACEF765381D9E5F9DFCC6E6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.47875299241054285945204037162801:50001231000000:2800:DEB3C7CF5F4C00ED5F128FBD4DAD8E3DCAD6D36CF44D68173DAE1A4E6D9BD889.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.15781484390796283677632809794119:50001231000000:2800:9EC8F9177534CDA22DFFF8A4C1F56F0CE27DA1D61854469EFDE531B05DF274CD.png?needInitFileName=true?needInitFileName=true)
数据导出：待数据解析完成后，会话便会进入数据展示状态，将数据可视化的展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便的在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.47893771402318637754252448063059:50001231000000:2800:6CC60381F468F7549492F1E246E034D680FDD97B275D0544E250FEFB60EFBB91.png?needInitFileName=true?needInitFileName=true)
③ 场景化模板选择区域：新建会话的入口，DevEco Profiler提供Launch、ArkUI、Frame、Concurrency、ArkWeb、Network、Time、Allocation、Snapshot、CPU等场景化分析模板，提供对不同性能问题场景的数据分析方案。
：Launch冷启动场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.45463870687347834771263916768605:50001231000000:2800:BF6BE97898BAC18F0F3992E99863357EBC55B2EE0F7447EF1A32B11693B456AF.png?needInitFileName=true?needInitFileName=true)
：ArkUI卡顿丢帧场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150730.82028844256098228873065709301944:50001231000000:2800:D0760BEA15C567D21ADAC1A83116808CB6898120E5EAB870252C3D6FB892CA31.png?needInitFileName=true?needInitFileName=true)
：Frame卡顿丢帧场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.26709534267802833366778576071280:50001231000000:2800:7CAA7B3787C50DEB36EDBCC34847C1F0DE127465E305BEA864031F446141F310.png?needInitFileName=true?needInitFileName=true)
：Concurrency并行并发场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.84940369157071439353069328378651:50001231000000:2800:A0A3EE150657806007E2D861381D098E714DA3D2473DB1898C282A7C880B4CBB.png?needInitFileName=true?needInitFileName=true)
：ArkWeb加载丢帧场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.90185795020802694786721037633074:50001231000000:2800:585CE42FF5174713E3ADC19A081611485E51C02DEC958A87D97B3A6A0F0015FB.png?needInitFileName=true?needInitFileName=true)
：Network网络诊断场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.99598990886966167186697301303082:50001231000000:2800:04E784DBC1BCC5F0B6C02D1E0B8A4C35B9929218A095AE1366781AEBC776A929.png?needInitFileName=true?needInitFileName=true)
：Time函数耗时场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.76645723725270003410660964336660:50001231000000:2800:B9B34FB363C2B01872CE49F39E49C00A56D11156ACEA838B655B1916A14C5C99.png?needInitFileName=true?needInitFileName=true)
：Allocation内存泄露场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.53279221061564331003604125905933:50001231000000:2800:6496515F63038D32E175A97720DC27DDCDDB8C149EAFB24FF27A8B6F34F33A98.png?needInitFileName=true?needInitFileName=true)
：Snapshot内存快照场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.64001498427593538906900254287489:50001231000000:2800:4BF6C040E404EC77DA882BCC5988BBDB241741A19956DFFD91B4828176C1C350.png?needInitFileName=true?needInitFileName=true)
：CPU调度场景化模板。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.06541247647793488994734065130227:50001231000000:2800:6B29F4C243A6D2C4039EC13D271876109C16B9D905E52E00DD9EFF0E35A59470.png?needInitFileName=true?needInitFileName=true)
选中任意模板图标，点击下方Create Session按钮，即可创建出一个全新的会话。
数据导入：在③ 场景化模板选择区域，点击Open File按钮，即可选择数据进行导入。当前支持.insight，.htrace， .ftrace，.heapsnapshot，.rawheap,  .sys，.perfdata，.nas（包含Native Allocation数据的.htrace文件）文件的导入。
配置Profiler缓存路径：在③ 场景化模板选择区域，点击左上方设置按钮，会弹出文件选择器，设置Profiler缓存文件的保存路径。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.15655803689434951923593723423413:50001231000000:2800:67BDDA92E6D64C900CE8A659ABAD771B90A2F2283CFEB20103A390AF5B064355.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.35250282142975723153657020397664:50001231000000:2800:A726A710C8FE26C382D529B2C7E29C11EAF588C0CD722AE1E434DEB992DBDF14.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-data-V14
爬取时间: 2025-04-30 08:40:36
来源: Huawei Developer
在数据区域，DevEco Profiler提供了对性能数据的可视化呈现结果。由于每个场景化模板所提供的可视化能力各不相同，本章节会主要就所有模板均通用的能力展开介绍。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.94028545614304431014743048802340:50001231000000:2800:B0759E68672BA40BB59FD4C27080B3C3001844B6EA5325D576A4180A16431DED.png?needInitFileName=true?needInitFileName=true)
整个数据区可以分为五个区域：
① 工具控制栏：提供标记、收藏、离线符号导入、泳道过滤、泳道启动配置项等辅助功能的管理以及会话状态和时间轴的控制能力。
：标记列表按钮，点击后可以看到当前已放置的所有标记。可以查看/跳转到标记描述、时刻，支持修改标记的颜色。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.13955606053620045205569797965637:50001231000000:2800:981F9311349159ECB1A4DED50A194116C2A2BE4BC61AD264643EEA9059EE53A6.png?needInitFileName=true?needInitFileName=true)
：收藏泳道隐藏/折叠按钮，激活后隐藏/折叠收藏的泳道，置灰时为展示收藏的泳道。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.09209442339910796535077467215720:50001231000000:2800:07A3B1364BFA0B2256295A391EADEEBA5DBE2BCD500AA45A9524F50519671060.png?needInitFileName=true?needInitFileName=true)
：离线符号导入按钮，点击后可以导入带有调试符号表的Native库，对应的Native函数栈符号将被还原。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.43183644741407876586585936698797:50001231000000:2800:99627C34324C2E23B23909740D135DBF8C853D66A5C4CD9E787C3792807ECD30.png?needInitFileName=true?needInitFileName=true)
：泳道筛选按钮，点击可选择泳道进行过滤。筛选无需录制的泳道，可以降低数据采集本身的开销，但同时会造成数据分析维度的减少。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.84355354115088488040934107265878:50001231000000:2800:FB07BE119AC6E85E8A145901312543B26E1BE3AFACFBA9B4529971C4E07A0239.png?needInitFileName=true?needInitFileName=true)
：泳道启动配置项，点击后展示不同泳道对应的插件启动配置信息。支持将配置信息保存到配置文件，后续使用该类型模板默认生效当前配置。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150731.29040089455427069436318882714603:50001231000000:2800:E9816CE74B9ABDE224C59398BE95E59E3B441B989375C9D4AFB2708A3725420E.png?needInitFileName=true?needInitFileName=true)
② 时间轴：提供横向时间轴，用于显示数据时间戳。
③ 标记栏：用于放置标记，能够帮助开发者标记时间点或时间段。
④ 泳道区：泳道图区域。每个场景化模板都会预置一系列泳道单元（例如上图的“Frame”便是一个泳道单元）。泳道单元是整个DevEco Profiler工具内，数据组织的最小独立单元，用于剖析应用某一特定维度的运行数据，每个场景化模板均是由一系列泳道单元组成，每个泳道单元都会呈现某一维度的性能数据。开发者可以查看数据随时间变化的特征，发现数据异常的时间段，支持框选时间段后在详情面板查看对应的细节。
⑤ 详情区：展示详细的数据细节。开发者在泳道区域选择数据之后，以各类表格的形式呈现该时间段内各项详细数据。More面板将对左侧详情区中选中数据进行补充描述。
基本操作
开启/关闭会话控制
在数据区，首先可以开启和结束会话的录制，点击工具栏的首个按钮即可，如下图所示分别对应开启录制、结束录制功能，第三个状态则代表录制完成。与在会话区域录制的功能效果一致。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.67825510048603876919417288612982:50001231000000:2800:BC57BB5D2E9789ADFC1F9BF6D37DD33FD6B4BA5D1980E9888A29481036F43060.png?needInitFileName=true?needInitFileName=true)
时间轴控制
DevEco Profiler工具提供了各种丰富的时间轴操作功能：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.99159289123268249166873529786801:50001231000000:2800:D9351542A512065706F4BDBF3E6FDEA8B920262E05BFB695389F09382D8A18C2.png?needInitFileName=true?needInitFileName=true)
：数据全量展示按钮，点击后时间轴尺度自动调整，将展示会话完整时间范围内的数据。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.83454444269397501007337860409055:50001231000000:2800:A0B32DCF0974105212CE10A03CE13D72BEA88660E2EBC16FF7091B7AB22C3549.png?needInitFileName=true?needInitFileName=true)
：时间轴调整按钮（快捷键为W或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变小，更多数据细节会呈现。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.90278058874309128480179671923408:50001231000000:2800:A25F8DACA85CDB86C0B7A7969B0FCE0BA88F98F059D1E25263E0D6D9DF43AE67.png?needInitFileName=true?needInitFileName=true)
：时间轴调整按钮（快捷键为S或使用Ctrl+鼠标滚轮），点击后时间轴所展示的时长将变大，更易于观测整体数据趋势。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.16505860434903096833197761526181:50001231000000:2800:690497B14FFFF355506F7EC0E9337EEC086867C74C4C5B5B488E0B1D38E9F3F1.png?needInitFileName=true?needInitFileName=true)
拖动泳道区域下方的滑条(快捷键为A/D键或使用Shift+鼠标滚轮)，开发者可以调整时间轴所示的时间范围；拖动泳道右侧滑条（或者滑动鼠标滚轮），可以调整泳道单元上下滚动。具体快捷键使用方式请参见快捷键。
使用W/A/S/D等纯键盘的快捷键操作，仅在已激活的泳道区域生效。泳道区域中存在亮蓝色的选中边框即为激活状态。
查看详情面板
当开发者在泳道区域观察到可疑数据后，便可以通过框选或者点选的方式，将相关详细数据展示到详情面板中。泳道中条块状的数据支持点选查看，在泳道区域鼠标点击拖动再释放完成框选。可以在框选的同时按住Alt键，完成框选后时间轴尺度将会自动适应，整个框选时段会充满整个泳道区域，方便聚焦观察被选择的时段。
由于不同的泳道单元会展示不同维度的数据，因此详情面板展示的数据是来自于泳道区域中被选择的泳道单元。被选中的泳道单元会呈现蓝色，与其他泳道单元有明显差异。此外，当开发者直接选中泳道单元，而未进行框选或点选时，详情面板中会展示整个泳道单元的完整详细数据（效果等同于完整框选该泳道单元）。
添加/编辑标记
为了便于开发者记录分析出的关键时间点，DevEco Profiler工具提供了标记功能供开发者使用。
DevEco Profiler支持两种时间标记：
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.14787514661562293494868522114462:50001231000000:2800:B3C4798EC0B9BD1360F2FD605037F5B12444E3D94F015DC92DFA828EAA080043.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.79191584685503369271860311234098:50001231000000:2800:009323CD5DA435B56C13EE5FAC4C6BC2BB99CDA135B421C969D5A75D7DBF15E4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.79654955643903883939656094234325:50001231000000:2800:FDC632E7A030A718529928F0BD1F98EB55C7FF8F7AB73BAA40E00BF76C1B1A81.png?needInitFileName=true?needInitFileName=true)
开发者可以在时间轴下方的标记区域点击放置单个标记，也可以在框选时间段后，点击旗子按钮放置该时间段的标记，如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.12372915716224706361313768539779:50001231000000:2800:2BD5A698C59621B2EAC69CA9864A1BB968209671CFFFB1859FA28CBD22D77107.png?needInitFileName=true?needInitFileName=true)
支持使用“ctrl+, ”向前选中单个标记，“ctrl+. ”向后选中单个标记；“ctrl+[ ”向前选中时间段的标记，“ctrl+]”向后选中时间段时间标记。
标记放置完成后，可以通过双击标记按钮，在弹出的标记属性框中修改标记的描述和颜色信息，或者删除标记。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.74522056422768087592987325131881:50001231000000:2800:79730426E059E9929C2E68E1EACD7AC46E42040101BF3B67B4FA097DA2765E08.png?needInitFileName=true?needInitFileName=true)
此外，工具还提供了查看不同标记之间时间差的能力，只需要先选中一个标记，再鼠标悬浮在其他标记点上，便可在面板右下角后看到被悬浮的标记点和被选择的标记点的时间差。借助这个能力，开发者能够快速获知一些特定时刻的时间差，这对于分析时间敏感的性能问题尤其有用。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.62207131181631682625102818588586:50001231000000:2800:0587FB62A110E934165040BA69ED415CC9C5BC634FB988C2D4C58F2B115C4B9F.png?needInitFileName=true?needInitFileName=true)
收藏泳道单元
在使用工具分析，可能会遇到泳道单元过多，导致想分析的泳道单元间隔过远、分析低效的情况，使用收藏功能，可以帮助开发者将关注的泳道单元提拉到泳道区域的顶端。将鼠标悬停在想要收藏的泳道单元之上，出现收藏图标，点击该按钮即可完成收藏。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.91297188004357560847000943073985:50001231000000:2800:BE2E2602496B5E7A9C92CC35591C351A5FC834AA3A12276F504084FBC72FB1C4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.04419112851379397793614142266265:50001231000000:2800:FD7417B8C7F1454CA3B971ABDB402DAEA15197A8DD5C1DB6D0CC57560B9FB807.png?needInitFileName=true?needInitFileName=true)
再次点击该按钮则取消收藏。此外，由于顶部区域空间有限，工具还提供了压缩泳道的能力，点击泳道中图标，可以将收藏的泳道单元进行折叠。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.39807340946719280606195167405102:50001231000000:2800:1A7AEBB1B5DDC8A22544BE3CAB31581E37F4F52FF03EBA6C070F282EBE3C3432.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.53014295590905120288926017580009:50001231000000:2800:07CB9E16DCCD4C9EC0F596B851FA7DA36FE8330E89A51587DB5DAD9AF662B8E3.png?needInitFileName=true?needInitFileName=true)
如果泳道展示不完整，当鼠标悬浮到泳道标题区，会提示该泳道的泳道信息。
如果收藏的是子泳道，当鼠标悬浮到收藏的子泳道标题区，会提示该泳道的父泳道信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.29392567643327475208915311942967:50001231000000:2800:E0AF68C2B3D2124FDE8E431B48DE257A980E159D9A4FDCFE518D74C250BD45D4.png?needInitFileName=true?needInitFileName=true)
展开/折叠子泳道
工具提供了两种方式展开/折叠子泳道：
1、点击父泳道左边小三角符号。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150732.33258909660190698758825761149025:50001231000000:2800:53A5503700798B7455E945148963130B7E6D88E67583D20DDCDF8E88E14FA762.png?needInitFileName=true?needInitFileName=true)
2、双击父泳道表头区展开泳道。
全局搜索
为了帮助开发者迅速查找关心的性能数据，DevEco Profiler工具提供了全局搜索功能。
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.43552285425700386946652282495752:50001231000000:2800:58B2F6EF51638EC2B398D619AF662A187DAE58F0EDE80E49E41FF2D963E3AD9F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.55475070585539523716401644749207:50001231000000:2800:3D286BC8A0FF7BCCE51F56125F715E020AAEBA89D38F1E959B55FC0AF07D46C3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.57204478849670680714003826630259:50001231000000:2800:EC50CB139B82F950E24580FEE0463150E739853605E7C3DB9E31C080EE4EB82B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.85158717294436700918816304073608:50001231000000:2800:AAA4719EBC6C7E349848D7A896C317752D158784BDFF4A738FB563F1B9EF059E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.05568448020799787757285170483572:50001231000000:2800:E539656C7C01BFEE29DC25CA5B32CEC8EF75731B3AC9F48E46AB86698748119B.png?needInitFileName=true?needInitFileName=true)
离线符号解析
为便于开发者分析Native的函数热点，工具提供了符号导入的能力，开发者可以点击工具控制栏的按钮，选择带有调试信息的so库导入，之后工具会利用此信息，将采集到的函数偏移信息转换为对应的源码符号（包括系统so库，用户自编译的so库，三方库）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.11726096090893040625715918852154:50001231000000:2800:A06BB4A3DDD87D1A2B1F5276136BBDD400205B0033E0E0EB04F6163D13E33C8D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.82493741794090204392704919899808:50001231000000:2800:469A60581773555AA8081A2988D271C30E983B0EACF2A62EE2D3514321CC914E.png?needInitFileName=true?needInitFileName=true)
源码跳转
找到问题源码是调优过程中最为关键的一环。针对详情面板中所展示的函数栈帧信息（如下图所示），双击栈帧结点，工具便会在编辑器中打开相关源码文件，并定位到对应行号。此功能正常使用的前提是用于抓取性能数据的应用，是在DevEco Studio所在的开发环境中编译，且相关源文件位置并未改变。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.40878296559817987255443746566982:50001231000000:2800:09787A8E4CD91A7E5CB0094CBEA30744CE41796E017C92BC219B457D8B3D49FB.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-introduction-V14
爬取时间: 2025-04-30 08:41:10
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-process-V14
爬取时间: 2025-04-30 08:41:44
来源: Huawei Developer
流程概览
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.62334599265266162790057663318306:50001231000000:2800:68AC0E8E43084B9CF311A80F11AFEC3736486E50AA8E7A3CE790A55CD5C8AE34.png?needInitFileName=true?needInitFileName=true)
在开发应用时，开发者会对应用的运行情况有一个预期的指标，当应用在某些方面不能满足预期的指标或者表现不佳时，意味着您的应用可能存在性能问题，需要对应用进行性能优化以达到您的预期。应用的性能优化是一个不断持续的周期性的过程，您需要在应用开发过程中观察应用的运行表现来识别性能瓶颈，通过运行时数据来定界定位性能问题，定位根因后修复代码并验证优化措施的可行性，循环往复直到应用满足您的性能指标。DevEco Profiler也遵循以上流程，在使用DevEco Profiler进行性能优化时，您可以参考以下过程：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/realtime-monitor-V14
爬取时间: 2025-04-30 08:42:18
来源: Huawei Developer
解决性能问题，首先对当前应用的运行情况以及设备的资源消耗进行监测，以初步确定可能存在的性能问题以及问题出现的位置。
DevEco Profiler提供实时监控（Realtime Monitor）能力，该能力为您提供全方位的设备资源监测，覆盖系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、温度、电流以及能耗等多个维度的数据，帮助您初步识别性能瓶颈，定界问题所在。
配置并确认设备环境
为了能够正确地监测您的设备资源，首先您需要通过USB完成设备连接，打开“开发者模式”并选择允许“USB调试”，然后通过DevEco Studio将您开发的应用安装到设备上。随后您可以通过如下步骤来查看应用的实时资源使用情况。
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.59657034098077946098160496748760:50001231000000:2800:2356F4637C93716354C2206A3FF16E4FA3F58703F3C15F4C1203840A0F856B66.png?needInitFileName=true?needInitFileName=true)
当选择完您需要监控的应用以及进程之后，DevEco Profiler会自动为您打开实时监控（Realtime Monitor）的页面。
实时监控应用，多维度对比识别性能热区
在实时监控界面，设备各项资源的使用情况均以泳道图的形式在时间维度展示，提供系统事件、CPU占用等多维度信息，帮助您识别性能热区。
面板整体介绍
整个实时监控页面从上到下，依次展示了系统事件、异常事件、前台应用、CPU占用、内存占用、帧率、GPU使用率、温度、电流以及能耗等各个维度的数据，帮助您从多个维度来对比识别当前应用的性能热区。下面为您依次介绍每一条泳道的数据内容。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.90458264100842807121806835480881:50001231000000:2800:269B94D1004B19622A4BA193F2A3C1FF1C026552F094420B45AAECD2D5F43243.png?needInitFileName=true?needInitFileName=true)
泳道简介
② Anomaly泳道：用于展示设备侧上报的各种异常事件。
③ Foreground Ability泳道：用于展示应用/元服务的Ability状态。当Ability在前台运行时，会在此时间段内显示该Ability的名称；若当前无前台运行的Ability，则此时间段内显示“Background”。
④ CPU泳道：左侧饼图展示了当前时刻应用/元服务的CPU使用率、其他进程的CPU使用率以及空闲情况。右侧的泳道图则展示了时间窗内的整体CPU使用情况，其中灰色的部分代表系统中其他进程的CPU占用，蓝色部分则展示了当前应用/元服务的CPU占用情况。
⑤Memory泳道：左侧饼图展示了当前时刻应用/元服务的内存占用、其他进程的内存占用以及未使用的内存。右侧的泳道图则展示了时间窗内的整体内存使用情况，其中灰色的部分代表系统中其他进程的内存占用，蓝色部分则展示了当前应用/元服务的内存占用情况。
⑥FPS泳道：左侧仪表盘展示了当前设备屏幕的帧率瞬时值，红色、黄色、绿色区域则代表当前屏幕帧率是否达标理想状态。右侧柱状图则展示了每一次采集设备帧率时的数值。
⑦GPU泳道：左侧仪表盘展示了当前设备GPU使用率的瞬时值，右侧泳道则展示了时间窗内的整体GPU使用率。
⑧Temperature泳道：左侧温度计显示了当前设备温度信息，右侧泳道的数据采集周期为3秒，展示了时间窗内的设备温度信息以及温度等级。
⑨*Device Current泳道：左侧展示了当前设备最大电流、平均电流以及最新的电流值，右侧泳道则展示了时间窗内的设备电流信息。该泳道统计电池的电流会由于充放电导致电流为非准确的消耗值，使用*Device Current进行区分，若需要准确的消耗电流，可以在设备侧打开"关闭充电"，操作方式为设置 > 系统 > 开发者选项。
⑩Energy泳道：该泳道包含了各项部件（包括CPU、*Display、GPU、Location、Camera、Bluetooth、Flashlight、Audio、Wifi、Modem）的周期内平均功耗占比。通过图例上方的下拉多选框则可以勾选您想要监控的功耗使用情况的应用，选择多个应用后，该泳道会展示所有您所选择应用的功耗总和。右侧区域柱状图则展示了时间窗内各部件资源的实时使用情况，柱状图的颜色代表每种部件的功耗占比。Display指标只能测量不同亮度的屏幕电流，无法精确测量不同明暗色的显示电流，为提示开发者，使用*Display来突出该差异。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150733.19502540974129070330280070275308:50001231000000:2800:EE4E93FC41B4A8435D03B1CB84BFCF0283F2BD1903E76C7B6F47E71950EFC151.png?needInitFileName=true?needInitFileName=true)
FPS、GPU显示的是所使用设备的实时信息，而非当前调优应用/元服务的信息。
实时监控页面的常用操作交互方式
实时监控页面除了展示各个维度数据的瞬时值以及时间窗内的变化趋势之外，还提供了多种交互方式以供协助您更加便捷、快速、细致地分析您的数据。
-  点击会话区“Realtime Monitor”页签上的、按钮来即时控制实时监控界面的录制状态。
-  将鼠标悬浮于所关心的泳道数据上时，界面上会出现当前时间点的时间标线以及含有当前时间点上泳道详细数据的Tooltips。更进一步，当您将鼠标悬浮于时间轴之上时，实时监控页面内的所有泳道均会以Tooltips展示出该时刻的数据。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.74604725746305662857877374709442:50001231000000:2800:88ED5E080ABD71E67DD070F974051966C268B3FE4268E5C24AD487E115226298.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.36339037729060941310236457370419:50001231000000:2800:8C155ACE210BDE7C6802FB245C677A8FE4557D16A9BA50304434C2AE281FFEC2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.78034732602161888670498514427605:50001231000000:2800:099558124C037F2BA27EFFAC80BAB0C60F967ADAC95C43B55095BCB52F59E009.png?needInitFileName=true?needInitFileName=true)
-  实时监控界面部分泳道内的图例均支持选择/反选来增加/去除泳道内这一数据的展示，内容改变后泳道内的数据会自动缩放以适应泳道的高度，能够更加专注地分析所关心的数据。
至此，通过分析实时监控的多维度设备数据，可以了解到当前设备的具体运行情况以及可能出现性能问题的热点区域。接下来，可以通过深度录制更加详细的设备侧运行数据来更加详尽地分析应用可能存在的性能问题。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/deep-recording-V14
爬取时间: 2025-04-30 08:42:52
来源: Huawei Developer
创建深度分析任务并进行录制
开发者可针对不同的性能问题场景选择不同模式的分析任务，对应用/元服务进行深度分析。当前支持以下调优场景为：
1.  新建任务的入口，DevEco Profiler提供Launch、ArkUI、Frame、Concurrency、ArkWeb、Network、Time、Allocation、Snapshot、CPU等场景化分析任务类型。 ：在设备列表中选择设备。 ：在进程列表中选择要调测的应用（可以是正在运行的应用，也可以是已安装但未启动的应用）。 ：在DevEco Profiler主界面的新建任务区域，单击要创建的场景调优分析任务类型，并单击“Create Session”。创建后的分析任务，会显示在界面左侧的任务列表中。 ：调优详情，显示具体的调优内容。
2.  在右边录制详情区域，工具控制栏上有很多小图标，鼠标放上去会有一些功能提示，可以添加一些录制选项，各泳道区域也有下拉框选项，下拉选择不同的设置可以调整录制功能。
3.  单击任务窗口左上角的，启动录制，也可以选择左侧的任务列表中的，启动录制后，等待任务状态由“initializing”变为“recording”。录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板可以结束本次录制重新选择其他模板开始录制。
4.  在调优设备侧操作APP，执行要验证的操作，复现设备性能问题。单击该任务的停止按钮，进入数据分析阶段，所有泳道任务状态由“analyzing”变为“rendering”，分析结束，右侧调优详情区域显示具体调优内容，分析过程可能包含大量的数据，需要等待一段时间，请耐心等待解析完成。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.23261827172490182140296503152057:50001231000000:2800:C3ED2D0DAD1EAB8E89B64AA25E77F530BA4090D2D6922824E3B9CC507E3598F1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.26525783249060655491025045800528:50001231000000:2800:05655175C2664747E9D43810479F2DF056C73AC5A3D5FAA7C9326CB169E3D937.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.63729140909903057343716069107947:50001231000000:2800:C849E8CBCCCE9ED9E86AF7C276A66D26DD3EDA1778B4E04E8573767E3BECB3F4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.74629063986119101499773387093629:50001231000000:2800:2A7131126D8580C0C2465D6AF16394D3E41CAD00F7E65916C95D46FF3BAB8C5C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.41479676677678491883045967201671:50001231000000:2800:828D7B0E4EC5C12290DA445413C902AB953AB03B853CD80E21BBED7A343593F9.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.92927600902106974596699767273818:50001231000000:2800:9FDA740083F6AA80712CD24739C1303AC4491490CCABE8671E624FE12B14669F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.32650906890294544589282799679357:50001231000000:2800:2B0C8D4DFAE7DD94A2320314B6456924BB173EAECFC08ADFFF9A88267E89476B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.45396136842608432106402760656037:50001231000000:2800:23CD20FDCFDEB04092CE1699BE009C54E16D7FE912BBBC54795CF82089ED22B5.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.65073260608185571876336260508141:50001231000000:2800:74F4F19F8FBC8C74C822BBE4DAA9F8D3144553BF6A69041F9B40201A26D1152E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.87663602617356039464883442040844:50001231000000:2800:3777967ADA924D64AB14B34EEBDF7BBB9B3ED9E719D899D4AD75707A50C8BE7C.png?needInitFileName=true?needInitFileName=true)
当前的ArkTS Callstack/Callstack/Native Allocation/ArkTS Allocation泳道录制如果无值，泳道显示No Data，在泳道名称处可将光标悬浮于三角告警图标处，查看泳道报错的原因。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150734.88444850951826055852550168454537:50001231000000:2800:BD1EAB29E9D04488186FF409A925C0030950CA698B8FC5DDF73A9C1CC7EE556F.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-time-V14
爬取时间: 2025-04-30 08:43:27
来源: Huawei Developer
函数耗时分析及优化
开发应用或元服务过程中，如果遇到卡顿、加载耗时等性能问题，开发者通常会关注相关函数执行的耗时情况。DevEco Profiler提供的Time场景分析任务，可在应用/元服务运行时，展示热点区域内基于CPU和进程耗时分析的调用栈情况，并提供跳转至相关代码的能力，使开发者更便捷地进行代码优化。
在设备连接完成后，可按照如下方法查看耗时分析结果：
1.
2.  Time分析任务支持在录制前单击指定要录制的泳道： 调用栈分类从语言层面分为ArkTS、NAPI以及Native，从归属层面分为开发者代码以及系统代码。从这两个方面可以将调用栈类型归类如下： 其中每一个类型的亮色和灰色分别代表开发者和系统的代码。 Callstack基于采样模式采集数据，默认采样间隔是500微秒。耗时小于500微秒的函数，Details区域时间相关数据可能存在误差，可通过录制过程中多次触发该函数，根据其耗时百分比判断是否为热点函数。
3.  调用栈分类从语言层面分为ArkTS、NAPI以及Native，从归属层面分为开发者代码以及系统代码。从这两个方面可以将调用栈类型归类如下： 其中每一个类型的亮色和灰色分别代表开发者和系统的代码。
4.  其中每一个类型的亮色和灰色分别代表开发者和系统的代码。
5.  Callstack基于采样模式采集数据，默认采样间隔是500微秒。耗时小于500微秒的函数，Details区域时间相关数据可能存在误差，可通过录制过程中多次触发该函数，根据其耗时百分比判断是否为热点函数。
6.  Details区域会显示所选时间段内的函数栈耗时分布情况，Heaviest Stack区域会展示出“Details”区域选择节点所处的耗时最长的完整调用栈。 其中函数栈耗时分布有两种展现方式：
7.
8.
9.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.73048767740263574317038693587935:50001231000000:2800:DC13412C5CB13ACEC1D6A70B664EA39430CF5E3A909CCA4A91018E9CAE292036.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.88246860759720067303429955093869:50001231000000:2800:D7096B7A3232012C8E322CF13087F778F883B17D126A52B9D71368D5AF6F9861.png?needInitFileName=true?needInitFileName=true)
-  调用栈分类从语言层面分为ArkTS、NAPI以及Native，从归属层面分为开发者代码以及系统代码。从这两个方面可以将调用栈类型归类如下： 其中每一个类型的亮色和灰色分别代表开发者和系统的代码。
-  其中每一个类型的亮色和灰色分别代表开发者和系统的代码。
-  Callstack基于采样模式采集数据，默认采样间隔是500微秒。耗时小于500微秒的函数，Details区域时间相关数据可能存在误差，可通过录制过程中多次触发该函数，根据其耗时百分比判断是否为热点函数。
-  其中每一个类型的亮色和灰色分别代表开发者和系统的代码。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.18953492387452594511454880884041:50001231000000:2800:CF055D441011184BFA6B418E8BD77F28F5DB7601381B80EB89BF49C0F5D39C39.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.08155730220313899718315874656341:50001231000000:2800:AA0A60341D0F60B25C2700941B9011B58C12CF2AB07A3DADE0792BE9F82438F2.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.68655797140885845549419683684067:50001231000000:2800:952A8D8ADD07C99FFBD9D27FA5807625D3E03406B63DCA661B51A438205D1955.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.09148653547325511584105312720919:50001231000000:2800:4C590DA9914C902BA0E796C4FE4E587B5D36FB7CE9C39BA57299E287F031BA91.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.17526142577510596792390057101316:50001231000000:2800:D9E0BBC05E25B3F609B7EAEE6FB13F487A284BE90D0BE2E4DADE2D2B26D7447A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.41657913277753290786773448844923:50001231000000:2800:4349E22114068EA93F352B14EE5ABDEE430D702DFE43B6F967D3D44BC6E891B0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.10378296404011698681948902090020:50001231000000:2800:4BE5DC2BDC91EB83BE3ED2D1BCB8ED0CBB0325759D51020466CF6D7499DACA2B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.24184394523128521880686228954012:50001231000000:2800:FB51D0EB764FB768F0F2A3F06E6C55FBF693B92E164D56A1415F12526365BE3E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.17256480441661047257598935453892:50001231000000:2800:C9984B3CF559F9D4428087F987E89F71A7B56DC13C0790856204CC47B1F167D5.png?needInitFileName=true?needInitFileName=true)
多实例函数热点分析
在应用开发过程中，可能存在一些耗时操作，则需要引入Worker线程或者TaskPool任务池来协同处理。这些线程也可能会像主线程一样存在性能问题，所以需要同时对这些子线程进行性能调优。其中，主线程以及每一个Work线程或者TaskPool工作线程，都会对应一个方舟实例，通过连接这些方舟实例，开启性能采样，从而可以获取更全面的采样信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.76939842588007511610421862722881:50001231000000:2800:B0B9A2CB54C1D00D74D1A004FFDA24B39723CEA3311DC7FD51047D3AAE5F1034.png?needInitFileName=true?needInitFileName=true)
离线符号解析
DevEco Profiler提供离线符号解析能力，基于携带符号表信息的so库进行分析，可把符号地址解析为具体函数名称，便于定位函数位置。
对于有so库路径和偏移地址的采样数据，如图所示，通过导入对应的携带符号表信息的so库进行解析，补充release so库中缺失的符号表信息（包括系统so库，用户自编译的so库，三方库）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150735.45594849486356940822991965132846:50001231000000:2800:09AA385385CA9A29D9CF5026D36388A4A9630E7E2DDB084EC4515C308BE9BCEE.png?needInitFileName=true?needInitFileName=true)
您可以通过点击工具栏按钮，导入包含debug信息的so库。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.21527287120259280518577998385804:50001231000000:2800:E1332376E3DF5ACC2E325728EE5B2BE6BCAC22A3E741960C2EEC6595F1CD4A90.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.49276130952666916051496221986469:50001231000000:2800:2B94E0F0C8F2E7ACAE6E8AFA35974117B643D5835E41CB2A0422BD58181448D7.png?needInitFileName=true?needInitFileName=true)
查询自定义打点信息
相较于异步调度，DevEco Profiler当前基于采样分析的Time任务更善于分析同步性能问题。如开发者需要分析异步调度延时等问题，可先在ArkTS代码中进行自定义打点，当元服务/应用在Time分析过程中触发打点后，DevEco Profiler会将这些打点的Trace数据解析后，以任务方块形式呈现在“User Trace”泳道中。
您可以在“User Trace”子泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，获取该时间段内的用户打点信息。
单击User Trace泳道的“options”下拉列表，可以设置是按照Task Name维度还是Thread ID维度显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.16704478987128939427168320763454:50001231000000:2800:0B8ADE952F6832336FE197E024D69B20E5CDA1DE8B9EFBE1D770E9A1D826AEB0.png?needInitFileName=true?needInitFileName=true)
同时，您也可以单击“User Trace”子泳道中的任意一个任务块，“Details”区域将展示该任务块的详细信息。
此外，用户自定义打点信息，还可以在Frame分析、Network分析任务中查看到。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.25069502321858429346224873679489:50001231000000:2800:9893D28F7FD4B0579F7D220B1DDDB4F2C5C19723FB85318B5070E59E68C7E8FF.png?needInitFileName=true?needInitFileName=true)
能耗分析
DevEco Profiler提供Energy泳道，旨在帮助开发者了解应用能耗的构成，结合应用生命周期，识别潜在能耗问题。
鼠标悬浮在Energy泳道数据上，显示器件能耗使用情况。器件包含：CPU、*Display、GPU、Location、Camera、Bluetooth、Flashlight、Audio、Wifi、Modem。框选Energy泳道数据，Details中呈现框选时间段内的详情信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.82020347360554178180322884093192:50001231000000:2800:35EB9A99816C85B73B609152DDFA75CEACAD800E9975A70CE5FF95D6ECB56828.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-allocations-V14
爬取时间: 2025-04-30 08:44:01
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-allocations-memory-V14
爬取时间: 2025-04-30 08:44:36
来源: Huawei Developer
应用在开发过程中，可能会因为API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。
DevEco Profiler提供了基础的内存场景分析Allocation，您可以使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。
在设备连接完成后，可按照如下方法查看内存分析结果：
1.
2.  PSS：进程独占内存和按比例分配共享库占用内存之和。 RSS：进程独占内存和相关共享库占用内存之和。 USS：进程独占内存。 默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。 展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Gurad/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。 由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道。 单击工具控制栏中的按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。默认采用统计模式，统计间隔只在统计模式下才需要设置，可设置范围为1s~3600s，默认为10s，默认最小跟踪内存为1024Bytes。FP回栈模式下需要设置JS回栈深度和Native回栈深度，DWARF回栈模式下仅需要设置回栈深度。默认Native回栈深度为10层，JS回栈深度可配置范围为0-128，默认10层。设置完成后，在录制期间小于此大小的内存分配将被忽略，最大回栈深度将达到设置的值。
3.  PSS：进程独占内存和按比例分配共享库占用内存之和。 RSS：进程独占内存和相关共享库占用内存之和。 USS：进程独占内存。 默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。 展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Gurad/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。
4.  由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道。
5.  单击工具控制栏中的按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。默认采用统计模式，统计间隔只在统计模式下才需要设置，可设置范围为1s~3600s，默认为10s，默认最小跟踪内存为1024Bytes。FP回栈模式下需要设置JS回栈深度和Native回栈深度，DWARF回栈模式下仅需要设置回栈深度。默认Native回栈深度为10层，JS回栈深度可配置范围为0-128，默认10层。设置完成后，在录制期间小于此大小的内存分配将被忽略，最大回栈深度将达到设置的值。
6.  Details区域中显示此时间段内指定类型的内存分析统计信息： Graph字段统计方式为：计算/proc/process_dmabuf_info节点下该进程使用的内存大小。 “Details”区域中带标识的对象，表示其可以通过窗口访问。每个时段内已释放的内存大小在柱子上置灰，未释放的内存保持绿色。 点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。 统计模式（Statistics Mode）下不存在Allocations List信息。 选择任一对象，右侧会展示与该对象相关的所有库和调用者。
7.  Graph字段统计方式为：计算/proc/process_dmabuf_info节点下该进程使用的内存大小。
8.
9.  Graph字段统计方式为：计算/proc/process_dmabuf_info节点下该进程使用的内存大小。
10.  “Details”区域中带标识的对象，表示其可以通过窗口访问。每个时段内已释放的内存大小在柱子上置灰，未释放的内存保持绿色。
11.  点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。 统计模式（Statistics Mode）下不存在Allocations List信息。 选择任一对象，右侧会展示与该对象相关的所有库和调用者。
12.  点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
13.  统计模式（Statistics Mode）下不存在Allocations List信息。 选择任一对象，右侧会展示与该对象相关的所有库和调用者。
14.  Release应用暂不支持跳转到用户侧Native代码。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.18324109046108832454160018122641:50001231000000:2800:564F03E8A75B2DDC37B2F40E9199833EC6D3A889D15743CC2869675336E59674.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.14688737233168338889444175890125:50001231000000:2800:DBFDA4E906095FBB1F6BB794D2AC7B0D9DFB9AA38CA28976F9DB780A1A9E84F6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.64816898150241962429354650648856:50001231000000:2800:7A5AB1AB296C106438016EC3FFD305786F46F7F1C309690C7076BC599EBEF6D0.png?needInitFileName=true?needInitFileName=true)
-  PSS：进程独占内存和按比例分配共享库占用内存之和。 RSS：进程独占内存和相关共享库占用内存之和。 USS：进程独占内存。 默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。 展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Gurad/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。
-  由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道。
-  单击工具控制栏中的按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。默认采用统计模式，统计间隔只在统计模式下才需要设置，可设置范围为1s~3600s，默认为10s，默认最小跟踪内存为1024Bytes。FP回栈模式下需要设置JS回栈深度和Native回栈深度，DWARF回栈模式下仅需要设置回栈深度。默认Native回栈深度为10层，JS回栈深度可配置范围为0-128，默认10层。设置完成后，在录制期间小于此大小的内存分配将被忽略，最大回栈深度将达到设置的值。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.23198095317081914553261479568886:50001231000000:2800:9CD9D9B178D344A911A23DA762F585F85DFA69F7865012DA175C7698D97FB7FF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.62060598659180912128453676250212:50001231000000:2800:1CD6B4020E84BA08D35DEDD737F7453BEF3E3AE84F02F85D26372BA963C0E5DE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.79780100871047413419118285952938:50001231000000:2800:9DF08CEB7BDDC0DD8EF9AA5068EF51CF9AEBCD1058F33A81924D8B9848413C46.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.04050429958094897987087593105392:50001231000000:2800:96360C8907DC0C5976A752917CC649D79BB0F84942E2C82DF71D94A5F97918C7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150736.95858093184403206577196672763946:50001231000000:2800:6E0764082C1A35D81C967BD6F1F837ECB1633941B423BE1419B1F7D883F4E4E0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.67286305652415937304270539538272:50001231000000:2800:1AB998005550BF1B7918E45E708379768F7138A03FEDF4E6736235B0399FC304.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.56691273016614638478527577428837:50001231000000:2800:3B7634D3853F167B8E3ADC9E0963146BB0E968F0436DB725B3A75AFBE05A5AD3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.98807845446830258897635431048575:50001231000000:2800:5A744AFB76C2F243700BDA647EFCEE8D9648B1E04BD38ECE9558BA91C7128C77.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.47719849831617650719657444559947:50001231000000:2800:9BC7C9A533C3C7B52179EFCE14ACD49715C3433CF07E870666FC874063BCAF38.png?needInitFileName=true?needInitFileName=true)
-  Graph字段统计方式为：计算/proc/process_dmabuf_info节点下该进程使用的内存大小。
-
-  Graph字段统计方式为：计算/proc/process_dmabuf_info节点下该进程使用的内存大小。
-  “Details”区域中带标识的对象，表示其可以通过窗口访问。每个时段内已释放的内存大小在柱子上置灰，未释放的内存保持绿色。
-  点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。 统计模式（Statistics Mode）下不存在Allocations List信息。 选择任一对象，右侧会展示与该对象相关的所有库和调用者。
-  点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
-  统计模式（Statistics Mode）下不存在Allocations List信息。 选择任一对象，右侧会展示与该对象相关的所有库和调用者。
-
-  Graph字段统计方式为：计算/proc/process_dmabuf_info节点下该进程使用的内存大小。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.91726057902138855968698554408839:50001231000000:2800:34EC15F3ED797E515510C3ECD533DE6B25CB9E6C3FF6448336337D21B8E3AACA.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.62794139724856448499456044460223:50001231000000:2800:969E14E482A68B68B1FC582EA91C87858F0F0B0E4C6C9FC9DC4DE640D4FD4D6A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.57485191399013892289188837873469:50001231000000:2800:14C2181BCF4923DCD8908A122E559D433D2DB3BCB254FC80C6C035238C9444C1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.36842786776276588645131842461125:50001231000000:2800:D4A387601BA2576504AD7832BA082DBEF68FA2C1109C9320E421ED3BFE10892D.png?needInitFileName=true?needInitFileName=true)
-  点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
-  统计模式（Statistics Mode）下不存在Allocations List信息。 选择任一对象，右侧会展示与该对象相关的所有库和调用者。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.94360329109382050774415687893756:50001231000000:2800:D371534C12F91A966E77D063F9EFD2B1240DD7DFEA1F03FDDE4C8E642B4F7E19.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-allocations-data-filtering-V14
爬取时间: 2025-04-30 08:45:10
来源: Huawei Developer
Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。
通过内存状态筛选
在Allocation分析过程中，对“Native Allocation”泳道的内存状态信息进行过滤，便于开发者定位内存问题。
在“Native Allocation”泳道的“Detail”区域左下方的下拉框中，可以选择过滤内存状态：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150737.92363645225997656539721419741058:50001231000000:2800:E344896E775E35224CF6E75F5F84727E3358849D2B93CC6A1A7F0C2E7A1E57C7.png?needInitFileName=true?needInitFileName=true)
通过统计方式筛选
在“Native Allocation”泳道的“Statistics”页签中，可以打开“Native Size”选择统计方式以过滤统计数据：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.20704810653140942101400955290993:50001231000000:2800:D30C94A90912646AA4D234BF320CA36C8EFCC131D738A47CB6A30C02FA0B31E4.png?needInitFileName=true?needInitFileName=true)
通过so库名筛选
在“Native Allocation”泳道的“Allocations List”页签中，可以单击“Click to choose”选择要筛选的so库以过滤出与目标so库相关的数据：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.47175297095062264718187913147058:50001231000000:2800:3B02151E01F5FC9D05AEB47BC71E8AC3B8E44F9E653103210D64F72DD41ACB7B.png?needInitFileName=true?needInitFileName=true)
通过搜索筛选
在Native Allocation泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的<、>按键可依次显示搜索结果的详细内容。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.07171326241488894391418549227674:50001231000000:2800:88483313670BDF58E47E09C821D4E446A0CD863BCA90A416E152ADC4DED29223.png?needInitFileName=true?needInitFileName=true)
筛选内存分配堆栈
在Native Allocation泳道的Call Trees页签中，可以通过底部的“Call Trees”和“Constraints”选择框来过筛选和过滤内存分配栈。
Call Trees选择框包含两种过滤条件：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.39196382785670426107573140000386:50001231000000:2800:8CABF2B118C1C00A9EBC81B86085A0E63A9984EE766206EDCAD32338E4220B40.png?needInitFileName=true?needInitFileName=true)
Constraints选择框也包含了两种过滤条件：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.02004408549867909749778007331234:50001231000000:2800:A5D3AF696D4426576A307DE686E8A932512100C4037C52D9834CBC71431793BA.png?needInitFileName=true?needInitFileName=true)
在Call Trees页签的More区域，单击“Heaviest Stack”旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.90685744001659870187580352686418:50001231000000:2800:8FE053B8DE7803CE15164522D3C49590C2B217DDE32009E70AB9BFA02839CA97.png?needInitFileName=true?needInitFileName=true)
在Call Trees页签，可以通过底部的“Flame Chart”切换到火焰图视图。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.64553653807033183501813032146302:50001231000000:2800:4C3BDC37E145D5021150C1A79DBF8899E2BE6317364F5239E45843A3B3B65EAF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-boot-memory-V14
爬取时间: 2025-04-30 08:45:46
来源: Huawei Developer
应用/元服务在启动过程中对内存资源的占用情况，是开发者较为关心的问题。DevEco Profiler的Allocation分析任务，提供了启动内存分析能力，协助开发者优化启动过程的内存占用。
具体操作方法为：在任务列表中单击Allocation任务后的按钮。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.32958117796594313160849043501391:50001231000000:2800:4AD1FA9EE751325F145CAB410134B86416356C3D804C0516A90AD95ADC16FBB4.png?needInitFileName=true?needInitFileName=true)
在分析结束后，呈现出的数据类型以及相应的处理方法，与非启动过程的分析相同。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-snapshot-V14
爬取时间: 2025-04-30 08:46:20
来源: Huawei Developer
针对方舟虚拟机，DevEco Profiler提供了内存快照分析能力，结合Memory实时占用情况，分析不同时刻的方舟虚拟机内存对象占用情况及差异。
由于隐私安全政策，已上架应用市场的应用不支持使用Snapshot分析模板。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-snapshot-basic-operations-V14
爬取时间: 2025-04-30 08:46:55
来源: Huawei Developer
查看快照详情
1.
2.  单击任务左上角的进行泳道的新增和删除，再次单击此按钮可关闭设置并生效。
3.  “ArkTS Snapshot”泳道的紫色区块表示一次快照完成。 在“Statistics”页签中显示当前快照的详细信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.92944531022058598858791206631864:50001231000000:2800:A609FA8A2C8413E801B7E4A1818F49D995F9305E894CE35EE6EFB981A69BB4E8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.08168973522660115926097862660713:50001231000000:2800:17131EF345B37B4E2AEDB1A174242BA964B9C6AAD1AF998A101F731D381AE662.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.84734113277577566391821409178316:50001231000000:2800:DFD0B099AD169C38E172FE452D1CADE2FE1B9143190D920AB561A30A01DCFC2C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150738.52161997927400521672298982619537:50001231000000:2800:96F44E6B3075B4B3FF0CDD5B641726F0DA2E5EA3C14D6EC46124BED67B5C2AC3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.13985381917023440554562210090985:50001231000000:2800:C42316499411ED865C15DA972947C21A7E58B5FBC1FBB2399078CDC103DFEA72.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.69232865537524498511943405156130:50001231000000:2800:179E1B736138505C30616C35EE63955D941510285DF1E5F088D0DB3905031587.png?needInitFileName=true?needInitFileName=true)
节点属性与引用链
在“Snapshot”的“Statistics”页签和“Comparison”页签中，所有实例对象节点展开后会显示"<fields>"以及"<references>"，这两项节点分别代表该实例对象的属性以及该实例对象的引用链信息。
在“Snapshot”的More区域则展示“Fields”和“References”两个页签，分别代表Detail区域所选择对象的属性以及引用链信息，方便快捷查看所选中对象的属性等详细信息，而不需要跳转至对应对象。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.75453468473501464702879435686725:50001231000000:2800:6A2B4FDCE31EF45A99C4AA4BEA339AC7346ACC1952673DD004DDFD73CC5D4698.png?needInitFileName=true?needInitFileName=true)
节点跳转
在“Snapshot”的“Comparison”页签中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的“Statistics”页签并定位至该对象所在的位置，以查看该对象的详细信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.77320825214867836030632127022659:50001231000000:2800:3E4171A9A8E59135CAF18B7BF268AD34B3BA5FA0137677BB2E6B5AB2DEC61F59.png?needInitFileName=true?needInitFileName=true)
历史节点前进/后退
当在“Comparison”和“Statistics”之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.04210842500716950394491882235379:50001231000000:2800:87E319BECB7813CF1FFBADD9EA77493EF14453AC83E0875D30F791CAC07C75E7.png?needInitFileName=true?needInitFileName=true)
比较快照差异
在“Snapshot”的“Comparison”页签中，以当前选择的快照为base，下拉框选择的快照为Target，即可得到两次快照信息的比较结果。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.28239167434688305132681572719156:50001231000000:2800:1084B807985CC8DC44B993435E5680BD1D180CA0AEB06B1AE5AA2D2E5978E945.png?needInitFileName=true?needInitFileName=true)
在“Snapshot”的“Comparison”页签中，可进行两次快照的差异比较，比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.66587774619208687300604293522569:50001231000000:2800:C5D47C59E1E47C4C66617FF7E597889F1A7E6F21AA59C9A0E05A8DFDE875286E.png?needInitFileName=true?needInitFileName=true)
Heap Snapshot离线导入
DevEco Profiler提供Heap Snapshot离线导入能力，可导入一个或多个.heapsnapshot文件。
您可以在DevEco Profiler主界面的“Create Session”区域中，单击“Open File”，导入.heapsnapshot文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.20093595558577287305910439342518:50001231000000:2800:0241EF25B4FE73A016BA0626C9085EBBFF383C74E914D51695AE9AAF83A188D0.png?needInitFileName=true?needInitFileName=true)
可以导入与heapsnapshot文件匹配的.jsleaklist文件，展示jsleakwatcher监控采集到的内存泄漏对象。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.86352071933415208831291802427617:50001231000000:2800:B6354395BDA6A5D87D643E26FC87776B8FBD1A23CADC9BA1A5C4D013523A33C4.png?needInitFileName=true?needInitFileName=true)
Raw Heap离线导入
DevEco Profiler提供Raw Heap离线导入能力，可导入一个或多个.rawheap文件。
单击“Open File”，导入.rawheap文件后以下图所示形式呈现。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.23536326164204713975548882998066:50001231000000:2800:31E326B0D33A5868E3D70146F26326D9ABC84701B3768886FAF90A306C7C36EF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-arkts-memory-leak-analysis-V14
爬取时间: 2025-04-30 08:47:29
来源: Huawei Developer
分析步骤
分析内存泄漏问题步骤如下：
录制Snapshot模板数据
1.
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.70033134660647819669843701915193:50001231000000:2800:B14F1273FDBBEBB2C89F04D33A056729523B54D62D4302484507D6F746A91C72.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150739.54708029602491893378057408968272:50001231000000:2800:1D5AC12A4F82E70ABA353B029DEF097A0109BE41E2E794B2D8ECAC18C2DD4A20.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.80451834079457596458790846984668:50001231000000:2800:5CBB80EB2884BF43229DE9DD4C1943861D8BB53CE8D80ECFC4FA43738BB15D91.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.11141364071099611640336846301331:50001231000000:2800:0BDFA31CDCE3BEA8ECE06E93CF6A7B652B82BC8ABD56225683166F105980B8DF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.36553633479361638498510687427672:50001231000000:2800:E30089E2DD9ECB8BA42E3AB5D10973A6524A9AB9255744E08A10563CD25762DD.png?needInitFileName=true?needInitFileName=true)
分析Snapshot数据
常见对象介绍
JSArray
目前所有JSArray展开后为数组里的各个元素：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.78701178248770932246754403647731:50001231000000:2800:29D19EF41039B221D3CD2970AC36AF8C9656BCBD1CCBB7C3F6120152BACC7787.png?needInitFileName=true?needInitFileName=true)
其中_proto_：原型对象，所有数组的_proto_应该是一致的；length：内置属性访问器，可以访问数组长度。
TaggedDict
位于(array)标签中，一般为虚拟机内部创建的字典，ArkTS代码层面不可见。
TaggedArray
位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。
COWArray
位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。
JSObject
JSObject展开后为内部的各个属性如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.55233385682247329725654507707695:50001231000000:2800:5B2AF13FB74C9233400B68106BABA3F8C3E2703C32AC11A23424791A01BEE32A.png?needInitFileName=true?needInitFileName=true)
以下通过具体代码来介绍下实例化对象、声明对象、构造函数间的关系：
```typescript
class People {
old: number
name: string
constructor(old: number, name: string) {
this.old = old;
this.name = name;
}
printOld() {
console.log("old = ", this.old);
}
printName() {
console.log("name = ", this.name);
}
};
let p = new People(20, "Tom");
```
采集到的snapshot数据如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.25779992197094545895016815777617:50001231000000:2800:E53724595AC2B275EA5C0F96E3B86EB3FE77D53A9C5584A369774E00A0816829.png?needInitFileName=true?needInitFileName=true)
92729对象对应的是People，其主要声明了对象的属性和方法。
实例化对象的_proto_属性指向声明时的对象，声明对象里则会有constructor构造函数。当实例化多个对象时，实例化对象会有多个，但是声明对象和构造函数只有一个。
JSFunction
目前所有JSFunction都在(closure)标签中，展开即可看到所有JSFunction：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.82449205437703208509553998291840:50001231000000:2800:A5C7799C17E7F35F65DB9454C799C33EFE569161AB85C9BC22C13337E3DA3921.png?needInitFileName=true?needInitFileName=true)
每个函数展开后为函数内的各个属性：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.93839312038828334636562249144858:50001231000000:2800:BA318591E224873C1565B0CD68CDBD5CF16B7F55CD746E4EA1CBB6150CB6C6B8.png?needInitFileName=true?needInitFileName=true)
其中HomeObject表示父类对象，即该方法属于哪个对象；_proto_表示原型对象；LexicalEnv表示该函数的闭包上下文；name是内置属性访问器，可获取函数名；FunctionExtraInfo表示额外信息，比如一些napi接口会在这里记录函数地址；ProtoOrHClass表示原型或者隐藏类。
如果函数显示为anonymous()，则表示为匿名函数；如果函数显示为JSFunction()，则表示该函数可能为框架层函数，创建函数的时候未设置函数名。对于这两种函数名不可见的情况，可以通过查看其引用来间接确认其名称：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.54560361182297889104786725970647:50001231000000:2800:69B2167F9EE01E52D32ECE079EAD168C2C8EF48800E6E1E6173EB1354575D58E.png?needInitFileName=true?needInitFileName=true)
ArkInternalConstantPool
虚拟机创建的常量池，ArkTS代码层面不可见，涉及到的字符串常量会在(array)标签中展示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.93557726559855328921427484503676:50001231000000:2800:CAFCC9F3BB35FD23867818DB21FA337B5125FFBAB51C8A2D4690EAB80FA20E67.png?needInitFileName=true?needInitFileName=true)
LexicalEnv
闭包变量上下文；闭包是一个链状结构，如下所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.85039641201989653450914206827672:50001231000000:2800:10FCF619542DECD95D087E4BE0DEC51D46FD30F1297ED69DAA5D44A6DB56C9E6.png?needInitFileName=true?needInitFileName=true)
733这个节点本身是一个闭包数组，其中0号元素是调用者（或者再往上的调用者，以此类推）的闭包；1号元素存储的是调试信息；2号及以后的元素存储的就是闭包传递的变量，上例传递了一个变量。
InternalAccessor
内置属性访问器，会有getter和setter方法，通过getter、setter可以获取、设置该属性。
分析方法
查看对象名称
对于声明对象，可以通过constructor属性来确定对象名称。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.92429814743345238387728178377552:50001231000000:2800:490720E462546F172AC37E4B50EE06075DA9F30A8C384CE454AA855588F5B2D7.png?needInitFileName=true?needInitFileName=true)
对于实例化对象，一般没有constructor，则需要展开_proto_属性后查找constructor；
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.68700201168354834265406974334280:50001231000000:2800:7F9EEB82A4A4EDBACBE0DA16E8D9CE17BA1D6CD0112090A3C9121D17E2F1446C.png?needInitFileName=true?needInitFileName=true)
若对象里有一些标志性属性，可以通过在代码里搜索属性名称来找到具体是哪个对象。
如果对象间有继承关系，则可以继续展开_proto_：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.48619042138811267105301212604286:50001231000000:2800:95FF184A14979C58F8F2F24EEA8E9CCB47ECA1C781AF4F61EF0CF5C5A2F96232.png?needInitFileName=true?needInitFileName=true)
如上图则表明Man对象继承自People对象。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-cpu-V14
爬取时间: 2025-04-30 08:48:05
来源: Huawei Developer
开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。
查看各CPU使用情况
1.  CPU分析任务支持在录制前单击指定要录制的泳道。
2.  可在“CPU Core”右侧的下拉列表中选择显示内容： 框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息，以及所有时间片的数据统计信息。
3.  将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。
4.
5.
6.
7.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.26706748008691483265135772947882:50001231000000:2800:82F8CE6260E6729F13B353B592E78CDA2FE0E23C9AF215C254EF8FE1F440F569.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150740.71085952463911906956524386262992:50001231000000:2800:C2B2274E232A11110E13E86E55A95036FFC8ED7FB54666A58B6E4FB6C88EB40D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.38370246729445090994672956462406:50001231000000:2800:B7C3308F41D97578D00E790FD247C953373400E0460D5E11799EB5F54AF208A0.png?needInitFileName=true?needInitFileName=true)
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.79549691864256747858410696931965:50001231000000:2800:DC5ADCF94A249717AB81D50F8720E5BFD0E0CA395D2BDD25A42978B070C962E8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.07224477244026212446957790451245:50001231000000:2800:9599BE1DA09DAA419FDFFCED0239C891B4E82EC2628EC7EF98C8A10AF9A740D3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.92683446044962638660851911852573:50001231000000:2800:DC229DB3D74A5FD3965BC02A7DFAC352E57E7B15076E020F8531AD6888FAD5A8.png?needInitFileName=true?needInitFileName=true)
查询进程详情
-
-  中载重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。
-  并行度（Parallelism）取值范围是[1, cpu核数]，数值越小代表并行度越低。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.00368832223435587324422489960652:50001231000000:2800:650FD995750BA9F3FF346B50051132426F4E41475887E6727324A5C8D04D47BC.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.75430048376685869582049693560328:50001231000000:2800:F4F9BF70E49BE7E8A9763CD996D3E72EB4E8BFA6166372542EAF06724A491A31.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.09319316799756458121227028013305:50001231000000:2800:7394C0360B7A57CC916D41AF02F5EFA8528B6E1F55F6EF2DC190C02A0D8BEE12.png?needInitFileName=true?needInitFileName=true)
查看Trace详情
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.87742159790534227563217571487213:50001231000000:2800:D77C1519BA22B67051AC0FA49846CD8EDDFB425B468C7AF7541AA7330CED797B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150741.26096297265979887304876506880855:50001231000000:2800:0F91BB31DE0DD78702C4806240C76485C142BE0DC48D25386658D3995DBA13E8.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-lag-and-frame-loss-V14
爬取时间: 2025-04-30 08:48:40
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-frame-V14
爬取时间: 2025-04-30 08:49:14
来源: Huawei Developer
开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据进行分析，从而识别出导致卡顿丢帧的原因所在。此外，Frame任务窗口还集成了Time、CPU场景分析任务的功能，方便开发者在分析丢帧数据时同步对比同一时段的其他资源占用情况。
查看GPU使用情况
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.96650535945991293241532912570011:50001231000000:2800:7DB27CE1F2C0B7390058627777EC9DCC828C058DA25BCA5DD7AB3CD19BC823F1.png?needInitFileName=true?needInitFileName=true)
查看指定时间段内所有进程的Frame数据统计信息
1.  窗口下方的“Statistics”区域中会以进程为维度对选定时间段内的Frame信息进行统计，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.97838932184806729800171778449964:50001231000000:2800:C1B9B5C2813F59D517A7A9C0FC9C8EBA3D2ACEEBAB6C9A0972AB194C1F34AD20.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.66201751047546762527119692187017:50001231000000:2800:CEC0B0763E6E5FEFDCBC4B9E2FEC96F179B7D410A1B5CDD0923ABF0988A2E747.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.65429573742712273277206122081904:50001231000000:2800:D3B2134607BF7589CB29F74BA0BC5AAB7FB879BEADA7CE842967D87E848043C9.png?needInitFileName=true?needInitFileName=true)
查看指定时间段内指定进程的Frame数据统计信息
1.  窗口下方的“Details”区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.74770265370045457132051585038396:50001231000000:2800:8C55F5D08C5D9A3C997771A01952651D770B61B8904DEAD0E8B19C3C34C344C4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.07303317186127997710241179707087:50001231000000:2800:93C9D7A3085080B68EFD42A4269C49562DB75C150805468EEEDEE289A04319E2.png?needInitFileName=true?needInitFileName=true)
查看指定Frame信息
在子泳道（例如带“APP Frame”标签的泳道）中选中要查看的Frame，该泳道上方是耗时最长的非UI函数，下方是UI主线程泳道。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.47466238650761220656668338961239:50001231000000:2800:705C803ABD7FAEEBCB95E01218083A501597CC391A750F2AF66E1219BEABF40B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.29121039176778918177512193234378:50001231000000:2800:3248C3602B7D8080CB1061D55D328D7A0ADBAE9EF3E817123E065EE1430E8425.png?needInitFileName=true?needInitFileName=true)
查看屏幕帧率动态变化场景下丢帧和卡顿信息
Frame泳道下新增Lost Frames和Hitch Time两类子泳道，用于识别和优化卡顿和丢帧现象。
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.91884161657112720137021597234668:50001231000000:2800:0AC9CB6EB8BD5E6D154DD517811C81A24CB22D1A2A47736E4BF2ED1E4D03A4F2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.27909944925121739397784527861134:50001231000000:2800:4A162585CCF480A06AA18F3C67338AC8BF890D4AFD29708B71187604D073A7D7.png?needInitFileName=true?needInitFileName=true)
支持动效场景调优
开发者在开发应用时，会使用到动效，动效的卡顿影响到用户的使用体验。DevEco Profiler提供动效场景的调优，能帮助开发者优化动效场景。
鼠标放置在某个动效上，显示该动效的详细信息，包括响应时延、动效持续时间、完成时延、期望帧率、FPS。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.32523600804078927286554335407034:50001231000000:2800:5C998DF97B8D7E97DA10B96DB25B39CE872419659CFC7D3EBEE4662BB0FA6790.png?needInitFileName=true?needInitFileName=true)
查看组件帧率信息
-  如下图所示，vsync2和vsync4中，vsync周期内的组件由于渲染耗时长，导致以下两个vsync周期挤掉下一个vsync周期的渲染时间，导致掉帧的情况产生。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.86578169548092190071565573945115:50001231000000:2800:999646748FC0FC7808DF5DBACED489F8F39759470F6D22B2B6014714A646388F.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.44315158950132925739463910403566:50001231000000:2800:F00CB66DA206A5494018207F4AA834A64911C25ABA782C397D5F3BA9E8DB1811.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150742.97549748200907358691278361725615:50001231000000:2800:5E90F5701485E0BAEABC5A6B488C1E883C5CFFE84B211EE074F8B4664DE7681A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.97122592305012872325792108116129:50001231000000:2800:235877C0E7ADAE9B6FE801AAE9875170A7038C45AEB34E62C76A85FFBF29FC90.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.50248911292224143070933198249179:50001231000000:2800:AF953B5FE6F3D56C946F63E4AC963DE0A7B22CD27DD019BAF89D3D9FD04A09D2.png?needInitFileName=true?needInitFileName=true)
查看ArkWeb帧率统计信息
Frame泳道中的App Frame泳道和RS Frame泳道在框选时新增fps标记。RS泳道新增过滤按钮，用于过滤ArkWeb数据。
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.61693702964107143797997743589068:50001231000000:2800:C4AB0C76F66FA775B8348B3961A26580B8054D8B123C6545F43888446240AA8C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.68261934920981229000719102688249:50001231000000:2800:0497FE7C197ADE31C1FD4DC477D184F61B9E1CAA0599BFA651090E9D53512BFF.png?needInitFileName=true?needInitFileName=true)
Anomaly泳道：查看解码过度耗时和超过阈值的序列化、反序列化操作
如果工程中存在图片资源，并感知到解码绘制/渲染过程存在卡顿，可以通过Anomaly泳道查看主线程解码过程中是否存在解码过度耗时告警，并确认发生告警的时段。
如果应用中使用了worker, Taskpool工作线程等场景，通常会触发跨线程对象传递，并触发序列化和反序列化的操作。对于耗时超过阈值的序列化、反序列化操作，Anomaly也会给出对应的耗时告警，并给出发送这个操作的开始时间和耗时时间。
1.
2.  已上架应用市场的应用不支持录制Anomaly泳道。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.04094546298429294902807890412509:50001231000000:2800:B4B6638F250020E05A12D1B9D5BC802D5215782668291F5173BC07CC38167FC5.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.16187923494665949324338325003532:50001231000000:2800:17E6EACC7CFD7C441FDC5820F0E50EB45C37F332977FFC04ED503C834221D48B.png?needInitFileName=true?needInitFileName=true)
User Events泳道：查看用户事件耗时
开发者在卡顿丢帧场景可通过User Event用户事件，查看用户事件开始时间、应用开始处理时间以及应用处理耗时等情况。
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.06217549759484036445726274320823:50001231000000:2800:F67423619D5271EFB197A17432E8B314E49424BCB44B71D6BB21C1A26798A500.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.51184737793899429395084351003132:50001231000000:2800:369874C44BC57199BAA8BBCA93FDA04313A10C3F830D6E636956F8DFA983BD2F.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-arkui-analysis-V14
爬取时间: 2025-04-30 08:49:48
来源: Huawei Developer
ArkUI分析用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。常见场景包含：
场景1：布局嵌套过多引起的性能问题；
场景2：数据结构设计不合理，应用使用一个较大的Object，在更新时，只更新某些属性，导致其他没变化的属性也会更新，产生冗余刷新；
场景3：父组件中的子组件重复绑定同一个状态变量进行更新；
场景4：未正确使用装饰器，如错误使用@Prop传递一个大的对象进行深度拷贝。
ArkUI Component 泳道：查看组件绘制耗时
开发者通过ArkUI Component泳道可以直观感知组件绘制频度、耗时等统计情况。
1.
2.
3.  由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI Component泳道。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.13876373666022493452748274318163:50001231000000:2800:57A7B169C36B6ED053149BD05EDBF835D20A7A2803957E2192CF8347A9BAE229.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.73288181881652384799242421117633:50001231000000:2800:B8296DE55DB6D7B2A6F62CA66A2815C52105F002401363B4E12B3B09D32BB3CD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.72459463439606515516726384600728:50001231000000:2800:29F61BD8147FBE81B74E5DF92A436D2E6E0417EB4CD11244E3E2E0C22312A8F3.png?needInitFileName=true?needInitFileName=true)
ArkUI State 泳道分析
1.  Current Value以时间顺序展示状态变量变化，Current Values列展示变化后的值。
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150743.99557142910318013858787897004503:50001231000000:2800:319B1545EF960F932162B0B4FE155DD0B1304559DFA834D8FEE12FF3728A38C9.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.87967479076054432477426848684578:50001231000000:2800:E21DE7B1613AC9CDD742C0E61C2D67A92432691B863DE58294751B7A5C846E33.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.98090345616369486019899069683366:50001231000000:2800:BB46D67D611F8C6DA19E202068A55A1B9347F5FD58353D4AA4172B5FC2003E56.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.24573323155439174463689530134526:50001231000000:2800:CB1537332D5AEE255A916F790F772D5A41DD3BF54781AA530CAA5A15EA68C286.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-insight-session-launch-V14
爬取时间: 2025-04-30 08:50:22
来源: Huawei Developer
开发应用或元服务过程中，启动速度是很重要的一个指标。如果开发者需要分析启动过程的耗时瓶颈，优化应用或元服务的冷启动速度，可使用DevEco Profiler提供的Launch场景分析能力，录制启动过程中的关键数据进行分析，从而识别出导致启动缓慢的原因所在。此外，Launch任务窗口还集成了Time、CPU、Frame场景分析任务的功能，方便开发者在分析启动耗时的过程中同步对比同一时段的其他资源占用情况。
此处仅介绍“Launch”泳道相关内容，集成的Time、CPU、Frame场景分析任务的功能请参考对应任务的章节。
启动模式
启动模式分为自动启动和手动启动，可点击图标切换两种不同模式：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.05951249635604120967360996474368:50001231000000:2800:53C0F660E153957AB995678ECBD2EB487CA35962D32E58DEC5424E0935DA5DFE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.55528644716239240755754354437477:50001231000000:2800:C55091CA323688AB310E7458374C9AF9120781CFED8FC33F1B065F338D646648.png?needInitFileName=true?needInitFileName=true)
查看启动过程中各阶段的耗时情况
1.  Launch分析任务支持在录制前单击指定要录制的泳道。“Launch”泳道显示启动生命周期各阶段的耗时分布情况。
2.  展开各阶段的统计信息折叠表，可以看到各个任务的具体耗时信息。单击跳转按钮，可直接跳转至相关线程打点任务中。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.45457210499596641021042940020007:50001231000000:2800:298E2E841D31FCB438FA1EE1B351B29C5AD0DDCD8ED8C0F0129EF5E9C35C89A4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.30706907714773170673895571142361:50001231000000:2800:A5E87D1AB979008D653C3AF6C9EF2F7C2EEE90FBF34F9DF202E10DBE920314D7.png?needInitFileName=true?needInitFileName=true)
分析静态资源库加载耗时
1.  针对耗时超过预期的加载任务，可单击跳转按钮，跳转至相关线程打点任务中进行深度分析。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.25625066180064956088532307882219:50001231000000:2800:4DF13B232FD219484B801F6D51A16940D317E65D93A836C252D87EAD656B1939.png?needInitFileName=true?needInitFileName=true)
查看核心线程在CPU Core的运行情况
1.  单击对应CPU的跳转按钮，可进一步跳转到CPU Core泳道查看详细的调度信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.22129904056351664823864294158741:50001231000000:2800:23CC7249A3AD1FC423711E3ED2118DADC0D09264DA1172960D0261EBA2B0C8D0.png?needInitFileName=true?needInitFileName=true)
查看启动过程相关的线程Trace数据
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.49671966478943150067477994068261:50001231000000:2800:B50E7AD55D645ECF416E1F47E0288759F7B06602F6B4357FC19D3EF0B81F5811.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-parallel-concurrency-analysis-V14
爬取时间: 2025-04-30 08:50:59
来源: Huawei Developer
任务池（TaskPool）是为应用程序提供一个多线程的运行环境，降低整体资源的消耗、提高系统的整体性能，且您无需关心线程实例的生命周期。您可以使用任务池API创建后台任务（Task），并对所创建的任务进行如任务执行、任务取消的操作。
DevEco Profiler提供的Concurrency场景分析能力，帮助开发者针对并行并发场景，录制并行并发关键数据，分析Task的生命周期、吞吐量、耗时等性能问题。Concurrency模板支持展示ArkTS异步接口、NAPI异步接口、FFRT并发模型相关信息，并集成ArkTS Callstack、Callstack、Process信息，支持用户从Task生命周期关联到具体调用栈信息，方便用户定位并行并发性能问题。
查看Task统计信息
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.52111523504684092990504054641871:50001231000000:2800:EEC707EA5ADD84D3A41024A03E3B03AFB14EDCD1E839C0BAE792106392078D45.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150744.65613729165892221262287347966192:50001231000000:2800:699622D87EA2B4F7E970FEA3EFCA82B07C2DE3DB49A690CEFEA054A48EE6B6C8.png?needInitFileName=true?needInitFileName=true)
查看某一个Task的所有状态
1.
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.29620502534946702212442318025766:50001231000000:2800:FA53EE76A1232B6943C4BC3779D846B80320B9BBA49CEDB5BA0CD5474DDBF79A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.79589897586683734640072154329146:50001231000000:2800:51D1FFDE803C0DE9CE4480A97210A7C37525A6C94F0B001F6B052B5A18EE302B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.00469828573634980122429267619340:50001231000000:2800:00FF3C1C9394B1D08DFDC7DD604E84904245DA51479AF9D05DABFE176B5AE0AC.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.28983423573587287382774718895353:50001231000000:2800:7088C870AC47564BB870930E62D347A9F33E742E7A7E5F9836B0D9D8A9919DFC.png?needInitFileName=true?needInitFileName=true)
查看Task的某个状态
点击Task子泳道的某个执行节点，Details详情区里会出现task在该状态下的详细信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.14236374847836091284811134580225:50001231000000:2800:0ADB3CE76F71C1FB9529A83B3D53A3D2A8B0C545D1BDB02C2A64708DC19E3C18.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-arkweb-V14
爬取时间: 2025-04-30 08:51:33
来源: Huawei Developer
应用开发过程中，会通过在APP中嵌入webView以提高开发效率，可能面临ArkWeb加载和丢帧等问题。DevEco Profiler提供ArkWeb分析模板，可以结合ArkWeb执行流程的关键trace点来定位问题发生的阶段。如果问题发生在渲染阶段，可以结合H:RosenWeb数据，线程运行状态以及帧渲染流程打点数据，进一步分析丢帧问题。
ArkWeb加载问题分析
1.
2.  根据web页面加载过程中的关键trace点，划分了五个阶段，分别是：点击事件（Click Event）， 组件初始化（Component Initialization），主资源下载（PrimaryResource Download），子资源下载（Sub-Resource Download），渲染输出（Render And Output）。
3.  框选可以查看泳道的耗时阶段划分的关键trace点，并可以根据trace信息，关联到所在线程信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.06922151205838655330957876514314:50001231000000:2800:84827C8D68B45F655ECEA1BE77B8532ECC1536C9CB5E45AA2CF9ADC48038042C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.93242447432559735280498335451279:50001231000000:2800:C214EFC8E414E852EF1E13BA67DDAA2F87569C5B0C3147E925F779EEC9C5876C.png?needInitFileName=true?needInitFileName=true)
ArkWeb丢帧问题分析
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.93692641054467277644432627892521:50001231000000:2800:8482532C5526270E7EA13CBB8E749061A206B8E746831C72B3F4CEFB0A6689AC.png?needInitFileName=true?needInitFileName=true)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.53083497833026065306012652082705:50001231000000:2800:22BD22BAF4BB2A8BC612A236861CEF54E92E927314BB704ED6F71B829FD5CC0F.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-network-V14
爬取时间: 2025-04-30 08:52:08
来源: Huawei Developer
DevEco Profiler提供Network模板，帮助用户在应用运行过程中查看http协议栈网络信息，包括请求分段耗时以及请求具体内容，方便对网络问题进行调优。请求耗时按照以下五种阶段进行划分：DNS 解析、TCP链接、TLS链接、请求等待、接受响应，分别展示在各阶段的耗时，可以针对性的优化时延问题。同时，详情信息将展示每个请求中携带的信息，包含request、response侧及其携带的header、body、cookie信息，方便网络问题定位。
查看网络请求各阶段耗时
1.
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.75613028979147877003513077998380:50001231000000:2800:D0C7E6CB116C85378BF6D1A09E88513027E12FFA961EEB0DC2C7905B5F0AB3A2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.84594973830879099386858021295400:50001231000000:2800:87DE2602F3B63DC2D42B199AB498591CC884308E26ABEEE24E5FA26DA622B192.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.57878707441913799154486229968450:50001231000000:2800:459025877408DC520D2C0A6FCC211D4D6AE7AC27743EBBEE7DB02792D375EA86.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150745.34240597557175308853932508955751:50001231000000:2800:A20F0DE4919FFE6FC11A4435BB96A91B5C72EC3DA24077AFD581EAE516BCC119.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-profiler-appendix-V14
爬取时间: 2025-04-30 08:52:42
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-shortcut-key-V14
爬取时间: 2025-04-30 08:53:17
来源: Huawei Developer
| 快捷键  | 功能  | 生效条件  |
| --- | --- | --- |
| Ctrl+鼠标滚轮  | 放大/缩小泳道区时间窗  | 鼠标悬浮在被调整控件时  |
| Shift+鼠标滚轮  | 左/右横向移动  | 鼠标悬浮在被调整控件时  |
| Alt+鼠标左键框选  | 将被框选区直接放大充满整条泳道  | 鼠标左键框选泳道时  |
| W  | 放大泳道区时间窗  | 数据区获取到焦点时  |
| S  | 缩小泳道区时间窗  | 数据区获取到焦点时  |
| A  | 横向左移泳道区时间窗  | 数据区获取到焦点时  |
| D  | 横向右移泳道区时间窗  | 数据区获取到焦点时  |
| M  | 添加单个时间标签  | 数据区获取到焦点时  |
| Shift+M  | 添加时间段的标记  | 数据区获取到焦点时  |
| Ctrl+,  | 向前选中单个时间标签  | 数据区获取到焦点时  |
| Ctrl+.  | 向后选中单个时间标签  | 数据区获取到焦点时  |
| Ctrl+[  | 向前选中时间段的标记  | 数据区获取到焦点时  |
| Ctrl+]  | 向后选中时间段的标记  | 数据区获取到焦点时  |
| F1  | 打开工具文档  | 鼠标悬浮在DevEco Profiler界面时  |
| Alt+Click  | 火焰图条块置底  | 点击火焰图区任一条块时  |
| [  | 全局搜索上一个  | 数据区获取到焦点时  |
| ]  | 全局搜索下一个  | 数据区获取到焦点时  |
快捷键
功能
生效条件
Ctrl+鼠标滚轮
放大/缩小泳道区时间窗
鼠标悬浮在被调整控件时
Shift+鼠标滚轮
左/右横向移动
鼠标悬浮在被调整控件时
Alt+鼠标左键框选
将被框选区直接放大充满整条泳道
鼠标左键框选泳道时
W
放大泳道区时间窗
数据区获取到焦点时
S
缩小泳道区时间窗
数据区获取到焦点时
A
横向左移泳道区时间窗
数据区获取到焦点时
D
横向右移泳道区时间窗
数据区获取到焦点时
M
添加单个时间标签
数据区获取到焦点时
Shift+M
添加时间段的标记
数据区获取到焦点时
Ctrl+,
向前选中单个时间标签
数据区获取到焦点时
Ctrl+.
向后选中单个时间标签
数据区获取到焦点时
Ctrl+[
向前选中时间段的标记
数据区获取到焦点时
Ctrl+]
向后选中时间段的标记
数据区获取到焦点时
F1
打开工具文档
鼠标悬浮在DevEcoProfiler界面时
Alt+Click
火焰图条块置底
点击火焰图区任一条块时
[
全局搜索上一个
数据区获取到焦点时
]
全局搜索下一个
数据区获取到焦点时

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-app-test-V14
爬取时间: 2025-04-30 08:53:51
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-test-V14
爬取时间: 2025-04-30 08:54:25
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-code-test-V14
爬取时间: 2025-04-30 08:54:59
来源: Huawei Developer
DevEco Studio支持应用/元服务测试框架，提供测试用例执行能力，提供用例编写基础接口，输出测试结果，支持用户开发简洁易用的自动化测试脚本，支持代码覆盖率统计。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-instrument-test-V14
爬取时间: 2025-04-30 08:55:34
来源: Huawei Developer
创建Instrument Test测试用例
创建默认测试用例
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.23852151673372831054306720677414:50001231000000:2800:4D9DFB8A8A4F3713ADF9F35FE2B2FBB3BBD421F09FD58C93887C0E9966F07F38.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.67846567293337974654803910065442:50001231000000:2800:1BB4C383AA33575D2F802D2C84BFEC06662261F7AE592BAB2EDD1D7069556457.png?needInitFileName=true?needInitFileName=true)
自定义Ability和Resources
从5.0.3.403版本开始，新创建的工程/模块的ohosTest目录下默认不创建testability、testrunner和resources目录，历史工程仍保留这些目录，如果新工程需要使用ability或resources能力，需要开发者自行创建。
如果需要使用ability能力，需要同时创建testrunner目录及OpenHarmonyTestRunner.ets文件。
| 新版本  | 历史版本  |
| --- | --- |
|   |   |
新版本
历史版本
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.61757074373543094982083238134955:50001231000000:2800:41C3E10F1D969C1AE01FC42C538F188D6084023CA48D0AB5F71D39525E760F30.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.94243851049866132797866243957602:50001231000000:2800:5DDB6444990CB6A7E112F76431A10F0400A3A54C7A0F06D83C3037B86D579CEC.png?needInitFileName=true?needInitFileName=true)
1.
2.
运行Instrument Test测试用例
运行模式
使用DevEco Studio运行测试用例前，需要将设备与电脑进行连接，将工程编译成带签名信息的HAP，再安装到真机设备或模拟器上运行，具体请参考应用/元服务运行。
-
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.46717149117572243238622463879578:50001231000000:2800:E16AC39D4E3F8146DEC59C2B20B03DA99F35C5CFB2FEE66588F57E9C7909B903.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.58058931124335317033759175328769:50001231000000:2800:21B8C790B6F92F8C9ACD6F3CE115210744C74163E8BDFC9C5E72B623C25A33B6.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.40856366142233206731946078192430:50001231000000:2800:3EBD94E7D530CF04894C80B3C3A345D519550FB6EFF819629A0F629CF855657A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.97301176509691138607707384240750:50001231000000:2800:EAA436FCC400D04899EFFE1E98DDC1F28779FE80AE942E53092C8E1D1935EE10.png?needInitFileName=true?needInitFileName=true)
执行完测试任务后，查看测试结果。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.30284068407131007882549808178280:50001231000000:2800:599E53059E6FF49D6723B6A24885F567CC26A9F91598B410061A1D465CF32843.png?needInitFileName=true?needInitFileName=true)
调试模式
调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。
以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击右键 > Debug'测试文件名称'，以调试模式执行测试任务。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.99633913629207233743140675549585:50001231000000:2800:D45B07E674A75A51884F0E70EEA65C08F6F5D8A62716C3C760E21AAB8A74A9E0.png?needInitFileName=true?needInitFileName=true)
在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.81432827117861877846620333126000:50001231000000:2800:C4C7FBC5F5177E79422521604607FA6DD41A5E0B2325CDD0C0D504458525980D.png?needInitFileName=true?needInitFileName=true)
断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150746.00354845239795504948434129050782:50001231000000:2800:AF029D7FA84C113A539AE931D38DD9361923E5E3F74D4AC95364646B06DE4E74.png?needInitFileName=true?needInitFileName=true)
在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.68098525321539603045190798503420:50001231000000:2800:32BFE71E18D0DF689853FC1745AC10775663303081995A0ED39ED5AAD1292DCB.png?needInitFileName=true?needInitFileName=true)
涉及调试C++代码时，请打开Run/Debug Configurations窗口，点击Debugger页签，设置Debug type，参考调试C++代码。
覆盖率统计模式
在Instrument Test运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。
可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。
以文件级别为例，有两种方式启动测试：
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.55516788938158568709845787472096:50001231000000:2800:12681F0F2C451C51846A315D5DD30F8CC87836AF290BC8640F8BBBA9CAC4359A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.03106562054867698725159100452955:50001231000000:2800:96AC1902B103B4068855D5F4402FD5675E4B85FB6095C7D38B2007B7173FB050.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.71411463444273864771915221786904:50001231000000:2800:0AB1FA1625FF068E5EBEC7BB2A7FF2CDC945F6CBB5B7BDD95E2B9B67D19808EF.png?needInitFileName=true?needInitFileName=true)
启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.11866279579976355173261586749317:50001231000000:2800:D1463ADEF31F799B2E240D73733F5EAFEB746128540BACC1CBF2DBA5EB3E3768.png?needInitFileName=true?needInitFileName=true)
点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考查看覆盖率报告。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.26750399325915977946839777298189:50001231000000:2800:9EB20BF877782FF0DB028A546B823FA98F1CF69D053496950E0705DCB7F74FD4.png?needInitFileName=true?needInitFileName=true)
在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.99278396296885698512590639668974:50001231000000:2800:B76278E67826B290DC640D540330061C1651CDE048EBB87D75DFBBEFEBB9BAAE.png?needInitFileName=true?needInitFileName=true)
（可选）自定义测试用例运行任务
默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.65488490621145693125060324883624:50001231000000:2800:F79D02C86D795C9BD60D1C7FDDB27DB8CF7E45B257EAB83B4B5BC61DB64F5CB1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.18740704266402185106754615205997:50001231000000:2800:E8405DF6BC5ED6E930451CBC9B60736963EDE7499657C8C1AF8D7E93FCF3A21D.png?needInitFileName=true?needInitFileName=true)
使用过滤条件筛选待运行的测试用例
1.
2.  例如将测试参数配置为level=1, size=medium Key 含义说明 Value取值范围 level 用例级别 "0","1","2","3","4", 例如：-s level 1 size 用例粒度 "small","medium","large", 例如：-s size small testType 用例测试类型 "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.92256052690602982663188276974398:50001231000000:2800:353F53D1B89CDE78BB6150AF8AB39C2EFCB162A0CBF09542858A3E1D16DBAA68.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.44012559545655512535882121404716:50001231000000:2800:A0E48E13C128CECE9E3E793119E04C64C94714BC023AADDEFB7C0440FF90C439.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.21816190275653190058321718468311:50001231000000:2800:DA8E814BCE319B1982EA19924A33CE5CD653700FB66DB6475797FAC4E214F8E1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.49974640886149379460527741757220:50001231000000:2800:3C38D5A63B8312FF882BD1E209F34E702B35F1273938D15737273A1C04238B59.png?needInitFileName=true?needInitFileName=true)
| Key  | 含义说明  | Value取值范围  |
| --- | --- | --- |
| level  | 用例级别  | "0","1","2","3","4", 例如：-s level 1  |
| size  | 用例粒度  | "small","medium","large", 例如：-s size small  |
| testType  | 用例测试类型  | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.06532974486953306955547065901534:50001231000000:2800:7AC3CB5A85A37811A229B534783F95AC8A69EE3009AADC25CEB92879191EECA1.png?needInitFileName=true?needInitFileName=true)
调试C++代码
当开发者编写Instrument Test测试用例，涉及调试C++代码时，请打开Run/Debug Configurations窗口，点击Debugger页签，设置Debug type。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150747.39427214062393101097684795361208:50001231000000:2800:DD93712877929ECCFCA9C9B474FCE0EF5D4F132E9A16D6A65E8A1D89D1ACB288.png?needInitFileName=true?needInitFileName=true)
调试类型Debug type默认为Detect Automatically，关于各调试类型的说明如下表所示：
| 调试类型  | 调试代码  |
| --- | --- |
| Detect Automatically  | 自动检测。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。 如果检测到是Native模块，出现两个调试窗口（PandaDebugger、Native）；如果不是Native模块，只出现PandaDebugger调试窗口。  |
| ArkTS/JS  | 只调试ArkTS/JS，只出现PandaDebugger调试窗口。  |
| Native  | 单独调试C++，只出现Native调试窗口。  |
| Dual(ArkTS/JS + Native)  | 支持ArkTS/JS和C++混合调试，出现两个调试窗口（PandaDebugger、Native）。  |
调试类型
调试代码
Detect Automatically
自动检测。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。
如果检测到是Native模块，出现两个调试窗口（PandaDebugger、Native）；如果不是Native模块，只出现PandaDebugger调试窗口。
ArkTS/JS
只调试ArkTS/JS，只出现PandaDebugger调试窗口。
Native
单独调试C++，只出现Native调试窗口。
Dual(ArkTS/JS + Native)
支持ArkTS/JS和C++混合调试，出现两个调试窗口（PandaDebugger、Native）。
调试C++代码时，当前模块及所有依赖的HSP模块的Address Sanitizer配置要保持一致，若不一致，可能无法进入C++代码的断点处。
ASan检测
Instrument Test针对C/C++方法提供ASan检测能力，关于ASan的介绍请参考ASan检测，当前不支持JS语言。
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.09099805230987550040686766377784:50001231000000:2800:05E9C11FF8F6CBF370EDC1C227153D0A419BD63D34844C13D1100A2572F26917.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.57062280987933210270857872233283:50001231000000:2800:7593828505692B408B868120079B025FD2F57A65A3F03728F0CA0F035C7507FB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.74135474825774500047949462073498:50001231000000:2800:0F90C0AD04C915D9C897EB0D67200FFE66C7C636D79FAD9FFD40ACDB238D5434.png?needInitFileName=true?needInitFileName=true)
使用命令行执行测试Instrument Test
从hvigor-ohos-plugin 4.3.0版本开始支持。
-  覆盖率测试报告路径：<module-path>/.test/default/outputs/ohosTest/reports/index.html
多个module和scope之间用逗号分割。
测试结果文件：<module-path>/.test/default/intermediates/ohosTest/coverage_data/test_result.txt

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-local-test-V14
爬取时间: 2025-04-30 08:56:09
来源: Huawei Developer
当前不支持测试C/C++方法及系统API。
创建Local Test测试用例
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.10275135042381256279943683536880:50001231000000:2800:F7B7464C49897A7361DBEA47729AE0147CBCD6EAD6534D37471B5BC0556A341E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.61146669684453224797985322614967:50001231000000:2800:1D2E675C374C3F07349295B8835C190FAE5084996AF16378FEE3CEFD639F83A9.png?needInitFileName=true?needInitFileName=true)
运行Local Test测试用例
运行模式
可以采用运行工程目录（test）、测试文件（如Index.test.ets）、测试套件（describe）、测试方法（it）的方式来执行Local Test，各级别测试执行入口如下。
|   |   |
| --- | --- |
| 目录级  | 文件级  |
|   |   |
| 套件级  | 方法级  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.13610440168520322826722626882224:50001231000000:2800:5727D33F5FFE8E221BB236A14A4541FFC74C70DE1C9BDA84D1492E7642F6AF1A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.18680298171738584340750301696237:50001231000000:2800:B02C8D93BF77F9C7D9A7F9D0D0F034265180E363C6CCEE8060DDF14628336989.png?needInitFileName=true?needInitFileName=true)
目录级
文件级
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.26712857724406778945465344293892:50001231000000:2800:3B299A37966F5D49A9CFE92B2146804ED852625D842CD41174060C0BDB054252.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.46926509752037813062462600206591:50001231000000:2800:144294F5FB5AC894993AB16F96EC0E53CF512BB737ED271A5F8E341F08E4BAD2.png?needInitFileName=true?needInitFileName=true)
套件级
方法级
以文件级别为例，在工程目录中，选中文件，单击右键 > Run'测试文件名称'，执行测试。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.94662977278539201688193905684233:50001231000000:2800:7630596592EF079765D23C552C4BB4D7752B311C6CCDF51940A3D5584D426311.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.01555770105057537729864853221227:50001231000000:2800:373FB0E4154886BF4427A5C7786F7BF7869BBAE675248BEDFDB0A68BF7CE8023.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150748.16161781644896274581402050769606:50001231000000:2800:3C199461DA7E431949D3945149326A40A9CF1788A7AC261C3A3BDE5BAEE4CE5A.png?needInitFileName=true?needInitFileName=true)
执行完测试任务后，查看测试结果。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.10746473814267502360348783670063:50001231000000:2800:2F6C8B4F08D1E6921ABEC1D154EB12F0F82A914B8EF5853AE22639FB689E06B6.png?needInitFileName=true?needInitFileName=true)
调试模式
调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。
以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击右键 > Debug'测试文件名称'，以调试模式执行测试任务。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.74121594078848963463563994521831:50001231000000:2800:F185BA31C82310AB50C90F87AC3AEFA2F5F42B1EE7C043CC33463610A70CB97A.png?needInitFileName=true?needInitFileName=true)
在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.27995063793274684365025784198026:50001231000000:2800:7B544B7749155E1C7771ED7BE7212557D12312865B1DACAB851678652154E015.png?needInitFileName=true?needInitFileName=true)
断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.84915309024206873609635263496270:50001231000000:2800:1DC904EDD719F89469D7AF625F67A161AB4B5AA08D74CB2E9AB43ECF9E8BD0D0.png?needInitFileName=true?needInitFileName=true)
在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.89749060625032313831354889170098:50001231000000:2800:9EDA55D9257B5D2F461D66A3D2BBD61774A56CEE6A4EE23CD674F81D6A867CAB.png?needInitFileName=true?needInitFileName=true)
覆盖率统计模式
在LocalTest运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。
如前所述，覆盖率统计模式也有多级别入口，以文件级别为例，有两种方式启动测试：
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.53494942378334487369979051212689:50001231000000:2800:E91B8327946504FC437979FF7A4F7944FBD4F637D63453599D9A7491C3614906.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.92552218602884181167494729128682:50001231000000:2800:3554147094D8AA2F643EF055B62465F6AE33C60D00985CE871311C9087267BA2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.42280541432862650869369500369029:50001231000000:2800:DDF270A6079DCF3ED3944CF005726B160FC2FC8D9A3CD10B9A90791D46D95DA4.png?needInitFileName=true?needInitFileName=true)
启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.86366757279557702405242868574788:50001231000000:2800:39C5773AE0C18A58D8D05B8C8AA2AB7D1601D91F52BB8B375FCCAB1F57B41B3D.png?needInitFileName=true?needInitFileName=true)
点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考查看覆盖率报告。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.80835783160626855735293705692574:50001231000000:2800:F88FC017783E783B02620A575C94EB88D3F363B9E60C302BC4F034868DE8530F.png?needInitFileName=true?needInitFileName=true)
在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.29865098012113391505638885152897:50001231000000:2800:F01FBD350BC8E722DDAAAB8F710BF59785B0103376F8C98D16AD3840E1C03DD2.png?needInitFileName=true?needInitFileName=true)
（可选）自定义测试用例运行任务
默认情况下，测试用例可直接运行。如果需要自定义测试用例运行任务，可通过如下方法进行设置。
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.58932779014035983550827193762573:50001231000000:2800:C02F8D7D33698B297BEC6AF71FA4984852491BB0D438C8797D4242D6985B11BF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150749.91382784374350112321975569181427:50001231000000:2800:69B51D06FDAD047ABC1F1B9D230A71E03A67E4E1A56784818795A3B187072B01.png?needInitFileName=true?needInitFileName=true)
使用命令行执行Local Test
-  覆盖率测试报告路径：<module-path>/.test/default/outputs/test/reports/index.html
-  多个module和scope之间用英文逗号分割。
测试结果文件：<module-path>/.test/default/intermediates/test/coverage_data/test_result.txt

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-test-mock-V14
爬取时间: 2025-04-30 08:56:44
来源: Huawei Developer
在实际开发中，一些接口或者对象依赖于外部资源或复杂的逻辑，这些依赖在测试环境中难以复现，导致这些接口或者对象难以测试，此时，可以使用mock能力。当前Instrument Test和Local Test均支持mock能力，有两种实现方式，一是使用hamock或者hypium插件包的mock接口，二是使用import mock。
仅API 11及以上版本的Stage工程支持。
使用hamock/hypium插件包的mock接口
以下例子通过mock接口模拟类的某个方法，关于mock的更多说明可以参考mock能力。
1.
```typescript
export class ClassForMock {
constructor() {
}
method_1(arg: string) {
return '888888';
}
method_2(arg: string) {
return '999999';
}
}
```
2.
使用import mock
在mock-config.json5配置文件中定义目标module和mock文件的映射关系，运行时import目标module都将指向mock实现代码。以系统API bluetoothManager为例，具体实现如下。
1.
2.
3.

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ui-test-V14
爬取时间: 2025-04-30 08:57:18
来源: Huawei Developer
DevEco Studio支持黑盒覆盖率测试，不需要开发测试用例，将编译插桩的HAP包推到设备上，然后对该应用模拟用户操作，退出应用后即可生成覆盖率报告，当前仅支持Stage模型。
操作步骤
1.
2.
3.
4.  从API 13开始，如果用户使用最近任务列表一键清理来关闭应用，将不会执行onDestroy()回调，导致获取不到覆盖率数据。
5.  在多模块相互跳转的场景下，只需要取最后退出的模块下生成的覆盖率数据json文件，但特殊场景下如多模块无跳转关系，则需要取每个独立模块下生成的覆盖率数据json文件。
6.  在多模块相互跳转的场景下，需要取各模块的init_coverage.json文件路径，与黑盒覆盖率文件保存路径通过#拼接生成coverageFile参数。
7.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.66147654337282785136505720126372:50001231000000:2800:11B75138CB8194F018149453DEAB59FD76F6C955D202CA3430D0B0D595951C12.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.13647324723473734251190803421819:50001231000000:2800:20B4639B118CC52BEFE184E9999AD0FD9495F9F9A03EFE449E72BC1BAF54522D.png?needInitFileName=true?needInitFileName=true)
查看覆盖率报告
测试覆盖率报告有三个测量维度，分别是：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.94085909980993766437878370480822:50001231000000:2800:A07951657158D50AD4A760C0D692857013551C8C61189BEE9C14EC060D83B045.png?needInitFileName=true?needInitFileName=true)
以下是关于三个测量维度的细节说明：
-  常见的流程控制语句有if、while、do...while、switch、for等等，以及三目运算符（condition ? exprIfTrue : exprIfFalse），需要确保流程控制的每个边界情况（即分支）都被执行。
-  示例如下：
```typescript
import { window } from '@kit.ArkUI';  // +0  方法外不统计
let filePath :string;               // +0  方法外不统计
const fileName = 'a.txt';          // +0  方法外不统计
export function doTheThing ()  // +1
{                              // +1
let s1: string;              // +1
const str = 'aaa';           // +1
console.log(str);            // +1
}                              // +0
export class Person {         // +0  方法外不统计
name: string = ''           // +0  方法外不统计
constructor (n:string) {    // +1 构造函数
this.name = n;            // +1
}                           // +0
static sayHello () {        // +1  类静态方法
console.log('hello');     // +1
}                           // +0
walk () {                   // +1  类实例方法
for (                     // +1
let i=0;                // +1
i < 10;                 // +1
i++)                    // +1
{                         // +1
}                         // +0
}                           // +0
}                             // +0
function func ():object {    // +1
return Object({        // +1      一个语句被拆分为多行
a: 1,                // +1
b: 2,                // +1
})                     // +0
}                        // +0
func();                  // +0  方法外不统计
function foo(n:number, m:number){}   // +1
function bar():number {              // +1
return 1;                          // +1
}
foo(1, bar());                       // +0  方法外不统计
```
-  示例如下：
```typescript
import { window } from '@kit.ArkUI';  // +0  方法外不统计
let filePath :string;               // +0  方法外不统计
const fileName = 'a.txt';          // +0  方法外不统计
export function doTheThing ()  // +1
{                              // +1
let s1: string;              // +1
const str = 'aaa';           // +1
console.log(str);            // +1
}                              // +0
export class Person {         // +0  方法外不统计
name: string = ''           // +0  方法外不统计
constructor (n:string) {    // +1 构造函数
this.name = n;            // +1
}                           // +0
static sayHello () {        // +1  类静态方法
console.log('hello');     // +1
}                           // +0
walk () {                   // +1  类实例方法
for (                     // +1
let i=0;                // +1
i < 10;                 // +1
i++)                    // +1
{                         // +1
}                         // +0
}                           // +0
}                             // +0
function func ():object {    // +1
return Object({        // +1      一个语句被拆分为多行
a: 1,                // +1
b: 2,                // +1
})                     // +0
}                        // +0
func();                  // +0  方法外不统计
function foo(n:number, m:number){}   // +1
function bar():number {              // +1
return 1;                          // +1
}
foo(1, bar());                       // +0  方法外不统计
```
-
-
-  代码中的某些分支可能很难、甚至无法测试，Deveco Studio提供了instrument ignore * 语法来进行忽略，使得某些代码不计入覆盖率。 使用时需先清除缓存，点击菜单栏Build -> Clean Project。
```typescript
import {testA} from './Index'
// instrument ignore file       忽略整个文件
// instrument ignore next       忽略代码块
export function sum(a:number,b:number){
return a+b;
}
sum(1,2);
let a = 1;
// instrument ignore else       忽略else分支
if (a!=1) {
// do something
console.log('BBB');
}else {
console.log('AAA');
}
// instrument ignore if         忽略if分支
if (a==1) {
// do something
console.log('BBB');
}else {
console.log('AAA');
}
```
-  示例如下：
```typescript
import { window } from '@kit.ArkUI';  // +0  方法外不统计
let filePath :string;               // +0  方法外不统计
const fileName = 'a.txt';          // +0  方法外不统计
export function doTheThing ()  // +1
{                              // +1
let s1: string;              // +1
const str = 'aaa';           // +1
console.log(str);            // +1
}                              // +0
export class Person {         // +0  方法外不统计
name: string = ''           // +0  方法外不统计
constructor (n:string) {    // +1 构造函数
this.name = n;            // +1
}                           // +0
static sayHello () {        // +1  类静态方法
console.log('hello');     // +1
}                           // +0
walk () {                   // +1  类实例方法
for (                     // +1
let i=0;                // +1
i < 10;                 // +1
i++)                    // +1
{                         // +1
}                         // +0
}                           // +0
}                             // +0
function func ():object {    // +1
return Object({        // +1      一个语句被拆分为多行
a: 1,                // +1
b: 2,                // +1
})                     // +0
}                        // +0
func();                  // +0  方法外不统计
function foo(n:number, m:number){}   // +1
function bar():number {              // +1
return 1;                          // +1
}
foo(1, bar());                       // +0  方法外不统计
```
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.35075083374924499399380939229532:50001231000000:2800:3A7A3EB5B89E119E565031E075FFF86C3DFA020983F2E0473564FA2A6049AB57.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-app-analyzer-V14
爬取时间: 2025-04-30 08:57:53
来源: Huawei Developer
功能介绍
应用与元服务体检工具（AppAnalyzer）用于对应用和元服务进行本地测试体检，并给出体检报告、分析指导以及修改建议，帮助开发者提升应用与元服务质量。在体检过程中，工具会收集应用或元服务的trace信息、代码栈、内存快照以及应用或元服务页面的截屏，并保存在本地工程目录.appanalyzer下，帮助开发者快速进行问题分析定位。
开发者可以通过DevEco Studio连接本地设备，自主遍历HarmonyOS应用或元服务的功能，快速进行自测试，查看测试结果及评分。当前支持规则体检和场景化体检两种方式。
使用约束
当前仅phone类型的设备支持使用应用与元服务体检能力。
前置操作
规则体检
操作步骤
1.
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.26776166297390825029441538668290:50001231000000:2800:FC84B3FFAFBE378860690FFF4F94FF49DFF9B8A6D52BDD741DB69FC2317A229D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.51987767719172226614087380767886:50001231000000:2800:CD3653E389BCF31D386C5EA6F0A29B3662BA8DC0BE6FDD04D36615A3B9753697.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.88953080028710518662682682260395:50001231000000:2800:6A1D7D790C420C63F387703F03DED3049236F33726E90527926D70AF6ABAD766.png?needInitFileName=true?needInitFileName=true)
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.20173245535349143192844997312531:50001231000000:2800:DCCE3568C9DE017AB23942F76607EC86E8C25B03301B178EA501BBECCC7DE94B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150750.98733092032373807845951978608656:50001231000000:2800:D2DC11EEF05D5F86BDEA21F9DF2DD131EC7AD942B0F61643CB3759FAE82501D9.png?needInitFileName=true?needInitFileName=true)
评分方法和规则
应用与元服务体检当前支持兼容性、性能和最佳实践等测试类型检测。AppAnalyzer会根据体检结果计算出最后评分，满分为100分。评分的计算公式为：
评分 = Sum(检测通过的体检项权重）/Sum(体检项权重）*100
各体检项检测规则及权重请参考应用/元服务体检规则。
场景化体检
操作步骤
1.
2.  请勿在测试完成前点击结束，如果提前结束测试会导致测试结果不准确。
3.  手动遍历完成后点击结束按钮停止测试任务，查看测试结果如下。
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.06867641254403231457401437429560:50001231000000:2800:969F130128A2155ED1970BE021E816455710CE4E87C81130FA20A27981B79592.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.42580283186852066923627390248095:50001231000000:2800:B0F756290E6A1535737257966516975BADFFE59475150D3552B1C7581DAE36A7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.96205037241780577544252484079086:50001231000000:2800:14AC3AD28DD1B726BC15E7CA838D1D646F6D8697040F29DA331E1A553575887A.png?needInitFileName=true?needInitFileName=true)
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.37884009689432017687811124351269:50001231000000:2800:4CF368233F3FA219517AA88CC964541CB577FE4E101DD5EECEEB02270947D033.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.48427347794905385992313672728364:50001231000000:2800:7B8F15D26A9F4A5CFE0DE01A87277E1422E4FBC3F8070C29E9A3B1F6F9B12ACB.png?needInitFileName=true?needInitFileName=true)
评分方法和指标
AppAnalyzer会根据体检结果计算出总分，满分为100分，评分规则如下：
根据检测结果，某个场景的某个指标的评分规则：
总分是多个场景多个指标多个页面的平均值，如果同一个场景的同一个指标在同一个页面多次测试，取最差的结果作为得分。示例如下：
| 场景  | 子场景  | 指标  | 页面  | 测试次数  | 达标情况  | 得分  | 总分  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 页面间转场         | router或者navigation页面跳转         | 响应时延     | A->B   | 第一次  | 成功  | 0.6  | (0.6+0+0.6+0)/4*100=30  |
| 第二次  | 告警  |
| B->C   | 第一次  | 告警  | 0  |
| 第二次  | 失败  |
| 完成时延     | A->B   | 第一次  | 告警  | 0.6  |
| 第二次  | 成功  |
| B->C   | 第一次  | 失败  | 0  |
| 第二次  | 告警  |
场景
子场景
指标
页面
测试次数
达标情况
得分
总分
页面间转场
router或者navigation页面跳转
响应时延
A->B
第一次
成功
0.6
(0.6+0+0.6+0)/4*100=30
第二次
告警
B->C
第一次
告警
0
第二次
失败
完成时延
A->B
第一次
告警
0.6
第二次
成功
B->C
第一次
失败
0
第二次
告警
各体检场景对应的检测指标如下表所示：
| 场景  | 子场景  | 检测指标  |
| --- | --- | --- |
| 页面间转场   | router或者navigation页面跳转   | 点击响应时延  |
| 点击完成时延  |
场景
子场景
检测指标
页面间转场
router或者navigation页面跳转
点击响应时延
点击完成时延
查看历史报告
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.34341828564886305515832851792493:50001231000000:2800:8B79784579C7E1E7DD983F7F19F807AFB99D2DAFDC50B2213CA21C01EFCEAE67.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-publish-app-V14
爬取时间: 2025-04-30 08:58:28
来源: Huawei Developer
HarmonyOS通过数字证书与Profile文件等签名信息来保证应用/元服务的完整性，应用/元服务上架到AppGallery Connect必须通过签名校验。因此，您需要使用发布证书和Profile文件对应用/元服务进行签名后才能发布。
发布流程
开发者完成HarmonyOS应用/元服务开发后，需要将应用/元服务打包成App Pack（.app文件），用于上架到AppGallery Connect。发布应用/元服务的流程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.35115909619753266987154777141833:50001231000000:2800:5C9E9B3FEC31FDA8B3B1A425BA671E9C553A5C0617CAA691CE1A3C35E3308F15.png?needInitFileName=true?needInitFileName=true)
关于以上流程的详细介绍，请继续查阅本章节内容。
准备签名文件
HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请数字证书和Profile文件前，首先需要通过DevEco Studio来生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。
生成密钥和证书请求文件
1.  如果本地已有对应的密钥，无需新生成密钥，可以在Generate Key界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2.
3.
4.
5.
6.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.81338702278654755464785015083274:50001231000000:2800:669D8FA2D2255091F48C7657973CFB769C63865C9FB424F7C3D05B175504D5D3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.19984951872066114065315450754782:50001231000000:2800:5E4482344EFC9BCEB464E3B21D4B3817D25539AA93BE2BB903B965669EB20568.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.46271987107701809623819715418201:50001231000000:2800:5CF7681CB67D3ACFFC5F406DFD0E6E117293EB14BF511025062A47D4295DC992.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.85543107696727341178347043887785:50001231000000:2800:7B31331E89853CABE2B2FF387DFDF4621629B9AAAD27F5C85777AD2FB889FE1B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.58652629056949534153712445713499:50001231000000:2800:0117B40C7E61CBB0037289AE17A10F5BD4BF52B8787A5582427375285F27AED7.png?needInitFileName=true?needInitFileName=true)
申请发布证书和Profile文件
-  如果申请元服务的签名证书，在“创建应用”操作时，“是否元服务”选项请选择“是”。
用于发布的证书和Profile文件申请完成后，请在DevEco Studio中进行签名，请参考配置签名信息。
使用发布证书和发布Profile文件进行手动签名，只能用来打包应用上架，不能用来运行调试工程。
配置签名信息
使用制作的私钥（.p12）文件、在AppGallery Connect中申请的证书（.cer）文件和Profile（.p7b）文件，在DevEco Studio配置工程的签名信息，构建携带发布签名信息的APP。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150751.65038188012221993440122065813767:50001231000000:2800:0E5CB905A3AE23A88E82C5D8C06589D53B572F67A4FFD7BBEA49E28CEA7D1B91.png?needInitFileName=true?needInitFileName=true)
设置完签名信息后，单击OK进行保存，然后使用DevEco Studio生成APP，请参考编译构建.app文件。
（条件必选）更新公钥指纹
当应用需要使用以下开放能力的一种或多种时，发布应用前，需在AppGallery Connect中将调试应用的指纹更新为发布证书指纹。具体操作请参见配置应用签名证书指纹。
编译构建.app文件
应用上架时，要求应用包类型为Release类型。
打包APP时，DevEco Studio会将工程目录下的所有HAP/HSP模块打包到APP中，因此，如果工程目录中存在不需要打包到APP的HAP/HSP模块，请手动删除后再进行编译构建生成APP。
1.  当未指定构建模式时，构建APP包，默认Release模式；构建HAP/HSP/HAR包，默认Debug模式。 即Build APP(s)时，默认构建的APP包为Release类型，符合上架要求，开发者无需进行另外设置。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150752.77151169596950073248228486925142:50001231000000:2800:D1FEC9D0BF11AFA19B7D2E81ECF87760A12804AADD77B145E231DDE6542FDC1E.png?needInitFileName=true?needInitFileName=true)
上传软件包
DevEco Studio 5.0.5.200版本开始，支持在DevEco Studio内上传应用软件包。上传软件包前，请先创建应用。
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150752.70485589047460908868820982626509:50001231000000:2800:86330AF327D872DDF3BCA2B5A8CE58BC2F026D589F6D32CEC9D482FE39FB5EB8.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150752.94487084808002703567886189186070:50001231000000:2800:2B096860C881670D4CA4FC00FB87B65E8C44E5A1D8EEC3257F8EC0350F938A59.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150752.86690892406329301144527371357007:50001231000000:2800:297C60982147906D28519558E2AE68246371245F1897372269800AF1B06C087D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150752.06281027911654337389100887176547:50001231000000:2800:1B7B8CBEBE87486E6FD0F913074AA43DFCC4A02B954BDDB941B786229CD584DA.png?needInitFileName=true?needInitFileName=true)
发布.app文件到应用市场
将HarmonyOS应用/元服务打包成.app文件后上架到应用市场，发布详细操作指导请参考上架HarmonyOS应用或上架元服务。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-intelligent-assisted-programming-V14
爬取时间: 2025-04-30 08:59:02
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-codegenie-V14
爬取时间: 2025-04-30 08:59:37
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-codegenie-plugin-V14
爬取时间: 2025-04-30 09:00:12
来源: Huawei Developer
DevEco AI辅助编程工具（CodeGenie）为开发者提供高效的应用与服务AI编程支持，支持智能知识问答，同时支持ArkTS代码生成和万能卡片生成能力，帮助开发者提高编码效率。
使用方式
在DevEco Studio右侧边栏点击CodeGenie或输入快捷键Alt/Option+U进入DevEco CodeGenie。勾选同意隐私安全政策及使用条款后，点击Sign in，跳转华为账号登录页面。授权登录完成后返回DevEco Studio，提示登录成功，即可开始体验。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150752.79378500625171548660935654835003:50001231000000:2800:2FC631FB08152096E21980655FC9262EA1751A72B331F3850B4848EDBF990235.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-codegenie-knowledge-V14
爬取时间: 2025-04-30 09:00:46
来源: Huawei Developer
基于生成式搜索能力，通过查询生成、内容优选服务高效理解用户意图，问答交互式地获取编码相关知识。
示例
在对话区域选择HarmonyOS，输入需要查询的问题，开始问答。示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250423182213.03173564108554843091307481376073:50001231000000:2800:7D98EA7B167C4E7F03BFCFF34FDA21BDB97F34419872CAF91DE21D76423A94EE.gif)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-codegenie-code-edit-V14
爬取时间: 2025-04-30 09:01:20
来源: Huawei Developer
利用AI大模型分析并理解开发者在代码编辑区的上下文信息或自然语言描述信息，智能生成符合上下文的ArkTS或C++代码片段。支持在代码编辑区通过快捷键主动触发代码生成，或根据自然语言描述生成相应代码片段。
使用约束
建议在编辑区内已有较丰富上下文，能够使模型对编程场景有一定理解的情况下进行代码生成。在编辑器中的内容较少时，AI可能无法有效理解用户的意图并生成相应的代码。
模型反馈需满足规则：光标上文10行内，有效代码行数超过5行（排除单独{}、（）、[]括号行、空行、纯注释行场景），便于模型能理解代码上下文。
行内生成
安装CodeGenie后，只需在编码时稍作停顿，CodeGenie将在当前代码行即时生成代码。若开发者认可推荐的内容，可通过按Tab键采纳，或通过按ESC键忽略生成的内容。
若未打开代码生成功能，进入File > Settings>DevEcoCodeGenie > Code Generation页面开启。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150753.61297963762709376765380729790479:50001231000000:2800:A6EDFB12FDC60DAC471D726ED79CF481B3E641E39367ACA33056A13E84020585.png?needInitFileName=true?needInitFileName=true)
片段生成
当安装完成CodeGenie后，在编码区代码行输入回车，将出现CodeGenie根据上下文生成的多行代码片段。可使用Tab键采纳该代码生成内容，或者使用ESC键忽略。
若未打开代码生成功能，进入File > Settings>DevEcoCodeGenie > Code Generation页面开启。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150753.97924616995181518527901062571909:50001231000000:2800:F36D6E4C03C9956DCC765659D3410AB62A69B7EAB89D6DFB9BDDC538FBE43682.png?needInitFileName=true?needInitFileName=true)
CodeGenie常用快捷键如下：
| 操作  | macOS  | Windows  |
| --- | --- | --- |
| 触发多行代码生成  | Enter、Option+C  | Enter、Alt+C  |
| 触发单行代码生成  | Option+X  | Alt+X  |
| 采纳生成的代码  | Tab  | Tab  |
| 忽略生成的代码  | Esc  | Esc  |
| 查看上一个代码生成结果  | Option +[  | Alt + [  |
| 查看下一个代码生成结果  | Option + ]  | Alt + ]  |
| 重新生成代码内容（最多支持重新生成5次）  | Option + R  | Alt + R  |
| 展示CodeGenie面板  | Option + U  | Alt + U  |
操作
macOS
Windows
触发多行代码生成
Enter、Option+C
Enter、Alt+C
触发单行代码生成
Option+X
Alt+X
采纳生成的代码
Tab
Tab
忽略生成的代码
Esc
Esc
查看上一个代码生成结果
Option+[
Alt + [
查看下一个代码生成结果
Option+ ]
Alt + ]
重新生成代码内容（最多支持重新生成5次）
Option+ R
Alt + R
展示CodeGenie面板
Option+ U
Alt + U
自然语言生成代码
在对话框内，通过输入/调出命令，选择Code后可根据自然语言描述智能生成代码，生成内容可一键复制或一键插入至编辑区当前光标位置。
提问示例
使用ArkTs语言写一段代码，在页面中间部分插入Swiper组件，其中有3个Image组件，其图片资源名分别为app.media.phone，app.media.watch，app.media.glasses。这些Image组件的宽度撑满父布局，高度为600，图片缩放类型为保持图片宽高比不变，将图片完全显示在边界内。 Swiper组件设置为自动播放，播放时间间隔为2秒。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150753.54383525067690967685115474514205:50001231000000:2800:83531D596B2194ACE69255BCEE3A638ACA01A395F73616CC4C065CEBBD490480.gif?needInitFileName=true?needInitFileName=true)
代码生成设置
进入File > Settings>DevEcoCodeGenie > Code Generation页面开启代码生成功能。并根据编码习惯，设置行内生成和片段生成的时延。
如果已经熟悉了CodeGenie常用的快捷键，想要更加沉浸的体验，可以在该页面勾选Do not disturb，隐藏代码生成工具栏及快捷键提示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150753.21249572698484478047524503961718:50001231000000:2800:B767FC262754A438D8BEC3AA095F7B66A9B7F4998B8F3606A3CBC67F197FBD53.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-appendix-V14
爬取时间: 2025-04-30 18:55:28
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-codelinter-rule-V14
爬取时间: 2025-04-30 18:56:06
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-codelinter-rules-change-V14
爬取时间: 2025-04-30 18:56:42
来源: Huawei Developer
5.0.7.100
新增规则
变更规则
5.0.5.200
变更规则
5.0.3.800
新增规则
变更规则
-
下线规则
5.0.3.600
新增规则
变更规则
以下规则的部分场景，在5.0.3.600之前的版本检查执行Codelinter检查时不报错，升级至DevEco Studio 5.0.3.600版本后执行Codelinter检查将报错。
```typescript
// 支持检查构造函数中的参数类型
class Foo {
constructor(param: boolean = true) {} // 升级前不报错，升级后报错
}
```
5.0.3.500
新增规则
变更规则
下线规则

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-typescript-eslint-V14
爬取时间: 2025-04-30 18:57:18
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_adjacent-overload-signatures-V14
爬取时间: 2025-04-30 18:57:54
来源: Huawei Developer
建议函数重载的签名保持连续。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export declare function bar(): void;
export declare function foo(a: string): void;
export declare function foo(a: number, b: number): void;
export declare function foo(a: number, b: string, c?: string): void;
```
反例
```typescript
export declare function foo(a: string): void;
export declare function bar(): void;
export declare function foo(a: number, b: number): void;
export declare function foo(a: number, b: string, c?: string): void;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_await-thenable-V14
爬取时间: 2025-04-30 18:58:29
来源: Huawei Developer
不允许对不是“Thenable”对象的值使用await关键字（“Thenable”表示某个对象拥有“then”方法，比如Promise）。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_array-type-V14
爬取时间: 2025-04-30 18:59:07
来源: Huawei Developer
定义数组类型时，建议使用相同的样式。比如都使用T[]或者都使用Array<T>。
规则配置
选项
详情请参考typescript/array-type 选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_ban-ts-comment-V14
爬取时间: 2025-04-30 18:59:43
来源: Huawei Developer
不允许使用`@ts-<directional>`格式的注释，或要求在注释后进行补充说明。
规则配置
选项
详情请参考@typescript-eslint/ban-ts-comment选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_ban-tslint-comment-V14
爬取时间: 2025-04-30 19:00:20
来源: Huawei Developer
不允许使用`//tslint:<rule-flag>`格式的注释。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_ban-types-V14
爬取时间: 2025-04-30 19:00:56
来源: Huawei Developer
不允许使用某些类型。
规则配置
选项
详情请参考@typescript-eslint/ban-types选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_brace-style-V14
爬取时间: 2025-04-30 19:01:31
来源: Huawei Developer
对代码块强制执行一致的括号样式。
规则配置
选项
详情请参考@typescript-eslint/brace-style选项。
正例
```typescript
function foo(): boolean {
return true;
}
class C {
static {
foo();
}
public meth() {
foo();
}
}
export { C };
```
反例
```typescript
function foo(): boolean
{
return true;
}
class C {
static
{
foo();
}
public meth()
{
foo();
}
}
export { C };
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_class-literal-property-style-V14
爬取时间: 2025-04-30 19:02:06
来源: Huawei Developer
建议类中的字面量属性对外暴露时，保持一致的风格。
规则配置
选项
详情请参考@typescript-eslint/class-literal-property-style选项。
正例
```typescript
class Mx {
public readonly myField1 = 'hello';
public readonly myField2 = ['a', 'b'];
public readonly ['myField3'] = 'hello world';
public get myField4() {
return `hello ${this.myField1}`;
}
}
export { Mx };
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_comma-dangle-V14
爬取时间: 2025-04-30 19:02:44
来源: Huawei Developer
允许或禁止使用尾随逗号。
规则配置
选项
详情请参考@typescript-eslint/comma-dangle选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_comma-spacing-V14
爬取时间: 2025-04-30 19:03:19
来源: Huawei Developer
强制逗号前后的空格风格保持一致。
规则配置
选项
详情请参考@typescript-eslint/comma-spacing选项。
正例
```typescript
// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr1 = ['1', '2'];
export const arr2 = ['1',, '3'];
function qur(a: string, b: string) {
return `${a}${b}`;
}
qur('1', '2');
```
反例
```typescript
// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr = ['1' , '2'];
function qur(a: string ,b: string) {
return `${a}${b}`;
}
qur('1' ,'2');
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_consistent-indexed-object-style-V14
爬取时间: 2025-04-30 19:03:55
来源: Huawei Developer
允许或禁止使用“Record”类型。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/consistent-indexed-object-style选项。
正例
```typescript
// 默认推荐使用Record 类型
export type Foo = Record<string, unknown>;
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_consistent-type-assertions-V14
爬取时间: 2025-04-30 19:04:32
来源: Huawei Developer
强制使用一致的类型断言。
规则配置
选项
详情请参考@typescript-eslint/consistent-type-assertions选项。
正例
```typescript
// 默认推荐使用 ... as foo， 始终优先选择 const x = { ... } as T; 而不是const x: T = { ... };
interface MyType {
name: string;
}
export const x: MyType = {
name: 'hello'
};
export const y = x as object;
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_consistent-type-definitions-V14
爬取时间: 2025-04-30 19:05:08
来源: Huawei Developer
强制使用一致的类型声明样式，仅使用“interface”或者仅使用“type”。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/consistent-type-definitions选项。
正例
```typescript
// 基本类型的定义可以使用type
export type T1 = string;
// 默认推荐使用interface 进行对象类型定义
export interface T2 {
x: number;
}
export type Foo = string | T2;
```
反例
```typescript
// 默认推荐使用interface 进行对象类型定义
type T = { x: number };
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_consistent-type-imports-V14
爬取时间: 2025-04-30 19:05:44
来源: Huawei Developer
强制使用一致的类型导入风格。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/consistent-type-imports选项。
正例
```typescript
// 默认推荐使用import type Foo from '...'
import type { Foo } from 'Foo';
import type Bar from 'Bar';
export type T = Foo;
export const x: Bar = 1;
```
反例
```typescript
// 默认推荐使用import type Foo from '...'
import { Foo } from 'Foo';
import Bar from 'Bar';
export type T = Foo;
export const x: Bar = 1;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_default-param-last-V14
爬取时间: 2025-04-30 19:06:19
来源: Huawei Developer
强制默认参数位于参数列表的最后一个。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
const defaultValue = 0;
export function f1(a = defaultValue) {
return a;
}
export function f2(a: number, b = defaultValue) {
return a + b;
}
export function f3(a: number, b?: number) {
return b !== undefined ? a + b : a;
}
export function f4(a: number, b?: number, c = defaultValue) {
return b !== undefined ? a + b + c : a + c;
}
export function f5(a: number, b = defaultValue, c?: number) {
return c !== undefined ? a + c : a + b;
}
```
反例
```typescript
const defaultValue = 0;
export function f2(b = defaultValue, a: number) {
return a + b;
}
export function f3(b?: number, a: number) {
return b !== undefined ? a + b : a;
}
export function f4(b?: number, a: number, c = defaultValue) {
return b !== undefined ? a + b + c : a + c;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_dot-notation-V14
爬取时间: 2025-04-30 19:06:54
来源: Huawei Developer
强制使用点表示法。
访问属性有两种方式，一种是点表示法（foo.bar），另一种是括号表示法（foo["bar"]），点表示法更易于阅读，这里推荐使用点表示法。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/dot-notation选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_explicit-function-return-type-V14
爬取时间: 2025-04-30 19:07:31
来源: Huawei Developer
函数和类方法需要显式的定义返回类型。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/explicit-function-return-type选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_explicit-member-accessibility-V14
爬取时间: 2025-04-30 19:08:06
来源: Huawei Developer
在类属性和方法上需要显式定义访问修饰符。
规则配置
选项
详情请参考@typescript-eslint/explicit-member-accessibility选项。
正例
```typescript
export class Animal {
private animalName: string; // Property
public constructor(name: string) {
// Parameter property and constructor
this.animalName = name;
}
public get name(): string {
// get accessor
return this.animalName;
}
public set name(value: string) {
// set accessor
this.animalName = value;
}
public walk() {
// method
}
}
```
反例
```typescript
export class Animal {
private animalName: string; // Property
constructor(name: string) {
// Parameter property and constructor
this.animalName = name;
}
get name(): string {
// get accessor
return this.animalName;
}
set name(value: string) {
// set accessor
this.animalName = value;
}
walk() {
// method
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_explicit-module-boundary-types-V14
爬取时间: 2025-04-30 19:08:42
来源: Huawei Developer
导出到外部的函数和公共类方法，需要显式的定义返回类型和参数类型。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/explicit-module-boundary-types选项。
正例
反例
```typescript
// Should indicate that no value is returned (void)
export function test() {
return;
}
// Should indicate that a string is returned
export const arrowFn = () => 'test';
// All arguments should be typed
export const arrowFn = (arg): string => `test ${arg}`;
export const arrowFn = (arg: any): string => `test ${arg}`;
export class Test {
// Should indicate that no value is returned (void)
public method() {
return;
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_init-declarations-V14
爬取时间: 2025-04-30 19:09:51
来源: Huawei Developer
禁止或者要求在变量声明中进行初始化。
规则配置
选项
详情请参考@typescript-eslint/init-declarations选项。
正例
反例
```typescript
// 默认变量必须在声明时初始化
export function foo() {
console.info('hello');
}
export const bar: string;
export const qux: number;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_keyword-spacing-V14
爬取时间: 2025-04-30 19:10:29
来源: Huawei Developer
强制在关键字之前和关键字之后保持一致的空格风格。
规则配置
选项
详情请参考@typescript-eslint/keyword-spacing选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_lines-between-class-members-V14
爬取时间: 2025-04-30 19:11:06
来源: Huawei Developer
禁止或者要求类成员之间有空行分隔。
规则配置
选项
详情请参考@typescript-eslint/lines-between-class-members选项。
正例
```typescript
// 默认要求类成员成员之间有空行分隔
export class Foo {
public baz() {
console.info('baz');
}
public qux() {
console.info('qux');
}
}
```
反例
```typescript
// 默认要求类成员成员之间有空行分隔
export class Foo {
public baz() {
console.info('baz');
}
public qux() {
console.info('qux');
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_member-delimiter-style-V14
爬取时间: 2025-04-30 19:11:44
来源: Huawei Developer
要求接口和类型别名中的成员之间使用特定的分隔符。
支持定义的分隔符有三种：分号、逗号、无分隔符。
规则配置
选项
详情请参考@typescript-eslint/member-delimiter-style选项。
正例
```typescript
// 默认接口/类型别名定义为多行的场景下，每个成员应以分号 (;) 分隔。 最后一个成员必须有一个分隔符。
// 默认接口/类型别名定义为单行的场景下，每个成员应以分号 (;) 分隔。最后一个成员不能有分隔符。
// 接口/类型别名中的任何换行符都会使其成为多行。
export interface Foo1 {
name: string;
greet(): string;
}
export interface Foo2 { name: string }
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_member-ordering-V14
爬取时间: 2025-04-30 19:12:20
来源: Huawei Developer
要求类、接口和类型字面量中成员的排序方式保持一致的风格。
规则配置
选项
详情请参考@typescript-eslint/member-ordering选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_method-signature-style-V14
爬取时间: 2025-04-30 19:12:56
来源: Huawei Developer
定义函数类型的属性时，强制使用特定的风格。
有两种方式定义对象/接口中函数类型的属性，一种是定义为属性，属性签名是函数，另一种是直接定义为方法。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/method-signature-style选项。
正例
```typescript
// 默认要求定义为属性
export interface T1 {
func: (arg: string) => number;
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_naming-convention-V14
爬取时间: 2025-04-30 19:13:33
来源: Huawei Developer
强制标识符使用一致的命名风格。
规则配置
选项
详情请参考@typescript-eslint/naming-convention选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-array-constructor-V14
爬取时间: 2025-04-30 19:14:09
来源: Huawei Developer
不允许使用“Array”构造函数。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
const length = 500;
Array(length);
export const newArr: number[] = new Array(['1'].length);
export const arr = ['0', '1', '2'];
export const createArray = (array: string) => new Array(array.length);
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-base-to-string-V14
爬取时间: 2025-04-30 19:14:45
来源: Huawei Developer
要求当一个对象在字符串化时提供了有用的信息，才能调用“toString()”方法。
规则配置
选项
详情请参考@typescript-eslint/no-base-to-string选项。
正例
反例
```typescript
interface MyType {
name: string;
}
// Passing an object or class instance to string concatenation:
const obj: MyType = {
name: 'object'
};
export const v1 = '' + obj;
class MyClass {}
const value = new MyClass();
export const v2 = value + '';
// Interpolation and manual .toString() calls too:
export const v3 = `Value: ${value}`;
export const v4 = obj.toString();
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-confusing-non-null-assertion-V14
爬取时间: 2025-04-30 19:15:21
来源: Huawei Developer
不允许在可能产生混淆的位置使用非空断言。
在赋值或者等于旁边使用非空断言（!）会产生混淆，看起来类似于不等于，不建议这种写法。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-confusing-void-expression-V14
爬取时间: 2025-04-30 19:15:57
来源: Huawei Developer
要求void类型的表达式出现在合适的位置。
void指要被忽略的函数返回，如果将void类型的表达式作为值使用，比如分配给变量、作为函数参数传递或者从函数中返回，容易产生误导。
规则配置
选项
详情请参考@typescript-eslint/no-confusing-void-expression选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-dupe-class-members-V14
爬取时间: 2025-04-30 19:16:33
来源: Huawei Developer
不允许重复的类成员。
如果类成员中有同名的声明，最后一个声明会覆盖其他声明，可能会导致意外行为。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
/*eslint no-dupe-class-members: "error"*/
export class A {
public bar() {
console.info('bar');
}
public qux() {
console.info('qux');
}
}
export class B {
private name: string = 'bar';
public get bar() {
return this.name;
}
public set bar(value) {
this.name = value;
}
}
export class E {
public static bar() {
console.info('static bar');
}
public bar() {
console.info('method bar');
}
}
```
反例
```typescript
/*eslint no-dupe-class-members: "error"*/
export class A {
public bar() {
console.info('bar');
}
public bar() {
console.info('bar');
}
}
export class B {
private readonly name: string = 'bar';
public get bar() {
return this.name;
}
public bar() {
return this.name;
}
}
export class E {
public static bar() {
console.info('static bar');
}
public static bar() {
console.info('static bar');
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-duplicate-imports-V14
爬取时间: 2025-04-30 19:17:09
来源: Huawei Developer
禁止重复的模块导入。
规则配置
选项
详情请参考eslint/no-duplicate-imports选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-dynamic-delete-V14
爬取时间: 2025-04-30 19:17:45
来源: Huawei Developer
不允许在computed key表达式上使用“delete”运算符。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
const container: Record<string, number> = {
/* ... */
};
// Constant runtime lookups by string index
delete container.aaa;
// Constants that must be accessed by []
delete container['7'];
delete container['-Infinity'];
```
反例
```typescript
const container: Record<string, number> = {
/* ... */
};
// Can be replaced with the constant equivalents, such as container.aaa
delete container['aaa'];
delete container['Infinity'];
// Dynamic, difficult-to-reason-about lookups
const name = 'name';
delete container[name];
delete container[name.toUpperCase()];
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-empty-function-V14
爬取时间: 2025-04-30 19:18:21
来源: Huawei Developer
不允许使用空函数。
规则配置
选项
详情请参考@typescript-eslint/no-empty-function选项。
正例
该规则旨在消除空函数。如果函数包含注释，则不会将其视为问题。
```typescript
/*eslint no-empty-function: "error"*/
function foo() {
// do nothing.
}
const baz = () => {
foo();
};
export class Bar {
public meth1() {
// do something
}
public meth2() {
baz();
}
}
```
反例
```typescript
/*eslint no-empty-function: "error"*/
function foo() {
}
const baz = () => {
};
export class Bar {
public meth1() {
}
public meth2() {
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-empty-interface-V14
爬取时间: 2025-04-30 19:18:57
来源: Huawei Developer
不允许声明空接口。
规则配置
选项
详情请参考@typescript-eslint/no-empty-interface选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-explicit-any-V14
爬取时间: 2025-04-30 19:19:32
来源: Huawei Developer
不允许使用“any”类型。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/no-explicit-any选项。
正例
```typescript
export const age1 = 17;
export const age2 = [age1];
export const age3 = [age1];
export function greet1(): string {
return 'greet';
}
export function greet2(): string[] {
return ['greet'];
}
export function greet4(): string[][] {
return [['greet']];
}
export function greet5(param: readonly string[]): string {
return param[age1];
}
export function greet6(param: readonly string[]): string[] {
return [...param];
}
```
反例
```typescript
export const age1: any = 17;
export const age2: any = [age1];
export const age3: any = [age1];
export function greet1(): any {
return 'greet';
}
export function greet2(): any[] {
return ['greet'];
}
export function greet4(): any[][] {
return [['greet']];
}
export function greet5(param: readonly any[]): any {
return param[age1];
}
export function greet6(param: readonly any[]): any[] {
return [...param];
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-extraneous-class-V14
爬取时间: 2025-04-30 19:20:08
来源: Huawei Developer
不允许将类用作命名空间。
规则配置
选项
详情请参考@typescript-eslint/no-extraneous-class选项。
正例
反例
```typescript
export class StaticConstants {
public static readonly version = 'development'.length;
public static isProduction() {
return StaticConstants.version === 'production'.length;
}
}
export class HelloWorldLogger {
public constructor() {
console.log('Hello, world!');
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-extra-non-null-assertion-V14
爬取时间: 2025-04-30 19:20:43
来源: Huawei Developer
不允许多余的非空断言。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
interface BarType1 {
bar: number;
}
const foo1: BarType1 | null = null;
export const bar1 = foo1!!!.bar;
export function foo2(bar: number | undefined) {
const newBar: number = bar!!!;
console.info(`${newBar}`);
}
interface BarType2 {
n: number;
}
export function foo(bar?: BarType2) {
return bar!?.n;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-extra-parens-V14
爬取时间: 2025-04-30 19:21:19
来源: Huawei Developer
禁止使用不必要的括号。
规则配置
选项
详情请参考@typescript-eslint/no-extra-parens选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-extra-semi-V14
爬取时间: 2025-04-30 19:21:55
来源: Huawei Developer
禁止使用不必要的分号。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export const x = 5;
export function foo() {
// code
}
export const bar = () => {
// code
};
export class C {
public field: string = 'field';
static {
// code
}
public method() {
// code
}
}
```
反例
```typescript
export const x = 5;;
export function foo() {
// code
};
export const bar = () => {
// code
};;
export class C {
public field: string = 'field';;
static {
// code
};
public method() {
// code
};
};
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-floating-promises-V14
爬取时间: 2025-04-30 19:22:29
来源: Huawei Developer
要求正确处理Promise表达式。
floating-promise是指在创建Promise时，没有使用任何代码来处理它可能引发的错误，这是一种不正确的使用方式。
规则配置
选项
详情请参考@typescript-eslint/no-floating-promises选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-for-in-array-V14
爬取时间: 2025-04-30 19:23:04
来源: Huawei Developer
禁止使用 for-in 循环来遍历数组元素。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
declare const array: string[];
for (const value of array) {
console.log(value);
}
array.forEach((value) => {
console.log(value);
});
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-implicit-any-catch-V14
爬取时间: 2025-04-30 19:23:39
来源: Huawei Developer
禁止在 catch 表达式中使用隐式“any”类型
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则默认不允许使用隐式any类型。但是可以接受{"allowExplicitAny": true}对象作为规则参数，以允许使用显式的any类型。
示例：
在配置{"allowExplicitAny": true}的条件下，以下代码不会产生告警：
正例
```typescript
try {
// ...
} catch (e: unknown) {
// ...
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-implied-eval-V14
爬取时间: 2025-04-30 19:24:14
来源: Huawei Developer
禁止使用类似“eval()”的方法。
setTimeout()、setInterval()、setImmediate()或者execScript()这些函数可以接受一个字符串作为其第一个参数，比如
这种行为被认为是隐式“eval()”，不推荐使用。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
function alert(arg: string) {
console.log(arg);
}
const time = 100;
setTimeout(() => {
alert('Hi!');
}, time);
setInterval(() => {
alert('Hi!');
}, time);
const fn = () => {
console.info('fn');
};
setTimeout(fn, time);
class Foo {
public static fn = () => {
console.info('static');
};
public meth() {
console.info('method');
}
}
setTimeout(Foo.fn, time);
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-inferrable-types-V14
爬取时间: 2025-04-30 19:24:51
来源: Huawei Developer
不允许对初始化为数字、字符串或布尔值的变量或参数进行显式类型声明。
变量或者参数如果在初始化时定义为布尔、数字或者字符串类型，Typescript可以推断出其类型，不用显式声明其类型。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/no-inferrable-types选项。
正例
反例
```typescript
const num: number = 10;
export const a1: bigint = 10n;
export const a2: bigint = BigInt(num);
export const a3: boolean = !num;
export const a4: boolean = Boolean(null);
export const a5: boolean = true;
export const a6: null = null;
export class Foo {
public prop: number = num;
}
export function fn(a: number = num, b: boolean = true): void {
console.info(`${a}${b}`);
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-invalid-this-V14
爬取时间: 2025-04-30 19:25:25
来源: Huawei Developer
禁止在this的值为undefined的上下文中使用this。
规则配置
选项
详情请参考@typescript-eslint/no-invalid-this选项。
正例
```typescript
function baz(arg0: () => object) {
return arg0;
}
export class Bar {
public a: number;
public constructor() {
this.a = 0;
baz(() => this);
}
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-invalid-void-type-V14
爬取时间: 2025-04-30 19:26:00
来源: Huawei Developer
禁止在返回类型或者泛型类型之外使用void。
规则配置
选项
详情请参考@typescript-eslint/no-invalid-void-type选项。
正例
```typescript
export type NoOp = () => void;
export function noop(): void {
console.info('noop');
}
export const trulyUndefined = void Number.MAX_VALUE;
export async function promiseMeSomething(): Promise<void> {
return Promise.reject('value').catch(() => {
console.error('error');
});
}
export type StillVoid = void | never;
```
反例
```typescript
// 不允许使用void作为类型
export type PossibleValues = string | number | void;
// 不允许使用void作为类型
export type MorePossibleValues = string | (string | void);
// 不允许使用void作为类型
export function logSomething(thing: void) {
return thing;
}
export function printArg<T = void>(arg: T) {
return arg;
}
export interface Interface {
lambda: () => void;
// 不允许使用void作为类型
prop: void;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-loop-func-V14
爬取时间: 2025-04-30 19:26:35
来源: Huawei Developer
禁止在循环语句内包含不安全引用的函数声明。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-loss-of-precision-V14
爬取时间: 2025-04-30 19:27:10
来源: Huawei Developer
禁止使用失去精度的字面数字。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-magic-numbers-V14
爬取时间: 2025-04-30 19:27:46
来源: Huawei Developer
禁止使用魔法数字。
“魔法数字”是在代码中多次出现但没有明确含义的数字，最好将它们替换为常量。
规则配置
选项
详情请参考@typescript-eslint/no-magic-numbers选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-misused-new-V14
爬取时间: 2025-04-30 19:28:22
来源: Huawei Developer
要求正确地定义“new”和“constructor”。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export declare class C {
public name: string;
public constructor();
}
```
反例
```typescript
export declare class C {
// 应该定义为constructor(): C
public new(): C;
}
export interface I {
// 不应该定义constructor
constructor(): void;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-misused-promises-V14
爬取时间: 2025-04-30 19:28:57
来源: Huawei Developer
禁止在不正确的位置使用Promise。
规则配置
选项
详情请参考@typescript-eslint/no-misused-promises选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-namespace-V14
爬取时间: 2025-04-30 19:29:31
来源: Huawei Developer
禁止使用 TypeScript语法中的命名空间。
命名空间是一种过时的语法，推荐使用import/export。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/no-namespace选项。
正例
```typescript
// foo为模块名
declare module 'foo' {}
// anything inside a d.ts file
```
反例
```typescript
module foo {}
namespace foo {}
declare module foo {}
declare namespace foo {}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-non-null-asserted-optional-chain-V14
爬取时间: 2025-04-30 19:30:06
来源: Huawei Developer
禁止在可选链表达式之后使用非空断言。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
class CC {
public bar: string = 'hello';
public foo() {
console.info('foo');
}
}
function getInstance(): CC | undefined {
return new CC();
}
const instance = getInstance();
console.info(`${instance?.bar!}`);
instance?.foo()!;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-non-null-assertion-V14
爬取时间: 2025-04-30 19:30:40
来源: Huawei Developer
禁止以感叹号作为后缀的方式使用非空断言。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
interface Example {
property?: string;
}
declare const example: Example;
export const includesBaz = example.property?.includes('baz') ?? false;
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-parameter-properties-V14
爬取时间: 2025-04-30 19:31:14
来源: Huawei Developer
禁止在类构造函数中使用参数属性。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
默认禁止在构造函数中使用任何参数属性，如果想要使用某些属性，可以配置额外选项。
allows：接受一个字符串数组，数组中的属性可以使用。字符串支持以下值：
正例
```typescript
export class Foo {
public name: string;
public constructor(name: string) {
this.name = name;
}
}
```
反例
```typescript
export class Foo {
// 默认配置下，参数不允许使用readonly
public constructor(public readonly name: string) {}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-redeclare-V14
爬取时间: 2025-04-30 19:31:48
来源: Huawei Developer
禁止变量重复声明。
规则配置
选项
详情请参考@typescript-eslint/no-redeclare选项。
正例
```typescript
let a = '3';
a = '10';
console.info(a);
export class C {
static {
let c = '3';
c = '10';
console.info(c);
}
public foo() {
let b = '3';
b = '10';
console.info(b);
}
}
```
反例
```typescript
// 不允许重复声明变量a
const a = '3';
const a = '10';
export class C {
static {
// 不允许重复声明变量c
const c = '3';
const c = '10';
}
public foo() {
// 不允许重复声明变量b
const b = '3';
const b = '10';
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-require-imports-V14
爬取时间: 2025-04-30 19:32:21
来源: Huawei Developer
禁止使用“require()”语法导入依赖。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-restricted-syntax-V14
爬取时间: 2025-04-30 19:32:55
来源: Huawei Developer
不允许使用指定的（即用户在规则中定义的）语法。
规则配置
选项
详情请参考@typescript-eslint/no-restricted-syntax选项。
正例
反例
```typescript
/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export class CC {
public name: string;
public constructor(name: string) {
this.name = name;
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-shadow-V14
爬取时间: 2025-04-30 19:33:30
来源: Huawei Developer
禁止声明与外部作用域变量同名的变量。
规则配置
选项
详情请参考@typescript-eslint/no-shadow选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-this-alias-V14
爬取时间: 2025-04-30 19:34:04
来源: Huawei Developer
禁止将“this”赋值给一个变量。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/no-this-alias选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-throw-literal-V14
爬取时间: 2025-04-30 19:34:38
来源: Huawei Developer
禁止将字面量作为异常抛出。
规则配置
选项
详情请参考@typescript-eslint/no-throw-literal选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-type-alias-V14
爬取时间: 2025-04-30 19:35:12
来源: Huawei Developer
禁止使用类型别名。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/no-type-alias选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unnecessary-boolean-literal-compare-V14
爬取时间: 2025-04-30 19:35:46
来源: Huawei Developer
禁止将布尔值和布尔字面量直接进行比较。
规则配置
选项
详情请参考@typescript-eslint/no-unnecessary-boolean-literal-compare选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unnecessary-condition-V14
爬取时间: 2025-04-30 19:36:22
来源: Huawei Developer
不允许使用类型始终为真或始终为假的表达式作为判断条件。
规则配置
选项
详情请参考@typescript-eslint/no-unnecessary-condition选项。
正例
```typescript
const index = 0;
export function head(items: readonly string[]): string {
// Necessary, since items.length might be 0
if (items.length) {
return items[index].toUpperCase();
} else {
return '';
}
}
export function foo(arg: string): void {
// Necessary, since foo might be ''.
if (arg) {
}
}
export function bar(arg?: string | null) {
// Necessary, since arg might be nullish
return arg?.length;
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unnecessary-qualifier-V14
爬取时间: 2025-04-30 19:36:56
来源: Huawei Developer
禁止不必要的命名空间限定符。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export enum A {
b = 'x',
c = b
}
export namespace B {
export type C = number;
export const x: C = 3;
}
```
反例
```typescript
export enum A {
b = 'x',
c = A.b
}
export namespace B {
export type C = number;
export const x: B.C = 3;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unnecessary-type-arguments-V14
爬取时间: 2025-04-30 19:37:31
来源: Huawei Developer
当类型参数和默认值相同时，不允许显式使用。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
function f<T = number>(para: T): void {
console.info(`${para as number}`);
}
f(Number.MAX_VALUE);
f<string>('hello');
function g<T = number, U = string>(para1: T, para2?: U) {
if (para2 !== undefined) {
console.info(`${para2 as string}`);
}
console.info(`${para1 as number}`);
}
g<string>('para1', 'para2');
g<number, number>(Number.MAX_VALUE);
class C<T = number> {
public name: T;
public constructor(name: T) {
this.name = name;
}
}
new C(Number.MAX_VALUE);
new C<string>('hello');
```
反例
```typescript
function f<T = number>(para: T): void {
console.info(`${para as number}`);
}
// 参数类型默认是number，直接使用f()即可
f<number>(Number.MAX_VALUE);
function g<T = number, U = string>(para1: T, para2?: U) {
if (para2 !== undefined) {
console.info(`${para2 as string}`);
}
console.info(`${para1 as number}`);
}
// 第二个参数类型默认是string，直接使用g<string>()即可
g<string, string>('hello');
class C<T = number> {
public meth(para: T): void {
console.info(`${para as number}`);
}
}
// 参数类型默认是number，直接使用new C()即可
new C<number>();
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unnecessary-type-assertion-V14
爬取时间: 2025-04-30 19:38:05
来源: Huawei Developer
禁止不必要的类型断言。
如果类型断言没有更改表达式的类型，也就没有必要使用。
规则配置
选项
详情请参考@typescript-eslint/no-unnecessary-type-assertion选项。
正例
```typescript
const num = 3;
export const foo2 = num as number;
export const foo3 = 'foo' as string;
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unnecessary-type-constraint-V14
爬取时间: 2025-04-30 19:38:39
来源: Huawei Developer
不允许在泛型中使用不必要的约束条件。
泛型参数（<T>）如果不包含“extends”关键字，默认约束条件是“unknown”（即<T extends unknown>），所以“<T extends any>“、“<T extends unknown>“的写法是多余的。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export interface Foo<T> {
foo: T;
}
export const bar = <T>(param: T): void => {
console.info(`${param as string}`);
};
export function foo<T>(param: T): void {
console.info(`${param as string}`);
}
```
反例
```typescript
// extends any或者extends unknown的写法是多余的
export interface Foo<T extends any> {
foo: T;
}
export const bar = <T extends unknown>(param: T): void => {
console.info(`${param as string}`);
};
export function foo<T extends any>(param: T): void {
console.info(`${param as string}`);
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-argument-V14
爬取时间: 2025-04-30 19:39:14
来源: Huawei Developer
不允许将any类型的值作为函数的参数传入。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
declare function foo(arg1: string, arg2: number, arg3: string): void;
const anyTyped = Number.MAX_VALUE as any;
// 变量anyTyped是any类型，不允许作为参数传入函数中
foo(...anyTyped);
// 变量anyTyped是any类型，不允许作为参数传入函数中
foo(anyTyped, Number.MAX_VALUE, 'a');
const anyArray: any[] = [];
// 变量anyArray是any类型数组，不允许将数组元素作为参数传入函数中
foo(...anyArray);
const tuple1 = ['a', anyTyped, 'b'] as const;
// 变量anyTyped是any类型数组，不允许将数组元素作为参数传入函数中
foo(...tuple1);
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-assignment-V14
爬取时间: 2025-04-30 19:39:48
来源: Huawei Developer
禁止将“any”类型的值赋值给变量和属性。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
let [x] = ['1'];
[x] = ['1'] as [string];
console.info([x].toString());
// generic position examples
export const a1: Set<string> = new Set<string>();
export const a2: Map<string, string> = new Map<string, string>();
export const a3: Set<string[]> = new Set<string[]>();
export const a4: Set<Set<Set<string>>> = new Set<Set<Set<string>>>();
```
反例
```typescript
let [x] = ['1'];
[x] = ['1'] as [any];
[x] = '1' as any;
console.info([x].toString());
// generic position examples
export const a1: Set<string> = new Set<any>();
export const a2: Map<string, string> = new Map<any, string>();
export const a3: Set<string[]> = new Set<any[]>();
export const a4: Set<Set<Set<string>>> = new Set<Set<Set<any>>>();
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-call-V14
爬取时间: 2025-04-30 19:40:22
来源: Huawei Developer
禁止调用“any”类型的表达式。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
declare const typedVar: () => void;
declare const typedNested: { prop: { a: () => void } };
typedVar();
typedNested.prop.a();
((): void => {
console.info('hello');
})();
new Map();
export const raw = String.raw`foo`;
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-member-access-V14
爬取时间: 2025-04-30 19:40:56
来源: Huawei Developer
禁止成员访问“any”类型的值。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
declare const properlyTyped: { prop: { a: string } };
export const v1 = properlyTyped.prop.a;
const key = 'a';
export const v2 = properlyTyped.prop[key];
const arr = ['1', '2', '3'];
let idx = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];
```
反例
```typescript
declare const properlyTyped: { prop: { a: any } };
export const v1 = properlyTyped.prop.a;
const key = 'a' as any;
export const v2 = properlyTyped.prop[key];
const arr = ['1', '2', '3'];
let idx: any = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-return-V14
爬取时间: 2025-04-30 19:41:30
来源: Huawei Developer
函数禁止返回类型为“any”的值。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export function foo1(): string {
return '1';
}
export function foo2(): object {
return Object.create(null) as Record<string, unknown>;
}
export const foo3 = (): object[] => [];
export const foo4 = (): string[] => ['a'];
export function assignability1(): Set<string> {
return new Set<string>(['foo']);
}
```
反例
```typescript
export function foo1(): string {
return '1' as any;
}
export function foo2(): string {
return Object.create(null) as any;
}
export const foo3 = (): object[] => [] as any;
export const foo4 = (): string[] => ['a'] as any;
export function assignability1(): Set<string> {
return new Set<string>(['foo']) as any;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unused-expressions-V14
爬取时间: 2025-04-30 19:42:05
来源: Huawei Developer
代码中禁止包含未使用的表达式。
规则配置
选项
详情请参考@typescript-eslint/no-unused-expressions选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unused-vars-V14
爬取时间: 2025-04-30 19:42:39
来源: Huawei Developer
禁止定义未使用的变量。
规则配置
选项
详情请参考@typescript-eslint/no-unused-vars选项。
正例
```typescript
const x = 10;
console.info(`${x}`);
((foo) => {
return foo;
})();
const num = 50;
let myFunc1: () => number = () => num;
myFunc1 = () => setTimeout(() => {
// myFunc is considered used
myFunc1();
}, num);
```
反例
```typescript
const x = 10;
((foo) => {
return 'hello';
})();
const num = 50;
const myFunc1: () => number = () => num;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-use-before-define-V14
爬取时间: 2025-04-30 19:43:14
来源: Huawei Developer
禁止在变量声明之前使用变量。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/no-use-before-define选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-useless-constructor-V14
爬取时间: 2025-04-30 19:43:48
来源: Huawei Developer
禁止不必要的构造函数。
不必要的构造函数包括：空的构造函数，或者构造函数中直接执行父类构造函数的逻辑。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
class A {
public name: string = 'hello';
}
export class B {
public name: string = 'name';
public constructor() {
console.info('hello');
}
}
export class C extends A {
public constructor() {
super();
console.info('hello');
}
}
```
反例
```typescript
class A {
public name: string = 'name';
constructor() {
}
}
export class B extends A {
public name: string = 'name';
constructor() {
super();
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-as-const-V14
爬取时间: 2025-04-30 19:44:23
来源: Huawei Developer
对于字面量类型，强制使用“as const”。
将字面量类型的值转换为对应的字面量类型，有两种方式，一种是“as const”，另一种是“as 字面量类型”，推荐使用“as const”。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export const foo1 = 'bar';
export const foo2 = 'bar' as const;
export const foo3: 'bar' = 'bar' as const;
export const bar4 = 'bar' as string;
export const foo6 = { bar: 'baz' };
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-enum-initializers-V14
爬取时间: 2025-04-30 19:44:57
来源: Huawei Developer
推荐显式初始化每个枚举成员值。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-for-of-V14
爬取时间: 2025-04-30 19:45:32
来源: Huawei Developer
强制使用“for-of”循环而不是标准“for”循环。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
declare const array: string[];
for (const x of array) {
console.log(x);
}
for (let i = 0; i < array.length; i++) {
// i is used, so for-of could not be used.
console.log(`${i}-${array[i]}`);
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-function-type-V14
爬取时间: 2025-04-30 19:46:06
来源: Huawei Developer
强制使用函数类型而不是带有签名的对象类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export function foo(example: () => number): number {
return example();
}
// returns the function itself, not the `this` argument.
export type ReturnsSelf = (arg: string) => ReturnsSelf;
export interface Foo {
bar: string;
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-includes-V14
爬取时间: 2025-04-30 19:46:39
来源: Huawei Developer
强制使用“includes”方法而不是“indexOf”方法。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-literal-enum-member-V14
爬取时间: 2025-04-30 19:47:14
来源: Huawei Developer
要求所有枚举成员都定义为字面量值。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
详情请参考@typescript-eslint/prefer-literal-enum-member选项。
正例
反例
```typescript
const str = 'Test';
export enum Invalid {
a = str, // Variable assignment
b = {}, // Object assignment
c = `A template literal string`, // Template literal
d = new Set(1, 2, 3), // Constructor in assignment
e = 2 + 2 // Expression assignment
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-namespace-keyword-V14
爬取时间: 2025-04-30 19:47:49
来源: Huawei Developer
推荐使用“namespace”关键字而不是“module”关键字来声明一个自定义的 TypeScript 模块。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-nullish-coalescing-V14
爬取时间: 2025-04-30 19:48:23
来源: Huawei Developer
强制使用空合并运算符（??）而不是逻辑运算符。
规则配置
选项
详情请参考@typescript-eslint/prefer-nullish-coalescing选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-optional-chain-V14
爬取时间: 2025-04-30 19:48:58
来源: Huawei Developer
强制使用链式可选表达式，而不是链式逻辑与、否定逻辑或、或空对象。
规则配置
选项
详情请参考@typescript-eslint/prefer-optional-chain选项。
正例
```typescript
class Foo {
public a?: Foo = new Foo();
public b?: Foo = new Foo();
public c?: Foo = new Foo();
public method?(): void {
console.info('method');
}
}
const foo = new Foo();
export const c = foo.a?.b?.c;
foo.a?.b?.method?.();
```
反例
```typescript
class Foo {
public a?: Foo = new Foo();
public b?: Foo = new Foo();
public c?: Foo = new Foo();
public method?(): void {
console.info('method');
}
}
const foo = new Foo();
let c = foo.a;
c = c && c.b;
c = c && c.c;
export { c };
if (foo.a && foo.a.b && foo.a.b.method) {
foo.a.b.method();
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-readonly-V14
爬取时间: 2025-04-30 19:49:34
来源: Huawei Developer
如果私有成员从未在构造函数之外进行修改，则要求将其标记为“只读”。
规则配置
选项
详情请参考@typescript-eslint/prefer-readonly选项。
正例
```typescript
export class Container {
// Public members might be modified externally
public publicMember: boolean = true;
// Protected members might be modified by child classes
protected protectedMember: number = Number.MAX_VALUE;
// This is modified later on by the class
private modifiedLater = 'unchanged';
public mutate() {
this.modifiedLater = 'mutated';
}
}
```
反例
```typescript
export class Container {
// These member variables could be marked as readonly
private neverModifiedMember = true;
private onlyModifiedInConstructor: number;
// Private parameter properties can also be marked as readonly
private neverModifiedParameter: string;
public constructor(
onlyModifiedInConstructor: number,
// Private parameter properties can also be marked as readonly
neverModifiedParameter: string,
) {
this.neverModifiedParameter = neverModifiedParameter;
this.onlyModifiedInConstructor = onlyModifiedInConstructor;
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-readonly-parameter-types-V14
爬取时间: 2025-04-30 19:50:10
来源: Huawei Developer
要求将函数参数解析为“只读”类型，以防止参数被修改而产生一些副作用。
该规则校验比较严格，由开发者自主判断是否需要修复告警。
规则配置
选项
详情请参考@typescript-eslint/prefer-readonly-parameter-types选项。
正例
```typescript
const index = 0;
export function array1(arg: readonly string[]): void {
console.info(`${arg[index]}`);
}
export function array2(arg: readonly (readonly string[])[]): void {
console.info(`${arg[index][index]}`);
}
export function array3(arg: readonly [string, number]): void {
console.info(`${arg[index][index]}`);
}
export function array4(arg: readonly [readonly string[], number]): void {
console.info(`${arg[index][index]}`);
}
export function primitive1(arg: string): void {
console.info(`${arg}`);
}
export function primitive2(arg: number): void {
console.info(`${arg}`);
}
export function primitive3(arg: boolean): void {
console.info(`${arg}`);
}
export function primitive5(arg: null): void {
console.info(`${arg}`);
}
export function primitive6(arg: undefined): void {
console.info(`${arg}`);
}
```
反例
```typescript
const index = 0;
export function array1(arg: string[]): void {
console.info(`${arg[index]}`);
}
export function array2(arg: (string[])[]): void {
console.info(`${arg[index][index]}`);
}
export function array3(arg: [string, number]): void {
console.info(`${arg[index][index]}`);
}
export function array4(arg: [string[], number]): void {
console.info(`${arg[index][index]}`);
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-reduce-type-parameter-V14
爬取时间: 2025-04-30 19:50:46
来源: Huawei Developer
调用“Array#reduce”时推荐使用类型参数而不是强制转换类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
['1', '2', '3'].reduce<readonly string[]>((arr, text) => {
const newArr = [...arr];
newArr.push(text);
return newArr;
}, []);
```
反例
```typescript
['1', '2', '3'].reduce((arr, text) => {
const newArr = [...arr];
newArr.push(text);
return newArr;
}, [] as readonly string[]);
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-regexp-exec-V14
爬取时间: 2025-04-30 19:51:22
来源: Huawei Developer
如果未提供全局标志，推荐使用RegExp#exec”，而不是“String#match”。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-string-starts-ends-with-V14
爬取时间: 2025-04-30 19:51:58
来源: Huawei Developer
强制使用“String#startsWith”和“String#endsWith”而不是其他检查子字符串的等效方法。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
declare const foo: string;
declare const index: number;
// starts with
foo[index] === 'b';
foo.charAt(index) === 'b';
foo.indexOf('bar') === index;
foo.slice(index) === 'bar';
foo.substring(index) === 'bar';
foo.match(/^bar/) !== null;
/^bar/.test(foo);
// ends with
foo[foo.length - index] === 'b';
foo.charAt(foo.length - index) === 'b';
foo.lastIndexOf('bar') === foo.length - index;
foo.slice(-index) === 'bar';
foo.substring(foo.length - index) === 'bar';
foo.match(/bar$/) !== null;
/bar$/.test(foo);
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-ts-expect-error-V14
爬取时间: 2025-04-30 19:52:34
来源: Huawei Developer
强制使用“@ts-expect-error”而不是“@ts-ignore”。
该规则仅支持对.js/.ts文件进行检查。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// @ts-expect-error: with description
export const str: string = 1;
/**
* Explaining comment
*
* @ts-expect-error: with description */
export const multiLine: number = 'value';
/** @ts-expect-error: with description */
export const block: string = 1;
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_promise-function-async-V14
爬取时间: 2025-04-30 19:53:11
来源: Huawei Developer
要求任何返回Promise的函数或方法标记为async。
规则配置
选项
详情请参考@typescript-eslint/promise-function-async选项。
正例
```typescript
export const arrowFunctionReturnsPromise = async () => Promise.resolve('value');
export async function functionReturnsPromise() {
return Promise.resolve('value');
}
// An explicit return type that is not Promise means this function cannot be made async, so it is ignored by the rule
export function functionReturnsUnionWithPromiseExplicitly(
p: boolean
): string | Promise<string> {
return p ? 'value' : Promise.resolve('value');
}
export async function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
return p ? 'value' : Promise.resolve('value');
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_quotes-V14
爬取时间: 2025-04-30 19:53:47
来源: Huawei Developer
强制使用一致的反引号、双引号或单引号风格。
规则配置
选项
详情请参考@typescript-eslint/quotes选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_require-array-sort-compare-V14
爬取时间: 2025-04-30 19:54:25
来源: Huawei Developer
要求调用“Array#sort”时，始终提供“compareFunction”。
规则配置
选项
详情请参考@typescript-eslint/require-array-sort-compare选项。
正例
```typescript
declare const array: string[];
array.sort((a, b) => a.length - b.length);
array.sort((a, b) => a.localeCompare(b));
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_require-await-V14
爬取时间: 2025-04-30 19:55:00
来源: Huawei Developer
异步函数必须包含“await”。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_restrict-plus-operands-V14
爬取时间: 2025-04-30 19:55:35
来源: Huawei Developer
要求加法的两个操作数都是相同的类型，并且是“bigint”、“number”或“string”。
规则配置
选项
详情请参考@typescript-eslint/restrict-plus-operands选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_restrict-template-expressions-V14
爬取时间: 2025-04-30 19:56:11
来源: Huawei Developer
要求模板表达式中的变量为“string”类型。
规则配置
选项
详情请参考@typescript-eslint/restrict-template-expressions选项。
正例
```typescript
const arg: string | undefined = 'foo';
export const msg1 = `arg = ${arg}`;
export const msg2 = `arg = ${arg || 'default'}`;
```
反例
```typescript
const arg1 = ['1', '2'];
export const msg1 = `arg1 = ${arg1}`;
interface GeneratedObjectLiteralInterface {
name: string;
}
const arg2: GeneratedObjectLiteralInterface = { name: 'Foo' };
export const msg2 = `arg2 = ${arg2 || null}`;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_return-await-V14
爬取时间: 2025-04-30 19:56:46
来源: Huawei Developer
要求异步函数返回“await”。
规则配置
选项
详情请参考@typescript-eslint/return-await选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_semi-V14
爬取时间: 2025-04-30 19:57:22
来源: Huawei Developer
要求或不允许使用分号。
规则配置
选项
详情请参考@typescript-eslint/semi选项。
正例
```typescript
export const name = 'ESLint';
export class Foo {
public bar = '1';
}
```
反例
```typescript
// 默认在语句末尾需要加分号
export const name = 'ESLint'
export class Foo {
// 默认在语句末尾需要加分号
public bar = '1'
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_space-before-function-paren-V14
爬取时间: 2025-04-30 19:57:57
来源: Huawei Developer
强制在函数名和括号之间保持一致的空格风格。
规则配置
选项
详情请参考@typescript-eslint/space-before-function-paren选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_space-infix-ops-V14
爬取时间: 2025-04-30 19:58:34
来源: Huawei Developer
运算符前后要求有空格。
规则配置
选项
详情请参考@typescript-eslint/space-infix-ops选项。
正例
```typescript
declare const a: number;
declare const b: number;
export const c = a + b;
```
反例
```typescript
declare const a: number;
declare const b: number;
export const c = a+b;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_strict-boolean-expressions-V14
爬取时间: 2025-04-30 19:59:10
来源: Huawei Developer
不允许在布尔表达式中使用非布尔类型。
规则配置
选项
详情请参考@typescript-eslint/strict-boolean-expressions选项。
正例
```typescript
// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
return undefined;
}
const num: number | undefined = getNum();
if (num !== undefined) {
console.log('num is defined');
}
function getStr(): string | null {
return 'null';
}
const str: string | null = getStr();
if (str !== null) {
console.log('str is not empty');
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_switch-exhaustiveness-check-V14
爬取时间: 2025-04-30 19:59:45
来源: Huawei Developer
要求switch语句对于联合类型中值的判断是详尽无遗的。
当switch语句中的判断条件是字面量值的集合或者是一个枚举类型，如果case语句中缺少任何一个值的判断，并且没有default语句时，此规则会告警。
规则配置
选项
详情请参考@typescript-eslint/switch-exhaustiveness-check选项。
正例
```typescript
type Day =
| 'Monday'
| 'Tuesday'
| 'Wednesday'
| 'Thursday'
| 'Friday'
| 'Saturday'
| 'Sunday';
declare const day1: Day;
let result = '0';
switch (day1) {
case 'Monday':
result = '1';
break;
case 'Tuesday':
result = '2';
break;
case 'Wednesday':
result = '3';
break;
case 'Thursday':
result = '4';
break;
case 'Friday':
result = '5';
break;
case 'Saturday':
result = '6';
break;
case 'Sunday':
result = '7';
break;
}
declare const day2: Day;
result = '0';
switch (day2) {
case 'Monday':
result = '1';
break;
default:
result = '42';
}
console.info(result);
enum Fruit {
apple = 'apple',
banana = 'banana',
cherry = 'cherry'
}
declare const fruit: Fruit;
switch (fruit) {
case Fruit.apple:
console.log('an apple');
break;
case Fruit.banana:
console.log('a banana');
break;
case Fruit.cherry:
console.log('a cherry');
break;
}
```
反例
```typescript
type Day =
| 'Monday'
| 'Tuesday'
| 'Wednesday'
| 'Thursday'
| 'Friday'
| 'Saturday'
| 'Sunday';
declare const day: Day;
let result = '0';
switch (day) {
// 只处理了'Monday'，缺少其他值的判断，并且也没有default分支
case 'Monday':
result = '1';
break;
}
console.info(result);
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_triple-slash-reference-V14
爬取时间: 2025-04-30 20:00:20
来源: Huawei Developer
不允许某些三斜杠引用，推荐使用ES6风格的导入声明。
支持以下三种三斜杠引用方式的检查
规则配置
选项
详情请参考@typescript-eslint/triple-slash-reference选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_type-annotation-spacing-V14
爬取时间: 2025-04-30 20:00:56
来源: Huawei Developer
类型注释前后需要一致的空格风格。
规则配置
选项
详情请参考@typescript-eslint/type-annotation-spacing选项。
正例
```typescript
// 默认冒号前无空格，冒号后有空格
export const foo1: string = 'bar';
export declare function foo2(): string;
export class Foo3 {
public name: string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = () => void;
```
反例
```typescript
// 默认冒号前无空格，冒号后有空格
export const foo1 :string = 'bar';
export declare function foo2() :string;
export class Foo3 {
public name :string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = ()=>void;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_typedef-V14
爬取时间: 2025-04-30 20:01:30
来源: Huawei Developer
在某些位置需要类型注释。
支持检查的范围从选项中查看。
规则配置
选项
详情请参考@typescript-eslint/typedef选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_unbound-method-V14
爬取时间: 2025-04-30 20:02:06
来源: Huawei Developer
强制类作用域中的方法在预期范围内调用。
类方法作为独立变量传递时，不会保留类作用域，“this”不再指代当前类。解决方法是定义为“this: void”或者使用箭头函数。
规则配置
选项
详情请参考@typescript-eslint/unbound-method选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_unified-signatures-V14
爬取时间: 2025-04-30 20:02:41
来源: Huawei Developer
如果两个重载函数可以用联合类型参数（|）、可选参数（?）或者剩余参数（...）来重构成一个函数，不允许使用重载。
规则配置
选项
详情请参考@typescript-eslint/unified-signatures选项。
正例
```typescript
export declare function x(a: number | string): void;
export declare function y(...a: readonly number[]): void;
```
反例
```typescript
export declare function x(a: number): void;
export declare function x(a: string): void;
export declare function y(): void;
export declare function y(...a: readonly number[]): void;
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_prefer-const-V14
爬取时间: 2025-04-30 20:03:17
来源: Huawei Developer
推荐声明后未修改值的变量用const关键字来声明。
规则配置
选项
该规则无需配置额外选项。详情请参考eslint/prefer-const选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_eqeqeq-V14
爬取时间: 2025-04-30 20:03:51
来源: Huawei Developer
要求使用===和!==。
规则配置
选项
该规则无需配置额外选项。详情请参考eslint/eqeqeq选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-security-V14
爬取时间: 2025-04-30 20:04:26
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-commented-code-V14
爬取时间: 2025-04-30 20:05:01
来源: Huawei Developer
不使用的代码段建议直接删除，不允许通过注释的方式保留。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-cycle-V14
爬取时间: 2025-04-30 20:05:38
来源: Huawei Developer
该规则禁止使用循环依赖。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-aes-V14
爬取时间: 2025-04-30 20:06:14
来源: Huawei Developer
该规则禁止在AES加密算法中使用不安全的ECB加密模式，推荐使用Petal Aegis SDK中的安全AES接口，详情请参见对称加解密。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-dh-V14
爬取时间: 2025-04-30 20:06:53
来源: Huawei Developer
该规则禁止使用不安全的DH密钥协商算法，如DH模数长度小于2048bit。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-dh-key-V14
爬取时间: 2025-04-30 20:07:29
来源: Huawei Developer
该规则禁止使用不安全的DH密钥，如DH模数长度小于2048bit。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-dsa-V14
爬取时间: 2025-04-30 20:08:05
来源: Huawei Developer
该规则禁止使用不安全的DSA签名算法，如DSA模数长度小于2048bit、摘要中使用不安全的SHA1哈希算法。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-dsa-key-V14
爬取时间: 2025-04-30 20:08:40
来源: Huawei Developer
该规则禁止使用不安全的DSA密钥，如DSA模数长度小于2048bit。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-ecdsa-V14
爬取时间: 2025-04-30 20:09:16
来源: Huawei Developer
该规则禁止在ECDSA签名算法中使用不安全的SHA1摘要算法，推荐使用Petal Aegis SDK中的安全ECDSA接口，详情参见：ECDSA签名验签。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-hash-V14
爬取时间: 2025-04-30 20:09:51
来源: Huawei Developer
该规则使用禁止不安全的哈希算法，例如MD5、SHA1。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-mac-V14
爬取时间: 2025-04-30 20:10:27
来源: Huawei Developer
该规则禁止在MAC消息认证算法中使用不安全的哈希算法，例如SHA1。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-rsa-encrypt-V14
爬取时间: 2025-04-30 20:11:03
来源: Huawei Developer
该规则禁止使用不安全的RSA非对称加密算法，如RSA模数长度小于2048bit、填充模式为PKCS1、摘要或掩码摘要中使用不安全的MD5或SHA1哈希算法，推荐使用Petal Aegis SDK中的安全RSA加密和解密接口，详情参见：RSA加解密。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-rsa-key-V14
爬取时间: 2025-04-30 20:11:39
来源: Huawei Developer
该规则禁止使用不安全的RSA密钥，如RSA模数长度小于2048bit。推荐使用Petal Aegis SDK中的安全RSA签名接口，详情参见：RSA密钥。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unsafe-rsa-sign-V14
爬取时间: 2025-04-30 20:12:16
来源: Huawei Developer
该规则禁止不安全的RSA签名算法，如RSA模数长度小于2048bit、摘要或掩码摘要中使用不安全的MD5或SHA1哈希算法。推荐使用Petal Aegis SDK中的安全RSA签名接口，详情参见：RSA加解密。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-specified-interface-call-chain-check-V14
爬取时间: 2025-04-30 20:12:52
来源: Huawei Developer
该规则旨在标识指定接口的调用链，方便接口管理，调用链最大数量为5000。
规则配置
选项
该规则无需配置额外选项。
正例
下文中absolute-path-1.ets为依赖代码：
```typescript
// Absolute-Path1.ets
export class Cls1 {
public func1() {
console.log('This is func1 in cls1.');
}
public func2() {
console.log('This is func2 in cls1.');
}
}
```
下文中Correct.ets为正例测试代码，依赖上文中AbsolutePath1.ets：
反例
下文中absolute-path-1.ets为依赖代码：
```typescript
// absolute-path-1.ets
export class cls1 {
public func1() {
console.log('This is func1 in cls1.');
}
public func2() {
console.log('This is func2 in cls1.');
}
}
```
下文中incorrect.ets为反例测试代码，依赖上文中absolute-path-1.ets：
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-no-unsafe-3des-V14
爬取时间: 2025-04-30 20:13:30
来源: Huawei Developer
该规则禁止使用不安全的3DES加密模式，例如3DES|ECB。建议使用安全的3DES加密模式，例如3DES|CBC。详情参考3DES加密模式。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-performance-V14
爬取时间: 2025-04-30 20:14:06
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-high-frequency-log-check-V14
爬取时间: 2025-04-30 20:14:43
来源: Huawei Developer
不建议在高频函数中使用Hilog。
高频函数包括：onTouch、onItemDragMove、onDragMove、onMouse、onVisibleAreaChange、onAreaChange、onScroll（已废弃）、onWillScroll。
高耗时函数处理场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// Test.ets
@Entry
@Component
struct Index {
build() {
Column() {
Scroll()
.onScroll(() => {
const TAG = 'onScroll';
})
}
}
}
```
反例
```typescript
// Test.ets
import hilog from '@ohos.hilog';
@Entry
@Component
struct Index {
build() {
Column() {
Scroll()
.onScroll(() => {
// Avoid printing logs
hilog.info(1001, 'Index', 'onScroll')
})
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkts-no-use-any-export-current-V14
爬取时间: 2025-04-30 20:15:23
来源: Huawei Developer
避免使用export * 导出当前module中定义的类型和数据。
冷启动完成时延场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
class User {
id?: number;
name?: string;
}
// 当前文件 User.ets
export * from './User';
// 当前文件 User.ets
export * as XX from './User';
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkts-no-use-any-export-other-V14
爬取时间: 2025-04-30 20:16:03
来源: Huawei Developer
避免使用export * 导出其他module中定义的类型和数据。
冷启动完成时延场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 当前文件 User.ets
// 从 Product.ets 文件中导出Product成员
export { Product } from './Product';
class User {
id?: number;
name?: string;
}
```
反例
```typescript
// 当前文件 User.ets
// 从 Product.ets 文件中导出所有可导出的成员
export * from './Product';
// 从 Product.ets 文件中导出所有可导出的成员
export * as XX from './Product';
class User {
id?: number;
name?: string;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-avoid-empty-callback-V14
爬取时间: 2025-04-30 20:16:39
来源: Huawei Developer
避免设置空的系统回调监听。
根据ArkUI编程规范，建议修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Component
struct MyComponent {
doSomething() {
//业务逻辑
}
build() {
Button('Click', { type: ButtonType.Normal, stateEffect: true })
.onClick(() => {
this.doSomething()
})
}
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-abouttoreuse-V14
爬取时间: 2025-04-30 20:17:14
来源: Huawei Developer
避免在aboutToReuse中对自动更新值的状态变量进行更新。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
// 此处为复用的自定义组件
@Reusable
@Component
struct ItemComponent {
@State desc: string = '';
@State sum: number = 0;
@State avg: number = 0;
aboutToReuse(params: Record<string, Object>): void {
this.desc = params.desc as string;
this.sum = params.sum as number;
this.avg = params.avg as number;
}
build() {
Column() {
Text('子组件' + this.desc)
.fontSize(30)
.fontWeight(30)
Text('结果' + this.sum)
.fontSize(30)
.fontWeight(30)
Text('平均值' + this.avg)
.fontSize(30)
.fontWeight(30)
}
}
}
@Entry
@Component
struct MyComponent {
private data: MyDataSource = new MyDataSource();
aboutToAppear(): void {
for (let index = 0; index < 20; index++) {
this.data.pushData(index.toString())
}
}
build() {
Column() {
List() {
LazyForEach(this.data, (item: string) => {
ListItem() {
ItemComponent({ desc: item, sum: 0, avg: 0 })
}
.width('100%')
.height(100)
}, (item: string) => item)
}
.width('100%')
.height('100%')
}
.width('100%')
.height('100%')
}
}
```
反例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
// 此处为复用的自定义组件
@Reusable
@Component
struct ItemComponent {
@State desc: string = '';
@State sum: number = 0;
@Link avg: number;
aboutToReuse(params: Record<string, Object>): void {
this.desc = params.desc as string;
this.sum = params.sum as number;
this.avg = params.avg as number;
}
build() {
Column() {
Text('子组件' + this.desc)
.fontSize(30)
.fontWeight(30)
Text('结果' + this.sum)
.fontSize(30)
.fontWeight(30)
Text('平均值' + this.avg)
.fontSize(30)
.fontWeight(30)
}
}
}
@Entry
@Component
struct MyComponent {
private data: MyDataSource = new MyDataSource();
aboutToAppear(): void {
for (let index = 0; index < 20; index++) {
this.data.pushData(index.toString())
}
}
build() {
Column() {
List() {
LazyForEach(this.data, (item: string) => {
ListItem() {
ItemComponent({ desc: item, sum: 0, avg: 0 })
}
.width('100%')
.height(100)
}, (item: string) => item)
}
.width('100%')
.height('100%')
}
.width('100%')
.height('100%')
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-combine-same-arg-animateto-V14
爬取时间: 2025-04-30 20:17:53
来源: Huawei Developer
建议动画参数相同时使用同一个animateTo。
动效丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
@Entry
@Component
struct MyComponent {
@State textWidth: number = 200;
@State color: Color = Color.Red;
func1() {
animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
this.textWidth = (this.textWidth === 100 ? 200 : 100);
});
}
func2() {
animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
});
}
build() {
Column() {
Row()
.width(this.textWidth)
.height(10)
.backgroundColor(this.color)
Text('click')
.onClick(() => {
this.func1();
this.func2();
})
}
.width('100%')
.height('100%')
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-image-async-load-V14
爬取时间: 2025-04-30 20:18:28
来源: Huawei Developer
建议大图片使用异步加载。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-limit-refresh-scope-V14
爬取时间: 2025-04-30 20:19:04
来源: Huawei Developer
建议减少组件刷新范围。该规则已于5.0.3.500版本下线。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Entry
@Component
struct StackExample6 {
@State isVisible : boolean = false;
build() {
Column() {
Stack({alignContent: Alignment.Top}) {
Text().width('100%').height('70%').backgroundColor(0xd2cab3)
.align(Alignment.Center).textAlign(TextAlign.Center);
// 此处省略100个相同的背景Text组件
Stack() {
if (this.isVisible) {
Text('New Page').height("100%").height("70%").backgroundColor(0xd2cab3)
.align(Alignment.Center).textAlign(TextAlign.Center);
}
}.width('100%').height('70%')
}
Button("press").onClick(() => {
this.isVisible = !(this.isVisible);
})
}
}
}
```
反例
```typescript
@Entry
@Component
struct StackExample5 {
@State isVisible : boolean = false;
build() {
Column() {
Stack({alignContent: Alignment.Top}) {
Text().width('100%').height('70%').backgroundColor(0xd2cab3)
.align(Alignment.Center).textAlign(TextAlign.Center);
// 此处省略100个相同的背景Text组件
if (this.isVisible) {
Text('New Page').height("100%").height("70%").backgroundColor(0xd2cab3)
.align(Alignment.Center).textAlign(TextAlign.Center);
}
}
Button("press").onClick(() => {
this.isVisible = !(this.isVisible);
})
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-load-on-demand-V14
爬取时间: 2025-04-30 20:19:40
来源: Huawei Developer
建议使用按需加载。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Reusable
@Component
struct ItemComponent {
@State introduce: string = ''
aboutToReuse(params: Record<string, ESObject>) {
this.introduce = params.introduce
}
build() {
Text(this.introduce)
.fontSize(14)
.padding({ left: 5, right: 5 })
.margin({ top: 5 })
}
}
@Entry
@Component
struct MyComponent {
private data: MyDataSource = new MyDataSource()
build() {
List() {
LazyForEach(this.data, (item: string) => {
ListItem() {
// 使用reuseId对不同的自定义组件实例分别标注复用组，以达到最佳的复用效果
ItemComponent({ introduce: item }).reuseId(item)
}
}, (item: string) => item)
}
.width('100%')
.height('100%')
}
}
```
反例
```typescript
@Entry
@Component
struct MyComponent {
@State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
build() {
List() {
// List中建议使用LazyForEach
ForEach(this.arr, (item: number) => {
ListItem() {
Text(`item value: ${item}`)
}
}, (item: number) => item.toString())
}
.width('100%')
.height('100%')
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-no-func-as-arg-for-reusable-component-V14
爬取时间: 2025-04-30 20:20:15
来源: Huawei Developer
避免使用函数作为复用的自定义组件创建时的入参。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Reusable
@Component
struct ChildComponent {
@State desc: string = '';
@State sum: number = 0;
aboutToReuse(params: Record<string, Object>): void {
this.desc = params.desc as string;
this.sum = params.sum as number;
}
build() {
Column() {
Text('子组件' + this.desc)
.fontSize(30)
.fontWeight(30)
Text('结果' + this.sum)
.fontSize(30)
.fontWeight(30)
}
}
}
@Entry
@Component
struct MyComponent{
private data: MyDataSource = new MyDataSource();
@State sum: number = 0;
aboutToAppear(): void {
for (let index = 0; index < 20; index++) {
this.data.pushData(index.toString())
}
// 执行该异步函数
this.count();
}
// 模拟耗时操作逻辑
async count() {
let temp: number = 0;
for (let index = 0; index < 10000; index++) {
temp += index;
}
// 将结果放入状态变量中
this.sum = temp;
}
build() {
Column() {
List() {
LazyForEach(this.data, (item: string) => {
ListItem() {
// 子组件的传参通过状态变量进行
ChildComponent({ desc: item, sum: this.sum })
}
.width('100%')
.height(100)
}, (item: string) => item)
}
.width('100%')
.height('100%')
}
}
}
```
反例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
// 此处为复用的自定义组件
@Reusable
@Component
struct ChildComponent {
@State desc: string = '';
@State sum: number = 0;
aboutToReuse(params: Record<string, Object>): void {
this.desc = params.desc as string;
this.sum = params.sum as number;
}
build() {
Column() {
Text('子组件' + this.desc)
.fontSize(30)
.fontWeight(30)
Text('结果' + this.sum)
.fontSize(30)
.fontWeight(30)
}
}
}
@Entry
@Component
struct MyComponent{
private data: MyDataSource = new MyDataSource();
aboutToAppear(): void {
for (let index = 0; index < 20; index++) {
this.data.pushData(index.toString())
}
}
// 真实场景的函数中可能存在未知的耗时操作逻辑，此处用循环函数模拟耗时操作
count(): number {
let temp: number = 0;
for (let index = 0; index < 10000; index++) {
temp += index;
}
return temp;
}
build() {
Column() {
List() {
LazyForEach(this.data, (item: string) => {
ListItem() {
// 此处sum参数是函数获取的，实际开发场景无法预料该函数可能出现的耗时操作，每次进行组件复用都会重复触发此函数的调用
ChildComponent({ desc: item, sum: this.count() })
}
.width('100%')
.height(100)
}, (item: string) => item)
}
.height('100%')
.width('100%')
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-no-high-freq-log-V14
爬取时间: 2025-04-30 20:20:52
来源: Huawei Developer
建议在正式发布的版本中，注释掉或删除日志打印代码。该规则已于5.0.3.403版本下线。
正例
```typescript
import hilog from '@ohos.hilog';
@Entry
@Component
struct MyComponent{
build() {
Column() {
Scroll()
.onScroll(() => {
//正例
//hilog.info(1001, 'Index', 'onScroll')
// do something
})
}
}
}
```
反例
```typescript
import hilog from '@ohos.hilog';
@Entry
@Component
struct MyComponent{
build() {
Column() {
Scroll()
.onScroll(() => {
// 高频操作中不建议写日志
hilog.info(1001, 'Index', 'onScroll')
// do something
})
}
}
}
```
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-no-state-var-access-in-loop-V14
爬取时间: 2025-04-30 20:21:29
来源: Huawei Developer
避免在for、while等循环逻辑中频繁读取状态变量。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
import hilog from '@ohos.hilog'
@Entry
@Component
struct MyComponent{
@State message: string = '';
build() {
Column() {
Button('点击打印日志')
.onClick(() => {
this.message = 'click';
let logMessage: string = this.message;
for (let i = 0; i < 10; i++) {
hilog.info(0x0000, 'TAG', '%{public}s', logMessage);
}
})
.width('90%')
.backgroundColor(Color.Blue)
.fontColor(Color.White)
.margin({
top: 10
})
}
.justifyContent(FlexAlign.Start)
.alignItems(HorizontalAlign.Center)
.margin({
top: 15
})
}
}
```
反例
```typescript
import hilog from '@ohos.hilog'
@Entry
@Component
struct MyComponent{
@State message: string = '';
build() {
Column() {
Button('点击打印日志')
.onClick(() => {
this.message = 'click';
for (let i = 0; i < 10; i++) {
hilog.info(0x0000, 'TAG', '%{public}s', this.message);
}
})
.width('90%')
.backgroundColor(Color.Blue)
.fontColor(Color.White)
.margin({
top: 10
})
}
.justifyContent(FlexAlign.Start)
.alignItems(HorizontalAlign.Center)
.margin({
top: 15
})
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-no-stringify-lazyforeach-key-V14
爬取时间: 2025-04-30 20:22:05
来源: Huawei Developer
在使用LazyForEach进行组件复用的key生成器函数里，不要使用stringify。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-reduce-ges-distance-V14
爬取时间: 2025-04-30 20:22:41
来源: Huawei Developer
建议设置合理的拖动距离。
应用内点击响应时延场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-remove-container-without-property-V14
爬取时间: 2025-04-30 20:23:17
来源: Huawei Developer
建议尽量减少视图嵌套层次。该规则曾用名：@performance/hp-arkui-reduce-view-nest-level 。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Entry
@Component
struct MyComponent{
@State number: Number[] = Array.from(Array<number>(1000), (val, i) => i);
scroller: Scroller = new Scroller()
build() {
Column() {
Grid(this.scroller) {
ForEach(this.number, (item: number) => {
GridItem() {
Text(item.toString())
.fontSize(16)
.backgroundColor(0xF9CF93)
.width('100%')
.height(80)
.textAlign(TextAlign.Center)
.border({width:1})
}
}, (item:string) => item)
}
.columnsTemplate('1fr 1fr 1fr 1fr 1fr')
.columnsGap(0)
.rowsGap(0)
.size({ width: "100%", height: "100%" })
}
}
}
```
反例
```typescript
@Entry
@Component
struct MyComponent{
@State number: Number[] = Array.from(Array<number>(1000), (val, i) => i);
scroller: Scroller = new Scroller()
build() {
Column() {
Grid(this.scroller) {
ForEach(this.number, (item: number) => {
GridItem() {
Flex() {
Flex() {
Flex() {
Text(item.toString())
.fontSize(16)
.backgroundColor(0xF9CF93)
.width('100%')
.height(80)
.textAlign(TextAlign.Center)
.border({width:1})
}
}
}
}
}, (item:string) => item)
}
.columnsTemplate('1fr 1fr 1fr 1fr 1fr')
.columnsGap(0)
.rowsGap(0)
.size({ width: "100%", height: "100%" })
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-no-redundant-nest-V14
爬取时间: 2025-04-30 20:23:53
来源: Huawei Developer
避免冗余的嵌套。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Entry
@Component
struct MyComponent {
@State children: Number[] = Array.from(Array<number>(900), (v, k) => k);
build() {
Scroll() {
Grid() {
ForEach(this.children, (item: Number[]) => {
GridItem() {
Text(item.toString())
}.backgroundColor(Color.Yellow)
}, (item: string) => item)
}
.columnsTemplate('1fr 1fr 1fr 1fr')
.columnsGap(0)
.rowsGap(0)
.size({ width: "100%", height: "100%" })
}
}
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-remove-redundant-state-var-V14
爬取时间: 2025-04-30 20:24:30
来源: Huawei Developer
建议移除不关联UI组件的状态变量设置。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Entry
@Component
struct MyComponent {
@State message: string = "";
appendMsg(newMsg: String) : string {
this.message += newMsg;
return this.message;
}
build() {
Column() {
Stack() {
Text(this.message)
}
.backgroundColor("black")
.width(200)
.height(400)
Button("move")
}
}
}
```
反例
```typescript
@Entry
@Component
struct MyComponent {
@State message: string = "";
appendMsg(newMsg: String) : string {
this.message += newMsg;
return this.message;
}
build() {
Column() {
Stack() {
}
.backgroundColor("black")
.width(200)
.height(400)
Button("move")
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-remove-unchanged-state-var-V14
爬取时间: 2025-04-30 20:25:04
来源: Huawei Developer
建议移除未改变的状态变量设置。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
class Translate {
translateX: number = 20;
}
@Component
struct Title {
build() {
Row() {
// 本地资源 icon.png
Image($r('app.media.icon'))
.width(50)
.height(50)
Text("Title")
.fontSize(20)
}
}
}
@Entry
@Component
struct MyComponent{
@State translateObj: Translate = new Translate();
// 直接使用一般变量即可
button_msg: string = "i am button";
build() {
Column() {
Title()
Stack() {
}
.backgroundColor("black")
.width(200)
.height(400)
Button(this.button_msg)
.onClick(() => {
animateTo({
duration: 50
}, () => {
this.translateObj.translateX = (this.translateObj.translateX + 50) % 150
})
})
}
.translate({
x: this.translateObj.translateX
})
}
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui--replace-reusable-by-builder-V14
爬取时间: 2025-04-30 20:25:39
来源: Huawei Developer
建议使用@Builder替代嵌套的自定义组件。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Entry
@Component
struct MyComponent{
private data: MyDataSource = new MyDataSource();
aboutToAppear(): void {
for (let index = 0; index < 30; index++) {
this.data.pushData(index.toString())
}
}
build() {
Column() {
List() {
LazyForEach(this.data, (item: string) => {
ListItem() {
//  正例
ChildComponent({ desc: item })
}
}, (item: string) => item)
}
.height('100%')
.width('100%')
}
.width('100%')
}
}
// 正例 使用组件复用
@Reusable
@Component
struct ChildComponent {
@State desc: string = '';
aboutToReuse(params: Record<string, Object>): void {
this.desc = params.desc as string;
}
build() {
Column() {
// 使用@Builder，可以减少自定义组件创建和渲染的耗时
ChildComponentBuilder({ paramA: this.desc })
}
.width('100%')
}
}
class Temp {
paramA: string = '';
}
@Builder
function ChildComponentBuilder($$: Temp) {
Column() {
// 此处使用`${}`来进行按引用传递，让@Builder感知到数据变化，进行UI刷新
Text(`子组件 + ${$$.paramA}`)
.fontSize(30)
.fontWeight(30)
}
.width('100%')
}
```
反例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Entry
@Component
struct MyComponent{
private data: MyDataSource = new MyDataSource();
aboutToAppear(): void {
for (let index = 0; index < 30; index++) {
this.data.pushData(index.toString())
}
}
build() {
Column() {
List() {
LazyForEach(this.data, (item: string) => {
ListItem() {
//反例 使用自定义组件
ComponentA({ desc: item })
}
}, (item: string) => item)
}
.height('100%')
.width('100%')
}
}
}
@Reusable
@Component
struct ComponentA {
@State desc: string = '';
aboutToReuse(params: ESObject): void {
this.desc = params.desc as string;
}
build() {
// 在复用组件中嵌套使用自定义组件
ComponentB({ desc: this.desc })
}
}
@Component
struct ComponentB {
@State desc: string = '';
// 嵌套的组件中也需要实现aboutToReuse来进行UI的刷新
aboutToReuse(params: ESObject): void {
this.desc = params.desc as string;
}
build() {
Column() {
Text('子组件' + this.desc)
.fontSize(30)
.fontWeight(30)
}
.width('100%')
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-set-cache-count-for-lazyforeach-grid-V14
爬取时间: 2025-04-30 20:26:13
来源: Huawei Developer
建议在Grid下使用LazyForEach时设置合理的cacheCount。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Entry
@Component
struct MyComponent {
// 数据源
private data: MyDataSource = new MyDataSource();
aboutToAppear() {
for (let i = 1; i < 1000; i++) {
this.data.pushData(i);
}
}
build() {
Column({ space: 5 }) {
Grid() {
LazyForEach(this.data, (item: number) => {
GridItem() {
// 使用可复用自定义组件
// 业务逻辑
}
}, (item: string) => item)
}
// 设置GridItem的缓存数量
.cachedCount(2)
.columnsTemplate('1fr 1fr 1fr')
.columnsGap(10)
.rowsGap(10)
.margin(10)
.height(500)
.backgroundColor(0xFAEEE0)
}
}
}
```
反例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Entry
@Component
struct MyComponent {
// 数据源
private data: MyDataSource = new MyDataSource();
aboutToAppear() {
for (let i = 1; i < 1000; i++) {
this.data.pushData(i);
}
}
build() {
Column({ space: 5 }) {
Grid() {
LazyForEach(this.data, (item: number) => {
GridItem() {
// 使用可复用自定义组件
// 业务逻辑
}
}, (item: string) => item)
}
// 未设置GridItem的缓存数量
.columnsTemplate('1fr 1fr 1fr')
.columnsGap(10)
.rowsGap(10)
.margin(10)
.height(500)
.backgroundColor(0xFAEEE0)
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-suggest-cache-avplayer-V14
爬取时间: 2025-04-30 20:26:48
来源: Huawei Developer
建议缓存AVPlayer实例減少起播时延。
音视频起播速度慢的场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
import media from '@ohos.multimedia.media';
@Entry
@Component
struct MyComponent{
private avPlayer: media.AVPlayer | undefined = undefined;
aboutToAppear(): void {
// 页面创建时初始化AVPlayer实例
media.createAVPlayer().then((ret) => {
this.avPlayer = ret;
});
}
aboutToDisappear(): void {
// 离开页面时销毁AVPlayer实例
if (this.avPlayer) {
this.avPlayer.release();
}
this.avPlayer = undefined;
}
build() {
// 组件布局
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-reuseid-if-else-component-V14
爬取时间: 2025-04-30 20:27:25
来源: Huawei Developer
建议使用reuseId标记不同结构的组件构成。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-suggest-use-effectkit-blur-V14
爬取时间: 2025-04-30 20:28:00
来源: Huawei Developer
建议使用effectKit.createEffect实现模糊效果。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 导入图片处理模块
import image from "@ohos.multimedia.image";
// 导入图像效果模块
import effectKit from '@ohos.effectKit';
@Entry
@Component
struct MyComponent{
// 是否显示全屏模态页面。静态模糊用
@State isShowStaticBlur: boolean = false;
// PixelMap实例
@State pixelMap: image.PixelMap | undefined = undefined;
// ImageSource实例
imgSource: image.ImageSource | undefined = undefined;
// 静态模糊
async staticBlur() {
// 获得当前Ability的Context
let context = getContext(this);
// 获取resourceManager对象
let resourceMgr = context.resourceManager;
// 获rawfile目录下的图片
const fileData = await resourceMgr.getRawFileContent('startIcon.png');
// 创建ArrayBuffer实例
let buffer: ArrayBuffer = fileData.buffer.slice(0);
// 创建图片源实例
this.imgSource = image.createImageSource(buffer);
// 创建像素的属性
let opts: image.InitializationOptions = {
// 是否可编辑
editable: true,
// 像素格式。3表示RGBA_8888
pixelFormat: 3,
// 创建图片大小
size: {
height: 4,
width: 6
}
};
// 创建PixelMap
await this.imgSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
// 模糊半径
const blurRadius = 1;
// 创建Filter实例
let headFilter = effectKit.createEffect(pixelMap);
if (headFilter != null) {
// 设置静态模糊。将模糊效果添加到效果链表中
headFilter.blur(blurRadius);
// 获取已添加链表效果的源图像的image.PixelMap
headFilter.getEffectPixelMap().then((pixelMap: image.PixelMap) => {
this.pixelMap = pixelMap;
});
}
})
}
// 图片设置静态模糊的模态页面
@Builder
staticBlurBuilder() {
Stack() {
Image(this.pixelMap)
.width('100%')
.height('100%')
.objectFit(ImageFit.Fill)
Button('close')
.fontSize(20)
.onClick(() => {
this.isShowStaticBlur = false;
})
}
.width('100%')
.height('100%')
}
build() {
Column({ space: 10 }) {
Button('静态模糊')
.onClick(() => {
this.isShowStaticBlur = true;
// 设置静态模糊
this.staticBlur();
})
.bindContentCover(this.isShowStaticBlur, this.staticBlurBuilder(), {
// 全屏模态转场类型。上下切换动画
modalTransition: ModalTransition.DEFAULT
})
}
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-sg-anonymousid-async-V14
爬取时间: 2025-04-30 20:28:38
来源: Huawei Developer
建议在主线程中通过异步获取IFAA免密认证的匿名化ID。
高耗时函数处理场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-attribute-update-refresh-scope-V14
爬取时间: 2025-04-30 20:29:11
来源: Huawei Developer
建议使用attributeUpdater精准控制组件属性的刷新。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-grid-layout-options-V14
爬取时间: 2025-04-30 20:29:45
来源: Huawei Developer
建议在指定位置时使用GridLayoutOptions提升Grid性能。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Reusable
@Component
struct TextItem {
@State item: string = "";
build() {
Text(this.item)
.fontSize(16)
.backgroundColor(0xF9CF93)
.width('100%')
.height(80)
.textAlign(TextAlign.Center)
.onClick(() => {
this.item = 'click';
})
}
}
@Entry
@Component
export struct MyComponent{
private datasource: MyDataSource = new MyDataSource();
scroller: Scroller = new Scroller();
private irregularData: number[] = [];
layoutOptions: GridLayoutOptions = {
regularSize: [1, 1],
irregularIndexes: this.irregularData,
};
aboutToAppear() {
for (let i = 1; i <= 2000; i++) {
this.datasource.pushData(i + '');
if ((i - 1) % 4 === 0) {
this.irregularData.push(i - 1);
}
}
}
build() {
Column({ space: 5 }) {
Text('Set GridItem size using GridLayoutOptions').fontColor(0xCCCCCC).fontSize(9).width('90%')
Grid(this.scroller, this.layoutOptions) {
LazyForEach(this.datasource, (item: string, index: number) => {
GridItem() {
TextItem({ item: item })
}
}, (item: string) => item)
}
.cachedCount(1)
.columnsTemplate('1fr 1fr 1fr')
.columnsGap(10)
.rowsGap(10)
.width('90%')
.height('40%')
Button("scrollToIndex:1900").onClick(() => {
this.scroller.scrollToIndex(1900);
})
}.width('100%')
.margin({ top: 5 })
}
}
```
反例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Reusable
@Component
struct TextItem {
@State item: string = "";
build() {
Text(this.item)
.fontSize(16)
.backgroundColor(0xF9CF93)
.width('100%')
.height(80)
.textAlign(TextAlign.Center)
.onClick(() => {
this.item = 'click';
})
}
}
@Entry
@Component
struct MyComponent{
private datasource: MyDataSource = new MyDataSource();
scroller: Scroller = new Scroller();
aboutToAppear() {
for (let i = 1; i <= 2000; i++) {
this.datasource.pushData(i + '');
}
}
build() {
Column({ space: 5 }) {
Text('Use columnStart and columnEnd to set the GridItem size').fontColor(0xCCCCCC).fontSize(9).width('90%')
Grid(this.scroller) {
LazyForEach(this.datasource, (item: string, index: number) => {
if ((index % 4) === 0) {
GridItem() {
TextItem({ item: item })
}
.columnStart(0).columnEnd(2)
} else {
GridItem() {
TextItem({ item: item })
}
}
}, (item: string) => item)
}
.cachedCount(1)
.columnsTemplate('1fr 1fr 1fr')
.columnsGap(10)
.rowsGap(10)
.width('90%')
.height('40%')
Button("scrollToIndex:1900").onClick(() => {
this.scroller.scrollToIndex(1900);
})
}.width('100%')
.margin({ top: 5 })
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-id-in-get-resource-sync-api-V14
爬取时间: 2025-04-30 20:30:19
来源: Huawei Developer
建议在使用API getColorSync和getStringSync时建议使用带id版本。
高耗时函数处理场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-local-var-to-replace-state-var-V14
爬取时间: 2025-04-30 20:30:54
来源: Huawei Developer
建议使用临时变量替换状态变量。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Entry
@Component
struct MyComponent {
@State message: string = '';
appendMsg(newMsg: String) {
let message = this.message;
message += newMsg;
message += ";";
message += "<br/>";
this.message = message;
}
build() {
// 业务代码...
}
}
```
反例
```typescript
@Entry
@Component
struct MyComponent {
@State message: string = '';
appendMsg(newMsg: String) {
this.message += newMsg;
this.message += ";";
this.message += "<br/>";
}
build() {
// 业务代码...
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-object-link-to-replace-prop-V14
爬取时间: 2025-04-30 20:31:29
来源: Huawei Developer
建议使用@ObjectLink代替@Prop减少不必要的深拷贝。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Observed
class ClassA {
public c: number = 0;
constructor(c: number) {
this.c = c;
}
}
@Component
struct PropChild {
// @ObjectLink 装饰状态变量不会深拷贝
// 当修饰为ObjectLink时 ClassA必须同时被Observed修饰
@ObjectLink testNum: ClassA;
build() {
Text(`PropChild testNum ${this.testNum.c}`)
}
}
@Entry
@Component
struct Parent {
@State testNum: ClassA[] = [new ClassA(1)];
build() {
Column() {
Text(`Parent testNum ${this.testNum[0].c}`)
.onClick(() => {
this.testNum[0].c += 1;
})
// 当子组件不需要发生本地改变时，优先使用@ObjectLink，因为@Prop是会深拷贝数据，具有拷贝的性能开销，所以这个时候@ObjectLink是比@Link和@Prop更优的选择
PropChild({ testNum: this.testNum[0] })
}
}}
```
反例
```typescript
@Observed
class ClassA {
public c: number = 0;
constructor(c: number) {
this.c = c;
}
}
@Component
struct PropChild {
// @Prop 装饰状态变量会深拷贝
@Prop testNum: ClassA;
build() {
Text(`PropChild testNum ${this.testNum.c}`)
}
}
@Entry
@Component
struct Parent {
@State testNum: ClassA[] = [new ClassA(1)];
build() {
Column() {
Text(`Parent testNum ${this.testNum[0].c}`)
.onClick(() => {
this.testNum[0].c += 1;
})
// PropChild没有改变@Prop testNum: ClassA的值，所以这时最优的选择是使用@ObjectLink
PropChild({ testNum: this.testNum[0] })
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-onanimationstart-in-swiper-V14
爬取时间: 2025-04-30 20:32:02
来源: Huawei Developer
建议Swiper预加载机制搭配 OnAnimationStart 接口回调使用。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
import image from '@ohos.multimedia.image';
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { PhotoItem } from './component/ChildComponent';
import { MyObject } from './data/DataEntry';
@Entry
@Component
struct MyComponent{
cacheCount: number = 1
swiperController: SwiperController = new SwiperController();
private data: MyDataSource = new MyDataSource([]);
context = getContext(this);
build() {
Swiper(this.swiperController) {
LazyForEach(this.data, (item: MyObject, index?: number) => {
// 源码文件，请以工程实际为准
PhotoItem({ myIndex: index, dataSource: this.data })
}, (item: MyObject) => item.id) // item唯一id
}
.cachedCount(this.cacheCount)
.indicator(true)
.loop(false)
// 在OnAnimationStart接口回调中进行预加载资源的操作
.onAnimationStart((index: number, targetIndex: number) => {
if (targetIndex !== index) {
try {
// 获取resourceManager资源管理器
const resourceMgr = this.context.resourceManager;
// 获取rawfile文件夹下icon.png的ArrayBuffer
let str = "item" + (targetIndex + this.cacheCount + 2) + ".jpg";
resourceMgr.getRawFileContent(str).then((value) => {
// 创建imageSource
const imageSource = image.createImageSource(value.buffer);
imageSource.createPixelMap().then((value) => {
this.data.addData(targetIndex + this.cacheCount + 1, {
description: "" + (targetIndex + this.cacheCount + 1),
image: value
})
})
})
} catch (err) {
console.log("error code" + err);
}
}
})
.width('100%')
.height('100%')
}
}
```
反例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { PhotoItem } from './component/ChildComponent';
import { MyObject } from './data/DataEntry';
@Entry
@Component
struct MyComponent{
cacheCount: number = 1
swiperController: SwiperController = new SwiperController();
private data: MyDataSource = new MyDataSource([]);
context = getContext(this);
build() {
// Swiper组件没有使用OnAnimationStart进行预加载
Swiper(this.swiperController) {
LazyForEach(this.data, (item: MyObject, index?: number) => {
// 源码文件，请以工程实际为准
PhotoItem({ myIndex: index, dataSource: this.data })
}, (item: MyObject) => item.id)
}
.cachedCount(this.cacheCount)
.indicator(true)
.loop(false)
.width('100%')
.height('100%')
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-reusable-component-V14
爬取时间: 2025-04-30 20:32:35
来源: Huawei Developer
建议复杂组件的定义，尽量使用组件复用。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { GoodItems } from './data/DataEntry';
@Entry
@Component
struct MyComponent{
private data: MyDataSource = new MyDataSource([]);
build() {
Column() {
LazyForEach(this.data, (item: GoodItems) => {
GridItem() {
Column() {
Text(item.introduce)
.fontSize(14)
.padding({ left: 5, right: 5 })
.margin({ top: 5 })
Row() {
Text('￥')
.fontSize(10)
.fontColor(Color.Red)
.baselineOffset(-4)
Text(item.price)
.fontSize(16)
.fontColor(Color.Red)
Text(item.numb)
.fontSize(10)
.fontColor(Color.Gray)
.baselineOffset(-4)
.margin({ left: 5 })
}
.width('100%')
.justifyContent(FlexAlign.SpaceBetween)
.padding({ left: 5, right: 5 })
.margin({ top: 15 })
}
.borderRadius(10)
.backgroundColor(Color.White)
.clip(true)
.width('100%')
.height(290)
}
}, (item: GoodItems) => item.index)
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-row-column-to-replace-flex-V14
爬取时间: 2025-04-30 20:33:09
来源: Huawei Developer
建议使用Column/Row替代Flex。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-scale-to-replace-attr-animateto-V14
爬取时间: 2025-04-30 20:33:42
来源: Huawei Developer
建议组件布局改动时使用图形变换属性动画。
动效丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
@Entry
@Component
struct MyComponent {
@State textWidth: number = 10;
@State textHeight: number = 10;
build() {
Column() {
Text()
.backgroundColor(Color.Blue)
.fontColor(Color.White)
.fontSize(20)
.width(this.textWidth)
.height(this.textHeight)
Button('布局属性')
.backgroundColor(Color.Blue)
.fontColor(Color.White)
.fontSize(20)
.margin({ top: 30 })
.borderRadius(30)
.padding(10)
.onClick(() => {
animateTo({ duration: 1000 }, () => {
this.textWidth = 100;
this.textHeight = 100;
})
})
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-use-taskpool-for-web-request-V14
爬取时间: 2025-04-30 20:34:17
来源: Huawei Developer
建议网络资源的请求和返回使用taskpool线程池异步处理。
应用内点击完成时延场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-transition-to-replace-animateto-V14
爬取时间: 2025-04-30 20:34:51
来源: Huawei Developer
建议组件转场动画使用transition。
动效丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Entry
@Component
struct MyComponent {
@State show: boolean = true;
build() {
Column() {
Row() {
if (this.show) {
Text('value')
// Set id to make transition interruptible
.id('myText')
.transition(TransitionEffect.OPACITY.animation({ duration: 1000 }))
}
}.width('100%')
.height(100)
.justifyContent(FlexAlign.Center)
Text('toggle state')
.onClick(() => {
// Through transition, animates the appearance or disappearance of transparency.
this.show = !this.show;
})
}
}
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-arkui-use-word-break-in-space-V14
爬取时间: 2025-04-30 20:35:26
来源: Huawei Developer
建议使用word-break替换零宽空格(\u200b)。
根据ArkUI编程规范，建议修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
@Component
export struct MyComponent {
private diskName: string = '';
build() {
Text(this.diskName.split("").join("\u200B"))
.textAlign(TextAlign.Start)
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hp-arkui-wrap-waterflow-if-else-footer-V14
爬取时间: 2025-04-30 20:36:00
来源: Huawei Developer
建议使用容器包裹waterflow中footer的if-else逻辑。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Entry
@Component
struct MyComponent{
private datasource: MyDataSource = new MyDataSource();
private showFooterStatus = 2;
aboutToAppear() {
for (let i = 0; i <= 20; i++) {
this.datasource.pushData(i)
}
}
build() {
Column({ space: 2 }) {
WaterFlow({ footer: (): void => this.itemFoot() }) {
LazyForEach(this.datasource, (item: number) => {
FlowItem() {
ReusableFlowItem({ item: item })
}.onAppear(() => {
if (item + 20 == this.datasource.totalCount()) {
for (let i = 0; i < 100; i++) {
this.datasource.AddLastItem()
}
}
})
.width('100%')
}, (item: string) => item)
}
.columnsTemplate('1fr 1fr 1fr 1fr')
.columnsGap(10)
.rowsGap(5)
.width('100%')
.height('50%')
}
}
@Builder
itemFoot() {
//  外层加了一个column容器控制
Column() {
if (this.showFooterStatus == 1) {
// Code to show try again
} else if (this.showFooterStatus == 2) {
// Code to show end
} else {
// Code to show footer loading
}
}
}
}
@Component
@Reusable
struct ReusableFlowItem {
@State item: number = 0
aboutToReuse(params: Record<string, ESObject>) {
this.item = params.item;
}
build() {
Column() {
Text('N' + this.item)
.fontSize(12)
.height('16')
Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
.objectFit(ImageFit.Fill)
.width('100%')
.layoutWeight(1)
}
}
}
```
反例
```typescript
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
@Entry
@Component
struct MyComponent{
private datasource: MyDataSource = new MyDataSource();
private showFooterStatus = 2;
aboutToAppear() {
for (let i = 0; i <= 20; i++) {
this.datasource.pushData(i)
}
}
build() {
Column({ space: 2 }) {
WaterFlow({ footer: (): void => this.itemFoot() }) {
LazyForEach(this.datasource, (item: number) => {
FlowItem() {
ReusableFlowItem({ item: item })
}.onAppear(() => {
if (item + 20 == this.datasource.totalCount()) {
for (let i = 0; i < 100; i++) {
this.datasource.AddLastItem()
}
}
})
.width('100%')
}, (item: string) => item)
}
.columnsTemplate('1fr 1fr 1fr 1fr')
.columnsGap(10)
.rowsGap(5)
.width('100%')
.height('50%')
}
}
@Builder
itemFoot() {
//  这个作为footer的build的逻辑里有if逻辑，应该在外层加一个容器控制
if (this.showFooterStatus == 1) {
// Code to show try again
} else if (this.showFooterStatus == 2) {
// Code to show end
} else {
// Code to show footer loading
}
}
}
@Component
@Reusable
struct ReusableFlowItem {
@State item: number = 0
aboutToReuse(params: Record<string, ESObject>) {
this.item = params.item;
}
build() {
Column() {
Text('N' + this.item)
.fontSize(12)
.height('16')
Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
.objectFit(ImageFit.Fill)
.width('100%')
.layoutWeight(1)
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-performance-no-closures-V14
爬取时间: 2025-04-30 20:36:35
来源: Huawei Developer
建议函数内部变量尽量使用参数传递。
根据ArkTS编程规范，建议修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_hp-performance-no-dynamic-cls-func-V14
爬取时间: 2025-04-30 20:37:09
来源: Huawei Developer
避免动态声明function与class，仅适用于js/ts。
根据ArkTS编程规范，建议修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-lazyforeach-args-check-V14
爬取时间: 2025-04-30 20:37:44
来源: Huawei Developer
建议在LazyForEach参数中设置keyGenerator。该规则已于5.0.3.500版本下线。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-init-list-component-V14
爬取时间: 2025-04-30 20:38:17
来源: Huawei Developer
List组件在使用时，建议同时定义width和height属性。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-lottie-animation-destroy-check-V14
爬取时间: 2025-04-30 20:38:51
来源: Huawei Developer
该规则检测使用lottie加载的动画是否都正确销毁。
当使用lottie加载动画时，一般需要先通过lottie.loadAnimation将动画加载到内存，动画执行完毕后需要在合适的时机（例如：onDisAppear，onPageHide，aboutToDisappear）通过调用animationItem的destroy方法将单个动画销毁或者调用lottie.destroy()方法将当前页面所有动画销毁，如果动画未被销毁就会造成资源浪费，影响应用性能体验。
内存优化场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例1
正例2
反例1
反例2
反例3
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-high-loaded-frame-rate-range-V14
爬取时间: 2025-04-30 20:39:25
来源: Huawei Developer
不允许锁定最高帧率运行。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-number-init-check-V14
爬取时间: 2025-04-30 20:39:59
来源: Huawei Developer
该规则将检查number是否正确使用。
根据ArkTS高性能编程实践，建议修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-object-creation-check-V14
爬取时间: 2025-04-30 20:40:35
来源: Huawei Developer
建议使用字面量进行对象创建。仅支持检查ts文件，暂不支持ets文件检查。该规则已于5.0.3.500版本下线。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
// Test.ts
// 创建一个array
let arr: number[] = [];
// 创建一个普通对象
let obj = {};
// 创建一个正则对象
let reg = /../;
```
反例
```typescript
// Test.ts
// 创建一个array
let arr: number[] = new Array();
// 创建一个普通对象
let obj = new Object();
// 创建一个正则对象
let reg = new RegExp('/../');
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-sparse-array-check-V14
爬取时间: 2025-04-30 20:41:09
来源: Huawei Developer
建议避免使用稀疏数组。
根据ArkTS高性能编程实践，建议修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-start-window-icon-check-V14
爬取时间: 2025-04-30 20:41:44
来源: Huawei Developer
启动页图标分辨率建议不超过256 * 256。
冷启动响应时延场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
1、entry/src/main/module.json5中的mainElement对应的ability中配置了startWindowIcon
2、entry/src/main/resources/base/media目录下对应的图片文件分辨率小于等于256*256
反例
1、entry/src/main/module.json5中的mainElement对应的ability中配置了startWindowIcon
2、entry/src/main/resources/base/media目录下对应的图片文件分辨率大于256*256
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-timezone-interface-check-V14
爬取时间: 2025-04-30 20:42:18
来源: Huawei Developer
在获取非本地时间时，建议使用统一标准的i18n.Calendar接口获取时间时区相关信息。
规则配置
选项
该规则无需配置额外选项。
正例1
正例2
反例1
反例2
反例3
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-typed-array-check-V14
爬取时间: 2025-04-30 20:42:52
来源: Huawei Developer
数值数组推荐使用TypedArray。
根据ArkTS高性能编程实践，建议修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
const typedArray1: number[] = new Array(1, 2, 3);
const typedArray2: number[] = new Array(4, 5, 6);
let res: number[] = new Array(3);
for (let i = 0; i < 3; i++) {
res[i] = typedArray1[i] + typedArray2[i];
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-waterflow-data-preload-check-V14
爬取时间: 2025-04-30 20:43:26
来源: Huawei Developer
建议对waterflow子组件进行数据预加载。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
下文中WaterFlowDataSource.ets为依赖代码：
下文中Index.ets为正例测试代码，依赖上文中WaterFlowDataSource.ets：
```typescript
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource'
@Entry
@Component
struct WaterFlowDemo {
@State minSize: number = 80
@State maxSize: number = 180
@State fontSize: number = 24
@State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]
scroller: Scroller = new Scroller()
dataSource: WaterFlowDataSource = new WaterFlowDataSource()
private itemWidthArray: number[] = []
private itemHeightArray: number[] = []
// 计算FlowItem宽/高
getSize() {
let ret = Math.floor(Math.random() * this.maxSize)
return (ret > this.minSize ? ret : this.minSize)
}
// 设置FlowItem的宽/高数组
setItemSizeArray() {
for (let i = 0; i < 100; i++) {
this.itemWidthArray.push(this.getSize())
this.itemHeightArray.push(this.getSize())
}
}
aboutToAppear() {
this.setItemSizeArray()
}
@Builder
itemFoot() {
Text(`Footer`)
.fontSize(10)
.width(50)
.height(50)
.align(Alignment.Center)
.margin({ top: 2 })
}
build() {
Column({ space: 2 }) {
WaterFlow() {
LazyForEach(this.dataSource, (item: number) => {
FlowItem() {
ReusableFlowItem({ item: item })
}
.onAppear(() => {
// 即将触底时提前增加数据，即执行数据预加载
if (item + 20 == this.dataSource.totalCount()) {
for (let i = 0; i < 100; i++) {
this.dataSource.addLastItem()
}
}
})
.width('100%')
.height(this.itemHeightArray[item % 100])
.backgroundColor(this.colors[item % 5])
}, (item: string) => item)
}
.columnsTemplate('1fr 1fr')
.columnsGap(10)
.rowsGap(5)
.width('100%')
.height('100%')
}
}
}
@Reusable
@Component
struct ReusableFlowItem {
@State item: number = 0
// 从复用缓存中加入到组件树之前调用，可在此处更新组件的状态变量以展示正确的内容
aboutToReuse(params: Record<string, ESObject>) {
this.item = params.item;
}
build() {
Column() {
Text('N' + this.item).fontSize(12).height('16')
Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
.objectFit(ImageFit.Fill)
.width('100%')
.layoutWeight(1)
}
}
}
```
反例
下文中WaterFlowDataSource.ets为依赖代码：
下文中Index.ets为反例测试代码，依赖上文中WaterFlowDataSource.ets：
```typescript
// Index.ets
import { WaterFlowDataSource } from './WaterFlowDataSource'
@Entry
@Component
struct WaterFlowDemo {
@State minSize: number = 80
@State maxSize: number = 180
@State fontSize: number = 24
@State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]
scroller: Scroller = new Scroller()
dataSource: WaterFlowDataSource = new WaterFlowDataSource()
private itemWidthArray: number[] = []
private itemHeightArray: number[] = []
// 计算FlowItem宽/高
getSize() {
let ret = Math.floor(Math.random() * this.maxSize)
return (ret > this.minSize ? ret : this.minSize)
}
// 设置FlowItem的宽/高数组
setItemSizeArray() {
for (let i = 0; i < 100; i++) {
this.itemWidthArray.push(this.getSize())
this.itemHeightArray.push(this.getSize())
}
}
aboutToAppear() {
this.setItemSizeArray()
}
@Builder
itemFoot() {
Text(`Footer`)
.fontSize(10)
.backgroundColor(Color.Red)
.width(50)
.height(50)
.align(Alignment.Center)
.margin({ top: 2 })
}
build() {
Column({ space: 2 }) {
WaterFlow() {
LazyForEach(this.dataSource, (item: number) => {
FlowItem() {
ReusableFlowItem({ item: item })
}
.width('100%')
.height(this.itemHeightArray[item % 100])
.backgroundColor(this.colors[item % 5])
}, (item: string) => item)
}
.onReachEnd(() => {
console.info("onReachEnd")
setTimeout(() => {
for (let i = 0; i < 100; i++) {
this.datasource.AddLastItem()
}
}, 1000)
})
.columnsTemplate("1fr 1fr")
.columnsGap(10)
.rowsGap(5)
.backgroundColor(0xFAEEE0)
.width('100%')
.height('100%')
}
}
}
@Reusable
@Component
struct ReusableFlowItem {
@State item: number = 0
// 从复用缓存中加入到组件树之前调用，可在此处更新组件的状态变量以展示正确的内容
aboutToReuse(params: Record<string, ESObject>) {
this.item = params.item;
}
build() {
Column() {
Text("N" + this.item).fontSize(12).height('16')
Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
.objectFit(ImageFit.Fill)
.width('100%')
.layoutWeight(1)
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-multi-associations-state-var-check-V14
爬取时间: 2025-04-30 20:44:00
来源: Huawei Developer
多个组件关联同一数据时，建议在组件中使用@Watch装饰器添加更新条件，避免不必要的组件更新。
通用丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-constant-property-check-in-loops-V14
爬取时间: 2025-04-30 20:44:36
来源: Huawei Developer
在循环如需频繁访问某个常量，且该属性引用常量在循环中不会改变，建议提取到循环外部，减少属性访问的次数。
根据ArkTS高性能编程实践，建议修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-foreach-args-check-V14
爬取时间: 2025-04-30 20:45:11
来源: Huawei Developer
建议在ForEach参数中设置keyGenerator。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Entry
@Component
struct ForeachTest {
private data: string[] = ['1', '2', '3'];
build() {
RelativeContainer() {
List() {
ForEach(this.data, (item: string, index: number) => {
ListItem() {
Text(item);
}
}, (item: string, index: number) => item)
}
.width('100%')
.height('100%')
}
.height('100%')
.width('100%')
}
}
```
反例
```typescript
@Entry
@Component
struct ForeachTest {
private data: string[] = ['1', '2', '3'];
build() {
RelativeContainer() {
List() {
// ForEach缺少第三个参数，告警
ForEach(this.data, (item: string, index: number) => {
ListItem() {
Text(item);
}
})
}
.width('100%')
.height('100%')
}
.height('100%')
.width('100%')
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-foreach-index-check-V14
爬取时间: 2025-04-30 20:45:46
来源: Huawei Developer
使用Foreach组件时，不建议在keyGenerator中使用index作为返回值或者返回值的一部分，可能会导致性能问题。
滑动丢帧场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
@Entry
@Component
struct ForeachTest {
private data: string[] = ['one', 'two', 'three'];
build() {
RelativeContainer() {
List() {
ForEach(this.data, (item: string, index: number) => {
ListItem() {
Text(item);
}
}, (item: string, index: number) => item)
}
.width('100%')
.height('100%')
}
.height('100%')
.width('100%')
}
}
```
反例
```typescript
@Entry
@Component
struct ForeachTest {
private data: string[] = ['one', 'two', 'three'];
build() {
RelativeContainer() {
List() {
// warning line
ForEach(this.data, (item: string, index: number) => {
ListItem() {
Text(item);
}
}, (item: string, index: number) => item + index)
}
.width('100%')
.height('100%')
}
.height('100%')
.width('100%')
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-js-code-cache-by-precompile-check-V14
爬取时间: 2025-04-30 20:46:19
来源: Huawei Developer
建议通过预编译生成JavaScript字节码缓存，可以降低Web页面第一、二次的加载时间。
Web完成时延场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
反例
```typescript
import { webview } from '@kit.ArkWeb';
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct JsCodeCacheByPrecompileCheckReport {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('加载页面')
.onClick(() => {
hiTraceMeter.startTrace('unPrecompileJavaScript', 1);
this.controller.loadUrl('https://www.example.com/b.html');
})
// warning line
Web({ src: 'https://www.example.com/a.html', controller: this.controller })
.fileAccess(true)
.onPageBegin((event) => {
console.log(`load page begin: ${event?.url}`);
})
.onPageEnd((event) => {
hiTraceMeter.finishTrace('unPrecompileJavaScript', 1);
console.log(`load page end: ${event?.url}`);
})
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-js-code-cache-by-interception-check-V14
爬取时间: 2025-04-30 20:46:53
来源: Huawei Developer
在资源拦截场景下，建议生成JavaScript字节码缓存，可以降低Web页面非首次的加载时间。
Web完成时延场景下，建议优先修改。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
import { webview } from '@kit.ArkWeb';
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct JsCodeCacheByInterceptionCheckNoReport0 {
controller: webview.WebviewController = new webview.WebviewController();
responseResource: WebResourceResponse = new WebResourceResponse();
jsData: string = 'JavaScript Data';
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onControllerAttached(async () => {
for (const config of this.configs) {
let content = getContext().resourceManager.getRawFileContentSync(config.localPath);
try {
this.controller.precompileJavaScript(config.url, content, config.options)
.then((errCode: number) => {
console.log('precompile successfully!' );
}).catch((errCode: number) => {
console.error('precompile failed.' + errCode);
})
} catch (err) {
console.error('precompile failed!.' + err.code + err.message);
}
}
})
.onInterceptRequest((event) => {
if (event?.request.getRequestUrl() === 'https://www.example.com/test.js') {
this.responseResource.setResponseHeader([
{
headerKey: 'ResponseDataID',
headerValue: '0000000000001'
}
]);
this.responseResource.setResponseData(this.jsData);
this.responseResource.setResponseEncoding('utf-8');
this.responseResource.setResponseMimeType('application/javascript');
this.responseResource.setResponseCode(200);
this.responseResource.setReasonMessage('OK');
return this.responseResource;
}
return null;
})
.onPageBegin(() => {
hiTraceMeter.startTrace('getMessageData', 0);
})
.onPageEnd(() => {
hiTraceMeter.finishTrace('getMessageData', 0);
})
}
}
configs: Array<Config> = [
{
url: 'https://www.example.com/example.js',
localPath: 'example.js',
options: {
responseHeaders: [
{ headerKey: 'E-Tag', headerValue: 'xxx' },
{ headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
]
}
}
]
}
interface Config {
url: string,
localPath: string,
options: webview.CacheOptions
}
```
反例
拦截请求中未设置ResponseDataID或者自定义协议中isCodeCacheSupported设置为false，均不会生成字节码缓存。
```typescript
// Example without a custom protocol and without setting ResponseDataID in the header
import { webview } from '@kit.ArkWeb';
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct JsCodeCacheByInterceptionCheckReport0 {
controller: webview.WebviewController = new webview.WebviewController();
responseResource: WebResourceResponse = new WebResourceResponse();
jsData: string = 'JavaScript Data';
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onPageBegin(() => {
hiTraceMeter.startTrace('getMessageData', 0);
})
// warning line
.onInterceptRequest(event => {
if (event?.request.getRequestUrl() === 'https://www.example.com/test.js') {
this.responseResource.setResponseData(this.jsData);
this.responseResource.setResponseEncoding('utf-8');
this.responseResource.setResponseMimeType('application/javascript');
this.responseResource.setResponseCode(200);
this.responseResource.setReasonMessage('OK');
return this.responseResource;
}
return null;
})
.onControllerAttached(async () => {
this.controller.precompileJavaScript('', 'content', null)
.then((errCode: number) => {
console.log('precompile successfully!' );
}).catch((errCode: number) => {
console.error('precompile failed.' + errCode);
})
})
.onPageEnd(() => {
hiTraceMeter.finishTrace('getMessageData', 0);
})
}
.width('100%')
}
}
// Example with a custom protocol and with isCodeCacheSupported set to false
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct JsCodeCacheByInterceptionCheckReport2 {
// warning line
scheme2: webview.WebCustomScheme = { schemeName: "scheme2", isSupportCORS: true, isSupportFetch: true, isCodeCacheSupported: false }
webController: webview.WebviewController = new webview.WebviewController();
jsData: string = 'JavaScript Data';
aboutToAppear(): void {
try {
webview.WebviewController.customizeSchemes([this.scheme2])
} catch (error) {
let e: BusinessError = error as BusinessError;
console.error(`ErrorCode: ${e.code},  Message: ${e.message}`);
}
}
build() {
Column() {
Web({
src: $rawfile('index2.html'),
controller: this.webController
})
.fileAccess(true)
.javaScriptAccess(true)
.width('100%')
.height('100%')
.onConsole((event) => {
console.log('ets onConsole:' + event?.message.getMessage());
return false
})
.onInterceptRequest((event) => {
if (event?.request.getRequestUrl() == 'scheme2://www.intercept.com/test-cc2.js') {
let responseResource = new WebResourceResponse();
responseResource.setResponseHeader([
{
headerKey: 'ResponseDataID',
headerValue: '0000000000002'
}]);
responseResource.setResponseData(this.jsData);
responseResource.setResponseEncoding('utf-8');
responseResource.setResponseMimeType('application/javascript');
responseResource.setResponseCode(200);
responseResource.setReasonMessage('OK');
return responseResource;
}
return null;
})
.onControllerAttached(async () => {
this.webController.precompileJavaScript('', 'content', null)
.then((errCode: number) => {
console.log('precompile successfully!' );
}).catch((errCode: number) => {
console.error('precompile failed.' + errCode);
})
})
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-previewer-V14
爬取时间: 2025-04-30 20:47:26
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_value-for-local-initialization-V14
爬取时间: 2025-04-30 20:48:00
来源: Huawei Developer
如果组件的属性支持本地初始化，需要设置一个合法的不依赖运行时的默认值。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-page-method-on-preview-component-V14
爬取时间: 2025-04-30 20:48:34
来源: Huawei Developer
禁止在非路由组件上实例化onPageShow、onPageHide、onBackPress等页面级方法。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-unallowed-decorator-on-root-component-V14
爬取时间: 2025-04-30 20:49:08
来源: Huawei Developer
对于@Entry组件，不允许使用@Consume、@Link、@ObjectLink、@Prop注解；对于@Preview组件，建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件作为预览该组件的容器。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-cross-device-app-dev-V14
爬取时间: 2025-04-30 20:49:42
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_color-value-V14
爬取时间: 2025-04-30 20:50:16
来源: Huawei Developer
颜色值应当使用“$r”从color.json中引用，以适配不同的系统颜色模式，禁止使用固定的值。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_font-size-unit-V14
爬取时间: 2025-04-30 20:50:49
来源: Huawei Developer
字体大小单位建议使用fp，以适配系统字体设置。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
const FONT_SIZE = 12;
@Entry
@Component
struct Index {
build() {
RelativeContainer() {
Text('message').fontSize(FONT_SIZE)
Text('message').fontSize('12fp')
}
}
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_font-size-V14
爬取时间: 2025-04-30 20:51:23
来源: Huawei Developer
字体大小要求至少为8fp以便于阅读。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
const FONT_SIZE = 12;
@Entry
@Component
struct Index {
build() {
RelativeContainer() {
Text('message').fontSize(12)
Text('message').fontSize('12fp')
}
}
}
```
反例
```typescript
const FONT_SIZE = 7;
@Entry
@Component
struct Index1 {
build() {
RelativeContainer() {
Text('message').fontSize(FONT_SIZE)
Text('message').fontSize('7fp')
}
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_grid-columns-span-V14
爬取时间: 2025-04-30 20:51:57
来源: Huawei Developer
不推荐开发者将栅格中所有的GridCol子组件只设置span属性，且值与父组件的columns属性相等。这等效于子组件宽度始终为父容器的100%，栅格系统没有发挥作用，徒增页面组件树复杂度，影响性能。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_grid-span-value-V14
爬取时间: 2025-04-30 20:52:32
来源: Huawei Developer
在栅格布局组件GridCol中，span和offset不建议使用小数。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_size-unit-V14
爬取时间: 2025-04-30 20:53:06
来源: Huawei Developer
组件通用属性width、height和size，应当使用vp作为单位，以适配不同设备屏幕宽度。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_touch-target-size-V14
爬取时间: 2025-04-30 20:53:40
来源: Huawei Developer
组件通用属性responseRegion点击热区需满足最小尺寸要求。
主要交互元素或控件的可点击热区至少为48vp×48vp（推荐），不得小于40vp×40vp。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_sidebar-navigation-V14
爬取时间: 2025-04-30 20:54:14
来源: Huawei Developer
对于2in1和tablet设备，应将Tabs组件设置为侧边导航栏。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_color-contrast-V14
爬取时间: 2025-04-30 20:54:49
来源: Huawei Developer
文本和背景之间的颜色对比度至少为4.5:1以确保可读性。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hw-stylistic-V14
爬取时间: 2025-04-30 20:55:24
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_array-bracket-spacing-V14
爬取时间: 2025-04-30 20:55:58
来源: Huawei Developer
强制数组“[”之后和“]”之前加空格。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-brace-style-stylistic-V14
爬取时间: 2025-04-30 20:56:33
来源: Huawei Developer
强制大括号和语句位于同一行。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-comma-spacing-stylistic-V14
爬取时间: 2025-04-30 20:57:07
来源: Huawei Developer
强制数组元素和函数中多个参数之间的逗号后面加空格，逗号前不加空格。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_curly-V14
爬取时间: 2025-04-30 20:57:43
来源: Huawei Developer
条件语句和循环语句的逻辑代码必须写在大括号中。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export function test(a: number, b: number) {
if (a > b) {
console.info('doSomething');
} else if (a = b) {
console.info('doSomething');
} else {
console.info('doSomething');
}
while (a > b) {
a--;
console.info('doSomething');
}
console.info('doSomething');
}
```
反例
```typescript
export function test(a: number, b: number) {
if (a > b)
// Expected { after 'if' condition.
console.info('doSomething');
else if (a = b)
// Expected { after 'if' condition.
console.info('doSomething');
else
// Expected { after 'else'.
console.info('doSomething');
console.info('doSomething');
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-file-naming-convention-V14
爬取时间: 2025-04-30 20:58:17
来源: Huawei Developer
强制代码文件和资源文件保持一致的命名风格。
规则配置
选项
该规则默认检查代码文件和资源文件的命名风格，也可以接受一个对象作为参数{selector: string}，来指定只检查代码文件或者资源文件。"selector"支持配置为"resources"或者"code"。
示例：
1.以下配置只检查代码文件命名风格：
2.以下配置只检查资源文件命名风格：
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_indent-V14
爬取时间: 2025-04-30 20:58:51
来源: Huawei Developer
强制switch语句中的case和default缩进一层。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-keyword-spacing-stylistic-V14
爬取时间: 2025-04-30 20:59:24
来源: Huawei Developer
在关键字前后强制加空格。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export function test(a: number, b: number) {
if (a > b) {
console.info('doSomething');
} else if (a = b) {
console.info('doSomething');
} else {
console.info('doSomething');
}
for (const item of [a, b]) {
console.info(`${item}`);
}
}
```
反例
```typescript
export function test(a: number, b: number) {
// Expected space after 'if'.
if(a > b) {
console.info('doSomething');
// Expected space before 'else'.
// Expected space after 'if'.
}else if(a = b) {
console.info('doSomething');
// Expected space before 'else'.
// Expected space after 'else'.
}else{
console.info('doSomething');
}
// Expected space after 'for'.
for(const item of [a, b]) {
console.info(`${item}`);
}
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_max-len-V14
爬取时间: 2025-04-30 20:59:58
来源: Huawei Developer
强制代码行最大长度为120个字符。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-multi-spaces-V14
爬取时间: 2025-04-30 21:00:32
来源: Huawei Developer
不允许出现连续多个空格，除非是换行。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export const message: string = 'Hello World';
```
反例
```typescript
// Multiple spaces found before 'message'.
// Multiple spaces found before 'string'.
// Multiple spaces found before '='.
// Multiple spaces found before ''Hello World''.
export const   message:  string  =  'Hello World';
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_no-tabs-V14
爬取时间: 2025-04-30 21:01:06
来源: Huawei Developer
禁止使用tab作为缩进，推荐使用空格。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export const message: string = 'Hello World';
```
反例
```typescript
export    const    message:    string = 'Hello World';
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_object-property-newline-V14
爬取时间: 2025-04-30 21:01:39
来源: Huawei Developer
强制对象属性换行。该规则仅检查.ets文件类型。
对象属性不超过4个时，允许在同一行，也可以每个属性都换行。对象属性超过4个时，每个属性必须都换行。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_one-var-declaration-per-line-V14
爬取时间: 2025-04-30 21:02:13
来源: Huawei Developer
变量声明时，要求一次仅声明一个变量。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_operator-linebreak-V14
爬取时间: 2025-04-30 21:02:47
来源: Huawei Developer
强制运算符位于代码行末。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export function test(n1: number, n2: number): void {
if (n1 > n2) {
console.info('hello');
}
if (n1 >
n2) {
console.info('hello');
}
}
```
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-quotes-stylistic-V14
爬取时间: 2025-04-30 21:03:21
来源: Huawei Developer
强制字符串使用单引号。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_semi-spacing-V14
爬取时间: 2025-04-30 21:03:55
来源: Huawei Developer
强制分号之前不加空格。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export {x, test, C};
const x = 10;
function test(size: number): number {
let sum = 0;
for (let a = 0; a < size; a++) {
sum += a;
}
return sum;
}
class C {
public name: string = 'hello';
}
```
反例
```typescript
// Unexpected whitespace before semicolon.
export {x, test, C} ;
// Unexpected whitespace before semicolon.
const x = 10 ;
function test(size: number): number {
let sum = 0;
// Unexpected whitespace before semicolon.
// Unexpected whitespace before semicolon.
for (let a = 0 ; a < size ; a++) {
sum += a;
}
// Unexpected whitespace before semicolon.
return sum ;
}
class C {
// Unexpected whitespace before semicolon.
public name: string = 'hello' ;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_space-before-blocks-V14
爬取时间: 2025-04-30 21:04:28
来源: Huawei Developer
强制在“{”之前加空格。该规则仅检查.ets文件类型。
例外：
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-space-before-function-paren-stylistic-V14
爬取时间: 2025-04-30 21:05:02
来源: Huawei Developer
在函数名和“(”之间强制不加空格。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-space-infix-ops-stylistic-V14
爬取时间: 2025-04-30 21:05:36
来源: Huawei Developer
强制运算符前后都加空格。该规则仅检查.ets文件类型。
规则配置
选项
该规则无需配置额外选项。
正例
```typescript
export function test(size: number) {
for (let i = 0; i < size; i++) {
console.info(`${i}`);
}
}
export function test1(a: boolean, b: boolean, c: boolean) {
return a || (b && c)
}
```
反例
```typescript
export function test(size: number) {
// Operator '=' must be spaced.
// Operator '<' must be spaced.
for (let i=0; i<size; i++) {
console.info(`${i}`);
}
}
export function test1(a: boolean, b: boolean, c: boolean) {
// Operator '||' must be spaced.
// Operator '&&' must be spaced.
return a||b&&c;
}
```
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-codelinter-correctness-V14
爬取时间: 2025-04-30 21:06:10
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_listen-default-network-change-V14
爬取时间: 2025-04-30 21:06:43
来源: Huawei Developer
建议应用监听默认网络的变化，关闭原有网络的数据传输，并使用新网络建立数据传输。
该规则仅在联网类应用检查整个工程时才生效。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide_listen-multi-network-concurrent-V14
爬取时间: 2025-04-30 21:07:17
来源: Huawei Developer
建议应用订阅连接迁移通知，可在WiFi/蜂窝连接切换前后获取切换状态通知。
该规则仅在联网类应用检查整个工程时才生效。
规则配置
选项
该规则无需配置额外选项。
正例
反例
规则集
Code Linter代码检查规则的配置指导请参考代码Code Linter检查。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-environment-config-V14
爬取时间: 2025-04-30 21:07:51
来源: Huawei Developer
DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。
一般来说，如果使用的是个人或家庭网络，是不需要配置代理信息的，部分企业网络受限的情况下，才需要配置代理信息。
诊断开发环境
为了您开发应用/元服务的良好体验，DevEco Studio提供了开发环境诊断的功能，帮助您识别开发环境是否完备。您可以在欢迎页面单击Diagnose进行诊断。如果您已经打开了工程开发界面，也可以在菜单栏单击Help > Diagnostic Tools > Diagnose Development Environment进行诊断。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.26068774296334172571990335591461:50001231000000:2800:A7E778BB16CFA6243CAAEEDE5B0D49A936853888F7F5815DEE4E1A0415C9F8E5.png)
DevEco Studio开发环境诊断项包括电脑的配置、网络的连通情况等。如果检测结果为未通过，请根据检查项的描述和修复建议进行处理。
配置Proxy代理
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.70785941869089922190280221652975:50001231000000:2800:86C59D602A533DB369DA87DDB6436A25B15F922149F861F001DDF087D3589517.png)
配置NPM代理
Hvigor、ohpm在初始化时需要从npm仓库下载依赖，如果需要代理才能访问网络，请配置npm的代理。
1.
2.
3.  如果password中存在特殊字符，如@、#、*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：
4.  在系统或者用户的PATH变量中，添加Node.js安装位置的路径（默认路径为$DevEco Studio安装目录\tools\node下）。
5.  在系统或者用户的PATH变量中，添加Node.js安装位置的路径（默认路径为$DevEco Studio安装目录\tools\node下）。
6.  执行结果如下图所示，则说明代理设置成功。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181216.33938733382386657491950426141499:50001231000000:2800:C25BAA9A45B1601EF0F115E2F22EB9BD0CF7D2E52EA9D545C7AD78B611989135.png)
-  在系统或者用户的PATH变量中，添加Node.js安装位置的路径（默认路径为$DevEco Studio安装目录\tools\node下）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181217.41057845526426426285142129608148:50001231000000:2800:93E2E7EFDA218436E7020281A52C28FF50453162BBDA586CAD5F9B5F6DF0F1B9.png)
配置OHPM代理
具体配置如下：
填写并勾选以上信息后，点击OK。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181217.31195311525268884789564332289539:50001231000000:2800:EB1F62D663FAA80C4BCFF3AA1C6671AA9481E6065B203179743485D007E99A7B.png)
说明：ohpm默认校验registry仓库地址证书。如果环境检查中ohpm registry access出现'SELF_SIGNED_CERT_IN_CHAIN'或'UNABLE_TO_VERIFY_LEAF_SIGNATURE'等证书校验错误时，请查看FAQ-问题现象2解决证书校验错误问题。
在此界面配置的代理信息将写入“users/用户名/.ohpm”目录下的.ohpmrc文件。因此也可直接修改“users/用户名/.ohpm”目录下的.ohpmrc文件进行配置。
1.
2.  如果password中存在特殊字符，如@、#、*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：
3.  在此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量中，在系统或者用户的PATH变量中，添加ohpm安装位置下bin文件夹的路径。默认路径为：DevEco Studio解压目录\tools\ohpm。
4.  在此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量中，在系统或者用户的PATH变量中，添加ohpm安装位置下bin文件夹的路径。默认路径为：DevEco Studio解压目录\tools\ohpm。
5.  执行结果如下图所示，则说明代理设置成功。
-  在此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量中，在系统或者用户的PATH变量中，添加ohpm安装位置下bin文件夹的路径。默认路径为：DevEco Studio解压目录\tools\ohpm。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181217.48400837546501433328713129865941:50001231000000:2800:0EAE7227D39F5BACC86D5A2EE0F460CA881A40C55FEC96C44FE5AAB32914B30F.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-operation-and-services-V14
爬取时间: 2025-04-30 21:08:24
来源: Huawei Developer
DevEco Studio支持对崩溃问题进行定位以及对崩溃，卡顿，丢帧，能耗等异常进行数据分析。
页面布局
在DevEco Studio菜单栏点击View > Tool Windows > Operation Analyzer，进入运维服务页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.05952544244716389122118917715431:50001231000000:2800:43EBBFF3922517F50A5BF0326AACFBD11E8611E723A04F1C93EA8CFE56AC68A2.png?needInitFileName=true?needInitFileName=true)
点击Add account按钮，登录华为账号并授权后，可以查看当前账号下应用异常情况。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.10344733269877199227961213106358:50001231000000:2800:FB210AE46CA95D70F4B0943F604279011E2E9EAF0A1852D2D09C40D7A9FBB844.png?needInitFileName=true?needInitFileName=true)
当前页面共分为两个部分。页面左侧为菜单栏，右侧为数据内容展示区：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.80512710040788798536727277184256:50001231000000:2800:932D072FA2AD05789CA1788B6CDA2FFE8D52AD8339C3BD71B97419CB45732369.png?needInitFileName=true?needInitFileName=true)
Reports
展示具体的崩溃详情。支持混淆的代码还原，并可跳转到具体的代码行查找问题。
1号区域：展示崩溃问题列表。
2号区域：通过tab切换展示堆栈和系统内存的具体信息。
3号区域：当前选中的问题有多个不同的异常点，通过分页切换具体定位。
4号区域：符号表配置按钮。点击按钮将当前选中的堆栈还原为原始代码，选中带有路径的代码行，然后可以点击最右侧的Open in project按钮跳转到应用中问题所在位置。
5号区域：展示当前设备信息。
6号区域：可以切换不同设备型号及时间段查看崩溃发生的分布情况。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.78534358275322517077262932922842:50001231000000:2800:59A515C26DF8840DDDBAFD2DA4BBCE8E4E16BE56E2A232804F5852948961EA73.png?needInitFileName=true?needInitFileName=true)
Metrics
Crash分析
展示应用崩溃次数和崩溃率情况。
1号区域：通过tab页签可切换All，JsError（JavaScript崩溃错误），CppCrash（C++崩溃错误），OOM（内存导致的崩溃），ProcessKill（系统被强制终止），查看不同维度的崩溃次数、崩溃率进行分析。
2号区域：通过柱状图展示不同维度在所有的崩溃异常中的占比。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.85227918626137365963768878325840:50001231000000:2800:AE0C40FDB268E26D0319DC44A31D395C5EAAFFDBFA0EB8EDDBED771868ED31F3.png?needInitFileName=true?needInitFileName=true)
ProcessKill将通过柱状图和饼图联动，点击柱状图，通过饼图展示具体某个时间段的ProcessKill的类型分布。
Frame Loss分析
对连续丢帧情况进行多维度统计，便于迅速的定位问题所在位置。
1号区域：丢帧总览是统计最大维度的连续丢帧率。
2号区域：按照Page，Scenes两个维度展示丢帧异常率TOP N的页面或者场景。点击饼图上的某个区域，将展示具体页面或者场景的连续丢帧率情况。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.02625542406021937287861266919855:50001231000000:2800:5D8941630B247D7917A80E75DD2EF37B4C3D4606917575766B5CB86E46D6A6C7.png?needInitFileName=true?needInitFileName=true)
Launch分析
统计设备启动在不同维度的情况，帮助分析异常问题的分布情况。
1号区域：从左到右依次展示正常冷启动次数，慢冷启动次数，慢冷启动率信息。可点击右侧tab页签，切换展示冷启动或热启动的情况。
2号区域：通过柱状图形式展示各项参数的数据分布情况。
3号区域：按照应用版本，设备型号，系统版本展示启动的数据分布情况。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.72567844377115447023097648689047:50001231000000:2800:C50C56946A12C99C2C02285FC3CE9B8A13CC28585EB74CF1B53A1CE62BD80681.png?needInitFileName=true?needInitFileName=true)
Battery Usage分析
用于统计设备的总能耗以及前后台的能耗和耗电时长。
1号区域：能耗概览。通过折线图展示总能耗，前台能耗，后台能耗。
2号区域：展示前台能耗和耗电时长随Top 5设备器件分布情况。
3号区域：展示后台能耗和耗电时长随Top 5设备器件分布情况。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.62660068110362745361207175781973:50001231000000:2800:8D59EA5A6B4F475071B481C1A8402C38239FDB0535CA2A8D1F88D901D70D0C77.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-app-analyzer-rules-V14
爬取时间: 2025-04-30 21:08:58
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-app-analyzer-all-rules-V14
爬取时间: 2025-04-30 21:09:31
来源: Huawei Developer
通过AppAnalyzer对应用/元服务进行体检的指导请参考应用与元服务体检。
从5.0.7.100版本开始，下线部分体检规则，具体下线的规则参见以下表格。
兼容性
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| 应用/元服务支持在当前OS版本/设备类型安装  | 应用在其配置支持运行的对应软件版本/设备类型上成功安装。  | 应用，元服务  | 5  |
| 应用/元服务支持在当前OS版本/设备类型启动  | 应用正常启动，进入应用首界面。  | 应用，元服务  | 5  |
| 应用/元服务支持在当前OS版本/设备类型卸载  | 应用在其配置支持运行的对应软件版本/设备类型上成功卸载，卸载无残留(包括文件、数据和进程)。  | 应用，元服务  | 4  |
| 应用/元服务在当前OS版本/设备类型运行稳定  | APP要求在其支持的OS版本/设备类型上运行不会出现崩溃、冻屏无响应、无法返回等问题。  | 应用，元服务  | 3  |
体检规则
规则详情
应用或元服务规则
权重
应用/元服务支持在当前OS版本/设备类型安装
应用在其配置支持运行的对应软件版本/设备类型上成功安装。
应用，元服务
5
应用/元服务支持在当前OS版本/设备类型启动
应用正常启动，进入应用首界面。
应用，元服务
5
应用/元服务支持在当前OS版本/设备类型卸载
应用在其配置支持运行的对应软件版本/设备类型上成功卸载，卸载无残留(包括文件、数据和进程)。
应用，元服务
4
应用/元服务在当前OS版本/设备类型运行稳定
APP要求在其支持的OS版本/设备类型上运行不会出现崩溃、冻屏无响应、无法返回等问题。
应用，元服务
3
规格约束
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| Entry hap检测  | 在一个应用包中，同一个设备上必须要有一个Entry hap，且仅有一个；其他的hap为Feature hap，可以有一个或多个，也可以不含Feature hap。  | 应用，元服务  | 5  |
| 包名和版本号一致性检测（已下线）  | 在一个应用包中，所有HAP的配置文件中的bundleName、versionCode标签必须一致。  | 应用，元服务  | 4  |
| SDK版本检测（已下线）  | APP必须声明其所运行的最小和目标SDK版本号。  | 应用，元服务  | 3  |
| ReqPermissions权限检测（已下线）  | 在一个应用包中，所有entry和feature hap的ReqPermissions权限必须填写name，除此之外，user_grant权限则必填reason和usedScene字段。  | 应用，元服务  | 4  |
| 设备类型检测  | 在一个应用包中，每个hap包必须明确支持的设备类型，不能为空。  | 应用，元服务  | 5  |
| 应用/元服务必须有图标（已下线）  | 元服务/应用需要有图标。  | 应用，元服务  | 5  |
| 应用要支持64位so文件  | 如果APP集成native so，则要求提供64位so。  | 应用  | 4  |
| 元服务内所有包总和大小不超过10MB  | 单个元服务内所有包文件（加上其依赖的所有共享包）的大小总和不能超过10MB。  | 元服务  | 2  |
| 元服务单个包文件大小不超过2MB（已下线）  | 元服务内单个包文件（加上其依赖的所有共享包），大小不能超过2MB。  | 元服务  | 2  |
| 元服务免安装属性检测（已下线）  | 必须标识当前module是否支持免安装特性，元服务的所有entry、feature、shared包必须配置为免安装。  | 元服务  | 4  |
| 元服务预加载对应模块类型不能为entry（已下线）  | preloads列表配置的moduleName对应的moduleType（模块类型）不能为entry。  | 元服务  | 4  |
| 应用非免安装属性检测（已下线）  | 必须标识当前module是否支持免安装特性，应用的所有entry、feature、shared包必须配置为非免安装或不配置。  | 应用  | 2  |
| 卡片metadata元信息检测（已下线）  | 卡片metadata元信息标签，其key固定为ohos.extension.form，且value是配置文件的索引。  | 应用，元服务  | 3  |
| 卡片supportDimensions字段检测（已下线）  | 卡片仅支持的外观规格为：1*2,2*2,2*4,4*4。  | 应用，元服务  | 3  |
| 卡片defaultDimension字段检测（已下线）  | 卡片defaultDimension不可缺省，取值必须在supportDimensions配置中。  | 应用，元服务  | 3  |
| 卡片isDefault字段检测  | 卡片isDefault不可缺省，每个UIAbility有且只有一个默认卡片。  | 应用，元服务  | 3  |
| 卡片updateEnabled字段检测（已下线）  | 卡片配置文件中的updateEnabled不可缺省，设置为true时必须设置scheduledUpdateTime和updateDuration字段，可以设置其中一个或同时设置两个。  | 应用，元服务  | 3  |
| 卡片description字段检测  | 卡片description字段需要用索引方式填写。  | 应用，元服务  | 4  |
| 应用链接跳转检测  | 如果涉及通过链接拉起应用的功能，建议使用App Linking的方式支持该功能。  | 应用  | 3  |
体检规则
规则详情
应用或元服务规则
权重
Entry hap检测
在一个应用包中，同一个设备上必须要有一个Entry hap，且仅有一个；其他的hap为Feature hap，可以有一个或多个，也可以不含Feature hap。
应用，元服务
5
包名和版本号一致性检测（已下线）
在一个应用包中，所有HAP的配置文件中的bundleName、versionCode标签必须一致。
应用，元服务
4
SDK版本检测（已下线）
APP必须声明其所运行的最小和目标SDK版本号。
应用，元服务
3
ReqPermissions权限检测（已下线）
在一个应用包中，所有entry和feature hap的ReqPermissions权限必须填写name，除此之外，user_grant权限则必填reason和usedScene字段。
应用，元服务
4
设备类型检测
在一个应用包中，每个hap包必须明确支持的设备类型，不能为空。
应用，元服务
5
应用/元服务必须有图标（已下线）
元服务/应用需要有图标。
应用，元服务
5
应用要支持64位so文件
如果APP集成native so，则要求提供64位so。
应用
4
元服务内所有包总和大小不超过10MB
单个元服务内所有包文件（加上其依赖的所有共享包）的大小总和不能超过10MB。
元服务
2
元服务单个包文件大小不超过2MB（已下线）
元服务内单个包文件（加上其依赖的所有共享包），大小不能超过2MB。
元服务
2
元服务免安装属性检测（已下线）
必须标识当前module是否支持免安装特性，元服务的所有entry、feature、shared包必须配置为免安装。
元服务
4
元服务预加载对应模块类型不能为entry（已下线）
preloads列表配置的moduleName对应的moduleType（模块类型）不能为entry。
元服务
4
应用非免安装属性检测（已下线）
必须标识当前module是否支持免安装特性，应用的所有entry、feature、shared包必须配置为非免安装或不配置。
应用
2
卡片metadata元信息检测（已下线）
卡片metadata元信息标签，其key固定为ohos.extension.form，且value是配置文件的索引。
应用，元服务
3
卡片supportDimensions字段检测（已下线）
卡片仅支持的外观规格为：1*2,2*2,2*4,4*4。
应用，元服务
3
卡片defaultDimension字段检测（已下线）
卡片defaultDimension不可缺省，取值必须在supportDimensions配置中。
应用，元服务
3
卡片isDefault字段检测
卡片isDefault不可缺省，每个UIAbility有且只有一个默认卡片。
应用，元服务
3
卡片updateEnabled字段检测（已下线）
卡片配置文件中的updateEnabled不可缺省，设置为true时必须设置scheduledUpdateTime和updateDuration字段，可以设置其中一个或同时设置两个。
应用，元服务
3
卡片description字段检测
卡片description字段需要用索引方式填写。
应用，元服务
4
应用链接跳转检测
如果涉及通过链接拉起应用的功能，建议使用App Linking的方式支持该功能。
应用
3
UX测试（已下线）
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| 基础信息（已下线）  | 每个原子化服务有独立的图标、名称、描述、快照。基础信息将根据场景在服务中心、系统设置等界面展示。  | 元服务  | 2  |
| 服务卡片定时刷新（已下线）  | 服务卡片定时刷新最高频率限定在30分钟1次。  | 元服务  | 1  |
| 卡片背景圆角检测（已下线）  | 禁止自定义卡片背景的圆角。  | 元服务  | 1  |
| 卡片最小字体检测（已下线）  | 卡片内最小字号不小于8vp。  | 元服务  | 1  |
| 卡片内容圆角检测（已下线）  | 卡片内容（组件）圆角请在4vp、8vp、12vp参数中选择。  | 元服务  | 1  |
| 卡片热区大小检测（已下线）  | 卡片热区最短边不得小于32vp。  | 元服务  | 1  |
体检规则
规则详情
应用或元服务规则
权重
基础信息（已下线）
每个原子化服务有独立的图标、名称、描述、快照。基础信息将根据场景在服务中心、系统设置等界面展示。
元服务
2
服务卡片定时刷新（已下线）
服务卡片定时刷新最高频率限定在30分钟1次。
元服务
1
卡片背景圆角检测（已下线）
禁止自定义卡片背景的圆角。
元服务
1
卡片最小字体检测（已下线）
卡片内最小字号不小于8vp。
元服务
1
卡片内容圆角检测（已下线）
卡片内容（组件）圆角请在4vp、8vp、12vp参数中选择。
元服务
1
卡片热区大小检测（已下线）
卡片热区最短边不得小于32vp。
元服务
1
性能
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| 应用内点击操作响应快  | 时间起点：点击离手； 时间终点：界面发生变化； 应用内点击操作响应时延应≤ 100毫秒。  | 应用  | 3  |
| 应用内点击操作完成快  | 时间起点：点击离手； 时间终点：转场页面所有占位符加载完成； 应用内点击操作完成时延应≤ 1600毫秒。  | 应用  | 3  |
| 应用内滑动操作响应快  | 时间起点：手指滑动； 时间终点：界面发生变化； 应用内滑动操作响应时延应≤ 80毫秒。  | 应用  | 3  |
| 应用内滑动过程流畅  | 应用的滑动过程卡顿率≤ 5ms/s； 满帧30FPS的游戏类、地图类和视频类的应用帧率应≥ 29FPS。  | 应用  | 3  |
| 应用内转场操作流畅  | 应用内转场过程卡顿率≤ 0ms/s； 滑动过程卡顿率：动效时间内累计丢帧时间/动效时长。  | 应用  | 3  |
| 应用动态内存峰值占用  | 应用完成操作后，各类应用在后台的内存占用峰值应≤ 1300MB； 应用完成操作后切换到后，静置3min以后采集内存占用。 后台用户可感知应用不涉及，如导航、音乐播放等。  | 应用  | 3  |
| 应用前台场景内存峰值占用  | 应用前台场景峰值内存占用：应用在前台且亮屏使用规程的内存占用应≤ 1500MB。  | 应用  | 3  |
| 应用后台CPU占用峰值  | 应用后台CPU占用峰值：应用切换到后台等待3min后，开始采集3min内CPU Load < 5%。  | 应用  | 3  |
| 图形渲染服务处理节点数小于500  | 后端Render Server在每帧数据里处理的节点数不应该超过500，否侧会造成CPU使用过高，引发帧时延过高，从而导致丢帧。  | 应用  | 1  |
体检规则
规则详情
应用或元服务规则
权重
应用内点击操作响应快
时间起点：点击离手；
时间终点：界面发生变化；
应用内点击操作响应时延应≤ 100毫秒。
应用
3
应用内点击操作完成快
时间起点：点击离手；
时间终点：转场页面所有占位符加载完成；
应用内点击操作完成时延应≤ 1600毫秒。
应用
3
应用内滑动操作响应快
时间起点：手指滑动；
时间终点：界面发生变化；
应用内滑动操作响应时延应≤ 80毫秒。
应用
3
应用内滑动过程流畅
应用的滑动过程卡顿率≤ 5ms/s；
满帧30FPS的游戏类、地图类和视频类的应用帧率应≥ 29FPS。
应用
3
应用内转场操作流畅
应用内转场过程卡顿率≤ 0ms/s；
滑动过程卡顿率：动效时间内累计丢帧时间/动效时长。
应用
3
应用动态内存峰值占用
应用完成操作后，各类应用在后台的内存占用峰值应≤ 1300MB；
应用完成操作后切换到后，静置3min以后采集内存占用。
后台用户可感知应用不涉及，如导航、音乐播放等。
应用
3
应用前台场景内存峰值占用
应用前台场景峰值内存占用：应用在前台且亮屏使用规程的内存占用应≤ 1500MB。
应用
3
应用后台CPU占用峰值
应用后台CPU占用峰值：应用切换到后台等待3min后，开始采集3min内CPU Load < 5%。
应用
3
图形渲染服务处理节点数小于500
后端Render Server在每帧数据里处理的节点数不应该超过500，否侧会造成CPU使用过高，引发帧时延过高，从而导致丢帧。
应用
1
最佳实践
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| 避免过大的组件树节点数目  | 建议一个页面使用少于1000个组件树节点，节点树深度少于30层，子节点数不大于60个。  | 应用，元服务  | 2  |
| 避免执行脚本的耗时过长  | 脚本执行时间是指JS脚本在一次同步执行中消耗的时间，比如生命周期回调、事件处理函数的同步执行时间。建议单个JS脚本执行周期内运行时间不超过15毫秒。  | 应用，元服务  | 2  |
| 避免渲染界面的耗时过长  | 建议单次渲染时间不超过500ms。渲染界面的耗时过长会让用户觉得卡顿，体验较差，出现这一情况时，需要校验下是否同时渲染的区域太大；页面中单个组件的渲染时间不超过15ms。  | 应用，元服务  | 2  |
| ForEach性能检测  | ForEach中item数量不要超过50。  | 应用，元服务  | 2  |
| 单帧属性数量更新内容限制  | 在高帧率场景单帧更新属性数量建议滑动场景不超过300个，非滑动场景不超过1500个。  | 应用，元服务  | 2  |
| 单帧脏组件数量限制  | 高帧率场景更新组件数量（含布局更新）建议滑动场景不超过30个，非滑动场景单帧更新组件数不超过500个。  | 应用，元服务  | 2  |
| web组件初始化耗时检测  | 避免web组件初始化耗时过长。 应用web页面加载场景下，web组件初始化时间不超过25ms。  | 应用，元服务  | 2  |
| web执行js耗时检测  | 避免web页面js执行耗时过长。 应用web页面加载场景下，web页面单个js编译时间不超过30ms，单个js运行时间不超过30ms，总体js执行时间不超过300ms。  | 应用，元服务  | 2  |
| UI线程IO执行耗时长未并行化检测  | 避免UI线程中执行文件IO耗时过长。 UI主线程中，不应出现执行IO函数超过8.3毫秒，如果出现需要进行IO并行化改造。  | 应用，元服务  | 2  |
| UI线程耗时操作检测  | 避免UI线程中的函数耗时过长。 UI主线程中，不应出现函数超过8.3毫秒，如果出现需要进行IO并行化改造。  | 应用，元服务  | 2  |
| web主资源下载耗时检测  | 避免web主资源下载耗时过长。 应用web页面加载场景下，web主资源下载时间不超过300ms。  | 应用，元服务  | 2  |
| web子资源下载耗时检测  | 避免web子资源下载耗时过长。 应用web页面加载场景下，web单个子资源下载时间不超过200ms。  | 应用，元服务  | 2  |
| 短视频起播时延检测  | 时间起点：从用户滑动屏幕抬手后； 时间终点：到短视频第二帧画面(非封面帧)； 显示时间≤ 700毫秒。  | 应用  | 2  |
| 相机拍照完成时延检测  | 相机从拍照开始到生成可预览照片的完成时延不应超过1000ms。 如果超过，建议使用分段式拍照。 注意：请授予相机的权限。  | 应用  | 2  |
体检规则
规则详情
应用或元服务规则
权重
避免过大的组件树节点数目
建议一个页面使用少于1000个组件树节点，节点树深度少于30层，子节点数不大于60个。
应用，元服务
2
避免执行脚本的耗时过长
脚本执行时间是指JS脚本在一次同步执行中消耗的时间，比如生命周期回调、事件处理函数的同步执行时间。建议单个JS脚本执行周期内运行时间不超过15毫秒。
应用，元服务
2
避免渲染界面的耗时过长
建议单次渲染时间不超过500ms。渲染界面的耗时过长会让用户觉得卡顿，体验较差，出现这一情况时，需要校验下是否同时渲染的区域太大；页面中单个组件的渲染时间不超过15ms。
应用，元服务
2
ForEach性能检测
ForEach中item数量不要超过50。
应用，元服务
2
单帧属性数量更新内容限制
在高帧率场景单帧更新属性数量建议滑动场景不超过300个，非滑动场景不超过1500个。
应用，元服务
2
单帧脏组件数量限制
高帧率场景更新组件数量（含布局更新）建议滑动场景不超过30个，非滑动场景单帧更新组件数不超过500个。
应用，元服务
2
web组件初始化耗时检测
避免web组件初始化耗时过长。
应用web页面加载场景下，web组件初始化时间不超过25ms。
应用，元服务
2
web执行js耗时检测
避免web页面js执行耗时过长。
应用web页面加载场景下，web页面单个js编译时间不超过30ms，单个js运行时间不超过30ms，总体js执行时间不超过300ms。
应用，元服务
2
UI线程IO执行耗时长未并行化检测
避免UI线程中执行文件IO耗时过长。
UI主线程中，不应出现执行IO函数超过8.3毫秒，如果出现需要进行IO并行化改造。
应用，元服务
2
UI线程耗时操作检测
避免UI线程中的函数耗时过长。
UI主线程中，不应出现函数超过8.3毫秒，如果出现需要进行IO并行化改造。
应用，元服务
2
web主资源下载耗时检测
避免web主资源下载耗时过长。
应用web页面加载场景下，web主资源下载时间不超过300ms。
应用，元服务
2
web子资源下载耗时检测
避免web子资源下载耗时过长。
应用web页面加载场景下，web单个子资源下载时间不超过200ms。
应用，元服务
2
短视频起播时延检测
时间起点：从用户滑动屏幕抬手后；
时间终点：到短视频第二帧画面(非封面帧)；
显示时间≤ 700毫秒。
应用
2
相机拍照完成时延检测
相机从拍照开始到生成可预览照片的完成时延不应超过1000ms。
如果超过，建议使用分段式拍照。
注意：请授予相机的权限。
应用
2
功耗
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| 后台进程CPU负载约束（长时任务）  | 应用或元服务后台CPU运行：后台进程持续10分钟CPU负载不得高于10%；(8核负载，即总负载为80%)。  | 应用  | 1  |
| 后台进程CPU负载约束（短时任务）  | 应用或元服务后台CPU运行：后台进程任务期间CPU负载不得高于8%；(8核负载，即总负载为64%)。  | 应用  | 1  |
| 合理使用蓝牙资源  | 无长时任务的应用退到后台不允许有蓝牙扫描。  | 应用  | 1  |
| 合理使用麦克风或者扬声器  | 无长时任务的应用退后台禁止使用麦克风或扬声器。  | 应用  | 1  |
| 合理使用GPS资源  | 无长时任务的应用退后台禁止使用定位服务。  | 应用  | 1  |
| 合理使用sensor资源  | 应用退后台禁止使用传感器，前台使用时根据业务尽量使用once()接口监听结果。  | 应用  | 1  |
| 后台合理使用系统资源  | 无长时任务的应用退后台对应资源释放，不要直接或者间接持running lock锁。  | 应用  | 1  |
体检规则
规则详情
应用或元服务规则
权重
后台进程CPU负载约束（长时任务）
应用或元服务后台CPU运行：后台进程持续10分钟CPU负载不得高于10%；(8核负载，即总负载为80%)。
应用
1
后台进程CPU负载约束（短时任务）
应用或元服务后台CPU运行：后台进程任务期间CPU负载不得高于8%；(8核负载，即总负载为64%)。
应用
1
合理使用蓝牙资源
无长时任务的应用退到后台不允许有蓝牙扫描。
应用
1
合理使用麦克风或者扬声器
无长时任务的应用退后台禁止使用麦克风或扬声器。
应用
1
合理使用GPS资源
无长时任务的应用退后台禁止使用定位服务。
应用
1
合理使用sensor资源
应用退后台禁止使用传感器，前台使用时根据业务尽量使用once()接口监听结果。
应用
1
后台合理使用系统资源
无长时任务的应用退后台对应资源释放，不要直接或者间接持running lock锁。
应用
1
快速性能
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| 页面内点击操作完成时延快速检测  | 时间起点：点击离手； 时间终点：转场页面所有占位符加载完成； 应用内点击操作完成时延应≤ 1600毫秒。  | 应用  | 3  |
| 页面内滑动过程流畅性快速检测  | 应用的滑动过程卡顿率≤ 5ms/s； 满帧30FPS的游戏类、地图类和视频类的应用帧率应≥ 29FPS。  | 应用  | 3  |
| 页面转场操作流畅性快速检测  | 应用的应用内转场过程卡顿率≤ 0ms/s； 滑动过程卡顿率：动效时间内累计丢帧时间/动效时长。  | 应用  | 3  |
| 页面内节点数超过500过多快速检测  | 后端Render Server在每帧数据里处理的节点数不应该超过500，否侧会造成CPU使用过高，引发帧时延过高，从而导致丢帧。  | 应用  | 1  |
| 页面内白块检测  | 应用内页面检测到白块，需要避免在应用启动进入界面或者快速滑动场景下因数据来不及加载而出现白块。  | 应用  | 1  |
| 页面内点击操作响应时延快速检测  | 时间起点：点击离手； 时间终点：界面发生变化； 应用内点击操作响应时延应≤ 100毫秒。  | 应用  | 3  |
| 页面内滑动响应时延快速检测  | 时间起点：手指滑动； 时间终点：界面发生变化； 应用内滑动操作响应时延应≤ 80毫秒。  | 应用  | 3  |
| 避免页面内UI容器组件超出屏幕过多  | 避免滑动类容器组件区域超出屏幕显示范围10%。 滑动类容器组件的渲染范围与容器大小相同，超出屏幕的不可见部分为冗余渲染。 在页面切换的场景，过多的冗余渲染，可能会让用户觉得页面切换慢，响应不及时。 建议将滑动类容器组件的大小和位置限定在屏幕显示范围内。 如果因为嵌套滚动等效果，必须超出屏幕的，可以考虑使用分帧多次加载数据的方式，优先渲染可见部分，提升页面切换性能。  | 应用  | 1  |
| 应用冷启动完成时延检测  | 应用首页铺满全屏并且所有占位符加载完成。  | 应用  | 3  |
| 避免序列化反序列化耗时长  | 使用TaskPool/Worker并发能力时候，会检测对象和方法在跨线程传递时序列化和反序列化的耗时； 序列化和反序列化耗时应 ≤ 8ms。  | 应用  | 3  |
体检规则
规则详情
应用或元服务规则
权重
页面内点击操作完成时延快速检测
时间起点：点击离手；
时间终点：转场页面所有占位符加载完成；
应用内点击操作完成时延应≤ 1600毫秒。
应用
3
页面内滑动过程流畅性快速检测
应用的滑动过程卡顿率≤ 5ms/s；
满帧30FPS的游戏类、地图类和视频类的应用帧率应≥ 29FPS。
应用
3
页面转场操作流畅性快速检测
应用的应用内转场过程卡顿率≤ 0ms/s；
滑动过程卡顿率：动效时间内累计丢帧时间/动效时长。
应用
3
页面内节点数超过500过多快速检测
后端Render Server在每帧数据里处理的节点数不应该超过500，否侧会造成CPU使用过高，引发帧时延过高，从而导致丢帧。
应用
1
页面内白块检测
应用内页面检测到白块，需要避免在应用启动进入界面或者快速滑动场景下因数据来不及加载而出现白块。
应用
1
页面内点击操作响应时延快速检测
时间起点：点击离手；
时间终点：界面发生变化；
应用内点击操作响应时延应≤ 100毫秒。
应用
3
页面内滑动响应时延快速检测
时间起点：手指滑动；
时间终点：界面发生变化；
应用内滑动操作响应时延应≤ 80毫秒。
应用
3
避免页面内UI容器组件超出屏幕过多
避免滑动类容器组件区域超出屏幕显示范围10%。
滑动类容器组件的渲染范围与容器大小相同，超出屏幕的不可见部分为冗余渲染。
在页面切换的场景，过多的冗余渲染，可能会让用户觉得页面切换慢，响应不及时。
建议将滑动类容器组件的大小和位置限定在屏幕显示范围内。
如果因为嵌套滚动等效果，必须超出屏幕的，可以考虑使用分帧多次加载数据的方式，优先渲染可见部分，提升页面切换性能。
应用
1
应用冷启动完成时延检测
应用首页铺满全屏并且所有占位符加载完成。
应用
3
避免序列化反序列化耗时长
使用TaskPool/Worker并发能力时候，会检测对象和方法在跨线程传递时序列化和反序列化的耗时；
序列化和反序列化耗时应 ≤ 8ms。
应用
3
安全
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| 申请权限字段规范检测（已下线）  | 应用（包括应用引用的三方库）所需权限必须在应用的配置文件module.json5中严格按照权限开发指导逐个声明，申请user_grant权限时，必须填写reason字段。  | 应用，元服务  | 2  |
| Ability可见性设置检测  | 不对外交互的Ability其exported或visible属性禁止设置为true。  | 应用，元服务  | 2  |
| Ability权限设置检测  | 对外交互的Ability应设置合理的访问权限。  | 应用，元服务  | 2  |
| DataShareExtensionAbility组件权限检测  | DataShareExtensionAbility内接口设置合理的读写访问权限。  | 应用，元服务  | 2  |
| 权限申请最小化原则检测  | 权限申请满足最小化原则，禁止申请不必要的、新版本废弃的权限。  | 应用，元服务  | 2  |
| 公共事件接收器权限访问控制检测  | 对涉及敏感功能的公共事件进行访问权限控制。  | 应用，元服务  | 2  |
| 应用/元服务签名完整性检测  | 应用需保证签名完整性。  | 应用，元服务  | 2  |
| 应用/元服务签名信息检测  | 应用证书所有者的CN、OU、O、C字段不能为空。  | 应用，元服务  | 2  |
体检规则
规则详情
应用或元服务规则
权重
申请权限字段规范检测（已下线）
应用（包括应用引用的三方库）所需权限必须在应用的配置文件module.json5中严格按照权限开发指导逐个声明，申请user_grant权限时，必须填写reason字段。
应用，元服务
2
Ability可见性设置检测
不对外交互的Ability其exported或visible属性禁止设置为true。
应用，元服务
2
Ability权限设置检测
对外交互的Ability应设置合理的访问权限。
应用，元服务
2
DataShareExtensionAbility组件权限检测
DataShareExtensionAbility内接口设置合理的读写访问权限。
应用，元服务
2
权限申请最小化原则检测
权限申请满足最小化原则，禁止申请不必要的、新版本废弃的权限。
应用，元服务
2
公共事件接收器权限访问控制检测
对涉及敏感功能的公共事件进行访问权限控制。
应用，元服务
2
应用/元服务签名完整性检测
应用需保证签名完整性。
应用，元服务
2
应用/元服务签名信息检测
应用证书所有者的CN、OU、O、C字段不能为空。
应用，元服务
2
稳定性
| 体检规则  | 规则详情  | 应用或元服务规则  | 权重  |
| --- | --- | --- | --- |
| 应用/元服务崩溃检测  | 应用或元服务运行过程中无崩溃故障。  | 应用，元服务  | 2  |
| 应用/元服务卡死检测  | 应用或元服务运行过程中无冻屏卡死故障。  | 应用，元服务  | 4  |
| 应用/元服务内存泄漏检测  | 检测出引起内存泄露的代码，提供代码堆栈日志下载。  | 应用，元服务  | 4  |
体检规则
规则详情
应用或元服务规则
权重
应用/元服务崩溃检测
应用或元服务运行过程中无崩溃故障。
应用，元服务
2
应用/元服务卡死检测
应用或元服务运行过程中无冻屏卡死故障。
应用，元服务
4
应用/元服务内存泄漏检测
检测出引起内存泄露的代码，提供代码堆栈日志下载。
应用，元服务
4

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-quick-response-for-click-0403-V14
爬取时间: 2025-04-30 21:10:05
来源: Huawei Developer
检测逻辑
-  如图展示的是H:ABILITY_OR_PAGE_SWITCH泳道，其他转场泳道标记如下： H:APP_TRANSITION_FROM_OTHER_APP H:APP_TRANSITION_TO_OTHER_APP H:APP_SWIPER_NO_ANIMATION_SWITCH H:APP_TABS_NO_ANIMATION_SWITCH H:APP_TABS_FLING
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.50810607705704465574492280271264:50001231000000:2800:FD8BBF60AE0FBC268164194A8E1D007B246FDFAA9C3D7606E1728092CE4E9CAF.png?needInitFileName=true?needInitFileName=true)
计算逻辑
时延=结束时间 - 开始时间，小于等于100ms。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-quick-completion-for-click-0404-V14
爬取时间: 2025-04-30 21:10:40
来源: Huawei Developer
检测逻辑
点击后，经过1600ms后截图，检测图片是否存在白块。白块检测逻辑如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150802.97986147479421301617244073691675:50001231000000:2800:1860412CC242BA43AC43FFBC6FE2BE8C8AB37A477A59AD08802A40AE912607FD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.35354172054952745462076524446707:50001231000000:2800:134FE7439EA08D3EAE6E8BF8CA7767F9BACBF12712D92B8BEEE96E350C209FBA.png?needInitFileName=true?needInitFileName=true)
计算逻辑
查找白块数量为0。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-quick-response-for-swipe-0405-V14
爬取时间: 2025-04-30 21:11:14
来源: Huawei Developer
检测逻辑
-  如图展示的是H:APP_LIST_FLING泳道，其他滑动类泳道标记如下： H:APP_SWIPER_SCROLL H:APP_TABS_SCROLL H:WEB_LIST_FLING
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.33198088141403709371486049777864:50001231000000:2800:187CEC35E357ED08E3B537FB46C1B9C103B07D8FD26270FAD9694A371DDB3D2B.png?needInitFileName=true?needInitFileName=true)
计算逻辑
时延=结束时间-开始时间，小于等于80ms。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-smooth-for-swipe-0413-V14
爬取时间: 2025-04-30 21:11:48
来源: Huawei Developer
检测逻辑
-  其他转场泳道标记如下： H:APP_LIST_FLING H:APP_SWIPER_SCROLL H:WEB_LIST_FLING
-
-  总时长(s)：在以上泳道时间范围内，总时长 =【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。
-  每帧丢帧时间(ms)：max（【Waiting for Present Fence实际时长(ms)】- 【每帧时长(ms)】 * 1.5 , 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.05021813653461937640243859768559:50001231000000:2800:4D1C205C8FA58F57F90E86741C82972E1DD44EECF00A5266E10FC08F50E05740.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.50226346111558184461760451388889:50001231000000:2800:4AB9AA2CBD63E34A0031BDB3B97F4BDDB9CB44A5F604C3D8FD04C297005EBFFE.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.42481781134315846640328761077130:50001231000000:2800:E307D10EB9C8E80180E81004BDEBC1E65F427232191C445B37EE2B41371602E1.png?needInitFileName=true?needInitFileName=true)
计算逻辑
卡顿率(即流畅度) = 【每帧丢帧时间累计总和(ms)】/ 总时长(s)，须小于等5ms/s。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-smooth-for-transition-0414-V14
爬取时间: 2025-04-30 21:12:21
来源: Huawei Developer
检测逻辑
-  其他转场泳道标记如下： H:APP_TRANSITION_FROM_OTHER_APP H:APP_TRANSITION_TO_OTHER_APP H:APP_SWIPER_NO_ANIMATION_SWITCH H:APP_TABS_NO_ANIMATION_SWITCH H:APP_TABS_FLING
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.04721658781286909361415393777736:50001231000000:2800:036B1AD6F02AAA50B513B10617B43C5EEC38C6656B1D820A00D534AA950B13F1.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.79076417948899175329589845234622:50001231000000:2800:03CC87029D600872169602BAB053126B0E5BAC2EB9FDF2D9E499C2C6F40C4442.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.93489356608129996515940020991444:50001231000000:2800:B57184C0ADC202A57477E1FEB52B98E7820D1E97B7C082341FD3925A64B85E2C.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.32743413851012859894230900465942:50001231000000:2800:93780D24087F422AF945907FA39DE253355F4A8934D8230806CBB5ECD885CC10.png?needInitFileName=true?needInitFileName=true)
计算逻辑
卡顿率=所有【每帧丢帧时间(ms)】/ 总时长(s)，卡顿率小于等于0ms/s。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-peak-dynamic-memory-usage-0417-V14
爬取时间: 2025-04-30 21:12:55
来源: Huawei Developer
检测逻辑
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.23702238038328453203730325433006:50001231000000:2800:8B0A73D3036745AE09EDF5BFB7E038BAFF6AC3751C8852F997552DA35FE817A2.png?needInitFileName=true?needInitFileName=true)
计算逻辑
执行多轮测试，取最大Pss值为占用峰值，内存占用须小于1300M。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-peak-foreground-memory-usage-0418-V14
爬取时间: 2025-04-30 21:13:28
来源: Huawei Developer
检测逻辑
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.80397747588344777877809442504981:50001231000000:2800:369E7318C0F7F9C597E1086C8CA979AB651BBCB994F1CA60EBE6A6EEC5D681E0.png?needInitFileName=true?needInitFileName=true)
计算逻辑
执行多轮测试，取最大Pss值为占用峰值，内存占用小于1500M。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-peak-background-cpu-usage-0420-V14
爬取时间: 2025-04-30 21:14:03
来源: Huawei Developer
检测逻辑
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150803.34153455991636305407391523700919:50001231000000:2800:6F470AF2363056CCE68507A703C7A1FB740886EE07EB0CEF8E73F5DB64B51DF5.png?needInitFileName=true?needInitFileName=true)
计算逻辑
执行多轮测试，取最大值为cpu占用峰值，cpu占用率须小于5%。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-render-node-limit-0430-V14
爬取时间: 2025-04-30 21:14:38
来源: Huawei Developer
检测逻辑
-  H:APP_LIST_FLING H:APP_SWIPER_SCROLL H:WEB_LIST_FLING H:ABILITY_OR_PAGE_SWITCH H:APP_TRANSITION_FROM_OTHER_APP H:APP_TRANSITION_TO_OTHER_APP H:APP_SWIPER_NO_ANIMATION_SWITCH H:APP_TABS_NO_ANIMATION_SWITCH H:APP_TABS_FLING
-  H:APP_LIST_FLING H:APP_SWIPER_SCROLL H:WEB_LIST_FLING
-  H:ABILITY_OR_PAGE_SWITCH H:APP_TRANSITION_FROM_OTHER_APP H:APP_TRANSITION_TO_OTHER_APP H:APP_SWIPER_NO_ANIMATION_SWITCH H:APP_TABS_NO_ANIMATION_SWITCH H:APP_TABS_FLING
-  在泳道时序范围内，每一个RenderFrame为一帧，找到这一帧所有的ProcessedNodes字段，提取节点数累加求和（每一帧可能对应多个ProcessedNodes，所以需要累加求和），即每帧渲染的节点数 = Σ ProcessedNodes。
-  H:APP_LIST_FLING H:APP_SWIPER_SCROLL H:WEB_LIST_FLING
-  H:ABILITY_OR_PAGE_SWITCH H:APP_TRANSITION_FROM_OTHER_APP H:APP_TRANSITION_TO_OTHER_APP H:APP_SWIPER_NO_ANIMATION_SWITCH H:APP_TABS_NO_ANIMATION_SWITCH H:APP_TABS_FLING
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150804.48616194579593633892472643956415:50001231000000:2800:406E9FF5F170141C738F43ABD598A6A7D8649A8EDDEBF56D714BABAF2F2233FF.png?needInitFileName=true?needInitFileName=true)
计算逻辑
每帧渲染的节点数小于等于500。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-configuration-parameter-V14
爬取时间: 2025-04-30 21:15:12
来源: Huawei Developer
DevEco Studio基于IntelliJ平台开发，在原生的IntelliJ参数的基础上新增了部分参数，这些参数可在idea.properties中进行配置，参数列表如下：
| 参数  | 参数说明  |
| --- | --- |
| grs_url  | 设置DevEco Studio连接的云端环境。  |
| npm_config_strict_ssl  | 设置是否开启npm的https证书校验。默认为true，表示开启证书校验。  |
| ohpm_config_strict_ssl  | 设置是否开启ohpm的https证书校验。默认为true，表示开启证书校验。  |
参数
参数说明
grs_url
设置DevEco Studio连接的云端环境。
npm_config_strict_ssl
设置是否开启npm的https证书校验。默认为true，表示开启证书校验。
ohpm_config_strict_ssl
设置是否开启ohpm的https证书校验。默认为true，表示开启证书校验。
关闭证书校验，可能会带来安全风险，请谨慎使用。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-close-send-usage-statistics-V14
爬取时间: 2025-04-30 21:15:46
来源: Huawei Developer
DevEco Studio在首次启动时，弹窗出现提示开启数据采集功能。该功能用于帮助DevEco Studio改进使用体验，收集的数据将按照关于HUAWEI DevEco Studio 平台与隐私的声明处理。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150804.88036016785377702453301612946172:50001231000000:2800:181FA9DF13715A2774578E942FD6689FABAC90E364D2B25FD7F911BAF740A9D3.png?needInitFileName=true?needInitFileName=true)
若开发者后续需要关闭数据采集功能，请在File > Settings（macOS为DevEco Studio > Preferences）> Appearance & Behavior > System Settings > Data Sharing设置界面，取消勾选Send usage statistics关闭数据采集开关。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150804.62918950427290149268324655312150:50001231000000:2800:5BFB37AC6FE537CE623B95195F0B0B93644927A6096A7CD29F11244BBDE1D292.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-log-postback-V14
爬取时间: 2025-04-30 21:16:20
来源: Huawei Developer
若开发过程中遇到DevEco Studio卡顿、卡死或其他故障时，可点击IDE Error问题弹窗中Send Report，点击OK后向DevEco Studio回传日志信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150804.22843521527713268660279386010163:50001231000000:2800:4547EF9305863D333E2D2B0346675466F52CC05B5C4C5E38FEC4771C84B03562.png?needInitFileName=true?needInitFileName=true)
或通过菜单栏Help > Collect Logs and Diagnostic Data，选择并上传相关日志，帮助DevEco Studio提升稳定性体验。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150804.79611729977998933579781763608063:50001231000000:2800:F6894F9463B774463115BD5ACF05AE573665036B363080EF85FB05312426AF83.png?needInitFileName=true?needInitFileName=true)
若开发者后续需要关闭数据采集功能，请在File > Settings（macOS为DevEco Studio > Preferences）> Appearance & Behavior > System Settings > Data Sharing设置界面，取消勾选Send usage statistics关闭数据采集开关。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150804.78331283087330114094252401184315:50001231000000:2800:044C5830C93A6ED5357D7C0E992669E1A0CB32E226AE169FAD544506B820155F.png?needInitFileName=true?needInitFileName=true)

