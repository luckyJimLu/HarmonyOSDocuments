# 合并文件
合并时间: 2025-04-27 23:07:41

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/accessibility-kit-V14
爬取时间: 2025-04-27 22:37:48
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/accessibilitykit-overview-V14
爬取时间: 2025-04-27 22:38:02
来源: Huawei Developer
Accessibility（信息无障碍），是指任何人在任何情况下都能平等、方便地获取信息并利用信息。其目的是缩小全社会不同阶层、不同地区、不同年龄、不同健康状况的人群在信息理解、信息交互、信息利用方面的数字鸿沟，使其更加方便地参与社会生活，享受数字发展带来的便利。
Accessibility Kit（无障碍服务）提供应用适配无障碍的开放能力，以便应用可以更好的服务于障碍人群和障碍场景，如为组件添加无障碍焦点、无障碍朗读文本等。
能力范围
与相关Kit的关系
ArkUI Kit为Accessibility提供无障碍组件属性定义、无障碍事件发送能力，应用可基于ArkUI Kit为组件设置无障碍文本、描述信息等属性。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/screen-reading-adapt-guide-V14
爬取时间: 2025-04-27 22:38:16
来源: Huawei Developer
概述
屏幕朗读软件（Screen Reader）主要帮助视障人士使用移动智能设备，通过语音输出，获取屏幕或界面中的信息。视障用户无法通过视觉直接感知和理解用户界面。他/她们需要在屏幕上使用手指探索或手势逐步在界面上进行导航，同时通过设备的朗读反馈来理解界面信息和潜在的交互功能。因此，让用户能够快速、准确地感知界面内容并进行正确交互是无障碍开发的关键。视障用户需要先通过手势使某个UI对象获得焦点，同时系统朗读出该对象的内容和功能，然后视障用户双击屏幕点击或选择该对象。
因此，进行开发时应遵循以下原则：
同时，进行开发时，组件可以设置相应的无障碍属性和事件来更好地使用无障碍能力。
标注屏幕朗读内容的场景
控件包含显示文本（text）、无障碍文本（accessibilityText）2个属性，其中，显示文本为用户界面上呈现的信息，无障碍文本为无障碍专有的朗读信息，不在界面上显示。屏幕朗读提取信息进行朗读时无障碍文本的优先级大于显示文本，即当无障碍文本不为空时，会朗读无障碍文本，否则朗读显示文本。
所以：
accessibilityText( ) 设置无障碍文本。聚焦button时朗读效果为："按钮, Accessibility text"。
禁用屏幕朗读焦点的场景
装饰性的控件一般为分隔符、占位符和美化图标等，这类图形元素仅仅起到调整页面布局或装饰性效果，并不会向用户传达有效的信息或提供交互功能，删除后不影响指引用户体验。可以设置控件的无障碍是否可见的属性将其设置对无障碍不可见，这样在屏幕朗读模式下控件就不会获取焦点和朗读。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170225.00195888843350415338363671737774:50001231000000:2800:6F9BE5EA869E1609B0CDE129579907BF11FB3FF54E8614DCF9DBA82F23898469.png)
accessibilityGroup(true) 用于多个组件的组合，组合内的默认没有焦点。
.accessibilityLevel("no")用于组件设置不可聚焦，不被无障碍感知。
例如：以下代码同时显示“Broadcast”和“No broadcast”消息，但当ScreenReader处于“打开”状态时，message可被聚焦，但message1将不被聚焦。
多维嵌套场景
如果应用展示的是多维信息，还可能出现“嵌套组”的情况。在嵌套组中，应避免两个可获焦对象的功能或朗读内容产生重复。比如下图的天气卡片，时间和地点信息获取到焦点时，都是朗读的时间信息；不同焦点的重复朗读会额外增减用户的操作步骤，焦点控制杂乱，这些对同一个信息结构的完整描述应该统一标注在这几个子控件的父控件上。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170225.38258132941048548944188111054655:50001231000000:2800:D3208F69207BEBC16D0395BB5A832D33F712CF356C1C1C688C37690938712DEF.png)
组合场景
在一些场景中，一个功能上完整的UI对象可能是由若干个更小的UI组件组合而成的。若每一个小的UI组件都可以获焦并朗读，则会造成信息冗余和效率降低。同时由于可聚焦的组件过多过细，也会影响触摸浏览时走焦的性能体验。在这种情况下，将它们在功能或语义上聚合成一个自然组并作为一个独立可获焦的UI元素来向视障用户表达内容更加合理，且更加高效。
总体原则是：对于表示同一个对象信息的多个组件，需要进行组合标注，对外只暴露一个无障碍焦点。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170225.35518133232155367251648462471556:50001231000000:2800:2900A2BEE30D72257E8DBC949B36A733C979FB0668329AFB76A4C9465D841559.png)
如下，可以将多个控件设置为一个组，通过对组设置朗读标签，达到整组播报的效果，组内的子控件设置不可获取焦点。
按钮标注场景
对于用户可点击等操作的任何按钮，如果不是文本类控件，则须通过给出标注信息，包括用户自定义的控件中的虚拟按钮区域，否则可能会导致屏幕朗读用户无法完成对应的功能。
此类控件在进行标注时，标注文本不要包含控件类型、“单指双击即可打开”之类的字符串，此部分指引由屏幕朗读根据控件类型、控件状态，并结合用户是否开启了“新手指引”自动追加朗读。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170225.40611677741820648354554289214423:50001231000000:2800:CC93C3B04AC7579F06BB9244CEE72EDE9A8782AAA9AB1E1B3495D0C1298D0128.png)
在下面的代码片段中，您可以看到Image组件（它实际上是一个播放/暂停按钮），通过设置accessibilityText属性提供标注信息：
```typescript
const RESOURCE_STR_PLAY = $r('app.media.play')
const RESOURCE_STR_PAUSE = $r('app.media.pause')
@Component
export struct Rule_2_1_6 {
title: string = 'Rule 2.1.6'
@State isPlaying: boolean = false
play() {
// play audio file
}
pause() {
// pause playing of audio file
}
build() {
NavDestination() {
Column() {
Flex({
direction: FlexDirection.Column,
alignItems: ItemAlign.Center,
justifyContent: FlexAlign.Center,
}) {
Row() {
Image(this.isPlaying ? RESOURCE_STR_PAUSE : RESOURCE_STR_PLAY)
.width(50)
.height(50)
.onClick(() => {
this.isPlaying = !this.isPlaying
if (this.isPlaying) {
this.play()
} else {
this.pause()
}
})
.accessibilityText(this.isPlaying ? 'Pause' : 'Play') // 设置注释信息
Text('Good_morning.mp3')
.margin({
left: 10
})
}
}
.width('100%')
.height('100%')
.backgroundColor(Color.White)
}
}
.title(this.title)
}
}
```
插画/视频/动画的播报场景
如下图，插画信息有一定提示作用，插画和对应的功能介绍应该组合在一起，当焦点落到插画或者包含插画的符合控件时，需要朗读出对应的功能描述。建议插画和功能介绍作为一个组合使用一个焦点朗读。它可以借助“accessibilityGroup(true)”属性来实现。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170225.62373254427179359170506991961671:50001231000000:2800:D2A3AEA01B888FE6F3993CE729A77CED702944579456508ADD7535E462F62543.png)
以下List的每个Item，应该进行组合标注，从而给用户一个完整的提示信息：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170225.84322678564791343538972457656111:50001231000000:2800:E7A32D414F7C490CD8C3178C0A302969E9B7E8BCFBAF150DC62E0F30284A319D.png)
它可以借助“accessibilityGroup(true)”属性来实现：
内容动态变化场景
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170225.59166148689633373753982185471667:50001231000000:2800:3AEF180E4CCF44319FE1FBA11DC8969A416026BBBF41406CAFC6ADC152BEAFF2.png)

| 属性  | 类型  | 说明  | 例  |
| --- | --- | --- | --- |
| type  | EventType  | 主动播报事件类型  | announceForAccessibility  |
| bundleName  | string  | 目标应用名  | 当前应用包名  |
| triggerAction  | Action  | 触发事件的Action  | click或其他都不会有任何影响  |
| textAnnouncedForAccessibility  | string  | 主动播报的内容  | test123 text  |
属性
类型
说明
例
type
EventType
主动播报事件类型
announceForAccessibility
bundleName
string
目标应用名
当前应用包名
triggerAction
Action
触发事件的Action
click或其他都不会有任何影响
textAnnouncedForAccessibility
string
主动播报的内容
test123 text
控件状态变化场景
例如下图，播放暂停按钮对应着两种状态，在状态切换时需要实时变化对应的标注信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170226.15845245904212869282992016862453:50001231000000:2800:33506003D914EB4B742C9B0AAB3E2F6A11FEEDAC4D2A75D912ADA85BF0096926.png)
操作错误场景
比如网络连接错误，或者其他警告信息，不能仅仅以颜色区分，需要实时告诉用户错误提示和改进方法。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170226.99220096776615600183845173710533:50001231000000:2800:D9186BF8E82FD2FC1C52ACED71E162516AE05ED0BE47ED64940BC92B4379850B.png)
如下是一个将连接中断播报出来的例子。
多语种场景
当对朗读内容进行标注时，须对标注字符串进行多语种翻译，具体支持的语种和应用本身界面支持的语种保持一致。若采用多个字符串进行朗读内容的拼接，需考虑多语种的情况，避免拼接后朗读错误，例如阿拉伯语从右到左。
控件位置调整场景
移动过程中需要实时播报即将移动到的位置，新位置的播报会打断老位置的播报，放置到确定位置后，需要再播报已经放置的位置信息，尽量保证视障用户耳朵听到的信息和我们通过眼睛看到的信息是一致的。例如，网页书签被托起时，会播报已托起，移动的过程中，根据即将放置的位置播报“移至第几行，第几列”，放置后播报“已放至第几行，第几列”。应用可调用主动播报的接口来进行主动播报。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170226.37336469933166717575497369639791:50001231000000:2800:944D732241D6FADB19C4FBC57B26B59080668479CA04F5D3569AE6B74EFA6106.png)
重新设置新焦点位置的场景

| 属性  | 类型  | 说明  | 例  |
| --- | --- | --- | --- |
| type  | EventType  | 主动聚焦事件类型  | requestFocusForAccessibility  |
| bundleName  | string  | 目标应用名  | 当前应用包名  |
| triggerAction  | Action  | 触发事件的Action  | click或其他都不会有任何影响  |
| customId  | string  | 组件id  | abc345  |
属性
类型
说明
例
type
EventType
主动聚焦事件类型
requestFocusForAccessibility
bundleName
string
目标应用名
当前应用包名
triggerAction
Action
触发事件的Action
click或其他都不会有任何影响
customId
string
组件id
abc345

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkdata-V14
爬取时间: 2025-04-27 22:38:29
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-mgmt-overview-V14
爬取时间: 2025-04-27 22:38:43
来源: Huawei Developer
功能介绍
ArkData （方舟数据管理）为开发者提供数据存储、数据管理和数据同步能力，比如联系人应用数据可以保存到数据库中，提供数据库的安全、可靠以及共享访问等管理机制，也支持与手表同步联系人信息。
-  标准化数据定义：提供HarmonyOS跨应用、跨设备的统一数据类型标准，包含标准化数据类型和标准化数据结构。
-  数据存储：提供通用数据持久化能力，根据数据特点，分为用户首选项、键值型数据库和关系型数据库。
-  数据管理：提供高效的数据管理能力，包括权限管理、数据备份恢复、数据共享框架等。
-  数据同步：提供跨设备数据同步能力，比如分布式对象支持内存对象跨设备共享能力，分布式数据库支持跨设备数据库访问能力。
应用创建的数据库，都保存到应用沙盒，当应用卸载时，数据库也会自动删除。
运作机制
数据管理模块包括用户首选项、键值型数据管理、关系型数据管理、分布式数据对象、跨应用数据管理和统一数据管理框架。Interface接口层提供标准JS API接口，定义这些部件接口描述，供开发者参考。Frameworks&System service层负责实现部件数据存储、同步功能，还有一些SQLite和其他子系统的依赖。
图1数据管理架构图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170226.47406190661716326092384049478531:50001231000000:2800:E6C288ED60EB6614CC9203452B16B7B5D7CCAB4A3FFFC73C27C92E17BE9A558B.jpg)
-  用户首选项（Preferences）：提供了轻量级配置数据的持久化能力，并支持订阅数据变化的通知能力。不支持分布式同步，常用于保存应用配置信息、用户偏好设置等。
-  键值型数据管理（KV-Store）：提供了键值型数据库的读写、加密、手动备份以及订阅通知能力。应用需要使用键值型数据库的分布式能力时，KV-Store会将同步请求发送给DatamgrService由其完成跨设备数据同步。
-  关系型数据管理（RelationalStore）：提供了关系型数据库的增删改查、加密、手动备份以及订阅通知能力。应用需要使用关系型数据库的分布式能力时，RelationalStore部件会将同步请求发送给DatamgrService由其完成跨设备数据同步。
-  分布式数据对象（DataObject）：独立提供对象型结构数据的分布式能力。如果应用需要重启后仍获取之前的对象数据（包含跨设备应用和本设备应用），则使用数据管理服务（DatamgrService）的对象持久化能力，做暂时保存。
-  跨应用数据管理（DataShare）：提供了数据提供者provider、数据消费者consumer以及同设备跨应用数据交互的增、删、改、查以及订阅通知等能力。DataShare不与任何数据库绑定，可以对接关系型数据库、键值型数据库。如果开发C/C++应用甚至可以自行封装数据库。在提供标准的provider-consumer模式基础上，同时提供了静默数据访问能力，即不再拉起provider而是直接通过DatamgrService代理访问provider的数据（目前仅关系型数据库支持静默数据访问方式）。
-  统一数据管理框架（UDMF）：提供了数据跨应用、跨设备交互标准，定义了跨应用、跨设备数据交互过程中的数据语言，提升数据交互效率。提供安全、标准化数据流通通路，支持不同级别的数据访问权限与生命周期管理策略，实现高效的数据跨应用、跨设备共享。
-  数据管理服务（DatamgrService）：提供其它部件的同步及跨应用共享能力，包括RelationalStore和KV-Store跨设备同步，DataShare静默访问provider数据，暂存DataObject同步对象数据等。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uniform-data-definition-V14
爬取时间: 2025-04-27 22:38:56
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/unified-data-definition-overview-V14
爬取时间: 2025-04-27 22:39:10
来源: Huawei Developer
设备、应用交互的核心在于数据的互通，高效的数据互通基础是共识。为了降低应用/业务数据交互成本，促进数据生态建设，统一数据管理框架（UDMF）提供了标准化数据定义作为统一的HarmonyOS数据语言，用于构建跨应用、跨设备的统一数据标准与交互共识。
UDMF标准化数据定义包括标准化数据类型和标准化数据结构。
标准化数据类型：主要针对同一种数据类型，提供统一定义，即标准数据类型描述符，定义了包括标识数据类型的ID、类型归属关系等相关信息，用于解决HarmonyOS系统中的类型模糊问题。一般用于过滤或者识别某一种数据类型的场景，比如文件预览、文件分享等。
标准化数据结构：主要针对部分标准化数据类型定义了统一的数据内容结构，并明确了对应的描述信息。应用间使用标准化数据结构进行数据交互后，将遵从统一的解析标准，可有效减少适配相关的工作量。一般用于跨应用跨设备间的数据交互，比如拖拽。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uniform-data-type-descriptors-V14
爬取时间: 2025-04-27 22:39:24
来源: Huawei Developer
场景介绍
标准化数据类型（Uniform Type Descriptor，简称UTD）用于解决系统中的类型模糊问题，即针对同一种数据类型，存在不同的类型描述方式：MIME Type、文件扩展名等。例如描述jpg/jpeg类型图片时，可以使用image/jpeg、.jpg、.jpeg或image/picture等方式进行描述。
当相关类型的数据进行跨应用、跨设备传输时，目标端应用/设备需要进行多方面的适配，才能够对数据内容进行相关处理，且存在无法识别的情况。
标准化数据类型分为预置数据类型和应用自定义数据类型。并且支持从其他类型体系，如文件名后缀和MIME type转换为UTD标准类型。
针对标准化数据类型，典型的应用场景有：文件管理中的图片预览、系统分享等。
标准化数据类型的设计和分类原则
标准化数据类型按层级结构构建
基于MIME Type或文件后缀名进行类型区分，存在另一个不足：即扁平化的数据类型定义。
扁平/松散的类型定义难以描述不同类型间的兼容与继承关系，且在实际使用过程中，会增加应用处理数据类型时的开发复杂度。例如搜索场景，用户从精确地搜索动物相关的任意类型图片，进一步扩展到动物相关的任意图片、视频或音频资源。为了满足上述场景，我们需要在定义数据类型时，支持类型层级结构。
构建标准类型的层级结构，定义层级结构中的类型归属关系，能够帮助系统、应用实现数据类型的分层、分类管理。当用户进行数据分享或拖拽时，如果数据中同时包含图片、视频、音频等内容，系统/应用可以根据层级按需对分享内容进行整理，如分享了几张照片、几条视频或几个媒体资源文件等。
标准化数据类型的分类原则
UTD中定义的标准化数据类型在设计原则上按物理和逻辑分为两类。HarmonyOS中预置了常用的标准化数据类型，详见UTD预置列表。
-  按物理分类的根节点为general.entity，用于描述类型的物理属性，比如文件、目录等，具体可见图1。
-  按逻辑分类的根节点为general.object，用于描述类型的功能性特征，如图片、网页等，具体可见图2。
按照此分类原则，可以从两个维度对数据类型进行描述。如描述图片时，可以是一个图片对象，同时也可以是一个文件。
并非所有的格式都具有两个维度，如general.calendar，更多的注重calendar对象的功能性描述。
图1物理标准化数据类型示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170226.60751526353520586847589016260023:50001231000000:2800:52DC4666CCA2C4514E84F0B3F330E78325FBB6A31F818DB1885D92B4449B90E1.png)
图2逻辑标准化数据类型示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170226.55896154286351950527758775582170:50001231000000:2800:FBEB43FE584105C92FD50C8EFD3D597F2C9006DC2AF2C7EC4DF0AF97DF306342.png)
标准化数据类型的定义
标准化数据类型包含了标准化数据类型的标识ID、归属类型关系、简要描述等信息，具体可见TypeDescriptor属性，每个类型定义具体包含以下内容：
预置数据类型
基于常用的数据类型，预先定义了一部分标准数据类型描述符，即预置数据类型。如用于描述音频文件的“general.audio”，描述视频文件的“general.video”，更多预置数据类型参考UTD预置列表。
应用自定义数据类型
由于预置标准数据类型无法穷举所有数据类型，在业务跨应用、跨设备交互过程中，会涉及到一些应用独有的数据类型，因此支持应用声明自定义数据类型。
应用自定义的数据类型可继承已有的标准类型，例如业务自定义的图片类型可以使用“com.company.x-image”作为自定义数据类型的标识。
业务可以将自定义数据类型注册到系统中，这样其他业务可以在需要时引用，进而实现生态内各应用自定义数据类型的共享与统一。
工作原理
基于标准类型的层级结构，业务声明自己支持的数据类型标识符时，需要声明该类型标识符的层级逻辑，例如业务自定义图片类型UTD标识符“com.company.x-image”，并归属到general.image类中。UTD会检验自定义类型标识符，确保归属关系中不出现环状结构。
应用安装时，UTD会读取应用中自定义的数据类型进行安装，校验自定义类型数据符合约束条件后，应用自定义数据类型将被安装到设备中。应用启动后能正常读取到应用自定义的数据类型。如果引用其他应用定义的自定义数据类型，需要在应用开发时一并写入自定义数据类型配置文件中。
约束限制
针对自定义的类型描述各字段，有以下相关要求和限制：
-  TypeId：定义标准化数据类型的ID，该ID具有唯一性，由应用bundleName + 具体类型名组成，不可缺省，允许包含数字、大小写字母、-和.。
-  BelongingToTypes：定义标准化数据类型的归属关系，即该标准化数据类型归属于哪个更高层级的类型，所属类型可以为多个，但是必须为已存在的数据类型（标准化数据类型预置类型或其他新增自定义数据类型），不能为应用自定义类型本身，不能为空，且与现有标准化数据类型、其他新增自定义数据类型不能形成环形依赖结构。
-  FilenameExtensions：应用自定义标准化数据类型所关联的文件后缀。可以缺省；可以为多个，每个后缀为以.开头且长度不超过127的字符串。
-  MIMETypes：应用自定义标准化数据类型所关联的web消息数据类型。可以缺省；可以为多个，每个类型为长度不超过127的字符串。
-  Description：应用自定义标准化数据类型的简要说明。可以缺省；填写时，长度为不超过255的字符串。
-  ReferenceURL：应用自定义标准化数据类型的参考链接URL，用于描述类型的详细信息。可以缺省；填写时，长度为不超过255的字符串。
开发步骤
下面以新增媒体类文件类型场景为例，说明如何自定义UTD标准化数据类型。
1.  当前应用在entry\src\main\resources\rawfile\arkdata\utd\目录下新增utd.json5文件。
2.  在当前应用的utd.json5配置文件内新增所需的自定义数据类型。
```json
{
"UniformDataTypeDeclarations": [
{
"TypeId": "com.example.myFirstHap.image",
"BelongingToTypes": ["general.image"],
"FilenameExtensions": [".myImage", ".khImage"],
"MIMETypes": ["application/myImage", "application/khImage"],
"Description": "My Image.",
"ReferenceURL": ""
},
{
"TypeId": "com.example.myFirstHap.audio",
"BelongingToTypes": ["general.audio"],
"FilenameExtensions": [".myAudio", ".khAudio"],
"MIMETypes": ["application/myAudio", "application/khAudio"],
"Description": "My audio.",
"ReferenceURL": ""
},
{
"TypeId": "com.example.myFirstHap.video",
"BelongingToTypes": ["general.video"],
"FilenameExtensions": [".myVideo", ".khVideo"],
"MIMETypes": ["application/myVideo", "application/khVideo"],
"Description": "My video.",
"ReferenceURL": ""
}
]
}
```
3.  如果其他应用要直接使用当前应用内的自定义数据类型，需要在其应用的entry\src\main\resources\rawfile\arkdata\utd\目录下新增utd.json5文件。 然后在utd.json5配置文件中进行以下声明：
```json
{
"ReferenceUniformDataTypeDeclarations": [
{
"TypeId": "com.example.myFirstHap.image",
"BelongingToTypes": ["general.image"],
"FilenameExtensions": [".myImage", ".khImage"],
"MIMETypes": ["application/myImage", "application/khImage"],
"Description": "My Image.",
"ReferenceURL": ""
}
]
}
```
4.  其他应用也可以在DevEco Studio中创建utd.json5模板，在模板中引用当前应用内的自定义数据类型之后，基于已引用的自定义数据类型进行自定义。同时，DevEco Studio还会对配置文件中的字段进行格式校验，utd.json5配置文件示例如下：
```json
{
"UniformDataTypeDeclarations": [
{
"TypeId": "com.example.mySecondHap.image",
"BelongingToTypes": ["com.example.myFirstHap.image"],
"FilenameExtensions": [".myImageEx", ".khImageEx"],
"MIMETypes": ["application/my-ImageEx", "application/khImageEx"],
"Description": "My Image extension.",
"ReferenceURL": ""
}
]
}
```
接口说明
以下是UTD常用接口说明，对于预置数据类型和应用自定义数据类型同样适用，更多接口和详细说明，请见@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)。
| 接口名称 | 描述 |
| --- | --- |
| UniformDataType | 标准化数据类型的枚举定义。此处不再展开列举各枚举。 |
| belongsTo(type: string): boolean | 判断当前标准化数据类型是否归属于指定的标准化数据类型。 |
| isLowerLevelType(type: string): boolean | 判断当前标准化数据类型是否是指定标准化数据类型的低层级类型。 |
| isHigherLevelType(type: string): boolean | 判断当前标准化数据类型是否是指定标准化数据类型的高层级类型。 |
| getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string | 根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型ID，若有多个符合条件的标准化数据类型ID，则返回第一个。 |
| getUniformDataTypeByMIMEType(mimeType: string, belongsTo?: string): string | 根据给定的MIME类型和所归属的标准化数据类型查询标准化数据类型ID，若有多个符合条件的标准化数据类型ID，则返回第一个。 |
| getUniformDataTypesByFilenameExtension(filenameExtension: string, belongsTo?: string): Array<string> | 根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型ID列表。 |
| getUniformDataTypesByMIMEType(mimeType: string, belongsTo?: string): Array<string> | 根据给定的MIME类型和所归属的标准化数据类型查询标准化数据类型ID列表。 |
如何查询媒体类文件归属类型
下面以媒体类文件的归属类型查询场景为例，说明如何使用UTD。
```typescript
// 1.导入模块
import { uniformTypeDescriptor } from '@kit.ArkData';
try {
// 2.可根据 “.mp3” 文件后缀查询对应UTD数据类型，并查询对应UTD数据类型的具体属性
let fileExtention = '.mp3';
let typeId1 = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(fileExtention);
let typeObj1 = uniformTypeDescriptor.getTypeDescriptor(typeId1);
console.info('typeId:' + typeObj1.typeId);
console.info('belongingToTypes:' + typeObj1.belongingToTypes);
console.info('description:' + typeObj1.description);
console.info('referenceURL:' + typeObj1.referenceURL);
console.info('filenameExtensions:' + typeObj1.filenameExtensions);
console.info('mimeTypes:' + typeObj1.mimeTypes);
// 3.可根据 “audio/mp3” MIMEType查询对应UTD数据类型，并查询对应UTD数据类型的具体属性。
let mineType = 'audio/mp3';
let typeId2 = uniformTypeDescriptor.getUniformDataTypeByMIMEType(mineType);
let typeObj2 = uniformTypeDescriptor.getTypeDescriptor(typeId2);
console.info('typeId:' + typeObj2.typeId);
console.info('belongingToTypes:' + typeObj2.belongingToTypes);
console.info('description:' + typeObj2.description);
console.info('filenameExtensions:' + typeObj2.filenameExtensions);
console.info('mimeTypes:' + typeObj2.mimeTypes);
// 4.将数据类型进行比较，确认是否同一种数据类型
if (typeObj1 != null && typeObj2 != null) {
let ret = typeObj1.equals(typeObj2);
console.info('typeObj1 equals typeObj2, ret:' + ret);
}
// 5.将查询到的标准数据类型“general.mp3”与表示音频数据的已知标准数据类型“general.audio”做比较查询，确认是否存在归属关系。
if (typeObj1 != null) {
let ret = typeObj1.belongsTo('general.audio');
console.info('belongsTo, ret:' + ret);
let mediaTypeObj = uniformTypeDescriptor.getTypeDescriptor('general.media');
ret = mediaTypeObj.isHigherLevelType('general.audio'); // 确认是否存在归属关系
console.info('isHigherLevelType, ret:' + ret);
}
} catch (err) {
console.error('err message:' + err.message + ', err code:' + err.code);
}
```
如何通过文件后缀获取对应的MIMEType列表
下面以通过“.ts”文件后缀获取对应的MIMEType列表为例，说明如何通过文件后缀获取对应的MIMEType列表。
```typescript
// 1.导入模块
import { uniformTypeDescriptor } from '@kit.ArkData';
try {
// 2.可根据 “.ts” 文件后缀查询对应UTD数据类型。
let fileExtention = '.ts';
let typeIds = uniformTypeDescriptor.getUniformDataTypesByFilenameExtension(fileExtention);
for (let typeId of typeIds) {
// 3.根据UTD数据类型查询对应的MIMEType列表。
let typeObj = uniformTypeDescriptor.getTypeDescriptor(typeId);
let mimeTypes = typeObj.mimeTypes;
console.info('mimeTypes:' + mimeTypes);
}
} catch (err) {
console.error('err message:' + err.message + ', err code:' + err.code);
}
```
如何通过MIMEType获取对应的后缀列表
下面以通过“text/plain”MIMEType获取对应文件后缀列表为例，说明如何通过MIMEType获取对应的后缀列表。
```typescript
// 1.导入模块
import { uniformTypeDescriptor } from '@kit.ArkData';
try {
// 2.可根据 “text/plain” MIMEType查询对应UTD数据类型。
let mineType = 'text/plain';
let typeIds = uniformTypeDescriptor.getUniformDataTypesByMIMEType(mineType);
for (let typeId of typeIds) {
// 3. 根据UTD数据类型查询对应的MIMEType列表
let typeObj = uniformTypeDescriptor.getTypeDescriptor(typeId);
let filenameExtensions = typeObj.filenameExtensions;
console.info('filenameExtensions:' + filenameExtensions);
}
} catch (err) {
console.error('err message:' + err.message + ', err code:' + err.code);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uniform-data-structure-V14
爬取时间: 2025-04-27 22:39:37
来源: Huawei Developer
场景介绍
针对UTD标准化数据类型中的部分常见类型，为了方便业务使用，我们按照不同的数据类型提供了标准化数据结构，例如系统定义的桌面图标类型（对应的标准化数据类型标识为'openharmony.app-item'），我们明确定义了该数据结构对应的相关描述信息。
某些业务场景下应用可以直接使用我们具体定义的UTD标准化数据结构，例如跨应用拖拽场景。拖出方应用可以按照标准化数据结构将拖拽数据写入拖拽事件，拖入方应用从拖拽事件中读取拖拽数据并按照标准化数据结构进行数据的解析。这使得不同应用间的数据交互遵从相同的标准定义，有效减少了跨应用数据交互的开发工作量。
接口说明
UDMF针对部分标准化数据类型定义的标准化数据结构如下所示：
| 数据结构 | 数据类型 | 说明 |
| --- | --- | --- |
| PlainText | 'general.plain-text' | 纯文本 |
| Hyperlink | 'general.hyperlink' | 超链接 |
| HTML | 'general.html' | 富文本 |
| OpenHarmonyAppItem | 'openharmony.app-item' | 图标 |
| ContentForm | 'general.content-form' | 内容卡片 |
开发步骤
以使用标准化数据结构定义数据内容（包含超链接、纯文本两条数据记录）为例，提供基本的开发步骤。
```typescript
// 1. 导入unifiedDataChannel和uniformTypeDescriptor模块。
import { uniformDataStruct, uniformTypeDescriptor, unifiedDataChannel } from '@kit.ArkData';
// 2. 创建超链接数据记录。
let hyperlinkDetails : Record<string, string> = {
'attr1': 'value1',
'attr2': 'value2',
}
let hyperlink : uniformDataStruct.Hyperlink = {
uniformDataType:'general.hyperlink',
url : 'www.XXX.com',
description : 'This is the description of this hyperlink',
details : hyperlinkDetails,
}
hyperlink.description = '...';  // 修改hyperlink属性description
console.info(`hyperlink url = ${hyperlink.url}`);  // 访问对象属性。
// 3. 创建纯文本数据类型记录，将其添加到刚才创建的UnifiedData对象。
let plainTextDetails : Record<string, string> = {
'attr1': 'value1',
'attr2': 'value2',
}
let plainText : uniformDataStruct.PlainText = {
uniformDataType: 'general.plain-text',
textContent : 'This is plainText textContent example',
abstract : 'this is abstract',
details : plainTextDetails,
}
// 4. 创建一个统一数据对象实例。
let unifiedData = new unifiedDataChannel.UnifiedData();
let hyperlinkRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
let plainTextRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
// 5. 添加plainText数据记录。
unifiedData.addRecord(hyperlinkRecord);
unifiedData.addRecord(plainTextRecord);
// 6. 记录添加完成后，可获取当前UnifiedData对象内的所有数据记录。
let records = unifiedData.getRecords();
// 7. 遍历每条记录，判断该记录的数据类型，转换为子类对象，得到原数据记录。
for (let i = 0; i < records.length; i ++) {
let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
let record = unifiedDataRecord.getValue() as object;
if (record != undefined) {
// 读取该数据记录的类型
let type : string = record["uniformDataType"];
switch (type) {
case uniformTypeDescriptor.UniformDataType.HYPERLINK:
Object.keys(record).forEach(key => {
console.info('show records: ' + key + ', value:' + record[key]);
});
break;
case uniformTypeDescriptor.UniformDataType.PLAIN_TEXT:
Object.keys(record).forEach(key => {
console.info('show records: ' + key + ', value:' + record[key]);
});
break;
default:
break;
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uniform-data-type-list-V14
爬取时间: 2025-04-27 22:39:51
来源: Huawei Developer
标准化数据类型（Uniform Type Descriptor，简称UTD）用于解决系统中的类型模糊问题，即针对同一种数据类型，存在不同的类型描述方式：MIME Type、文件扩展名等。例如描述jpg/jpeg类型图片时，可以使用image/jpeg、.jpg、.jpeg或image/picture等方式进行描述。
当相关类型的数据进行跨应用、跨设备传输时，目标端应用/设备需要进行多方面的适配，才能够对数据内容进行相关处理，且存在无法识别的情况。
为了方便业务使用，系统中预置了一部分常用类型，从通用性、场景以及归属等角度将预置类型分为三类：基础类型，系统关联类型以及应用定义类型。
基础类型
基础类型表示通用数据类型，进行跨应用、跨设备设置跨平台交互时，能够被绝大多数应用、设备以及平台识别，标识ID为general.xxx。当前系统中预定义的通用类型列表如下：
| UTD-ID | BelongingTo类型 | 后缀名 | MIMEType类型 | 说明 |
| --- | --- | --- | --- | --- |
| general.entity | - | - | - | 所有表示物理存储类型的基类型 |
| general.object | - | - | - | 所有表示逻辑内容类型的基类型 |
| general.file | general.entity | - | - | 所有文件的基类型 |
| general.directory | general.entity | - | - | 所有目录的基类型 |
| general.folder | general.directory | - | - | 所有文件夹的基类型 |
| general.symlink | general.entity | - | - | 所有符号链接的基类型 |
| general.composite-object | general.object | - | - | 所有组合内容类型（例如PDF文件类型混合了文本和图片类数据）的基类型 |
| general.media | general.object | - | - | 所有媒体的基类型 |
| general.content-form | general.object | - | - | 数据内容卡片类型 |
| general.image | general.media | - | - | 所有图片的基类型 |
| general.png | general.image | .png | image/png | PNG图片类型 |
| general.jpeg | general.image | .jpg, .jpeg,.jpe | image/jpeg | JPEG图片类型 |
| general.tiff | general.image | .tif, .tiff | image/tiff | TIFF图片类型 |
| general.raw-image | general.image | - | - | 所有原始图像格式的基类型 |
| general.fax | general.image | - | - | 传真图像的基本类型 |
| general.xbitmap-image | general.image | .xbm | image/x-xbitmap,image/x-xbm | X Window系统（X11）中使用的位图图像格式 |
| general.gif | general.image | .gif | image/gif | GIF图片类型 |
| general.djvu-image | general.image | .djv,.djvu | image/vnd.djvu | DjVu图片类型 |
| general.jng-image | general.image | .jng | image/x-jng | JPEG网络图片类型 |
| general.pcx-image | general.image | .pcx | image/vnd.zbrush.pcx | 画笔位图图片类型 |
| general.pbm-image | general.image | .pbm | image/x-portable-bitmap | 可移植位图图片类型 |
| general.pgm-image | general.image | .pgm | image/x-portable-graymap | 可移植灰度图片类型 |
| general.pnm-image | general.image | .pnm | image/x-portable-anymap | 可移植任意图片类型 |
| general.ppm-image | general.image | .ppm | image/x-portable-pixmap | 可移植完整RGB图片类型 |
| general.rgb-image | general.image | .rgb | image/x-rgb | RGB位图类型 |
| general.svg-image | general.image | .svg,.svgz | image/svg+xml | 可扩展矢量图形类型 |
| general.wbmp-image | general.image | .wbmp | image/vnd.wap.wbmp | 无线位图类型 |
| general.xpixmap-image | general.image | .xpm | image/x-xpixmap | XMP图片类型 |
| general.xwindowdump-image | general.image | .xwd | image/x-xwindowdump | XWD图片类型 |
| general.heif | general.image | .heif, .heifs, .hif | image/heif | 高效图像文件格式 |
| general.heic | general.image | .heic, .heics | image/heic | 高效容器图像文件格式 |
| general.jpeg-2000 | general.image | .jp2, .jpg2, .jpx, .jpf, .jpm | image/jp2, image/jpx, image/jpm | JPEG 2000图片类型 |
| general.ief-image | general.image | .ief | image/ief | 图像交换格式 |
| general.video | general.media | - | - | 所有视频的基类型 |
| general.avi | general.video | .avi, .vfw | video/avi, video/msvideo, video/x-msvideo | AVI视频类型 |
| general.mpeg | general.video | .mpg, .mpeg, .m75, .m15,.mpe | video/mpg, video/mpeg, video/x-mpg, video/x-mpeg | MPEG-1或MPEG-2视频类型 |
| general.mpeg-4 | general.video | .mp4, .mp4v, .mpeg4 | video/mp4, video/mp4v | MPEG-4视频类型 |
| general.3gpp | general.video | .3gp, .3gpp | video/3gpp | 3GPP视频类型 |
| general.3gpp2 | general.video | .3g2, .3gp2, .3gpp2 | video/3gpp2 | 3GPP2视频类型 |
| general.vob | general.video | .vob | video/mpeg, video/x-ms-vob | DVD视频类媒体的容器类型 |
| general.dif-video | general.video | .dif | video/dv | 原始数字视频类型 |
| general.dv-video | general.video | .dv | video/dv | DV视频类型 |
| general.flc-animation | general.video | .fli, .flc | video/fli, video/flc | FLIC动画类型 |
| general.mng | general.video | .mng | video/x-mng | 多重图像网络图形类型 |
| general.mpegurl-video | general.video | .mxu, .m4u | video/vnd.mpegurl | 视频播放列表类型 |
| general.ts | general.video | .ts | video/mp2ts, video/mp2t | mpeg传输流格式 |
| general.mp2t | general.video | .m2ts, .mts, .m2t | video/mp2t | 蓝光BDAV 视频类型 |
| general.mpeg-2 | general.video | .mpeg2, .mpv2, .mp2v, .m2v, .mpv | video/mpeg | MPEG-2视频格式 |
| general.mpeg-1 | general.video | .mpeg1, .mpv1, .mp1v, .m1v | video/mpeg | MPEG-1视频格式 |
| general.divx-video | general.video | .divx | video/divx | DivX编码电影文件类型 |
| general.ogv | general.video | .ogv | video/ogg | Ogg视频格式 |
| general.h264-video | general.video | .h264 | video/H264 | H.264编码视频格式 |
| general.audio | general.media | - | - | 所有音频的基类型 |
| general.ogg | general.audio | .ogg | audio/ogg | OGG音频类型 |
| general.aiff | general.audio | .aiff | audio/aiff | AIFF音频类型 |
| general.pcm | general.audio | .pcm | audio/pcm | PCM音频类型 |
| general.flac | general.audio | .flac | audio/flac | FLAC音频类型 |
| general.alac | general.audio | .alac | audio/alac | ALAC音频类型 |
| general.mp3 | general.audio | .mp3 | audio/mp3 | MPEG-3音频类型 |
| general.aac | general.audio | .aac | audio/aac | AAC音频类型 |
| general.au-audio | general.audio | .au, .snd | audio/basic, audio/au, audio/snd | Au音频类型 |
| general.aifc-audio | general.audio | .aifc, .aif, .aiff | audio/x-aiff | 音频交换文件格式 |
| general.amr | general.audio | .amr | audio/amr | 自适应多速率音频编解码音频类型 |
| general.amr-wb | general.audio | .awb | audio/amr-wb | 自适应多速率宽带音频类型 |
| general.gsm | general.audio | .gsm | audio/x-gsm, audio/gsm | 全球移动音频格式 |
| general.imy | general.audio | .imy | audio/imelody | 非复调铃声交换对象格式音频 |
| general.kar | general.audio | .kar | audio/midi | 卡拉ok MIDI音频类型 |
| general.mpegurl-audio | general.audio | .m3u | audio/mpegurl,audio/x-mpegurl | 音频播放列表类型 |
| general.mpeg-4-audio | general.audio | .m4a, .m4b | audio/mpeg | 只有音频的MPEG-4类型 |
| general.midi-audio | general.audio | .mid, .midi | audio/midi | MIDI音频类型 |
| general.mp2 | general.audio | .mp2 | audio/mpeg | mp2音频类型 |
| general.mpeg-audio | general.audio | .mpga | audio/mpeg | MPEG音频类型 |
| general.mxmf | general.audio | .mxmf | audio/mobile-xmf | 移动XMF音频类型 |
| general.ota | general.audio | .ota | audio/midi | OTA 铃声音频类型 |
| general.pls | general.audio | .pls | audio/x-scpls | 多媒体播放列表类型 |
| general.rtttl | general.audio | .rtttl | audio/midi | RTTTL格式 |
| general.psid | general.audio | .sid, .psid | audio/prs.sid | SID音频类型 |
| general.ulaw-audio | general.audio | .au, .ulw, .snd | audio/basic, audio/au, audio/snd | μLaw音频类型 |
| general.xmf | general.audio | .xmf | audio/midi | 可扩展音乐文件类型 |
| general.ac3-audio | general.audio | .ac3 | audio/ac3 | 音频编解码器3文件格式 |
| general.archive | general.object | - | - | 所有文件和目录存档文件的基类型 |
| general.tar-archive | general.archive | .tar | application/x-tar, application/tar | TAR压缩文件类型 |
| general.zip-archive | general.archive | .zip | application/zip | Zip压缩文件类型 |
| general.disk-image | general.archive | - | - | 所有可作为卷装载项的文件类型的基类型 |
| general.bz2-archive | general.archive | .bz2, .bzip2 | application/x-bzip2 | BZ2存档文件类型 |
| general.opg | general.archive | .opg | - | OPG存档文件类型 |
| general.lha-archive | general.archive | .lha | application/x-lha | LHARC压缩文件类型 |
| general.lzh-archive | general.archive | .lzh | application/x-lzh | LZH压缩文件类型 |
| general.lzx-archive | general.archive | .lzx | application/x-lzx | LZX压缩文件类型 |
| general.shar-archive | general.archive | .shar | application/x-shar | Unix Shar压缩文件类型 |
| general.cpio-archive | general.archive | .cpio | application/x-cpio | Unix CPIO压缩文件类型 |
| general.web-archive | general.archive | .mht, .mhtml | application/x-mimearchive | 网页归档文件类型 |
| general.ustar | general.archive | .ustar | application/x-ustar | 统一的标准磁带归档格式类型 |
| general.taz-archive | general.tar-archive | .taz,.tar.z,.tz | application/x-gtar | TAZ压缩文件类型 |
| general.bz-archive | general.archive | .bz | application/x-bzip | Bzip压缩文件类型 |
| general.tar-bzip-archive | general.bz-archive | .tbz | application/x-bzip-compressed-tar | Bzip压缩后的TAR压缩文件类型 |
| general.tar-bzip2-archive | general.bz2-archive | .tbz2 | application/x-bzip2-compressed-tar | Bzip2压缩后的TAR压缩文件类型 |
| general.xar-archive | general.archive | .xar | application/x-xar | XAR压缩文件类型 |
| general.lza-archive | general.archive | .lza | application/x-lzh-compressed | LZA压缩文件类型 |
| general.arj-archive | general.archive | .arj | application/x-arj | ARJ压缩文件类型 |
| general.lzma-archive | general.archive | .lzma | application/x-lzma | LZMA压缩文件类型 |
| general.lzma86-archive | general.archive | .lzma86 | - | LZMA86压缩文件类型 |
| general.hfs-disk-image | general.disk-image | .hfs | - | HFS镜像文件类型 |
| general.img-disk-image | general.disk-image | .img | application/x-raw-disk-image | IMG镜像文件类型 |
| general.virtual-cd | general.disk-image | .vcd | application/x-cdlink | CD镜像文件类型 |
| general.iso | general.disk-image | .iso | application/x-iso9660-image | 光盘镜像文件类型 |
| general.text | general.object | - | - | 所有文本的基类型 |
| general.plain-text | general.text | .txt,.text | text/plain | 未指定编码的文本类型，无修饰的文本 |
| general.html | general.text | .html, .htm | text/html | HTML文本类型 |
| general.hyperlink | general.text | - | - | 超链接类型 |
| general.xml | general.text | .xml | text/xml | XML文本类型 |
| general.asc-text | general.text | .asc | text/plain | ASCII文本类型 |
| general.portable-object | general.text | .po | text/plain | 可移植对象类型 |
| general.rich-text | general.text | .rtf,.rtx | text/rtf, text/richtext | 富文本格式类型 |
| general.delimited-values-text | general.text | - | - | 带分隔符文本基类型 |
| general.diff | general.text | .diff | text/plain | 文本或源代码版本间差异描述数据类型 |
| general.setext | general.text | .etx | text/x-setext | 结构增强文本类型 |
| general.gcd | general.text | .gcd | text/x-pcs-gcd | 通用内容描述符 |
| general.p7r | general.text | .p7r | application/x-pkcs7-certreqresp | 证书请求响应文件类型 |
| general.pem | general.text | .pem | application/x-pem-file | 增强私隐邮件证书文件类型 |
| general.log | general.text | .log | text/plain | 日志文件类型 |
| general.tel | general.text | .tel |   | 包含器件封装、网络拓扑、编码信息等的原理图信息文件类型 |
| general.ion | general.text | .ion | text/plain | 文件内容描述类型 |
| general.conf | general.text | .conf | text/plain | 通用配置文件类型 |
| general.calendar | general.text | - | - | 所有日程类数据的基类型 |
| general.vcs | general.calendar | .vcs | text/calendar | VCalendar日历数据类型 |
| general.ics | general.calendar | .ics | text/calendar | ICalendar日历数据类型 |
| general.comma-separated-values-text | general.delimited-values-text | .csv | text/csv | 基于逗号分隔符文本类型 |
| general.tab-separated-values-text | general.delimited-values-text | .tsv | text/tab-separated-values | 基于Tab分隔符文本类型 |
| general.mathml | general.xml | .mml | text/mathml,application/mathml+xml | 数学标记语言文件类型 |
| general.xhtml | general.xml | .xhtml | application/xhtml+xml | 扩展超文本标识语言文件类型 |
| general.rss | general.xml | .rss | application/rss+xml | 丰富站点摘要 |
| general.rdf | general.xml | .rdf | application/rdf+xml | 资源描述框架文件类型 |
| general.source-code | general.text | - | - | 所有源代码的基类型 |
| general.markdown | general.text | .md, .markdown, .markdn, .mdown | text/markdown | Markdown数据类型 |
| general.chess-pgn | general.plain-text | .pgn | application/x-chess-pgn,application/vnd.chess-pgn | 可移植式棋局记号数据类型 |
| general.text-lst | general.plain-text | .lst | - | 数据列表类型 |
| general.c-source | general.source-code | .c | text/x-csrc | C源代码类型 |
| general.c-header | general.source-code | .h | text/x-chdr | C头文件类型 |
| general.c-plus-plus-source | general.source-code | .cp, .cpp, .c++, .cc, .cxx | text/x-c++src | C++源代码类型 |
| general.c-plus-plus-header | general.source-code | .hpp, .h++ , .hxx, .hh | text/x-c++hdr | C++头文件类型 |
| general.java-source | general.source-code | .java, .jav | text/x-java | Java源代码类型 |
| general.boo-source | general.source-code | .boo | text/x-boo | Boo源代码类型 |
| general.d-source | general.source-code | .d | text/x-dsrc | D源代码类型 |
| general.html-component | general.source-code | .htc | text/x-component | HTML组件类型 |
| general.pascal-source | general.source-code | .p,.pas | text/x-pascal | Pascal源代码类型 |
| general.tex | general.source-code | - | - | TeX源代码基类型 |
| general.dvi | general.tex | .dvi | application/x-dvi | 设备独立的数据类型 |
| general.script | general.source-code | - | - | 所有脚本语言源代码的基类型 |
| general.type-script | general.source-code | .ts | - | TypeScript源代码类型 |
| general.java-script | general.source-code | .js, .jscript, .javascript | text/javascript | JavaScript源代码类型 |
| general.css | general.script | .css | text/css | CSS样式表类型 |
| general.haskell-script | general.script | .hs | text/x-haskell | Haskell脚本类型 |
| general.literate-haskell-script | general.script | .lhs | text/x-literate-haskell | Literate Haskell脚本类型 |
| general.tcl-script | general.script | .tcl | text/x-tcl | TCL脚本类型 |
| general.json | general.script | .json | application/json | JSON数据类型 |
| general.yaml | general.script | .yaml, .yml | application/yaml | YAML文档类型 |
| general.shell-script | general.script | .sh, .command | text/x-shellscript | shell脚本类型 |
| general.ets | general.script | .ets |   | extended TypeScript源代码类型 |
| general.json5 | general.script | .json5 |   | JSON5数据交换类型 |
| general.csh-script | general.shell-script | .csh | text/x-csh | C-shell脚本类型 |
| general.perl-script | general.shell-script | .pl, .pm | text/x-perl-script | Perl脚本类型 |
| general.python-script | general.shell-script | .py | text/x-python-script | Python脚本类型 |
| general.ruby-script | general.shell-script | .rb, .rbw | text/ruby-script | Ruby脚本类型 |
| general.php-script | general.shell-script | .php, .php3, .php4, .ph3, .ph4, .phtml | text/x-php-script, text/php, application/php | PHP脚本类型 |
| general.uri | general.object | - | - | 统一资源标识符 |
| general.file-uri | general.uri | - | - | 统一文件资源标识符 |
| general.navigation | general.object | - | - | 所有导航类数据的基类型 |
| general.location | general.navigation | - | - | 导航定位类型 |
| general.database | general.object | - | - | 所有数据库文件的基类型 |
| general.vcard | general.object | .vcf, .vcard | text/vcard,text/x-vcard | 所有电子名片类数据的基类型 |
| general.message | general.object | - | - | 所有消息类数据的基类型 |
| general.contact | general.object | - | - | 所有联系人类数据的基类型 |
| general.executable | general.object | - | - | 所有可执行文件的基类型 |
| general.c-object | general.executable | .o | application/x-object | 编译后的C对象文件 |
| general.octet-stream | general.object | - | application/octet-stream - | 任意二进制数据类型 |
| general.mesh-model | general.object | .msh,.mesh,.silo | model/mesh | 三维网格模型数据类型 |
| general.certificate | general.object | - | - | 安全证书数据基类型 |
| general.cer-certificate | general.certificate | .cer | application/pkix-cert | 互联网安全证书 |
| general.crt-certificate | general.certificate | .crt | application/x-x509-ca-cert,application/x-x509-server-cert,application/x-x509-user-cert | 安全证书数据类型 |
| general.crl-certificate | general.certificate | .crl | application/x-pkix-crl | 证书吊销列表文件类型 |
| general.cad | general.object | - | - | 计算机辅助设计数据类型 |
| general.iges | general.cad | .iges,.igs | model/iges | IGES绘图数据类型 |
| general.font | general.object | - | - | 所有字体数据类型的基础类型 |
| general.truetype-font | general.font | .ttf | font/ttf | TrueType字体类型 |
| general.truetype-collection-font | general.font | .ttc | font/collection | TrueType collection字体类型 |
| general.opentype-font | general.font | .otf | font/otf | OpenType 字体类型 |
| general.ofd | general.composite-object | .ofd | - | 电子文件版式文档格式 |
| general.prn | general.composite-object | .prn | - | 打印到文件数据类型 |
| general.ebook | general.composite-object | - | - | 所有电子书文件格式的基类型 |
| general.epub | general.ebook | .epub | application/epub+zip | 电子出版物（EPUB）文件格式类型 |
系统关联类型
系统定义数据类型与具体的平台/操作系统有较为深入的关联，支持系统/平台内的跨应用交互，标识ID为os-name.xxx。当前系统中预定义的系统关联类型列表如下：
| UTD-ID | BelongingTo类型 | 后缀名 | MIMEType类型 | 说明 |
| --- | --- | --- | --- | --- |
| openharmony.form | general.object | - | - | HarmonyOS系统定义的Form类型 |
| openharmony.app-item | general.object | - | - | HarmonyOS系统定义的桌面图标类型 |
| openharmony.want | general.object | - | - | HarmonyOS系统定义的Want数据类型 |
| openharmony.atomic-service | general.object | - | - | HarmonyOS系统定义的元服务数据类型 |
| openharmony.package | general.directory | - | - | HarmonyOS系统定义的文件封装类型 |
| openharmony.hap | openharmony.package | .hap | - | HarmonyOS系统定义的Ability封装类型 |
| openharmony.app | openharmony.package | .app | - | HarmonyOS系统定义的应用包类型 |
| openharmony.hdoc | general.composite-object | .hdoc | - | HarmonyOS系统定义的备忘录文件格式。 |
| openharmony.hinote | general.composite-object | .hinote | - | HarmonyOS系统定义的笔记文件格式。 |
| openharmony.styled-string | general.composite-object | - | - | HarmonyOS系统定义的样式字符串类型 |
| openharmony.moving-photo | general.media | - | - | HarmonyOS系统定义的动图Moving Photo类型 |
| openharmony.pixel-map | general.image | - | - | HarmonyOS系统定义的Pixel map数据类型 |
| macos.dmg | general.disk-image | .dmg | application/x-apple-diskimage | MacOS系统定义的安装包格式文件类型 |
| debian.deb | general.archive | .deb,.udeb | application/x-debian-package,application/vnd.debian.binary-package | Debian系统中的软件安装包类型 |
| com.android.apk | general.archive | .apk, .apks, .aab, .xapk, .apkm, .akp | application/vnd.android.package-archive | Android安装包文件类型 |
| redhat.rpm-archive | general.archive | .rpm | application/x-rpm | RedHat软件安装包类型 |
| com.huawei.hmos.settings.wifi | general.text | .hmoswifi |   | HarmonyOS wifi分享配置文件类型 |
应用定义类型
应用定义类型表示该类型由具体的应用或者组织进行定义与维护，数据的交互依赖特定的应用进行识别，标识ID为com.company-name.xxx或org.orgnization-name.xxx。当前系统中预定义的应用定义类型列表如下：
| UTD-ID | BelongingTo类型 | 后缀名 | MIMEType类型 | 说明 |
| --- | --- | --- | --- | --- |
| com.microsoft.bmp | general.image | .bmp, .bm | image/bmp, image/x-ms-bmp | WINDOWS位图图像类型 |
| com.microsoft.ico | general.image | .ico | image/ico, image/x-icon | WINDOWS图标图像类型 |
| com.microsoft.advanced-systems-format | general.media | .asf | video/x-ms-asf, application/vnd.ms-asf | 微软高级流格式 |
| com.microsoft.waveform-audio | general.audio,com.microsoft.advanced-systems-format | .wav, .wave | audio/wav, audio/wave, audio/x-wav | WINDOWS波形音频类型 |
| com.microsoft.windows-media-wm | general.video,com.microsoft.advanced-systems-format | .wm | video/x-ms-wm | WINDOWS WM视频类型 |
| com.microsoft.windows-media-wmv | general.video,com.microsoft.advanced-systems-format | .wmv | video/x-ms-wmv | WINDOWS WMV视频类型 |
| com.microsoft.windows-media-wmp | general.video,com.microsoft.advanced-systems-format | .wmp | video/x-ms-wmp | WINDOWS WMP视频类型 |
| com.microsoft.windows-media-wma | general.audio,com.microsoft.advanced-systems-format | .wma | audio/x-ms-wma | Windows WMA音频类型. |
| com.microsoft.windows-media-wmx | general.video,com.microsoft.advanced-systems-format | .wmx | video/x-ms-wmx | WINDOWS WMX视频类型 |
| com.microsoft.windows-media-wvx | general.video,com.microsoft.advanced-systems-format | .wvx | video/x-ms-wvx | WINDOWS WVX视频类型 |
| com.microsoft.windows-media-wax | general.audio,com.microsoft.advanced-systems-format | .wax | audio/x-ms-wax | Windows WAX音频类型 |
| com.microsoft.windows-media-wmd | com.microsoft.advanced-systems-format, general.zip-archive | .wmd | application/x-ms-wmd | Windows Media下载包格式 |
| com.microsoft.windows-media-wmz | com.microsoft.advanced-systems-format, general.zip-archive | .wmz | application/x-ms-wmz | Windows Media Player皮肤存档格式 |
| com.microsoft.portable-executable | general.executable | .exe,.dll | application/vnd.microsoft.portable-executable | Microsoft Windows应用程序类型 |
| com.microsoft.windows-installer | general.executable | .msi | application/x-msi | Windows安装包文件格式 |
| com.microsoft.publisher.pub | general.composite-object | .pub | application/x-mspublisher | Windows Publisher文档格式 |
| com.microsoft.windows-media-playlist | general.xml,general.media | .wpl | application/vnd.ms-wpl | Windows Media Player播放列表 |
| com.microsoft.access.mdb | general.database | .mdb | application/msaccess | Microsoft Access数据库类型 |
| com.microsoft.hta | general.archive,general.executable | .hta | application/hta | HTML应用程序 |
| com.microsoft.internet.ins | general.text | .ins | application/x-internet-signup | 互联网服务文件格式 |
| com.microsoft.internet.isp | general.text | .isp | application/x-internet-signup | IIS互联网服务提供商配置文件格式 |
| com.microsoft.ini | general.text | .ini | - | Windows 初始化文件 |
| com.microsoft.email | general.message | .eml | message/rfc822 | 电子邮件类型 |
| com.microsoft.message | general.message | .msg | - | Outlook消息文件类型 |
| com.microsoft.pst | general.archive | .pst | - | Outlook数据文件 |
| com.microsoft.cab-archive | general.archive | .cab | application/vnd.ms-cab-compressed | Windows Cab文件类型 |
| com.microsoft.wim | general.disk-image | .wim | application/x-ms-wim | Windows镜像文件类型 |
| com.microsoft.swm | general.disk-image | .swm | application/x-ms-wim | Windows镜像文件分片类型 |
| com.microsoft.advanced-stream-redirector | general.video | .asx | video/x-ms-asf | 微软高级数据流转向器 |
| com.microsoft.cur | general.image | .cur | image/ico | Microsoft Windows鼠标指针图像 |
| com.microsoft.dds | general.image | .dds | image/vnd-ms.dds | DirectDraw Surface图像类型 |
| com.microsoft.metafile | general.composite-object | .wmf | - | Microsoft Windows的图形档案格式 |
| com.microsoft.word.doc | general.composite-object | .doc | application/msword | Microsoft Word数据类型 |
| com.microsoft.excel.xls | general.composite-object | .xls | application/vnd.ms-excel | Microsoft Excel数据类型 |
| com.microsoft.powerpoint.ppt | general.composite-object | .ppt | application/vnd.ms-powerpoint | Microsoft PowerPoint演示文稿类型 |
| com.microsoft.word.dot | general.composite-object | .dot | application/msword | Microsoft Word模板类型 |
| com.microsoft.powerpoint.pps | general.composite-object | .pps | application/vnd.ms-powerpoint | Microsoft PowerPoint演示文稿幻灯片放映类型 |
| com.microsoft.powerpoint.pot | general.composite-object | .pot | application/vnd.ms-powerpoint | Microsoft PowerPoint演示文稿模板类型 |
| com.microsoft.excel.xlt | general.composite-object | .xlt | application/vnd.ms-excel | Microsoft Excel模板类型 |
| com.microsoft.visio.vsd | general.composite-object | .vsd | application/vnd.visio | Microsoft Visio数据类型 |
| com.microsoft.excel.dif | general.composite-object | .dif | - | Microsoft Excel数据交换格式 |
| com.microsoft.lsf-video | general.video | .lsf, .lsx | video/x-la-asf | 流媒体格式 |
| org.openxmlformats.openxml | general.archive | - | - | Office Open XML文档基类型 |
| org.openxmlformats.wordprocessingml.document | org.openxmlformats.openxml, general.composite-object | .docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document | Office Open XML文档类型 |
| org.openxmlformats.spreadsheetml.sheet | org.openxmlformats.openxml, general.composite-object | .xlsx | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | Office Open XML电子表格类型 |
| org.openxmlformats.presentationml.presentation | org.openxmlformats.openxml, general.composite-object | .pptx | application/vnd.openxmlformats-officedocument.presentationml.presentation | Office Open XML演示文稿类型 |
| org.openxmlformats.drawingml.visio | org.openxmlformats.openxml, general.composite-object | .vsdx | application/vnd.openxmlformats-officedocument.drawingml.drawing | Office OpenXML Visio类型 |
| org.openxmlformats.wordprocessingml.template | org.openxmlformats.openxml, general.composite-object | .dotx | application/vnd.openxmlformats-officedocument.wordprocessingml.template | Office Open XML文档模板类型 |
| org.openxmlformats.presentationml.template | org.openxmlformats.openxml, general.composite-object | .potx | application/vnd.openxmlformats-officedocument.presentationml.template | Office Open XML演示文稿模板类型 |
| org.openxmlformats.presentationml.slideshow | org.openxmlformats.openxml, general.composite-object | .ppsx | application/vnd.openxmlformats-officedocument.presentationml.slideshow | Office Open XML幻灯片放映类型 |
| org.openxmlformats.spreadsheetml.template | org.openxmlformats.openxml, general.composite-object | .xltx | application/vnd.openxmlformats-officedocument.spreadsheetml.template | Office Open XML电子表格模板类型 |
| org.openxmlformats.drawingml.template | org.openxmlformats.openxml, general.composite-object | .vstx | - | Office OpenXML Visio模板类型 |
| org.openxmlformats.wordprocessingml.document.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .docm | application/vnd.ms-word.document.macroEnabled.12 | Office Open XML文档类型 (启用宏功能) |
| org.openxmlformats.wordprocessingml.template.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .dotm | application/vnd.ms-word.template.macroEnabled.12 | Office Open XML文档模板类型 (启用宏功能) |
| org.openxmlformats.spreadsheetml.template.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .xltm | application/vnd.ms-excel.template.macroEnabled.12 | Office Open XML电子表格模板类型 (启用宏功能) |
| org.openxmlformats.spreadsheetml.addin.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .xlam | application/vnd.ms-excel.addin.macroEnabled.12 | Office Open XML电子表格外接程序类型 (启用宏功能) |
| org.openxmlformats.spreadsheetml.binary.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .xlsb | application/vnd.ms-excel.sheet.binary.macroEnabled.12 | Office Open XML电子表格二进制类型 (启用宏功能) |
| org.openxmlformats.spreadsheetml.sheet.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .xlsm | application/vnd.ms-excel.sheet.macroEnabled.12 | Office Open XML电子表格类型 (启用宏功能) |
| org.openxmlformats.presentationml.addin.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .ppam | application/vnd.ms-powerpoint.addin.macroEnabled.12 | Office Open XML演示文稿外接程序类型(启用宏功能) |
| org.openxmlformats.presentationml.presentation.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .pptm | application/vnd.ms-powerpoint.presentation.macroEnabled.12 | Office Open XML演示文稿类型(启用宏功能) |
| org.openxmlformats.presentationml.slideshow.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .ppsm | application/vnd.ms-powerpoint.slideshow.macroEnabled.12 | Office Open XML幻灯片放映类型(启用宏功能) |
| org.openxmlformats.presentationml.template.macroenabled | org.openxmlformats.openxml, general.composite-object, general.executable | .potm | application/vnd.ms-powerpoint.template.macroEnabled.12 | Office Open XML演示文稿模板类型 (启用宏功能) |
| org.openxmlformats.drawingml.visio.macroenabled | org.openxmlformats.openxml, general.composite-object | .vsdm | - | Office OpenXML Visio类型（启用宏功能） |
| org.openxmlformats.drawingml.template.macroenabled | org.openxmlformats.openxml, general.composite-object | .vstm | - | Office OpenXML Visio模板类型（启用宏功能） |
| com.kingsoft.office | general.archive | - | - | Kingsoft办公文档基类型 |
| com.kingsoft.office.writer.wps | com.kingsoft.office,general.composite-object | .wps | - | Kingsoft文档类型 |
| com.kingsoft.office.writer.wpt | com.kingsoft.office,general.composite-object | .wpt | - | Kingsoft文档模板类型 |
| com.kingsoft.office.presentation.dps | com.kingsoft.office,general.composite-object | .dps | - | Kingsoft演示文稿类型 |
| com.kingsoft.office.presentation.template | com.kingsoft.office,general.composite-object | .dpt | - | Kingsoft演示文稿模板类型 |
| com.kingsoft.office.spreadsheets.et | com.kingsoft.office,general.composite-object | .et | - | Kingsoft电子表格类型 |
| com.kingsoft.office.spreadsheets.template | com.kingsoft.office,general.composite-object | .ett | - | Kingsoft电子表格模板类型 |
| com.kingsoft.office.spreadsheets.etx | com.kingsoft.office,general.composite-object | .etx | - | Kingsoft电子表格类型 |
| com.kingsoft.office.spreadsheets.ettx | com.kingsoft.office,general.composite-object | .ettx | - | Kingsoft电子表格模板类型 |
| org.oasis.opendocument | general.archive | - | - | OpenDocument文档基类型 |
| org.oasis.opendocument.text | org.oasis.opendocument, general.composite-object | .odt, .fodt | application/vnd.oasis.opendocument.text | OpenDocument文档类型. |
| org.oasis.opendocument.spreadsheet | org.oasis.opendocument, general.composite-object | .ods, .fods | application/vnd.oasis.opendocument.spreadsheet | OpenDocument电子表格类型 |
| org.oasis.opendocument.presentation | org.oasis.opendocument, general.composite-object | .odp, .fodp | application/vnd.oasis.opendocument.presentation | OpenDocument演示文档类型 |
| org.oasis.opendocument.graphics | org.oasis.opendocument, general.composite-object | .odg, .fodg | application/vnd.oasis.opendocument.graphics | OpenDocument图形类型 |
| org.oasis.opendocument.formula | org.oasis.opendocument | .odf | application/vnd.oasis.opendocument.formula | OpenDocument公式类型 |
| org.oasis-open.opendocument.chart | org.oasis.opendocument, general.composite-object | .odc | application/vnd.oasis.opendocument.chart | OpenDocument图表类型 |
| org.oasis-open.opendocument.text-master | org.oasis.opendocument, general.composite-object | .odm | application/vnd.oasis.opendocument.text-master | OpenDocument主文档类型 |
| org.oasis-open.opendocument.text-web | org.oasis.opendocument, general.composite-object | .oth | application/vnd.oasis.opendocument.text-web | OpenDocument HTML模板类型 |
| org.oasis-open.opendocument.database | org.oasis.opendocument, general.database | .odb | application/vnd.oasis.opendocument.database | OpenDocument数据库类型 |
| org.oasis-open.opendocument.image | org.oasis.opendocument, general.image | .odi | application/vnd.oasis.opendocument.image | OpenDocument图片类型 |
| org.oasis-open.opendocument.formula-template | org.oasis.opendocument, general.composite-object | .otf | application/vnd.oasis.opendocument.formula-template | OpenDocument公式模板类型 |
| org.oasis-open.opendocument.chart-template | org.oasis.opendocument, general.composite-object | .otc | application/vnd.oasis.opendocument.chart-template | OpenDocument图表模板类型 |
| org.oasis-open.opendocument.presentation-template | org.oasis.opendocument, general.composite-object | .otp | application/vnd.oasis.opendocument.presentation-template | OpenDocument演示文档模板类型 |
| org.oasis-open.opendocument.image-template | org.oasis.opendocument, general.image | .oti | application/vnd.oasis.opendocument.image-template | OpenDocument图片模板类型 |
| org.oasis-open.opendocument.graphics-template | org.oasis.opendocument, general.composite-object | .otg | application/vnd.oasis.opendocument.graphics-template | OpenDocument图形模板类型 |
| org.oasis-open.opendocument.spreadsheet-template | org.oasis.opendocument, general.composite-object | .ots | application/vnd.oasis.opendocument.spreadsheet-template | OpenDocument电子表格模板类型 |
| org.oasis-open.opendocument.text-template | org.oasis.opendocument, general.composite-object | .ott | application/vnd.oasis.opendocument.text-template | OpenDocument文档模板类型 |
| org.openoffice | general.archive | - | - | OpenOffice文档基类型 |
| org.openoffice.calc | org.openoffice, general.composite-object | .sxc | application/vnd.sun.xml.calc | OpenOffice计算电子表格类型 |
| org.openoffice.draw | org.openoffice, general.composite-object | .sxd | application/vnd.sun.xml.draw | OpenOffice绘图类型 |
| org.openoffice.writer-global | org.openoffice, general.composite-object | .sxg | application/vnd.sun.xml.writer.global | OpenOffice主文档类型 |
| org.openoffice.impress | org.openoffice, general.composite-object | .sxi | application/vnd.sun.xml.impress | OpenOffice演示文稿类型 |
| org.openoffice.math | org.openoffice, general.composite-object | .sxm | application/vnd.sun.xml.math | OpenOffice数学公式类型 |
| org.openoffice.writer | org.openoffice, general.composite-object | .sxw | application/vnd.sun.xml.writer | OpenOffice文档类型 |
| org.openoffice.calc.template | org.openoffice, general.composite-object | .stc | application/vnd.sun.xml.calc.template | OpenOffice计算电子表格模板类型 |
| org.openoffice.draw.template | org.openoffice, general.composite-object | .std | application/vnd.sun.xml.draw.template | OpenOffice绘图模板类型 |
| org.openoffice.impress.template | org.openoffice, general.composite-object | .sti | application/vnd.sun.xml.impress.template | OpenOffice演示文稿模板类型 |
| org.openoffice.writer.template | org.openoffice, general.composite-object | .stw | application/vnd.sun.xml.writer.template | OpenOffice文档模板类型 |
| com.staroffice | general.archive | - | - | StarOffice文档基类型 |
| com.staroffice.draw | com.staroffice, general.composite-object | .sda | application/vnd.stardivision.draw | StarOffice绘图类型 |
| com.staroffice.calc | com.staroffice, general.composite-object | .sdc | application/vnd.stardivision.calc | StarOffice计算电子表格类型 |
| com.staroffice.impress | com.staroffice, general.composite-object | .sdd,.sdp | application/vnd.stardivision.impress | StarOffice演示文稿类型 |
| com.staroffice.writer | com.staroffice, general.composite-object | .sdw | application/vnd.stardivision.writer | StarOffice文本文档类型 |
| com.staroffice.chart | com.staroffice, general.composite-object | .sds | application/vnd.stardivision.chart | StarOffice图表类型 |
| com.staroffice.mail | com.staroffice, general.composite-object | .sdm | application/vnd.stardivision.mail | StarOffice邮件消息类型 |
| com.staroffice.writer-global | com.staroffice, general.composite-object | .sgl | application/vnd.stardivision.writer-global | StarOffice主文档类型 |
| com.staroffice.math | com.staroffice, general.composite-object | .smf | application/vnd.stardivision.math | StarOffice数学公式类型 |
| com.staroffice.template | com.staroffice, general.composite-object | .vor | application/vnd.stardivision.template | StarOffice模板类型 |
| com.adobe.pdf | general.composite-object | .pdf | application/pdf | PDF数据类型 |
| com.adobe.postscript | general.composite-object | .ps | application/postscript | PostScript数据类型 |
| com.adobe.framemaker | general.composite-object | .book,.fm,.frame,.maker | application/x-maker | Adobe FrameMaker数据文件类型 |
| com.adobe.framemaker.mif | general.composite-object | .mif | application/vnd.mif | FrameMaker交换文件格式 |
| com.adobe.postscript-font | general.font | - | - | PostScript 字体类型 |
| com.adobe.postscript-pfb-font | com.adobe.postscript-font | .pfb | application/x-font | PostScript Font Binary字体类型 |
| com.adobe.postscript-pfa-font | com.adobe.postscript-font | .pfa | application/x-font | Adobe Type 1 字体类型 |
| com.adobe.encapsulated-postscript | com.adobe.postscript | .eps | - | Encapsulated PostScript类型 |
| com.adobe.photoshop-image | general.image | .psd | image/x-photoshop, image/photoshop, image/psd, application/photoshop | Adobe Photoshop图片类型 |
| com.adobe.illustrator.ai-image | general.image | .ai | - | Adobe Illustrator图片类型 |
| com.adobe.dcr | general.video | .dcr | application/x-director | Adobe Shockwave媒体文件类型 |
| com.adobe.dir | general.video | .dir | application/x-director | Adobe Director电影文件类型 |
| com.adobe.dxr | general.video | .dxr | application/x-director | 受保护（不可编辑）电影文件类型 |
| com.adobe.futuresplash | general.video | .spl | application/futuresplash, application/x-futuresplash | FutureSplash动画类型 |
| com.adobe.flash | general.video | .swf, .flv | application/x-shockwave-flash, video/x-flv | Flash视频类型 |
| com.adobe.f4v | general.video | .f4v | video/mp4 | Flash MP4视频文件格式 |
| com.adobe.dng-raw-image | general.raw-image | .dng | image/x-adobe-dng | 数字负片类型 |
| com.sun.java-class | general.executable | .class | - | Java类文件类型 |
| com.sun.java-archive | general.archive,general.executable | .jar | application/java-archive | JAVA存档文件类型 |
| com.sun.raster | general.image | .ras | image/x-cmu-raster | Sun Raster图像格式 |
| org.gnu.gnu-tar-archive | general.archive | .gtar | application/x-gtar | GUN存档文件类型 |
| org.gnu.gnu-zip-archive | general.archive | .gz, .gzip | application/x-gzip, application/gzip | GZIP存档文件类型 |
| org.gnu.gnu-zip-tar-archive | general.archive | .tgz | application/x-gtar | GZIP TAR存档文件类型 |
| org.gnu.texinfo | general.source-code | .texinfo,.texi | application/x-texinfo | GNU Texinfo源文件类型 |
| com.amazon.mobi | general.ebook | .mobi | application/x-mobipocket-ebook | MOBI电子书文件格式类型 |
| com.amazon.azw | general.ebook | .azw | application/vnd.amazon.ebook | AZW电子书文件格式类型 |
| com.amazon.azw3 | general.ebook | .azw3 | application/vnd.amazon.mobi8-ebook, application/x-mobi8-ebook | AZW3电子书文件格式类型 |
| com.amazon.kfx | general.ebook | .kfx | - | KFX电子书文件格式类型 |
| com.autodesk.dwg | general.composite-object | .dwg | image/vnd.dwg | AutoCAD绘图保存格式 |
| com.autodesk.dxf | general.composite-object | .dxf | image/vnd.dxf | AutoCAD绘图交换交流格式 |
| com.autodesk.dws | general.composite-object | .dws | - | AutoCAD绘图标准文件模板格式 |
| com.autodesk.dwt | general.composite-object | .dwt | - | AutoCAD绘图模板文件 |
| com.autodesk.dwf | general.composite-object | .dwf | model/vnd.dwf | AutoCAD网络文件格式 |
| com.autodesk.dwfx | general.composite-object | .dwfx | - | AutoCAD 2D/3D绘图的XPS文档格式 |
| com.autodesk.shp | general.composite-object | .shp | - | AutoCAD 3D矢量数据格式 |
| com.autodesk.shx | general.composite-object | .shx | - | AutoCAD创建的形状编译类型 |
| com.autodesk.slide-library | general.composite-object | .slb | - | AutoCAD幻灯片库文件格式 |
| com.autodesk.line | general.text | .lin | - | AutoCAD线型类型文件格式 |
| com.autodesk.plotter | general.composite-object | .plt | - | AutoCAD绘图文档 |
| org.tug.bib | general.tex | .bib | text/x-bibtex | TeX参考文献数据类型 |
| org.tug.cls | general.tex | .cls | text/x-tex | TeX类文件类型 |
| org.tug.sty | general.tex | .sty | text/x-tex | TeX样式文件类型 |
| org.tug.tex | general.tex | .tex | text/x-tex | TeX源文件类型 |
| org.latex-project.latex | general.tex | .ltx, .latex | application/x-latex | LaTeX源文件类型 |
| com.apple.media.playlist | general.media | .m3u8 | application/vnd.apple.mpegurl | UTF-8 M3U播放列表格式 |
| com.truevision.tga-image | general.image | .tga | image/targa, image/tga, application/tga | 标签图形（TaggedGraphics）图像类型 |
| com.sgi.sgi-image | general.image | .sgi | image/sgi | 硅图（Silicon Graphics）图像类型 |
| com.ilm.openexr-image | general.image | .exr | - | 开放标准的高动态范围图像格式类型 |
| com.kodak.flashpix.image | general.image | .fpx | image/fpx, application/vnd.fpx | FlashPix 图像文件类型 |
| com.coreldraw.cdr | general.image | .cdr | image/x-coreldraw | CorelDRAW矢量图类型 |
| com.coreldraw.cdt | general.image | .cdt | image/x-coreldrawtemplate | CorelDRAW矢量图模板类型 |
| com.coreldraw.cpt | general.image | .cpt | image/x-corelphotopaint | Corel PHOTO-PAINT图片类型 |
| com.coreldraw.pat | general.image | .pat | image/x-coreldrawpattern | CorelDRAW模式文件类型 |
| com.ea.iff-ilbm | general.image | .ilbm | image/x-ilbm | 交错位图图像类型 |
| org.aomedia.avif-image | general.image | .avif | image/avif | AVIF图片类型 |
| com.google.webp | general.image | .webp | image/webp | WebP图像格式 |
| org.gimp.xcf | general.image | .xcf | application/x-xcf,image/x-xcf | GIMP图像类型 |
| com.aol.art-image | general.image | .art | image/x-jg | ART图像格式 |
| com.real.realmedia | general.video | .rm | application/vnd.rn-realmedia | 流媒体视频类型 |
| com.real.realmedia-vbr | general.video | .rmvb | application/vnd.rn-realmedia-vbr | RealMedia可变比特率格式 |
| com.real.realvideo | general.video | .rv | video/x-pn-realvideo | RealVideo格式 |
| org.matroska.mkv | general.video | .mkv | video/x-matroska | Matroska视频类型 |
| com.sgi.movie | general.video | .movie | video/x-sgi-movie | SGI电影格式 |
| org.webmproject.webm | general.video | .webm | video/webm | WebM音视频媒体类型 |
| com.apple.m4v | general.video | .m4v | video/m4v | M4V视频类型 |
| com.apple.quicktime-movie | general.video | .mov,.qt,.movie | video/quicktime | QuickTime视频类型 |
| com.apple.m4p-audio | general.audio | .m4p | audio/mp4 | iTunes音乐商店音频文件格式 |
| com.real.realaudio | general.audio | .ram, .ra | audio/vnd.rn-realaudio, audio/x-pn-realaudio | RealMedia音频类型 |
| com.digidesign.sd2-audio | general.audio | .sd2 | audio/x-sd2 | 单声道/立体声音频类型（Digidesign Sound Designer II） |
| org.matroska.mka | general.audio | .mka | audio/x-matroska | Matroska音频类型 |
| com.yamaha.smaf | general.audio | .mmf | application/vnd.smaf | 合成音乐移动应用程序格式 |
| org.xiph.ogg | general.audio | .oga,.ogg | application/ogg | Ogg Vorbis音频格式 |
| com.sseyo.koan-audio | general.audio | .skd,.skm, .skp, .skt | application/x-koan | Koan互联网音乐文件格式 |
| com.j2.jfx-fax | general.fax | .jfx | - | J2 jConnect传真文件类型 |
| com.js.efx-fax | general.fax | .efx | image/efax | 电子传真文件类型 |
| com.canon.cr2-raw-image | general.raw-image | .cr2 | image/x-canon-cr2 | 佳能Raw 2图像 |
| com.canon.cr3-raw-image | general.raw-image | .cr3 | image/x-canon-cr3 | 佳能Raw 3图像 |
| com.canon.crw-raw-image | general.raw-image | .crw | image/x-canon-crw | 佳能Raw CIFF图像文件 |
| com.sony.arw-raw-image | general.raw-image | .arw | image/x-sony-arw | Sony数码相机原始图像格式 |
| com.nikon.nef-raw-image | general.raw-image | .nef | image/x-nikon-nef | Nikon数码相机原始图像格式 |
| com.nikon.nrw-raw-image | general.raw-image | .nrw | image/x-nikon-nrw | Nikon原始图像格式 |
| com.apple.webarchive | general.archive | .webarchive | application/x-webarchive | Safari Web存档文件格式 |
| com.apple.binhex-archive | general.archive | .hqx | application/mac-binhex40 | BinHex 4.0编码文件格式 |
| com.apple.quicktime-link | general.text | .qtl | application/x-quicktimeplayer | QuickTime链接文件类型 |
| org.troff | general.text | .man,.t, .roff | text/troff | Unix troff格式 |
| com.wolfram.mathematica.notebook | general.text | .nb | application/mathematica | Mathematica笔记本文件格式 |
| com.red-bean.sgf | general.text | .sgf | application/x-go-sgf | Smart Game棋盘游戏记录文件 |
| org.bittorrent.torrent | general.text | .torrent | application/x-bittorrent | BitTorrent文件类型 |
| com.spatial.acis.sat | general.text | .sat | - | ACIS三维模型类型 |
| com.netscape.proxy-autoconfig | general.plain-text | .pac | application/x-ns-proxy-autoconfig | 代理自动配置文件类型 |
| io.qt.moc | general.source-code | .moc | text/x-moc | Qt元对象编译文件格式 |
| org.gnumeric.spreadsheet | general.xml | .gnumeric | application/x-gnumeric | Gnumeric电子表格类型 |
| com.real.smil | general.xml | .smil | application/smil | 同步多媒体集成语言类型 |
| com.ghostscript.font | general.font | .gsf | application/x-font | Ghostscript字体格式 |
| org.x.pcf-font | general.font | .pcf | application/x-font,application/x-font-pcf | PCF字体格式 |
| org.openpgp.signature | general.object | .pgp | application/pgp-signature | PGP安全密钥类型 |
| org.hdfgroup.hdf | general.composite-object | .hdf | application/x-hdf | 分层数据格式 |
| com.edrawsoft.edrawmax | general.composite-object | .eddx | application/x-eddx | Edraw Max绘图格式 |
| com.edrawsoft.edrawmind | general.composite-object | .emmx | application/x-emmx | Edraw MindMaster绘图格式 |
| net.cnki.caj | general.composite-object | .caj | application/caj | CAJ学术期刊文件格式 |
| com.mindjet.mindmanager.mmap | general.composite-object | .mmap | - | MindManager思维导图格式 |
| com.hp.graphics-language | general.composite-object | .hpgl | application/vnd.hp-hpgl | HP图形语言绘图格式 |
| com.wolfram.cdf | general.composite-object | .cdf | application/x-cdf | Wolfram可计算的文档格式 |
| de.cinderella.cdy | general.composite-object | .cdy | application/vnd.cinderella | Cinderella结构文件格式 |
| com.3dsystems.stereolithography | general.composite-object | .stl | application/vnd.ms-pki.stl | Stereolithography三维文件格式 |
| com.abisource.word | general.composite-object | .abw | application/x-abiword | AbiWord文档类型 |
| io.sourceforge.freemind | general.composite-object | .mm | application/x-freemind | FreeMind思维导图文件格式 |
| com.idsoftware.doom | general.archive | .wad | application/x-doom | Doom WAD 游戏数据文件类型 |
| com.android.webarchive | general.archive | .webarchivexml | application/x-webarchive-xml | Android Web存档文件格式 |
| com.rarlab.rar-archive | general.archive | .rar | application/rar,application/vnd.rar | WinRAR压缩文档类型 |
| org.7-zip.7-zip-archive | general.archive | .7z | application/x-7z-compressed | 7-zip压缩文档类型 |
| com.rsa.pkcs-12 | general.archive | .pfx,.p12 | application/x-pkcs12 | PKCS #12 证书文件类型 |
| com.stuffit.sit-archive | general.archive | .sit | application/x-stuffit | StuffIt压缩文件格式 |
| com.allume.stuffit-archive | general.archive | .sit, .sitx | application/x-stuffit, application/x-sit , application/stuffit | Stuffit压缩格式类型（Stuffit archive） |
| org.tukaani.xz-archive | general.archive | .xz | application/x-xz | XZ压缩文件类型 |
| org.tukaani.tar-xz-archive | org.tukaani.xz-archive | .txz | application/x-xz-compressed-tar | XZ压缩后的TAR压缩文件类型 |
| com.winzip.zipx | general.archive | .zipx | - | ZIPX压缩文件类型 |
| org.godotengine.tpz-archive | general.archive | .tpz | - | Godot引擎导出文件类型 |
| org.mozilla.xpinstall | general.archive | .xpi | application/x-xpinstall | 压缩文件类型 |
| com.ezbsystems.zipped-iso | general.disk-image | .isz | - | Zip压缩后的ISO镜像文件类型 |
| com.dbase.dbf | general.database | .dbf | application/dbf, application/dbase | 数据库文件格式 |
| com.youtube.video | general.video | .yt, .vt | video/vnd.youtube.yt | Youtube视频格式 |
| com.cisco.webex-video | general.video | .wrf | video/x-webex | WebEx录制格式 |
| org.csiro.annodex | general.video | .axv | video/annodex | Annodex视频格式 |
| com.fujifilm.raf-raw-image | general.raw-image | .raf | image/x-fuji-raf | Fujifilm原始图像格式 |
| com.panasonic.rw2-raw-image | general.raw-image | .rw2, .raw | image/x-panasonic-raw | Panasonic原始图像格式 |
| com.pentax.pef-raw-image | general.raw-image | .pef | image/x-pentax-pef | Pentax电子原始图像格式 |
| com.sumsung.srw-raw-image | general.raw-image | .srw | image/x-samsung-srw | Samsung原始图像格式 |
| com.epson.erf-raw-image | general.raw-image | .erf | image/x-epson-erf | Epson原始图像格式 |
| com.olympus.orf-raw-image | general.raw-image | .orf | image/x-olympus-orf | Olympus原始图像格式 |
| org.w3.woff | general.font | .woff | font/woff | Web开放字体格式类型 |
| org.sqlite.database | general.database | .sqlite, .sqlite3, .db, .db3, .s3db, .sl3 | application/vnd.sqlite3 | SQLite 数据库类型 |
| com.microsoft.pdb | general.database | .pdb | application/x-ms-pdb | 程序数据库类型 |
| com.monkeysaudio.ape-audio | general.audio | .pdb | audio/x-monkeys-audio | Monkey's Audio音频类型 |
| org.xiph.opus-audio | general.audio | .opus | audio/opus | Opus有损音频编码格式 |
| com.microsoft.tlb | general.object | .tlb |   | OLE类型库类型 |
| com.microsoft.catalog | general.object | .cat |   | Windows目录文件类型 |
| com.microsoft.vbscript | general.script | .vbs | application/x-vbs | VBScript脚本类型 |
| com.microsoft.sys | general.object | .sys |   | Windows系统文件类型 |
| com.microsoft.powershell-script | general.script | .ps1 |   | Windows PowerShell脚本类型 |
| com.microsoft.registry | general.database | .reg |   | DOS批处理文件类型 |
| com.microsoft.dos-batch | general.script | .bat | application/x-bat | Windows注册表类型 |
| com.microsoft.inf | general.text | .inf | text/plain | 安装信息文件 |
| com.microsoft.sccd | general.xml | .sccd |   | 签名自定义功能描述符 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-data-persistence-V14
爬取时间: 2025-04-27 22:40:05
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-data-persistence-overview-V14
爬取时间: 2025-04-27 22:40:18
来源: Huawei Developer
应用数据持久化，是指应用将内存中的数据通过文件或数据库的形式保存到设备上。内存中的数据形态通常是任意的数据结构或数据对象，存储介质上的数据形态可能是文本、数据库、二进制文件等。
HarmonyOS标准系统支持典型的存储数据形态，包括用户首选项、键值型数据库、关系型数据库。
开发者可以根据如下功能介绍，选择合适的数据形态以满足自己应用数据的持久化需要。
-  用户首选项（Preferences）：通常用于保存应用的配置信息。数据通过文本的形式保存在设备中，应用使用过程中会将文本中的数据全量加载到内存中，所以访问速度快、效率高，但不适合需要存储大量数据的场景。
-  键值型数据库（KV-Store）：一种非关系型数据库，其数据以“键值”对的形式进行组织、索引和存储，其中“键”作为唯一标识符。适合很少数据关系和业务关系的业务数据存储，同时因其在分布式场景中降低了解决数据库版本兼容问题的复杂度，和数据同步过程中冲突解决的复杂度而被广泛使用。相比于关系型数据库，更容易做到跨设备跨版本兼容。
-  关系型数据库（RelationalStore）：一种关系型数据库，以行和列的形式存储数据，广泛用于应用中的关系型数据的处理，包括一系列的增、删、改、查等接口，开发者也可以运行自己定义的SQL语句来满足复杂业务场景的需要。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-persistence-by-preferences-V14
爬取时间: 2025-04-27 22:40:32
来源: Huawei Developer
场景介绍
用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。当用户希望有一个全局唯一存储的地方，可以采用用户首选项来进行存储。Preferences会将该数据缓存在内存中，当用户读取的时候，能够快速从内存中获取数据，当需要持久化时可以使用flush接口将内存中的数据写入持久化文件中。Preferences会随着存放的数据量越多而导致应用占用的内存越大，因此，Preferences不适合存放过多的数据，也不支持通过配置加密，适用的场景一般为应用保存用户的个性化设置（字体大小，是否开启夜间模式）等。
运作机制
如图所示，用户程序通过ArkTS接口调用用户首选项读写对应的数据文件。开发者可以将用户首选项持久化文件的内容加载到Preferences实例，每个文件唯一对应到一个Preferences实例，系统会通过静态容器将该实例存储在内存中，直到主动从内存中移除该实例或者删除该文件。
应用首选项的持久化文件保存在应用沙箱内部，可以通过context获取其路径。具体可见获取应用文件路径。
图1用户首选项运作机制
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170227.69244540156366446394746091021814:50001231000000:2800:EAE0C4BEF9B1DB70F76E267A7740F6D1FE8C64C11D6EF9F462CC8B42671D42F7.jpg)
约束限制
-  首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。
-  Key键为string类型，要求非空且长度不超过1024个字节。
-  如果Value值为string类型，请使用UTF-8编码格式，可以为空，不为空时长度不超过16MB。
-  当存储的数据中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。
-  当调用removePreferencesFromCache或者deletePreferences后，订阅的数据变更会主动取消订阅，重新getPreferences后需要重新订阅数据变更。
-  不允许deletePreferences与其他接口多线程、多进程并发调用，否则会发生不可预期行为。
-  内存会随着存储数据量的增大而增大，所以存储的数据量应该是轻量级的，建议存储的数据不超过50MB，当存储的数据较大时，在使用同步接口创建Preferences对象和持久化数据时会变成耗时操作，不建议在主线程中使用，否则可能出现appfreeze问题。
接口说明
以下是用户首选项持久化功能的相关接口，更多接口及使用方式请见用户首选项。
| 接口名称 | 描述 |
| --- | --- |
| getPreferencesSync(context: Context, options: Options): Preferences | 获取Preferences实例。该接口存在异步接口。 |
| putSync(key: string, value: ValueType): void | 将数据写入Preferences实例，可通过flush将Preferences实例持久化。该接口存在异步接口。 |
| hasSync(key: string): boolean | 检查Preferences实例是否包含名为给定Key的存储键值对。给定的Key值不能为空。该接口存在异步接口。 |
| getSync(key: string, defValue: ValueType): ValueType | 获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。该接口存在异步接口。 |
| deleteSync(key: string): void | 从Preferences实例中删除名为给定Key的存储键值对。该接口存在异步接口。 |
| flush(callback: AsyncCallback<void>): void | 将当前Preferences实例的数据异步存储到用户首选项持久化文件中。 |
| on(type: 'change', callback: Callback<string>): void | 订阅数据变更，订阅的数据发生变更后，在执行flush方法后，触发callback回调。 |
| off(type: 'change', callback?: Callback<string>): void | 取消订阅数据变更。 |
| deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void | 从内存中移除指定的Preferences实例。若Preferences实例有对应的持久化文件，则同时删除其持久化文件。 |
开发步骤
1.  导入@kit.ArkData模块。
```typescript
import { preferences } from '@kit.ArkData';
```
2.  获取Preferences实例。
```typescript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
let dataPreferences: preferences.Preferences | null = null;
class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage) {
let options: preferences.Options = { name: 'myStore' };
dataPreferences = preferences.getPreferencesSync(this.context, options);
}
}
```
3.  写入数据。 使用putSync()方法保存数据到缓存的Preferences实例中。在写入数据后，如有需要，可使用flush()方法将Preferences实例的数据存储到持久化文件。 当对应的键已经存在时，putSync()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。 示例代码如下所示：
```typescript
import { util } from '@kit.ArkTS';
if (dataPreferences.hasSync('startup')) {
console.info("The key 'startup' is contained.");
} else {
console.info("The key 'startup' does not contain.");
// 此处以此键值对不存在时写入数据为例
dataPreferences.putSync('startup', 'auto');
// 当字符串有特殊字符时，需要将字符串转为Uint8Array类型再存储
let uInt8Array1 = new util.TextEncoder().encodeInto("~！@#￥%……&*（）——+？");
dataPreferences.putSync('uInt8', uInt8Array1);
}
```
4.  读取数据。 使用getSync()方法获取数据，即指定键对应的值。如果值为null或者非默认值类型，则返回默认数据。 示例代码如下所示：
```typescript
let val = dataPreferences.getSync('startup', 'default');
console.info("The 'startup' value is " + val);
// 当获取的值为带有特殊字符的字符串时，需要将获取到的Uint8Array转换为字符串
let uInt8Array2 : preferences.ValueType = dataPreferences.getSync('uInt8', new Uint8Array(0));
let textDecoder = util.TextDecoder.create('utf-8');
val = textDecoder.decodeToString(uInt8Array2 as Uint8Array);
console.info("The 'uInt8' value is " + val);
```
5.  删除数据。 使用deleteSync()方法删除指定键值对，示例代码如下所示：
```typescript
dataPreferences.deleteSync('startup');
```
6.  数据持久化。 应用存入数据到Preferences实例后，可以使用flush()方法实现数据持久化。示例代码如下所示：
```typescript
dataPreferences.flush((err: BusinessError) => {
if (err) {
console.error(`Failed to flush. Code:${err.code}, message:${err.message}`);
return;
}
console.info('Succeeded in flushing.');
})
```
7.  订阅数据变更。 应用订阅数据变更需要指定observer作为回调方法。订阅的Key值发生变更后，当执行flush()方法时，observer被触发回调。示例代码如下所示：
```typescript
let observer = (key: string) => {
console.info('The key' + key + 'changed.');
}
dataPreferences.on('change', observer);
// 数据产生变更，由'auto'变为'manual'
dataPreferences.put('startup', 'manual', (err: BusinessError) => {
if (err) {
console.error(`Failed to put the value of 'startup'. Code:${err.code},message:${err.message}`);
return;
}
console.info("Succeeded in putting the value of 'startup'.");
if (dataPreferences !== null) {
dataPreferences.flush((err: BusinessError) => {
if (err) {
console.error(`Failed to flush. Code:${err.code}, message:${err.message}`);
return;
}
console.info('Succeeded in flushing.');
})
}
})
```
8.  删除指定文件。 使用deletePreferences()方法从内存中移除指定文件对应的Preferences实例，包括内存中的数据。若该Preference存在对应的持久化文件，则同时删除该持久化文件，包括指定文件及其备份文件、损坏文件。 调用该接口后，应用不允许再使用该Preferences实例进行数据操作，否则会出现数据一致性问题。 成功删除后，数据及文件将不可恢复。 示例代码如下所示：
```typescript
preferences.deletePreferences(this.context, options, (err: BusinessError) => {
if (err) {
console.error(`Failed to delete preferences. Code:${err.code}, message:${err.message}`);
return;
}
console.info('Succeeded in deleting preferences.');
})
```
9.  调用该接口后，应用不允许再使用该Preferences实例进行数据操作，否则会出现数据一致性问题。
10.  成功删除后，数据及文件将不可恢复。
-  调用该接口后，应用不允许再使用该Preferences实例进行数据操作，否则会出现数据一致性问题。
-  成功删除后，数据及文件将不可恢复。
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-persistence-by-kv-store-V14
爬取时间: 2025-04-27 22:40:46
来源: Huawei Developer
场景介绍
键值型数据库存储键值对形式的数据，当需要存储的数据没有复杂的关系模型，比如存储商品名称及对应价格、员工工号及今日是否已出勤等，由于数据复杂度低，更容易兼容不同数据库版本和设备类型，因此推荐使用键值型数据库持久化此类数据。
约束限制
-  设备协同数据库，针对每条记录，Key的长度≤896 Byte，Value的长度<4 MB。
-  单版本数据库，针对每条记录，Key的长度≤1 KB，Value的长度<4 MB。
-  每个应用程序最多支持同时打开16个键值型分布式数据库。
-  键值型数据库事件回调方法中不允许进行阻塞操作，例如修改UI组件。
接口说明
以下是键值型数据库持久化功能的相关接口，大部分为异步接口。异步接口均有callback和Promise两种返回形式，下表均以callback形式为例，更多接口及使用方式请见分布式键值数据库。
| 接口名称 | 描述 |
| --- | --- |
| createKVManager(config: KVManagerConfig): KVManager | 创建一个KVManager对象实例，用于管理数据库对象。 |
| getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void | 指定options和storeId，创建并得到指定类型的KVStore数据库。 |
| put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void | 添加指定类型的键值对到数据库。 |
| get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void | 获取指定键的值。 |
| delete(key: string, callback: AsyncCallback<void>): void | 从数据库中删除指定键值的数据。 |
| closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void | 通过storeId的值关闭指定的分布式键值数据库。 |
| deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void | 通过storeId的值删除指定的分布式键值数据库。 |
开发步骤
1.  若要使用键值型数据库，首先要获取一个KVManager实例，用于管理数据库对象。示例代码如下所示： Stage模型示例： FA模型示例：
2.  创建并获取键值数据库。示例代码如下所示：
3.  调用put()方法向键值数据库中插入数据。示例代码如下所示： 当Key值存在时，put()方法会修改其值，否则新增一条数据。
4.  调用get()方法获取指定键的值。示例代码如下所示：
5.  调用delete()方法删除指定键值的数据。示例代码如下所示：
6.  通过storeId的值关闭指定的分布式键值数据库。示例代码如下所示：
7.  通过storeId的值删除指定的分布式键值数据库。示例代码如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-persistence-by-rdb-store-V14
爬取时间: 2025-04-27 22:41:00
来源: Huawei Developer
场景介绍
关系型数据库基于SQLite组件，适用于存储包含复杂关系数据的场景，比如一个班级的学生信息，需要包括姓名、学号、各科成绩等，又或者公司的雇员信息，需要包括姓名、工号、职位等，由于数据之间有较强的对应关系，复杂程度比键值型数据更高，此时需要使用关系型数据库来持久化保存数据。
大数据量场景下查询数据可能会导致耗时长甚至应用卡死，如有相关操作可参考文档批量数据写数据库场景，且有建议如下：
基本概念
-  谓词：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。
-  结果集：指用户查询之后的结果集合，可以对数据进行访问。结果集提供了灵活的数据访问方式，可以更方便地拿到用户想要的数据。
运作机制
关系型数据库对应用提供通用的操作接口，底层使用SQLite作为持久化存储引擎，支持SQLite具有的数据库特性，包括但不限于事务、索引、视图、触发器、外键、参数化查询和预编译SQL语句。
图1关系型数据库运作机制
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170227.21025910735781447012222071412403:50001231000000:2800:486CFCE01EE21CB8E83927C8D653F8106FCB9171ED6CF901991AB8385EAE24E5.jpg)
约束限制
-  系统默认日志方式是WAL（Write Ahead Log）模式，系统默认落盘方式是FULL模式。
-  数据库中有4个读连接和1个写连接，线程获取到空闲读连接时，即可进行读取操作。当没有空闲读连接且有空闲写连接时，会将写连接当做读连接来使用。
-  为保证数据的准确性，数据库同一时间只能支持一个写操作。
-  当应用被卸载完成后，设备上的相关数据库文件及临时文件会被自动清除。
-  ArkTS侧支持的基本数据类型：number、string、二进制类型数据、boolean。
-  为保证插入并读取数据成功，建议一条数据不要超过2M。超出该大小，插入成功，读取失败。
接口说明
以下是关系型数据库持久化功能的相关接口，大部分为异步接口。异步接口均有callback和Promise两种返回形式，下表均以callback形式为例，更多接口及使用方式请见关系型数据库。
| 接口名称 | 描述 |
| --- | --- |
| getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void | 获得一个RdbStore，操作关系型数据库，用户可以根据自己的需求配置RdbStore的参数，然后通过RdbStore调用相关接口可以执行相关的数据操作。 |
| executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>):void | 执行包含指定参数但不返回值的SQL语句。 |
| insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>):void | 向目标表中插入一行数据。 |
| update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>):void | 根据predicates的指定实例对象更新数据库中的数据。 |
| delete(predicates: RdbPredicates, callback: AsyncCallback<number>):void | 根据predicates的指定实例对象从数据库中删除数据。 |
| query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>):void | 根据指定条件查询数据库中的数据。 |
| deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void | 删除数据库。 |
开发步骤
因Stage模型、FA模型的差异，个别示例代码提供了在两种模型下的对应示例；示例代码未区分模型或没有对应注释说明时默认在两种模型下均适用。
关系库数据库操作或者存储过程中，有可能会因为各种原因发生非预期的数据库异常情况（抛出14800011），此时需要对数据库进行重建并恢复数据，以保障正常的应用开发，具体可见关系型数据库异常重建。
1.  使用关系型数据库实现数据持久化，需要获取一个RdbStore，其中包括建库、建表、升降级等操作。示例代码如下所示： Stage模型示例： FA模型示例： 应用创建的数据库与其上下文（Context）有关，即使使用同样的数据库名称，但不同的应用上下文，会产生多个数据库，例如每个UIAbility都有各自的上下文。 当应用首次获取数据库（调用getRdbStore）后，在应用沙箱内会产生对应的数据库文件。使用数据库的过程中，在与数据库文件相同的目录下可能会产生以-wal和-shm结尾的临时文件。此时若开发者希望移动数据库文件到其它地方使用查看，则需要同时移动这些临时文件，当应用被卸载完成后，其在设备上产生的数据库文件及临时文件也会被移除。 错误码的详细介绍请参见通用错误码和关系型数据库错误码。
```typescript
import { relationalStore } from '@kit.ArkData'; // 导入模块
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
// 此处示例在Ability中实现，使用者也可以在其他合理场景中使用
class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage) {
const STORE_CONFIG :relationalStore.StoreConfig= {
name: 'RdbTest.db', // 数据库文件名
securityLevel: relationalStore.SecurityLevel.S3, // 数据库安全级别
encrypt: false, // 可选参数，指定数据库是否加密，默认不加密
customDir: 'customDir/subCustomDir', // 可选参数，数据库自定义路径。数据库将在如下的目录结构中被创建：context.databaseDir + '/rdb/' + customDir，其中context.databaseDir是应用沙箱对应的路径，'/rdb/'表示创建的是关系型数据库，customDir表示自定义的路径。当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。
isReadOnly: false // 可选参数，指定数据库是否以只读方式打开。该参数默认为false，表示数据库可读可写。该参数为true时，只允许从数据库读取数据，不允许对数据库进行写操作，否则会返回错误码801。
};
// 判断数据库版本，如果不匹配则需进行升降级操作
// 假设当前数据库版本为3，表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, IDENTITY)
const SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT)'; // 建表Sql语句, IDENTITY为bigint类型，sql中指定类型为UNLIMITED INT
relationalStore.getRdbStore(this.context, STORE_CONFIG, (err, store) => {
if (err) {
console.error(`Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
return;
}
console.info('Succeeded in getting RdbStore.');
// 当数据库创建时，数据库默认版本为0
if (store.version === 0) {
store.executeSql(SQL_CREATE_TABLE); // 创建数据表
// 设置数据库的版本，入参为大于0的整数
store.version = 3;
}
// 如果数据库版本不为0且和当前数据库版本不匹配，需要进行升降级操作
// 当数据库存在并假定版本为1时，例应用从某一版本升级到当前版本，数据库需要从1版本升级到2版本
if (store.version === 1) {
// version = 1：表结构：EMPLOYEE (NAME, SALARY, CODES, ADDRESS) => version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS)
(store as relationalStore.RdbStore).executeSql('ALTER TABLE EMPLOYEE ADD COLUMN AGE INTEGER');
store.version = 2;
}
// 当数据库存在并假定版本为2时，例应用从某一版本升级到当前版本，数据库需要从2版本升级到3版本
if (store.version === 2) {
// version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS) => version = 3：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES)
(store as relationalStore.RdbStore).executeSql('ALTER TABLE EMPLOYEE DROP COLUMN ADDRESS TEXT');
store.version = 3;
}
});
// 请确保获取到RdbStore实例后，再进行数据库的增、删、改、查等操作
}
}
```
2.  应用创建的数据库与其上下文（Context）有关，即使使用同样的数据库名称，但不同的应用上下文，会产生多个数据库，例如每个UIAbility都有各自的上下文。
3.  当应用首次获取数据库（调用getRdbStore）后，在应用沙箱内会产生对应的数据库文件。使用数据库的过程中，在与数据库文件相同的目录下可能会产生以-wal和-shm结尾的临时文件。此时若开发者希望移动数据库文件到其它地方使用查看，则需要同时移动这些临时文件，当应用被卸载完成后，其在设备上产生的数据库文件及临时文件也会被移除。
4.  错误码的详细介绍请参见通用错误码和关系型数据库错误码。
5.  获取到RdbStore后，调用insert()接口插入数据。示例代码如下所示： 关系型数据库没有显式的flush操作实现持久化，数据插入即保存在持久化文件。
```typescript
let store: relationalStore.RdbStore | undefined = undefined;
let value1 = 'Lisa';
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
let value5 = BigInt('15822401018187971961171');
// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
'NAME': value1,
'AGE': value2,
'SALARY': value3,
'CODES': value4,
'IDENTITY': value5,
};
const valueBucket2: relationalStore.ValuesBucket = {
NAME: value1,
AGE: value2,
SALARY: value3,
CODES: value4,
IDENTITY: value5,
};
const valueBucket3: relationalStore.ValuesBucket = {
"NAME": value1,
"AGE": value2,
"SALARY": value3,
"CODES": value4,
"IDENTITY": value5,
};
if (store !== undefined) {
(store as relationalStore.RdbStore).insert('EMPLOYEE', valueBucket1, (err: BusinessError, rowId: number) => {
if (err) {
console.error(`Failed to insert data. Code:${err.code}, message:${err.message}`);
return;
}
console.info(`Succeeded in inserting data. rowId:${rowId}`);
})
}
```
6.  根据谓词指定的实例对象，对数据进行修改或删除。 调用update()方法修改数据，调用delete()方法删除数据。示例代码如下所示：
```typescript
let value6 = 'Rose';
let value7 = 22;
let value8 = 200.5;
let value9 = new Uint8Array([1, 2, 3, 4, 5]);
let value10 = BigInt('15822401018187971967863');
// 以下三种方式可用
const valueBucket4: relationalStore.ValuesBucket = {
'NAME': value6,
'AGE': value7,
'SALARY': value8,
'CODES': value9,
'IDENTITY': value10,
};
const valueBucket5: relationalStore.ValuesBucket = {
NAME: value6,
AGE: value7,
SALARY: value8,
CODES: value9,
IDENTITY: value10,
};
const valueBucket6: relationalStore.ValuesBucket = {
"NAME": value6,
"AGE": value7,
"SALARY": value8,
"CODES": value9,
"IDENTITY": value10,
};
// 修改数据
let predicates1 = new relationalStore.RdbPredicates('EMPLOYEE'); // 创建表'EMPLOYEE'的predicates
predicates1.equalTo('NAME', 'Lisa'); // 匹配表'EMPLOYEE'中'NAME'为'Lisa'的字段
if (store !== undefined) {
(store as relationalStore.RdbStore).update(valueBucket4, predicates1, (err: BusinessError, rows: number) => {
if (err) {
console.error(`Failed to update data. Code:${err.code}, message:${err.message}`);
return;
}
console.info(`Succeeded in updating data. row count: ${rows}`);
})
}
// 删除数据
predicates1 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates1.equalTo('NAME', 'Lisa');
if (store !== undefined) {
(store as relationalStore.RdbStore).delete(predicates1, (err: BusinessError, rows: number) => {
if (err) {
console.error(`Failed to delete data. Code:${err.code}, message:${err.message}`);
return;
}
console.info(`Delete rows: ${rows}`);
})
}
```
7.  根据谓词指定的查询条件查找数据。 调用query()方法查找数据，返回一个ResultSet结果集。示例代码如下所示： 当应用完成查询数据操作，不再使用结果集（ResultSet）时，请及时调用close方法关闭结果集，释放系统为其分配的内存。
```typescript
let predicates2 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates2.equalTo('NAME', 'Rose');
if (store !== undefined) {
(store as relationalStore.RdbStore).query(predicates2, ['ID', 'NAME', 'AGE', 'SALARY', 'IDENTITY'], (err: BusinessError, resultSet) => {
if (err) {
console.error(`Failed to query data. Code:${err.code}, message:${err.message}`);
return;
}
console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
// resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
while (resultSet.goToNextRow()) {
const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
const identity = resultSet.getValue(resultSet.getColumnIndex('IDENTITY'));
console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}, identity=${identity}`);
}
// 释放数据集的内存
resultSet.close();
})
}
```
8.  在同路径下备份数据库。关系型数据库支持两种手动备份和自动备份（仅系统应用可用）两种方式，具体可见关系型数据库备份。 此处以手动备份为例：
```typescript
if (store !== undefined) {
// "Backup.db"为备份数据库文件名，默认在RdbStore同路径下备份。也可指定路径：customDir + "backup.db"
(store as relationalStore.RdbStore).backup("Backup.db", (err: BusinessError) => {
if (err) {
console.error(`Failed to backup RdbStore. Code:${err.code}, message:${err.message}`);
return;
}
console.info(`Succeeded in backing up RdbStore.`);
})
}
```
9.  从备份数据库中恢复数据。关系型数据库支持两种方式：恢复手动备份数据和恢复自动备份数据（仅系统应用可用），具体可见关系型数据库数据恢复。 此处以调用restore接口恢复手动备份数据为例：
```typescript
if (store !== undefined) {
(store as relationalStore.RdbStore).restore("Backup.db", (err: BusinessError) => {
if (err) {
console.error(`Failed to restore RdbStore. Code:${err.code}, message:${err.message}`);
return;
}
console.info(`Succeeded in restoring RdbStore.`);
})
}
```
10.  删除数据库。 调用deleteRdbStore()方法，删除数据库及数据库相关文件。示例代码如下： Stage模型示例： FA模型示例：
```typescript
relationalStore.deleteRdbStore(this.context, 'RdbTest.db', (err: BusinessError) => {
if (err) {
console.error(`Failed to delete RdbStore. Code:${err.code}, message:${err.message}`);
return;
}
console.info('Succeeded in deleting RdbStore.');
});
```
-  应用创建的数据库与其上下文（Context）有关，即使使用同样的数据库名称，但不同的应用上下文，会产生多个数据库，例如每个UIAbility都有各自的上下文。
-  当应用首次获取数据库（调用getRdbStore）后，在应用沙箱内会产生对应的数据库文件。使用数据库的过程中，在与数据库文件相同的目录下可能会产生以-wal和-shm结尾的临时文件。此时若开发者希望移动数据库文件到其它地方使用查看，则需要同时移动这些临时文件，当应用被卸载完成后，其在设备上产生的数据库文件及临时文件也会被移除。
-  错误码的详细介绍请参见通用错误码和关系型数据库错误码。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-data-sync-V14
爬取时间: 2025-04-27 22:41:13
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/sync-app-data-across-devices-overview-V14
爬取时间: 2025-04-27 22:41:27
来源: Huawei Developer
场景介绍
跨设备数据同步功能（即分布式功能），指将数据同步到一个组网环境中的其他设备。常用于用户应用程序数据内容在可信认证的不同设备间，进行自由同步、修改和查询。
例如：当设备1上的应用A在分布式数据库中增、删、改数据后，设备2上的应用A也可以获取到该数据库变化。可在分布式图库、备忘录、联系人、文件管理器等场景中使用。
不同应用间订阅数据库变化通知，则请参考跨应用数据共享实现。
根据跨设备同步数据生命周期的不同，可以分为：
-  临时数据生命周期较短，通常保存到内存中。比如游戏应用产生的过程数据，建议使用分布式数据对象。
-  持久数据生命周期较长，需要保存到存储的数据库中，根据数据关系和特点，可以选择关系型数据库或者键值型数据库。比如图库应用的各种相册、封面、图片等属性信息，建议使用关系型数据库；图库应用的具体图片缩略图，建议使用键值型数据库。
基本概念
在分布式场景中，会涉及多个设备，组网内设备之间看到的数据是否一致称为分布式数据库的一致性。
分布式数据库一致性可以分为强一致性、弱一致性和最终一致性。
-  强一致性：是指某一设备成功增、删、改数据后，组网内任意设备可立即读取数据获得更新后的值。
-  弱一致性：是指某一设备成功增、删、改数据后，组网内设备可能读取到本次更新后的数据，也可能读取不到，不能保证在多长时间后每个设备的数据一定是一致的。
-  最终一致性：是指某一设备成功增、删、改数据后，组网内设备可能读取不到本次更新后的数据，但在某个时间窗口之后组网内设备的数据能够达到一致状态。
强一致性对分布式数据的管理要求非常高，在服务器的分布式场景可能会遇到。因为移动终端设备的不常在线、以及无中心的特性，所以同应用跨设备数据同步不支持强一致性，只支持最终一致性。
跨设备同步访问控制机制
数据跨设备同步时，数据管理基于设备等级和数据安全标签进行访问控制，具体可见跨设备同步访问控制机制。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-sync-of-kv-store-V14
爬取时间: 2025-04-27 22:41:41
来源: Huawei Developer
场景介绍
键值型数据库适合不涉及过多数据关系和业务关系的业务数据存储，比SQL数据库存储拥有更好的读写性能，同时因其在分布式场景中降低了解决数据库版本兼容问题的复杂度，和数据同步过程中冲突解决的复杂度而被广泛使用。
基本概念
在使用键值型数据库跨设备数据同步前，请先了解以下概念。
单版本数据库
单版本是指数据在本地是以单个条目为单位的方式保存，当数据在本地被用户修改时，不管它是否已经被同步出去，均直接在这个条目上进行修改。多个设备全局只保留一份数据，多个设备的相同记录（主码相同）会按时间最新保留一条记录，数据不分设备，设备之间修改相同的key会覆盖。同步也以此为基础，按照它在本地被写入或更改的顺序将当前最新一次修改逐条同步至远端设备，常用于联系人、天气等应用存储场景。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170227.86574299133026222598936046354133:50001231000000:2800:D1BDE8C08280EEAA4EB73F78DF17D6F07876CC17500A8ADB83B71B320E1BC07A.jpg)
多设备协同数据库
多设备协同分布式数据库建立在单版本数据库之上，对应用程序存入的键值型数据中的Key前面拼接了本设备的DeviceID标识符，这样能保证每个设备产生的数据严格隔离。数据以设备的维度管理，不存在冲突；支持按照设备的维度查询数据。
底层按照设备的维度管理这些数据，多设备协同数据库支持以设备的维度查询分布式数据，但是不支持修改远端设备同步过来的数据。需要分开查询各设备数据的可以使用设备协同版本数据库。常用于图库缩略图存储场景。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170227.68189775392093242547081326140696:50001231000000:2800:A244B34E1540AB90B1F5A8748B7304E4AE77B381755BAB69717D5833C08ABEA4.jpg)
同步方式
数据管理服务提供了两种同步方式：手动同步和自动同步。键值型数据库可选择其中一种方式实现同应用跨设备数据同步。
手动同步
由应用程序调用sync接口来触发，需要指定同步的设备列表和同步模式。同步模式分为PULL_ONLY（将远端数据拉取到本端）、PUSH_ONLY（将本端数据推送到远端）和PUSH_PULL（将本端数据推送到远端同时也将远端数据拉取到本端）。带有Query参数的同步接口，支持按条件过滤的方法进行同步，将符合条件的数据同步到远端。
自动同步
在跨设备Call调用实现的多端协同场景中，在应用程序更新数据后，由分布式数据库自动将本端数据推送到远端，同时也将远端数据拉取到本端来完成数据同步，应用不需要主动调用sync接口。
运作机制
底层通信组件完成设备发现和认证，会通知上层应用程序设备上线。收到设备上线的消息后数据管理服务可以在两个设备之间建立加密的数据传输通道，利用该通道在两个设备之间进行数据同步。
数据跨设备同步机制
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170228.47535649910364552195108752857266:50001231000000:2800:90F76DB59BD9DD0E98ACB184413256097CD2B69C36639657A9977F6501D02E2F.jpg)
如图所示，通过put、delete接口触发自动同步，将分布式数据通过通信适配层发送给对端设备，实现分布式数据的自动同步。
手动同步则是手动调用sync接口触发同步，将分布式数据通过通信适配层发送给对端设备。
数据变化通知机制
增、删、改数据库时，会给订阅者发送数据变化的通知。主要分为本地数据变化通知和分布式数据变化通知。
-  本地数据变化通知：本地设备的应用内订阅数据变化通知，数据库增删改数据时，会收到通知。
-  分布式数据变化通知：同一应用订阅组网内其他设备数据变化的通知，其他设备增删改数据时，本设备会收到通知。
约束限制
-  设备协同数据库，针对每条记录，Key的长度≤896 Byte，Value的长度<4 MB。
-  单版本数据库，针对每条记录，Key的长度≤1 KB，Value的长度<4 MB。
-  键值型数据库不支持应用程序自定义冲突解决策略。
-  每个应用程序最多支持同时打开16个键值型分布式数据库。
-  单个数据库最多支持注册8个订阅数据变化的回调。
接口说明
以下是单版本键值型分布式数据库跨设备数据同步功能的相关接口，大部分为异步接口。异步接口均有callback和Promise两种返回形式，下表均以callback形式为例，更多接口及使用方式请见分布式键值数据库。
| 接口名称 | 描述 |
| --- | --- |
| createKVManager(config: KVManagerConfig): KVManager | 创建一个KVManager对象实例，用于管理数据库对象。 |
| getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void | 指定options和storeId，创建并得到指定类型的KVStore数据库。 |
| put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void | 插入和更新数据。 |
| on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void | 订阅数据库中数据的变化。 |
| get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void | 查询指定Key键的值。 |
| sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void | 在手动模式下，触发数据库同步。 |
开发步骤
此处以单版本键值型数据库跨设备数据同步的开发为例。以下是具体的开发流程和开发步骤。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170228.93524916158818441726210052726449:50001231000000:2800:B5AAA994151DABB9D275DC4FDB11D8E1F93479372091E999501F3481814A5979.png)
数据只允许向数据安全标签不高于对端设备安全等级的设备同步数据，具体规则可见跨设备同步访问控制机制。
1.  导入模块。
```typescript
import { distributedKVStore } from '@kit.ArkData';
```
2.  请求权限。
3.  根据配置构造分布式数据库管理类实例。
```typescript
// Stage模型获取context
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
let kvManager: distributedKVStore.KVManager | undefined = undefined;
class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage:window.WindowStage) {
let context = this.context;
}
}
// FA模型获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
let context = featureAbility.getContext();
// 获取context之后，构造分布式数据库管理类实例
try {
const kvManagerConfig: distributedKVStore.KVManagerConfig = {
bundleName: 'com.example.datamanagertest',
context: context
}
kvManager = distributedKVStore.createKVManager(kvManagerConfig);
console.info('Succeeded in creating KVManager.');
// 继续创建获取数据库
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to create KVManager. Code:${error.code},message:${error.message}`);
}
if (kvManager !== undefined) {
kvManager = kvManager as distributedKVStore.KVManager;
// 进行后续创建数据库等相关操作
// ...
}
```
4.  获取并得到指定类型的键值型数据库。
```typescript
let kvStore: distributedKVStore.SingleKVStore | undefined = undefined;
try {
let child1 = new distributedKVStore.FieldNode('id');
child1.type = distributedKVStore.ValueType.INTEGER;
child1.nullable = false;
child1.default = '1';
let child2 = new distributedKVStore.FieldNode('name');
child2.type = distributedKVStore.ValueType.STRING;
child2.nullable = false;
child2.default = 'zhangsan';
let schema = new distributedKVStore.Schema();
schema.root.appendChild(child1);
schema.root.appendChild(child2);
schema.indexes = ['$.id', '$.name'];
// 0表示COMPATIBLE模式，1表示STRICT模式。
schema.mode = 1;
// 支持在检查Value时，跳过skip指定的字节数，且取值范围为[0,4M-2]。
schema.skip = 0;
const options: distributedKVStore.Options = {
createIfMissing: true,
encrypt: false,
backup: false,
autoSync: false,
// kvStoreType不填时，默认创建多设备协同数据库
// 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE_COLLABORATION,
kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
// schema 可以不填，在需要使用schema功能时可以构造此参数，例如：使用谓词查询等。
schema: schema,
securityLevel: distributedKVStore.SecurityLevel.S3
};
kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options, (err, store: distributedKVStore.SingleKVStore) => {
if (err) {
console.error(`Failed to get KVStore: Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in getting KVStore.');
kvStore = store;
// 请确保获取到键值数据库实例后，再进行相关数据操作
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
if (kvStore !== undefined) {
kvStore = kvStore as distributedKVStore.SingleKVStore;
// 进行后续相关数据操作，包括数据的增、删、改、查、订阅数据变化等操作
// ...
}
```
5.  订阅分布式数据变化，如需关闭订阅分布式数据变化，调用off('dataChange')关闭。
```typescript
try {
kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_ALL, (data) => {
console.info(`dataChange callback call data: ${data}`);
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. code:${error.code},message:${error.message}`);
}
```
6.  将数据写入分布式数据库。
```typescript
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
// 如果未定义Schema则Value可以传其他符合要求的值。
const VALUE_TEST_STRING_ELEMENT = '{"id":0, "name":"lisi"}';
try {
kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err) => {
if (err !== undefined) {
console.error(`Failed to put data. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in putting data.');
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
```
7.  查询分布式数据库数据。
```typescript
try {
kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err) => {
if (err !== undefined) {
console.error(`Failed to put data. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in putting data.');
kvStore = kvStore as distributedKVStore.SingleKVStore;
kvStore.get(KEY_TEST_STRING_ELEMENT, (err, data) => {
if (err != undefined) {
console.error(`Failed to get data. Code:${err.code},message:${err.message}`);
return;
}
console.info(`Succeeded in getting data. Data:${data}`);
});
});
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to get data. Code:${error.code},message:${error.message}`);
}
```
8.  同步数据到其他设备。 选择同一组网环境下的设备以及同步模式（需用户在应用首次启动的弹窗中确认选择同步模式），进行数据同步。 在手动同步的方式下，其中的deviceIds通过调用devManager.getAvailableDeviceListSync方法得到。
```typescript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
let devManager: distributedDeviceManager.DeviceManager;
try {
// create deviceManager
devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
// deviceIds由deviceManager调用getAvailableDeviceListSync方法得到
let deviceIds: string[] = [];
if (devManager != null) {
let devices = devManager.getAvailableDeviceListSync();
for (let i = 0; i < devices.length; i++) {
deviceIds[i] = devices[i].networkId as string;
}
}
try {
// 1000表示最大延迟时间为1000ms
kvStore.sync(deviceIds, distributedKVStore.SyncMode.PUSH_ONLY, 1000);
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
} catch (err) {
let error = err as BusinessError;
console.error("createDeviceManager errCode:" + error.code + ",errMessage:" + error.message);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-sync-of-rdb-store-V14
爬取时间: 2025-04-27 22:41:56
来源: Huawei Developer
场景介绍
当应用程序本地存储的关系型数据存在跨设备同步的需求时，可以将需要同步的表数据迁移到新的支持跨设备的表中，当然也可以在刚完成表创建时设置其支持跨设备。
基本概念
关系型数据库跨设备数据同步，支持应用在多设备间同步存储的关系型数据。
-  应用在数据库中新创建表后，可以设置其为分布式表。在查询远程设备数据库时，根据本地表名可以获取指定远程设备的分布式表名。
-  设备之间同步数据，数据同步有两种方式，将数据从本地设备推送到远程设备或将数据从远程设备拉至本地设备。
运作机制
底层通信组件完成设备发现和认证，会通知上层应用程序设备上线。收到设备上线的消息后数据管理服务可以在两个设备之间建立加密的数据传输通道，利用该通道在两个设备之间进行数据同步。
数据跨设备同步机制
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170228.61415241547505551274123097263622:50001231000000:2800:9F0B5F2F42903888D5D46D5E6E7D3DA4E3546BCC7C0EC847D408C7D16A30F009.jpg)
业务将数据写入关系型数据库后，向数据管理服务发起同步请求。
数据管理服务从应用沙箱内读取待同步数据，根据对端设备的deviceId将数据发送到其他设备的数据管理服务。再由数据管理服务将数据写入同应用的数据库内。
数据变化通知机制
增、删、改数据库时，会给订阅者发送数据变化的通知。主要分为本地数据变化通知和分布式数据变化通知。
-  本地数据变化通知：本地设备的应用内订阅数据变化通知，数据库增删改数据时，会收到通知。
-  分布式数据变化通知：同一应用订阅组网内其他设备数据变化的通知，其他设备增删改数据时，本设备会收到通知。
约束限制
-  每个应用程序最多支持同时打开16个关系型分布式数据库。
-  单个数据库最多支持注册8个订阅数据变化的回调。
接口说明
以下是关系型设备协同分布式数据库跨设备数据同步功能的相关接口，大部分为异步接口。异步接口均有callback和Promise两种返回形式，下表均以callback形式为例，更多接口及使用方式请见关系型数据库。
| 接口名称 | 描述 |
| --- | --- |
| setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void | 设置分布式同步表。 |
| sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void | 分布式数据同步。 |
| on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void | 订阅分布式数据变化。 |
| off(event:'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void | 取消订阅分布式数据变化。 |
| obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void | 根据本地数据库表名获取指定设备上的表名。 |
| remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string> , callback: AsyncCallback<ResultSet>): void | 根据指定条件查询远程设备数据库中的数据。 |
开发步骤
数据只允许向数据安全标签不高于对端设备安全等级的设备同步数据，具体规则可见跨设备同步访问控制机制。
1.  导入模块。
```typescript
import { relationalStore } from '@kit.ArkData';
```
2.  请求权限。
3.  创建关系型数据库，设置将需要进行分布式同步的表。
```typescript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage) {
const STORE_CONFIG: relationalStore.StoreConfig = {
name: "RdbTest.db",
securityLevel: relationalStore.SecurityLevel.S3
};
relationalStore.getRdbStore(this.context, STORE_CONFIG, (err: BusinessError, store: relationalStore.RdbStore) => {
store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)', (err) => {
// 设置分布式同步表。
store.setDistributedTables(['EMPLOYEE']);
// 进行数据的相关操作
})
})
}
}
```
4.  分布式数据同步。使用SYNC_MODE_PUSH触发同步后，数据将从本设备向组网内的其它所有设备同步。
```typescript
// 构造用于同步分布式表的谓词对象
let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
// 调用同步数据的接口
if(store != undefined)
{
(store as relationalStore.RdbStore).sync(relationalStore.SyncMode.SYNC_MODE_PUSH, predicates, (err, result) => {
// 判断数据同步是否成功
if (err) {
console.error(`Failed to sync data. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in syncing data.');
for (let i = 0; i < result.length; i++) {
console.info(`device:${result[i][0]},status:${result[i][1]}`);
}
})
}
```
5.  分布式数据订阅。数据同步变化将触发订阅回调方法执行，回调方法的入参为发生变化的设备ID。
```typescript
let devices: string | undefined = undefined;
try {
// 调用分布式数据订阅接口，注册数据库的观察者
// 当分布式数据库中的数据发生更改时，将调用回调
if(store != undefined) {
(store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, (storeObserver)=>{
if(devices != undefined){
for (let i = 0; i < devices.length; i++) {
console.info(`The data of device:${devices[i]} has been changed.`);
}
}
});
}
} catch (err) {
console.error('Failed to register observer. Code:${err.code},message:${err.message}');
}
// 当前不需要订阅数据变化时，可以将其取消。
try {
if(store != undefined) {
(store as relationalStore.RdbStore).off('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, (storeObserver)=>{
});
}
} catch (err) {
console.error('Failed to register observer. Code:${err.code},message:${err.message}');
}
```
6.  跨设备查询。如果数据未完成同步，或未触发数据同步，应用可以使用此接口从指定的设备上查询数据。 deviceIds通过调用deviceManager.getAvailableDeviceListSync方法得到。
```typescript
// 获取deviceIds
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined ;
try {
dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
let devices = dmInstance.getAvailableDeviceListSync();
deviceId = devices[0].networkId;
// 构造用于查询分布式表的谓词对象
let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
// 调用跨设备查询接口，并返回查询结果
if(store != undefined && deviceId != undefined) {
(store as relationalStore.RdbStore).remoteQuery(deviceId, 'EMPLOYEE', predicates, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES'],
(err: BusinessError, resultSet: relationalStore.ResultSet) => {
if (err) {
console.error(`Failed to remoteQuery data. Code:${err.code},message:${err.message}`);
return;
}
console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
}
)
}
} catch (err) {
let code = (err as BusinessError).code;
let message = (err as BusinessError).message;
console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-sync-of-distributed-data-object-V14
爬取时间: 2025-04-27 22:42:10
来源: Huawei Developer
场景介绍
传统方式下，设备之间的数据同步，需要开发者完成消息处理逻辑，包括：建立通信链接、消息收发处理、错误重试、数据冲突解决等操作，工作量非常大。而且设备越多，调试复杂度也将同步增加。
其实设备之间的状态、消息发送进度、发送的数据等都是“变量”。如果这些变量支持“全局”访问，那么开发者跨设备访问这些变量就能像操作本地变量一样，从而能够自动高效、便捷地实现数据多端同步。
分布式数据对象即实现了对“变量”的“全局”访问。向应用开发者提供内存对象的创建、查询、删除、修改、订阅等基本数据对象的管理能力，同时具备分布式能力。为开发者在分布式应用场景下提供简单易用的JS接口，轻松实现多设备间同应用的数据协同，同时设备间可以监听对象的状态和数据变更。满足超级终端场景下，相同应用多设备间的数据对象协同需求。与传统方式相比，分布式数据对象大大减少了开发者的工作量。
目前分布式数据对象只能在跨端迁移和通过跨设备Call调用实现的多端协同场景中使用。
基本概念
-  分布式内存数据库 分布式内存数据库将数据缓存在内存中，以便应用获得更快的数据存取速度，不会将数据进行持久化。若数据库关闭，则数据不会保留。
-  分布式数据对象 分布式数据对象是一个JS对象型的封装。每一个分布式数据对象实例会创建一个内存数据库中的数据表，每个应用程序创建的内存数据库相互隔离，对分布式数据对象的“读取”或“赋值”会自动映射到对应数据库的get/put操作。 分布式数据对象的生命周期包括以下状态：
运作机制
图1分布式数据对象运作机制
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170228.74478024257394790412926949116356:50001231000000:2800:6DB06690B8CE7036BC7D547DB7D24D4590B37D7C634EB88A9E0FA3A2A7B8D260.jpg)
分布式数据对象生长在分布式内存数据库之上，在分布式内存数据库上进行了JS对象型的封装，能像操作本地变量一样操作分布式数据对象，数据的跨设备同步由系统自动完成。
JS对象型存储与封装机制
-  为每个分布式数据对象实例创建一个内存数据库，通过SessionId标识，每个应用程序创建的内存数据库相互隔离。
-  在分布式数据对象实例化的时候，（递归）遍历对象所有属性，使用“Object.defineProperty”定义所有属性的set和get方法，set和get中分别对应数据库一条记录的put和get操作，Key对应属性名，Value对应属性值。
-  在开发者对分布式数据对象进行“读取”或者“赋值”的时候，都会自动调用到set和get方法，映射到对应数据库的操作。
表1分布式数据对象和分布式数据库的对应关系
| 分布式对象实例 | 对象实例 | 属性名称 | 属性值 |
| --- | --- | --- | --- |
| 分布式内存数据库 | 一个数据库（sessionID标识） | 一条数据库记录的key | 一条数据库记录的value |
跨设备同步和数据变更通知机制
分布式数据对象，最重要的功能就是对象之间的数据同步。可信组网内的设备可以在本地创建分布式数据对象，并设置sessionID。不同设备上的分布式数据对象，通过设置相同的sessionID，建立对象之间的同步关系。
如下图所示，设备A和设备B上的“分布式数据对象1”，其sessionID均为session1，这两个对象建立了session1的同步关系。
图2对象的同步关系
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170228.10413883675047985507178791979162:50001231000000:2800:E3C73D75BCE132E02BAA353AAF0ECA8AA63BAEACE2C3C32E480964C62C3E5967.jpg)
一个同步关系中，一个设备只能有一个对象加入。比如上图中，设备A的“分布式数据对象1”已经加入了session1的同步关系，所以设备A的“分布式数据对象2”就加入失败了。
建立同步关系后，每个Session有一份共享对象数据。加入了同一个Session的对象，支持以下操作：
（1）读取/修改Session中的数据。
（2）监听数据变更，感知其他设备对共享对象数据的修改。
（3）监听状态变更，感知其他设备的加入和退出。
分布式数据对象加入session时，如果它的数据与session中的数据不同，则它会更新session中的数据。如果希望分布式数据对象加入sessionId时不更新session中的数据，并且得到session中的数据，需要将对象的属性的值设置为undefined（资产类型的属性则是将它的各个属性值设置为空字符串）。
同步的最小单位
关于分布式数据对象的数据同步，值得注意的是，同步的最小单位是“属性”。比如，下图中对象1包含三个属性：name、age和parents。当其中一个属性变更时，则数据同步时只需同步此变更的属性。
对象属性支持基本类型（数字类型、布尔类型、字符串类型）以及复杂类型（数组、基本类型嵌套）。针对复杂类型的数据修改，目前仅支持对根属性的修改，暂不支持对下级属性的修改。
```typescript
dataObject['parents'] = {mom: "amy"}; // 支持的修改
dataObject['parents']['mon'] = "amy"; // 不支持的修改
```
图3数据同步视图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170228.40612432977381163084258112841297:50001231000000:2800:AA638BFDBD24053A42D2D81A59AB2E98EE994D71E57374F1F9988620BF9DF58E.jpg)
对象持久化缓存机制
分布式对象主要运行在应用程序的进程空间。当调用分布式对象持久化接口时，通过分布式数据库对对象进行持久化和同步，进程退出后数据也不会丢失。
该场景是分布式对象的扩展场景，主要用于以下情况：
-  在设备上创建持久化对象后APP退出，重新打开APP，创建持久化对象，加入同一个Session，数据可以恢复到APP退出前的数据。
-  在设备A上创建持久化对象并同步后持久化到设备B后，A设备的APP退出，设备B打开APP，创建持久化对象，加入同一个Session，数据可以恢复到A设备退出前的数据。
资产同步机制
在分布式对象中，可以使用资产类型来描述本地实体资产文件，分布式对象跨设备同步时，该文件会和数据一起同步到其他设备上。当前只支持资产类型，不支持资产类型数组。如需同步多个资产，可将每个资产作为分布式对象的一个根属性实现。
约束限制
-  目前分布式数据对象只能在跨端迁移和通过跨设备Call调用实现的多端协同场景中使用。
-  不同设备间只有相同bundleName的应用才能直接同步。
-  分布式数据对象的数据同步发生在同一个应用程序下，且同sessionID之间。
-  不建议创建过多的分布式数据对象，每个分布式数据对象将占用100-150KB内存。
-  每个分布式数据对象大小不超过500KB。
-  设备A修改1KB数据，设备B收到变更通知，50ms内完成。
-  单个应用程序最多只能创建16个分布式数据对象实例。
-  考虑到性能和用户体验，最多不超过3个设备进行数据协同。
-  如对复杂类型的数据进行修改，仅支持修改根属性，暂不支持下级属性修改。资产同步机制中，资产类型的数据支持下一级属性修改。
-  支持JS接口间的互通，与其他语言不互通。
接口说明
以下是分布式对象跨设备数据同步功能的相关接口，大部分为异步接口。异步接口均有callback和Promise两种返回形式，下表均以callback形式为例，更多接口及使用方式请见分布式数据对象。
| 接口名称 | 描述 |
| --- | --- |
| create(context: Context, source: object): DataObject | 创建并得到一个分布式数据对象实例。 |
| genSessionId(): string | 创建一个sessionId，可作为分布式数据对象的sessionId。 |
| setSessionId(sessionId: string, callback: AsyncCallback<void>): void | 设置同步的sessionId，当可信组网中有多个设备时，多个设备间的对象如果设置为同一个sessionId，就能自动同步。 |
| setSessionId(callback: AsyncCallback<void>): void | 退出所有已加入的session。 |
| on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void | 监听分布式数据对象的数据变更。 |
| off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void | 取消监听分布式数据对象的数据变更。 |
| on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void): void | 监听分布式数据对象的上下线。 |
| off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' |'offline' ) => void): void | 取消监听分布式数据对象的上下线。 |
| save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void | 保存分布式数据对象。 |
| revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void | 撤回保存的分布式数据对象。 |
| bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void | 绑定融合资产。 |
开发步骤
在跨端迁移中使用分布式数据对象迁移数据
1.  迁移发起端在onContinue接口中创建分布式数据对象并保存数据到接收端： 1.1 调用create接口创建并得到一个分布式数据对象实例。 1.2 调用genSessionId接口创建一个sessionId，调用setSessionId接口设置同步的sessionId，并将这个sessionId放入wantParam。 1.3 从wantParam获取接收端设备networkId，使用这个networkId调用save接口保存数据到接收端。
2.  接收端在onCreate和onNewWant接口中创建分布式数据对象并注册恢复状态监听： 2.1 调用create接口创建并得到一个分布式数据对象实例。 2.2 注册恢复状态监听。收到状态为'restored'的回调通知时，表示接收端分布式数据对象已恢复发起端保存过来的数据。 2.3 从want.parameters中获取发起端放入的sessionId，调用setSessionId接口设置同步的sessionId。
-  跨端迁移时，在迁移发起端调用setsessionId接口设置同步的sessionId后，必须再调用save接口保存数据到接收端。
-  跨端迁移需要配置continuable标签，详见应用接续开发步骤。
-  wantParam中的"sessionId"字段可能被其他服务占用，建议自定义一个key存取sessionId。
-  可以使用资产类型记录资产附件（文件、图片、视频等类型文件）的相关信息，迁移资产类型数据时，对应的资产附件会一起迁移到对端。
-  接收端需要将业务数据的初始值设置为undefined，才能恢复发起端保存的数据，否则接收端的数据会覆盖同步到发起端。如果是资产数据，需要将资产数据的各个属性设置为空字符串而不是将整个资产数据设置为undefined。
-  暂不支持资产类型数组，如果要迁移多个文件，在业务数据中定义多条资产数据来记录。
-  目前仅支持迁移分布式文件目录下的文件，非分布式文件目录下的文件可以复制或移动到分布式文件目录下再进行迁移。文件的操作和URI的获取详见文件管理和文件URI。
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { commonType, distributedDataObject } from '@kit.ArkData';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 业务数据定义
class Data {
title: string | undefined;
text: string | undefined;
attachment: commonType.Asset; // 可以使用资产类型记录分布式目录下的文件，迁移资产数据时，对应的文件会一起迁移到接收端。（不迁移文件时不需要此字段，下方代码中的createAttachment、createEmptyAttachment方法也都不需要。）
// attachment2: commonType.Asset; // 暂不支持资产类型数组，如果要迁移多个文件，在业务数据中定义多条资产数据来记录
constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset) {
this.title = title;
this.text = text;
this.attachment = attachment;
}
}
const TAG = '[DistributedDataObject]';
let dataObject: distributedDataObject.DataObject;
export default class EntryAbility extends UIAbility {
// 1. 迁移发起端在onContinue接口中创建分布式数据对象并保存数据到接收端
onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult | Promise<AbilityConstant.OnContinueResult> {
// 1.1 调用create接口创建并得到一个分布式数据对象实例
let attachment = this.createAttachment();
let data = new Data('The title', 'The text', attachment);
dataObject = distributedDataObject.create(this.context, data);
// 1.2 调用genSessionId接口创建一个sessionId，调用setSessionId接口设置同步的sessionId，并将这个sessionId放入wantParam
let sessionId = distributedDataObject.genSessionId();
console.log(TAG + `gen sessionId: ${sessionId}`);
dataObject.setSessionId(sessionId);
wantParam.distributedSessionId = sessionId;
// 1.3 从wantParam获取接收端设备networkId，使用这个networkId调用save接口保存数据到接收端
let deviceId = wantParam.targetDevice as string;
console.log(TAG + `get deviceId: ${deviceId}`);
dataObject.save(deviceId);
return AbilityConstant.OnContinueResult.AGREE;
}
// 2. 接收端在onCreate和onNewWant接口中创建分布式数据对象并加入组网进行数据恢复
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
if (launchParam.launchReason == AbilityConstant.LaunchReason.CONTINUATION) {
if (want.parameters && want.parameters.distributedSessionId) {
this.restoreDistributedDataObject(want);
}
}
}
// 2. 接收端在onCreate和onNewWant接口中创建分布式数据对象并加入组网进行数据恢复
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
if (launchParam.launchReason == AbilityConstant.LaunchReason.CONTINUATION) {
if (want.parameters && want.parameters.distributedSessionId) {
this.restoreDistributedDataObject(want);
}
}
}
restoreDistributedDataObject(want: Want) {
if (!want.parameters || !want.parameters.distributedSessionId) {
console.error(TAG + 'missing sessionId');
return;
}
// 2.1 调用create接口创建并得到一个分布式数据对象实例
let attachment = this.createEmptyAttachment(); // 接收端需要将资产数据的各个属性设置为空字符串，才能恢复发起端保存的资产数据
let data = new Data(undefined, undefined, attachment);
dataObject = distributedDataObject.create(this.context, data);
// 2.2 注册恢复状态监听。收到状态为'restored'的回调通知时，表示接收端分布式数据对象已恢复发起端保存过来的数据（有资产数据时，对应的文件也迁移过来了）
dataObject.on('status', (sessionId: string, networkId: string, status: string) => {
if (status == 'restored') { // 收到'restored'的状态通知表示已恢复发起端保存的数据
console.log(TAG + `title: ${dataObject['title']}, text: ${dataObject['text']}`);
}
});
// 2.3 从want.parameters中获取发起端放入的sessionId，调用setSessionId接口设置同步的sessionId
let sessionId = want.parameters.distributedSessionId as string;
console.log(TAG + `get sessionId: ${sessionId}`);
dataObject.setSessionId(sessionId);
}
// 在分布式文件目录下创建一个文件并使用资产类型记录（也可以记录分布式文件目录下已有文件，非分布式文件目录下的文件可以复制或移动到分布式文件目录下再进行记录）
createAttachment() {
let attachment = this.createEmptyAttachment();
try {
let distributedDir: string = this.context.distributedFilesDir; // 分布式文件目录
let fileName: string = 'text_attachment.txt'; // 文件名
let filePath: string = distributedDir + '/' + fileName; // 文件路径
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
fileIo.writeSync(file.fd, 'The text in attachment');
fileIo.closeSync(file.fd);
let uri: string = fileUri.getUriFromPath(filePath); // 获取文件URI
let stat = fileIo.statSync(filePath); // 获取文件详细属性信息
// 写入资产数据
attachment = {
name: fileName,
uri: uri,
path: filePath,
createTime: stat.ctime.toString(),
modifyTime: stat.mtime.toString(),
size: stat.size.toString()
}
} catch (e) {
let err = e as BusinessError;
console.error(TAG + `file error, error code: ${err.code}, error message: ${err.message}`);
}
return attachment;
}
createEmptyAttachment() {
let attachment: commonType.Asset = {
name: '',
uri: '',
path: '',
createTime: '',
modifyTime: '',
size: ''
}
return attachment;
}
}
```
在多端协同中使用分布式数据对象
1.  调用端调用startAbilityByCall接口拉起对端Ability： 1.1 调用genSessionId接口创建一个sessionId，通过分布式设备管理接口获取对端设备networkId。 1.2 组装want，并将sessionId放入want。 1.3 调用startAbilityByCall接口拉起对端Ability。
2.  调用端拉起对端Ability后创建分布式数据对象并加入组网： 2.1 创建分布式数据对象实例。 2.2 注册数据变更监听。 2.3 设置同步sessionId加入组网。
3.  被调用端被拉起后创建和恢复分布式数据对象： 3.1 创建分布式数据对象实例。 3.2 注册数据变更监听。 3.3 从want中获取源端放入的sessionId，使用这个sessionId加入组网。
-  暂时只支持在跨设备Call调用实现的多端协同中使用分布式数据对象进行数据同步。
-  跨设备Call调用实现的多端协同开发需要申请ohos.permission.DISTRIBUTED_DATASYNC权限和配置单实例启动标签。
-  wantParam中的"sessionId"字段可能被其他服务占用，建议自定义一个key存取sessionId。
-  使用分布式设备管理获取对端设备networkId详见设备信息查询开发指导。
示例代码如下：
```typescript
import { AbilityConstant, Caller, common, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { distributedDataObject } from '@kit.ArkData';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 业务数据定义
class Data {
title: string | undefined;
text: string | undefined;
constructor(title: string | undefined, text: string | undefined) {
this.title = title;
this.text = text;
}
}
const TAG = '[DistributedDataObject]';
let sessionId: string;
let caller: Caller;
let dataObject: distributedDataObject.DataObject;
export default class EntryAbility extends UIAbility {
// 1. 调用端调用startAbilityByCall接口拉起对端Ability
callRemote() {
if (caller) {
console.error(TAG + 'call remote already');
return;
}
let context = getContext(this) as common.UIAbilityContext;
// 1.1 调用genSessionId接口创建一个sessionId，通过分布式设备管理接口获取对端设备networkId
sessionId = distributedDataObject.genSessionId();
console.log(TAG + `gen sessionId: ${sessionId}`);
let deviceId = getRemoteDeviceId();
if (deviceId == "") {
console.warn(TAG + 'no remote device');
return;
}
console.log(TAG + `get remote deviceId: ${deviceId}`);
// 1.2 组装want，并将sessionId放入want
let want: Want = {
bundleName: 'com.example.collaboration',
abilityName: 'EntryAbility',
deviceId: deviceId,
parameters: {
'ohos.aafwk.param.callAbilityToForeground': true, // 前台启动，非必须
'distributedSessionId': sessionId
}
}
try {
// 1.3 调用startAbilityByCall接口拉起对端Ability
context.startAbilityByCall(want).then((res) => {
if (!res) {
console.error(TAG + 'startAbilityByCall failed');
}
caller = res;
})
} catch (e) {
let err = e as BusinessError;
console.error(TAG + `get remote deviceId error, error code: ${err.code}, error message: ${err.message}`);
}
}
// 2. 拉起对端Ability后创建分布式数据对象
createDataObject() {
if (!caller) {
console.error(TAG + 'call remote first');
return;
}
if (dataObject) {
console.error(TAG + 'create dataObject already');
return;
}
let context = getContext(this) as common.UIAbilityContext;
// 2.1 创建分布式数据对象实例
let data = new Data('The title', 'The text');
dataObject = distributedDataObject.create(context, data);
// 2.2 注册数据变更监听
dataObject.on('change', (sessionId: string, fields: Array<string>) => {
fields.forEach((field) => {
console.log(TAG + `${field}: ${dataObject[field]}`);
});
});
// 2.3 设置同步sessionId加入组网
dataObject.setSessionId(sessionId);
}
// 3. 被调用端被拉起后创建和恢复分布式数据对象
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
if (want.parameters && want.parameters.distributedSessionId) {
// 3.1 创建分布式数据对象实例
let data = new Data(undefined, undefined);
dataObject = distributedDataObject.create(this.context, data);
// 3.2 注册数据变更监听
dataObject.on('change', (sessionId: string, fields: Array<string>) => {
fields.forEach((field) => {
console.log(TAG + `${field}: ${dataObject[field]}`);
});
});
// 3.3 从want中获取源端放入的sessionId，使用这个sessionId加入组网
let sessionId = want.parameters.distributedSessionId as string;
console.log(TAG + `onCreate get sessionId: ${sessionId}`);
dataObject.setSessionId(sessionId);
}
}
}
// 获取可信组网中的设备
function getRemoteDeviceId() {
let deviceId = "";
try {
let deviceManager = distributedDeviceManager.createDeviceManager('com.example.collaboration');
let devices = deviceManager.getAvailableDeviceListSync();
if (devices[0] && devices[0].networkId) {
deviceId = devices[0].networkId;
}
} catch (e) {
let err = e as BusinessError;
console.error(TAG + `get remote deviceId error, error code: ${err.code}, error message: ${err.message}`);
}
return deviceId;
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-reliability-security-V14
爬取时间: 2025-04-27 22:42:23
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-reliability-security-overview-V14
爬取时间: 2025-04-27 22:42:36
来源: Huawei Developer
功能场景
在系统运行中，存储损坏、存储空间不足、文件系统权限、系统掉电等都可能导致数据库发生故障。比如联系人应用的数据库损坏，导致用户的联系人丢失；日历应用的数据库损坏，导致丢失日历提醒等。为此数据管理提供了数据可靠性与安全性相关的解决方案和能力保障。
-  备份、恢复功能：重要业务应用（如银行）数据丢失，出现严重异常场景，可以通过备份恢复数据库，保证关键数据不丢失。
-  数据库加密功能：当数据库中存储如认证凭据、财务数据等高敏感信息时，可对数据库进行加密，提高数据库安全性。
-  数据库分类分级：数据跨设备同步时，数据管理基于数据安全标签和设备安全等级进行访问控制，保证数据安全。
-  E类加密数据库：应用存储用户敏感信息时应使用E类数据库，在锁屏的情况下，满足一定条件时，会触发密钥的销毁。此时E类数据库不可操作。当锁屏解锁后，密钥会恢复，E类数据库恢复正常读写操作。保证敏感信息的安全性。
另外，备份数据库存储在应用的沙箱内，当存储空间不足时，可以选择删除本地的数据库备份，释放空间。
基本概念
在进行数据可靠性与安全性相关功能的开发前，请先了解以下相关概念。
数据库备份与恢复
-  数据库备份：指对当前数据库的数据库文件进行完整备份。HarmonyOS数据库备份针对数据库全量文件进行完整的备份。 在进行数据库备份的时候，无需关闭数据库，直接调用对应的数据库备份接口就能完成对数据库文件的备份。
-  数据库恢复：从指定的备份文件恢复到当前数据库文件。恢复完成时，当前数据库数据恢复到和指定备份文件一致。
数据库加密
数据库加密是对整个数据库文件的加密，可以增强数据库的安全性，有效保护数据库内容。
数据库分类分级
分布式数据管理对数据实施分类分级保护，提供基于数据安全标签以及设备安全等级的访问控制机制。
数据安全标签和设备安全等级越高，加密措施和访问控制措施越严格，数据安全性越高。
运作机制
数据库备份与恢复机制
数据库在备份时，会将当前的数据库备份在指定的文件中，后续对数据库的操作不会影响备份的数据库文件。只有当恢复指定数据库文件时，才会将备份的数据库文件覆盖当前数据库，实现数据的回滚。
-  键值型数据库备份路径：/data/service/el1(el2)/public/database/...{appId}/kvdb/backup/...{storeId}
-  关系型数据库备份路径：/data/app/el1(el2)/100/database/...{bundlename}/rdb
数据库加密机制
HarmonyOS数据库加密时，应用开发者无需传入密钥，只需要设置数据库加密的状态即可。系统会自动帮助开发者将数据库加密，使用huks通用密钥库系统，完成数据库密钥的生成及加密保护。
约束限制
-  数据库加密的密钥一年自动更换一次。
-  键值型数据库最多可以备份5份。
-  键值型数据库的自动备份需要在熄屏且充电的状态下进行。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-backup-and-restore-V14
爬取时间: 2025-04-27 22:42:50
来源: Huawei Developer
场景介绍
当应用在处理一项重要的操作，显然是不能被打断的。例如：写入多个表关联的事务。此时，每个表的写入都是单独的，但是表与表之间的事务关联性不能被分割。
如果操作的过程中出现问题，开发者可以使用恢复功能，将数据库恢复到之前的状态，重新对数据库进行操作。
在数据库被篡改、删除、或者设备断电场景下，数据库可能会因为数据丢失、数据损坏、脏数据等而不可用，可以通过数据库的备份恢复能力将数据库恢复至可用状态。
键值型数据库和关系型数据库均支持对数据库的备份和恢复。另外，键值型数据库还支持删除数据库备份，以释放本地存储空间。
键值型数据库备份、恢复与删除
键值型数据库，通过backup接口实现数据库备份，通过restore接口实现数据库恢复，通过deletebackup接口删除数据库备份。具体接口及功能，可见分布式键值数据库。
1.  创建数据库。 (1) 创建kvManager。 (2) 配置数据库参数。 (3) 创建kvStore。
```typescript
import { distributedKVStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
let kvManager: distributedKVStore.KVManager;
let kvStore: distributedKVStore.SingleKVStore | undefined = undefined;
let context = getContext(this);
const kvManagerConfig: distributedKVStore.KVManagerConfig = {
context: context,
bundleName: 'com.example.datamanagertest'
}
try {
kvManager = distributedKVStore.createKVManager(kvManagerConfig);
console.info('Succeeded in creating KVManager.');
try {
const options: distributedKVStore.Options = {
createIfMissing: true,
encrypt: true,
backup: false,
autoSync: false,
kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
securityLevel: distributedKVStore.SecurityLevel.S3
};
kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options, (err, store: distributedKVStore.SingleKVStore) => {
if (err) {
console.error(`Failed to get KVStore. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in getting KVStore.');
kvStore = store;
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to create KVManager. Code:${error.code},message:${error.message}`);
}
if (kvStore !== undefined) {
kvStore = kvStore as distributedKVStore.SingleKVStore;
//进行后续操作
//...
}
```
2.  使用put()方法插入数据。
```typescript
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value_test_string';
try {
kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err) => {
if (err !== undefined) {
console.error(`Fail to put data. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in putting data.');
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
```
3.  使用backup()方法备份数据。
```typescript
let backupFile = 'BK001';
try {
kvStore.backup(backupFile, (err) => {
if (err) {
console.error(`Fail to backup data.code:${err.code},message:${err.message}`);
} else {
console.info('Succeeded in backupping data.');
}
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
```
4.  使用delete()方法删除数据（模拟意外删除、篡改场景）。
```typescript
try {
kvStore.delete(KEY_TEST_STRING_ELEMENT, (err) => {
if (err !== undefined) {
console.error(`Fail to delete data. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in deleting data.');
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
```
5.  使用restore()方法恢复数据。
```typescript
try {
kvStore.restore(backupFile, (err) => {
if (err) {
console.error(`Fail to restore data. Code:${err.code},message:${err.message}`);
} else {
console.info('Succeeded in restoring data.');
}
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
```
6.  当本地设备存储空间有限或需要重新备份时，还可使用deleteBackup()方法删除备份，释放存储空间。
```typescript
let files = [backupFile];
try {
kvStore.deleteBackup(files).then((data) => {
console.info(`Succeed in deleting Backup. Data:filename is ${data[0]},result is ${data[1]}.`);
}).catch((err: BusinessError) => {
console.error(`Fail to delete Backup. Code:${err.code},message:${err.message}`);
})
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
```
关系型数据库备份
数据库操作或者存储过程中，有可能会因为各种原因发生非预期的数据库异常的情况，可以根据需要使用关系型数据库的备份能力，以便在数据库异常时，可靠高效地恢复数据保证业务数据正常使用。
关系型数据库支持两种手动备份和自动备份（仅系统应用可用）两种方式。
手动备份
手动备份：通过调用backup接口实现数据库手动备份。示例如下：
```typescript
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
let store: relationalStore.RdbStore | undefined = undefined;
let context = getContext(this);
const STORE_CONFIG: relationalStore.StoreConfig = {
name: 'RdbTest.db',
securityLevel: relationalStore.SecurityLevel.S3,
allowRebuild: true
};
relationalStore.getRdbStore(context, STORE_CONFIG, (err, rdbStore) => {
store = rdbStore;
if (err) {
console.error(`Failed to get RdbStore. Code:${err.code},message:${err.message}`);
return;
}
store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)', (err) => {
})
console.info('Succeeded in getting RdbStore.');
// "Backup.db"为备份数据库文件名，默认在RdbStore同路径下备份。也可指定路径：customDir + "backup.db"
(store as relationalStore.RdbStore).backup("Backup.db", (err: BusinessError) => {
if (err) {
console.error(`Failed to backup RdbStore. Code:${err.code}, message:${err.message}`);
return;
}
console.info(`Succeeded in backing up RdbStore.`);
})
})
```
关系型数据库异常重建
在创建或使用关系型数据库的过程中，抛出14800011异常错误码说明数据库出现异常，可以删除数据库后恢复数据。
需要通过在StoreConfig中配置allowRebuild参数为true以设置数据库在出现异常时自动删库。数据库重建成功后为空库，需要开发者重新建表并且使用提前备份好的数据进行数据恢复，备份操作可见关系型数据库备份，数据恢复可见关系型数据库恢复。
若数据库异常前已配置StoreConfig中的allowRebuild为true，则数据库出现异常时将自动删库。
若数据库异常前未配置StoreConfig中的allowRebuild或allowRebuild配置为false，则需将其配置为true再次进行开库。具体示例如下：
```typescript
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
let store: relationalStore.RdbStore | undefined = undefined;
let context = getContext(this);
const STORE_CONFIG: relationalStore.StoreConfig = {
name: 'RdbTest.db',
securityLevel: relationalStore.SecurityLevel.S3,
allowRebuild: true
};
relationalStore.getRdbStore(context, STORE_CONFIG, (err, rdbStore) => {
store = rdbStore;
if (err) {
console.error(`Failed to get RdbStore. Code:${err.code},message:${err.message}`);
return;
}
store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)', (err) => {
})
console.info('Succeeded in getting RdbStore.');
})
```
关系型数据库数据恢复
针对数据库出现异常的情况，在数据库重建成功后，需要用提前备份好的数据进行数据恢复。
恢复方式分以下两种，手动备份恢复和自动备份恢复（仅系统应用可用）。
恢复手动备份数据
关系型数据库通过调用backup接口可以实现手动备份数据库，通过restore接口可以实现手动恢复数据库。
具体恢复过程和关键示例代码片段如下，完整示例代码请结合关系型数据库的备份、重建等上下文进行实现。
1.  抛出数据库异常错误码。
```typescript
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
if (store != undefined) {
(store as relationalStore.RdbStore).query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]).then((result: relationalStore.ResultSet) => {
let resultSet = result;
try {
/* ...
业务的增删改逻辑
...
*/
// 抛出异常
if (resultSet?.rowCount == -1) {
resultSet ?.isColumnNull(0);
}
// todo resultSet.goToFirstRow(), resultSet.count等其它接口也会抛异常
while (resultSet.goToNextRow()) {
console.info(JSON.stringify(resultSet.getRow()))
}
resultSet.close();
} catch (err) {
if (err.code === 14800011) {
// 执行下文的步骤，即关闭结果集之后进行数据的恢复
}
console.error(JSON.stringify(err));
}
})
}
```
2.  关闭所有打开着的结果集。
```typescript
// 获取所有打开着的结果集
let resultSets: Array<relationalStore.ResultSet> = [];
// 使用resultSet.close()方法关闭所有打开着的结果集
for (let resultSet of resultSets) {
try {
resultSet.close();
} catch (e) {
if (e.code !== 14800014) {
console.error(`Code:${e.code}, message:${e.message}`);
}
}
}
```
3.  调用restore接口恢复数据。
```typescript
try {
let context = getContext();
// "Backup.db"为备份数据库文件名，默认在RdbStore同路径下备份。也可指定路径：customDir + "backup.db"
let backup = context.databaseDir + '/backup/test_backup.db';
if(!fileIo.access(backup)) {
console.info("no backup file");
try {
(store as relationalStore.RdbStore).close;
store = undefined;
} catch (e) {
if (e.code != 14800014) {
console.info(JSON.stringify(e));
}
}
let storeConfig: relationalStore.StoreConfig = {
name: "BackupResotreTest.db",
securityLevel: relationalStore.SecurityLevel.S3,
allowRebuild: true
}
// todo 开库建表
// todo 自行生成数据
return
}
// 调用restore接口恢复数据
(store as relationalStore.RdbStore).restore(backup);
} catch (e) {
console.error(`Code:${e.code}, message:${e.message}`);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-encryption-V14
爬取时间: 2025-04-27 22:43:04
来源: Huawei Developer
场景介绍
为了增强数据库的安全性，数据库提供了一个安全适用的数据库加密能力，从而对数据库存储的内容实施有效保护。通过数据库加密等安全方法实现了数据库数据存储的保密性和完整性要求，使得数据库以密文方式存储并在密态方式下工作，确保了数据安全。
加密后的数据库只能通过接口进行访问，无法通过其它方式打开数据库文件。数据库的加密属性在创建数据库时确认，无法变更。
键值型数据库和关系型数据库均支持数据库加密操作，其中关系型数据库支持自定义加密/解密的密钥和其他参数。
键值型数据库加密
键值型数据库，通过options中encrypt参数来设置是否加密，默认为false，表示不加密。encrypt参数为true时表示加密。
具体接口及功能，可见分布式键值数据库。
```typescript
import { distributedKVStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
let kvManager: distributedKVStore.KVManager | undefined = undefined;
let kvStore: distributedKVStore.SingleKVStore | undefined = undefined;
let context = getContext(this);
const kvManagerConfig: distributedKVStore.KVManagerConfig = {
context: context,
bundleName: 'com.example.datamanagertest',
}
try {
kvManager = distributedKVStore.createKVManager(kvManagerConfig);
console.info('Succeeded in creating KVManager.');
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to create KVManager. Code:${error.code},message:${error.message}`);
}
if (kvManager !== undefined) {
kvManager = kvManager as distributedKVStore.KVManager;
try {
const options: distributedKVStore.Options = {
createIfMissing: true,
// 设置数据库加密
encrypt: true,
backup: false,
autoSync: false,
kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
securityLevel: distributedKVStore.SecurityLevel.S3
};
kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options, (err, store: distributedKVStore.SingleKVStore) => {
if (err) {
console.error(`Fail to get KVStore. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in getting KVStore.');
kvStore = store;
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
}
if (kvStore !== undefined) {
kvStore = kvStore as distributedKVStore.SingleKVStore;
//进行后续操作
//...
}
```
关系型数据库加密
关系型数据库，通过StoreConfig中encrypt属性来设置是否加密。encrypt参数为true时表示加密；为false时表示不加密；默认值为false。
当encrypt为true时，支持开发者通过ArkTs API中的可选属性cryptoParam设置自定义的加密/解密密钥和算法等参数。Native侧暂不支持此配置项。
针对cryptoParam的配置与否，有如下两种场景：
场景1：不配置cryptoParam属性，此时会使用默认的加密配置进行数据库的加密/解密。
```typescript
import { relationalStore } from '@kit.ArkData';
let store: relationalStore.RdbStore;
let context = getContext(this);
const STORE_CONFIG: relationalStore.StoreConfig = {
name: 'RdbTest.db',
securityLevel: relationalStore.SecurityLevel.S3,
encrypt: true
};
relationalStore.getRdbStore(context, STORE_CONFIG, (err, rdbStore) => {
store = rdbStore;
if (err) {
console.error(`Failed to get RdbStore. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in getting RdbStore.');
})
```
场景2：配置cryptoParam属性，此时会使用开发者自定义的密钥和算法参数进行数据库的加密/解密。
```typescript
import { relationalStore } from '@kit.ArkData';
let context = getContext(this);
// 初始化需要使用的密钥
let key = new Uint8Array(32);
for (let i = 0; i < 32; i++) {
key[i] = i;
}
// 初始化加密算法
const CRYPTO_PARAM : relationalStore.CryptoParam = {
encryptionKey: key, // 必选参数，使用指定的密钥打开加密数据库。为空则由数据库负责生成并保存密钥，并使用生成的密钥打开数据库文件。
iterationCount: 25000, // 可选参数，迭代次数。迭代次数必须大于零。不指定或等于零则使用默认值10000和默认加密算法。
encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC, // 可选参数，加密/解密算法。如不指定，默认算法为AES_256_GCM。
hmacAlgo: relationalStore.HmacAlgo.SHA256, // 可选参数，HMAC算法。如不指定，默认值为SHA256。
kdfAlgo: relationalStore.KdfAlgo.KDF_SHA512, // 可选参数，KDF算法。如不指定，默认值和HMAC算法相等。
cryptoPageSize: 2048 // 可选参数，加密/解密时使用的页大小。必须为1024到65536范围内的整数并且为2的幂。如不指定，默认值为1024。
}
const STORE_CONFIG : relationalStore.StoreConfig = {
name: "encrypted.db",
securityLevel: relationalStore.SecurityLevel.S3,
encrypt: true,
cryptoParam: CRYPTO_PARAM
}
async function run() {
let store = await relationalStore.getRdbStore(context, STORE_CONFIG);
if (store == null) {
console.error('Failed to get RdbStore.');
} else {
console.info('Succeeded in getting RdbStore.');
}
// 调用完后需要将密钥清零
CRYPTO_PARAM.encryptionKey.fill(0);
}
run();
```
如果开发者不关心加密使用的算法及参数，则无需配置cryptoParam属性，使用默认加密配置即可。当开发者需要自定义加密配置，或需要打开非默认配置的加密数据库时，则需要配置cryptoParam属性。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/access-control-by-device-and-data-level-V14
爬取时间: 2025-04-27 22:43:17
来源: Huawei Developer
基本概念
分布式数据管理对数据实施分类分级保护，提供基于数据安全标签以及设备安全等级的访问控制机制。
数据安全标签和设备安全等级越高，加密措施和访问控制措施越严格，数据安全性越高。
数据安全标签
按照数据分类分级规范要求，可将数据分为S1、S2、S3、S4四个安全等级。
| 风险等级 | 风险标准 | 定义 | 样例 |
| --- | --- | --- | --- |
| 严重 | S4 | 业界法律法规定义的特殊数据类型，涉及个人的最私密领域的信息或一旦泄露、篡改、破坏、销毁可能会给个人或组织造成重大的不利影响的数据。 | 政治观点、宗教和哲学信仰、工会成员资格、基因数据、生物信息、健康和性生活状况，性取向等或设备认证鉴权、个人信用卡等财物信息等。 |
| 高 | S3 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严峻的不利影响。 | 个人实时精确定位信息、运动轨迹等。 |
| 中 | S2 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。 | 个人的详细通信地址、姓名昵称等。 |
| 低 | S1 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致有限的不利影响。 | 性别、国籍、用户申请记录等。 |
设备安全等级
根据设备安全能力，比如是否有TEE、是否有安全存储芯片等，将设备安全等级分为SL1、SL2、SL3、SL4、SL5五个等级。例如，手表通常为低安全的SL1设备，手机、平板通常为高安全的SL4设备。
在设备组网时可以通过hidumper -s 3511查看设备安全等级。
跨设备同步访问控制机制
数据跨设备同步时，数据管理基于数据安全标签和设备安全等级进行访问控制。规则为，在本设备的数据安全标签不高于对端设备的设备安全等级时，数据才能从本设备同步到对端设备，否则不能同步。具体访问控制矩阵如下：
| 设备安全级别 | 可同步的数据安全标签 |
| --- | --- |
| SL1 | S1 |
| SL2 | S1~S2 |
| SL3 | S1~S3 |
| SL4 | S1~S4 |
| SL5 | S1~S4 |
例如，手表通常为低安全的SL1设备。若创建数据安全标签为S1的数据库，则此数据库数据可以在这些设备间同步；若创建的数据库标签为S2-S4，则不能在这些设备间同步。
场景介绍
分布式数据库的访问控制机制确保了数据存储和同步时的安全能力。在创建数据库时，应当基于数据分类分级规范合理地设置数据库的安全标签，确保数据库内容和数据标签的一致性。
使用键值型数据库实现数据分级
键值型数据库，通过securityLevel参数设置数据库的安全等级。此处以创建安全等级为S3的数据库为例。
具体接口及功能，可见分布式键值数据库。
在单设备使用场景下，KV数据库支持修改securityLevel开库参数进行安全等级升级。数据库安全等级升级操作需要注意以下几点：
```typescript
import { distributedKVStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
let kvManager: distributedKVStore.KVManager;
let kvStore: distributedKVStore.SingleKVStore;
let context = getContext(this);
const kvManagerConfig: distributedKVStore.KVManagerConfig = {
context: context,
bundleName: 'com.example.datamanagertest'
}
try {
kvManager = distributedKVStore.createKVManager(kvManagerConfig);
console.info('Succeeded in creating KVManager.');
try {
const options: distributedKVStore.Options = {
createIfMissing: true,
encrypt: true,
backup: false,
autoSync: false,
kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
securityLevel: distributedKVStore.SecurityLevel.S3
};
kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options, (err, store: distributedKVStore.SingleKVStore) => {
if (err) {
console.error(`Failed to get KVStore. Code:${err.code},message:${err.message}`);
return;
}
console.info('Succeeded in getting KVStore.');
kvStore = store;
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to create KVManager. Code:${error.code},message:${error.message}`);
}
```
使用关系型数据库实现数据分级
关系型数据库，通过securityLevel参数设置数据库的安全等级。此处以创建安全等级为S3的数据库为例。
具体接口及功能，可见关系型数据库。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { relationalStore } from '@kit.ArkData';
let store: relationalStore.RdbStore;
let context = getContext(this);
const STORE_CONFIG: relationalStore.StoreConfig = {
name: 'RdbTest.db',
securityLevel: relationalStore.SecurityLevel.S3
};
let promise = relationalStore.getRdbStore(context, STORE_CONFIG);
promise.then(async (rdbStore) => {
store = rdbStore;
console.info('Succeeded in getting RdbStore.')
}).catch((err: BusinessError) => {
console.error(`Failed to get RdbStore. Code:${err.code},message:${err.message}`);
})
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/encrypted_estore_guidelines-V14
爬取时间: 2025-04-27 22:43:31
来源: Huawei Developer
场景介绍
为了满足数据库的安全特性，存有敏感信息的应用会在EL5（加密路径切换请参考获取和修改加密分区EL1-EL4路径切换）路径下创建了一个E类数据库。在锁屏的情况下，满足一定条件时，会触发密钥的销毁，此时E类数据库不可读写。当锁屏解锁后，密钥会恢复，E类数据库恢复正常读写操作。这样的设计可以有效防止用户数据的泄露。
然而，在锁屏的情况下，应用程序仍然可以继续写入数据，由于此时E类数据库不可读写，可能会导致数据丢失。为了解决这个问题，当前提供了一种方案：在锁屏的情况下，将数据存储在EL2路径下的C类数据库中。当解锁后，再将数据迁移到E类数据库中。这样可以确保数据在锁屏期间的安全性和完整性。
键值型数据库和关系型数据库均支持E类加密数据库。
实现机制
通过封装Mover类、Store类、SecretKeyObserver类和ECStoreManager类实现应用数据库密钥加锁和解锁状态下E类数据库和C类数据库的切换和操作。
Mover类：提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中有数据，使用该接口将数据迁移到E类数据库。
Store类：提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。
SecretKeyObserver类：提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。
ECStoreManager类：用于管理应用的E类数据库和C类数据库。
配置权限
使用EL5路径下的数据库，需要配置ohos.permission.PROTECT_SCREEN_LOCK_DATA权限。
```typescript
// module.json5
"requestPermissions": [
{
"name": "ohos.permission.PROTECT_SCREEN_LOCK_DATA"
}
]
```
键值型数据库E类加密
本章节提供键值型数据库的E类加密数据库使用方式，提供Mover类、Store类、SecretKeyObserver类和ECStoreManager类的具体实现，并在EntryAbility和index按键事件中展示这几个类的使用方式。
Mover
提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中存在数据，使用该接口将数据迁移到E类数据库。
```typescript
// Mover.ts
import { distributedKVStore } from '@kit.ArkData';
export class Mover {
async move(eStore: distributedKVStore.SingleKVStore, cStore: distributedKVStore.SingleKVStore): Promise<void> {
if (eStore != null && cStore != null) {
let entries: distributedKVStore.Entry[] = await cStore.getEntries('key_test_string');
await eStore.putBatch(entries);
console.info(`ECDB_Encry move success`);
}
}
}
```
Store
提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。
```typescript
// Store.ts
import { distributedKVStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
let kvManager: distributedKVStore.KVManager;
export class StoreInfo {
kvManagerConfig: distributedKVStore.KVManagerConfig;
storeId: string;
option: distributedKVStore.Options;
}
export class Store {
async getECStore(storeInfo: StoreInfo): Promise<distributedKVStore.SingleKVStore> {
try {
kvManager = distributedKVStore.createKVManager(storeInfo.kvManagerConfig);
console.info("Succeeded in creating KVManager");
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
}
if (kvManager !== undefined) {
kvManager = kvManager as distributedKVStore.KVManager;
let kvStore: distributedKVStore.SingleKVStore | null;
try {
kvStore = await kvManager.getKVStore<distributedKVStore.SingleKVStore>(storeInfo.storeId, storeInfo.option);
if (kvStore != undefined) {
console.info(`ECDB_Encry succeeded in getting store : ${storeInfo.storeId}`);
return kvStore;
}
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
}
}
putOnedata(kvStore: distributedKVStore.SingleKVStore): void {
if (kvStore != undefined) {
const KEY_TEST_STRING_ELEMENT = 'key_test_string' + String(Date.now());
const VALUE_TEST_STRING_ELEMENT = 'value_test_string' + String(Date.now());
try {
kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err) => {
if (err !== undefined) {
console.error(`Failed to put data. Code:${err.code},message:${err.message}`);
return;
}
console.info(`ECDB_Encry Succeeded in putting data.${KEY_TEST_STRING_ELEMENT}`);
});
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
}
}
getDataNum(kvStore: distributedKVStore.SingleKVStore): void {
if (kvStore != undefined) {
let resultSet: distributedKVStore.KVStoreResultSet;
kvStore.getResultSet("key_test_string").then((result: distributedKVStore.KVStoreResultSet) => {
console.info(`ECDB_Encry Succeeded in getting result set num ${result.getCount()}`);
resultSet = result;
if (kvStore != null) {
kvStore.closeResultSet(resultSet).then(() => {
console.info('Succeeded in closing result set');
}).catch((err: BusinessError) => {
console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
});
}
}).catch((err: BusinessError) => {
console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
});
}
}
deleteOnedata(kvStore: distributedKVStore.SingleKVStore): void {
if (kvStore != undefined) {
kvStore.getEntries('key_test_string', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
if (err != undefined) {
console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
return;
}
if (kvStore != null && entries.length != 0) {
kvStore.delete(entries[0].key, (err: BusinessError) => {
if (err != undefined) {
console.error(`Failed to delete.code is ${err.code},message is ${err.message}`);
return;
}
console.info('ECDB_Encry Succeeded in deleting');
});
}
});
}
}
updataOnedata(kvStore: distributedKVStore.SingleKVStore): void {
if (kvStore != undefined) {
kvStore.getEntries('key_test_string', async (err: BusinessError, entries: distributedKVStore.Entry[]) => {
if (err != undefined) {
console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
return;
}
if (kvStore != null && entries.length != 0) {
console.info(`ECDB_Encry old data:${entries[0].key},value :${entries[0].value.value.toString()}`)
await kvStore.put(entries[0].key, "new value_test_string" + String(Date.now()) + 'new').then(() => {
}).catch((err: BusinessError) => {
console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
});
}
console.info(`ECDB_Encry updata success`)
});
}
}
}
```
SecretKeyObserver
该类提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。
```typescript
// SecretKeyObserver.ts
import { ECStoreManager } from './ECStoreManager';
export enum SecretStatus {
Lock,
UnLock
}
export class SecretKeyObserver {
onLock(): void {
this.lockStatuas = SecretStatus.Lock;
this.storeManager.closeEStore();
}
onUnLock(): void {
this.lockStatuas = SecretStatus.UnLock;
}
getCurrentStatus(): number {
return this.lockStatuas;
}
initialize(storeManager: ECStoreManager): void {
this.storeManager = storeManager;
}
updatalockStatus(code: number) {
if (code === SecretStatus.Lock) {
this.onLock();
} else {
this.lockStatuas = code;
}
}
// 初始获取锁屏状态
private lockStatuas: number = SecretStatus.UnLock;
private storeManager: ECStoreManager;
}
export let lockObserve = new SecretKeyObserver();
```
ECStoreManager
ECStoreManager类用于管理应用的E类数据库和C类数据库。支持配置数据库信息、配置迁移函数的信息，可根据密钥状态为应用提供相应的数据库句柄，并提供了关闭E类数据库、数据迁移完成后销毁C类数据库等接口。
```typescript
// ECStoreManager.ts
import { distributedKVStore } from '@kit.ArkData';
import { Mover } from './Mover';
import { BusinessError } from '@kit.BasicServicesKit';
import { StoreInfo, Store } from './Store';
import { SecretStatus } from './SecretKeyObserver';
let store = new Store();
export class ECStoreManager {
config(cInfo: StoreInfo, other: StoreInfo): void {
this.cInfo = cInfo;
this.eInfo = other;
}
configDataMover(mover: Mover): void {
this.mover = mover;
}
async getCurrentStore(screanStatus: number): Promise<distributedKVStore.SingleKVStore> {
console.info(`ECDB_Encry GetCurrentStore start screanStatus: ${screanStatus}`);
if (screanStatus === SecretStatus.UnLock) {
try {
this.eStore = await store.getECStore(this.eInfo);
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to GetECStore.code is ${error.code},message is ${error.message}`);
}
// 解锁状态 获取e类库
if (this.needMove) {
if (this.eStore != undefined && this.cStore != undefined) {
await this.mover.move(this.eStore, this.cStore);
}
this.deleteCStore();
console.info(`ECDB_Encry Data migration is complete. Destroy cstore`);
this.needMove = false;
}
return this.eStore;
} else {
// 加锁状态 获取c类库
this.needMove = true;
try {
this.cStore = await store.getECStore(this.cInfo);
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to GetECStore.code is ${error.code},message is ${error.message}`);
}
return this.cStore;
}
}
closeEStore(): void {
try {
let kvManager = distributedKVStore.createKVManager(this.eInfo.kvManagerConfig);
console.info("Succeeded in creating KVManager");
if (kvManager != undefined) {
kvManager.closeKVStore(this.eInfo.kvManagerConfig.bundleName, this.eInfo.storeId);
this.eStore = null;
console.info(`ECDB_Encry close EStore success`)
}
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
}
}
deleteCStore(): void {
try {
let kvManager = distributedKVStore.createKVManager(this.cInfo.kvManagerConfig);
console.info("Succeeded in creating KVManager");
if (kvManager != undefined) {
kvManager.deleteKVStore(this.cInfo.kvManagerConfig.bundleName, this.cInfo.storeId);
this.cStore = null;
console.info("ECDB_Encry delete cStore success");
}
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
}
}
private eStore: distributedKVStore.SingleKVStore = null;
private cStore: distributedKVStore.SingleKVStore = null;
private cInfo: StoreInfo | null = null;
private eInfo: StoreInfo | null = null;
private needMove: boolean = false;
private mover: Mover | null = null;
}
```
EntryAbility
模拟应用启动期间，注册对COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED公共事件的监听，并配置相应的数据库信息、密钥状态信息等。
```typescript
// EntryAbility.ets
import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { distributedKVStore } from '@kit.ArkData';
import { ECStoreManager } from './ECStoreManager';
import { StoreInfo } from './Store';
import { Mover } from './Mover';
import { SecretKeyObserver } from './SecretKeyObserver';
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
export let storeManager = new ECStoreManager();
export let e_secretKeyObserver = new SecretKeyObserver();
let mover = new Mover();
let subscriber: commonEventManager.CommonEventSubscriber;
export function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
if (!err) {
console.info('ECDB_Encry createSubscriber');
subscriber = commonEventSubscriber;
try {
commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
if (err) {
console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
} else {
console.info(`ECDB_Encry SubscribeCB ${data.code}`);
e_secretKeyObserver.updatalockStatus(data.code);
}
});
} catch (error) {
const err: BusinessError = error as BusinessError;
console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
}
} else {
console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
}
}
let cInfo: StoreInfo | null = null;
let eInfo: StoreInfo | null = null;
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
let cContext = this.context;
cInfo = {
"kvManagerConfig": {
context: cContext,
bundleName: 'com.example.ecstoredemo',
},
"storeId": "cstore",
"option": {
createIfMissing: true,
encrypt: false,
backup: false,
autoSync: false,
// kvStoreType不填时，默认创建多设备协同数据库
kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
// 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE_COLLABORATION,
securityLevel: distributedKVStore.SecurityLevel.S3
}
}
let eContext = this.context.createModuleContext("entry");
eContext.area = contextConstant.AreaMode.EL5;
eInfo = {
"kvManagerConfig": {
context: eContext,
bundleName: 'com.example.ecstoredemo',
},
"storeId": "estore",
"option": {
createIfMissing: true,
encrypt: false,
backup: false,
autoSync: false,
// kvStoreType不填时，默认创建多设备协同数据库
kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
// 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE_COLLABORATION,
securityLevel: distributedKVStore.SecurityLevel.S3
}
}
console.info(`ECDB_Encry store area : estore:${eContext.area},cstore${cContext.area}`);
// 监听COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED事件 code == 1解锁状态，code==0加锁状态
try {
commonEventManager.createSubscriber({
events: ['COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED']
}, createCB);
console.info(`ECDB_Encry success subscribe`);
} catch (error) {
const err: BusinessError = error as BusinessError;
console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
}
storeManager.config(cInfo, eInfo);
storeManager.configDataMover(mover);
e_secretKeyObserver.initialize(storeManager);
}
onDestroy(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
}
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
windowStage.loadContent('pages/Index', (err) => {
if (err.code) {
hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
});
}
onWindowStageDestroy(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
}
onForeground(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
}
onBackground(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
}
}
```
Index按键事件
使用Button按钮，通过点击按钮来模拟应用操作数据库，如插入数据、删除数据、更新数据和获取数据数量的操作等，展示数据库基本的增删改查能力。
```typescript
// Index.ets
import { storeManager, e_secretKeyObserver } from "../entryability/EntryAbility";
import { distributedKVStore } from '@kit.ArkData';
import { Store } from '../entryability/Store';
let storeOption = new Store();
let lockStatus: number = 1;
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Column() {
Button('加锁/解锁').onClick((event: ClickEvent) => {
if (lockStatus) {
e_secretKeyObserver.onLock();
lockStatus = 0;
} else {
e_secretKeyObserver.onUnLock();
lockStatus = 1;
}
lockStatus ? this.message = "解锁" : this.message = "加锁";
}).margin("5");
Button('store type').onClick(async (event: ClickEvent) => {
e_secretKeyObserver.getCurrentStatus() ? this.message = "estroe" : this.message = "cstore";
}).margin("5");
Button("put").onClick(async (event: ClickEvent) => {
let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
storeOption.putOnedata(store);
}).margin(5)
Button("Get").onClick(async (event: ClickEvent) => {
let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
storeOption.getDataNum(store);
}).margin(5)
Button("delete").onClick(async (event: ClickEvent) => {
let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
storeOption.deleteOnedata(store);
}).margin(5)
Button("updata").onClick(async (event: ClickEvent) => {
let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
storeOption.updataOnedata(store);
}).margin(5)
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
}
.width('100%')
}
.height('100%')
}
}
```
关系型数据库E类加密
本章节提供关系型数据库的E类加密数据库使用方式，提供Mover类，Store类，SecretKeyObserver类和ECStoreManager类的具体实现，并在EntryAbility和index按键事件中展示这几个类的使用方式。
Mover
提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中有数据，使用该接口将数据迁移到E类数据库。
```typescript
// Mover.ts
import { relationalStore } from '@kit.ArkData';
export class Mover {
async move(eStore: relationalStore.RdbStore, cStore: relationalStore.RdbStore) {
if (eStore != null && cStore != null) {
let predicates = new relationalStore.RdbPredicates('employee');
let resultSet = await cStore.query(predicates);
while (resultSet.goToNextRow()) {
let bucket = resultSet.getRow();
await eStore.insert('employee', bucket);
}
}
}
}
```
Store
提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。其中StoreInfo类用于存储获取数据库相关信息。
```typescript
// Store.ts
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { Context } from '@kit.AbilityKit';
export class StoreInfo {
context: Context;
config: relationalStore.StoreConfig;
storeId: string;
}
let id = 1;
const SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)';
export class Store {
async getECStore(storeInfo: StoreInfo): Promise<relationalStore.RdbStore> {
let rdbStore: relationalStore.RdbStore | null;
try {
rdbStore = await relationalStore.getRdbStore(storeInfo.context, storeInfo.config);
if (rdbStore.version == 0) {
await rdbStore.executeSql(SQL_CREATE_TABLE);
console.info(`ECDB_Encry succeeded in getting Store ：${storeInfo.storeId}`);
rdbStore.version = 1;
}
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
return rdbStore;
}
async putOnedata(rdbStore: relationalStore.RdbStore) {
if (rdbStore != undefined) {
const valueBucket: relationalStore.ValuesBucket = {
ID: id++,
NAME: 'Lisa',
AGE: 18,
SALARY: 100.5,
CODES: new Uint8Array([1, 2, 3, 4, 5]),
};
try {
await rdbStore.insert("EMPLOYEE", valueBucket);
console.info(`ECDB_Encry insert success`);
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
}
}
async getDataNum(rdbStore: relationalStore.RdbStore) {
if (rdbStore != undefined) {
try {
let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
let resultSet = await rdbStore.query(predicates);
let count = resultSet.rowCount;
console.info(`ECDB_Encry getdatanum success count : ${count}`);
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
}
}
async deleteAlldata(rdbStore: relationalStore.RdbStore) {
if (rdbStore != undefined) {
try {
let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.equalTo('AGE', 18);
await rdbStore.delete(predicates);
console.info(`ECDB_Encry delete Success`);
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
}
}
async updataOnedata(rdbStore: relationalStore.RdbStore) {
if (rdbStore != undefined) {
try {
let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.equalTo('NAME', 'Lisa');
const valueBucket: relationalStore.ValuesBucket = {
NAME: 'Anna',
SALARY: 100.5,
CODES: new Uint8Array([1, 2, 3, 4, 5]),
};
await rdbStore.update(valueBucket, predicates);
console.info(`ECDB_Encry update success`);
} catch (e) {
let error = e as BusinessError;
console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
}
}
}
}
```
SecretKeyObserver
该类提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。
```typescript
// SecretKeyObserver.ts
import { ECStoreManager } from './ECStoreManager';
export enum SecretStatus {
Lock,
UnLock
}
export class SecretKeyObserver {
onLock(): void {
this.lockStatuas = SecretStatus.Lock;
this.storeManager.closeEStore();
}
onUnLock(): void {
this.lockStatuas = SecretStatus.UnLock;
}
getCurrentStatus(): number {
return this.lockStatuas;
}
initialize(storeManager: ECStoreManager): void {
this.storeManager = storeManager;
}
updatalockStatus(code: number) {
if (this.lockStatuas === SecretStatus.Lock) {
this.onLock();
} else {
this.lockStatuas = code;
}
}
private lockStatuas: number = SecretStatus.UnLock;
private storeManager: ECStoreManager;
}
export let lockObserve = new SecretKeyObserver();
```
ECStoreManager
ECStoreManager类用于管理应用的E类数据库和C类数据库。支持配置数据库信息、配置迁移函数的信息，可根据密钥状态为应用提供相应的数据库句柄，并提供了关闭E类数据库、数据迁移完成后销毁C类数据库等接口。
```typescript
// ECStoreManager.ts
import { relationalStore } from '@kit.ArkData';
import { Mover } from './Mover';
import { BusinessError } from '@kit.BasicServicesKit';
import { StoreInfo, Store } from './Store';
import { SecretStatus } from './SecretKeyObserver';
let store = new Store();
export class ECStoreManager {
config(cInfo: StoreInfo, other: StoreInfo): void {
this.cInfo = cInfo;
this.eInfo = other;
}
configDataMover(mover: Mover): void {
this.mover = mover;
}
async getCurrentStore(screanStatus: number): Promise<relationalStore.RdbStore> {
if (screanStatus === SecretStatus.UnLock) {
try {
this.eStore = await store.getECStore(this.eInfo);
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to GetECStore.code is ${error.code},message is ${error.message}`);
}
// 解锁状态 获取e类库
if (this.needMove) {
if (this.eStore != undefined && this.cStore != undefined) {
await this.mover.move(this.eStore, this.cStore);
console.info(`ECDB_Encry cstore data move to estore success`);
}
this.deleteCStore();
this.needMove = false;
}
return this.eStore;
} else {
// 加锁状态 获取c类库
this.needMove = true;
try {
this.cStore = await store.getECStore(this.cInfo);
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to GetECStore.code is ${error.code},message is ${error.message}`);
}
return this.cStore;
}
}
closeEStore(): void {
this.eStore = undefined;
}
async deleteCStore() {
try {
await relationalStore.deleteRdbStore(this.cInfo.context, this.cInfo.storeId)
} catch (e) {
let error = e as BusinessError;
console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
}
}
private eStore: relationalStore.RdbStore = null;
private cStore: relationalStore.RdbStore = null;
private cInfo: StoreInfo | null = null;
private eInfo: StoreInfo | null = null;
private needMove: boolean = false;
private mover: Mover | null = null;
}
```
EntryAbility
模拟在应用启动期间，注册对COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED公共事件的监听，并配置相应的数据库信息、密钥状态信息等。
```typescript
// EntryAbility.ets
import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { relationalStore } from '@kit.ArkData';
import { ECStoreManager } from './ECStoreManager';
import { StoreInfo } from './Store';
import { Mover } from './Mover';
import { SecretKeyObserver } from './SecretKeyObserver';
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
export let storeManager = new ECStoreManager();
export let e_secretKeyObserver = new SecretKeyObserver();
let mover = new Mover();
let subscriber: commonEventManager.CommonEventSubscriber;
export function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
if (!err) {
console.info('ECDB_Encry createSubscriber');
subscriber = commonEventSubscriber;
try {
commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
if (err) {
console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
} else {
console.info(`ECDB_Encry SubscribeCB ${data.code}`);
e_secretKeyObserver.updatalockStatus(data.code);
}
});
} catch (error) {
const err: BusinessError = error as BusinessError;
console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
}
} else {
console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
}
}
let cInfo: StoreInfo | null = null;
let eInfo: StoreInfo | null = null;
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
let cContext = this.context;
cInfo = {
context: cContext,
config: {
name: 'cstore.db',
securityLevel: relationalStore.SecurityLevel.S3,
},
storeId: "cstore.db"
}
let eContext = this.context.createModuleContext("entry");
eContext.area = contextConstant.AreaMode.EL5;
eInfo = {
context: eContext,
config: {
name: 'estore.db',
securityLevel: relationalStore.SecurityLevel.S3,
},
storeId: "estore.db",
}
// 监听COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED事件 code == 1解锁状态，code==0加锁状态
console.info(`ECDB_Encry store area : estore:${eContext.area},cstore${cContext.area}`)
try {
commonEventManager.createSubscriber({
events: ['COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED']
}, createCB);
console.info(`ECDB_Encry success subscribe`);
} catch (error) {
const err: BusinessError = error as BusinessError;
console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
}
storeManager.config(cInfo, eInfo);
storeManager.configDataMover(mover);
e_secretKeyObserver.initialize(storeManager);
}
onDestroy(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
}
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
windowStage.loadContent('pages/Index', (err) => {
if (err.code) {
hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
});
}
onWindowStageDestroy(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
}
onForeground(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
}
onBackground(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
}
}
```
Index按键事件
使用Button按钮，通过点击按钮来模拟应用操作数据库，如插入数据、删除数据、更新数据和获取数据数量的操作等，展示数据库基本的增删改查能力。
```typescript
// Index.ets
import { storeManager, e_secretKeyObserver } from "../entryability/EntryAbility";
import { relationalStore } from '@kit.ArkData';
import { Store } from '../entryability/Store';
let storeOption = new Store();
let lockStatus: number = 1;
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Column() {
Button('加锁/解锁').onClick((event: ClickEvent) => {
if (lockStatus) {
e_secretKeyObserver.onLock();
lockStatus = 0;
} else {
e_secretKeyObserver.onUnLock();
lockStatus = 1;
}
lockStatus ? this.message = "解锁" : this.message = "加锁";
}).margin("5");
Button('store type').onClick(async (event: ClickEvent) => {
e_secretKeyObserver.getCurrentStatus() ? this.message = "estroe" : this.message = "cstore";
console.info(`ECDB_Encry current store : ${this.message}`);
}).margin("5");
Button("put").onClick(async (event: ClickEvent) => {
let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
storeOption.putOnedata(store);
}).margin(5)
Button("Get").onClick(async (event: ClickEvent) => {
let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
storeOption.getDataNum(store);
}).margin(5)
Button("delete").onClick(async (event: ClickEvent) => {
let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
storeOption.deleteAlldata(store);
}).margin(5)
Button("updata").onClick(async (event: ClickEvent) => {
let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
storeOption.updataOnedata(store);
}).margin(5)
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/cross-app-data-share-V14
爬取时间: 2025-04-27 22:43:45
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/data-share-overview-V14
爬取时间: 2025-04-27 22:43:59
来源: Huawei Developer
功能简介
跨应用数据共享提供了向其他应用共享以及管理其数据的方法，支持不同应用之间的数据协同。
在许多应用场景中都需要用到数据共享，比如将电话簿、短信、媒体库中的数据共享给其他应用等。当然，不是所有的数据都允许其他应用访问，比如账号、密码等；有些数据也只允许其他应用查询而不允许其删改，比如短信等。所以针对不同数据共享场景以及数据隐私保护，设计一个安全、便捷的跨应用数据共享机制是十分必要的。
当前，基于跨应用数据共享中涉及的数据提供方应用个数的不同情况，数据管理提供支持一对多跨应用数据共享和多对多跨应用数据共享的能力。
基本概念
在进行跨应用数据共享开发前，先了解以下相关概念。
-  数据提供方：提供数据及实现相关业务的应用程序，也称为生产者或服务端。
-  数据访问方：访问数据提供方所提供的数据或业务的应用程序，也称为消费者或客户端。
-  数据集：用户要插入的数据集合，可以是一条或多条数据。数据集以键值对的形式存在，键为字符串类型，值支持数字、字符串、布尔值、无符号整型数组等多种数据类型。
-  结果集：用户查询之后的结果集合，其提供了灵活的数据访问方式，以便用户获取各项数据。
-  谓词：用户访问数据库中的数据所使用的筛选条件，经常被应用在更新数据、删除数据和查询数据等场景。
一对多跨应用数据共享
跨应用一对多数据共享的场景，目前仅对系统应用开放，暂不具体展开提供相关内容和指导。
多对多跨应用数据共享
区别于一对多数据共享只有一个数据提供方，当多个应用之间需要相互进行数据共享时，即多对多的跨应用数据共享场景下，对于数据的定义、流通和权限管理等是十分必要的。统一数据管理框架（Unified Data Management Framework, UDMF）即提供一种新的数据共享与交互方式，可以实现多对多跨应用数据共享，具体相关实现可见下文。
具体实现
通过标准化数据通路实现数据共享
应用可以根据UDMF标准化数据通路提供的数据接入与读取接口，将符合标准化数据定义的数据写入UDMF不同的数据共享通路，并提供多应用进行读取。写入UDMF中的数据依据应用定义的权限、数据通路定义的权限以及整个UDMF框架定义的权限管理逻辑进行管理，写入通路中的数据的生命周期的管理也遵循上述逻辑。这样离散在各个应用的碎片化数据可以在UDMF的不同通路中形成聚合效应，提升开发者跨应用数据协同的效率，同时提升用户的数据体验。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/many-to-many-data-share-V14
爬取时间: 2025-04-27 22:44:13
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/unified-data-channels-V14
爬取时间: 2025-04-27 22:44:26
来源: Huawei Developer
场景介绍
在多对多跨应用数据共享的场景下，需要提供一条数据通路能够接入多个不同应用的数据并共享给其他应用进行读取。
UDMF针对多对多跨应用数据共享的不同业务场景提供了标准化的数据通路，提供了标准化的数据接入与读取接口。
标准化数据通路的定义和实现
标准化数据通路是为各种业务场景提供的跨应用的数据接入与读取通路，它可以暂存应用需要共享的符合标准化数据定义的统一数据对象，并提供给其他应用进行访问，同时按照一定的策略对暂存数据的修改、删除权限和生命周期进行管理。
标准化数据通路通过UDMF提供的系统服务实现，应用（数据提供方）需要共享公共数据时可以通过UDMF提供的插入接口将数据写入到UDMF的数据通路中，并且可以通过UDMF提供的更新和删除接口对本应用已经存入数据进行更新和删除操作。目标应用（数据访问方）可以通过UDMF提供的读取接口进行数据的访问。UDMF会统一对数据的生命周期进行管理，每小时定期清理存入时长超过一小时的数据。
统一数据对象UnifiedData在UDMF数据通路中具有全局唯一URI标识，其定义为udmf://intention/bundleName/groupId，其中各组成部分的含义分别为：
-  udmf:协议名，表示使用UDMF提供的数据通路。
-  intention:UDMF已经支持的数据通路类型枚举值，对应不同的业务场景。
-  bundleName:数据来源应用的包名称。
-  groupId:分组名称，支持批量数据分组管理。
当前UDMF中的跨应用数据共享通路有：公共数据通路
公共数据通路：应用共享的公用数据共享通路，所有应用均可向通路中写入数据，写入方可以根据写入数据时生成的数据唯一标识符进行数据的更新、删除、指定数据标识符进行查询、全量查询，而数据读取方只能读取当前数据通路中的全量数据，通路对应的Intention枚举类型为DATA_HUB。
接口说明
以下是UDMF标准化数据通路的相关接口，均为异步接口。异步接口均有callback和Promise两种返回形式，下表均以callback形式为例，更多接口及使用方式请见标准化数据通路和标准化数据定义与描述。
| 接口名称 | 描述 |
| --- | --- |
| insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void | 将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符，使用callback异步回调。 |
| updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void | 更新已写入UDMF的公共数据通路的数据，使用callback异步回调。 |
| queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void | 查询UDMF公共数据通路的数据，使用callback异步回调。 |
| deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void | 删除UDMF公共数据通路的数据，返回删除的数据集，使用callback异步回调。 |
开发步骤
以一次多对多数据共享的过程为例说明开发步骤，数据提供方可以通过UMDF提供的insertData接口将数据写入公共数据通路，获取到的返回值（生成的数据的唯一标识符），可用于对其插入的数据进行更新和删除操作。数据访问方则可以通过UDMF提供的查询接口获取当前公共数据通路的全量数据。
数据提供方
1.  导入unifiedDataChannel和uniformTypeDescriptor模块。
```typescript
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
```
2.  创建一个统一数据对象并插入到UDMF的公共数据通路中。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
let plainText = new unifiedDataChannel.PlainText();
plainText.textContent = 'hello world!';
let unifiedData = new unifiedDataChannel.UnifiedData(plainText);
// 指定要插入数据的数据通路枚举类型
let options: unifiedDataChannel.Options = {
intention: unifiedDataChannel.Intention.DATA_HUB
}
try {
unifiedDataChannel.insertData(options, unifiedData, (err, key) => {
if (err === undefined) {
console.info(`Succeeded in inserting data. key = ${key}`);
} else {
console.error(`Failed to insert data. code is ${err.code},message is ${err.message} `);
}
});
} catch (e) {
let error: BusinessError = e as BusinessError;
console.error(`Insert data throws an exception. code is ${error.code},message is ${error.message} `);
}
```
3.  更新上一步骤插入的统一数据对象。
```typescript
let plainTextUpdate = new unifiedDataChannel.PlainText();
plainTextUpdate.textContent = 'How are you!';
let unifiedDataUpdate = new unifiedDataChannel.UnifiedData(plainTextUpdate);
// 指定要更新的统一数据对象的URI
let optionsUpdate: unifiedDataChannel.Options = {
// 此处的key值仅为示例，不可直接使用，其值与insertData接口回调函数中key保持一致
key: 'udmf://DataHub/com.ohos.test/0123456789'
};
try {
unifiedDataChannel.updateData(optionsUpdate, unifiedDataUpdate, (err) => {
if (err === undefined) {
console.info('Succeeded in updating data.');
} else {
console.error(`Failed to update data. code is ${err.code},message is ${err.message} `);
}
});
} catch (e) {
let error: BusinessError = e as BusinessError;
console.error(`Update data throws an exception. code is ${error.code},message is ${error.message} `);
}
```
4.  删除存储在UDMF公共数据通路中的统一数据对象。
```typescript
// 指定要删除数据的数据通路枚举类型
let optionsDelete: unifiedDataChannel.Options = {
intention: unifiedDataChannel.Intention.DATA_HUB
};
try {
unifiedDataChannel.deleteData(optionsDelete, (err, data) => {
if (err === undefined) {
console.info(`Succeeded in deleting data. size = ${data.length}`);
for (let i = 0; i < data.length; i++) {
let records = data[i].getRecords();
for (let j = 0; j < records.length; j++) {
if (records[j].getType() === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
let text = records[j] as unifiedDataChannel.PlainText;
console.info(`${i + 1}.${text.textContent}`);
}
}
}
} else {
console.error(`Failed to delete data. code is ${err.code},message is ${err.message} `);
}
});
} catch (e) {
let error: BusinessError = e as BusinessError;
console.error(`Delete data throws an exception. code is ${error.code},message is ${error.message} `);
}
```
数据访问方
1.  导入unifiedDataChannel和uniformTypeDescriptor模块。
```typescript
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
```
2.  查询存储在UDMF公共数据通路中的全量统一数据对象。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
// 指定要查询数据的数据通路枚举类型
let options: unifiedDataChannel.Options = {
intention: unifiedDataChannel.Intention.DATA_HUB
};
try {
unifiedDataChannel.queryData(options, (err, data) => {
if (err === undefined) {
console.info(`Succeeded in querying data. size = ${data.length}`);
for (let i = 0; i < data.length; i++) {
let records = data[i].getRecords();
for (let j = 0; j < records.length; j++) {
if (records[j].getType() === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
let text = records[j] as unifiedDataChannel.PlainText;
console.info(`${i + 1}.${text.textContent}`);
}
}
}
} else {
console.error(`Failed to query data. code is ${err.code},message is ${err.message} `);
}
});
} catch(e) {
let error: BusinessError = e as BusinessError;
console.error(`Query data throws an exception. code is ${error.code},message is ${error.message} `);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/native-relational-store-guidelines-V14
爬取时间: 2025-04-27 22:44:40
来源: Huawei Developer
场景介绍
RelationalStore提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。
基本概念
-  谓词：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。
-  结果集：指用户查询之后的结果集合，可以对数据进行访问。结果集提供了灵活的数据访问方式，可以更方便地拿到用户想要的数据。
约束限制
-  系统默认日志方式是WAL（Write Ahead Log）模式，系统默认落盘方式是FULL模式。
-  数据库中连接池的最大数量是4个，用以管理用户的读操作。
-  为保证数据的准确性，数据库同一时间只能支持一个写操作。
-  当应用被卸载完成后，设备上的相关数据库文件及临时文件会被自动清除。
-  使用API11新增的端云同步等接口时，需要确保已实现云服务功能。
接口说明
详细的接口说明请参考RDB。
| 接口名称 | 描述 |
| --- | --- |
| OH_Rdb_GetOrOpen(const OH_Rdb_Config *config, int *errCode) | 获得一个相关的OH_Rdb_Store实例，操作关系型数据库。 |
| OH_Rdb_Execute(OH_Rdb_Store *store, const char *sql) | 执行包含指定参数但不返回值的SQL语句。 |
| OH_Rdb_Insert(OH_Rdb_Store *store, const char *table, OH_VBucket *valuesBucket) | 向目标表中插入一行数据。 |
| OH_Rdb_Update(OH_Rdb_Store *store, OH_VBucket *valuesBucket, OH_Predicates *predicates) | 根据OH_Predicates的指定实例对象更新数据库中的数据。 |
| OH_Rdb_Delete(OH_Rdb_Store *store, OH_Predicates *predicates) | 根据OH_Predicates的指定实例对象从数据库中删除数据。 |
| OH_Rdb_Query(OH_Rdb_Store *store, OH_Predicates *predicates, const char *const *columnNames, int length) | 根据指定条件查询数据库中的数据。 |
| OH_Rdb_DeleteStore(const OH_Rdb_Config *config) | 删除数据库。 |
| OH_VBucket_PutAsset(OH_VBucket *bucket, const char *field, Rdb_Asset *value) | 把Rdb_Asset类型的数据放到指定的OH_VBucket对象中。 |
| OH_VBucket_PutAssets(OH_VBucket *bucket, const char *field, Rdb_Asset *value, uint32_t count) | 把Rdb_Asset数组类型的数据放到指定的OH_VBucket对象中。 |
| OH_Rdb_SetDistributedTables(OH_Rdb_Store *store, const char *tables[], uint32_t count, Rdb_DistributedType type, const Rdb_DistributedConfig *config) | 设置分布式数据库表。 |
| OH_Rdb_FindModifyTime(OH_Rdb_Store *store, const char *tableName, const char *columnName, OH_VObject *values) | 获取数据库指定表中指定列的数据的最后修改时间。 |
| OH_Rdb_CloudSync(OH_Rdb_Store *store, Rdb_SyncMode mode, const char *tables[], uint32_t count, const Rdb_ProgressObserver *observer) | 手动执行对指定表的端云同步，使用该接口需要实现云服务功能。 |
| int OH_Data_Asset_SetName(Data_Asset *asset, const char *name) | 为资产类型数据设置名称。 |
| int OH_Data_Asset_SetUri(Data_Asset *asset, const char *uri) | 为资产类型数据设置绝对路径。 |
| int OH_Data_Asset_SetPath(Data_Asset *asset, const char *path) | 为资产类型数据设置应用沙箱里的相对路径。 |
| int OH_Data_Asset_SetCreateTime(Data_Asset *asset, int64_t createTime) | 为资产类型数据设置创建时间。 |
| int OH_Data_Asset_SetModifyTime(Data_Asset *asset, int64_t modifyTime) | 为资产类型数据设置最后修改时间。 |
| int OH_Data_Asset_SetSize(Data_Asset *asset, size_t size) | 为资产类型数据设置占用空间大小。 |
| int OH_Data_Asset_SetStatus(Data_Asset *asset, Data_AssetStatus status) | 为资产类型数据设置状态码。 |
| int OH_Data_Asset_GetName(Data_Asset *asset, char *name, size_t *length) | 获取资产类型数据的名称。 |
| int OH_Data_Asset_GetUri(Data_Asset *asset, char *uri, size_t *length) | 获取资产类型数据的绝对路径。 |
| int OH_Data_Asset_GetPath(Data_Asset *asset, char *path, size_t *length) | 获取资产类型数据在应用沙箱内的相对路径。 |
| int OH_Data_Asset_GetCreateTime(Data_Asset *asset, int64_t *createTime) | 获取资产类型数据的创建时间。 |
| int OH_Data_Asset_GetModifyTime(Data_Asset *asset, int64_t *modifyTime) | 获取资产类型数据的最后修改时间。 |
| int OH_Data_Asset_GetSize(Data_Asset *asset, size_t *size) | 获取资产类型数据的占用空间大小。 |
| int OH_Data_Asset_GetStatus(Data_Asset *asset, Data_AssetStatus *status) | 获取资产类型数据的状态码。 |
| Data_Asset *OH_Data_Asset_CreateOne() | 创造一个资产类型实例。使用完毕后需要调用OH_Data_Asset_DestroyOne释放内存。 |
| int OH_Data_Asset_DestroyOne(Data_Asset *asset) | 销毁一个资产类型实例并回收内存。 |
| Data_Asset **OH_Data_Asset_CreateMultiple(uint32_t count) | 创造指定数量的资产类型实例。使用完毕后需要调用OH_Data_Asset_DestroyMultiple释放内存。 |
| int OH_Data_Asset_DestroyMultiple(Data_Asset **assets, uint32_t count) | 销毁指定数量的资产类型实例并回收内存。 |
| int OH_Rdb_Subscribe(OH_Rdb_Store *store, Rdb_SubscribeType type, const Rdb_DataObserver *observer) | 为数据库注册观察者, 当分布式数据库中的数据发生更改时，将调用回调。 |
| int OH_Rdb_Unsubscribe(OH_Rdb_Store *store, Rdb_SubscribeType type, const Rdb_DataObserver *observer) | 从数据库中删除指定类型的指定观察者。 |
| int OH_Rdb_SubscribeAutoSyncProgress(OH_Rdb_Store *store, const Rdb_ProgressObserver *observer) | 订阅RDB存储的自动同步进程, 当收到自动同步进度的通知时，将调用回调。 |
| int OH_Rdb_UnsubscribeAutoSyncProgress(OH_Rdb_Store *store, const Rdb_ProgressObserver *observer) | 取消订阅RDB存储的自动同步进程。 |
开发步骤
添加动态链接库
CMakeLists.txt中添加以下lib。
头文件
1.  获取OH_Rdb_Store实例，创建数据库文件。其中dataBaseDir变量为应用沙箱路径，Stage模式下建议使用数据库目录，参考Context的databaseDir属性。FA模式下，由于没有接口获取数据库沙箱路径，可使用应用程序的文件目录，可参考Context的getFilesDir接口。area为数据库文件存放的安全区域，详见contextConstant，开发时需要实现由AreaMode枚举值对Rdb_SecurityArea枚举值的转换。示例代码如下所示：
2.  获取到OH_Rdb_Store后，调用OH_Rdb_Execute接口创建表，并调用OH_Rdb_Insert接口插入数据。示例代码如下所示： 关系型数据库没有显式的flush操作实现持久化，数据插入即保存在持久化文件。
3.  根据谓词指定的实例对象，对数据进行修改或删除。 调用OH_Rdb_Update方法修改数据，调用OH_Rdb_Delete方法删除数据。示例代码如下所示：
4.  根据谓词指定的查询条件查找数据。 调用OH_Rdb_Query方法查找数据，返回一个OH_Cursor结果集。示例代码如下所示：
5.  向数据库表中插入资产类型数据。
6.  从结果集中读取资产类型数据。
7.  查询数据的最后修改时间。调用OH_Rdb_FindModifyTime查询指定表中指定列的数据的最后修改时间，该接口返回一个有两列数据的OH_Cursor对象，第一列为传入的主键/RowId，第二列为最后修改时间。示例代码如下所示：
8.  创建分布式表。调用OH_Rdb_Execute接口创建表之后，可以将已创建的表设置成分布式表，并配置相关的分布式选项。使用该接口需要实现云服务功能。示例代码如下所示：
9.  对分布式表手动执行端云同步。调用OH_Rdb_SetDistributedTables创建分布式表之后，可以对该表进行手动端云同步。使用该接口需要实现云服务功能。示例代码如下所示：
10.  将数据观察者注册到指定的存储对象(store)上，并订阅指定类型(type)的事件。在数据发生变化时，系统会调用相应的回调函数来处理进度观察。调用OH_Rdb_Subscribe接口订阅数据变化事件。使用该接口需要实现云服务功能。示例代码如下所示： 调用OH_Rdb_Subscribe接口订阅本地数据库数据变更的事件。示例代码如下所示：
11.  从指定的存储对象(store)中取消对指定类型(type)的事件的订阅。取消后，系统将不再调用相应的回调函数来处理进度观察。调用OH_Rdb_Unsubscribe接口取消订阅数据变化事件。使用该接口需要实现云服务功能。示例代码如下所示： 调用OH_Rdb_Unsubscribe接口取消订阅本地数据库数据变更的事件。示例代码如下所示：
12.  将进度观察者注册到指定的存储对象(store)上，以便订阅自动同步进度的事件。当存储对象进行自动同步时，系统会调用相应的回调函数处理进度观察。调用OH_Rdb_SubscribeAutoSyncProgress接口订阅自动同步进度事件。使用该接口需要实现云服务功能。示例代码如下所示：
13.  从指定的存储对象(store)中取消订阅自动同步进度的事件。取消后，系统将不再调用相应的回调函数来处理进度观察。调用OH_Rdb_UnsubscribeAutoSyncProgress接口取消订阅自动同步进度事件。使用该接口需要实现云服务功能。示例代码如下所示：
14.  删除数据库。调用OH_Rdb_DeleteStore方法，删除数据库及数据库相关文件。示例代码如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ative-unified-data-management-framework-guidelines-V14
爬取时间: 2025-04-27 22:44:54
来源: Huawei Developer
场景介绍
统一数据管理框架（UDMF）：提供了数据跨应用、跨设备交互标准，定义了跨应用、跨设备数据交互过程中的数据语言，提升数据交互效率。提供安全、标准化数据流通通路，支持不同级别的数据访问权限与生命周期管理策略，实现高效的数据跨应用、跨设备共享。
基本概念
-  标准化数据类型：Uniform Type Descriptor，简称UTD。主要针对同一种数据类型，提供统一定义，即标准数据类型描述符，定义了包括标识数据类型的ID、类型归属关系等相关信息，用于解决HarmonyOS系统中的类型模糊问题。一般用于过滤或者识别某一种数据类型的场景，比如文件预览、文件分享等。
-  标准化数据结构：Unified Data Structure，简称UDS。主要针对部分标准化数据类型定义了统一的数据内容结构，并明确了对应的描述信息。应用间使用标准化数据结构进行数据交互后，将遵从统一的解析标准，可有效减少适配相关的工作量。一般用于跨应用跨设备间的数据交互，比如拖拽。
-  统一数据记录： Unified Record，对UDMF支持的数据内容的抽象定义，例如一条文本记录、一条图片记录等。
-  统一数据对象： Unified Data，用于封装一组数据记录Unified Record。
-  统一数据提供者: Unified Data Provider，配置到统一数据记录中，用来提供UDS数据。通常用于数据的延迟发送场景，让UDS数据在数据使用方从统一数据记录中实际获取时才发生数据的转移。
约束限制
接口说明
详细的接口说明请参考UDMF接口文档。
| 接口名称 | 描述 |
| --- | --- |
| OH_Utd* OH_Utd_Create(const char* typeId) | 创建一个指向统一数据类型描述符OH_Utd的指针。 |
| void OH_Utd_Destroy(OH_Utd* pThis) | 销毁指向统一数据类型描述符OH_Utd的指针。 |
| const char** OH_Utd_GetTypesByFilenameExtension(const char* extension, unsigned int* count) | 通过文件后缀名获取标准化数据类型ID。 |
| const char** OH_Utd_GetTypesByMimeType(const char* mimeType, unsigned int* count) | 通过MIME类型获取标准化数据类型ID。 |
| bool OH_Utd_Equals(OH_Utd* utd1, OH_Utd* utd2) | 判断两种标准化数据类型是否相等。 |
| void OH_Utd_DestroyStringList(const char** list, unsigned int count) | 销毁字符串列表数据。 |
| OH_UdsHyperlink* OH_UdsHyperlink_Create() | 创建一个指向标准化数据结构超链接类型OH_UdsHyperlink的指针。 |
| void OH_UdsHyperlink_Destroy(OH_UdsHyperlink* pThis) | 销毁指向标准化数据结构超链接类型OH_UdsHyperlink的指针。 |
| const char* OH_UdsHyperlink_GetType(OH_UdsHyperlink* pThis) | 获取OH_UdsHyperlink中的标准化数据类型ID。 |
| const char* OH_UdsHyperlink_GetUrl(OH_UdsHyperlink* pThis) | 获取OH_UdsHyperlink中的链接URL。 |
| const char* OH_UdsHyperlink_GetDescription(OH_UdsHyperlink* pThis) | 获取OH_UdsHyperlink中的链接内容描述。 |
| int OH_UdsHyperlink_SetUrl(OH_UdsHyperlink* pThis, const char* url) | 设置OH_UdsHyperlink中的链接URL。 |
| int OH_UdsHyperlink_SetDescription(OH_UdsHyperlink* pThis, const char* description) | 设置OH_UdsHyperlink中的链接内容描述。 |
| OH_UdmfData* OH_UdmfData_Create() | 创建一个指向统一数据对象OH_UdmfData的指针。 |
| void OH_UdmfData_Destroy(OH_UdmfData* pThis) | 销毁指向统一数据对象OH_UdmfData的指针。 |
| int OH_UdmfData_AddRecord(OH_UdmfData* pThis, OH_UdmfRecord* record) | 向OH_UdmfData中增加一条OH_UdmfRecord数据记录。 |
| bool OH_UdmfData_HasType(OH_UdmfData* pThis, const char* type) | 判断统一数据对象OH_UdmfData是否存在指定类型。 |
| OH_UdmfRecord** OH_UdmfData_GetRecords(OH_UdmfData* pThis, unsigned int* count) | 获取OH_UdmfData中全部的数据记录。 |
| OH_UdmfRecord* OH_UdmfRecord_Create() | 创建一个指向统一数据记录OH_UdmfRecord的指针。 |
| void OH_UdmfRecord_Destroy(OH_UdmfRecord* pThis) | 销毁指向统一数据记录OH_UdmfRecord的指针。 |
| int OH_UdmfRecord_AddHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink) | 向OH_UdmfRecord添加超链接类型数据。 |
| char** OH_UdmfRecord_GetTypes(OH_UdmfRecord* pThis, unsigned int* count) | 获取OH_UdmfRecord中全部的数据类型。 |
| int OH_UdmfRecord_GetHyperlink(OH_UdmfRecord* pThis, OH_UdsHyperlink* hyperlink) | 获取OH_UdmfRecord中超链接类型数据。 |
| int OH_Udmf_GetUnifiedData(const char* key, Udmf_Intention intention, OH_UdmfData* unifiedData) | 从UDMF数据库中获取数据。 |
| int OH_Udmf_SetUnifiedData(Udmf_Intention intention, OH_UdmfData* unifiedData, char* key, unsigned int keyLen) | 向UDMF数据库中写入数据。 |
| OH_UdmfRecordProvider* OH_UdmfRecordProvider_Create() | 创建一个指向统一数据提供者的指针。 |
| int OH_UdmfRecordProvider_SetData(OH_UdmfRecordProvider* provider, void* context, const OH_UdmfRecordProvider_GetData callback, const UdmfData_Finalize finalize) | 设置统一数据提供者的回调函数。 |
| int OH_UdmfRecord_SetProvider(OH_UdmfRecord* pThis, const char* const* types, unsigned int count, OH_UdmfRecordProvider* provider) | 将统一数据提供者配置到OH_UdmfRecord中。 |
添加动态链接库
CMakeLists.txt中添加以下lib。
引用头文件
通过不同方式获取纯文本类型数据
下面以获取纯文本数据的查询场景为例，说明如何使用UTD。
使用UDMF发送UDS数据
下面以发送超链接hyperlink类型数据场景为例，说明如何使用UDS与UDMF。
使用UDMF接收UDS数据
下面继续以获取超链接hyperlink类型数据场景为例，说明如何使用UDS与UDMF。
使用UDMF延迟发送UDS数据
定义UDS数据提供函数
下面以超链接hyperlink类型数据场景为例，说明如何定义一个提供UDS数据的回调函数。
延迟发送UDS数据
下面以延迟发送超链接hyperlink类型数据场景为例，说明如何使用OH_UdmfRecordProvider与UDMF。需要注意，此步骤完成后超链接类型数据并未真正写入数据库，只有当数据使用者从OH_UdmfRecord中获取OH_UdsHyperlink时，才会触发上文定义的GetDataCallback数据提供函数，从中得到数据。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/preferences-guidelines-V14
爬取时间: 2025-04-27 22:45:08
来源: Huawei Developer
场景介绍
用户首选项（Preferences）模块主要提供轻量级Key-Value操作，支持本地应用存储少量数据，数据存储在本地文件中，同时也加载在内存中，所以访问速度更快，效率更高。首选项提供非关系型数据存储，不宜存储大量数据，经常用于操作键值对形式数据的场景。
约束限制
接口说明
详细的接口说明请参考Preferences接口文档。
| 接口名称 | 描述 |
| --- | --- |
| OH_Preferences * OH_Preferences_Open (OH_PreferencesOption *option, int *errCode) | 打开一个Preferences实例对象并创建指向它的指针。 当不再需要使用指针时，请使用OH_Preferences_Close关闭实例对象。 |
| int OH_Preferences_Close (OH_Preferences *preference) | 关闭一个Preferences实例对象。 |
| int OH_Preferences_GetInt (OH_Preferences *preference, const char *key, int *value) | 获取Preferences实例对象中Key对应的整型值。 |
| int OH_Preferences_GetBool (OH_Preferences *preference, const char *key, bool *value) | 获取Preferences实例对象中Key对应的布尔值。 |
| int OH_Preferences_GetString (OH_Preferences *preference, const char *key, char **value, uint32_t *valueLen) | 获取Preferences实例对象中Key对应的字符串。 |
| void OH_Preferences_FreeString (char *string) | 释放从Preferences实例对象中获取的字符串。 |
| int OH_Preferences_SetInt (OH_Preferences *preference, const char *key, int value) | 根据Key设置Preferences实例对象中的整型值。 |
| int OH_Preferences_SetBool (OH_Preferences *preference, const char *key, bool value) | 根据Key设置Preferences实例对象中的布尔值。 |
| int OH_Preferences_SetString (OH_Preferences *preference, const char *key, const char *value) | 根据Key设置Preferences实例对象中的字符串。 |
| int OH_Preferences_Delete (OH_Preferences *preference, const char *key) | 在Preferences实例对象中删除Key对应的KV数据。 |
| int OH_Preferences_RegisterDataObserver (OH_Preferences *preference, void *context, OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount) | 对选取的Key注册数据变更订阅。订阅的Key的值发生变更后，在调用OH_Preferences_Close()后触发回调。 |
| int OH_Preferences_UnregisterDataObserver (OH_Preferences *preference, void *context, OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount) | 取消注册选取Key的数据变更订阅。 |
| OH_PreferencesOption * OH_PreferencesOption_Create (void) | 创建一个Preferences配置选项的OH_PreferencesOption实例对象以及指向它的指针。 当不再需要使用指针时，请使用OH_PreferencesOption_Destroy销毁实例对象，否则会导致内存泄漏。 |
| int OH_PreferencesOption_SetFileName (OH_PreferencesOption *option, const char *fileName) | 设置Preferences配置选项OH_PreferencesOption实例对象的文件名称。名称长度需大于零且小于等于255字节，名称中不能包含'/'且不能以'/'结尾。 |
| int OH_PreferencesOption_SetBundleName (OH_PreferencesOption *option, const char *bundleName) | 设置Preferences配置选项OH_PreferencesOption实例对象的包名称。 |
| int OH_PreferencesOption_SetDataGroupId (OH_PreferencesOption *option, const char *dataGroupId) | 设置Preferences配置选项OH_PreferencesOption实例对象的应用组ID。 |
| int OH_PreferencesOption_Destroy (OH_PreferencesOption *option) | 销毁Preferences配置选项OH_PreferencesOption实例。 |
| const char * OH_PreferencesPair_GetKey (const OH_PreferencesPair *pairs, uint32_t index) | 获取KV数据中索引对应数据的键。 |
| const OH_PreferencesValue * OH_PreferencesPair_GetPreferencesValue (const OH_PreferencesPair *pairs, uint32_t index) | 获取KV数据数组中索引对应的值。 |
| Preference_ValueType OH_PreferencesValue_GetValueType (const OH_PreferencesValue *object) | 获取PreferencesValue对象的数据类型。 |
| int OH_PreferencesValue_GetInt (const OH_PreferencesValue *object, int *value) | 从PreferencesValue对象OH_PreferencesValue中获取一个整型值。 |
| int OH_PreferencesValue_GetBool (const OH_PreferencesValue *object, bool *value) | 从PreferencesValue对象OH_PreferencesValue中获取一个布尔值。 |
| int OH_PreferencesValue_GetString (const OH_PreferencesValue *object, char **value, uint32_t *valueLen) | 从PreferencesValue对象OH_PreferencesValue中获取字符串。 |
添加动态链接库
CMakeLists.txt中添加以下lib。
引用头文件
开发步骤
下列实例展示如何通过Preferences实现对KV数据的修改与持久化。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-V14
爬取时间: 2025-04-27 22:45:21
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-overview-V14
爬取时间: 2025-04-27 22:45:34
来源: Huawei Developer
ArkTS是HarmonyOS应用开发的官方高级语言。
ArkTS提供了声明式UI范式、状态管理、渲染控制等相应的能力，让开发者能够以更简洁、更自然的方式开发应用。
ArkTS在TypeScript（简称TS）生态基础上做了进一步扩展，保持了TS的基本风格，同时通过规范定义强化开发期静态检查和分析，提升代码健壮性，并实现更好的程序执行稳定性和性能。对比标准TS的差异可以参考从TypeScript到ArkTS的适配规则。ArkTS同时也支持与TS/JavaScript（简称JS）高效互操作。
ArkTS基础类库和容器类库增强了语言的基础功能，提供包括高精度浮点运算、二进制Buffer、XML生成解析转换和多种容器库等能力，协助开发者简化开发工作，提升开发效率。
针对TS/JS并发能力支持有限的问题，ArkTS对并发编程API和能力进行了增强，提供了TaskPool和Worker两种并发API供开发者选择。另外，ArkTS进一步提出了Sendable的概念来支持对象在并发实例间的引用传递，提升ArkTS对象在并发实例间的通信性能。
方舟编译运行时（ArkCompiler）支持ArkTS、TS、JS的编译运行，目前它主要分为ArkTS编译工具链和ArkTS运行时两部分。其中ArkTS编译工具链负责在开发侧将高级语言编译为方舟字节码文件（*.abc），而ArkTS运行时则负责在设备侧运行字节码文件执行程序逻辑。
未来，ArkTS会结合应用开发/运行的需求持续演进，逐步提供并发能力增强、系统类型增强、分布式开发范式等更多特性。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-utils-V14
爬取时间: 2025-04-27 22:45:48
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-utils-overview-V14
爬取时间: 2025-04-27 22:46:02
来源: Huawei Developer
ArkTS基础类库是一个功能齐全的API集合，精心设计了一系列关键且实用的功能模块。
ArkTS基础类库主要提供了XML生成解析转换、二进制Buffer、多种容器类库、URL字符串解析和高精度浮点计算等能力，协助开发者简化开发工作，提升开发效率。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/xml-generation-parsing-conversion-V14
爬取时间: 2025-04-27 22:46:15
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/xml-overview-V14
爬取时间: 2025-04-27 22:46:29
来源: Huawei Developer
XML（可扩展标记语言）是一种用于描述数据的标记语言，旨在提供一种通用的方式来传输和存储数据，特别是Web应用程序中经常使用的数据。XML并不预定义标记。因此，XML更加灵活，并且可以适用于广泛的应用领域。
XML文档由元素（element）、属性（attribute）和内容（content）组成。
-  元素指的是标记对，包含文本、属性或其他元素。
-  属性提供了有关元素的其他信息。
-  内容则是元素包含的数据或子元素。
XML还可以通过使用XML Schema或DTD（文档类型定义）来定义文档结构。这些机制允许开发人员创建自定义规则以验证XML文档是否符合其预期的格式。
XML还支持命名空间、实体引用、注释、处理指令等特性，使其能够灵活地适应各种数据需求。
语言基础类库提供了XML相关的基础能力，包括：XML的生成、XML的解析和XML的转换。
以下是一个简单的XML样例及对应说明，更多XML的接口和具体使用，请见@ohos.xml。
```xml
<?xml version="1.0" encoding="utf-8"?> <!-- 声明 -->
<!-- 处理指令 -->
<?xml-stylesheet type="text/css" href="style.css"?>
<!-- 元素、属性及属性值 -->
<note importance="high">
<title>Happy</title>
<!-- 实体引用 -->
<todo>&amp;</todo>
<!-- 命名空间的声明及统一资源标识符 -->
<h:table xmlns:h="http://www.w3.org/TR/html4/">
<h:tr>
<h:td>Apples</h:td>
<h:td>Bananas</h:td>
</h:tr>
</h:table>
</note>
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/xml-generation-V14
爬取时间: 2025-04-27 22:46:42
来源: Huawei Developer
XML可以作为数据交换格式，被各种系统和应用程序所支持。例如Web服务，可以将结构化数据以XML格式进行传递。
XML还可以作为消息传递格式，在分布式系统中用于不同节点之间的通信与交互。
注意事项
-  XML标签必须成对出现，生成开始标签就要生成结束标签。
-  XML标签对大小写敏感，开始标签与结束标签大小写要一致。
开发步骤
XML模块提供XmlSerializer类来生成XML数据，输入为固定长度的Arraybuffer或DataView对象，该对象用于存放生成的XML数据。
通过调用不同的方法来写入不同的内容，如startElement(name: string)写入元素开始标记，setText(text: string)写入标签值。
XML模块的API接口可以参考@ohos.xml的详细描述，按需求调用对应函数可以生成一份完整的XML数据。
1.  引入模块。
```typescript
import { xml, util } from '@kit.ArkTS';
```
2.  创建缓冲区，构造XmlSerializer对象。可以基于Arraybuffer构造XmlSerializer对象，也可以基于DataView构造XmlSerializer对象。
```typescript
// 方式1：基于Arraybuffer构造XmlSerializer对象
let arrayBuffer: ArrayBuffer = new ArrayBuffer(2048); // 创建一个2048字节的缓冲区
let serializer: xml.XmlSerializer = new xml.XmlSerializer(arrayBuffer); // 基于Arraybuffer构造XmlSerializer对象
// 方式2：基于DataView构造XmlSerializer对象
// let arrayBuffer: ArrayBuffer = new ArrayBuffer(2048);
// let dataView: DataView = new DataView(arrayBuffer);
// let serializer: xml.XmlSerializer = new xml.XmlSerializer(dataView);
```
3.  调用XML元素生成函数。
```typescript
serializer.setDeclaration(); // 写入xml的声明
serializer.startElement('bookstore'); // 写入元素开始标记
serializer.startElement('book'); // 嵌套元素开始标记
serializer.setAttributes('category', 'COOKING'); // 写入属性及属性值
serializer.startElement('title');
serializer.setAttributes('lang', 'en');
serializer.setText('Everyday'); // 写入标签值
serializer.endElement(); // 写入结束标记
serializer.startElement('author');
serializer.setText('Giana');
serializer.endElement();
serializer.startElement('year');
serializer.setText('2005');
serializer.endElement();
serializer.endElement();
serializer.endElement();
```
4.  使用Uint8Array操作Arraybuffer，调用TextDecoder对Uint8Array解码后输出。 输出结果如下：
```typescript
let uint8Array: Uint8Array = new Uint8Array(arrayBuffer); // 使用Uint8Array读取arrayBuffer的数据
let textDecoder: util.TextDecoder = util.TextDecoder.create(); // 调用util模块的TextDecoder类
let result: string = textDecoder.decodeToString(uint8Array); // 对uint8Array解码
console.info(result);
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/xml-parsing-V14
爬取时间: 2025-04-27 22:46:56
来源: Huawei Developer
对于以XML作为载体传递的数据，实际使用中需要对相关的节点进行解析，一般包括解析XML标签和标签值、解析XML属性和属性值、解析XML事件类型和元素深度三类操作。如在Web服务中，XML是SOAP（Simple Object Access Protocol）协议的基础，SOAP消息通常以XML格式封装，包含请求和响应参数，通过解析这些XML消息，Web服务可以处理来自客户端的请求并生成相应的响应。
XML模块提供XmlPullParser类对XML文件解析，输入为含有XML文本的ArrayBuffer或DataView，输出为解析得到的信息。
表1XML解析选项，其详细介绍请参见ParseOptions。
| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supportDoctype | boolean | 否 | 是否忽略文档类型。默认为false，表示不解析文档类型。 |
| ignoreNameSpace | boolean | 否 | 是否忽略命名空间。默认为false，表示对命名空间进行解析。 |
| tagValueCallbackFunction | (name: string, value: string) => boolean | 否 | 获取tagValue回调函数，打印标签及标签值。默认为null，表示不进行XML标签和标签值的解析。 |
| attributeValueCallbackFunction | (name: string, value: string) => boolean | 否 | 获取attributeValue回调函数， 打印属性及属性值。默认为null，表示不进行XML属性和属性值的解析。 |
| tokenValueCallbackFunction | (eventType: EventType, value: ParseInfo) => boolean | 否 | 获取tokenValue回调函数，打印标签事件类型及parseInfo对应属性。默认为null，表示不进行XML事件类型解析。 |
注意事项
-  XML解析及转换需要确保传入的XML数据符合标准格式。
-  XML解析目前不支持按指定节点解析对应的节点值。
解析XML标签和标签值
1.  引入模块。
```typescript
import { xml, util } from '@kit.ArkTS'; // 需要使用util模块函数对文件编码
```
2.  对XML文件编码后调用XmlPullParser。 可以基于ArrayBuffer构造XmlPullParser对象， 也可以基于DataView构造XmlPullParser对象（两种构造方式返回结果无区别可任选一种）。
```typescript
let strXml: string =
'<?xml version="1.0" encoding="utf-8"?>' +
'<note importance="high" logged="true">' +
'<title>Play</title>' +
'<lens>Work</lens>' +
'</note>';
let textEncoder: util.TextEncoder = new util.TextEncoder();
let arrBuffer: Uint8Array = textEncoder.encodeInto(strXml); // 对数据编码，防止包含中文字符乱码
// 方式1：基于ArrayBuffer构造XmlPullParser对象
let that: xml.XmlPullParser = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
// 方式2：基于DataView构造XmlPullParser对象
// let dataView: DataView = new DataView(arrBuffer.buffer as object as ArrayBuffer);
// let that: xml.XmlPullParser = new xml.XmlPullParser(dataView, 'UTF-8');
```
3.  自定义回调函数，本例直接打印出标签及标签值。
```typescript
function func(name: string, value: string): boolean {
if (name == 'note') {
console.info(name);
}
if (value == 'Play' || value == 'Work') {
console.info('    ' + value);
}
if (name == 'title' || name == 'lens') {
console.info('  ' + name);
}
return true; //true:继续解析 false:停止解析
}
```
4.  设置解析选项，调用parse函数。 输出结果如下所示：
```typescript
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tagValueCallbackFunction:func};
that.parse(options);
```
解析XML属性和属性值
1.  引入模块。
```typescript
import { xml, util } from '@kit.ArkTS'; // 需要使用util模块函数对文件编码
```
2.  对XML文件编码后调用XmlPullParser。
```typescript
let strXml: string =
'<?xml version="1.0" encoding="utf-8"?>' +
'<note importance="high" logged="true">' +
'    <title>Play</title>' +
'    <title>Happy</title>' +
'    <lens>Work</lens>' +
'</note>';
let textEncoder: util.TextEncoder = new util.TextEncoder();
let arrBuffer: Uint8Array = textEncoder.encodeInto(strXml); // 对数据编码，防止包含中文字符乱码
let that: xml.XmlPullParser = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
```
3.  自定义回调函数，本例直接打印出属性及属性值。
```typescript
let str: string = '';
function func(name: string, value: string): boolean {
str += name + ' ' + value + ' ';
return true; // true:继续解析 false:停止解析
}
```
4.  设置解析选项，调用parse函数。 输出结果如下所示：
```typescript
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, attributeValueCallbackFunction:func};
that.parse(options);
console.info(str); // 一次打印出所有的属性及其值
```
解析XML事件类型和元素深度
1.  引入模块。
```typescript
import { xml, util } from '@kit.ArkTS'; // 需要使用util模块函数对文件编码
```
2.  对XML文件编码后调用XmlPullParser。
```typescript
let strXml: string =
'<?xml version="1.0" encoding="utf-8"?>' +
'<note importance="high" logged="true">' +
'<title>Play</title>' +
'</note>';
let textEncoder: util.TextEncoder = new util.TextEncoder();
let arrBuffer: Uint8Array = textEncoder.encodeInto(strXml); // 对数据编码，防止包含中文字符乱码
let that: xml.XmlPullParser = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
```
3.  自定义回调函数，本例直接打印元素事件类型及元素深度。
```typescript
let str: string  = '';
function func(name: xml.EventType, value: xml.ParseInfo): boolean {
str = name + ' ' + value.getDepth(); // getDepth 获取元素的当前深度
console.info(str)
return true; //true:继续解析 false:停止解析
}
```
4.  设置解析选项，调用parse函数。 输出结果如下所示：
```typescript
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func};
that.parse(options);
```
场景示例
此处以调用所有解析选项为例，提供解析XML标签、属性和事件类型的开发示例。
```typescript
import { xml, util } from '@kit.ArkTS';
let strXml: string =
'<?xml version="1.0" encoding="UTF-8"?>' +
'<book category="COOKING">' +
'<title lang="en">Everyday</title>' +
'<author>Giana</author>' +
'</book>';
let textEncoder: util.TextEncoder = new util.TextEncoder();
let arrBuffer: Uint8Array = textEncoder.encodeInto(strXml);
let that: xml.XmlPullParser = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
let str: string = '';
function tagFunc(name: string, value: string): boolean {
str = name + value;
console.info('tag-' + str);
return true;
}
function attFunc(name: string, value: string): boolean {
str = name + ' ' + value;
console.info('attri-' + str);
return true;
}
function tokenFunc(name: xml.EventType, value: xml.ParseInfo): boolean {
str = name + ' ' + value.getDepth();
console.info('token-' + str);
return true;
}
let options: xml.ParseOptions = {
supportDoctype: true,
ignoreNameSpace: true,
tagValueCallbackFunction: tagFunc,
attributeValueCallbackFunction: attFunc,
tokenValueCallbackFunction: tokenFunc
};
that.parse(options);
```
输出结果如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/xml-conversion-V14
爬取时间: 2025-04-27 22:47:10
来源: Huawei Developer
将XML文本转换为JavaScript对象可以更轻松地处理和操作数据，并且更适合在JavaScript应用程序中使用。
语言基础类库提供ConvertXML类将XML文本转换为JavaScript对象，输入为待转换的XML字符串及转换选项，输出为转换后的JavaScript对象。具体转换选项可见API参考@ohos.convertxml。
注意事项
XML解析及转换需要确保传入的XML数据符合标准格式。
开发步骤
此处以XML转为JavaScript对象后获取其标签值为例，说明转换效果。
1.  引入模块。
```typescript
import { convertxml } from '@kit.ArkTS';
```
2.  输入待转换的XML，设置转换选项，支持的转换选项及含义具体可见ConvertOptions。 传入的XML文本中，若包含“&”字符，请使用实体引用“&amp;”替换。
```typescript
let xml: string =
'<?xml version="1.0" encoding="utf-8"?>' +
'<note importance="high" logged="true">' +
'    <title>Happy</title>' +
'    <todo>Work</todo>' +
'    <todo>Play</todo>' +
'</note>';
let options: convertxml.ConvertOptions = {
// trim: false 转换后是否删除文本前后的空格，否
// declarationKey: "_declaration" 转换后文件声明使用_declaration来标识
// instructionKey: "_instruction" 转换后指令使用_instruction标识
// attributesKey: "_attributes" 转换后属性使用_attributes标识
// textKey: "_text" 转换后标签值使用_text标识
// cdataKey: "_cdata" 转换后未解析数据使用_cdata标识
// docTypeKey: "_doctype" 转换后文档类型使用_doctype标识
// commentKey: "_comment" 转换后注释使用_comment标识
// parentKey: "_parent" 转换后父类使用_parent标识
// typeKey: "_type" 转换后元素类型使用_type标识
// nameKey: "_name" 转换后标签名称使用_name标识
// elementsKey: "_elements" 转换后元素使用_elements标识
trim: false,
declarationKey: "_declaration",
instructionKey: "_instruction",
attributesKey: "_attributes",
textKey: "_text",
cdataKey: "_cdata",
doctypeKey: "_doctype",
commentKey: "_comment",
parentKey: "_parent",
typeKey: "_type",
nameKey: "_name",
elementsKey: "_elements"
}
```
3.  调用转换函数，打印结果。 输出结果如下所示：
```typescript
let conv: convertxml.ConvertXML = new convertxml.ConvertXML();
let result: object = conv.convertToJSObject(xml, options);
let strRes: string = JSON.stringify(result); // 将js对象转换为json字符串，用于显式输出
console.info(strRes);
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/buffer-V14
爬取时间: 2025-04-27 22:47:24
来源: Huawei Developer
Buffer模块基于内存管理机制，将内存区域抽象为可以读写、修改的逻辑对象，旨在提供二进制数据处理的高效接口。每个Buffer实例对象都是连续的字节序列，支持创建自定义大小的内存块，这样方便存储和操作各种不同类型的数据。
Buffer模块的核心功能包括：
1.  创建和分配内存：允许开发者基于uint32限制的指定大小初始化Buffer，创建后拥有固定的内存容量。
2.  读写和复制数据：通过索引访问Buffer内的字节，支持按字节块读取和写入，支持复制Buffer的某一部分到另一个Buffer或数组。
3.  转换操作：提供了将Buffer与基本类型（如Uint8Array、string等）之间互相转换的方法，适应不同数据处理需求。
4.  内存操作：能够截取部分Buffer、切片以及合并多个Buffer，便于处理和管理数据流。
Buffer模块的主要应用场景包括：
1.  大数据传输：当需要传输大量数据时，如二进制文件、数据库记录或网络报文，Buffer作为数据的存储和处理容器，能减少拷贝和内存消耗，提升传输效率。
2.  图像和音频处理：在图像编码、解码，音频数据流处理等方面，Buffer可帮助开发者方便地操作像素或采样数据，确保数据的完整性。
3.  二进制数据操作：Buffer提供稳定的接口解析和操作二进制数据。
Buffer模块各接口使用详见：@ohos.buffer。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/containers-V14
爬取时间: 2025-04-27 22:47:37
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/container-overview-V14
爬取时间: 2025-04-27 22:47:51
来源: Huawei Developer
容器类库，用于存储各种数据类型的元素，并具备一系列处理数据元素的方法，作为纯数据结构容器来使用具有一定的优势。
容器类采用了类似静态语言的方式来实现，并通过对存储位置以及属性的限制，让每种类型的数据都能在完成自身功能的基础上去除冗余逻辑，保证了数据的高效访问，提升了应用的性能。
当前提供了线性和非线性两类容器。线性类容器底层通过数组实现，非线性类容器底层通过hash或者红黑树实现。线性容器和非线性容器都是非多线程安全的。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/linear-container-V14
爬取时间: 2025-04-27 22:48:04
来源: Huawei Developer
线性容器实现能按顺序访问的数据结构，其底层主要通过数组实现，包括ArrayList、Vector、List、LinkedList、Deque、Queue、Stack七种。
线性容器，充分考虑了数据访问的速度，运行时（Runtime）通过一条字节码指令就可以完成增、删、改、查等操作。
各线性容器类型特征对比
| 类名 | 特征及建议使用场景 |
| --- | --- |
| ArrayList | 动态数组，占用一片连续的内存空间。需要频繁读取元素时推荐使用。 |
| List | 单向链表，占用的空间可以不连续。需要频繁的插入删除元素且需要使用单向链表时推荐使用。 |
| LinkedList | 双向链表，占用的空间可以不连续。需要频繁的插入删除元素且需要使用双向链表时推荐使用。 |
| Deque | 双端队列，可以从容器头尾进行进出元素操作，占用一片连续的内存空间。需要频繁访问、操作头尾元素时推荐使用。 |
| Queue | 队列，从容器尾部插入元素，从容器头部弹出元素，占用一片连续的内存空间。一般符合先进先出的场景可以使用。 |
| Stack | 栈，只能从容器的一端进行插入删除操作，占用一片连续的内存空间。一般符合先进后出的场景可以使用。 |
| Vector | 动态数组，占用一片连续的内存空间。该类型已不再维护，推荐使用ArrayList。 |
ArrayList
ArrayList即动态数组，可用来构造全局的数组对象。 当需要频繁读取集合中的元素时，推荐使用ArrayList。
ArrayList依据泛型定义，要求存储位置是一片连续的内存空间，初始容量大小为10，并支持动态扩容，每次扩容大小为原始容量的1.5倍。
ArrayList进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(element: T) | 在数组尾部增加一个元素。 |
| 增加元素 | insert(element: T, index: number) | 在指定位置插入一个元素。 |
| 访问元素 | arr[index: number] | 获取指定index对应的value值，通过指令获取保证访问速度。 |
| 访问元素 | forEach(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => void, thisArg?: Object) | 访问整个ArrayList容器的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | arr[index] = xxx | 修改指定index位置对应的value值。 |
| 删除元素 | remove(element: T) | 删除第一个匹配到的元素。 |
| 删除元素 | removeByRange(fromIndex: number, toIndex:number) | 删除指定范围内的元素。 |
List
List可用来构造一个单向链表对象，即只能通过头结点开始访问到尾节点。List依据泛型定义，在内存中的存储位置可以是不连续的。
List和LinkedList相比，LinkedList是双向链表，可以快速地在头尾进行增删，而List是单向链表，无法双向操作。
当需要频繁的插入删除元素，并且需要使用单向链表时，推荐使用List高效操作。
可以通过get/set等接口对存储的元素进行修改，List进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(element: T) | 在数组尾部增加一个元素。 |
| 增加元素 | insert(element: T, index: number) | 在指定位置插入一个元素。 |
| 访问元素 | get(index: number) | 获取指定index位置对应的元素。 |
| 访问元素 | list[index: number] | 获取指定index位置对应的元素，但会导致未定义结果。 |
| 访问元素 | getFirst() | 获取第一个元素。 |
| 访问元素 | getLast() | 获取最后一个元素。 |
| 访问元素 | getIndexOf(element: T) | 获取第一个匹配指定元素的位置。 |
| 访问元素 | getLastIndexOf(element: T) | 获取最后一个匹配指定元素的位置。 |
| 访问元素 | forEach(callbackfn: (value:T, index?: number, list?: List<T>)=> void,thisArg?: Object) | 遍历访问整个List容器的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | set(index:number, element: T) | 修改指定index位置的元素值为element。 |
| 修改元素 | list[index] = element | 修改指定index位置的元素值为element，但会导致未定义结果。 |
| 修改元素 | replaceAllElements(callbackFn:(value: T,index?: number,list?: List<T>)=>T,thisArg?: Object) | 对List内元素进行逐个替换。 |
| 删除元素 | remove(element: T) | 删除第一个匹配到的元素。 |
| 删除元素 | removeByIndex(index:number) | 删除index位置对应的元素。 |
LinkedList
LinkedList可用来构造一个双向链表对象，可以在某一节点向前或者向后遍历List。LinkedList依据泛型定义，在内存中的存储位置可以是不连续的。
LinkedList和List相比，LinkedList是双向链表，可以快速地在头尾进行增删，而List是单向链表，无法双向操作。
LinkedList和ArrayList相比，插入数据效率LinkedList优于ArrayList，而查询效率ArrayList优于LinkedList。
当需要频繁的插入删除元素，并且需要使用双向链表时，推荐使用LinkedList高效操作。
可以通过get/set等接口对存储的元素进行修改，LinkedList进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(element: T) | 在数组尾部增加一个元素。 |
| 增加元素 | insert(element: T, index: number) | 在指定位置插入一个元素。 |
| 访问元素 | get(index: number) | 获取指定index位置对应的元素。 |
| 访问元素 | list[index: number] | 获取指定index位置对应的元素，但会导致未定义结果。 |
| 访问元素 | getFirst() | 获取第一个元素。 |
| 访问元素 | getLast() | 获取最后一个元素。 |
| 访问元素 | getIndexOf(element: T) | 获取第一个匹配指定元素的位置。 |
| 访问元素 | getLastIndexOf(element: T) | 获取最后一个匹配指定元素的位置。 |
| 访问元素 | forEach(callbackFn: (value: T, index?: number, list?: LinkedList<T>) => void, thisArg?: Object) | 遍历访问整个LinkedList容器的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | set(index:number, element: T) | 修改指定index位置的元素值为element。 |
| 修改元素 | list[index] = element | 修改指定index位置的元素值为element，但会导致未定义结果。 |
| 删除元素 | remove(element: T) | 删除第一个匹配到的元素。 |
| 删除元素 | removeByIndex(index:number) | 删除index位置对应的元素。 |
Deque
Deque可用来构造双端队列对象，存储元素遵循先进先出以及先进后出的规则，双端队列可以分别从队头或者队尾进行访问。
Deque依据泛型定义，要求存储位置是一片连续的内存空间，其初始容量大小为8，并支持动态扩容，每次扩容大小为原始容量的2倍。Deque底层采用循环队列实现，入队及出队操作效率都比较高。
Deque和Queue相比，Deque允许在两端执行增删元素的操作，Queue只能在头部删除元素，尾部增加元素。
Deque和Vector相比，它们都支持在两端增删元素，但Deque不能进行中间插入的操作。对头部元素的插入删除效率高于Vector，而Vector访问元素的效率高于Deque。
需要频繁在集合两端进行增删元素的操作时，推荐使用Deque。
Deque进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | insertFront(element: T) | 在头部增加一个元素。 |
| 增加元素 | insertEnd(element: T) | 在尾部增加一个元素。 |
| 访问元素 | getFirst() | 获取第一个元素，不进行出队操作。 |
| 访问元素 | getLast() | 获取最后一个元素，不进行出队操作。 |
| 访问元素 | popFirst() | 获取第一个元素，并进行出队操作。 |
| 访问元素 | popLast() | 获取最后一个元素，并进行出队操作。 |
| 访问元素 | forEach(callbackFn:(value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object) | 遍历访问整个Deque容器的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | forEach(callbackFn:(value: T, index?: number, deque?: Deque<T>)=> void, thisArg?: Object) | 通过遍历修改整个Deque容器的元素。 |
| 删除元素 | popFirst() | 对队首元素进行出队操作并删除。 |
| 删除元素 | popLast() | 对队尾元素进行出队操作并删除。 |
Queue
Queue可用来构造队列对象，存储元素遵循先进先出的规则。
Queue依据泛型定义，要求存储位置是一片连续的内存空间，初始容量大小为8，并支持动态扩容，每次扩容大小为原始容量的2倍。
Queue底层采用循环队列实现，入队及出队操作效率都比较高。
Queue和Deque相比，Queue只能在一端删除一端增加，Deque可以两端增删。
一般符合先进先出的场景可以使用Queue。
Queue进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(element: T) | 在尾部增加一个元素。 |
| 访问元素 | getFirst() | 获取队首元素，不进行出队操作。 |
| 访问元素 | pop() | 获取队首元素，并进行出队操作。 |
| 访问元素 | forEach(callbackFn: (value: T, index?: number, queue?: Queue<T>) => void,thisArg?: Object) | 遍历访问整个Queue容器的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | forEach(callbackFn: (value: T, index?: number, queue?: Queue<T>) => void,thisArg?: Object) | 通过遍历修改整个Queue容器的元素。 |
| 删除元素 | pop() | 对队首元素进行出队操作并删除。 |
Stack
Stack可用来构造栈对象，存储元素遵循先进后出的规则。
Stack依据泛型定义，要求存储位置是一片连续的内存空间，初始容量大小为8，并支持动态扩容，每次扩容大小为原始容量的1.5倍。Stack底层基于数组实现，入栈出栈均从数组的一端操作。
Stack和Queue相比，Queue基于循环队列实现，只能在一端删除，另一端插入，而Stack都在一端操作。
一般符合先进后出的场景可以使用Stack。
Stack进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | push(item: T) | 在栈顶增加一个元素。 |
| 访问元素 | peek() | 获取栈顶元素，不进行出队操作。 |
| 访问元素 | pop() | 获取栈顶元素，并进行出队操作。 |
| 访问元素 | locate(element: T) | 获取元素对应的位置。 |
| 访问元素 | forEach(callbackFn: (value: T, index?: number, stack?: Stack<T>) => void, thisArg?: Object) | 遍历访问整个Stack容器的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | forEach(callbackFn: (value: T, index?: number, stack?: Stack<T>) => void, thisArg?: Object) | 通过遍历修改整个Stack容器的元素。 |
| 删除元素 | pop() | 对栈顶元素进行出队操作并删除。 |
Vector
API version 9开始，该接口不再维护，推荐使用ArrayList。
Vector是指连续存储结构，可用来构造全局的数组对象。Vector依据泛型定义，要求存储位置是一片连续的内存空间，初始容量大小为10，并支持动态扩容，每次扩容大小为原始容量的2倍。
Vector和ArrayList相似，都是基于数组实现，但Vector提供了更多操作数组的接口。Vector在支持操作符访问的基础上，还增加了get/set接口，提供更为完善的校验及容错机制，满足用户不同场景下的需求。
Vector进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(element: T) | 在数组尾部增加一个元素。 |
| 增加元素 | insert(element: T, index: number) | 在指定位置插入一个元素。 |
| 访问元素 | get(index: number) | 获取指定index位置对应的元素。 |
| 访问元素 | vec[index: number] | 获取指定index位置对应的元素，通过指令获取保证访问速度。 |
| 访问元素 | getFirst() | 获取第一个元素。 |
| 访问元素 | getLastElement() | 获取最后一个元素。 |
| 访问元素 | getIndexOf(element: T) | 获取第一个匹配指定元素的位置。 |
| 访问元素 | getLastIndexOf(element: T) | 获取最后一个匹配指定元素的位置。 |
| 访问元素 | forEach(callbackFn: (value: T, index?: number, Vector?: Vector<T>) => void, thisArg?: Object) | 遍历访问整个Vector容器的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | set(index:number, element: T) | 修改指定index位置的元素值为element。 |
| 修改元素 | vec[index] = element | 修改指定index位置的元素值为element。 |
| 修改元素 | replaceAllElements(callbackFn:(value: T,index?: number,list?: List<T>)=>T,thisArg?: Object) | 对Vector内元素进行逐个替换。 |
| 修改元素 | setLength(newSize:number) | 设置Vector的长度大小。 |
| 删除元素 | remove(element: T) | 删除第一个匹配到的元素。 |
| 删除元素 | removeByIndex(index:number) | 删除index位置对应的元素。 |
| 删除元素 | removeByRange(fromIndex:number,toIndex:number) | 删除指定范围内的元素。 |
线性容器的使用
此处列举常用的线性容器ArrayList、Deque、Stack、List的使用示例，包括导入模块、增加元素、访问元素及修改等操作。示例代码如下所示：
```typescript
// ArrayList
import { ArrayList } from '@kit.ArkTS'; // 导入ArrayList模块
let arrayList1: ArrayList<string> = new ArrayList();
arrayList1.add('a'); // 增加一个值为'a'的元素
let arrayList2: ArrayList<number> = new ArrayList();
arrayList2.add(1); // 增加一个值为1的元素
console.info(`result: ${arrayList2[0]}`); // 访问索引为0的元素。输出：result: 1
arrayList1[0] = 'one'; // 修改索引为0的元素
console.info(`result: ${arrayList1[0]}`); // 输出：result: one
// Deque
import { Deque } from '@kit.ArkTS'; // 导入Deque模块
let deque1: Deque<string> = new Deque();
deque1.insertFront('a'); // 头部增加一个值为'a'的元素
let deque2: Deque<number> = new Deque();
deque2.insertFront(1); // 头部增加一个值为1的元素
console.info(`result: ${deque2.getFirst()}`); // 访问队列首部的元素。输出：result: 1
deque1.insertEnd('one'); // 尾部增加一个值为'one'的元素
console.info(`result: ${deque1.getLast()}`); // 访问队列尾部的元素。输出：result: one
// Stack
import { Stack } from '@kit.ArkTS'; // 导入Stack模块
let stack1: Stack<string> = new Stack();
stack1.push('a'); // 向栈里增加一个值为'a'的元素
let stack2: Stack<number> = new Stack();
stack2.push(1); // 向栈里增加一个值为1的元素
console.info(`result: ${stack1.peek()}`); // 访问栈顶元素。输出：result: a
console.info(`result: ${stack2.pop()}`); // 删除栈顶元素并返回该删除元素。输出：result: 1
console.info(`result: ${stack2.length}`); // 输出：result: 0
// List
import { List } from '@kit.ArkTS'; // 导入List模块
let list1: List<string> = new List();
list1.add('a'); // 增加一个值为'a'的元素
let list2: List<number> = new List();
list2.insert(0, 0); // 在0号位置插入（增加）一个值为0的元素
let list3: List<Array<number>> = new List();
let b2 = [1, 2, 3];
list3.add(b2); // 增加一个Array类型的元素
console.info(`result: ${list1[0]}`); // 访问索引为0的元素。输出：result: a
console.info(`result: ${list3.get(0)}`); // 访问索引为0的元素。输出：result: 1,2,3
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/nonlinear-container-V14
爬取时间: 2025-04-27 22:48:18
来源: Huawei Developer
非线性容器实现能快速查找的数据结构，其底层通过hash或者红黑树实现，包括HashMap、HashSet、TreeMap、TreeSet、LightWeightMap、LightWeightSet、PlainArray七种。非线性容器中的key及value的类型均满足ECMA标准。
各非线性容器类型特征对比
| 类名 | 特征及建议使用场景 |
| --- | --- |
| HashMap | 存储具有关联关系的键值对集合，存储元素中键唯一，依据键的hash值确定存储位置。访问速度较快，但不能自定义排序。需要快速存取、插入删除键值对数据时推荐使用。 |
| HashSet | 存储一系列值的集合，存储元素中值唯一，依据值的hash确定存储位置。允许放入null值，但不能自定义排序。需要不重复的集合或需要去重某个集合时可以使用。 |
| TreeMap | 存储具有关联关系的键值对集合，存储元素中键唯一，允许用户自定义排序方法。一般需要按序存储键值对的场景可以使用。 |
| TreeSet | 存储一系列值的集合，存储元素中值唯一，允许用户自定义排序方法，但不建议放入null值。一般需要按序存储集合的场景可以使用。 |
| LightWeightMap | 存储具有关联关系的键值对集合，存储元素中键唯一，底层采用更加轻量级的结构，空间占用小。需要存取键值对数据且内存不充足时推荐使用。 |
| LightWeightSet | 存储一系列值的集合，存储元素中值唯一，底层采用更加轻量级的结构，空间占用小。需要不重复的集合或需要去重某个集合时推荐使用。 |
| PlainArray | 存储具有关联关系的键值对集合，存储元素中键唯一，底层与LightWeightMap一样采用更加轻量级的结构，且键固定为number类型。需要存储键为number类型的键值对时可以使用。 |
HashMap
HashMap可用来存储具有关联关系的key-value键值对集合，存储元素中key是唯一的，每个key会对应一个value值。
HashMap依据泛型定义，集合中通过key的hash值确定其存储位置，从而快速找到键值对。HashMap的初始容量大小为16，并支持动态扩容，每次扩容大小为原始容量的2倍。HashMap底层基于HashTable实现，冲突策略采用链地址法。
HashMap和TreeMap相比，HashMap依据键的hashCode存取数据，访问速度较快。而TreeMap是有序存取，效率较低。
HashSet基于HashMap实现。HashMap的输入参数由key、value两个值组成。在HashSet中，只对value对象进行处理。
需要快速存取、删除以及插入键值对数据时，推荐使用HashMap。
HashMap进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | set(key: K, value: V) | 增加一个键值对。 |
| 访问元素 | get(key: K) | 获取key对应的value值。 |
| 访问元素 | keys() | 返回一个迭代器对象，包含map中的所有key值。 |
| 访问元素 | values() | 返回一个迭代器对象，包含map中的所有value值。 |
| 访问元素 | entries() | 返回一个迭代器对象，包含map中的所有键值对。 |
| 访问元素 | forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object) | 遍历访问整个map的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<[K,V]> | 创建迭代器以进行数据访问。 |
| 修改元素 | replace(key: K, newValue: V) | 修改指定key对应的value值。 |
| 修改元素 | forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object) | 通过遍历修改整个map的元素。 |
| 删除元素 | remove(key: K) | 删除map中匹配到的键值对。 |
| 删除元素 | clear() | 清空整个map。 |
HashSet
HashSet可用来存储一系列值的集合，存储元素中value是唯一的。
HashSet依据泛型定义，集合中通过value的hash值确定其存储位置，从而快速找到该值。HashSet初始容量大小为16，支持动态扩容，每次扩容大小为原始容量的2倍。value的类型满足ECMA标准中要求的类型。HashSet基于HashMap实现，只对value对象进行处理。底层数据结构与HashMap一致。
HashSet和TreeSet相比，HashSet中的数据无序存放，即不能由用户指定排序方式，而TreeSet是有序存放，能够依照用户给定的排序函数对元素进行排序。它们集合中的元素都不允许重复，但HashSet允许放入null值，TreeSet不建议存放null值，可能会对排序结果产生影响。
可以利用HashSet不重复的特性，当需要不重复的集合或需要去重某个集合的时候使用。
HashSet进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(value: T) | 增加一个值。 |
| 访问元素 | values() | 返回一个迭代器对象，包含set中的所有value值。 |
| 访问元素 | entries() | 返回一个迭代器对象，包含类似键值对的数组，键值都是value。 |
| 访问元素 | forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object) | 遍历访问整个set的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object) | 通过遍历修改整个set的元素。 |
| 删除元素 | remove(value: T) | 删除set中匹配到的值。 |
| 删除元素 | clear() | 清空整个set。 |
TreeMap
TreeMap可用来存储具有关联关系的key-value键值对集合，存储元素中key是唯一的，每个key会对应一个value值。
TreeMap依据泛型定义，集合中的key值是有序的，TreeMap的底层是一棵二叉树，可以通过树的二叉查找快速的找到键值对。key的类型满足ECMA标准中要求的类型。TreeMap中的键值是有序存储的。TreeMap底层基于红黑树实现，可以进行快速的插入和删除。
TreeMap和HashMap相比，HashMap依据键的hashCode存取数据，访问速度较快。而TreeMap是有序存取，效率较低。
一般需要存储有序键值对的场景，可以使用TreeMap。
TreeMap进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | set(key: K, value: V) | 增加一个键值对。 |
| 访问元素 | get(key: K) | 获取key对应的value值。 |
| 访问元素 | getFirstKey() | 获取map中排在首位的key值。 |
| 访问元素 | getLastKey() | 获取map中排在未位的key值。 |
| 访问元素 | keys() | 返回一个迭代器对象，包含map中的所有key值。 |
| 访问元素 | values() | 返回一个迭代器对象，包含map中的所有value值。 |
| 访问元素 | entries() | 返回一个迭代器对象，包含map中的所有键值对。 |
| 访问元素 | forEach(callbackFn: (value?: V, key?: K, map?: TreeMap<K, V>) => void, thisArg?: Object) | 遍历访问整个map的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<[K,V]> | 创建迭代器以进行数据访问。 |
| 修改元素 | replace(key: K, newValue: V) | 修改指定key对应的value值。 |
| 修改元素 | forEach(callbackFn: (value?: V, key?: K, map?: TreeMap<K, V>) => void, thisArg?: Object) | 通过遍历修改整个map的元素。 |
| 删除元素 | remove(key: K) | 删除map中匹配到的键值对。 |
| 删除元素 | clear() | 清空整个map。 |
TreeSet
TreeSet可用来存储一系列值的集合，存储元素中value是唯一的。
TreeSet依据泛型定义，集合中的value值是有序的，TreeSet的底层是一棵二叉树，可以通过树的二叉查找快速的找到该value值，value的类型满足ECMA标准中要求的类型。TreeSet中的值是有序存储的。TreeSet底层基于红黑树实现，可以进行快速的插入和删除。
TreeSet基于TreeMap实现，在TreeSet中，只对value对象进行处理。TreeSet可用于存储一系列值的集合，元素中value唯一，且能够依照用户给定的排序函数对元素进行排序。
TreeSet和HashSet相比，HashSet中的数据无序存放，而TreeSet是有序存放。它们集合中的元素都不允许重复，但HashSet允许放入null值，TreeSet不建议存放null值，可能会对排序结果产生影响。
一般需要存储有序集合的场景，可以使用TreeSet。
TreeSet进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(value: T) | 增加一个值。 |
| 访问元素 | values() | 返回一个迭代器对象，包含set中的所有value值。 |
| 访问元素 | entries() | 返回一个迭代器对象，包含类似键值对的数组，键值都是value。 |
| 访问元素 | getFirstValue() | 获取set中排在首位的value值。 |
| 访问元素 | getLastValue() | 获取set中排在未位的value值。 |
| 访问元素 | forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object) | 遍历访问整个set的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object) | 通过遍历修改整个set的元素。 |
| 删除元素 | remove(value: T) | 删除set中匹配到的值。 |
| 删除元素 | clear() | 清空整个set。 |
LightWeightMap
LightWeightMap可用来存储具有关联关系的key-value键值对集合，存储元素中key是唯一的，每个key会对应一个value值。LightWeightMap依据泛型定义，采用更加轻量级的结构，底层标识唯一key通过hash实现，其冲突策略为线性探测法。集合中的key值的查找依赖于hash值以及二分查找算法，通过一个数组存储hash值，然后映射到其他数组中的key值以及value值，key的类型满足ECMA标准中要求的类型。
初始默认容量大小为8，每次扩容大小为原始容量的2倍。
LightWeightMap和HashMap都是用来存储键值对的集合，LightWeightMap占用内存更小。
当需要存取key-value键值对时，推荐使用占用内存更小的LightWeightMap。
LightWeightMap进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | set(key: K, value: V) | 增加一个键值对。 |
| 访问元素 | get(key: K) | 获取key对应的value值。 |
| 访问元素 | getIndexOfKey(key: K) | 获取map中指定key的index。 |
| 访问元素 | getIndexOfValue(value: V) | 获取map中指定value出现的第一个的index。 |
| 访问元素 | keys() | 返回一个迭代器对象，包含map中的所有key值。 |
| 访问元素 | values() | 返回一个迭代器对象，包含map中的所有value值。 |
| 访问元素 | entries() | 返回一个迭代器对象，包含map中的所有键值对。 |
| 访问元素 | getKeyAt(index: number) | 获取指定index对应的key值。 |
| 访问元素 | getValueAt(index: number) | 获取指定index对应的value值。 |
| 访问元素 | forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object) | 遍历访问整个map的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<[K,V]> | 创建迭代器以进行数据访问。 |
| 修改元素 | setValueAt(index: number, newValue: V) | 修改指定index对应的value值。 |
| 修改元素 | forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object) | 通过遍历修改整个map的元素。 |
| 删除元素 | remove(key: K) | 删除map中指定key匹配到的键值对。 |
| 删除元素 | removeAt(index: number) | 删除map中指定index对应的键值对。 |
| 删除元素 | clear() | 清空整个map。 |
LightWeightSet
LightWeightSet可用来存储一系列值的集合，存储元素中value是唯一的。
LightWeightSet依据泛型定义，采用更加轻量级的结构，初始默认容量大小为8，每次扩容大小为原始容量的2倍。集合中的value值的查找依赖于hash以及二分查找算法，通过一个数组存储hash值，然后映射到其他数组中的value值，value的类型满足ECMA标准中要求的类型。
LightWeightSet底层标识唯一value基于hash实现，其冲突策略为线性探测法，查找策略基于二分查找法。
LightWeightSet和HashSet都是用来存储键值的集合，LightWeightSet的占用内存更小。
当需要存取某个集合或是对某个集合去重时，推荐使用占用内存更小的LightWeightSet。
LightWeightSet进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(value: T) | 增加一个值。 |
| 访问元素 | getIndexOf(key: T) | 获取对应的index值。 |
| 访问元素 | getValueAt(index: number) | 获取指定index对应的value值。 |
| 访问元素 | values() | 返回一个迭代器对象，包含set中的所有value值。 |
| 访问元素 | entries() | 返回一个迭代器对象，包含类似键值对的数组，键值都是value。 |
| 访问元素 | forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object) | 遍历访问整个set的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<T> | 创建迭代器以进行数据访问。 |
| 修改元素 | forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object) | 通过遍历修改整个set的元素。 |
| 删除元素 | remove(key: K) | 删除set中匹配到的键值对。 |
| 删除元素 | removeAt(index: number) | 删除set中指定index对应的值。 |
| 删除元素 | clear() | 清空整个set。 |
PlainArray
PlainArray可用来存储具有关联关系的键值对集合，存储元素中key是唯一的，并且对于PlainArray来说，其key的类型为number类型。每个key会对应一个value值，类型依据泛型的定义，PlainArray采用更加轻量级的结构，集合中的key值的查找依赖于二分查找算法，然后映射到其他数组中的value值。
初始默认容量大小为16，每次扩容大小为原始容量的2倍。
PlainArray和LightWeightMap都是用来存储键值对，且均采用轻量级结构，但PlainArray的key值类型只能为number类型。
当需要存储key值为number类型的键值对时，可以使用PlainArray。
PlainArray进行增、删、改、查操作的常用API如下：
| 操作 | 方法 | 描述 |
| --- | --- | --- |
| 增加元素 | add(key: number,value: T) | 增加一个键值对。 |
| 访问元素 | get(key: number) | 获取key对应的value值。 |
| 访问元素 | getIndexOfKey(key: number) | 获取PlainArray中指定key的index。 |
| 访问元素 | getIndexOfValue(value: T) | 获取PlainArray中指定value出现的第一个的index。 |
| 访问元素 | getKeyAt(index: number) | 获取指定index对应的key值。 |
| 访问元素 | getValueAt(index: number) | 获取指定index对应的value值。 |
| 访问元素 | forEach(callbackFn: (value: T, index?: number, PlainArray?: PlainArray<T>) => void, thisArg?: Object) | 遍历访问整个PlainArray的元素。 |
| 访问元素 | [Symbol.iterator]():IterableIterator<[number, T]> | 创建迭代器以进行数据访问。 |
| 修改元素 | setValueAt(index:number, value: T) | 修改指定index对应的value值。 |
| 修改元素 | forEach(callbackFn: (value: T, index?: number, PlainArray?: PlainArray<T>) => void, thisArg?: Object) | 通过遍历修改整个PlainArray的元素。 |
| 删除元素 | remove(key: number) | 删除PlainArray中指定key匹配到的键值对。 |
| 删除元素 | removeAt(index: number) | 删除PlainArray中指定index对应的键值对。 |
| 删除元素 | removeRangeFrom(index: number, size: number) | 删除PlainArray中指定范围内的元素。 |
| 删除元素 | clear() | 清空整个PlainArray。 |
非线性容器的使用
此处列举常用的非线性容器HashMap、TreeMap、LightWeightMap、PlainArray的使用示例，包括导入模块、增加元素、访问元素及修改等操作，示例代码如下所示：
```typescript
// HashMap
import { HashMap } from '@kit.ArkTS'; // 导入HashMap模块
let hashMap1: HashMap<string, number> = new HashMap();
hashMap1.set('a', 123); // 增加一个键为'a'，值为123的元素
let hashMap2: HashMap<number, number> = new HashMap();
hashMap2.set(4, 123); // 增加一个键为4，值为123的元素
console.info(`result: ${hashMap2.hasKey(4)}`); // 判断是否含有键为4的元素。输出：result: true
console.info(`result: ${hashMap1.get('a')}`); // 访问键为'a'的元素。输出：result: 123
// TreeMap
import { TreeMap } from '@kit.ArkTS'; // 导入TreeMap模块
let treeMap: TreeMap<string, number> = new TreeMap();
treeMap.set('a', 123); // 增加一个键为'a'，值为123的元素
treeMap.set('6', 356); // 增加一个键为'6'，值为356的元素
console.info(`result: ${treeMap.get('a')}`); // 访问键为'a'的元素。输出：result: 123
console.info(`result: ${treeMap.getFirstKey()}`); // 访问首元素。输出：result: 6
console.info(`result: ${treeMap.getLastKey()}`); // 访问尾元素。输出：result: a
// LightWeightMap
import { LightWeightMap } from '@kit.ArkTS'; // 导入LightWeightMap模块
let lightWeightMap: LightWeightMap<string, number> = new LightWeightMap();
lightWeightMap.set('x', 123); // 增加一个键为'x'，值为123的元素
lightWeightMap.set('8', 356); // 增加一个键为'8'，值为356的元素
console.info(`result: ${lightWeightMap.get('a')}`); // 访问键为'a'的元素。输出：result: undefined
console.info(`result: ${lightWeightMap.get('x')}`); // 访问键为'x'的元素，获取其值。输出：result: 123
console.info(`result: ${lightWeightMap.getIndexOfKey('8')}`); // 访问键为'8'的元素，获取其索引。输出：result: 0
// PlainArray
import { PlainArray } from '@kit.ArkTS'; // 导入PlainArray模块
let plainArray: PlainArray<string> = new PlainArray();
plainArray.add(1, 'sdd'); // 增加一个键为1，值为'sdd'的元素
plainArray.add(2, 'sff'); // 增加一个键为2，值为'sff'的元素
console.info(`result: ${plainArray.get(1)}`); // 访问键为1的元素，获取值。输出：result: sdd
console.info(`result: ${plainArray.getKeyAt(1)}`); // 访问索引为1的元素，获取键。输出：result: 2
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-concurrency-V14
爬取时间: 2025-04-27 22:48:32
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/concurrency-overview-V14
爬取时间: 2025-04-27 22:48:45
来源: Huawei Developer
并发是指在同一时间内，存在多个任务同时执行的情况。对于多核设备，这些任务可能同时在不同CPU上并行执行。对于单核设备，多个并发任务不会在同一时刻并行执行，但是CPU会在某个任务休眠或进行I/O操作等状态下切换任务，调度执行其他任务，提升CPU的资源利用率。
为了提升应用的响应速度与帧率，避免耗时任务对UI主线程的影响，ArkTS提供了异步并发和多线程并发两种处理策略。
-  异步并发是指异步代码在执行到一定程度后会被暂停，以便在未来某个时间点继续执行，这种情况下，同一时间只有一段代码在执行。ArkTS通过Promise和async/await提供异步并发能力，适用于单次I/O任务的开发场景。详细请参见使用异步并发能力。
-  多线程并发允许在同一时间段内同时执行多段代码。在UI主线程继续响应用户操作和更新UI的同时，后台线程也能执行耗时操作，从而避免应用出现卡顿。ArkTS通过TaskPool和Worker提供多线程并发能力，适用于耗时任务等并发场景。详细请参见多线程并发概述。
并发多线程场景下，不同并发线程间需要进行数据通信，不同类别对象的传输方式存在差异，包括拷贝或内存共享等。
并发能力在多种场景中都有应用，其中包括异步并发任务、耗时任务（CPU密集型任务、I/O密集型任务和同步任务等）、长时任务、常驻任务等。开发者可以根据不同的任务诉求和场景，选择相应的并发策略进行优化和开发，也可以具体查看应用多线程开发实践案例。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/async-concurrency-overview-V14
爬取时间: 2025-04-27 22:48:59
来源: Huawei Developer
Promise和async/await提供异步并发能力，是标准的JS异步语法。异步代码会被挂起并在之后继续执行，同一时间只有一段代码执行，适用于单次I/O任务的场景开发，例如一次网络请求、一次文件读写等操作。无需另外启动线程执行。
异步语法是一种编程语言的特性，允许程序在执行某些操作时不必等待其完成，而是可以继续执行其他操作。
Promise
Promise是一种用于处理异步操作的对象，可以将异步操作转换为类似于同步操作的风格，以方便代码编写和维护。Promise提供了一个状态机制来管理异步操作的不同阶段，并提供了一些方法来注册回调函数以处理异步操作的成功或失败的结果。
Promise有三种状态：pending（进行中）、fulfilled（已完成）和rejected（已拒绝）。Promise对象创建后处于pending状态，并在异步操作完成后转换为fulfilled或rejected状态。
最基本的用法是通过构造函数实例化一个Promise对象，同时传入一个带有两个参数的函数，通常称为executor函数。executor函数接收两个参数：resolve和reject，分别表示异步操作成功和失败时的回调函数。例如，以下代码创建了一个Promise对象并模拟了一个异步操作：
```typescript
const promise: Promise<number> = new Promise((resolve: Function, reject: Function) => {
setTimeout(() => {
const randomNumber: number = Math.random();
if (randomNumber > 0.5) {
resolve(randomNumber);
} else {
reject(new Error('Random number is too small'));
}
}, 1000);
})
```
上述代码中，setTimeout函数模拟了一个异步操作，并在1秒钟后随机生成一个数字。如果随机数大于0.5，则执行resolve回调函数并将随机数作为参数传递；否则执行reject回调函数并传递一个错误对象作为参数。
Promise对象创建后，可以使用then方法和catch方法指定fulfilled状态和rejected状态的回调函数。then方法可接受两个参数，一个处理fulfilled状态的函数，另一个处理rejected状态的函数。只传一个参数则表示当Promise对象状态变为fulfilled时，then方法会自动调用这个回调函数，并将Promise对象的结果作为参数传递给它。使用catch方法注册一个回调函数，用于处理“失败”的结果，即捕获Promise的状态改变为rejected状态或操作失败抛出的异常。例如：
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
promise.then((result: number) => {
console.info(`Random number is ${result}`);
}).catch((error: BusinessError) => {
console.error(error.message);
});
```
上述代码中，then方法的回调函数接收Promise对象的成功结果作为参数，并将其输出到控制台上。如果Promise对象进入rejected状态，则catch方法的回调函数接收错误对象作为参数，并将其输出到控制台上。
当Promise被reject且未通过catch方法来处理时，会触发unhandledrejection事件。可使用errorManager.on('error')接口监听该事件，以全局捕获未处理的Promise reject。
async/await
async/await是一种用于处理异步操作的Promise语法糖，使得编写异步代码变得更加简单和易读。通过使用async关键字声明一个函数为异步函数，并使用await关键字等待Promise的解析（完成或拒绝），以同步的方式编写异步操作的代码。
async函数是一个返回Promise对象的函数，用于表示一个异步操作。在async函数内部，可以使用await关键字等待一个Promise对象的解析，并返回其解析值。如果一个async函数抛出异常，那么该函数返回的Promise对象将被拒绝，并且异常信息会被传递给Promise对象的onRejected()方法。
下面是一个使用async/await的例子，其中模拟了一个以同步方式执行异步操作的场景，该操作会在3秒钟后返回一个字符串。
```typescript
async function myAsyncFunction(): Promise<string> {
const result: string = await new Promise((resolve: Function) => {
setTimeout(() => {
resolve('Hello, world!');
}, 3000);
});
console.info(result); // 输出： Hello, world!
return result;
}
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
.onClick(async () => {
let res = await myAsyncFunction();
console.info("res is: " + res);
})
}
.width('100%')
}
.height('100%')
}
}
```
在上述示例代码中，使用了await关键字来等待Promise对象的解析，并将其解析值存储在result变量中。
需要注意的是，由于要等待异步操作完成，因此需要将整个操作包在async函数中，并搭配await关键字使用。除了在async函数中使用await外，还可以使用try/catch块来捕获异步操作中的异常。
```typescript
async function myAsyncFunction(): Promise<void> {
try {
const result: string = await new Promise((resolve: Function) => {
resolve('Hello, world!');
});
} catch (e) {
console.error(`Get exception: ${e}`);
}
}
myAsyncFunction();
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/multithread-concurrency-V14
爬取时间: 2025-04-27 22:49:13
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/multi-thread-concurrency-overview-V14
爬取时间: 2025-04-27 22:49:26
来源: Huawei Developer
并发模型是用来实现不同应用场景中并发任务的编程模型，常见的并发模型分为基于内存共享的并发模型和基于消息通信的并发模型。
Actor并发模型作为基于消息通信并发模型的典型代表，不需要开发者去面对锁带来的一系列复杂偶发的问题，同时并发度也相对较高，因此得到了广泛的支持和使用。
当前ArkTS提供了TaskPool和Worker两种并发能力，TaskPool和Worker都基于Actor并发模型实现。
Actor并发模型和内存共享并发模型的具体对比请见多线程并发模型。
多线程并发模型
内存共享并发模型指多线程同时执行任务，这些线程依赖同一内存并且都有权限访问，线程访问内存前需要抢占并锁定内存的使用权，没有抢占到内存的线程需要等待其他线程释放使用权再执行。
Actor并发模型每一个线程都是一个独立Actor，每个Actor有自己独立的内存，Actor之间通过消息传递机制触发对方Actor的行为，不同Actor之间不能直接访问对方的内存空间。
Actor并发模型对比内存共享并发模型的优势在于不同线程间内存隔离，不会产生不同线程竞争同一内存资源的问题。开发者不需要考虑对内存上锁导致的一系列功能、性能问题，提升了开发效率。
由于Actor并发模型线程之间不共享内存，需要通过线程间通信机制传输并发任务和任务结果。
本文以经典的生产者消费者问题为例，对比呈现这两种模型在解决具体问题时的差异。
内存共享模型
以下示例伪代码和示意图展示了如何使用内存共享模型解决生产者消费者问题。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170230.11205329479566227709476607208807:50001231000000:2800:F5794CAC525A26D7C19D7D75045BB1490C6E822AD33CC94AA6D35A44954E8154.png)
为了避免不同生产者或消费者同时访问一块共享内存的容器时产生的脏读，脏写现象，同一时间只能有一个生产者或消费者访问该容器，也就是不同生产者和消费者争夺使用容器的锁。当一个角色获取锁之后其他角色需要等待该角色释放锁之后才能重新尝试获取锁以访问该容器。
```typescript
// 此段示例为伪代码仅作为逻辑示意，便于开发者理解使用内存共享模型和Actor模型的区别
class Queue {
// ...
push(value: number) {}
empty(): boolean {
// ...
return true
}
pop(value: number) :number {
// ...
return value;
}
}
class Mutex {
// ...
lock(): boolean {
// ...
return true;
}
unlock() {
}
}
class BufferQueue {
queue: Queue = new Queue()
mutex: Mutex = new Mutex()
add(value: number) {
// 尝试获取锁
if (this.mutex.lock()) {
this.queue.push(value)
this.mutex.unlock()
}
}
take(value: number): number {
let res: number = 0;
// 尝试获取锁
if (this.mutex.lock()) {
if (this.queue.empty()) {
res = 1;
}
let num: number = this.queue.pop(value)
this.mutex.unlock()
res = num;
}
return res;
}
}
// 构造一段全局共享的内存
let g_bufferQueue = new BufferQueue()
class Producer {
constructor() {
}
run() {
let value = Math.random()
// 跨线程访问bufferQueue对象
g_bufferQueue.add(value)
}
}
class ConsumerTest {
constructor() {
}
run() {
// 跨线程访问bufferQueue对象
let num = 123;
let res = g_bufferQueue.take(num)
if (res != null) {
// 添加消费逻辑
}
}
}
function Main(): void {
let consumer: ConsumerTest = new ConsumerTest()
let producer1: Producer = new Producer()
for (let i = 0;i < 0;i++) {
// 模拟启动多线程执行生产任务
// let thread = new Thread()
// thread.run(producer.run())
// consumer.run()
}
}
```
Actor模型
以下示例简单展示了如何使用基于Actor模型的TaskPool并发能力来解决生产者消费者问题。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170230.76279357139754768299685059759587:50001231000000:2800:001796039BEF10561775B2DC8281ADC1A226DE15DF8ECC420E506509EB22124A.png)
Actor模型不同角色之间并不共享内存，生产者线程和UI线程都有自己的虚拟机实例，两个虚拟机实例之间拥有独占的内存，相互隔离。生产者生产出结果后通过序列化通信将结果发送给UI线程，UI线程消费结果后再发送新的生产任务给生产者线程。
```typescript
import { taskpool } from '@kit.ArkTS';
// 跨线程并发任务
@Concurrent
async function produce(): Promise<number> {
// 添加生产相关逻辑
console.info("producing...");
return Math.random();
}
class Consumer {
public consume(value: Object) {
// 添加消费相关逻辑
console.info("consuming value: " + value);
}
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World'
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
Button() {
Text("start")
}.onClick(() => {
let produceTask: taskpool.Task = new taskpool.Task(produce);
let consumer: Consumer = new Consumer();
for (let index: number = 0; index < 10; index++) {
// 执行生产异步并发任务
taskpool.execute(produceTask).then((res: Object) => {
consumer.consume(res);
}).catch((e: Error) => {
console.error(e.message);
})
}
})
.width('20%')
.height('20%')
}
.width('100%')
}
.height('100%')
}
}
```
TaskPool和Worker
ArkTS提供了TaskPool和Worker两种并发能力供开发者选择，各自的运作机制和注意事项请见TaskPool简介和Worker简介，两者之间实现的特点和适用场景也存在差异，请见TaskPool和Worker的对比。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/taskpool-introduction-V14
爬取时间: 2025-04-27 22:49:40
来源: Huawei Developer
任务池（TaskPool）作用是为应用程序提供一个多线程的运行环境，降低整体资源的消耗、提高系统的整体性能，且您无需关心线程实例的生命周期。具体接口信息及使用方法详情请见TaskPool。
TaskPool运作机制
TaskPool运作机制示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170230.22872154019692151545901864356681:50001231000000:2800:4B8FB30085AB4AAAD63041CE8643886A1029E11BF399C49D39C2CD4E3A62398B.png)
TaskPool支持开发者在宿主线程封装任务抛给任务队列，系统选择合适的工作线程，进行任务的分发及执行，再将结果返回给宿主线程。接口直观易用，支持任务的执行、取消，以及指定优先级的能力，同时通过系统统一线程管理，结合动态调度及负载均衡算法，可以节约系统资源。系统默认会启动一个任务工作线程，当任务较多时会扩容，工作线程数量上限跟当前设备的物理核数相关，具体数量内部管理，保证最优的调度及执行效率，长时间没有任务分发时会缩容，减少工作线程数量。
TaskPool注意事项
-  实现任务的函数需要使用@Concurrent装饰器标注，且仅支持在.ets文件中使用。
-  从API version 11开始，跨并发实例传递带方法的实例对象时，该类必须使用装饰器@Sendable装饰器标注，且仅支持在.ets文件中使用。
-  任务函数在TaskPool工作线程的执行耗时不能超过3分钟（不包含Promise和async/await异步调用的耗时，例如网络下载、文件读写等I/O任务的耗时），否则会被强制退出。
-  实现任务的函数入参需满足序列化支持的类型，详情请参见线程间通信对象。
-  ArrayBuffer参数在TaskPool中默认转移，需要设置转移列表的话可通过接口setTransferList()设置。
-  由于不同线程中上下文对象是不同的，因此TaskPool工作线程只能使用线程安全的库，例如UI相关的非线程安全库不能使用。
-  序列化传输的数据量大小限制为16MB。
-  Priority的IDLE优先级是用来标记需要在后台运行的耗时任务（例如数据同步、备份），它的优先级别是最低的。这种优先级标记的任务只会在所有线程都空闲的情况下触发执行，并且只会占用一个线程来执行。
-  Promise不支持跨线程传递，如果TaskPool返回pending或rejected状态的Promise，会返回失败；对于fulfilled状态的Promise，TaskPool会解析返回的结果，如果结果可以跨线程传递，则返回成功。
-  不支持在TaskPool工作线程中使用AppStorage。
-  TaskPool支持开发者在宿主线程封装任务抛给任务队列，理论上可以支持任意多的任务，但任务的执行受限于任务的优先级以及系统资源的影响，在工作线程扩容到最大后，可能会导致任务的执行效率下降。
@Concurrent装饰器
在使用TaskPool时，执行的并发函数需要使用该装饰器修饰，否则无法通过相关校验。
从API version 9开始，支持使用@Concurrent装饰器声明并校验并发函数。
装饰器说明
| @Concurrent并发装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 使用场景 | 仅支持在Stage模型的工程中使用。仅支持在.ets文件中使用。 |
| 装饰的函数类型 | 允许标注async函数或普通函数。禁止标注generator、箭头函数、类方法。不支持类成员函数或者匿名函数。 |
| 装饰的函数内的变量类型 | 允许使用local变量、入参和通过import引入的变量。禁止使用闭包变量。 |
| 装饰的函数内的返回值类型 | 支持的类型请查线程间通信对象。 |
由于@Concurrent标记的函数不能访问闭包，因此@Concurrent标记的函数内部不能调用当前文件的其他函数，例如：
```typescript
function bar() {
}
@Concurrent
function foo() {
bar(); // 违反闭包原则，报错
}
```
装饰器使用示例
并发函数一般使用
并发函数为一个计算两数之和的普通函数，taskpool执行该函数并返回结果。
示例：
```typescript
import { taskpool } from '@kit.ArkTS';
@Concurrent
function add(num1: number, num2: number): number {
return num1 + num2;
}
async function ConcurrentFunc(): Promise<void> {
try {
let task: taskpool.Task = new taskpool.Task(add, 1, 2);
console.info("taskpool res is: " + await taskpool.execute(task));
} catch (e) {
console.error("taskpool execute error is: " + e);
}
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World'
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
ConcurrentFunc();
})
}
.width('100%')
}
.height('100%')
}
}
```
并发函数返回Promise
并发函数中返回Promise的表现需关注，如下例所示，其中testPromise、testPromise1等并发同步函数会处理该Promise并返回结果。
示例：
```typescript
import { taskpool } from '@kit.ArkTS';
@Concurrent
function testPromise(args1: number, args2: number): Promise<number> {
return new Promise<number>((testFuncA, testFuncB)=>{
testFuncA(args1 + args2);
});
}
@Concurrent
async function testPromise1(args1: number, args2: number): Promise<number> {
return new Promise<number>((testFuncA, testFuncB)=>{
testFuncA(args1 + args2);
});
}
@Concurrent
async function testPromise2(args1: number, args2: number): Promise<number> {
return await new Promise<number>((testFuncA, testFuncB)=>{
testFuncA(args1 + args2);
});
}
@Concurrent
function testPromise3() {
return Promise.resolve(1);
}
@Concurrent
async function testPromise4(): Promise<number> {
return 1;
}
@Concurrent
async function testPromise5(): Promise<string> {
return await new Promise((resolve) => {
setTimeout(()=>{
resolve("Promise setTimeout after resolve");
}, 1000)
});
}
async function testConcurrentFunc() {
let task1: taskpool.Task = new taskpool.Task(testPromise, 1, 2);
let task2: taskpool.Task = new taskpool.Task(testPromise1, 1, 2);
let task3: taskpool.Task = new taskpool.Task(testPromise2, 1, 2);
let task4: taskpool.Task = new taskpool.Task(testPromise3);
let task5: taskpool.Task = new taskpool.Task(testPromise4);
let task6: taskpool.Task = new taskpool.Task(testPromise5);
taskpool.execute(task1).then((d:object)=>{
console.info("task1 res is: " + d);
}).catch((e:object)=>{
console.info("task1 catch e: " + e);
})
taskpool.execute(task2).then((d:object)=>{
console.info("task2 res is: " + d);
}).catch((e:object)=>{
console.info("task2 catch e: " + e);
})
taskpool.execute(task3).then((d:object)=>{
console.info("task3 res is: " + d);
}).catch((e:object)=>{
console.info("task3 catch e: " + e);
})
taskpool.execute(task4).then((d:object)=>{
console.info("task4 res is: " + d);
}).catch((e:object)=>{
console.info("task4 catch e: " + e);
})
taskpool.execute(task5).then((d:object)=>{
console.info("task5 res is: " + d);
}).catch((e:object)=>{
console.info("task5 catch e: " + e);
})
taskpool.execute(task6).then((d:object)=>{
console.info("task6 res is: " + d);
}).catch((e:object)=>{
console.info("task6 catch e: " + e);
})
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Column() {
Button(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
testConcurrentFunc();
})
}
.width('100%')
}
.height('100%')
}
}
```
并发函数中使用自定义类或函数
并发函数中使用自定义类或函数时需定义在不同文件，否则会被认为是闭包，如下例所示。
示例：
```typescript
// Index.ets
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { testAdd, MyTestA, MyTestB } from './Test';
function add(arg: number) {
return ++arg;
}
class TestA {
constructor(name: string) {
this.name = name;
}
name: string = 'ClassA';
}
class TestB {
static nameStr: string = 'ClassB';
}
@Concurrent
function TestFunc() {
// case1：在并发函数中直接调用同文件内定义的类或函数
// 直接调用同文件定义的函数add()，add飘红报错：Only imported variables and local variables can be used in @Concurrent decorated functions. <ArkTSCheck>
// add(1);
// 直接使用同文件定义的TestA构造，TestA飘红报错：Only imported variables and local variables can be used in @Concurrent decorated functions. <ArkTSCheck>
// let a = new TestA("aaa");
// 直接访问同文件定义的TestB的成员nameStr，TestB飘红报错：Only imported variables and local variables can be used in @Concurrent decorated functions. <ArkTSCheck>
// console.info("TestB name is: " + TestB.nameStr);
// case2：在并发函数中调用定义在Test.ets文件并导入当前文件的类或函数
// 输出结果：res1 is: 2
console.info("res1 is: " + testAdd(1));
let tmpStr = new MyTestA("TEST A");
// 输出结果：res2 is: TEST A
console.info("res2 is: " + tmpStr.name);
// 输出结果：res3 is: MyTestB
console.info("res3 is: " + MyTestB.nameStr);
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(() => {
let task = new taskpool.Task(TestFunc);
taskpool.execute(task).then(() => {
console.info("taskpool: execute task success!");
}).catch((e:BusinessError) => {
console.error(`taskpool: execute: Code: ${e.code}, message: ${e.message}`);
})
})
}
.height('100%')
.width('100%')
}
}
```
```typescript
// Test.ets
export function testAdd(arg: number) {
return ++arg;
}
@Sendable
export class MyTestA {
constructor(name: string) {
this.name = name;
}
name: string = 'MyTestA';
}
export class MyTestB {
static nameStr:string = 'MyTestB';
}
```
并发异步函数中使用Promise
并发异步函数中如果使用Promise，建议搭配await使用。这样TaskPool会捕获Promise中可能发生的异常。推荐使用示例如下。
示例：
```typescript
import { taskpool } from '@kit.ArkTS'
@Concurrent
async function testPromiseError() {
await new Promise<number>((resolve, reject) => {
resolve(1);
}).then(()=>{
throw new Error("testPromise Error");
})
}
@Concurrent
async function testPromiseError1() {
await new Promise<string>((resolve, reject) => {
reject("testPromiseError1 Error msg");
})
}
@Concurrent
function testPromiseError2() {
return new Promise<string>((resolve, reject) => {
reject("testPromiseError2 Error msg");
})
}
async function testConcurrentFunc() {
let task1: taskpool.Task = new taskpool.Task(testPromiseError);
let task2: taskpool.Task = new taskpool.Task(testPromiseError1);
let task3: taskpool.Task = new taskpool.Task(testPromiseError2);
taskpool.execute(task1).then((d:object)=>{
console.info("task1 res is: " + d);
}).catch((e:object)=>{
console.info("task1 catch e: " + e);
})
taskpool.execute(task2).then((d:object)=>{
console.info("task2 res is: " + d);
}).catch((e:object)=>{
console.info("task2 catch e: " + e);
})
taskpool.execute(task3).then((d:object)=>{
console.info("task3 res is: " + d);
}).catch((e:object)=>{
console.info("task3 catch e: " + e);
})
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Column() {
Button(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
testConcurrentFunc();
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/worker-introduction-V14
爬取时间: 2025-04-27 22:49:54
来源: Huawei Developer
Worker主要作用是为应用程序提供一个多线程的运行环境，可满足应用程序在执行过程中与宿主线程分离，在后台线程中运行一个脚本进行耗时操作，极大避免类似于计算密集型或高延迟的任务阻塞宿主线程的运行。具体接口信息及使用方法详情请见Worker。
Worker运作机制
图1Worker运作机制示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170231.30610609115110537440495482226210:50001231000000:2800:0F9434615602A1B439A61D8509E58F0C6E7655AE4C6F0F258FCF6C381372BD7D.png)
创建Worker的线程称为宿主线程（不一定是主线程，工作线程也支持创建Worker子线程），Worker自身的线程称为Worker子线程（或Actor线程、工作线程）。每个Worker子线程与宿主线程拥有独立的实例，包含基础设施、对象、代码段等，因此每个Worker启动存在一定的内存开销，需要限制Worker的子线程数量。Worker子线程和宿主线程之间的通信是基于消息传递的，Worker通过序列化机制与宿主线程之间相互通信，完成命令及数据交互。
Worker注意事项
创建Worker的注意事项
Worker线程文件需要放在"{moduleName}/src/main/ets/"目录层级之下，否则不会被打包到应用中。有手动和自动两种创建Worker线程目录及文件的方式。
-  手动创建：开发者手动创建相关目录及文件，此时需要配置build-profile.json5的相关字段信息，Worker线程文件才能确保被打包到应用中。 Stage模型： FA模型：
```json
"buildOption": {
"sourceOption": {
"workers": [
"./src/main/ets/workers/worker.ets"
]
}
}
```
-  自动创建：DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息，无需再手动在build-profile.json5中进行相关配置。
文件路径注意事项
当使用Worker模块具体功能时，均需先构造Worker实例对象，其构造函数与API版本相关，且构造函数需要传入Worker线程文件的路径（scriptURL）。
```typescript
// 导入模块
import { worker } from '@kit.ArkTS';
// API 9及之后版本使用：
const worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/worker.ets');
// API 8及之前版本使用：
const worker2: worker.Worker = new worker.Worker('entry/ets/workers/worker.ets');
```
Stage模型下的文件路径规则
构造函数中的scriptURL要求如下：
1） 加载Ability中Worker线程文件场景
加载Ability中的worker线程文件，加载路径规则：{moduleName}/ets/{relativePath}。
```typescript
import { worker } from '@kit.ArkTS';
// worker线程文件所在路径："entry/src/main/ets/workers/worker.ets"
const workerStage1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/worker.ets');
// worker线程文件所在路径："testworkers/src/main/ets/ThreadFile/workers/worker.ets"
const workerStage2: worker.ThreadWorker = new worker.ThreadWorker('testworkers/ets/ThreadFile/workers/worker.ets');
```
2） 加载HSP中Worker线程文件场景
加载HSP中worker线程文件，加载路径规则：{moduleName}/ets/{relativePath}。
```typescript
import { worker } from '@kit.ArkTS';
// worker线程文件所在路径： "hsp/src/main/ets/workers/worker.ets"
const workerStage3: worker.ThreadWorker = new worker.ThreadWorker('hsp/ets/workers/worker.ets');
```
3） 加载HAR中Worker线程文件场景
加载HAR中worker线程文件存在以下两种情况：
-  @标识路径加载形式：所有种类的模块加载本地HAR中的Worker线程文件，加载路径规则：@{moduleName}/ets/{relativePath}。
-  相对路径加载形式：本地HAR加载该包内的Worker线程文件，加载路径规则：创建Worker对象所在文件与Worker线程文件的相对路径。
当开启useNormalizedOHMUrl（即将工程目录中与entry同级别的应用级build-profile.json5文件中strictMode属性的useNormalizedOHMUrl字段配置为true）或HAR包会被打包成三方包使用时，则HAR包中使用Worker仅支持通过相对路径的加载形式创建。
```typescript
import { worker } from '@kit.ArkTS';
// @标识路径加载形式：
// worker线程文件所在路径: "har/src/main/ets/workers/worker.ets"
const workerStage4: worker.ThreadWorker = new worker.ThreadWorker('@har/ets/workers/worker.ets');
// 相对路径加载形式：
// worker线程文件所在路径: "har/src/main/ets/workers/worker.ets"
// 创建Worker对象的文件所在路径："har/src/main/ets/components/mainpage/MainPage.ets"
const workerStage5: worker.ThreadWorker = new worker.ThreadWorker('../../workers/worker.ets');
```
FA模型下的文件路径规则
构造函数中的scriptURL为：Worker线程文件与"{moduleName}/src/main/ets/MainAbility"的相对路径。
```typescript
import { worker } from '@kit.ArkTS';
// 主要说明以下三种场景：
// 场景1： Worker线程文件所在路径："{moduleName}/src/main/ets/MainAbility/workers/worker.ets"
const workerFA1: worker.ThreadWorker = new worker.ThreadWorker("workers/worker.ets", {name:"first worker in FA model"});
// 场景2： Worker线程文件所在路径："{moduleName}/src/main/ets/workers/worker.ets"
const workerFA2: worker.ThreadWorker = new worker.ThreadWorker("../workers/worker.ets");
// 场景3： Worker线程文件所在路径："{moduleName}/src/main/ets/MainAbility/ThreadFile/workers/worker.ets"
const workerFA3: worker.ThreadWorker = new worker.ThreadWorker("ThreadFile/workers/worker.ets");
```
生命周期注意事项
-  Worker的创建和销毁耗费性能，建议开发者合理管理已创建的Worker并重复使用。Worker空闲时也会一直运行，因此当不需要Worker时，可以调用terminate()接口或close()方法主动销毁Worker。若Worker处于已销毁或正在销毁等非运行状态时，调用其功能接口，会抛出相应的错误。
-  Worker的数量由内存管理策略决定，设定的内存阈值为1.5GB和设备物理内存的60%中的较小者。在内存允许的情况下，系统最多可以同时运行64个Worker。如果尝试创建的Worker数量超出这一上限，系统将抛出错误：“Worker initialization failure, the number of workers exceeds the maximum.”。实际运行的Worker数量会根据当前内存使用情况动态调整。一旦所有Worker和主线程的累积内存占用超过了设定的阈值，系统将触发内存溢出（OOM）错误，导致应用程序崩溃。
Worker基本用法示例
1.  DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建“worker”为例。 此外，还支持手动创建Worker文件，具体方式和相关注意事项请见创建Worker的注意事项。
2.  导入Worker模块。
```typescript
// Index.ets
import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS'
```
3.  在宿主线程中通过调用ThreadWorker的constructor()方法创建Worker对象，当前线程为宿主线程，并注册回调函数。
```typescript
// Index.ets
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(() => {
// 创建Worker对象
let workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets');
// 注册onmessage回调，当宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息时被调用，在宿主线程执行
workerInstance.onmessage = (e: MessageEvents) => {
let data: string = e.data;
console.info("workerInstance onmessage is: ", data);
}
// 注册onerror回调，当Worker在执行过程中发生异常时被调用，在宿主线程执行
workerInstance.onerror = (err: ErrorEvent) => {
console.info("workerInstance onerror message is: " + err.message);
}
// 注册onmessageerror回调，当Worker对象接收到一条无法被序列化的消息时被调用，在宿主线程执行
workerInstance.onmessageerror = () => {
console.info('workerInstance onmessageerror');
}
// 注册onexit回调，当Worker销毁时被调用，在宿主线程执行
workerInstance.onexit = (e: number) => {
// 当Worker正常退出时code为0，异常退出时code为1
console.info("workerInstance onexit code is: ", e);
}
// 向Worker线程发送消息
workerInstance.postMessage('1');
})
}
.height('100%')
.width('100%')
}
}
```
4.  在Worker文件中注册回调函数。
```typescript
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
// 注册onmessage回调，当Worker线程收到来自其宿主线程通过postMessage接口发送的消息时被调用，在Worker线程执行
workerPort.onmessage = (e: MessageEvents) => {
let data: string = e.data;
console.info('workerPort onmessage is: ', data);
// 向主线程发送消息
workerPort.postMessage('2');
}
// 注册onmessageerror回调，当Worker对象接收到一条无法被序列化的消息时被调用，在Worker线程执行
workerPort.onmessageerror = () => {
console.info('workerPort onmessageerror');
}
// 注册onerror回调，当Worker在执行过程中发生异常被调用，在Worker线程执行
workerPort.onerror = (err: ErrorEvent) => {
console.info('workerPort onerror err is: ', err.message);
}
```
跨har包加载Worker
1.  创建har详情参考开发静态共享包。
2.  在har中创建Worker线程文件相关内容。
```typescript
// worker.ets
workerPort.onmessage = (e: MessageEvents) => {
console.info("worker thread receive message: ", e.data);
workerPort.postMessage('worker thread post message to main thread');
}
```
3.  在entry模块的oh-package.json5文件中配置har包的依赖。
```typescript
// 在entry模块配置har包的依赖
{
"name": "entry",
"version": "1.0.0",
"description": "Please describe the basic information.",
"main": "",
"author": "",
"license": "",
"dependencies": {
"har": "file:../har"
}
}
```
4.  在entry模块中加载har包中的Worker线程文件。
```typescript
// Index.ets
import { worker } from '@kit.ArkTS';
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(() => {
// 通过@标识路径加载形式，加载har中Worker线程文件
let workerInstance = new worker.ThreadWorker('@har/ets/workers/worker.ets');
workerInstance.onmessage = () => {
console.info('main thread onmessage');
};
workerInstance.postMessage('hello world');
})
}
.height('100%')
.width('100%')
}
}
```
多级Worker生命周期管理
由于支持创建多级Worker（即通过父Worker创建子Worker的机制形成层级线程关系），且Worker线程生命周期由用户自行管理，因此需要注意多级Worker生命周期的正确管理。若用户销毁父Worker时未能结束其子Worker的运行，会产生不可预期的结果。建议用户确保子Worker的生命周期始终在父Worker生命周期范围内，并在销毁父Worker前先销毁所有子Worker。
推荐使用示例
```typescript
// 在主线程中创建Worker线程（父Worker），在worker线程中再次创建Worker线程（子Worker）
// main thread
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';
// 主线程中创建父worker对象
const parentworker = new worker.ThreadWorker("entry/ets/workers/parentworker.ets");
parentworker.onmessage = (e: MessageEvents) => {
console.info("主线程收到父worker线程信息 " + e.data);
}
parentworker.onexit = () => {
console.info("父worker退出");
}
parentworker.onerror = (err: ErrorEvent) => {
console.info("主线程接收到父worker报错 " + err);
}
parentworker.postMessage("主线程发送消息给父worker-推荐示例");
```
```typescript
// parentworker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
// 创建父Worker线程中与主线程通信的对象
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e : MessageEvents) => {
if (e.data == "主线程发送消息给父worker-推荐示例") {
let childworker = new worker.ThreadWorker("entry/ets/workers/childworker.ets");
childworker.onmessage = (e: MessageEvents) => {
console.info("父Worker收到子Worker的信息 " + e.data);
if (e.data == "子Worker向父Worker发送信息") {
workerPort.postMessage("父Worker向主线程发送信息");
}
}
childworker.onexit = () => {
console.info("子Worker退出");
// 子Worker退出后再销毁父Worker
workerPort.close();
}
childworker.onerror = (err: ErrorEvent) => {
console.info("子Worker发生报错 " + err);
}
childworker.postMessage("父Worker向子Worker发送信息-推荐示例");
}
}
```
```typescript
// childworker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
// 创建子Worker线程中与父Worker线程通信的对象
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
if (e.data == "父Worker向子Worker发送信息-推荐示例") {
// 子Worker线程业务逻辑...
console.info("业务执行结束，然后子Worker销毁");
workerPort.close();
}
}
```
不推荐使用示例
不建议父Worker主动销毁后，子Worker仍向父Worker发送消息。
```typescript
// main thread
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';
const parentworker = new worker.ThreadWorker("entry/ets/workers/parentworker.ets");
parentworker.onmessage = (e: MessageEvents) => {
console.info("主线程收到父Worker信息" + e.data);
}
parentworker.onexit = () => {
console.info("父Worker退出");
}
parentworker.onerror = (err: ErrorEvent) => {
console.info("主线程接收到父Worker报错 " + err);
}
parentworker.postMessage("主线程发送消息给父Worker");
```
```typescript
// parentworker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e : MessageEvents) => {
console.info("父Worker收到主线程的信息 " + e.data);
let childworker = new worker.ThreadWorker("entry/ets/workers/childworker.ets")
childworker.onmessage = (e: MessageEvents) => {
console.info("父Worker收到子Worker的信息 " + e.data);
}
childworker.onexit = () => {
console.info("子Worker退出");
workerPort.postMessage("父Worker向主线程发送信息");
}
childworker.onerror = (err: ErrorEvent) => {
console.info("子Worker发生报错 " + err);
}
childworker.postMessage("父Worker向子Worker发送信息");
// 创建子Worker后，销毁父Worker
workerPort.close();
}
```
```typescript
// childworker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
console.info("子Worker收到信息 " + e.data);
// 父Worker销毁后，子Worker向父Worker发送信息，行为不可预期
workerPort.postMessage("子Worker向父Worker发送信息");
setTimeout(() => {
workerPort.postMessage("子Worker向父Worker发送信息");
}, 1000);
}
```
不建议在明确父Worker发起销毁操作的同步调用前后仍在父Worker线程创建子Worker。不建议在不确定父Worker是否发起销毁操作的情况下，仍在父Worker线程创建子Worker，即创建子Worker线程成功之前需保证父Worker线程始终处于存活状态。
```typescript
// main thread
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';
const parentworker = new worker.ThreadWorker("entry/ets/workers/parentworker.ets");
parentworker.onmessage = (e: MessageEvents) => {
console.info("主线程收到父Worker信息" + e.data);
}
parentworker.onexit = () => {
console.info("父Worker退出");
}
parentworker.onerror = (err: ErrorEvent) => {
console.info("主线程接收到父Worker报错 " + err);
}
parentworker.postMessage("主线程发送消息给父Worker");
```
```typescript
// parentworker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e : MessageEvents) => {
console.info("父Worker收到主线程的信息 " + e.data);
// 父Worker销毁后创建子Worker，行为不可预期
workerPort.close();
let childworker = new worker.ThreadWorker("entry/ets/workers/childworker.ets");
// 子Worker线程未确认创建成功前销毁父Worker，行为不可预期
// let childworker = new worker.ThreadWorker("entry/ets/workers/childworker.ets");
// workerPort.close();
childworker.onmessage = (e: MessageEvents) => {
console.info("父Worker收到子Worker的信息 " + e.data);
}
childworker.onexit = () => {
console.info("子Worker退出");
workerPort.postMessage("父Worker向主线程发送信息");
}
childworker.onerror = (err: ErrorEvent) => {
console.info("子Worker发生报错 " + err);
}
childworker.postMessage("父Worker向子Worker发送信息");
}
```
```typescript
// childworker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
console.info("子Worker收到信息 " + e.data);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/taskpool-vs-worker-V14
爬取时间: 2025-04-27 22:50:08
来源: Huawei Developer
TaskPool（任务池）和Worker的作用是为应用程序提供一个多线程的运行环境，用于处理耗时的计算任务或其他密集型任务。可以有效地避免这些任务阻塞宿主线程，从而最大化系统的利用率，降低整体资源消耗，并提高系统的整体性能。
本文将从实现特点和适用场景两个方面来进行TaskPool与Worker的比较。
实现特点对比
表1TaskPool和Worker的实现特点对比
| 实现 | TaskPool | Worker |
| --- | --- | --- |
| 内存模型 | 线程间隔离，内存不共享。 | 线程间隔离，内存不共享。 |
| 参数传递机制 | 采用标准的结构化克隆算法（Structured Clone）进行序列化、反序列化，完成参数传递。 支持ArrayBuffer转移和SharedArrayBuffer共享。  | 采用标准的结构化克隆算法（Structured Clone）进行序列化、反序列化，完成参数传递。 支持ArrayBuffer转移和SharedArrayBuffer共享。  |
| 参数传递 | 直接传递，无需封装，默认进行transfer。 | 消息对象唯一参数，需要自己封装。 |
| 方法调用 | 直接将方法传入调用。 | 在Worker线程中进行消息解析并调用对应方法。 |
| 返回值 | 异步调用后默认返回。 | 主动发送消息，需在onmessage解析赋值。 |
| 生命周期 | TaskPool自行管理生命周期，无需关心任务负载高低。 | 开发者自行管理Worker的数量及生命周期。 |
| 任务池个数上限 | 自动管理，无需配置。 | 同个进程下，最多支持同时开启64个Worker线程，实际数量由进程内存决定。 |
| 任务执行时长上限 | 3分钟（不包含Promise和async/await异步调用的耗时，例如网络下载、文件读写等I/O任务的耗时），长时任务无执行时长上限。 | 无限制。 |
| 设置任务的优先级 | 支持配置任务优先级。 | 不支持。 |
| 执行任务的取消 | 支持取消已经发起的任务。 | 不支持。 |
| 线程复用 | 支持。 | 不支持。 |
| 任务延时执行 | 支持。 | 不支持。 |
| 设置任务依赖关系 | 支持。 | 不支持。 |
| 串行队列 | 支持。 | 不支持。 |
| 任务组 | 支持。 | 不支持。 |
采用标准的结构化克隆算法（Structured Clone）进行序列化、反序列化，完成参数传递。
支持ArrayBuffer转移和SharedArrayBuffer共享。
采用标准的结构化克隆算法（Structured Clone）进行序列化、反序列化，完成参数传递。
支持ArrayBuffer转移和SharedArrayBuffer共享。
适用场景对比
TaskPool和Worker均支持多线程并发能力。由于TaskPool的工作线程会绑定系统的调度优先级，并且支持负载均衡（自动扩缩容），而Worker需要开发者自行创建，存在创建耗时以及不支持设置调度优先级，故在性能方面使用TaskPool会优于Worker，因此大多数场景推荐使用TaskPool。
TaskPool偏向独立任务维度，该任务在线程中执行，无需关注线程的生命周期，超长任务（大于3分钟且非长时任务）会被系统自动回收；而Worker偏向线程的维度，支持长时间占据线程执行，需要主动管理线程生命周期。
常见的一些开发场景及适用具体说明如下：
-  运行时间超过3分钟（不包含Promise和async/await异步调用的耗时，例如网络下载、文件读写等I/O任务的耗时）的任务。例如后台进行1小时的预测算法训练等CPU密集型任务，需要使用Worker。场景示例可参考常驻任务开发指导。
-  有关联的一系列同步任务。例如在一些需要创建、使用句柄的场景中，句柄创建每次都是不同的，该句柄需永久保存，保证使用该句柄进行操作，需要使用Worker。场景示例可参考使用Worker处理关联的同步任务。
-  需要设置优先级的任务。例如图库直方图绘制场景，后台计算的直方图数据会用于前台界面的显示，影响用户体验，需要高优先级处理，需要使用TaskPool。
-  需要频繁取消的任务。例如图库大图浏览场景，为提升体验，会同时缓存当前图片左右侧各2张图片，往一侧滑动跳到下一张图片时，要取消另一侧的一个缓存任务，需要使用TaskPool。
-  大量或者调度点较分散的任务。例如大型应用的多个模块包含多个耗时任务，不方便使用Worker去做负载管理，推荐采用TaskPool。场景示例可参考批量数据写数据库场景。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/interthead-communication-V14
爬取时间: 2025-04-27 22:50:22
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/interthread-communication-overview-V14
爬取时间: 2025-04-27 22:50:36
来源: Huawei Developer
线程间通信指的是并发多线程间存在的数据交换行为。由于ArkTS语言兼容TS/JS，其运行时的实现与其它所有的JS引擎一样，都是基于Actor内存隔离的并发模型提供并发能力。
对于不同的数据对象，在ArkTS线程间通信的行为是有差异的，比如普通JS对象、ArrayBuffer对象、SharedArrayBuffer对象等，跨线程的行为是不一致的，包括序列化反序列化拷贝、数据转移、数据共享等不同行为。
以JS对象为例，其在并发任务间的通信采用了标准的Structure Clone算法（序列化反序列化），通过序列化将JS对象转成与引擎无关的数据（字符串或内存块等），在另一个并发实例通过反序列化，还原成与原JS对象内容一致的新对象，因此通常需要经过深拷贝，效率较低。除了支持JS标准的序列化反序列化能力外，还支持绑定Native的JS对象传输及Sendable对象的共享能力。
ArkTS目前主要提供两种并发能力支持线程间通信：TaskPool和Worker。
-  Worker是Actor并发模型标准的跨线程通信API，与Web Worker或者Node.js Worker的使用方式基本一致。
-  TaskPool提供了功能更强、并发编程更简易的任务池API。其中TaskPool涉及跨并发实例的对象传递行为与Worker一致，还是采用了标准的Structured Clone算法，并发通信的对象越大，耗时就越长。
基于ArkTS提供的TaskPool及Worker并发接口，支持多种线程间通信能力，可以满足开发者的不同线程间通信场景。比如：独立的耗时任务场景、多个耗时任务场景、TaskPool线程与宿主线程通信场景、Worker线程和宿主线程的异步通信场景、Worker同步调用宿主线程的接口等场景。同时，基于Node-API提供的机制，支持C++线程跨线程调用ArkTS接口。
图1 序列化反序列化原理图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170231.62479251824107753926010159571529:50001231000000:2800:3F62306711FBF27BE7492B5402ADB3C30BE9035B91A9BCB9E8F64FA8E918EC2C.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/interthead-communication-object-V14
爬取时间: 2025-04-27 22:50:49
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/normal-object-V14
爬取时间: 2025-04-27 22:51:03
来源: Huawei Developer
普通对象跨线程时通过拷贝形式传递，两个线程的对象内容一致，但是指向各自线程的隔离内存区间，被分配在各自线程的虚拟机本地堆（LocalHeap）。例如Ecmascript262规范定义的Object、Array、Map等对象是通过这种方式实现跨并发实例通信的。通信过程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170231.19645765597291215706686267652548:50001231000000:2800:89B5958928C5FE05131FE5E97EC69700686D8C65B229527F10A3F9656E5D2B0A.png)
普通类实例对象跨线程通过拷贝形式传递，只能传递数据，类实例上的方法会丢失。可以使用@Sendable装饰器标识为Sendable类，类实例对象跨线程传递后，可携带类方法。
使用示例
此处提供了一个传递普通对象的简单示例，具体实现如下：
```typescript
// Test.ets
// 自定义class TestA
export class TestA {
constructor(name: string) {
this.name = name;
}
name: string = 'ClassA';
}
```
```typescript
// Index.ets
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { TestA } from './Test';
@Concurrent
async function test1(arg: TestA) {
console.info("TestA name is: " + arg.name);
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(() => {
// 1. 创建Test实例objA
let objA = new TestA("TestA");
// 2. 创建任务task，将objA传递给该任务，objA非sendable对象，通过序列化传递给子线程
let task = new taskpool.Task(test1, objA);
// 3. 执行任务
taskpool.execute(task).then(() => {
console.info("taskpool: execute task success!");
}).catch((e:BusinessError) => {
console.error(`taskpool: execute task: Code: ${e.code}, message: ${e.message}`);
})
})
}
.height('100%')
.width('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arraybuffer-object-V14
爬取时间: 2025-04-27 22:51:16
来源: Huawei Developer
ArrayBuffer内部包含一块Native内存，该ArrayBuffer的JS对象壳被分配在虚拟机本地堆（LocalHeap）。与普通对象一样，需要经过序列化与反序列化拷贝传递，但是Native内存有两种传输方式：拷贝和转移。
传输时采用拷贝的话，需要经过深拷贝（递归遍历），传输后两个线程都可以独立访问ArrayBuffer。通信过程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170231.56414194003720486227783260020446:50001231000000:2800:20CCFDFE8B62D146B342681AAA823A05D7780F464772296472091BC2D7D1C18E.png)
如果采用转移的方式，则原线程无法使用此ArrayBuffer对象，跨线程时只需重建JS壳，Native内存无需拷贝，效率更高。通信过程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170231.40594296014992194402484648603255:50001231000000:2800:E0C940D9B87D44F77EC208F5B8FB639D7796A8840DD7087DF48CEF62C51DD2D6.png)
ArrayBuffer可以用来表示图片等资源，在应用开发中，会遇到需要进行图片处理的场景（比如需要调整一张图片的亮度、饱和度、大小等），为了避免阻塞UI主线程，可以将图片传递到子线程中执行这些操作。转移方式性能更高，但是原线程不能再访问ArrayBuffer对象，如果两个线程都需要访问，则需要采用拷贝方式，否则建议采用转移方式，提升性能。
下面将分别通过拷贝和转移的方式，将图片传递到子线程中。
ArrayBuffer拷贝传输方式
在ArkTS中，TaskPool传递ArrayBuffer数据时，默认使用转移的方式，通过调用setTransferList()接口，指定对应的部分数据传递方式为转移方式，其余部分数据可以切换成拷贝的方式。
首先，实现一个需要在Task中执行的用于处理ArrayBuffer的接口。
然后，通过拷贝的方式将ArrayBuffer数据传递到Task中，并在Task中处理ArrayBuffer。
最后，UI主线程接收到Task执行完毕后返回的ArrayBuffer数据，拼接数据展示。
```typescript
// Index.ets
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
@Concurrent
function adjustImageValue(arrayBuffer: ArrayBuffer): ArrayBuffer {
// 对arrayBuffer进行操作
return arrayBuffer;  // 返回值默认转移
}
function createImageTask(arrayBuffer: ArrayBuffer, isParamsByTransfer: boolean): taskpool.Task {
let task: taskpool.Task = new taskpool.Task(adjustImageValue, arrayBuffer);
if (!isParamsByTransfer) { // 是否使用转移方式
// 传递空数组[]，全部arrayBuffer参数传递均采用拷贝方式
task.setTransferList([]);
}
return task;
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(() => {
let taskNum = 4;
let arrayBuffer = new ArrayBuffer(1024 * 1024);
let taskPoolGroup = new taskpool.TaskGroup();
// 创建taskNum个Task
for (let i: number = 0; i < taskNum; i++) {
let arrayBufferSlice: ArrayBuffer = arrayBuffer.slice(arrayBuffer.byteLength / taskNum * i, arrayBuffer.byteLength / taskNum * (i + 1));
// 使用拷贝方式传入ArrayBuffer，所以isParamsByTransfer为false
taskPoolGroup.addTask(createImageTask(arrayBufferSlice, false));
}
// 执行Task
taskpool.execute(taskPoolGroup).then((data) => {
// 返回结果，对数组拼接，获得最终结果
}).catch((e: BusinessError) => {
console.error(e.message);
})
})
}
.height('100%')
.width('100%')
}
}
```
ArrayBuffer转移传输方式
在TaskPool中，传递ArrayBuffer数据，默认使用转移方式，原线程不能再使用传输给子线程的ArrayBuffer。所以在上文示例的基础上，去除task.setTransferList接口就可以实现，即createImageTask第二个参数传入true。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/shared-arraybuffer-object-V14
爬取时间: 2025-04-27 22:51:30
来源: Huawei Developer
SharedArrayBuffer内部包含一块Native内存，其JS对象壳被分配在虚拟机本地堆（LocalHeap）。支持跨并发实例间共享，但是访问及修改需要采用Atomics类，防止数据竞争。SharedArrayBuffer可以用于多个并发实例间的状态共享或者数据共享。通信过程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170231.64757822499961364997829917275118:50001231000000:2800:97615663C8B8CF6C48B4A200FCAEE83474A756449B678C709963569919D9BC3E.png)
使用示例
这里提供了一个简单示例，使用TaskPool传递一个Int32Array对象，具体实现如下：
```typescript
import { taskpool } from '@kit.ArkTS';
@Concurrent
function transferAtomics(arg1: Int32Array) {
console.info("wait begin::");
// 使用Atomics进行操作
let res = Atomics.wait(arg1, 0, 0, 3000);
return res;
}
// 定义可共享对象
let sab: SharedArrayBuffer = new SharedArrayBuffer(20);
let int32 = new Int32Array(sab);
let task: taskpool.Task = new taskpool.Task(transferAtomics, int32);
taskpool.execute(task).then((res) => {
console.info("this res is: " + res);
});
setTimeout(() => {
Atomics.notify(int32, 0, 1);
}, 1000);
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/transferabled-object-V14
爬取时间: 2025-04-27 22:51:43
来源: Huawei Developer
Transferable对象（也称为NativeBinding对象）指的是一个JS对象，绑定了一个C++对象，且主体功能由C++提供，其JS对象壳被分配在虚拟机本地堆（LocalHeap）。跨线程传输时可以直接复用同一个C++对象，相比于JS对象的拷贝模式，传输效率较高。因此，可共享或转移的NativeBinding对象也被称为Transferable对象。
共享模式
如果C++实现能够保证线程安全性，则这个NativeBinding对象的C++部分可以支持共享传输。此时，NativeBinding对象跨线程传输后，只需要重新创建JS壳，就可以桥接到相同的C++对象上。通信过程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170231.26669041651302077469969241484861:50001231000000:2800:945C3901EFF7A281F790313E1D85FED02ADD4FBE1B0318C77668696BDBA9340B.png)
常见的共享模式NativeBinding对象包括Context，Context对象包含应用程序组件的上下文信息，它提供了一种访问系统服务和资源的方式，使得应用程序组件可以与系统进行交互。获取Context信息的方法可以参考获取上下文信息。
示例可参考使用TaskPool进行频繁数据库操作。
转移模式
如果C++实现包含了数据，且无法保证线程安全性，则这个NativeBinding对象的C++部分需要采用转移方式传输。此时，NativeBinding对象跨线程传输后，只需要重新创建JS壳，就可以桥接到C++对象上，不过原对象需要移除对此对象的绑定关系。通信过程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170231.83161844108144055563949634709044:50001231000000:2800:1C1A11C2E650561FB66BF8597B74E211043290AF704E9B1DB08DD1D1DCF36CD9.png)
常见的转移模式NativeBinding对象包括PixelMap，PixelMap对象可以读取或写入图像数据以及获取图像信息，常用于在应用或系统中显示图片。
使用示例
这里提供了一个跨线程传递PixelMap对象的示例以帮助更好理解。首先获取rawfile文件夹中的图片资源，然后在子线程中创建PixelMap对象传递给主线程，具体实现如下：
```typescript
// Index.ets
import { taskpool } from '@kit.ArkTS';
import { loadPixelMap } from './pixelMapTest';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
@State pixelMap: PixelMap | undefined = undefined;
private loadImageFromThread(): void {
const resourceMgr = getContext(this).resourceManager;
// 此处‘startIcon.png’为media下复制到rawfile文件夹中，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
resourceMgr.getRawFd('startIcon.png').then(rawFileDescriptor => {
taskpool.execute(loadPixelMap, rawFileDescriptor).then(pixelMap => {
if (pixelMap) {
this.pixelMap = pixelMap as PixelMap;
console.log('Succeeded in creating pixelMap.');
// 主线程释放pixelMap。由于子线程返回pixelMap时已调用setTransferDetached，所以此处能够立即释放pixelMap。
this.pixelMap.release();
} else {
console.error('Failed to create pixelMap.');
}
}).catch((e: BusinessError) => {
console.error('taskpool execute loadPixelMap failed. Code: ' + e.code + ', message: ' + e.message);
});
});
}
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: 'container', align: VerticalAlign.Center },
middle: { anchor: 'container', align: HorizontalAlign.Center }
})
.onClick(() => {
this.loadImageFromThread();
})
}
.height('100%')
.width('100%')
}
}
```
```typescript
// pixelMapTest.ets
import { image } from '@kit.ImageKit';
@Concurrent
export async function loadPixelMap(rawFileDescriptor: number): Promise<PixelMap> {
// 创建imageSource。
const imageSource = image.createImageSource(rawFileDescriptor);
// 创建pixelMap。
const pixelMap = imageSource.createPixelMapSync();
// 释放imageSource。
imageSource.release();
// 使pixelMap在跨线程传输完成后，断开原线程的引用。
pixelMap.setTransferDetached(true);
// 返回pixelMap给主线程。
return pixelMap;
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/sendable-object-V14
爬取时间: 2025-04-27 22:51:57
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-sendable-V14
爬取时间: 2025-04-27 22:52:11
来源: Huawei Developer
在传统JS引擎上，对象的并发通信开销的优化方式只有一种，就是把实现下沉到Native侧，通过Transferable对象的转移或共享方式降低并发通信开销。而开发者仍然还有大量对象并发通信的诉求，这个问题在业界的JS引擎实现上并没有得到解决。
ArkTS提供了Sendable对象类型，在并发通信时支持通过引用传递来解决上述问题。
Sendable对象为可共享的，其跨线程前后指向同一个JS对象，如果其包含了JS或者Native内容，均可以直接共享，如果底层是Native实现的，则需要考虑线程安全性。通信过程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170232.80636722682008485561906678362593:50001231000000:2800:01809A63A9ECEAC9E85DD162B9A2677DB9290C3219AFE8E7AD80AAAFA3851591.png)
与其它ArkTS对象不一样的是，符合Sendable协议的数据对象在运行时必须是类型固定的对象。
当多个并发实例尝试同时更新Sendable数据时，会发生数据竞争，例如ArkTS共享容器的多线程操作。因此，ArkTS提供了异步锁的机制来避免不同并发实例间的数据竞争。同时，还可以通过对象冻结接口冻结对象，将其变为只读对象，就可以不用考虑数据的竞争问题。
Sendable对象提供了并发实例间高效的通信效率，即引用传递的能力，一般适用于开发者自定义大对象需要线程间通信的场景，例如子线程读取数据库的数据返回宿主线程。
基础概念
Sendable协议
Sendable协议定义了ArkTS的可共享对象体系及其规格约束。符合Sendable协议的数据（以下简称Sendable对象）可以在ArkTS并发实例间传递。
默认情况下，Sendable数据在ArkTS并发实例间（包括UI主线程、TaskPool线程、Worker线程）传递的行为是引用传递。同时，ArkTS也支持Sendable数据在ArkTS并发实例间拷贝传递。
ISendable
在ArkTS语言基础库@arkts.lang中引入了interface ISendable，没有任何必须的方法或属性。ISendable是所有Sendable类型（除了null和undefined）的父类型。ISendable主要用在开发者自定义Sendable数据结构的场景中。类装饰器@Sendable装饰器是implement ISendable的语法糖。
Sendable class
从API version 11开始，支持使用@Sendable装饰器校验Sendable class。
Sendable class需同时满足以下两个规则：
1.  当且仅当被标注了@Sendable装饰器。
2.  需满足Sendable约束，详情可查Sendable使用规则。
Sendable function
Sendable function需同时满足以下两个规则：
1.  当且仅当被标注了@Sendable装饰器。
2.  需满足Sendable约束，详情可查Sendable使用规则。
Sendable interface
Sendable interface需同时满足以下两个规则：
1.  当且仅当是ISendable或者继承了ISendable。
2.  需满足Sendable约束，详情可查Sendable使用规则。
Sendable支持的数据类型
-  所有的ArkTS基本数据类型：boolean, number, string, bigint, null, undefined。
-  ArkTS语言标准库中定义的容器类型数据（须显式引入@arkts.collections）。
-  ArkTS语言标准库中定义的异步锁对象（须显式引入@arkts.utils）。
-  继承了ISendable的interface。
-  标注了@Sendable装饰器的class。
-  标注了@Sendable装饰器的function。
-  接入Sendable的系统对象。
-  元素均为Sendable类型的union type数据。
-  JS内置对象在并发实例间的传递遵循结构化克隆算法，跨线程行为是拷贝传递。因此JS内置对象的实例不是Sendable类型。
-  对象字面量、数组字面量在并发实例间的传递遵循结构化克隆算法，跨线程行为是拷贝传递。因此，对象字面量和数组字面量不是Sendable类型。
Sendable的实现原理
为了实现Sendable数据在不同并发实例间的引用传递，Sendable共享对象会分配在共享堆中，以实现跨并发实例的内存共享。
共享堆（SharedHeap）是进程级别的堆空间，与虚拟机本地堆（LocalHeap）不同的是，LocalHeap只能被单个并发实例访问，而SharedHeap可以被所有线程访问。一个Sendable共享对象的跨线程行为是引用传递。因此，Sendable可能被多个并发实例引用，判断Sendable共享对象是否存活，取决于所有并发实例的对象是否存在对此Sendable共享对象的引用。
SharedHeap与LocalHeap关系图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170232.43747853943848763477821903450128:50001231000000:2800:D5D6BDC4C1F7C332228F0B57C6934133E450F6E77B6682D40539B4A7386DD41E.png)
各个并发实例间的LocalHeap是隔离的，SharedHeap是进程级别的堆，可以被所有的并发实例引用。但是SharedHeap不能引用LocalHeap中的对象。
@Sendable装饰器
声明并校验Sendable class以及Sendable function。
| @Sendable装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 使用场景限制 | 仅支持在Stage模型的工程中使用。仅支持在.ets文件中使用。 |
| 装饰的函数类型限制 | 仅支持装饰普通function和Async function类型。 |
| 装饰的类继承关系限制 | Sendable class只能继承Sendable class，普通Class不可以继承Sendable class。 |
| 装饰的对象内的属性类型限制 | 1. 支持string、number、boolean、bigint、null、undefined、Sendable class、collections.Array、collections.Map、collections.Set、ArkTSUtils.locks.AsyncLock。 2. 禁止使用闭包变量。 3. 不支持通过#定义私有属性，需用private。 4. 不支持计算属性。 |
| 装饰的对象内的属性的其他限制 | 成员属性必须显式初始化。成员属性不能跟感叹号。 |
| 装饰的函数或类对象内的方法参数限制 | 允许使用local变量、入参和通过import引入的变量。禁止使用闭包变量，定义在顶层的Sendable class和Sendable function除外。 |
| Sendable Class及Sendable Function的限制 | 不支持增加属性、不支持删除属性、允许修改属性，修改前后属性的类型必须一致、不支持修改方法。 |
| 适用场景 | 1. 在TaskPool或Worker中使用类方法/Sendable函数。 2. 传输对象数据量较大的使用场景。序列化耗时会随着数据量增大而增大，使用Sendable对数据改造后传输100KB数据时效率提升约20倍，传输1M数据时效率提升约100倍。 |
1. 支持string、number、boolean、bigint、null、undefined、Sendable class、collections.Array、collections.Map、collections.Set、ArkTSUtils.locks.AsyncLock。
2. 禁止使用闭包变量。
3. 不支持通过#定义私有属性，需用private。
4. 不支持计算属性。
1. 在TaskPool或Worker中使用类方法/Sendable函数。
2. 传输对象数据量较大的使用场景。序列化耗时会随着数据量增大而增大，使用Sendable对数据改造后传输100KB数据时效率提升约20倍，传输1M数据时效率提升约100倍。
装饰器修饰Class使用示例：
```typescript
@Sendable
class SendableTestClass {
desc: string = "sendable: this is SendableTestClass ";
num: number = 5;
printName() {
console.info("sendable: SendableTestClass desc is: " + this.desc);
}
get getNum(): number {
return this.num;
}
}
```
装饰器修饰Function使用示例：
```typescript
@Sendable
type SendableFuncType = () => void;
@Sendable
class TopLevelSendableClass {
num: number = 1;
PrintNum() {
console.info("Top level sendable class");
}
}
@Sendable
function TopLevelSendableFunction() {
console.info("Top level sendable function");
}
@Sendable
function SendableTestFunction() {
const topClass = new TopLevelSendableClass(); // 顶层sendable class
topClass.PrintNum();
TopLevelSendableFunction(); // 顶层sendable function
console.info("Sendable test function");
}
@Sendable
class SendableTestClass {
constructor(func: SendableFuncType) {
this.callback = func;
}
callback: SendableFuncType; // 顶层sendable function
CallSendableFunc() {
SendableTestFunction(); // 顶层sendable function
}
}
let sendableClass = new SendableTestClass(SendableTestFunction);
sendableClass.callback();
sendableClass.CallSendableFunc();
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/sendable-constraints-V14
爬取时间: 2025-04-27 22:52:25
来源: Huawei Developer
Sendable class只能继承自Sendable class
Sendable对象布局及原型链不可变，非Sendable对象可以通过特殊方式修改布局，不允许互相继承。这里的class不包括变量。Sendable class不能继承自变量。
正例：
```typescript
@Sendable
class A {
constructor() {
}
}
@Sendable
class B extends A {
constructor() {
super()
}
}
```
反例：
```typescript
class A {
constructor() {
}
}
@Sendable
class B extends A {
constructor() {
super()
}
}
```
非Sendable class只能继承自非Sendable class
Sendable对象布局及原型链不可变，由于非Sendable对象可以通过特殊方式修改布局，因此不允许互相继承。
正例：
```typescript
class A {
constructor() {
}
}
class B extends A {
constructor() {
super()
}
}
```
反例：
```typescript
@Sendable
class A {
constructor() {
}
}
class B extends A {
constructor() {
super()
}
}
```
非Sendable class只能实现非Sendable interface
如果非Sendable class实现了Sendable interface，可能会被认为是Sendable的，实际是非Sendable的，导致错误使用。
正例：
```typescript
interface I {};
class B implements I {};
```
反例：
```typescript
import { lang } from '@kit.ArkTS';
type ISendable = lang.ISendable;
interface I extends ISendable {};
class B implements I {};
```
Sendable class/interface成员变量必须是Sendable支持的数据类型
Sendable数据不能持有非Sendable数据，因此Sendable数据的成员属性必须为Sendable数据。
正例：
```typescript
@Sendable
class A {
constructor() {
}
a: number = 0;
}
```
反例：
```typescript
@Sendable
class A {
constructor() {
}
b: Array<number> = [1, 2, 3] // 需使用collections.Array
}
```
Sendable class/interface的成员变量不支持使用!断言
Sendable对象的成员属性必须赋初值，“!”修饰的变量可以不赋初值，因此不支持使用“!” 。
正例：
```typescript
@Sendable
class A {
constructor() {
}
a: number = 0;
}
```
反例：
```typescript
@Sendable
class A {
constructor() {
}
a!: number;
}
```
Sendable class/interface的成员变量不支持使用计算属性名
Sendable对象的布局不可变，计算属性不能静态确定对象布局，因此不支持。
正例：
```typescript
@Sendable
class A {
num1: number = 1;
num2: number = 2;
add(): number {
return this.num1 + this.num2;
}
}
```
反例：
```typescript
enum B {
b1 = "bbb"
}
@Sendable
class A {
["aaa"]: number = 1; // ["aaa"] is allowed in other classes in ets files
[B.b1]: number = 2; // [B.b1] is allowed in other classes in ets files
}
```
泛型类中的Sendable class，collections.Array，collections.Map，collections.Set的模板类型必须是Sendable类型
Sendable数据不能持有非Sendable数据，因此泛型类中的Sendable数据的模版类型必须是Sendable类型。
正例：
```typescript
import { collections } from '@kit.ArkTS';
try {
let arr1: collections.Array<number> = new collections.Array<number>();
let num: number = 1;
arr1.push(num);
} catch (e) {
console.error(`taskpool execute: Code: ${e.code}, message: ${e.message}`);
}
```
反例：
```typescript
import { collections } from '@kit.ArkTS';
try {
let arr1: collections.Array<Array<number>> = new collections.Array<Array<number>>();
let arr2: Array<number> = new Array<number>();
arr2.push(1);
arr1.push(arr2);
} catch (e) {
console.error(`taskpool execute: Code: ${e.code}, message: ${e.message}`);
}
```
Sendable class的内部不允许使用当前模块内上下文环境中定义的变量
由于Sendable对象在不同并发实例间的上下文环境不同，属于单个虚拟机实例，如果直接访问会有非预期行为。不支持Sendable对象使用当前模块内上下文环境中定义的变量，如果违反，编译阶段会报错。
从API version 12开始，sendable class的内部支持使用top level的sendable class对象。
正例：
```typescript
import { lang } from '@kit.ArkTS';
type ISendable = lang.ISendable;
interface I extends ISendable {}
@Sendable
class B implements I {
static o: number = 1;
static bar(): B {
return new B();
}
}
@Sendable
class C {
v: I = new B();
u: number = B.o;
foo() {
return B.bar();
}
}
```
反例：
```typescript
import { lang } from '@kit.ArkTS';
type ISendable = lang.ISendable;
interface I extends ISendable {}
@Sendable
class B implements I {}
function bar(): B {
return new B();
}
let b = new B();
{
@Sendable
class A implements I {}
@Sendable
class C {
u: I = bar(); // bar不是sendable class对象，编译报错
v: I = new A(); // A不是定义在top level中，编译报错
foo() {
return b; // b不是sendable class对象，而是sendable class的实例，编译报错
}
}
}
```
Sendable class和Sendable function不能使用除了@Sendable的其它装饰器
如果类装饰器定义在ts文件中，产生修改类的布局的行为，那么会造成运行时的错误。
正例：
```typescript
@Sendable
class A {
num: number = 1;
}
```
反例：
```typescript
@Sendable
@Observed
class C {
num: number = 1;
}
```
不能使用对象字面量/数组字面量初始化Sendable类型
对象字面量/数组字面量是非Sendable类型，Sendable数据类型只能通过Sendable类型的new表达式创建。
正例：
```typescript
import { collections } from '@kit.ArkTS';
let arr1: collections.Array<number> = new collections.Array<number>(1, 2, 3); // 是Sendable类型
```
反例：
```typescript
import { collections } from '@kit.ArkTS';
let arr2: collections.Array<number> = [1, 2, 3]; // 不是Sendable类型，编译报错
let arr3: number[] = [1, 2, 3]; // 不是Sendable类型，正例，不报错
let arr4: number[] = new collections.Array<number>(1, 2, 3); // 编译报错
```
非Sendable类型不可以as成Sendable类型
除了Object类型，非Sendable类型不可以as成Sendable类型。非Sendable类型通过as强转成Sendable类型后实际是非Sendable的类型数据，会导致错误使用。Sendable类型在不违反Sendable规则的前提下需要和非Sendable类型行为兼容，因此Sendable类型可以as成非Sendable类型。
正例：
```typescript
class A {
state: number = 0;
}
@Sendable
class SendableA {
state: number = 0;
}
let a1: A = new SendableA() as A;
```
反例：
```typescript
class A {
state: number = 0;
}
@Sendable
class SendableA {
state: number = 0;
}
let a2: SendableA = new A() as SendableA;
```
箭头函数不支持共享
箭头函数不支持使用Sendable装饰器，是非Sendable函数，因此不支持共享。
正例：
```typescript
@Sendable
type SendableFuncType = () => void;
@Sendable
function SendableFunc() {
console.info("Sendable func");
}
@Sendable
class SendableClass {
constructor(f: SendableFuncType) {
this.func = f;
}
func: SendableFuncType;
}
let sendableClass = new SendableClass(SendableFunc);
```
反例：
```typescript
@Sendable
type SendableFuncType = () => void;
let func: SendableFuncType = () => {}; // 编译报错
@Sendable
class SendableClass {
func: SendableFuncType = () => {}; // 编译报错
}
```
Sendable装饰器修饰类型时仅支持修饰函数类型
当前仅支持声明Sendable函数类型，因此只能修饰函数类型。
正例：
```typescript
@Sendable
type SendableFuncType = () => void;
```
反例：
```typescript
@Sendable
type A = number; // 编译报错
@Sendable
class C {}
@Sendable
type D = C; // 编译报错
```
注意事项
在HAR中使用Sendable时，需开启编译生成TS文件的配置。详情可查编译生成TS文件。
与TS/JS交互的规则
ArkTS通用规则（目前只针对Sendable对象）
| 规则 |
| --- |
| Sendable对象传入TS/JS的接口中，禁止操作其对象布局（增、删属性，改变属性类型）。 |
| Sendable对象设置到TS/JS的对象上，TS中获取到这个Sendable对象后，禁止操作其对象布局（增、删属性，改变属性类型）。 |
| Sendable对象放入TS/JS的容器中，TS中获取到这个Sendable对象后，禁止操作其对象布局（增、删属性，改变属性类型）。 |
此处改变属性类型不包括Sendable对象类型的改变，比如从Sendable class A 变为Sendable class B。
NAPI规则（目前只针对Sendable对象）
| 规则 |
| --- |
| 禁止删除属性，不能使用的接口有：napi_delete_property。 |
| 禁止新增属性，不能使用的接口有：napi_set_property、napi_set_named_property、napi_define_properties。 |
| 禁止修改属性类型，不能使用的接口有：napi_set_property、napi_set_named_property、napi_define_properties。 |
| 不支持Symbol相关接口和类型，不能使用的接口有：napi_create_symbol、napi_is_symbol_object、napi_symbol。 |
与UI交互的规则
Sendable数据需要与makeObserved联用，才可以观察Sendable对象的数据变化，具体使用请参考makeObserved和@Sendable装饰的class配合文档。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-async-lock-introduction-V14
爬取时间: 2025-04-27 22:52:38
来源: Huawei Developer
为了解决多线程并发任务间的数据竞争问题，ArkTS引入了异步锁能力。异步锁可能会被类对象持有，因此为了更方便地在并发实例间获取同一个异步锁对象，AsyncLock对象支持跨线程引用传递。
由于ArkTS语言支持异步操作，阻塞锁容易产生死锁问题，因此在ArkTS中仅支持异步锁（非阻塞式锁）。同时，异步锁还可以用于保证单线程内的异步任务时序一致性，防止异步任务时序不确定导致的同步问题。
更多异步锁相关接口，可见异步锁ArkTSUtils.locks。
使用异步锁的方法需要标记为async，调用方需要使用await修饰，才能保证时序正确。
使用示例
为了解决@Sendable共享对象在不同线程修改共享变量导致的竞争问题，可以采用异步锁进行数据保护。示例如下：
```typescript
import { ArkTSUtils, taskpool } from '@kit.ArkTS';
@Sendable
export class A {
private count_: number = 0;
lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();
public async getCount(): Promise<number> {
// 对需要保护的数据加异步锁
return this.lock_.lockAsync(() => {
return this.count_;
})
}
public async increaseCount() {
// 对需要保护的数据加异步锁
await this.lock_.lockAsync(() => {
this.count_++;
})
}
}
@Concurrent
async function printCount(a: A) {
console.info("InputModule: count is:" + await a.getCount());
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
// 创建sendable对象a
let a: A = new A();
// 将实例a传递给子线程
await taskpool.execute(printCount, a);
})
}
.height('100%')
.width('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ason-parsing-generation-V14
爬取时间: 2025-04-27 22:52:52
来源: Huawei Developer
ASON工具与JS提供的JSON工具类似，JSON用于进行JS对象的序列化（stringify）、反序列化（parse）。ASON则提供了Sendable对象的序列化、反序列化能力。可以通过ASON.stringify方法将对象转换成字符串，也可以通过ASON.parse方法将字符串转成Sendable对象，以便此对象在并发任务间进行高性能引用传递。
ASON.parse默认生成的对象为Sendable对象，布局不可变，不支持增删属性。如果需要支持返回对象的布局可变，可以指定返回类型为MAP，此时会全部返回collections.Map对象，支持增删属性。
使用示例
采用ASON提供的接口，对Sendable对象进行序列化、反序列化。
```typescript
import { ArkTSUtils, collections } from '@kit.ArkTS';
ArkTSUtils.ASON.parse("{}")
ArkTSUtils.ASON.stringify(new collections.Array(1, 2, 3))
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-collections-introduction-V14
爬取时间: 2025-04-27 22:53:05
来源: Huawei Developer
ArkTS容器集
ArkTS共享容器（@arkts.collections (ArkTS容器集)）是一种在并发任务间共享传输的容器类，可以用于并发场景下的高性能数据传递。功能与Ecmascript262规范定义的容器类似，但仍然有部分差异，具体可见共享容器与原生API方法的行为差异对比。
ArkTS共享容器在多个并发任务间传递时，其默认行为是引用传递，支持多个并发任务可以操作同一个容器实例。另外，也支持拷贝传递，即每个并发任务持有一个ArkTS容器实例。
ArkTS共享容器并不是线程安全的，内部使用了fail-fast（快速失败）机制，即当检测多个并发实例同时对容器进行结构性改变时，会触发异常。因此，在容器内修改属性的场景下，开发者需要使用ArkTS提供的异步锁机制保证ArkTS容器的安全访问。
ArkTS共享容器包含如下几种：Array、Map、Set、TypedArray（Int8Array、Uint8Array、Int16Array、Uint16Array、Int32Array、Uint32Array、Uint8ClampedArray、Float32Array）、ArrayBuffer等，具体可见@arkts.collections (ArkTS容器集)。
容器集使用示例如下：
```typescript
import { ArkTSUtils, collections, taskpool } from '@kit.ArkTS';
@Concurrent
async function add(arr: collections.Array<number>, lock: ArkTSUtils.locks.AsyncLock) {
await lock.lockAsync(() => {  // 如果不添加异步锁，任务会因为数据竞争冲突，导致抛异常失败
arr[0]++;
})
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(() => {
let taskGroup = new taskpool.TaskGroup();
let lock = new ArkTSUtils.locks.AsyncLock();
let arr = collections.Array.create<number>(1, 0);
let count = 1000;
while (count--) {
taskGroup.addTask(add, arr, lock);
}
taskpool.execute(taskGroup).then(() => {
console.info(`Return success: ${arr[0]} === ${count}`);
}).catch((e: Error) => {
console.error("Return error.");
})
})
}
.height('100%')
.width('100%')
}
}
```
共享容器与原生API方法的行为差异对比
ArkTS提供了Sendable数据相关的共享容器集，接口行为与原生API存在部分差异，具体可见下文对比。
ArkTS共享容器的类型与Ecmascript262规范定义的原生容器的类型不一致，因此采用原生容器Array的isArray()方法判断collections.Array实例对象会返回false。
Array
支持原生容器Array通过collections.Array.from方法转换为ArkTS Array容器；支持通过原生容器Array的from方法将ArkTS Array容器转换为原生容器Array。
| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| length: number | readonly length: number | 是 | 为了防止undefined扩散，不允许设置length。 |
| new(arrayLength ?: number): any[] | static create(arrayLength: number, initialValue: T): Array | 是 | 为了防止undefined扩散，构造函数中必须提供一个初始值的构造函数。 |
| new <T>(arrayLength: number): T[] | constructor() | 否 | / |
| new <T>(...items: T[]): T[] | constructor(first: T, ...left: T[]) | 是 | 为了防止undefined扩散，构造函数中必须提供一个初始值的构造函数，继承场景下，无法调用该函数进行对象构造。 |
| from<T>(arrayLike: ArrayLike<T>): T[] | static from<T>(arrayLike: ArrayLike<T>): Array<T> | 否 | / |
| pop(): T | undefined | pop(): T | undefined | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| push(...items: T[]): number | push(...items: T[]): number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| concat(...items: ConcatArray<T>[]): T[] | concat(...items: ConcatArray<T>[]): Array<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| concat(...items: (T | ConcatArray<T>)[]): T[] | concat(...items: ConcatArray<T>[]): Array<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| join(separator?: string): string | join(separator?: string): string | 否 | / |
| shift(): T | undefined | shift(): T | undefined | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| slice(start?: number, end?: number): T[] | slice(start?: number, end?: number): Array<T> | 否 | / |
| sort(compareFn?: (a: T, b: T) => number): this | sort(compareFn?: (a: T, b: T) => number): Array<T> | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 2. 继承场景下，无法获得实际类型的返回值。 |
| unshift(...items: T[]): number | unshift(...items: T[]): number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| indexOf(searchElement: T, fromIndex?: number): number | indexOf(searchElement: T, fromIndex?: number): number | 否 | / |
| forEach(callbackfn: (value: T, index: number, array: T[]) => void, thisArg?: any): void | forEach(callbackFn: (value: T, index: number, array: Array<T>) => void): void | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| map<U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[] | map<U>(callbackFn: (value: T, index: number, array: Array<T>) => U): Array<U> | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| filter(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): T[] | filter(predicate: (value: T, index: number, array: Array<T>) => boolean): Array<T> | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T | reduce(callbackFn: (previousValue: T, currentValue: T, currentIndex: number, array: Array<T>) => T): T | 否 | / |
| reduce<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U | reduce<U>(callbackFn: (previousValue: U, currentValue: T, currentIndex: number, array: Array<T>) => U, initialValue: U): U | 否 | / |
| [n: number]: T | [index: number]: T | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| findIndex(predicate: (value: T, index: number, obj: T[]) => unknown, thisArg?: any): number | findIndex(predicate: (value: T, index: number, obj: Array<T>) => boolean): number | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| fill(value: T, start?: number, end?: number): this | fill(value: T, start?: number, end?: number): Array<T> | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 2. 继承场景下，无法获得实际类型的返回值。 |
| entries(): IterableIterator<[number, T]> | entries(): IterableIterator<[number, T]> | 否 | / |
| keys(): IterableIterator<number> | keys(): IterableIterator<number> | 否 | / |
| values(): IterableIterator<T> | values(): IterableIterator<T> | 否 | / |
| includes(searchElement: T, fromIndex?: number): boolean | includes(searchElement: T, fromIndex?: number): boolean | 否 | / |
| at(index: number): T | undefined | at(index: number): T | undefined | 否 | / |
1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。
2. 继承场景下，无法获得实际类型的返回值。
1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。
2. 继承场景下，无法获得实际类型的返回值。
ArrayBuffer
| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| readonly byteLength: number | readonly byteLength: number | 否 | / |
| slice(begin: number, end?: number): ArrayBuffer | slice(begin: number, end?: number): ArrayBuffer | 否 | / |
| new(byteLength: number): ArrayBuffer | constructor(byteLength: number) | 否 | / |
TypedArray（以Int8Array为例）
支持原生容器TypedArray通过collections.TypedArray.from方法转换为ArkTS TypedArray容器；支持通过原生容器TypedArray的from方法将ArkTS TypedArray容器转换为原生容器TypedArray。
| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| readonly buffer: ArrayBufferLike | readonly buffer: ArrayBuffer | 否 | / |
| readonly byteLength: number | readonly byteLength: number | 否 | / |
| readonly byteOffset: number | readonly byteOffset: number | 否 | / |
| readonly length: number | readonly length: number | 否 | / |
| readonly BYTES_PER_ELEMENT: number | static readonly BYTES_PER_ELEMENT: number | 否 | / |
| copyWithin(target: number, start: number, end?: number): this | copyWithin(target: number, start: number, end?: number): Int8Array | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| every(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean | every(predicate: TypedArrayPredicateFn<number, Int8Array>): boolean | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 2. ArkTS不支持this，因此不支持thisArg参数。 |
| fill(value: number, start?: number, end?: number): this | fill(value: number, start?: number, end?: number): Int8Array | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| filter(predicate: (value: number, index: number, array: Int8Array) => any, thisArg?: any): Int8Array | filter(predicate: TypedArrayPredicateFn<number, Int8Array>): Int8Array | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 2. ArkTS不支持this，因此不支持thisArg参数。 |
| find(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number | undefined | find(predicate: TypedArrayPredicateFn<number, Int8Array>): number | undefined | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 2. ArkTS不支持this，因此不支持thisArg参数。 |
| findIndex(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number | findIndex(predicate: TypedArrayPredicateFn<number, Int8Array>): number | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| forEach(callbackfn: (value: number, index: number, array: Int8Array) => void, thisArg?: any): void | forEach(callbackFn: (value: number, index: number, array: Int8Array) => void): void | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 2. ArkTS不支持this，因此不支持thisArg参数。 |
| indexOf(searchElement: number, fromIndex?: number): number | indexOf(searchElement: number, fromIndex?: number): number | 否 | / |
| join(separator?: string): string | join(separator?: string): string | 否 | / |
| map(callbackfn: (value: number, index: number, array: Int8Array) => number, thisArg?: any): Int8Array | map(callbackFn: TypedArrayForEachCallback<number, Int8Array>): Int8Array | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 2. ArkTS不支持this，因此不支持thisArg参数。 |
| reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number | reduce(callbackFn: TypedArrayReduceCallback<number, number, Int8Array>): number | 否 | / |
| reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number, initialValue: number): number | reduce(callbackFn: TypedArrayReduceCallback<number, number, Int8Array>, initialValue: number): number | 否 | / |
| reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U | reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Int8Array>, initialValue: U): U | 否 | / |
| reverse(): Int8Array | reverse(): Int8Array | 否 | / |
| set(array: ArrayLike<number>, offset?: number): void | set(array: ArrayLike<number>, offset?: number): void | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| slice(start?: number, end?: number): Int8Array | slice(start?: number, end?: number): Int8Array | 否 | / |
| some(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean | some(predicate: TypedArrayPredicateFn<number, Int8Array>): boolean | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| sort(compareFn?: (a: number, b: number) => number): this | sort(compareFn?: TypedArrayCompareFn<number>): Int8Array | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 2. 继承场景下，无法获得实际类型的返回值。 |
| subarray(begin?: number, end?: number): Int8Array | subarray(begin?: number, end?: number): Int8Array | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| [index: number]: number | [index: number]: number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| entries(): IterableIterator<[number, number]> | entries(): IterableIterator<[number, number]> | 否 | / |
| keys(): IterableIterator<number> | keys(): IterableIterator<number> | 否 | / |
| values(): IterableIterator<number> | values(): IterableIterator<number> | 否 | / |
| includes(searchElement: number, fromIndex?: number): boolean | includes(searchElement: number, fromIndex?: number): boolean | 否 | / |
| at(index: number): number | undefined | at(index: number): number | undefined | 否 | / |
| new(length: number): Int8Array | constructor(length: number) | 否 | / |
| new(array: ArrayLike<number> | ArrayBufferLike): Int8Array | constructor(array: ArrayLike<number> | ArrayBuffer) | 否 | / |
| new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Int8Array | constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number) | 否 | / |
| from(arrayLike: ArrayLike<number>): Int8Array | static from(arrayLike: ArrayLike<number>): Int8Array | 否 | / |
| from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int8Array | static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Int8Array | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| from(arrayLike: Iterable<number>, mapfn?: (v: number, k: number) => number, thisArg?: any): Int8Array | static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Int8Array | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。
2. ArkTS不支持this，因此不支持thisArg参数。
1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。
2. ArkTS不支持this，因此不支持thisArg参数。
1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。
2. ArkTS不支持this，因此不支持thisArg参数。
1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。
2. ArkTS不支持this，因此不支持thisArg参数。
1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。
2. ArkTS不支持this，因此不支持thisArg参数。
1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。
2. 继承场景下，无法获得实际类型的返回值。
Map
| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| readonly size: number | readonly size: number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| clear(): void | clear(): void | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| delete(key: K): boolean | delete(key: K): boolean | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| forEach(callbackfn: (value: V, key: K, map: Map<K, V>) => void, thisArg?: any): void | forEach(callbackFn: (value: V, key: K, map: Map<K, V>) => void): void | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 2. ArkTS不支持this，因此不支持thisArg参数。 |
| get(key: K): V | undefined | get(key: K): V | undefined | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| has(key: K): boolean | has(key: K): boolean | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| set(key: K, value: V): this | set(key: K, value: V): Map<K, V> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| entries(): IterableIterator<[K, V]> | entries(): IterableIterator<[K, V]> | 否 | / |
| keys(): IterableIterator<K> | keys(): IterableIterator<K> | 否 | / |
| values(): IterableIterator<V> | values(): IterableIterator<V> | 否 | / |
| new <K, V>(entries?: readonly (readonly [K, V])[] | null): Map<K, V> | constructor(entries?: readonly (readonly [K, V])[] | null) | 是 | 构造时传入的k,v键值不能是非Sendable数据，否则编译会报错。 |
1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。
2. ArkTS不支持this，因此不支持thisArg参数。
Set
| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| readonly size: number | readonly size: number | 是 | Sendable类和接口中不允许使用计算属性名称(arkts-sendable-compated-prop-name)。 |
| add(value: T): this | add(value: T): Set<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| clear(): void | clear(): void | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| delete(value: T): boolean | delete(value: T): boolean | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| forEach(callbackfn: (value: T, value2: T, set: Set<T>) => void, thisArg?: any): void | forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 2. ArkTS不支持this，因此不支持thisArg参数。 |
| has(value: T): boolean | has(value: T): boolean | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| entries(): IterableIterator<[T, T]> | entries(): IterableIterator<[T, T]> | 否 | / |
| keys(): IterableIterator<T> | keys(): IterableIterator<T> | 否 | / |
| values(): IterableIterator<T> | values(): IterableIterator<T> | 是 | Sendable类和接口中不允许使用计算属性名称(arkts-sendable-compated-prop-name)。 |
| new <T = any>(values?: readonly T[] | null): Set<T> | constructor(values?: readonly T[] | null) | 是 | 构造时传入数据不能是非Sendable数据，否则编译会报错。 |
1. 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。
2. ArkTS不支持this，因此不支持thisArg参数。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-sendable-module-V14
爬取时间: 2025-04-27 22:53:20
来源: Huawei Developer
共享模块是进程内只会加载一次的模块，使用"use shared"这一指令来标记一个模块是否为共享模块。
非共享模块在同一线程内只加载一次，在不同线程间会加载多次，在不同的线程内都会产生新的模块对象。因此可以使用共享模块来实现进程单例。
约束限制
-  "use shared"需要与"use strict"一样写在ArkTS文件顶层，写在import语句之后其他语句之前。 共享属性不存在传递性，即非共享模块A不会引入了共享模块B而使A变成共享。
-  共享模块只支持ets文件。
-  共享模块内不允许使用side-effects-import。 共享模块在同一进程内只加载一次，可在不同线程间共享。 共享模块加载时，导入的非共享模块不会立刻加载。在共享模块内访问依赖的非共享模块导出变量时，会在本线程懒加载对应的非共享模块，非共享模块在线程间是隔离的，不同线程访问时都会进行至多一次的模块懒加载。 由于side-effects-import不涉及导出变量，所以永远不会被加载，因此不支持。
```typescript
// 不允许使用side-effects-import
import "./sharedModule"
```
-  共享模块导出的变量必须都是可共享对象。 共享模块在并发实例间可共享，因此模块导出的所有对象都必须是可共享的，可共享对象参考Sendable规格。
-  共享模块中不允许直接导出模块。
```typescript
// test.ets
export let num = 1;
export let str = 'aaa';
// 共享模块
'use shared'
export * from './test'; // 编译报错，不允许直接导出模块
export {num, str} from './test'; // 正确示例，导出对象合集
```
-  共享模块可以引用共享模块或非共享模块。不限制共享模块的引用和被引用场景。
-  napi_load_module、napi_load_module_with_info以及动态加载不支持加载共享模块。
使用示例
1.  共享模块内导出Sendable对象。
```typescript
// 共享模块sharedModule.ets
import { ArkTSUtils } from '@kit.ArkTS';
// 声明当前模块为共享模块，只能导出可Sendable数据
"use shared"
// 共享模块，SingletonA全局唯一
@Sendable
class SingletonA {
private count_: number = 0;
lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock()
public async getCount(): Promise<number> {
return this.lock_.lockAsync(() => {
return this.count_;
})
}
public async increaseCount() {
await this.lock_.lockAsync(() => {
this.count_++;
})
}
}
export let singletonA = new SingletonA();
```
2.  在多个线程中操作共享模块导出的对象。
```typescript
import { taskpool } from '@kit.ArkTS';
import { singletonA } from './sharedModule';
@Concurrent
async function increaseCount() {
await singletonA.increaseCount();
console.info("SharedModule: count is:" + await singletonA.getCount());
}
@Concurrent
async function printCount() {
console.info("SharedModule: count is:" + await singletonA.getCount());
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
Row() {
Column() {
Button("MainThread print count")
.onClick(async () => {
await printCount();
})
Button("Taskpool print count")
.onClick(async () => {
await taskpool.execute(printCount);
})
Button("MainThread increase count")
.onClick(async () => {
await increaseCount();
})
Button("Taskpool increase count")
.onClick(async () => {
await taskpool.execute(increaseCount);
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/sendable-freeze-V14
爬取时间: 2025-04-27 22:53:34
来源: Huawei Developer
Sendable对象支持冻结操作，冻结后的对象变成只读对象，不能增删改属性，因此在多个并发实例间访问均不需要加锁，可以通过调用Object.freeze接口冻结对象。
使用示例
1.  提供ts文件封装Object.freeze方法。
```typescript
// helper.ts
export function freezeObj(obj: any) {
Object.freeze(obj);
}
```
2.  通过调用freeze方法冻结对象，并将对象发送给子线程。
```typescript
// Index.ets
import { freezeObj } from './helper';
import { worker } from '@kit.ArkTS';
@Sendable
export class GlobalConfig {
// 一些配置属性与方法
init() {
// 初始化相关逻辑
freezeObj(this); // 初始化完成后冻结当前对象
}
}
@Entry
@Component
struct Index {
build() {
Column() {
Text("Sendable freezeObj Test")
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
let gConifg = new GlobalConfig();
gConifg.init();
const workerInstance = new worker.ThreadWorker('entry/ets/workers/Worker.ets', { name: "Worker1" });
workerInstance.postMessage(gConifg);
})
}
.height('100%')
.width('100%')
}
}
```
3.  子线程不加锁直接操作对象。
```typescript
// Worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { GlobalConfig } from '../pages/Index';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
let gConfig: GlobalConfig = e.data;
// 使用gConfig对象
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/sendable-guide-V14
爬取时间: 2025-04-27 22:53:48
来源: Huawei Developer
Sendable对象可以在不同并发实例间通过引用传递。通过引用传递方式传输对象相比序列化方式更加高效，同时不会丢失class上携带的成员方法。因此，Sendable主要可以解决两个场景的问题：
-  跨并发实例传输大数据（例如可能达到100KB以上的数据）。
-  跨并发实例传递带方法的class实例对象。
跨并发实例传输大数据场景
由于跨并发实例序列化的开销随着数据量线性增长，因此当传输数据量较大时（100KB数据大约1ms传输耗时），跨并发实例的拷贝开销大，影响应用性能。引用传递方式传输对象可提升性能。
示例：
```typescript
// Index.ets
import { taskpool } from '@kit.ArkTS';
import { testTypeA, testTypeB, Test } from './sendable';
import { BusinessError, emitter } from '@kit.BasicServicesKit';
// 在并发函数中模拟数据处理
@Concurrent
async function taskFunc(obj: Test) {
console.info("test task res1 is: " + obj.data1.name + " res2 is: " + obj.data2.name);
}
async function test() {
// 使用taskpool传递数据
let a: testTypeA = new testTypeA("testTypeA");
let b: testTypeB = new testTypeB("testTypeB");
let obj: Test = new Test(a, b);
let task: taskpool.Task = new taskpool.Task(taskFunc, obj);
await taskpool.execute(task);
}
@Concurrent
function SensorListener() {
// 监听逻辑
// ...
}
@Entry
@Component
struct Index {
build() {
Column() {
Text("Listener task")
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
let sensorTask = new taskpool.LongTask(SensorListener);
emitter.on({ eventId: 0 }, (data) => {
// Do something here
console.info(`Receive ACCELEROMETER data: {${data.data?.x}, ${data.data?.y}, ${data.data?.z}`);
});
taskpool.execute(sensorTask).then(() => {
console.info("Add listener of ACCELEROMETER success");
}).catch((e: BusinessError) => {
// Process error
})
})
Text("Data processing task")
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
test();
})
}
.height('100%')
.width('100%')
}
}
```
```typescript
// sendable.ets
// 将数据量较大的数据在Sendable class中组装
@Sendable
export class testTypeA {
name: string = "A";
constructor(name: string) {
this.name = name;
}
}
@Sendable
export class testTypeB {
name: string = "B";
constructor(name: string) {
this.name = name;
}
}
@Sendable
export class Test {
data1: testTypeA;
data2: testTypeB;
constructor(arg1: testTypeA, arg2: testTypeB) {
this.data1 = arg1;
this.data2 = arg2;
}
}
```
跨并发实例传递带方法的class实例对象
由于序列化传输实例对象时会丢失方法，在必须调用实例方法的场景中，需使用引用传递方式进行开发。在数据处理过程中有需要解析的数据，可使用ASON工具进行数据解析。
示例：
```typescript
// Index.ets
import { taskpool, ArkTSUtils } from '@kit.ArkTS';
import { SendableTestClass, ISendable } from './sendable';
// 在并发函数中模拟数据处理
@Concurrent
async function taskFunc(sendableObj: SendableTestClass) {
console.info("SendableTestClass: name is: " + sendableObj.printName() + ", age is: " + sendableObj.printAge() + ", sex is: " + sendableObj.printSex());
sendableObj.setAge(28);
console.info("SendableTestClass: age is: " + sendableObj.printAge());
// 解析sendableObj.arr数据生成JSON字符串
let str = ArkTSUtils.ASON.stringify(sendableObj.arr);
console.info("SendableTestClass: str is: " + str);
// 解析该数据并生成ISendable数据
let jsonStr = '{"name": "Alexa", "age": 23, "sex": "female"}';
let obj = ArkTSUtils.ASON.parse(jsonStr) as ISendable;
console.info("SendableTestClass: type is: " + typeof obj);
console.info("SendableTestClass: name is: " + (obj as object)?.["name"]); // 输出: 'Alexa'
console.info("SendableTestClass: age is: " + (obj as object)?.["age"]); // 输出: 23
console.info("SendableTestClass: sex is: " + (obj as object)?.["sex"]); // 输出: 'female'
}
async function test() {
// 使用taskpool传递数据
let obj: SendableTestClass = new SendableTestClass();
let task: taskpool.Task = new taskpool.Task(taskFunc, obj);
await taskpool.execute(task);
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(() => {
test();
})
}
.height('100%')
.width('100%')
}
}
```
```typescript
// sendable.ets
// 定义模拟类Test，模仿开发过程中需传递带方法的class
import { lang, collections } from '@kit.ArkTS'
export type ISendable = lang.ISendable;
@Sendable
export class SendableTestClass {
name: string = 'John';
age: number = 20;
sex: string = "man";
arr: collections.Array<number> = new collections.Array<number>(1, 2, 3);
constructor() {
}
setAge(age: number) : void {
this.age = age;
}
printName(): string {
return this.name;
}
printAge(): number {
return this.age;
}
printSex(): string {
return this.sex;
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/interthead-communication-guide-V14
爬取时间: 2025-04-27 22:54:02
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/independent-time-consuming-task-V14
爬取时间: 2025-04-27 22:54:15
来源: Huawei Developer
对于一个独立运行的耗时任务，只需要在任务执行完毕后将结果返回给宿主线程，没有上下文依赖，可以通过以下方式实现。
下面以图片加载为例进行说明。
1.  实现子线程需要执行的任务。
```typescript
// IconItemSource.ets
export class IconItemSource {
image: string | Resource = '';
text: string | Resource = '';
constructor(image: string | Resource = '', text: string | Resource = '') {
this.image = image;
this.text = text;
}
}
```
2.  通过TaskPool中的execute方法执行上述任务，即加载图片。
```typescript
// Index.ets
import { taskpool } from '@kit.ArkTS';
import { IconItemSource } from './IconItemSource';
import { loadPicture } from './IndependentTask';
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
let iconItemSourceList: IconItemSource[] = [];
// 创建Task
let lodePictureTask: taskpool.Task = new taskpool.Task(loadPicture, 30);
// 执行Task，并返回结果
taskpool.execute(lodePictureTask).then((res: object) => {
// loadPicture方法的执行结果
iconItemSourceList = res as IconItemSource[];
})
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/multi-time-consuming-tasks-V14
爬取时间: 2025-04-27 22:54:29
来源: Huawei Developer
如果有多个任务同时执行，由于任务的复杂度不同，执行时间会不一样，返回数据的时间也是不可控的。如果宿主线程需要所有任务执行完毕的数据，那么可以通过下面这种方式实现。
除此以外，如果需要处理的数据量较大（比如一个列表中有10000条数据），把这些数据都放在一个Task中处理也是比较耗时的。那么就可以将原始数据拆分成多个列表，并将每个子列表分配给一个独立的Task进行执行，并且等待全部执行完毕后拼成完整的数据，这样可以节省处理时间，提升用户体验。
下面以多个任务进行图片加载为例进行说明。
1.  实现子线程需要执行的任务。
```typescript
// IconItemSource.ets
export class IconItemSource {
image: string | Resource = '';
text: string | Resource = '';
constructor(image: string | Resource = '', text: string | Resource = '') {
this.image = image;
this.text = text;
}
}
```
2.  将需要执行的Task放到了一个TaskGroup里面，当TaskGroup中所有的Task都执行完毕后，会把每个Task运行的结果都放在一个数组中返回到宿主线程，而不是每执行完一个Task就返回一次，这样就可以在返回的数据里拿到所有的Task执行结果，方便宿主线程使用。
```typescript
// MultiTask.ets
import { taskpool } from '@kit.ArkTS';
import { IconItemSource } from './IconItemSource';
import { loadPicture } from './IndependentTask';
let iconItemSourceList: IconItemSource[][];
let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
taskGroup.addTask(new taskpool.Task(loadPicture, 30));
taskGroup.addTask(new taskpool.Task(loadPicture, 20));
taskGroup.addTask(new taskpool.Task(loadPicture, 10));
taskpool.execute(taskGroup).then((ret: object) => {
let tmpLength = (ret as IconItemSource[][]).length
for (let i = 0; i < tmpLength; i++) {
for (let j = 0; j < ret[i].length; j++) {
iconItemSourceList.push(ret[i][j]);
}
}
})
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/taskpool-communicates-with-mainthread-V14
爬取时间: 2025-04-27 22:54:43
来源: Huawei Developer
如果一个Task，不仅需要返回最后的执行结果，而且需要定时通知宿主线程状态、数据的变化，或者需要分段返回数量级较大的数据（比如从数据库中读取大量数据），可以通过下面这种方式实现。
下面以多个图片加载任务结果实时返回为例进行说明。
1.  首先，实现一个方法，用来接收Task发送的消息。
```typescript
// TaskSendDataUsage.ets
function notice(data: number): void {
console.info("子线程任务已执行完，共加载图片: ", data);
}
```
2.  然后，在Task需要执行的任务中，添加sendData()接口将消息发送给宿主线程。
```typescript
// IconItemSource.ets
export class IconItemSource {
image: string | Resource = '';
text: string | Resource = '';
constructor(image: string | Resource = '', text: string | Resource = '') {
this.image = image;
this.text = text;
}
}
```
3.  最后，在宿主线程通过onReceiveData()接口接收消息。 这样宿主线程就可以通过notice()接口接收到Task发送的数据。
```typescript
// TaskSendDataUsage.ets
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
let iconItemSourceList: IconItemSource[];
let lodePictureTask: taskpool.Task = new taskpool.Task(loadPictureSendData, 30);
// 设置notice方法接收Task发送的消息
lodePictureTask.onReceiveData(notice);
taskpool.execute(lodePictureTask).then((res: object) => {
iconItemSourceList = res as IconItemSource[];
})
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/worker-communicates-with-mainthread-V14
爬取时间: 2025-04-27 22:54:57
来源: Huawei Developer
在ArkTS中，Worker相对于Taskpool存在一定的差异性，有数量限制但是可以长时间存在。一个Worker中可能会执行多个不同的任务，每个任务执行的时长或者返回的结果可能都不相同，宿主线程需要根据情况调用Worker中的不同方法，Worker则需要及时地将结果返回给宿主线程。
下面以Worker响应"hello world"请求为例进行说明。
1.  首先，创建一个执行多个任务Worker。
```typescript
// Worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
// Worker接收宿主线程的消息，做相应的处理
workerPort.onmessage = (e: MessageEvents): void => {
if (e.data === 'hello world') {
workerPort.postMessage('success');
}
}
```
2.  这里的宿主线程为UI主线程，在宿主线程中创建这个Worker的对象，在点击Button的时候调用postmessage向Worker发送消息，通过Worker的onmessage方法接收Worker返回的数据。
```typescript
// Index.ets
import { worker } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
function promiseCase() {
let p: Promise<void> = new Promise<void>((resolve: Function, reject: Function) => {
setTimeout(() => {
resolve(1);
}, 100)
}).then(undefined, (error: BusinessError) => {
})
return p;
}
async function postMessageTest() {
let ss = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
let res = undefined;
let flag = false;
let isTerminate = false;
ss.onexit = () => {
isTerminate = true;
}
// 接收Worker线程发送的消息
ss.onmessage = (e) => {
res = e.data;
flag = true;
console.info("worker:: res is  " + res);
}
// 给Worker线程发送消息
ss.postMessage("hello world");
while (!flag) {
await promiseCase();
}
ss.terminate();
while (!isTerminate) {
await promiseCase();
}
}
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
postMessageTest();
})
}
.width('100%')
}
.height('100%')
}
}
```
在上文这段示例代码中，Worker接收来自宿主线程的消息，并做了相应处理后把结果发回给宿主线程。这样就可以实现宿主线程和Worker间的即时通信，方便宿主线程使用Worker的运行结果。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/worker-invoke-mainthread-interface-V14
爬取时间: 2025-04-27 22:55:10
来源: Huawei Developer
如果一个接口在主线程中已经实现了，Worker需要调用该接口，那么可以使用下面这种方式实现。
下面以Worker同步调用宿主线程接口为例进行说明。
1.  首先，在宿主线程实现需要调用的接口，并且创建Worker对象，在Worker上注册需要调用的接口。
```typescript
// IconItemSource.ets
export class IconItemSource {
image: string | Resource = '';
text: string | Resource = '';
constructor(image: string | Resource = '', text: string | Resource = '') {
this.image = image;
this.text = text;
}
}
```
2.  然后，在Worker中通过callGlobalCallObjectMethod接口就可以调用宿主线程中的setUp()方法了。
```typescript
// Worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
try {
// 调用方法无入参
let res: string = workerPort.callGlobalCallObjectMethod("picData", "setUp", 0) as string;
console.error("worker: ", res);
} catch (error) {
// 异常处理
console.error("worker: error code is " + error.code + " error message is " + error.message);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/multithread-develop-guide-V14
爬取时间: 2025-04-27 22:55:24
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/multithread-develop-overview-V14
爬取时间: 2025-04-27 22:55:38
来源: Huawei Developer
ArkTS应用开发过程中，需要用到并发能力的业务场景很多，不同业务场景需要使用的并发能力不同，对应的主要任务类型也不同。
针对常见的业务场景，主要可以对应分为三种并发任务：
耗时任务：业务逻辑包含较大计算量或多次I/O读写等需要长时间执行的任务。
长时任务：业务逻辑包含监听或定期采集数据等需要长时间保持运行的任务。
常驻任务：业务逻辑跟随主线程生命周期或与主线程绑定的任务。
不同任务类型下可再细划分，比如典型的耗时任务有CPU密集型任务、I/O密集型任务以及同步任务，分别对应的典型业务场景也不相同。请开发者根据场景任务类型对应选择并发能力。
对于各应用多线程开发过程中遇到常见的场景，接下来的章节也会列举一些案例进行介绍。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/time-consuming-task-V14
爬取时间: 2025-04-27 22:55:51
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/time-consuming-task-overview-V14
爬取时间: 2025-04-27 22:56:05
来源: Huawei Developer
耗时任务指的是需要长时间执行的任务，如果在UI主线程执行可能导致应用卡顿掉帧、响应慢等问题。典型的耗时任务有CPU密集型任务、I/O密集型任务以及同步任务。
对应耗时任务，常见的业务场景分类如下所示：
| 常见业务场景 | 具体业务描述 | CPU密集型 | I/O密集型 | 同步任务 |
| --- | --- | --- | --- | --- |
| 图片/视频编解码 | 将图片或视频进行编解码再展示。 | √ | √ | × |
| 压缩/解压缩 | 对本地压缩包进行解压操作或者对本地文件进行压缩操作。 | √ | √ | × |
| JSON解析 | 对JSON字符串的序列化和反序列化操作。 | √ | × | × |
| 模型运算 | 对数据进行模型运算分析等。 | √ | × | × |
| 网络下载 | 密集网络请求下载资源、图片、文件等。 | × | √ | × |
| 数据库操作 | 将聊天记录、页面布局信息、音乐列表信息等保存到数据库，或者应用二次启动时，读取数据库展示相关信息。 | × | √ | × |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/cpu-intensive-task-development-V14
爬取时间: 2025-04-27 22:56:20
来源: Huawei Developer
CPU密集型任务是指需要占用系统资源处理大量计算能力的任务，需要长时间运行，这段时间会阻塞线程其它事件的处理，不适宜放在UI主线程进行。例如图像处理、视频编码、数据分析等。
基于多线程并发机制处理CPU密集型任务可以提高CPU利用率，提升应用程序响应速度。
当任务不需要长时间（3分钟）占据后台线程，而是一个个独立的任务时，推荐使用TaskPool，反之推荐使用Worker。
接下来将以图像直方图处理以及后台长时间的模型预测任务分别进行举例。
使用TaskPool进行图像直方图处理
1.  实现图像处理的业务逻辑。
2.  数据分段，通过任务组发起关联任务调度。 创建TaskGroup并通过addTask()添加对应的任务，通过execute()执行任务组，并指定为高优先级，在当前任务组所有任务结束后，会将直方图处理结果同时返回。
3.  结果数组汇总处理。
```typescript
import { taskpool } from '@kit.ArkTS';
@Concurrent
function imageProcessing(dataSlice: ArrayBuffer): ArrayBuffer {
// 步骤1: 具体的图像处理操作及其他耗时操作
return dataSlice;
}
function histogramStatistic(pixelBuffer: ArrayBuffer): void {
// 步骤2: 分成三段并发调度
let number: number = pixelBuffer.byteLength / 3;
let buffer1: ArrayBuffer = pixelBuffer.slice(0, number);
let buffer2: ArrayBuffer = pixelBuffer.slice(number, number * 2);
let buffer3: ArrayBuffer = pixelBuffer.slice(number * 2);
let group: taskpool.TaskGroup = new taskpool.TaskGroup();
group.addTask(imageProcessing, buffer1);
group.addTask(imageProcessing, buffer2);
group.addTask(imageProcessing, buffer3);
taskpool.execute(group, taskpool.Priority.HIGH).then((ret: Object) => {
// 步骤3: 结果数组汇总处理
})
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World'
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
let buffer: ArrayBuffer = new ArrayBuffer(24);
histogramStatistic(buffer);
})
}
.width('100%')
}
.height('100%')
}
}
```
使用Worker进行长时间数据分析
本文通过某地区提供的房价数据训练一个简易的房价预测模型，该模型支持通过输入房屋面积和房间数量去预测该区域的房价，模型需要长时间运行，房价预测需要使用前面的模型运行结果，因此需要使用Worker。
1.  DevEco Studio提供了Worker创建的模板，新建一个Worker线程，例如命名为“MyWorker”。
2.  在宿主线程中通过调用ThreadWorker的constructor()方法创建Worker对象。
```typescript
// Index.ets
import { worker } from '@kit.ArkTS';
const workerInstance: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/MyWorker.ts');
```
3.  在宿主线程中通过调用onmessage()方法接收Worker线程发送过来的消息，并通过调用postMessage()方法向Worker线程发送消息。 例如向Worker线程发送训练和预测的消息，同时接收Worker线程发送回来的消息。
```typescript
// Index.ets
let done = false;
// 接收Worker子线程的结果
workerInstance.onmessage = (() => {
console.info('MyWorker.ts onmessage');
if (!done) {
workerInstance.postMessage({ 'type': 1, 'value': 0 });
done = true;
}
})
workerInstance.onerror = (() => {
// 接收Worker子线程的错误信息
})
// 向Worker子线程发送训练消息
workerInstance.postMessage({ 'type': 0 });
```
4.  在MyWorker.ts文件中绑定Worker对象，当前线程为Worker线程。
```typescript
// MyWorker.ts
import { worker, ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@kit.ArkTS';
let workerPort: ThreadWorkerGlobalScope = worker.workerPort;
```
5.  在Worker线程中通过调用onmessage()方法接收宿主线程发送的消息内容，并通过调用postMessage()方法向宿主线程发送消息。 例如在Worker线程中定义预测模型及其训练过程，同时与宿主线程进行信息交互。
```typescript
// MyWorker.ts
// 定义训练模型及结果
let result: Array<number>;
// 定义预测函数
function predict(x: number): number {
return result[x];
}
// 定义优化器训练过程
function optimize(): void {
result = [0];
}
// Worker线程的onmessage逻辑
workerPort.onmessage = (e: MessageEvents): void => {
// 根据传输的数据的type选择进行操作
switch (e.data.type as number) {
case 0:
// 进行训练
optimize();
// 训练之后发送宿主线程训练成功的消息
workerPort.postMessage({ type: 'message', value: 'train success.' });
break;
case 1:
// 执行预测
const output: number = predict(e.data.value as number);
// 发送宿主线程预测的结果
workerPort.postMessage({ type: 'predict', value: output });
break;
default:
workerPort.postMessage({ type: 'message', value: 'send message is invalid' });
break;
}
}
```
6.  在Worker线程中完成任务之后，执行Worker线程销毁操作。销毁线程的方式主要有两种：根据需要可以在宿主线程中对Worker线程进行销毁；也可以在Worker线程中主动销毁Worker线程。 在宿主线程中通过调用onexit()方法定义Worker线程销毁后的处理逻辑。 方式一：在宿主线程中通过调用terminate()方法销毁Worker线程，并终止Worker接收消息。 方式二：在Worker线程中通过调用close()方法主动销毁Worker线程，并终止Worker接收消息。
```typescript
// Worker线程销毁后，执行onexit回调方法
workerInstance.onexit = (): void => {
console.info("main thread terminate");
}
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170233.81535343531071044664222807145104:50001231000000:2800:92028063850225158FC551E6DC262C154B34CCA988DD0BCBF29B5C48E74F2073.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/io-intensive-task-development-V14
爬取时间: 2025-04-27 22:57:13
来源: Huawei Developer
使用异步并发可以解决单次I/O任务阻塞的问题，但是如果遇到I/O密集型任务，同样会阻塞线程中其它任务的执行，这时需要使用多线程并发能力来进行解决。
I/O密集型任务的性能重点通常不在于CPU的处理能力，而在于I/O操作的速度和效率。这种任务通常需要频繁地进行磁盘读写、网络通信等操作。此处以频繁读写系统文件来模拟I/O密集型并发任务的处理。
1.  定义并发函数，内部密集调用I/O能力。
```typescript
// write.ets
import { fileIo } from '@kit.CoreFileKit'
// 定义并发函数，内部密集调用I/O能力
// 写入文件的实现
export async function write(data: string, filePath: string): Promise<void> {
let file: fileIo.File = await fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
await fileIo.write(file.fd, data);
fileIo.close(file);
}
```
2.  使用TaskPool执行包含密集I/O的并发函数：通过调用execute()方法执行任务，并在回调中进行调度结果处理。示例中获取filePath1和filePath2的方式请参见获取应用文件路径，在TaskPool中使用context需先在并发函数外部准备好，通过入参传递给并发函数才可使用。
```typescript
// Index.ets
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
let context = getContext() as common.UIAbilityContext;
// 使用TaskPool执行包含密集I/O的并发函数
// 数组较大时，I/O密集型任务任务分发也会抢占UI主线程，需要使用多线程能力
taskpool.execute(concurrentTest, context).then(() => {
// 调度结果处理
console.info("taskpool: execute success")
})
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/sync-task-development-V14
爬取时间: 2025-04-27 22:57:27
来源: Huawei Developer
同步任务是指在多个线程之间协调执行的任务，其目的是确保多个任务按照一定的顺序和规则执行，例如使用锁来防止数据竞争。
同步任务的实现需要考虑多个线程之间的协作和同步，以确保数据的正确性和程序的正确执行。
由于TaskPool偏向于单个独立的任务，因此当各个同步任务之间相对独立时推荐使用TaskPool，例如一系列导入的静态方法，或者单例实现的方法。如果同步任务之间有关联性，则需要使用Worker，例如无法单例创建的类对象实现的方法。
使用TaskPool处理同步任务
当调度独立的任务，或者一系列任务为静态方法实现，或者可以通过单例构造唯一的句柄或类对象，可在不同任务线程之间使用时，推荐使用TaskPool。
由于Actor模型不同线程间内存隔离的特性，普通单例无法在不同线程间使用。可以通过共享模块导出单例解决该问题。
1.  定义并发函数，实现业务逻辑。
2.  创建任务Task，通过execute()接口执行该任务。
3.  对任务返回的结果进行操作。
如下示例中业务使用TaskPool调用相关同步方法的代码，首先定义并发函数taskpoolFunc，需要注意必须使用@Concurrent装饰器装饰该函数；其次定义函数mainFunc，该函数功能为创建任务，执行任务并对任务返回的结果进行操作。
```typescript
// Index.ets代码
import { taskpool} from '@kit.ArkTS';
// 步骤1: 定义并发函数，实现业务逻辑
@Concurrent
async function taskpoolFunc(num: number): Promise<number> {
// 根据业务逻辑实现相应的功能
let tmpNum: number = num + 100;
return tmpNum;
}
async function mainFunc(): Promise<void> {
// 步骤2: 创建任务并执行
let task1: taskpool.Task = new taskpool.Task(taskpoolFunc, 1);
let res1: number = await taskpool.execute(task1) as number;
let task2: taskpool.Task = new taskpool.Task(taskpoolFunc, res1);
let res2: number = await taskpool.execute(task2) as number;
// 步骤3: 对任务返回的结果进行操作
console.info("taskpool: task res1 is: " + res1);
console.info("taskpool: task res2 is: " + res2);
}
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
.onClick(async () => {
mainFunc();
})
}
.width('100%')
.height('100%')
}
}
}
```
使用Worker处理关联的同步任务
当一系列同步任务需要使用同一个句柄调度，或者需要依赖某个类对象调度，无法在不同任务池之间共享时，需要使用Worker。
1.  在UI主线程中创建Worker对象，同时接收Worker线程发送回来的消息。DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。
```typescript
// Index.ets
import { worker } from '@kit.ArkTS';
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
let w: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/MyWorker.ts');
w.onmessage = (): void => {
// 接收Worker子线程的结果
}
w.onerror = (): void => {
// 接收Worker子线程的错误信息
}
// 向Worker子线程发送Set消息
w.postMessage({'type': 0, 'data': 'data'})
// 向Worker子线程发送Get消息
w.postMessage({'type': 1})
// ...
// 根据实际业务，选择时机以销毁线程
w.terminate()
})
}
.width('100%')
}
.height('100%')
}
}
```
2.  在Worker线程中绑定Worker对象，同时处理同步任务逻辑。
```typescript
// handle.ts代码
export default class Handle {
syncGet() {
return;
}
syncSet(num: number) {
return;
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/long-time-task-V14
爬取时间: 2025-04-27 22:57:41
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/long-time-task-overview-V14
爬取时间: 2025-04-27 22:57:54
来源: Huawei Developer
在应用业务实现过程中，对于需要较长时间不定时运行的任务，称为长时任务。长时任务如果放在UI主线程中执行会阻塞UI主线程的UI业务，出现卡顿丢帧等影响用户体验的问题。因此通常需要将这个独立的长时任务放到单独的子线程中执行。
典型的长时任务场景如下所示：
| 常见业务场景 | 具体业务描述 |
| --- | --- |
| 定期采集传感器数据 | 周期性采集一些传感器信息（例如位置信息、速度传感器等），应用运行阶段长时间不间断运行。 |
| 监听Socket端口信息 | 长时间监听Socket数据，不定时需要响应处理。 |
上述业务场景均为独立的长时任务，任务执行周期长，跟外部交互简单，分发到后台线程后，需要不定期响应，以获取结果。这些类型的任务使用TaskPool可以简化开发工作量，避免管理复杂的生命周期，避免线程泛滥，开发者只需要将上述独立的长时任务放入TaskPool队列，再等待结果即可。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/long-time-task-guide-V14
爬取时间: 2025-04-27 22:58:08
来源: Huawei Developer
此处提供使用TaskPool进行长时任务的开发指导，以定期采集传感器数据为例。
使用TaskPool进行传感器数据监听
1.  导入需要用到的模块。
```typescript
// Index.ets
import { sensor } from '@kit.SensorServiceKit';
import { taskpool } from '@kit.ArkTS';
import { BusinessError, emitter } from '@kit.BasicServicesKit';
```
2.  定义长时任务，内部监听sensor数据，并通过emitter注册销毁通知。
```typescript
// Index.ets
@Concurrent
async function SensorListener() : Promise<void> {
sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
emitter.emit({ eventId: 0 }, { data: data });
}, { interval: 1000000000 });
emitter.on({ eventId: 1 }, () => {
sensor.off(sensor.SensorId.ACCELEROMETER)
emitter.off(1)
})
}
```
3.  宿主线程定义注册及销毁的行为。
```typescript
// Index.ets
@Entry
@Component
struct Index {
sensorTask?: taskpool.LongTask
build() {
Column() {
Text("Add listener")
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
this.sensorTask = new taskpool.LongTask(SensorListener);
emitter.on({ eventId: 0 }, (data) => {
// Do something here
console.info(`Receive ACCELEROMETER data: {${data.data?.x}, ${data.data?.y}, ${data.data?.z}`);
});
taskpool.execute(this.sensorTask).then(() => {
console.info("Add listener of ACCELEROMETER success");
}).catch((e: BusinessError) => {
// Process error
})
})
Text("Delete listener")
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
emitter.emit({ eventId: 1 });
emitter.off(0);
if(this.sensorTask != undefined) {
taskpool.terminateTask(this.sensorTask);
} else {
console.error("sensorTask is undefined.");
}
})
}
.height('100%')
.width('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/resident-task-V14
爬取时间: 2025-04-27 22:58:21
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/resident-task-overview-V14
爬取时间: 2025-04-27 22:58:35
来源: Huawei Developer
在应用业务实现过程中，对于一些长耗时（大于3min）且并发量不大的常驻任务场景，使用Worker在后台线程中运行这些耗时逻辑，避免阻塞UI主线程而导致出现丢帧卡顿等影响用户体验性的问题 。
常驻任务是指相比于短时任务，时间更长的任务，可能跟UI主线程生命周期一致。相比于长时任务，常驻任务更倾向于跟线程绑定的任务，单次运行时间更长（比如超过3分钟）。
对应常驻任务，较为常见的业务场景如下：
| 常见业务场景 | 具体业务描述 |
| --- | --- |
| 游戏中台场景 | 启动子线程作为游戏业务的主逻辑线程，UI线程只负责渲染。 |
| 长耗时任务场景 | 后台长时间的模型预测任务、或者硬件测试等。 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/resident-task-guide-V14
爬取时间: 2025-04-27 22:58:49
来源: Huawei Developer
此处提供使用Worker进行常驻任务的开发指导，Worker会持续执行任务直到宿主线程发出终止指令。
开发过程和示例如下所示：
1.  DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建“Worker”为例。 此外，还支持手动创建Worker文件，具体方式和相关注意事项请见创建Worker的注意事项。
2.  导入Worker模块。
```typescript
// Index.ets
import { worker } from '@kit.ArkTS';
```
3.  在宿主线程中通过调用ThreadWorker的constructor()方法创建Worker对象，当前线程为宿主线程。
```typescript
// Index.ets
const workerInstance: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
```
4.  此处宿主线程为UI主线程，宿主线程发送'start'，开始执行某个长期运行的任务并接收子线程返回的相关消息。在不需要执行该任务时发送'stop'，停止该任务执行，该示例中10s后结束该任务。
```typescript
// Index.ets
@Entry
@Component
struct Index {
build() {
Column() {
Text("Listener task")
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
workerInstance.postMessage({type: 'start'})
workerInstance.onmessage = (event) => {
console.info('UI主线程收到消息:', event.data);
}
// 10秒后停止worker
setTimeout(() => {
workerInstance.postMessage({ type: 'stop' });
}, 10000);
})
}
.height('100%')
.width('100%')
}
}
```
5.  在Worker线程中当接受到宿主线程发送的消息为'start'时，开始执行某个长时间不定期运行的任务并实时返回消息给宿主线程。当接收到的消息为'stop'时结束该任务执行并返回相应消息给宿主线程。
```typescript
// Worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
let isRunning = false;
workerPort.onmessage = (e: MessageEvents) => {
const type = e.data.type as string;
if (type === 'start') {
if (!isRunning) {
isRunning = true;
// 开始常驻任务
performTask();
}
} else if (type === 'stop') {
isRunning = false;
workerPort.close();  // 关闭Worker
}
}
// 模拟常驻任务
function performTask() {
if (isRunning) {
// 模拟某个长期运行的任务
workerPort.postMessage('Worker is performing a task');
// 1秒后再次执行任务
setTimeout(performTask, 1000);
}
workerPort.postMessage('Worker is stop performing a task');
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/multithread-develop-case-V14
爬取时间: 2025-04-27 22:59:02
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/batch-database-operations-guide-V14
爬取时间: 2025-04-27 22:59:16
来源: Huawei Developer
使用TaskPool进行频繁数据库操作
对于需要频繁数据库操作的场景，由于读写数据库存在耗时，因此推荐在子线程中操作，避免阻塞UI线程。
通过ArkTS提供的TaskPool能力，可以将数据库操作任务移到子线程中，实现如下。
1.  创建多个子任务，支持数据库创建、插入、查询、清除等操作。
2.  UI主线程调用子任务完成增删改查等数据库操作。
```typescript
// Index.ets
import { relationalStore, ValuesBucket } from '@kit.ArkData';
import { taskpool } from '@kit.ArkTS';
@Concurrent
async function create(context: Context) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 创建表
const CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS test (" +
"id INTEGER PRIMARY KEY AUTOINCREMENT, " +
"name TEXT NOT NULL, " +
"age INTEGER, " +
"salary REAL, " +
"blobType BLOB)";
await store.executeSql(CREATE_TABLE_SQL);
console.info(`Create table test successfully!`);
}
@Concurrent
async function insert(context: Context, valueBucketArray: Array<relationalStore.ValuesBucket>) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 数据插入
await store.batchInsert("test", valueBucketArray as Object as Array<relationalStore.ValuesBucket>);
}
@Concurrent
async function query(context: Context): Promise<Array<relationalStore.ValuesBucket>> {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 获取结果集
let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates("test");
let resultSet = await store.query(predicates);  // 查询所有数据
console.info(`Query data successfully! row count:${resultSet.rowCount}`);
let index = 0;
let result = new Array<relationalStore.ValuesBucket>(resultSet.rowCount)
resultSet.goToFirstRow()
do {
result[index++] = resultSet.getRow()
} while (resultSet.goToNextRow());
resultSet.close();
return result
}
@Concurrent
async function clear(context: Context) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
await relationalStore.deleteRdbStore(context, CONFIG);
console.info(`Delete Store.db successfully!`);
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
let context = getContext(this);
// 数据准备
const count = 5
let valueBucketArray = new Array<relationalStore.ValuesBucket>(count);
for (let i = 0; i < count; i++) {
let v : relationalStore.ValuesBucket = {
id: i,
name: "zhangsan" + i,
age: 20,
salary: 5000 + 50 * i
};
valueBucketArray[i] = v;
}
await taskpool.execute(create, context)
await taskpool.execute(insert, context, valueBucketArray)
let index = 0
let ret = await taskpool.execute(query, context) as Array<relationalStore.ValuesBucket>
for (let v of ret) {
console.info(`Row[${index}].id = ${v.id}`)
console.info(`Row[${index}].name = ${v.name}`)
console.info(`Row[${index}].age = ${v.age}`)
console.info(`Row[${index}].salary = ${v.salary}`)
index++
}
await taskpool.execute(clear, context)
})
}
.height('100%')
.width('100%')
}
}
```
使用Sendable进行大容量数据库操作
由于数据库数据跨线程传递存在耗时，当数据量较大时，仍然会占用UI主线程，推荐采用Sendable封装数据库数据，降低跨线程开销。
1.  定义数据库中的数据格式，可采用Sendable，减少跨线程耗时。
```typescript
// SharedValuesBucket.ets
export interface IValueBucket {
id: number
name: string
age: number
salary: number
}
@Sendable
export class SharedValuesBucket implements IValueBucket {
id: number = 0
name: string = ""
age: number = 0
salary: number = 0
constructor(v: IValueBucket) {
this.id = v.id;
this.name = v.name;
this.age = v.age;
this.salary = v.salary
}
}
```
2.  UI主线程发起，在子线程进行数据的增删改查等操作。
```typescript
// Index.ets
import { relationalStore, ValuesBucket } from '@kit.ArkData';
import { collections, taskpool } from '@kit.ArkTS';
import { IValueBucket, SharedValuesBucket } from './SharedValuesBucket';
@Concurrent
async function create(context: Context) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 创建表
const CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS test (" +
"id INTEGER PRIMARY KEY AUTOINCREMENT, " +
"name TEXT NOT NULL, " +
"age INTEGER, " +
"salary REAL, " +
"blobType BLOB)";
await store.executeSql(CREATE_TABLE_SQL);
console.info(`Create table test successfully!`);
}
@Concurrent
async function insert(context: Context, valueBucketArray: collections.Array<SharedValuesBucket | undefined>) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 数据插入
await store.batchInsert("test", valueBucketArray as Object as Array<ValuesBucket>);
}
@Concurrent
async function query(context: Context): Promise<collections.Array<SharedValuesBucket | undefined>> {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 获取结果集
let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates("test");
let resultSet = await store.query(predicates); // 查询所有数据
console.info(`Query data successfully! row count:${resultSet.rowCount}`);
let index = 0;
let result = collections.Array.create<SharedValuesBucket | undefined>(resultSet.rowCount, undefined)
resultSet.goToFirstRow()
do {
let v: IValueBucket = {
id: resultSet.getLong(resultSet.getColumnIndex("id")),
name: resultSet.getString(resultSet.getColumnIndex("name")),
age: resultSet.getLong(resultSet.getColumnIndex("age")),
salary: resultSet.getLong(resultSet.getColumnIndex("salary"))
};
result[index++] = new SharedValuesBucket(v)
} while (resultSet.goToNextRow());
resultSet.close();
return result
}
@Concurrent
async function clear(context: Context) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
await relationalStore.deleteRdbStore(context, CONFIG);
console.info(`Delete Store.db successfully!`);
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
let context = getContext(this);
// 数据准备
const count = 5
let valueBucketArray = collections.Array.create<SharedValuesBucket | undefined>(count, undefined);
for (let i = 0; i < count; i++) {
let v: IValueBucket = {
id: i,
name: "zhangsan" + i,
age: 20,
salary: 5000 + 50 * i
};
valueBucketArray[i] = new SharedValuesBucket(v);
}
await taskpool.execute(create, context)
await taskpool.execute(insert, context, valueBucketArray)
let index = 0
let ret: collections.Array<SharedValuesBucket> =
await taskpool.execute(query, context) as collections.Array<SharedValuesBucket>
for (let v of ret.values()) {
console.info(`Row[${index}].id = ${v.id}`)
console.info(`Row[${index}].name = ${v.name}`)
console.info(`Row[${index}].age = ${v.age}`)
console.info(`Row[${index}].salary = ${v.salary}`)
index++
}
await taskpool.execute(clear, context)
})
}
.height('100%')
.width('100%')
}
}
```
复杂类实例对象使用Sendable进行大容量数据库操作
普通类实例对象的属性可持有Sendable类实例对象。
对于复杂的普通类实例对象，可以先将相应数据库数据字段封装为Sendable类实例对象，再由普通类实例对象持有，从而降低跨线程开销。
1.  定义数据库中的数据格式，可采用Sendable，减少跨线程耗时。
```typescript
// SharedValuesBucket.ets
export interface IValueBucket {
id: number;
name: string;
age: number;
salary: number;
}
@Sendable
export class SharedValuesBucket implements IValueBucket {
id: number = 0;
name: string = "";
age: number = 0;
salary: number = 0;
constructor(v: IValueBucket) {
this.id = v.id;
this.name = v.name;
this.age = v.age;
this.salary = v.salary;
}
}
```
2.  定义普通类实例对象，持有Sendable类实例对象。
```typescript
// Material.ets
import { SharedValuesBucket } from './SharedValuesBucket';
import { collections } from '@kit.ArkTS';
export class Material {
seq: number = 0;
materialName: string = "";
// ... 省略其他属性
buckets: collections.Array<SharedValuesBucket | undefined>;
constructor(seq: number, materialName: string, buckets: collections.Array<SharedValuesBucket | undefined>) {
this.seq = seq;
this.materialName = materialName;
this.buckets = buckets;
}
getBuckets() : collections.Array<SharedValuesBucket | undefined>{
return this.buckets;
}
setBuckets(buckets: collections.Array<SharedValuesBucket | undefined>) {
this.buckets = buckets;
}
}
```
3.  UI主线程发起，在子线程进行数据的增删改查等操作。
```typescript
// Index.ets
import { relationalStore, ValuesBucket } from '@kit.ArkData';
import { collections, taskpool } from '@kit.ArkTS';
import { IValueBucket, SharedValuesBucket } from './SharedValuesBucket';
import { Material } from './Material';
@Concurrent
async function create(context: Context) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 创建表
const CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS test (" +
"id INTEGER PRIMARY KEY AUTOINCREMENT, " +
"name TEXT NOT NULL, " +
"age INTEGER, " +
"salary REAL, " +
"blobType BLOB)";
await store.executeSql(CREATE_TABLE_SQL);
console.info(`Create table test successfully!`);
}
@Concurrent
async function insert(context: Context, valueBucketArray: collections.Array<SharedValuesBucket | undefined>) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 数据插入
await store.batchInsert("test", valueBucketArray as Object as Array<ValuesBucket>);
}
@Concurrent
async function query(context: Context): Promise<collections.Array<SharedValuesBucket | undefined>> {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
console.info(`Create Store.db successfully!`);
// 获取结果集
let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates("test");
let resultSet = await store.query(predicates); // 查询所有数据
console.info(`Query data successfully! row count:${resultSet.rowCount}`);
let index = 0;
let result = collections.Array.create<SharedValuesBucket | undefined>(resultSet.rowCount, undefined)
resultSet.goToFirstRow()
do {
let v: IValueBucket = {
id: resultSet.getLong(resultSet.getColumnIndex("id")),
name: resultSet.getString(resultSet.getColumnIndex("name")),
age: resultSet.getLong(resultSet.getColumnIndex("age")),
salary: resultSet.getLong(resultSet.getColumnIndex("salary"))
};
result[index++] = new SharedValuesBucket(v)
} while (resultSet.goToNextRow());
resultSet.close();
return result
}
@Concurrent
async function clear(context: Context) {
const CONFIG: relationalStore.StoreConfig = {
name: "Store.db",
securityLevel: relationalStore.SecurityLevel.S1,
};
// 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
await relationalStore.deleteRdbStore(context, CONFIG);
console.info(`Delete Store.db successfully!`);
}
function initMaterial() : Material {
// 数据准备
const count = 5
let valueBucketArray = collections.Array.create<SharedValuesBucket | undefined>(count, undefined);
for (let i = 0; i < count; i++) {
let v: IValueBucket = {
id: i,
name: "zhangsan" + i,
age: 20,
salary: 5000 + 50 * i
};
valueBucketArray[i] = new SharedValuesBucket(v);
}
let material = new Material(1, "test", valueBucketArray);
return material;
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
let context = getContext(this);
let material = initMaterial();
await taskpool.execute(create, context);
await taskpool.execute(insert, context, material.getBuckets());
let index = 0;
let ret: collections.Array<SharedValuesBucket> =
await taskpool.execute(query, context) as collections.Array<SharedValuesBucket>;
material.setBuckets(ret);
for (let v of ret.values()) {
console.info(`Row[${index}].id = ${v.id}`);
console.info(`Row[${index}].name = ${v.name}`);
console.info(`Row[${index}].age = ${v.age}`);
console.info(`Row[${index}].salary = ${v.salary}`);
index++;
}
await taskpool.execute(clear, context);
})
}
.height('100%')
.width('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/concurrent-loading-modules-guide-V14
爬取时间: 2025-04-27 22:59:30
来源: Huawei Developer
在应用启动过程中，会有多个业务模块需要加载，例如地图类应用的定位、打车、导航等不同的模块，如果全部在UI主线程初始化，则会严重影响冷启动耗时。此时需要在不同子线程并行化加载这些模块功能，降低启动耗时。
通过使用ArkTS提供的TaskPool能力，可以将不同业务初始化任务移到子线程中，业务模块通过下沉C++实现成NativeBinding对象、或者在ArkTS层定义Sendable对象，就可以将初始化的模块返回UI主线程调用，实现如下。
1.  各业务功能（SDK）模块定义（这里以Sendable对象为例）。 计算器业务模块定义如下： 定时器业务模块定义如下：
```typescript
// sdk/Calculator.ets
import { collections } from '@kit.ArkTS'
@Sendable
export class Calculator {
history?: collections.Array<collections.Array<string>>
totalCount: number = 0
static init(): Calculator {
let calc = new Calculator()
calc.totalCount = 0
calc.history = collections.Array.create(calc.totalCount, collections.Array.create(2, ""));
return calc
}
add(a: number, b: number) {
let result = a + b;
this.newCalc(`${a} + ${b}`, `${result}`);
return result
}
sub(a: number, b: number) {
let result = a - b;
this.newCalc(`${a} - ${b}`, `${result}`);
return result
}
mul(a: number, b: number) {
let result = a * b;
this.newCalc(`${a} * ${b}`, `${result}`);
return result
}
div(a: number, b: number) {
let result = a / b;
this.newCalc(`${a} / ${b}`, `${result}`);
return result
}
getHistory(): collections.Array<collections.Array<string>> {
return this.history!;
}
showHistory() {
for (let i = 0; i < this.totalCount; i++) {
console.info(`${i}: ${this.history![i][0]} = ${this.history![i][1]}`)
}
}
private newCalc(opt: string, ret: string) {
let newRecord = new collections.Array<string>(opt, ret)
this.totalCount = this.history!.unshift(newRecord)
}
}
```
2.  在UI主线程触发各业务模块分发到子线程，加载完成后在UI主线程使用。
```typescript
// Index.ets
import { Calculator } from '../sdk/Calculator'
import { TimerSdk } from '../sdk/TimerSdk'
import { taskpool } from '@kit.ArkTS';
@Concurrent
function initCalculator(): Calculator {
return Calculator.init()
}
@Concurrent
function initTimerSdk(): TimerSdk {
return TimerSdk.init()
}
@Entry
@Component
struct Index {
calc?: Calculator
timer?: TimerSdk
aboutToAppear(): void {
taskpool.execute(initCalculator).then((ret) => {
this.calc = ret as Calculator
})
taskpool.execute(initTimerSdk).then((ret) => {
this.timer = ret as TimerSdk
})
}
build() {
Row() {
Column() {
Text("calculate add")
.id('add')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
let result = this.calc?.add(1, 2)
console.info(`Result is ${result}`)
})
Text("show history")
.id('show')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
this.calc?.showHistory()
})
Text("countdown")
.id('get')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
console.info(`Timer start`)
await this.timer?.Countdown(1000);
console.info(`Timer end`)
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/global-configuration-guide-V14
爬取时间: 2025-04-27 22:59:44
来源: Huawei Developer
对于需要使用进程单例的场景，例如不同并发实例间需要数据保持一致的全局配置项业务，可以采用共享模块来实现。
如下示例实现了只有Wi-Fi打开且用户登陆后才能下载的业务功能，具体步骤如下。
1.  编写全局配置文件。
```typescript
// Config.ets
import { ArkTSUtils } from '@kit.ArkTS';
"use shared"
@Sendable
class Config {
lock: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock
isLogin: boolean = false;
loginUser?: string;
wifiOn: boolean = false
async login(user: string) {
return this.lock.lockAsync(() => {
this.isLogin = true;
this.loginUser = user
}, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
}
async logout(user?: string) {
return this.lock.lockAsync(() => {
this.isLogin = false
this.loginUser = ""
}, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
}
async getIsLogin(): Promise<boolean> {
return this.lock.lockAsync(() => {
return this.isLogin
}, ArkTSUtils.locks.AsyncLockMode.SHARED)
}
async getUser(): Promise<string> {
return this.lock.lockAsync(() => {
return this.loginUser!
}, ArkTSUtils.locks.AsyncLockMode.SHARED)
}
async setWifiState(state: boolean) {
return this.lock.lockAsync(() => {
this.wifiOn = state
}, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
}
async isWifiOn() {
return this.lock.lockAsync(() => {
return this.wifiOn;
}, ArkTSUtils.locks.AsyncLockMode.SHARED)
}
}
export let config = new Config()
```
2.  UI主线程及子线程访问全局配置项。
```typescript
import { config } from './Config'
import { taskpool } from '@kit.ArkTS';
@Concurrent
async function download() {
if (!await config.isWifiOn()) {
console.info("wifi is off")
return false;
}
if (!await config.getIsLogin()) {
console.info("not login")
return false;
}
console.info(`User[${await config.getUser()}] start download ...`)
return true;
}
@Entry
@Component
struct Index {
@State message: string = 'not login';
@State wifiState: string = "wifi off";
@State downloadResult: string = "";
input: string = ""
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
TextInput({ placeholder: "请输入用户名" })
.fontSize(20)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onChange((value) => {
this.input = value;
})
Text("login")
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
if (!await config.getIsLogin() && this.input) {
this.message = "login: " + this.input
config.login(this.input)
}
})
.backgroundColor(0xcccccc)
Text("logout")
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
if (await config.getIsLogin()) {
this.message = "not login"
config.logout()
}
})
.backgroundColor(0xcccccc)
Text(this.wifiState)
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
Toggle({ type: ToggleType.Switch })
.onChange(async (isOn: boolean) => {
await config.setWifiState(isOn)
this.wifiState = isOn ? "wifi on" : "wifi off";
})
Text("download")
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
let ret = await taskpool.execute(download)
this.downloadResult = ret ? "download success" : "download fail";
})
Text(this.downloadResult)
.fontSize(20)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/makeobserved-sendable-V14
爬取时间: 2025-04-27 22:59:57
来源: Huawei Developer
当需要网络下载或者本地生成的数据需要发送到UI线程进行展示时，因为ArkUI的标注和@Sendable装饰器不能同时修饰变量和对象，所以对于此类场景，需要使用makeObserved在ArkUI中导入可观察的Sendable共享数据。
本示例将说明下面的场景：
```typescript
// SendableData.ets
@Sendable
export class SendableData {
name: string = 'Tom';
age: number = 20;
gender: number = 1;
likes: number = 1;
follow: boolean = false;
}
```
```typescript
import { taskpool } from '@kit.ArkTS';
import { SendableData } from './SendableData';
import { UIUtils } from '@kit.ArkUI';
@Concurrent
function threadGetData(param: string): SendableData {
// 在子线程处理数据
let ret = new SendableData();
console.info(`Concurrent threadGetData, param ${param}`);
ret.name = param + "-o";
ret.age = Math.floor(Math.random() * 40);
ret.likes = Math.floor(Math.random() * 100);
return ret;
}
@Entry
@ComponentV2
struct Index {
// 通过makeObserved给普通对象或是Sendable对象添加可观察能力
@Local send: SendableData = UIUtils.makeObserved(new SendableData());
build() {
Column() {
Text(this.send.name)
Button("change name").onClick(() => {
// 可以观察到属性的改变
this.send.name += "0";
})
Button("task").onClick(() => {
// 将待执行的函数放入taskpool内部任务队列等待，等待分发到工作线程执行。
// 因为数据的构建和处理可以在子线程中完成，但有观察能力的数据不能传给子线程，只有在UI主线程里才可以操作可观察的数据。
// 所以这里只是将`this.send`的属性`name`传给子线程操作。
taskpool.execute(threadGetData, this.send.name).then(val => {
// 和@Local一起使用，可以观察this.send的变化
this.send = UIUtils.makeObserved(val as SendableData);
})
})
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/native-interthread-shared-V14
爬取时间: 2025-04-27 23:00:11
来源: Huawei Developer
当应用在C++层进行多线程的并发计算时，因为ArkTS的API需要在ArkTS的环境执行，为了避免在非UI主线程每次回调等待UI主线程ArkTS环境中执行的API调用结果，需要在这些C++线程上创建ArkTS执行环境和直接调用API，并且可能需要在C++线程之间对Sendable对象进行共享和操作。
为了支持此类场景，需要实现在C++线程上创建调用ArkTS的能力，其次还需要对Sendable对象进行多线程共享和操作。
在C++线程上调用ArkTS能力
关于如何使用Node-API接口在C++线程创建ArkTS运行环境并调用，具体请见使用Node-API接口创建ArkTS运行时环境。
核心代码片段如下所示：
ArkTS文件定义
```typescript
// SendableObjTest.ets
@Sendable
export class SendableObjTest {
static newSendable() {
return 1024;
}
}
```
Naitve实现加载ArkTS模块的能力
主要分为四个步骤：创建执行环境、加载模块、查找并调用模块（也可以直接通过Node-API接口创建Sendable对象）的函数和最后销毁执行环境。其中第二步加载模块具体可见使用Node-API接口进行模块加载，第三步查找并调用函数及更多Node-API接口能力可见Node-API。
在C++线程之间操作Sendable共享对象
实现在C++调用ArkTS能力之后，需要通过序列化和反序列化跨线程传递。因为napi_value不是多线程安全的，所以不能直接在多线程之间直接共享napi_value变量。
下面代码例子说明了如何序列化和反序列化传递对象，注意因为Sendable共享对象是引用传递，所以序列化不会产生另外一份拷贝数据，而是直接传递对象引用到反序列化线程，所以在性能上相比非Sendable对象的序列化和反序列化更为高效。
ArkTS文件定义
```typescript
// SendableObjTest.ets
@Sendable
export class SendableObjTest {
static newSendable() {
return 1024;
}
}
```
Naitve实现两个线程的序列化反序列化Sendable的逻辑
UI主线程发起调用
```typescript
// Index.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
import { SendableObjTest } from './SendableObjTest'
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
SendableObjTest.newSendable()
hilog.info(0x0000, 'testTag', 'Test send Sendable begin');
testNapi.testSendSendable();
hilog.info(0x0000, 'testTag', 'Test send Sendable end');
})
}
.width('100%')
}
.height('100%')
}
}
```
整个过程主要包括的逻辑实现为：
1.  在入口main函数所在的UI主线程创建ArkTS运行环境，并发起一个C++子线程创建Sendable对象保存到result中，然后将result引用的Sendable对象序列化到一个全局序列化数据serializationData中。
2.  当这些流程完成后，发起另外一个C++子线程，并在这个新的线程中创建ArkTS运行环境。然后再通过反序列化接口从serializationData中反序列化出UI主线程创建的Sendable对象，并保存到result中，从而实现了Sendable对象的跨C++线程传递。反序列化完成后，需要销毁反序列化数据避免内存泄露。这时UI主线程和子线程都同时持有这个Sendable共享对象，即可通过Node-API进行对象操作，比如读写或者传递到ArkTS层等。 操作对象需要符合Sendable对象的规则，具体可见Sendable使用规则与约束。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-cross-language-interaction-V14
爬取时间: 2025-04-27 23:00:25
来源: Huawei Developer
除了支持使用ArkTS进行开发外，开发者还可以通过使用Node-API实现ArkTS和C/C++（Native）的跨语言交互。
其中，HarmonyOS的Node-API，是对Node.js社区的拓展版本，与Node.js社区的Node API并不完全兼容。
在使用Node-API进行跨语言开发流程中，开发者可以根据Node-API支持的数据类型和接口情况，进行Native能力的开发和封装，通过导入模块的方式在ArkTS侧导入Native模块后，即可实现跨语言交互。
Node-API扩展能力接口进一步扩展了NAPI的功能，提供了一些额外的接口，用于在NAPI模块中与ArkTS进行更灵活的交互和定制，这些接口可以用于创建自定义ArkTS对象等场景。同时，开发者还可参考Node-API开发规范和Node-API常见问题高效地进行跨语言功能开发。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-runtime-V14
爬取时间: 2025-04-27 23:00:39
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-runtime-overview-V14
爬取时间: 2025-04-27 23:00:52
来源: Huawei Developer
ArkTS运行时是HarmonyOS上应用默认语言运行时，运行着ArkTS、TS、JS语言的字节码和相关标准库，支持解释器、AOT和JIT高效执行方式，并提供完善的跨语言调用接口实现Node-API，支持多语言混合开发。
ArkTS Runtime主要由四个子系统组成：
-  Core Subsystem：主要由与语言无关的基础运行库组成，包括承载字节码的File组件、支持Debugger的Tooling组件、负责适配系统调用的Base库组件等。
-  Execution Subsystem：包含执行方舟字节码的解释器、快速路径内联缓存以及文件模块化管理运行。
-  Compiler Subsystem：包含Stub编译器、基于IR的编译优化框架、AOT静态编译器和JIT动态编译器（实验中）。
-  Runtime subsystem：包含以下ArkTS/TS/JS运行相关的模块。 内存管理：对象分配器与垃圾回收器（并发标记和部分内存压缩的CMS-GC和Partial-Compressing-GC）。 分析工具：DFX工具、cpu和heap的profiling工具。 并发管理：Actor并发模型中的abc文件管理器。 标准库：ECMAScript规范定义的标准库、高效的container容器库与对象模型。 其他：异步工作队列、跟C++交互的Node-API接口等。
-  内存管理：对象分配器与垃圾回收器（并发标记和部分内存压缩的CMS-GC和Partial-Compressing-GC）。
-  分析工具：DFX工具、cpu和heap的profiling工具。
-  并发管理：Actor并发模型中的abc文件管理器。
-  标准库：ECMAScript规范定义的标准库、高效的container容器库与对象模型。
-  其他：异步工作队列、跟C++交互的Node-API接口等。
-  内存管理：对象分配器与垃圾回收器（并发标记和部分内存压缩的CMS-GC和Partial-Compressing-GC）。
-  分析工具：DFX工具、cpu和heap的profiling工具。
-  并发管理：Actor并发模型中的abc文件管理器。
-  标准库：ECMAScript规范定义的标准库、高效的container容器库与对象模型。
-  其他：异步工作队列、跟C++交互的Node-API接口等。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/gc-introduction-V14
爬取时间: 2025-04-27 23:01:06
来源: Huawei Developer
GC（全称 Garbage Collection），即垃圾回收。在计算机领域，GC就是找到内存中的垃圾，释放和回收内存空间。当前主流编程语言实现的GC算法主要分为两大类：引用计数和对象追踪（即Tracing GC）。
GC算法简述
GC的类型
引用计数
当一个对象A被另一个对象B指向时，A引用计数+1；反之当该指向断开时，A引用计数-1。当A引用计数为0时，回收对象A。
比如以上代码中，对象parent被另一个对象child持有，对象parent引用计数加1，同时child也被parent持有，对象child引用计数也加1，这就是循环引用。一直到main函数结束后，对象parent和child依然无法释放，导致内存泄漏。
对象追踪
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170234.10658686460487167678674475285682:50001231000000:2800:C501E36925F4F1DCE983119C9BB27F177389470069BEDD221A1217A62436A605.png)
根对象包括程序运行中的栈内对象，全局对象等当前时刻一定存活的对象，同时被根对象所引用的对象也是存活状态，由此可以通过遍历得到所有存活的对象。如图所示，从根对象开始遍历对象以及对象的域，所有可达的对象打上标记（蓝色），即为活对象，剩下的不可达对象（黄色）即为垃圾。
引用计数和对象追踪算法各有优劣，但考虑到引用计数存在循环引用的致命性能问题，方舟ArkTS运行时选择基于对象追踪（即Tracing GC）算法来设计GC算法。
对象追踪的三种类型
对象追踪算法通过遍历对象图标记出垃圾，而根据垃圾回收方式的不同，对象追踪可以分为三种基本类型：标记-清扫回收、标记-复制回收、标记-整理回收。以下图示中蓝色标记为可达对象，黄色标记为不可达对象。
标记-清扫回收
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170234.43530354604483247225998754521495:50001231000000:2800:ED57766E666A83C29D21FD48652A16803B7CCA631C695426B650BC4964C0F67B.png)
完成对象图遍历后，将不可达对象内容擦除，并放入一个空闲队列，用于下次对象的再分配。
该种回收方式不需要搬移对象，所以回收效率非常高。但由于回收的对象内存地址不一定连续，所以该回收方式最大的缺点是会导致内存空间碎片化，降低内存分配效率，极端情况下甚至会出现还有大量内存的情况下分配不出一个比较大的对象的情况
标记-复制回收
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170234.47840941658960554094394077322479:50001231000000:2800:46BBA608307A2209C6C6C84198820BB0B1353DFD856F8CF351716B21E0E7B9B9.png)
在对象图的遍历过程中，将找到的可达对象直接复制到一个全新的内存空间中。遍历完成后，一次将旧的内存空间全部回收。
显然，这种方式可以解决内存碎片的问题，且通过一次遍历便完成整个GC过程，效率较高。但同时在极端情况下，这种回收方式需要预留一半的内存空间，以确保所有活的对象能被拷贝，空间利用率较低。
标记-整理回收
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170234.89973422453697073523652392967898:50001231000000:2800:42A85119B6F56E68584BF6BB899D7F5C8D8D10C81AEC35E59029B58DEB6A88B4.png)
完成对象图遍历后，将可达对象（蓝色）往本区域（或指定区域）的头部空闲位置复制，然后将已经完成复制的对象回收整理到空闲队列中。
这种回收方式既解决了“标记-清扫回收”引入的大量内存空间碎片的问题，又不需要像“标记-复制回收”那样浪费一半的内存空间，但是性能上开销比“标记-复制回收”稍大一些。
HPP GC
HPP GC（High Performance Partial Garbage Collection）,即高性能部分垃圾回收，其中“High Performance”主要体现在三方面，分代模型、混合算法和GC流程优化。在算法方面，HPP GC会根据不同对象区域、采取不同的回收方式。
分代模型
方舟JS运行时采用传统的分代模型，将对象进行分类。考虑到大多数新分配的对象都会在一次GC之后被回收，而大多数经过多次GC之后依然存活的对象会继续存活，方舟JS运行时将对象划分为年轻代对象和老年代对象，并将对象分配到不同的空间。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170234.74926409018429509644730094128265:50001231000000:2800:B8B3C3A50732A9B6B935EA6C752731F8221D3547118EB731075B209227CC2B54.png)
方舟JS运行时将新分配的对象直接分配到年轻代（Young Space）的From空间。经过一次GC后依然存活的对象，会进入To空间,然后会交换from和to空间的类型。而经过再次GC后依然存活的对象，会被复制到老年代（Old Space）。
混合算法
HPP GC是一种“部分复制+部分整理+部分清扫”的混合算法，支持根据年轻代对象和老年代对象的不同特点，分别采取不同的回收方式。
-  部分复制 考虑到年轻代对象生命周期较短，回收较为频繁，且年轻代对象大小有限的特点，方舟JS运行时对年轻代对象采用“标记-复制回收”算法。
-  部分整理+部分清扫 根据老年代对象的特点，引入启发式Collection Set（简称CSet）选择算法。此选择算法的基本原理是：在标记阶段对每个区域的存活对象进行大小统计，然后在回收阶段优先选出存活对象少、回收代价小的区域进行对象整理回收，再对剩下的区域进行清扫回收。
具体的回收策略如下：
（注：存活率=存活对象大小/区域大小）
-  根据设定的释放区域个数阈值，选出最终的CSet队列，进行整理回收。
-  对未被选入CSet队列的区域进行清扫回收。
启发式CSet选择算法同时兼顾了 “标记-整理回收”和“标记-清扫回收”这两种算法的优点，既避免了内存碎片问题，也兼顾了性能。
流程优化
HPP GC流程中引入了大量的并发和并行优化，以减少对应用性能的影响。采用了并发+并行标记（Marking）、并发+并行清扫（Sweep）、并行复制/整理（Evacuation）、并行回改（Update）和并发清理（Clear）执行GC任务。
Heap结构及其配置参数
Heap结构
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170234.00647679223788953281087812297468:50001231000000:2800:83F05E3A69E5797ED36F3FE88489479367701184BBB93BD40D41379FB5EB5E80.png)
注：每个空间会有一个或多个region进行分区域管理，region是空间向内存分配器申请的单位。
相关参数
以下参数未提示可配置的均为不可配置项，由系统自行设定。
根据系统分配heap总大小64MB-128MB/128MB-256MB/大于256MB的三个范围，以下参数系统会设置不同的大小。如果表格内范围仅有一个值，则表示该参数值不随heap总大小变化。手机设备heap总大小默认为大于256MB。
开发者可以查看hidebug接口文档，使用相关接口查询内存信息。
堆大小相关参数
| 参数名称 | 范围 | 作用 |
| --- | --- | --- |
| HeapSize | 448MB | 主线程默认堆空间总大小,小内存设备会依据实际内存池大小修正 |
| SemiSpaceSize | 2MB-4MB/2MB-8MB/2MB-16MB | semispace空间大小 |
| NonmovableSpaceSize | 2MB/6MB/64MB | nonmovableSpace空间大小 |
| SnapshotSpaceSize | 512KB | 快照空间大小 |
| MachineCodeSpaceSize | 2MB | 机器码空间大小 |
worker线程堆上限
| 参数名称 | 范围 | 作用 |
| --- | --- | --- |
| HeapSize | 768 MB | work类型线程堆空间大小 |
Semi Space
heap中会生成两个Semi Space供copying使用。
| 参数名称 | 范围 | 作用 |
| --- | --- | --- |
| semiSpaceSize | 2MB-4MB/2MB-8MB/2MB-16MB | semispace空间大小，会根据堆总大小有不同的范围限制 |
| semiSpaceTriggerConcurrentMark | 1M/1.5M/1.5M | 首次单独触发Semi Space的并发mark的界限值，超过该值则触发 |
| semiSpaceStepOvershootSize | 2MB | 允许过冲最大大小 |
Old Space 和 Huge Object Space
初始化时均设定为Heap剩余未分配空间的大小，默认手机设备主线程OldSpaceSize上限接近350MB。
| 参数名称 | 范围 | 作用 |
| --- | --- | --- |
| oldSpaceOvershootSize | 4MB/8MB/8MB | oldSpace允许过冲最大大小 |
其他空间
| 参数名称 | 范围 | 作用 |
| --- | --- | --- |
| defaultReadOnlySpaceSize | 256 KB | ReadOnlySpace默认空间大小 |
| defaultNonMovableSpaceSize | 2 MB/6 MB/64 MB | NonMovableSpace默认空间大小 |
| defaultSnapshotSpaceSize | 512 KB/512 KB/ 4 MB | SnapshotSpace默认空间大小 |
| defaultMachineCodeSpaceSize | 2 MB/2 MB/8 MB | MachineCodeSpace默认空间大小 |
解释器栈大小
| 参数名称 | 范围 | 作用 |
| --- | --- | --- |
| maxStackSize | 128KB | 控制解释器栈帧大小 |
并发参数
| 参数名称 | 值 | 作用 |
| --- | --- | --- |
| gcThreadNum | 7 | gc线程数量，默认为7，可通过gc-thread-num参数自行设定该参数值 |
| MIN_TASKPOOL_THREAD_NUM | 3 | 线程池最小线程数 |
| MAX_TASKPOOL_THREAD_NUM | 7 | 线程池最大线程数 |
注：该线程池主要用于执行GC流程中的并发任务，实际线程池初始化综合参考gcThreadNum以及线程上下限，gcThreadNum为负值时初始化线程池线程数 = CPU核心数/2
其他参数
| 参数名称 | 值 | 作用 |
| --- | --- | --- |
| minAllocLimitGrowingStep | 2M/4M/8M | heap整体重新计算空间大小限制时，控制oldSpace、heapObject和globalNative的最小增长步长 |
| minGrowingStep | 4M/8M/16M | 调整oldSpace的最小增长步长 |
| longPauseTime | 40ms | 判断是否为超长GC界限，超长GC会触发完整GC日志信息打印，方便开发者定位分析。可通过gc-long-paused-time进行配置 |
其他：新增单VM内ArrayBuffer的native总内存上限为4GB
GC流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170234.67412383605088506659123428546872:50001231000000:2800:1B7C8D47FF7E1A3C1CAE3416240E6ADEBD387EBF19E1F7613F8389C1317E21FA.png)
HPP GC的类型
Young GC
Old GC
Full GC
此后的Smart GC或者 IDLE GC 都是在上述三种GC中做选择。
触发策略
空间阈值触发GC
native绑定大小达到阈值触发GC
切换后台触发GC
-  典型日志：app is inBackground，app is not inBackground GC 日志中可区分GCReason::SWITCH_BACKGROUND
执行策略
ConcurrentMark
new space GC前后的阈值调整
第一次OldGC后阈值的调整
第二次及以后的OldGC对old Space/global space阈值调整，以及增长因子的调整
PartialGC的Cset 选择策略
-  典型日志：Select CSet failure: number is too few, "Max evacuation size is 6_MB. The CSet region number: " << selectedRegionNumber;, "Select CSet success: number is " << collectRegionSet_.size();
SharedHeap
SharedHeap结构
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170235.88045261231239576034731549670524:50001231000000:2800:5DD641E2365AD3FC2CF5DB7286D2A8EC9C09560FC4DE1E6B9EA950ABCB509625.png)
注：SharedHeap主要用于线程间共享使用的对象，提高效率并节省内存的产物。共享堆并不单独属于某个线程，保存具有共享价值的对象，存活率会更高，去除了SemiSpace的类型。
特性
Smart GC
特性介绍
在应用性能敏感场景，通过将JS线程(SmartGC对worker线程和taskpool线程不生效)GC触发水线临时调整到JS堆最大值（JS线程默认448MB），尽量避免触发GC导致应用掉帧。如果敏感场景持续时间过久，对象分配已经达到了堆最大值，则还是会触发GC，且这次GC由于积累的对象太多，GC时间会相对较久。
支持敏感场景
当前该特性使能由系统侧进行管控，三方应用暂无接口直接调用。
日志关键词: “SmartGC”
交互流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170235.73488558517227367209022886088048:50001231000000:2800:20BC209542C4E6147233B410B35A7A96078FBAE1651AE8F402D4E3C78729B16B.png)
标记性能敏感场景，在进入和退出性能敏感场景时，在堆上标记，避免不必要的GC，维持高性能表现。
日志解释
开启全量日志
默认情况下详细的GC日志仅在GC耗时超过40ms的情况下才会打印，如果需要开启所有GC执行的日志需要使用命令在设备中开启。
使用样例：
```shell
# 设置开启GC全量日志参数，开启参数为0x905d，关闭GC全量日志，设置为默认值为0x105c
hdc shell param set persist.ark.properties 0x905d
# 重启生效
hdc shell reboot
```
典型日志
以下日志为一次GC完整执行后的统计信息，具体到GC的类型不同会有一些差异。开发者可以在导出的日志文件中搜索关键词[gc]查看GC相关的日志,也可以查看关键词ArkCompiler查看更为全面虚拟机相关的日志。
GC开发者调试接口
以下接口仅供调试使用，非正式对外SDK接口，不应在应用正式版本中使用。
ArkTools.hintGC()
使用参考
```typescript
// 首先需要声明接口
declare class ArkTools {
static hintGC(): void;
}
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
Button("触发HintGC").onClick((event: ClickEvent) => {
ArkTools.hintGC();  //方法内直接调用
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-runtime-module-V14
爬取时间: 2025-04-27 23:01:20
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/module-principle-V14
爬取时间: 2025-04-27 23:01:34
来源: Huawei Developer
为了解决大型、复杂应用开发过程中，部分代码编译时被多次拷贝导致包体积增大、文件依赖、代码与资源共享困难以及单例和全局变量污染等问题，同时为了方便开发者代码编写与功能维护，ArkTS支持应用模块化编译打包运行。
模块化是指将 ArkTS/TS/JS拆分为多个模块（文件或片段），并通过编译工具或运行时机制将这些模块加载、解析、组合并执行的过程。
其中ArkTS支持的模块类型有ets/ts/js文件、 json文件、Native模块，ArkTS中支持ECMAScript模块规范及CommonJS模块规范，此外ArkTS也对加载方式进行了拓展，包含动态加载、延时加载、同步动态加载Native模块、Node-API接口加载文件。
模块化运行加载流程
ArkTS模块化运行根据ECMA规范实现，以后序遍历的方式执行模块：从模块图的最左侧子树开始，执行模块，然后执行它们的同级，然后执行它们的父级。此算法递归运行，直至执行到模块图的根。
以下图为例，每个父节点加载了对应子节点，并按照代码中的import顺序执行同级。下面的模块图文件执行顺序为：D->F->G->E->B->I->H->C->A。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170235.65217922389917378610801198835265:50001231000000:2800:63BAAF68EB1989157D6EB13341F6884F6C4E66FDC8BEAFA879878E2E3E8161A1.png)
其中A文件称为入口文件，即这个文件是一个执行起点。一些内置的加载接口如windowStage.loadContent、路由跳转等页面拉起接口（即不是通过import写法拉起的文件），入参文件都会作为入口文件执行。
以A文件为入口，会加载一整套文件，包含A文件，A文件依赖的文件，这些文件后面依赖的文件，直到各分支叶节点。
ArkTS支持的模块化规范
ECMAScript模块
ECMAScript模块（ECMAScript Modules，后文称ES Module）是JavaScript自ECMAScript6.0之后，从标准层面（ECMAScript® 2025 Language Specification (tc39.es)）实现的模块功能。其模块功能由两个命令组成：export和import。
ArkTS中export和import用法详见ArkTS语言介绍。
CommonJS模块
CommonJS模块是JavaScript社区2009年提出的标准，首先在Node.js采用部分标准并实现。CommonJS将每个文件视为一个模块，通过module变量代表当前模块，module.exports即为该模块对外导出的变量，每个模块还拥有exports变量（exports === module.exports）。
导入导出写法参考下表：
| 加载类型 | 模块导入 | 模块导出（不能把module.exports与exports混用） |
| --- | --- | --- |
| 变量 | const ohos = require('ohos') | exports.add = add module.exports.name = name |
| 变量 | const ohos = require('ohos') | module.exports = add |
| 函数 | const ohos = require('ohos') ohos.fun(); | exports.fun = function foo () {} module.exports.fun = function foo () {} |
exports.add = add
module.exports.name = name
const ohos = require('ohos')
ohos.fun();
exports.fun = function foo () {}
module.exports.fun = function foo () {}
CommonJS模块只适用于第三方包导出，不支持开发者在工程中创建使用。
CommonJS与ES Module支持规格
CommonJS与ES Module互相引用支持规格如下表所示，导入导出语法遵循各自模块的规范写法。
| 互相引用关系 | ES Module 导出 | CommonJS导出 |
| --- | --- | --- |
| ES Module 导入 | 支持 | 支持 |
| CommonJS导入 | 不支持 | 支持 |
ArkTS支持加载的模块类型
ets/ts/js
针对ets/ts/js模块类型的加载遵循ECMAScript模块规范及CommonJS模块规范。
JSON文件
JSON（JavaScript Object Notation），是一种轻量级的数据交互格式，采用完全独立于编程语言的文本格式来存储和表示数据。
JSON文件只能使用default方式导入，如下所示：
Native模块
Native模块（so）的导入导出与加载ets/ts/js语法规格一致。可参考：静态方式加载native模块。
Native模块不支持在CommonJS模块中导入。
示例：
```typescript
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```
ArkTS当前限制：不支持native模块导出和导入同时使用命名空间。
反例：
不建议通过 import * as xxx from 'xxx' 方式进行导入。该方式导入会产生运行时异常，建议使用默认导入。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-dynamic-import-V14
爬取时间: 2025-04-27 23:01:47
来源: Huawei Developer
动态import支持条件延迟加载，支持部分反射功能，可以提升页面的加载速度；动态import支持加载HSP模块/HAR模块/OHPM包/Native库等，并且HAR模块间只有变量动态import时还可以进行模块解耦。
技术适用场景介绍
应用开发的有些场景中，如果希望根据条件导入模块或者按需导入模块，可以使用动态导入代替静态导入。下面是可能会需要动态导入的场景：
业务扩展场景介绍
动态import在业务上除了能实现条件延迟加载，还可以实现部分反射功能。实例如下，HAP动态import HAR包harlibrary，并调用静态成员函数staticAdd()、成员函数instanceAdd()，以及全局方法addHarlibrary()。
```typescript
// harlibrary's src/main/ets/utils/Calc.ets
export class Calc {
public static staticAdd(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am harlibrary in staticAdd, %d + %d = %d', a, b, c);
return c;
}
public instanceAdd(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am harlibrary in instanceAdd, %d + %d = %d', a, b, c);
return c;
}
}
export function addHarlibrary(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am harlibrary in addHarlibrary, %d + %d = %d', a, b, c);
return c;
}
```
```typescript
// harlibrary's Index.ets
export { Calc, addHarlibrary } from './src/main/ets/utils/Calc'
```
```json
// HAP's oh-package.json5
"dependencies": {
"harlibrary": "file:../harlibrary"
}
```
```typescript
// HAP's src/main/ets/pages/Index.ets
import('harlibrary').then((ns:ESObject) => {
ns.Calc.staticAdd(8, 9);  // 调用静态成员函数staticAdd()
let calc:ESObject = new ns.Calc();  // 实例化类Calc
calc.instanceAdd(10, 11);  // 调用成员函数instanceAdd()
ns.addHarlibrary(6, 7);  // 调用全局方法addHarlibrary()
// 使用类、成员函数和方法的字符串名字进行反射调用
let className = 'Calc';
let methodName = 'instanceAdd';
let staticMethod = 'staticAdd';
let functionName = 'addHarlibrary';
ns[className][staticMethod](12, 13);  // 调用静态成员函数staticAdd()
let calc1:ESObject = new ns[className]();  // 实例化类Calc
calc1[methodName](14, 15);  // 调用成员函数instanceAdd()
ns[functionName](16, 17);  // 调用全局方法addHarlibrary()
});
```
动态import实现方案介绍
动态import根据入参是常量还是变量，分成动态import常量表达式和动态import变量表达式两大特性规格。
以下是动态import支持的规格列表：
| 动态import场景 | 动态import详细分类 | 说明 |
| --- | --- | --- |
| 本地工程模块 | 动态import模块内文件路径 | 要求路径以./或../开头 |
| 本地工程模块 | 动态import HSP模块名 | - |
| 本地工程模块 | 动态import HSP模块文件路径 | 暂仅支持动态import常量表达式，不支持动态import变量表达式 |
| 本地工程模块 | 动态import HAR模块名 | - |
| 本地工程模块 | 动态import HAR模块文件路径 | 暂仅支持动态import常量表达式，不支持动态import变量表达式 |
| 远程包 | 动态import远程HAR模块名 | - |
| 远程包 | 动态import ohpm包名 | - |
| API | 动态import @system.* | - |
| API | 动态import @ohos.* | - |
| API | 动态import @arkui-x.* | - |
| 模块Native库 | 动态import libNativeLibrary.so | - |
注：
动态import实现中的关键点
动态import常量表达式
动态import常量表达式是指动态import的入参为常量的场景。下面以HAP引用其他模块或API的示例来说明典型用法。
说明：本文示例代码中Index.ets等路径是按照当前DevEco Studio的模块配置设置，如后续发生变化，请调整位置及其他文件相对路径。
-  HAP常量动态import HAR模块名
```typescript
// HAR's Index.ets
export function add(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
return c;
}
```
-  HAP常量动态import HAR模块文件路径
```typescript
// HAR's Index.ets
export function add(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
return c;
}
```
-  HAP常量动态import HSP模块名
```typescript
// HSP's Index.ets
export function add(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
return c;
}
```
-  HAP常量动态import HSP模块名文件路径
```typescript
// HSP's Index.ets
export function add(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
return c;
}
```
-  HAP常量动态import远程HAR模块名
```typescript
// HAP's src/main/ets/pages/Index.ets
import('@ohos/crypto-js').then((ns:ESObject) => {
console.info('DynamicImport @ohos/crypto-js: ' + ns.CryptoJS.MD5(123456));
});
```
-  HAP常量动态import ohpm包
```typescript
// HAP's src/main/ets/pages/Index.ets
import('json5').then((ns:ESObject) => {
console.info('DynamicImport json5');
});
```
-  HAP常量动态import自己的单文件
```typescript
// HAP's src/main/ets/Calc.ets
export function add(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am a HAP, %d + %d = %d', a, b, c);
return c;
}
```
-  HAP常量动态import自己的Native库
```typescript
// libnativeapi.so's index.d.ts
export const add: (a:number, b:number) => number;
```
-  HAP常量动态import加载API
```typescript
// HAP's src/main/ets/pages/Index.ets
import('@system.app').then((ns:ESObject) => { ns.default.terminate(); });
import('@system.router').then((ns:ESObject) => { ns.default.clear(); });
import('@ohos.curves').then((ns:ESObject) => { ns.default.springMotion(0.555, 0.75, 0.001); });
import('@ohos.matrix4').then((ns:ESObject) => { ns.default.identity(); });
import('@ohos.hilog').then((ns:ESObject) => { ns.default.info(0x0000, 'testTag', '%{public}s', 'DynamicImport @ohos.hilog.'); });
```
动态import变量表达式
DevEco Studio中模块间的依赖关系通过oh-package.json5中的dependencies进行配置。dependencies列表中所有模块默认都会进行安装（本地模块）或下载（远程模块），但是不会默认参与编译。HAP/HSP编译时会以入口文件（一般为Index.ets/ts）开始搜索依赖关系，搜索到的模块或文件才会加入编译。
在编译期，静态import和常量动态import可以被打包工具rollup及其插件识别解析，加入依赖树中，参与到编译流程，最终生成方舟字节码。但是如果是变量动态import，该变量值可能需要进行运算或者外部传入才能得到，在编译态无法解析出其内容，也就无法加入编译。为了将这部分模块/文件加入编译，还需要额外增加一个runtimeOnly的buildOption配置，用于配置动态import的变量实际的模块名或者文件路径。
1. runtimeOnly字段schema配置格式
在HAP/HSP/HAR的build-profile.json5中的buildOption中增加runtimeOnly配置项，仅在通过变量动态import时配置，静态import和常量动态import无需配置；并且，通过变量动态import加载API时也无需配置runtimeOnly。
如下实例说明如何配置通过变量动态import其他模块，以及变量动态import本模块自己的单文件：
```typescript
// 变量动态import其他模块myHar
let harName = 'myHar';
import(harName).then(……);
// 变量动态import本模块自己的单文件src/main/ets/index.ets
let filePath = './Calc';
import(filePath).then(……);
```
对应的runtimeOnly配置：
```typescript
"buildOption": {
"arkOptions": {
"runtimeOnly": {
"packages": [ "myHar" ]  // 配置本模块变量动态import其他模块名，要求与dependencies中配置的名字一致。
"sources": [ "./src/main/ets/utils/Calc.ets" ]  // 配置本模块变量动态import自己的文件路径，路径相对于当前build-profile.json5文件。
}
}
}
```
"runtimeOnly"的"packages"：用于配置本模块变量动态import其他模块名，要求与dependencies中配置的名字一致。
"runtimeOnly"的"sources"：用于配置本模块变量动态import自己的文件路径，路径相对于当前build-profile.json5文件。
2. 使用实例
-  HAP变量动态import HAR模块名
```typescript
// HAR's Index.ets
export function add(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
return c;
}
```
-  HAP变量动态import HSP模块名
```typescript
// HSP's Index.ets
export function add(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
return c;
}
```
-  HAP变量动态import远程HAR模块名
```typescript
// HAP's src/main/ets/pages/Index.ets
let packageName = '@ohos/crypto-js';
import(packageName).then((ns:ESObject) => {
console.info('DynamicImport @ohos/crypto-js: ' + ns.CryptoJS.MD5(123456));
});
```
-  HAP变量动态import ohpm包
```typescript
// HAP's src/main/ets/pages/Index.ets
let packageName = 'json5';
import(packageName).then((ns:ESObject) => {
console.info('DynamicImport json5');
});
```
-  HAP变量动态import自己的单文件
```typescript
// HAP's src/main/ets/Calc.ets
export function add(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am a HAP, %d + %d = %d', a, b, c);
return c;
}
```
-  HAP变量动态import自己的Native库
```typescript
// libnativeapi.so's index.d.ts
export const add: (a:number, b:number) => number;
```
-  HAP变量动态import加载API
```typescript
// HAP's src/main/ets/pages/Index.ets
let packageName = '@system.app';
import(packageName).then((ns:ESObject) => { ns.default.terminate(); });
packageName = '@system.router';
import(packageName).then((ns:ESObject) => { ns.default.clear(); });
packageName = '@ohos.curves';
import(packageName).then((ns:ESObject) => { ns.default.springMotion(0.555, 0.75, 0.001); });
packageName = '@ohos.matrix4';
import(packageName).then((ns:ESObject) => { ns.default.identity(); });
packageName = '@ohos.hilog';
import(packageName).then((ns:ESObject) => { ns.default.info(0x0000, 'testTag', '%{public}s', 'DynamicImport @ohos.hilog.'); });
```
变量动态import加载API时无需配置runtimeOnly。
HAR模块间动态import依赖解耦
当应用包含多个HAR包，且HAR包之间依赖关系比较复杂。在DevEco Studio中配置依赖关系时，可能会形成循环依赖。这时，如果HAR之间的依赖关系中仅有变量动态import，可以将HAR包之间直接依赖关系转移到HAP/HSP中配置，HAR包之间无需配置依赖关系，从而达到HAR包间依赖解耦的目的。如下示意图：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170235.82799291007985261186170982917826:50001231000000:2800:6E33D32E7A47ABCA1D1210CBEBD26BAA78C0CAAB632F643B3CB93D66A787C116.png)
HAR之间依赖关系转移到HAP/HSP后：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170235.45495306853862137536981304135121:50001231000000:2800:3D31F80AA140D76BF79AA620843019B715D1332F80E1119F2AB2A6545EEE0E02.png)
1. 使用限制
-  仅限本地源码HAR包之间形成循环依赖时可使用该规避方案。
-  被转移依赖的HAR之间只能通过变量动态import，不能有静态import或常量动态import。
-  转移依赖时，dependencies和runtimeOnly依赖配置要同时转移。
-  HSP不支持转移依赖。即：HAP->HSP1->HSP2->HSP3，这里的HSP2和HSP3不能转移到HAP上面。
-  转移依赖的整个链路上只能有HAR，不能跨越HSP转移。即：HAP->HAR1->HAR2->HSP->HAR3->HAR4。 HAR1对HAR2的依赖可以转移到HAP上，HAR3对HAR4的依赖可以转移到HSP上，但是，不能将HAR3或HAR4转移到HAP上。
2. 使用实例
下面的实例HAP变量动态import HAR包har1，har1变量动态import另一个HAR包har2。
```json
// HAP's oh-package.json5
"dependencies": {
"har1": "file:../har1"
}
```
```json
// HAP's build-profile.json5
"buildOption": {
"arkOptions": {
"runtimeOnly": {
"packages": [
"har1"  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
]
}
}
}
```
```typescript
// HAP's src/main/ets/pages/Index.ets
let harName = 'har1';
import(harName).then((ns:ESObject) => {
console.info('DynamicImport addHar1 4 + 5 = ' + ns.addHar1(4, 5));
});
```
```json
// har1's oh-package.json5
"dependencies": {
"har2": "file:../har2"
}
```
```json
// har1's build-profile.json5
"buildOption": {
"arkOptions": {
"runtimeOnly": {
"packages": [
"har2"  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
]
}
}
}
```
```typescript
// har1's Index.ets
export { addHar1 } from './src/main/ets/utils/Calc'
```
```typescript
// har1's src/main/ets/utils/Calc.ets
export function addHar1(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am har1, %d + %d = %d', a, b, c);
let harName = 'har2';
import(harName).then((ns:ESObject) => {
console.info('DynamicImport addHar2 4 + 5 = ' + ns.addHar2(4, 5));
});
return c;
}
```
```typescript
// har2's Index.ets
export { addHar2 } from './src/main/ets/utils/Calc'
```
```typescript
// har2's src/main/ets/utils/Calc.ets
export function addHar2(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am har2, %d + %d = %d', a, b, c);
return c;
}
```
har1对har2的依赖dependencies和runtimeOnly配置转移到HAP中，har1不需要配置对har2的dependencies和runtimeOnly配置：
```json
// HAP's oh-package.json5
"dependencies": {
"har1": "file:../har1",
"har2": "file:../har2"
}
```
```json
// HAP's build-profile.json5
"buildOption": {
"arkOptions": {
"runtimeOnly": {
"packages": [
"har1",
"har2"
]
}
}
}
```
```typescript
// HAP's src/main/ets/pages/Index.ets
let harName = 'har1';
import(harName).then((ns:ESObject) => {
console.info('DynamicImport addHar1 4 + 5 = ' + ns.addHar1(4, 5));
});
```
```typescript
// har1's Index.ets
export { addHar1 } from './src/main/ets/utils/Calc'
```
```typescript
// har1's src/main/ets/utils/Calc.ets
export function addHar1(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am har1, %d + %d = %d', a, b, c);
let harName = 'har2';
import(harName).then((ns:ESObject) => {
console.info('DynamicImport addHar2 4 + 5 = ' + ns.addHar2(4, 5));
});
return c;
}
```
```typescript
// har2's Index.ets
export { addHar2 } from './src/main/ets/utils/Calc'
```
```typescript
// har2's src/main/ets/utils/Calc.ets
export function addHar2(a:number, b:number):number {
let c = a + b;
console.info('DynamicImport I am har2, %d + %d = %d', a, b, c);
return c;
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-lazy-import-V14
爬取时间: 2025-04-27 23:02:01
来源: Huawei Developer
随着应用程序功能的不断扩展，冷启动所需的时间显著增长，主要是由于在启动初期加载了大量模块，其中存在大量未被实际执行的冗余文件。这种情形不仅拖延了应用的初始化过程，还造成了资源的无效占用，亟需采取措施精简加载流程，剔除非必需的文件执行，以优化冷启动性能，确保用户体验的流畅性。
-  延迟加载特性在API12版本开始支持。
-  开发者如需在API12上使用lazy import语法，需在工程中配置"compatibleSdkVersionStage": "beta3"，否则将无法通过编译。参考DevEco Studio build-profile.json5配置文件说明。
功能特性
延迟加载特性可使待加载文件在冷启动阶段不被加载，直至应用程序实际运行过程中需要用到这些组件时，才按需同步加载相关文件，从而缩短应用冷启动耗时。
使用方式
开发者可以利用诸如Trace工具或日志记录等手段，来识别冷启动期间未被实际调用的文件，分析方法可参考延迟加载lazy-import使用指导。通过对这些数据的分析，开发者能够精准地定位出启动阶段不必预先加载的文件列表。针对这些文件的调用点，可以直接增加lazy标识。但需要注意的是，后续执行的加载是同步加载，有可能会阻塞任务执行（如点击任务，触发了延迟加载，那么运行时会去执行冷启动未加载的文件，从而增加耗时），因此是否使用lazy需要开发者自行评估。
不推荐开发者盲目增加lazy，同样会增大编译及运行时的识别开销。
场景行为解析
-  使用lazy-import延迟加载。 执行结果为：
```typescript
// main.ets
import lazy { a } from "./mod1";    // "mod1" 未执行
import { c } from "./mod2";         // "mod2" 执行
// ...
console.info("main executed");
while (false) {
let xx = a;
}
// mod1.ets
export let a = "mod1 executed"
console.info(a);
// mod2.ets
export let c = "mod2 executed"
console.info(c);
```
-  同时对同一模块引用lazy-import与原生import。 执行结果为： 如果在main.ets内删除lazy关键字，执行顺序为：
```typescript
// main.ets
import lazy { a } from "./mod1";    // "mod1" 未执行
import { c } from "./mod2";         // "mod2" 执行
import { b } from "./mod1";         // "mod1" 执行
// ...
console.info("main executed");
while (false) {
let xx = a;
}
// mod1.ets
export let a = "mod1 a executed"
console.info(a);
export let b = "mod1 b executed"
console.info(b);
// mod2.ets
export let c = "mod2 c executed"
console.info(c);
```
语法规格
| 语法 | ModuleRequest | ImportName | LocalName | API12是否支持lazy加载 |
| --- | --- | --- | --- | --- |
| import lazy { x } from "mod"; | "mod" | "x" | "x" | 支持 |
| import lazy { x as v } from "mod"; | "mod" | "x" | "v" | 支持 |
-  延迟加载共享模块或依赖路径内包含共享模块。 延迟加载对于共享模块依旧生效，使用限制参考共享模块开发指导。
错误示例
以下写法将引起编译报错。
```typescript
export lazy var v;                  // 编译器提示报错：应用编译报错
export lazy default function f(){}; // 编译器提示报错：应用编译报错
export lazy default function(){};   // 编译器提示报错：应用编译报错
export lazy default 42;             // 编译器提示报错：应用编译报错
export lazy { x };                    // 编译器提示报错：应用编译报错
export lazy { x as v };               // 编译器提示报错：应用编译报错
export lazy { x } from "mod";         // 编译器提示报错：应用编译报错
export lazy { x as v } from "mod";    // 编译器提示报错：应用编译报错
export lazy * from "mod";           // 编译器提示报错：应用编译报错
import lazy v from "mod";           // 编译器提示报错：应用编译报错
import lazy * as ns from "mod";     // 编译器提示报错：应用编译报错
```
与type关键词同时使用将会导致报错。
```typescript
import lazy type { obj } from "./mod";    // 不支持，编译器、应用编译报错
import type lazy { obj } from "./mod";    // 不支持，编译器、应用编译报错
```
不推荐用法
-  在同一ets文件中，期待延迟加载的依赖模块标记不完全。 标记不完全将导致延迟加载失效，并且增加识别延迟加载的开销。
```typescript
// main.ets
import lazy { a } from "./mod1";    // 从"mod1"内获取a对象，标记为延迟加载
import { c } from "./mod2";
import { b } from "./mod1";         // 再次获取"mod1"内属性，未标记lazy，"mod1"默认执行
// ...
```
-  在同一ets文件中，未使用懒加载变量并再次导出，不支持延迟加载变量被re-export导出。 这种方式导出的变量c未在B.ets中使用，文件B.ets不触发执行。在文件A.ets中使用变量c时，该变量未初始化，抛js异常。 执行结果: 执行结果:
```typescript
// A.ets
import { c } from "./B";
console.info(c);
// B.ets
import lazy { c } from "./C";    // 从"C"内获取c对象，标记为延迟加载
export { c }
// C.ets
let c = "c";
export { c }
```
-  暂不支持lazy-import延迟加载kit。
-  开发者需要评估使用延迟加载存在的影响。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/js-apis-load-native-module-V14
爬取时间: 2025-04-27 23:02:15
来源: Huawei Developer
loadNativeModule接口的功能是同步方式动态加载native模块。它的主要目的是在需要某个native模块时才进行加载，从而避免在应用启动时加载不必要的模块。但是使用该接口时会产生加载so耗时，需要开发者自行评估是否会对功能产生影响。
函数说明
| 参数 | 说明 |
| --- | --- |
| moduleName | 加载的模块名 |
moduleName指的是待加载模块所在的HAP下module.json5中配置的名字。
loadNativeModule只局限于在UI主线程中进行模块加载。
该接口功能不论是加载常量字符串还是变量表达式入参，都需要配置依赖。
loadNativeModule支持的场景
| 场景 | 示例 |
| --- | --- |
| 系统库模块 | 加载@ohos.或@system. |
| 应用内native模块 | 加载libNativeLibrary.so |
使用示例
libentry.so的index.d.ts文件如下
1.在加载本地so库时，首先需要在oh-package.json5文件中配置dependencies项
```json
{
"dependencies": {
"libentry.so": "file:../src/main/cpp/types/libentry"
}
}
```
2.其次，还需要在build-profile.json5中进行配置
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
3.用loadNativeModule加载libentry.so，调用函数add

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-import-native-module-V14
爬取时间: 2025-04-27 23:02:28
来源: Huawei Developer
在ES6(ECMAScript6.0)模块设计中，社区使用import语法加载其他文件导出的内容（ECMA规范定义语法规格）。
为支持开发者便捷使用该功能导入native模块(so)导出的内容，ArkTS进行相关适配，并给出以下几种支持写法。
直接导入
在native模块的index.d.ts文件中导出，在文件内直接导入。
具名导入
```typescript
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```
```typescript
// test.ets
import { add } from 'libentry.so'
add(2, 3);
```
默认导入
```typescript
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```
```typescript
// test.ets
import add from 'libentry.so'
add.add(2, 3);
```
命名空间导入
```typescript
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```
```typescript
// test.ets
import * as add from 'libentry.so'
add.add(2, 3);
```
间接导入
转为具名变量导出再导入
```typescript
// test1.ets
import hilog from '@ohos.hilog'
export { hilog }
```
```typescript
// test2.ets
import { hilog } from './test1'
hilog.info(0x000, 'testTag', '%{public}s', 'test');
```
转为命名空间导出再导入
```typescript
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```
```typescript
// test1.ets
export * from 'libentry.so'
```
```typescript
// test2.ets
import { add } from './test1'
add(2, 3);
```
注意：不支持native模块导出和导入同时使用命名空间。
反例：
```typescript
// test1.ets
export * from 'libentry.so'
```
```typescript
// test2.ets
import * as add from 'file1'
// 无法获取add对象
```
动态导入
直接导入
```typescript
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```
```typescript
// test.ets
import('libentry.so').then((ns:ESObject) => {
ns.default.add(2, 3);
})
```
间接导入
```typescript
// test1.ets
import add from 'libentry.so'
export { add }
// test2.ets
import('./test1').then((ns:ESObject) => {
ns.add.add(2, 3);
})
```
注意：不支持动态加载时，导出文件使用命名空间导出。
反例：
```typescript
// test1.ets
export * from 'libentry.so'
```
```typescript
// test2.ets
import('./test1').then((ns:ESObject) => {
// 无法获取ns对象
})
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/load-module-base-nodeapi-V14
爬取时间: 2025-04-27 23:02:42
来源: Huawei Developer
Node-API中的napi_load_module接口的功能是在宿主线程中进行当前hap/hsp包工程内模块的加载，用法场景局限，但传参简单。napi_load_module_with_info可支持宿主线程或子线程内加载har包、hsp包、native模块等多种文件类型，用法更加丰富，但使用时需要标记所加载包的信息。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-module-side-effects-V14
爬取时间: 2025-04-27 23:02:55
来源: Huawei Developer
概述
当使用ArkTS模块化时，模块的加载和执行可能会引发副作用。副作用指的是模块导入时除了导出功能或对象之外，额外的行为或状态变化，这些行为可能影响程序的其他部分，并导致产生非预期的顶层代码执行、全局状态变化、原型链修改、导入内容未定义等问题。
ArkTS模块化导致副作用的场景及优化方式
模块执行顶层代码
副作用产生场景
模块在被导入时，整个模块文件中的顶层代码会立即执行，而不仅仅是导出的部分。这意味着，即使只想使用模块中的某些导出内容，但是任何在顶层作用域中执行的代码也会被运行，从而产生副作用。
```typescript
// module.ets
console.log("Module loaded!"); // 这段代码在导入时会立即执行，可能会导致副作用。
export const data = 1;
// main.ets
import { data } from  './module' // 导入时，module.ets中的console.log会执行，产生输出。
console.log(data);
```
输出内容：
```typescript
Module loaded!
1
```
产生的副作用
即使只需要data，console.log("Module loaded!") 仍会运行，导致开发者可能预期只输出data的值，但却额外输出了“Module loaded!”，影响输出内容。
优化方式
优化方式1：去除顶层代码，只导出需要的内容，避免不必要的代码执行。
```typescript
// module.ets
export const data = 1;
// main.ets
import { data } from  './module'
console.log(data);
```
输出内容：
```typescript
1
```
优化方式2：将可能引发副作用的代码放在函数或方法内部，只有在需要时再执行，而不是在模块加载时立即执行。
```typescript
// module.ets
export function initialize() {
console.log("Module loaded!");
}
export const data = 1;
// main.ets
import { data } from  './module'
console.log(data);
```
输出内容：
```typescript
1
```
修改全局对象
副作用产生场景
顶层代码或导入的模块可能会直接操作全局变量，从而改变全局状态，引发副作用。
```typescript
// module.ets
export let data1 = "data from module"
globalThis.someGlobalVar = 100; // 改变了全局状态
// sideEffectModule.ets
export let data2 = "data from side effect module"
globalThis.someGlobalVar = 200; // 也变了全局状态
// moduleUseGlobalVar.ets
import { data1 } from './module' // 此时可能预期全局变量someGlobalVar的值为100
export function useGlobalVar() {
console.log(data1);
console.log(globalThis.someGlobalVar); // 此时由于main.ets中加载了sideEffectModule模块，someGlobalVar的值已经被改为200
}
// main.ets（执行入口）
import { data1 } from "./module" // 将全局变量someGlobalVar的值改为100
import { data2 } from "./sideEffectModule" // 又将全局变量someGlobalVar的值改为200
import { useGlobalVar } from './moduleUseGlobalVar'
useGlobalVar();
function maybeNotCalledAtAll() {
console.log(data1);
console.log(data2);
}
```
输出内容：
产生的副作用
模块加载时直接改变全局变量globalThis.someGlobalVar的值，影响其他使用该变量的模块或代码。
优化方式
将可能引发副作用的代码放在函数或方法内部，只有在需要时再执行，而不是在模块加载时立即执行。
```typescript
// module.ets
export let data1 = "data from module"
export function changeGlobalVar() {
globalThis.someGlobalVar = 100;
}
// sideEffectModule.ets
export let data2 = "data from side effect module"
export function changeGlobalVar() {
globalThis.someGlobalVar = 200;
}
// moduleUseGlobalVar.ets
import { data1, changeGlobalVar } from './module'
export function useGlobalVar() {
console.log(data1);
changeGlobalVar(); // 在需要的时候执行代码，而不是模块加载时执行。
console.log(globalThis.someGlobalVar);
}
// main.ets（执行入口）
import { data1 } from "./module"
import { data2 } from "./sideEffectModule"
import { useGlobalVar } from './moduleUseGlobalVar'
useGlobalVar();
function maybeNotCalledAtAll() {
console.log(data1);
console.log(data2);
}
```
输出内容：
修改应用级ArkUI组件的状态变量信息
副作用产生场景
顶层代码或导入的模块可能会直接修改应用级ArkUI组件的状态变量信息，从而改变全局状态，引发副作用。
```typescript
// module.ets
export let data = "data from module"
AppStorage.setOrCreate("SomeAppStorageVar", 200); // 修改应用全局的UI状态
// Index.ets
import { data } from "./module" // 将AppStorage中的SomeAppStorageVar改为200
@Entry
@Component
struct Index {
// 开发者可能预期该值为100，但是由于module模块导入，该值已经被修改为200，但开发者可能并不知道值已经被修改
@StorageLink("SomeAppStorageVar") message: number = 100;
build() {
Row() {
Column() {
Text("test" + this.message)
.fontSize(50)
}
.width("100%")
}
.height("100%")
}
}
function maybeNotCalledAtAll() {
console.log(data);
}
```
显示内容：
产生的副作用
模块加载时直接改变AppStorage中SomeAppStorageVar的值，影响其他使用该变量的模块或代码。
ArkUI组件的状态变量信息可以通过一些应用级接口修改，详见ArkUI状态管理接口文档。
优化方式
将可能引发副作用的代码放在函数或方法内部，只有在需要时再执行，而不是在模块加载时立即执行。
```typescript
// module.ets
export let data = "data from module"
export function initialize() {
AppStorage.setOrCreate("SomeAppStorageVar", 200);
}
// Index.ets
import { data } from "./module"
@Entry
@Component
struct Index {
@StorageLink("SomeAppStorageVar") message: number = 100;
build() {
Row() {
Column() {
Text("test" + this.message)
.fontSize(50)
}
.width("100%")
}
.height("100%")
}
}
function maybeNotCalledAtAll() {
console.log(data);
}
```
显示内容：
修改内置全局变量或原型链（ArkTS内禁止修改对象原型与内置方法）
副作用产生场景
某些第三方库或框架可能会修改内置的全局对象或原型链，以便在较旧的浏览器或运行环境中支持现代的JavaScript特性。这可能会影响其他代码的运行。
```typescript
// modifyPrototype.ts
export let data = "data from modifyPrototype"
Array.prototype.includes = function (value) {
return this.indexOf(value) !== -1;
};
// main.ets
import { data } from "./modifyPrototype" // 此时修改了Array的原型链
let arr = [1, 2, 3, 4];
console.log("arr.includes(1) = " + arr.includes(1)); // 此时调用的是modifyPrototype.ts中的Array.prototype.includes方法
function maybeNotCalledAtAll() {
console.log(data);
}
```
产生的副作用
修改内置的全局对象或原型链，影响其他代码运行。
优化方式
导入可能会修改内置的全局对象或原型链的第三方库时，确认该第三方库的行为是符合预期的。
循环依赖
副作用产生场景
ArkTS模块化支持循环依赖，即模块A依赖模块B，同时模块B又依赖模块A。在这种情况下，某些导入的模块可能尚未完全加载，从而导致部分代码在执行时行为异常，产生意外的副作用。
```typescript
// a.ets
import { b } from "./b"
console.log('Module A: ', b);
export const a = 'A';
// b.ets
import { a } from "./a"
console.log('Module B: ', a);
export const b = 'B';
```
输出内容：
产生的副作用
由于模块间相互依赖，模块的执行顺序可能导致导出的内容为空或未定义，影响代码的逻辑流。
优化方式
尽量避免模块间的循环依赖，确保模块的加载顺序是明确和可控的，以避免产生意外的副作用。@security/no-cycle循环依赖检查工具可以辅助检查循环依赖。
延迟加载（lazy import）改变模块执行顺序，可能导致预期的全局变量未定义
副作用产生场景
延迟加载特性可使待加载模块在冷启动阶段不被加载，直至应用程序实际运行过程中需要用到这些模块时，才按需同步加载相关模块，从而缩短应用冷启动耗时。但这也同时会改变模块的执行顺序。
```typescript
// module.ets
export let data = "data from module"
globalThis.someGlobalVar = 100;
// moduleUseGlobalVar.ets
import lazy { data } from "./module"
console.log(globalThis.someGlobalVar); // 此时由于lazy特性，module模块还未执行，someGlobalVar的值为undefined
console.log(data); // 使用到module模块的变量，此时module模块执行，someGlobalVar的值变为100
```
输出内容：
产生的副作用
由于使用到延迟加载（lazy import）特性，会导致模块变量在使用到时再执行对应的模块，模块中的一些全局变量修改行为也会延迟，可能会导致运行结果不符合预期。
优化方式
将可能引发副作用的代码放在函数或方法内部，只有在需要时再执行，而不是在模块加载时立即执行。
```typescript
// module.ets
export let data = "data from module"
export function initialize() {
globalThis.someGlobalVar = 100; // 延迟到函数调用时执行
}
// moduleUseGlobalVar.ets
import lazy { data, initialize } from "./module"
initialize(); // 执行初始化函数，初始化someGlobalVar
console.log(globalThis.someGlobalVar); // 此时someGlobalVar一定为预期的值
console.log(data);
```
输出内容：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-compilation-tool-chain-V14
爬取时间: 2025-04-27 23:03:09
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/compilation-tool-chain-overview-V14
爬取时间: 2025-04-27 23:03:23
来源: Huawei Developer
为了支持ArkTS应用编译，ArkTS编译构建SDK提供一套完整的编译工具链，通过将其部署在Hvigor编译任务的编排工具上，实现将应用的ArkTS/TS/JS源码编译生成方舟字节码文件（*.abc）。
在编译过程中，首先是语法转换阶段，包含了语法检查、UI转换。同时为了源码安全，使用ArkGuard源码混淆工具对源码进行混淆操作，并且在落盘字节码之前判断是否需要进行字节码自定义修改，如果需要则加载自定义修改代码并执行，在生成字节码文件后，使用Disassembler反汇编工具可以查看字节码文件中包含的内容，字节码的具体内容可以参考方舟字节码章节。
ArkTS编译工具链当前主要包括如下功能。
1.  语法检查：检查ArkTS/TS语法正确性。
2.  UI转换：将ArkTS的UI范式语法转换为标准TS语法。
3.  源码混淆：使用ArkGuard源码混淆工具对源码进行混淆，开发者可根据业务需要选择开启。
4.  字节码编译：方舟编译器编译方舟字节码文件（*.abc）。
5.  自定义修改方舟字节码：提供开发者修改字节码能力的入口，在字节码编译落盘前调用。
6.  反汇编：使用Disassembler反汇编工具将字节数据反汇编成可阅读的汇编指令。
流程详情参考下图：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170236.25422749565573843632799590118525:50001231000000:2800:8FA2D9CA14A378583934C614BEE6981CD4359AFDFE3ADF175E01A4A88C90A10A.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-bytecode-V14
爬取时间: 2025-04-27 23:03:36
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-bytecode-overview-V14
爬取时间: 2025-04-27 23:03:50
来源: Huawei Developer
方舟字节码文件是ArkTS/TS/JS编译后的二进制产物，本章节介绍了方舟字节码文件的各个部分，方便开发者深入了解字节码文件内容，从而进行字节码的分析和修改。
-  方舟字节码文件格式：介绍字节码文件中包含的各个部分的结构信息，以及各种结构的存储方式和依赖关系。
-  方舟字节码基本原理：介绍字节码中构成指令的重要概念和具体的指令格式及含义，帮助开发者了解方舟字节码指令，进行指令相关的特性开发工作。
-  方舟字节码函数命名规则：介绍字节码文件中函数名字的字符串的命名规则。
-  编译期自定义修改方舟字节码：介绍如何修改字节码文件的内容。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-bytecode-file-format-V14
爬取时间: 2025-04-27 23:04:04
来源: Huawei Developer
方舟字节码文件是ArkTS/TS/JS编译后的二进制产物。本文详细介绍了方舟字节码文件的格式，旨在帮助开发者深入了解构成字节码的各个部分，从而指导开发者进行字节码的分析和修改工作。
约束
本文仅适用于版本号为12.0.6.0的方舟字节码（版本号为方舟编译器内部保留字段，开发者无需关注）。
字节码文件数据类型
整型
| 名称 | 说明 |
| --- | --- |
| uint8_t | 8-bit无符号整数。 |
| uint16_t | 16-bit无符号整数，采用小端字节序。 |
| uint32_t | 32-bit无符号整数，采用小端字节序。 |
| uleb128 | leb128编码的无符号整数。 |
| sleb128 | leb128编码的有符号整数。 |
字符串
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| utf16_length | uleb128 | 值为len << 1 | is_ascii，其中len是字符串在UTF-16编码中的大小，is_ascii标记该字符串是否仅包含ASCII字符，可能的值是0或1。 |
| data | uint8_t[] | 以'\0'结尾的MUTF-8编码字符序列。 |
TaggedValue
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| tag | uint8_t | 表示数据种类的标记。 |
| data | uint8_t[] | 根据不同的标记，data是不同类型的数据或者为空。 |
TypeDescriptor
TypeDescriptor是类(Class) 名称的格式，由'L'、'_'、ClassName和';'组成：L_ClassName;。其中，ClassName是类的全名，名字中的'.'会被替换为'/'。
字节码文件布局
字节码文件起始于Header结构。文件中的所有结构均可以从Header出发，直接或间接地访问到。字节码文件中结构的引用方式包括偏移量和索引。偏移量是一个32位长度的值，表示当前结构的起始位置在字节码文件中相对于文件头的距离，从0开始计算。索引是一个16位长度的值，表示当前结构在索引区域中的位置，此机制将在IndexSection章节描述。
字节码文件中所有的多字节值均采用小端字节序。
Header
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| magic | uint8_t[8] | 文件头魔数，值必须是'P' 'A' 'N' 'D' 'A' '\0' '\0' '\0'。 |
| checksum | uint32_t | 字节码文件除文件头魔数和本校验字段之外的内容的adler32校验和。 |
| version | uint8_t[4] | 字节码文件的版本号 (Version) 。 |
| file_size | uint32_t | 字节码文件的大小，以字节为单位。 |
| foreign_off | uint32_t | 一个偏移量，指向外部区域。外部区域中仅包含类型为ForeignClass或ForeignMethod的元素。foreign_off指向该区域的第一个元素。 |
| foreign_size | uint32_t | 外部区域的大小，以字节为单位。 |
| num_classes | uint32_t | ClassIndex结构中元素的数量，即文件中定义的Class的数量。 |
| class_idx_off | uint32_t | 一个偏移量，指向ClassIndex。 |
| num_lnps | uint32_t | LineNumberProgramIndex结构中元素的数量，即文件中定义的Line number program的数量。 |
| lnp_idx_off | uint32_t | 一个偏移量，指向LineNumberProgramIndex。 |
| reserved | uint32_t | 方舟字节码文件内部使用的保留字段。 |
| reserved | uint32_t | 方舟字节码文件内部使用的保留字段。 |
| num_index_regions | uint32_t | IndexSection结构中元素的数量，即文件中IndexHeader的数量。 |
| index_section_off | uint32_t | 一个偏移量，指向IndexSection。 |
Version
字节码版本号由4个部分组成，格式为：主版本号.次版本号.特性版本号.编译版本号。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| 主版本号 | uint8_t | 标识整体架构调整引入的字节码文件格式变更。 |
| 次版本号 | uint8_t | 标识局部架构调整或者重大特性调整引入的字节码文件格式变更。 |
| 特性版本号 | uint8_t | 标识中小特性引入的字节码文件格式变更。 |
| 编译版本号 | uint8_t | 标识缺陷修复引入的字节码文件格式变更。 |
ForeignClass
描述字节码文件中的外部类。外部类在其他文件中声明，并在当前字节码文件中被引用。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| name | String | 外部类的名称，命名遵循TypeDescriptor语法。 |
ForeignMethod
描述字节码文件中的外部方法。外部方法在其他文件中声明，并在当前字节码文件中被引用。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| class_idx | uint16_t | 一个指向该方法所从属的类的索引，指向一个在ClassRegionIndex中的位置，该位置的值是一个指向Class或ForeignClass的偏移量。 |
| reserved | uint16_t | 方舟字节码文件内部使用的保留字段。 |
| name_off | uint32_t | 一个偏移量，指向字符串，表示方法名称。 |
| index_data | uleb128 | 方法的MethodIndexData数据。 |
注意：
通过ForeignMethod的偏移量，可以找到适当的IndexHeader以解析class_idx。
ClassIndex
ClassIndex结构的作用是通过名称快速地定位到Class的定义。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| offsets | uint32_t[] | 一个数组，数组中每个元素的值是一个指向Class的偏移量。数组中的元素根据类的名称进行排序，名称遵循TypeDescriptor语法。数组长度由Header中的num_classes指定。 |
Class
在字节码文件中，一个类可以表示方舟字节码的一个源代码文件或者一种内置的Annotation。当表示源代码文件时，类的方法对应源代码文件中的函数，类的字段对应源文件中的内部信息；当表示内置的Annotation时，类中不包含字段与方法。源代码文件中的一个类在字节码文件中表示为一个对应其构造函数的方法。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| name | String | Class的名称，命名遵循TypeDescriptor语法。 |
| reserved | uint32_t | 方舟字节码文件内部使用的保留字段。 |
| access_flags | uleb128 | Class的访问标志，是ClassAccessFlag的组合。 |
| num_fields | uleb128 | Class的字段的数量。 |
| num_methods | uleb128 | Class的方法的数量。 |
| class_data | TaggedValue[] | 不定长度的数组，数组中每个元素都是TaggedValue类型，元素的标记是ClassTag类型，数组中的元素按照标记递增排序（0x00标记除外）。 |
| fields | Field[] | Class的字段的数组，数组中每一个元素都是Field类型。数组长度由num_fields指定。 |
| methods | Method[] | Class的方法的数组，数组中每一个元素都是Method类型。数组长度由num_methods指定。 |
ClassAccessFlag
| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACC_PUBLIC | 0x0001 | 默认属性，方舟字节码中的Class均具备此标志。 |
| ACC_ANNOTATION | 0x2000 | 声明该类为Annotation类型。 |
ClassTag
| 名称 | 值 | 数量 | 格式 | 说明 |
| --- | --- | --- | --- | --- |
| NOTHING | 0x00 | 1 | none | 拥有此标记的TaggedValue，是其所在class_data的最后一项。 |
| SOURCE_LANG | 0x02 | 0-1  | uint8_t | 拥有此标记的TaggedValue的data是0，表示源码语言是ArkTS/TS/JS。 |
| SOURCE_FILE | 0x07 | 0-1 | uint32_t | 拥有此标记的TaggedValue的data是一个偏移量，指向字符串，表示源文件的名称。 |
注意：
ClassTag是class_data中元素 (TaggedValue) 所具备的标记，表头中的“数量”指的是在某一个Class的class_data中拥有此标记的元素出现的次数。
Field
描述字节码文件中的字段。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| class_idx | uint16_t | 一个指向该字段从属的类的索引，指向一个在ClassRegionIndex中的位置，该位置的值是Type类型，是一个指向Class的偏移量。 |
| type_idx | uint16_t | 一个指向定义该字段的类型的索引，指向一个在ClassRegionIndex中的位置，该位置的值是Type类型。 |
| name_off | uint32_t | 一个偏移量，指向字符串，表示字段的名称。 |
| reserved | uleb128 | 方舟字节码文件内部使用的保留字段。 |
| field_data | TaggedValue[] | 不定长度的数组，数组中每个元素都是TaggedValue类型，元素的标记是FieldTag类型，数组中的元素按照标记递增排序（0x00标记除外）。 |
注意：
通过Field的偏移量，可以找到适当的IndexHeader以解析class_idx和type_idx。
FieldTag
| 名称 | 值 | 数量 | 格式 | 说明 |
| --- | --- | --- | --- | --- |
| NOTHING | 0x00 | 1 | none | 拥有此标记的TaggedValue，是其所在field_data的最后一项。 |
| INT_VALUE | 0x01 | 0-1 | sleb128 | 拥有此标记的TaggedValue的data的类型为boolean、byte、char、short 或 int。 |
| VALUE | 0x02 | 0-1 | uint32_t | 拥有此标记的TaggedValue的data的类型为Value formats中的FLOAT或ID。 |
注意：
FieldTag是field_data中元素 (TaggedValue) 所具备的标记，表头中的“数量”指的是在某一个Field的field_data中拥有此标记的元素出现的次数。
Method
描述字节码文件中的方法。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| class_idx | uint16_t | 一个指向该方法所从属的类的索引，指向一个在ClassRegionIndex中的位置，该位置的值是Type类型，是一个指向Class的偏移量。 |
| reserved | uint16_t | 方舟字节码文件内部使用的保留字段。 |
| name_off | uint32_t | 一个偏移量，指向字符串，表示方法名称。 |
| index_data | uleb128 | 方法的MethodIndexData数据。 |
| method_data | TaggedValue[] | 不定长度的数组，数组中每个元素都是TaggedValue类型，元素的标记是MethodTag类型，数组中的元素按照标记递增排序（0x00标记除外）。 |
注意：
通过Method的偏移量，可以找到适当的IndexHeader以解析class_idx。
MethodIndexData
MethodIndexData是一个无符号32位整数，划分为3个部分。
| 位 | 名称 | 格式 | 说明 |
| --- | --- | --- | --- |
| 0 - 15 | header_index | uint16_t | 指向一个在IndexSection中的位置，该位置的值是IndexHeader。通过IndexHeader可以找到该方法引用的所有方法 (Method) 、字符串或字面量数组 (LiteralArray) 的偏移量。 |
| 16 - 23 | function_kind | uint8_t | 表示方法的函数类型 (FunctionKind) 。 |
| 24 - 31 | reserved | uint8_t | 方舟字节码文件内部使用的保留字段。 |
FunctionKind
| 名称 | 值 | 说明 |
| --- | --- | --- |
| FUNCTION | 0x1 | 普通函数。 |
| NC_FUNCTION | 0x2 | 普通箭头函数。 |
| GENERATOR_FUNCTION | 0x3 | 生成器函数。 |
| ASYNC_FUNCTION | 0x4 | 异步函数。 |
| ASYNC_GENERATOR_FUNCTION | 0x5 | 异步生成器函数。 |
| ASYNC_NC_FUNCTION | 0x6 | 异步箭头函数。 |
| CONCURRENT_FUNCTION | 0x7 | 并发函数。 |
MethodTag
| 名称 | 值 | 数量 | 格式 | 说明 |
| --- | --- | --- | --- | --- |
| NOTHING | 0x00 | 1 | none | 拥有此标记的TaggedValue，是其所在method_data的最后一项。 |
| CODE | 0x01 | 0-1  | uint32_t | 拥有此标记的TaggedValue的data是一个偏移量，指向Code，表示方法的代码段。 |
| SOURCE_LANG | 0x02 | 0-1 | uint8_t | 拥有此标记的TaggedValue的data是0，表示源码语言是ArkTS/TS/JS。 |
| DEBUG_INFO | 0x05 | 0-1 | uint32_t | 拥有此标记的TaggedValue的data是一个偏移量，指向DebugInfo，表示方法的调试信息。 |
| ANNOTATION | 0x06 | >=0 | uint32_t | 拥有此标记的TaggedValue的data是一个偏移量，指向Annotation， 表示方法的注解。 |
注意：
MethodTag是method_data中元素 (TaggedValue) 所具备的标记，表头中的“数量”指的是在某一个Method的method_data中拥有此标记的元素出现的次数。
Code
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| num_vregs | uleb128 | 寄存器的数量，存放入参和默认参数的寄存器不计算在内。 |
| num_args | uleb128 | 入参和默认参数的总数量。 |
| code_size | uleb128 | 所有指令的总大小，以字节为单位。 |
| tries_size | uleb128 | try_blocks数组的长度，即TryBlock的数量。 |
| instructions | uint8_t[] | 所有指令的数组。 |
| try_blocks | TryBlock[] | 一个数组，数组中每一个元素都是TryBlock类型。 |
TryBlock
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| start_pc | uleb128 | TryBlock的第一条指令距离其所在Code的instructions的起始位置的偏移量。 |
| length | uleb128 | TryBlock的大小，以字节为单位。 |
| num_catches | uleb128 | 与TryBlock关联的CatchBlock的数量，值为1。 |
| catch_blocks | CatchBlock[] | 与TryBlock关联的CatchBlock的数组，数组中有且仅有一个可以捕获所有类型的异常的CatchBlock。 |
CatchBlock
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| type_idx | uleb128 | 值是0，表示此CatchBlock块捕获了所有类型的异常。 |
| handler_pc | uleb128 | 异常处理逻辑的第一条指令的程序计数器。 |
| code_size | uleb128 | 此CatchBlock的大小，以字节为单位。 |
Annotation
描述一个注解结构。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| class_idx | uint16_t | 一个指向当前Annotation所从属的类的索引，指向一个在ClassRegionIndex中的位置，该位置的值是Type类型，是一个指向Class的偏移量。 |
| count | uint16_t | elements数组的长度。 |
| elements | AnnotationElement[] | 一个数组，数组的每个元素都是AnnotationElement类型。 |
| element_types | uint8_t[] | 一个数组，数组的每个元素都是AnnotationElementTag类型，用于描述一个AnnotationElement。每个元素在element_types数组中的位置和其对应的AnnotationElement在elements数组中的位置一致。 |
注意：
通过Annotation的偏移量，可以找到适当的IndexHeader以解析class_idx。
AnnotationElementTag
| 名称 | 标记 |
| --- | --- |
| u1 | '1' |
| i8 | '2' |
| u8 | '3' |
| i16 | '4' |
| u16 | '5' |
| i32 | '6' |
| u32 | '7' |
| i64 | '8' |
| u64 | '9' |
| f32 | 'A' |
| f64 | 'B' |
| string | 'C' |
| method | 'E' |
| annotation | 'G' |
| literalarray | '#' |
| unknown | '0' |
AnnotationElement
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| name_off | uint32_t | 一个偏移量，指向字符串，表示注解元素的名称。 |
| value | uint32_t | 注解元素的值，若值的宽度不超过32位，则此处存储值本身。否则，此处存储的值为指向Value formats格式的偏移量。 |
Value formats
不同的值类型，有不同的值编码格式，包括INTEGER, LONG, FLOAT, DOUBLE, ID。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| INTEGER | uint32_t | 有符号的四字节整数值。 |
| LONG | uint64_t | 有符号的八字节整数值。 |
| FLOAT | uint32_t | 四字节位模式，向右零扩展，系统会将其解译为 IEEE754 32 位浮点值。 |
| DOUBLE | uint64_t | 八字节位模式，向右零扩展，系统会将其解译为 IEEE754 64 位浮点值。 |
| ID | uint32_t | 四字节位模式，表示文件中某个结构的偏移量。 |
LineNumberProgramIndex
行号程序索引 (LineNumberProgramIndex) 结构是一个数组，便于使用更紧凑的索引访问行号程序 (Line number program) 。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| offsets | uint32_t[] | 一个数组，数组中每个元素的值是一个偏移量，指向一个行号程序。数组长度由Header中的num_lnps指定。 |
DebugInfo
调试信息 (DebugInfo) 包含方法的程序计数器与源代码中的行列号之间的映射以及有关局部变量的信息。调试信息的格式由DWARF调试信息格式第3版（见第6.2项）的内容演变形成。基于状态机 (State machine) 的执行模型对行号程序 (Line number program)进行解释，可得到映射和局部变量信息编码。为对不同方法的相同行号程序进行去重，程序中引用的所有常量都被移动到了常量池 (Constant pool) 中。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| line_start | uleb128 | 状态机的行号寄存器的初始值。 |
| num_parameters | uleb128 | 入参和默认参数的总数量。 |
| parameters | uleb128[] | 存放方法入参的名称的数组，数组长度是num_parameters。每一个元素的值是字符串的偏移量或者0，如果是0，则代表对应的参数不具有名称。 |
| constant_pool_size | uleb128 | 常量池的大小，以字节为单位。 |
| constant_pool | uleb128[] | 存放常量池数据的数组，数组长度是constant_pool_size。 |
| line_number_program_idx | uleb128 | 一个索引，指向一个在LineNumberProgramIndex中的位置，该位置的值是一个指向Line number program的偏移量。Line number program的长度可变，以END_SEQUENCE操作码结束。 |
Constant pool
常量池 (Constant pool) 是DebugInfo中存放常量的结构。很多方法都具有相似的行号程序，其区别仅在于变量名、变量类型和文件名。为了对这类行号程序进行去重，程序中引用的所有常量都存储在常量池。在解释程序时，状态机维护一个指向常量池的指针。当状态机解释一条需要常量参数的指令时，会从内存常量池指针指向的位置读取值，然后递增指针。
State machine
状态机 (State machine) 的作用是产生DebugInfo信息。状态机中有以下的寄存器：
| 名称 | 初始值 | 说明 |
| --- | --- | --- |
| address | 0 | 程序计数器（指向方法的某个指令），只能单调递增。 |
| line | DebugInfo的属性line_start的值 | 无符号整数，对应源码中的行号。所有的行都是从1开始编号，因此寄存器的值不能小于1。 |
| column | 0 | 无符号整数，对应源码中的列号。 |
| file | class_data（参见Class）中SOURCE_FILE标记的值，或者0 | 一个偏移量，指向字符串，表示源文件的名称。如果没有文件名信息（Class中没有SOURCE_FILE标记），那么寄存器的值是0。 |
| source_code | 0 | 一个偏移量，指向字符串，表示源文件的源码。如果没有源码信息，那么寄存器的值是0。 |
| constant_pool_ptr | DebugInfo中常量池的第一个字节的地址 | 指向当前常量值的指针。 |
Line number program
一个行号程序 (Line number program) 由指令组成。每条指令都包含一个字节的操作码以及可选参数。根据操作码的不同，参数的值可能被编码在指令中（称为指令参数），或者需要从常量池中获取（称为常量池参数）。
| 操作码 | 值 | 指令参数 | 常量池参数 | 参数说明 | 说明 |
| --- | --- | --- | --- | --- | --- |
| END_SEQUENCE | 0x00 |   |   |   | 标记行号程序的结束。 |
| ADVANCE_PC | 0x01 |   | uleb128 addr_diff | addr_diff：address寄存器的值待增加的数值 | address寄存器中的值加上addr_diff，指向下一个地址，而不生成位置条目。 |
| ADVANCE_LINE | 0x02 |   | sleb128 line_diff | line_diff：line寄存器的值待增加的数值 | line寄存器中的值加上line_diff，指向下一个行位置，而不生成位置条目。 |
| START_LOCAL | 0x03 | sleb128 register_num | uleb128 name_idx uleb128 type_idx  | register_num：将包含局部变量的寄存器 name_idx：一个偏移量，指向字符串，表示变量的名称 type_idx：一个偏移量，指向字符串，表示变量的类型  | 在当前地址中引入一个带有名称和类型的局部变量。将要包含这个变量的寄存器的编号被编码在指令中。如果寄存器的编号是-1，则意味着这个是累加器寄存器。name_idx和type_idx的值可能是0，如果是0，则代表着对应的信息是不存在的。 |
| START_LOCAL_EXTENDED | 0x04 | sleb128 register_num | uleb128 name_idx uleb128 type_idx uleb128 sig_idx  | register_num：将包含局部变量的寄存器 name_idx：一个偏移量，指向字符串，表示变量的名称 type_idx：一个偏移量，指向字符串，表示变量的类型 sig_idx：一个偏移量，指向字符串，表示变量的签名  | 在当前地址中引入一个带有名称、类型和签名的局部变量。将要包含这个变量的寄存器的编号被编码在指令中。如果寄存器的编号是-1，则意味着这个是累加器寄存器。name_idx、type_idx和sig_idx的值可能是0，如果是0，则代表着对应的信息是不存在的。 |
| END_LOCAL | 0x05 | sleb128 register_num |   | register_num：包含局部变量的寄存器 | 在当前地址将指定寄存器中的局部变量标记为超出范围。寄存器的编号为-1，则意味着是累加器寄存器。 |
| SET_FILE | 0x09 |   | uleb128 name_idx | name_idx：一个偏移量，指向字符串，表示文件的名称 | 设置file寄存器的值。name_idx的值可能是0，如果是0，则代表着对应的信息是不存在的。 |
| SET_SOURCE_CODE | 0x0a |   | uleb128 source_idx | source_idx：一个偏移量，指向字符串，表示文件的源码 | 设置source_code寄存器的值。source_idx的值可能是0，如果是0，则代表着对应的信息是不存在的。 |
| SET_COLUMN | 0x0b |   | uleb128 column_num | column_num：待设置的列号 | 设置column寄存器的值，并生成一个位置条目。 |
| 特殊操作码 | 0x0c..0xff |   |   |   | 使 line 和 address 寄存器指向下一个地址，并生成一个位置条目。详情参阅下文中的说明。 |
uleb128 name_idx
uleb128 type_idx
register_num：将包含局部变量的寄存器
name_idx：一个偏移量，指向字符串，表示变量的名称
type_idx：一个偏移量，指向字符串，表示变量的类型
uleb128 name_idx
uleb128 type_idx
uleb128 sig_idx
register_num：将包含局部变量的寄存器
name_idx：一个偏移量，指向字符串，表示变量的名称
type_idx：一个偏移量，指向字符串，表示变量的类型
sig_idx：一个偏移量，指向字符串，表示变量的签名
对于值在0x0c和0xff（含）之间的特殊操作码，状态机按照以下步骤将line和address寄存器移动一小部分，然后生成一个新的位置条目（参见DWARF调试信息格式第3版第6.2.5.1项 Special Opcodes）：
| 步骤序号 | 操作 | 说明 |
| --- | --- | --- |
| 1 | adjusted_opcode = opcode - OPCODE_BASE | 计算调整后的操作码。OPCODE_BASE的值是0x0c，是第一个特殊操作码。 |
| 2 | address += adjusted_opcode / LINE_RANGE | 增加address寄存器中的值。LINE_RANGE的值是15，用来计算行号信息的变化。 |
| 3 | line += LINE_BASE + (adjusted_opcode % LINE_RANGE) | 增加line寄存器中的值。LINE_BASE的值是-4，是最小的行号增量值；最大的行号增量值是LINE_BASE + LINE_RANGE - 1。 |
| 4 |   | 生成一个新的位置条目。 |
注意：
“特殊操作码”是通过此公式计算得到：(line_increment - LINE_BASE) + (address_increment * LINE_RANGE) + OPCODE_BASE。
IndexSection
通常情况下，字节码文件的各个结构使用32位偏移量来引用，当一个结构引用另一个结构时，需要在当前结构中记录被引用结构的32位偏移量。为了减小文件体积，字节码文件被分割成多个索引区域 (Index region)，每个索引区域内的结构使用16位索引。IndexSection结构描述了索引区域的集合。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| headers | IndexHeader[] | 一个数组，数组中每个元素是IndexHeader类型。数组中的元素根据区域的起始偏移量进行排序。数组长度由Header中的num_index_regions指定。 |
IndexHeader
每个IndexHeader结构描述一个索引区域。每个索引区域都有两类索引：指向Type的索引和指向方法、字符串或者字面量数组的索引。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| start_off | uint32_t | 该区域的起始偏移量。 |
| end_off | uint32_t | 该区域的结束偏移量。 |
| class_region_idx_size | uint32_t | 该区域的ClassRegionIndex中元素的数量，最大值为65536。 |
| class_region_idx_off | uint32_t | 一个偏移量，指向ClassRegionIndex。 |
| method_string_literal_region_idx_size | uint32_t | 该区域的MethodStringLiteralRegionIndex中元素的数量，最大值为65536。 |
| method_string_literal_region_idx_off | uint32_t | 一个偏移量，指向MethodStringLiteralRegionIndex。 |
| reserved | uint32_t | 方舟字节码文件内部使用的保留字段。 |
| reserved | uint32_t | 方舟字节码文件内部使用的保留字段。 |
| reserved | uint32_t | 方舟字节码文件内部使用的保留字段。 |
| reserved | uint32_t | 方舟字节码文件内部使用的保留字段。 |
ClassRegionIndex
ClassRegionIndex结构的作用是允许通过更紧凑的索引，找到对应的Type。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| types | Type[] | 一个数组，数组中每个元素都是Type类型。数组长度由IndexHeader中的class_region_idx_size指定。 |
Type
表示一个基本类型编码或一个指向Class的偏移量，是一个32位的值。
基本类型采用以下方式编码：
| 类型 | 编码 |
| --- | --- |
| u1 | 0x00 |
| i8 | 0x01 |
| u8 | 0x02 |
| i16 | 0x03 |
| u16 | 0x04 |
| i32 | 0x05 |
| u32 | 0x06 |
| f32 | 0x07 |
| f64 | 0x08 |
| i64 | 0x09 |
| u64 | 0x0a |
| any | 0x0c |
MethodStringLiteralRegionIndex
MethodStringLiteralRegionIndex结构的作用是允许通过更紧凑的索引，找到对应的方法、字符串或者字面量数组。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| offsets | uint32_t[] | 一个数组，数组中每个元素的值是一个偏移量，指向方法、字符串或者字面量数组。数组长度由IndexHeader中的method_string_literal_region_idx_size指定。 |
LiteralArray
描述字节码文件中的字面量数组。
| 名称 | 格式 | 说明 |
| --- | --- | --- |
| num_literals | uint32_t | literals数组的长度。 |
| literals | Literal[] | 一个数组，数组的每个元素都是Literal类型。 |
Literal
描述字节码文件中的字面量，根据字面量值的字节数的不同，有四种编码格式。
| 名称 | 格式 | 对齐方式 | 说明 |
| --- | --- | --- | --- |
| ByteOne | uint8_t | 1个字节 | 单字节的值。 |
| ByteTwo | uint16_t | 2个字节 | 双字节的值。 |
| ByteFour | uint32_t | 4个字节 | 四字节的值。 |
| ByteEight | uint64_t | 8个字节 | 八字节的值。 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-bytecode-fundamentals-V14
爬取时间: 2025-04-27 23:04:18
来源: Huawei Developer
总体设计
概述
方舟字节码（Ark Bytecode），是由方舟编译器编译ArkTS/TS/JS生成的，提供给方舟运行时解释执行的二进制文件，字节码中的主要内容是方舟字节码指令。
本文旨在介绍方舟字节码指令相关的设计，将在后续章节中对构成指令的重要概念和具体的指令格式及含义进行说明，帮助开发者了解方舟字节码指令，指导开发者进行指令相关的特性开发工作。
一条方舟字节码指令，由操作码（指令的名称）和指令入参列表组成。操作码包含无前缀的操作码和有前缀的操作码两种情况。寄存器、立即数以及string id/method id/literal id，均可以作为指令的入参，除此之外，部分指令中使用累加器作为默认参数。
方舟字节码中，除寄存器和累加器之外，还存在全局变量、模块（module）命名空间和模块变量、词法环境和词法变量、补丁变量4种值存储方式。指令可以使用这4种储值位置中的值作为入参。
术语和约束
术语
本文涉及的术语清单：
| 术语 | 说明 |
| --- | --- |
| acc | accumulator，累加器，方舟字节码中一个特殊的寄存器 |
| bit | 一个比特，本文中用位表示 |
| hole | 还未进行初始化的对象或变量 |
| id | index，索引，是string id/method id/literal id的总称 |
| string id | string index，16位的数字，用于索引到对应的字符串 |
| method id | method index，16位的数字，用于索引到对应的方法 |
| literal id | literal index，16位的数字，用于索引到对应的字面量数组 |
| lexical environment | 词法环境，用来存放闭包变量的语义环境 |
| lexical variable | 词法变量，词法环境中所存的闭包变量 |
约束
字节码构成
操作码与前缀
方舟字节码中的操作码通常被编码为一个8位的值，因此至多只能有256个操作码。随着方舟编译器运行时功能的演进，字节码的数量也在逐步增加，已经超过了256个。因此，方舟字节码引入了前缀（prefix），将操作码最大宽度从8位扩展到16位。8位操作码（无前缀的）用于表示频繁出现的指令，16位操作码（有前缀的）用于表示出现频率不高的指令。
带前缀的操作码为小端法存储的16位值，由8位操作码和8位前缀组成，编码规则为：操作码左移8位，再与前缀相或。
| 前缀操作码 | 助记符 | 描述 |
| --- | --- | --- |
| 0xfe | throw | 有条件/无条件的throw指令 |
| 0xfd | wide | 含有更宽编码宽度的立即数、id或寄存器索引的指令 |
| 0xfc | deprecated | 方舟编译器不再会产生的指令，仅用于维护运行时兼容性； 本文后续章节中将省略对这些指令的说明 |
| 0xfb | callruntime | 调用运行时方法的指令 |
方舟编译器不再会产生的指令，仅用于维护运行时兼容性；
本文后续章节中将省略对这些指令的说明
前缀操作码的助记符的形式为前缀助记符.操作码助记符, 例如，wide.stlexvar。stlexvar指令的操作码是0x0d，前缀wide是0xfd，则此带前缀的指令（wide.stlexvar）的操作码是0x0dfd。
寄存器与累加器
方舟虚拟机模型基于寄存器，所有的寄存器均是虚拟寄存器。当寄存器中存放原始类型的值时，寄存器的宽度是64位；当寄存器中存放对象类型的值时，寄存器的宽度适应为足够宽，以存放对该对象的引用。
方舟字节码中，存在一个名为累加器（accumulator，也简称作acc）的不可见寄存器。acc是许多指令的默认目标寄存器，也是许多指令的默认参数。acc不占用编码宽度，有助于产生更为紧凑的字节码。
示例代码：
```typescript
function foo(): number {
return 1;
}
```
字节码中的相关指令：
```typescript
.function any .foo(any a0, any a1, any a2) {
ldai 0x1
return
}
```
指令ldai 0x1：将整型字面量1加载到acc中；
指令return：将acc中的值返回。
立即数
方舟字节码中部分指令采用常数形式来表示整型数值、双精度浮点型数值、跳转偏移量等数据。这类常数被称为立即数，可以是8位、16位、32位或64位。
方法索引、字符串索引、字面量索引
方舟字节码中存放着源文件中使用到的所有方法、字符串和字面量数组的偏移量。其中，字面量数组中存放着各种字面量数据，例如整型数字、字符串偏移量和方法偏移量。在方舟字节码指令中，这些方法、字符串以及字面量数组的索引都是16位的，分别被称作方法索引（method id）、字符串索引（string id）以及字面量索引（literal id）。这些索引被编码在指令中，以引用方法、字符串和字面量数组。
值存储方式
全局变量
在Script编译模式下，全局变量是一个存储在全局唯一的映射中的变量，其键值为全局变量的名称，值为全局变量的值。全局变量可通过全局（global）相关的指令进行访问。
示例代码：
```typescript
function foo(): void {
a += 2;
b = 5;
}
```
字节码中的相关指令：
```typescript
.function any .foo(any a0, any a1, any a2) {
tryldglobalbyname 0x0, a
sta v4
ldai 0x2
add2 0x1, v4
trystglobalbyname 0x2, a
ldai 0x5
trystglobalbyname 0x3, b
...
}
```
指令tryldglobalbyname 0x0, a：将名称为a的全局变量加载进acc，不存在名称为a的全局变量时，抛出异常；
指令trystglobalbyname 0x2, a：将acc中的值存放到名称为a的全局变量上，不存在名称为a的全局变量时，抛出异常；
指令trystglobalbyname 0x3, b：将acc中的值存放到名称为b的全局变量上，不存在名称为b的全局变量时，抛出异常。
注意：
上述指令中出现的0x0，0x2，0x3是方舟运行时内部使用的保留数字，开发者无需关注。
模块命名空间和模块变量
源文件中所有使用到的模块命名空间（module namespace）都会被编译进一个数组中，指令中使用索引来引用一个模块命名空间。例如，指令getmodulenamespace 0x1引用了索引0x1处的模块命名空间。
源文件中所有使用到的模块变量（module variable）都会被编译进一个数组中，指令中使用索引来引用一个模块变量。例如，指令stmodulevar 0x1引用了索引0x1处的模块变量。
在函数中，如果一个模块变量的声明和这个函数在同一个源文件中，则将这个变量称为局部模块变量；否则称为外部模块变量。例如，指令ldlocalmodulevar和ldexternalmodulevar分别用于加载局部模块变量和外部模块变量。
产生模块指令的相关场景，包括import和export，主要场景列举如下：
注意：
模块相关的逻辑是编译器的内部实现，随着方舟编译器的后续演进，可能会出现新的涉及模块指令的场景；另一方面，现有的模块命名空间和模块变量指令的相关场景，也可能会随着需求演进和代码重构，不再涉及产生模块相关指令。
示例代码：
```typescript
import { a, b } from "./module_foo"
import * as c from "./module_bar"
export let d: number = 3;
a + b + d;
```
字节码中的相关指令：
```typescript
.function any .func_main_0(any a0, any a1, any a2) {
getmodulenamespace 0x1
ldai 0x3
stmodulevar 0x0
ldexternalmodulevar 0x0
sta v0
throw.undefinedifholewithname a
ldexternalmodulevar 0x1
sta v1
throw.undefinedifholewithname b
lda v1
add2 0x0, v0
sta v0
ldlocalmodulevar 0x0
sta v1
throw.undefinedifholewithname d
lda v1
add2 0x1, v0
...
}
```
指令getmodulenamespace 0x1：获取1号槽位上的模块命名空间（c），存放到acc中；
指令stmodulevar 0x0：将acc中的值存放到当前模块的0号槽位上；
指令ldexternalmodulevar 0x0：加载外部模块的0号槽位上的值（a），存放到acc中；
指令ldlocalmodulevar 0x0：加载当前局部模块的0号槽位上的值（d），存放到acc中。
词法环境和词法变量
方舟字节码中，词法环境（lexical environment）可以看作是一个具有多个槽位的数组，每个槽位对应一个词法变量（lexical variable），一个方法中可能会存在多个词法环境。指令中使用词法环境的相对层级编号和槽位索引，来表示一个词法变量。例如，指令ldlexvar 0x1, 0x2的含义是：将1个层次外的词法环境的2号槽位上的值存放到acc中。
注意：
lexical相关的逻辑是编译器的内部实现。随着方舟编译器的后续演进，可能会出现新的涉及lexical指令的场景；另一方面，现有的lexical指令的相关场景，也可能会随着需求演进和代码重构，不再涉及产生lexical相关指令。
示例代码：
```typescript
function foo(): void {
let a: number = 1;
function bar(): number {
return a;
}
}
```
字节码中的相关指令：
```typescript
.function any .foo(any a0, any a1, any a2) {
newlexenv 0x1
...
definefunc 0x0, .bar, 0x0
sta v3
ldai 0x1
...
stlexvar 0x0, 0x0
...
}
.function any .bar(any a0, any a1, any a2) {
...
ldlexvar 0x0, 0x0
...
}
```
指令newlexenv 0x1：创建一个槽位数为1的词法环境，将其存放到acc中，并进入该词法环境；
指令stlexvar 0x0, 0x0：将acc中的值存放到0个层次外的词法环境的0号槽位上；
指令ldlexvar 0x0, 0x0：将0个层次外的词法环境的0号槽位上的值存放到acc中。
共享词法环境
共享词法环境是一类特殊的词法环境。与一般词法环境的区别在于，共享词法环境中的每个词法变量都是sendable对象。方舟编译器通过共享词法环境实现词法变量在多线程的共享。
示例代码：
```typescript
@Sendable
class A { }
@Sendable
class B {
u: A = new A()
}
```
字节码中的相关指令：
指令callruntime.newsendableenv 0x1：创建一个槽位数为1的共享词法环境，并进入该词法环境；
指令callruntime.stsendablevar 0x0, 0x0：将acc中的值存放到0个层次外的共享词法环境的0号槽位上；
指令callruntime.ldsendablevar 0x0, 0x0：将0个层次外的共享词法环境的0号槽位上的值存放到acc中。
补丁变量
方舟编译器支持补丁模式的编译，当源文件发生修改时，经过补丁模式编译，生成一个补丁字节码，配合原字节码，完成功能的更新。方舟编译器在补丁模式下编译时，产生的补丁变量会被存放在一个特殊的补丁词法环境中。方舟字节码中使用补丁词法环境上的槽位编号来引用补丁变量。例如，指令ldpatchvar 0x1加载的是槽位号为1的补丁变量。
示例代码：
```typescript
function bar(): void {} // 新增语句，编译补丁
function foo(): void {
bar(); // 新增语句，编译补丁
}
```
字节码中的相关指令：
```typescript
.function any foo(...) {
...
wide.ldpatchvar 0x0
sta v4
lda v4
callarg0 0x0
...
}
.function any patch_main_0(...) {
newlexenv 0x1
definefunc 0x1, bar:(any,any,any), 0x0
wide.stpatchvar 0x0
...
}
```
指令wide.stpatchvar 0x0：将函数bar存放到补丁词法环境的0号槽位；
指令wide.ldpatchvar 0x0：将补丁词法环境上0号槽位的值存放到acc中。
函数调用规范
对于一个包含了N个形参的方法，该方法所使用的寄存器中的最后N+3个会被用于传递参数。其中，前三个寄存器固定表示函数本身（FunctionObject）、new.target（NewTarget）和函数所在的词法环境中的this（this），后续的N个寄存器依次对应这N个形参。
示例代码：
```typescript
function foo(a: number, b: number): void {}
```
字节码中的相关指令：
```typescript
.function any .foo(any a0, any a1, any a2, any a3, any a4) {
// a0: FunctionObject
// a1: NewTarget
// a2: this
// a3: a
// a4: b
}
```
字节码格式说明
| 助记符 | 语义说明 |
| --- | --- |
| ID16 | 8位操作码，16位id |
| IMM16 | 8位操作码，16位立即数 |
| IMM16_ID16 | 8位操作码，16位立即数，16位id |
| IMM16_ID16_ID16_IMM16_V8 | 8位操作码，16位立即数，2个16位id，16位立即数，8位寄存器 |
| IMM16_ID16_IMM8 | 8位操作码，16位立即数，16位id，8位立即数 |
| IMM16_ID16_V8 | 8位操作码，16位立即数，16位id，8位寄存器 |
| IMM16_IMM16 | 8位操作码，2个16位立即数 |
| IMM16_IMM8_V8 | 8位操作码，16位立即数，8位立即数，8位寄存器 |
| IMM16_V8 | 8位操作码，16位立即数，8位寄存器 |
| IMM16_V8_IMM16 | 8位操作码，16位立即数，8位寄存器，16位立即数 |
| IMM16_V8_V8 | 8位操作码，16位立即数，2个8位寄存器 |
| IMM32 | 8位操作码，32位立即数 |
| IMM4_IMM4 | 8位操作码，2个4位立即数 |
| IMM64 | 8位操作码，64位立即数 |
| IMM8 | 8位操作码，8位立即数 |
| IMM8_ID16 | 8位操作码，8位立即数，16位id |
| IMM8_ID16_ID16_IMM16_V8 | 8位操作码，8位立即数，2个16位id，16位立即数，8位寄存器 |
| IMM8_ID16_IMM8 | 8位操作码，8位立即数，16位id，8位立即数 |
| IMM8_ID16_V8 | 8位操作码，8位立即数，16位id，8位寄存器 |
| IMM8_IMM16 | 8位操作码，8位立即数，16位立即数 |
| IMM8_IMM8 | 8位操作码，2个8位立即数 |
| IMM8_IMM8_V8 | 8位操作码，2个8位立即数，8位寄存器 |
| IMM8_V8 | 8位操作码，8位立即数，8位寄存器 |
| IMM8_V8_IMM16 | 8位操作码，8位立即数，8位寄存器，16位立即数 |
| IMM8_V8_V8 | 8位操作码，8位立即数，2个8位寄存器 |
| IMM8_V8_V8_V8 | 8位操作码，8位立即数，3个8位寄存器 |
| IMM8_V8_V8_V8_V8 | 8位操作码，8位立即数，4个8位寄存器 |
| NONE | 8位操作码 |
| PREF_IMM16 | 16位前缀操作码，16位立即数 |
| PREF_IMM16_ID16 | 16位前缀操作码，16位立即数，16位id |
| PREF_IMM16_V8 | 16位前缀操作码，16位立即数，8位寄存器 |
| PREF_IMM16_V8_V8 | 16位前缀操作码，16位立即数，2个8位寄存器 |
| PREF_IMM8 | 16位前缀操作码，8位立即数 |
| PREF_NONE | 16位前缀操作码 |
| PREF_V8 | 16位前缀操作码，8位寄存器 |
| PREF_V8_ID16 | 16位前缀操作码，8位寄存器，16位id |
| PREF_V8_IMM32 | 16位前缀操作码，8位寄存器，32位立即数 |
| V16_V16 | 8位操作码，2个16位寄存器 |
| V4_V4 | 8位操作码，2个4位寄存器 |
| V8 | 8位操作码，8位寄存器 |
| V8_IMM16 | 8位操作码，8位寄存器，16位立即数 |
| V8_IMM8 | 8位操作码，8位寄存器，8位立即数 |
| V8_V8 | 8位操作码，2个8位寄存器 |
| V8_V8_V8 | 8位操作码，3个8位寄存器 |
| V8_V8_V8_V8 | 8位操作码，4个8位寄存器 |
字节码汇总集合
下表中汇总了当前版本的所有方舟字节码，寄存器索引、立即数和id通过每四位宽度使用一个字符替代的形式来描述。
以指令defineclasswithbuffer RR, @AAAA, @BBBB, +CCCC, vDD为例：
| 操作码 | 格式 | 助记符/语法 | 参数 | 说明 |
| --- | --- | --- | --- | --- |
| 0x00 | NONE | ldundefined |  | 将undefined加载进acc。 |
| 0x01 | NONE | ldnull |  | 将null加载进acc。 |
| 0x02 | NONE | ldtrue |  | 将true加载进acc。 |
| 0x03 | NONE | ldfalse |  | 将false加载进acc。 |
| 0x04 | NONE | createemptyobject |  | 创建一个空对象，并将其存放到acc中。 |
| 0x05 | IMM8 | createemptyarray RR | R：方舟运行时内部使用的8位保留数字 | 创建一个空数组，并将其存放到acc中。 |
| 0x06 | IMM8_ID16 | createarraywithbuffer RR, @AAAA | R：方舟运行时内部使用的8位保留数字 A：16位的literal id | 使用索引A对应的字面量数组，创建一个数组对象，并将其存放到acc中。 |
| 0x07 | IMM8_ID16 | createobjectwithbuffer RR, @AAAA | R：方舟运行时内部使用的8位保留数字 A：16位的literal id | 使用索引A对应的字面量数组，创建一个对象，并将其存放到acc中。 |
| 0x08 | IMM8_IMM8_V8 | newobjrange RR, +AA, vBB | R：方舟运行时内部使用的8位保留数字 A：参数数量 B：类对象 B + 1, ..., B + A - 1：传递给构造函数的参数 | 以B + 1, ..., B + A - 1作为参数，创建一个B类的实例，并将其存放到acc中。 |
| 0x09 | IMM8 | newlexenv +AA | A：词法环境中的槽位数目 | 创建一个槽位数为A的词法环境，将其存放到acc中，并进入该词法环境。 |
| 0x0a | IMM8_V8 | add2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A + acc，并将计算结果存放到acc中。 |
| 0x0b | IMM8_V8 | sub2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A - acc，并将计算结果存放到acc中。 |
| 0x0c | IMM8_V8 | mul2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A * acc，并将计算结果存放到acc中。 |
| 0x0d | IMM8_V8 | div2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A / acc，并将计算结果存放到acc中。 |
| 0x0e | IMM8_V8 | mod2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A % acc，并将计算结果存放到acc中。 |
| 0x0f | IMM8_V8 | eq RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A == acc，并将计算结果存放到acc中。 |
| 0x10 | IMM8_V8 | noteq RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A != acc，并将计算结果存放到acc中。 |
| 0x11 | IMM8_V8 | less RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A < acc，并将计算结果存放到acc中。 |
| 0x12 | IMM8_V8 | lesseq RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A <= acc，并将计算结果存放到acc中。 |
| 0x13 | IMM8_V8 | greater RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A > acc，并将计算结果存放到acc中。 |
| 0x14 | IMM8_V8 | greatereq RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A >= acc，并将计算结果存放到acc中。 |
| 0x15 | IMM8_V8 | shl2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A << acc，并将计算结果存放到acc中。 |
| 0x16 | IMM8_V8 | shr2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A >>> acc，并将计算结果存放到acc中。 |
| 0x17 | IMM8_V8 | ashr2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A >> acc，并将计算结果存放到acc中。 |
| 0x18 | IMM8_V8 | and2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A & acc，并将计算结果存放到acc中。 |
| 0x19 | IMM8_V8 | or2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A | acc，并将计算结果存放到acc中。 |
| 0x1a | IMM8_V8 | xor2 RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A ^ acc，并将计算结果存放到acc中。 |
| 0x1b | IMM8_V8 | exp RR, vAA | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 A：操作数 | 计算A ** acc，并将计算结果存放到acc中。 |
| 0x1c | IMM8 | typeof RR | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 | 计算typeof acc，并将计算结果存放到acc中。 |
| 0x1d | IMM8 | tonumber RR | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 | 以acc作为参数，执行ToNumber，将结果存放到acc中。 |
| 0x1e | IMM8 | tonumeric RR | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 | 以acc作为参数，执行ToNumeric，将结果存放到acc中。 |
| 0x1f | IMM8 | neg RR | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 | 计算-acc，并将计算结果存放到acc中。 |
| 0x20 | IMM8 | not RR | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 | 计算~acc，并将计算结果存放到acc中。 |
| 0x21 | IMM8 | inc RR | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 | 计算acc + 1，并将计算结果存放到acc中。 |
| 0x22 | IMM8 | dec RR | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 | 计算acc - 1，并将计算结果存放到acc中。 |
| 0x23 | NONE | istrue | 默认入参：acc：对象 | 计算acc == true，并将计算结果存放到acc中。 |
| 0x24 | NONE | isfalse | 默认入参：acc：对象 | 计算acc == false，并将计算结果存放到acc中。 |
| 0x25 | IMM8_V8 | isin RR, vAA | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 A：对象 | 计算A in acc，并将计算结果存放到acc中。 |
| 0x26 | IMM8_V8 | instanceof RR, vAA | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 A：对象 | 计算A instanceof acc，并将计算结果存放到acc中。 |
| 0x27 | IMM8_V8 | strictnoteq RR, vAA | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 A：对象 | 计算acc !== A，并将计算结果存放到acc中。 |
| 0x28 | IMM8_V8 | stricteq RR, vAA | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 A：对象 | 计算acc === A，并将计算结果存放到acc中。 |
| 0x29 | IMM8 | callarg0 RR | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 | 不传递参数，直接调用acc中存放的函数对象，并将结果存放到acc中。 |
| 0x2a | IMM8_V8 | callarg1 RR, vAA | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：参数 | 以A作为参数，调用acc中存放的函数对象，并将结果存放到acc中。 |
| 0x2b | IMM8_V8_V8 | callargs2 RR, vAA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A, B：参数 | 以A，B作为参数，调用acc中存放的函数对象，并将结果存放到acc中。 |
| 0x2c | IMM8_V8_V8_V8 | callargs3 RR, vAA, vBB, vCC | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A, B, C：参数 | 以A, B, C作为参数，调用acc中存放的函数对象，并将结果存放到acc中。 |
| 0x2d | IMM8_V8 | callthis0 RR, vAA | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：对象 | 将this的值设置为A，不传递参数，调用acc中存放的函数对象，并将结果存放到acc中。 |
| 0x2e | IMM8_V8_V8 | callthis1 RR, vAA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：对象 B：参数 | 将this的值设置为A，以B作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。 |
| 0x2f | IMM8_V8_V8_V8 | callthis2 RR, vAA, vBB, vCC | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：对象 B, C：参数 | 将this的值设置为A，以B，C作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。 |
| 0x30 | IMM8_V8_V8_V8_V8 | callthis3 RR, vAA, vBB, vCC, vDD | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：对象 B, C, D：参数 | 将this的值设置为A，以B, C, D作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。 |
| 0x31 | IMM8_IMM8_V8 | callthisrange RR, +AA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：参数数量 B：对象 B + 1, ..., B + A：参数 | 将this的值设置为B，以B + 1，...，B + A作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。 |
| 0x32 | IMM8_IMM8_V8 | supercallthisrange RR, +AA, vBB | R：方舟运行时内部使用的8位保留数字 A：参数数量 B, ..., B + A - 1：参数 | 以B, ..., B + A - 1作为参数, 调用super函数，并将结果存放到acc中。 当A的值是0时，B是undefined。 此指令仅出现在非箭头函数中。 |
| 0x33 | IMM8_ID16_IMM8 | definefunc RR, @AAAA, +BB | R：方舟运行时内部使用的8位保留数字 A：method id B：方法A的形参数量 | 创建方法A的函数对象，并将其存放到acc中。 |
| 0x34 | IMM8_ID16_IMM8 | definemethod RR, @AAAA, +BB | 默认入参：acc：类对象或类对象的对象原型，方法为静态方法时，acc中是类对象 R：方舟运行时内部使用的8位保留数字 A：method id B：方法A的形参数量 | 创建方法A的函数对象，将acc中的对象设置为该函数对象的HomeObject属性，并将该函数对象存放到acc中。 |
| 0x35 | IMM8_ID16_ID16_IMM16_V8 | defineclasswithbuffer RR, @AAAA, @BBBB, +CCCC, vDD | R：方舟运行时内部使用的8位保留数字 A：类的构造函数的method id B：literal id C：方法A的形参数量 D：父类 | 使用索引B对应的字面量数组和父类D，创建A的类对象，并将其存放到acc中。 |
| 0x36 | V8 | getnextpropname vAA | A：迭代器 | 执行for-in迭代器A的next方法，并将结果存放到acc中。 |
| 0x37 | IMM8_V8 | ldobjbyvalue RR, vAA | 默认入参：acc：属性键值 R：方舟运行时内部使用的8位保留数字 A：对象 | 加载A对象的键值为acc的属性，并将结果存放到acc中。 |
| 0x38 | IMM8_V8_V8 | stobjbyvalue RR, vAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0x39 | IMM8_V8 | ldsuperbyvalue RR, vAA | 默认入参：acc：属性键值 R：方舟运行时内部使用的8位保留数字 A：对象 | 在当前函数中，获取super的键值为acc的属性，并将其存放到acc中。若该属性为访问器属性，则将A中的对象作为调用该属性getter函数时的this参数。 |
| 0x3a | IMM8_IMM16 | ldobjbyindex RR, +AAAA | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 A：属性键值 | 加载acc中所存对象的键值为A的属性，并将其存放到acc中。 |
| 0x3b | IMM8_V8_IMM16 | stobjbyindex RR, vAA, +BBBB | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0x3c | IMM4_IMM4 | ldlexvar +A, +B | A：词法环境层级 B：槽位号 | 将A个层次外的词法环境的B号槽位上的值存放到acc中。 |
| 0x3d | IMM4_IMM4 | stlexvar +A, +B | 默认入参：acc：值 A：词法环境层级 B：槽位号 | 将acc中的值存放到A个层次外的词法环境的B号槽位上。 |
| 0x3e | ID16 | lda.str @AAAA | A：string id | 将索引A对应的字符串存放到acc中。 |
| 0x3f | IMM8_ID16 | tryldglobalbyname RR, @AAAA | R：方舟运行时内部使用的8位保留数字 A：string id | 将名称为索引A对应的字符串的全局变量存放进acc中，不存在名称为A的全局变量时，抛出异常。 |
| 0x40 | IMM8_ID16 | trystglobalbyname RR, @AAAA | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：string id | 将acc中的值存放到名称为索引A对应的字符串的全局变量上，不存在名称为A的全局变量时，抛出异常。 |
| 0x41 | IMM16_ID16 | ldglobalvar RRRR, @AAAA | R：方舟运行时内部使用的16位保留数字 A：string id | 将名称为索引A对应的字符串的全局变量的值存放到acc中，该变量一定存在。 |
| 0x42 | IMM8_ID16 | ldobjbyname RR, @AAAA | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 A：string id | 加载acc中所存对象的键值为索引A对应的字符串的属性，并将其存放到acc中。 |
| 0x43 | IMM8_ID16_V8 | stobjbyname RR, @AAAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：string id B：对象 | 将acc中的值存放到对象B的键值为索引A对应的字符串的属性上。 |
| 0x44 | V4_V4 | mov vA, vB | A, B：寄存器索引 | 将寄存器B中的内容复制到寄存器A中。 |
| 0x45 | V8_V8 | mov vAA, vBB | A, B：寄存器索引 | 将寄存器B中的内容复制到寄存器A中。 |
| 0x46 | IMM8_ID16 | ldsuperbyname RR, @AAAA | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 A：string id | 在当前函数中，获取super的键值为索引A对应的字符串的属性，并将其存放到acc中。若该属性为访问器属性，则将acc中的对象作为调用该属性getter函数时的this参数。 |
| 0x47 | IMM16_ID16 | stconsttoglobalrecord RRRR, @AAAA | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：string id | 将acc的值存放到全局变量中以const定义的名字为索引A对应的字符串的常量。 |
| 0x48 | IMM16_ID16 | sttoglobalrecord RRRR, @AAAA | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：string id | 将acc的值存放到全局变量中以let定义的名字为索引A对应的字符串的变量。 |
| 0x49 | IMM8_ID16 | ldthisbyname RR, @AAAA | R：方舟运行时内部使用的8位保留数字 A：string id | 加载this的键值为索引A对应的字符串的属性，并把结果存放到acc中。 |
| 0x4a | IMM8_ID16 | stthisbyname RR, @AAAA | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：string id | 将acc中的值存放到this的键值为索引A对应的字符串的属性上。 |
| 0x4b | IMM8 | ldthisbyvalue RR | 默认入参：acc：属性键值 R：方舟运行时内部使用的8位保留数字 | 加载this的键值为acc的属性，并将结果存放到acc中。 |
| 0x4c | IMM8_V8 | stthisbyvalue RR, vAA | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：属性键值 | 将acc中的值存放到this的键值为A的属性上。 |
| 0x4d | IMM8 | jmp +AA | A：有符号的分支偏移量 | 无条件跳转到分支A。 |
| 0x4e | IMM16 | jmp +AAAA | A：有符号的分支偏移量 | 无条件跳转到分支A。 |
| 0x4f | IMM8 | jeqz +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc == 0，如果为真，则跳转到分支A。 |
| 0x50 | IMM16 | jeqz +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc == 0，如果为真，则跳转到分支A。 |
| 0x51 | IMM8 | jnez +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc != 0，如果为真，则跳转到分支A。 |
| 0x52 | IMM8 | jstricteqz +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc === 0，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x53 | IMM8 | jnstricteqz +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc !== 0，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x54 | IMM8 | jeqnull +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc == null，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x55 | IMM8 | jnenull +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc != null，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x56 | IMM8 | jstricteqnull +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc === null，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x57 | IMM8 | jnstricteqnull +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc !== null，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x58 | IMM8 | jequndefined +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc == undefined，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x59 | IMM8 | jneundefined +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc != undefined，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x5a | IMM8 | jstrictequndefined +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc === undefined，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x5b | IMM8 | jnstrictequndefined +AA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc !== undefined，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x5c | V8_IMM8 | jeq vAA, +BB | 默认入参：acc：值 A：值 B：有符号的分支偏移量 | 计算acc == A，如果为真，则跳转到分支B。 指令功能未使能，暂不可用。 |
| 0x5d | V8_IMM8 | jne vAA, +BB | 默认入参：acc：值 A：值 B：有符号的分支偏移量 | 计算acc != A，如果为真，则跳转到分支B。 指令功能未使能，暂不可用。 |
| 0x5e | V8_IMM8 | jstricteq vAA, +BB | 默认入参：acc：对象 A：对象 B：有符号的分支偏移量 | 计算acc === A，如果为真，则跳转到分支B。 指令功能未使能，暂不可用。 |
| 0x5f | V8_IMM8 | jnstricteq vAA, +BB | 默认入参：acc：对象 A：对象 B：有符号的分支偏移量 | 计算acc !== A，如果为真，则跳转到分支B。 指令功能未使能，暂不可用。 |
| 0x60 | V8 | lda vAA | A：寄存器索引 | 将寄存器A中的内容存放到acc中。 |
| 0x61 | V8 | sta vAA | 默认入参：acc A：寄存器索引 | 将acc中的内容存放到寄存器A中。 |
| 0x62 | IMM32 | ldai +AAAAAAAA | A：常量字面量 | 将整型字面量A存放到acc中。 |
| 0x63 | IMM64 | fldai +AAAAAAAAAAAAAAAA | A：常量字面量 | 将双精度浮点型字面量A存放到acc中。 |
| 0x64 | NONE | return | 默认入参：acc：值 | 返回acc中的值。 |
| 0x65 | NONE | returnundefined |  | 返回undefined。 |
| 0x66 | NONE | getpropiterator | 默认入参：acc：对象 | 将acc中所存的对象的for-in迭代器存放到acc中。 |
| 0x67 | IMM8 | getiterator RR | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 | 执行GetIterator(acc, sync)方法，并将结果存放到acc中。 |
| 0x68 | IMM8_V8 | closeiterator RR, vAA | R：方舟运行时内部使用的8位保留数字 A：对象 | 以类型为 iteratorRecord 的A作为参数，执行IteratorClose，并将结果存放到acc中。 |
| 0x69 | NONE | poplexenv |  | 跳出当前的词法环境，进入外面一层词法环境。 |
| 0x6a | NONE | ldnan |  | 将nan存放到acc中。 |
| 0x6b | NONE | ldinfinity |  | 将infinity存放到acc中。 |
| 0x6c | NONE | getunmappedargs |  | 将当前函数的arguments存放到acc中。 |
| 0x6d | NONE | ldglobal |  | 将global对象存放到acc中。 |
| 0x6e | NONE | ldnewtarget |  | 将当前函数的隐式参数NewTarget存放到acc中。 指令功能未使能，暂不可用。 |
| 0x6f | NONE | ldthis |  | 将this存放到acc中。 |
| 0x70 | NONE | ldhole |  | 将hole存放到acc中。 |
| 0x71 | IMM8_ID16_IMM8 | createregexpwithliteral RR, @AAAA, +BB | R：方舟运行时内部使用的8位保留数字 A：string id B：指代正则表达式修饰符 | 使用索引A对应的字符串和B指代的修饰符，创建一个正则表达式，并存放到acc中。 B和所指代的修饰符的对应关系为：0（默认值，无修饰符），1（g），2（i），4（m），8（s），16（u），32（y）；B也可以指代符合语法规范的修饰符的组合，例如3，指代的修饰符是gi。 |
| 0x72 | IMM16_ID16_IMM8 | createregexpwithliteral RRRR, @AAAA, +BB | R：方舟运行时内部使用的16位保留数字 A：string id B：指代正则表达式修饰符 | 使用索引A对应的字符串和B指代的修饰符，创建一个正则表达式，并存放到acc中。 B和所指代的修饰符的对应关系为：0（默认值，无修饰符），1（g），2（i），4（m），8（s），16（u），32（y）；B也可以指代符合语法规范的修饰符的组合，例如3，指代的修饰符是gi。 |
| 0x73 | IMM8_IMM8_V8 | callrange RR, +AA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：参数数量 B,..., B + A - 1：参数 | 以B, ..., B + A - 1作为参数，调用acc中存放的函数对象，并将结果存放到acc中。 |
| 0x74 | IMM16_ID16_IMM8 | definefunc RRRR, @AAAA, +BB | R：方舟运行时内部使用的16位保留数字 A：method id B：方法A的形参数量 | 创建方法A的函数对象，并将其存放到acc中。 |
| 0x75 | IMM16_ID16_ID16_IMM16_V8 | defineclasswithbuffer RRRR, @AAAA, @BBBB, +CCCC, vDD | R：方舟运行时内部使用的16位保留数字 A：类的构造函数的method id B：literal id C：方法A的形参数量 D：父类 | 使用索引B对应的字面量数组和父类D，创建A的类对象，并将其存放到acc中。 |
| 0x76 | IMM8 | gettemplateobject RR | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 | 执行GetTemplateObject(acc)，并将结果存放到acc中。 |
| 0x77 | IMM8_V8 | setobjectwithproto RR, vAA | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 A：值 | 将acc中存放对象的 __proto__ 属性设置为A。 |
| 0x78 | IMM8_V8_V8 | stownbyvalue RR, vAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0x79 | IMM8_V8_IMM16 | stownbyindex RR, vAA, +BBBB | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0x7a | IMM8_ID16_V8 | stownbyname RR, @AAAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：string id B：对象 | 将acc中的值存放到对象B的键值为索引A对应的字符串的属性上。 |
| 0x7b | IMM8 | getmodulenamespace +AA | A：模块索引 | 对第A个模块，执行GetModuleNamespace，并将结果存放到acc中。 |
| 0x7c | IMM8 | stmodulevar +AA | 默认入参：acc：值 A：槽位号 | 将acc中的值存放到槽位号为A的模块变量中。 |
| 0x7d | IMM8 | ldlocalmodulevar +AA | A：槽位号 | 将槽位号为A的局部模块变量存放到acc中。 |
| 0x7e | IMM8 | ldexternalmodulevar +AA | A：槽位号 | 将槽位号为A的外部模块变量存放到acc中。 |
| 0x7f | IMM16_ID16 | stglobalvar RRRR, @AAAA | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：string id | 将acc中的值存放到名字为索引A对应的字符串的全局变量上，这个变量一定存在。 |
| 0x80 | IMM16 | createemptyarray RRRR | R：方舟运行时内部使用的16位保留数字 | 创建一个空数组，并将其存放到acc中。 |
| 0x81 | IMM16_ID16 | createarraywithbuffer RRRR, @AAAA | R：方舟运行时内部使用的16位保留数字 A：literal id | 使用索引A对应的字面量数组，创建一个数组对象, 并将其存放到acc中。 |
| 0x82 | IMM16_ID16 | createobjectwithbuffer RRRR, @AAAA | R：方舟运行时内部使用的16位保留数字 A：literal id | 使用索引A对应的字面量数组，创建一个对象, 并将其存放到acc中。 |
| 0x83 | IMM16_IMM8_V8 | newobjrange RRRR, +AA, vBB | R：方舟运行时内部使用的16位保留数字 A：参数数量 B：类对象 B + 1, ..., B + A - 1：传递给构造函数的参数 | 以B + 1, ..., B + A - 1作为参数，创建一个B类的实例，并将其存放到acc中。 |
| 0x84 | IMM16 | typeof RRRR | 默认入参：acc：对象 R：方舟运行时内部使用的16位保留数字 | 计算typeof acc，并将计算结果存放到acc中。 |
| 0x85 | IMM16_V8 | ldobjbyvalue RRRR, vAA | 默认入参：acc：属性键值 R：方舟运行时内部使用的16位保留数字 A：对象 | 加载A对象的键值为acc的属性，并将结果存放到acc中。 |
| 0x86 | IMM16_V8_V8 | stobjbyvalue RRRR, vAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0x87 | IMM16_V8 | ldsuperbyvalue RRRR, vAA | 默认入参：acc：属性键值 R：方舟运行时内部使用的16位保留数字 A：对象 | 在当前函数中，获取super的键值为acc的属性，并将其存放到acc中。若该属性为访问器属性，则将A中的对象作为调用该属性getter函数时的this参数。 |
| 0x88 | IMM16_IMM16 | ldobjbyindex RRRR, +AAAA | 默认入参：acc：对象 R：方舟运行时内部使用的16位保留数字 A：属性键值 | 加载acc中所存对象的键值为A的属性，并将其存放到acc中。 |
| 0x89 | IMM16_V8_IMM16 | stobjbyindex RRRR, vAA, +BBBB | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0x8a | IMM8_IMM8 | ldlexvar +AA, +BB | A：词法环境层级 B：槽位号 | 将A个层次外的词法环境的B号槽位上的值存放到acc中。 |
| 0x8b | IMM8_IMM8 | stlexvar +AA, +BB | 默认入参：acc：值 A：词法环境层级 B：槽位号 | 将acc中的值存放到A个层次外的词法环境的B号槽位上。 |
| 0x8c | IMM16_ID16 | tryldglobalbyname RRRR, @AAAA | R：方舟运行时内部使用的16位保留数字 A：string id | 将名称为索引A对应的字符串的全局变量存放进acc中，不存在名称为A的全局变量时，抛出异常。 |
| 0x8d | IMM16_ID16 | trystglobalbyname RRRR, @AAAA | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：string id | 将acc中的值存放到名称为索引A对应的字符串的全局变量上，不存在名称为A的全局变量时，抛出异常。 |
| 0x8e | IMM8_ID16_V8 | stownbynamewithnameset RR, @AAAA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：string id B：对象 | 将acc中的函数对象存放到对象B的键值为索引A对应的字符串的属性上，并将函数的名称设置为索引A对应的字符串。 |
| 0x8f | V16_V16 | mov vAAAA, vBBBB | A, B：寄存器索引 | 将寄存器B中的内容复制到寄存器A中。 |
| 0x90 | IMM16_ID16 | ldobjbyname RRRR, @AAAA | 默认入参：acc：对象 R：方舟运行时内部使用的16位保留数字 A：string id | 加载acc中所存对象的键值为索引A对应的字符串的属性，并将其存放到acc中。 |
| 0x91 | IMM16_ID16_V8 | stobjbyname RRRR, @AAAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：string id B：对象 | 将acc中的值存放到对象B的键值为索引A对应的字符串的属性上。 |
| 0x92 | IMM16_ID16 | ldsuperbyname RRRR, @AAAA | 默认入参：acc：对象 R：方舟运行时内部使用的16位保留数字 A：string id | 在当前函数中，获取super的键值为索引A对应的字符串的属性，并将其存放到acc中。若该属性为访问器属性，则将acc中的对象作为调用该属性getter函数时的this参数。 |
| 0x93 | IMM16_ID16 | ldthisbyname RRRR, @AAAA | R：方舟运行时内部使用的16位保留数字 A：string id | 加载this的键值为索引A对应的字符串的属性，并把结果存放到acc中。 |
| 0x94 | IMM16_ID16 | stthisbyname RRRR, @AAAA | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：string id | 将acc中的值存放到this的键值为索引A对应的字符串的属性上。 |
| 0x95 | IMM16 | ldthisbyvalue RRRR | 默认入参：acc：属性键值 R：方舟运行时内部使用的16位保留数字 | 加载this的键值为acc的属性，并将结果存放到acc中。 |
| 0x96 | IMM16_V8 | stthisbyvalue RRRR, vAA | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：属性键值 | 将acc中的值存放到this的键值为A的属性上。 |
| 0x97 | V8 | asyncgeneratorreject vAA | 默认入参：acc：异常 A：生成器 | 使用 generator A和acc中存放的异常，执行AsyncGeneratorReject，并将结果存放到acc中。 |
| 0x98 | IMM32 | jmp +AAAAAAAA | A：有符号的分支偏移量 | 无条件跳转到分支A。 |
| 0x99 | IMM8_V8_V8 | stownbyvaluewithnameset RR, vAA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上，并将函数的名称设置为B。 |
| 0x9a | IMM32 | jeqz +AAAAAAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc == 0，如果为真，则跳转到分支A。 |
| 0x9b | IMM16 | jnez +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc != 0，如果为真，则跳转到分支A。 |
| 0x9c | IMM32 | jnez +AAAAAAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc != 0，如果为真，则跳转到分支A。 |
| 0x9d | IMM16 | jstricteqz +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc === 0，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x9e | IMM16 | jnstricteqz +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc !== 0，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0x9f | IMM16 | jeqnull +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc == null，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0xa0 | IMM16 | jnenull +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc != null，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0xa1 | IMM16 | jstricteqnull +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc === null，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0xa2 | IMM16 | jnstricteqnull +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc !== null，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0xa3 | IMM16 | jequndefined +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc == undefined，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0xa4 | IMM16 | jneundefined +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc != undefined，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0xa5 | IMM16 | jstrictequndefined +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc === undefined，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0xa6 | IMM16 | jnstrictequndefined +AAAA | 默认入参：acc：值 A：有符号的分支偏移量 | 计算acc !== undefined，如果为真，则跳转到分支A。 指令功能未使能，暂不可用。 |
| 0xa7 | V8_IMM16 | jeq vAA, +BBBB | 默认入参：acc：值 A：值 B：有符号的分支偏移量 | 计算acc == A，如果为真，则跳转到分支B。 指令功能未使能，暂不可用。 |
| 0xa8 | V8_IMM16 | jne vAA, +BBBB | 默认入参：acc：值 A：值 B：有符号的分支偏移量 | 计算acc != A，如果为真，则跳转到分支B。 指令功能未使能，暂不可用。 |
| 0xa9 | V8_IMM16 | jstricteq vAA, +BBBB | 默认入参：acc：值 A：值 B：有符号的分支偏移量 | 计算acc === A，如果为真，则跳转到分支B。 指令功能未使能，暂不可用。 |
| 0xaa | V8_IMM16 | jnstricteq vAA, +BBBB | 默认入参：acc：值 A：值 B：有符号的分支偏移量 | 计算acc !== A，如果为真，则跳转到分支B。 指令功能未使能，暂不可用。 |
| 0xab | IMM16 | getiterator RRRR | 默认入参：acc：对象 R：方舟运行时内部使用的16位保留数字 | 执行GetIterator(acc, sync)方法，并将结果存放到acc中。 |
| 0xac | IMM16_V8 | closeiterator RRRR, vAA | R：方舟运行时内部使用的16位保留数字 A：对象 | 以类型为 iteratorRecord 的A作为参数，执行IteratorClose，并将结果存放到acc中。 |
| 0xad | NONE | ldsymbol |  | 加载Symbol对象到acc中。 |
| 0xae | NONE | asyncfunctionenter |  | 创建一个异步函数对象，并将这个对象存放到acc中。 |
| 0xaf | NONE | ldfunction |  | 将当前的函数对象加载到acc中。 |
| 0xb0 | NONE | debugger |  | 调试时用于暂停执行。 |
| 0xb1 | V8 | creategeneratorobj vAA | A：函数对象 | 使用函数对象A，创建一个generator，并将其存放到acc中。 |
| 0xb2 | V8_V8 | createiterresultobj vAA, vBB | A：对象 B：布尔值 | 以 value A和 done B作为参数，执行CreateIterResultObject，并将结果存放到acc中。 |
| 0xb3 | IMM8_V8_V8 | createobjectwithexcludedkeys +AA, vBB, vCC | A：范围寄存器数量 B：对象 C, ..., C + A：属性键值 | 基于对象B，创建一个排除了键值C, ..., C + A的对象，并将其存放到acc中。 这个指令用于支持使用析构和扩展语法创建对象。 |
| 0xb4 | IMM8_V8 | newobjapply RR, vAA | 默认入参：acc：参数列表 R：方舟运行时内部使用的8位保留数字 A：类对象 | 使用acc中存放的参数列表，创建一个A类的实例，并将其存放到acc中。 |
| 0xb5 | IMM16_V8 | newobjapply RRRR, vAA | 默认入参：acc：参数列表 R：方舟运行时内部使用的16位保留数字 A：类对象 | 使用acc中存放的参数列表，创建一个A类的实例，并将其存放到acc中。 |
| 0xb6 | IMM8_ID16 | newlexenvwithname +AA, @BBBB | A：词法环境中的槽位数量 B：literal id | 使用索引B对应的字面量数组中所存放的词法变量名称，创建一个具有A个槽位的词法环境，将这个词法环境存放到acc中，并进入该词法环境。 |
| 0xb7 | V8 | createasyncgeneratorobj vAA | A：函数对象 | 基于函数对象A，创建一个异步的generator，并将其存放到acc中。 |
| 0xb8 | V8_V8_V8 | asyncgeneratorresolve vAA, vBB, vCC | A：生成器 B：对象 C：布尔值 | 以 generator A, value B和 done C作为参数，执行AsyncGeneratorResolve，并将结果存放到acc中。 |
| 0xb9 | IMM8_V8 | supercallspread RR, vAA | 默认入参：acc：类对象 R：方舟运行时内部使用的8位保留数字 A：参数列表 | 以参数列表A作为参数，调用acc中所存类的父类构造函数，并将结果存放到acc中。 |
| 0xba | IMM8_V8_V8 | apply RR, vAA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：对象 B：参数列表 | 将this设置为A，以参数列表B作为参数，调用acc中存放的函数对象，并将返回值存放到acc中。 |
| 0xbb | IMM8_IMM8_V8 | supercallarrowrange RR, +AA, vBB | 默认入参：acc：类对象 R：方舟运行时内部使用的8位保留数字 A：参数数量 B, ..., B + A - 1：参数 | 以B, ..., B + A - 1作为参数，调用acc中所存类的父类的构造函数，并将结果存放到acc中。 如果A的值为0，则B为undefined。 此指令仅出现在箭头函数中。 |
| 0xbc | V8_V8_V8_V8 | definegettersetterbyvalue vAA, vBB, vCC, vDD | 默认入参：acc：是否需要为访问器设置名称，是一个布尔值 A：对象 B：属性键值 C：getter函数对象 D：setter函数对象 | 以getter方法 C和setter方法 D作为参数，定义对象A的键值为B的属性的访问器，并将结果对象存放到acc中。 如果C是undefined，则不会设置getter，如果D是undefined，则不会设置setter。 |
| 0xbd | NONE | dynamicimport | 默认入参：acc：值 | 使用acc中的值作为参数，执行ImportCalls，并把结果存放到acc中。 |
| 0xbe | IMM16_ID16_IMM8 | definemethod RRRR, @AAAA, +BB | 默认入参：acc：类对象或类对象的对象原型，方法为静态方法时，acc中是类对象 R：方舟运行时内部使用的16位保留数字 A：method id B：方法A的形参数量 | 创建方法A的函数对象，将acc中的对象设置为该函数对象的[[[HomeObject]]](https://262.ecma-international.org/12.0/#sec-ecmascript-function-objects)属性，并将该函数对象存放到acc中。 |
| 0xbf | NONE | resumegenerator | 默认入参：acc：生成器 | 基于acc中存放的generator，执行GeneratorResume，并将结果存放到acc中。 |
| 0xc0 | NONE | getresumemode | 默认入参：acc：生成器 | 获取acc中所存放的generator的执行完成后恢复值的类型，并将其存放到acc中。 |
| 0xc1 | IMM16 | gettemplateobject RRRR | 默认入参：acc：对象 R：方舟运行时内部使用的16位保留数字 | 执行GetTemplateObject(acc)，并将结果存放到acc中。 |
| 0xc2 | V8 | delobjprop vAA | 默认入参：acc：属性键值 A：对象 | 删除对象A的键值为acc的属性。 |
| 0xc3 | V8 | suspendgenerator vAA | 默认入参：acc：值 A：生成器 | 使用acc中所存放的值，挂起generator A，并将结果存放到acc中。 |
| 0xc4 | V8 | asyncfunctionawaituncaught vAA | 默认入参：acc：值 A：函数对象 | 使用函数对象A和acc的值，执行AwaitExpression，并将结果存放到acc中。 |
| 0xc5 | V8 | copydataproperties vAA | 默认入参：acc：对象 A：目标对象 | 将acc中所存放的对象的所有属性拷贝到A中，并将A存放到acc中。 |
| 0xc6 | V8_V8 | starrayspread vAA, vBB | 默认入参：acc：值 A：数组 B：数组索引 | 将acc中的值按照SpreadElement的形式存放到数组A的以索引B起始的位置上，并将结果数组的长度存放到acc中。 |
| 0xc7 | IMM16_V8 | setobjectwithproto RRRR, vAA | 默认入参：acc：对象 R：方舟运行时内部使用的16位保留数字 A：值 | 将acc中存放对象的 __proto__ 属性设置为A。 |
| 0xc8 | IMM16_V8_V8 | stownbyvalue RRRR, vAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0xc9 | IMM8_V8_V8 | stsuperbyvalue RR, vAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：对象 B：属性键值 | 在当前函数中，将acc中的值存放到super的键值为B的属性上。若该属性为访问器属性，则将A中的对象作为调用该属性setter函数时的this参数。 |
| 0xca | IMM16_V8_V8 | stsuperbyvalue RRRR, vAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：对象 B：属性键值 | 在当前函数中，将acc中的值存放到super的键值为B的属性上。若该属性为访问器属性，则将A中的对象作为调用该属性setter函数时的this参数。 |
| 0xcb | IMM16_V8_IMM16 | stownbyindex RRRR, vAA, +BBBB | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0xcc | IMM16_ID16_V8 | stownbyname RRRR, @AAAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：string id B：对象 | 将acc中的值存放到对象B的键值为索引A对应的字符串的属性上。 |
| 0xcd | V8 | asyncfunctionresolve vAA | 默认入参：acc：值 A：异步的函数对象 | 使用acc中的值，解析对象A的Promise对象，并将结果存放到acc中。 |
| 0xce | V8 | asyncfunctionreject vAA | 默认入参：acc：值 A：异步的函数对象 | 使用acc中的值，驳回对象A的Promise对象，并将结果存放到acc中。 |
| 0xcf | IMM8 | copyrestargs +AA | A：形参列表中剩余参数所在的位次 | 复制剩余参数，并将复制出的参数数组副本存放到acc中。 |
| 0xd0 | IMM8_ID16_V8 | stsuperbyname RR, @AAAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的8位保留数字 A：string id B：对象 | 在当前函数中，将acc中的值存放到super的键值为索引A对应的字符串的属性上。 若该属性为访问器属性，则将B中的对象作为调用该属性setter函数时的this参数。 |
| 0xd1 | IMM16_ID16_V8 | stsuperbyname RRRR, @AAAA, vBB | 默认入参：acc：值 R：方舟运行时内部使用的16位保留数字 A：string id B：对象 | 在当前函数中，将acc中的值存放到super的键值为索引A对应的字符串的属性上。 若该属性为访问器属性，则将B中的对象作为调用该属性setter函数时的this参数。 |
| 0xd2 | IMM16_V8_V8 | stownbyvaluewithnameset RRRR, vAA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上，并将函数的名称设置为B。 |
| 0xd3 | ID16 | ldbigint @AAAA | A：string id | 基于索引A对应的字符串，创建BigInt类型的值，并将其存放到acc中。 |
| 0xd4 | IMM16_ID16_V8 | stownbynamewithnameset RRRR, @AAAA, vBB | 默认入参：acc：函数对象 R：方舟运行时内部使用的16位保留数字 A：string id B：对象 | 将acc中的函数对象存放到对象B的键值为索引A对应的字符串的属性上，并将函数的名称设置为索引A对应的字符串。 |
| 0xd5 | NONE | nop |  | 无操作。 |
| 0xd6 | IMM8 | setgeneratorstate +AA | 默认入参：acc：生成器对象 A：生成器状态 | 将acc中存放的generator的状态设置为A (参考：GeneratorState和AsyncGeneratorState) A可能的值有以下几项：undefined(0x0)、suspendedStart(0x1)、suspendedYield(0x2)、executing(0x3)、completed(0x4)和awaitingReturn(0x5)。 |
| 0xd7 | IMM8 | getasynciterator RR | 默认入参：acc：对象 R：方舟运行时内部使用的8位保留数字 | 执行GetIterator(acc, async)，并将结果存放到acc上。 |
| 0xd8 | IMM8_IMM16_IMM16 | ldprivateproperty RR, +AAAA, +BBBB | 默认入参：acc：对象 A：词法环境层级 B：槽位号 | 加载A个层次外的词法环境的B号槽位上的值，作为属性键值，将acc中所存放对象的该键值对应的值存放到acc中。 |
| 0xd9 | IMM8_IMM16_IMM16_V8 | stprivateproperty RR, +AAAA, +BBBB, vCC | A：词法环境层级 B：槽位号 C：对象 | 加载A个层次外的词法环境的B号槽位上的值，作为属性键值，将acc中的值存放到C中所存放对象的该键值上。 |
| 0xda | IMM8_IMM16_IMM16 | testin RR, +AAAA, +BBBB | 默认入参：acc：对象 A：词法环境层级 B：槽位号 | 加载A个层次外的词法环境的B号槽位上的值，计算是否in acc，将结果存放到acc中。 |
| 0xdb | IMM8_ID16_V8 | definefieldbyname RR, @AAAA, vBB | 默认入参：acc：值 A：string id B：对象 | 为对象B定义一个键值为A的属性，并将acc中的值存放到其中。 |
| 0xdc | IMM8_ID16_V8 | definepropertybyname RR, @AAAA, vBB | 默认入参：acc：值 A：string id B：对象 | 为对象B定义一个键值为A的属性，并将acc中的值存放到其中。 |
| 0xfb | PREF_NONE | callruntime.notifyconcurrentresult | 默认入参：acc：并发函数的返回值 | 将并发函数的返回值通知运行时。 此指令仅出现在并发函数中。 |
| 0xfc | (deprecated) |  |  | （弃用的操作码） |
| 0xfd | PREF_IMM16_V8_V8 | wide.createobjectwithexcludedkeys +AAAA, vBB, vCC | A：范围寄存器数量 B：对象 C, ..., C + A：属性键值 | 基于对象B，创建一个排除了键值C, ..., C + A的对象，并将其存放到acc中。 这个指令用例支持使用析构和扩展语法创建对象。 |
| 0xfe | PREF_NONE | throw | 默认入参：acc：异常 | 抛出acc中存放的异常。 |
| 0x01fb | PREF_IMM8_V8_V8 | callruntime.definefieldbyvalue RR, vAA, vBB | 默认入参：acc：值 A：属性键值 B：对象 | 为对象B定义一个键值为A的属性，并将acc中的值存放到其中。 |
| 0x01fc | (deprecated) |  |  | （弃用的操作码） |
| 0x01fd | PREF_IMM16_V8 | wide.newobjrange +AAAA, vBB | A：参数数量 B：类对象 B + 1, ..., B + A - 1：传递给构造函数的参数 | 以B + 1, ..., B + A - 1作为参数，创建一个B类的实例，并将其存放到acc中。 |
| 0x01fe | PREF_NONE | throw.notexists |  | 抛出异常：未定义的方法。 |
| 0x02fb | PREF_IMM8_IMM32_V8 | callruntime.definefieldbyindex RR, +AAAAAAAA, vBB | 默认入参：acc：值 A：属性键值 B：对象 | 为对象B定义一个键值为A的属性，并将acc中的值存放到其中。 |
| 0x02fc | (deprecated) |  |  | （弃用的操作码） |
| 0x02fd | PREF_IMM16 | wide.newlexenv +AAAA | A：词法环境中的槽位数目 | 创建一个槽位数为A的词法环境，将其存放到acc中，并进入该词法环境。 |
| 0x02fe | PREF_NONE | throw.patternnoncoercible |  | 抛出异常：此对象不可以强制执行。 |
| 0x03fb | PREF_NONE | callruntime.topropertykey | 默认入参：acc：值 | 将acc中的值转换为属性值，如果转换失败，则抛出错误。 |
| 0x03fc | (deprecated) |  |  | （弃用的操作码） |
| 0x03fd | PREF_IMM16_ID16 | wide.newlexenvwithname +AAAA, @BBBB | A：词法环境中的槽位数量 B：literal id | 使用索引B对应的字面量数组中所存放的词法变量名称，创建一个具有A个槽位的词法环境，将这个词法环境存放到acc中，并进入该词法环境。 |
| 0x03fe | PREF_NONE | throw.deletesuperproperty |  | 抛出异常：删除父类的属性。 |
| 0x04fb | PREF_IMM_16_ID16 | callruntime.createprivateproperty +AAAA, @BBBB | A：要创建的符号数量 B：literal id | 创建A个符号；从索引B对应的字面量数组中获取存放的私有方法，如果其中存在私有实例方法，则额外创建一个符号（"method"），将所有创建出的符号按照创建顺序，依次放到当前类所在的词法环境的末尾。 此指令仅出现在定义类的时候。 |
| 0x04fc | (deprecated) |  |  | （弃用的操作码） |
| 0x04fd | PREF_IMM16_V8 | wide.callrange +AAAA, vBB | 默认入参：acc：函数对象 A：参数数量 B, ..., B + A - 1：参数 | 以B, ..., B + A - 1作为参数，调用acc中存放的函数对象，并将结果存放到acc中。 |
| 0x04fe | PREF_V8 | throw.constassignment vAA | A：常量变量的名称 | 抛出异常：对常量变量进行赋值。 |
| 0x05fb | PREF_IMM8_IMM_16_IMM_16_V8 | callruntime.defineprivateproperty RR, +AAAA, +BBBB, vCC | 默认入参：acc：值 A：词法环境层数 B：槽位号 C：对象 | 加载A个层次外的词法环境的B号槽位上的符号，赋值为acc，将其作为私有属性添加到对象C上。 |
| 0x05fc | (deprecated) |  |  | （弃用的操作码） |
| 0x05fd | PREF_IMM16_V8 | wide.callthisrange +AAAA, vBB | 默认入参：acc：函数对象 A：参数数量 B：对象 B + 1, ..., B + A：参数 | 将this的值设置为B，以B + 1，...，B + A作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。 |
| 0x05fe | PREF_V8 | throw.ifnotobject vAA | A：对象 | 如果A不是一个对象，抛出异常。 |
| 0x06fb | PREF_IMM8_V8 | callruntime.callinit +RR, vAA | acc：函数对象 R：方舟运行时内部使用的8位保留数字 A：对象 | 将this的值设置为A，不传递参数，调用acc中存放的函数对象，并将结果存放到acc中。 |
| 0x06fc | (deprecated) |  |  | （弃用的操作码） |
| 0x06fd | PREF_IMM16_V8 | wide.supercallthisrange +AAAA, vBB | A：参数数量 B, ..., B + A - 1：参数 | 以B, ..., B + A - 1作为参数, 调用super函数，并将结果存放到acc中。 当A的值是0时，B是undefined。 此指令仅出现在非箭头函数中。 |
| 0x06fe | PREF_V8_V8 | throw.undefinedifhole vAA, vBB | A：对象 B：对象名称 | 如果A的值是hole，则抛出异常：B的值是undefined。 |
| 0x07fb | PREF_IMM16_ID16_ID16_IMM16_V8 | callruntime.definesendableclass RRRR, @AAAA, @BBBB, +CCCC, vDD | R：方舟运行时内部使用的16位保留数字 A：sendable class的构造函数的method id B：literal id C：方法A的形参数量 D：父类 | 使用索引B对应的字面量数组和父类D，创建一个A类的对象，并将其存放到acc中。 |
| 0x07fc | (deprecated) |  |  | （弃用的操作码） |
| 0x07fd | PREF_IMM16_V8 | wide.supercallarrowrange +AAAA, vBB | 默认入参：acc：类对象 A：参数数量 B, ..., B + A - 1:参数 | 以B, ..., B + A - 1作为参数，调用acc中所存类的父类的构造函数，并将结果存放到acc中。 如果A的值为0，则B为undefined。 此指令仅出现在箭头函数中。 |
| 0x07fe | PREF_IMM8 | throw.ifsupernotcorrectcall +AA | 默认入参：acc：对象 A：错误种类 | 如果super没有被正确调用，抛出错误。 |
| 0x08fb | PREF_IMM16 | callruntime.ldsendableclass +AAAA | A：词法环境层级 | 将A个层次外的词法环境的sendable class存放到acc中。 |
| 0x08fc | (deprecated) |  |  | （弃用的操作码） |
| 0x08fd | PREF_IMM32 | wide.ldobjbyindex +AAAAAAAA | 默认入参：acc：对象 A：属性键值 | 加载acc中所存对象的键值为A的属性，并将其存放到acc中。 |
| 0x08fe | PREF_IMM16 | throw.ifsupernotcorrectcall +AAAA | 默认入参：acc：对象 A：错误种类 | 如果super没有被正确调用，抛出错误。 |
| 0x09fb | PREF_IMM8 | callruntime.ldsendableexternalmodulevar +AA | A：槽位号 | 将槽位号为A的外部模块变量存放到acc中。此指令仅出现在sendable class和sendable function中。 |
| 0x09fc | (deprecated) |  |  | （弃用的操作码） |
| 0x09fd | PREF_V8_IMM32 | wide.stobjbyindex vAA, +BBBBBBBB | 默认入参：acc：值 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0x09fe | PREF_ID16 | throw.undefinedifholewithname @AAAA | 默认入参：acc：对象 A：string id | 如果acc中的值是hole，则抛出异常：A的值是undefined。 |
| 0x0afb | PREF_IMM16 | callruntime.wideldsendableexternalmodulevar +AAAA | A：槽位号 | 将槽位号为A的外部模块变量存放到acc中。此指令仅出现在sendable class和sendable function中。 |
| 0x0afc | (deprecated) |  |  | （弃用的操作码） |
| 0x0afd | PREF_V8_IMM32 | wide.stownbyindex vAA, +BBBBBBBB | 默认入参：acc：值 A：对象 B：属性键值 | 将acc中的值存放到对象A的键值为B的属性上。 |
| 0x0bfb | PREF_IMM8 | callruntime.newsendableenv +AA | A：共享词法环境中的槽位数目 | 创建一个槽位数为A的共享词法环境，并进入该词法环境。 |
| 0x0bfc | (deprecated) |  |  | （弃用的操作码） |
| 0x0bfd | PREF_IMM16 | wide.copyrestargs +AAAA | A：形参列表中剩余参数起始的位次 | 复制剩余参数，并将复制出的参数数组副本存放到acc中。 |
| 0x0cfb | PREF_IMM16 | callruntime.widenewsendableenv +AAAA | A：共享词法环境中的槽位数目 | 创建一个槽位数为A的共享词法环境，并进入该词法环境 。 |
| 0x0cfc | (deprecated) |  |  | （弃用的操作码） |
| 0x0cfd | PREF_IMM16_IMM16 | wide.ldlexvar +AAAA, +BBBB | A：词法环境层级 B：槽位号 | 将A个层次外的词法环境的B号槽位上的值存放到acc中。 |
| 0x0dfb | PREF_IMM4_IMM4 | callruntime.stsendablevar +A +B | 默认入参：acc：值 A：共享词法环境层级 B：槽位号 | 将acc中的值存放到A个层次外的共享词法环境的B号槽位上。 |
| 0x0dfc | (deprecated) |  |  | （弃用的操作码） |
| 0x0dfd | PREF_IMM16_IMM16 | wide.stlexvar +AAAA, +BBBB | 默认入参：acc：值 A：词法环境层级 B：槽位号 | 将acc中的值存放到A个层次外的词法环境的B号槽位上。 |
| 0x0efb | PREF_IMM8_IMM8 | callruntime.stsendablevar +AA +BB | 默认入参：acc：值 A：共享词法环境层级 B：槽位号 | 将acc中的值存放到A个层次外的共享词法环境的B号槽位上 。 |
| 0x0efc | (deprecated) |  |  | （弃用的操作码） |
| 0x0efd | PREF_IMM16 | wide.getmodulenamespace +AAAA | A：模块索引 | 对第A个模块，执行GetModuleNamespace，并将结果存放到acc中。 |
| 0x0ffb | PREF_IMM16_IMM16 | callruntime.widestsendablevar +AAAA +BBBB | 默认入参：acc：值 A：共享词法环境层级 B：槽位号 | 将acc中的值存放到A个层次外的共享词法环境的B号槽位上。 |
| 0x0ffc | (deprecated) |  |  | （弃用的操作码） |
| 0x0ffd | PREF_IMM16 | wide.stmodulevar +AAAA | 默认入参：acc：值 A：槽位号 | 将acc中的值存放到槽位号为A的模块变量中。 |
| 0x10fb | PREF_IMM4_IMM4 | callruntime.ldsendablevar +A +B | A：共享词法环境层级 B：槽位号 | 将A个层次外的共享词法环境的B号槽位上的值存放到acc中。 |
| 0x10fc | (deprecated) |  |  | （弃用的操作码） |
| 0x10fd | PREF_IMM16 | wide.ldlocalmodulevar +AAAA | A：槽位号 | 将槽位号为A的局部模块变量存放到acc中。 |
| 0x11fb | PREF_IMM8_IMM8 | callruntime.ldsendablevar +AA + BB | A：共享词法环境层级 B：槽位号 | 将A个层次外的共享词法环境的B号槽位上的值存放到acc中。 |
| 0x11fc | (deprecated) |  |  | （弃用的操作码） |
| 0x11fd | PREF_IMM16 | wide.ldexternalmodulevar +AAAA | A：槽位号 | 将槽位号为A的外部模块变量存放到acc中。 |
| 0x12fb | PREF_IMM16_IMM16 | callruntime.wideldsendablevar +AAAA +BBBB | A：共享词法环境层级 B：槽位号 | 将A个层次外的共享词法环境的B号槽位上的值存放到acc中。 |
| 0x12fc | (deprecated) |  |  | （弃用的操作码） |
| 0x12fd | PREF_IMM16 | wide.ldpatchvar +AAAA | A：补丁变量槽位号 | 将槽位号为A的补丁变量加载到acc中。 此指令仅出现在补丁模式编译场景下。 |
| 0x13fb | PREF_IMM8 | callruntime.istrue +RR | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 | 计算acc == true，并将计算结果存放到acc中。 |
| 0x13fc | (deprecated) |  |  | （弃用的操作码） |
| 0x13fd | PREF_IMM16 | wide.stpatchvar +AAAA | 默认入参：acc：值 A：补丁变量槽位号 | 将acc中的值存放进槽位号为A的补丁变量中。 此指令仅出现在补丁模式编译场景下。 |
| 0x14fb | PREF_IMM8 | callruntime.isfalse +RR | 默认入参：acc：操作数 R：方舟运行时内部使用的8位保留数字 | 计算acc == false，并将计算结果存放到acc中。 |
| 0x15fb | PREF_IMM8 | callruntime.ldlazymodulevar +AA | A：槽位号 | 将槽位号为A的外部模块变量存放到acc中。此指令仅适用于通过lazy import导入的模块变量。 |
| 0x16fb | PREF_IMM16 | callruntime.wideldlazymodulevar +AAAA | A：槽位号 | 将槽位号为A的外部模块变量存放到acc中。此指令仅适用于通过lazy import导入的模块变量。 |
| 0x17fb | PREF_IMM8 | callruntime.ldlazysendablemodulevar +AA | A：槽位号 | 将槽位号为A的外部模块变量存放到acc中。此指令仅适用于通过lazy import导入的模块变量且仅出现在sendable class和sendable function中。 |
| 0x18fb | PREF_IMM16 | callruntime.wideldlazysendablemodulevar +AAAA | A：槽位号 | 将槽位号为A的外部模块变量存放到acc中。此指令仅适用于通过lazy import导入的模块变量且仅出现在sendable class和sendable function中。 |
| 0x14fc 0x15fc ... 0x2efc | (deprecated) |  |  | （弃用的操作码） |
R：方舟运行时内部使用的8位保留数字
A：16位的literal id
R：方舟运行时内部使用的8位保留数字
A：16位的literal id
R：方舟运行时内部使用的8位保留数字
A：参数数量
B：类对象
B + 1, ..., B + A - 1：传递给构造函数的参数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
A：操作数
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
A：对象
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
A：对象
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
A：对象
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
A：对象
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：参数
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A, B：参数
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A, B, C：参数
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：对象
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：对象
B：参数
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：对象
B, C：参数
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：对象
B, C, D：参数
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：参数数量
B：对象
B + 1, ..., B + A：参数
R：方舟运行时内部使用的8位保留数字
A：参数数量
B, ..., B + A - 1：参数
以B, ..., B + A - 1作为参数, 调用super函数，并将结果存放到acc中。
当A的值是0时，B是undefined。
此指令仅出现在非箭头函数中。
R：方舟运行时内部使用的8位保留数字
A：method id
B：方法A的形参数量
默认入参：acc：类对象或类对象的对象原型，方法为静态方法时，acc中是类对象
R：方舟运行时内部使用的8位保留数字
A：method id
B：方法A的形参数量
R：方舟运行时内部使用的8位保留数字
A：类的构造函数的method id
B：literal id
C：方法A的形参数量
D：父类
默认入参：acc：属性键值
R：方舟运行时内部使用的8位保留数字
A：对象
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：对象
B：属性键值
默认入参：acc：属性键值
R：方舟运行时内部使用的8位保留数字
A：对象
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
A：属性键值
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：对象
B：属性键值
A：词法环境层级
B：槽位号
默认入参：acc：值
A：词法环境层级
B：槽位号
R：方舟运行时内部使用的8位保留数字
A：string id
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：string id
R：方舟运行时内部使用的16位保留数字
A：string id
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
A：string id
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：string id
B：对象
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
A：string id
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：string id
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：string id
R：方舟运行时内部使用的8位保留数字
A：string id
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：string id
默认入参：acc：属性键值
R：方舟运行时内部使用的8位保留数字
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：属性键值
默认入参：acc：值
A：有符号的分支偏移量
默认入参：acc：值
A：有符号的分支偏移量
默认入参：acc：值
A：有符号的分支偏移量
默认入参：acc：值
A：有符号的分支偏移量
计算acc === 0，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc !== 0，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc == null，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc != null，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc === null，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc !== null，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc == undefined，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc != undefined，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc === undefined，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc !== undefined，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：值
B：有符号的分支偏移量
计算acc == A，如果为真，则跳转到分支B。
指令功能未使能，暂不可用。
默认入参：acc：值
A：值
B：有符号的分支偏移量
计算acc != A，如果为真，则跳转到分支B。
指令功能未使能，暂不可用。
默认入参：acc：对象
A：对象
B：有符号的分支偏移量
计算acc === A，如果为真，则跳转到分支B。
指令功能未使能，暂不可用。
默认入参：acc：对象
A：对象
B：有符号的分支偏移量
计算acc !== A，如果为真，则跳转到分支B。
指令功能未使能，暂不可用。
默认入参：acc
A：寄存器索引
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
R：方舟运行时内部使用的8位保留数字
A：对象
将当前函数的隐式参数NewTarget存放到acc中。
指令功能未使能，暂不可用。
R：方舟运行时内部使用的8位保留数字
A：string id
B：指代正则表达式修饰符
使用索引A对应的字符串和B指代的修饰符，创建一个正则表达式，并存放到acc中。
B和所指代的修饰符的对应关系为：0（默认值，无修饰符），1（g），2（i），4（m），8（s），16（u），32（y）；B也可以指代符合语法规范的修饰符的组合，例如3，指代的修饰符是gi。
R：方舟运行时内部使用的16位保留数字
A：string id
B：指代正则表达式修饰符
使用索引A对应的字符串和B指代的修饰符，创建一个正则表达式，并存放到acc中。
B和所指代的修饰符的对应关系为：0（默认值，无修饰符），1（g），2（i），4（m），8（s），16（u），32（y）；B也可以指代符合语法规范的修饰符的组合，例如3，指代的修饰符是gi。
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：参数数量
B,..., B + A - 1：参数
R：方舟运行时内部使用的16位保留数字
A：method id
B：方法A的形参数量
R：方舟运行时内部使用的16位保留数字
A：类的构造函数的method id
B：literal id
C：方法A的形参数量
D：父类
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
A：值
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：对象
B：属性键值
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：对象
B：属性键值
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：string id
B：对象
默认入参：acc：值
A：槽位号
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：string id
R：方舟运行时内部使用的16位保留数字
A：literal id
R：方舟运行时内部使用的16位保留数字
A：literal id
R：方舟运行时内部使用的16位保留数字
A：参数数量
B：类对象
B + 1, ..., B + A - 1：传递给构造函数的参数
默认入参：acc：对象
R：方舟运行时内部使用的16位保留数字
默认入参：acc：属性键值
R：方舟运行时内部使用的16位保留数字
A：对象
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：对象
B：属性键值
默认入参：acc：属性键值
R：方舟运行时内部使用的16位保留数字
A：对象
默认入参：acc：对象
R：方舟运行时内部使用的16位保留数字
A：属性键值
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：对象
B：属性键值
A：词法环境层级
B：槽位号
默认入参：acc：值
A：词法环境层级
B：槽位号
R：方舟运行时内部使用的16位保留数字
A：string id
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：string id
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：string id
B：对象
默认入参：acc：对象
R：方舟运行时内部使用的16位保留数字
A：string id
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：string id
B：对象
默认入参：acc：对象
R：方舟运行时内部使用的16位保留数字
A：string id
R：方舟运行时内部使用的16位保留数字
A：string id
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：string id
默认入参：acc：属性键值
R：方舟运行时内部使用的16位保留数字
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：属性键值
默认入参：acc：异常
A：生成器
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：对象
B：属性键值
默认入参：acc：值
A：有符号的分支偏移量
默认入参：acc：值
A：有符号的分支偏移量
默认入参：acc：值
A：有符号的分支偏移量
默认入参：acc：值
A：有符号的分支偏移量
计算acc === 0，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc !== 0，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc == null，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc != null，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc === null，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc !== null，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc == undefined，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc != undefined，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc === undefined，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：有符号的分支偏移量
计算acc !== undefined，如果为真，则跳转到分支A。
指令功能未使能，暂不可用。
默认入参：acc：值
A：值
B：有符号的分支偏移量
计算acc == A，如果为真，则跳转到分支B。
指令功能未使能，暂不可用。
默认入参：acc：值
A：值
B：有符号的分支偏移量
计算acc != A，如果为真，则跳转到分支B。
指令功能未使能，暂不可用。
默认入参：acc：值
A：值
B：有符号的分支偏移量
计算acc === A，如果为真，则跳转到分支B。
指令功能未使能，暂不可用。
默认入参：acc：值
A：值
B：有符号的分支偏移量
计算acc !== A，如果为真，则跳转到分支B。
指令功能未使能，暂不可用。
默认入参：acc：对象
R：方舟运行时内部使用的16位保留数字
R：方舟运行时内部使用的16位保留数字
A：对象
A：对象
B：布尔值
A：范围寄存器数量
B：对象
C, ..., C + A：属性键值
基于对象B，创建一个排除了键值C, ..., C + A的对象，并将其存放到acc中。
这个指令用于支持使用析构和扩展语法创建对象。
默认入参：acc：参数列表
R：方舟运行时内部使用的8位保留数字
A：类对象
默认入参：acc：参数列表
R：方舟运行时内部使用的16位保留数字
A：类对象
A：词法环境中的槽位数量
B：literal id
A：生成器
B：对象
C：布尔值
默认入参：acc：类对象
R：方舟运行时内部使用的8位保留数字
A：参数列表
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：对象
B：参数列表
默认入参：acc：类对象
R：方舟运行时内部使用的8位保留数字
A：参数数量
B, ..., B + A - 1：参数
以B, ..., B + A - 1作为参数，调用acc中所存类的父类的构造函数，并将结果存放到acc中。
如果A的值为0，则B为undefined。
此指令仅出现在箭头函数中。
默认入参：acc：是否需要为访问器设置名称，是一个布尔值
A：对象
B：属性键值
C：getter函数对象
D：setter函数对象
以getter方法 C和setter方法 D作为参数，定义对象A的键值为B的属性的访问器，并将结果对象存放到acc中。
如果C是undefined，则不会设置getter，如果D是undefined，则不会设置setter。
默认入参：acc：类对象或类对象的对象原型，方法为静态方法时，acc中是类对象
R：方舟运行时内部使用的16位保留数字
A：method id
B：方法A的形参数量
默认入参：acc：对象
R：方舟运行时内部使用的16位保留数字
默认入参：acc：属性键值
A：对象
默认入参：acc：值
A：生成器
默认入参：acc：值
A：函数对象
默认入参：acc：对象
A：目标对象
默认入参：acc：值
A：数组
B：数组索引
默认入参：acc：对象
R：方舟运行时内部使用的16位保留数字
A：值
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：对象
B：属性键值
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：对象
B：属性键值
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：对象
B：属性键值
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：对象
B：属性键值
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：string id
B：对象
默认入参：acc：值
A：异步的函数对象
默认入参：acc：值
A：异步的函数对象
默认入参：acc：值
R：方舟运行时内部使用的8位保留数字
A：string id
B：对象
在当前函数中，将acc中的值存放到super的键值为索引A对应的字符串的属性上。
若该属性为访问器属性，则将B中的对象作为调用该属性setter函数时的this参数。
默认入参：acc：值
R：方舟运行时内部使用的16位保留数字
A：string id
B：对象
在当前函数中，将acc中的值存放到super的键值为索引A对应的字符串的属性上。
若该属性为访问器属性，则将B中的对象作为调用该属性setter函数时的this参数。
默认入参：acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：对象
B：属性键值
默认入参：acc：函数对象
R：方舟运行时内部使用的16位保留数字
A：string id
B：对象
默认入参：acc：生成器对象
A：生成器状态
将acc中存放的generator的状态设置为A (参考：GeneratorState和AsyncGeneratorState)
A可能的值有以下几项：undefined(0x0)、suspendedStart(0x1)、suspendedYield(0x2)、executing(0x3)、completed(0x4)和awaitingReturn(0x5)。
默认入参：acc：对象
R：方舟运行时内部使用的8位保留数字
默认入参：acc：对象
A：词法环境层级
B：槽位号
A：词法环境层级
B：槽位号
C：对象
默认入参：acc：对象
A：词法环境层级
B：槽位号
默认入参：acc：值
A：string id
B：对象
默认入参：acc：值
A：string id
B：对象
将并发函数的返回值通知运行时。
此指令仅出现在并发函数中。
A：范围寄存器数量
B：对象
C, ..., C + A：属性键值
基于对象B，创建一个排除了键值C, ..., C + A的对象，并将其存放到acc中。
这个指令用例支持使用析构和扩展语法创建对象。
默认入参：acc：值
A：属性键值
B：对象
A：参数数量
B：类对象
B + 1, ..., B + A - 1：传递给构造函数的参数
默认入参：acc：值
A：属性键值
B：对象
A：词法环境中的槽位数量
B：literal id
A：要创建的符号数量
B：literal id
创建A个符号；从索引B对应的字面量数组中获取存放的私有方法，如果其中存在私有实例方法，则额外创建一个符号（"method"），将所有创建出的符号按照创建顺序，依次放到当前类所在的词法环境的末尾。
此指令仅出现在定义类的时候。
默认入参：acc：函数对象
A：参数数量
B, ..., B + A - 1：参数
默认入参：acc：值
A：词法环境层数
B：槽位号
C：对象
默认入参：acc：函数对象
A：参数数量
B：对象
B + 1, ..., B + A：参数
acc：函数对象
R：方舟运行时内部使用的8位保留数字
A：对象
A：参数数量
B, ..., B + A - 1：参数
以B, ..., B + A - 1作为参数, 调用super函数，并将结果存放到acc中。
当A的值是0时，B是undefined。
此指令仅出现在非箭头函数中。
A：对象
B：对象名称
R：方舟运行时内部使用的16位保留数字
A：sendable class的构造函数的method id
B：literal id
C：方法A的形参数量
D：父类
默认入参：acc：类对象
A：参数数量
B, ..., B + A - 1:参数
以B, ..., B + A - 1作为参数，调用acc中所存类的父类的构造函数，并将结果存放到acc中。
如果A的值为0，则B为undefined。
此指令仅出现在箭头函数中。
默认入参：acc：对象
A：错误种类
默认入参：acc：对象
A：属性键值
默认入参：acc：对象
A：错误种类
默认入参：acc：值
A：对象
B：属性键值
默认入参：acc：对象
A：string id
默认入参：acc：值
A：对象
B：属性键值
A：词法环境层级
B：槽位号
默认入参：acc：值
A：共享词法环境层级
B：槽位号
默认入参：acc：值
A：词法环境层级
B：槽位号
默认入参：acc：值
A：共享词法环境层级
B：槽位号
默认入参：acc：值
A：共享词法环境层级
B：槽位号
默认入参：acc：值
A：槽位号
A：共享词法环境层级
B：槽位号
A：共享词法环境层级
B：槽位号
A：共享词法环境层级
B：槽位号
将槽位号为A的补丁变量加载到acc中。
此指令仅出现在补丁模式编译场景下。
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
默认入参：acc：值
A：补丁变量槽位号
将acc中的值存放进槽位号为A的补丁变量中。
此指令仅出现在补丁模式编译场景下。
默认入参：acc：操作数
R：方舟运行时内部使用的8位保留数字
0x14fc
0x15fc
...
0x2efc

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-bytecode-function-name-V14
爬取时间: 2025-04-27 23:04:32
来源: Huawei Developer
概述
本文介绍字节码文件中Method的name_off字段指向的字符串的命名规则，该规则从方舟字节码文件版本12.0.4.0开始生效。
入口函数
模块加载时被执行的函数，名称固定为func_main_0。
非入口函数
其他函数在字节码文件中的名称结构如下:
```typescript
#前缀#原函数名
```
下面的章节将会详细介绍前缀和原函数名。
前缀
前缀包含函数定义时所在的作用域信息。包含以下几个部分：
前缀的结构为：
```typescript
<作用域标签1><作用域名称1>[<重名序号>]<作用域标签2><作用域名称2><[重名序号]>...<作用域标签n><作用域名称n>[<重名序号>]<作用域标签n+1>
```
其中<>仅为便于阅读的分割标识，并不包含在实际的前缀中,[]表示可以为空。仅当出现重名作用域时才需要[<重名序号>]，即[<重名序号>]可以为空。最后一个作用域标签是本函数所对应的标签。
作用域标签
作用域标签表示作用域的类型。作用域和对应的作用域标签如下表所示，其他的作用域不会被记录进函数名中：
| 作用域 | 作用域标签 | 说明 |
| --- | --- | --- |
| 类 | ~ | class关键字定义的作用域 |
| 实例函数 | > | 类的实例成员函数定义的作用域 |
| 静态函数 | < | 类的静态成员函数定义的作用域 |
| 构造函数 | = | 类的构造函数定义的作用域 |
| 普通函数 | * | 除了以上类型的其它所有函数定义的作用域 |
| namespace/module | & | namespace或module关键字定义的作用域 |
| enum | % | enum关键字定义的作用域 |
作用域名称
源代码中定义作用域时所使用的名称。匿名则为空字符串。为了降低字节码体积，方舟编译器会对较长的作用域名称进行优化，此时作用域名称以@十六进制数字的形式体现。这个数字代表作用域名称的字符串在一个字符串数组中的索引：在字节码文件中源代码对应的Class中有一个名为scopeNames的field, 这个field的值是指向一个LiteralArray的偏移，这个LiteralArray存储的是一个字符串数组。十六进制数字就是代表作用域名称在这个数组中的索引。原函数名不会转换为索引。
例子：
```typescript
function longFuncName() {                  // longFuncName的函数名为"#*#longFuncName"，其中"longFuncName"是原函数名，不会转换为索引。
function A() { }                       // A的函数名"#*@0*#A"，其中"@0"表示在其对应LiteralArray中，索引为0的字符串，此时这个字符串是"longFuncName"。即这个函数原本的名称为"#*longFuncName*#A"
function B() { }                       // B的函数名"#*@0*#B"
}
```
重名序号
如果源码中相同作用域下出现了同名的实体，同名的名称后会加上重名序号，重名序号以^十六进制数字的形式表示。出现重名时，第一个不编号即重名序号为空，从第二个开始编号，编号从1开始。
例子：
```typescript
namespace A {
function bar() { }                      // bar的函数名为"#&A*#bar"
}
namespace A {
function foo() { }                      // foo的函数名为"#&A^1*#foo"，其中"^1" 为重名序号
}
```
原函数名
原函数名代表函数在源代码中的名字，匿名函数则为空字符串。同样地，如果源码中相同作用域下出现了同名的函数，重名的名称后面会加上重名序号，包括匿名函数。
```typescript
function foo() {}                           // 原函数名为"foo"
() => { }                                   // 原函数名为""
() => { }                                   // 原函数名为"^1"
```
特殊情况
```typescript
let a = () => {}                            // 原函数名为"a"
```
```typescript
let B = {
b : () => {}                            // 原函数名为"b"
}
```
```typescript
let a = {
"a.b#c^2": () => {}                     // 原函数名为""
"x\\y#": () => {}                       // 原函数名为"^1"
}
```
开发者应尽量避免使用除字母、数字、下划线以外的字符命名函数，以免出现二义性。
示例
```typescript
namespace A {                               // namespace在字节码中的函数名为"#&#A"
class B {                               // 构造函数在字节码中的函数名为"#&A~B=#B"
m() {                               // 函数m在字节码中的函数名为"#&A~B>#m"
return () => {}                 // 匿名函数在字节码中的函数名为"#&A~B>m*#"
}
static s() {}                       // 静态函数s在字节码中的函数名为"#&A~B<#s"
}
enum E {                                // enum在字节码中的函数名为"#&A%#E"
}
}
```
```typescript
namespace LongNamespaceName {               // namespace在字节码中的函数名为"#&#LongNamespaceName"
class LongClassName {                   // 构造函数在字节码中的函数名为"#&@1~@0=#LongClassName"
longFunctionName() {                // 实例函数在字节码中的函数名为"#&@1~@0>#longFunctionName"
}
longFunctionName() {                // 函数在字节码中的函数名为"#&@1~@0>#longFunctionName^1"
function inSecondFunction() {}  // 函数在字节码中的函数名为"#&@1~@0>@2^1*#inSecondFunction"
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/customize-bytecode-during-compilation-V14
爬取时间: 2025-04-27 23:04:45
来源: Huawei Developer
开发者如果希望自定义修改方舟字节码文件的内容，可以使用ArkTS编译工具链提供的自定义修改方舟字节码文件能力。
能力配置说明
准备一个操作方舟字节码文件的动态库文件，在工程的配置文件build-profile.json5中配置编译选项transformLib，选项值为这个动态库的路径，编译器会在指定的时机加载这个动态库，并且执行其中特定的Transform方法。
能力执行机制
如果工程的build-profile.json5没有配置transformLib选项，编译器会直接生成方舟字节码文件到默认位置。如果配置了transformLib并且对应的动态库文件是能正确加载的，编译器会先生成方舟字节码文件到默认的目标位置，然后调用动态库中的Transform方法，同时将这个方舟字节码文件的路径作为参数传入。Transform方法即为开发者自定义修改编写的重新生成方舟字节码文件的相关逻辑。
下面的开发示例是一个动态库的模板，开发者需要根据自身的需求去实现Transform的具体逻辑。
开发示例
1.  创建自定义修改动态库的源码。
2.  使用c语言编译工具（这里使用g++）编译出对应平台的链接库文件。 Windows平台： Linux平台： Mac平台：
3.  在DevEco Studio中配置build-profile.json5中配置transformLib选项（这里用windows环境举例）。 选项中配置的路径为步骤2生成的链接库文件在项目中的路径（这里是dll目录下）。
4.  重新编译项目，即可完成自定义修改方舟字节码。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170237.21429785943423613906316438919706:50001231000000:2800:E3C278B6A726F07FF60821E1A4031498EC93EF01F3AD17BCE0E810D3CFDC2732.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/tool-disassembler-V14
爬取时间: 2025-04-27 23:04:59
来源: Huawei Developer
简介
Disassembler是ArkTS反汇编工具，如果开发者需要分析方舟字节码文件（*.abc）相关问题，可使用Disassembler将字节数据反汇编成可阅读的汇编指令。
工具随DevEco Studio SDK发布，以windows平台为例，Disassembler工具位置为：[DevEco Studio安装目录]\sdk[SDK版本]\HarmonyOS\toolchains\ark_disasm.exe。
命令行说明
反汇编命令：
参数说明：
| 参数 | 是否可缺省 | 描述 |
| --- | --- | --- |
| [options] | 可缺省 | 命令选项，详见下文options选项说明。 |
| input_file | 不可缺省 | 待反汇编的方舟字节码文件路径。 |
| output_file | 不可缺省 | 反汇编内容的输出文件路径。 |
options选项说明：
| 选项 | 是否可缺省 | 是否存在入参 | 描述 |
| --- | --- | --- | --- |
| --debug | 可缺省 | 不带参数 | 使能输出调试信息，默认输出到屏幕。 |
| --debug-file | 可缺省 | 带参数 | 如果使能了--debug，指定调试信息的输出文件。 |
| --help | 可缺省 | 不带参数 | 打印帮助提示。 |
| --skip-string-literals | 可缺省 | 不带参数 | 跳过对字符串字面量的反汇编。 |
| --quiet | 可缺省 | 不带参数 | 使能所有'--skip-'开头的选项。 |
| --verbose | 可缺省 | 不带参数 | 使能输出额外信息（字节位置、方舟字节码格式、操作码）。 |
| --version | 可缺省 | 不带参数 | 显示配套方舟字节码文件版本号以及最低支持的方舟字节码文件版本。 |
使用示例
假设已存在方舟字节码文件：test.abc，其源代码如下：
执行如下命令，就能生成反汇编文件：test.txt。生成的反汇编文件内带有操作码及格式等信息。
查看反汇编文件的内容。
内容如下
使用参数--verbose，可打印偏移量等更多详细信息。
此处列出部分示例。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/source-obfuscation-V14
爬取时间: 2025-04-27 23:05:13
来源: Huawei Developer
代码混淆简介
针对工程源码的混淆可以降低工程被破解攻击的风险，缩短代码的类与成员的名称，减小应用的大小。
使用约束
混淆范围
在应用工程中，代码混淆支持以下格式文件混淆，混淆后的缓存文件保存在模块目录下的build/[...]/release目录下。
局限性
1.语言的限制
代码混淆工具在处理不同编程语言时，其类型分析机制、混淆策略和执行效率都会因目标语言的特性而呈现差异。以业界常用的ProGuard为例，其主要面向Java这类强类型语言进行混淆。由于强类型语言具有严格的类型系统，每个类型都有明确的定义来源。这种特性使得混淆过程中的类型关系追踪和处理更为精确，从而大幅减少了需要配置保留规则的场景。
相比之下，Arkguard混淆工具主要针对JS、TS和ArkTS语言。JS支持运行时动态修改对象、函数，而混淆是在编译阶段进行的静态处理，这种差异可能导致混淆后的名称在运行时无法被正确解析，进而引发运行时异常。TS和ArkTS虽然引入了静态类型系统，但采用了结构性类型机制，即具有相同结构的不同命名类型会被视为等价类型。因此，在TS和ArkTS中仍然无法追溯类型的确切来源。基于这些特性，使用Arkguard时需要对更多的语法场景进行白名单配置，同时，Arkguard采用全局生效的属性保留机制，根据白名单统一保留所有同名属性，而无法支持针对特性类型的精确保留配置。
具体而言，可以参考以下示例：
假设Arkguard支持配置指定类型的白名单，配置类A1作为白名单，类A1的属性prop1在白名单中，而A2中的prop1属性不在白名单中。此时，a2作为参数被传入test函数中，调用prop1属性时会导致功能异常。
```typescript
// 混淆前
class A1 {
prop1: string = '';
}
class A2 {
prop1: string = '';
}
function test(input: A1) {
console.log(input.prop1);
}
let a2 = new A2();
a2.prop1 = 'prop a2';
test(a2);
```
```typescript
// 混淆后
class A1 {
prop1: string = '';
}
class A2 {
a: string = '';
}
function test(input: A1) {
console.log(input.prop1);
}
let a2 = new A2();
a2.a = 'prop a2';
test(a2);
```
综上所述，开发者应了解这种语言差异带来的混淆效果差异，并尽量使用不重复的名称，以使在各种场景下的混淆效果更好。
2.安全保证的有限性
与其他代码混淆工具一样，混淆只能在一定程度上增加逆向过程的难度，并不能真正阻止逆向工程。
并且，由于ArkGuard混淆工具仅支持基础混淆能力，开发者不应只依赖ArkGuard来保证应用的安全性，对于源码安全有高要求的开发者，应考虑使用应用加密、第三方安全加固等安全措施来保护代码。
开启代码混淆
开启混淆步骤
代码混淆能力已在系统中集成，可通过以下方式在DevEco Studio开启使用。
-  开启混淆开关 在本模块build-profile.json5配置文件中的arkOptions.obfuscation.ruleOptions字段中，通过enable字段配置是否开启混淆。使用不同版本的DevEco Studio，enable字段的默认值可能会有所不同，具体可以参考版本变更说明。
-  配置混淆规则 打开混淆开关，仅开启默认混淆功能，默认混淆范围为局部变量和参数。若需要开启更多混淆功能，需要在files字段对应的混淆配置文件obfuscation-rules.txt中进行选项配置。使用不同版本的DevEco Studio，obfuscation-rules.txt文件中的默认值可能会有所不同，具体可以参考版本变更说明。
-  指定release编译 代码混淆当前仅支持release编译，不支持debug编译。即开启混淆开关后，若为release编译则会进行混淆，若为debug编译则不会进行混淆。开发者可参考指定构建模式查看和修改构建模式。 release编译与debug编译的区别并不只包含混淆，若需要明确应用行为差异是否由于混淆，应该通过开启或关闭混淆开关排查，而不是仅通过切换release或debug编译来区分。
三种混淆配置文件
-  obfuscation-rules.txt 不论是HAP、HAR还是HSP，在本模块的build-profile.json5配置文件中都有arkOptions.obfuscation.ruleOptions.files字段，用于指定在编译本模块时需要生效的混淆规则，新建工程时会创建默认文件obfuscation-rules.txt。
-  consumer-rules.txt 对于HAR模块，在build-profile.json5中额外有一个arkOptions.obfuscation.consumerFiles字段，用于指定当本包被依赖时，期望在其他模块生效的混淆规则，新建HAR模块时会创建默认文件consumer-rules.txt。它与obfuscation-rules字段的区别是：obfuscation-rules在编译本模块时生效，consumer-rules在编译依赖本模块的其他模块时生效。
-  obfuscation.txt 不同于以上两种开发者可自行修改的配置文件，obfuscation.txt是在编译构建HAR时根据consumer-rules.txt和依赖模块的混淆规则文件自动生成的文件，它作为一种编译产物存在于发布的HAR包中，用于在其他应用使用该发布包时应用相应的混淆规则。obfuscation.txt内容的生成逻辑请参考混淆规则合并策略。 针对三方库中obfuscation.txt文件，只有在模块的oh-package.json5文件中依赖三方库时，三方库中的obfuscation.txt文件才会生效；如果在工程的oh-package.json5文件中进行依赖，则三方库的obfuscation.txt文件不会生效。
下表简要总结了三种配置文件的差异：

| 配置文件（示例） | 配置类型 | 是否可修改配置 | 是否影响本模块的混淆 | 是否影响其他模块的混淆 |
| --- | --- | --- | --- | --- |
| obfuscation-rules.txt | 自定义 | 是 | 是 | 否 |
| consumer-rules.txt | 自定义 | 是 | 否 | 是 |
| obfuscation.txt | 编译产物 | 不涉及，构建HAR时自动生成 | 不涉及 | 是 |
混淆规则
混淆规则分为两种类型，一种是混淆选项，一种是保留选项；前者是提供顶层作用域名称、属性名称、文件名称等多种混淆功能配置开关，后者是提供各种混淆功能的白名单配置能力。
注意
若修改应用的混淆配置文件，新配置需要重新全量编译才能生效。
混淆选项
-disable-obfuscation
关闭所有混淆。如果使用这个选项，那么构建出来的HAP、HSP或HAR将不会被混淆。
-enable-property-obfuscation
开启属性混淆。 如果使用这个选项，那么所有的属性名都会被混淆，除了下面场景：
-  被import/export直接导入或导出的类、对象的属性名不会被混淆。例如下面例子中的属性名data不会被混淆。
-  ArkUI组件中的属性名不会被混淆。例如下面例子中的message和data不会被混淆。
-  被保留选项指定的属性名不会被混淆。
-  SDK API列表中的属性名不会被混淆。SDK API列表是构建时从SDK中自动提取出来的一个名称列表，其缓存文件为systemApiCache.json，路径为工程目录下build/default/cache/{...}/release/obfuscation中。
-  字符串字面量属性名不会被混淆。例如下面例子中的"name"和"age"不会被混淆。 如果想混淆字符串字面量属性名，需要在该选项的基础上再使用-enable-string-property-obfuscation选项。例如： 注意： 1.如果代码里面有字符串属性名包含特殊字符(除了a-z，A-Z，0-9，_之外的字符)，例如let obj = {"\n": 123, "": 4, " ": 5}，建议不要开启-enable-string-property-obfuscation选项，因为可能无法通过保留选项来指定保留这些名字。 2.SDK API的属性白名单中不包含声明文件中使用的字符串常量值，例如示例中的字符串'ohos.want.action.home'未包含在属性白名单中。 因此在开启了-enable-string-property-obfuscation选项时，如果想保留代码中使用的SDK API字符串常量的属性不被混淆，例如obj['ohos.want.action.home']，那么需要使用keep选项保留。
-enable-toplevel-obfuscation
开启顶层作用域名称混淆。如果使用这个选项，那么所有的顶层作用域的名称都会被混淆，除了下面场景：
-enable-filename-obfuscation
开启文件/文件夹名称混淆。如果使用这个选项，那么所有的文件/文件夹名称都会被混淆，例如：
除了下面场景：
注意：
由于系统会在应用运行时加载某些指定的文件，针对这类文件，开发者需要手动在-keep-file-name选项中配置相应的白名单，防止指定文件被混淆，导致运行失败。
编译入口、Ability组件、Worker多线程，这三种不能混淆的文件名在DevEco Studio 5.0.3.500版本已被自动收集进白名单中，无需再手动配置，其它不能混淆文件名的场景仍需开发者手动配置。
-enable-export-obfuscation
开启直接导入或导出的类或对象的名称和属性名混淆。如果使用这个选项，那么模块中的直接导入或导出的名称都会被混淆，除了下面场景：
注意：
1.  混淆导入或导出的类中属性名称需要同时开启-enable-property-obfuscation与-enable-export-obfuscation选项。
2.  编译HSP时，如果开启-enable-export-obfuscation选项，需要在模块中的混淆配置文件obfuscation-rules.txt中保留对外暴露的接口。
3.  HAP/HSP/HAR依赖HSP场景下，编译时如果开启-enable-export-obfuscation选项，需要在模块中的混淆配置文件obfuscation-rules.txt中保留HSP导入的接口。
-compact
去除不必要的空格符和所有的换行符。如果使用这个选项，那么所有代码会被压缩到一行。
注意：
release模式构建的应用栈信息仅包含代码行号，不包含列号，因此compact功能开启后无法依据报错栈中的行号定位到源码具体位置。
-remove-log
删除以下场景中对 console.*语句的调用，要求console.*语句返回值未被调用。
1.  代码块中的调用 例如：
2.  module或namespace中的调用 例如：
```typescript
namespace ns {
console.log('in ns');
}
```
-print-namecache filepath
将名称缓存保存到指定的文件路径。名称缓存包含名称混淆前后的映射。
注意：
每次全量构建工程时都会生成新的namecache.json文件，因此您每次发布新版本时都要注意保存一个该文件的副本。
-apply-namecache filepath
复用指定的名称缓存文件。名字将会被混淆成缓存映射对应的名字，如果没有对应，将会被混淆成新的随机段名字。
该选项应该在增量编译场景中被使用。
默认情况下，DevEco Studio会在临时的缓存目录中保存缓存文件，并且在增量编译场景中自动应用该缓存文件。
缓存目录：build/default/cache/{...}/release/obfuscation。
-remove-comments
删除编译生成的声明文件中的JsDoc注释。
注意：
编译生成的源码文件中的注释默认会被全部删除，不支持配置保留。
可通过keep-comments配置来保留编译生成的声明文件中的JsDoc注释。
保留选项
-keep-property-name [,identifiers,...]
指定想保留的属性名，支持使用名称类通配符。例如下面的例子：
-  该选项在开启-enable-property-obfuscation时生效。
-  属性白名单作用于全局。即代码中出现多个重名属性，只要与-keep-property-name配置白名单名称相同，均不会被混淆。
哪些属性名应该被保留?
1.为了保障混淆的正确性，建议保留所有不通过点语法访问的属性。例如，通过字符串访问的对象属性：
对于如下的字符串常量形式的属性调用，可以选择性保留：
2.对于间接导出的场景，例如export MyClass和let a = MyClass; export {a};，如果不想混淆它们的属性名，那么需要使用保留选项来保留这些属性名。另外，对于直接导出的类或对象的属性的属性名，例如下面例子中的name和age，如果不想混淆它们，那么也需要使用保留选项来保留这些属性名。
3.so库的API（例如示例中的foo），如果要在ArkTS/TS/JS文件中使用需手动保留API名称。
4.JSON数据解析及对象序列化时，需要保留使用到的字段，例如：
```typescript
// 示例JSON文件结构(test.json)：
/*
{
"jsonProperty": "value",
"otherProperty": "value2"
}
*/
const jsonData = fs.readFileSync('./test.json', 'utf8');
let jsonObj = JSON.parse(jsonData);
let jsonProp = jsonObj.jsonProperty; // jsonProperty应该被保留
class jsonTest {
prop1: string = '';
prop2: number = 0
}
let obj = new jsonTest();
const jsonStr = JSON.stringify(obj); // prop1、prop2会被混淆，应该被保留
```
5.使用到的数据库相关的字段，需要手动保留。例如，数据库键值对类型（ValuesBucket）中的属性：
6.源码中自定义装饰器修饰了成员变量、成员方法、参数，同时其源码编译的中间产物为js文件时（如编译release源码HAR或者源码包含@ts-ignore、@ts-nocheck），这些装饰器所在的成员变量/成员方法名称需要被保留。这是由于ts高级语法特性转换为js标准语法时，将上述装饰器所在的成员变量/成员方法名称硬编码为字符串常量。
示例：
-keep-global-name [,identifiers,...]
指定要保留的顶层作用域或导入和导出元素的名称，支持使用名称类通配符。例如：
namespace中导出的名称可以通过-keep-global-name选项保留，示例如下：
-keep-global-name指定的白名单作用于全局。即代码中出现多个顶层作用域名称或者导出名称，只要与-keep-global-name配置的白名单名称相同，均不会被混淆。
哪些顶层作用域的名称应该被保留?
在JavaScript中全局变量是globalThis的属性。如果在代码中使用globalThis去访问全局变量，那么该变量名应该被保留。
示例：
当以命名导入的方式导入 so 库的 API时，若同时开启-enable-toplevel-obfuscation和-enable-export-obfuscation选项，需要手动保留 API 的名称。
-keep-file-name [,identifiers,...]
指定要保留的文件/文件夹的名称(不需要写文件后缀)，支持使用名称类通配符。例如：
哪些文件名应该被保留?
1.在使用require引入文件路径时，由于ArkTS不支持CommonJS语法，因此这种情况下路径应该被保留。
2.对于动态导入的路径名，由于无法识别import函数中的参数是否为路径，因此这种情况下路径应该被保留。
3.在使用动态路由进行路由跳转时，传递给动态路由的路径应该被保留。动态路由提供系统路由表和自定义路由表两种方式。若采用自定义路由表进行跳转，配置白名单的方式与上述第二种动态引用场景一致。而若采用系统路由表进行跳转，则需要将模块下resources/base/profile/route_map.json文件中pageSourceFile字段对应的路径添加到白名单中。
-keep-comments [,identifiers,...]
保留编译生成的声明文件中class，function，namespace，enum，struct，interface，module，type及属性上方的JsDoc注释，支持使用名称类通配符。例如想保留声明文件中Human类上方的JsDoc注释，可进行以下配置：
注意：
-keep-dts filepath
指定路径的.d.ts文件中的名称（例如变量名、类名、属性名等）会被添加至-keep-global-name和-keep-property-name白名单中。请注意，filepath仅支持绝对路径，并且可以指定为一个目录。在这种情况下，该目录中所有.d.ts文件中的名称都将被保留。
-keep filepath
保留指定相对路径中的所有名称（例如变量名、类名、属性名等）不被混淆。这个路径可以是文件与文件夹，若是文件夹，则文件夹下的文件及子文件夹中文件都不混淆。
路径仅支持相对路径，./与../为相对于混淆配置文件所在目录，支持使用路径类通配符。
如何在模块中保留远程HAR包
方式一：指定远程HAR包在模块级oh_modules中的具体路径（该路径为软链接路径，真实路径为工程级oh_modules中的文件路径）。因为在配置模块级oh_modules中的路径作为白名单时，需要具体到包名或之后的目录才能正确地软链接到真实的目录路径，所以不能仅配置HAR包的上级目录名称。
方式二：指定远程HAR包在工程级oh_modules中的具体路径。因为工程级oh_modules中的文件路径都为真实路径，所以其路径均可配置。
模块级oh_moudles和工程级oh_modules在DevEco Studio中的目录结构如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170238.38659469199029176028677917951513:50001231000000:2800:C234A29B71551DD6CA75F4B299B45C3C161BD69BBAFD6A0F19B9FE4FDF0BE734.png)
注意：
保留选项支持的通配符
名称类通配符
名称类通配符使用方式如下：

| 通配符 | 含义 | 示例 |
| --- | --- | --- |
| ? | 匹配任意单个字符 | "AB?"能匹配"ABC"等，但不能匹配"AB" |
| * | 匹配任意数量的任意字符 | "*AB*"能匹配"AB"、"aABb"、"cAB"、"ABc"等 |
使用示例：
保留所有以a开头的属性名称：
保留所有单个字符的属性名称：
保留所有属性名称：
路径类通配符
路径类通配符使用方式如下：

| 通配符 | 含义 | 示例 |
| --- | --- | --- |
| ? | 匹配任意单个字符，除了路径分隔符/ | "../a?"能匹配"../ab"等，但不能匹配"../a/" |
| * | 匹配任意数量的任意字符，除了路径分隔符/ | "../a*/c"能匹配"../ab/c"，但不能匹配"../ab/d/s/c" |
| ** | 匹配任意数量的任意字符 | "../a**/c"能匹配"../ab/c"，也能匹配"../ab/d/s/c" |
| ! | 表示非，只能写在某个路径最前端，用来排除用户配置的白名单中已有的某种情况 | "!../a/b/c.ets"表示除"../a/b/c.ets"以外 |
使用示例：
表示路径../a/b/中所有文件夹（不包含子文件夹）中的c.ets文件不会被混淆：
表示路径../a/b/中所有文件夹（包含子文件夹）中的c.ets文件不会被混淆：
表示路径../a/b/中，除了c.ets文件以外的其它文件都不会被混淆。其中，!不可单独使用，只能用来排除白名单中已有的情况：
表示路径../a/中的所有文件（不包含子文件夹）不会被混淆：
表示路径../a/下的所有文件夹（包含子文件夹）中的所有文件不会被混淆：
表示模块内的所有文件不会被混淆：
注意：
(1)以上选项，不支持配置通配符*、?、!作其它含义使用。
例如：
此时*表示匹配任意数量的任意字符，配置效果为所有属性名称都不混淆，而不是只有*属性不被混淆。
(2)-keep选项中只允许使用/路径格式，不支持\或\\。
注释
可以使用#在混淆规则文件中进行注释。每行以#开头的文本会被当做是注释，例如下面的例子：
构建HAR时，注释不会被合并到最后的obfuscation.txt文件中。
混淆规则合并策略
编译工程中的某个模块时，其最终所应用的混淆规则是以下文件中配置的混淆规则的合并:
上述文件中的混淆规则的优先级是一致的。构建模块时，这些规则文件将按照以下合并策略（伪代码）进行合并。
最后使用的混淆规则来自于对象finalRule。
如果构建的是HAR，那么最终的obfuscation.txt文件内容来自于自身和本地依赖的library的consumerFiles选项，以及依赖的HAR的obfuscation.txt文件的合并。
当consumerFiles指定的混淆配置文件中包含以下混淆规则时，这些混淆规则会被合并到HAR包的obfuscation.txt文件中，而其他混淆规则不会。
library中混淆注意事项
1.  如果consumerFiles指定的混淆配置文件中包含上述混淆选项，当其他模块依赖该HAR包时，这些混淆选项会与主模块的混淆规则合并，从而影响主模块。因此不建议开发者在consumer-rules.txt文件中配置混淆选项，建议仅配置保留选项。
2.  如果在consumerFiles指定的混淆配置文件中添加-keep-dts选项，会被转换成-keep-global-name和-keep-property-name。
报错栈还原
经过混淆的应用程序中代码名称会发生更改，crash时打印的报错栈更难以理解，因为报错栈与源码不完全一致。开发人员可使用DevEco Studio命令工具Command Line Tools中的hstack插件来还原源码堆栈，进而分析问题。反混淆工具需要使用应用编译过程中生成的sourceMaps.map文件以及混淆名称映射文件nameCache.json文件，因此请本地备份它们。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170238.26754823946031805220515043229483:50001231000000:2800:8B91062C4FA88F51CFCD8F0B5A15C6CEA9342E8F598130BFF87CD8430598D8AF.png)
代码混淆开启指导
说明
-  DevEco Studio右上角Product选项，将其中Build Mode选择release，可开启release编译模式。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170238.23335473849386949905709872475661:50001231000000:2800:1387F9CA4E83549F974BB91F441AE9B1B134B3DB12B59063D272F415D6E396AA.png)
FAQ
混淆各功能上线SDK版本  

| 混淆选项 | 功能描述 | 最低版本号 |
| --- | --- | --- |
| -disable-obfuscation | 关闭混淆 | 4.0.9.2 |
| -enable-property-obfuscation | 属性混淆 | 4.0.9.2 |
| -enable-string-property-obfuscation | 字符串字面量属性名混淆 | 4.0.9.2 |
| -enable-toplevel-obfuscation | 顶层作用域名称混淆 | 4.0.9.2 |
| -enable-filename-obfuscation | HAR包文件/文件夹名称混淆   HAP/HSP文件/文件夹名称混淆  | 4.1.5.3   5.0.0.19  |
| -enable-export-obfuscation | 向外导入或导出的名称混淆 | 4.1.5.3 |
| -compact | 去除不必要的空格符和所有的换行符 | 4.0.9.2 |
| -remove-log | 删除特定场景中的console.* | 4.0.9.2 |
| -print-namecache | 将名称缓存保存到指定的文件路径 | 4.0.9.2 |
| -apply-namecache | 复用指定的名称缓存文件 | 4.0.9.2 |
| -remove-comments | 删除文件中所有注释 | 4.1.5.3 |
| -keep-property-name | 保留属性名 | 4.0.9.2 |
| -keep-global-name | 保留顶层作用域的名称 | 4.0.9.2 |
| -keep-file-name | 保留HAR包的文件/文件夹的名称   保留HAP/HSP包的文件/文件夹的名称  | 4.1.5.3   5.0.0.19  |
| -keep-dts | 保留指定路径的.d.ts文件中的名称 | 4.0.9.2 |
| -keep-comments | 保留编译生成的声明文件中class，function，namespace，enum，struct，interface，module，type及属性上方的JsDoc注释 | 4.1.5.3 |
| -keep | 保留指定路径中的所有名称 | 5.0.0.18 |
| 通配符 | 名称类和路径类的保留选项支持通配符 | 5.0.0.24 |
HAR包文件/文件夹名称混淆
HAP/HSP文件/文件夹名称混淆
4.1.5.3
5.0.0.19
保留HAR包的文件/文件夹的名称
保留HAP/HSP包的文件/文件夹的名称
4.1.5.3
5.0.0.19
如何查看混淆效果
下图为应用编译的简要流程图：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170238.81894686370440431096966021942540:50001231000000:2800:1129F41535146BAB8F9FA3867E9F24EFCD3C00D928F07AE6F8112D464A2204B1.png)
在混淆结束后会将中间产物落盘，因此可以在编译产物build目录中找到混淆后的中间产物以查看混淆效果，同时可以找到混淆生成的名称映射表及系统API白名单文件。
-  混淆后的文件目录：build/default/[...]/release/模块名
-  混淆名称映射表及系统API白名单目录：build/default/[...]/release/obfuscation
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170238.87534740303250793666674667192521:50001231000000:2800:3022DD4CAB126EDCA49708A31B071330F3EFD5D54B8E5CDFD7C38FED6957F935.png)
如何排查功能异常
排查功能异常步骤
1.  应用运行时崩溃分析方法： 1.打开应用运行日志或者点击DevEco Studio中出现的Crash弹窗，找到运行时崩溃栈。 2.应用运行时崩溃栈中的行号为编译产物的行号，方法名也可能为混淆后名称；因此排查时建议直接根据崩溃栈查看编译产物，进而分析哪些名称不能被混淆，然后将其配置进白名单中。
2.  应用在运行时未崩溃但出现功能异常的分析方法（比如白屏）： 1.打开应用运行日志：选择HiLog，检索与功能异常直接相关的日志，定位问题发生的上下文。 2.定位异常代码段：通过分析日志，找到导致功能异常的具体代码块。 3.增强日志输出：在疑似异常的功能代码中，对处理的数据字段增加日志记录。 4.分析并确定关键字段：通过对新增日志输出的分析，识别是否由于混淆导致该字段的数据异常。 5.配置白名单保护关键字段：将确认在混淆后对应用功能产生直接影响的关键字段添加到白名单中。
排查非预期的混淆能力
若出现预期外的混淆效果，检查是否是依赖的本地模块/三方库开启了某些混淆选项。
示例：
假设当前模块未配置-compact，但是混淆的中间产物中代码都被压缩成一行，可按照以下步骤排查混淆选项：
说明：
三方库中obfuscation.txt不建议配置如下开关选项，这些选项会在主模块开启混淆时生效，进而出现预期外的混淆效果，甚至会出现应用运行时崩溃。因此建议联系发布此三方库方删除这些选项并重新出包。
常见报错案例
开启-enable-property-obfuscation选项可能出现的问题
案例一：报错内容为 Cannot read property 'xxx' of undefined
开启属性混淆后，"jsonProperty" 被混淆成随机字符 "i"，但json文件中为原始名称，从而导致值为undefined。
解决方案：使用-keep-property-name选项将json文件里的字段配置到白名单。
案例二：使用了数据库相关的字段，开启属性混淆后，出现报错
报错内容为 table Account has no column named a23 in 'INSET INTO Account(a23)'
代码里使用了数据库字段，混淆时该SQL语句中字段名称被混淆，但数据库中字段为原始名称，从而导致报错。
解决方案：使用-keep-property-name选项将使用到的数据库字段配置到白名单。
案例三：使用Record<string, Object>作为对象的类型时，该对象里的属性被混淆，导致功能异常
问题现象：
parameters的类型为Record<string, Object>，在开启属性混淆后，parameters对象中的属性linkSource被混淆，进而导致功能异常。示例如下：
问题原因：
在这个示例中，所创建的对象的内容需要传递给系统来加载某个页面，因此对象中的属性名称不能被混淆，否则会造成功能异常。示例中parameters的类型为Record<string, Object>，这只是一个表示以字符串为键的对象的泛型定义，并没有详细描述其内部结构和属性类型。因此，混淆工具无法识别该对象内部哪些属性不应被混淆，从而可能导致内部属性名linkSource被混淆。
解决方案：
将混淆后会出现问题的属性名配置到属性白名单中，示例如下：
同时开启-enable-export-obfuscation和-enable-toplevel-obfuscation选项可能出现的问题
当开启这两个选项时，主模块调用其他模块方法时涉及的方法名称混淆情况如下：
| 主模块 | 依赖模块 | 导入与导出的名称混淆情况 |
| --- | --- | --- |
| HAP/HSP | HSP | HSP和主模块是独立编译的，混淆后名称会不一致，因此都需要配置白名单 |
| HAP/HSP | 本地HAR | 本地HAR与主模块一起编译，混淆后名称一致 |
| HAP/HSP | 三方库 | 三方库中导出的名称及其属性会被收集到白名单，因此导入和导出时都不会被混淆 |
HSP需要将给其他模块用的方法配置到白名单中。因为主模块里也需要配置相同的白名单，所以推荐将HSP配置了白名单的混淆文件(假设名称为hsp-white-list.txt)添加到依赖它的模块的混淆配置项里，即下图files字段里。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170238.62200554528079698542377533056872:50001231000000:2800:DA194688B23EA815993188E5BAA511FCCE389F4C3CA8108002D5BD26416D756E.png)
案例一：动态导入某个类，类定义的地方被混淆，导入类名时却没有混淆，导致报错
导出的类 "Test1" 是一个顶层作用域名，当 "Test1" 被动态使用时，它是一个属性。因为没有开启-enable-property-obfuscation选项，所以名称混淆了，但属性没有混淆。
解决方案：使用-keep-global-name选项将 "Test1" 配置到白名单。
案例二：在使用namespace中的方法时，该方法定义的地方被混淆了，但使用的地方却没有被混淆，导致报错
```typescript
// 混淆前
export namespace ns1 {
export class person1 {}
}
import {ns1} from './file1'
let person1 = new ns1.person1()
// 混淆后
export namespace a3 {
export class b2 {}
}
import {a3} from './file1'
let person1 = new a3.person1()
```
namespace里的 "person1" 属于export元素，当通过 "ns1.person1" 调用时，它被视为一个属性。由于未开-enable-property-obfuscation选项，导致在使用时未对其进行混淆。
解决方案：
案例三：使用了declare global，混淆后报语法错误
报错内容为 SyntaxError: Unexpected token。
解决方案：使用-keep-global-name选项将__global配置到白名单中。
未开启-enable-string-property-obfuscation混淆选项，字符串字面量属性名却被混淆，导致字符串字面量属性名的值为undefined
解决方案：
开启-enable-filename-obfuscation选项后，可能会出现的问题
案例一：报错为 Error Failed to get a resolved OhmUrl for 'D:code/MyApplication/f12/library1/pages/d.ets' imported by 'undefined'
工程的目录结构如下图所示，模块library1的外层还有目录 "directory"，开启文件名混淆后，"directory" 被混淆为f12，导致路径找不到。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170238.33008121026461838708016129348888:50001231000000:2800:79D633C6DE15839011C57D0A20723AAEC9715DA4EBF1852227983DD09C6F174C.png)
解决方案：
案例二：报错为 Cannot find module 'ets/appability/AppAbility' which is application Entry Point
由于系统会在应用运行时加载ability文件，用户需要手动配置相应的白名单，防止指定文件被混淆，导致运行失败。
解决方案：使用-keep-file-name选项，将src/main/module.json5文件中，'srcEntry'字段所对应的路径配置到白名单中。
使用-keep-global-name选项配置白名单时，可能会出现的问题
报错内容为 Cannot read properties of undefined (reading 'has')。
解决方案：将SDK更新至最低4.1.6.3版本。
HAP与HSP依赖相同的本地源码HAR模块，可能会出现的问题
-  若开启-enable-export-obfuscation和-enable-toplevel-obfuscation选项，在应用运行时会出现加载接口失败的问题。 原因是HAP与HSP独立执行构建与混淆流程，本地源码HAR模块中暴露的接口在HAP与HSP中被混淆成不同的名称。
解决方案：
同时开启-enable-property-obfuscation和-keep选项可能会出现的问题
问题现象
使用如下混淆配置：
并且在file2.ts中导入file1.ts的接口。此时，接口中有属性的类型为对象类型，该对象类型的属性在file1.ts中被保留，在file2.ts中被混淆，从而导致调用时引发功能异常。示例如下：
问题原因
-keep选项保留file1.ts文件时，file1.ts中代码不会被混淆。对于导出属性（如address）所属类型内的属性，不会被自动收集在属性白名单中。因此，该类型内的属性在其他文件中被使用时，会被混淆。
解决方案
方案一：使用interface定义该属性的类型，并使用export进行导出，这样该属性会被自动被收集到属性白名单中。示例如下：
方案二：使用-keep-property-name选项，将未直接导出的类型内的属性配置到属性白名单中。示例如下：

