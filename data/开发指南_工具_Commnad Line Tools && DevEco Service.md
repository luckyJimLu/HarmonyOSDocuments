# 合并文件
合并时间: 2025-05-01 07:31:54

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-commandline-get-V14
爬取时间: 2025-04-30 21:24:51
来源: Huawei Developer
该命令行工具集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、三方库的包管理ohpm、命令行解析hstack、编译构建hvigorw。
命令行工具获取
请前往下载中心获取命令行工具Command Line Tools，并根据下载中心页面工具完整性指导进行完整性校验。
HarmonyOS SDK已嵌入命令行工具中，无需额外下载配置。
配置环境变量
Windows
将解压后command-line-tools文件夹的bin目录配置到系统或者用户的PATH变量中。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.03897237065912744959400437341402:50001231000000:2800:5C3582B37C177350BD655590BDB79B2B6A3B2F4876FA5D947EC062F2148B11A0.png?needInitFileName=true?needInitFileName=true)
macOS/Linux
下载配置完成即可使用相关命令行工具能力。如需验证是否配置成功，可以使用相关命令验证，例如执行codelinter -v指令，检查是否可以正确获取codelinter工具版本。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-command-line-codelinter-V14
爬取时间: 2025-04-30 21:25:25
来源: Huawei Developer
codelinter同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。
codelinter命令行格式为：
options：可选配置，请参考表1。
dir：待检查的工程根目录；为可选参数，如不指定，默认为当前上下文目录。
| 指令  | 说明  |
| --- | --- |
| --config/-c <filepath>  | 指定执行codelinter检查的规则配置文件，<filepath>指定执行检查的规则配置文件位置。  |
| --fix  | 设置codelinter检查同时执行QuickFix。  |
| --format/-f  | 设置检查结果的输出格式。目前支持default/json/xml/html四种格式；不指定时，默认是default格式（文本格式）。  |
| --output/-o <filepath>  | 指定检查结果保存位置，且命令行窗口不展示检查结果。<filepath>指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会显示在命令行窗口中。  |
| --version/-v  | 查看codelinter版本。  |
| --product/-p <productName>  | 指定当前生效的product。 <productName> 为生效的product名称。  |
| --incremental/-i  | 对Git工程中的增量文件（包含新增/修改/重命名的文件）执行Code Linter检查。  |
| --help/-h  | 查询codelinter命令行帮助。  |
指令
说明
--config/-c<filepath>
指定执行codelinter检查的规则配置文件，<filepath>指定执行检查的规则配置文件位置。
--fix
设置codelinter检查同时执行QuickFix。
--format/-f
设置检查结果的输出格式。目前支持default/json/xml/html四种格式；不指定时，默认是default格式（文本格式）。
--output/-o<filepath>
指定检查结果保存位置，且命令行窗口不展示检查结果。<filepath>指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会显示在命令行窗口中。
--version/-v
查看codelinter版本。
--product/-p<productName>
指定当前生效的product。 <productName> 为生效的product名称。
--incremental/-i
对Git工程中的增量文件（包含新增/修改/重命名的文件）执行Code Linter检查。
--help/-h
查询codelinter命令行帮助。
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.08832503041866122538410923714417:50001231000000:2800:C79BB4C5631326FDD97B9DA7EBD759FE3A59D4BA7D38A4616AB7B5E508C30050.png?needInitFileName=true?needInitFileName=true)
-
-
-
-
-
-
-
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.47280382993366407827558907134029:50001231000000:2800:3EDE2774E22F9DEDCA08534B7C1A508F427A4B9C785F7E47D0CF983ACA12DBD6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.11348529931446880189046983084940:50001231000000:2800:6C1C1B32EC875D5083E880727BA806EB62E2C80B182DF0486299A6729BC12E72.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.60850222597133534103183666676904:50001231000000:2800:3544BB88E93A8311768F83CC5AC2C4E58C160108D1D2F6E8B3197E84BA3B6590.png?needInitFileName=true?needInitFileName=true)
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.26212639141393479408111493576758:50001231000000:2800:1C41B8BB3685AC2417A2D1D4B33CA889F98D196EB59F5490067681886118409C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.10932837051078684741626913186927:50001231000000:2800:B0934781520129835121F48E01238D76BCD563719E1FDB316BE91B5BE142E71F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.71821807248946005390513097006649:50001231000000:2800:48078D80F465D75E068B4E8A10BB7A6999B0F201B281D8426C4E8E3F85DDD967.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.54006618416216577073171122595679:50001231000000:2800:76FAE7A0133B15D5E8A70718EDB3B5B9431B7C0D9D4A3D12FA33E3088FE1B587.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-command-line-hstack-V14
爬取时间: 2025-04-30 21:26:01
来源: Huawei Developer
简介
hstack是DevEco Studio为开发人员提供的用于将release应用混淆后的crash堆栈还原为源码对应堆栈的工具，支持Windows、Mac、Linux三个平台。
hstack命令行格式为:
options: 可选配置，请参考表hstack命令行配置。
| 指令 | 说明 |
| --- | --- |
| -i/--input | 可选，指定工程crash文件归档目录。 |
| -c/--crash | 可选，指定一条crash堆栈。 |
| -o/--output | 可选，指定解析结果输出目录（输入指定为-c时， -o参数指定一个输出文件）。 |
| -s/--sourcemapDir | 可选，指定工程sourcemap文件归档目录。 |
| --so/--soDir | 可选，指定工程shared object文件归档目录。 |
| -n/--nameObfuscation | 可选 ，指定工程nameCache文件归档目录。 |
| -v/--version | 查看hstack版本。 |
| -h/--help | 查询hstack命令行帮助。 |
指令
说明
-i/--input
可选，指定工程crash文件归档目录。
-c/--crash
可选，指定一条crash堆栈。
-o/--output
可选，指定解析结果输出目录（输入指定为-c时， -o参数指定一个输出文件）。
-s/--sourcemapDir
可选，指定工程sourcemap文件归档目录。
--so/--soDir
可选，指定工程shared object文件归档目录。
-n/--nameObfuscation
可选 ，指定工程nameCache文件归档目录。
-v/--version
查看hstack版本。
-h/--help
查询hstack命令行帮助。
环境配置
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.86580355993558084657770909456856:50001231000000:2800:93F68B8FA1FC9F84B6572109CA719353E737A847F7E6208E0851952BAED6A987.png?needInitFileName=true?needInitFileName=true)
使用示例
1.
2.
3.
4.
5.  解析完成后，outputDir目录下会生成对应的解析结果，文件以原始crash文件名加“_”前缀进行命名。crash堆栈中的C++日志以及ArkTS日志均已解析为源码对应的文件路径以及行列号，结果如下图所示： 说明：在构建Release应用时，so文件是默认不包含符号表信息的，如果需要在构建Release应用时生成包含符号表的so文件，需要在工程的模块级build-profile.json5文件的buildOption属性中，配置如下信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.35159744624991841080010014182381:50001231000000:2800:7F7EBFF8EE6BD8B40060D658963D829F9AD47566898191187F168458B43F9D91.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.85961887006283308169574297092929:50001231000000:2800:83BA6A2FBD831E451312061EA2EA67F8ECDED376AB5B84A59B05743377304BE2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.63512790123696573187549357935232:50001231000000:2800:E7F450C5498301A73D9E6F36353C3FD7FD7991E9CA012FB9C70C5742E0E659E7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.21728542900479788737642765165664:50001231000000:2800:FF26474DB1E4F518471A61E67E228C67EA07989C13ACAE47B81F84056B2BA987.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.58299428304281731077170604450963:50001231000000:2800:7E7AED8613426198FA658E32A93E0D2AC8C5466CF0B565972F470CCD9A955749.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.35402942788682256453185170365402:50001231000000:2800:1568DA6F1CC4DF163FB4C57AEE5D2CAA8319D619242827F89A530653CB8EE117.png?needInitFileName=true?needInitFileName=true)
堆栈解析方案说明
以如下代码为例。
Entry模块通过独立har包形式引用har模块中的har方法：
```typescript
import {har} from 'Har'
@Entry
@Component
struct Index {
@State har: string = 'Har';
build() {
Row() {
Column() {
Text(this.har)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
let entryClass = new EntryClass();
entryClass.callHarFunction();
})
}
.width('100%')
}
.height('100%')
}
}
class EntryClass {
callHarFunction() {
har()
}
}
```
生成的crash如下：
crash中，包含混淆后的方法名（或属性名）、路径信息以及混淆后的行列号信息，其中：
在对堆栈进行还原时，可分为以下三步：
1.  根据路径信息entry|har|1.0.0|src/main/ets/components/mainpage/MainPage.js，可在entry模块sourcemap文件中找到如下字段：
2.  基于步骤1找到的sourcemap信息，根据sources及mappings字段进行解析，可以将路径以及行列号还原如下： 该文件位于entry模块oh_modules路径下。 如果对应sourcemap中包含package-info字段，则可以利用package-info中对应模块的sourcemap，对该条堆栈进行二次解析。例如该堆栈中包package-info为har|1.0.0，可利用har中的sourcemap对该堆栈进行再次解析，方案如下：
3.  以第二条堆栈为例： 通过步骤1与步骤2，将该堆栈路径以及行列号信息进行解析，结果如下： 在对应模块编译产物中的nameCache文件中，通过解析后的文件路径找到如下字段： 该字段的IdentifierCache与MemberMethodCache中保存了方法名混淆前后的映射关系，对应格式为： "源码方法名:该方法起始行号:该方法结束行号":"混淆后方法名"。 第二条堆栈混淆后的方法名为"i"，利用上述字段对该方法名进行还原： 通过上述方式，可以得到源码的方法名。
```json
"callHarFunction:24:26": "i"
```
4.
```json
"callHarFunction:24:26": "i"
```
通过上述方式，即可利用编译产物对release应用的crash信息进行解析还原。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-commandline-V14
爬取时间: 2025-04-30 21:26:35
来源: Huawei Developer
Hvigor通过hvigorw工具，实现命令行交互。
配置环境变量
1.  在系统或者用户的PATH变量中，添加hvigorw的路径：${COMMANDLINE_TOOL_DIR}/command-line-tools/bin，其中COMMANDLINE_TOOL_DIR是命令行工具的安装路径。
2.  在系统或者用户的PATH变量中，添加hvigorw的路径：${COMMANDLINE_TOOL_DIR}/command-line-tools/bin，其中COMMANDLINE_TOOL_DIR是命令行工具的安装路径。
3.
-  在系统或者用户的PATH变量中，添加hvigorw的路径：${COMMANDLINE_TOOL_DIR}/command-line-tools/bin，其中COMMANDLINE_TOOL_DIR是命令行工具的安装路径。
命令行使用方式
hvigorw命令行格式为：
其中taskNames是任务，可同时执行多个任务，options是可选参数，具体的任务和可选参数请参考常用命令。
hvigorw命令需要在工程根目录下执行。
常用命令
常见的任务和参数如下，更多任务请参考任务详细说明。
查询
| 参数 | 说明 |
| --- | --- |
| -h, --help | 打印Hvigor的命令帮助信息。 |
| -v, --version | 打印Hvigor版本信息。 |
参数
说明
-h, --help
打印Hvigor的命令帮助信息。
-v, --version
打印Hvigor版本信息。
编译构建
| 任务 | 说明 |
| --- | --- |
| clean | 清理构建产物build目录。 |
| collectCoverage | 基于打点数据生成覆盖率统计报表。 |
| assembleHap | 构建Hap应用。 |
| assembleApp | 构建App应用。 |
| assembleHsp | 构建Hsp包。 |
| assembleHar | 构建Har包。 |
任务
说明
clean
清理构建产物build目录。
collectCoverage
基于打点数据生成覆盖率统计报表。
assembleHap
构建Hap应用。
assembleApp
构建App应用。
assembleHsp
构建Hsp包。
assembleHar
构建Har包。
编译构建命令行常用扩展参数：
| 参数 | 说明 |
| --- | --- |
| -p buildMode={debug | release} | 采用debug/release模式进行编译构建。 缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。 关于构建模式的详细说明，请参考指定构建模式。针对HAR构建，请参考构建HAR。 |
| -p debuggable=true/false | 该配置会覆盖构建模式中对应的buildOption中的debuggable配置。 关于debuggable的合并优先级，请参考合并编译选项规则。 |
| -p product={ProductName} | 指定product进行编译, 编译product下配置的module target。 缺省时：默认为default。 |
| -p module={ModuleName}@{TargetName} | 指定模块及target进行编译，可指定多个相同类型的模块进行编译以逗号分割；TargetName不指定时默认为default。 限制：此参数需要与--mode module参数搭配使用。 缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。 |
| -p ohos-test-coverage={true | false} | 执行测试框架代码覆盖率插桩编译。  |
| -p coverage={true | false} |
| -p parameterFile=param.json/json5 | 设置oh-package.json5文件的参数配置文件，其中"param"可自行修改为对应配置文件名称。详细使用请参考parameterFile。 |
参数
说明
-p buildMode={debug | release}
采用debug/release模式进行编译构建。
缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。
关于构建模式的详细说明，请参考指定构建模式。针对HAR构建，请参考构建HAR。
-p debuggable=true/false
该配置会覆盖构建模式中对应的buildOption中的debuggable配置。
关于debuggable的合并优先级，请参考合并编译选项规则。
-p product={ProductName}
指定product进行编译, 编译product下配置的module target。
缺省时：默认为default。
-p module={ModuleName}@{TargetName}
指定模块及target进行编译，可指定多个相同类型的模块进行编译以逗号分割；TargetName不指定时默认为default。
限制：此参数需要与--mode module参数搭配使用。
缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。
-p ohos-test-coverage={true | false}
执行测试框架代码覆盖率插桩编译。
-p coverage={true | false}
-p parameterFile=param.json/json5
设置oh-package.json5文件的参数配置文件，其中"param"可自行修改为对应配置文件名称。详细使用请参考parameterFile。
测试相关的命令行：
| 命令行 | 说明 |
| --- | --- |
| hvigorw onDeviceTest -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName} |  说明 从Hvigor 4.3.0版本开始支持。  通过命令行方式执行Instrument Test。  module：执行测试的模块，缺省默认是执行所有模块的用例。HAP/HAR/HSP模块都支持。 coverage：是否需要覆盖率报告，缺省默认为true。 scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。  多个module和scope之间用逗号分割。  覆盖率测试结果文件：<module-path>/.test/default/outputs/ohosTest/reports 测试结果文件：path_to_project/module_name/.test/default/intermediates/ohosTest/coverage_data/test_result.txt  |
| hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName} | 通过命令行方式执行Local Test。  module：执行测试的模块，缺省默认是执行所有模块的用例。HAP/HAR/HSP模块都支持。 coverage：是否需要覆盖率报告，缺省默认为true。 scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。  多个module和scope之间用逗号分割。  覆盖率测试结果文件：<module-path>/.test/default/outputs/test/reports 测试结果文件：path_to_project/module_name/.test/default/intermediates/test/coverage_data/test_result.txt  |
命令行
说明
hvigorw onDeviceTest -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}
从Hvigor 4.3.0版本开始支持。
通过命令行方式执行Instrument Test。
多个module和scope之间用逗号分割。
-  <module-path>/.test/default/outputs/ohosTest/reports
hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}
通过命令行方式执行Local Test。
多个module和scope之间用逗号分割。
-  <module-path>/.test/default/outputs/test/reports
日志
| 参数 | 说明 |
| --- | --- |
| -e, --error | 设置hvigor的日志级别为error。 |
| -w, --warn | 设置Hvigor的日志级别为warn。 |
| -i, --info | 设置Hvigor的日志级别为info。 |
| -d, --debug | 设置Hvigor的日志级别为debug。 |
| --stacktrace，--no-stacktrace | Hvigor默认使能关闭打印所有异常的堆栈信息，如需开启在命令行后添加该选项。 |
参数
说明
-e, --error
设置hvigor的日志级别为error。
-w, --warn
设置Hvigor的日志级别为warn。
-i, --info
设置Hvigor的日志级别为info。
-d, --debug
设置Hvigor的日志级别为debug。
--stacktrace，--no-stacktrace
Hvigor默认使能关闭打印所有异常的堆栈信息，如需开启在命令行后添加该选项。
可视化
| 参数 | 说明 |
| --- | --- |
| --analyze=normal | 在DevEco Studio中开启Build Analyzer构建分析，设置为普通模式，通过简单打点数据进行分析。 |
| --config properties.hvigor.analyzeHtml=true | 在工程的.hvigor/report目录下生成构建可视化html文件，该文件可直接在浏览器中打开。 |
| --analyze=false | 不启用Build Analyzer构建分析。 |
| --analyze=advanced | 启用Build Analyzer构建分析，并设置为进阶模式，通过更加详细的打点数据进行分析。如果需要更详细的任务耗时数据，请选择该模式。 |
| --analyze | 同--analyze=normal命令。 从Hvigor 4.3.0开始废弃，请使用--analyze=normal替换。 |
| --no-analyze | 同--analyze=false命令。 从Hvigor 4.3.0开始废弃，请使用--analyze=false替换。 |
| --verbose-analyze | 同--analyze=advanced命令。 从hvigor 4.3.0开始废弃，请使用--analyze=advanced替换。 |
参数
说明
--analyze=normal
在DevEco Studio中开启Build Analyzer构建分析，设置为普通模式，通过简单打点数据进行分析。
--config properties.hvigor.analyzeHtml=true
在工程的.hvigor/report目录下生成构建可视化html文件，该文件可直接在浏览器中打开。
--analyze=false
不启用Build Analyzer构建分析。
--analyze=advanced
启用Build Analyzer构建分析，并设置为进阶模式，通过更加详细的打点数据进行分析。如果需要更详细的任务耗时数据，请选择该模式。
--analyze
同--analyze=normal命令。
从Hvigor 4.3.0开始废弃，请使用--analyze=normal替换。
--no-analyze
同--analyze=false命令。
从Hvigor 4.3.0开始废弃，请使用--analyze=false替换。
--verbose-analyze
同--analyze=advanced命令。
从hvigor 4.3.0开始废弃，请使用--analyze=advanced替换。
daemon
| 参数 | 说明 |
| --- | --- |
| --daemon | 使能daemon。 |
| --no-daemon | Hvigor默认使能daemon，如需关闭，可在命令行后添加该选项。 命令行模式下推荐使用此参数。 |
| --stop-daemon | 关闭当前工程的daemon进程。 |
| --stop-daemon-all | 关闭所有工程的daemon进程。 |
| --status-daemon | 查询当前环境中所有的Hvigor daemon进程信息。 |
| --max-old-space-size=12345 | 设置daemon进程老生代内存大小为12345MB。 |
参数
说明
--daemon
使能daemon。
--no-daemon
Hvigor默认使能daemon，如需关闭，可在命令行后添加该选项。
命令行模式下推荐使用此参数。
--stop-daemon
关闭当前工程的daemon进程。
--stop-daemon-all
关闭所有工程的daemon进程。
--status-daemon
查询当前环境中所有的Hvigor daemon进程信息。
--max-old-space-size=12345
设置daemon进程老生代内存大小为12345MB。
性能
| 参数 | 说明 |
| --- | --- |
| --parallel, --no-parallel | Hvigor默认使能并行编译能力，如需关闭在命令行后添加该选项。 |
| --incremental, --no-incremental | Hvigor默认使能增量编译能力，如需关闭在命令行后添加该选项。 |
参数
说明
--parallel, --no-parallel
Hvigor默认使能并行编译能力，如需关闭在命令行后添加该选项。
--incremental, --no-incremental
Hvigor默认使能增量编译能力，如需关闭在命令行后添加该选项。
公共命令
| 任务 | 说明 |
| --- | --- |
| tasks | 打印工程各模块包含的任务信息。 |
| taskTree | 打印工程各模块的任务依赖关系信息。 |
| version | 打印Hvigor的相关版本信息。 |
| prune | 清除30天内未使用的Hvigor缓存文件并从pnpm存储中删除未引用的包。 |
任务
说明
tasks
打印工程各模块包含的任务信息。
taskTree
打印工程各模块的任务依赖关系信息。
version
打印Hvigor的相关版本信息。
prune
清除30天内未使用的Hvigor缓存文件并从pnpm存储中删除未引用的包。
其他命令
| 参数 | 说明 |
| --- | --- |
| -s,--sync | 处理并持久化Hvigor部分工程信息到工程./hvigor/outputs/sync/output.json中。 |
| -m,--mode | 在对应的目录执行相应的task，例hvigorw clean -m project在工程目录下执行build目录清理（即清理工程级别的build文件夹）。 |
| --enable-build-script-type-check | 使能工程中hvigorfile.ts的类型检查，该字段已废弃，请使用--type-check替换。 |
| --type-check, --no-type-check | Hvigor默认使能关闭工程中hvigorfile.ts的类型检查，如需开启，可在命令行后添加该选项。 |
| --no-pnpm-frozen-lockfile，--pnpm-frozen-lockfile | Hvigor默认使能不忽略pnpm-lock.yaml文件，如需开启，可在命令行后添加该选项。 忽略pnpm-lock.yaml文件，按照hvigor-config.json5的配置安装Hvigor插件的依赖（如果不忽略pnpm-lock.yaml文件，在使用Hvigor 2.0.0及以上版本的CI场景下安装Hvigor插件依赖时将报错）。 说明 该命令在4.1 Release及以上版本中已废弃。在CI场景中将自动配置，无需开发者手动配置。  |
| --config, -c | 指定hvigor-config.json5配置文件中的参数。 当前仅支持设置properties里的参数，具体支持的参数请查看hvigor-config.json5中properties支持的参数。 --config properties.key=value 同 -c properties.key=value |
| --watch | 使能观察模式，主要用于预览和热加载场景。 |
| --generate-build-profile, --no-generate-build-profile | 已废弃。使能生成BuildProfile.ets文件。 |
| --node-home <string> | 指定nodejs路径。 |
参数
说明
-s,--sync
处理并持久化Hvigor部分工程信息到工程./hvigor/outputs/sync/output.json中。
-m,--mode
在对应的目录执行相应的task，例hvigorw clean -m project在工程目录下执行build目录清理（即清理工程级别的build文件夹）。
--enable-build-script-type-check
使能工程中hvigorfile.ts的类型检查，该字段已废弃，请使用--type-check替换。
--type-check, --no-type-check
Hvigor默认使能关闭工程中hvigorfile.ts的类型检查，如需开启，可在命令行后添加该选项。
--no-pnpm-frozen-lockfile，--pnpm-frozen-lockfile
Hvigor默认使能不忽略pnpm-lock.yaml文件，如需开启，可在命令行后添加该选项。
忽略pnpm-lock.yaml文件，按照hvigor-config.json5的配置安装Hvigor插件的依赖（如果不忽略pnpm-lock.yaml文件，在使用Hvigor 2.0.0及以上版本的CI场景下安装Hvigor插件依赖时将报错）。
该命令在4.1 Release及以上版本中已废弃。在CI场景中将自动配置，无需开发者手动配置。
--config, -c
指定hvigor-config.json5配置文件中的参数。
当前仅支持设置properties里的参数，具体支持的参数请查看hvigor-config.json5中properties支持的参数。
--config properties.key=value 同 -c properties.key=value
--watch
使能观察模式，主要用于预览和热加载场景。
--generate-build-profile, --no-generate-build-profile
已废弃。使能生成BuildProfile.ets文件。
--node-home <string>
指定nodejs路径。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-cli-V14
爬取时间: 2025-04-30 21:27:09
来源: Huawei Developer
ohpm作为OpenHarmony三方库的包管理工具，支持OpenHarmony共享包的发布、安装和依赖管理。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-system-platform-V14
爬取时间: 2025-04-30 21:27:46
来源: Huawei Developer
ohpm支持在Windows、MacOS、Linux操作系统下使用。
ohpm通过软链接或符号链接的方式构建依赖关系。不同操作系统需满足如下要求：
Windows：
MacOS：
工程代码文件所在文件系统类型需为APFS（macOS系统下默认为APFS）。
如在macOS上挂载了其他不支持符号链接的文件系统（如FAT32或exFAT），则无法在其上创建符号链接。
Linux：
EXT4、Btrfs、XFS、ZFS等常见Linux文件系统类型均满足要求。
部分较老或简单的文件系统（不支持符号链接），可能存在无法在其上创建或正确解析软链接的情况。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpmrc-V14
爬取时间: 2025-04-30 21:28:22
来源: Huawei Developer
ohpm配置文件。
描述
ohpm从命令行和.ohpmrc文件中获取其配置设置。ohpm config命令可用于修改用户级.ohpmrc文件的内容。
文件
注释
.ohpmrc 文件中以 # 或 ; 字符为注释符。
更新配置
执行如下命令可设置用户级配置：
默认配置项
| 配置项  | 字段名称  | 字段说明  | 字段类型  | 默认值  | 备注  |
| --- | --- | --- | --- | --- | --- |
| 仓库设置  | registry  | 下载仓库  | 字符串  | https://ohpm.openharmony.cn/ohpm/  | 可以配置多个仓库地址，以英文逗号间隔，多个仓库地址的优先级按照配置顺序排序。  |
| @group:registry  | 指定仓库  | 字符串  | ""  | 根据group指定组织的仓库地址。支持多个仓库地址，以英文逗号间隔，且优先级大于registry配置，多个仓库地址的优先级按照配置顺序排序。  |
| 发布设置  | publish_registry  | 发布仓库  | 字符串  | https://ohpm.openharmony.cn/ohpm/  | 配置发布的仓库地址，仅支持配置一个仓库地址。  |
| publish_id  | 用户发布号  | 字符串  | ""  | 用户发布号，用来发布三方库，全局唯一。  |
| 路径设置  | cache  | 缓存路径  | 字符串  | ~/.ohpm/cache  | -  |
| key_path  | 私钥路径  | 字符串  | ""  | 利用ssh-keygen工具生成的私钥的放置路径地址。  |
| 网络设置   | no_proxy  | 不使用proxy代理  | 字符串  | ""  | 配置不使用代理的仓库地址，可配置多个，以英文逗号间隔；值可以是域名或者ip，支持二级域名通配符*（例如：*.huawei.com）。  |
| http_proxy  | http代理  | 字符串  | ""  | 支持用户名和密码的网络代理，特殊字符需要转义。示例：http://proxy_server:port。  |
| https_proxy  | https代理  | 字符串  | ""  | 支持用户名和密码的网络代理，特殊字符需要转义。示例：https://proxy_server:port。  |
| strict_ssl  | ssl校验  | 布尔  | true  | 默认值为true，校验https证书；若配置为false，则不校验https证书。  |
| ca_files  | ca证书路径  | 字符串  | ""  | strict_ssl=true时校验服务端证书需要的ca证书放置路径，可以放置多个证书路径，以英文逗号间隔。详情请见：CA证书获取及配置。  |
| fetch_timeout  | 请求超时时间  | 数值  | 60000  | 取值范围：[10000，360000]，单位为毫秒。如果设置的fetch_timeout值不在取值范围内，则默认为：60000。  |
| 并发设置    | max_concurrent  | 最大并发量  | 数值  | 50  | 取值范围：[1, 200]，设置每个模块在安装时允许的最大并发量。  |
| retry_times  | 出错重试次数  | 数值  | 1  | 取值范围：[0, 5], 针对白名单内的异常，程序会按配置重试指定次数，白名单有： ECONNRESET：连接被对端重置ECONNREFUSED：连接被服务器拒绝ETIMEDOUT：连接超时RESPONSETIMEOUT：响应超时TARBADARCHIVE：包格式异常  |
| retry_interval  | 出错重试间隔时间  | 数值  | 1000  | 取值范围：[1000, 60000], 单位毫秒。  |
| 依赖冲突设置   | resolve_conflict  | 开启自动解决依赖版本冲突功能  | 布尔  | true  | 默认开启。当设置为true或缺省时，ohpm会自动处理依赖版本冲突，详情请见：resolve_conflict。  |
| resolve_conflict_strict  | 开启严格模式依赖冲突处理功能  | 布尔  | false  | 默认关闭。当设置为true时，ohpm会按照严格模式处理依赖版本冲突，详情请见：resolve_conflict_strict。  |
| 其他设置             | log_level  | 日志级别  | 字符串  | info  | 可设置日志输出级别，对应级别类型有debug、info、warn、error。  |
| install_all  | 是否安装工程所有模块的依赖  | 布尔  | true  | 默认为true。当设置为true或缺省时，在执行ohpm install、ohpm update、ohpm uninstall时，将会安装工程下所有模块的依赖。详情请见install_all。  |
| :_auth和:_read_auth  | AccessToken配置项  | 字符串  | 无  | ohpm-repo支持使用access token进行认证。详情请见AccessToken。  |
| enforce_dependency_key  | 开启依赖名称校验  | 布尔  | false  | 默认为false。设置为true后，ohpm会校验配置的本地依赖名称与其对应的包名是否一致，若不一致会导致命令执行失败。详情请见enforce_dependency_key。  |
| ensure_dependency_include  | 开启依赖扫描功能  | 布尔  | false  | 默认为false。从ohpm 1.7.0开始，在执行ohpm publish命令时，会检查发布包的源码中，静态导入的三方依赖是否都声明在oh-package.json5的dependencies或dynamicDependencies中。若缺少依赖声明且字段设置为false时，会提示相应告警信息；设置为true时，则会使命令执行失败并提示错误信息。  |
| projectPackageJson:<project_root>  | 工程oh-package.json5配置覆盖  | 字符串  | 无  | 用于覆盖工程根目录下oh-package.json5中的配置。 配置项名称中的<project_root>表示工程根目录路径（根据实际情况替换为真实的工程根目录路径）。配置项的值为指定的工程级oh-package.json5文件的路径，支持使用相对路径（当使用相对路径时，根路径为<project_root>）。  |
| disallow_nested_package  | 开启包内.har/.tgz依赖 配置路径检测  | 布尔  | false  | 默认为false。设置为true后，在执行prepublish/publish时，会扫描包内是否存在'./'形式配置且后缀为.har/.tgz格式的依赖，如果存在，则会使命令执行失败并提示报错信息。  |
| odm_r2_project_root  | 开启overrideDependencyMap中相对路径自动转换功能  | 布尔  | false  | 默认为false。设置为true后，当存在overrideDependencyMap配置且其配置项对应的配置文件内存在相对路径的依赖配置时，ohpm会基于工程根路径解析来查找这些相对路径。详情见odm_r2_project_root。  |
| enable_cross_process_lock  | 启用跨进程锁  | 布尔  | true  | 默认为true。由于oh_modules目录结构限制，ohpm不支持在同一个工程下并行运行多个ohpm install、ohpm update或ohpm uninstall命令，若需要在同一个工程下执行多个ohpm install、ohpm update或ohpm uninstall命令，则必须将该配置设置为true，以保证这多个命令以串行的方式运行。  |
| compability_log_level  | 兼容性字段检测日志等级  | 字符串  | warn  | 默认为warn。在执行prepublish、publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（'compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'），如果未配置，则会根据日志等级打印提示或报错。详情请见compability_log_level。  |
| use_stream_threshold_size  | 流式上传阈值  | 数值  | 5  | 取值范围：[0, 300]，单位mb。当publish三方库的文件体积大于此阈值时将会使用流式上传三方库，如果仓库不存在流式上传接口则自动转为Base64方式上传。  |
| lockfile_stable_order  | oh-package-lock.json5内容稳定排序  | 布尔  | false  | 默认为false。若设置为true，会确保在oh-package.json5文件未变更时，当前已生成的oh-package-lock.json5各字段内容不变。  |
配置项
字段名称
字段说明
字段类型
默认值
备注
仓库设置
registry
下载仓库
字符串
https://ohpm.openharmony.cn/ohpm/
可以配置多个仓库地址，以英文逗号间隔，多个仓库地址的优先级按照配置顺序排序。
@group:registry
指定仓库
字符串
""
根据group指定组织的仓库地址。支持多个仓库地址，以英文逗号间隔，且优先级大于registry配置，多个仓库地址的优先级按照配置顺序排序。
发布设置
publish_registry
发布仓库
字符串
https://ohpm.openharmony.cn/ohpm/
配置发布的仓库地址，仅支持配置一个仓库地址。
publish_id
用户发布号
字符串
""
用户发布号，用来发布三方库，全局唯一。
路径设置
cache
缓存路径
字符串
~/.ohpm/cache
-
key_path
私钥路径
字符串
""
利用ssh-keygen工具生成的私钥的放置路径地址。
网络设置
no_proxy
不使用proxy代理
字符串
""
配置不使用代理的仓库地址，可配置多个，以英文逗号间隔；值可以是域名或者ip，支持二级域名通配符*（例如：*.huawei.com）。
http_proxy
http代理
字符串
""
支持用户名和密码的网络代理，特殊字符需要转义。示例：http://proxy_server:port。
https_proxy
https代理
字符串
""
支持用户名和密码的网络代理，特殊字符需要转义。示例：https://proxy_server:port。
strict_ssl
ssl校验
布尔
true
默认值为true，校验https证书；若配置为false，则不校验https证书。
ca_files
ca证书路径
字符串
""
strict_ssl=true时校验服务端证书需要的ca证书放置路径，可以放置多个证书路径，以英文逗号间隔。详情请见：CA证书获取及配置。
fetch_timeout
请求超时时间
数值
60000
取值范围：[10000，360000]，单位为毫秒。如果设置的fetch_timeout值不在取值范围内，则默认为：60000。
并发设置
max_concurrent
最大并发量
数值
50
取值范围：[1, 200]，设置每个模块在安装时允许的最大并发量。
retry_times
出错重试次数
数值
1
取值范围：[0, 5], 针对白名单内的异常，程序会按配置重试指定次数，白名单有：
retry_interval
出错重试间隔时间
数值
1000
取值范围：[1000, 60000], 单位毫秒。
依赖冲突设置
resolve_conflict
开启自动解决依赖版本冲突功能
布尔
true
默认开启。当设置为true或缺省时，ohpm会自动处理依赖版本冲突，详情请见：resolve_conflict。
resolve_conflict_strict
开启严格模式依赖冲突处理功能
布尔
false
默认关闭。当设置为true时，ohpm会按照严格模式处理依赖版本冲突，详情请见：resolve_conflict_strict。
其他设置
log_level
日志级别
字符串
info
可设置日志输出级别，对应级别类型有debug、info、warn、error。
install_all
是否安装工程所有模块的依赖
布尔
true
默认为true。当设置为true或缺省时，在执行ohpm install、ohpm update、ohpm uninstall时，将会安装工程下所有模块的依赖。详情请见install_all。
:_auth和:_read_auth
AccessToken配置项
字符串
无
ohpm-repo支持使用access token进行认证。详情请见AccessToken。
enforce_dependency_key
开启依赖名称校验
布尔
false
默认为false。设置为true后，ohpm会校验配置的本地依赖名称与其对应的包名是否一致，若不一致会导致命令执行失败。详情请见enforce_dependency_key。
ensure_dependency_include
开启依赖扫描功能
布尔
false
默认为false。从ohpm 1.7.0开始，在执行ohpm publish命令时，会检查发布包的源码中，静态导入的三方依赖是否都声明在oh-package.json5的dependencies或dynamicDependencies中。若缺少依赖声明且字段设置为false时，会提示相应告警信息；设置为true时，则会使命令执行失败并提示错误信息。
projectPackageJson:<project_root>
工程oh-package.json5配置覆盖
字符串
无
用于覆盖工程根目录下oh-package.json5中的配置。
disallow_nested_package
开启包内.har/.tgz依赖
配置路径检测
布尔
false
默认为false。设置为true后，在执行prepublish/publish时，会扫描包内是否存在'./'形式配置且后缀为.har/.tgz格式的依赖，如果存在，则会使命令执行失败并提示报错信息。
odm_r2_project_root
开启overrideDependencyMap中相对路径自动转换功能
布尔
false
默认为false。设置为true后，当存在overrideDependencyMap配置且其配置项对应的配置文件内存在相对路径的依赖配置时，ohpm会基于工程根路径解析来查找这些相对路径。详情见odm_r2_project_root。
enable_cross_process_lock
启用跨进程锁
布尔
true
默认为true。由于oh_modules目录结构限制，ohpm不支持在同一个工程下并行运行多个ohpm install、ohpm update或ohpm uninstall命令，若需要在同一个工程下执行多个ohpm install、ohpm update或ohpm uninstall命令，则必须将该配置设置为true，以保证这多个命令以串行的方式运行。
compability_log_level
兼容性字段检测日志等级
字符串
warn
默认为warn。在执行prepublish、publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（'compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'），如果未配置，则会根据日志等级打印提示或报错。详情请见compability_log_level。
use_stream_threshold_size
流式上传阈值
数值
5
取值范围：[0, 300]，单位mb。当publish三方库的文件体积大于此阈值时将会使用流式上传三方库，如果仓库不存在流式上传接口则自动转为Base64方式上传。
lockfile_stable_order
oh-package-lock.json5内容稳定排序
布尔
false
默认为false。若设置为true，会确保在oh-package.json5文件未变更时，当前已生成的oh-package-lock.json5各字段内容不变。
CA证书获取及配置
依次访问以下证书下载地址，并根据下图操作下载CA证书到本地：
下载证书，请选择保存类型为证书链。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.39503732399691329491857889772216:50001231000000:2800:57C22032676FA0D9A37C38759A80DDFAF11823094720F0C39556AB3FBFF983EA.png?needInitFileName=true?needInitFileName=true)
在 .ohpmrc 文件中配置 ca_files=证书路径1,证书路径2。
install_all
在ohpm客户端1.8.0版本的.ohpmrc中支持install_all配置，用于控制ohpm install，ohpm update，ohpm uninstall的行为，install_all在.ohpmrc文件中设置为true或缺省时：
resolve_conflict
ohpm客户端在1.5.0版本开始支持依赖版本冲突自动解决功能。只需要在.ohpmrc文件中，将resolve_conflict配置为true或缺省，即可开启该功能。依赖冲突的处理策略为：当您的项目同时依赖了某个三方库的不同版本时，ohpm将选择其中的最高版本进行安装。
若某个三方库同时存在远程版本和本地版本（本地文件或源码依赖），无论本地版本的版本号是否大于远程版本，ohpm的冲突处理策略都会优先选择本地版本作为待安装的版本。
模块内依赖版本冲突
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.23399581997713055543018743232675:50001231000000:2800:4087D74F80EABAD0A1B5D2C0A1F0D1976E6214DFFDB382DAD16E4ED6120C2C3A.png?needInitFileName=true?needInitFileName=true)
如上图所示的依赖路径中，moduleA 为您正在开发的模块，其直接依赖为 B@1.1，C@1.1。其中 B@1.1 与 C@1.1 分别依赖了 D 的两个版本 D@1.2 与 D@1.3。当您开启了依赖版本冲突自动解决功能，ohpm将会选择 D@1.3 版本作为待安装的版本，最终依赖路径被解析为下图蓝色箭头所指向的路径：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.62288294913191637948860261491474:50001231000000:2800:CE941F3D56DB97633A69B6DFD4F85F06D6B5552B5214924487A393ECCB2EBB2C.png?needInitFileName=true?needInitFileName=true)
模块间依赖版本冲突
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.36616600117908356595932442942471:50001231000000:2800:1386FA0B4A35BF3AA08CECE69E920B3E20FF7CD81D542D6BDEE2A22ADF178B4B.png?needInitFileName=true?needInitFileName=true)
如上图所示的依赖路径中，moduleA、moduleB 为您同一项目下正在开发的两个模块，其中moduleA 依赖 B@1.1，moduleB 依赖 C@1.1，B@1.1 与 C@1.1 分别依赖了 D 的两个版本 D@1.2 与 D@1.3。当您开启了依赖版本冲突自动解决功能，并且您是使用 ohpm install --all 进行安装时，ohpm将会选择 D@1.3 版本作为待安装的版本，最终依赖路径被解析为下图蓝色箭头所指向的路径：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.38907324226778806365863207928595:50001231000000:2800:F8F4D7D35ACAFDE64672E8F766E0F2962AC7498FA1B55D9A97F406EA0B20B3D1.png?needInitFileName=true?needInitFileName=true)
更新依赖版本的场景
当您希望将您某个模块的直接依赖更新成另一个版本，如下图所示，您手动将 C@1.1 更新为 C@1.2：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.40841347715195521782869725450644:50001231000000:2800:2904A0BDB97C8E8E43BF54503571A91A7CCD2F480376DBBE6DB1BDE31A0C0FB0.png?needInitFileName=true?needInitFileName=true)
由于 C 更新为 C@1.2 后，不再依赖 D，若依赖 D 的版本在更新 C 版本之前已经通过 ohpm 的自动冲突处理机制锁定为 D@1.3 版本，此时 C 版本的升级将不会导致 D 的版本由 D@1.3 回退为 D@1.2，这样可以保证每一次更新都只是在上一次结果上进行影响最小的修改，最终的依赖路径将会被解析为下图蓝色箭头所指向的路径：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.00330146323944925993377823004153:50001231000000:2800:07B9EB4290967D63F9AEC81241C976D43F61C1760D36263F7A25B8D940FB5942.png?needInitFileName=true?needInitFileName=true)
对于上述场景，如果希望D版本同时也回退至D@1.2版本，则需要在ohpm install之前执行ohpm clean命令清理各模块下的oh-package-lock.json5文件，以消除上一次安装结果的影响。
ohpm install命令带--target_path选项时依赖冲突处理
target_path下是hvigor在构建时根据目标产物target为各模块自动生成定制的依赖配置文件（oh-package.json5），详见target_path。在生成的oh-package.json5中，依赖的版本部分可能包含targetName，示例："A": "1.0.0+targetName"。
包含targetName信息的版本完整格式为：<major>.<minor>.<patch>[-<pre-release>][+<targetName>]，此时冲突处理规则如下：
1、<major>.<minor>.<patch>[-<pre-release>]部分的比较规则依然遵循上文各场景所描述的处理规则，即取版本号最大的依赖。
2、当两个版本<major>.<minor>.<patch>[-<pre-release>]部分一致时，取尾部有[+<targetName>]信息的依赖。
1、当两个版本尾部均有[+<targetName>]信息，且targetName不一致时，会根据<target_path>/dependencyMap.json5中targetName是否为空进行区分处理。
2、当两个依赖中有一个是本地依赖时，优先取本地依赖；当两个依赖均是本地依赖时，获取本地依赖包内oh-package.json5配置的version再次按照上述规则继续比较。
限制条件说明
由于本功能尚在Beta阶段，存在如下的限制条件：
1.  如难以感知本地文件或本地源码依赖中的版本号，建议使用overrides来处理冲突。
resolve_conflict_strict
ohpm客户端从5.0.9版本，开始支持严格的依赖版本冲突处理机制。在.ohpmrc文件中，将resolve_conflict_strict配置为true开启该功能。
严格模式下，当您的项目同时依赖了某个三方库的不同版本时，ohpm将按照严格模式冲突决策算法决策出最符合要求的版本进行安装，当程序不能决策出符合要求的版本时将报错。
严格模式冲突决策算法
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.82190217079035881688765368416984:50001231000000:2800:1DBE86EC7B3A1D10B9490A927EECC768F8E22A31FA43E7FA85A4F21601B03811.png?needInitFileName=true?needInitFileName=true)
AccessToken
AccessToken是 ohpm-repo 2.1.0版本新引入的认证机制，用户通过ohpm-repo界面生成Token，并将其配置至ohpm客户端配置文件中。
在与 ohpm-repo 交互时，客户端会自动附带Token进行身份验证。该Token分两种权限等级：
每位用户每种权限类型的Token最多可生成10个，首次生成时系统自动复制到剪贴板，后续不再显示完整Token内容。
如何获取AccessToken
当前AccessToken仅 ohpm-repo 支持，在 ohpm-repo 的个人中心->认证管理->AccessToken页面进行生成。
如何配置AccessToken
配置示例如下所示:
其中 ：
enforce_dependency_key
ohpm从1.7.0版本开始，支持在.ohpmrc文件中支持配置enforce_dependency_key，该配置项值为布尔类型，默认为false。将配置设置为true后，ohpm会校验各模块的oh-package.json5中配置的直接依赖中的本地依赖名称与其对应的包名(模块名)是否一致，若不一致会导致依赖安装失败并在错误日志中打印出不一致的依赖名称与其对应的包名(模块名)。
示例：
在MyApplication工程下存在一个名称为foo的模块，foo模块的oh-package.json5如下所示：
在MyApplication工程下存在另一个名称为bar的模块，且bar模块中依赖了foo模块，bar模块的oh-package.json5如下所示：
如上所示，bar模块的oh-package.json5中配置了对foo模块的依赖，并为foo模块起了一个别名为fee。当在.ohpmrc中将enforce_dependency_key配置为true时：
此时在MyApplication下执行ohpm install --all命令将打印如下错误日志，同时会中断命令的执行：
若没有配置enforce_dependency_key或将其配置为false时，命令将不会被中断，同时上述错误日志的日志级别将会下调为告警日志：
建议在.ohpmrc文件中配置enforce_dependency_key为true，禁止以别名的方式配置本地依赖，避免出现如下场景：
基于上述示例，在MyApplication下真的存在一个名称为fee的模块，且该模块的版本号小于foo模块，fee模块的oh-package.json5如下所示：
且entry模块中同时依赖了fee与bar，entry模块的oh-package.json5依赖配置如下所示：
此时在entry的依赖树中，依赖fee存在两个版本：一个别名为fee的foo模块，一个名称为fee的fee模块，若此时开启了resolve_conflict，由于fee模块的实际版本号为1.0.0要小于foo模块的版本号2.0.0，在执行ohpm install时将只会在entry模块的oh_modules下安装以fee为别名的foo模块，而实际的fee模块则不会被安装，如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.79834924381791074128717981219902:50001231000000:2800:8C54AAF7119864880C90AE3A653662B9D07A41DCA1A8B3B66D3486C814B5DCF3.png?needInitFileName=true?needInitFileName=true)
在entry的oh_modules下会生成一个名称为fee的软连接，该链接却指向foo模块的实际路径：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.74901351748841382256587243242980:50001231000000:2800:D9FAB97EBBE6139FB0B670865A7205F7578C998AC8F07768E9E12EFC1CC286D8.png?needInitFileName=true?needInitFileName=true)
如果entry实际希望依赖的是真实的fee模块而不是foo模块，则此时会导致entry无法编译成功。
1、从ohpm客户端5.0.7开始，若项目级build-profile.json5文件中strictMode字段下配置了useNormalizedOHMUrl开关且useNormalizedOHMUrl=true，则该配置优先级高于enforce_dependency_key，如果ohpm检测到依赖别名与oh-package.json5中name不一致时，会报错提示并中止程序执行；若未配置useNormalizedOHMUrl或useNormalizedOHMUrl=false时，是否校验别名一致性则根据enforce_dependency_key配置决定。
2、项目级build-profile.json5文件中，products节点下任意product字段配置了useNormalizedOHMUrl=true，则ohpm中useNormalizedOHMUrl开关会被设置为true，即ohpm检测到项目中依赖别名与oh-package.json5中name不一致时，会报错提示并中止程序执行。
odm_r2_project_root
odm_r2_project_root是ohpm客户端1.8.0新增的开关配置，默认为false，可以通过config命令或直接在.ohpmrc文件中修改其值。
当该配置为true时，若在overrideDependencyMap中配置的依赖项替换文件中存在以相对路径配置的本地依赖项时，在ohpm运行时会基于工程根路径来查找这些本地依赖项。
示例：
如上第3步所示，当odm_r2_project_root开关设置为true时，在ohpm运行时会以工程根目录为起点查找"./test.har"，比如：工程根路径为：D:\path\to\MyProject，在ohpm运行时解析得到test.har的绝对路径为：D:\path\to\MyProject\test.har。
compability_log_level
ohpm客户端从5.0.1开始新增开关配置'compability_log_level'字段，用于控制在缺少兼容性检测需要的字段时ohpm的处理逻辑。
compability_log_level字段默认赋值为'warn'，可配置的日志等级请见开关配置项说明。
在执行prepublish、publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'），详见模块级oh-package.json5字段说明，下面统称 '兼容性字段'，如果未配置，则会根据日志等级打印提示或报错。
开关配置项说明

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-oh-package-json5-V14
爬取时间: 2025-04-30 21:28:55
来源: Huawei Developer
从OHPM 5.0.0版本开始，支持区分工程级与模块级oh-package.json5配置。其中：
开发者可将标准的DevEco Studio工程下的各个模块打成HAR包后，发布到OpenHarmony三方库中心仓；所有发布到仓库的包必须包含模块级oh-package.json5文件，以描述当前包基本信息。
工程级oh-package.json5 字段说明
| 配置项 | 字段名称 | 字段说明 | 字段要求 | 字段类型 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 开发态版本 | modelVersion | 开发态版本号 | 必选 | 字符串 | 无 | 开发态版本号。 |
| 描述配置 | description | 简介 | 可选 | 字符串 | 无 | 用于描述工程信息的字符串。 |
| 依赖配置     | dependencies | 生产依赖 | 可选 | 对象 | {} | 用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（不建议在工程级oh-package.json5中配置生产依赖）。 |
| devDependencies | 开发依赖 | 可选 | 对象 | {} | 配置开发态依赖，配置只能参与项目的开发或测试阶段的依赖。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（如手机）上使用，则不能在其中配置。 |
| dynamicDependencies | 动态依赖 | 可选 | 对象 | {} | 配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用（不建议在工程级oh-package.json5中配置动态依赖）。 |
| overrides | 依赖覆盖配置 | 可选 | 对象 | {} | 支持将依赖树中的包替换为另一个指定版本，详情见overrides。 |
| overrideDependencyMap | 重写依赖关系 | 可选 | 对象 | {} | 支持将依赖树中包的子依赖替换为配置文件中配置的依赖，详情见overrideDependencyMap。 |
| 其他 | scripts | 自定义脚本 | 可选 | 对象 | {} | 维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。 |
| hooks | 钩子 | 可选 | 对象 | {} | 安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。 |
| parameterFile | 参数化配置文件路径 | 可选 | 字符串 | 无 | 标识是否开启参数化。未配置：关闭参数化；已配置：开启参数化。需同时指定参数化配置文件路径，详见parameterFile。 |
配置项
字段名称
字段说明
字段要求
字段类型
默认值
备注
开发态版本
modelVersion
开发态版本号
必选
字符串
无
开发态版本号。
描述配置
description
简介
可选
字符串
无
用于描述工程信息的字符串。
依赖配置
dependencies
生产依赖
可选
对象
{}
用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（不建议在工程级oh-package.json5中配置生产依赖）。
devDependencies
开发依赖
可选
对象
{}
配置开发态依赖，配置只能参与项目的开发或测试阶段的依赖。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（如手机）上使用，则不能在其中配置。
dynamicDependencies
动态依赖
可选
对象
{}
配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用（不建议在工程级oh-package.json5中配置动态依赖）。
overrides
依赖覆盖配置
可选
对象
{}
支持将依赖树中的包替换为另一个指定版本，详情见overrides。
overrideDependencyMap
重写依赖关系
可选
对象
{}
支持将依赖树中包的子依赖替换为配置文件中配置的依赖，详情见overrideDependencyMap。
其他
scripts
自定义脚本
可选
对象
{}
维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。
hooks
钩子
可选
对象
{}
安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。
parameterFile
参数化配置文件路径
可选
字符串
无
标识是否开启参数化。未配置：关闭参数化；已配置：开启参数化。需同时指定参数化配置文件路径，详见parameterFile。
不建议在工程级依赖中配置非devDependencies的依赖，即一个Hsp/Har模块的非开发态依赖都要在相应模块的dependencies和dynamicDependencies中声明。
模块级oh-package.json5字段说明
| 配置项 | 字段名称 | 字段说明 | 字段要求 | 字段类型 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 描述配置        | name | 名称 | 必选 | 字符串 | 无 | 格式为：@group/packagename或packagename，长度：[1, 128]，全局唯一，即一个应用中，不同package的package name不能重名。建议name命名时包含组织名称group，便于管理和识别三方库。 name中只有在存在组织名称group时，才能有且仅能有一个'@'符号，有且仅有一个路径分隔符'/'。 组织名称group格式： 1、仅允许以小写字母开头，可由小写字母、数字、中划线(-)、下划线(_)组成。 2、禁止以中划线（-）、下划线（_）结尾。 3、不允许为ArkTS 的保留关键字。 packagename格式： 1、仅允许以小写字母开头，可由小写字母、数字、点（.）、中划线（-）、下划线（_）组成。 2、禁止以点（.）、中划线（-）、下划线（_）结尾。 3、不允许为ArkTS的保留关键字。 |
| version | 版本号 | 必选 | 字符串 | 1.0.0 | 必须遵循 semver 语义化规范，从1.0.0开始。 |
| description | 简介 | 可选 | 字符串 | 无 | 用于描述三方库信息的字符串，有助于被搜索发现。 |
| keywords | 关键字 | 可选 | 数组 | [] | 关键字信息数组，便于搜索使用。例如：["tools", "project"]。 |
| author | 作者 | 可选 | 对象或字符串 | 无 | 包含 name 字段（可选）和 email 字段（可选），例如："author": {"name": "xxx" , "email": "xxx@xxx.com" }。或者直接为作者名称，例如："author": "xxx"。 name字段允许使用字母、数字，点（.），中划线（-），下划线（_），空格，中文。其中首字母必须为英文字母。 |
| homepage | 主页链接 | 可选 | 字符串 | "" | 通常是项目gitee链接。 |
| repository | 仓库地址 | 可选 | 字符串 | "" | 开源代码仓库地址。在私仓管理界面的系统设置处可定义是否为必填。 |
| license | 开源协议 | 必选 | 字符串 | "ISC" | 当前项目的开源许可证。遵循 spdx license 规范。许可证若为 GPL，repository 建议不为空。 |
| 依赖配置    | dependencies | 生产依赖 | 可选 | 对象 | {} | 用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（参与编译/运行阶段使用的依赖）。 |
| devDependencies | 开发依赖 | 可选 | 对象 | {} | 用于配置开发态依赖，只能参与项目的开发或测试阶段。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（手机）上使用，则不能在其中配置。 |
| dynamicDependencies | 动态依赖 | 可选 | 对象 | {} | 用于配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用。 |
| 文件配置  | main | 入口 | 必选 | 字符串 | 无 | 指定加载的入口文件。 |
| types | 类型定义 | 可选 | 字符串 | "" | 指定类型定义的文件名。当用 typescript 定义新的类型，需要提供给其他开发者使用，则需要指定其声明文件，一般为 .d.ts，.d.ets 文件。 |
| 兼容性检测相关配置    | compatibleSdkVersion | SDK版本 | 可选 | 字符串 | 无 | 三方库开发者使用的SDK版本，构建时由Hvigor自动填充，提供给SDK做兼容性检测。 在prepublish、publish时，ohpm会对该字段进行检测(非空和长度校验)，并根据.ohpmrc中开关 compability_log_level配置的值进行提示或报错处理。 配置示例参看兼容性字段配置示例。 |
| compatibleSdkType | SDK类型 | 可选 | 字符串 | 无 | 三方库开发者使用的SDK类型，构建时由Hvigor自动填充，提供给SDK做兼容性检测, 示例值："OpenHarmony"、"HarmonyOS"。 在prepublish、publish时，ohpm会对该字段进行检测(非空和长度校验)，并根据.ohpmrc中开关 compability_log_level配置的值进行提示或报错处理。 配置示例参看兼容性字段配置示例。 |
| obfuscated | 混淆标识 | 可选 | 布尔 | 无 | 三方库是否开启混淆标识，构建时由Hvigor自动填充，提供给SDK做兼容性检测。 在prepublish、publish时，ohpm会对该字段进行检测(非空校验)，并根据.ohpmrc中开关 compability_log_level配置的值进行提示或报错处理。 配置示例参看兼容性字段配置示例。 |
| nativeComponents | native so依赖配置 | 可选 | 数组 | 无 | 三方库使用的so包配置，构建时由Hvigor自动填充，提供给SDK做兼容性检测。 对于用户自行引入的so依赖(存放于libs目录)，需要用户手动维护该数组，数组单个元素类型为对象，对象内可配置的字段有：name、compatibleSdkVersion、compatibleSdkType。 在prepublish、publish时，如果包内存在so包，则ohpm会对该字段进行检测，并根据.ohpmrc中开关 compability_log_level 配置的值进行提示或报错处理；反之则不检测该字段。 配置示例参看兼容性字段配置示例。 |
| 其他       | artifactType | 类型 | 可选 | 字符串 | "original" | OpenHarmony包制品类型，有两个选项：original、obfuscation。original：源码，即发布源码(.ts/.ets)；obfuscation：混淆代码，即源码经过混淆之后发布上传。 |
| scripts | 自定义脚本 | 可选 | 对象 | {} | 维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。 |
| hooks | 钩子 | 可选 | 对象 | {} | 安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。 |
| category | 检查规则白名单 | 可选 | 字符串 | {} | 在私仓管理界面配置后自动生成，白名单为分号隔开的字符串列表，每个列表项必须是一个由大小写字母或下划线组成的字符串，包含在白名单中的配置项，不再做规则检查。 |
| packageType | 包类型 | 可选 | 字符串 | InterfaceHar | 标识模块是否为HSP包，在新建Shared Library时会自动生成该字段，并默认赋值为"InterfaceHar"；Static Library中没有该字段，标识为普通HAR包。 |
配置项
字段名称
字段说明
字段要求
字段类型
默认值
备注
描述配置
name
名称
必选
字符串
无
格式为：@group/packagename或packagename，长度：[1, 128]，全局唯一，即一个应用中，不同package的package name不能重名。建议name命名时包含组织名称group，便于管理和识别三方库。
name中只有在存在组织名称group时，才能有且仅能有一个'@'符号，有且仅有一个路径分隔符'/'。
组织名称group格式：
1、仅允许以小写字母开头，可由小写字母、数字、中划线(-)、下划线(_)组成。
2、禁止以中划线（-）、下划线（_）结尾。
3、不允许为ArkTS 的保留关键字。
packagename格式：
1、仅允许以小写字母开头，可由小写字母、数字、点（.）、中划线（-）、下划线（_）组成。
2、禁止以点（.）、中划线（-）、下划线（_）结尾。
3、不允许为ArkTS的保留关键字。
version
版本号
必选
字符串
1.0.0
必须遵循semver语义化规范，从1.0.0开始。
description
简介
可选
字符串
无
用于描述三方库信息的字符串，有助于被搜索发现。
keywords
关键字
可选
数组
[]
关键字信息数组，便于搜索使用。例如：["tools", "project"]。
author
作者
可选
对象或字符串
无
包含 name 字段（可选）和 email 字段（可选），例如："author": {"name": "xxx" , "email": "xxx@xxx.com" }。或者直接为作者名称，例如："author": "xxx"。
name字段允许使用字母、数字，点（.），中划线（-），下划线（_），空格，中文。其中首字母必须为英文字母。
homepage
主页链接
可选
字符串
""
通常是项目gitee链接。
repository
仓库地址
可选
字符串
""
开源代码仓库地址。在私仓管理界面的系统设置处可定义是否为必填。
license
开源协议
必选
字符串
"ISC"
当前项目的开源许可证。遵循spdx license规范。许可证若为 GPL，repository 建议不为空。
依赖配置
dependencies
生产依赖
可选
对象
{}
用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（参与编译/运行阶段使用的依赖）。
devDependencies
开发依赖
可选
对象
{}
用于配置开发态依赖，只能参与项目的开发或测试阶段。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（手机）上使用，则不能在其中配置。
dynamicDependencies
动态依赖
可选
对象
{}
用于配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用。
文件配置
main
入口
必选
字符串
无
指定加载的入口文件。
types
类型定义
可选
字符串
""
指定类型定义的文件名。当用 typescript 定义新的类型，需要提供给其他开发者使用，则需要指定其声明文件，一般为 .d.ts，.d.ets 文件。
兼容性检测相关配置
compatibleSdkVersion
SDK版本
可选
字符串
无
三方库开发者使用的SDK版本，构建时由Hvigor自动填充，提供给SDK做兼容性检测。
在prepublish、publish时，ohpm会对该字段进行检测(非空和长度校验)，并根据.ohpmrc中开关compability_log_level配置的值进行提示或报错处理。
配置示例参看兼容性字段配置示例。
compatibleSdkType
SDK类型
可选
字符串
无
三方库开发者使用的SDK类型，构建时由Hvigor自动填充，提供给SDK做兼容性检测, 示例值："OpenHarmony"、"HarmonyOS"。
在prepublish、publish时，ohpm会对该字段进行检测(非空和长度校验)，并根据.ohpmrc中开关compability_log_level配置的值进行提示或报错处理。
配置示例参看兼容性字段配置示例。
obfuscated
混淆标识
可选
布尔
无
三方库是否开启混淆标识，构建时由Hvigor自动填充，提供给SDK做兼容性检测。
在prepublish、publish时，ohpm会对该字段进行检测(非空校验)，并根据.ohpmrc中开关compability_log_level配置的值进行提示或报错处理。
配置示例参看兼容性字段配置示例。
nativeComponents
native so依赖配置
可选
数组
无
三方库使用的so包配置，构建时由Hvigor自动填充，提供给SDK做兼容性检测。
对于用户自行引入的so依赖(存放于libs目录)，需要用户手动维护该数组，数组单个元素类型为对象，对象内可配置的字段有：name、compatibleSdkVersion、compatibleSdkType。
在prepublish、publish时，如果包内存在so包，则ohpm会对该字段进行检测，并根据.ohpmrc中开关compability_log_level配置的值进行提示或报错处理；反之则不检测该字段。
配置示例参看兼容性字段配置示例。
其他
artifactType
类型
可选
字符串
"original"
OpenHarmony包制品类型，有两个选项：original、obfuscation。original：源码，即发布源码(.ts/.ets)；obfuscation：混淆代码，即源码经过混淆之后发布上传。
scripts
自定义脚本
可选
对象
{}
维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。
hooks
钩子
可选
对象
{}
安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。
category
检查规则白名单
可选
字符串
{}
在私仓管理界面配置后自动生成，白名单为分号隔开的字符串列表，每个列表项必须是一个由大小写字母或下划线组成的字符串，包含在白名单中的配置项，不再做规则检查。
packageType
包类型
可选
字符串
InterfaceHar
标识模块是否为HSP包，在新建Shared Library时会自动生成该字段，并默认赋值为"InterfaceHar"；Static Library中没有该字段，标识为普通HAR包。
依赖名使用要求：
1、在oh-package.json5文件中dependencies、devDependencies、dynamicDependencies节点声明本地依赖时，允许配置的依赖名和依赖包的包名（即包内oh-package.json5中配置的name）不一致，但不推荐该用法，在默认情况下ohpm会通过告警日志来提示此类问题。
若希望将告警升级为报错并中断命令执行，可以通过在.ohpmrc中配置enforce_dependency_key=true；或在项目级build-profile.json5文件中将strictMode字段下配置useNormalizedOHMUrl=true。
2、使用参数化配置时，依赖名和依赖包的包名（即包内oh-package.json5中配置的name）必须保持一致，否则会报错并中断命令执行。
3、在oh-package.json5、overrideDependencyMap、parameterFile文件中，不建议使用无效的转义字符（例如：\a、\e、\o等）或Unicode编码（例如：\uxxxx）。
兼容性字段配置示例
三方库开发者使用的SDK和当前集成该三方库工程编译时使用的SDK可能存在不一致的情况。因此，ohpm新增了兼容性检测相关配置以帮助SDK做兼容性分析。配置示例如下：
创建一个新的oh-package.json5文件
通过命令行创建 oh-package.json5文件，执行如下命令：
1.  导航到包的目录。
2.  执行初始化命令，并按照问卷填写相关参数。 对无命名空间模块，执行以下命令： 对有命名空间模块，执行以下命令：
3.  对无命名空间模块，执行以下命令：
4.  对有命名空间模块，执行以下命令：
5.  若跳过问卷填写，创建默认文件，可在初始化命令行加上配置参数 --yes。 默认创建的oh-package.json5 文件示例：
-  对无命名空间模块，执行以下命令：
-  对有命名空间模块，执行以下命令：
依赖配置说明
ohpm 存在 dependencies，devDependencies和dynamicDependencies 三种依赖类型。同时支持具体版本号，范围版本号，tag标签，本地har/tgz文件路径和本地源码目录多种方式引入依赖。
```json
{
"dependencies": {
// 具体版本号引入，支持符合semver标准的版本号
"specific_version": "1.0.0",
// 范围版本号引入，^引入1.x.x的最新版本，~引入1.0.x的最新版本。范围版本优先选取正式版本，无匹配的正式版本才会选取先行版本
"scope_version": "^1.0.1",
// tag标签引入，示例引入标签为"beta"对应的版本号
"tag_version": "tag:beta",
// 本地文件引入，可引入本地har/tgz文件
"local_file": "file:./xx.har",
// 本地源码引入，可引入本地其他模块的源码，示例直接引入本地的"module1"模块
"local_source_code": "file:../module1"
},
"devDependencies": {
// 支持依赖引入类型同dependencies
},
"dynamicDependencies": {
// 支持依赖引入类型同 dependencies
}
}
```
overrides
ohpm客户端在1.4.0版本开始支持Override机制，可以在项目级别的oh-package.json5（即项目根目录下的oh-package.json5）文件中添加overrides配置，方便将依赖树中的依赖替换为另一个版本。替换的版本既可以是一个具体的版本号，也可以是一个模糊版本，还可以是本地存在的HAR包或源码目录。
例如，想要确保foo始终安装1.0.0版本，可以在项目级的oh-package.json5中增加如下配置：
overrides必须配置在项目级别的oh-package.json5中，配置在模块级别的oh-package.json5中将不会生效。
```json
{
"overrides": {
"foo": "1.0.0"
}
}
```
若本地存在foo的源码或者HAR包，想确保foo始终使用您本地的版本，可以在项目级的oh-package.json5中如下配置：
```json
{
"overrides": {
// 本地存在"foo"的源码目录，如项目根目录下的foo目录
// "foo": "file:./foo"
// 本地存在"foo"的HAR文件，如项目根目录下的libs目录中的foo.har
"foo": "file:./libs/foo.har"
}
}
```
parameterFile
OHPM新增了参数化配置功能。开发者可在项目根目录配置一个参数化文件（json5格式文件），在该文件中维护模块或依赖版本信息，不同模块将根据该文件中的版本进行配置，满足不同构建场景下，开发者快速切换依赖版本的需要。同时，支持通过命令行指定参数化文件，降低流水线场景下模块和依赖版本的变更难度。
OHPM客户端在1.6.0版本开始支持参数化配置。可以在项目级别的oh-package.json5文件（即项目根目录下的oh-package.json5）中添加parameterFile配置，并同时指定parameterFile文件路径。配置规则如下：
基础配置示例
工程级oh-package.json5示例：
```json
{
"modelVersion": "5.0.2",
"description": "Please describe the project information.",
...
"parameterFile": './parameterFile/parameterFile.json5' // 开启参数化并指定参数化配置文件路径
}
```
模块级oh-package.json5示例：
```json
{
"name": "parameter-test",
"version": "@param:version", //使用时必须以 '@param:' 开头
"description": "test desc.",
"main": "index.ets",
"author": "test author",
"license": "ISC",
"dependencies": {
"libtest1": "@param:dependencies.libtest1"
},
"devDependencies": {
"libtest2": "@param:devDependencies.libtest2"
},
"dynamicDependencies": {
"libtest3": "@param:dynamicDependencies.libtest3"
},
}
```
parameterFile所指向文件的配置示例：
```json
{
"version": "1.0.0",
"dependencies": {
"libtest1": "1.0.1"
},
"devDependencies": {
"libtest2": "*"
},
"dynamicDependencies": {
"libtest3": "latest"
}
}
```
一仓多包示例
一个代码仓有多个har/hsp模块，发包时，一般需要开发者手动修改所有模块的版本号后再打包发布，若模块较多，操作繁琐且效率低下，建议使用参数化配置解决该问题，详细示例如下。
当所有模块版本不一致：
如下工程结构所示，所有模块的oh-package.json5中version字段均配置参数化版本（'@param:'开头部分），不同模块的版本均不一致，但都由参数化配置文件'parameter.json'全局统一管理；发包前，只需修改'parameter.json'文件中相关模块的版本，再构建所有模块即可；打包构建时，所有模块的参数化版本均会被替换为'parameter.json'中配置的具体版本（如：@param:har1会被替换为：1.0.0）。
当所有模块版本一致：
如下工程结构所示，所有模块均使用同一个参数化版本（@param:module_version），发包前，只需修改'parameter.json'中module_version的值, 再构建所有模块即可；打包构建时，所有模块的参数化版本均会被替换为'parameter.json'中module_version对应的版本（如：@param:module_version会被替换为：1.0.0）。
overrideDependencyMap
OHPM客户端在1.7.0版本开始支持使用overrideDependencyMap机制重写源码模块或三方库的依赖关系。开发者可在工程级oh-package.json5文件中新增overrideDependencyMap配置，在该配置对象中通过key-value形式配置依赖关系重写文件；其中，key为依赖标识符，value为依赖关系重写文件路径。在依赖安装时， ohpm会将依赖树中的某个依赖节点的所有直接子依赖替换为对应依赖关系重写文件中配置的依赖项，依赖关系重写文件中支持配置的依赖类型为dependencies、devDependencies、dynamicDependencies，通过使用overrideDependencyMap机制，可以满足开发者在不同场景下，动态变更依赖的需求。
同时，支持在.ohpmrc中使用projectPackageJson配置项来覆盖项目根目录下oh-package.json5中的配置，方便开发者快速切换配置，详情见ohpmrc中projectPackageJson配置。
配置说明
-  "[@group/]libname[@version]" : "config_path"，其中 [@group/]libname[@version] 为依赖标识符key, config_path为配置文件路径value。
overrideDependencyMap场景示例
.ohpmrc中projectPackageJson配置
通过在.ohpmrc文件中配置projectPackageJson，可同时实现对overrides、overrideDependencyMap字段配置的效果，替换项目级oh-package.json5文件中相应的配置，方便开发者在不同使用场景下快速切换使用。配置格式及使用约束如下所示：
-  projectPackageJson:<project_root>=<config_path>, 其中 projectPackageJson:<project_root> 部分视做key, config_path 部分视做value。配置key指定项目根目录路径（绝对路径），配置value指定json5格式配置文件路径用以覆盖项目级oh-package.json5中的配置。
-  projectPackageJson:D:\test\TestProject=projectPackageJson.json5
示例
下面演示在.ohpmrc中配置同一工程的不同环境下的projectPackageJson配置，当配置生效时，会直接覆盖项目级oh-package.json5中对应配置。
oh-package-lock.json5
oh-package-lock.json5用于锁定所有依赖的版本，以及缓存依赖的元数据信息。不建议开发者手动修改该文件的内容，也不建议开发者使用其他分析工具直接读取该文件的内容。
建议将oh-package-lock.json5文件提交到代码仓库中进行版本管理。优点如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-common-commands-V14
爬取时间: 2025-04-30 21:29:29
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-config-V14
爬取时间: 2025-04-30 21:30:03
来源: Huawei Developer
设置ohpm用户级配置项。
命令格式
配置文件中信息以键值对<key> = <value>形式存在。
功能描述
ohpm 从命令行和 .ohpmrc 文件中获取其配置设置。有关更多 .ohpmrc 文件信息和可用配置选项，请参阅ohpmrc章节。
ohpm config 仅支持配置项字段（默认项字段请查阅ohpmrc章节），且仅支持修改用户级目录下的 .ohpmrc 文件。
子命令
set
在用户级目录下 .ohpmrc 文件中，以键值对<key> = <value>形式写入数据。
get
将从命令行，项目级 .ohpmrc 文件，用户级 .ohpmrc 文件（优先级依次递减）中获取的值进行标准输出。
如果未提供键值，则此命令执行效果与命令 ohpm config list 相同。
list
显示所有配置项。
delete
删除用户级目录下 ohpmrc 文件中指定的键值。
Options
json
可以在 config list 命令后面配置 -j或者--json 参数，以 json 格式输出所有配置项及默认值。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-help-V14
爬取时间: 2025-04-30 21:30:40
来源: Huawei Developer
获取有关 ohpm 的帮助。
命令格式
command：命令名称。
功能描述
如果提供了命令名称，则显示相应命令的帮助信息。
如果提供的命令名称不存在或未提供，则显示所有命令的概要信息。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150808.11564569110059783878009117665580:50001231000000:2800:8D11D7373E34D89CDD0B80E4619A020228C5D8AA0CB58279989524F55AF07931.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-info-V14
爬取时间: 2025-04-30 21:31:13
来源: Huawei Developer
查询指定三方库的具体信息。
命令格式
功能描述
用于调用云端查询接口，查看指定包的详细信息，并将结果进行标准输出。
Options
registry
可以在 info 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
fetch_timeout
可以在 info 命令后面配置 -ft <number> 或者 --fetch_timeout <number> 参数，用以设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 info 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验https证书。
上述选项中配置的registry，fetch_timeout和strict_ssl，仅在执行当前info命令时生效，不会修改项目级或者用户级的配置文件。
示例
执行以下命令：
结果示例：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-init-V14
爬取时间: 2025-04-30 21:31:47
来源: Huawei Developer
创建 oh-package.json5 文件。
命令格式
功能描述
在工作目录下，生成一个新的 oh-package.json5 文件，初始化一个 package。
执行命令时，命令行会出现交互界面，可填写一系列关于三方库的基本信息，例如：三方库名称、版本等。ohpm 会根据现有字段、依赖项和所选选项做出合理的猜测，它会保留已设置的任何字段和值，在工作目录下创建一个 oh-package.json5 文件。
Options
yes
可以在 init 命令后面指定 -y或者--yes 参数，命令行将会完全跳过交互界面，创建默认的 oh-package.json5 文件。
默认内容如下：
若当前工作目录下不存在 oh-package.json5 文件，则文件中 name 字段默认为当前工作目录名称；若当前工作目录下已存在 oh-package.json5 文件，则新文件中 name 字段复用已存在文件中的 name 字段，并且最后覆盖原有oh-package.json5文件。
group
可以在 init 命令后面配置 -g <group_name> 或者 --group <group_name>参数，创建一个 oh-package.json5 文件，其中 name 字段的命名空间为 @group_name。
示例
-  当前工作目录下不存在 oh-package.json5 文件。 在" D:\demo " 路径下，执行如下命令： 执行结果为：
-  当前工作目录下已存在其中 name 字段为 demo_name 的 oh-package.json5 文件。 在" D:\demo " 路径下，执行如下命令： 执行结果为：
-  创建一个 oh-package.json5 文件，其中参数 name 字段为 "@group_name/demo" ，而不是仅为 "demo"。 执行结果为：问卷中 name 字段自动显示为 @group_name/demo。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-install-V14
爬取时间: 2025-04-30 21:32:20
来源: Huawei Developer
安装三方库。
命令格式
功能描述
用于安装指定组件或 oh-package.json5 文件中所有的依赖。如果存在 oh-package-lock.json5 文件，安装将取决于 oh-package-lock.json5 文件中锁定的版本。
-  ohpm install 将依赖项安装到本地 oh_modules 文件夹中，并将所有依赖项作为 dependencies，写入 oh-package.json5 文件。
-  ohpm install <folder> 安装本地文件夹，则默认会创建一个软链接指向该文件夹。 示例：
-  ohpm install <har file> 安装压缩包，请注意压缩包的要求： 示例：
Options
all
可以在 install 命令后面配置 --all 参数，安装您项目下所有模块在其 oh-package.json5 中配置的全部依赖项。
save-dynamic
可以在 install 命令后面配置 --save-dynamic 参数，安装的三方库信息将会写入 oh-package.json5 文件的 dynamicDependencies 中。
save-dev
可以在 install 命令后面配置 --save-dev 参数，安装的三方库信息将会写入 oh-package.json5 文件的 devDependencies 中。
save-prod
可以在 install 命令后面配置 --save-prod 参数，安装的三方库信息将会写入 oh-package.json5 文件的 dependencies 中，这是 ohpm 的默认行为。
no-save
可以在 install 命令后面配置 --no-save 参数，安装的三方库信息将不会写入 oh-package.json5 文件中。
prefix
可以在 install 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
parameterFile
可以在 install 命令后面配置 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。
registry
可以在 install 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
fetch_timeout
可以在 install 命令后面配置 -ft <number> 或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 install 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
max_concurrent
可以在 install 命令后面配置 -mc <number> 或者 --max_concurrent <number> 参数，设置最大活动并发请求数（即ohpm操作期间任何时间的最大网络请求数），如果没有指定，默认最大并发请求数为50次。
retry_times
可以在 install 命令后面配置 -rt <number> 或者 --retry_times <number> 参数，设置操作失败前的最大重试次数，如果没有指定，默认最大重试次数为1次。
retry_interval
可以在 install 命令后面配置 -ri <number> 或者 --retry_interval <number> 参数，设置重试失败前的等待时间，如果没有指定，默认等待时间为1000ms。
experimental-concurrently-safe
可以在 install 命令后面配置 --experimental-concurrently-safe 参数，并发安全地安装依赖。这是一个实验性选项。
target_path
可以在 install 命令后面配置 --target_path <string> 参数，用来指定在特定目标产物target语境下各模块的依赖配置文件（oh-package.json5）的路径。在执行ohpm install时，ohpm会优先安装<target_path>/<moduleName>/oh-package.json5文件中依赖。详情参见target_path。
示例
安装 lottie 三方库，执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150808.40240009637737477788125296791867:50001231000000:2800:BA5C7523CEF81A6D25FF068FB964BA98A58B05E12589C2CD4C591F6A8AE70CFA.png?needInitFileName=true?needInitFileName=true)
oh_modules
ohpm 1.0.0~1.3.0
使用 ohpm 安装时，项目中各 Module 的依赖项被统一安装在 Module 根目录下的 oh_modules 目录中，Module 中所有直接依赖和间接依赖都以平铺的方式存储在 oh_modules 目录下的 .ohpm 目录中，Module 的直接依赖则以软链接的方式添加进 oh_modules 文件夹的根目录中。因此，相同依赖项只会安装一次，从而减少磁盘使用空间，加快安装速度。
ohpm 1.4.x
ohpm 客户端从 1.4.0 版本开始，同一项目下所有 Module 的依赖都会被统一安装在项目根目录下的 oh_modules 目录中，同时会在项目各 Module 根目录下的 oh_modules 中生成该 Module 的直接依赖的软连接，这些软连接会指向项目根目录下 oh_modules 中的 .ohpm 目录下依赖实际存储目录。
target_path
为了支持在构建过程中针对不同的产物定制不同的依赖，Hvigor会在构建时根据目标产物target为各模块自动生成定制的依赖配置文件（oh-package.json5），开发者可以在ohpm install时使用target_path选项来指定在特定目标产物target语境下各模块的依赖配置文件（oh-package.json5）的路径。
ohpm会优先安装<target_path>/moduleName/oh-package.json5文件中配置的依赖，并在<project_root>/moduleName下生成对应的oh-package-<targetName>-lock.json5文件。当指定target_path时，默认会开启依赖版本冲突自动处理功能，在依赖安装完成后，ohpm还会根据实际安装的依赖版本在<target_path>/resolve-conflict/moduleName目录下生成新的oh-package.json5文件。
target_path目录结构示例：
dependencyMap.json5内容示例：
ohpm install指定target_path时依赖配置优先级说明：
1、<target_path>/dependencyMap.json5中rootDependency配置的oh-package.json5的优先级高于<project_root>/oh-package.json5。
2、.ohpmrc中projectPackageJson指定的项目级配置文件中overrides、overrideDependencyMap配置优先级同时高于<target_path>/dependencyMap.json5中rootDependency配置的oh-package.json5中对应配置 和 <project_root>/oh-package.json5中对应配置。
3、<target_path>/moduleName/oh-package.json5的优先级高于overrideDependencyMap中的依赖配置文件。
4、overrides中的依赖版本优先级高于<target_path>/moduleName/oh-package.json5中对应的依赖版本。
仅当<target_path>/dependencyMap.json5中targetName的值不为空且不等于'default'时，<project_root>/moduleName目录下生成的lock文件名才会变更为：oh-package-targetName-lock.json5。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-list-V14
爬取时间: 2025-04-30 21:32:54
来源: Huawei Developer
列出已安装的三方库。
命令格式
功能描述
以树形结构列出当前项目安装的所有三方库信息，以及它们的依赖关系。
当指定三方库名称时，会列出指定三方库名称的所有父依赖；当未指定三方库名称时，默认只列出所有的直接依赖，可通过添加选项 depth 来指定要打印的依赖层级。
Options
depth
可以在 list 命令后面配置 -d <number> 或者  --depth <number> 参数，设置输出树形结构的最大深度，超过该深度则不进行输出，不配置则取默认值 0，只展示直接依赖。
json
可以在 list 命令后面配置 -j 或者 --json 参数，以  json 格式输出当前项目安装的所有三方库信息，以及它们的依赖关系。
prefix
可以在 list 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
parameterFile
可以在 list 命令后面配置 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。
示例
-  查看当前项目安装的所有三方库及依赖关系。 执行以下命令： 结果示例：
-  查看当前项目安装的某个三方库的依赖关系 执行以下命令： 结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150808.17498791349849375810520169759787:50001231000000:2800:00E545CAEC231DEFB5DFD94D51B7F9F771B9CFEC9084825FE647307A606B6C78.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.96651776874177988648296590898673:50001231000000:2800:93C8ECCC6BD0DEE0BCE7774CE590A17B27E73DD1906C3CBFA1005A6FFC3F475F.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-publish-V14
爬取时间: 2025-04-30 21:33:28
来源: Huawei Developer
发布一个三方库。
命令格式
功能描述
发布校验规则
三方库校验规则
1.  README.md文件、LICENSE文件和CHANGELOG.md三个文件在该HAR包发布至OpenHarmony 三方库中心仓时必须包含，且不能为空。
开闭源规则
1.  开源 不进行 ArkTS 代码相关编译的，只进行 cpp 代码编译和 OpenHarmony 资源处理，还有模块部分原始配置文件会被打包。其 oh-package.json5 文件中的 "artifactType" 字段值为 original。
2.  闭源 ArkTS 代码会被编译成混淆的 js 和 d.ets 和 d.ts 等声明文件，进行 cpp 代码编译和 OpenHarmony 资源处理，还有模块部分原始配置文件会被打包。其 oh-package.json5 文件中 "artifactType" 属性值为 obfuscation。此时则检查 oh-package.json5 文件中 "types" 属性中定义的声明文件是否带有扩展名 ".d.ts/.d.ets"，且对应路径下存在该文件。若无则进行报错，且不会发布。
Options
publish_id
可以在 publish 命令后面配置 --publish_id <id> 参数，指定发布码。
key_path
可以在 publish 命令后面配置 --key_path <p> 参数，指定ssh私钥路径。
tag
可以在 publish 命令后面配置 -t <tag_name>或者 --tag <tag_name> 参数，给将要发布的三方库打上标签。
publish_registry
可以在 publish 命令后面配置 --publish_registry <r> 参数，指定发布仓库地址。如果未指定，默认从配置中获取发布仓库地址。
fetch_timeout
可以在 publish 命令后面配置 -ft <number>或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 publish 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
示例
发布工作目录下的三方库，执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.11852493312724699943850966142669:50001231000000:2800:FBF72AB36F5C304B8A8298F02DB91B174AE6B1040A5EF3A91E3D7A2279A57339.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-uninstall-V14
爬取时间: 2025-04-30 21:34:02
来源: Huawei Developer
卸载三方库。
命令格式
功能描述
卸载指定已安装的模块，并将 oh-package.json5 文件中 dependencies、devDependencies 属性里移除指定三方库信息；若没有指定三方库，则不做任何动作。
如无需在 oh-package.json5 文件中 dependencies、devDependencies 属性里移除指定三方库信息，则可配置 --no-save 参数。
Options
all
您可以在 uninstall 命令后面配置 --all 参数，表示卸载当前模块指定依赖成功后同时安装当前工程下的所有模块的依赖。
no-save
您可以在 uninstall 命令后面配置 --no-save 参数，卸载的三方库信息不会从 oh-package.json5 文件中删除。
prefix
可以在 uninstall 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
registry
可以在 uninstall 命令后面配置 --registry <registry> 参数，当检测到oh-package.json5文件存在未安装的三方包时，卸载命令执行后，会自动从registry指定的仓库中下载并安装该三方包；如果没有指定，默认从配置中获取仓库地址。
fetch_timeout
可以在 uninstall 命令后面配置 -ft <number> 或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 uninstall 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
experimental-concurrently-safe
可以在 uninstall 命令后面配置 --experimental-concurrently-safe 参数，并发安全地安装依赖。这是一个实验性选项。
示例
从当前工程下卸载直接依赖的某个package。
执行以下命令：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-prepublish-V14
爬取时间: 2025-04-30 21:34:36
来源: Huawei Developer
预发布一个三方库。
命令格式
功能描述
Options
无。
示例
预发布工作目录下的三方库，执行以下命令：
结果示例：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-unpublish-V14
爬取时间: 2025-04-30 21:35:09
来源: Huawei Developer
下架已发布的三方库。
命令格式
功能描述
Options
force
强制下架。
publish_registry
可以在 unpublish 命令后面配置 --publish_registry <r> 参数，指定发布仓库地址。如果未指定，默认从配置中获取发布仓库地址。
publish_id
可以在 unpublish 命令后面配置 --publish_id <id> 参数，指定发布码。
key_path
可以在 unpublish 命令后面配置 --key_path <p> 参数，指定ssh私钥路径。
fetch_timeout
可以在 install 命令后面配置 -ft, --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 unpublish 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
示例
下架已发布的三方库，执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.75761013005635923839173109285802:50001231000000:2800:74F57E8B218A19A02B8F5D1AAFCBED462689D42C2034743E45F1D7660D7AFD6F.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-update-V14
爬取时间: 2025-04-30 21:35:43
来源: Huawei Developer
更新三方库。
命令格式
功能描述
根据三方库及其依赖版本号的semver规范，将本地安装的三方库更新到最新版本。若未指定三方库名称，则全量更新当前工程的依赖，且会安装缺少的三方库。
Options
all
您可以在 update 命令后面配置 --all 参数，表示更新当前模块指定依赖成功后同时安装当前工程下的所有模块的依赖。
prefix
可以在 update 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
fetch_timeout
可以在 update 命令后面配置 -ft <number>或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为 60000 ms。
max_concurrent
可以在 update 命令后面配置 -mc <number> 或者 --max_concurrent <number> 参数，设置最大活动并发请求数（即 ohpm 操作期间任何时间的最大网络请求数），如果没有指定，默认最大并发请求数为 50 次。
retry_times
可以在 update 命令后面配置 -rt <number> 或者 --retry_times <number> 参数，设置操作失败前的最大重试次数，如果没有指定，默认最大重试次数为 1 次。
retry_interval
可以在 update 命令后面配置 -ri <number> 或者 --retry_interval <number> 参数，设置重试失败前的等待时间，如果没有指定，默认等待时间为 1000 ms。
strict_ssl
可以在 update 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
registry
可以在 update 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
all-modules
可以在 update 命令后面配置 --all-modules 参数，表示同步更新所有模块的依赖关系。
tag-filter
可以在 update 命令后面配置 --tag-filter <regex> 参数，表示更新以tag为规范，只更新tag符合正则表达式的依赖。使用 --tag-filter 参数默认更新所有模块的依赖关系。
experimental-concurrently-safe
可以在 update 命令后面配置 --experimental-concurrently-safe 参数，并发安全地安装依赖。这是一个实验性选项。
示例
若当前三方库是 APP，且它的依赖项为：dep1 ( dep2, ...)，dep1 已发布的版本有：
^ 依赖项
使用^符号会更新到版本 x.y.z 中 y 和 z 的最新版本。如果 APP 中 oh-package.json5 文件中 dep1 的版本号为：
ohpm update 则安装 dep1@1.2.2，因为最新版本指向 1.2.2，且1.2.2 满足 ^1.1.1。
~ 依赖项
使用~符号会更新到版本 x.y.z 中 z 的最新版本。如果 APP 中 oh-package.json5 文件中 dep1 的版本号为：
ohpm update 则安装 dep1@1.1.2，尽管最新版本指向 1.2.2，但 1.2.2 不满足 ~1.1.1（版本号须 1.1.1 ≤ version < 1.2.0），所以 ~1.1.1 使用满足最高排序版本，即1.1.2 ，进行更新。
tag 依赖项
使用 tag 会更新到 tag 对应的版本。如果 APP 中 oh-package.json5 文件中 dep1 的版本号为：
如果此时 release 标签对应版本被变更为 1.2.2，ohpm update --tag-filter ^r 则会将 dep1@1.2.0 更新为 dep1@1.2.2，因为 dep1 是通过 release 标签引入，release 符合 --tag-filter 指定的 ^r 正则表达式，所以会重新获取 release 标签对应的版本 1.2.2。
低于 1.0.0 版本的 ^ 依赖项
-  如果 APP 中 dep1 依赖版本号低于 1.0.0 且带有 ^，例如： ohpm update 则安装 dep1@0.2.0，因为没有其他版本满足 ^0.2.0。
-  但是 dep1 依赖版本号是 ^0.4.0： ohpm update 则安装  dep1@0.4.1，因为它是满足 ^0.4.0（版本号须 0.4.0 ≤ version < 0.5.0）的最高排序版本。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-root-V14
爬取时间: 2025-04-30 21:36:17
来源: Huawei Developer
在标准输出中打印有效的 oh_modules 目录路径信息。
命令格式
功能描述
可以在模块的任意子目录下执行，用于打印命令工作路径下所在包的有效 oh_modules 目录路径信息。
Options
prefix
可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh_modules 目录路径信息。
示例
项目结构为：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.01446337137642905558116097574776:50001231000000:2800:13ED0007D0C2B8E61E349917D55A570D6C0ADE2A208278926C66EB4F3C836A32.png?needInitFileName=true?needInitFileName=true)
在entry模块的src目录下执行：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.76939989076239814079939480149988:50001231000000:2800:A115C1028843AF7AA4546DF38BB2295F9620B5E50D13BE58EAE0F0532C19262B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-version-V14
爬取时间: 2025-04-30 21:36:52
来源: Huawei Developer
管理模块版本。
命令格式
功能描述
在模块目录中运行此命令以获取或升级版本号，同时将数据回写入 oh-package.json5 中。
参数说明
无参数
当无参数使用ohpm version命令时，则会将当前模块的版本号打印至标准输出中。
newversion
newversion 参数应为一个合法的语义化版本，命令会将当前模块版本改写为 newversion 并打印在标准输出中。
major
当参数为 major 时，有以下几种情况：
minor
当参数为 minor 时，固定主版本号，变化次版本号与修订号，有以下几种情况：
patch
当参数为 patch 时，固定主版本号与次版本号，变化修订号，有以下几种情况：
Options
prefix
可以在 version 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
parameterFile
可以在 version 命令后面配置 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。
示例
当前模块为 entry，版本号为 1.0.0，在当前模块的根目录执行：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.09034240218797443201744881702965:50001231000000:2800:C38E2D84120A5B72E3169D59410E852A3061384E8003E7CDAC6FF3D2D1D10BB5.png?needInitFileName=true?needInitFileName=true)
接着执行：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.99792597285301364272028544892374:50001231000000:2800:849B9F4BFA031071EC6C392B4A60C97DFB35133CA1D867C9B865BDB7D95601DE.png?needInitFileName=true?needInitFileName=true)
接着执行：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.47742872004811374754938129569281:50001231000000:2800:614B7B0C8A5B9C88819222C1DEBB30E140C99CD4E74A7E321E3642244F1BF8A9.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-cache-V14
爬取时间: 2025-04-30 21:37:25
来源: Huawei Developer
清理 ohpm 缓存文件夹。
命令格式
功能描述
用于清理 ohpm 缓存文件夹。
关于缓存设计的说明
ohpm 将缓存数据存储在配置的 cache 目录下名为 content-v1 的文件夹中，存储所有通过 http 请求获取的 har 包数据。包的路径使用包的 sha512 哈希值分割成 3 端，第 1、2 位作为第一级目录，哈希值第 3、4 位作为第二级目录，哈希值第 5 位到结尾的所有字符作为文件名。使用哈希值可以将文件较均匀地分布在各个目录下，分成 3 层目录结构避免一个目录下文件数量过多，可以提升文件索引效率。
配置
缓存的配置方式见ohpmrc。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-run-V14
爬取时间: 2025-04-30 21:37:59
来源: Huawei Developer
执行用户自定义脚本。
命令格式
功能描述
-  scripts对象内部支持"key":"value"方式配置多个待执行脚本。如以下示例所示，scriptName 1、scriptName 2、scriptName 3为脚本别名（scriptName）；“echo hello”等为（scriptContent），后续内容均参考此说明。
传递参数
-  该示例表明，脚本scriptName 3的参数paramKey1会被替换为newValue, 并新增一个参数paramKey4。
支持多命令
支持 && 和 || 两种命令连接符 （&& 和 || 没有优先级区分，命令从左到右执行，不支持用括号来改变各个子命令的优先级）。
约束
| 约束项  | 说明  |
| --- | --- |
| scriptKey 命名约束  | 合法的 scriptKey 的名字可以包含字母（包含大小写），数字，ASCII 冒号 :，ASCII下划线 _ ，ASCII链接符 -，首字母必须是小写字母  |
| scriptContent 约束  | 合法的scriptContent不能引用除ohpm run以外的其它ohpm命令  |
| scriptContent 中使用 ohpm run 的约束  | 1、ohpm run 依赖的其它script别名必须在同一 oh-package.json5 中存在 2、ohpm run 引用关系是一个有向无环图，不支持递归或循环引用  |
约束项
说明
scriptKey 命名约束
合法的 scriptKey 的名字可以包含字母（包含大小写），数字，ASCII 冒号 :，ASCII下划线 _ ，ASCII链接符 -，首字母必须是小写字母
scriptContent 约束
合法的scriptContent不能引用除ohpm run以外的其它ohpm命令
scriptContent 中使用 ohpm run 的约束
1、ohpm run 依赖的其它script别名必须在同一 oh-package.json5 中存在
2、ohpm run 引用关系是一个有向无环图，不支持递归或循环引用
Options
prefix
可以通过 --prefix 指定包的根目录，该目录下必须存在 oh-package.json5 文件。不支持通过这种方式调用依赖包中的脚本别名。
示例
参数传递的使用示例
运行 script_name 的脚本，并指定脚本中参数agr1，agr2，agr3，agr4，取值分别为1，2，3，4，以上四种参数传递的方法均可生效。
oh-package.json5配置如下：
成功示例
执行脚本testSuc，如下所示：
执行结果：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.76044058976408207599548374513938:50001231000000:2800:4B069031E77D6BC2AA21A15DC01B35E3F45A49AF9DD956BE517331E31A749226.png?needInitFileName=true?needInitFileName=true)
失败示例
执行脚本testFail，如下所示：
执行结果：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.11092927674099199748932681857556:50001231000000:2800:DA249778E5430F84CECFF6122E71DA15900C8BDB141FBD9C719BEB192E6A2C10.png?needInitFileName=true?needInitFileName=true)
逻辑符(&&、||)使用示例
执行脚本testLogic，如下所示：
执行结果：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.62007914077619583798443087055848:50001231000000:2800:D754B7DDD272E3D62709D129B9CEE3F6E219C36A816D8EAB8EEA793AFC60B154.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm--version-V14
爬取时间: 2025-04-30 21:38:33
来源: Huawei Developer
查询 ohpm cli 安装版本。
命令格式
功能描述
示例
查询 ohpm cli 安装版本，可执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.90745396782137369475186724523823:50001231000000:2800:C68E5D5E7EFF64F07C804D0A4B5815EC5ABE6DDE3F8CA65F0DBF211282A762C0.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-ping-V14
爬取时间: 2025-04-30 21:39:07
来源: Huawei Developer
ping ohpm 仓库地址。
命令格式
功能描述
对给定的或者是配置中的仓库地址进行身份验证。如果有效，将会输出相关信息，比如以下内容：
否则将会输出错误信息，比如以下内容：
Options
registry
可以在 ping 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
fetch_timeout
可以在 ping 命令后面配置 -ft <number> 或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为 60000 ms。
strict_ssl
可以在 ping 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-clean-V14
爬取时间: 2025-04-30 21:39:42
来源: Huawei Developer
清理工程下所有模块的ohpm安装产物。
命令格式
功能描述
清理工程下所有模块的oh_modules目录、oh-package-lock.json5文件和oh-package-targetName-lock.json5文件(指定选项--target_path安装时生成)，清理完成后会在控制台打印耗时信息。
Options
keep-lockfile
可以在 clean 命令后面配置-kl或者--keep-lockfile参数，执行清理时会保留oh-package-lock.json5文件和oh-package-targetName-lock.json5文件(指定选项--target_path安装时生成)。
注意事项
示例

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-dist-tags-V14
爬取时间: 2025-04-30 21:40:16
来源: Huawei Developer
tag可标记一个三方库的某个版本，在install时可用tag代替版本号安装包。
命令格式
功能描述
操作tag。分为查看三方库的所有tag，给三方库的某个版本添加tag，修改tag到三方库的另一个版本，删除三方库的某个tag。
"latest"是一个预设的标签，不允许直接通过dist-tags命令来进行修改。该标签自动指向最高的正式版本；若无正式版本，则默认指向最高的先行版本。
以第三方库a为例，假定其版本序列包括"1.0.1-beta"、"1.0.1"和"2.0.1-beta"，在这种情况下，"latest"会自动映射到"1.0.1"，因为它是当前最高的正式版本。
子命令
list
列出指定三方库的所有标签。输出结果中，`latest`标签始终位于首位，其他标签按照字典序排列显示。
add
给某个版本的三方库增加一个标签。若该三方库已存在相同标签，则添加操作将会失败。
update
更新指定包的某个标签所对应的版本。如果指定的标签不存在，则更新操作将失败。
remove
删除指定包的一个标签。如果该标签并未存在于包中，则删除操作将会失败。
Options
publish_id
可以在 publish 命令后面配置 --publish_id <id> 参数，指定发布码。
key_path
可以在 publish 命令后面配置 --key_path <p> 参数，指定ssh私钥路径。
registry
可以在 install 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
publish_registry
可以在 publish 命令后面配置 --publish_registry <r> 参数，指定发布仓库地址。如果未指定，默认从配置中获取发布仓库地址。
fetch_timeout
可以在 publish 命令后面配置 -ft <number>或者  --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 publish 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
示例
如果想要通过使用tag，在oh-package.json5文件中引入包@ohos/axios的1.0.0版本，步骤如下：
1.  通过ohpm dist-tag的子命令add，对包@ohos/axios的1.0.0版本添加标签名beta。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-convert-V14
爬取时间: 2025-04-30 21:40:52
来源: Huawei Developer
将npm格式三方库转换为ohpm三方库。
命令格式
功能描述
将指定ohpm或npm仓库中的某个包或者本地node_modules目录下的包转换成满足ohpm格式要求的HAR包，并保存至当前工作目录，转换后的包将支持上传至ohpm-repo私仓或OpenHarmony三方库中心仓。
-  ohpm convert @group/pkg@version --registry <ohpm/npm仓库地址> 下载指定仓库中的某个包及其所有依赖项，并且将该包及其依赖转换为满足ohpm格式要求的HAR包。
-  ohpm convert <node_modules_path> 转换本地node_modules中的所有包为为满足ohpm格式要求的HAR包，<node_modules_path>必须为npm执行install命令后生成的node_modules目录。 示例：
ohpm convert命令仅保留package.json或oh-package.json5中的name、version、main、types、license、description、author、keywords、homepage、repository、artifactType、dependencies、devDependencies、dynamicDependencies、overrides、scripts、hooks字段，具体字段说明请参考oh-package.json5 字段说明。
Options
registry
可以在convert命令后面配置 --registry <registry> 参数，指定仓库地址。如果指定了--registry，convert命令将从远程仓库地址下载指定的包及其依赖后，进行转换处理。如果没有指定--registry，convert命令将从本地node_modules目录进行转换处理。
publish
可以在 convert命令后面配置 --publish 参数 ，若指定该参数，执行convert命令前请确认.ohpmrc推包相关配置无误，当所有包转换完成后将根据.ohpmrc中的配置依次进行推包。
示例
转换远程npm三方库中的包
转换npm三方库中的axios包，执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.38640117491151816761021954511540:50001231000000:2800:0C251AADA5AC6520E83A32D7C9E92C86CDC4967B59739C3AC517B08268F431DC.png?needInitFileName=true?needInitFileName=true)
转换本地node_modules目录中的包
执行npm install uuid后，转换本地node_modules目录中的包，执行以下命令：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.05377081723929883704150293051915:50001231000000:2800:B2C720D9ED2852C7337DDA0FE8A87B6FAA4674FBFF12FE650272ACC215E9B7A5.png?needInitFileName=true?needInitFileName=true)
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.08725511591312341950012140086986:50001231000000:2800:41E0F522CD0FB1CA7241C6DC6F91C3087B59FAA2B59BAEE021CF88B856C568BA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-command-line-building-app-V14
爬取时间: 2025-04-30 21:41:27
来源: Huawei Developer
除了使用DevEco Studio一键式构建应用/元服务外，还可以使用命令行工具来调用Hvigor任务进行构建。通过命令行的方式构建应用或元服务，可用于构筑CI（Continuous Integration）流水线，按照计划时间自动化的构建HAP/APP、签名、安装运行等操作。
通过命令行方式构建应用或元服务，可在Windows、Linux和macOS下调用相应命令来执行，本文将以Linux系统为例进行讲解，包括准备构建环境、构建HAP、签名运行等操作。在调用命令行任务上，Windows/macOS系统与Linux系统没有区别，仅在搭建构建环境上存在差异。
系统平台要求
-  Linux：64位操作系统
-  GLIBC：2.28或更高版本
-  内存：推荐使用16GB及以上，最小8GB
-  硬盘：100GB及以上
预置条件
配置JDK
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181219.89018995808535325848454576132649:50001231000000:2800:697781506E123844197F2FA42A8D0C3E282B1E267FC71CB15CB489DFE131CC6A.png)
获取命令行工具
1.  将解压后所在的路径定义为COMMANDLINE_TOOL_DIR，在后续配置hdc、hvigor、ohpm工具环境变量时使用。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181219.11272882155636313643827633567038:50001231000000:2800:0167020A6030381B2D48AC2C680AC77C70C1D34A84AD70C96CC3A479F4E723FF.png)
配置hdc环境变量
hdc命令行工具用于HarmonyOS应用/元服务调试所需的工具，该工具存放在命令行工具自带的sdk下的toolchains目录中。为方便使用hdc命令行工具，请将其添加到环境变量中。
1.
配置hvigor环境变量
1.
2.
配置npm镜像仓库
若您的工程在hvigor/hvigor-config.json5文件中依赖npm三方组件，流水线中则需要配置npm镜像地址，编译时才能正确地下载它。
安装ohpm
1.
2.
3.
安装libGL1库
在linux系统的构建场景下，使用纹理压缩功能需要安装libGL1库。
1.
构建应用
安装工程及模块依赖
使用命令行进行构建前，需要分别进入工程及各个模块下执行ohpm install命令，安装工程及各个模块依赖的三方库。
1.
2.
3.
执行Hvigor命令进行构建
1.
补充说明：
| 选项 | 说明 |
| --- | --- |
| -p buildMode={debug | release} | 采用debug/release模式进行编译构建。 缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。 关于构建模式的详细说明，请参考指定构建模式。针对HAR构建，请参考构建HAR。 |
| -p product={ProductName} | 指定product进行编译, 编译product下配置的module target。 缺省时：默认为default。 |
| -p module={ModuleName}@{TargetName} | 指定模块及target进行编译，可指定多个相同类型的模块进行编译以逗号分割；TargetName不指定时默认为default。 限制：此参数需要与--mode module参数搭配使用。 缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。 |
| -p ohos-test-coverage={true | false} | 执行测试框架代码覆盖率插桩编译。 |
选项
说明
-p buildMode={debug | release}
采用debug/release模式进行编译构建。
缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。
关于构建模式的详细说明，请参考指定构建模式。针对HAR构建，请参考构建HAR。
-p product={ProductName}
指定product进行编译, 编译product下配置的module target。
缺省时：默认为default。
-p module={ModuleName}@{TargetName}
指定模块及target进行编译，可指定多个相同类型的模块进行编译以逗号分割；TargetName不指定时默认为default。
限制：此参数需要与--mode module参数搭配使用。
缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。
-p ohos-test-coverage={true | false}
执行测试框架代码覆盖率插桩编译。
| 选项 | 说明 |
| --- | --- |
| clean | 清理构建产物 |
| assembleHap | 构建Hap应用 |
| assembleApp | 构建App应用 |
| assembleHsp | 构建Hsp包 |
| assembleHar | 构建Har包 |
选项
说明
clean
清理构建产物
assembleHap
构建Hap应用
assembleApp
构建App应用
assembleHsp
构建Hsp包
assembleHar
构建Har包
附：Hvigor命令行参数详见：常用命令。
运行应用
准备申请签名所需文件
准备好申请签名所需3个文件：密钥（.p12文件）、数字证书（.cer文件）、Profile（.p7b文件）。
生成密钥和证书请求文件
使用Open JDK携带的Keytool工具生成密钥和证书请求文件。
1.
2.  生成公私钥文件的参数说明如下：
3.  生成证书请求文件的参数说明如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181219.04152614590494830519846416326260:50001231000000:2800:9EBAC0992DFB0F324C21B878D308E5A6F25490E25F80EA4CAADD671521B4456B.png)
申请调试数字证书和Profile文件
生成证书请求文件后，在AppGallery Connect中申请、下载调试数字证书和Profile文件，具体请参考申请调试证书和Profile文件。
对HAP进行签名
通过Hvigor打包生成的HAP不会携带签名信息，如果要在真机设备上运行HAP，需要使用命令行工具对HAP进行签名。
1.  关于该命令中需要修改的参数说明如下，其余参数不需要修改：
运行应用
通过HDC工具将HAP推送到真机设备上进行安装，需要注意的是，推送的HAP必须是携带签名信息的，否则会导致HAP安装失败。
在设备上运行HAP的命令如下：
示例脚本

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-V14
爬取时间: 2025-04-30 21:42:01
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-overview-V14
爬取时间: 2025-04-30 21:42:35
来源: Huawei Developer
ohpm-repo 是一个搭建轻量级的ohpm私仓服务的工具。它与 ohpm 包管理器兼容，并按需缓存所有依赖项，加速私有网络中的安装。
私有性
所发的三方库都是私有的，只能根据配置进行访问。
缓存
ohpm-repo 根据需要缓存所有依赖项，加快私有网络的安装速度。
部署
ohpm-repo 支持单点部署和多实例部署。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-quickstart-V14
爬取时间: 2025-04-30 21:43:09
来源: Huawei Developer
ohpm-repo 私仓不允许使用 root 用户启动，请使用其他用户安装运行。
如何安装
ohpm-repo
1.  ohpm-repo 依赖于 node 运行，支持 node.js 18.x 及以上版本，请提前安装 nodejs，并完成环境变量的配置。Node.js安装请参考Node.js官方网站。
2.  下载 ohpm-repo 私仓工具包。请在下载中心获取最新的ohpm-repo，并根据下载中心页面工具完整性指导进行完整性校验。
3.  解压 ohpm-repo 私仓工具包。
4.  请将ohpm-repo工具包解压目录中bin目录的路径配置到系统环境变量path中，执行如下查询命令: 针对Linux和Mac系统，建议使用bash或zsh作为命令行界面。如果使用其他类型shell，写入ohpm-repo部署根目录deploy_root的环境变量时，默认写入.bashrc文件中。
5.  在启动 ohpm-repo 前还需要先按照如下方式完成配置修改： 进入 ohpm-repo 解压目录的 conf 目录内，打开 config.yaml配置文件。 ohpm-repo成功启动后修改配置文件方法：
6.  检查listen配置，默认配置为 localhost:8088 ，表示仅支持监听本机地址；如果希望其他机器通过ip/域名访问，则建议修改 listen 配置为ohpm-repo部署机器的ip：
7.  db：元数据存储 与db所适配的store类型 fileDB local storage mysql local storage，sftp storage， custom storage
8.  检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址、不配置取默认值，详情见：server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改 host 为本机指定的 ip/域名，例如 listen 为 0.0.0.0:8088，故 server 需配置为 http://<指定部署机器的ip/域名>:8088。
9.  进入ohpm-repo工具包解压目录中的 bin 目录下，执行安装命令: 结果实例：
10.  安装成功后，必须根据给出的提示信息刷新部署目录的环境变量，针对 Window 系统和 Linux/Mac 系统，有不同处理方式：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150811.55657358600451276267908325276729:50001231000000:2800:D97556A3F9CE4DB3FCEBAD3A6507731E17EAC52EC9B1E400C31727712EFC7CA8.png?needInitFileName=true?needInitFileName=true)
| db：元数据存储 | 与db所适配的store类型 |
| --- | --- |
| fileDB | local storage |
| mysql | local storage，sftp storage， custom storage |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150811.38715909936382264300722678251703:50001231000000:2800:82BB2C2D227CBC9553E13EE80A3C24007D8D3FFF498698C919868FA62AFB74E2.png?needInitFileName=true?needInitFileName=true)
如何启动
ohpm-repo安装成功后，进入ohpm-repo工具包解压目录下的 bin 目录下，执行如下命令，启动 ohpm-repo：
启动成功，将会出现以下日志信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150811.35876256792818463576972792853253:50001231000000:2800:4C9EDADFB1C12EE7BE2ACBA85B1B555BCE59E7B6E26F201959DC31DB34F1C558.png?needInitFileName=true?needInitFileName=true)
ohpm-repo 首次启动时，默认创建一个管理员账号，账号名称：admin，密码：12345Qq!。该账号在首次登录时，需要修改其密码，请修改密码后，重新登录该账号。
从ohpm-repo获取三方库
可以为所有项目配置该私有仓，例如执行以下命令：
或者在命令行中配置参数 --registry 使用，例如以下命令：
<配置的ohpm-repo私仓服务地址>：配置文件中store.config.server的地址信息，例如：store.config.server:为 http://127.0.0.1:8088，故 registry 为：http://127.0.0.1:8088/repos/ohpm。如果store.config.server没有配置，取默认值。
将三方库发布到 ohpm-repo
三方库包含静态共享包 HAR 包和动态共享包 HSP 包，可以通过 ohpm 命令行工具和使用 Web 页面两种方式发布。
从 ohpm 命令行工具 1.3.0 版本和 ohpm-repo 私仓 1.1.0 版本开始，支持动态共享包 HSP 包以 .tgz 文件形式发布到ohpm-repo，之前版本仅支持发布以 .har 文件形式的静态共享包 。
使用命令行工具发布
1.  示例： 公钥和私钥存储在 D 盘 的 path 目录下，公钥和私钥名称分别为 my_key_path.pub 和 my_key_path。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.08283196862511016369967631381573:50001231000000:2800:2CAEE31FE5A92F36865F6F96909CCAFA5FE7BADB3CBDD1087147DED0097DCB3A.png?needInitFileName=true?needInitFileName=true)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.39940863219749724972664767925170:50001231000000:2800:79E1F263AFBF1F9D8F9789F469A44E26BFB1DE368D00B41DE799DD78B62A841A.png?needInitFileName=true?needInitFileName=true)
1.  执行 ''ohpm publish <HAR包路径>'' 命令发布 HAR包，<HAR包路径> 指向的文件后缀需为 .har 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令： 动态共享包 HSP 包不能直接发布在ohpm-repo内，需要先转化为 .tgz 包，转换方法见：编译HSP模块。TGZ 包的发布流程同 HAR 一致。 执行 ''ohpm publish <TGZ 包路径>'' 命令发布 TGZ 包，< TGZ 包路径> 指向的文件后缀需为 .tgz 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
2.  执行 ''ohpm publish <HAR包路径>'' 命令发布 HAR包，<HAR包路径> 指向的文件后缀需为 .har 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
3.  动态共享包 HSP 包不能直接发布在ohpm-repo内，需要先转化为 .tgz 包，转换方法见：编译HSP模块。TGZ 包的发布流程同 HAR 一致。 执行 ''ohpm publish <TGZ 包路径>'' 命令发布 TGZ 包，< TGZ 包路径> 指向的文件后缀需为 .tgz 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
-  执行 ''ohpm publish <HAR包路径>'' 命令发布 HAR包，<HAR包路径> 指向的文件后缀需为 .har 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
-  动态共享包 HSP 包不能直接发布在ohpm-repo内，需要先转化为 .tgz 包，转换方法见：编译HSP模块。TGZ 包的发布流程同 HAR 一致。 执行 ''ohpm publish <TGZ 包路径>'' 命令发布 TGZ 包，< TGZ 包路径> 指向的文件后缀需为 .tgz 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
使用Web页面发布
在Web页面用管理员账号登录ohpm-repo私仓管理地址，在个人中心 > 仓库管理中，点击管理三方包 > 上传三方包，包的后缀名必须为 .har 或者 .tgz。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.25013711224826400270334726356967:50001231000000:2800:447C844FE758124E1A9C765701579C35CB8CF213AB248E3D5EDD3BED5DFF4691.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.95046083672915742685713820212954:50001231000000:2800:D184E4E368504DF6A56B9D8DDA16320DEBDB0DD27D0F464E4B04141259BFDE0C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-configuration-V14
爬取时间: 2025-04-30 21:43:44
来源: Huawei Developer
config.yaml 是 ohpm-repo 的重要文件，可以在其中修改默认参数配置，启动插件和扩展功能。ohpm-repo 私仓解压目录中的 conf 目录下带有一个默认配置文件 config.yaml，ohpm-repo 执行 install 命令时默认读取该文件。
ohpm-repo成功启动后修改配置文件方法：
默认配置
配置项说明
listen
格式为三段式，即 <proto>://<host>:<port>，其中 <proto> 可以不填，默认为 http，如：
-  监听本机回环地址（默认）：
-  监听具体地址（建议）：
-  监听所有地址（当选择监听所有地址时，配置项store中 server 值必须配置）：
listen值建议监听具体的地址。proto 支持 http 和 https 协议，支持缺省，缺省时默认为 http。为了确保ohpm-repo链接的安全，建议选择使用 https 协议，如果配置为 https 协议，则需要完善https相关配置。
https
当配置listen时选择使用 https 协议，则需要配置 https_key 和 https_cert：
为了确保ohpm-repo链接的安全，建议选择使用 https 协议，可以使用如下命令，在当前命令行所在目录生成 https 协议使用的证书私钥文件和证书文件（需要提前安装安全套接字层密码库Openssl）：
参考配置如下：
deploy_root
ohpm-repo的部署目录，存储运行时生成的文件数据。
-  如果 <deploy_root> 字段为空，则默认路径为： windows系统: ~/AppData/Roaming/Huawei/ohpm-repo 其他操作系统：~/ohpm-repo
-  如果<deploy_root>字段不为空，则路径必须为绝对路径，且路径所指向文件夹必须存在。
参考配置如下：
server
服务相关配置，具体为：
参考配置如下：
db是元数据存储的配置项，store是文件存储的配置项。db支持fileDB本地存储和mysql数据库存储；store支持file storage存储，sftp存储和custom storage 自定义插件存储。db和store不能随意搭配，需要符合表1的匹配规范：
| db：元数据存储  | 与db所适配的store：三方包文件存储  |
| --- | --- |
| filedb  | file storage  |
| mysql(ohpm-repo 1.1.0开始支持）  | file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持）  |
db：元数据存储
与db所适配的store：三方包文件存储
filedb
file storage
mysql(ohpm-repo 1.1.0开始支持）
file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持）
db
ohpm-repo运行过程产生的用户信息，运行状态等元数据存储配置，支持本地磁盘存储filedb和 mysql 数据库存储。
本地磁盘存储
默认使用本地磁盘存储，配置如下：
如果想修改数据库文件存储路径同时保留旧的数据，则需要把旧路径下的数据文件迁移至新路径。
参考配置如下：
Mysql存储
参考配置如下：
为了避免潜在的安全风险，建议使用非最高权限的数据库账户进行连接。
store
三方库及其元数据等资源文件存储配置，支持本地磁盘存储，sftp存储和自定义插件存储。
本地磁盘存储
默认使用本地磁盘存储文件，具体配置为：
上传资源后如若要修改存储路径，则需要把旧路径下的数据迁移至新路径中。
参考配置如下：
sftp 存储
支持使用 sftp 存储文件，仅当数据存储为 mysql 存储时才能使用 sftp 存储，具体配置为：
参考配置如下：
custom存储
使用自定义插件存储，具体配置为：
参考配置如下：
use_reverse_proxy
当use_reverse_proxy配置为true时，必须在反向代理配置时刷新x-forwarded-for值（如果存在多级代理，只需要在最外层代理配置刷新），如果不刷新将存在x-forwarded-for数据被篡改风险，反向代理配置刷新x-forwarded-for命令如下：
uplink
参考配置如下：
logs
参考配置如下：
loglevel
loglevel 自定义配置，具体配置为：
参考配置如下：
auth_plugin
ohpm-repo 从 2.3.0 版本开始支持自定义认证插件（需配套使用1.8.0及以上版本ohpm命令行工具），允许您开发定制化的认证插件来对接您自己的用户信息系统。自定义认证插件开发流程见认证插件说明文档。
参数说明：
参考配置如下：
compability_log_level
allow_remove_depended_packages
allow_new_file_upload_api
关于 deploy_root
deploy_root 为ohpm-repo的部署目录，通过配置文件中字段 <deploy_root> 可进行配置。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-log-V14
爬取时间: 2025-04-30 21:44:17
来源: Huawei Developer
与任何 web 应用程序相同，ohpm-repo 有一个内置的日志记录器，其定义了四种日志类型。
访问日志 - access.log
访问日志中主要包含操作时间、服务器 ip、操作源、操作结果以及请求接口或者请求静态资源，其文件保存个数最多为 180 个。
操作日志 - operate.log
操作日志中主要包含操作时间、日志级别、操作人id(userId)、终端 ip(ip)、操作资源（resource）、操作方法名（event）以及操作结果（result），其文件保存个数最多为 180 个。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.35623342065282818817212976935957:50001231000000:2800:783D80FD9520F23D1AEBCA242594DA6BC16F9AA531741D5807D16AD93D2C0E15.png?needInitFileName=true?needInitFileName=true)
操作方法名(event)： 当在ohpm-repo管理界面执行一些列操作时，会在operate.log文件生成一条条操作数据，操作方法名即表示当前操作涉及到的方法名字，例如login即表示登录操作，analyzePackage即表示上传包时对包的解析操作。
| 序号  | Event描述  | 说明  |
| --- | --- | --- |
| 1  | generateAccessToken / deleteAccessToken  | 生成 / 删除AccessToken  |
| 2  | login / logout  | 登入 / 登出  |
| 3  | publish / unPublish  | 上架 / 下载资源包  |
| 4  | addGroup / deleteGroup  | 添加/删除组织  |
| 5  | updateGroup  | 更新组织  |
| 6  | addMember/deleteMember  | 添加 / 删除组织成员  |
| 7  | addAdminMember/deleteAdminMember  | 添加/删除组织管理员  |
| 8  | addPublicKey / delPublicKeyByld  | 添加 / 删除发布公钥  |
| 9  | updateRepo  | 更新仓库  |
| 10  | analyzePackage  | 解析上传的包文件  |
| 11  | uploadPackage  | 上传包文件  |
| 12  | getPackageSizeLimit  | 获取包的大小限制  |
| 13  | addUplink / deleteUplink  | 添加 / 删除uplink  |
| 14  | updateUplink  | 更新uplink  |
| 15  | updateUplinkProxy  | 更新Uplink代理  |
| 16  | addUser / delUserByUserld  | 添加/删除用户  |
| 17  | changePassWord  | 改变用户账户密码  |
| 18  | resetPassWord  | 重置用户账户密码  |
| 19  | changeRole  | 修改用户角色(管理员和非管理员)  |
| 20  | register  | 注册账户  |
| 21  | resetKey  | 重置系统秘钥  |
序号
Event描述
说明
1
generateAccessToken / deleteAccessToken
生成 / 删除AccessToken
2
login / logout
登入 / 登出
3
publish / unPublish
上架 / 下载资源包
4
addGroup / deleteGroup
添加/删除组织
5
updateGroup
更新组织
6
addMember/deleteMember
添加 / 删除组织成员
7
addAdminMember/deleteAdminMember
添加/删除组织管理员
8
addPublicKey / delPublicKeyByld
添加 / 删除发布公钥
9
updateRepo
更新仓库
10
analyzePackage
解析上传的包文件
11
uploadPackage
上传包文件
12
getPackageSizeLimit
获取包的大小限制
13
addUplink / deleteUplink
添加 / 删除uplink
14
updateUplink
更新uplink
15
updateUplinkProxy
更新Uplink代理
16
addUser / delUserByUserld
添加/删除用户
17
changePassWord
改变用户账户密码
18
resetPassWord
重置用户账户密码
19
changeRole
修改用户角色(管理员和非管理员)
20
register
注册账户
21
resetKey
重置系统秘钥
运行日志 - run.log
运行日志中主要包含操作时间、日志级别以及日志信息，其文件保存个数最多为 30个。运行日志定义了日志级别：all，trace，debug，info，warn，error，fatal，mark 和 off。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.46126780660082606477138917150484:50001231000000:2800:98F6EC9709F03FFABD838B656735F92C7FED45C309A98E7A8AEC82D008A107F0.png?needInitFileName=true?needInitFileName=true)
运行错误日志 - repoError.log
当ohpm-repo在运行过程中，所有run.log中生成的error日志都会打印到repoError.log中，是error日志的集合，日志打印级别与run.log日志保持一致。
下载错误日志
当从仓库中下载某个包失败时，仓库会生成一条错误日志记录在数据库中的 downloadfailure 表中，当为ohpm-repo配置了 sftp 存储服务时，从任意一个 sftp 服务中下载失败时，都会生成一条错误日志并保存。每条日志都有 handled 标识，handled 为 0 时表示已处理，handled 为 1 时表示未处理。
日志存储路径
日志存储的默认路径为 ./logs，相对路径基准为ohpm-repo部署根目录deploy_root。
日志打印级别
在配置文件中可以设置访问、操作、运行日志的打印级别，日志将会只打印不低于设置级别的日志，日志级别由低到高为：all，trace，debug，info，warn，error，fatal，mark 和 off。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-command-V14
爬取时间: 2025-04-30 21:44:51
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-help-V14
爬取时间: 2025-04-30 21:45:26
来源: Huawei Developer
获取有关 ohpm-repo 的帮助。
命令格式
参数
command：命令名称
功能描述
-  如果提供了命令名称，则显示相应命令的帮助信息。
-  如果提供的命令名称不存在或未提供，则显示所有命令的概要信息。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.32819790041888325732924563132219:50001231000000:2800:46C4FCA150FA000FCEEA3D4D66562FCFCEFCEC0376AACD0E9E7155CDF2FC1A2A.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-install-V14
爬取时间: 2025-04-30 21:46:00
来源: Huawei Developer
安装ohpm-repo服务。
命令格式
功能描述
在启动服务之前做好准备工作，包括：检查ohpm-repo配置文件的合法性和数据库的初始化等。
选项
config
-  默认值："<binary_root>/conf/config.yaml" <binary_root>：ohpm-repo 私仓解压根目录。
-  类型： String
可以在 install 命令后面配置 --config <string> 参数，指定配置文件路径。支持相对路径，以当前命令行工作路径作为根目录。
执行 install 成功后，会在<deploy_root>/conf中生成一个运行时配置文件config.yaml，作为后续命令的配置文件，其中 <deploy_root> 为ohpm-repo部署目录。
skip-db
在install命令后面配置-sd或者--skip-db，指定是否跳过对mysql数据库中数据表的初始化；默认会读取ohpm-repo解压目录中的schema.sql文件，对mysql数据库中的表进行初始化。
在ohpm-repo配置文件config.yaml中，配置项db.type只有为mysql时，此参数才生效。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.94033514246097794578112455933813:50001231000000:2800:913E5733214B7A6BFD6FEE5FB2C7995E69BF23E7859CDBDF5D7DC5CA5EAB6A3A.png?needInitFileName=true?needInitFileName=true)
注意
安装成功后，必须根据给出的提示信息刷新环境变量，针对 Window 系统和 Linux/Mac 系统，有不同处理方式：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-start-V14
爬取时间: 2025-04-30 21:46:34
来源: Huawei Developer
启动ohpm-repo服务。
前提条件
已成功执行install命令，并按要求刷新环境变量。
命令格式
功能描述
用于启动ohpm-repo服务，创建一个ohpm-repo实例。
启动时将ohpm-repo服务的 pid 存放到 <deploy_root>/runtime/.pid 文件中，其中 <deploy_root> 为ohpm-repo私仓部署目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.80691983855939629649038119993993:50001231000000:2800:8BAE4A756CBFF22BDA57C8BB19B7643E8CB87B0CFEABC3C17AF66004A5743C9C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restart-V14
爬取时间: 2025-04-30 21:47:08
来源: Huawei Developer
重新启动ohpm-repo服务。
前提条件
已成功执行install命令，并按要求刷新环境变量。
命令格式
功能描述
停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务.
启动时将ohpm-repo服务的 pid 存放到 <deploy_root>/runtime/.pid 文件，其中 <deploy_root> 为ohpm-repo私仓部署目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.33622078469017877139567911907214:50001231000000:2800:54C3F57A05F84292D5DC2549298A1CA7F432EE27D4AE1305707B658818199112.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-stop-V14
爬取时间: 2025-04-30 21:47:41
来源: Huawei Developer
停止ohpm-repo实例。
命令格式
功能描述
用于停止已经启动的ohpm-repo实例。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.59702217443014725761366102561757:50001231000000:2800:D6A140CFF9843F1EBA2C45FB9FD544383EBC12D79BC1D5158CBF458BC0CAEBEC.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo--version-V14
爬取时间: 2025-04-30 21:48:15
来源: Huawei Developer
查询ohpm-repo版本。
命令格式
功能描述
打印ohpm-repo的版本号。
示例
执行以下命令，查看版本信息：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.60117360288300131349660905772953:50001231000000:2800:67D30ADD0FEB1C36578A04AF821B38AE50FB843148CBCFBE3B75E2283EF4C01B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-encrypt_password-V14
爬取时间: 2025-04-30 21:48:49
来源: Huawei Developer
加密明文密码。
命令格式
功能描述
使用指定的加密组件加密从标准输入读取的数据，并在标准输出中输出密文。
选项
crypto_path
必须在 encrypt_password 命令后面配置 --crypto_path <string> 参数，指定加密组件的路径。如果是完整组件，将用该组件去加密明文密码。如果是一个空目录，则命令将生成新的加密组件并加密明文密码。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.49665635163565191913264390815438:50001231000000:2800:6A492DC677F398A441E6BED4D90D2EC8991B692AB97CE99E5DA2CD10273D4156.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-pack-V14
爬取时间: 2025-04-30 21:49:25
来源: Huawei Developer
打包ohpm-repo部署目录文件。
前提条件
已成功执行start 命令或者restart 命令，ohpm-repo服务启动成功。
命令格式
功能描述
用于打包ohpm-repo部署目录deploy_root下的conf ，db和meta目录。
说明：
参数
<deploy_root>
必须在 pack 命令后面配置 <deploy_root> 参数，指定待打包的ohpm-repo私仓部署目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.35148452895622111456855362597851:50001231000000:2800:4BEB20A5A7F32802A3E6E62717692D2EB771DA3A7B7F30E8FAD920B395755D78.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-deploy-V14
爬取时间: 2025-04-30 21:49:58
来源: Huawei Developer
使用备份文件部署新的ohpm-repo实例。
前提条件
已获得由pack 命令打包的 .zip 文件。
命令格式
功能描述
命令将使用由 ohpm-repo pack 得到的打包产物部署新的ohpm-repo实例。 命令要求数据存储必须使用mysql，文件存储必须使用  sftp ，且在命令执行时，会检查数据库 mysql 中存储的ohpm-repo实例列表与配置的 sftp 存储目录中的ohpm-repo实例列表是否一致，若不一致则命令执行失败。
参数
<file_path>
必须在 deploy 命令后面配置 <file_path> 参数，指定打包产物路径。
选项
deploy_root
可以在 deploy 命令后面配置 --deploy_root <string> 参数，未配置将使用默认值。支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
logs
可以在 deploy 命令后面配置 --logs <string> 参数，指定 log 目录，优先级高于 config.yaml 中的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
uplinkCachePath
可以在 deploy 命令后面配置 --uplinkCachePath <string> 参数，指定远程包缓存路径，优先级高于 config.yaml 中的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
部署实例成功后，命令行所配置的deploy_root，logs 和 uplinkCachePath会写入到运行时配置文件中，可从 <deploy_root>/conf 目录中的配置文件 config.yaml 中查看。
skip-db
在deploy命令后面配置-sd或者--skip-db，指定是否跳过对mysql数据库中数据表的初始化；默认会读取ohpm-repo解压目录中的schema.sql文件，对mysql数据库中的表进行初始化。
在ohpm-repo配置文件config.yaml中，配置项db.type只有为mysql时，此参数才生效。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.41117529849524581618342569315721:50001231000000:2800:64E2CBF7A4438B5077996E43BB07C6CA7F08B9729454C15C5453810B64E575D2.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restore-V14
爬取时间: 2025-04-30 21:50:32
来源: Huawei Developer
将 ohpm-repo pack 打包产物替换 <deploy_root> 目录下相应文件，重启服务。
前提条件
命令格式
功能描述
该命令会停止当前ohpm-repo服务，并用打包文件 <file_path> 中的内容替换ohpm-repo部署根目录 <deploy_root> 的相应文件，然后重启ohpm-repo服务。该命令执行前必须已经执行过ohpm-repo实例启动命令 ohpm-repo start。
支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
参数
<file_path>
指定待解压的打包文件路径。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.29902279044155118323258458241902:50001231000000:2800:4A0DFC627DD676248D4D926EEC5873E66A82ACBA6233C58872D571B11726F937.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-mirror_storage-V14
爬取时间: 2025-04-30 21:51:07
来源: Huawei Developer
同步 sftp 存储的包。
前提条件
命令格式
功能描述
该命令必须配置文件存储插件模块为 sftp。命令会将源sftp目录下满足 <target> 条件的包同步到目标sftp目录下。
参数
<source_sftp>
必须在 mirror_storage 命令后面配置 <source_sftp> 参数，指定源sftp配置的名字。
<target_sftp>
必须在 mirror_storage 命令后面配置 <target_sftp> 参数，指定目标sftp配置的名字。
<target>
必须在 mirror_storage 命令后配置 <target> 参数，指定满足条件的包；或使用 @all 指定所有包。
选项
failed
可以在 mirror_storage 命令后面配置 --failed 选项，则只同步在下载错误日志中未被处理的且满足 <target> 条件的包，如果同步成功，则相应的错误日志会被设置成 handled。
示例
执行以下命令，同步包 @ohos/axios@2.0.3：
说明：将名为 test_one_sftp 的sftp目录中 @ohos/axios@2.0.3 包同步到名为 test_two_sftp 的sftp目录中。
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.94639501308319891011670272765776:50001231000000:2800:96DA42188C5EAB6EE03F9B4CE18D8CF342C7F8F665EB9290C2C7584B27530D30.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-check_storage-V14
爬取时间: 2025-04-30 21:51:40
来源: Huawei Developer
检查 sftp 中存储包的完整性。
前提条件
命令格式
功能描述
命令根据元数据检查 sftp 存储的包是否存在且完整。该命令要求数据存储 db 模块必须使用 mysql，文件存储 store 模块必须使用 sftp。
参数
<target>
必须在 check_storage 命令后面配置 <target> 参数，指定要检查的包或者用 @all 指定检查所有包。
选项
failed
可以在 check_storage 命令后面配置 --failed 选项 ，则只检查在下载错误日志中未被处理的且满足<target>条件的包。
示例
执行以下命令，检查包 @ohos/basic-ftp 的完整性：
检查 @ohos/basic-ftp 包在所有 sftp 存储目录中的完整性。
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.91174950421846738044757764858152:50001231000000:2800:921DEB9D518A56CE9AF05619880523272BDB8E9BDF0BA80181699F87742BCACF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-remove_instance-V14
爬取时间: 2025-04-30 21:52:15
来源: Huawei Developer
删除本机实例信息。
前提条件
命令格式
功能描述
该命令会停止当前运行的ohpm-repo服务，同时删除本机在 mysql 和 sftp 中的实例信息。命令要求数据存储 db 模块必须使用 mysql，文件存储 store 模块必须使用 sftp。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.06030284216243310096606784157288:50001231000000:2800:F7CBC6A0D2F3B7F5D36DAD89369CBC0F7ED6F5E23C07F7BC15DCE14C60481DEC.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-command-data-migration-V14
爬取时间: 2025-04-30 21:52:49
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-export-pkginfo-V14
爬取时间: 2025-04-30 21:53:24
来源: Huawei Developer
导出ohpm-repo或OpenHarmony三方库中心仓已上架的包列表。
命令格式
功能描述
将所有或者与输入正则表达式匹配的已上架库的包名导出到当前目录的pkgInfo_xxx.json文件。
选项
--public-registry
在export_pkginfo命令后面配置--public-registry  <string>，指定OpenHarmony三方库中心仓registry地址获取已上架的包列表。
--http-proxy
在export_pkginfo命令后面配置--http-proxy  <string>，发起请求时将为上面配置的--public-registry地址设置代理。
--filter
在export_pkginfo命令后面配置--filter <string>，可以根据正则表达式导出匹配的包列表，根据完整包名匹配。
三方包的命名规则为：@<组织名>/<包名>@<版本号>。
示例
执行以下命令从ohpm-repo中导出已上架的包列表：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.09072874196839927698886142877675:50001231000000:2800:C285D7C729AA62A369B437AFF7107812EFD0382F19F3FABF9A9972382B6DCE9E.png?needInitFileName=true?needInitFileName=true)
执行以下命令从OpenHarmony三方库中心仓中导出已上架的包列表：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.25961594709780162054721868032298:50001231000000:2800:A0B860019ECCAFE208FB2E96427EE2D488FB92D6778FDAB9B495D87F1E1DCDE0.png?needInitFileName=true?needInitFileName=true)
执行以下命令从ohpm-repo本地存储中，导出所有名为 pack1，版本是 1.1 的（可以是 1.1.1, 1.1.2, 1.1.3等）已上架的包列表：
执行以下命令从ohpm-repo配置的public-registry仓库中，导出所有属于组ohos，且名为lottie的所有版本的已上架的包列表：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-batch-download-V14
爬取时间: 2025-04-30 21:53:58
来源: Huawei Developer
批量下载ohpm-repo或OpenHarmony三方库中心仓的包文件。
前提条件
已成功执行export_pkginfo 命令，生成pkgInfo_xxx.json文件。
命令格式
功能描述
根据提供的包名列表用于批量下载ohpm-repo或OpenHarmony三方库中心仓的包文件，并导出zip文件。
说明：执行export_pkginfo 命令生成的pkgInfo_xxx.json文件中记录着ohpm-repo或OpenHarmony三方库中心仓中所有已上架的包，若仅需要批量下载部分包文件，可以手动修改pkgInfo_xxx.json文件，命令只会批量下载pkgInfo_xxx.json文件中指定的包。
参数
<pkg_list>
必须在 batch_download 命令后面配置 <pkg_list> 参数，指定执行export_pkginfo 命令导出的json文件。
选项
--public-registry
在batch_download命令后面配置--public-registry  <string>，指定OpenHarmony三方库中心仓registry地址下载包文件。
--http-proxy
在batch_download命令后面配置--http-proxy  <string>，发起请求时将为上面配置的--public-registry地址设置代理。
--not-use-proxy
在batch_download命令后面配置--not-use-proxy  <string>，发起请求时不会为指定的地址设置代理，如果有个多个地址请使用英文逗号分割并使用url编码转换特殊字符。
示例
执行以下命令从ohpm-repo中批量下载包文件：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.05152402250640835741500443957257:50001231000000:2800:E6B12C51983A21CB0130457A6F22FF2AED200FCEE03220114A4DD0EE638EADF5.png?needInitFileName=true?needInitFileName=true)
1、生成的zip文件中存在 pkgInfo.json 文件，其中记录了每个包的文件名、包名、组织、上传者、Tag标签，用于在批量上传时准确指定ohpm-repo的数据库中某个用户为某个包的真实上传用户，同时将包的Tag标签一起上传。
2、命令执行中，如果某个包的用户在ohpm-repo中不存在，将默认指定该包的上传用户为管理员用户或者组织的管理者用户。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.68225564042457732931386355714202:50001231000000:2800:F5D16E08697379CD6E0C82724A02D64CE78BEB9E2B2DDA55DF55D4405BB4FB92.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.74180809753020180270618822673789:50001231000000:2800:EE437603C61364E0D554917DADA8069EABE1B7EE75856F7DEFE150C4C0EC58CD.png?needInitFileName=true?needInitFileName=true)
执行以下命令从OpenHarmony三方库中心仓中批量下载包文件：
结果示例：
如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo网站页面中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-batch-publish-V14
爬取时间: 2025-04-30 21:54:32
来源: Huawei Developer
批量上传包文件。
前提条件
已成功执行batch_download 命令、export_userinfo 命令、import_userinfo 命令，确保每个包指定的包文件、用户和组织都存在。
命令格式
功能描述
根据提供的zip文件批量上传其中的包到ohpm-repo。
参数
<zip_file>
必须在batch_publish命令后面配置<zip_file>参数，指定执行batch_download命令导出的zip文件。
选项
--force
在batch_publish命令后面配置--force，进行批量上传时某个包的组织在ohpm-repo中不存在，将选取一位管理员用户作为组织负责人自动创建组织。
示例
执行以下命令：
结果示例：
如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo实例缓存中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-export-userinfo-V14
爬取时间: 2025-04-30 21:55:06
来源: Huawei Developer
导出用户必要的DB数据。
命令格式
功能描述
在当前的工作目录导出记录了DB数据的 export_userInfo_xxx.zip 文件，其中包含加密组件和下面的9个数据表。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.27996260988850957887101613286111:50001231000000:2800:BDB7916A7B24EE19A95D01A37077569963F8B823D2EC06DE9A5D187BEB32596F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.91752015594546016038614116471577:50001231000000:2800:448ED2D9D35523C688406C182677B64A1670F839985770FB806E6FE7702E33CB.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-import-userinfo-V14
爬取时间: 2025-04-30 21:55:42
来源: Huawei Developer
导入用户DB数据。
前提条件
已成功执行export_userinfo 命令。
命令格式
功能描述
根据提供的zip文件导入用户DB数据到ohpm-repo。
参数
<zip_file>
必须在 import_userinfo 命令后面配置 <zip_file> 参数，指定执行export_userinfo 命令导出的zip文件。
选项
clean-db
可以在 import_userinfo 命令后面配置 --clean-db  参数，指定在导入数据前先清空DB数据。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.92455944894445804127236544144340:50001231000000:2800:D74A015AD41140F4EEE33F36DB6617F6B2752C134B9BC45A6813C847F8872407.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-deploy-guide-V14
爬取时间: 2025-04-30 21:56:17
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-deploy-single-instance-V14
爬取时间: 2025-04-30 21:56:50
来源: Huawei Developer
ohpm-repo 私仓不允许使用 root 用户启动，请使用其他用户安装运行。
安装ohpm-repo工具
1.  ohpm-repo 依赖于 node 运行，支持 node.js 18.x 及以上版本，请提前安装 nodejs,并完成环境变量的配置。Node.js 安装请参考Node.js官方网站。
2.  下载 ohpm-repo 工具包，点击链接获取。
3.  解压 ohpm-repo私仓工具包。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.22608594620222147268999985613100:50001231000000:2800:9C456635A6A9B143284C496AA2BA7935B77510B5C237F02898AE18B0CD607819.png?needInitFileName=true?needInitFileName=true)
1.  终端输出版本号（如：2.0.0），则表示安装包解压无问题。如有报错，请参考FAQ解决。 针对Linux和Mac系统，建议使用bash作为命令行界面。
2.  数据存储 db 模块使用filedb： 文件存储 store 模块使用fs： 检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址，不配置取默认值，具体请参考server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改server的 host 为本机指定的 ip/域名，例如 listen 为 0.0.0.0:8088，故 server 需配置为  http://<指定部署机器的ip/域名>:8088。
3.  数据存储 db 模块使用filedb：
4.  文件存储 store 模块使用fs：
5.  检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址，不配置取默认值，具体请参考server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改server的 host 为本机指定的 ip/域名，例如 listen 为 0.0.0.0:8088，故 server 需配置为  http://<指定部署机器的ip/域名>:8088。
6.  不配置参数 --config，默认使用ohpm-repo根目录中 conf 目录内自带的配置文件 config.yaml。 启动成功日志信息如下：
-  数据存储 db 模块使用filedb：
-  文件存储 store 模块使用fs：
-  检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址，不配置取默认值，具体请参考server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改server的 host 为本机指定的 ip/域名，例如 listen 为 0.0.0.0:8088，故 server 需配置为  http://<指定部署机器的ip/域名>:8088。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.09254167520488159729722668904307:50001231000000:2800:E2CC243A4BD904D64267B1DE4425DA6020B7FF7991BC214BA362AD8A5BC822BF.png?needInitFileName=true?needInitFileName=true)
启动ohpm-repo
执行 start 命令启动ohpm-repo。
启动成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.35477309498065697430032434860588:50001231000000:2800:C56769554102F36616E6F29FA60672A26B4282151AC80EEDAF496B525F52DBEA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-deploy-multiple-instances-V14
爬取时间: 2025-04-30 21:57:25
来源: Huawei Developer
ohpm-repo 私仓不允许使用 root 用户启动，请使用其他用户安装运行。只有db存储为mysql且store存储为sftp或者custom时，才支持多实例方式部署。本章节多实例部署以db存储为mysql，store存储为sftp为例。
环境准备
安装ohpm-repo工具
1.
2.  终端输出版本号（如：2.0.0），则表示安装包解压无问题。如有报错，请参考FAQ解决。 针对Linux和Mac系统，建议使用bash作为命令行界面。
3.  1、ohpm-repo文件的存储路径为： <sftp服务器配置的存储根目录> +<store配置的path路径>，其中path只支持相对路径，必须以/开头。例如sftp服务器存储根目录为/user/sftp/data，store中path配置的路径为/source，故最终ohpm-repo文件存储路径为/user/sftp/data/source。 2、多实例部署ohpm-repo时，必须配置反向代理服务器，转发客户端请求到部署的多个ohpm-repo实例服务器中，故store.config.server必须手动配置为反向代理服务器的域名/ip地址，且需要配置use_reverse_proxy值为true。
4.  1、ohpm-repo文件的存储路径为： <sftp服务器配置的存储根目录> +<store配置的path路径>，其中path只支持相对路径，必须以/开头。例如sftp服务器存储根目录为/user/sftp/data，store中path配置的路径为/source，故最终ohpm-repo文件存储路径为/user/sftp/data/source。 2、多实例部署ohpm-repo时，必须配置反向代理服务器，转发客户端请求到部署的多个ohpm-repo实例服务器中，故store.config.server必须手动配置为反向代理服务器的域名/ip地址，且需要配置use_reverse_proxy值为true。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.65607136310205994255207384376784:50001231000000:2800:825E7C59CB44D68E23D175C595FC4724B035905F1185A6A5812EDD8C80CAF1C7.png?needInitFileName=true?needInitFileName=true)
-  1、ohpm-repo文件的存储路径为： <sftp服务器配置的存储根目录> +<store配置的path路径>，其中path只支持相对路径，必须以/开头。例如sftp服务器存储根目录为/user/sftp/data，store中path配置的路径为/source，故最终ohpm-repo文件存储路径为/user/sftp/data/source。 2、多实例部署ohpm-repo时，必须配置反向代理服务器，转发客户端请求到部署的多个ohpm-repo实例服务器中，故store.config.server必须手动配置为反向代理服务器的域名/ip地址，且需要配置use_reverse_proxy值为true。
1.  不配置参数--config，则默认使用 ohpm-repo 解压目录中 conf 目录内自带的配置文件config.yaml。 安装成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.40393824776991426365594347822256:50001231000000:2800:C69F428DDDFB1296A003B2D86AA75F20FB1C97D5B014109D71DAAADCA5DE7AEF.png?needInitFileName=true?needInitFileName=true)
部署首个节点
进入ohpm-repo解压目录的 bin 目录中，命令行启动ohpm-repo。
启动成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.08478191607331922230834887130897:50001231000000:2800:3CF4E00E9F49D5FEEE4D5F4ACAEF2DFC415F3C758654F0D30158643ED3D1C68C.png?needInitFileName=true?needInitFileName=true)
打包和部署
为帮助更方便地完成多实例部署，已提供打包和部署命令。
打包
在完成了多实例配置并首次启动过ohpm-repo服务实例的机器上，执行 ohpm-repo pack <deploy_root>。
该命令用来打包备份ohpm-repo的 <deploy_root>/conf，<deploy_root>/meta 目录，并在命令行工作目录下生成压缩包。
打包成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.98595397421206323312868691017226:50001231000000:2800:8ECCDDE4E8BD50DB26CE73DDA3B309255F0A3BA388AFB7D1085860ADDC76CC33.png?needInitFileName=true?needInitFileName=true)
部署
将 pack 命令的产物拷贝到其他机器中。在解压ohpm-repo压缩包后，使用 ohpm-repo deploy <file_path> 命令部署新的实例。
部署成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.82979833051036729212318226517604:50001231000000:2800:F39822B49A46F58E25477B3C969BD54027746F70F835DF8BE5CE77F2C0BD1106.png?needInitFileName=true?needInitFileName=true)
部署成功后可执行 ohpm-repo start 启动ohpm-repo。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.22492215809876455618146935100382:50001231000000:2800:FFCE2FCC119F367616CE101B1E318976B663337E43F53EF2309041E90B15DC23.png?needInitFileName=true?needInitFileName=true)
配置自动重启（可选）
为ohpm-repo实例配置系统重启时自动重启的功能。
在进行该配置前需要将 ohpm-repo 工具 bin 目录配置到环境变量path中。
Linux
1.  当 mysql 或 sftp 服务与 ohpm-repo 部署在同一服务器上时，请将 mysql 和 sftp 的启动命令放在 ohpm-repo start 命令之前。
```typescript
@reboot /bin/sh run-repo.sh >/dev/null 2>&1
```
其中 run-repo.sh 表示要执行的脚本路径；>/dev/null 2>&1 表示将输出重定向到空设备，即不输出任何信息。
现在，每次系统启动时，都会自动执行 run-repo.sh 脚本中的命令。
Windows
1.  当 mysql 或 sftp 服务与 ohpm-repo 部署在同一服务器上时，请将 mysql 和 sftp 的启动命令放在 ohpm-repo start 命令之前。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.59920250406600099005616797339153:50001231000000:2800:0CF677D3C00658E9666779295A9B145F0AA9BBACD4DEE15CE67219FA240CA29D.png?needInitFileName=true?needInitFileName=true)
现在，每次系统启动时，都会自动执行 run-repo.bat 脚本中的命令。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-web-introduction-V14
爬取时间: 2025-04-30 21:57:58
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-web-front-page-V14
爬取时间: 2025-04-30 21:58:36
来源: Huawei Developer
ohpm-repo私仓从5.0.2版本开始，新增接口防重放攻击机制。请保持ohpm-repo私仓部署的服务器与访问ohpm-repo私仓管理界面的客户端机器时间同步。如出现访问页面报错“非法请求”，请参考FAQ解决。
启动 ohpm-repo 私仓后，可以通过浏览器访问ohpm-repo页面，访问路径为http://<机器IP>:<监听端口>。
其中，http是ohpm-repo的默认网络协议，可以在配置文件中进行修改。<机器IP> 是部署ohpm-repo服务器的IP地址，<监听端口> 是ohpm-repo配置文件中 listen 选项所设置的监听端口。
例如，将ohpm-repo部署在 IP 为 192.168.10.10 的服务器上（如不清楚部署ohpm-repo服务器的 IP，可在 Linux 上运行ifconfig 命令，Windows 上运行 ipconfig 命令查看），同时ohpm-repo配置文件的 listen 选项配置为 0.0.0.0:8088，此时访问ohpm-repo页面的 URL 就是 http://192.168.10.10:8088。
ohpm-repo会自动创建默认管理员账号，账号名称：admin，账号密码：12345Qq!。为保证ohpm-repo账号安全，该账号在首次登录时，强制修改该密码，请设置新密码后重新登录。
首页
首页主要展示当前 ohpm-repo 私仓存储的包信息，同时提供搜索功能，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.71820217002931210520126069819115:50001231000000:2800:D92B28BA91D914F912A165E8E29A5743C44E5EAA69FD2493DB201228C93D1CD7.png?needInitFileName=true?needInitFileName=true)
包详情页
包详情页主要展示当前包的详细信息，这些信息主要来源于包的内部文件，同时记录了包的版本信息和下载量数据，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.62428663869492245192284226816010:50001231000000:2800:86CFC72B2E43F99062B4DC25B666C4E7E1B6A2A35632896323EB333316E8FADF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-web-user-center-V14
爬取时间: 2025-04-30 21:59:09
来源: Huawei Developer
个人中心主页是 ohpm-repo 私仓的核心管理页面，整个系统在此进行集中管理和操作，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.40552461671615547344296554224199:50001231000000:2800:2FAC7523271D28D964F7F1B127DF8632F94B9691B599B2CBD316F0B43595B583.png?needInitFileName=true?needInitFileName=true)
-  为保障账户安全，请勿使用简单或重复密码，并定期更换密码。
-  管理员菜单： 普通用户菜单：
-  管理员菜单：
-  普通用户菜单：
-  管理员菜单：
-  普通用户菜单：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.05808920378438099985579146612364:50001231000000:2800:0726709547778BBC46EEF102C30C5DD9A8BB8F46D6CA738622635E79FDE60C6C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.43759389085526507008079124805250:50001231000000:2800:F2241B097FB740FE153438DF36BB4F403E8B7C7265E98ADFDE4E9A8DDAC9478C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-user-management-V14
爬取时间: 2025-04-30 21:59:44
来源: Huawei Developer
存储在 ohpm-repo 私仓的包目前仅支持使用 ohpm-cli 命令行工具下载，且在下载过程中，ohpm-repo不会对下载者进行身份认证。因此，对于ohpm-repo私仓的用户管理，只需要关注和管理有发布包需求的用户即可。用户管理页面可以新增用户、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.85686453525128119797189756977547:50001231000000:2800:FC0F5A28CB388A48D5CE5DB49931EF022F826741C017A65759B81ADE4F9E7943.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.  5. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名搜索，搜索页面效果如下图所示(以指定用户类型为系统管理员，用户名为user3为例)：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.92236760028920303093136252018522:50001231000000:2800:9C0DBDAC5DBE4068939DD444B17CF9597C265C1DCAB3A905E166F5591C9B038B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.50924150188959932427574458794826:50001231000000:2800:62BCE7CCFAB5428BB92D42D2042941455688A665C05FCE5AA507E041997E0FC4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.02368896680635171647486854654876:50001231000000:2800:A82FDAE1A891137CD43526FD1254774B91C9E840480D35E6496A6D7D464CC582.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.13378458794419381027059649859787:50001231000000:2800:CD08890F3680770C201293F403ADB39F970481835478E2B7B980E3B563E57527.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.37187879502906512482367481800646:50001231000000:2800:9A7FB01DF80D381FEFD213C447E4B07A8F04FF030A4AFB997A5301C8F8288228.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-depot-management-V14
爬取时间: 2025-04-30 22:00:18
来源: Huawei Developer
仓库管理主要负责管理仓库信息，包括仓库的存储、uplink 和代理信息。
管理仓库
管理仓库页面展示当前仓库信息，包含编辑仓库和管理三方库两部分，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.15625936284233660274908578320128:50001231000000:2800:B9CAB6CE78A12303472FF03827C540879C08EC2F2DE995664D235567870E9191.png?needInitFileName=true?needInitFileName=true)
点击“编辑”按钮，进入仓库信息面板，可以修改仓库的name 、uplink和描述信息，其中uplink为下拉框选择，选项为仓库管理页面的uplinks面板配置的uplink仓库，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.40754399152652503047579814259448:50001231000000:2800:E6F1473954805178AC470B128BD0D4963F5185C091F5004826FFEF437B2924B0.png?needInitFileName=true?needInitFileName=true)
点击“管理三方包”按钮，进入仓库管理详情面板，展示所有已上传至ohpm-repo的三方包信息，管理三方库包含上传三方库包、单个包下架、批量下架和搜索三方包四个功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.68843012820283457992247237959574:50001231000000:2800:8B27C9E3BC98EFA820476E111F199306ED58A2B5FE8BB3AC6AA5DAA01FE9890F.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.  - name：支持对包名进行模糊搜索。 - version：支持输入最小版本号和最大版本号，进行版本号区间搜索。 - Publisher：支持对包发布者名称进行模糊搜索。 - Author：支持对包作者名称进行模糊搜索。 - PublishTime：支持对包发布时间进行区间搜索。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.13187402396683696603834156068346:50001231000000:2800:E7ABE76BFC6E5BA7E332C921899AE54DE7FEFAA242B543C6721FBBACCA2E66BD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.02935671513988892946573096340893:50001231000000:2800:9E0FBD3E12F99EC7659237057B2BFF9E2E907333C50A174BEDF96D1D69B08A22.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.31648750428580541557519012868131:50001231000000:2800:9F36B7189DF770E29FEF69916E2818519E18F3C4E5D318B1CEBAD4CAB3BCB625.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.22374534670852503317122056230087:50001231000000:2800:47C1C60CE418D873A072178278EDBF5FE523328EC1193B6A914C16F597F36636.png?needInitFileName=true?needInitFileName=true)
uplinks
uplink 功能可以让当前仓库获取配置的 uplink 仓库的所有包，若从某个已配置 uplink 的仓库下载当前仓库中不存在的三方包时，则会通过 uplink 仓库下载该包，如果访问 uplink  仓库需要代理，请配置好所需代理信息，uplink 页面如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.29407421620727513229651759748728:50001231000000:2800:AA308BFEAF73180F9F6100D4967C9AE95856788FA09CE774C65342E7CC697AC3.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.78315001054836874243174977772304:50001231000000:2800:8B62DB5212557153E92ABD34E05F47D1931B8166ACAD8D2690D3941B7CC7BCC6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.55993131972660207306849383578500:50001231000000:2800:63062123280E4A145AC37BE115641BD7C5C25045627C8D53111E8D8F1A16B17A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.23232575520666311605469834108297:50001231000000:2800:C25A34EADA5774F6CAA5AA6C07C68587499126C1FB3497CFF87318E5C43442F1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.51640832512338465187121732131805:50001231000000:2800:551E486D618BBE0F26CE7F71A8E94643EECC13516B26139399B5693F00B37BCA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-certification-V14
爬取时间: 2025-04-30 22:00:52
来源: Huawei Developer
当前 ohpm-repo 的认证方式有证书认证和AccessToken两种方式：
证书认证：在使用ohpm客户端执行publish，unpublish或dist-tags相关命令时，通过嵌入加密ssh证书进行身份验证。
AccessToken认证：将 ohpm-repo 生成的AccessToken配置到ohpm客户端配置文件中，实现publish、unpublish、dist-tags、info和install等操作的免密认证。
证书认证
使用 ohpm 发布包时，需要先在配置文件 .ohpmrc 文件中配置 publish_id 和 key_path 。publish_id 对应发布码，key_path 对应私钥的地址，其详细发布流程见：使用命令行工具发布。认证管理主要是管理私钥对应的公钥信息，在用户使用 ohpm 发布包时进行校验。认证管理页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.61474342816840637931274817360690:50001231000000:2800:0B3A2FF68D9FFBFBF75FB2C9FB50909ADD3EE10BDB9DB72023E66487F05D3882.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.93326111794630038900577941517504:50001231000000:2800:0CD9E7ACD5E5B919A2DA7D6091F1789F4243239BEA9472CE9D21DE98067F7C7C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.50293244426518300133960578427379:50001231000000:2800:682840F3C7D545FBEEF4D28DECE85296B83E3CC4ACEF24637665163BC1132957.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.10274993267940621038448668897699:50001231000000:2800:E706403E5A3DF623CF291CEBC81557E6B416CAD2DE22D6B90DB1AEFDBBDD69FE.png?needInitFileName=true?needInitFileName=true)
AccessToken
AccessToken是 ohpm-repo 2.1.0版本新引入的认证机制（需配套使用1.6.0及以上版本的ohpm命令行工具），用户通过 ohpm-repo 界面生成Token，并将其配置至ohpm客户端配置文件中。在与 ohpm-repo 交互时，客户端会自动附带Token进行身份验证。
该Token分两种权限等级：只读Token允许执行info和install操作；读写Token除了包含只读权限外，还支持publish，unpublish和dist-tags相关操作。每位用户每种权限类型的Token最多可生成10个，首次生成时系统自动复制到剪贴板，后续不再显示完整Token内容。AccessToken页面效果如下:
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.37181454821109840968887170223039:50001231000000:2800:BC0B653D6D1AAD1F76ED43AA1A87ADD9D4D4681ECD0D6853A959CF99BB10B787.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.
5.  其中 //127.0.0.1:8088/repos/ohpm/ 是您 ohpm-repo 的registry地址去除协议名的部分，:_auth 和 :_read_auth 分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish和dist-tags操作时只会使用读写Token。每种Token最多配置三条。
6.  其中 //127.0.0.1:8088/repos/ohpm/ 是您 ohpm-repo 的registry地址去除协议名的部分，:_auth 和 :_read_auth 分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish和dist-tags操作时只会使用读写Token。每种Token最多配置三条。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.87057533473961452388656393350661:50001231000000:2800:F03400AA931F3E1528F1A50D2C3B1F6B643559B681D79C8BC87CF37D305BA9C1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.68330071656118486246821295630845:50001231000000:2800:73CA9F2C7212A74AFC39BD4ED61587A75EB4C7119781BC069CB54A1A984F73E3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.42924793626095230263766566279090:50001231000000:2800:2223BF5064108F86E670860C8FCEA78F99F18B71ECD5ECC99EC8293D38526418.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.65958405422127488440439550915331:50001231000000:2800:981D3B92E1EA06EF84BA70AC1FA9673EFA84209CD2D51EE35633293AC6434253.png?needInitFileName=true?needInitFileName=true)
1.  其中 //127.0.0.1:8088/repos/ohpm/ 是您 ohpm-repo 的registry地址去除协议名的部分，:_auth 和 :_read_auth 分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish和dist-tags操作时只会使用读写Token。每种Token最多配置三条。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-organization-V14
爬取时间: 2025-04-30 22:01:28
来源: Huawei Developer
在 ohpm 中包的命名格式为@<group>/<package_name>或者<package_name>。
其中 group 是组织，package_name 是包名。当想要上传一个含有组织（例如@ohos/axios）的包时，在ohpm-repo中需要先创建出该组织（例如ohos）才能进行上传。
在发布HAR/HSP包时，建议将组织名称包含在包名（package_name）中，便于管理和识别三方库。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.04652403786802588425644812815042:50001231000000:2800:EE231F50EE30F906F6E814428F02A1A6828DFDD6CC6EFCA451BC8C9722272444.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.46451647894857348835830509648637:50001231000000:2800:C8215B2F1C3F2EDD6F8C13C300DDCC5910F700D10A12AE1C2377B77B5AF37156.png?needInitFileName=true?needInitFileName=true)
1.
2.  描述：展示组织的基本信息。 包：展示该组织下仓库所上传的所有包信息。 点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
3.  描述：展示组织的基本信息。
4.  包：展示该组织下仓库所上传的所有包信息。
5.  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
6.
7.
8.  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。
9.  点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.22898963826309196340234827049500:50001231000000:2800:BAD94DCFC6C574555BCB44645F50880F30E7C1D15A0218CA5B981565F514AF61.png?needInitFileName=true?needInitFileName=true)
-  描述：展示组织的基本信息。
-  包：展示该组织下仓库所上传的所有包信息。
-  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
-
-
-  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。
-  点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.90028420384771095752341450081102:50001231000000:2800:B51B4AB1C2E88C937DB56779AFAEAFB2BD2AAF4E93085D615585CCBD857146C3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.67429640005924547702003471606932:50001231000000:2800:443EE52F4D68E09BC15CEDA4BDD9E40D78880ECEC3CB3FBEA3C785FE7C49D972.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.26091553908006047211584655317127:50001231000000:2800:09FC44091AD5A59D5CDAD383D6CD36939BE785770C68EDE9A7FA0BA8B1F83E10.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.38366375684456243219149614644566:50001231000000:2800:B47FE1EAE2F6C6496B9C0F51AD28487D2732C057EBCA07A95ACD4144BDD8E0BF.png?needInitFileName=true?needInitFileName=true)
-  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。
-  点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.71124109784006110231942555875248:50001231000000:2800:CC0D998D46C33ABE72963AF5772787FC88C576E1CB523392DC4E4517CC34EAAF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.21532950519167126563398931249618:50001231000000:2800:8BC18AC1D226B6C45B5F072ED5AA52DA9CB7749F5CF8EB1411E9A348E5DE2E31.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.59001859983751297041938698372534:50001231000000:2800:66A90AA27A229AD9217A039D51D73395B5FF3FD18765ED1B635845A36DF8B67D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.63606025364365585868516490821997:50001231000000:2800:3E4EA46B07CD20F894077642BAC144088E912D33C6C0CFD1898BA3C1C9D3A484.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.55021919619868174969312501856742:50001231000000:2800:78EAAC02A69E780B843429B7533760118EC0D079C69CC64B5B185076C49365A4.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.77075001964110236487646602926660:50001231000000:2800:07B6BB151447DD1DD79D0A701CFF625F79E14E5AC9A89A8681C7D26B738AFCEF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.58053739886164357483033387410505:50001231000000:2800:99774BE8E8CB6A36A8B2D013BA834731932FA0971B5F7F0A219B55524CE3562D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.47900642351136772255227672070848:50001231000000:2800:70E266F96BC71336F3CEBD7CBB48D8B89CA62753AD05C3078DE26E681BF7AD9E.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-operation-log-V14
爬取时间: 2025-04-30 22:02:01
来源: Huawei Developer
操作日志界面显示用户通过ohpm-repo管理界面进行的所有操作，以及通过ohpm命令行工具执行publish，unpublish和dist-tags等相关命令所记录的日志。操作日志界面分为两个部分：第一部分为筛选条件，第二部分是展示符合筛选条件的数据。
操作日志的数据每隔一天会定时清除，默认保留100天内的操作日志数据，数据保留时间可通过config.yaml中配置项operation_log_retention设定。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.28890655523445467389112246895663:50001231000000:2800:8D88169A6B79F7033E42B855C7196A6294E2775DFCCFA35ACF10996E6ABF0802.png?needInitFileName=true?needInitFileName=true)
-
-  一级事件类型 二级事件类型 三级事件类型 用户管理 新增用户 - 删除用户 - 修改用户角色 - 重置用户密码 - 仓库管理 管理仓库 更新代码仓 上架资源包 下架资源包 uplink 更新Uplink代理 添加Uplink 修改Uplink 删除Uplink tag 增加Tag 更新Tag 删除Tag 认证管理 证书认证 添加发布公钥 删除发布公钥 Access Token 生成Access Token 删除Access Token 组织管理 组织 添加分组 修改分组 删除分组 组织成员 添加组成员 删除组成员 组织管理员 添加组管理员 删除组管理员 系统设置 更新oh-package.json5检查规则 - 重置系统秘钥 - 更新系统安全配置 -
-
-  一级事件类型 二级事件类型 三级事件类型 用户管理 新增用户 - 删除用户 - 修改用户角色 - 重置用户密码 - 仓库管理 管理仓库 更新代码仓 上架资源包 下架资源包 uplink 更新Uplink代理 添加Uplink 修改Uplink 删除Uplink tag 增加Tag 更新Tag 删除Tag 认证管理 证书认证 添加发布公钥 删除发布公钥 Access Token 生成Access Token 删除Access Token 组织管理 组织 添加分组 修改分组 删除分组 组织成员 添加组成员 删除组成员 组织管理员 添加组管理员 删除组管理员 系统设置 更新oh-package.json5检查规则 - 重置系统秘钥 - 更新系统安全配置 -
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.61388748870877607273059552799658:50001231000000:2800:0479E39D5F628B40290810D4F91EED59860067B233C3D88ACD5A65BCC5F59481.png?needInitFileName=true?needInitFileName=true)
-
-  一级事件类型 二级事件类型 三级事件类型 用户管理 新增用户 - 删除用户 - 修改用户角色 - 重置用户密码 - 仓库管理 管理仓库 更新代码仓 上架资源包 下架资源包 uplink 更新Uplink代理 添加Uplink 修改Uplink 删除Uplink tag 增加Tag 更新Tag 删除Tag 认证管理 证书认证 添加发布公钥 删除发布公钥 Access Token 生成Access Token 删除Access Token 组织管理 组织 添加分组 修改分组 删除分组 组织成员 添加组成员 删除组成员 组织管理员 添加组管理员 删除组管理员 系统设置 更新oh-package.json5检查规则 - 重置系统秘钥 - 更新系统安全配置 -
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.87652258951728978388016801849468:50001231000000:2800:0FB5A3B1A9B35B01BE5003AA51A1B8AD66B2B85B6752A80CD587C37839A8CC95.png?needInitFileName=true?needInitFileName=true)
| 一级事件类型  | 二级事件类型  | 三级事件类型  |
| --- | --- | --- |
| 用户管理     | 新增用户  | -  |
| 删除用户  | -  |
| 修改用户角色  | -  |
| 重置用户密码  | -  |
| 仓库管理           | 管理仓库    | 更新代码仓  |
| 上架资源包  |
| 下架资源包  |
| uplink     | 更新Uplink代理  |
| 添加Uplink  |
| 修改Uplink  |
| 删除Uplink  |
| tag    | 增加Tag  |
| 更新Tag  |
| 删除Tag  |
| 认证管理     | 证书认证   | 添加发布公钥  |
| 删除发布公钥  |
| Access Token   | 生成Access Token  |
| 删除Access Token  |
| 组织管理        | 组织    | 添加分组  |
| 修改分组  |
| 删除分组  |
| 组织成员   | 添加组成员  |
| 删除组成员  |
| 组织管理员   | 添加组管理员  |
| 删除组管理员  |
| 系统设置    | 更新oh-package.json5检查规则  | -  |
| 重置系统秘钥  | -  |
| 更新系统安全配置  | -  |
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.68729163888615171005897257456449:50001231000000:2800:85249D9F26563CFDF035F81B544F16AD546F81FA0CFDF97F6E8867261BA1A709.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.36310381444171648244980840373607:50001231000000:2800:C44F4B464332FB923B166E71A831D02C670559B01B380B74B828E4ED64CEB1C9.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.73003638034581421181235223647258:50001231000000:2800:643A3D0DDD28C8716D022119D4097A4ACCB2613F7ACF25EBF398B05B7B7EFE38.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-system-settings-V14
爬取时间: 2025-04-30 22:02:35
来源: Huawei Developer
系统设置是ohpm-repo系统层面的管理，当前支持"oh-package.json5检查规则"和"系统安全"两大功能。
oh-package.json5检查规则
oh-package.json5检查规则是ohpm-repo对上传包的oh-package.json5文件进行校验的规则管理。当前主要针对category，repository和name三个字段设定规则。
category白名单：若其为空，系统将不会对category字段进行校验。若配置了值，则category字段的值就必须存在于白名单中。
repository：决定repository字段在oh-package.json5文件中是否必须存在。如果设置为必须，那么在上传包时，oh-package.json5文件中就必须包含repository字段。
name：oh-package.json5文件中name字段是否必须包含组织名，如果设置为是，则上传包时，则name字段必须包含组织名，无组织包将会上传失败。
页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.79989450484704659842819681170190:50001231000000:2800:9555D0FA86F7669DE482DB5258183675504EF510CF4D4E123DD02E7A11351342.png?needInitFileName=true?needInitFileName=true)
系统安全
系统安全页面中有两部分配置项：重置系统秘钥和配置是否支持匿名访问。页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.22974414700588881773588544757764:50001231000000:2800:373ED5DB85633E8E84C6991D00CE9E3A646C10BDFD62C39E08B715DA5CFD4FED.png?needInitFileName=true?needInitFileName=true)
系统密钥用于重新加密ohpm-repo服务中用户上传的公钥和uplinks的网络代理口令信息。点击重置系统密钥，将出现重置提示，如果确定重置，需要点击按钮“是”，将出现密码输入框，由于重置系统秘钥是敏感操作，故需要输入当前登录账户的密码进行再次认证，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.57021211267402708891796795831540:50001231000000:2800:D7C2BDB930EFD182EC7E0BFB36521C88B52C946243173671F91EF9F985120C35.png?needInitFileName=true?needInitFileName=true)
2. ohpm-repo匿名访问配置
ohpm-repo从5.0.5版本开始支持配置匿名访问功能。默认情况下，ohpm-repo支持匿名访问。如果需要配置不支持匿名访问，需要点击按钮“否”后提交，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.80541995023107263020989373783261:50001231000000:2800:0A4F67E5F4EC1AD52672EE54669AF144A8ADD7C87CC1B9387315A5BF922000A1.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.60874788798543763418936300299703:50001231000000:2800:FF6B9C5415EB1A25413DF3305A4733A31BCAC17D6C894217D84A764F4E25B720.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-configuration-guide-V14
爬取时间: 2025-04-30 22:03:12
来源: Huawei Developer
为了保障用户在使用ohpm-repo过程中更加安全可靠，我们收集如下推荐安全配置项，用户可以根据自己的需要采纳配置。
最小权限启动
为降低风险，提高系统的稳定性和可维护性，ohpm-repo必须使用非root权限进行启动部署。
加密连接和监听具体地址
多实例部署
ohpm-repo用于存储私有仓库三方包数据，为了避免数据丢失，且保证ohpm-repo的高可用性，推荐元数据存储使用mysql，包数据存储使用自定义存储插件，通过使用负载均衡，部署ohpm-repo多个实例。
Mysql存储
参考配置如下：
自定义存储
使用自定义插件存储，具体配置为：
参考配置如下：
禁止匿名访问
在默认设置下，ohpm-repo仓库中的所有包信息均可供任意用户自由查看，且包文件也支持任意用户下载。为了避免不相关的人访问ohpm-repo，我们建议在ohpm-repo管理界面的系统设置>系统安全页面，关闭匿名访问功能（默认保持开启）。关闭后，只有在.ohpmrc文件中正确配置仓库只读或读写AccessToken的用户才能够通过ohpm工具下载三方包，只有登录ohpm-repo账户，才能够访问ohpm-repo管理界面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.25566523837202326515912232031060:50001231000000:2800:85A357DFBB5D4D7789E440E881DA26BBB49B054601AE5E8B567F779FE612F523.png?needInitFileName=true?needInitFileName=true)
用户访问频率控制
为了避免恶意用户频繁对仓库进行访问操作，我们在配置文件中设置配置项user_rate_limit，默认单个用户访问接口的频率为100次/秒，配置范围为 (0, 10000]。
用户上传次数控制
为了避免恶意用户频繁发布三方包，我们在配置文件中设置配置项upload_max_times，默认单个用户24小时内上传次数限制为100次，配置范围为 (0, 100000]，用户可以根据自身业务需要修改此配置值，如改为1000次。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-faq-V14
爬取时间: 2025-04-30 22:03:45
来源: Huawei Developer
ohpm-repo私仓工具获取与升级
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.99993342738547533059912223577028:50001231000000:2800:975A49213925C86AD2A2C356E19655E8E0027F5E10B799E2EA4CE67DF6B9DAE0.png?needInitFileName=true?needInitFileName=true)
ohpm-repo启动后如何修改配置文件，并使得修改后配置文件生效
ohpm-repo部署目录和ohpm-repo解压目录说明
-  ohpm-repo解压目录：<binary_root>，ohpm-repo安装包解压后所在的根目录，存放的是ohpm-repo压缩包解压后的内容；
-  ohpm-repo部署目录：<deploy_root>，ohpm-repo运行时产生数据的存储位置，包括配置文件，日志文件，加密组件等信息。ohpm-repo部署目录在不同版本有不同的配置方法。
-  ohpm-repo部署目录默认路径如下： ohpm-repo部署目录和ohpm-repo解压目录不要放在同一目录中。
ohpm-repo 的权限管理
账户权限：系统管理员和系统普通用户
1.  账户的注册 ohpm-repo注册的账户有两种类型：用户类型和管理员类型。ohpm-repo初次启动默认有一个管理员账户：账户名:admin；密码:12345Qq!。
2.
3.
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.67178619321422403544069710993902:50001231000000:2800:C3109330E1E4FC535E9633354E18C650F072E7BD5EDA9C440CDF72117814F442.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.90975314662078308155794478696249:50001231000000:2800:01C461C8B04C84BE4C9730424BC07ED106FB4F6A6B10F1DC0648547ACEFE50AE.png?needInitFileName=true?needInitFileName=true)
组织权限：组织成员和组织管理员
1.
2.
3.
4.
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.89456321046649874225459486757585:50001231000000:2800:590E8F051C6101BA41BCEBF0DC8ACC69921F60D98B27DF6713C121F4AFE47722.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.47321712053997458722000800725764:50001231000000:2800:5CC59BFF7F9D497A5C88C36F263E46DF70A83796F08618799A26EE6BDBBC0A41.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.66572876615675872090440626633559:50001231000000:2800:AA7EBBEAA3F3E8A06F1B35A4761CFACDA6204C42CAA1B0914F449E51649E11FD.png?needInitFileName=true?needInitFileName=true)
上传包和卸载包权限管理
三方包可以分为有组织的包和没有组织的包两类，上传和下架包可以通过ohpm-repo和ohpm命令行工具两种方式操作。
ohpm-repo 的元数据与三方包数据管理
元数据与三方包数据介绍
ohpm-repo的数据包括两部分：
元数据和三方包数据存储方式介绍
-  元数据和三方包数据的存储方法不能够随意搭配，匹配规则和支持的ohpm-repo版本信息见下图： 存储方式的变更：如果元数据和包数据的存储位置需要改变，可以通过数据迁移指导进行完成。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.07422447522451821687793401008277:50001231000000:2800:B32A334E0004AF75834C4E6E1C5F0D392F145379BF0AAA52577173F722D8CF7F.png?needInitFileName=true?needInitFileName=true)
ohpm-repo认证方式
ohpm在执行publish，unpublish和dist-tags等需要修改ohpm-repo数据库内容命令时，需要获取读写权限才能够操作。
从ohpm-repo5.0.5版本开始，如果ohpm-repo配置不支持匿名访问，ohpm在执行install，info和update命令时需要通过AccessToken认证或者自定义AccessToken认证方法，正确配置读写/只读AccessToken信息获取读权限。
认证方式说明
认证失败FAQ
使用证书认证执行publish/unpublish/dist-tags等命令失败
使用证书认证在 git-bash 终端下执行 ohpm publish XX.har 发包到ohpm-repo中报错：The content of private key in the key_path error
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.76822431905860292076527195910178:50001231000000:2800:95D72A16380609062D3D4978FF907DE4D0E9EB524D36EAC8D8B19687D3BC8F31.png?needInitFileName=true?needInitFileName=true)
使用AccessToken认证，执行publish/unpublish/dist-tags等命令失败
应用内 hsp 包如何发布到ohpm-repo
执行ohpm-repo命令报错
在执行ohpm-repo install 或者 ohpm-repo start 的时候报错：server install failed: YAMLException: bad indentation of a mapping entry
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.62195555874782554915765642801878:50001231000000:2800:479A3FB17425C41233D33CF7943CB9BE3D607D4B3765F37387FBC1806C5A4FED.png?needInitFileName=true?needInitFileName=true)
ohpm-repo的配置文件config.yaml 中配置缩进格式不对，并且在报错信息中会提示出错误的位置。
执行命令 ohpm-repo <command>，报错 ohpm-repo 不存在或者 <command> 命令不存在。
ohpm-repo成功启动后，根据配置文件中的 listen 值访问ohpm-repo私仓管理界面，界面不显示信息或者无法打开页面
机器A部署ohpm-repo私仓服务，在机器B上通过A的域名+端口访问已部署的ohpm-repo私仓服务，打开包的描述页出错
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.29365039130470205345019936500860:50001231000000:2800:22E8F2DFD03A0800A6CA3FE17023C8C122D04BA9BF64C3B52C14145E6845EFB3.png?needInitFileName=true?needInitFileName=true)
执行ohpm-repo install 时报错：fail to initialize encryption component: Error: invalid crypto component.
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.39091164227388031673138364646063:50001231000000:2800:887AFF9896CD75A98BCAFDAB4F200A9F54C6CB837FEBE75331F0F5997DD6F0FF.png?needInitFileName=true?needInitFileName=true)
执行 ohpm publish XX.har 发包到ohpm-repo私仓中报错
报错：connect ECONNREFUSED ::1:8089
报错：The content of private key in the key_path error.
报错：HttpCode 400 Group does not exist!
-  现象：ohpm执行publish命令，命令行报错信息为 HttpCode 400 Group does not exist!
报错：HttpCode 400 You are not a developer of the group!
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.56342109341626475584547559690854:50001231000000:2800:4372398F42AB4AB9A140250AD7227E36110A9B07E9712B0E9A33FAA598873855.png?needInitFileName=true?needInitFileName=true)
报错：ohpm ERROR: HttpCode 404 Not Found
报错：Same ohpm package is exists!
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.93781224266523214892811543543934:50001231000000:2800:1C90E64518E4360A7CB844E97069408E2CB5C7B69614711D44594076CBB393B0.png?needInitFileName=true?needInitFileName=true)
报错：Request Entity Too Large
报错：The packageType is no equals the exists packageType!
执行 ohpm install XX.har 从ohpm-repo私仓中下载包报错
ohpm-repo配置uplink后，执行install命令下载uplink所配置仓库中的包失败
-
-  上述地址，网络协议均为 https ,端口均为 443。
-  上述地址，网络协议均为 https ,端口均为 443。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.93186205056932556485669160293698:50001231000000:2800:86B4B12ABE306FD4905B8AD524A8B48EACC6A29800261F0487FBF8AADE94E934.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.07835176637135841769036363526813:50001231000000:2800:7EBE514305DE3FB16541CD6DECE1FD0F194CC20B3FB44CACFE256EF876914EB3.png?needInitFileName=true?needInitFileName=true)
-  上述地址，网络协议均为 https ,端口均为 443。
访问ohpm-repo私仓管理界面报错
访问ohpm-repo私仓管理界面中页面功能，报错：非法请求
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.53094070362500686185386858688234:50001231000000:2800:DDC331FFDA0D3B361A6BC8A1E94CDE70A7A8A37F441D6ABF194E307A6669D719.png?needInitFileName=true?needInitFileName=true)
访问ohpm-repo私仓管理页面，报错“加密组件无效”。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.50807282833957598925237071508435:50001231000000:2800:AB441D50A1BBB304CB91C300115D5EF3A97CD30855A318C1085F7911834FD997.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.00385739513731281193454242385945:50001231000000:2800:B6C224DD737E0F5440E8698208A35EED937D2CF8A02B02BA417A779E5F7A41DF.png?needInitFileName=true?needInitFileName=true)
访问ohpm-repo私仓管理界面，报错：“系统配置错误，请联系管理员“
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.45236911772928587159279674099605:50001231000000:2800:B5BFBFE96D8C760085D5903538903DDA555F97A04788540A55B589716AA8E78E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.79657083526955407196787058822091:50001231000000:2800:D86E0E1EA8225AD6156930969DF08FD7C8F1BE32FADD18CED69E420F6C2C44CD.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-appendix-V14
爬取时间: 2025-04-30 22:04:20
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-historical-version-V14
爬取时间: 2025-04-30 22:04:54
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-overview-history-V14
爬取时间: 2025-04-30 22:05:28
来源: Huawei Developer
ohpm-repo 是一个搭建轻量级的 ohpm 私仓服务的工具。它与 ohpm 包管理器兼容，并按需缓存所有依赖项，加速私有网络中的安装。
私有性
您所发的三方库都是私有的，只能根据您的配置进行访问。
缓存
ohpm-repo 根据需要缓存所有依赖项，加快私有网络的安装速度。
部署
ohpm-repo 支持单点部署和多实例部署。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-quickstart-history-V14
爬取时间: 2025-04-30 22:06:02
来源: Huawei Developer
如何安装
ohpm-repo
1.  下载 ohpm-repo 工具包，点击链接获取。
2.  解压文件，进入文件 bin 目录下，执行安装脚本 setup.bat(windows) 或者 setup.sh(linux/macos)。
3.  安装完成之后，进入解压文件 bin 目录下，执行如下命令： 终端输出为版本号（如：1.0.1），则表示安装成功。 若想在其他目录使用 ohpm-repo，请将 ohpm-repo工具包解压目录中 bin 目录的路径配置到系统环境变量 path 中。
4.  在启动 ohpm-repo 前还需要先按照如下方式完成配置修改，进入 ohpm-repo 的安装目录下的 conf 目录，打开 config.yaml 配置文件；
5.  检查 listen 配置，当配置为 localhost:8088 时表示仅支持监听本机地址；如果希望局域网内其他机器均可访问，则建议修改 listen 配置为监听所有地址：
6.  检查是否配置了 store.plugin_config.server，若没有配置，则在运行时该配置会自动设置成 listen 配置的值；若 listen 配置为监听所有地址 listen: 0.0.0.0:8088，则该值需要配置为详细地址，如： 如果为ohpm-repo服务配置了反向代理服务器，则该地址需要填写为反向代理服务器的地址。 config.yaml中各项配置的详细描述请见：配置文件
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.59647315904884147146151011131917:50001231000000:2800:5EEBE3AD4DF435874F4D2253F7F3AFB12C2F6F906F7D8B42DCF5F8AC6D93A794.png?needInitFileName=true?needInitFileName=true)
如何启动
完成配置修改后，进入安装 bin 目录下，执行如下命令，启动 ohpm-repo：
启动成功，将会出现以下日志信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.41933707321648791551433008666261:50001231000000:2800:D11DA3833F8901CFCD81AE1529DD33C93C3150EB92C7B168612A3A832BAB735F.png?needInitFileName=true?needInitFileName=true)
ohpm-repo 首次启动时，默认创建一个管理员账号，账号名称：admin，密码：12345Qq! 。该账号在首次登录时，需要修改其密码，请您修改密码后，重新登录该账号。
从ohpm-repo获取三方库
您可以为所有项目配置该私有仓，例如执行以下命令：
或者在命令行中配置参数 --registry 使用，例如以下命令：
<配置的ohpm-repo服务地址> 为配置文件中的 store.plugin_config.server 地址信息，此处需要完整的地址格式，例如：http://127.0.0.1:8088，故 registry 为：http://127.0.0.1:8088/repos/ohpm
将三方库发布到ohpm-repo
使用命令行工具发布
1.  示例： 公钥和私钥存储在 D 盘 的path 目录下，公钥和私钥名称分别为 my_key_path.pub和my_key_path。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.79712070593057991968948484935005:50001231000000:2800:B1DB756CFAE918A583677902DE366C2959084896293A7E4078AA1B901A011620.png?needInitFileName=true?needInitFileName=true)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.28991094437642272706556848389217:50001231000000:2800:BD906B77003A60DCF9BC39144FD18ADEE70190413C589090F084C53A222BD2E6.png?needInitFileName=true?needInitFileName=true)
1.  或在命令行中配置参数 --publish_registry 使用，例如以下命令：
命令行工具支持发布 HAR 包和 由 HSP 模块打包出来的 TGZ 包，TGZ 包的发布流程与 HAR 包一致。更多详细内容请参考：开发及引用共享包。
使用Web页面发布
在Web页面用管理员账号登录ohpm-repo，在个人中心 > 仓库管理中，点击管理三方包 > 上传三方包。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.22984055648339705064976345612938:50001231000000:2800:79F33EAEE57ADC149B498860B0C2A1DF905A8C625E0A924D34281739C1C4E2FB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.69342083921433746786084285642324:50001231000000:2800:7AF547D3D8C8A07771A535C1C59DB5997FDCDF7A7558F6BBFCFE20A3B2B7EE22.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-configuration-history-V14
爬取时间: 2025-04-30 22:06:35
来源: Huawei Developer
config.yaml 是 ohpm-repo 的重要文件，您可以在其中修改默认参数配置，启动插件或者扩展功能。ohpm-repo 在解压包的conf目录下带有一个默认配置文件 config.yaml，ohpm-repo 启动时默认读取该文件。
默认配置
目前发布的版本有两个，分别为 1.0.1 和1.1.0，配置文件内容存在不同：版本1.1.0 新增支持日志路径配置，数据存储 mysql 配置和文件存储 sftp 配置等。
ohpm-repo 1.0.1版本
ohpm-repo 1.1.0版本
配置项说明
listen
格式为三段式，即 <proto>: //<host>: <port>，其中 <proto> 可以不填，默认为 http，如：
-  监听本机回环地址：
-  监听所有地址：
proto 支持 http 和 https 协议，且支持缺省，缺省时默认为http。如果您配置为 https协议，则需要完善 https 相关配置。
https
当您在配置 listen 时选择使用 https 协议，则需要配置 https.key 和 https.cert：
为了确保ohpm-repo链接的安全，建议您选择使用 https 协议，您可以使用如下命令生成 https 协议使用的证书私钥文件和证书文件：
参考配置如下：
server
服务相关配置，具体为：
-  fetch_timeout: 当使用 uplink 时，请求 uplink 数据的请求/响应超时时间，单位为秒，默认60 秒，取值范围为 (0, 3600]。
参考配置如下：
1.1.0 版本额外添加一个参数 api_timeout， 默认值取 60。
db
ohpm-repo运行过程产生的用户信息，运行状态等数据存储配置，支持本地磁盘存储和 mysql 存储。
本地磁盘存储
默认使用本地磁盘存储，配置如下：
-  path: 数据存储地址，默认值为 ./db ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
-  path: 数据存储地址，默认值为 ./db ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
-  path: 数据存储地址，默认值为 ./db ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
如果想修改数据存储路径同时保留旧的数据，则需要把旧路径下的数据文件迁移至新路径。
参考配置如下：
Mysql存储
ohpm-repo 从 1.1.0 版本开始支持使用 mysql 存储。
-  database: 数据库名。 参考配置如下：
-  database: 数据库名。 参考配置如下：
-  database: 数据库名。 参考配置如下：
store
三方库及其元数据等资源文件存储配置，支持本地磁盘存储和 sftp 存储。
本地磁盘存储
默认使用本地磁盘存储文件，具体配置为：
-  path: 存储根目录路径，默认为 ./storage ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
-  path: 存储根目录路径，默认为 ./storage ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
-  path: 存储根目录路径，默认为 ./storage ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
参考配置如下：
Sftp 存储
ohpm-repo 从 1.1.0 版本开始支持使用 sftp 存储文件，仅当数据存储为mysql 存储时才能使用sftp 存储。
参考配置如下：
uplink
-  store_path: 远程包缓存路径，默认路径为 ./uplink，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
参考配置如下：
logs
ohpm-repo 从 1.1.0 版本开始支持 logs 自定义配置。
-  logs_path: 日志存储，默认路径为 ./logs ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
参考配置如下：
loglevel
loglevel 自定义配置，具体配置为：
参考配置如下：
关于 deploy_root
deploy_root 为ohpm-repo的部署目录，需要注意的是：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-log-history-V14
爬取时间: 2025-04-30 22:07:09
来源: Huawei Developer
与任何 web 应用程序相同，ohpm-repo 有一个内置的日志记录器，其定义了四种日志类型。
访问日志 - access.log
访问日志中主要包含操作时间、服务器 ip、操作源、操作结果以及请求接口或者请求静态资源，其文件保存个数最多为 180 个。
操作日志 - operate.log
操作日志中主要包含操作时间、操作人、终端 ip、操作方法名以及操作结果，其文件保存个数最多为 180 个。
运行日志 - run.log
运行日志中主要包含操作时间、日志级别以及日志信息，其文件保存个数最多为 30个。运行日志定义了日志级别：all，trace，debug，info，warn，error，fatal，mark 和 off。
下载错误日志
当从仓库中下载某个包失败时，仓库会生成一条错误日志记录在数据库中的 downloadfailure 表中，当为ohpm-repo配置了 sftp 存储服务时，从任意一个sftp 服务中下载失败时，都会生成一条错误日志并保存。每条日志都有 handled 标识，handled 为 0 时表示已处理，handled 为 1 时表示未处理。
日志存储路径
日志存储的默认路径为 ./logs
-  1.1.0 版本开始支持在配置文件中自定义日志存储路径。
-  在ohpm-repo start或ohpm-repo deploy启动时，如果指定 <deploy_root> 参数，以上相对路径基准为指定的 <deploy_root>目录。
-  如果没有指定 <deploy_root> 参数，则相对路径基准为： windows系统: ~/AppData/Roaming/Huawei/ohpm-repo 其他操作系统：~/ohpm-repo
日志打印级别
在配置文件中可以设置访问、操作、运行日志的打印级别，日志将会只打印不低于设置级别的日志，日志级别由低到高为：all，trace，debug，info，warn，error，fatal，mark 和 off。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-command-history-V14
爬取时间: 2025-04-30 22:07:45
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-help-history-V14
爬取时间: 2025-04-30 22:08:19
来源: Huawei Developer
获取有关 ohpm-repo 的帮助。
命令格式
参数
功能描述
-  如果提供了命令名称，则显示相应命令的帮助信息。
-  如果提供的命令名称不存在或未提供，则显示所有命令的概要信息。
示例
执行以下命令：
结果示例：
1.0.1：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.48073824147363634063250661788112:50001231000000:2800:817E5A757EA9F40F2FB5A0B9845024C9A26C8F2FB17653BB9E7C3A8C16E2F3AB.png?needInitFileName=true?needInitFileName=true)
1.1.0：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.86111557335935457990030054761187:50001231000000:2800:DF50C23C0F2AB949101FBF42707297139B05473D5E87A674EA1ECE25C352A461.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-start-history-V14
爬取时间: 2025-04-30 22:08:53
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-start101-history-V14
爬取时间: 2025-04-30 22:09:26
来源: Huawei Developer
启动ohpm-repo服务。
命令格式
功能描述
用于启动ohpm-repo服务，创建一个ohpm-repo实例。
选项
listen
您可以在 start 命令后面配置 --listen <string> 参数，指定启动端口和绑定访问地址，优先级高于 config.yaml中 listen 的配置。listen 参数可以指定协议 http 或者 https，若指定为 https，config.yaml文件中必须配置证书。若不指定，默认为 http。
config
-  <binary_root>：ohpm-repo 项目根目录
您可以在 start 命令后面配置 --config 参数，指定配置文件路径，仅支持绝对路径配置。
执行 start 过程中，会把读取到的配置文件拷贝至相对路径 /conf/config.yaml 内。其中相对路径的基准根目录为：
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.24765951722449525041231702089526:50001231000000:2800:16789BB14F1FEBAFE60DF9206B18A0589C7CF525585EB761591A7A3F4E298267.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-start110-history-V14
爬取时间: 2025-04-30 22:10:00
来源: Huawei Developer
启动ohpm-repo服务。
命令格式
功能描述
用于启动ohpm-repo服务，创建一个ohpm-repo实例。
-  第一次启动ohpm-repo后，ohpm-repo工具目录下生成 .deploy_root 文件。如果后续您想更改部署路径，可以先删除 .deploy_root 文件，并在start 命令后面配置 config、crypto_path、deploy_root 参数。
-  如果首次启动停止后，再次启动，指定了 config、crypto_path、deploy_root参数，则参数会直接被忽略，默认根据 .deploy_root 文件记录的部署根目录去加载配置和加密组件。
选项
listen
您可以在 start 命令后面配置 --listen <string> 参数，指定启动端口和绑定访问地址，优先级高于 config.yaml中 listen 的配置。listen 参数可以指定协议 http 或者 https，若指定为 https，config.yaml文件中必须配置证书。若不指定，默认为 http。
config
-  <binary_root>：ohpm-repo 私仓工具包解压目录。
您可以在 start 命令后面配置 --config <string> 参数，指定配置文件路径。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。
执行 start 过程中，会把读取到的配置文件拷贝至路径 <deploy_root>/conf/config.yaml 内。
crypto_path
您可以在 start 命令后面配置 --crypto_path <string>参数，指定ohpm-repo运行时使用的加密组件。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。如果不配置crypto_path，当 <deploy_root>/meta 路径下不存在加密组件时，会自动生成新的加密组件。
执行 start 过程中，会把读取到的加密组件拷贝至路径 <deploy_root>/meta 内，不配置该参数，新建的加密组件也会保存在此处。
deploy_root
您可以在 start 命令后面配置 --deploy_root <string> 参数，指定ohpm-repo部署的根目录。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.23884131673900365631744839997031:50001231000000:2800:B60B72B06384902C2A56E5D9DACE70ABECCF3A96B2EE68B875BA75665DBEE0DB.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restart-history-V14
爬取时间: 2025-04-30 22:10:34
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restart101-history-V14
爬取时间: 2025-04-30 22:11:08
来源: Huawei Developer
重新启动ohpm-repo服务。
命令格式
功能描述
停止当前运行时的ohpm-repo服务，重新启动一个新的ohpm-repo服务。
选项
listen
您可以在 restart 命令后面配置 --listen <string> 参数，指定启动端口和绑定访问地址，优先级高于 config.yaml中 listen 的配置。listen 参数可以指定协议 http 或者 https，若指定为 https，config.yaml文件中必须配置证书。若不指定，默认为 http。
config
-  <binary_root>：ohpm-repo 项目根目录
-  类型： String
您可以在 restart 命令后面配置 --config 参数，指定配置文件路径，仅支持绝对路径配置。
执行 restart 过程中，会把读取到的配置文件拷贝至相对路径 /conf/config.yaml 内。
其中相对路径的根目录为：
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.38821178040381746990450551672458:50001231000000:2800:2AB938C553C1B6374F30779C7EB8E60D909BD7307F081C2763C2BFAB33704E26.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restart110-history-V14
爬取时间: 2025-04-30 22:11:42
来源: Huawei Developer
重新启动ohpm-repo服务。
命令格式
功能描述
停止当前运行时的ohpm-repo服务，重新启动一个新的ohpm-repo服务。
说明：
-  如果ohpm-repo已经启动过，再次执行 restart 重启，指定的 config、crypto_path 和deploy_root参数会被直接忽略，默认根据 .deploy_root 文件记录的部署目录去加载配置和加密组件。
选项
listen
您可以在 restart 命令后面配置 --listen <string> 参数，指定启动端口和绑定访问地址，优先级高于 config.yaml中 listen 的配置。listen 参数可以指定协议 http 或者 https，若指定为 https，config.yaml文件中必须配置证书。若不指定，默认为 http。
config
-  <binary_root>：ohpm-repo 私仓工具包解压目录。
-  类型： String
您可以在 restart 命令后面配置 --config <string> 参数，指定配置文件路径。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。
执行 start 过程中，会把读取到的配置文件拷贝至路径 <deploy_root>/conf/config.yaml 内。
crypto_path
您可以在 restart 命令后面配置 --crypto_path <string>参数，指定ohpm-repo运行时使用的加密组件。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。如果不配置crypto_path，当<deploy_root>/meta 路径下不存在加密组件时，会自动生成新的加密组件。
执行 start 过程中，会把读取到的加密组件拷贝至路径 <deploy_root>/meta 内，不配置该参数，新建的加密组件也会保存在此处。
deploy_root
您可以在 restart 命令后面配置 --deploy_root <string> 参数，指定ohpm-repo部署的根目录。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.77528182561740632162699268450277:50001231000000:2800:E52977C9917613E2E76EF57CE60E134FF450A930634DCBE8B39C847A6A861296.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-stop-history-V14
爬取时间: 2025-04-30 22:12:17
来源: Huawei Developer
停止ohpm-repo实例。
命令格式
功能描述
用于停止ohpm-repo实例。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.37895945960052545161558616840153:50001231000000:2800:99578CE4977B9BD20730BD200EED8B2776FA5FBED3BDD871220A39D74DA5FC3B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-version-history-V14
爬取时间: 2025-04-30 22:12:51
来源: Huawei Developer
查询ohpm-repo版本。
命令格式
功能描述
打印ohpm-repo的版本号。
可在执行setup安装脚本后，对安装版本信息进行校验。
示例
执行以下命令，查看版本信息：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.60298709788234076341130040299504:50001231000000:2800:F9B2E015FD57694FB2A132B246E295C0ECED7A2AFB236FD95121C2B90722B1EB.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-encrypt-history-V14
爬取时间: 2025-04-30 22:13:25
来源: Huawei Developer
加密明文密码。
命令格式
功能描述
使用指定的加密组件加密从标准输入读取的数据，并在标准输出中输出密文。
选项
crypto_path
您必须在 encrypt_password 命令后面配置 --crypto_path <string>参数，指定加密组件的路径。如果是完整组件，将用该组件去加密明文密码。如果是一个空目录，则命令将生成新的加密组件并加密明文密码。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.57485963524455732260787980663904:50001231000000:2800:AFCCE5C9282945244DB079D10FC67924A6F6F4738A249192E45F32DB3772145B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-pack-history-V14
爬取时间: 2025-04-30 22:14:00
来源: Huawei Developer
打包ohpm-repo部署根目录文件。
说明：ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
用于打包ohpm-repo<deploy_root>目录下的 conf ，db 和 meta 目录。
参数
<deploy_root>
您必须在 pack 命令后面配置 <deploy_root> 参数，指定待打包的ohpm-repo部署根目录。
启动ohpm-repo成功后，可以通过查看 ohpm-repo 工具中生成的 .deploy_root 文件查看部署根目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.30727628775238648591897522331792:50001231000000:2800:8547D06FFB20BA891A55B92574EB17661F30EE9EB9DFCB08F7FD32470132FD2E.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restore-history-V14
爬取时间: 2025-04-30 22:14:35
来源: Huawei Developer
将 ohpm-repo pack 打包产物替换到 <deploy_root> 目录下相应文件，重启服务。
ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
该命令会停止当前ohpm-repo服务，并用打包文件 <file_path> 中的内容替换ohpm-repo部署根目录 <deploy_root> 的相应文件，然后重启ohpm-repo服务。该命令执行前必须已经执行过ohpm-repo实例启动命令 ohpm-repo start。
-  支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
-  首次启动ohpm-repo实例后，会在ohpm-repo工具根目录中生成 .deploy_root 文件，其记录的是<deploy_root>，会自动读取识别，无需在命令中指定 <deploy_root> 路径。
参数
<file_path>
指定待解压的打包文件路径。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.25708759236248132224078844921933:50001231000000:2800:CA03D2D63BC561B5C0695DB84FDFDE65998D074A6C3A6A4A1B94F9277C543303.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-deploy-history-V14
爬取时间: 2025-04-30 22:15:09
来源: Huawei Developer
使用备份文件部署新的ohpm-repo实例。
ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
参数
<file_path>
您必须在 deploy 命令后面配置 <file_path> 参数，指定打包产物路径。
选项
deploy_root
您可以在 deploy 命令后面配置 --deploy_root <string> 参数，指定新的ohpm-repo部署根目录。支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
logs
您可以在 deploy 命令后面配置 --logs <string> 参数，指定 log 目录，优先级高于 config.yaml 中的 logs 配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
uplink
您可以在 deploy 命令后面配置 --uplink <string> 参数，指定远程包缓存路径，优先级高于 config.yaml 中 uplink.store_path 的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.18445473548857430630361752616554:50001231000000:2800:4074C1C56595068B79A6D7CF2FC5788F49AEC76A000D1C6B51B15FAEED00FD63.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-checkstorage-history-V14
爬取时间: 2025-04-30 22:15:44
来源: Huawei Developer
检查 sftp 中存储包的完整性。
ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
命令根据元数据检查 sftp 存储的包是否存在且完整。该命令要求文件存储模块必须配置为 ohpm-repo-plugin-sftp。
参数
<target>
您必须在 check_storage 命令后面配置 <target> 参数，指定要检查的包或者用 @all 指定检查所有包。
选项
failed
您可以在 check_storage 命令后面配置 --failed 选项 ，则只检查在下载错误日志中未被处理的且满足<target>条件的包。
示例
执行以下命令，检查包 @ohos/axios@2.0.3 的完整性：
检查 @ohos/axios@2.0.3 包在所有 sftp 存储目录中的完整性。
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.98217897505401988063961243058314:50001231000000:2800:B168CD1FE6C7CC44F76D740D7B3BD50EBFDDB4B2A91F182618472444CEBB18EC.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-mirrorstorage-history-V14
爬取时间: 2025-04-30 22:16:19
来源: Huawei Developer
同步 sftp 存储的包。
ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
该命令要求配置文件中文件存储必须为 ohpm-repo-plugin-sftp。命令会将源sftp目录下满足 <target> 条件的包同步到目标sftp目录下。
参数
<source_sftp>
您必须在 mirror_storage 命令后面配置 <source_sftp> 参数 ，指定源sftp配置的名字。
<target_sftp>
您必须在 mirror_storage 命令后面配置 <target_sftp> 参数 ，指定目标sftp配置的名字。
<target>
您必须在 mirror_storage 命令后配置 <target> 参数，指定满足条件的包；或使用 @all 指定所有包。
选项
failed
您可以在 mirror_storage 命令后面配置 --failed 选项，则只同步在下载错误日志中未被处理的且满足<target>条件的包，如果同步成功，则相应的错误日志会被设置成 handled。
示例
执行以下命令，同步包 @ohos/axios@2.0.3：
将名为 test_one_sftp 的 sftp 目录中 @ohos/axios@2.0.3 包同步到名为 test_two_sftp 的sftp目录中。
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.97901108561351255269127914693378:50001231000000:2800:FE29ED9F0FEA7916B36CCA8D51A54018B021E9C887DF77F8C869C358F510B77A.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-deploy-guide-history-V14
爬取时间: 2025-04-30 22:16:53
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-deploy-single-history-V14
爬取时间: 2025-04-30 22:17:26
来源: Huawei Developer
安装ohpm-repo工具
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.31003364800872240447017035551719:50001231000000:2800:F240D6464ADE55086C03CD1FD390C083B0E95EBE1FA0A0FCD7DFF7D0B8CF455F.png?needInitFileName=true?needInitFileName=true)
若您想在其他目录使用 ohpm-repo，请将 bin 目录路径配置到系统环境变量 path 中。
启动ohpm-repo
1.  设置数据存储 db 模块。 设置文件存储 store 模块。
2.  设置数据存储 db 模块。
3.  设置文件存储 store 模块。
-  设置数据存储 db 模块。
-  设置文件存储 store 模块。
1.  1.0.1 版本和 1.1.0 版本启动ohpm-repo存在不同，其中 1.1.0 版本支持指定ohpm-repo部署根目录 执行以下命令，其中 config： 指定启动时使用的配置文件。 结果示例： 执行以下命令： 结果示例：
2.  执行以下命令，其中 config： 指定启动时使用的配置文件。 结果示例：
3.  执行以下命令： 结果示例：
-  执行以下命令，其中 config： 指定启动时使用的配置文件。 结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.28859140398015827843885519148887:50001231000000:2800:C5F7F61F96C5CAB1BA132D452830C6F25D96F26C4D2AA3929B3C8BE5A9DB617C.png?needInitFileName=true?needInitFileName=true)
-  执行以下命令： 结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.06057049526132527278730666514558:50001231000000:2800:73BFCA394712BF8A7453B8E55439480C0644E4968181108EF931488620E59C35.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-multi-deploy-history-V14
爬取时间: 2025-04-30 22:18:00
来源: Huawei Developer
从 1.1.0 开始支持多实例部署。
环境准备
1、准备 mysql 数据库服务；
2、准备至少一个 sftp 存储服务，ohpm-repo 最大支持连接3个 sftp 服务；
3、安装 node.js 16.x 及以上版本。
安装ohpm-repo工具1.1.0
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.90484708777376333619532666670861:50001231000000:2800:0867B8A36D7BF8FA79CE2B1D2E2919045AFD03905761C9ED1B1485D19175244E.png?needInitFileName=true?needInitFileName=true)
若您想在其他目录使用 ohpm-repo，请将 bin 目录路径配置到系统环境变量 path 中。
多实例配置
1.  --crypto_path 参数用于指定加密组件，如果您是第一次执行该命令，可以指定一个空目录，在加密后会生成新的加密组件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.59444336135670451108412907613538:50001231000000:2800:550A22A345C4CC9104F1C6F77B11949293BCD1B7828B516CEAD9944BF67CE488.png?needInitFileName=true?needInitFileName=true)
1.  设置数据存储 db 模块。 设置文件存储 store 模块，sftp配置最多只能设置3个。
2.  设置数据存储 db 模块。
3.  设置文件存储 store 模块，sftp配置最多只能设置3个。
-  设置数据存储 db 模块。
-  设置文件存储 store 模块，sftp配置最多只能设置3个。
部署首个节点
进入 bin 目录，命令行启动ohpm-repo。
启动成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.91529266081511317030921930473385:50001231000000:2800:FBB681FEF1C5AF431AFC3D293F359A9D712EECF62B09425552AD56310610CD4B.png?needInitFileName=true?needInitFileName=true)
打包和部署
为帮助您更方便地完成多实例部署，为您提供打包、部署命令。
打包
在完成了多实例配置并首次启动过ohpm-repo服务实例的机器上，执行 ohpm-repo pack <deploy_root>。
该命令用来打包备份ohpm-repo的 <deploy_root>/conf， <deploy_root>/meta 目录，并在命令行工作目录下生成压缩包。
打包成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.28800889565756004887826975391521:50001231000000:2800:39CF06D43BCBD346566C8127C474559E4255ED4E86E6EC577299676A2529159D.png?needInitFileName=true?needInitFileName=true)
部署
将 pack 命令的产物拷贝到其他机器中。
在安装私仓工具后，使用 ohpm-repo deploy <file_path> --deploy_root <deploy_root> 命令部署新的实例；
部署成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.72903684188265576510153789016441:50001231000000:2800:258A1972BE1A4B2F29E61222FBE7C1FCE02749B9515216B8C3D7C9A185453078.png?needInitFileName=true?needInitFileName=true)
部署成功后可执行 ohpm-repo start 启动ohpm-repo。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.13490585232329922420105128209620:50001231000000:2800:1524A186CFC515C788C632B13CA3A738942A34BF16AA191EF0C821309491A3D9.png?needInitFileName=true?needInitFileName=true)
配置自动重启（可选）
为ohpm-repo实例配置系统重启时自动重启的功能。
在进行该配置前需要将 ohpm-repo 工具 bin 目录配置到环境变量path中。
Linux
1.  当 mysql 或 sftp 服务与 ohpm-repo 部署在同一服务器上时，请将 mysql 和 sftp 的启动命令放在 ohpm-repo start 命令之前。
2.  其中 run-repo.sh 表示要执行的脚本路径；>/dev/null 2>&1 表示将输出重定向到空设备，即不输出任何信息。
```typescript
@reboot /bin/sh run-repo.sh >/dev/null 2>&1
```
现在，每次系统启动时，都会自动执行 run-repo.sh 脚本中的命令。
Windows
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.24952377505033212029540372032987:50001231000000:2800:1D628A9AE9014F9CF920CB9D06E6B818EB0137F6C70F564C09CB26E23B881236.png?needInitFileName=true?needInitFileName=true)
现在，每次系统启动时，都会自动执行 run-repo.bat 脚本中的命令。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-data-migration-V14
爬取时间: 2025-04-30 22:18:34
来源: Huawei Developer
ohpm-repo2.2.0版本开始支持数据迁移功能。在ohpm-repo 配置文件中，db是元数据存储的配置项，store是文件存储的配置项，db和store不能随意搭配，需要符合下面表格中的匹配规范。如果需要改变db和store的存储方式，需要进行数据迁移操作。
| db：元数据存储  | 与db所适配的store：三方包文件存储  |
| --- | --- |
| filedb  | file storage  |
| mysql(ohpm-repo 1.1.0开始支持）  | file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持）  |
db：元数据存储
与db所适配的store：三方包文件存储
filedb
file storage
mysql(ohpm-repo 1.1.0开始支持）
file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持）
简要流程
为保证数据不丢失，请在数据迁移前务必进行数据的备份；启动ohpm-repo，使用迁移命令导出数据；修改配置文件中db和store的存储方式，以新存储方式启动ohpm-repo；使用迁移命令导入数据。
如果您当前使用的ohpm-repo版本不支持您所需要的存储方式，请参考升级指导文档，进行ohpm-repo的升级。
备份ohpm-repo数据
请参考数据备份指导文档进行操作。
使用迁移命令导出数据
1.  使用export_userinfo命令导出下面九个数据表的数据，并且导出加密组件，在命令执行目录生成打包export_userInfo_xxx.zip 文件。 user group groupmember publickey access_token uplink uplinkproxy repo
2.
3.  使用batch_download命令，从ohpm-repo配置的store存储目录中批量下载包文件。 使用第2步生成的 pkgInfo_xxxx.json 作为batch_download命令参数，批量下载har或tgz包，在命令执行目录生成 batch_download_xxx.zip 文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.59175069315659903294004522649041:50001231000000:2800:66D21FEEFF0F731E34BD2B95BEE4AFFD517743AEB159BE79DC55E6503DA1970A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.77185951925010000068855019173250:50001231000000:2800:FC74F5BA8C85AD7A03B305A838F3B08E0E93DC462F8F76008FCC948FE79F53A1.png?needInitFileName=true?needInitFileName=true)
如果不迁移所有的包，您可以在第2步生成的pkgInfo_xxxx.json文件中删除掉不需要下载的包。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.29282909116656857550895157970742:50001231000000:2800:9BFD1E1E914B15D8E103B16A8628FABC903B58D614E95A7BC0509955B7849CE5.png?needInitFileName=true?needInitFileName=true)
batch_download_xxx.zip 文件中存在 pkgInfo.json 文件，其中记录了每个包的 文件名、组织、上传者，用于在批量上传时准确指定发包来源。
新存储方式重启ohpm-repo
打开ohpm-repo压缩包解压根目录中配置文件config.yaml，修改db和store配置项，指定所需存储方式。
修改db和store配置项后，需要您在配置文件中同时配置新的<deploy_root>目录。
使用修改后的配置文件重新执行安装命令（这一步必须执行，初始化数据库和其他必要的配置）
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.22417245715876305905864328273987:50001231000000:2800:B12013007B52EA6AEFF9047F13BF684037C20438CFEF2B5B70297C5205C8206B.png?needInitFileName=true?needInitFileName=true)
根据提示信息刷新环境变量，然后重新启动ohpm-repo
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.13873061698911427177311880713323:50001231000000:2800:C8CD03D6DCA2F743D147D0EF5AD356F5360E7A38DE239F583E69C524452188CD.png?needInitFileName=true?needInitFileName=true)
使用迁移命令导入数据
1.  使用import_userinfo命令将export_userInfo_xxx.zip中的数据导入数据库。 所有数据导入成功后，可登录ohpm-repo管理网页进行验证。
2.  使用batch_publish命令，将批量下载生成的 batch_download_xxx.zip 中的包依次发布到ohpm-repo。 所有包发布成功。进入ohpm-repo网站查看包数量和包详情是否正确。 在batch_publish命令后面可以配置--force，如果进行批量上传时某个包的组织在ohpm-repo中不存在，将任意选取ohpm-repo中一位管理员用户作为组织负责人，自动创建组织。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.80159031642296882112937182165201:50001231000000:2800:4FB94471F11044037E236E7439E7647031F4AC6E6C360E1682EB3E7D4C458033.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.07128017668720613920409992053298:50001231000000:2800:5A2CDE836F9804F83F9799D08DACC17E3B1561D57F2309165FA09FD4D081FFE0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.71531109212604567237140603014239:50001231000000:2800:D0D7C1E68553C88FB11617CAD5A62A5DE3663D538F63013C39199E5309361DD1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.48636690914754265353749790693417:50001231000000:2800:0AB51E8CE40FFDD1F00521008959B6BCFA22B5E6937D57A16D56644161D89188.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-upgrade-V14
爬取时间: 2025-04-30 22:19:08
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-upgrade-101_to_110-V14
爬取时间: 2025-04-30 22:19:42
来源: Huawei Developer
在升级之前，请务必备份好 ohpm-repo 私仓工具中的的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括：<deploy_root>ohpm-repo部署根目录内数据，db元数据和store三方包数据，详细步骤可参考数据备份。
1.  旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.0.1 版本 ohpm-repo 私仓工具包解压目录下的 bin 目录，执行 stop。 若您想在其他目录使用 ohpm-repo，请将对应版本 ohpm-repo 工具包解压目录中 bin 目录的路径配置到系统环境变量 path 中。
2.  下载并解压工具包：下载版本 1.1.0 的 ohpm-repo 包，并解压（请解压到一个空文件夹中）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.89026411986807045756060967916057:50001231000000:2800:EC3EDECB0003332AF07F3DD4B9F286E29AFBB22D81BC330CF8AB88E7A82D79F1.png?needInitFileName=true?needInitFileName=true)
1.  安装完成之后，进入ohpm-repo 私仓工具包解压目录下的 bin 目录，执行如下命令： 终端输出为版本号（如：1.1.0），则表示解压成功。
2.  移植配置文件信息：新版本 1.1.0 的配置文件与旧版本 1.0.1相比差异不大，可直接拷贝旧版本中的配置文件有效信息至新版本配置文件中。 可直接拷贝旧版本中的listen， https， server， db， store 和 uplink 等信息至新版本配置文件对应位置；新版本中的 logs_path 和 loglevel 参数可直接使用默认值，不做修改。 如果ohpm-repo版本1.0.1使用的配置文件，配置项均为默认项，则无需移植配置文件信息，直接执行下一步启动操作。
3.  结果示例：
4.  版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.96079913883674740287757438719621:50001231000000:2800:5AD524ED8AF00810AE01F1CE299981BB2142F7630FC0234F947A97422BA43A0E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.06864233975962006462809638321901:50001231000000:2800:97AD7B6907FA432DF913100CDD9593CA36FAD42FE8659B5AA231AA217F47D8A8.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-upgrade-101_to_2xx-V14
爬取时间: 2025-04-30 22:20:16
来源: Huawei Developer
升级至2.X.X版本与升级至5.X.X版本步骤一致，本文以升级至2.X.X版本为例。
在升级之前，请务必备份好ohpm-repo 私仓工具中的的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括：<deploy_root>私仓部署根目录内数据，db元数据和store三方包数据，详细步骤可参考数据备份。
1.  旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.0.1 版本 ohpm-repo 私仓工具包解压目录下的 bin 目录，执行 stop 若您想在其他目录使用 ohpm-repo，请将对应版本 ohpm-repo 工具包解压目录中 bin 目录的路径配置到系统环境变量 path 中。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.61953158226333113939223520867575:50001231000000:2800:435C5ACBA98F8D101E12D7B0576E83625D10077B7BC2B5411F10FEE482F6EA9E.png?needInitFileName=true?needInitFileName=true)
1.  终端输出版本号 2.X.X，则表示解压成功。
1.  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
2.  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
3.  在使用新部署目录时，旧版本部署目录中meta文件一定要迁移到新版本部署目录中，否则使用meta加密组件加密的数据无法被正确解密。
4.  结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
5.  结果示例：
6.  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
7.  Window 系统： 关闭当前窗口，重新开启一个窗口
8.  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
9.  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
-  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
-  结果示例：
-  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
-  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.94070602754015893465524469133693:50001231000000:2800:8F66D60FAC789D3C091631410A8AE187F4B070FF79EA28C0EC89FB897F4D8E77.png?needInitFileName=true?needInitFileName=true)
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.94597753034437090164662592434192:50001231000000:2800:D8F7DB480D23E25CE18EDD0AFED696C89F7AD2057766B5699B3EC144221ABC9B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-upgrade-110_to_2xx-V14
爬取时间: 2025-04-30 22:20:50
来源: Huawei Developer
升级至2.X.X版本与升级至5.X.X版本步骤一致，本文以升级至2.X.X版本为例。
在升级之前，请务必备份好 ohpm-repo 私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括：<deploy_root>ohpm-repo部署根目录内数据，db元数据和store三方包数据，详细步骤可参考数据备份。
1.  旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.1.0 版本 ohpm-repo 私仓工具包解压目录下的 bin 目录，执行 stop
1.
2.  安装完成之后，进入ohpm-repo 私仓工具包解压目录下的 bin 目录，执行如下命令： 终端输出为版本号 2.X.X，则表示解压成功。
3.  移植配置文件信息：版本 2.X.X 的配置文件与版本 1.1.0 相比有较大差异，需要提取旧版本配置文件信息至新版本配置文件中，移植的具体内容如下： 如果 1.1.0  版本ohpm-repo的部署目录 deploy_root 使用的是默认路径，即可省略此操作。 在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。 新版本配置文件还添加了很多信息的配置，例如deploy_root和logs_path等，此类信息在升级过程中可不改变，使用默认项。
4.  如果 1.1.0  版本ohpm-repo的部署目录 deploy_root 使用的是默认路径，即可省略此操作。
5.  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
6.  在使用新部署目录时，旧版本的部署目录中meta文件一定要迁移到新版本部署目录中，否则使用meta加密组件加密的数据无法被正确解密。
7.  新版本服务启动：正确拷贝替换配置文件信息后，进入ohpm-repo 私仓工具包解压目录下的 bin 目录，执行以下命令启动新版本ohpm-repo服务： 结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。 结果示例：
8.  结果示例：
9.  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
10.  Window 系统： 关闭当前窗口，重新开启一个窗口
11.  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
12.  结果示例：
13.  在多实例部署中，可先升级一台机器，然后拷贝其配置文件到其他机器中进行快速升级，具体步骤如下 该方法要求部署的多实例机器之间，使用的配置文件除根目录 deploy_root 外，其他配置项必须完全相同。 若您想在其他目录使用 ohpm-repo，请将对应版本ohpm-repo根目录中 bin 目录的路径配置到系统环境变量 path 中。 终端输出为版本号2.0.0，则表示安装成功。 结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
14.  若您想在其他目录使用 ohpm-repo，请将对应版本ohpm-repo根目录中 bin 目录的路径配置到系统环境变量 path 中。
15.
16.  终端输出为版本号2.0.0，则表示安装成功。
17.  结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
18.  结果示例：
19.  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
20.  Window 系统： 关闭当前窗口，重新开启一个窗口
21.  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
22.  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.04674863425710531739845174791599:50001231000000:2800:2111D432146F39075F3DE26CA3FFECC021A745213AA60EB78DB2ABEB5DC0C88A.png?needInitFileName=true?needInitFileName=true)
-  如果 1.1.0  版本ohpm-repo的部署目录 deploy_root 使用的是默认路径，即可省略此操作。
-  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
-  结果示例：
-  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
-  结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.32036157558708426692307178951240:50001231000000:2800:0B18735416430727C5B1F1E9BD5A585FD7A0A811F946BE56E447641B977F2A22.png?needInitFileName=true?needInitFileName=true)
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.82914000579436934517902771962314:50001231000000:2800:F783C3379F93173AD63BCCF01A4BCD37603A59C5CC62BA04CE8C8445A4914035.png?needInitFileName=true?needInitFileName=true)
-  若您想在其他目录使用 ohpm-repo，请将对应版本ohpm-repo根目录中 bin 目录的路径配置到系统环境变量 path 中。
-
-  终端输出为版本号2.0.0，则表示安装成功。
-  结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
-  结果示例：
-  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
-  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.34176686661052547979305463707720:50001231000000:2800:664ABC0D4B9D532041FEEAC0274F7B60A4952B543D142C003D726946393737B6.png?needInitFileName=true?needInitFileName=true)
1.  结果示例：
2.  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
3.  Window 系统： 关闭当前窗口，重新开启一个窗口
4.  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
5.  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.23455539467578368556581869521479:50001231000000:2800:BBB65D792E1984766CFA3D943279D772D0968501DCD2E7C1B5EDD596D335D085.png?needInitFileName=true?needInitFileName=true)
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.24964762217483858425613674344270:50001231000000:2800:C120BB1DA856193CA0A967C83DDC440C31427FBA8E211505607EB399619544A9.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-upgrade-2xx_to_2xx-V14
爬取时间: 2025-04-30 22:21:25
来源: Huawei Developer
如需将ohpm-repo版本2.X.X/5.X.X版本升级到更高的2.X.X/5.X.X版本，可参考此文档。
1. 在升级之前，请务必备份好ohpm-repo私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括：<deploy_root>ohpm-repo部署根目录内数据，db元数据和store三方包数据，详细步骤可参考数据备份。
2. 如果您想要改变db元数据和store三方包的存储方式，可在正确升级后参考数据迁移文档指导修改。
1.
2.
3.  终端输出为新版本的版本号，则表示解压成功。
4.
5.  在使用新部署目录时，旧版本的部署目录中meta文件必须要迁移到新版本部署目录中，否则将导致使用meta加密组件加密的数据无法被正确解密。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.71796581606257948523557094028293:50001231000000:2800:81AECB32BCC59A6AE805C24007E0FD8060C6B43EFFC69CD8D9567960BC3CCAF5.png?needInitFileName=true?needInitFileName=true)
1.  结果示例： Window系统： 关闭当前窗口，重新开启一个窗口。 Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
2.  结果示例：
3.  Window系统： 关闭当前窗口，重新开启一个窗口。 Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
4.  Window系统： 关闭当前窗口，重新开启一个窗口。
5.  Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
6.  5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ；
7.  5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
8.  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
-  结果示例：
-  Window系统： 关闭当前窗口，重新开启一个窗口。 Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  Window系统： 关闭当前窗口，重新开启一个窗口。
-  Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ；
-  5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.91573063780917727932475722179425:50001231000000:2800:58D8EA4E9A5805DAAF5A871E041FCFD502CC12C4C8AE4F910568C4073BDA0B00.png?needInitFileName=true?needInitFileName=true)
-  Window系统： 关闭当前窗口，重新开启一个窗口。
-  Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ；
-  5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ；
-  5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.56942355866896389333990280955502:50001231000000:2800:4FF20902A75FA29B0A2100547F8468F28ADC7317080D9C06B8AF46101AD7EAFF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-storageplugin-V14
爬取时间: 2025-04-30 22:21:59
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-plugin-configuration-V14
爬取时间: 2025-04-30 22:22:35
来源: Huawei Developer
ohpm-repo 从2.2.0版本开始支持自定义存储插件（需要配套使用1.7.0及以上版本ohpm命令行工具），允许您开发定制化的存储插件来对接您自己的存储系统，您希望将ohpm-repo下的三方包文件存储在华为云OBS或者其他云储存平台，可以按照如下步骤来实现自定义存储插件。
当您使用自定义认证插件对接自己的存储系统时，如果存在网络通信，建议使用https协议，确保信息安全传输。
准备工作
编辑CustomStorage.ts文件，实现存储插件接口 StoragePlugin
接口类StoragePlugin中包含如下五个函数，需要在实现类中完成功能的实现。
1.  init 实现初始化准备工作。在配置文件 config.yaml 中 store.config 处可自定义一些插件所需要的参数信息，可通过函数 getStorageConfigInfo() 读取配置文件中自定义的参数信息。
2.  save 实现本地文件的上传功能。返回值为一个字符串，能够标识所上传的文件。函数入参为上传文件的本地路径srcPath和待上传包的详细信息packageInfo，packageInfo为可选项。 在实现save方法的时候，上传每一个三方包有四个文件待上传：<package_name>.har包文件，metadata.json文件，readme.md和changelog.md文件。由于后面三个文件在每个三方包中名称都相同，请存放在不同位置或者使用不同文件名存储，避免文件被覆盖。
3.  delete 实现已上传文件的删除功能。函数入参为savedResponse：上传文件 save 后的返回信息，通过入参信息定位已上传文件，进行文件的删除；返回值信息为删除的结果，布尔类型。
4.  实现已上传文件的内容读取功能。函数入参为savedResponse：上传文件save后的返回信息，通过入参信息定位已上传文件，进行文件内容读取；返回所读取到的文件信息，数据类型为 Buffer。
5.  getDownloadUrl 实现已上传文件下载URL的获取。函数入参为savedResponse：上传文件save后的返回信息，通过入参信息定位已上传文件，进行文件内容读取；返回所读取到文件的下载URL，数据类型为 string。
使用插件文件和启动ohpm-repo
1.  安装 typescript 包，编译 ts 文件为 js 文件。
2.  编译插件文件 如果 CustomStorage.ts 没有存放在 plugins 内，请先修改tsconfig.json文件 include 和 outDir 参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。
3.  如果 CustomStorage.ts 没有存放在 plugins 内，请先修改tsconfig.json文件 include 和 outDir 参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。
4.  编译后文件存放指定位置 编译后获得的 CustomStorage.js 需要与 CustomStorage.ts 保持在同一级目录中，否则会编译出错，默认输出在./plugins/outDir 内，需要把 CustomStorage.js 拷贝到 CustomStorage.ts 同级目录./plugins 中（ohpm-repo成功启动后可删除CustomStorage.ts文件）。
5.  编辑配置文件 为了保证ohpm-repo能够正确加载自定义存储插件，需要修改配置文件 config.yaml，主要涉及 store 处内容修改。 参数说明：
6.  ohpm-repo 服务部署 在完成上述操作之后，按照ohpm-repo部署指导，完成服务部署。
-  如果 CustomStorage.ts 没有存放在 plugins 内，请先修改tsconfig.json文件 include 和 outDir 参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-template-file-V14
爬取时间: 2025-04-30 22:23:10
来源: Huawei Developer
模板文件中包含自定义storage插件需要的两个文件：CustomStorage.ts和tsconfig.json。
插件模板CustomStorage.ts
```typescript
import {StoragePlugin} from '../libs/plugins/storage/customStorage/StoragePlugin';  // 插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），StoragePlugin接口类的默认引用地址
import {getStorageConfigInfo} from '../libs/common/getStorageConfigInfo';           // 插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），getStorageConfigInfo方法的默认引用地址
export class CustomStorage implements StoragePlugin {
async init(): Promise<void>{
// 配置文件中 store 项格式参考
// store:
//   type: custom    // store 存储类型为 custom，即用户自定义
//   config:         // 配置信息：export_name和plugin_path 是必选配置项
//     export_name: ExampleDemo          // 插件类的名字：例如 ExampleDemo
//     plugin_path: ../plugins/storage/customStorage/ExampleDemo.js    // 插件文件的存放位置
//     configInfo1: "info1";             // 自定义配置信息（可选项）
//     configInfo2: "info2";             // 自定义配置信息（可选项）
//     ...
// 通过函数 getStorageConfigInfo() 可以获取到配置文件config.yaml中store.config处自定义配置的信息
const configStorageInfo = await getStorageConfigInfo();
//举例说明：当配置文件 store.config处定义 configInfo1和 configInfo2信息，可读取
const configInfo1 = configStorageInfo.configInfo1 as string; //获取到configInfo1的值为 "info1"
const configInfo2 = configStorageInfo.configInfo2 as string; //获取到configInfo2的值为: "info2"
};
/**
* 通过文件的本地路径，把数据保存到指定的 storage 内
* @param srcPath： 上传文件的本地路径
* @param packageInfo: 可选参数，待上传包的详细信息，包含包名（含组织名）和包版本号两部分，包名：packageInfo.packageName，包版本：packageInfo.version.
* @returns 上传文件 save 后的返回信息： 能够标识文件，方便文件删除和读取
*/
async save(srcPath: string, packageInfo: any): Promise<string>{
let savedResponse: string;
return savedResponse;
};
/** 通过上传文件获得的返回信息，定位文件，进行文件的删除，返回删除结果
* @param savedResponse： 上传文件 save 后的返回信息
* @returns 删除的结果：true 表示删除成功
*/
async delete(savedResponse: string): Promise<boolean>{
let isDeleteSuccess: boolean;
return isDeleteSuccess;
};
/**
* 过上传文件获得的返回信息，定位文件，进行获取文件内容，数据格式为 Buffer
* @param savedResponse 上传文件 save 后的返回信息
* @returns 获取文件的内容，数据格式为 Buffer
*/
async download(savedResponse: string): Promise<Buffer>{
let fileContent: Buffer;
return fileContent;
};
/**
* 根据保存文件生成的结果字符串，获取文件下载url
* @param savedResponse 保存文件的结果字符串
*/
async getDownloadUrl(savedResponse: string): Promise<string>{
let fileDownloadUrl: string;
return fileDownloadUrl;
};
}
```
ts编译的配置文件tsconfig.json

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-custom-auth-plugin-V14
爬取时间: 2025-04-30 22:23:44
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-custom-auth-plugin-configuration-V14
爬取时间: 2025-04-30 22:24:18
来源: Huawei Developer
ohpm-repo 从2.3.0版本开始支持自定义认证插件（需配套使用1.8.0及以上版本ohpm命令行工具），允许您使用AccessToken认证，开发定制化的认证插件来对接开发者自己的用户信息系统。
当您使用自定义认证插件对接自己的用户系统时，如果存在网络通信，建议使用https协议，确保信息安全传输。
准备工作
编辑CustomAuth.ts文件，实现认证插件接口AuthPlugin
打开 CustomAuth.ts 模板文件，需要编写代码实现接口类AuthPlugin，实现auth和getUserInfo两个基础方法，实现类 CustomAuth 的名字可自定义修改。
接口类AuthPlugin中包含如下三个方法，需要在实现类中完成功能的实现。
1.  通过读写AccessToken获取对应用户信息，函数的入参为读写AccessToken值，返回值有四个参数：用户的id值，用户的name值，用户所属于的组织列表belongGroupList，用户所管理的组织列表groupAdminList。
2.  通过只读AccessToken获取对应用户信息，函数的入参为只读AccessToken值，返回值有四个参数：用户的id值，用户的name值，用户所属于的组织列表belongGroupList，用户所管理的组织列表groupAdminList。当ohpm-repo配置不支持匿名访问时，ohpm可以通过配置只读AccessToken值，获取执行install，info和update命令的权限。
3.  实现根据用户id获取用户名字的功能。函数入参为用户的id值；返回值为用户的名字。
插件文件的使用和ohpm-repo的启动
1.
2.  如果CustomAuth.ts没有存放在ohpm-repo解压根目录的plugins 内，请先修改tsconfig.json 文件中include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。
3.  如果CustomAuth.ts没有存放在ohpm-repo解压根目录的plugins 内，请先修改tsconfig.json 文件中include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。
4.  编译后获得的CustomAuth.js 需要与CustomAuth.ts 保持在同一级目录中，否则会编译出错，默认输出在./plugins/outDir 内，需要把CustomAuth.js 拷贝到CustomAuth.ts同级目录./plugins 中（ohpm-repo成功启动后可删除CustomAuth.ts文件）。
5.  参数说明：
6.  当ohpm-repo 成功启动后，在ohpm客户端的配置文件.ohpmrc中新增一行（//是有效字符，不是注释，勿删）。 其中ip和port为ohpm-repo私仓启动机器所在的ip值和端口值；readOnlyToken/readWriteToken为用户信息系统内有效的只读/读写accessToken值，通过该accessToken值，用户调用自定义认证插件CustomAuth中auth和authWithReadOnly方法，能够获取到有效的用户信息。
-  如果CustomAuth.ts没有存放在ohpm-repo解压根目录的plugins 内，请先修改tsconfig.json 文件中include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-custom-auth-plugin-template-V14
爬取时间: 2025-04-30 22:24:52
来源: Huawei Developer
模板文件中包含自定义auth插件需要的两个文件：CustomAuth.ts和tsconfig.json。
插件模板CustomAuth.ts
ts编译的配置文件tsconfig.json

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-data-backup-V14
爬取时间: 2025-04-30 22:25:27
来源: Huawei Developer
数据迁移或者版本升级之前请务必进行数据备份，以免重要数据丢失，无法回滚。备份的内容包括<deploy_root>ohpm-repo部署根目录内数据，db元数据和store三方包数据。
备份deploy_root部署根目录
<deploy_root>：ohpm-repo部署根目录，默认的路径为：
windows系统：~/AppData/Roaming/Huawei/ohpm-repo
其他操作系统：~/ohpm-repo
ohpm-repo在版本1.1.0之前不支持配置<deploy_root>，都采用默认值，若您的ohpm-repo支持且配置了<deploy_root>，请找到对应目录，并使用常用的压缩工具打包备份该目录。
如果配置文件中db，storage，logs 和 uplink的存储路径可配置，且存储位置不在ohpm-repo部署根目录<deploy_root>中，请找到对应目录进行数据备份。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150831.09000329974936460435591207732360:50001231000000:2800:F81CED96EF392EC16E460A8736D9726D462ABED680B95576DE415A4A7B321E4D.png?needInitFileName=true?needInitFileName=true)
备份<包存储目录>和<Mysql>
如果您使用的是本地存储（配置文件中db为filedb本地存储，store为fs本地存储），在备份<deploy_root>时已经完成db和store的备份，请忽略该步骤。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150831.33830202066272431657738050259782:50001231000000:2800:1E2EE27844607EAE16014DEDB9AC9AD7F0D863B0C7D8D9CF057E3F5F5BDD7FD6.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150831.62986371393685599236439870481120:50001231000000:2800:D1F4E1FD60A9358C983C97E546F12CFF42994BFC25873E6EE692157BB97BC5D1.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-export-metadata-V14
爬取时间: 2025-04-30 22:26:01
来源: Huawei Developer
支持通过export_pkginfo和batch_download命令，将OpenHarmony三方库中心仓中所有包批量导出，并能够通过batch_publish命令将导出的库批量上传至部署的ohpm-repo实例中。
开始执行下面的命令之前，请确保已经执行过ohpm-repo install和ohpm-repo start命令。
获取所有已上架的包列表
使用export_pkginfo命令，导出OpenHarmony三方库中心仓已上架的包列表。
执行结果
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150831.81507022094199869236247106204023:50001231000000:2800:3F50DC21152A0ED6550CA02465D555813C1EF8DB3B257FE88A8F87EC6D648360.png?needInitFileName=true?needInitFileName=true)
批量下载三方包
执行batch_download命令将上一步生成的pkgInfo_xxx.json文件中记录的包全部下载。
若只需要下载中心仓的部分包，可以手动修改pkgInfo_xxx.json文件，此时该命令只会批量下载pkgInfo_xxx.json文件中指定的包。
执行结果
批量上传
执行batch_publish命令将上一步生成的batch_download_xxx.zip压缩包中全部包批量上传到ohpm-repo。
执行结果
如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo实例缓存中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-interface-protocol-V14
爬取时间: 2025-04-30 22:26:35
来源: Huawei Developer
概述
ohpm客户端与ohpm-repo私仓通过REST API交互，目前一共有六种API：
ohpm客户端在访问ohpm-repo时，支持公私钥和Access Token两种认证方式：
Fetch Metadata
返回指定包的metadata元数据。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| group  | string  | 否  | 组织名，以@开头，比如@ohos  |
| package_name  | string  | 是  | 包名 (不含组织部分)  |
属性
类型
必填项
描述
group
string
否
组织名，以@开头，比如@ohos
package_name
string
是
包名 (不含组织部分)
请求示例（以请求一个应用内的HAR包 @test/package1 为例）：
响应成功示例（以请求一个应用内的HAR包 @test/package1 为例）：
metadata响应数据说明:
响应数据中包含八个顶级字段，描述如下：
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| _id  | string  | 是  | 包名，并用作数据库的主键ID  |
| _rev  | number  | 是  | 包的版本数量  |
| name  | string  | 是  | 包名  |
| description  | string  | 是  | 包的描述  |
| dist-tags  | json  | 是  | 包的所有标签信息  |
| versions  | json  | 是  | 包的所有版本数据  |
| packageType  | string  | 否  | 包的类型，详情见说明  |
| time  | json  | 是  | 包的发布时间  |
属性
类型
必填项
描述
_id
string
是
包名，并用作数据库的主键ID
_rev
number
是
包的版本数量
name
string
是
包名
description
string
是
包的描述
dist-tags
json
是
包的所有标签信息
versions
json
是
包的所有版本数据
packageType
string
否
包的类型，详情见说明
time
json
是
包的发布时间
顶级字段中versions字段包含包的所有版本数据，有17个字段内容，描述如下：
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| _id  | string  | 是  | 包名@包的版本号，如：@myscope/myhsplib@1.0.0  |
| _nodeVersion  | string  | 是  | 发布时使用的node.js版本  |
| _ohpmVersion  | string  | 是  | 发布时使用的ohpm客户端版本  |
| name  | string  | 是  | 包名  |
| version  | string  | 是  | 包的版本号  |
| description  | string  | 是  | 包的描述  |
| author  | json  | 是  | 包的作者信息  |
| repository  | string  | 否  | 包的源码仓库地址  |
| license  | string  | 否  | 包的项目开源许可证，详情见说明  |
| packageType  | string  | 否  | 包的类型，详情见说明  |
| dependencies  | json  | 否  | 包的运行时依赖  |
| devDependencies  | json  | 否  | 包的开发态依赖  |
| dynamicDependencies  | json  | 否  | 包的动态依赖，只针对HSP包  |
| types  | string  | 条件必填  | 包的类型声明文件  |
| main  | string  | 条件必填  | 包的入口文件  |
| dist  | json  | 是  | 维护包的SSRI值及下载地址，详情见说明  |
| hspType  | string  | 条件必填  | HSP包的类型，详情见说明  |
属性
类型
必填项
描述
_id
string
是
包名@包的版本号，如：@myscope/myhsplib@1.0.0
_nodeVersion
string
是
发布时使用的node.js版本
_ohpmVersion
string
是
发布时使用的ohpm客户端版本
name
string
是
包名
version
string
是
包的版本号
description
string
是
包的描述
author
json
是
包的作者信息
repository
string
否
包的源码仓库地址
license
string
否
包的项目开源许可证，详情见说明
packageType
string
否
包的类型，详情见说明
dependencies
json
否
包的运行时依赖
devDependencies
json
否
包的开发态依赖
dynamicDependencies
json
否
包的动态依赖，只针对HSP包
types
string
条件必填
包的类型声明文件
main
string
条件必填
包的入口文件
dist
json
是
维护包的SSRI值及下载地址，详情见说明
hspType
string
条件必填
HSP包的类型，详情见说明
Login
客户端登录，获得上传包，下架包和编辑标签tag时所需的 token。
请求示例：
请求示例中请求体（@./path/to/login-body/file.json）示例 ：
请求体包含五个字段，描述如下：
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| version  | string  | 是  | 协议版本  |
| publishId  | string  | 是  | 发布码  |
| timestamp  | number  | 是  | 发布时间戳  |
| nonce  | string  | 是  | 随机数  |
| signature  | string  | 是  | 签名值，具体见说明  |
属性
类型
必填项
描述
version
string
是
协议版本
publishId
string
是
发布码
timestamp
number
是
发布时间戳
nonce
string
是
随机数
signature
string
是
签名值，具体见说明
1、publishId: 由ohpm-repo私仓生成的发布码，与用户绑定，每个用户的发布码是唯一的，在客户端的 .ohpmrc 文件中通过 publish_id 配置；
2、timestamp: 时间戳，单位为毫秒；
3、nonce: 客户端在登录时动态生成的uuidv4随机数；
4、signature: 客户端在登录时，将协议版本、发布码、发布时间戳和随机数以 v{version}-{publishId}-{timestamp}-{nonce} 格式组合而成，并使用私钥经RSA-SHA256算法签名而生成。
响应成功示例：
token: 使用公私钥认证时，ohpm-repo生成的认证信息。认证信息必须验证有效，才有权限执行上传包、下架包和编辑标签tag等操作。
Publish
上传一个HAR/HSP包到ohpm-repo私仓中
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
属性
类型
必填项
描述
package_name
string
是
包名
若包名中包含组织名，则package_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package_name为@myscope%2fmypkg。
请求示例（以上传一个应用内的HSP包 @myscope/myhsppkg 为例）：
请求示例中metadata元数据文件（@./path/to/metadata/file.json）内容由ohpm客户端生成，内容如下所示：
响应成功示例：
响应失败示例：
1、发布失败时，ohpm客户端会根据状态码取响应体中error字段的值或状态描述statusText的值，进行打印提示。
2、additionalMsg: 当响应体中存在该字段且不为空时，ohpm客户端会在发布包成功后打印该字段的值。
流式上传一个HAR/HSP到ohpm-repo
ohpm客户端从5.0.1版本开始支持使用流式上传，当上传的三方包大小超过阈值（默认5M）时，ohpm会优先调用流式上传接口进行上传。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
属性
类型
必填项
描述
package_name
string
是
包名
若包名中包含组织名，则package_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package_name为@myscope%2fmypkg。
请求示例（以上传一个应用内的HSP包 @myscope/myhsppkg 为例）：
其中， Content-Type是multipart/form-data；hsp.tgz是待上传的HSP包。
请求示例中元数据文件（@./path/to/metadata/file.json）内容由ohpm客户端生成，如下所示：
响应成功示例：
响应失败示例：
1、发布失败时，ohpm客户端会根据状态码取响应体中error字段的值或状态描述statusText的值，进行打印提示。
2、additionalMsg: 当响应体中存在该字段且不为空时，ohpm客户端会在发布包成功后打印该字段的值。
Unpublish
从ohpm-repo中下架一个HAR/HSP包 （下架一个包的某个版本，或是整个包）。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
属性
类型
必填项
描述
package_name
string
是
包名
请求示例：
Ping
检测与ohpm-repo仓库的网络连通性。
请求示例：
响应成功示例：
DistTags
新增tag
为包添加tag。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
| tag  | string  | 是  | 标签名  |
属性
类型
必填项
描述
package_name
string
是
包名
tag
string
是
标签名
若包名中包含组织名，则package_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package_name为@myscope%2fmypkg。
请求示例（为包 @myscope/myhsppkg@1.0.0 增加标签（tag）test）：
更新tag
修改包tag对应的版本号。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
| tag  | string  | 是  | 标签名  |
属性
类型
必填项
描述
package_name
string
是
包名
tag
string
是
标签名
请求示例（为包 @myscope/myhsppkg 修改标签（tag）test对应版本号为2.0.0）：
删除tag
删除包的tag。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
| tag  | string  | 是  | 标签名  |
属性
类型
必填项
描述
package_name
string
是
包名
tag
string
是
标签名
请求示例（删除包 @myscope/myhsppkg 的标签（tag）test）：
仓库响应码说明
| 响应码  | 范围  | 说明  |
| --- | --- | --- |
| 200  | 仓库所有接口  | 成功  |
| 400  | 仓库所有接口  | 客户端传参校验失败、登录失败  |
| 401  | Publish, Unpublish, DistTags  | 认证失败  |
| 404  | 访问仓库不存在的接口  | 接口不存在  |
| 500  | 仓库所有接口  | 服务内部错误  |
| 598  | Publish  | 当仓库上传接口返回的响应状态码为598时，ohpm 5.0.1及以上版本会尝试去重新上传  |
响应码
范围
说明
200
仓库所有接口
成功
400
仓库所有接口
客户端传参校验失败、登录失败
401
Publish,Unpublish,DistTags
认证失败
404
访问仓库不存在的接口
接口不存在
500
仓库所有接口
服务内部错误
598
Publish
当仓库上传接口返回的响应状态码为598时，ohpm 5.0.1及以上版本会尝试去重新上传
由于流式上传接口在ohpm 5.0.1版本才开始支持，当ohpm调用该接口时，若返回的响应状态码为404时，ohpm客户端会再次调用上传接口上传。为了保证与ohpm客户端的兼容性，请确保当访问仓库不存在的接口仓库的响应状态码为404。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-commandline-get-V14
爬取时间: 2025-04-30 23:06:26
来源: Huawei Developer
该命令行工具集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、三方库的包管理ohpm、命令行解析hstack、编译构建hvigorw。
命令行工具获取
请前往下载中心获取命令行工具Command Line Tools，并根据下载中心页面工具完整性指导进行完整性校验。
HarmonyOS SDK已嵌入命令行工具中，无需额外下载配置。
配置环境变量
Windows
将解压后command-line-tools文件夹的bin目录配置到系统或者用户的PATH变量中。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.03897237065912744959400437341402:50001231000000:2800:5C3582B37C177350BD655590BDB79B2B6A3B2F4876FA5D947EC062F2148B11A0.png?needInitFileName=true?needInitFileName=true)
macOS/Linux
下载配置完成即可使用相关命令行工具能力。如需验证是否配置成功，可以使用相关命令验证，例如执行codelinter -v指令，检查是否可以正确获取codelinter工具版本。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-command-line-codelinter-V14
爬取时间: 2025-04-30 23:07:02
来源: Huawei Developer
codelinter同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。
codelinter命令行格式为：
options：可选配置，请参考表1。
dir：待检查的工程根目录；为可选参数，如不指定，默认为当前上下文目录。
| 指令  | 说明  |
| --- | --- |
| --config/-c <filepath>  | 指定执行codelinter检查的规则配置文件，<filepath>指定执行检查的规则配置文件位置。  |
| --fix  | 设置codelinter检查同时执行QuickFix。  |
| --format/-f  | 设置检查结果的输出格式。目前支持default/json/xml/html四种格式；不指定时，默认是default格式（文本格式）。  |
| --output/-o <filepath>  | 指定检查结果保存位置，且命令行窗口不展示检查结果。<filepath>指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会显示在命令行窗口中。  |
| --version/-v  | 查看codelinter版本。  |
| --product/-p <productName>  | 指定当前生效的product。 <productName> 为生效的product名称。  |
| --incremental/-i  | 对Git工程中的增量文件（包含新增/修改/重命名的文件）执行Code Linter检查。  |
| --help/-h  | 查询codelinter命令行帮助。  |
指令
说明
--config/-c<filepath>
指定执行codelinter检查的规则配置文件，<filepath>指定执行检查的规则配置文件位置。
--fix
设置codelinter检查同时执行QuickFix。
--format/-f
设置检查结果的输出格式。目前支持default/json/xml/html四种格式；不指定时，默认是default格式（文本格式）。
--output/-o<filepath>
指定检查结果保存位置，且命令行窗口不展示检查结果。<filepath>指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会显示在命令行窗口中。
--version/-v
查看codelinter版本。
--product/-p<productName>
指定当前生效的product。 <productName> 为生效的product名称。
--incremental/-i
对Git工程中的增量文件（包含新增/修改/重命名的文件）执行Code Linter检查。
--help/-h
查询codelinter命令行帮助。
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.08832503041866122538410923714417:50001231000000:2800:C79BB4C5631326FDD97B9DA7EBD759FE3A59D4BA7D38A4616AB7B5E508C30050.png?needInitFileName=true?needInitFileName=true)
-
-
-
-
-
-
-
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.47280382993366407827558907134029:50001231000000:2800:3EDE2774E22F9DEDCA08534B7C1A508F427A4B9C785F7E47D0CF983ACA12DBD6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.11348529931446880189046983084940:50001231000000:2800:6C1C1B32EC875D5083E880727BA806EB62E2C80B182DF0486299A6729BC12E72.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.60850222597133534103183666676904:50001231000000:2800:3544BB88E93A8311768F83CC5AC2C4E58C160108D1D2F6E8B3197E84BA3B6590.png?needInitFileName=true?needInitFileName=true)
1.
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150805.26212639141393479408111493576758:50001231000000:2800:1C41B8BB3685AC2417A2D1D4B33CA889F98D196EB59F5490067681886118409C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.10932837051078684741626913186927:50001231000000:2800:B0934781520129835121F48E01238D76BCD563719E1FDB316BE91B5BE142E71F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.71821807248946005390513097006649:50001231000000:2800:48078D80F465D75E068B4E8A10BB7A6999B0F201B281D8426C4E8E3F85DDD967.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.54006618416216577073171122595679:50001231000000:2800:76FAE7A0133B15D5E8A70718EDB3B5B9431B7C0D9D4A3D12FA33E3088FE1B587.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-command-line-hstack-V14
爬取时间: 2025-04-30 23:07:36
来源: Huawei Developer
简介
hstack是DevEco Studio为开发人员提供的用于将release应用混淆后的crash堆栈还原为源码对应堆栈的工具，支持Windows、Mac、Linux三个平台。
hstack命令行格式为:
options: 可选配置，请参考表hstack命令行配置。
| 指令 | 说明 |
| --- | --- |
| -i/--input | 可选，指定工程crash文件归档目录。 |
| -c/--crash | 可选，指定一条crash堆栈。 |
| -o/--output | 可选，指定解析结果输出目录（输入指定为-c时， -o参数指定一个输出文件）。 |
| -s/--sourcemapDir | 可选，指定工程sourcemap文件归档目录。 |
| --so/--soDir | 可选，指定工程shared object文件归档目录。 |
| -n/--nameObfuscation | 可选 ，指定工程nameCache文件归档目录。 |
| -v/--version | 查看hstack版本。 |
| -h/--help | 查询hstack命令行帮助。 |
指令
说明
-i/--input
可选，指定工程crash文件归档目录。
-c/--crash
可选，指定一条crash堆栈。
-o/--output
可选，指定解析结果输出目录（输入指定为-c时， -o参数指定一个输出文件）。
-s/--sourcemapDir
可选，指定工程sourcemap文件归档目录。
--so/--soDir
可选，指定工程shared object文件归档目录。
-n/--nameObfuscation
可选 ，指定工程nameCache文件归档目录。
-v/--version
查看hstack版本。
-h/--help
查询hstack命令行帮助。
环境配置
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.86580355993558084657770909456856:50001231000000:2800:93F68B8FA1FC9F84B6572109CA719353E737A847F7E6208E0851952BAED6A987.png?needInitFileName=true?needInitFileName=true)
使用示例
1.
2.
3.
4.
5.  解析完成后，outputDir目录下会生成对应的解析结果，文件以原始crash文件名加“_”前缀进行命名。crash堆栈中的C++日志以及ArkTS日志均已解析为源码对应的文件路径以及行列号，结果如下图所示： 说明：在构建Release应用时，so文件是默认不包含符号表信息的，如果需要在构建Release应用时生成包含符号表的so文件，需要在工程的模块级build-profile.json5文件的buildOption属性中，配置如下信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.35159744624991841080010014182381:50001231000000:2800:7F7EBFF8EE6BD8B40060D658963D829F9AD47566898191187F168458B43F9D91.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.85961887006283308169574297092929:50001231000000:2800:83BA6A2FBD831E451312061EA2EA67F8ECDED376AB5B84A59B05743377304BE2.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.63512790123696573187549357935232:50001231000000:2800:E7F450C5498301A73D9E6F36353C3FD7FD7991E9CA012FB9C70C5742E0E659E7.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.21728542900479788737642765165664:50001231000000:2800:FF26474DB1E4F518471A61E67E228C67EA07989C13ACAE47B81F84056B2BA987.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.58299428304281731077170604450963:50001231000000:2800:7E7AED8613426198FA658E32A93E0D2AC8C5466CF0B565972F470CCD9A955749.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.35402942788682256453185170365402:50001231000000:2800:1568DA6F1CC4DF163FB4C57AEE5D2CAA8319D619242827F89A530653CB8EE117.png?needInitFileName=true?needInitFileName=true)
堆栈解析方案说明
以如下代码为例。
Entry模块通过独立har包形式引用har模块中的har方法：
```typescript
import {har} from 'Har'
@Entry
@Component
struct Index {
@State har: string = 'Har';
build() {
Row() {
Column() {
Text(this.har)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
let entryClass = new EntryClass();
entryClass.callHarFunction();
})
}
.width('100%')
}
.height('100%')
}
}
class EntryClass {
callHarFunction() {
har()
}
}
```
生成的crash如下：
crash中，包含混淆后的方法名（或属性名）、路径信息以及混淆后的行列号信息，其中：
在对堆栈进行还原时，可分为以下三步：
1.  根据路径信息entry|har|1.0.0|src/main/ets/components/mainpage/MainPage.js，可在entry模块sourcemap文件中找到如下字段：
2.  基于步骤1找到的sourcemap信息，根据sources及mappings字段进行解析，可以将路径以及行列号还原如下： 该文件位于entry模块oh_modules路径下。 如果对应sourcemap中包含package-info字段，则可以利用package-info中对应模块的sourcemap，对该条堆栈进行二次解析。例如该堆栈中包package-info为har|1.0.0，可利用har中的sourcemap对该堆栈进行再次解析，方案如下：
3.  以第二条堆栈为例： 通过步骤1与步骤2，将该堆栈路径以及行列号信息进行解析，结果如下： 在对应模块编译产物中的nameCache文件中，通过解析后的文件路径找到如下字段： 该字段的IdentifierCache与MemberMethodCache中保存了方法名混淆前后的映射关系，对应格式为： "源码方法名:该方法起始行号:该方法结束行号":"混淆后方法名"。 第二条堆栈混淆后的方法名为"i"，利用上述字段对该方法名进行还原： 通过上述方式，可以得到源码的方法名。
```json
"callHarFunction:24:26": "i"
```
4.
```json
"callHarFunction:24:26": "i"
```
通过上述方式，即可利用编译产物对release应用的crash信息进行解析还原。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-hvigor-commandline-V14
爬取时间: 2025-04-30 23:08:10
来源: Huawei Developer
Hvigor通过hvigorw工具，实现命令行交互。
配置环境变量
1.  在系统或者用户的PATH变量中，添加hvigorw的路径：${COMMANDLINE_TOOL_DIR}/command-line-tools/bin，其中COMMANDLINE_TOOL_DIR是命令行工具的安装路径。
2.  在系统或者用户的PATH变量中，添加hvigorw的路径：${COMMANDLINE_TOOL_DIR}/command-line-tools/bin，其中COMMANDLINE_TOOL_DIR是命令行工具的安装路径。
3.
-  在系统或者用户的PATH变量中，添加hvigorw的路径：${COMMANDLINE_TOOL_DIR}/command-line-tools/bin，其中COMMANDLINE_TOOL_DIR是命令行工具的安装路径。
命令行使用方式
hvigorw命令行格式为：
其中taskNames是任务，可同时执行多个任务，options是可选参数，具体的任务和可选参数请参考常用命令。
hvigorw命令需要在工程根目录下执行。
常用命令
常见的任务和参数如下，更多任务请参考任务详细说明。
查询
| 参数 | 说明 |
| --- | --- |
| -h, --help | 打印Hvigor的命令帮助信息。 |
| -v, --version | 打印Hvigor版本信息。 |
参数
说明
-h, --help
打印Hvigor的命令帮助信息。
-v, --version
打印Hvigor版本信息。
编译构建
| 任务 | 说明 |
| --- | --- |
| clean | 清理构建产物build目录。 |
| collectCoverage | 基于打点数据生成覆盖率统计报表。 |
| assembleHap | 构建Hap应用。 |
| assembleApp | 构建App应用。 |
| assembleHsp | 构建Hsp包。 |
| assembleHar | 构建Har包。 |
任务
说明
clean
清理构建产物build目录。
collectCoverage
基于打点数据生成覆盖率统计报表。
assembleHap
构建Hap应用。
assembleApp
构建App应用。
assembleHsp
构建Hsp包。
assembleHar
构建Har包。
编译构建命令行常用扩展参数：
| 参数 | 说明 |
| --- | --- |
| -p buildMode={debug | release} | 采用debug/release模式进行编译构建。 缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。 关于构建模式的详细说明，请参考指定构建模式。针对HAR构建，请参考构建HAR。 |
| -p debuggable=true/false | 该配置会覆盖构建模式中对应的buildOption中的debuggable配置。 关于debuggable的合并优先级，请参考合并编译选项规则。 |
| -p product={ProductName} | 指定product进行编译, 编译product下配置的module target。 缺省时：默认为default。 |
| -p module={ModuleName}@{TargetName} | 指定模块及target进行编译，可指定多个相同类型的模块进行编译以逗号分割；TargetName不指定时默认为default。 限制：此参数需要与--mode module参数搭配使用。 缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。 |
| -p ohos-test-coverage={true | false} | 执行测试框架代码覆盖率插桩编译。  |
| -p coverage={true | false} |
| -p parameterFile=param.json/json5 | 设置oh-package.json5文件的参数配置文件，其中"param"可自行修改为对应配置文件名称。详细使用请参考parameterFile。 |
参数
说明
-p buildMode={debug | release}
采用debug/release模式进行编译构建。
缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。
关于构建模式的详细说明，请参考指定构建模式。针对HAR构建，请参考构建HAR。
-p debuggable=true/false
该配置会覆盖构建模式中对应的buildOption中的debuggable配置。
关于debuggable的合并优先级，请参考合并编译选项规则。
-p product={ProductName}
指定product进行编译, 编译product下配置的module target。
缺省时：默认为default。
-p module={ModuleName}@{TargetName}
指定模块及target进行编译，可指定多个相同类型的模块进行编译以逗号分割；TargetName不指定时默认为default。
限制：此参数需要与--mode module参数搭配使用。
缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。
-p ohos-test-coverage={true | false}
执行测试框架代码覆盖率插桩编译。
-p coverage={true | false}
-p parameterFile=param.json/json5
设置oh-package.json5文件的参数配置文件，其中"param"可自行修改为对应配置文件名称。详细使用请参考parameterFile。
测试相关的命令行：
| 命令行 | 说明 |
| --- | --- |
| hvigorw onDeviceTest -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName} |  说明 从Hvigor 4.3.0版本开始支持。  通过命令行方式执行Instrument Test。  module：执行测试的模块，缺省默认是执行所有模块的用例。HAP/HAR/HSP模块都支持。 coverage：是否需要覆盖率报告，缺省默认为true。 scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。  多个module和scope之间用逗号分割。  覆盖率测试结果文件：<module-path>/.test/default/outputs/ohosTest/reports 测试结果文件：path_to_project/module_name/.test/default/intermediates/ohosTest/coverage_data/test_result.txt  |
| hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName} | 通过命令行方式执行Local Test。  module：执行测试的模块，缺省默认是执行所有模块的用例。HAP/HAR/HSP模块都支持。 coverage：是否需要覆盖率报告，缺省默认为true。 scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。  多个module和scope之间用逗号分割。  覆盖率测试结果文件：<module-path>/.test/default/outputs/test/reports 测试结果文件：path_to_project/module_name/.test/default/intermediates/test/coverage_data/test_result.txt  |
命令行
说明
hvigorw onDeviceTest -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}
从Hvigor 4.3.0版本开始支持。
通过命令行方式执行Instrument Test。
多个module和scope之间用逗号分割。
-  <module-path>/.test/default/outputs/ohosTest/reports
hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}
通过命令行方式执行Local Test。
多个module和scope之间用逗号分割。
-  <module-path>/.test/default/outputs/test/reports
日志
| 参数 | 说明 |
| --- | --- |
| -e, --error | 设置hvigor的日志级别为error。 |
| -w, --warn | 设置Hvigor的日志级别为warn。 |
| -i, --info | 设置Hvigor的日志级别为info。 |
| -d, --debug | 设置Hvigor的日志级别为debug。 |
| --stacktrace，--no-stacktrace | Hvigor默认使能关闭打印所有异常的堆栈信息，如需开启在命令行后添加该选项。 |
参数
说明
-e, --error
设置hvigor的日志级别为error。
-w, --warn
设置Hvigor的日志级别为warn。
-i, --info
设置Hvigor的日志级别为info。
-d, --debug
设置Hvigor的日志级别为debug。
--stacktrace，--no-stacktrace
Hvigor默认使能关闭打印所有异常的堆栈信息，如需开启在命令行后添加该选项。
可视化
| 参数 | 说明 |
| --- | --- |
| --analyze=normal | 在DevEco Studio中开启Build Analyzer构建分析，设置为普通模式，通过简单打点数据进行分析。 |
| --config properties.hvigor.analyzeHtml=true | 在工程的.hvigor/report目录下生成构建可视化html文件，该文件可直接在浏览器中打开。 |
| --analyze=false | 不启用Build Analyzer构建分析。 |
| --analyze=advanced | 启用Build Analyzer构建分析，并设置为进阶模式，通过更加详细的打点数据进行分析。如果需要更详细的任务耗时数据，请选择该模式。 |
| --analyze | 同--analyze=normal命令。 从Hvigor 4.3.0开始废弃，请使用--analyze=normal替换。 |
| --no-analyze | 同--analyze=false命令。 从Hvigor 4.3.0开始废弃，请使用--analyze=false替换。 |
| --verbose-analyze | 同--analyze=advanced命令。 从hvigor 4.3.0开始废弃，请使用--analyze=advanced替换。 |
参数
说明
--analyze=normal
在DevEco Studio中开启Build Analyzer构建分析，设置为普通模式，通过简单打点数据进行分析。
--config properties.hvigor.analyzeHtml=true
在工程的.hvigor/report目录下生成构建可视化html文件，该文件可直接在浏览器中打开。
--analyze=false
不启用Build Analyzer构建分析。
--analyze=advanced
启用Build Analyzer构建分析，并设置为进阶模式，通过更加详细的打点数据进行分析。如果需要更详细的任务耗时数据，请选择该模式。
--analyze
同--analyze=normal命令。
从Hvigor 4.3.0开始废弃，请使用--analyze=normal替换。
--no-analyze
同--analyze=false命令。
从Hvigor 4.3.0开始废弃，请使用--analyze=false替换。
--verbose-analyze
同--analyze=advanced命令。
从hvigor 4.3.0开始废弃，请使用--analyze=advanced替换。
daemon
| 参数 | 说明 |
| --- | --- |
| --daemon | 使能daemon。 |
| --no-daemon | Hvigor默认使能daemon，如需关闭，可在命令行后添加该选项。 命令行模式下推荐使用此参数。 |
| --stop-daemon | 关闭当前工程的daemon进程。 |
| --stop-daemon-all | 关闭所有工程的daemon进程。 |
| --status-daemon | 查询当前环境中所有的Hvigor daemon进程信息。 |
| --max-old-space-size=12345 | 设置daemon进程老生代内存大小为12345MB。 |
参数
说明
--daemon
使能daemon。
--no-daemon
Hvigor默认使能daemon，如需关闭，可在命令行后添加该选项。
命令行模式下推荐使用此参数。
--stop-daemon
关闭当前工程的daemon进程。
--stop-daemon-all
关闭所有工程的daemon进程。
--status-daemon
查询当前环境中所有的Hvigor daemon进程信息。
--max-old-space-size=12345
设置daemon进程老生代内存大小为12345MB。
性能
| 参数 | 说明 |
| --- | --- |
| --parallel, --no-parallel | Hvigor默认使能并行编译能力，如需关闭在命令行后添加该选项。 |
| --incremental, --no-incremental | Hvigor默认使能增量编译能力，如需关闭在命令行后添加该选项。 |
参数
说明
--parallel, --no-parallel
Hvigor默认使能并行编译能力，如需关闭在命令行后添加该选项。
--incremental, --no-incremental
Hvigor默认使能增量编译能力，如需关闭在命令行后添加该选项。
公共命令
| 任务 | 说明 |
| --- | --- |
| tasks | 打印工程各模块包含的任务信息。 |
| taskTree | 打印工程各模块的任务依赖关系信息。 |
| version | 打印Hvigor的相关版本信息。 |
| prune | 清除30天内未使用的Hvigor缓存文件并从pnpm存储中删除未引用的包。 |
任务
说明
tasks
打印工程各模块包含的任务信息。
taskTree
打印工程各模块的任务依赖关系信息。
version
打印Hvigor的相关版本信息。
prune
清除30天内未使用的Hvigor缓存文件并从pnpm存储中删除未引用的包。
其他命令
| 参数 | 说明 |
| --- | --- |
| -s,--sync | 处理并持久化Hvigor部分工程信息到工程./hvigor/outputs/sync/output.json中。 |
| -m,--mode | 在对应的目录执行相应的task，例hvigorw clean -m project在工程目录下执行build目录清理（即清理工程级别的build文件夹）。 |
| --enable-build-script-type-check | 使能工程中hvigorfile.ts的类型检查，该字段已废弃，请使用--type-check替换。 |
| --type-check, --no-type-check | Hvigor默认使能关闭工程中hvigorfile.ts的类型检查，如需开启，可在命令行后添加该选项。 |
| --no-pnpm-frozen-lockfile，--pnpm-frozen-lockfile | Hvigor默认使能不忽略pnpm-lock.yaml文件，如需开启，可在命令行后添加该选项。 忽略pnpm-lock.yaml文件，按照hvigor-config.json5的配置安装Hvigor插件的依赖（如果不忽略pnpm-lock.yaml文件，在使用Hvigor 2.0.0及以上版本的CI场景下安装Hvigor插件依赖时将报错）。 说明 该命令在4.1 Release及以上版本中已废弃。在CI场景中将自动配置，无需开发者手动配置。  |
| --config, -c | 指定hvigor-config.json5配置文件中的参数。 当前仅支持设置properties里的参数，具体支持的参数请查看hvigor-config.json5中properties支持的参数。 --config properties.key=value 同 -c properties.key=value |
| --watch | 使能观察模式，主要用于预览和热加载场景。 |
| --generate-build-profile, --no-generate-build-profile | 已废弃。使能生成BuildProfile.ets文件。 |
| --node-home <string> | 指定nodejs路径。 |
参数
说明
-s,--sync
处理并持久化Hvigor部分工程信息到工程./hvigor/outputs/sync/output.json中。
-m,--mode
在对应的目录执行相应的task，例hvigorw clean -m project在工程目录下执行build目录清理（即清理工程级别的build文件夹）。
--enable-build-script-type-check
使能工程中hvigorfile.ts的类型检查，该字段已废弃，请使用--type-check替换。
--type-check, --no-type-check
Hvigor默认使能关闭工程中hvigorfile.ts的类型检查，如需开启，可在命令行后添加该选项。
--no-pnpm-frozen-lockfile，--pnpm-frozen-lockfile
Hvigor默认使能不忽略pnpm-lock.yaml文件，如需开启，可在命令行后添加该选项。
忽略pnpm-lock.yaml文件，按照hvigor-config.json5的配置安装Hvigor插件的依赖（如果不忽略pnpm-lock.yaml文件，在使用Hvigor 2.0.0及以上版本的CI场景下安装Hvigor插件依赖时将报错）。
该命令在4.1 Release及以上版本中已废弃。在CI场景中将自动配置，无需开发者手动配置。
--config, -c
指定hvigor-config.json5配置文件中的参数。
当前仅支持设置properties里的参数，具体支持的参数请查看hvigor-config.json5中properties支持的参数。
--config properties.key=value 同 -c properties.key=value
--watch
使能观察模式，主要用于预览和热加载场景。
--generate-build-profile, --no-generate-build-profile
已废弃。使能生成BuildProfile.ets文件。
--node-home <string>
指定nodejs路径。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-cli-V14
爬取时间: 2025-04-30 23:08:45
来源: Huawei Developer
ohpm作为OpenHarmony三方库的包管理工具，支持OpenHarmony共享包的发布、安装和依赖管理。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-system-platform-V14
爬取时间: 2025-04-30 23:09:20
来源: Huawei Developer
ohpm支持在Windows、MacOS、Linux操作系统下使用。
ohpm通过软链接或符号链接的方式构建依赖关系。不同操作系统需满足如下要求：
Windows：
MacOS：
工程代码文件所在文件系统类型需为APFS（macOS系统下默认为APFS）。
如在macOS上挂载了其他不支持符号链接的文件系统（如FAT32或exFAT），则无法在其上创建符号链接。
Linux：
EXT4、Btrfs、XFS、ZFS等常见Linux文件系统类型均满足要求。
部分较老或简单的文件系统（不支持符号链接），可能存在无法在其上创建或正确解析软链接的情况。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpmrc-V14
爬取时间: 2025-04-30 23:09:55
来源: Huawei Developer
ohpm配置文件。
描述
ohpm从命令行和.ohpmrc文件中获取其配置设置。ohpm config命令可用于修改用户级.ohpmrc文件的内容。
文件
注释
.ohpmrc 文件中以 # 或 ; 字符为注释符。
更新配置
执行如下命令可设置用户级配置：
默认配置项
| 配置项  | 字段名称  | 字段说明  | 字段类型  | 默认值  | 备注  |
| --- | --- | --- | --- | --- | --- |
| 仓库设置  | registry  | 下载仓库  | 字符串  | https://ohpm.openharmony.cn/ohpm/  | 可以配置多个仓库地址，以英文逗号间隔，多个仓库地址的优先级按照配置顺序排序。  |
| @group:registry  | 指定仓库  | 字符串  | ""  | 根据group指定组织的仓库地址。支持多个仓库地址，以英文逗号间隔，且优先级大于registry配置，多个仓库地址的优先级按照配置顺序排序。  |
| 发布设置  | publish_registry  | 发布仓库  | 字符串  | https://ohpm.openharmony.cn/ohpm/  | 配置发布的仓库地址，仅支持配置一个仓库地址。  |
| publish_id  | 用户发布号  | 字符串  | ""  | 用户发布号，用来发布三方库，全局唯一。  |
| 路径设置  | cache  | 缓存路径  | 字符串  | ~/.ohpm/cache  | -  |
| key_path  | 私钥路径  | 字符串  | ""  | 利用ssh-keygen工具生成的私钥的放置路径地址。  |
| 网络设置   | no_proxy  | 不使用proxy代理  | 字符串  | ""  | 配置不使用代理的仓库地址，可配置多个，以英文逗号间隔；值可以是域名或者ip，支持二级域名通配符*（例如：*.huawei.com）。  |
| http_proxy  | http代理  | 字符串  | ""  | 支持用户名和密码的网络代理，特殊字符需要转义。示例：http://proxy_server:port。  |
| https_proxy  | https代理  | 字符串  | ""  | 支持用户名和密码的网络代理，特殊字符需要转义。示例：https://proxy_server:port。  |
| strict_ssl  | ssl校验  | 布尔  | true  | 默认值为true，校验https证书；若配置为false，则不校验https证书。  |
| ca_files  | ca证书路径  | 字符串  | ""  | strict_ssl=true时校验服务端证书需要的ca证书放置路径，可以放置多个证书路径，以英文逗号间隔。详情请见：CA证书获取及配置。  |
| fetch_timeout  | 请求超时时间  | 数值  | 60000  | 取值范围：[10000，360000]，单位为毫秒。如果设置的fetch_timeout值不在取值范围内，则默认为：60000。  |
| 并发设置    | max_concurrent  | 最大并发量  | 数值  | 50  | 取值范围：[1, 200]，设置每个模块在安装时允许的最大并发量。  |
| retry_times  | 出错重试次数  | 数值  | 1  | 取值范围：[0, 5], 针对白名单内的异常，程序会按配置重试指定次数，白名单有： ECONNRESET：连接被对端重置ECONNREFUSED：连接被服务器拒绝ETIMEDOUT：连接超时RESPONSETIMEOUT：响应超时TARBADARCHIVE：包格式异常  |
| retry_interval  | 出错重试间隔时间  | 数值  | 1000  | 取值范围：[1000, 60000], 单位毫秒。  |
| 依赖冲突设置   | resolve_conflict  | 开启自动解决依赖版本冲突功能  | 布尔  | true  | 默认开启。当设置为true或缺省时，ohpm会自动处理依赖版本冲突，详情请见：resolve_conflict。  |
| resolve_conflict_strict  | 开启严格模式依赖冲突处理功能  | 布尔  | false  | 默认关闭。当设置为true时，ohpm会按照严格模式处理依赖版本冲突，详情请见：resolve_conflict_strict。  |
| 其他设置             | log_level  | 日志级别  | 字符串  | info  | 可设置日志输出级别，对应级别类型有debug、info、warn、error。  |
| install_all  | 是否安装工程所有模块的依赖  | 布尔  | true  | 默认为true。当设置为true或缺省时，在执行ohpm install、ohpm update、ohpm uninstall时，将会安装工程下所有模块的依赖。详情请见install_all。  |
| :_auth和:_read_auth  | AccessToken配置项  | 字符串  | 无  | ohpm-repo支持使用access token进行认证。详情请见AccessToken。  |
| enforce_dependency_key  | 开启依赖名称校验  | 布尔  | false  | 默认为false。设置为true后，ohpm会校验配置的本地依赖名称与其对应的包名是否一致，若不一致会导致命令执行失败。详情请见enforce_dependency_key。  |
| ensure_dependency_include  | 开启依赖扫描功能  | 布尔  | false  | 默认为false。从ohpm 1.7.0开始，在执行ohpm publish命令时，会检查发布包的源码中，静态导入的三方依赖是否都声明在oh-package.json5的dependencies或dynamicDependencies中。若缺少依赖声明且字段设置为false时，会提示相应告警信息；设置为true时，则会使命令执行失败并提示错误信息。  |
| projectPackageJson:<project_root>  | 工程oh-package.json5配置覆盖  | 字符串  | 无  | 用于覆盖工程根目录下oh-package.json5中的配置。 配置项名称中的<project_root>表示工程根目录路径（根据实际情况替换为真实的工程根目录路径）。配置项的值为指定的工程级oh-package.json5文件的路径，支持使用相对路径（当使用相对路径时，根路径为<project_root>）。  |
| disallow_nested_package  | 开启包内.har/.tgz依赖 配置路径检测  | 布尔  | false  | 默认为false。设置为true后，在执行prepublish/publish时，会扫描包内是否存在'./'形式配置且后缀为.har/.tgz格式的依赖，如果存在，则会使命令执行失败并提示报错信息。  |
| odm_r2_project_root  | 开启overrideDependencyMap中相对路径自动转换功能  | 布尔  | false  | 默认为false。设置为true后，当存在overrideDependencyMap配置且其配置项对应的配置文件内存在相对路径的依赖配置时，ohpm会基于工程根路径解析来查找这些相对路径。详情见odm_r2_project_root。  |
| enable_cross_process_lock  | 启用跨进程锁  | 布尔  | true  | 默认为true。由于oh_modules目录结构限制，ohpm不支持在同一个工程下并行运行多个ohpm install、ohpm update或ohpm uninstall命令，若需要在同一个工程下执行多个ohpm install、ohpm update或ohpm uninstall命令，则必须将该配置设置为true，以保证这多个命令以串行的方式运行。  |
| compability_log_level  | 兼容性字段检测日志等级  | 字符串  | warn  | 默认为warn。在执行prepublish、publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（'compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'），如果未配置，则会根据日志等级打印提示或报错。详情请见compability_log_level。  |
| use_stream_threshold_size  | 流式上传阈值  | 数值  | 5  | 取值范围：[0, 300]，单位mb。当publish三方库的文件体积大于此阈值时将会使用流式上传三方库，如果仓库不存在流式上传接口则自动转为Base64方式上传。  |
| lockfile_stable_order  | oh-package-lock.json5内容稳定排序  | 布尔  | false  | 默认为false。若设置为true，会确保在oh-package.json5文件未变更时，当前已生成的oh-package-lock.json5各字段内容不变。  |
配置项
字段名称
字段说明
字段类型
默认值
备注
仓库设置
registry
下载仓库
字符串
https://ohpm.openharmony.cn/ohpm/
可以配置多个仓库地址，以英文逗号间隔，多个仓库地址的优先级按照配置顺序排序。
@group:registry
指定仓库
字符串
""
根据group指定组织的仓库地址。支持多个仓库地址，以英文逗号间隔，且优先级大于registry配置，多个仓库地址的优先级按照配置顺序排序。
发布设置
publish_registry
发布仓库
字符串
https://ohpm.openharmony.cn/ohpm/
配置发布的仓库地址，仅支持配置一个仓库地址。
publish_id
用户发布号
字符串
""
用户发布号，用来发布三方库，全局唯一。
路径设置
cache
缓存路径
字符串
~/.ohpm/cache
-
key_path
私钥路径
字符串
""
利用ssh-keygen工具生成的私钥的放置路径地址。
网络设置
no_proxy
不使用proxy代理
字符串
""
配置不使用代理的仓库地址，可配置多个，以英文逗号间隔；值可以是域名或者ip，支持二级域名通配符*（例如：*.huawei.com）。
http_proxy
http代理
字符串
""
支持用户名和密码的网络代理，特殊字符需要转义。示例：http://proxy_server:port。
https_proxy
https代理
字符串
""
支持用户名和密码的网络代理，特殊字符需要转义。示例：https://proxy_server:port。
strict_ssl
ssl校验
布尔
true
默认值为true，校验https证书；若配置为false，则不校验https证书。
ca_files
ca证书路径
字符串
""
strict_ssl=true时校验服务端证书需要的ca证书放置路径，可以放置多个证书路径，以英文逗号间隔。详情请见：CA证书获取及配置。
fetch_timeout
请求超时时间
数值
60000
取值范围：[10000，360000]，单位为毫秒。如果设置的fetch_timeout值不在取值范围内，则默认为：60000。
并发设置
max_concurrent
最大并发量
数值
50
取值范围：[1, 200]，设置每个模块在安装时允许的最大并发量。
retry_times
出错重试次数
数值
1
取值范围：[0, 5], 针对白名单内的异常，程序会按配置重试指定次数，白名单有：
retry_interval
出错重试间隔时间
数值
1000
取值范围：[1000, 60000], 单位毫秒。
依赖冲突设置
resolve_conflict
开启自动解决依赖版本冲突功能
布尔
true
默认开启。当设置为true或缺省时，ohpm会自动处理依赖版本冲突，详情请见：resolve_conflict。
resolve_conflict_strict
开启严格模式依赖冲突处理功能
布尔
false
默认关闭。当设置为true时，ohpm会按照严格模式处理依赖版本冲突，详情请见：resolve_conflict_strict。
其他设置
log_level
日志级别
字符串
info
可设置日志输出级别，对应级别类型有debug、info、warn、error。
install_all
是否安装工程所有模块的依赖
布尔
true
默认为true。当设置为true或缺省时，在执行ohpm install、ohpm update、ohpm uninstall时，将会安装工程下所有模块的依赖。详情请见install_all。
:_auth和:_read_auth
AccessToken配置项
字符串
无
ohpm-repo支持使用access token进行认证。详情请见AccessToken。
enforce_dependency_key
开启依赖名称校验
布尔
false
默认为false。设置为true后，ohpm会校验配置的本地依赖名称与其对应的包名是否一致，若不一致会导致命令执行失败。详情请见enforce_dependency_key。
ensure_dependency_include
开启依赖扫描功能
布尔
false
默认为false。从ohpm 1.7.0开始，在执行ohpm publish命令时，会检查发布包的源码中，静态导入的三方依赖是否都声明在oh-package.json5的dependencies或dynamicDependencies中。若缺少依赖声明且字段设置为false时，会提示相应告警信息；设置为true时，则会使命令执行失败并提示错误信息。
projectPackageJson:<project_root>
工程oh-package.json5配置覆盖
字符串
无
用于覆盖工程根目录下oh-package.json5中的配置。
disallow_nested_package
开启包内.har/.tgz依赖
配置路径检测
布尔
false
默认为false。设置为true后，在执行prepublish/publish时，会扫描包内是否存在'./'形式配置且后缀为.har/.tgz格式的依赖，如果存在，则会使命令执行失败并提示报错信息。
odm_r2_project_root
开启overrideDependencyMap中相对路径自动转换功能
布尔
false
默认为false。设置为true后，当存在overrideDependencyMap配置且其配置项对应的配置文件内存在相对路径的依赖配置时，ohpm会基于工程根路径解析来查找这些相对路径。详情见odm_r2_project_root。
enable_cross_process_lock
启用跨进程锁
布尔
true
默认为true。由于oh_modules目录结构限制，ohpm不支持在同一个工程下并行运行多个ohpm install、ohpm update或ohpm uninstall命令，若需要在同一个工程下执行多个ohpm install、ohpm update或ohpm uninstall命令，则必须将该配置设置为true，以保证这多个命令以串行的方式运行。
compability_log_level
兼容性字段检测日志等级
字符串
warn
默认为warn。在执行prepublish、publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（'compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'），如果未配置，则会根据日志等级打印提示或报错。详情请见compability_log_level。
use_stream_threshold_size
流式上传阈值
数值
5
取值范围：[0, 300]，单位mb。当publish三方库的文件体积大于此阈值时将会使用流式上传三方库，如果仓库不存在流式上传接口则自动转为Base64方式上传。
lockfile_stable_order
oh-package-lock.json5内容稳定排序
布尔
false
默认为false。若设置为true，会确保在oh-package.json5文件未变更时，当前已生成的oh-package-lock.json5各字段内容不变。
CA证书获取及配置
依次访问以下证书下载地址，并根据下图操作下载CA证书到本地：
下载证书，请选择保存类型为证书链。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150806.39503732399691329491857889772216:50001231000000:2800:57C22032676FA0D9A37C38759A80DDFAF11823094720F0C39556AB3FBFF983EA.png?needInitFileName=true?needInitFileName=true)
在 .ohpmrc 文件中配置 ca_files=证书路径1,证书路径2。
install_all
在ohpm客户端1.8.0版本的.ohpmrc中支持install_all配置，用于控制ohpm install，ohpm update，ohpm uninstall的行为，install_all在.ohpmrc文件中设置为true或缺省时：
resolve_conflict
ohpm客户端在1.5.0版本开始支持依赖版本冲突自动解决功能。只需要在.ohpmrc文件中，将resolve_conflict配置为true或缺省，即可开启该功能。依赖冲突的处理策略为：当您的项目同时依赖了某个三方库的不同版本时，ohpm将选择其中的最高版本进行安装。
若某个三方库同时存在远程版本和本地版本（本地文件或源码依赖），无论本地版本的版本号是否大于远程版本，ohpm的冲突处理策略都会优先选择本地版本作为待安装的版本。
模块内依赖版本冲突
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.23399581997713055543018743232675:50001231000000:2800:4087D74F80EABAD0A1B5D2C0A1F0D1976E6214DFFDB382DAD16E4ED6120C2C3A.png?needInitFileName=true?needInitFileName=true)
如上图所示的依赖路径中，moduleA 为您正在开发的模块，其直接依赖为 B@1.1，C@1.1。其中 B@1.1 与 C@1.1 分别依赖了 D 的两个版本 D@1.2 与 D@1.3。当您开启了依赖版本冲突自动解决功能，ohpm将会选择 D@1.3 版本作为待安装的版本，最终依赖路径被解析为下图蓝色箭头所指向的路径：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.62288294913191637948860261491474:50001231000000:2800:CE941F3D56DB97633A69B6DFD4F85F06D6B5552B5214924487A393ECCB2EBB2C.png?needInitFileName=true?needInitFileName=true)
模块间依赖版本冲突
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.36616600117908356595932442942471:50001231000000:2800:1386FA0B4A35BF3AA08CECE69E920B3E20FF7CD81D542D6BDEE2A22ADF178B4B.png?needInitFileName=true?needInitFileName=true)
如上图所示的依赖路径中，moduleA、moduleB 为您同一项目下正在开发的两个模块，其中moduleA 依赖 B@1.1，moduleB 依赖 C@1.1，B@1.1 与 C@1.1 分别依赖了 D 的两个版本 D@1.2 与 D@1.3。当您开启了依赖版本冲突自动解决功能，并且您是使用 ohpm install --all 进行安装时，ohpm将会选择 D@1.3 版本作为待安装的版本，最终依赖路径被解析为下图蓝色箭头所指向的路径：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.38907324226778806365863207928595:50001231000000:2800:F8F4D7D35ACAFDE64672E8F766E0F2962AC7498FA1B55D9A97F406EA0B20B3D1.png?needInitFileName=true?needInitFileName=true)
更新依赖版本的场景
当您希望将您某个模块的直接依赖更新成另一个版本，如下图所示，您手动将 C@1.1 更新为 C@1.2：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.40841347715195521782869725450644:50001231000000:2800:2904A0BDB97C8E8E43BF54503571A91A7CCD2F480376DBBE6DB1BDE31A0C0FB0.png?needInitFileName=true?needInitFileName=true)
由于 C 更新为 C@1.2 后，不再依赖 D，若依赖 D 的版本在更新 C 版本之前已经通过 ohpm 的自动冲突处理机制锁定为 D@1.3 版本，此时 C 版本的升级将不会导致 D 的版本由 D@1.3 回退为 D@1.2，这样可以保证每一次更新都只是在上一次结果上进行影响最小的修改，最终的依赖路径将会被解析为下图蓝色箭头所指向的路径：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.00330146323944925993377823004153:50001231000000:2800:07B9EB4290967D63F9AEC81241C976D43F61C1760D36263F7A25B8D940FB5942.png?needInitFileName=true?needInitFileName=true)
对于上述场景，如果希望D版本同时也回退至D@1.2版本，则需要在ohpm install之前执行ohpm clean命令清理各模块下的oh-package-lock.json5文件，以消除上一次安装结果的影响。
ohpm install命令带--target_path选项时依赖冲突处理
target_path下是hvigor在构建时根据目标产物target为各模块自动生成定制的依赖配置文件（oh-package.json5），详见target_path。在生成的oh-package.json5中，依赖的版本部分可能包含targetName，示例："A": "1.0.0+targetName"。
包含targetName信息的版本完整格式为：<major>.<minor>.<patch>[-<pre-release>][+<targetName>]，此时冲突处理规则如下：
1、<major>.<minor>.<patch>[-<pre-release>]部分的比较规则依然遵循上文各场景所描述的处理规则，即取版本号最大的依赖。
2、当两个版本<major>.<minor>.<patch>[-<pre-release>]部分一致时，取尾部有[+<targetName>]信息的依赖。
1、当两个版本尾部均有[+<targetName>]信息，且targetName不一致时，会根据<target_path>/dependencyMap.json5中targetName是否为空进行区分处理。
2、当两个依赖中有一个是本地依赖时，优先取本地依赖；当两个依赖均是本地依赖时，获取本地依赖包内oh-package.json5配置的version再次按照上述规则继续比较。
限制条件说明
由于本功能尚在Beta阶段，存在如下的限制条件：
1.  如难以感知本地文件或本地源码依赖中的版本号，建议使用overrides来处理冲突。
resolve_conflict_strict
ohpm客户端从5.0.9版本，开始支持严格的依赖版本冲突处理机制。在.ohpmrc文件中，将resolve_conflict_strict配置为true开启该功能。
严格模式下，当您的项目同时依赖了某个三方库的不同版本时，ohpm将按照严格模式冲突决策算法决策出最符合要求的版本进行安装，当程序不能决策出符合要求的版本时将报错。
严格模式冲突决策算法
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.82190217079035881688765368416984:50001231000000:2800:1DBE86EC7B3A1D10B9490A927EECC768F8E22A31FA43E7FA85A4F21601B03811.png?needInitFileName=true?needInitFileName=true)
AccessToken
AccessToken是 ohpm-repo 2.1.0版本新引入的认证机制，用户通过ohpm-repo界面生成Token，并将其配置至ohpm客户端配置文件中。
在与 ohpm-repo 交互时，客户端会自动附带Token进行身份验证。该Token分两种权限等级：
每位用户每种权限类型的Token最多可生成10个，首次生成时系统自动复制到剪贴板，后续不再显示完整Token内容。
如何获取AccessToken
当前AccessToken仅 ohpm-repo 支持，在 ohpm-repo 的个人中心->认证管理->AccessToken页面进行生成。
如何配置AccessToken
配置示例如下所示:
其中 ：
enforce_dependency_key
ohpm从1.7.0版本开始，支持在.ohpmrc文件中支持配置enforce_dependency_key，该配置项值为布尔类型，默认为false。将配置设置为true后，ohpm会校验各模块的oh-package.json5中配置的直接依赖中的本地依赖名称与其对应的包名(模块名)是否一致，若不一致会导致依赖安装失败并在错误日志中打印出不一致的依赖名称与其对应的包名(模块名)。
示例：
在MyApplication工程下存在一个名称为foo的模块，foo模块的oh-package.json5如下所示：
在MyApplication工程下存在另一个名称为bar的模块，且bar模块中依赖了foo模块，bar模块的oh-package.json5如下所示：
如上所示，bar模块的oh-package.json5中配置了对foo模块的依赖，并为foo模块起了一个别名为fee。当在.ohpmrc中将enforce_dependency_key配置为true时：
此时在MyApplication下执行ohpm install --all命令将打印如下错误日志，同时会中断命令的执行：
若没有配置enforce_dependency_key或将其配置为false时，命令将不会被中断，同时上述错误日志的日志级别将会下调为告警日志：
建议在.ohpmrc文件中配置enforce_dependency_key为true，禁止以别名的方式配置本地依赖，避免出现如下场景：
基于上述示例，在MyApplication下真的存在一个名称为fee的模块，且该模块的版本号小于foo模块，fee模块的oh-package.json5如下所示：
且entry模块中同时依赖了fee与bar，entry模块的oh-package.json5依赖配置如下所示：
此时在entry的依赖树中，依赖fee存在两个版本：一个别名为fee的foo模块，一个名称为fee的fee模块，若此时开启了resolve_conflict，由于fee模块的实际版本号为1.0.0要小于foo模块的版本号2.0.0，在执行ohpm install时将只会在entry模块的oh_modules下安装以fee为别名的foo模块，而实际的fee模块则不会被安装，如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.79834924381791074128717981219902:50001231000000:2800:8C54AAF7119864880C90AE3A653662B9D07A41DCA1A8B3B66D3486C814B5DCF3.png?needInitFileName=true?needInitFileName=true)
在entry的oh_modules下会生成一个名称为fee的软连接，该链接却指向foo模块的实际路径：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150807.74901351748841382256587243242980:50001231000000:2800:D9FAB97EBBE6139FB0B670865A7205F7578C998AC8F07768E9E12EFC1CC286D8.png?needInitFileName=true?needInitFileName=true)
如果entry实际希望依赖的是真实的fee模块而不是foo模块，则此时会导致entry无法编译成功。
1、从ohpm客户端5.0.7开始，若项目级build-profile.json5文件中strictMode字段下配置了useNormalizedOHMUrl开关且useNormalizedOHMUrl=true，则该配置优先级高于enforce_dependency_key，如果ohpm检测到依赖别名与oh-package.json5中name不一致时，会报错提示并中止程序执行；若未配置useNormalizedOHMUrl或useNormalizedOHMUrl=false时，是否校验别名一致性则根据enforce_dependency_key配置决定。
2、项目级build-profile.json5文件中，products节点下任意product字段配置了useNormalizedOHMUrl=true，则ohpm中useNormalizedOHMUrl开关会被设置为true，即ohpm检测到项目中依赖别名与oh-package.json5中name不一致时，会报错提示并中止程序执行。
odm_r2_project_root
odm_r2_project_root是ohpm客户端1.8.0新增的开关配置，默认为false，可以通过config命令或直接在.ohpmrc文件中修改其值。
当该配置为true时，若在overrideDependencyMap中配置的依赖项替换文件中存在以相对路径配置的本地依赖项时，在ohpm运行时会基于工程根路径来查找这些本地依赖项。
示例：
如上第3步所示，当odm_r2_project_root开关设置为true时，在ohpm运行时会以工程根目录为起点查找"./test.har"，比如：工程根路径为：D:\path\to\MyProject，在ohpm运行时解析得到test.har的绝对路径为：D:\path\to\MyProject\test.har。
compability_log_level
ohpm客户端从5.0.1开始新增开关配置'compability_log_level'字段，用于控制在缺少兼容性检测需要的字段时ohpm的处理逻辑。
compability_log_level字段默认赋值为'warn'，可配置的日志等级请见开关配置项说明。
在执行prepublish、publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'），详见模块级oh-package.json5字段说明，下面统称 '兼容性字段'，如果未配置，则会根据日志等级打印提示或报错。
开关配置项说明

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-oh-package-json5-V14
爬取时间: 2025-04-30 23:10:30
来源: Huawei Developer
从OHPM 5.0.0版本开始，支持区分工程级与模块级oh-package.json5配置。其中：
开发者可将标准的DevEco Studio工程下的各个模块打成HAR包后，发布到OpenHarmony三方库中心仓；所有发布到仓库的包必须包含模块级oh-package.json5文件，以描述当前包基本信息。
工程级oh-package.json5 字段说明
| 配置项 | 字段名称 | 字段说明 | 字段要求 | 字段类型 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 开发态版本 | modelVersion | 开发态版本号 | 必选 | 字符串 | 无 | 开发态版本号。 |
| 描述配置 | description | 简介 | 可选 | 字符串 | 无 | 用于描述工程信息的字符串。 |
| 依赖配置     | dependencies | 生产依赖 | 可选 | 对象 | {} | 用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（不建议在工程级oh-package.json5中配置生产依赖）。 |
| devDependencies | 开发依赖 | 可选 | 对象 | {} | 配置开发态依赖，配置只能参与项目的开发或测试阶段的依赖。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（如手机）上使用，则不能在其中配置。 |
| dynamicDependencies | 动态依赖 | 可选 | 对象 | {} | 配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用（不建议在工程级oh-package.json5中配置动态依赖）。 |
| overrides | 依赖覆盖配置 | 可选 | 对象 | {} | 支持将依赖树中的包替换为另一个指定版本，详情见overrides。 |
| overrideDependencyMap | 重写依赖关系 | 可选 | 对象 | {} | 支持将依赖树中包的子依赖替换为配置文件中配置的依赖，详情见overrideDependencyMap。 |
| 其他 | scripts | 自定义脚本 | 可选 | 对象 | {} | 维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。 |
| hooks | 钩子 | 可选 | 对象 | {} | 安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。 |
| parameterFile | 参数化配置文件路径 | 可选 | 字符串 | 无 | 标识是否开启参数化。未配置：关闭参数化；已配置：开启参数化。需同时指定参数化配置文件路径，详见parameterFile。 |
配置项
字段名称
字段说明
字段要求
字段类型
默认值
备注
开发态版本
modelVersion
开发态版本号
必选
字符串
无
开发态版本号。
描述配置
description
简介
可选
字符串
无
用于描述工程信息的字符串。
依赖配置
dependencies
生产依赖
可选
对象
{}
用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（不建议在工程级oh-package.json5中配置生产依赖）。
devDependencies
开发依赖
可选
对象
{}
配置开发态依赖，配置只能参与项目的开发或测试阶段的依赖。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（如手机）上使用，则不能在其中配置。
dynamicDependencies
动态依赖
可选
对象
{}
配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用（不建议在工程级oh-package.json5中配置动态依赖）。
overrides
依赖覆盖配置
可选
对象
{}
支持将依赖树中的包替换为另一个指定版本，详情见overrides。
overrideDependencyMap
重写依赖关系
可选
对象
{}
支持将依赖树中包的子依赖替换为配置文件中配置的依赖，详情见overrideDependencyMap。
其他
scripts
自定义脚本
可选
对象
{}
维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。
hooks
钩子
可选
对象
{}
安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。
parameterFile
参数化配置文件路径
可选
字符串
无
标识是否开启参数化。未配置：关闭参数化；已配置：开启参数化。需同时指定参数化配置文件路径，详见parameterFile。
不建议在工程级依赖中配置非devDependencies的依赖，即一个Hsp/Har模块的非开发态依赖都要在相应模块的dependencies和dynamicDependencies中声明。
模块级oh-package.json5字段说明
| 配置项 | 字段名称 | 字段说明 | 字段要求 | 字段类型 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 描述配置        | name | 名称 | 必选 | 字符串 | 无 | 格式为：@group/packagename或packagename，长度：[1, 128]，全局唯一，即一个应用中，不同package的package name不能重名。建议name命名时包含组织名称group，便于管理和识别三方库。 name中只有在存在组织名称group时，才能有且仅能有一个'@'符号，有且仅有一个路径分隔符'/'。 组织名称group格式： 1、仅允许以小写字母开头，可由小写字母、数字、中划线(-)、下划线(_)组成。 2、禁止以中划线（-）、下划线（_）结尾。 3、不允许为ArkTS 的保留关键字。 packagename格式： 1、仅允许以小写字母开头，可由小写字母、数字、点（.）、中划线（-）、下划线（_）组成。 2、禁止以点（.）、中划线（-）、下划线（_）结尾。 3、不允许为ArkTS的保留关键字。 |
| version | 版本号 | 必选 | 字符串 | 1.0.0 | 必须遵循 semver 语义化规范，从1.0.0开始。 |
| description | 简介 | 可选 | 字符串 | 无 | 用于描述三方库信息的字符串，有助于被搜索发现。 |
| keywords | 关键字 | 可选 | 数组 | [] | 关键字信息数组，便于搜索使用。例如：["tools", "project"]。 |
| author | 作者 | 可选 | 对象或字符串 | 无 | 包含 name 字段（可选）和 email 字段（可选），例如："author": {"name": "xxx" , "email": "xxx@xxx.com" }。或者直接为作者名称，例如："author": "xxx"。 name字段允许使用字母、数字，点（.），中划线（-），下划线（_），空格，中文。其中首字母必须为英文字母。 |
| homepage | 主页链接 | 可选 | 字符串 | "" | 通常是项目gitee链接。 |
| repository | 仓库地址 | 可选 | 字符串 | "" | 开源代码仓库地址。在私仓管理界面的系统设置处可定义是否为必填。 |
| license | 开源协议 | 必选 | 字符串 | "ISC" | 当前项目的开源许可证。遵循 spdx license 规范。许可证若为 GPL，repository 建议不为空。 |
| 依赖配置    | dependencies | 生产依赖 | 可选 | 对象 | {} | 用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（参与编译/运行阶段使用的依赖）。 |
| devDependencies | 开发依赖 | 可选 | 对象 | {} | 用于配置开发态依赖，只能参与项目的开发或测试阶段。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（手机）上使用，则不能在其中配置。 |
| dynamicDependencies | 动态依赖 | 可选 | 对象 | {} | 用于配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用。 |
| 文件配置  | main | 入口 | 必选 | 字符串 | 无 | 指定加载的入口文件。 |
| types | 类型定义 | 可选 | 字符串 | "" | 指定类型定义的文件名。当用 typescript 定义新的类型，需要提供给其他开发者使用，则需要指定其声明文件，一般为 .d.ts，.d.ets 文件。 |
| 兼容性检测相关配置    | compatibleSdkVersion | SDK版本 | 可选 | 字符串 | 无 | 三方库开发者使用的SDK版本，构建时由Hvigor自动填充，提供给SDK做兼容性检测。 在prepublish、publish时，ohpm会对该字段进行检测(非空和长度校验)，并根据.ohpmrc中开关 compability_log_level配置的值进行提示或报错处理。 配置示例参看兼容性字段配置示例。 |
| compatibleSdkType | SDK类型 | 可选 | 字符串 | 无 | 三方库开发者使用的SDK类型，构建时由Hvigor自动填充，提供给SDK做兼容性检测, 示例值："OpenHarmony"、"HarmonyOS"。 在prepublish、publish时，ohpm会对该字段进行检测(非空和长度校验)，并根据.ohpmrc中开关 compability_log_level配置的值进行提示或报错处理。 配置示例参看兼容性字段配置示例。 |
| obfuscated | 混淆标识 | 可选 | 布尔 | 无 | 三方库是否开启混淆标识，构建时由Hvigor自动填充，提供给SDK做兼容性检测。 在prepublish、publish时，ohpm会对该字段进行检测(非空校验)，并根据.ohpmrc中开关 compability_log_level配置的值进行提示或报错处理。 配置示例参看兼容性字段配置示例。 |
| nativeComponents | native so依赖配置 | 可选 | 数组 | 无 | 三方库使用的so包配置，构建时由Hvigor自动填充，提供给SDK做兼容性检测。 对于用户自行引入的so依赖(存放于libs目录)，需要用户手动维护该数组，数组单个元素类型为对象，对象内可配置的字段有：name、compatibleSdkVersion、compatibleSdkType。 在prepublish、publish时，如果包内存在so包，则ohpm会对该字段进行检测，并根据.ohpmrc中开关 compability_log_level 配置的值进行提示或报错处理；反之则不检测该字段。 配置示例参看兼容性字段配置示例。 |
| 其他       | artifactType | 类型 | 可选 | 字符串 | "original" | OpenHarmony包制品类型，有两个选项：original、obfuscation。original：源码，即发布源码(.ts/.ets)；obfuscation：混淆代码，即源码经过混淆之后发布上传。 |
| scripts | 自定义脚本 | 可选 | 对象 | {} | 维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。 |
| hooks | 钩子 | 可选 | 对象 | {} | 安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。 |
| category | 检查规则白名单 | 可选 | 字符串 | {} | 在私仓管理界面配置后自动生成，白名单为分号隔开的字符串列表，每个列表项必须是一个由大小写字母或下划线组成的字符串，包含在白名单中的配置项，不再做规则检查。 |
| packageType | 包类型 | 可选 | 字符串 | InterfaceHar | 标识模块是否为HSP包，在新建Shared Library时会自动生成该字段，并默认赋值为"InterfaceHar"；Static Library中没有该字段，标识为普通HAR包。 |
配置项
字段名称
字段说明
字段要求
字段类型
默认值
备注
描述配置
name
名称
必选
字符串
无
格式为：@group/packagename或packagename，长度：[1, 128]，全局唯一，即一个应用中，不同package的package name不能重名。建议name命名时包含组织名称group，便于管理和识别三方库。
name中只有在存在组织名称group时，才能有且仅能有一个'@'符号，有且仅有一个路径分隔符'/'。
组织名称group格式：
1、仅允许以小写字母开头，可由小写字母、数字、中划线(-)、下划线(_)组成。
2、禁止以中划线（-）、下划线（_）结尾。
3、不允许为ArkTS 的保留关键字。
packagename格式：
1、仅允许以小写字母开头，可由小写字母、数字、点（.）、中划线（-）、下划线（_）组成。
2、禁止以点（.）、中划线（-）、下划线（_）结尾。
3、不允许为ArkTS的保留关键字。
version
版本号
必选
字符串
1.0.0
必须遵循semver语义化规范，从1.0.0开始。
description
简介
可选
字符串
无
用于描述三方库信息的字符串，有助于被搜索发现。
keywords
关键字
可选
数组
[]
关键字信息数组，便于搜索使用。例如：["tools", "project"]。
author
作者
可选
对象或字符串
无
包含 name 字段（可选）和 email 字段（可选），例如："author": {"name": "xxx" , "email": "xxx@xxx.com" }。或者直接为作者名称，例如："author": "xxx"。
name字段允许使用字母、数字，点（.），中划线（-），下划线（_），空格，中文。其中首字母必须为英文字母。
homepage
主页链接
可选
字符串
""
通常是项目gitee链接。
repository
仓库地址
可选
字符串
""
开源代码仓库地址。在私仓管理界面的系统设置处可定义是否为必填。
license
开源协议
必选
字符串
"ISC"
当前项目的开源许可证。遵循spdx license规范。许可证若为 GPL，repository 建议不为空。
依赖配置
dependencies
生产依赖
可选
对象
{}
用于配置参与编译/运行阶段使用的依赖，声明需要在代码中import的三方库（参与编译/运行阶段使用的依赖）。
devDependencies
开发依赖
可选
对象
{}
用于配置开发态依赖，只能参与项目的开发或测试阶段。如果被依赖的组件最终要与依赖的组件一起发布到目标机器（手机）上使用，则不能在其中配置。
dynamicDependencies
动态依赖
可选
对象
{}
用于配置项目动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用。
文件配置
main
入口
必选
字符串
无
指定加载的入口文件。
types
类型定义
可选
字符串
""
指定类型定义的文件名。当用 typescript 定义新的类型，需要提供给其他开发者使用，则需要指定其声明文件，一般为 .d.ts，.d.ets 文件。
兼容性检测相关配置
compatibleSdkVersion
SDK版本
可选
字符串
无
三方库开发者使用的SDK版本，构建时由Hvigor自动填充，提供给SDK做兼容性检测。
在prepublish、publish时，ohpm会对该字段进行检测(非空和长度校验)，并根据.ohpmrc中开关compability_log_level配置的值进行提示或报错处理。
配置示例参看兼容性字段配置示例。
compatibleSdkType
SDK类型
可选
字符串
无
三方库开发者使用的SDK类型，构建时由Hvigor自动填充，提供给SDK做兼容性检测, 示例值："OpenHarmony"、"HarmonyOS"。
在prepublish、publish时，ohpm会对该字段进行检测(非空和长度校验)，并根据.ohpmrc中开关compability_log_level配置的值进行提示或报错处理。
配置示例参看兼容性字段配置示例。
obfuscated
混淆标识
可选
布尔
无
三方库是否开启混淆标识，构建时由Hvigor自动填充，提供给SDK做兼容性检测。
在prepublish、publish时，ohpm会对该字段进行检测(非空校验)，并根据.ohpmrc中开关compability_log_level配置的值进行提示或报错处理。
配置示例参看兼容性字段配置示例。
nativeComponents
native so依赖配置
可选
数组
无
三方库使用的so包配置，构建时由Hvigor自动填充，提供给SDK做兼容性检测。
对于用户自行引入的so依赖(存放于libs目录)，需要用户手动维护该数组，数组单个元素类型为对象，对象内可配置的字段有：name、compatibleSdkVersion、compatibleSdkType。
在prepublish、publish时，如果包内存在so包，则ohpm会对该字段进行检测，并根据.ohpmrc中开关compability_log_level配置的值进行提示或报错处理；反之则不检测该字段。
配置示例参看兼容性字段配置示例。
其他
artifactType
类型
可选
字符串
"original"
OpenHarmony包制品类型，有两个选项：original、obfuscation。original：源码，即发布源码(.ts/.ets)；obfuscation：混淆代码，即源码经过混淆之后发布上传。
scripts
自定义脚本
可选
对象
{}
维护一个脚本别名到脚本内容的映射表，开发者可以通过ohpm run <脚本别名>来触发对应脚本内容的执行。
hooks
钩子
可选
对象
{}
安装或卸载的钩子设置，包含 "preInstall", "postInstall", "preUninstall", "postUninstall","preVersion", "postVersion", "prePublish", "postPublish" 字段。仅支持执行当前工程中的 hooks，不支持执行依赖中的 hooks。
category
检查规则白名单
可选
字符串
{}
在私仓管理界面配置后自动生成，白名单为分号隔开的字符串列表，每个列表项必须是一个由大小写字母或下划线组成的字符串，包含在白名单中的配置项，不再做规则检查。
packageType
包类型
可选
字符串
InterfaceHar
标识模块是否为HSP包，在新建Shared Library时会自动生成该字段，并默认赋值为"InterfaceHar"；Static Library中没有该字段，标识为普通HAR包。
依赖名使用要求：
1、在oh-package.json5文件中dependencies、devDependencies、dynamicDependencies节点声明本地依赖时，允许配置的依赖名和依赖包的包名（即包内oh-package.json5中配置的name）不一致，但不推荐该用法，在默认情况下ohpm会通过告警日志来提示此类问题。
若希望将告警升级为报错并中断命令执行，可以通过在.ohpmrc中配置enforce_dependency_key=true；或在项目级build-profile.json5文件中将strictMode字段下配置useNormalizedOHMUrl=true。
2、使用参数化配置时，依赖名和依赖包的包名（即包内oh-package.json5中配置的name）必须保持一致，否则会报错并中断命令执行。
3、在oh-package.json5、overrideDependencyMap、parameterFile文件中，不建议使用无效的转义字符（例如：\a、\e、\o等）或Unicode编码（例如：\uxxxx）。
兼容性字段配置示例
三方库开发者使用的SDK和当前集成该三方库工程编译时使用的SDK可能存在不一致的情况。因此，ohpm新增了兼容性检测相关配置以帮助SDK做兼容性分析。配置示例如下：
创建一个新的oh-package.json5文件
通过命令行创建 oh-package.json5文件，执行如下命令：
1.  导航到包的目录。
2.  执行初始化命令，并按照问卷填写相关参数。 对无命名空间模块，执行以下命令： 对有命名空间模块，执行以下命令：
3.  对无命名空间模块，执行以下命令：
4.  对有命名空间模块，执行以下命令：
5.  若跳过问卷填写，创建默认文件，可在初始化命令行加上配置参数 --yes。 默认创建的oh-package.json5 文件示例：
-  对无命名空间模块，执行以下命令：
-  对有命名空间模块，执行以下命令：
依赖配置说明
ohpm 存在 dependencies，devDependencies和dynamicDependencies 三种依赖类型。同时支持具体版本号，范围版本号，tag标签，本地har/tgz文件路径和本地源码目录多种方式引入依赖。
```json
{
"dependencies": {
// 具体版本号引入，支持符合semver标准的版本号
"specific_version": "1.0.0",
// 范围版本号引入，^引入1.x.x的最新版本，~引入1.0.x的最新版本。范围版本优先选取正式版本，无匹配的正式版本才会选取先行版本
"scope_version": "^1.0.1",
// tag标签引入，示例引入标签为"beta"对应的版本号
"tag_version": "tag:beta",
// 本地文件引入，可引入本地har/tgz文件
"local_file": "file:./xx.har",
// 本地源码引入，可引入本地其他模块的源码，示例直接引入本地的"module1"模块
"local_source_code": "file:../module1"
},
"devDependencies": {
// 支持依赖引入类型同dependencies
},
"dynamicDependencies": {
// 支持依赖引入类型同 dependencies
}
}
```
overrides
ohpm客户端在1.4.0版本开始支持Override机制，可以在项目级别的oh-package.json5（即项目根目录下的oh-package.json5）文件中添加overrides配置，方便将依赖树中的依赖替换为另一个版本。替换的版本既可以是一个具体的版本号，也可以是一个模糊版本，还可以是本地存在的HAR包或源码目录。
例如，想要确保foo始终安装1.0.0版本，可以在项目级的oh-package.json5中增加如下配置：
overrides必须配置在项目级别的oh-package.json5中，配置在模块级别的oh-package.json5中将不会生效。
```json
{
"overrides": {
"foo": "1.0.0"
}
}
```
若本地存在foo的源码或者HAR包，想确保foo始终使用您本地的版本，可以在项目级的oh-package.json5中如下配置：
```json
{
"overrides": {
// 本地存在"foo"的源码目录，如项目根目录下的foo目录
// "foo": "file:./foo"
// 本地存在"foo"的HAR文件，如项目根目录下的libs目录中的foo.har
"foo": "file:./libs/foo.har"
}
}
```
parameterFile
OHPM新增了参数化配置功能。开发者可在项目根目录配置一个参数化文件（json5格式文件），在该文件中维护模块或依赖版本信息，不同模块将根据该文件中的版本进行配置，满足不同构建场景下，开发者快速切换依赖版本的需要。同时，支持通过命令行指定参数化文件，降低流水线场景下模块和依赖版本的变更难度。
OHPM客户端在1.6.0版本开始支持参数化配置。可以在项目级别的oh-package.json5文件（即项目根目录下的oh-package.json5）中添加parameterFile配置，并同时指定parameterFile文件路径。配置规则如下：
基础配置示例
工程级oh-package.json5示例：
```json
{
"modelVersion": "5.0.2",
"description": "Please describe the project information.",
...
"parameterFile": './parameterFile/parameterFile.json5' // 开启参数化并指定参数化配置文件路径
}
```
模块级oh-package.json5示例：
```json
{
"name": "parameter-test",
"version": "@param:version", //使用时必须以 '@param:' 开头
"description": "test desc.",
"main": "index.ets",
"author": "test author",
"license": "ISC",
"dependencies": {
"libtest1": "@param:dependencies.libtest1"
},
"devDependencies": {
"libtest2": "@param:devDependencies.libtest2"
},
"dynamicDependencies": {
"libtest3": "@param:dynamicDependencies.libtest3"
},
}
```
parameterFile所指向文件的配置示例：
```json
{
"version": "1.0.0",
"dependencies": {
"libtest1": "1.0.1"
},
"devDependencies": {
"libtest2": "*"
},
"dynamicDependencies": {
"libtest3": "latest"
}
}
```
一仓多包示例
一个代码仓有多个har/hsp模块，发包时，一般需要开发者手动修改所有模块的版本号后再打包发布，若模块较多，操作繁琐且效率低下，建议使用参数化配置解决该问题，详细示例如下。
当所有模块版本不一致：
如下工程结构所示，所有模块的oh-package.json5中version字段均配置参数化版本（'@param:'开头部分），不同模块的版本均不一致，但都由参数化配置文件'parameter.json'全局统一管理；发包前，只需修改'parameter.json'文件中相关模块的版本，再构建所有模块即可；打包构建时，所有模块的参数化版本均会被替换为'parameter.json'中配置的具体版本（如：@param:har1会被替换为：1.0.0）。
当所有模块版本一致：
如下工程结构所示，所有模块均使用同一个参数化版本（@param:module_version），发包前，只需修改'parameter.json'中module_version的值, 再构建所有模块即可；打包构建时，所有模块的参数化版本均会被替换为'parameter.json'中module_version对应的版本（如：@param:module_version会被替换为：1.0.0）。
overrideDependencyMap
OHPM客户端在1.7.0版本开始支持使用overrideDependencyMap机制重写源码模块或三方库的依赖关系。开发者可在工程级oh-package.json5文件中新增overrideDependencyMap配置，在该配置对象中通过key-value形式配置依赖关系重写文件；其中，key为依赖标识符，value为依赖关系重写文件路径。在依赖安装时， ohpm会将依赖树中的某个依赖节点的所有直接子依赖替换为对应依赖关系重写文件中配置的依赖项，依赖关系重写文件中支持配置的依赖类型为dependencies、devDependencies、dynamicDependencies，通过使用overrideDependencyMap机制，可以满足开发者在不同场景下，动态变更依赖的需求。
同时，支持在.ohpmrc中使用projectPackageJson配置项来覆盖项目根目录下oh-package.json5中的配置，方便开发者快速切换配置，详情见ohpmrc中projectPackageJson配置。
配置说明
-  "[@group/]libname[@version]" : "config_path"，其中 [@group/]libname[@version] 为依赖标识符key, config_path为配置文件路径value。
overrideDependencyMap场景示例
.ohpmrc中projectPackageJson配置
通过在.ohpmrc文件中配置projectPackageJson，可同时实现对overrides、overrideDependencyMap字段配置的效果，替换项目级oh-package.json5文件中相应的配置，方便开发者在不同使用场景下快速切换使用。配置格式及使用约束如下所示：
-  projectPackageJson:<project_root>=<config_path>, 其中 projectPackageJson:<project_root> 部分视做key, config_path 部分视做value。配置key指定项目根目录路径（绝对路径），配置value指定json5格式配置文件路径用以覆盖项目级oh-package.json5中的配置。
-  projectPackageJson:D:\test\TestProject=projectPackageJson.json5
示例
下面演示在.ohpmrc中配置同一工程的不同环境下的projectPackageJson配置，当配置生效时，会直接覆盖项目级oh-package.json5中对应配置。
oh-package-lock.json5
oh-package-lock.json5用于锁定所有依赖的版本，以及缓存依赖的元数据信息。不建议开发者手动修改该文件的内容，也不建议开发者使用其他分析工具直接读取该文件的内容。
建议将oh-package-lock.json5文件提交到代码仓库中进行版本管理。优点如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-common-commands-V14
爬取时间: 2025-04-30 23:11:05
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-config-V14
爬取时间: 2025-04-30 23:11:39
来源: Huawei Developer
设置ohpm用户级配置项。
命令格式
配置文件中信息以键值对<key> = <value>形式存在。
功能描述
ohpm 从命令行和 .ohpmrc 文件中获取其配置设置。有关更多 .ohpmrc 文件信息和可用配置选项，请参阅ohpmrc章节。
ohpm config 仅支持配置项字段（默认项字段请查阅ohpmrc章节），且仅支持修改用户级目录下的 .ohpmrc 文件。
子命令
set
在用户级目录下 .ohpmrc 文件中，以键值对<key> = <value>形式写入数据。
get
将从命令行，项目级 .ohpmrc 文件，用户级 .ohpmrc 文件（优先级依次递减）中获取的值进行标准输出。
如果未提供键值，则此命令执行效果与命令 ohpm config list 相同。
list
显示所有配置项。
delete
删除用户级目录下 ohpmrc 文件中指定的键值。
Options
json
可以在 config list 命令后面配置 -j或者--json 参数，以 json 格式输出所有配置项及默认值。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-help-V14
爬取时间: 2025-04-30 23:12:14
来源: Huawei Developer
获取有关 ohpm 的帮助。
命令格式
command：命令名称。
功能描述
如果提供了命令名称，则显示相应命令的帮助信息。
如果提供的命令名称不存在或未提供，则显示所有命令的概要信息。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150808.11564569110059783878009117665580:50001231000000:2800:8D11D7373E34D89CDD0B80E4619A020228C5D8AA0CB58279989524F55AF07931.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-info-V14
爬取时间: 2025-04-30 23:12:50
来源: Huawei Developer
查询指定三方库的具体信息。
命令格式
功能描述
用于调用云端查询接口，查看指定包的详细信息，并将结果进行标准输出。
Options
registry
可以在 info 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
fetch_timeout
可以在 info 命令后面配置 -ft <number> 或者 --fetch_timeout <number> 参数，用以设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 info 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验https证书。
上述选项中配置的registry，fetch_timeout和strict_ssl，仅在执行当前info命令时生效，不会修改项目级或者用户级的配置文件。
示例
执行以下命令：
结果示例：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-init-V14
爬取时间: 2025-04-30 23:13:24
来源: Huawei Developer
创建 oh-package.json5 文件。
命令格式
功能描述
在工作目录下，生成一个新的 oh-package.json5 文件，初始化一个 package。
执行命令时，命令行会出现交互界面，可填写一系列关于三方库的基本信息，例如：三方库名称、版本等。ohpm 会根据现有字段、依赖项和所选选项做出合理的猜测，它会保留已设置的任何字段和值，在工作目录下创建一个 oh-package.json5 文件。
Options
yes
可以在 init 命令后面指定 -y或者--yes 参数，命令行将会完全跳过交互界面，创建默认的 oh-package.json5 文件。
默认内容如下：
若当前工作目录下不存在 oh-package.json5 文件，则文件中 name 字段默认为当前工作目录名称；若当前工作目录下已存在 oh-package.json5 文件，则新文件中 name 字段复用已存在文件中的 name 字段，并且最后覆盖原有oh-package.json5文件。
group
可以在 init 命令后面配置 -g <group_name> 或者 --group <group_name>参数，创建一个 oh-package.json5 文件，其中 name 字段的命名空间为 @group_name。
示例
-  当前工作目录下不存在 oh-package.json5 文件。 在" D:\demo " 路径下，执行如下命令： 执行结果为：
-  当前工作目录下已存在其中 name 字段为 demo_name 的 oh-package.json5 文件。 在" D:\demo " 路径下，执行如下命令： 执行结果为：
-  创建一个 oh-package.json5 文件，其中参数 name 字段为 "@group_name/demo" ，而不是仅为 "demo"。 执行结果为：问卷中 name 字段自动显示为 @group_name/demo。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-install-V14
爬取时间: 2025-04-30 23:13:59
来源: Huawei Developer
安装三方库。
命令格式
功能描述
用于安装指定组件或 oh-package.json5 文件中所有的依赖。如果存在 oh-package-lock.json5 文件，安装将取决于 oh-package-lock.json5 文件中锁定的版本。
-  ohpm install 将依赖项安装到本地 oh_modules 文件夹中，并将所有依赖项作为 dependencies，写入 oh-package.json5 文件。
-  ohpm install <folder> 安装本地文件夹，则默认会创建一个软链接指向该文件夹。 示例：
-  ohpm install <har file> 安装压缩包，请注意压缩包的要求： 示例：
Options
all
可以在 install 命令后面配置 --all 参数，安装您项目下所有模块在其 oh-package.json5 中配置的全部依赖项。
save-dynamic
可以在 install 命令后面配置 --save-dynamic 参数，安装的三方库信息将会写入 oh-package.json5 文件的 dynamicDependencies 中。
save-dev
可以在 install 命令后面配置 --save-dev 参数，安装的三方库信息将会写入 oh-package.json5 文件的 devDependencies 中。
save-prod
可以在 install 命令后面配置 --save-prod 参数，安装的三方库信息将会写入 oh-package.json5 文件的 dependencies 中，这是 ohpm 的默认行为。
no-save
可以在 install 命令后面配置 --no-save 参数，安装的三方库信息将不会写入 oh-package.json5 文件中。
prefix
可以在 install 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
parameterFile
可以在 install 命令后面配置 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。
registry
可以在 install 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
fetch_timeout
可以在 install 命令后面配置 -ft <number> 或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 install 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
max_concurrent
可以在 install 命令后面配置 -mc <number> 或者 --max_concurrent <number> 参数，设置最大活动并发请求数（即ohpm操作期间任何时间的最大网络请求数），如果没有指定，默认最大并发请求数为50次。
retry_times
可以在 install 命令后面配置 -rt <number> 或者 --retry_times <number> 参数，设置操作失败前的最大重试次数，如果没有指定，默认最大重试次数为1次。
retry_interval
可以在 install 命令后面配置 -ri <number> 或者 --retry_interval <number> 参数，设置重试失败前的等待时间，如果没有指定，默认等待时间为1000ms。
experimental-concurrently-safe
可以在 install 命令后面配置 --experimental-concurrently-safe 参数，并发安全地安装依赖。这是一个实验性选项。
target_path
可以在 install 命令后面配置 --target_path <string> 参数，用来指定在特定目标产物target语境下各模块的依赖配置文件（oh-package.json5）的路径。在执行ohpm install时，ohpm会优先安装<target_path>/<moduleName>/oh-package.json5文件中依赖。详情参见target_path。
示例
安装 lottie 三方库，执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150808.40240009637737477788125296791867:50001231000000:2800:BA5C7523CEF81A6D25FF068FB964BA98A58B05E12589C2CD4C591F6A8AE70CFA.png?needInitFileName=true?needInitFileName=true)
oh_modules
ohpm 1.0.0~1.3.0
使用 ohpm 安装时，项目中各 Module 的依赖项被统一安装在 Module 根目录下的 oh_modules 目录中，Module 中所有直接依赖和间接依赖都以平铺的方式存储在 oh_modules 目录下的 .ohpm 目录中，Module 的直接依赖则以软链接的方式添加进 oh_modules 文件夹的根目录中。因此，相同依赖项只会安装一次，从而减少磁盘使用空间，加快安装速度。
ohpm 1.4.x
ohpm 客户端从 1.4.0 版本开始，同一项目下所有 Module 的依赖都会被统一安装在项目根目录下的 oh_modules 目录中，同时会在项目各 Module 根目录下的 oh_modules 中生成该 Module 的直接依赖的软连接，这些软连接会指向项目根目录下 oh_modules 中的 .ohpm 目录下依赖实际存储目录。
target_path
为了支持在构建过程中针对不同的产物定制不同的依赖，Hvigor会在构建时根据目标产物target为各模块自动生成定制的依赖配置文件（oh-package.json5），开发者可以在ohpm install时使用target_path选项来指定在特定目标产物target语境下各模块的依赖配置文件（oh-package.json5）的路径。
ohpm会优先安装<target_path>/moduleName/oh-package.json5文件中配置的依赖，并在<project_root>/moduleName下生成对应的oh-package-<targetName>-lock.json5文件。当指定target_path时，默认会开启依赖版本冲突自动处理功能，在依赖安装完成后，ohpm还会根据实际安装的依赖版本在<target_path>/resolve-conflict/moduleName目录下生成新的oh-package.json5文件。
target_path目录结构示例：
dependencyMap.json5内容示例：
ohpm install指定target_path时依赖配置优先级说明：
1、<target_path>/dependencyMap.json5中rootDependency配置的oh-package.json5的优先级高于<project_root>/oh-package.json5。
2、.ohpmrc中projectPackageJson指定的项目级配置文件中overrides、overrideDependencyMap配置优先级同时高于<target_path>/dependencyMap.json5中rootDependency配置的oh-package.json5中对应配置 和 <project_root>/oh-package.json5中对应配置。
3、<target_path>/moduleName/oh-package.json5的优先级高于overrideDependencyMap中的依赖配置文件。
4、overrides中的依赖版本优先级高于<target_path>/moduleName/oh-package.json5中对应的依赖版本。
仅当<target_path>/dependencyMap.json5中targetName的值不为空且不等于'default'时，<project_root>/moduleName目录下生成的lock文件名才会变更为：oh-package-targetName-lock.json5。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-list-V14
爬取时间: 2025-04-30 23:14:33
来源: Huawei Developer
列出已安装的三方库。
命令格式
功能描述
以树形结构列出当前项目安装的所有三方库信息，以及它们的依赖关系。
当指定三方库名称时，会列出指定三方库名称的所有父依赖；当未指定三方库名称时，默认只列出所有的直接依赖，可通过添加选项 depth 来指定要打印的依赖层级。
Options
depth
可以在 list 命令后面配置 -d <number> 或者  --depth <number> 参数，设置输出树形结构的最大深度，超过该深度则不进行输出，不配置则取默认值 0，只展示直接依赖。
json
可以在 list 命令后面配置 -j 或者 --json 参数，以  json 格式输出当前项目安装的所有三方库信息，以及它们的依赖关系。
prefix
可以在 list 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
parameterFile
可以在 list 命令后面配置 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。
示例
-  查看当前项目安装的所有三方库及依赖关系。 执行以下命令： 结果示例：
-  查看当前项目安装的某个三方库的依赖关系 执行以下命令： 结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150808.17498791349849375810520169759787:50001231000000:2800:00E545CAEC231DEFB5DFD94D51B7F9F771B9CFEC9084825FE647307A606B6C78.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.96651776874177988648296590898673:50001231000000:2800:93C8ECCC6BD0DEE0BCE7774CE590A17B27E73DD1906C3CBFA1005A6FFC3F475F.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-publish-V14
爬取时间: 2025-04-30 23:15:07
来源: Huawei Developer
发布一个三方库。
命令格式
功能描述
发布校验规则
三方库校验规则
1.  README.md文件、LICENSE文件和CHANGELOG.md三个文件在该HAR包发布至OpenHarmony 三方库中心仓时必须包含，且不能为空。
开闭源规则
1.  开源 不进行 ArkTS 代码相关编译的，只进行 cpp 代码编译和 OpenHarmony 资源处理，还有模块部分原始配置文件会被打包。其 oh-package.json5 文件中的 "artifactType" 字段值为 original。
2.  闭源 ArkTS 代码会被编译成混淆的 js 和 d.ets 和 d.ts 等声明文件，进行 cpp 代码编译和 OpenHarmony 资源处理，还有模块部分原始配置文件会被打包。其 oh-package.json5 文件中 "artifactType" 属性值为 obfuscation。此时则检查 oh-package.json5 文件中 "types" 属性中定义的声明文件是否带有扩展名 ".d.ts/.d.ets"，且对应路径下存在该文件。若无则进行报错，且不会发布。
Options
publish_id
可以在 publish 命令后面配置 --publish_id <id> 参数，指定发布码。
key_path
可以在 publish 命令后面配置 --key_path <p> 参数，指定ssh私钥路径。
tag
可以在 publish 命令后面配置 -t <tag_name>或者 --tag <tag_name> 参数，给将要发布的三方库打上标签。
publish_registry
可以在 publish 命令后面配置 --publish_registry <r> 参数，指定发布仓库地址。如果未指定，默认从配置中获取发布仓库地址。
fetch_timeout
可以在 publish 命令后面配置 -ft <number>或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 publish 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
示例
发布工作目录下的三方库，执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.11852493312724699943850966142669:50001231000000:2800:FBF72AB36F5C304B8A8298F02DB91B174AE6B1040A5EF3A91E3D7A2279A57339.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-uninstall-V14
爬取时间: 2025-04-30 23:15:41
来源: Huawei Developer
卸载三方库。
命令格式
功能描述
卸载指定已安装的模块，并将 oh-package.json5 文件中 dependencies、devDependencies 属性里移除指定三方库信息；若没有指定三方库，则不做任何动作。
如无需在 oh-package.json5 文件中 dependencies、devDependencies 属性里移除指定三方库信息，则可配置 --no-save 参数。
Options
all
您可以在 uninstall 命令后面配置 --all 参数，表示卸载当前模块指定依赖成功后同时安装当前工程下的所有模块的依赖。
no-save
您可以在 uninstall 命令后面配置 --no-save 参数，卸载的三方库信息不会从 oh-package.json5 文件中删除。
prefix
可以在 uninstall 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
registry
可以在 uninstall 命令后面配置 --registry <registry> 参数，当检测到oh-package.json5文件存在未安装的三方包时，卸载命令执行后，会自动从registry指定的仓库中下载并安装该三方包；如果没有指定，默认从配置中获取仓库地址。
fetch_timeout
可以在 uninstall 命令后面配置 -ft <number> 或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 uninstall 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
experimental-concurrently-safe
可以在 uninstall 命令后面配置 --experimental-concurrently-safe 参数，并发安全地安装依赖。这是一个实验性选项。
示例
从当前工程下卸载直接依赖的某个package。
执行以下命令：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-prepublish-V14
爬取时间: 2025-04-30 23:16:15
来源: Huawei Developer
预发布一个三方库。
命令格式
功能描述
Options
无。
示例
预发布工作目录下的三方库，执行以下命令：
结果示例：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-unpublish-V14
爬取时间: 2025-04-30 23:16:49
来源: Huawei Developer
下架已发布的三方库。
命令格式
功能描述
Options
force
强制下架。
publish_registry
可以在 unpublish 命令后面配置 --publish_registry <r> 参数，指定发布仓库地址。如果未指定，默认从配置中获取发布仓库地址。
publish_id
可以在 unpublish 命令后面配置 --publish_id <id> 参数，指定发布码。
key_path
可以在 unpublish 命令后面配置 --key_path <p> 参数，指定ssh私钥路径。
fetch_timeout
可以在 install 命令后面配置 -ft, --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 unpublish 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
示例
下架已发布的三方库，执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.75761013005635923839173109285802:50001231000000:2800:74F57E8B218A19A02B8F5D1AAFCBED462689D42C2034743E45F1D7660D7AFD6F.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-update-V14
爬取时间: 2025-04-30 23:17:23
来源: Huawei Developer
更新三方库。
命令格式
功能描述
根据三方库及其依赖版本号的semver规范，将本地安装的三方库更新到最新版本。若未指定三方库名称，则全量更新当前工程的依赖，且会安装缺少的三方库。
Options
all
您可以在 update 命令后面配置 --all 参数，表示更新当前模块指定依赖成功后同时安装当前工程下的所有模块的依赖。
prefix
可以在 update 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
fetch_timeout
可以在 update 命令后面配置 -ft <number>或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为 60000 ms。
max_concurrent
可以在 update 命令后面配置 -mc <number> 或者 --max_concurrent <number> 参数，设置最大活动并发请求数（即 ohpm 操作期间任何时间的最大网络请求数），如果没有指定，默认最大并发请求数为 50 次。
retry_times
可以在 update 命令后面配置 -rt <number> 或者 --retry_times <number> 参数，设置操作失败前的最大重试次数，如果没有指定，默认最大重试次数为 1 次。
retry_interval
可以在 update 命令后面配置 -ri <number> 或者 --retry_interval <number> 参数，设置重试失败前的等待时间，如果没有指定，默认等待时间为 1000 ms。
strict_ssl
可以在 update 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
registry
可以在 update 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
all-modules
可以在 update 命令后面配置 --all-modules 参数，表示同步更新所有模块的依赖关系。
tag-filter
可以在 update 命令后面配置 --tag-filter <regex> 参数，表示更新以tag为规范，只更新tag符合正则表达式的依赖。使用 --tag-filter 参数默认更新所有模块的依赖关系。
experimental-concurrently-safe
可以在 update 命令后面配置 --experimental-concurrently-safe 参数，并发安全地安装依赖。这是一个实验性选项。
示例
若当前三方库是 APP，且它的依赖项为：dep1 ( dep2, ...)，dep1 已发布的版本有：
^ 依赖项
使用^符号会更新到版本 x.y.z 中 y 和 z 的最新版本。如果 APP 中 oh-package.json5 文件中 dep1 的版本号为：
ohpm update 则安装 dep1@1.2.2，因为最新版本指向 1.2.2，且1.2.2 满足 ^1.1.1。
~ 依赖项
使用~符号会更新到版本 x.y.z 中 z 的最新版本。如果 APP 中 oh-package.json5 文件中 dep1 的版本号为：
ohpm update 则安装 dep1@1.1.2，尽管最新版本指向 1.2.2，但 1.2.2 不满足 ~1.1.1（版本号须 1.1.1 ≤ version < 1.2.0），所以 ~1.1.1 使用满足最高排序版本，即1.1.2 ，进行更新。
tag 依赖项
使用 tag 会更新到 tag 对应的版本。如果 APP 中 oh-package.json5 文件中 dep1 的版本号为：
如果此时 release 标签对应版本被变更为 1.2.2，ohpm update --tag-filter ^r 则会将 dep1@1.2.0 更新为 dep1@1.2.2，因为 dep1 是通过 release 标签引入，release 符合 --tag-filter 指定的 ^r 正则表达式，所以会重新获取 release 标签对应的版本 1.2.2。
低于 1.0.0 版本的 ^ 依赖项
-  如果 APP 中 dep1 依赖版本号低于 1.0.0 且带有 ^，例如： ohpm update 则安装 dep1@0.2.0，因为没有其他版本满足 ^0.2.0。
-  但是 dep1 依赖版本号是 ^0.4.0： ohpm update 则安装  dep1@0.4.1，因为它是满足 ^0.4.0（版本号须 0.4.0 ≤ version < 0.5.0）的最高排序版本。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-root-V14
爬取时间: 2025-04-30 23:17:57
来源: Huawei Developer
在标准输出中打印有效的 oh_modules 目录路径信息。
命令格式
功能描述
可以在模块的任意子目录下执行，用于打印命令工作路径下所在包的有效 oh_modules 目录路径信息。
Options
prefix
可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh_modules 目录路径信息。
示例
项目结构为：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.01446337137642905558116097574776:50001231000000:2800:13ED0007D0C2B8E61E349917D55A570D6C0ADE2A208278926C66EB4F3C836A32.png?needInitFileName=true?needInitFileName=true)
在entry模块的src目录下执行：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.76939989076239814079939480149988:50001231000000:2800:A115C1028843AF7AA4546DF38BB2295F9620B5E50D13BE58EAE0F0532C19262B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-version-V14
爬取时间: 2025-04-30 23:18:30
来源: Huawei Developer
管理模块版本。
命令格式
功能描述
在模块目录中运行此命令以获取或升级版本号，同时将数据回写入 oh-package.json5 中。
参数说明
无参数
当无参数使用ohpm version命令时，则会将当前模块的版本号打印至标准输出中。
newversion
newversion 参数应为一个合法的语义化版本，命令会将当前模块版本改写为 newversion 并打印在标准输出中。
major
当参数为 major 时，有以下几种情况：
minor
当参数为 minor 时，固定主版本号，变化次版本号与修订号，有以下几种情况：
patch
当参数为 patch 时，固定主版本号与次版本号，变化修订号，有以下几种情况：
Options
prefix
可以在 version 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。
parameterFile
可以在 version 命令后面配置 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。
示例
当前模块为 entry，版本号为 1.0.0，在当前模块的根目录执行：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.09034240218797443201744881702965:50001231000000:2800:C38E2D84120A5B72E3169D59410E852A3061384E8003E7CDAC6FF3D2D1D10BB5.png?needInitFileName=true?needInitFileName=true)
接着执行：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150809.99792597285301364272028544892374:50001231000000:2800:849B9F4BFA031071EC6C392B4A60C97DFB35133CA1D867C9B865BDB7D95601DE.png?needInitFileName=true?needInitFileName=true)
接着执行：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.47742872004811374754938129569281:50001231000000:2800:614B7B0C8A5B9C88819222C1DEBB30E140C99CD4E74A7E321E3642244F1BF8A9.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-cache-V14
爬取时间: 2025-04-30 23:19:04
来源: Huawei Developer
清理 ohpm 缓存文件夹。
命令格式
功能描述
用于清理 ohpm 缓存文件夹。
关于缓存设计的说明
ohpm 将缓存数据存储在配置的 cache 目录下名为 content-v1 的文件夹中，存储所有通过 http 请求获取的 har 包数据。包的路径使用包的 sha512 哈希值分割成 3 端，第 1、2 位作为第一级目录，哈希值第 3、4 位作为第二级目录，哈希值第 5 位到结尾的所有字符作为文件名。使用哈希值可以将文件较均匀地分布在各个目录下，分成 3 层目录结构避免一个目录下文件数量过多，可以提升文件索引效率。
配置
缓存的配置方式见ohpmrc。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-run-V14
爬取时间: 2025-04-30 23:19:38
来源: Huawei Developer
执行用户自定义脚本。
命令格式
功能描述
-  scripts对象内部支持"key":"value"方式配置多个待执行脚本。如以下示例所示，scriptName 1、scriptName 2、scriptName 3为脚本别名（scriptName）；“echo hello”等为（scriptContent），后续内容均参考此说明。
传递参数
-  该示例表明，脚本scriptName 3的参数paramKey1会被替换为newValue, 并新增一个参数paramKey4。
支持多命令
支持 && 和 || 两种命令连接符 （&& 和 || 没有优先级区分，命令从左到右执行，不支持用括号来改变各个子命令的优先级）。
约束
| 约束项  | 说明  |
| --- | --- |
| scriptKey 命名约束  | 合法的 scriptKey 的名字可以包含字母（包含大小写），数字，ASCII 冒号 :，ASCII下划线 _ ，ASCII链接符 -，首字母必须是小写字母  |
| scriptContent 约束  | 合法的scriptContent不能引用除ohpm run以外的其它ohpm命令  |
| scriptContent 中使用 ohpm run 的约束  | 1、ohpm run 依赖的其它script别名必须在同一 oh-package.json5 中存在 2、ohpm run 引用关系是一个有向无环图，不支持递归或循环引用  |
约束项
说明
scriptKey 命名约束
合法的 scriptKey 的名字可以包含字母（包含大小写），数字，ASCII 冒号 :，ASCII下划线 _ ，ASCII链接符 -，首字母必须是小写字母
scriptContent 约束
合法的scriptContent不能引用除ohpm run以外的其它ohpm命令
scriptContent 中使用 ohpm run 的约束
1、ohpm run 依赖的其它script别名必须在同一 oh-package.json5 中存在
2、ohpm run 引用关系是一个有向无环图，不支持递归或循环引用
Options
prefix
可以通过 --prefix 指定包的根目录，该目录下必须存在 oh-package.json5 文件。不支持通过这种方式调用依赖包中的脚本别名。
示例
参数传递的使用示例
运行 script_name 的脚本，并指定脚本中参数agr1，agr2，agr3，agr4，取值分别为1，2，3，4，以上四种参数传递的方法均可生效。
oh-package.json5配置如下：
成功示例
执行脚本testSuc，如下所示：
执行结果：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.76044058976408207599548374513938:50001231000000:2800:4B069031E77D6BC2AA21A15DC01B35E3F45A49AF9DD956BE517331E31A749226.png?needInitFileName=true?needInitFileName=true)
失败示例
执行脚本testFail，如下所示：
执行结果：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.11092927674099199748932681857556:50001231000000:2800:DA249778E5430F84CECFF6122E71DA15900C8BDB141FBD9C719BEB192E6A2C10.png?needInitFileName=true?needInitFileName=true)
逻辑符(&&、||)使用示例
执行脚本testLogic，如下所示：
执行结果：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.62007914077619583798443087055848:50001231000000:2800:D754B7DDD272E3D62709D129B9CEE3F6E219C36A816D8EAB8EEA793AFC60B154.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm--version-V14
爬取时间: 2025-04-30 23:20:12
来源: Huawei Developer
查询 ohpm cli 安装版本。
命令格式
功能描述
示例
查询 ohpm cli 安装版本，可执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.90745396782137369475186724523823:50001231000000:2800:C68E5D5E7EFF64F07C804D0A4B5815EC5ABE6DDE3F8CA65F0DBF211282A762C0.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-ping-V14
爬取时间: 2025-04-30 23:20:47
来源: Huawei Developer
ping ohpm 仓库地址。
命令格式
功能描述
对给定的或者是配置中的仓库地址进行身份验证。如果有效，将会输出相关信息，比如以下内容：
否则将会输出错误信息，比如以下内容：
Options
registry
可以在 ping 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
fetch_timeout
可以在 ping 命令后面配置 -ft <number> 或者 --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为 60000 ms。
strict_ssl
可以在 ping 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-clean-V14
爬取时间: 2025-04-30 23:21:21
来源: Huawei Developer
清理工程下所有模块的ohpm安装产物。
命令格式
功能描述
清理工程下所有模块的oh_modules目录、oh-package-lock.json5文件和oh-package-targetName-lock.json5文件(指定选项--target_path安装时生成)，清理完成后会在控制台打印耗时信息。
Options
keep-lockfile
可以在 clean 命令后面配置-kl或者--keep-lockfile参数，执行清理时会保留oh-package-lock.json5文件和oh-package-targetName-lock.json5文件(指定选项--target_path安装时生成)。
注意事项
示例

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-dist-tags-V14
爬取时间: 2025-04-30 23:21:56
来源: Huawei Developer
tag可标记一个三方库的某个版本，在install时可用tag代替版本号安装包。
命令格式
功能描述
操作tag。分为查看三方库的所有tag，给三方库的某个版本添加tag，修改tag到三方库的另一个版本，删除三方库的某个tag。
"latest"是一个预设的标签，不允许直接通过dist-tags命令来进行修改。该标签自动指向最高的正式版本；若无正式版本，则默认指向最高的先行版本。
以第三方库a为例，假定其版本序列包括"1.0.1-beta"、"1.0.1"和"2.0.1-beta"，在这种情况下，"latest"会自动映射到"1.0.1"，因为它是当前最高的正式版本。
子命令
list
列出指定三方库的所有标签。输出结果中，`latest`标签始终位于首位，其他标签按照字典序排列显示。
add
给某个版本的三方库增加一个标签。若该三方库已存在相同标签，则添加操作将会失败。
update
更新指定包的某个标签所对应的版本。如果指定的标签不存在，则更新操作将失败。
remove
删除指定包的一个标签。如果该标签并未存在于包中，则删除操作将会失败。
Options
publish_id
可以在 publish 命令后面配置 --publish_id <id> 参数，指定发布码。
key_path
可以在 publish 命令后面配置 --key_path <p> 参数，指定ssh私钥路径。
registry
可以在 install 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。
publish_registry
可以在 publish 命令后面配置 --publish_registry <r> 参数，指定发布仓库地址。如果未指定，默认从配置中获取发布仓库地址。
fetch_timeout
可以在 publish 命令后面配置 -ft <number>或者  --fetch_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。
strict_ssl
可以在 publish 命令后面配置 --strict_ssl true 参数，校验 https 证书；配置 --strict_ssl false 参数，不校验 https 证书。
示例
如果想要通过使用tag，在oh-package.json5文件中引入包@ohos/axios的1.0.0版本，步骤如下：
1.  通过ohpm dist-tag的子命令add，对包@ohos/axios的1.0.0版本添加标签名beta。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-convert-V14
爬取时间: 2025-04-30 23:22:30
来源: Huawei Developer
将npm格式三方库转换为ohpm三方库。
命令格式
功能描述
将指定ohpm或npm仓库中的某个包或者本地node_modules目录下的包转换成满足ohpm格式要求的HAR包，并保存至当前工作目录，转换后的包将支持上传至ohpm-repo私仓或OpenHarmony三方库中心仓。
-  ohpm convert @group/pkg@version --registry <ohpm/npm仓库地址> 下载指定仓库中的某个包及其所有依赖项，并且将该包及其依赖转换为满足ohpm格式要求的HAR包。
-  ohpm convert <node_modules_path> 转换本地node_modules中的所有包为为满足ohpm格式要求的HAR包，<node_modules_path>必须为npm执行install命令后生成的node_modules目录。 示例：
ohpm convert命令仅保留package.json或oh-package.json5中的name、version、main、types、license、description、author、keywords、homepage、repository、artifactType、dependencies、devDependencies、dynamicDependencies、overrides、scripts、hooks字段，具体字段说明请参考oh-package.json5 字段说明。
Options
registry
可以在convert命令后面配置 --registry <registry> 参数，指定仓库地址。如果指定了--registry，convert命令将从远程仓库地址下载指定的包及其依赖后，进行转换处理。如果没有指定--registry，convert命令将从本地node_modules目录进行转换处理。
publish
可以在 convert命令后面配置 --publish 参数 ，若指定该参数，执行convert命令前请确认.ohpmrc推包相关配置无误，当所有包转换完成后将根据.ohpmrc中的配置依次进行推包。
示例
转换远程npm三方库中的包
转换npm三方库中的axios包，执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.38640117491151816761021954511540:50001231000000:2800:0C251AADA5AC6520E83A32D7C9E92C86CDC4967B59739C3AC517B08268F431DC.png?needInitFileName=true?needInitFileName=true)
转换本地node_modules目录中的包
执行npm install uuid后，转换本地node_modules目录中的包，执行以下命令：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.05377081723929883704150293051915:50001231000000:2800:B2C720D9ED2852C7337DDA0FE8A87B6FAA4674FBFF12FE650272ACC215E9B7A5.png?needInitFileName=true?needInitFileName=true)
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150810.08725511591312341950012140086986:50001231000000:2800:41E0F522CD0FB1CA7241C6DC6F91C3087B59FAA2B59BAEE021CF88B856C568BA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-command-line-building-app-V14
爬取时间: 2025-04-30 23:23:06
来源: Huawei Developer
除了使用DevEco Studio一键式构建应用/元服务外，还可以使用命令行工具来调用Hvigor任务进行构建。通过命令行的方式构建应用或元服务，可用于构筑CI（Continuous Integration）流水线，按照计划时间自动化的构建HAP/APP、签名、安装运行等操作。
通过命令行方式构建应用或元服务，可在Windows、Linux和macOS下调用相应命令来执行，本文将以Linux系统为例进行讲解，包括准备构建环境、构建HAP、签名运行等操作。在调用命令行任务上，Windows/macOS系统与Linux系统没有区别，仅在搭建构建环境上存在差异。
系统平台要求
-  Linux：64位操作系统
-  GLIBC：2.28或更高版本
-  内存：推荐使用16GB及以上，最小8GB
-  硬盘：100GB及以上
预置条件
配置JDK
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181219.89018995808535325848454576132649:50001231000000:2800:697781506E123844197F2FA42A8D0C3E282B1E267FC71CB15CB489DFE131CC6A.png)
获取命令行工具
1.  将解压后所在的路径定义为COMMANDLINE_TOOL_DIR，在后续配置hdc、hvigor、ohpm工具环境变量时使用。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181219.11272882155636313643827633567038:50001231000000:2800:0167020A6030381B2D48AC2C680AC77C70C1D34A84AD70C96CC3A479F4E723FF.png)
配置hdc环境变量
hdc命令行工具用于HarmonyOS应用/元服务调试所需的工具，该工具存放在命令行工具自带的sdk下的toolchains目录中。为方便使用hdc命令行工具，请将其添加到环境变量中。
1.
配置hvigor环境变量
1.
2.
配置npm镜像仓库
若您的工程在hvigor/hvigor-config.json5文件中依赖npm三方组件，流水线中则需要配置npm镜像地址，编译时才能正确地下载它。
安装ohpm
1.
2.
3.
安装libGL1库
在linux系统的构建场景下，使用纹理压缩功能需要安装libGL1库。
1.
构建应用
安装工程及模块依赖
使用命令行进行构建前，需要分别进入工程及各个模块下执行ohpm install命令，安装工程及各个模块依赖的三方库。
1.
2.
3.
执行Hvigor命令进行构建
1.
补充说明：
| 选项 | 说明 |
| --- | --- |
| -p buildMode={debug | release} | 采用debug/release模式进行编译构建。 缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。 关于构建模式的详细说明，请参考指定构建模式。针对HAR构建，请参考构建HAR。 |
| -p product={ProductName} | 指定product进行编译, 编译product下配置的module target。 缺省时：默认为default。 |
| -p module={ModuleName}@{TargetName} | 指定模块及target进行编译，可指定多个相同类型的模块进行编译以逗号分割；TargetName不指定时默认为default。 限制：此参数需要与--mode module参数搭配使用。 缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。 |
| -p ohos-test-coverage={true | false} | 执行测试框架代码覆盖率插桩编译。 |
选项
说明
-p buildMode={debug | release}
采用debug/release模式进行编译构建。
缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。
关于构建模式的详细说明，请参考指定构建模式。针对HAR构建，请参考构建HAR。
-p product={ProductName}
指定product进行编译, 编译product下配置的module target。
缺省时：默认为default。
-p module={ModuleName}@{TargetName}
指定模块及target进行编译，可指定多个相同类型的模块进行编译以逗号分割；TargetName不指定时默认为default。
限制：此参数需要与--mode module参数搭配使用。
缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。
-p ohos-test-coverage={true | false}
执行测试框架代码覆盖率插桩编译。
| 选项 | 说明 |
| --- | --- |
| clean | 清理构建产物 |
| assembleHap | 构建Hap应用 |
| assembleApp | 构建App应用 |
| assembleHsp | 构建Hsp包 |
| assembleHar | 构建Har包 |
选项
说明
clean
清理构建产物
assembleHap
构建Hap应用
assembleApp
构建App应用
assembleHsp
构建Hsp包
assembleHar
构建Har包
附：Hvigor命令行参数详见：常用命令。
运行应用
准备申请签名所需文件
准备好申请签名所需3个文件：密钥（.p12文件）、数字证书（.cer文件）、Profile（.p7b文件）。
生成密钥和证书请求文件
使用Open JDK携带的Keytool工具生成密钥和证书请求文件。
1.
2.  生成公私钥文件的参数说明如下：
3.  生成证书请求文件的参数说明如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314181219.04152614590494830519846416326260:50001231000000:2800:9EBAC0992DFB0F324C21B878D308E5A6F25490E25F80EA4CAADD671521B4456B.png)
申请调试数字证书和Profile文件
生成证书请求文件后，在AppGallery Connect中申请、下载调试数字证书和Profile文件，具体请参考申请调试证书和Profile文件。
对HAP进行签名
通过Hvigor打包生成的HAP不会携带签名信息，如果要在真机设备上运行HAP，需要使用命令行工具对HAP进行签名。
1.  关于该命令中需要修改的参数说明如下，其余参数不需要修改：
运行应用
通过HDC工具将HAP推送到真机设备上进行安装，需要注意的是，推送的HAP必须是携带签名信息的，否则会导致HAP安装失败。
在设备上运行HAP的命令如下：
示例脚本

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-V14
爬取时间: 2025-04-30 23:23:41
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-overview-V14
爬取时间: 2025-04-30 23:24:15
来源: Huawei Developer
ohpm-repo 是一个搭建轻量级的ohpm私仓服务的工具。它与 ohpm 包管理器兼容，并按需缓存所有依赖项，加速私有网络中的安装。
私有性
所发的三方库都是私有的，只能根据配置进行访问。
缓存
ohpm-repo 根据需要缓存所有依赖项，加快私有网络的安装速度。
部署
ohpm-repo 支持单点部署和多实例部署。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-quickstart-V14
爬取时间: 2025-04-30 23:24:50
来源: Huawei Developer
ohpm-repo 私仓不允许使用 root 用户启动，请使用其他用户安装运行。
如何安装
ohpm-repo
1.  ohpm-repo 依赖于 node 运行，支持 node.js 18.x 及以上版本，请提前安装 nodejs，并完成环境变量的配置。Node.js安装请参考Node.js官方网站。
2.  下载 ohpm-repo 私仓工具包。请在下载中心获取最新的ohpm-repo，并根据下载中心页面工具完整性指导进行完整性校验。
3.  解压 ohpm-repo 私仓工具包。
4.  请将ohpm-repo工具包解压目录中bin目录的路径配置到系统环境变量path中，执行如下查询命令: 针对Linux和Mac系统，建议使用bash或zsh作为命令行界面。如果使用其他类型shell，写入ohpm-repo部署根目录deploy_root的环境变量时，默认写入.bashrc文件中。
5.  在启动 ohpm-repo 前还需要先按照如下方式完成配置修改： 进入 ohpm-repo 解压目录的 conf 目录内，打开 config.yaml配置文件。 ohpm-repo成功启动后修改配置文件方法：
6.  检查listen配置，默认配置为 localhost:8088 ，表示仅支持监听本机地址；如果希望其他机器通过ip/域名访问，则建议修改 listen 配置为ohpm-repo部署机器的ip：
7.  db：元数据存储 与db所适配的store类型 fileDB local storage mysql local storage，sftp storage， custom storage
8.  检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址、不配置取默认值，详情见：server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改 host 为本机指定的 ip/域名，例如 listen 为 0.0.0.0:8088，故 server 需配置为 http://<指定部署机器的ip/域名>:8088。
9.  进入ohpm-repo工具包解压目录中的 bin 目录下，执行安装命令: 结果实例：
10.  安装成功后，必须根据给出的提示信息刷新部署目录的环境变量，针对 Window 系统和 Linux/Mac 系统，有不同处理方式：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150811.55657358600451276267908325276729:50001231000000:2800:D97556A3F9CE4DB3FCEBAD3A6507731E17EAC52EC9B1E400C31727712EFC7CA8.png?needInitFileName=true?needInitFileName=true)
| db：元数据存储 | 与db所适配的store类型 |
| --- | --- |
| fileDB | local storage |
| mysql | local storage，sftp storage， custom storage |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150811.38715909936382264300722678251703:50001231000000:2800:82BB2C2D227CBC9553E13EE80A3C24007D8D3FFF498698C919868FA62AFB74E2.png?needInitFileName=true?needInitFileName=true)
如何启动
ohpm-repo安装成功后，进入ohpm-repo工具包解压目录下的 bin 目录下，执行如下命令，启动 ohpm-repo：
启动成功，将会出现以下日志信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150811.35876256792818463576972792853253:50001231000000:2800:4C9EDADFB1C12EE7BE2ACBA85B1B555BCE59E7B6E26F201959DC31DB34F1C558.png?needInitFileName=true?needInitFileName=true)
ohpm-repo 首次启动时，默认创建一个管理员账号，账号名称：admin，密码：12345Qq!。该账号在首次登录时，需要修改其密码，请修改密码后，重新登录该账号。
从ohpm-repo获取三方库
可以为所有项目配置该私有仓，例如执行以下命令：
或者在命令行中配置参数 --registry 使用，例如以下命令：
<配置的ohpm-repo私仓服务地址>：配置文件中store.config.server的地址信息，例如：store.config.server:为 http://127.0.0.1:8088，故 registry 为：http://127.0.0.1:8088/repos/ohpm。如果store.config.server没有配置，取默认值。
将三方库发布到 ohpm-repo
三方库包含静态共享包 HAR 包和动态共享包 HSP 包，可以通过 ohpm 命令行工具和使用 Web 页面两种方式发布。
从 ohpm 命令行工具 1.3.0 版本和 ohpm-repo 私仓 1.1.0 版本开始，支持动态共享包 HSP 包以 .tgz 文件形式发布到ohpm-repo，之前版本仅支持发布以 .har 文件形式的静态共享包 。
使用命令行工具发布
1.  示例： 公钥和私钥存储在 D 盘 的 path 目录下，公钥和私钥名称分别为 my_key_path.pub 和 my_key_path。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.08283196862511016369967631381573:50001231000000:2800:2CAEE31FE5A92F36865F6F96909CCAFA5FE7BADB3CBDD1087147DED0097DCB3A.png?needInitFileName=true?needInitFileName=true)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.39940863219749724972664767925170:50001231000000:2800:79E1F263AFBF1F9D8F9789F469A44E26BFB1DE368D00B41DE799DD78B62A841A.png?needInitFileName=true?needInitFileName=true)
1.  执行 ''ohpm publish <HAR包路径>'' 命令发布 HAR包，<HAR包路径> 指向的文件后缀需为 .har 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令： 动态共享包 HSP 包不能直接发布在ohpm-repo内，需要先转化为 .tgz 包，转换方法见：编译HSP模块。TGZ 包的发布流程同 HAR 一致。 执行 ''ohpm publish <TGZ 包路径>'' 命令发布 TGZ 包，< TGZ 包路径> 指向的文件后缀需为 .tgz 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
2.  执行 ''ohpm publish <HAR包路径>'' 命令发布 HAR包，<HAR包路径> 指向的文件后缀需为 .har 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
3.  动态共享包 HSP 包不能直接发布在ohpm-repo内，需要先转化为 .tgz 包，转换方法见：编译HSP模块。TGZ 包的发布流程同 HAR 一致。 执行 ''ohpm publish <TGZ 包路径>'' 命令发布 TGZ 包，< TGZ 包路径> 指向的文件后缀需为 .tgz 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
-  执行 ''ohpm publish <HAR包路径>'' 命令发布 HAR包，<HAR包路径> 指向的文件后缀需为 .har 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
-  动态共享包 HSP 包不能直接发布在ohpm-repo内，需要先转化为 .tgz 包，转换方法见：编译HSP模块。TGZ 包的发布流程同 HAR 一致。 执行 ''ohpm publish <TGZ 包路径>'' 命令发布 TGZ 包，< TGZ 包路径> 指向的文件后缀需为 .tgz 文件的具体路径。例如执行以下命令： 或在命令行中配置参数 --publish_registry 使用，例如以下命令：
使用Web页面发布
在Web页面用管理员账号登录ohpm-repo私仓管理地址，在个人中心 > 仓库管理中，点击管理三方包 > 上传三方包，包的后缀名必须为 .har 或者 .tgz。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.25013711224826400270334726356967:50001231000000:2800:447C844FE758124E1A9C765701579C35CB8CF213AB248E3D5EDD3BED5DFF4691.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.95046083672915742685713820212954:50001231000000:2800:D184E4E368504DF6A56B9D8DDA16320DEBDB0DD27D0F464E4B04141259BFDE0C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-configuration-V14
爬取时间: 2025-04-30 23:25:24
来源: Huawei Developer
config.yaml 是 ohpm-repo 的重要文件，可以在其中修改默认参数配置，启动插件和扩展功能。ohpm-repo 私仓解压目录中的 conf 目录下带有一个默认配置文件 config.yaml，ohpm-repo 执行 install 命令时默认读取该文件。
ohpm-repo成功启动后修改配置文件方法：
默认配置
配置项说明
listen
格式为三段式，即 <proto>://<host>:<port>，其中 <proto> 可以不填，默认为 http，如：
-  监听本机回环地址（默认）：
-  监听具体地址（建议）：
-  监听所有地址（当选择监听所有地址时，配置项store中 server 值必须配置）：
listen值建议监听具体的地址。proto 支持 http 和 https 协议，支持缺省，缺省时默认为 http。为了确保ohpm-repo链接的安全，建议选择使用 https 协议，如果配置为 https 协议，则需要完善https相关配置。
https
当配置listen时选择使用 https 协议，则需要配置 https_key 和 https_cert：
为了确保ohpm-repo链接的安全，建议选择使用 https 协议，可以使用如下命令，在当前命令行所在目录生成 https 协议使用的证书私钥文件和证书文件（需要提前安装安全套接字层密码库Openssl）：
参考配置如下：
deploy_root
ohpm-repo的部署目录，存储运行时生成的文件数据。
-  如果 <deploy_root> 字段为空，则默认路径为： windows系统: ~/AppData/Roaming/Huawei/ohpm-repo 其他操作系统：~/ohpm-repo
-  如果<deploy_root>字段不为空，则路径必须为绝对路径，且路径所指向文件夹必须存在。
参考配置如下：
server
服务相关配置，具体为：
参考配置如下：
db是元数据存储的配置项，store是文件存储的配置项。db支持fileDB本地存储和mysql数据库存储；store支持file storage存储，sftp存储和custom storage 自定义插件存储。db和store不能随意搭配，需要符合表1的匹配规范：
| db：元数据存储  | 与db所适配的store：三方包文件存储  |
| --- | --- |
| filedb  | file storage  |
| mysql(ohpm-repo 1.1.0开始支持）  | file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持）  |
db：元数据存储
与db所适配的store：三方包文件存储
filedb
file storage
mysql(ohpm-repo 1.1.0开始支持）
file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持）
db
ohpm-repo运行过程产生的用户信息，运行状态等元数据存储配置，支持本地磁盘存储filedb和 mysql 数据库存储。
本地磁盘存储
默认使用本地磁盘存储，配置如下：
如果想修改数据库文件存储路径同时保留旧的数据，则需要把旧路径下的数据文件迁移至新路径。
参考配置如下：
Mysql存储
参考配置如下：
为了避免潜在的安全风险，建议使用非最高权限的数据库账户进行连接。
store
三方库及其元数据等资源文件存储配置，支持本地磁盘存储，sftp存储和自定义插件存储。
本地磁盘存储
默认使用本地磁盘存储文件，具体配置为：
上传资源后如若要修改存储路径，则需要把旧路径下的数据迁移至新路径中。
参考配置如下：
sftp 存储
支持使用 sftp 存储文件，仅当数据存储为 mysql 存储时才能使用 sftp 存储，具体配置为：
参考配置如下：
custom存储
使用自定义插件存储，具体配置为：
参考配置如下：
use_reverse_proxy
当use_reverse_proxy配置为true时，必须在反向代理配置时刷新x-forwarded-for值（如果存在多级代理，只需要在最外层代理配置刷新），如果不刷新将存在x-forwarded-for数据被篡改风险，反向代理配置刷新x-forwarded-for命令如下：
uplink
参考配置如下：
logs
参考配置如下：
loglevel
loglevel 自定义配置，具体配置为：
参考配置如下：
auth_plugin
ohpm-repo 从 2.3.0 版本开始支持自定义认证插件（需配套使用1.8.0及以上版本ohpm命令行工具），允许您开发定制化的认证插件来对接您自己的用户信息系统。自定义认证插件开发流程见认证插件说明文档。
参数说明：
参考配置如下：
compability_log_level
allow_remove_depended_packages
allow_new_file_upload_api
关于 deploy_root
deploy_root 为ohpm-repo的部署目录，通过配置文件中字段 <deploy_root> 可进行配置。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-log-V14
爬取时间: 2025-04-30 23:25:58
来源: Huawei Developer
与任何 web 应用程序相同，ohpm-repo 有一个内置的日志记录器，其定义了四种日志类型。
访问日志 - access.log
访问日志中主要包含操作时间、服务器 ip、操作源、操作结果以及请求接口或者请求静态资源，其文件保存个数最多为 180 个。
操作日志 - operate.log
操作日志中主要包含操作时间、日志级别、操作人id(userId)、终端 ip(ip)、操作资源（resource）、操作方法名（event）以及操作结果（result），其文件保存个数最多为 180 个。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150812.35623342065282818817212976935957:50001231000000:2800:783D80FD9520F23D1AEBCA242594DA6BC16F9AA531741D5807D16AD93D2C0E15.png?needInitFileName=true?needInitFileName=true)
操作方法名(event)： 当在ohpm-repo管理界面执行一些列操作时，会在operate.log文件生成一条条操作数据，操作方法名即表示当前操作涉及到的方法名字，例如login即表示登录操作，analyzePackage即表示上传包时对包的解析操作。
| 序号  | Event描述  | 说明  |
| --- | --- | --- |
| 1  | generateAccessToken / deleteAccessToken  | 生成 / 删除AccessToken  |
| 2  | login / logout  | 登入 / 登出  |
| 3  | publish / unPublish  | 上架 / 下载资源包  |
| 4  | addGroup / deleteGroup  | 添加/删除组织  |
| 5  | updateGroup  | 更新组织  |
| 6  | addMember/deleteMember  | 添加 / 删除组织成员  |
| 7  | addAdminMember/deleteAdminMember  | 添加/删除组织管理员  |
| 8  | addPublicKey / delPublicKeyByld  | 添加 / 删除发布公钥  |
| 9  | updateRepo  | 更新仓库  |
| 10  | analyzePackage  | 解析上传的包文件  |
| 11  | uploadPackage  | 上传包文件  |
| 12  | getPackageSizeLimit  | 获取包的大小限制  |
| 13  | addUplink / deleteUplink  | 添加 / 删除uplink  |
| 14  | updateUplink  | 更新uplink  |
| 15  | updateUplinkProxy  | 更新Uplink代理  |
| 16  | addUser / delUserByUserld  | 添加/删除用户  |
| 17  | changePassWord  | 改变用户账户密码  |
| 18  | resetPassWord  | 重置用户账户密码  |
| 19  | changeRole  | 修改用户角色(管理员和非管理员)  |
| 20  | register  | 注册账户  |
| 21  | resetKey  | 重置系统秘钥  |
序号
Event描述
说明
1
generateAccessToken / deleteAccessToken
生成 / 删除AccessToken
2
login / logout
登入 / 登出
3
publish / unPublish
上架 / 下载资源包
4
addGroup / deleteGroup
添加/删除组织
5
updateGroup
更新组织
6
addMember/deleteMember
添加 / 删除组织成员
7
addAdminMember/deleteAdminMember
添加/删除组织管理员
8
addPublicKey / delPublicKeyByld
添加 / 删除发布公钥
9
updateRepo
更新仓库
10
analyzePackage
解析上传的包文件
11
uploadPackage
上传包文件
12
getPackageSizeLimit
获取包的大小限制
13
addUplink / deleteUplink
添加 / 删除uplink
14
updateUplink
更新uplink
15
updateUplinkProxy
更新Uplink代理
16
addUser / delUserByUserld
添加/删除用户
17
changePassWord
改变用户账户密码
18
resetPassWord
重置用户账户密码
19
changeRole
修改用户角色(管理员和非管理员)
20
register
注册账户
21
resetKey
重置系统秘钥
运行日志 - run.log
运行日志中主要包含操作时间、日志级别以及日志信息，其文件保存个数最多为 30个。运行日志定义了日志级别：all，trace，debug，info，warn，error，fatal，mark 和 off。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.46126780660082606477138917150484:50001231000000:2800:98F6EC9709F03FFABD838B656735F92C7FED45C309A98E7A8AEC82D008A107F0.png?needInitFileName=true?needInitFileName=true)
运行错误日志 - repoError.log
当ohpm-repo在运行过程中，所有run.log中生成的error日志都会打印到repoError.log中，是error日志的集合，日志打印级别与run.log日志保持一致。
下载错误日志
当从仓库中下载某个包失败时，仓库会生成一条错误日志记录在数据库中的 downloadfailure 表中，当为ohpm-repo配置了 sftp 存储服务时，从任意一个 sftp 服务中下载失败时，都会生成一条错误日志并保存。每条日志都有 handled 标识，handled 为 0 时表示已处理，handled 为 1 时表示未处理。
日志存储路径
日志存储的默认路径为 ./logs，相对路径基准为ohpm-repo部署根目录deploy_root。
日志打印级别
在配置文件中可以设置访问、操作、运行日志的打印级别，日志将会只打印不低于设置级别的日志，日志级别由低到高为：all，trace，debug，info，warn，error，fatal，mark 和 off。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-command-V14
爬取时间: 2025-04-30 23:26:33
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-help-V14
爬取时间: 2025-04-30 23:27:07
来源: Huawei Developer
获取有关 ohpm-repo 的帮助。
命令格式
参数
command：命令名称
功能描述
-  如果提供了命令名称，则显示相应命令的帮助信息。
-  如果提供的命令名称不存在或未提供，则显示所有命令的概要信息。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.32819790041888325732924563132219:50001231000000:2800:46C4FCA150FA000FCEEA3D4D66562FCFCEFCEC0376AACD0E9E7155CDF2FC1A2A.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-install-V14
爬取时间: 2025-04-30 23:27:41
来源: Huawei Developer
安装ohpm-repo服务。
命令格式
功能描述
在启动服务之前做好准备工作，包括：检查ohpm-repo配置文件的合法性和数据库的初始化等。
选项
config
-  默认值："<binary_root>/conf/config.yaml" <binary_root>：ohpm-repo 私仓解压根目录。
-  类型： String
可以在 install 命令后面配置 --config <string> 参数，指定配置文件路径。支持相对路径，以当前命令行工作路径作为根目录。
执行 install 成功后，会在<deploy_root>/conf中生成一个运行时配置文件config.yaml，作为后续命令的配置文件，其中 <deploy_root> 为ohpm-repo部署目录。
skip-db
在install命令后面配置-sd或者--skip-db，指定是否跳过对mysql数据库中数据表的初始化；默认会读取ohpm-repo解压目录中的schema.sql文件，对mysql数据库中的表进行初始化。
在ohpm-repo配置文件config.yaml中，配置项db.type只有为mysql时，此参数才生效。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.94033514246097794578112455933813:50001231000000:2800:913E5733214B7A6BFD6FEE5FB2C7995E69BF23E7859CDBDF5D7DC5CA5EAB6A3A.png?needInitFileName=true?needInitFileName=true)
注意
安装成功后，必须根据给出的提示信息刷新环境变量，针对 Window 系统和 Linux/Mac 系统，有不同处理方式：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-start-V14
爬取时间: 2025-04-30 23:28:15
来源: Huawei Developer
启动ohpm-repo服务。
前提条件
已成功执行install命令，并按要求刷新环境变量。
命令格式
功能描述
用于启动ohpm-repo服务，创建一个ohpm-repo实例。
启动时将ohpm-repo服务的 pid 存放到 <deploy_root>/runtime/.pid 文件中，其中 <deploy_root> 为ohpm-repo私仓部署目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.80691983855939629649038119993993:50001231000000:2800:8BAE4A756CBFF22BDA57C8BB19B7643E8CB87B0CFEABC3C17AF66004A5743C9C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restart-V14
爬取时间: 2025-04-30 23:28:50
来源: Huawei Developer
重新启动ohpm-repo服务。
前提条件
已成功执行install命令，并按要求刷新环境变量。
命令格式
功能描述
停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务.
启动时将ohpm-repo服务的 pid 存放到 <deploy_root>/runtime/.pid 文件，其中 <deploy_root> 为ohpm-repo私仓部署目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.33622078469017877139567911907214:50001231000000:2800:54C3F57A05F84292D5DC2549298A1CA7F432EE27D4AE1305707B658818199112.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-stop-V14
爬取时间: 2025-04-30 23:29:24
来源: Huawei Developer
停止ohpm-repo实例。
命令格式
功能描述
用于停止已经启动的ohpm-repo实例。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.59702217443014725761366102561757:50001231000000:2800:D6A140CFF9843F1EBA2C45FB9FD544383EBC12D79BC1D5158CBF458BC0CAEBEC.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo--version-V14
爬取时间: 2025-04-30 23:29:58
来源: Huawei Developer
查询ohpm-repo版本。
命令格式
功能描述
打印ohpm-repo的版本号。
示例
执行以下命令，查看版本信息：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.60117360288300131349660905772953:50001231000000:2800:67D30ADD0FEB1C36578A04AF821B38AE50FB843148CBCFBE3B75E2283EF4C01B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-encrypt_password-V14
爬取时间: 2025-04-30 23:30:32
来源: Huawei Developer
加密明文密码。
命令格式
功能描述
使用指定的加密组件加密从标准输入读取的数据，并在标准输出中输出密文。
选项
crypto_path
必须在 encrypt_password 命令后面配置 --crypto_path <string> 参数，指定加密组件的路径。如果是完整组件，将用该组件去加密明文密码。如果是一个空目录，则命令将生成新的加密组件并加密明文密码。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150813.49665635163565191913264390815438:50001231000000:2800:6A492DC677F398A441E6BED4D90D2EC8991B692AB97CE99E5DA2CD10273D4156.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-pack-V14
爬取时间: 2025-04-30 23:31:07
来源: Huawei Developer
打包ohpm-repo部署目录文件。
前提条件
已成功执行start 命令或者restart 命令，ohpm-repo服务启动成功。
命令格式
功能描述
用于打包ohpm-repo部署目录deploy_root下的conf ，db和meta目录。
说明：
参数
<deploy_root>
必须在 pack 命令后面配置 <deploy_root> 参数，指定待打包的ohpm-repo私仓部署目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.35148452895622111456855362597851:50001231000000:2800:4BEB20A5A7F32802A3E6E62717692D2EB771DA3A7B7F30E8FAD920B395755D78.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-deploy-V14
爬取时间: 2025-04-30 23:31:44
来源: Huawei Developer
使用备份文件部署新的ohpm-repo实例。
前提条件
已获得由pack 命令打包的 .zip 文件。
命令格式
功能描述
命令将使用由 ohpm-repo pack 得到的打包产物部署新的ohpm-repo实例。 命令要求数据存储必须使用mysql，文件存储必须使用  sftp ，且在命令执行时，会检查数据库 mysql 中存储的ohpm-repo实例列表与配置的 sftp 存储目录中的ohpm-repo实例列表是否一致，若不一致则命令执行失败。
参数
<file_path>
必须在 deploy 命令后面配置 <file_path> 参数，指定打包产物路径。
选项
deploy_root
可以在 deploy 命令后面配置 --deploy_root <string> 参数，未配置将使用默认值。支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
logs
可以在 deploy 命令后面配置 --logs <string> 参数，指定 log 目录，优先级高于 config.yaml 中的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
uplinkCachePath
可以在 deploy 命令后面配置 --uplinkCachePath <string> 参数，指定远程包缓存路径，优先级高于 config.yaml 中的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
部署实例成功后，命令行所配置的deploy_root，logs 和 uplinkCachePath会写入到运行时配置文件中，可从 <deploy_root>/conf 目录中的配置文件 config.yaml 中查看。
skip-db
在deploy命令后面配置-sd或者--skip-db，指定是否跳过对mysql数据库中数据表的初始化；默认会读取ohpm-repo解压目录中的schema.sql文件，对mysql数据库中的表进行初始化。
在ohpm-repo配置文件config.yaml中，配置项db.type只有为mysql时，此参数才生效。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.41117529849524581618342569315721:50001231000000:2800:64E2CBF7A4438B5077996E43BB07C6CA7F08B9729454C15C5453810B64E575D2.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restore-V14
爬取时间: 2025-04-30 23:32:18
来源: Huawei Developer
将 ohpm-repo pack 打包产物替换 <deploy_root> 目录下相应文件，重启服务。
前提条件
命令格式
功能描述
该命令会停止当前ohpm-repo服务，并用打包文件 <file_path> 中的内容替换ohpm-repo部署根目录 <deploy_root> 的相应文件，然后重启ohpm-repo服务。该命令执行前必须已经执行过ohpm-repo实例启动命令 ohpm-repo start。
支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
参数
<file_path>
指定待解压的打包文件路径。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.29902279044155118323258458241902:50001231000000:2800:4A0DFC627DD676248D4D926EEC5873E66A82ACBA6233C58872D571B11726F937.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-mirror_storage-V14
爬取时间: 2025-04-30 23:32:53
来源: Huawei Developer
同步 sftp 存储的包。
前提条件
命令格式
功能描述
该命令必须配置文件存储插件模块为 sftp。命令会将源sftp目录下满足 <target> 条件的包同步到目标sftp目录下。
参数
<source_sftp>
必须在 mirror_storage 命令后面配置 <source_sftp> 参数，指定源sftp配置的名字。
<target_sftp>
必须在 mirror_storage 命令后面配置 <target_sftp> 参数，指定目标sftp配置的名字。
<target>
必须在 mirror_storage 命令后配置 <target> 参数，指定满足条件的包；或使用 @all 指定所有包。
选项
failed
可以在 mirror_storage 命令后面配置 --failed 选项，则只同步在下载错误日志中未被处理的且满足 <target> 条件的包，如果同步成功，则相应的错误日志会被设置成 handled。
示例
执行以下命令，同步包 @ohos/axios@2.0.3：
说明：将名为 test_one_sftp 的sftp目录中 @ohos/axios@2.0.3 包同步到名为 test_two_sftp 的sftp目录中。
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.94639501308319891011670272765776:50001231000000:2800:96DA42188C5EAB6EE03F9B4CE18D8CF342C7F8F665EB9290C2C7584B27530D30.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-check_storage-V14
爬取时间: 2025-04-30 23:33:27
来源: Huawei Developer
检查 sftp 中存储包的完整性。
前提条件
命令格式
功能描述
命令根据元数据检查 sftp 存储的包是否存在且完整。该命令要求数据存储 db 模块必须使用 mysql，文件存储 store 模块必须使用 sftp。
参数
<target>
必须在 check_storage 命令后面配置 <target> 参数，指定要检查的包或者用 @all 指定检查所有包。
选项
failed
可以在 check_storage 命令后面配置 --failed 选项 ，则只检查在下载错误日志中未被处理的且满足<target>条件的包。
示例
执行以下命令，检查包 @ohos/basic-ftp 的完整性：
检查 @ohos/basic-ftp 包在所有 sftp 存储目录中的完整性。
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.91174950421846738044757764858152:50001231000000:2800:921DEB9D518A56CE9AF05619880523272BDB8E9BDF0BA80181699F87742BCACF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-remove_instance-V14
爬取时间: 2025-04-30 23:34:02
来源: Huawei Developer
删除本机实例信息。
前提条件
命令格式
功能描述
该命令会停止当前运行的ohpm-repo服务，同时删除本机在 mysql 和 sftp 中的实例信息。命令要求数据存储 db 模块必须使用 mysql，文件存储 store 模块必须使用 sftp。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.06030284216243310096606784157288:50001231000000:2800:F7CBC6A0D2F3B7F5D36DAD89369CBC0F7ED6F5E23C07F7BC15DCE14C60481DEC.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-command-data-migration-V14
爬取时间: 2025-04-30 23:34:37
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-export-pkginfo-V14
爬取时间: 2025-04-30 23:35:12
来源: Huawei Developer
导出ohpm-repo或OpenHarmony三方库中心仓已上架的包列表。
命令格式
功能描述
将所有或者与输入正则表达式匹配的已上架库的包名导出到当前目录的pkgInfo_xxx.json文件。
选项
--public-registry
在export_pkginfo命令后面配置--public-registry  <string>，指定OpenHarmony三方库中心仓registry地址获取已上架的包列表。
--http-proxy
在export_pkginfo命令后面配置--http-proxy  <string>，发起请求时将为上面配置的--public-registry地址设置代理。
--filter
在export_pkginfo命令后面配置--filter <string>，可以根据正则表达式导出匹配的包列表，根据完整包名匹配。
三方包的命名规则为：@<组织名>/<包名>@<版本号>。
示例
执行以下命令从ohpm-repo中导出已上架的包列表：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.09072874196839927698886142877675:50001231000000:2800:C285D7C729AA62A369B437AFF7107812EFD0382F19F3FABF9A9972382B6DCE9E.png?needInitFileName=true?needInitFileName=true)
执行以下命令从OpenHarmony三方库中心仓中导出已上架的包列表：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.25961594709780162054721868032298:50001231000000:2800:A0B860019ECCAFE208FB2E96427EE2D488FB92D6778FDAB9B495D87F1E1DCDE0.png?needInitFileName=true?needInitFileName=true)
执行以下命令从ohpm-repo本地存储中，导出所有名为 pack1，版本是 1.1 的（可以是 1.1.1, 1.1.2, 1.1.3等）已上架的包列表：
执行以下命令从ohpm-repo配置的public-registry仓库中，导出所有属于组ohos，且名为lottie的所有版本的已上架的包列表：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-batch-download-V14
爬取时间: 2025-04-30 23:35:46
来源: Huawei Developer
批量下载ohpm-repo或OpenHarmony三方库中心仓的包文件。
前提条件
已成功执行export_pkginfo 命令，生成pkgInfo_xxx.json文件。
命令格式
功能描述
根据提供的包名列表用于批量下载ohpm-repo或OpenHarmony三方库中心仓的包文件，并导出zip文件。
说明：执行export_pkginfo 命令生成的pkgInfo_xxx.json文件中记录着ohpm-repo或OpenHarmony三方库中心仓中所有已上架的包，若仅需要批量下载部分包文件，可以手动修改pkgInfo_xxx.json文件，命令只会批量下载pkgInfo_xxx.json文件中指定的包。
参数
<pkg_list>
必须在 batch_download 命令后面配置 <pkg_list> 参数，指定执行export_pkginfo 命令导出的json文件。
选项
--public-registry
在batch_download命令后面配置--public-registry  <string>，指定OpenHarmony三方库中心仓registry地址下载包文件。
--http-proxy
在batch_download命令后面配置--http-proxy  <string>，发起请求时将为上面配置的--public-registry地址设置代理。
--not-use-proxy
在batch_download命令后面配置--not-use-proxy  <string>，发起请求时不会为指定的地址设置代理，如果有个多个地址请使用英文逗号分割并使用url编码转换特殊字符。
示例
执行以下命令从ohpm-repo中批量下载包文件：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150814.05152402250640835741500443957257:50001231000000:2800:E6B12C51983A21CB0130457A6F22FF2AED200FCEE03220114A4DD0EE638EADF5.png?needInitFileName=true?needInitFileName=true)
1、生成的zip文件中存在 pkgInfo.json 文件，其中记录了每个包的文件名、包名、组织、上传者、Tag标签，用于在批量上传时准确指定ohpm-repo的数据库中某个用户为某个包的真实上传用户，同时将包的Tag标签一起上传。
2、命令执行中，如果某个包的用户在ohpm-repo中不存在，将默认指定该包的上传用户为管理员用户或者组织的管理者用户。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.68225564042457732931386355714202:50001231000000:2800:F5D16E08697379CD6E0C82724A02D64CE78BEB9E2B2DDA55DF55D4405BB4FB92.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.74180809753020180270618822673789:50001231000000:2800:EE437603C61364E0D554917DADA8069EABE1B7EE75856F7DEFE150C4C0EC58CD.png?needInitFileName=true?needInitFileName=true)
执行以下命令从OpenHarmony三方库中心仓中批量下载包文件：
结果示例：
如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo网站页面中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-batch-publish-V14
爬取时间: 2025-04-30 23:36:20
来源: Huawei Developer
批量上传包文件。
前提条件
已成功执行batch_download 命令、export_userinfo 命令、import_userinfo 命令，确保每个包指定的包文件、用户和组织都存在。
命令格式
功能描述
根据提供的zip文件批量上传其中的包到ohpm-repo。
参数
<zip_file>
必须在batch_publish命令后面配置<zip_file>参数，指定执行batch_download命令导出的zip文件。
选项
--force
在batch_publish命令后面配置--force，进行批量上传时某个包的组织在ohpm-repo中不存在，将选取一位管理员用户作为组织负责人自动创建组织。
示例
执行以下命令：
结果示例：
如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo实例缓存中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-export-userinfo-V14
爬取时间: 2025-04-30 23:36:54
来源: Huawei Developer
导出用户必要的DB数据。
命令格式
功能描述
在当前的工作目录导出记录了DB数据的 export_userInfo_xxx.zip 文件，其中包含加密组件和下面的9个数据表。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.27996260988850957887101613286111:50001231000000:2800:BDB7916A7B24EE19A95D01A37077569963F8B823D2EC06DE9A5D187BEB32596F.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.91752015594546016038614116471577:50001231000000:2800:448ED2D9D35523C688406C182677B64A1670F839985770FB806E6FE7702E33CB.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-import-userinfo-V14
爬取时间: 2025-04-30 23:37:28
来源: Huawei Developer
导入用户DB数据。
前提条件
已成功执行export_userinfo 命令。
命令格式
功能描述
根据提供的zip文件导入用户DB数据到ohpm-repo。
参数
<zip_file>
必须在 import_userinfo 命令后面配置 <zip_file> 参数，指定执行export_userinfo 命令导出的zip文件。
选项
clean-db
可以在 import_userinfo 命令后面配置 --clean-db  参数，指定在导入数据前先清空DB数据。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.92455944894445804127236544144340:50001231000000:2800:D74A015AD41140F4EEE33F36DB6617F6B2752C134B9BC45A6813C847F8872407.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-deploy-guide-V14
爬取时间: 2025-04-30 23:38:01
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-deploy-single-instance-V14
爬取时间: 2025-04-30 23:38:35
来源: Huawei Developer
ohpm-repo 私仓不允许使用 root 用户启动，请使用其他用户安装运行。
安装ohpm-repo工具
1.  ohpm-repo 依赖于 node 运行，支持 node.js 18.x 及以上版本，请提前安装 nodejs,并完成环境变量的配置。Node.js 安装请参考Node.js官方网站。
2.  下载 ohpm-repo 工具包，点击链接获取。
3.  解压 ohpm-repo私仓工具包。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150815.22608594620222147268999985613100:50001231000000:2800:9C456635A6A9B143284C496AA2BA7935B77510B5C237F02898AE18B0CD607819.png?needInitFileName=true?needInitFileName=true)
1.  终端输出版本号（如：2.0.0），则表示安装包解压无问题。如有报错，请参考FAQ解决。 针对Linux和Mac系统，建议使用bash作为命令行界面。
2.  数据存储 db 模块使用filedb： 文件存储 store 模块使用fs： 检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址，不配置取默认值，具体请参考server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改server的 host 为本机指定的 ip/域名，例如 listen 为 0.0.0.0:8088，故 server 需配置为  http://<指定部署机器的ip/域名>:8088。
3.  数据存储 db 模块使用filedb：
4.  文件存储 store 模块使用fs：
5.  检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址，不配置取默认值，具体请参考server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改server的 host 为本机指定的 ip/域名，例如 listen 为 0.0.0.0:8088，故 server 需配置为  http://<指定部署机器的ip/域名>:8088。
6.  不配置参数 --config，默认使用ohpm-repo根目录中 conf 目录内自带的配置文件 config.yaml。 启动成功日志信息如下：
-  数据存储 db 模块使用filedb：
-  文件存储 store 模块使用fs：
-  检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址，不配置取默认值，具体请参考server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改server的 host 为本机指定的 ip/域名，例如 listen 为 0.0.0.0:8088，故 server 需配置为  http://<指定部署机器的ip/域名>:8088。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.09254167520488159729722668904307:50001231000000:2800:E2CC243A4BD904D64267B1DE4425DA6020B7FF7991BC214BA362AD8A5BC822BF.png?needInitFileName=true?needInitFileName=true)
启动ohpm-repo
执行 start 命令启动ohpm-repo。
启动成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.35477309498065697430032434860588:50001231000000:2800:C56769554102F36616E6F29FA60672A26B4282151AC80EEDAF496B525F52DBEA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-deploy-multiple-instances-V14
爬取时间: 2025-04-30 23:39:10
来源: Huawei Developer
ohpm-repo 私仓不允许使用 root 用户启动，请使用其他用户安装运行。只有db存储为mysql且store存储为sftp或者custom时，才支持多实例方式部署。本章节多实例部署以db存储为mysql，store存储为sftp为例。
环境准备
安装ohpm-repo工具
1.
2.  终端输出版本号（如：2.0.0），则表示安装包解压无问题。如有报错，请参考FAQ解决。 针对Linux和Mac系统，建议使用bash作为命令行界面。
3.  1、ohpm-repo文件的存储路径为： <sftp服务器配置的存储根目录> +<store配置的path路径>，其中path只支持相对路径，必须以/开头。例如sftp服务器存储根目录为/user/sftp/data，store中path配置的路径为/source，故最终ohpm-repo文件存储路径为/user/sftp/data/source。 2、多实例部署ohpm-repo时，必须配置反向代理服务器，转发客户端请求到部署的多个ohpm-repo实例服务器中，故store.config.server必须手动配置为反向代理服务器的域名/ip地址，且需要配置use_reverse_proxy值为true。
4.  1、ohpm-repo文件的存储路径为： <sftp服务器配置的存储根目录> +<store配置的path路径>，其中path只支持相对路径，必须以/开头。例如sftp服务器存储根目录为/user/sftp/data，store中path配置的路径为/source，故最终ohpm-repo文件存储路径为/user/sftp/data/source。 2、多实例部署ohpm-repo时，必须配置反向代理服务器，转发客户端请求到部署的多个ohpm-repo实例服务器中，故store.config.server必须手动配置为反向代理服务器的域名/ip地址，且需要配置use_reverse_proxy值为true。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.65607136310205994255207384376784:50001231000000:2800:825E7C59CB44D68E23D175C595FC4724B035905F1185A6A5812EDD8C80CAF1C7.png?needInitFileName=true?needInitFileName=true)
-  1、ohpm-repo文件的存储路径为： <sftp服务器配置的存储根目录> +<store配置的path路径>，其中path只支持相对路径，必须以/开头。例如sftp服务器存储根目录为/user/sftp/data，store中path配置的路径为/source，故最终ohpm-repo文件存储路径为/user/sftp/data/source。 2、多实例部署ohpm-repo时，必须配置反向代理服务器，转发客户端请求到部署的多个ohpm-repo实例服务器中，故store.config.server必须手动配置为反向代理服务器的域名/ip地址，且需要配置use_reverse_proxy值为true。
1.  不配置参数--config，则默认使用 ohpm-repo 解压目录中 conf 目录内自带的配置文件config.yaml。 安装成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.40393824776991426365594347822256:50001231000000:2800:C69F428DDDFB1296A003B2D86AA75F20FB1C97D5B014109D71DAAADCA5DE7AEF.png?needInitFileName=true?needInitFileName=true)
部署首个节点
进入ohpm-repo解压目录的 bin 目录中，命令行启动ohpm-repo。
启动成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.08478191607331922230834887130897:50001231000000:2800:3CF4E00E9F49D5FEEE4D5F4ACAEF2DFC415F3C758654F0D30158643ED3D1C68C.png?needInitFileName=true?needInitFileName=true)
打包和部署
为帮助更方便地完成多实例部署，已提供打包和部署命令。
打包
在完成了多实例配置并首次启动过ohpm-repo服务实例的机器上，执行 ohpm-repo pack <deploy_root>。
该命令用来打包备份ohpm-repo的 <deploy_root>/conf，<deploy_root>/meta 目录，并在命令行工作目录下生成压缩包。
打包成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.98595397421206323312868691017226:50001231000000:2800:8ECCDDE4E8BD50DB26CE73DDA3B309255F0A3BA388AFB7D1085860ADDC76CC33.png?needInitFileName=true?needInitFileName=true)
部署
将 pack 命令的产物拷贝到其他机器中。在解压ohpm-repo压缩包后，使用 ohpm-repo deploy <file_path> 命令部署新的实例。
部署成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.82979833051036729212318226517604:50001231000000:2800:F39822B49A46F58E25477B3C969BD54027746F70F835DF8BE5CE77F2C0BD1106.png?needInitFileName=true?needInitFileName=true)
部署成功后可执行 ohpm-repo start 启动ohpm-repo。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150816.22492215809876455618146935100382:50001231000000:2800:FFCE2FCC119F367616CE101B1E318976B663337E43F53EF2309041E90B15DC23.png?needInitFileName=true?needInitFileName=true)
配置自动重启（可选）
为ohpm-repo实例配置系统重启时自动重启的功能。
在进行该配置前需要将 ohpm-repo 工具 bin 目录配置到环境变量path中。
Linux
1.  当 mysql 或 sftp 服务与 ohpm-repo 部署在同一服务器上时，请将 mysql 和 sftp 的启动命令放在 ohpm-repo start 命令之前。
```typescript
@reboot /bin/sh run-repo.sh >/dev/null 2>&1
```
其中 run-repo.sh 表示要执行的脚本路径；>/dev/null 2>&1 表示将输出重定向到空设备，即不输出任何信息。
现在，每次系统启动时，都会自动执行 run-repo.sh 脚本中的命令。
Windows
1.  当 mysql 或 sftp 服务与 ohpm-repo 部署在同一服务器上时，请将 mysql 和 sftp 的启动命令放在 ohpm-repo start 命令之前。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.59920250406600099005616797339153:50001231000000:2800:0CF677D3C00658E9666779295A9B145F0AA9BBACD4DEE15CE67219FA240CA29D.png?needInitFileName=true?needInitFileName=true)
现在，每次系统启动时，都会自动执行 run-repo.bat 脚本中的命令。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-web-introduction-V14
爬取时间: 2025-04-30 23:39:44
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-web-front-page-V14
爬取时间: 2025-04-30 23:40:18
来源: Huawei Developer
ohpm-repo私仓从5.0.2版本开始，新增接口防重放攻击机制。请保持ohpm-repo私仓部署的服务器与访问ohpm-repo私仓管理界面的客户端机器时间同步。如出现访问页面报错“非法请求”，请参考FAQ解决。
启动 ohpm-repo 私仓后，可以通过浏览器访问ohpm-repo页面，访问路径为http://<机器IP>:<监听端口>。
其中，http是ohpm-repo的默认网络协议，可以在配置文件中进行修改。<机器IP> 是部署ohpm-repo服务器的IP地址，<监听端口> 是ohpm-repo配置文件中 listen 选项所设置的监听端口。
例如，将ohpm-repo部署在 IP 为 192.168.10.10 的服务器上（如不清楚部署ohpm-repo服务器的 IP，可在 Linux 上运行ifconfig 命令，Windows 上运行 ipconfig 命令查看），同时ohpm-repo配置文件的 listen 选项配置为 0.0.0.0:8088，此时访问ohpm-repo页面的 URL 就是 http://192.168.10.10:8088。
ohpm-repo会自动创建默认管理员账号，账号名称：admin，账号密码：12345Qq!。为保证ohpm-repo账号安全，该账号在首次登录时，强制修改该密码，请设置新密码后重新登录。
首页
首页主要展示当前 ohpm-repo 私仓存储的包信息，同时提供搜索功能，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.71820217002931210520126069819115:50001231000000:2800:D92B28BA91D914F912A165E8E29A5743C44E5EAA69FD2493DB201228C93D1CD7.png?needInitFileName=true?needInitFileName=true)
包详情页
包详情页主要展示当前包的详细信息，这些信息主要来源于包的内部文件，同时记录了包的版本信息和下载量数据，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.62428663869492245192284226816010:50001231000000:2800:86CFC72B2E43F99062B4DC25B666C4E7E1B6A2A35632896323EB333316E8FADF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-web-user-center-V14
爬取时间: 2025-04-30 23:40:52
来源: Huawei Developer
个人中心主页是 ohpm-repo 私仓的核心管理页面，整个系统在此进行集中管理和操作，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.40552461671615547344296554224199:50001231000000:2800:2FAC7523271D28D964F7F1B127DF8632F94B9691B599B2CBD316F0B43595B583.png?needInitFileName=true?needInitFileName=true)
-  为保障账户安全，请勿使用简单或重复密码，并定期更换密码。
-  管理员菜单： 普通用户菜单：
-  管理员菜单：
-  普通用户菜单：
-  管理员菜单：
-  普通用户菜单：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.05808920378438099985579146612364:50001231000000:2800:0726709547778BBC46EEF102C30C5DD9A8BB8F46D6CA738622635E79FDE60C6C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.43759389085526507008079124805250:50001231000000:2800:F2241B097FB740FE153438DF36BB4F403E8B7C7265E98ADFDE4E9A8DDAC9478C.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-user-management-V14
爬取时间: 2025-04-30 23:41:27
来源: Huawei Developer
存储在 ohpm-repo 私仓的包目前仅支持使用 ohpm-cli 命令行工具下载，且在下载过程中，ohpm-repo不会对下载者进行身份认证。因此，对于ohpm-repo私仓的用户管理，只需要关注和管理有发布包需求的用户即可。用户管理页面可以新增用户、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.85686453525128119797189756977547:50001231000000:2800:FC0F5A28CB388A48D5CE5DB49931EF022F826741C017A65759B81ADE4F9E7943.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.  5. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名搜索，搜索页面效果如下图所示(以指定用户类型为系统管理员，用户名为user3为例)：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.92236760028920303093136252018522:50001231000000:2800:9C0DBDAC5DBE4068939DD444B17CF9597C265C1DCAB3A905E166F5591C9B038B.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150817.50924150188959932427574458794826:50001231000000:2800:62BCE7CCFAB5428BB92D42D2042941455688A665C05FCE5AA507E041997E0FC4.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.02368896680635171647486854654876:50001231000000:2800:A82FDAE1A891137CD43526FD1254774B91C9E840480D35E6496A6D7D464CC582.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.13378458794419381027059649859787:50001231000000:2800:CD08890F3680770C201293F403ADB39F970481835478E2B7B980E3B563E57527.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.37187879502906512482367481800646:50001231000000:2800:9A7FB01DF80D381FEFD213C447E4B07A8F04FF030A4AFB997A5301C8F8288228.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-depot-management-V14
爬取时间: 2025-04-30 23:42:01
来源: Huawei Developer
仓库管理主要负责管理仓库信息，包括仓库的存储、uplink 和代理信息。
管理仓库
管理仓库页面展示当前仓库信息，包含编辑仓库和管理三方库两部分，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.15625936284233660274908578320128:50001231000000:2800:B9CAB6CE78A12303472FF03827C540879C08EC2F2DE995664D235567870E9191.png?needInitFileName=true?needInitFileName=true)
点击“编辑”按钮，进入仓库信息面板，可以修改仓库的name 、uplink和描述信息，其中uplink为下拉框选择，选项为仓库管理页面的uplinks面板配置的uplink仓库，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.40754399152652503047579814259448:50001231000000:2800:E6F1473954805178AC470B128BD0D4963F5185C091F5004826FFEF437B2924B0.png?needInitFileName=true?needInitFileName=true)
点击“管理三方包”按钮，进入仓库管理详情面板，展示所有已上传至ohpm-repo的三方包信息，管理三方库包含上传三方库包、单个包下架、批量下架和搜索三方包四个功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.68843012820283457992247237959574:50001231000000:2800:8B27C9E3BC98EFA820476E111F199306ED58A2B5FE8BB3AC6AA5DAA01FE9890F.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.  - name：支持对包名进行模糊搜索。 - version：支持输入最小版本号和最大版本号，进行版本号区间搜索。 - Publisher：支持对包发布者名称进行模糊搜索。 - Author：支持对包作者名称进行模糊搜索。 - PublishTime：支持对包发布时间进行区间搜索。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.13187402396683696603834156068346:50001231000000:2800:E7ABE76BFC6E5BA7E332C921899AE54DE7FEFAA242B543C6721FBBACCA2E66BD.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.02935671513988892946573096340893:50001231000000:2800:9E0FBD3E12F99EC7659237057B2BFF9E2E907333C50A174BEDF96D1D69B08A22.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.31648750428580541557519012868131:50001231000000:2800:9F36B7189DF770E29FEF69916E2818519E18F3C4E5D318B1CEBAD4CAB3BCB625.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.22374534670852503317122056230087:50001231000000:2800:47C1C60CE418D873A072178278EDBF5FE523328EC1193B6A914C16F597F36636.png?needInitFileName=true?needInitFileName=true)
uplinks
uplink 功能可以让当前仓库获取配置的 uplink 仓库的所有包，若从某个已配置 uplink 的仓库下载当前仓库中不存在的三方包时，则会通过 uplink 仓库下载该包，如果访问 uplink  仓库需要代理，请配置好所需代理信息，uplink 页面如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.29407421620727513229651759748728:50001231000000:2800:AA308BFEAF73180F9F6100D4967C9AE95856788FA09CE774C65342E7CC697AC3.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.78315001054836874243174977772304:50001231000000:2800:8B62DB5212557153E92ABD34E05F47D1931B8166ACAD8D2690D3941B7CC7BCC6.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150818.55993131972660207306849383578500:50001231000000:2800:63062123280E4A145AC37BE115641BD7C5C25045627C8D53111E8D8F1A16B17A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.23232575520666311605469834108297:50001231000000:2800:C25A34EADA5774F6CAA5AA6C07C68587499126C1FB3497CFF87318E5C43442F1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.51640832512338465187121732131805:50001231000000:2800:551E486D618BBE0F26CE7F71A8E94643EECC13516B26139399B5693F00B37BCA.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-certification-V14
爬取时间: 2025-04-30 23:42:36
来源: Huawei Developer
当前 ohpm-repo 的认证方式有证书认证和AccessToken两种方式：
证书认证：在使用ohpm客户端执行publish，unpublish或dist-tags相关命令时，通过嵌入加密ssh证书进行身份验证。
AccessToken认证：将 ohpm-repo 生成的AccessToken配置到ohpm客户端配置文件中，实现publish、unpublish、dist-tags、info和install等操作的免密认证。
证书认证
使用 ohpm 发布包时，需要先在配置文件 .ohpmrc 文件中配置 publish_id 和 key_path 。publish_id 对应发布码，key_path 对应私钥的地址，其详细发布流程见：使用命令行工具发布。认证管理主要是管理私钥对应的公钥信息，在用户使用 ohpm 发布包时进行校验。认证管理页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.61474342816840637931274817360690:50001231000000:2800:0B3A2FF68D9FFBFBF75FB2C9FB50909ADD3EE10BDB9DB72023E66487F05D3882.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.93326111794630038900577941517504:50001231000000:2800:0CD9E7ACD5E5B919A2DA7D6091F1789F4243239BEA9472CE9D21DE98067F7C7C.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.50293244426518300133960578427379:50001231000000:2800:682840F3C7D545FBEEF4D28DECE85296B83E3CC4ACEF24637665163BC1132957.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.10274993267940621038448668897699:50001231000000:2800:E706403E5A3DF623CF291CEBC81557E6B416CAD2DE22D6B90DB1AEFDBBDD69FE.png?needInitFileName=true?needInitFileName=true)
AccessToken
AccessToken是 ohpm-repo 2.1.0版本新引入的认证机制（需配套使用1.6.0及以上版本的ohpm命令行工具），用户通过 ohpm-repo 界面生成Token，并将其配置至ohpm客户端配置文件中。在与 ohpm-repo 交互时，客户端会自动附带Token进行身份验证。
该Token分两种权限等级：只读Token允许执行info和install操作；读写Token除了包含只读权限外，还支持publish，unpublish和dist-tags相关操作。每位用户每种权限类型的Token最多可生成10个，首次生成时系统自动复制到剪贴板，后续不再显示完整Token内容。AccessToken页面效果如下:
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.37181454821109840968887170223039:50001231000000:2800:BC0B653D6D1AAD1F76ED43AA1A87ADD9D4D4681ECD0D6853A959CF99BB10B787.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.
5.  其中 //127.0.0.1:8088/repos/ohpm/ 是您 ohpm-repo 的registry地址去除协议名的部分，:_auth 和 :_read_auth 分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish和dist-tags操作时只会使用读写Token。每种Token最多配置三条。
6.  其中 //127.0.0.1:8088/repos/ohpm/ 是您 ohpm-repo 的registry地址去除协议名的部分，:_auth 和 :_read_auth 分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish和dist-tags操作时只会使用读写Token。每种Token最多配置三条。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.87057533473961452388656393350661:50001231000000:2800:F03400AA931F3E1528F1A50D2C3B1F6B643559B681D79C8BC87CF37D305BA9C1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.68330071656118486246821295630845:50001231000000:2800:73CA9F2C7212A74AFC39BD4ED61587A75EB4C7119781BC069CB54A1A984F73E3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.42924793626095230263766566279090:50001231000000:2800:2223BF5064108F86E670860C8FCEA78F99F18B71ECD5ECC99EC8293D38526418.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.65958405422127488440439550915331:50001231000000:2800:981D3B92E1EA06EF84BA70AC1FA9673EFA84209CD2D51EE35633293AC6434253.png?needInitFileName=true?needInitFileName=true)
1.  其中 //127.0.0.1:8088/repos/ohpm/ 是您 ohpm-repo 的registry地址去除协议名的部分，:_auth 和 :_read_auth 分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish和dist-tags操作时只会使用读写Token。每种Token最多配置三条。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-organization-V14
爬取时间: 2025-04-30 23:43:10
来源: Huawei Developer
在 ohpm 中包的命名格式为@<group>/<package_name>或者<package_name>。
其中 group 是组织，package_name 是包名。当想要上传一个含有组织（例如@ohos/axios）的包时，在ohpm-repo中需要先创建出该组织（例如ohos）才能进行上传。
在发布HAR/HSP包时，建议将组织名称包含在包名（package_name）中，便于管理和识别三方库。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.04652403786802588425644812815042:50001231000000:2800:EE231F50EE30F906F6E814428F02A1A6828DFDD6CC6EFCA451BC8C9722272444.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.46451647894857348835830509648637:50001231000000:2800:C8215B2F1C3F2EDD6F8C13C300DDCC5910F700D10A12AE1C2377B77B5AF37156.png?needInitFileName=true?needInitFileName=true)
1.
2.  描述：展示组织的基本信息。 包：展示该组织下仓库所上传的所有包信息。 点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
3.  描述：展示组织的基本信息。
4.  包：展示该组织下仓库所上传的所有包信息。
5.  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
6.
7.
8.  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。
9.  点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150819.22898963826309196340234827049500:50001231000000:2800:BAD94DCFC6C574555BCB44645F50880F30E7C1D15A0218CA5B981565F514AF61.png?needInitFileName=true?needInitFileName=true)
-  描述：展示组织的基本信息。
-  包：展示该组织下仓库所上传的所有包信息。
-  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
-
-
-  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。
-  点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.90028420384771095752341450081102:50001231000000:2800:B51B4AB1C2E88C937DB56779AFAEAFB2BD2AAF4E93085D615585CCBD857146C3.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.67429640005924547702003471606932:50001231000000:2800:443EE52F4D68E09BC15CEDA4BDD9E40D78880ECEC3CB3FBEA3C785FE7C49D972.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.26091553908006047211584655317127:50001231000000:2800:09FC44091AD5A59D5CDAD383D6CD36939BE785770C68EDE9A7FA0BA8B1F83E10.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.38366375684456243219149614644566:50001231000000:2800:B47FE1EAE2F6C6496B9C0F51AD28487D2732C057EBCA07A95ACD4144BDD8E0BF.png?needInitFileName=true?needInitFileName=true)
-  点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。
-  点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.71124109784006110231942555875248:50001231000000:2800:CC0D998D46C33ABE72963AF5772787FC88C576E1CB523392DC4E4517CC34EAAF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.21532950519167126563398931249618:50001231000000:2800:8BC18AC1D226B6C45B5F072ED5AA52DA9CB7749F5CF8EB1411E9A348E5DE2E31.png?needInitFileName=true?needInitFileName=true)
1.
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.59001859983751297041938698372534:50001231000000:2800:66A90AA27A229AD9217A039D51D73395B5FF3FD18765ED1B635845A36DF8B67D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.63606025364365585868516490821997:50001231000000:2800:3E4EA46B07CD20F894077642BAC144088E912D33C6C0CFD1898BA3C1C9D3A484.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.55021919619868174969312501856742:50001231000000:2800:78EAAC02A69E780B843429B7533760118EC0D079C69CC64B5B185076C49365A4.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.77075001964110236487646602926660:50001231000000:2800:07B6BB151447DD1DD79D0A701CFF625F79E14E5AC9A89A8681C7D26B738AFCEF.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.58053739886164357483033387410505:50001231000000:2800:99774BE8E8CB6A36A8B2D013BA834731932FA0971B5F7F0A219B55524CE3562D.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.47900642351136772255227672070848:50001231000000:2800:70E266F96BC71336F3CEBD7CBB48D8B89CA62753AD05C3078DE26E681BF7AD9E.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-operation-log-V14
爬取时间: 2025-04-30 23:43:45
来源: Huawei Developer
操作日志界面显示用户通过ohpm-repo管理界面进行的所有操作，以及通过ohpm命令行工具执行publish，unpublish和dist-tags等相关命令所记录的日志。操作日志界面分为两个部分：第一部分为筛选条件，第二部分是展示符合筛选条件的数据。
操作日志的数据每隔一天会定时清除，默认保留100天内的操作日志数据，数据保留时间可通过config.yaml中配置项operation_log_retention设定。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.28890655523445467389112246895663:50001231000000:2800:8D88169A6B79F7033E42B855C7196A6294E2775DFCCFA35ACF10996E6ABF0802.png?needInitFileName=true?needInitFileName=true)
-
-  一级事件类型 二级事件类型 三级事件类型 用户管理 新增用户 - 删除用户 - 修改用户角色 - 重置用户密码 - 仓库管理 管理仓库 更新代码仓 上架资源包 下架资源包 uplink 更新Uplink代理 添加Uplink 修改Uplink 删除Uplink tag 增加Tag 更新Tag 删除Tag 认证管理 证书认证 添加发布公钥 删除发布公钥 Access Token 生成Access Token 删除Access Token 组织管理 组织 添加分组 修改分组 删除分组 组织成员 添加组成员 删除组成员 组织管理员 添加组管理员 删除组管理员 系统设置 更新oh-package.json5检查规则 - 重置系统秘钥 - 更新系统安全配置 -
-
-  一级事件类型 二级事件类型 三级事件类型 用户管理 新增用户 - 删除用户 - 修改用户角色 - 重置用户密码 - 仓库管理 管理仓库 更新代码仓 上架资源包 下架资源包 uplink 更新Uplink代理 添加Uplink 修改Uplink 删除Uplink tag 增加Tag 更新Tag 删除Tag 认证管理 证书认证 添加发布公钥 删除发布公钥 Access Token 生成Access Token 删除Access Token 组织管理 组织 添加分组 修改分组 删除分组 组织成员 添加组成员 删除组成员 组织管理员 添加组管理员 删除组管理员 系统设置 更新oh-package.json5检查规则 - 重置系统秘钥 - 更新系统安全配置 -
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.61388748870877607273059552799658:50001231000000:2800:0479E39D5F628B40290810D4F91EED59860067B233C3D88ACD5A65BCC5F59481.png?needInitFileName=true?needInitFileName=true)
-
-  一级事件类型 二级事件类型 三级事件类型 用户管理 新增用户 - 删除用户 - 修改用户角色 - 重置用户密码 - 仓库管理 管理仓库 更新代码仓 上架资源包 下架资源包 uplink 更新Uplink代理 添加Uplink 修改Uplink 删除Uplink tag 增加Tag 更新Tag 删除Tag 认证管理 证书认证 添加发布公钥 删除发布公钥 Access Token 生成Access Token 删除Access Token 组织管理 组织 添加分组 修改分组 删除分组 组织成员 添加组成员 删除组成员 组织管理员 添加组管理员 删除组管理员 系统设置 更新oh-package.json5检查规则 - 重置系统秘钥 - 更新系统安全配置 -
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150820.87652258951728978388016801849468:50001231000000:2800:0FB5A3B1A9B35B01BE5003AA51A1B8AD66B2B85B6752A80CD587C37839A8CC95.png?needInitFileName=true?needInitFileName=true)
| 一级事件类型  | 二级事件类型  | 三级事件类型  |
| --- | --- | --- |
| 用户管理     | 新增用户  | -  |
| 删除用户  | -  |
| 修改用户角色  | -  |
| 重置用户密码  | -  |
| 仓库管理           | 管理仓库    | 更新代码仓  |
| 上架资源包  |
| 下架资源包  |
| uplink     | 更新Uplink代理  |
| 添加Uplink  |
| 修改Uplink  |
| 删除Uplink  |
| tag    | 增加Tag  |
| 更新Tag  |
| 删除Tag  |
| 认证管理     | 证书认证   | 添加发布公钥  |
| 删除发布公钥  |
| Access Token   | 生成Access Token  |
| 删除Access Token  |
| 组织管理        | 组织    | 添加分组  |
| 修改分组  |
| 删除分组  |
| 组织成员   | 添加组成员  |
| 删除组成员  |
| 组织管理员   | 添加组管理员  |
| 删除组管理员  |
| 系统设置    | 更新oh-package.json5检查规则  | -  |
| 重置系统秘钥  | -  |
| 更新系统安全配置  | -  |
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.68729163888615171005897257456449:50001231000000:2800:85249D9F26563CFDF035F81B544F16AD546F81FA0CFDF97F6E8867261BA1A709.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.36310381444171648244980840373607:50001231000000:2800:C44F4B464332FB923B166E71A831D02C670559B01B380B74B828E4ED64CEB1C9.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.73003638034581421181235223647258:50001231000000:2800:643A3D0DDD28C8716D022119D4097A4ACCB2613F7ACF25EBF398B05B7B7EFE38.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-system-settings-V14
爬取时间: 2025-04-30 23:44:19
来源: Huawei Developer
系统设置是ohpm-repo系统层面的管理，当前支持"oh-package.json5检查规则"和"系统安全"两大功能。
oh-package.json5检查规则
oh-package.json5检查规则是ohpm-repo对上传包的oh-package.json5文件进行校验的规则管理。当前主要针对category，repository和name三个字段设定规则。
category白名单：若其为空，系统将不会对category字段进行校验。若配置了值，则category字段的值就必须存在于白名单中。
repository：决定repository字段在oh-package.json5文件中是否必须存在。如果设置为必须，那么在上传包时，oh-package.json5文件中就必须包含repository字段。
name：oh-package.json5文件中name字段是否必须包含组织名，如果设置为是，则上传包时，则name字段必须包含组织名，无组织包将会上传失败。
页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.79989450484704659842819681170190:50001231000000:2800:9555D0FA86F7669DE482DB5258183675504EF510CF4D4E123DD02E7A11351342.png?needInitFileName=true?needInitFileName=true)
系统安全
系统安全页面中有两部分配置项：重置系统秘钥和配置是否支持匿名访问。页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.22974414700588881773588544757764:50001231000000:2800:373ED5DB85633E8E84C6991D00CE9E3A646C10BDFD62C39E08B715DA5CFD4FED.png?needInitFileName=true?needInitFileName=true)
系统密钥用于重新加密ohpm-repo服务中用户上传的公钥和uplinks的网络代理口令信息。点击重置系统密钥，将出现重置提示，如果确定重置，需要点击按钮“是”，将出现密码输入框，由于重置系统秘钥是敏感操作，故需要输入当前登录账户的密码进行再次认证，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.57021211267402708891796795831540:50001231000000:2800:D7C2BDB930EFD182EC7E0BFB36521C88B52C946243173671F91EF9F985120C35.png?needInitFileName=true?needInitFileName=true)
2. ohpm-repo匿名访问配置
ohpm-repo从5.0.5版本开始支持配置匿名访问功能。默认情况下，ohpm-repo支持匿名访问。如果需要配置不支持匿名访问，需要点击按钮“否”后提交，页面效果如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.80541995023107263020989373783261:50001231000000:2800:0A4F67E5F4EC1AD52672EE54669AF144A8ADD7C87CC1B9387315A5BF922000A1.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.60874788798543763418936300299703:50001231000000:2800:FF6B9C5415EB1A25413DF3305A4733A31BCAC17D6C894217D84A764F4E25B720.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-configuration-guide-V14
爬取时间: 2025-04-30 23:44:52
来源: Huawei Developer
为了保障用户在使用ohpm-repo过程中更加安全可靠，我们收集如下推荐安全配置项，用户可以根据自己的需要采纳配置。
最小权限启动
为降低风险，提高系统的稳定性和可维护性，ohpm-repo必须使用非root权限进行启动部署。
加密连接和监听具体地址
多实例部署
ohpm-repo用于存储私有仓库三方包数据，为了避免数据丢失，且保证ohpm-repo的高可用性，推荐元数据存储使用mysql，包数据存储使用自定义存储插件，通过使用负载均衡，部署ohpm-repo多个实例。
Mysql存储
参考配置如下：
自定义存储
使用自定义插件存储，具体配置为：
参考配置如下：
禁止匿名访问
在默认设置下，ohpm-repo仓库中的所有包信息均可供任意用户自由查看，且包文件也支持任意用户下载。为了避免不相关的人访问ohpm-repo，我们建议在ohpm-repo管理界面的系统设置>系统安全页面，关闭匿名访问功能（默认保持开启）。关闭后，只有在.ohpmrc文件中正确配置仓库只读或读写AccessToken的用户才能够通过ohpm工具下载三方包，只有登录ohpm-repo账户，才能够访问ohpm-repo管理界面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.25566523837202326515912232031060:50001231000000:2800:85A357DFBB5D4D7789E440E881DA26BBB49B054601AE5E8B567F779FE612F523.png?needInitFileName=true?needInitFileName=true)
用户访问频率控制
为了避免恶意用户频繁对仓库进行访问操作，我们在配置文件中设置配置项user_rate_limit，默认单个用户访问接口的频率为100次/秒，配置范围为 (0, 10000]。
用户上传次数控制
为了避免恶意用户频繁发布三方包，我们在配置文件中设置配置项upload_max_times，默认单个用户24小时内上传次数限制为100次，配置范围为 (0, 100000]，用户可以根据自身业务需要修改此配置值，如改为1000次。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-faq-V14
爬取时间: 2025-04-30 23:45:27
来源: Huawei Developer
ohpm-repo私仓工具获取与升级
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.99993342738547533059912223577028:50001231000000:2800:975A49213925C86AD2A2C356E19655E8E0027F5E10B799E2EA4CE67DF6B9DAE0.png?needInitFileName=true?needInitFileName=true)
ohpm-repo启动后如何修改配置文件，并使得修改后配置文件生效
ohpm-repo部署目录和ohpm-repo解压目录说明
-  ohpm-repo解压目录：<binary_root>，ohpm-repo安装包解压后所在的根目录，存放的是ohpm-repo压缩包解压后的内容；
-  ohpm-repo部署目录：<deploy_root>，ohpm-repo运行时产生数据的存储位置，包括配置文件，日志文件，加密组件等信息。ohpm-repo部署目录在不同版本有不同的配置方法。
-  ohpm-repo部署目录默认路径如下： ohpm-repo部署目录和ohpm-repo解压目录不要放在同一目录中。
ohpm-repo 的权限管理
账户权限：系统管理员和系统普通用户
1.  账户的注册 ohpm-repo注册的账户有两种类型：用户类型和管理员类型。ohpm-repo初次启动默认有一个管理员账户：账户名:admin；密码:12345Qq!。
2.
3.
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.67178619321422403544069710993902:50001231000000:2800:C3109330E1E4FC535E9633354E18C650F072E7BD5EDA9C440CDF72117814F442.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.90975314662078308155794478696249:50001231000000:2800:01C461C8B04C84BE4C9730424BC07ED106FB4F6A6B10F1DC0648547ACEFE50AE.png?needInitFileName=true?needInitFileName=true)
组织权限：组织成员和组织管理员
1.
2.
3.
4.
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150821.89456321046649874225459486757585:50001231000000:2800:590E8F051C6101BA41BCEBF0DC8ACC69921F60D98B27DF6713C121F4AFE47722.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.47321712053997458722000800725764:50001231000000:2800:5CC59BFF7F9D497A5C88C36F263E46DF70A83796F08618799A26EE6BDBBC0A41.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.66572876615675872090440626633559:50001231000000:2800:AA7EBBEAA3F3E8A06F1B35A4761CFACDA6204C42CAA1B0914F449E51649E11FD.png?needInitFileName=true?needInitFileName=true)
上传包和卸载包权限管理
三方包可以分为有组织的包和没有组织的包两类，上传和下架包可以通过ohpm-repo和ohpm命令行工具两种方式操作。
ohpm-repo 的元数据与三方包数据管理
元数据与三方包数据介绍
ohpm-repo的数据包括两部分：
元数据和三方包数据存储方式介绍
-  元数据和三方包数据的存储方法不能够随意搭配，匹配规则和支持的ohpm-repo版本信息见下图： 存储方式的变更：如果元数据和包数据的存储位置需要改变，可以通过数据迁移指导进行完成。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.07422447522451821687793401008277:50001231000000:2800:B32A334E0004AF75834C4E6E1C5F0D392F145379BF0AAA52577173F722D8CF7F.png?needInitFileName=true?needInitFileName=true)
ohpm-repo认证方式
ohpm在执行publish，unpublish和dist-tags等需要修改ohpm-repo数据库内容命令时，需要获取读写权限才能够操作。
从ohpm-repo5.0.5版本开始，如果ohpm-repo配置不支持匿名访问，ohpm在执行install，info和update命令时需要通过AccessToken认证或者自定义AccessToken认证方法，正确配置读写/只读AccessToken信息获取读权限。
认证方式说明
认证失败FAQ
使用证书认证执行publish/unpublish/dist-tags等命令失败
使用证书认证在 git-bash 终端下执行 ohpm publish XX.har 发包到ohpm-repo中报错：The content of private key in the key_path error
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.76822431905860292076527195910178:50001231000000:2800:95D72A16380609062D3D4978FF907DE4D0E9EB524D36EAC8D8B19687D3BC8F31.png?needInitFileName=true?needInitFileName=true)
使用AccessToken认证，执行publish/unpublish/dist-tags等命令失败
应用内 hsp 包如何发布到ohpm-repo
执行ohpm-repo命令报错
在执行ohpm-repo install 或者 ohpm-repo start 的时候报错：server install failed: YAMLException: bad indentation of a mapping entry
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.62195555874782554915765642801878:50001231000000:2800:479A3FB17425C41233D33CF7943CB9BE3D607D4B3765F37387FBC1806C5A4FED.png?needInitFileName=true?needInitFileName=true)
ohpm-repo的配置文件config.yaml 中配置缩进格式不对，并且在报错信息中会提示出错误的位置。
执行命令 ohpm-repo <command>，报错 ohpm-repo 不存在或者 <command> 命令不存在。
ohpm-repo成功启动后，根据配置文件中的 listen 值访问ohpm-repo私仓管理界面，界面不显示信息或者无法打开页面
机器A部署ohpm-repo私仓服务，在机器B上通过A的域名+端口访问已部署的ohpm-repo私仓服务，打开包的描述页出错
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.29365039130470205345019936500860:50001231000000:2800:22E8F2DFD03A0800A6CA3FE17023C8C122D04BA9BF64C3B52C14145E6845EFB3.png?needInitFileName=true?needInitFileName=true)
执行ohpm-repo install 时报错：fail to initialize encryption component: Error: invalid crypto component.
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.39091164227388031673138364646063:50001231000000:2800:887AFF9896CD75A98BCAFDAB4F200A9F54C6CB837FEBE75331F0F5997DD6F0FF.png?needInitFileName=true?needInitFileName=true)
执行 ohpm publish XX.har 发包到ohpm-repo私仓中报错
报错：connect ECONNREFUSED ::1:8089
报错：The content of private key in the key_path error.
报错：HttpCode 400 Group does not exist!
-  现象：ohpm执行publish命令，命令行报错信息为 HttpCode 400 Group does not exist!
报错：HttpCode 400 You are not a developer of the group!
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.56342109341626475584547559690854:50001231000000:2800:4372398F42AB4AB9A140250AD7227E36110A9B07E9712B0E9A33FAA598873855.png?needInitFileName=true?needInitFileName=true)
报错：ohpm ERROR: HttpCode 404 Not Found
报错：Same ohpm package is exists!
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.93781224266523214892811543543934:50001231000000:2800:1C90E64518E4360A7CB844E97069408E2CB5C7B69614711D44594076CBB393B0.png?needInitFileName=true?needInitFileName=true)
报错：Request Entity Too Large
报错：The packageType is no equals the exists packageType!
执行 ohpm install XX.har 从ohpm-repo私仓中下载包报错
ohpm-repo配置uplink后，执行install命令下载uplink所配置仓库中的包失败
-
-  上述地址，网络协议均为 https ,端口均为 443。
-  上述地址，网络协议均为 https ,端口均为 443。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.93186205056932556485669160293698:50001231000000:2800:86B4B12ABE306FD4905B8AD524A8B48EACC6A29800261F0487FBF8AADE94E934.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.07835176637135841769036363526813:50001231000000:2800:7EBE514305DE3FB16541CD6DECE1FD0F194CC20B3FB44CACFE256EF876914EB3.png?needInitFileName=true?needInitFileName=true)
-  上述地址，网络协议均为 https ,端口均为 443。
访问ohpm-repo私仓管理界面报错
访问ohpm-repo私仓管理界面中页面功能，报错：非法请求
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.53094070362500686185386858688234:50001231000000:2800:DDC331FFDA0D3B361A6BC8A1E94CDE70A7A8A37F441D6ABF194E307A6669D719.png?needInitFileName=true?needInitFileName=true)
访问ohpm-repo私仓管理页面，报错“加密组件无效”。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.50807282833957598925237071508435:50001231000000:2800:AB441D50A1BBB304CB91C300115D5EF3A97CD30855A318C1085F7911834FD997.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.00385739513731281193454242385945:50001231000000:2800:B6C224DD737E0F5440E8698208A35EED937D2CF8A02B02BA417A779E5F7A41DF.png?needInitFileName=true?needInitFileName=true)
访问ohpm-repo私仓管理界面，报错：“系统配置错误，请联系管理员“
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150822.45236911772928587159279674099605:50001231000000:2800:B5BFBFE96D8C760085D5903538903DDA555F97A04788540A55B589716AA8E78E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.79657083526955407196787058822091:50001231000000:2800:D86E0E1EA8225AD6156930969DF08FD7C8F1BE32FADD18CED69E420F6C2C44CD.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-appendix-V14
爬取时间: 2025-04-30 23:46:01
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-historical-version-V14
爬取时间: 2025-04-30 23:46:35
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-overview-history-V14
爬取时间: 2025-04-30 23:47:08
来源: Huawei Developer
ohpm-repo 是一个搭建轻量级的 ohpm 私仓服务的工具。它与 ohpm 包管理器兼容，并按需缓存所有依赖项，加速私有网络中的安装。
私有性
您所发的三方库都是私有的，只能根据您的配置进行访问。
缓存
ohpm-repo 根据需要缓存所有依赖项，加快私有网络的安装速度。
部署
ohpm-repo 支持单点部署和多实例部署。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-quickstart-history-V14
爬取时间: 2025-04-30 23:47:42
来源: Huawei Developer
如何安装
ohpm-repo
1.  下载 ohpm-repo 工具包，点击链接获取。
2.  解压文件，进入文件 bin 目录下，执行安装脚本 setup.bat(windows) 或者 setup.sh(linux/macos)。
3.  安装完成之后，进入解压文件 bin 目录下，执行如下命令： 终端输出为版本号（如：1.0.1），则表示安装成功。 若想在其他目录使用 ohpm-repo，请将 ohpm-repo工具包解压目录中 bin 目录的路径配置到系统环境变量 path 中。
4.  在启动 ohpm-repo 前还需要先按照如下方式完成配置修改，进入 ohpm-repo 的安装目录下的 conf 目录，打开 config.yaml 配置文件；
5.  检查 listen 配置，当配置为 localhost:8088 时表示仅支持监听本机地址；如果希望局域网内其他机器均可访问，则建议修改 listen 配置为监听所有地址：
6.  检查是否配置了 store.plugin_config.server，若没有配置，则在运行时该配置会自动设置成 listen 配置的值；若 listen 配置为监听所有地址 listen: 0.0.0.0:8088，则该值需要配置为详细地址，如： 如果为ohpm-repo服务配置了反向代理服务器，则该地址需要填写为反向代理服务器的地址。 config.yaml中各项配置的详细描述请见：配置文件
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.59647315904884147146151011131917:50001231000000:2800:5EEBE3AD4DF435874F4D2253F7F3AFB12C2F6F906F7D8B42DCF5F8AC6D93A794.png?needInitFileName=true?needInitFileName=true)
如何启动
完成配置修改后，进入安装 bin 目录下，执行如下命令，启动 ohpm-repo：
启动成功，将会出现以下日志信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.41933707321648791551433008666261:50001231000000:2800:D11DA3833F8901CFCD81AE1529DD33C93C3150EB92C7B168612A3A832BAB735F.png?needInitFileName=true?needInitFileName=true)
ohpm-repo 首次启动时，默认创建一个管理员账号，账号名称：admin，密码：12345Qq! 。该账号在首次登录时，需要修改其密码，请您修改密码后，重新登录该账号。
从ohpm-repo获取三方库
您可以为所有项目配置该私有仓，例如执行以下命令：
或者在命令行中配置参数 --registry 使用，例如以下命令：
<配置的ohpm-repo服务地址> 为配置文件中的 store.plugin_config.server 地址信息，此处需要完整的地址格式，例如：http://127.0.0.1:8088，故 registry 为：http://127.0.0.1:8088/repos/ohpm
将三方库发布到ohpm-repo
使用命令行工具发布
1.  示例： 公钥和私钥存储在 D 盘 的path 目录下，公钥和私钥名称分别为 my_key_path.pub和my_key_path。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.79712070593057991968948484935005:50001231000000:2800:B1DB756CFAE918A583677902DE366C2959084896293A7E4078AA1B901A011620.png?needInitFileName=true?needInitFileName=true)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.28991094437642272706556848389217:50001231000000:2800:BD906B77003A60DCF9BC39144FD18ADEE70190413C589090F084C53A222BD2E6.png?needInitFileName=true?needInitFileName=true)
1.  或在命令行中配置参数 --publish_registry 使用，例如以下命令：
命令行工具支持发布 HAR 包和 由 HSP 模块打包出来的 TGZ 包，TGZ 包的发布流程与 HAR 包一致。更多详细内容请参考：开发及引用共享包。
使用Web页面发布
在Web页面用管理员账号登录ohpm-repo，在个人中心 > 仓库管理中，点击管理三方包 > 上传三方包。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.22984055648339705064976345612938:50001231000000:2800:79F33EAEE57ADC149B498860B0C2A1DF905A8C625E0A924D34281739C1C4E2FB.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150823.69342083921433746786084285642324:50001231000000:2800:7AF547D3D8C8A07771A535C1C59DB5997FDCDF7A7558F6BBFCFE20A3B2B7EE22.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-configuration-history-V14
爬取时间: 2025-04-30 23:48:16
来源: Huawei Developer
config.yaml 是 ohpm-repo 的重要文件，您可以在其中修改默认参数配置，启动插件或者扩展功能。ohpm-repo 在解压包的conf目录下带有一个默认配置文件 config.yaml，ohpm-repo 启动时默认读取该文件。
默认配置
目前发布的版本有两个，分别为 1.0.1 和1.1.0，配置文件内容存在不同：版本1.1.0 新增支持日志路径配置，数据存储 mysql 配置和文件存储 sftp 配置等。
ohpm-repo 1.0.1版本
ohpm-repo 1.1.0版本
配置项说明
listen
格式为三段式，即 <proto>: //<host>: <port>，其中 <proto> 可以不填，默认为 http，如：
-  监听本机回环地址：
-  监听所有地址：
proto 支持 http 和 https 协议，且支持缺省，缺省时默认为http。如果您配置为 https协议，则需要完善 https 相关配置。
https
当您在配置 listen 时选择使用 https 协议，则需要配置 https.key 和 https.cert：
为了确保ohpm-repo链接的安全，建议您选择使用 https 协议，您可以使用如下命令生成 https 协议使用的证书私钥文件和证书文件：
参考配置如下：
server
服务相关配置，具体为：
-  fetch_timeout: 当使用 uplink 时，请求 uplink 数据的请求/响应超时时间，单位为秒，默认60 秒，取值范围为 (0, 3600]。
参考配置如下：
1.1.0 版本额外添加一个参数 api_timeout， 默认值取 60。
db
ohpm-repo运行过程产生的用户信息，运行状态等数据存储配置，支持本地磁盘存储和 mysql 存储。
本地磁盘存储
默认使用本地磁盘存储，配置如下：
-  path: 数据存储地址，默认值为 ./db ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
-  path: 数据存储地址，默认值为 ./db ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
-  path: 数据存储地址，默认值为 ./db ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
如果想修改数据存储路径同时保留旧的数据，则需要把旧路径下的数据文件迁移至新路径。
参考配置如下：
Mysql存储
ohpm-repo 从 1.1.0 版本开始支持使用 mysql 存储。
-  database: 数据库名。 参考配置如下：
-  database: 数据库名。 参考配置如下：
-  database: 数据库名。 参考配置如下：
store
三方库及其元数据等资源文件存储配置，支持本地磁盘存储和 sftp 存储。
本地磁盘存储
默认使用本地磁盘存储文件，具体配置为：
-  path: 存储根目录路径，默认为 ./storage ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
-  path: 存储根目录路径，默认为 ./storage ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
-  path: 存储根目录路径，默认为 ./storage ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
参考配置如下：
Sftp 存储
ohpm-repo 从 1.1.0 版本开始支持使用 sftp 存储文件，仅当数据存储为mysql 存储时才能使用sftp 存储。
参考配置如下：
uplink
-  store_path: 远程包缓存路径，默认路径为 ./uplink，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
参考配置如下：
logs
ohpm-repo 从 1.1.0 版本开始支持 logs 自定义配置。
-  logs_path: 日志存储，默认路径为 ./logs ，支持相对和绝对路径配置，当配置为相对路径时，则以ohpm-repo部署目录为根目录。
参考配置如下：
loglevel
loglevel 自定义配置，具体配置为：
参考配置如下：
关于 deploy_root
deploy_root 为ohpm-repo的部署目录，需要注意的是：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-log-history-V14
爬取时间: 2025-04-30 23:48:49
来源: Huawei Developer
与任何 web 应用程序相同，ohpm-repo 有一个内置的日志记录器，其定义了四种日志类型。
访问日志 - access.log
访问日志中主要包含操作时间、服务器 ip、操作源、操作结果以及请求接口或者请求静态资源，其文件保存个数最多为 180 个。
操作日志 - operate.log
操作日志中主要包含操作时间、操作人、终端 ip、操作方法名以及操作结果，其文件保存个数最多为 180 个。
运行日志 - run.log
运行日志中主要包含操作时间、日志级别以及日志信息，其文件保存个数最多为 30个。运行日志定义了日志级别：all，trace，debug，info，warn，error，fatal，mark 和 off。
下载错误日志
当从仓库中下载某个包失败时，仓库会生成一条错误日志记录在数据库中的 downloadfailure 表中，当为ohpm-repo配置了 sftp 存储服务时，从任意一个sftp 服务中下载失败时，都会生成一条错误日志并保存。每条日志都有 handled 标识，handled 为 0 时表示已处理，handled 为 1 时表示未处理。
日志存储路径
日志存储的默认路径为 ./logs
-  1.1.0 版本开始支持在配置文件中自定义日志存储路径。
-  在ohpm-repo start或ohpm-repo deploy启动时，如果指定 <deploy_root> 参数，以上相对路径基准为指定的 <deploy_root>目录。
-  如果没有指定 <deploy_root> 参数，则相对路径基准为： windows系统: ~/AppData/Roaming/Huawei/ohpm-repo 其他操作系统：~/ohpm-repo
日志打印级别
在配置文件中可以设置访问、操作、运行日志的打印级别，日志将会只打印不低于设置级别的日志，日志级别由低到高为：all，trace，debug，info，warn，error，fatal，mark 和 off。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-command-history-V14
爬取时间: 2025-04-30 23:49:23
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-help-history-V14
爬取时间: 2025-04-30 23:49:58
来源: Huawei Developer
获取有关 ohpm-repo 的帮助。
命令格式
参数
功能描述
-  如果提供了命令名称，则显示相应命令的帮助信息。
-  如果提供的命令名称不存在或未提供，则显示所有命令的概要信息。
示例
执行以下命令：
结果示例：
1.0.1：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.48073824147363634063250661788112:50001231000000:2800:817E5A757EA9F40F2FB5A0B9845024C9A26C8F2FB17653BB9E7C3A8C16E2F3AB.png?needInitFileName=true?needInitFileName=true)
1.1.0：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.86111557335935457990030054761187:50001231000000:2800:DF50C23C0F2AB949101FBF42707297139B05473D5E87A674EA1ECE25C352A461.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-start-history-V14
爬取时间: 2025-04-30 23:50:31
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-start101-history-V14
爬取时间: 2025-04-30 23:51:05
来源: Huawei Developer
启动ohpm-repo服务。
命令格式
功能描述
用于启动ohpm-repo服务，创建一个ohpm-repo实例。
选项
listen
您可以在 start 命令后面配置 --listen <string> 参数，指定启动端口和绑定访问地址，优先级高于 config.yaml中 listen 的配置。listen 参数可以指定协议 http 或者 https，若指定为 https，config.yaml文件中必须配置证书。若不指定，默认为 http。
config
-  <binary_root>：ohpm-repo 项目根目录
您可以在 start 命令后面配置 --config 参数，指定配置文件路径，仅支持绝对路径配置。
执行 start 过程中，会把读取到的配置文件拷贝至相对路径 /conf/config.yaml 内。其中相对路径的基准根目录为：
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.24765951722449525041231702089526:50001231000000:2800:16789BB14F1FEBAFE60DF9206B18A0589C7CF525585EB761591A7A3F4E298267.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-start110-history-V14
爬取时间: 2025-04-30 23:51:39
来源: Huawei Developer
启动ohpm-repo服务。
命令格式
功能描述
用于启动ohpm-repo服务，创建一个ohpm-repo实例。
-  第一次启动ohpm-repo后，ohpm-repo工具目录下生成 .deploy_root 文件。如果后续您想更改部署路径，可以先删除 .deploy_root 文件，并在start 命令后面配置 config、crypto_path、deploy_root 参数。
-  如果首次启动停止后，再次启动，指定了 config、crypto_path、deploy_root参数，则参数会直接被忽略，默认根据 .deploy_root 文件记录的部署根目录去加载配置和加密组件。
选项
listen
您可以在 start 命令后面配置 --listen <string> 参数，指定启动端口和绑定访问地址，优先级高于 config.yaml中 listen 的配置。listen 参数可以指定协议 http 或者 https，若指定为 https，config.yaml文件中必须配置证书。若不指定，默认为 http。
config
-  <binary_root>：ohpm-repo 私仓工具包解压目录。
您可以在 start 命令后面配置 --config <string> 参数，指定配置文件路径。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。
执行 start 过程中，会把读取到的配置文件拷贝至路径 <deploy_root>/conf/config.yaml 内。
crypto_path
您可以在 start 命令后面配置 --crypto_path <string>参数，指定ohpm-repo运行时使用的加密组件。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。如果不配置crypto_path，当 <deploy_root>/meta 路径下不存在加密组件时，会自动生成新的加密组件。
执行 start 过程中，会把读取到的加密组件拷贝至路径 <deploy_root>/meta 内，不配置该参数，新建的加密组件也会保存在此处。
deploy_root
您可以在 start 命令后面配置 --deploy_root <string> 参数，指定ohpm-repo部署的根目录。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.23884131673900365631744839997031:50001231000000:2800:B60B72B06384902C2A56E5D9DACE70ABECCF3A96B2EE68B875BA75665DBEE0DB.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restart-history-V14
爬取时间: 2025-04-30 23:52:12
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restart101-history-V14
爬取时间: 2025-04-30 23:52:46
来源: Huawei Developer
重新启动ohpm-repo服务。
命令格式
功能描述
停止当前运行时的ohpm-repo服务，重新启动一个新的ohpm-repo服务。
选项
listen
您可以在 restart 命令后面配置 --listen <string> 参数，指定启动端口和绑定访问地址，优先级高于 config.yaml中 listen 的配置。listen 参数可以指定协议 http 或者 https，若指定为 https，config.yaml文件中必须配置证书。若不指定，默认为 http。
config
-  <binary_root>：ohpm-repo 项目根目录
-  类型： String
您可以在 restart 命令后面配置 --config 参数，指定配置文件路径，仅支持绝对路径配置。
执行 restart 过程中，会把读取到的配置文件拷贝至相对路径 /conf/config.yaml 内。
其中相对路径的根目录为：
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150824.38821178040381746990450551672458:50001231000000:2800:2AB938C553C1B6374F30779C7EB8E60D909BD7307F081C2763C2BFAB33704E26.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restart110-history-V14
爬取时间: 2025-04-30 23:53:20
来源: Huawei Developer
重新启动ohpm-repo服务。
命令格式
功能描述
停止当前运行时的ohpm-repo服务，重新启动一个新的ohpm-repo服务。
说明：
-  如果ohpm-repo已经启动过，再次执行 restart 重启，指定的 config、crypto_path 和deploy_root参数会被直接忽略，默认根据 .deploy_root 文件记录的部署目录去加载配置和加密组件。
选项
listen
您可以在 restart 命令后面配置 --listen <string> 参数，指定启动端口和绑定访问地址，优先级高于 config.yaml中 listen 的配置。listen 参数可以指定协议 http 或者 https，若指定为 https，config.yaml文件中必须配置证书。若不指定，默认为 http。
config
-  <binary_root>：ohpm-repo 私仓工具包解压目录。
-  类型： String
您可以在 restart 命令后面配置 --config <string> 参数，指定配置文件路径。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。
执行 start 过程中，会把读取到的配置文件拷贝至路径 <deploy_root>/conf/config.yaml 内。
crypto_path
您可以在 restart 命令后面配置 --crypto_path <string>参数，指定ohpm-repo运行时使用的加密组件。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。如果不配置crypto_path，当<deploy_root>/meta 路径下不存在加密组件时，会自动生成新的加密组件。
执行 start 过程中，会把读取到的加密组件拷贝至路径 <deploy_root>/meta 内，不配置该参数，新建的加密组件也会保存在此处。
deploy_root
您可以在 restart 命令后面配置 --deploy_root <string> 参数，指定ohpm-repo部署的根目录。支持相对和绝对路径配置，当配置为相对路径时，则以当前命令行工作路径作为根目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.77528182561740632162699268450277:50001231000000:2800:E52977C9917613E2E76EF57CE60E134FF450A930634DCBE8B39C847A6A861296.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-stop-history-V14
爬取时间: 2025-04-30 23:53:54
来源: Huawei Developer
停止ohpm-repo实例。
命令格式
功能描述
用于停止ohpm-repo实例。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.37895945960052545161558616840153:50001231000000:2800:99578CE4977B9BD20730BD200EED8B2776FA5FBED3BDD871220A39D74DA5FC3B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-version-history-V14
爬取时间: 2025-04-30 23:54:27
来源: Huawei Developer
查询ohpm-repo版本。
命令格式
功能描述
打印ohpm-repo的版本号。
可在执行setup安装脚本后，对安装版本信息进行校验。
示例
执行以下命令，查看版本信息：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.60298709788234076341130040299504:50001231000000:2800:F9B2E015FD57694FB2A132B246E295C0ECED7A2AFB236FD95121C2B90722B1EB.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-encrypt-history-V14
爬取时间: 2025-04-30 23:55:01
来源: Huawei Developer
加密明文密码。
命令格式
功能描述
使用指定的加密组件加密从标准输入读取的数据，并在标准输出中输出密文。
选项
crypto_path
您必须在 encrypt_password 命令后面配置 --crypto_path <string>参数，指定加密组件的路径。如果是完整组件，将用该组件去加密明文密码。如果是一个空目录，则命令将生成新的加密组件并加密明文密码。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.57485963524455732260787980663904:50001231000000:2800:AFCCE5C9282945244DB079D10FC67924A6F6F4738A249192E45F32DB3772145B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-pack-history-V14
爬取时间: 2025-04-30 23:55:35
来源: Huawei Developer
打包ohpm-repo部署根目录文件。
说明：ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
用于打包ohpm-repo<deploy_root>目录下的 conf ，db 和 meta 目录。
参数
<deploy_root>
您必须在 pack 命令后面配置 <deploy_root> 参数，指定待打包的ohpm-repo部署根目录。
启动ohpm-repo成功后，可以通过查看 ohpm-repo 工具中生成的 .deploy_root 文件查看部署根目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.30727628775238648591897522331792:50001231000000:2800:8547D06FFB20BA891A55B92574EB17661F30EE9EB9DFCB08F7FD32470132FD2E.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-restore-history-V14
爬取时间: 2025-04-30 23:56:10
来源: Huawei Developer
将 ohpm-repo pack 打包产物替换到 <deploy_root> 目录下相应文件，重启服务。
ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
该命令会停止当前ohpm-repo服务，并用打包文件 <file_path> 中的内容替换ohpm-repo部署根目录 <deploy_root> 的相应文件，然后重启ohpm-repo服务。该命令执行前必须已经执行过ohpm-repo实例启动命令 ohpm-repo start。
-  支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
-  首次启动ohpm-repo实例后，会在ohpm-repo工具根目录中生成 .deploy_root 文件，其记录的是<deploy_root>，会自动读取识别，无需在命令中指定 <deploy_root> 路径。
参数
<file_path>
指定待解压的打包文件路径。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.25708759236248132224078844921933:50001231000000:2800:CA03D2D63BC561B5C0695DB84FDFDE65998D074A6C3A6A4A1B94F9277C543303.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-deploy-history-V14
爬取时间: 2025-04-30 23:56:43
来源: Huawei Developer
使用备份文件部署新的ohpm-repo实例。
ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
参数
<file_path>
您必须在 deploy 命令后面配置 <file_path> 参数，指定打包产物路径。
选项
deploy_root
您可以在 deploy 命令后面配置 --deploy_root <string> 参数，指定新的ohpm-repo部署根目录。支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
logs
您可以在 deploy 命令后面配置 --logs <string> 参数，指定 log 目录，优先级高于 config.yaml 中的 logs 配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
uplink
您可以在 deploy 命令后面配置 --uplink <string> 参数，指定远程包缓存路径，优先级高于 config.yaml 中 uplink.store_path 的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。
示例
执行以下命令：
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150825.18445473548857430630361752616554:50001231000000:2800:4074C1C56595068B79A6D7CF2FC5788F49AEC76A000D1C6B51B15FAEED00FD63.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-checkstorage-history-V14
爬取时间: 2025-04-30 23:57:17
来源: Huawei Developer
检查 sftp 中存储包的完整性。
ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
命令根据元数据检查 sftp 存储的包是否存在且完整。该命令要求文件存储模块必须配置为 ohpm-repo-plugin-sftp。
参数
<target>
您必须在 check_storage 命令后面配置 <target> 参数，指定要检查的包或者用 @all 指定检查所有包。
选项
failed
您可以在 check_storage 命令后面配置 --failed 选项 ，则只检查在下载错误日志中未被处理的且满足<target>条件的包。
示例
执行以下命令，检查包 @ohos/axios@2.0.3 的完整性：
检查 @ohos/axios@2.0.3 包在所有 sftp 存储目录中的完整性。
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.98217897505401988063961243058314:50001231000000:2800:B168CD1FE6C7CC44F76D740D7B3BD50EBFDDB4B2A91F182618472444CEBB18EC.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-mirrorstorage-history-V14
爬取时间: 2025-04-30 23:57:51
来源: Huawei Developer
同步 sftp 存储的包。
ohpm-repo 1.1.0 版本开始支持此命令。
命令格式
功能描述
该命令要求配置文件中文件存储必须为 ohpm-repo-plugin-sftp。命令会将源sftp目录下满足 <target> 条件的包同步到目标sftp目录下。
参数
<source_sftp>
您必须在 mirror_storage 命令后面配置 <source_sftp> 参数 ，指定源sftp配置的名字。
<target_sftp>
您必须在 mirror_storage 命令后面配置 <target_sftp> 参数 ，指定目标sftp配置的名字。
<target>
您必须在 mirror_storage 命令后配置 <target> 参数，指定满足条件的包；或使用 @all 指定所有包。
选项
failed
您可以在 mirror_storage 命令后面配置 --failed 选项，则只同步在下载错误日志中未被处理的且满足<target>条件的包，如果同步成功，则相应的错误日志会被设置成 handled。
示例
执行以下命令，同步包 @ohos/axios@2.0.3：
将名为 test_one_sftp 的 sftp 目录中 @ohos/axios@2.0.3 包同步到名为 test_two_sftp 的sftp目录中。
结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.97901108561351255269127914693378:50001231000000:2800:FE29ED9F0FEA7916B36CCA8D51A54018B021E9C887DF77F8C869C358F510B77A.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-deploy-guide-history-V14
爬取时间: 2025-04-30 23:58:25
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-deploy-single-history-V14
爬取时间: 2025-04-30 23:58:59
来源: Huawei Developer
安装ohpm-repo工具
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.31003364800872240447017035551719:50001231000000:2800:F240D6464ADE55086C03CD1FD390C083B0E95EBE1FA0A0FCD7DFF7D0B8CF455F.png?needInitFileName=true?needInitFileName=true)
若您想在其他目录使用 ohpm-repo，请将 bin 目录路径配置到系统环境变量 path 中。
启动ohpm-repo
1.  设置数据存储 db 模块。 设置文件存储 store 模块。
2.  设置数据存储 db 模块。
3.  设置文件存储 store 模块。
-  设置数据存储 db 模块。
-  设置文件存储 store 模块。
1.  1.0.1 版本和 1.1.0 版本启动ohpm-repo存在不同，其中 1.1.0 版本支持指定ohpm-repo部署根目录 执行以下命令，其中 config： 指定启动时使用的配置文件。 结果示例： 执行以下命令： 结果示例：
2.  执行以下命令，其中 config： 指定启动时使用的配置文件。 结果示例：
3.  执行以下命令： 结果示例：
-  执行以下命令，其中 config： 指定启动时使用的配置文件。 结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.28859140398015827843885519148887:50001231000000:2800:C5F7F61F96C5CAB1BA132D452830C6F25D96F26C4D2AA3929B3C8BE5A9DB617C.png?needInitFileName=true?needInitFileName=true)
-  执行以下命令： 结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.06057049526132527278730666514558:50001231000000:2800:73BFCA394712BF8A7453B8E55439480C0644E4968181108EF931488620E59C35.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-multi-deploy-history-V14
爬取时间: 2025-04-30 23:59:35
来源: Huawei Developer
从 1.1.0 开始支持多实例部署。
环境准备
1、准备 mysql 数据库服务；
2、准备至少一个 sftp 存储服务，ohpm-repo 最大支持连接3个 sftp 服务；
3、安装 node.js 16.x 及以上版本。
安装ohpm-repo工具1.1.0
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150826.90484708777376333619532666670861:50001231000000:2800:0867B8A36D7BF8FA79CE2B1D2E2919045AFD03905761C9ED1B1485D19175244E.png?needInitFileName=true?needInitFileName=true)
若您想在其他目录使用 ohpm-repo，请将 bin 目录路径配置到系统环境变量 path 中。
多实例配置
1.  --crypto_path 参数用于指定加密组件，如果您是第一次执行该命令，可以指定一个空目录，在加密后会生成新的加密组件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.59444336135670451108412907613538:50001231000000:2800:550A22A345C4CC9104F1C6F77B11949293BCD1B7828B516CEAD9944BF67CE488.png?needInitFileName=true?needInitFileName=true)
1.  设置数据存储 db 模块。 设置文件存储 store 模块，sftp配置最多只能设置3个。
2.  设置数据存储 db 模块。
3.  设置文件存储 store 模块，sftp配置最多只能设置3个。
-  设置数据存储 db 模块。
-  设置文件存储 store 模块，sftp配置最多只能设置3个。
部署首个节点
进入 bin 目录，命令行启动ohpm-repo。
启动成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.91529266081511317030921930473385:50001231000000:2800:FBB681FEF1C5AF431AFC3D293F359A9D712EECF62B09425552AD56310610CD4B.png?needInitFileName=true?needInitFileName=true)
打包和部署
为帮助您更方便地完成多实例部署，为您提供打包、部署命令。
打包
在完成了多实例配置并首次启动过ohpm-repo服务实例的机器上，执行 ohpm-repo pack <deploy_root>。
该命令用来打包备份ohpm-repo的 <deploy_root>/conf， <deploy_root>/meta 目录，并在命令行工作目录下生成压缩包。
打包成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.28800889565756004887826975391521:50001231000000:2800:39CF06D43BCBD346566C8127C474559E4255ED4E86E6EC577299676A2529159D.png?needInitFileName=true?needInitFileName=true)
部署
将 pack 命令的产物拷贝到其他机器中。
在安装私仓工具后，使用 ohpm-repo deploy <file_path> --deploy_root <deploy_root> 命令部署新的实例；
部署成功日志信息如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.72903684188265576510153789016441:50001231000000:2800:258A1972BE1A4B2F29E61222FBE7C1FCE02749B9515216B8C3D7C9A185453078.png?needInitFileName=true?needInitFileName=true)
部署成功后可执行 ohpm-repo start 启动ohpm-repo。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.13490585232329922420105128209620:50001231000000:2800:1524A186CFC515C788C632B13CA3A738942A34BF16AA191EF0C821309491A3D9.png?needInitFileName=true?needInitFileName=true)
配置自动重启（可选）
为ohpm-repo实例配置系统重启时自动重启的功能。
在进行该配置前需要将 ohpm-repo 工具 bin 目录配置到环境变量path中。
Linux
1.  当 mysql 或 sftp 服务与 ohpm-repo 部署在同一服务器上时，请将 mysql 和 sftp 的启动命令放在 ohpm-repo start 命令之前。
2.  其中 run-repo.sh 表示要执行的脚本路径；>/dev/null 2>&1 表示将输出重定向到空设备，即不输出任何信息。
```typescript
@reboot /bin/sh run-repo.sh >/dev/null 2>&1
```
现在，每次系统启动时，都会自动执行 run-repo.sh 脚本中的命令。
Windows
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.24952377505033212029540372032987:50001231000000:2800:1D628A9AE9014F9CF920CB9D06E6B818EB0137F6C70F564C09CB26E23B881236.png?needInitFileName=true?needInitFileName=true)
现在，每次系统启动时，都会自动执行 run-repo.bat 脚本中的命令。

# 合并文件
合并时间: 2025-05-01 07:31:54

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-data-migration-V14
爬取时间: 2025-05-01 00:00:08
来源: Huawei Developer
ohpm-repo2.2.0版本开始支持数据迁移功能。在ohpm-repo 配置文件中，db是元数据存储的配置项，store是文件存储的配置项，db和store不能随意搭配，需要符合下面表格中的匹配规范。如果需要改变db和store的存储方式，需要进行数据迁移操作。
| db：元数据存储  | 与db所适配的store：三方包文件存储  |
| --- | --- |
| filedb  | file storage  |
| mysql(ohpm-repo 1.1.0开始支持）  | file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持）  |
db：元数据存储
与db所适配的store：三方包文件存储
filedb
file storage
mysql(ohpm-repo 1.1.0开始支持）
file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持）
简要流程
为保证数据不丢失，请在数据迁移前务必进行数据的备份；启动ohpm-repo，使用迁移命令导出数据；修改配置文件中db和store的存储方式，以新存储方式启动ohpm-repo；使用迁移命令导入数据。
如果您当前使用的ohpm-repo版本不支持您所需要的存储方式，请参考升级指导文档，进行ohpm-repo的升级。
备份ohpm-repo数据
请参考数据备份指导文档进行操作。
使用迁移命令导出数据
1.  使用export_userinfo命令导出下面九个数据表的数据，并且导出加密组件，在命令执行目录生成打包export_userInfo_xxx.zip 文件。 user group groupmember publickey access_token uplink uplinkproxy repo
2.
3.  使用batch_download命令，从ohpm-repo配置的store存储目录中批量下载包文件。 使用第2步生成的 pkgInfo_xxxx.json 作为batch_download命令参数，批量下载har或tgz包，在命令执行目录生成 batch_download_xxx.zip 文件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.59175069315659903294004522649041:50001231000000:2800:66D21FEEFF0F731E34BD2B95BEE4AFFD517743AEB159BE79DC55E6503DA1970A.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.77185951925010000068855019173250:50001231000000:2800:FC74F5BA8C85AD7A03B305A838F3B08E0E93DC462F8F76008FCC948FE79F53A1.png?needInitFileName=true?needInitFileName=true)
如果不迁移所有的包，您可以在第2步生成的pkgInfo_xxxx.json文件中删除掉不需要下载的包。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150827.29282909116656857550895157970742:50001231000000:2800:9BFD1E1E914B15D8E103B16A8628FABC903B58D614E95A7BC0509955B7849CE5.png?needInitFileName=true?needInitFileName=true)
batch_download_xxx.zip 文件中存在 pkgInfo.json 文件，其中记录了每个包的 文件名、组织、上传者，用于在批量上传时准确指定发包来源。
新存储方式重启ohpm-repo
打开ohpm-repo压缩包解压根目录中配置文件config.yaml，修改db和store配置项，指定所需存储方式。
修改db和store配置项后，需要您在配置文件中同时配置新的<deploy_root>目录。
使用修改后的配置文件重新执行安装命令（这一步必须执行，初始化数据库和其他必要的配置）
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.22417245715876305905864328273987:50001231000000:2800:B12013007B52EA6AEFF9047F13BF684037C20438CFEF2B5B70297C5205C8206B.png?needInitFileName=true?needInitFileName=true)
根据提示信息刷新环境变量，然后重新启动ohpm-repo
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.13873061698911427177311880713323:50001231000000:2800:C8CD03D6DCA2F743D147D0EF5AD356F5360E7A38DE239F583E69C524452188CD.png?needInitFileName=true?needInitFileName=true)
使用迁移命令导入数据
1.  使用import_userinfo命令将export_userInfo_xxx.zip中的数据导入数据库。 所有数据导入成功后，可登录ohpm-repo管理网页进行验证。
2.  使用batch_publish命令，将批量下载生成的 batch_download_xxx.zip 中的包依次发布到ohpm-repo。 所有包发布成功。进入ohpm-repo网站查看包数量和包详情是否正确。 在batch_publish命令后面可以配置--force，如果进行批量上传时某个包的组织在ohpm-repo中不存在，将任意选取ohpm-repo中一位管理员用户作为组织负责人，自动创建组织。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.80159031642296882112937182165201:50001231000000:2800:4FB94471F11044037E236E7439E7647031F4AC6E6C360E1682EB3E7D4C458033.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.07128017668720613920409992053298:50001231000000:2800:5A2CDE836F9804F83F9799D08DACC17E3B1561D57F2309165FA09FD4D081FFE0.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.71531109212604567237140603014239:50001231000000:2800:D0D7C1E68553C88FB11617CAD5A62A5DE3663D538F63013C39199E5309361DD1.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.48636690914754265353749790693417:50001231000000:2800:0AB51E8CE40FFDD1F00521008959B6BCFA22B5E6937D57A16D56644161D89188.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-upgrade-V14
爬取时间: 2025-05-01 00:00:43
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-upgrade-101_to_110-V14
爬取时间: 2025-05-01 00:01:17
来源: Huawei Developer
在升级之前，请务必备份好 ohpm-repo 私仓工具中的的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括：<deploy_root>ohpm-repo部署根目录内数据，db元数据和store三方包数据，详细步骤可参考数据备份。
1.  旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.0.1 版本 ohpm-repo 私仓工具包解压目录下的 bin 目录，执行 stop。 若您想在其他目录使用 ohpm-repo，请将对应版本 ohpm-repo 工具包解压目录中 bin 目录的路径配置到系统环境变量 path 中。
2.  下载并解压工具包：下载版本 1.1.0 的 ohpm-repo 包，并解压（请解压到一个空文件夹中）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.89026411986807045756060967916057:50001231000000:2800:EC3EDECB0003332AF07F3DD4B9F286E29AFBB22D81BC330CF8AB88E7A82D79F1.png?needInitFileName=true?needInitFileName=true)
1.  安装完成之后，进入ohpm-repo 私仓工具包解压目录下的 bin 目录，执行如下命令： 终端输出为版本号（如：1.1.0），则表示解压成功。
2.  移植配置文件信息：新版本 1.1.0 的配置文件与旧版本 1.0.1相比差异不大，可直接拷贝旧版本中的配置文件有效信息至新版本配置文件中。 可直接拷贝旧版本中的listen， https， server， db， store 和 uplink 等信息至新版本配置文件对应位置；新版本中的 logs_path 和 loglevel 参数可直接使用默认值，不做修改。 如果ohpm-repo版本1.0.1使用的配置文件，配置项均为默认项，则无需移植配置文件信息，直接执行下一步启动操作。
3.  结果示例：
4.  版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.96079913883674740287757438719621:50001231000000:2800:5AD524ED8AF00810AE01F1CE299981BB2142F7630FC0234F947A97422BA43A0E.png?needInitFileName=true?needInitFileName=true)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150828.06864233975962006462809638321901:50001231000000:2800:97AD7B6907FA432DF913100CDD9593CA36FAD42FE8659B5AA231AA217F47D8A8.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-upgrade-101_to_2xx-V14
爬取时间: 2025-05-01 00:01:51
来源: Huawei Developer
升级至2.X.X版本与升级至5.X.X版本步骤一致，本文以升级至2.X.X版本为例。
在升级之前，请务必备份好ohpm-repo 私仓工具中的的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括：<deploy_root>私仓部署根目录内数据，db元数据和store三方包数据，详细步骤可参考数据备份。
1.  旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.0.1 版本 ohpm-repo 私仓工具包解压目录下的 bin 目录，执行 stop 若您想在其他目录使用 ohpm-repo，请将对应版本 ohpm-repo 工具包解压目录中 bin 目录的路径配置到系统环境变量 path 中。
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.61953158226333113939223520867575:50001231000000:2800:435C5ACBA98F8D101E12D7B0576E83625D10077B7BC2B5411F10FEE482F6EA9E.png?needInitFileName=true?needInitFileName=true)
1.  终端输出版本号 2.X.X，则表示解压成功。
1.  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
2.  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
3.  在使用新部署目录时，旧版本部署目录中meta文件一定要迁移到新版本部署目录中，否则使用meta加密组件加密的数据无法被正确解密。
4.  结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
5.  结果示例：
6.  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
7.  Window 系统： 关闭当前窗口，重新开启一个窗口
8.  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
9.  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
-  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
-  结果示例：
-  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
-  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.94070602754015893465524469133693:50001231000000:2800:8F66D60FAC789D3C091631410A8AE187F4B070FF79EA28C0EC89FB897F4D8E77.png?needInitFileName=true?needInitFileName=true)
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 .~/.bashrc。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.94597753034437090164662592434192:50001231000000:2800:D8F7DB480D23E25CE18EDD0AFED696C89F7AD2057766B5699B3EC144221ABC9B.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-upgrade-110_to_2xx-V14
爬取时间: 2025-05-01 00:02:25
来源: Huawei Developer
升级至2.X.X版本与升级至5.X.X版本步骤一致，本文以升级至2.X.X版本为例。
在升级之前，请务必备份好 ohpm-repo 私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括：<deploy_root>ohpm-repo部署根目录内数据，db元数据和store三方包数据，详细步骤可参考数据备份。
1.  旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.1.0 版本 ohpm-repo 私仓工具包解压目录下的 bin 目录，执行 stop
1.
2.  安装完成之后，进入ohpm-repo 私仓工具包解压目录下的 bin 目录，执行如下命令： 终端输出为版本号 2.X.X，则表示解压成功。
3.  移植配置文件信息：版本 2.X.X 的配置文件与版本 1.1.0 相比有较大差异，需要提取旧版本配置文件信息至新版本配置文件中，移植的具体内容如下： 如果 1.1.0  版本ohpm-repo的部署目录 deploy_root 使用的是默认路径，即可省略此操作。 在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。 新版本配置文件还添加了很多信息的配置，例如deploy_root和logs_path等，此类信息在升级过程中可不改变，使用默认项。
4.  如果 1.1.0  版本ohpm-repo的部署目录 deploy_root 使用的是默认路径，即可省略此操作。
5.  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
6.  在使用新部署目录时，旧版本的部署目录中meta文件一定要迁移到新版本部署目录中，否则使用meta加密组件加密的数据无法被正确解密。
7.  新版本服务启动：正确拷贝替换配置文件信息后，进入ohpm-repo 私仓工具包解压目录下的 bin 目录，执行以下命令启动新版本ohpm-repo服务： 结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。 结果示例：
8.  结果示例：
9.  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
10.  Window 系统： 关闭当前窗口，重新开启一个窗口
11.  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
12.  结果示例：
13.  在多实例部署中，可先升级一台机器，然后拷贝其配置文件到其他机器中进行快速升级，具体步骤如下 该方法要求部署的多实例机器之间，使用的配置文件除根目录 deploy_root 外，其他配置项必须完全相同。 若您想在其他目录使用 ohpm-repo，请将对应版本ohpm-repo根目录中 bin 目录的路径配置到系统环境变量 path 中。 终端输出为版本号2.0.0，则表示安装成功。 结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
14.  若您想在其他目录使用 ohpm-repo，请将对应版本ohpm-repo根目录中 bin 目录的路径配置到系统环境变量 path 中。
15.
16.  终端输出为版本号2.0.0，则表示安装成功。
17.  结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
18.  结果示例：
19.  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
20.  Window 系统： 关闭当前窗口，重新开启一个窗口
21.  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
22.  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.04674863425710531739845174791599:50001231000000:2800:2111D432146F39075F3DE26CA3FFECC021A745213AA60EB78DB2ABEB5DC0C88A.png?needInitFileName=true?needInitFileName=true)
-  如果 1.1.0  版本ohpm-repo的部署目录 deploy_root 使用的是默认路径，即可省略此操作。
-  在ohpm-repo 2.0.0 版本中，listen 的默认值已更改为listen: 0.0.0.0:8088，如果 listen 的 host 配置为 0.0.0.0，则字段 store.config.server 不可省略，必须配置为详细地址，例如http://localhost:8088。
-  结果示例：
-  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
-  结果示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150829.32036157558708426692307178951240:50001231000000:2800:0B18735416430727C5B1F1E9BD5A585FD7A0A811F946BE56E447641B977F2A22.png?needInitFileName=true?needInitFileName=true)
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.82914000579436934517902771962314:50001231000000:2800:F783C3379F93173AD63BCCF01A4BCD37603A59C5CC62BA04CE8C8445A4914035.png?needInitFileName=true?needInitFileName=true)
-  若您想在其他目录使用 ohpm-repo，请将对应版本ohpm-repo根目录中 bin 目录的路径配置到系统环境变量 path 中。
-
-  终端输出为版本号2.0.0，则表示安装成功。
-  结果示例： Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
-  结果示例：
-  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
-  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.34176686661052547979305463707720:50001231000000:2800:664ABC0D4B9D532041FEEAC0274F7B60A4952B543D142C003D726946393737B6.png?needInitFileName=true?needInitFileName=true)
1.  结果示例：
2.  Window 系统： 关闭当前窗口，重新开启一个窗口 Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
3.  Window 系统： 关闭当前窗口，重新开启一个窗口
4.  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
5.  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.23455539467578368556581869521479:50001231000000:2800:BBB65D792E1984766CFA3D943279D772D0968501DCD2E7C1B5EDD596D335D085.png?needInitFileName=true?needInitFileName=true)
-  Window 系统： 关闭当前窗口，重新开启一个窗口
-  Linux 系统或 Mac 系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.24964762217483858425613674344270:50001231000000:2800:C120BB1DA856193CA0A967C83DDC440C31427FBA8E211505607EB399619544A9.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-upgrade-2xx_to_2xx-V14
爬取时间: 2025-05-01 00:02:59
来源: Huawei Developer
如需将ohpm-repo版本2.X.X/5.X.X版本升级到更高的2.X.X/5.X.X版本，可参考此文档。
1. 在升级之前，请务必备份好ohpm-repo私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括：<deploy_root>ohpm-repo部署根目录内数据，db元数据和store三方包数据，详细步骤可参考数据备份。
2. 如果您想要改变db元数据和store三方包的存储方式，可在正确升级后参考数据迁移文档指导修改。
1.
2.
3.  终端输出为新版本的版本号，则表示解压成功。
4.
5.  在使用新部署目录时，旧版本的部署目录中meta文件必须要迁移到新版本部署目录中，否则将导致使用meta加密组件加密的数据无法被正确解密。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.71796581606257948523557094028293:50001231000000:2800:81AECB32BCC59A6AE805C24007E0FD8060C6B43EFFC69CD8D9567960BC3CCAF5.png?needInitFileName=true?needInitFileName=true)
1.  结果示例： Window系统： 关闭当前窗口，重新开启一个窗口。 Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。 结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
2.  结果示例：
3.  Window系统： 关闭当前窗口，重新开启一个窗口。 Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
4.  Window系统： 关闭当前窗口，重新开启一个窗口。
5.  Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
6.  5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ；
7.  5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
8.  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
-  结果示例：
-  Window系统： 关闭当前窗口，重新开启一个窗口。 Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  Window系统： 关闭当前窗口，重新开启一个窗口。
-  Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ；
-  5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  结果示例： 版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.91573063780917727932475722179425:50001231000000:2800:58D8EA4E9A5805DAAF5A871E041FCFD502CC12C4C8AE4F910568C4073BDA0B00.png?needInitFileName=true?needInitFileName=true)
-  Window系统： 关闭当前窗口，重新开启一个窗口。
-  Linux/Mac系统： 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ； 5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ；
-  5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
-  5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc ；
-  5.0.1及以后版本： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者 .~/.bashrc；当shell为zsh时执行source ~/.zshrc或者 .~/.zshrc。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150830.56942355866896389333990280955502:50001231000000:2800:4FF20902A75FA29B0A2100547F8468F28ADC7317080D9C06B8AF46101AD7EAFF.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-storageplugin-V14
爬取时间: 2025-05-01 00:03:33
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-plugin-configuration-V14
爬取时间: 2025-05-01 00:04:07
来源: Huawei Developer
ohpm-repo 从2.2.0版本开始支持自定义存储插件（需要配套使用1.7.0及以上版本ohpm命令行工具），允许您开发定制化的存储插件来对接您自己的存储系统，您希望将ohpm-repo下的三方包文件存储在华为云OBS或者其他云储存平台，可以按照如下步骤来实现自定义存储插件。
当您使用自定义认证插件对接自己的存储系统时，如果存在网络通信，建议使用https协议，确保信息安全传输。
准备工作
编辑CustomStorage.ts文件，实现存储插件接口 StoragePlugin
接口类StoragePlugin中包含如下五个函数，需要在实现类中完成功能的实现。
1.  init 实现初始化准备工作。在配置文件 config.yaml 中 store.config 处可自定义一些插件所需要的参数信息，可通过函数 getStorageConfigInfo() 读取配置文件中自定义的参数信息。
2.  save 实现本地文件的上传功能。返回值为一个字符串，能够标识所上传的文件。函数入参为上传文件的本地路径srcPath和待上传包的详细信息packageInfo，packageInfo为可选项。 在实现save方法的时候，上传每一个三方包有四个文件待上传：<package_name>.har包文件，metadata.json文件，readme.md和changelog.md文件。由于后面三个文件在每个三方包中名称都相同，请存放在不同位置或者使用不同文件名存储，避免文件被覆盖。
3.  delete 实现已上传文件的删除功能。函数入参为savedResponse：上传文件 save 后的返回信息，通过入参信息定位已上传文件，进行文件的删除；返回值信息为删除的结果，布尔类型。
4.  实现已上传文件的内容读取功能。函数入参为savedResponse：上传文件save后的返回信息，通过入参信息定位已上传文件，进行文件内容读取；返回所读取到的文件信息，数据类型为 Buffer。
5.  getDownloadUrl 实现已上传文件下载URL的获取。函数入参为savedResponse：上传文件save后的返回信息，通过入参信息定位已上传文件，进行文件内容读取；返回所读取到文件的下载URL，数据类型为 string。
使用插件文件和启动ohpm-repo
1.  安装 typescript 包，编译 ts 文件为 js 文件。
2.  编译插件文件 如果 CustomStorage.ts 没有存放在 plugins 内，请先修改tsconfig.json文件 include 和 outDir 参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。
3.  如果 CustomStorage.ts 没有存放在 plugins 内，请先修改tsconfig.json文件 include 和 outDir 参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。
4.  编译后文件存放指定位置 编译后获得的 CustomStorage.js 需要与 CustomStorage.ts 保持在同一级目录中，否则会编译出错，默认输出在./plugins/outDir 内，需要把 CustomStorage.js 拷贝到 CustomStorage.ts 同级目录./plugins 中（ohpm-repo成功启动后可删除CustomStorage.ts文件）。
5.  编辑配置文件 为了保证ohpm-repo能够正确加载自定义存储插件，需要修改配置文件 config.yaml，主要涉及 store 处内容修改。 参数说明：
6.  ohpm-repo 服务部署 在完成上述操作之后，按照ohpm-repo部署指导，完成服务部署。
-  如果 CustomStorage.ts 没有存放在 plugins 内，请先修改tsconfig.json文件 include 和 outDir 参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-template-file-V14
爬取时间: 2025-05-01 00:04:41
来源: Huawei Developer
模板文件中包含自定义storage插件需要的两个文件：CustomStorage.ts和tsconfig.json。
插件模板CustomStorage.ts
```typescript
import {StoragePlugin} from '../libs/plugins/storage/customStorage/StoragePlugin';  // 插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），StoragePlugin接口类的默认引用地址
import {getStorageConfigInfo} from '../libs/common/getStorageConfigInfo';           // 插件文件CustomStorage.ts存储在默认位置（ohpm-repo解压根目录的plugins文件夹内），getStorageConfigInfo方法的默认引用地址
export class CustomStorage implements StoragePlugin {
async init(): Promise<void>{
// 配置文件中 store 项格式参考
// store:
//   type: custom    // store 存储类型为 custom，即用户自定义
//   config:         // 配置信息：export_name和plugin_path 是必选配置项
//     export_name: ExampleDemo          // 插件类的名字：例如 ExampleDemo
//     plugin_path: ../plugins/storage/customStorage/ExampleDemo.js    // 插件文件的存放位置
//     configInfo1: "info1";             // 自定义配置信息（可选项）
//     configInfo2: "info2";             // 自定义配置信息（可选项）
//     ...
// 通过函数 getStorageConfigInfo() 可以获取到配置文件config.yaml中store.config处自定义配置的信息
const configStorageInfo = await getStorageConfigInfo();
//举例说明：当配置文件 store.config处定义 configInfo1和 configInfo2信息，可读取
const configInfo1 = configStorageInfo.configInfo1 as string; //获取到configInfo1的值为 "info1"
const configInfo2 = configStorageInfo.configInfo2 as string; //获取到configInfo2的值为: "info2"
};
/**
* 通过文件的本地路径，把数据保存到指定的 storage 内
* @param srcPath： 上传文件的本地路径
* @param packageInfo: 可选参数，待上传包的详细信息，包含包名（含组织名）和包版本号两部分，包名：packageInfo.packageName，包版本：packageInfo.version.
* @returns 上传文件 save 后的返回信息： 能够标识文件，方便文件删除和读取
*/
async save(srcPath: string, packageInfo: any): Promise<string>{
let savedResponse: string;
return savedResponse;
};
/** 通过上传文件获得的返回信息，定位文件，进行文件的删除，返回删除结果
* @param savedResponse： 上传文件 save 后的返回信息
* @returns 删除的结果：true 表示删除成功
*/
async delete(savedResponse: string): Promise<boolean>{
let isDeleteSuccess: boolean;
return isDeleteSuccess;
};
/**
* 过上传文件获得的返回信息，定位文件，进行获取文件内容，数据格式为 Buffer
* @param savedResponse 上传文件 save 后的返回信息
* @returns 获取文件的内容，数据格式为 Buffer
*/
async download(savedResponse: string): Promise<Buffer>{
let fileContent: Buffer;
return fileContent;
};
/**
* 根据保存文件生成的结果字符串，获取文件下载url
* @param savedResponse 保存文件的结果字符串
*/
async getDownloadUrl(savedResponse: string): Promise<string>{
let fileDownloadUrl: string;
return fileDownloadUrl;
};
}
```
ts编译的配置文件tsconfig.json

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-custom-auth-plugin-V14
爬取时间: 2025-05-01 00:05:16
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-custom-auth-plugin-configuration-V14
爬取时间: 2025-05-01 00:05:51
来源: Huawei Developer
ohpm-repo 从2.3.0版本开始支持自定义认证插件（需配套使用1.8.0及以上版本ohpm命令行工具），允许您使用AccessToken认证，开发定制化的认证插件来对接开发者自己的用户信息系统。
当您使用自定义认证插件对接自己的用户系统时，如果存在网络通信，建议使用https协议，确保信息安全传输。
准备工作
编辑CustomAuth.ts文件，实现认证插件接口AuthPlugin
打开 CustomAuth.ts 模板文件，需要编写代码实现接口类AuthPlugin，实现auth和getUserInfo两个基础方法，实现类 CustomAuth 的名字可自定义修改。
接口类AuthPlugin中包含如下三个方法，需要在实现类中完成功能的实现。
1.  通过读写AccessToken获取对应用户信息，函数的入参为读写AccessToken值，返回值有四个参数：用户的id值，用户的name值，用户所属于的组织列表belongGroupList，用户所管理的组织列表groupAdminList。
2.  通过只读AccessToken获取对应用户信息，函数的入参为只读AccessToken值，返回值有四个参数：用户的id值，用户的name值，用户所属于的组织列表belongGroupList，用户所管理的组织列表groupAdminList。当ohpm-repo配置不支持匿名访问时，ohpm可以通过配置只读AccessToken值，获取执行install，info和update命令的权限。
3.  实现根据用户id获取用户名字的功能。函数入参为用户的id值；返回值为用户的名字。
插件文件的使用和ohpm-repo的启动
1.
2.  如果CustomAuth.ts没有存放在ohpm-repo解压根目录的plugins 内，请先修改tsconfig.json 文件中include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。
3.  如果CustomAuth.ts没有存放在ohpm-repo解压根目录的plugins 内，请先修改tsconfig.json 文件中include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。
4.  编译后获得的CustomAuth.js 需要与CustomAuth.ts 保持在同一级目录中，否则会编译出错，默认输出在./plugins/outDir 内，需要把CustomAuth.js 拷贝到CustomAuth.ts同级目录./plugins 中（ohpm-repo成功启动后可删除CustomAuth.ts文件）。
5.  参数说明：
6.  当ohpm-repo 成功启动后，在ohpm客户端的配置文件.ohpmrc中新增一行（//是有效字符，不是注释，勿删）。 其中ip和port为ohpm-repo私仓启动机器所在的ip值和端口值；readOnlyToken/readWriteToken为用户信息系统内有效的只读/读写accessToken值，通过该accessToken值，用户调用自定义认证插件CustomAuth中auth和authWithReadOnly方法，能够获取到有效的用户信息。
-  如果CustomAuth.ts没有存放在ohpm-repo解压根目录的plugins 内，请先修改tsconfig.json 文件中include和outDir参数，前者指定待编译插件代码的存储目录，后者指定编译完成后文件的输出位置，然后再在ohpm-repo解压根目录执行编译命令tsc。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-custom-auth-plugin-template-V14
爬取时间: 2025-05-01 00:06:24
来源: Huawei Developer
模板文件中包含自定义auth插件需要的两个文件：CustomAuth.ts和tsconfig.json。
插件模板CustomAuth.ts
ts编译的配置文件tsconfig.json

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-data-backup-V14
爬取时间: 2025-05-01 00:06:58
来源: Huawei Developer
数据迁移或者版本升级之前请务必进行数据备份，以免重要数据丢失，无法回滚。备份的内容包括<deploy_root>ohpm-repo部署根目录内数据，db元数据和store三方包数据。
备份deploy_root部署根目录
<deploy_root>：ohpm-repo部署根目录，默认的路径为：
windows系统：~/AppData/Roaming/Huawei/ohpm-repo
其他操作系统：~/ohpm-repo
ohpm-repo在版本1.1.0之前不支持配置<deploy_root>，都采用默认值，若您的ohpm-repo支持且配置了<deploy_root>，请找到对应目录，并使用常用的压缩工具打包备份该目录。
如果配置文件中db，storage，logs 和 uplink的存储路径可配置，且存储位置不在ohpm-repo部署根目录<deploy_root>中，请找到对应目录进行数据备份。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150831.09000329974936460435591207732360:50001231000000:2800:F81CED96EF392EC16E460A8736D9726D462ABED680B95576DE415A4A7B321E4D.png?needInitFileName=true?needInitFileName=true)
备份<包存储目录>和<Mysql>
如果您使用的是本地存储（配置文件中db为filedb本地存储，store为fs本地存储），在备份<deploy_root>时已经完成db和store的备份，请忽略该步骤。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150831.33830202066272431657738050259782:50001231000000:2800:1E2EE27844607EAE16014DEDB9AC9AD7F0D863B0C7D8D9CF057E3F5F5BDD7FD6.png?needInitFileName=true?needInitFileName=true)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150831.62986371393685599236439870481120:50001231000000:2800:D1F4E1FD60A9358C983C97E546F12CFF42994BFC25873E6EE692157BB97BC5D1.png?needInitFileName=true?needInitFileName=true)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-ohpm-repo-export-metadata-V14
爬取时间: 2025-05-01 00:07:32
来源: Huawei Developer
支持通过export_pkginfo和batch_download命令，将OpenHarmony三方库中心仓中所有包批量导出，并能够通过batch_publish命令将导出的库批量上传至部署的ohpm-repo实例中。
开始执行下面的命令之前，请确保已经执行过ohpm-repo install和ohpm-repo start命令。
获取所有已上架的包列表
使用export_pkginfo命令，导出OpenHarmony三方库中心仓已上架的包列表。
执行结果
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250117150831.81507022094199869236247106204023:50001231000000:2800:3F50DC21152A0ED6550CA02465D555813C1EF8DB3B257FE88A8F87EC6D648360.png?needInitFileName=true?needInitFileName=true)
批量下载三方包
执行batch_download命令将上一步生成的pkgInfo_xxx.json文件中记录的包全部下载。
若只需要下载中心仓的部分包，可以手动修改pkgInfo_xxx.json文件，此时该命令只会批量下载pkgInfo_xxx.json文件中指定的包。
执行结果
批量上传
执行batch_publish命令将上一步生成的batch_download_xxx.zip压缩包中全部包批量上传到ohpm-repo。
执行结果
如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo实例缓存中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-interface-protocol-V14
爬取时间: 2025-05-01 00:08:06
来源: Huawei Developer
概述
ohpm客户端与ohpm-repo私仓通过REST API交互，目前一共有六种API：
ohpm客户端在访问ohpm-repo时，支持公私钥和Access Token两种认证方式：
Fetch Metadata
返回指定包的metadata元数据。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| group  | string  | 否  | 组织名，以@开头，比如@ohos  |
| package_name  | string  | 是  | 包名 (不含组织部分)  |
属性
类型
必填项
描述
group
string
否
组织名，以@开头，比如@ohos
package_name
string
是
包名 (不含组织部分)
请求示例（以请求一个应用内的HAR包 @test/package1 为例）：
响应成功示例（以请求一个应用内的HAR包 @test/package1 为例）：
metadata响应数据说明:
响应数据中包含八个顶级字段，描述如下：
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| _id  | string  | 是  | 包名，并用作数据库的主键ID  |
| _rev  | number  | 是  | 包的版本数量  |
| name  | string  | 是  | 包名  |
| description  | string  | 是  | 包的描述  |
| dist-tags  | json  | 是  | 包的所有标签信息  |
| versions  | json  | 是  | 包的所有版本数据  |
| packageType  | string  | 否  | 包的类型，详情见说明  |
| time  | json  | 是  | 包的发布时间  |
属性
类型
必填项
描述
_id
string
是
包名，并用作数据库的主键ID
_rev
number
是
包的版本数量
name
string
是
包名
description
string
是
包的描述
dist-tags
json
是
包的所有标签信息
versions
json
是
包的所有版本数据
packageType
string
否
包的类型，详情见说明
time
json
是
包的发布时间
顶级字段中versions字段包含包的所有版本数据，有17个字段内容，描述如下：
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| _id  | string  | 是  | 包名@包的版本号，如：@myscope/myhsplib@1.0.0  |
| _nodeVersion  | string  | 是  | 发布时使用的node.js版本  |
| _ohpmVersion  | string  | 是  | 发布时使用的ohpm客户端版本  |
| name  | string  | 是  | 包名  |
| version  | string  | 是  | 包的版本号  |
| description  | string  | 是  | 包的描述  |
| author  | json  | 是  | 包的作者信息  |
| repository  | string  | 否  | 包的源码仓库地址  |
| license  | string  | 否  | 包的项目开源许可证，详情见说明  |
| packageType  | string  | 否  | 包的类型，详情见说明  |
| dependencies  | json  | 否  | 包的运行时依赖  |
| devDependencies  | json  | 否  | 包的开发态依赖  |
| dynamicDependencies  | json  | 否  | 包的动态依赖，只针对HSP包  |
| types  | string  | 条件必填  | 包的类型声明文件  |
| main  | string  | 条件必填  | 包的入口文件  |
| dist  | json  | 是  | 维护包的SSRI值及下载地址，详情见说明  |
| hspType  | string  | 条件必填  | HSP包的类型，详情见说明  |
属性
类型
必填项
描述
_id
string
是
包名@包的版本号，如：@myscope/myhsplib@1.0.0
_nodeVersion
string
是
发布时使用的node.js版本
_ohpmVersion
string
是
发布时使用的ohpm客户端版本
name
string
是
包名
version
string
是
包的版本号
description
string
是
包的描述
author
json
是
包的作者信息
repository
string
否
包的源码仓库地址
license
string
否
包的项目开源许可证，详情见说明
packageType
string
否
包的类型，详情见说明
dependencies
json
否
包的运行时依赖
devDependencies
json
否
包的开发态依赖
dynamicDependencies
json
否
包的动态依赖，只针对HSP包
types
string
条件必填
包的类型声明文件
main
string
条件必填
包的入口文件
dist
json
是
维护包的SSRI值及下载地址，详情见说明
hspType
string
条件必填
HSP包的类型，详情见说明
Login
客户端登录，获得上传包，下架包和编辑标签tag时所需的 token。
请求示例：
请求示例中请求体（@./path/to/login-body/file.json）示例 ：
请求体包含五个字段，描述如下：
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| version  | string  | 是  | 协议版本  |
| publishId  | string  | 是  | 发布码  |
| timestamp  | number  | 是  | 发布时间戳  |
| nonce  | string  | 是  | 随机数  |
| signature  | string  | 是  | 签名值，具体见说明  |
属性
类型
必填项
描述
version
string
是
协议版本
publishId
string
是
发布码
timestamp
number
是
发布时间戳
nonce
string
是
随机数
signature
string
是
签名值，具体见说明
1、publishId: 由ohpm-repo私仓生成的发布码，与用户绑定，每个用户的发布码是唯一的，在客户端的 .ohpmrc 文件中通过 publish_id 配置；
2、timestamp: 时间戳，单位为毫秒；
3、nonce: 客户端在登录时动态生成的uuidv4随机数；
4、signature: 客户端在登录时，将协议版本、发布码、发布时间戳和随机数以 v{version}-{publishId}-{timestamp}-{nonce} 格式组合而成，并使用私钥经RSA-SHA256算法签名而生成。
响应成功示例：
token: 使用公私钥认证时，ohpm-repo生成的认证信息。认证信息必须验证有效，才有权限执行上传包、下架包和编辑标签tag等操作。
Publish
上传一个HAR/HSP包到ohpm-repo私仓中
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
属性
类型
必填项
描述
package_name
string
是
包名
若包名中包含组织名，则package_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package_name为@myscope%2fmypkg。
请求示例（以上传一个应用内的HSP包 @myscope/myhsppkg 为例）：
请求示例中metadata元数据文件（@./path/to/metadata/file.json）内容由ohpm客户端生成，内容如下所示：
响应成功示例：
响应失败示例：
1、发布失败时，ohpm客户端会根据状态码取响应体中error字段的值或状态描述statusText的值，进行打印提示。
2、additionalMsg: 当响应体中存在该字段且不为空时，ohpm客户端会在发布包成功后打印该字段的值。
流式上传一个HAR/HSP到ohpm-repo
ohpm客户端从5.0.1版本开始支持使用流式上传，当上传的三方包大小超过阈值（默认5M）时，ohpm会优先调用流式上传接口进行上传。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
属性
类型
必填项
描述
package_name
string
是
包名
若包名中包含组织名，则package_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package_name为@myscope%2fmypkg。
请求示例（以上传一个应用内的HSP包 @myscope/myhsppkg 为例）：
其中， Content-Type是multipart/form-data；hsp.tgz是待上传的HSP包。
请求示例中元数据文件（@./path/to/metadata/file.json）内容由ohpm客户端生成，如下所示：
响应成功示例：
响应失败示例：
1、发布失败时，ohpm客户端会根据状态码取响应体中error字段的值或状态描述statusText的值，进行打印提示。
2、additionalMsg: 当响应体中存在该字段且不为空时，ohpm客户端会在发布包成功后打印该字段的值。
Unpublish
从ohpm-repo中下架一个HAR/HSP包 （下架一个包的某个版本，或是整个包）。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
属性
类型
必填项
描述
package_name
string
是
包名
请求示例：
Ping
检测与ohpm-repo仓库的网络连通性。
请求示例：
响应成功示例：
DistTags
新增tag
为包添加tag。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
| tag  | string  | 是  | 标签名  |
属性
类型
必填项
描述
package_name
string
是
包名
tag
string
是
标签名
若包名中包含组织名，则package_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package_name为@myscope%2fmypkg。
请求示例（为包 @myscope/myhsppkg@1.0.0 增加标签（tag）test）：
更新tag
修改包tag对应的版本号。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
| tag  | string  | 是  | 标签名  |
属性
类型
必填项
描述
package_name
string
是
包名
tag
string
是
标签名
请求示例（为包 @myscope/myhsppkg 修改标签（tag）test对应版本号为2.0.0）：
删除tag
删除包的tag。
| 属性  | 类型  | 必填项  | 描述  |
| --- | --- | --- | --- |
| package_name  | string  | 是  | 包名  |
| tag  | string  | 是  | 标签名  |
属性
类型
必填项
描述
package_name
string
是
包名
tag
string
是
标签名
请求示例（删除包 @myscope/myhsppkg 的标签（tag）test）：
仓库响应码说明
| 响应码  | 范围  | 说明  |
| --- | --- | --- |
| 200  | 仓库所有接口  | 成功  |
| 400  | 仓库所有接口  | 客户端传参校验失败、登录失败  |
| 401  | Publish, Unpublish, DistTags  | 认证失败  |
| 404  | 访问仓库不存在的接口  | 接口不存在  |
| 500  | 仓库所有接口  | 服务内部错误  |
| 598  | Publish  | 当仓库上传接口返回的响应状态码为598时，ohpm 5.0.1及以上版本会尝试去重新上传  |
响应码
范围
说明
200
仓库所有接口
成功
400
仓库所有接口
客户端传参校验失败、登录失败
401
Publish,Unpublish,DistTags
认证失败
404
访问仓库不存在的接口
接口不存在
500
仓库所有接口
服务内部错误
598
Publish
当仓库上传接口返回的响应状态码为598时，ohpm 5.0.1及以上版本会尝试去重新上传
由于流式上传接口在ohpm 5.0.1版本才开始支持，当ohpm调用该接口时，若返回的响应状态码为404时，ohpm客户端会再次调用上传接口上传。为了保证与ohpm客户端的兼容性，请确保当访问仓库不存在的接口仓库的响应状态码为404。

