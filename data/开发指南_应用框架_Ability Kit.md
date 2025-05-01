# 合并文件
合并时间: 2025-04-27 22:34:24

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview
爬取时间: 2025-04-27 22:07:46
来源: Huawei Developer
在开始应用开发前，需要先完成以下准备工作。
注册成为开发者
在华为开发者联盟网站上，注册成为开发者，并完成实名认证，从而享受联盟开放的各类能力和服务。
创建应用
在AppGallery Connect（简称AGC）上，参考创建项目和创建应用完成HarmonyOS应用的创建，从而使用各类服务。
配置安装DevEco Studio
安装最新版DevEco Studio。具体安装指导请参见安装DevEco Studio。
使用DevEco Studio创建应用工程
使用DevEco Studio创建应用工程。具体创建工程指导请参见创建一个新的工程。
配置签名信息
使用模拟器和预览器调试无需配置签名信息，使用真机设备调试则需要对HAP进行签名。
目前提供了两种签名方式，请根据实际情况选择：
（条件必选）添加公钥指纹
当应用需要使用以下开放能力的一种或多种时，为正常调试运行应用，需要预先添加公钥指纹。
发布应用前，需要将调试应用的指纹更新为发布指纹。
添加公钥指纹，具体操作请参见配置应用签名证书指纹。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/abilitykit-overview-V14
爬取时间: 2025-04-27 22:07:59
来源: Huawei Developer
Ability Kit（程序框架服务）提供了应用程序开发和运行的应用模型，是系统为开发者提供的应用程序所需能力的抽象提炼，它提供了应用程序必备的组件和运行机制。有了应用模型，开发者可以基于一套统一的模型进行应用开发，使应用开发更简单、高效。
使用场景
能力范围
亮点/特征
1.  为复杂应用而设计
2.  原生支持应用组件级的跨端迁移和多端协同 Stage模型实现了应用组件与UI解耦。
3.  支持多设备和多窗口形态 应用组件管理和窗口管理在架构层面解耦。
4.  平衡应用能力和系统管控成本 Stage模型重新定义应用能力的边界，平衡应用能力和系统管控成本。
与相关Kit的关系
ArkUI: 在Ability Kit的UIAbility组件中，可以使用ArkUI提供的组件、事件、动效、状态管理等能力。
ArkTS: ArkTS提供了语言运行时相关能力。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/application-models-V14
爬取时间: 2025-04-27 22:08:14
来源: Huawei Developer
应用模型的构成要素
应用模型是系统为开发者提供的应用程序所需能力的抽象提炼，它提供了应用程序必备的组件和运行机制。有了应用模型，开发者可以基于一套统一的模型进行应用开发，使应用开发更简单、高效。
应用模型的构成要素包括：
1.  应用组件 应用组件是应用的基本组成单位，是应用的运行入口。用户启动、使用和退出应用过程中，应用组件会在不同的状态间切换，这些状态称为应用组件的生命周期。应用组件提供生命周期的回调函数，开发者通过应用组件的生命周期回调感知应用的状态变化。应用开发者在编写应用时，首先需要编写的就是应用组件，同时还需编写应用组件的生命周期回调函数，并在应用配置文件中配置相关信息。这样，操作系统在运行期间通过配置文件创建应用组件的实例，并调度它的生命周期回调函数，从而执行开发者的代码。
2.  应用进程模型 应用进程模型定义应用进程的创建和销毁方式，以及进程间的通信方式。
3.  应用线程模型 应用线程模型定义应用进程内线程的创建和销毁方式、主线程和UI线程的创建方式、线程间的通信方式。
4.  应用任务管理模型（仅对系统应用开放） 应用任务管理模型定义任务（Mission）的创建和销毁方式，以及任务与组件间的关系。所谓任务，即用户使用一个应用组件实例的记录。每次用户启动一个新的应用组件实例，都会生成一个新的任务。例如，用户启动一个视频应用，此时在“最近任务”界面，将会看到视频应用这个任务，当用户点击这个任务时，系统会把该任务切换到前台，如果这个视频应用中的视频编辑功能也是通过应用组件编写的，那么在用户启动视频编辑功能时，会创建视频编辑的应用组件实例，在“最近任务”界面中，将会展示视频应用、视频编辑两个任务。
5.  应用配置文件 应用配置文件中包含应用配置信息、应用组件信息、权限信息、开发者自定义信息等，这些信息在编译构建、分发和运行阶段分别提供给编译工具、应用市场和操作系统使用。
应用模型概况
随着系统的演进发展，先后提供了两种应用模型：
-  FA（Feature Ability）模型：从API 7开始支持的模型，已经不再主推。
-  Stage模型：从API 9开始新增的模型，是目前主推且会长期演进的模型。在该模型中，由于提供了AbilityStage、WindowStage等类作为应用组件和Window窗口的“舞台”，因此称这种应用模型为Stage模型。
通过对比认识FA模型与Stage模型
Stage模型与FA模型最大的区别在于：Stage模型中，多个应用组件共享同一个ArkTS引擎实例；而FA模型中，每个应用组件独享一个ArkTS引擎实例。因此在Stage模型中，应用组件之间可以方便的共享对象和状态，同时减少复杂应用运行对内存的占用。Stage模型作为主推的应用模型，开发者通过它能够更加便利地开发出分布式场景下的复杂应用。
可通过如下对比表格了解两种模型的整体概况。
表1FA模型与Stage模型差异概览
| 项目 | FA模型 | Stage模型 |
| --- | --- | --- |
| 应用组件 | 1. 组件分类  - PageAbility组件：包含UI，提供展示UI的能力。详细介绍请参见PageAbility组件概述。 - ServiceAbility组件：提供后台服务的能力，无UI。详细介绍请参见ServiceAbility组件概述。 - DataAbility组件：提供数据分享的能力，无UI。详细介绍请参见DataAbility组件概述。 2. 开发方式 通过导出匿名对象、固定入口文件的方式指定应用组件。开发者无法进行派生，不利于扩展能力。 | 1. 组件分类  - UIAbility组件：包含UI，提供展示UI的能力，主要用于和用户交互。详细介绍请参见UIAbility组件概述。 - ExtensionAbility组件：提供特定场景（如卡片、输入法）的扩展能力，满足更多的使用场景。详细介绍请参见ExtensionAbility组件概述。 2. 开发方式 采用面向对象的方式，将应用组件以类接口的形式开放给开发者，可以进行派生，利于扩展能力。 |
| 进程模型 | 有两类进程： 1. 主进程 2. 渲染进程 详细介绍请参见进程模型。 | 有三类进程： 1. 主进程 2. ExtensionAbility进程 3. 渲染进程 详细介绍请参见进程模型。 |
| 线程模型 | 1. ArkTS引擎实例的创建 一个进程可以运行多个应用组件实例，每个应用组件实例分别运行在单独的ArkTS引擎实例中。 2. 线程模型 每个ArkTS引擎实例都在一个单独线程（非主线程）上创建，主线程没有ArkTS引擎实例。 3. 进程内对象共享：不支持。 详细介绍请参见线程模型。 | 1. ArkTS引擎实例的创建 一个进程可以运行多个应用组件实例，所有应用组件实例共享一个ArkTS引擎实例。 2. 线程模型 ArkTS引擎实例在主线程上创建。 3. 进程内对象共享：支持。 详细介绍请参见线程模型。 |
| 应用配置文件 | 使用config.json描述应用信息、HAP信息和应用组件信息。 详细介绍请参见应用配置文件概述（FA模型）。 | 使用app.json5描述应用信息，module.json5描述HAP信息、应用组件信息。 详细介绍请参见应用配置文件概述（Stage模型）。 |
1. 组件分类
- PageAbility组件：包含UI，提供展示UI的能力。详细介绍请参见PageAbility组件概述。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170213.04237254927927575940318192249172:50001231000000:2800:F740AE723CC93DDC3A5F4A314D4136034745D5DFEE720B56131606A49BE2B234.png)
- ServiceAbility组件：提供后台服务的能力，无UI。详细介绍请参见ServiceAbility组件概述。
- DataAbility组件：提供数据分享的能力，无UI。详细介绍请参见DataAbility组件概述。
2. 开发方式
通过导出匿名对象、固定入口文件的方式指定应用组件。开发者无法进行派生，不利于扩展能力。
1. 组件分类
- UIAbility组件：包含UI，提供展示UI的能力，主要用于和用户交互。详细介绍请参见UIAbility组件概述。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170213.42053441213266569925221335755796:50001231000000:2800:746F7A0533BD164A838CF3CD1FDD5083C80A77ACCBC148A636087F87B3DA0647.png)
- ExtensionAbility组件：提供特定场景（如卡片、输入法）的扩展能力，满足更多的使用场景。详细介绍请参见ExtensionAbility组件概述。
2. 开发方式
采用面向对象的方式，将应用组件以类接口的形式开放给开发者，可以进行派生，利于扩展能力。
有两类进程：
1. 主进程
2. 渲染进程
详细介绍请参见进程模型。
有三类进程：
1. 主进程
2. ExtensionAbility进程
3. 渲染进程
详细介绍请参见进程模型。
1. ArkTS引擎实例的创建
一个进程可以运行多个应用组件实例，每个应用组件实例分别运行在单独的ArkTS引擎实例中。
2. 线程模型
每个ArkTS引擎实例都在一个单独线程（非主线程）上创建，主线程没有ArkTS引擎实例。
3. 进程内对象共享：不支持。
详细介绍请参见线程模型。
1. ArkTS引擎实例的创建
一个进程可以运行多个应用组件实例，所有应用组件实例共享一个ArkTS引擎实例。
2. 线程模型
ArkTS引擎实例在主线程上创建。
3. 进程内对象共享：支持。
详细介绍请参见线程模型。
使用config.json描述应用信息、HAP信息和应用组件信息。
详细介绍请参见应用配置文件概述（FA模型）。
使用app.json5描述应用信息，module.json5描述HAP信息、应用组件信息。
详细介绍请参见应用配置文件概述（Stage模型）。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/stage-model-development-V14
爬取时间: 2025-04-27 22:08:27
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/stage-model-development-overview-V14
爬取时间: 2025-04-27 22:08:42
来源: Huawei Developer
基本概念
下图展示了Stage模型中的基本概念。
图1Stage模型概念图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170213.49501751738361953552892691790460:50001231000000:2800:234EF74D7D3031A8463F41EB41E3F0314E0F75489B219CB2EC3F5E3259BA1753.png)
-  AbilityStage 每个Entry类型或者Feature类型的HAP在运行期都有一个AbilityStage类实例，当HAP中的代码首次被加载到进程中的时候，系统会先创建AbilityStage实例。
-  UIAbility组件和ExtensionAbility组件 Stage模型提供UIAbility和ExtensionAbility两种类型的组件，这两种组件都有具体的类承载，支持面向对象的开发方式。 UIAbility组件是一种包含UI的应用组件，主要用于和用户交互。例如，图库类应用可以在UIAbility组件中展示图片瀑布流，在用户选择某个图片后，在新的页面中展示图片的详细内容。同时用户可以通过返回键返回到瀑布流页面。UIAbility组件的生命周期只包含创建/销毁/前台/后台等状态，与显示相关的状态通过WindowStage的事件暴露给开发者。 ExtensionAbility组件是一种面向特定场景的应用组件。开发者并不直接从ExtensionAbility组件派生，而是需要使用ExtensionAbility组件的派生类。目前ExtensionAbility组件有用于卡片场景的FormExtensionAbility，用于输入法场景的InputMethodExtensionAbility，用于闲时任务场景的WorkSchedulerExtensionAbility等多种派生类，这些派生类都是基于特定场景提供的。例如，用户在桌面创建应用的卡片，需要应用开发者从FormExtensionAbility派生，实现其中的回调函数，并在配置文件中配置该能力。ExtensionAbility组件的派生类实例由用户触发创建，并由系统管理生命周期。在Stage模型上，三方应用开发者不能开发自定义服务，而需要根据自身的业务场景通过ExtensionAbility组件的派生类来实现。
-  UIAbility组件是一种包含UI的应用组件，主要用于和用户交互。例如，图库类应用可以在UIAbility组件中展示图片瀑布流，在用户选择某个图片后，在新的页面中展示图片的详细内容。同时用户可以通过返回键返回到瀑布流页面。UIAbility组件的生命周期只包含创建/销毁/前台/后台等状态，与显示相关的状态通过WindowStage的事件暴露给开发者。
-  ExtensionAbility组件是一种面向特定场景的应用组件。开发者并不直接从ExtensionAbility组件派生，而是需要使用ExtensionAbility组件的派生类。目前ExtensionAbility组件有用于卡片场景的FormExtensionAbility，用于输入法场景的InputMethodExtensionAbility，用于闲时任务场景的WorkSchedulerExtensionAbility等多种派生类，这些派生类都是基于特定场景提供的。例如，用户在桌面创建应用的卡片，需要应用开发者从FormExtensionAbility派生，实现其中的回调函数，并在配置文件中配置该能力。ExtensionAbility组件的派生类实例由用户触发创建，并由系统管理生命周期。在Stage模型上，三方应用开发者不能开发自定义服务，而需要根据自身的业务场景通过ExtensionAbility组件的派生类来实现。
-  WindowStage 每个UIAbility实例都会与一个WindowStage类实例绑定，该类起到了应用进程内窗口管理器的作用。它包含一个主窗口。也就是说UIAbility实例通过WindowStage持有了一个主窗口，该主窗口为ArkUI提供了绘制区域。
-  Context 在Stage模型上，Context及其派生类向开发者提供在运行期可以调用的各种资源和能力。UIAbility组件和各种ExtensionAbility组件的派生类都有各自不同的Context类，他们都继承自基类Context，但是各自又根据所属组件，提供不同的能力。
-  UIAbility组件是一种包含UI的应用组件，主要用于和用户交互。例如，图库类应用可以在UIAbility组件中展示图片瀑布流，在用户选择某个图片后，在新的页面中展示图片的详细内容。同时用户可以通过返回键返回到瀑布流页面。UIAbility组件的生命周期只包含创建/销毁/前台/后台等状态，与显示相关的状态通过WindowStage的事件暴露给开发者。
-  ExtensionAbility组件是一种面向特定场景的应用组件。开发者并不直接从ExtensionAbility组件派生，而是需要使用ExtensionAbility组件的派生类。目前ExtensionAbility组件有用于卡片场景的FormExtensionAbility，用于输入法场景的InputMethodExtensionAbility，用于闲时任务场景的WorkSchedulerExtensionAbility等多种派生类，这些派生类都是基于特定场景提供的。例如，用户在桌面创建应用的卡片，需要应用开发者从FormExtensionAbility派生，实现其中的回调函数，并在配置文件中配置该能力。ExtensionAbility组件的派生类实例由用户触发创建，并由系统管理生命周期。在Stage模型上，三方应用开发者不能开发自定义服务，而需要根据自身的业务场景通过ExtensionAbility组件的派生类来实现。
开发流程
基于Stage模型开发应用时，在应用模型部分，涉及如下开发过程。
表1Stage模型开发流程
| 任务 | 简介 | 相关指导 |
| --- | --- | --- |
| 应用组件开发 | 本章节介绍了如何使用Stage模型的UIAbility组件和ExtensionAbility组件开发应用。 | - 应用/组件级配置 - UIAbility组件 - ExtensionAbility组件 - AbilityStage组件容器 - 应用上下文Context - 组件启动规则 |
| 了解进程模型 | 本章节介绍了Stage模型的进程模型以及几种常用的进程间通信方式。 | 进程模型概述 |
| 了解线程模型 | 本章节介绍了Stage模型的线程模型以及几种常用的线程间通信方式。 | 线程模型概述 |
| 应用配置文件 | 本章节介绍Stage模型中应用配置文件的开发要求。 | Stage模型应用配置文件 |
-应用/组件级配置
-UIAbility组件
-ExtensionAbility组件
-AbilityStage组件容器
-应用上下文Context
-组件启动规则

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/stage-model-application-components-V14
爬取时间: 2025-04-27 22:08:56
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/application-component-configuration-stage-V14
爬取时间: 2025-04-27 22:09:10
来源: Huawei Developer
在开发应用时，需要配置应用的一些标签，例如应用的包名、图标等标识特征的属性。本文描述了在开发应用需要配置的一些关键标签。
应用包名配置
应用需要在工程的AppScope目录下的app.json5配置文件中配置bundleName标签，该标签用于标识应用的唯一性。推荐采用反域名形式命名（如com.example.demo，建议第一级为域名后缀com，第二级为厂商/个人名，第三级为应用名，也可以多级）。
图标和标签配置
图标和标签通常一起配置，对应app.json5配置文件和module.json5配置文件中的icon和label。在DevEco Studio 5.0.3.800版本及之后，module.json5配置文件中的icon和label不再强制要求配置，而app.json5配置文件中的icon和label仍然是必选参数。因此，module.json5配置文件中的icon和label可以省略。
生成机制
-  HAP中包含UIAbility 如果在module.json5配置文件的abilities标签中配置了icon和label，且该对应的ability中skills标签下面的entities中包含"entity.system.home"、actions中包含"ohos.want.action.home"或者"action.system.home"，则系统将优先返回module.json5中的icon与label。如果存在多个满足条件的ability，优先返回module.json5中mainElement对应的ability配置的icon和label。 如果在module.json5配置文件的abilities标签中未设置icon和label，系统将返回app.json5中的icon和label。
-  如果在module.json5配置文件的abilities标签中配置了icon和label，且该对应的ability中skills标签下面的entities中包含"entity.system.home"、actions中包含"ohos.want.action.home"或者"action.system.home"，则系统将优先返回module.json5中的icon与label。如果存在多个满足条件的ability，优先返回module.json5中mainElement对应的ability配置的icon和label。
-  如果在module.json5配置文件的abilities标签中未设置icon和label，系统将返回app.json5中的icon和label。
-  HAP中不包含UIAbility，系统将返回app.json5中的icon和label。
-  如果在module.json5配置文件的abilities标签中配置了icon和label，且该对应的ability中skills标签下面的entities中包含"entity.system.home"、actions中包含"ohos.want.action.home"或者"action.system.home"，则系统将优先返回module.json5中的icon与label。如果存在多个满足条件的ability，优先返回module.json5中mainElement对应的ability配置的icon和label。
-  如果在module.json5配置文件的abilities标签中未设置icon和label，系统将返回app.json5中的icon和label。
应用场景
效果图如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170213.77147873518512263522218134133640:50001231000000:2800:68A1DBC935601626EFA3D753598E81CED84EE14BBFC5932FD5AF1FB7327D6177.png)
配置示例
-  方式一：配置app.json5（推荐）
```json
{
"app": {
"icon": "$media:app_icon",
"label": "$string:app_name"
// ...
}
}
```
-  方式二：配置module.json5 如果需要在桌面显示UIAbility图标，除了需要配置icon与label字段，还需要在skills标签下面的entities中添加"entity.system.home"、actions中添加"ohos.want.action.home"。
```json
{
"module": {
// ...
"abilities": [
{
"icon": "$media:icon",
"label": "$string:EntryAbility_label",
"skills": [
{
"entities": [
"entity.system.home"
],
"actions": [
"ohos.want.action.home"
]
}
],
}
]
}
}
```
管控规则
系统对无图标应用实施严格管控，防止一些恶意应用故意配置无桌面应用图标，导致用户找不到软件所在的位置，无法操作卸载应用，在一定程度上保证用户终端设备的安全。
如果预置应用确需隐藏桌面应用图标，需要配置AllowAppDesktopIconHide应用特权。申请该特权后，应用不会在桌面上显示。除预置应用外，其他应用不支持隐藏桌面图标。
应用版本声明配置
应用版本声明需要在工程的AppScope目录下的app.json5配置文件中配置versionCode标签和versionName标签。versionCode用于标识应用的版本号，该标签值为32位非负整数。此数字仅用于确定某个版本是否比另一个版本更新，数值越大表示版本越高。versionName标签标识版本号的文字描述。
Module支持的设备类型配置
Module支持的设备类型需要在module.json5配置文件中配置deviceTypes标签，如果deviceTypes标签中添加了某种设备，则表明当前的Module支持在该设备上运行。
Module权限配置
Module访问系统或其他应用受保护部分所需的权限信息需要在module.json5配置文件中配置requestPermissions标签。该标签用于声明需要申请权限的名称、申请权限的原因以及权限使用的场景。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiability-V14
爬取时间: 2025-04-27 22:09:23
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiability-overview-V14
爬取时间: 2025-04-27 22:09:37
来源: Huawei Developer
概述
UIAbility组件是一种包含UI的应用组件，主要用于和用户交互。
UIAbility的设计理念：
1.  原生支持应用组件级的跨端迁移和多端协同。
2.  支持多设备和多窗口形态。
UIAbility划分原则与建议：
UIAbility组件是系统调度的基本单元，为应用提供绘制界面的窗口。一个应用可以包含一个或多个UIAbility组件。例如，在支付应用中，可以将入口功能和收付款功能分别配置为独立的UIAbility。
每一个UIAbility组件实例都会在最近任务列表中显示一个对应的任务。
对于开发者而言，可以根据具体场景选择单个还是多个UIAbility，划分建议如下：
-  如果开发者希望在任务视图中看到一个任务，建议使用“一个UIAbility+多个页面”的方式，可以避免不必要的资源加载。
-  如果开发者希望在任务视图中看到多个任务，或者需要同时开启多个窗口，建议使用多个UIAbility实现不同的功能。 例如，即时通讯类应用中的消息列表与音视频通话采用不同的UIAbility进行开发，既可以方便地切换任务窗口，又可以实现应用的两个任务窗口在一个屏幕上分屏显示。
任务视图用于快速查看和管理当前设备上运行的所有任务或应用。
声明配置
为使应用能够正常使用UIAbility，需要在module.json5配置文件的abilities标签中声明UIAbility的名称、入口、标签等相关信息。
```json
{
"module": {
// ...
"abilities": [
{
"name": "EntryAbility", // UIAbility组件的名称
"srcEntry": "./ets/entryability/EntryAbility.ets", // UIAbility组件的代码路径
"description": "$string:EntryAbility_desc", // UIAbility组件的描述信息
"icon": "$media:icon", // UIAbility组件的图标
"label": "$string:EntryAbility_label", // UIAbility组件的标签
"startWindowIcon": "$media:icon", // UIAbility组件启动页面图标资源文件的索引
"startWindowBackground": "$color:start_window_background", // UIAbility组件启动页面背景颜色资源文件的索引
// ...
}
]
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiability-lifecycle-V14
爬取时间: 2025-04-27 22:09:51
来源: Huawei Developer
概述
当用户打开、切换和返回到对应应用时，应用中的UIAbility实例会在其生命周期的不同状态之间转换。UIAbility类提供了一系列回调，通过这些回调可以知道当前UIAbility实例的某个状态发生改变，会经过UIAbility实例的创建和销毁，或者UIAbility实例发生了前后台的状态切换。
UIAbility的生命周期包括Create、Foreground、Background、Destroy四个状态，如下图所示。
图1UIAbility生命周期状态
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170213.04782141517355356908081637416523:50001231000000:2800:EDE51C8C729B0E3BB68619BE0DA430AFDA6C226DC53C3257B151C1E0BB7EC56B.png)
生命周期状态说明
Create状态
Create状态为在应用加载过程中，UIAbility实例创建完成时触发，系统会调用onCreate()回调。可以在该回调中进行页面初始化操作，例如变量定义资源加载等，用于后续的UI展示。
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 页面初始化
}
// ...
}
```
Want是对象间信息传递的载体，可以用于应用组件间的信息传递。Want的详细介绍请参见信息传递载体Want。
WindowStageCreate和WindowStageDestroy状态
UIAbility实例创建完成之后，在进入Foreground之前，系统会创建一个WindowStage。WindowStage创建完成后会进入onWindowStageCreate()回调，可以在该回调中设置UI加载、设置WindowStage的事件订阅。
图2WindowStageCreate和WindowStageDestroy状态
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170214.16560701827981740119765701196565:50001231000000:2800:6079B57DF102F45606511F2258FE5CC547C5C5DEA4C6DCD0C02542B4C9C13C6D.png)
在onWindowStageCreate()回调中通过loadContent()方法设置应用要加载的页面，并根据需要调用on('windowStageEvent')方法订阅WindowStage的事件（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）。
不同开发场景下WindowStage事件的时序可能存在差异。
```typescript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[EntryAbility]';
const DOMAIN_NUMBER: number = 0xFF00;
export default class EntryAbility extends UIAbility {
// ...
onWindowStageCreate(windowStage: window.WindowStage): void {
// 设置WindowStage的事件订阅（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）
try {
windowStage.on('windowStageEvent', (data) => {
let stageEventType: window.WindowStageEventType = data;
switch (stageEventType) {
case window.WindowStageEventType.SHOWN: // 切到前台
hilog.info(DOMAIN_NUMBER, TAG, `windowStage foreground.`);
break;
case window.WindowStageEventType.ACTIVE: // 获焦状态
hilog.info(DOMAIN_NUMBER, TAG, `windowStage active.`);
break;
case window.WindowStageEventType.INACTIVE: // 失焦状态
hilog.info(DOMAIN_NUMBER, TAG, `windowStage inactive.`);
break;
case window.WindowStageEventType.HIDDEN: // 切到后台
hilog.info(DOMAIN_NUMBER, TAG, `windowStage background.`);
break;
case window.WindowStageEventType.RESUMED: // 前台可交互状态
hilog.info(DOMAIN_NUMBER, TAG, `windowStage resumed.`);
break;
case window.WindowStageEventType.PAUSED: // 前台不可交互状态
hilog.info(DOMAIN_NUMBER, TAG, `windowStage paused.`);
break;
default:
break;
}
});
} catch (exception) {
hilog.error(DOMAIN_NUMBER, TAG,
`Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}`);
}
hilog.info(DOMAIN_NUMBER, TAG, `%{public}s`, `Ability onWindowStageCreate`);
// 设置UI加载
windowStage.loadContent('pages/Index', (err, data) => {
// ...
});
}
}
```
WindowStage的相关使用请参见窗口开发指导。
对应于onWindowStageCreate()回调。在UIAbility实例销毁之前，则会先进入onWindowStageDestroy()回调，可以在该回调中释放UI资源。
```typescript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
windowStage: window.WindowStage | undefined = undefined;
// ...
onWindowStageCreate(windowStage: window.WindowStage): void {
this.windowStage = windowStage;
// ...
}
onWindowStageDestroy() {
// 释放UI资源
}
}
```
WindowStageWillDestroy状态
对应onWindowStageWillDestroy()回调，在WindowStage销毁前执行，此时WindowStage可以使用。
```typescript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[EntryAbility]';
const DOMAIN_NUMBER: number = 0xFF00;
export default class EntryAbility extends UIAbility {
windowStage: window.WindowStage | undefined = undefined;
// ...
onWindowStageCreate(windowStage: window.WindowStage): void {
this.windowStage = windowStage;
// ...
}
onWindowStageWillDestroy(windowStage: window.WindowStage) {
// 释放通过windowStage对象获取的资源
// 在onWindowStageWillDestroy()中注销WindowStage事件订阅（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）
try {
if (this.windowStage) {
this.windowStage.off('windowStageEvent');
}
} catch (err) {
let code = (err as BusinessError).code;
let message = (err as BusinessError).message;
hilog.error(DOMAIN_NUMBER, TAG, `Failed to disable the listener for windowStageEvent. Code is ${code}, message is ${message}`);
}
}
onWindowStageDestroy() {
// 释放UI资源
}
}
```
WindowStage的相关使用请参见窗口开发指导。
Foreground和Background状态
Foreground和Background状态分别在UIAbility实例切换至前台和切换至后台时触发，对应于onForeground()回调和onBackground()回调。
onForeground()回调，在UIAbility的UI可见之前，如UIAbility切换至前台时触发。可以在onForeground()回调中申请系统需要的资源，或者重新申请在onBackground()中释放的资源。
onBackground()回调，在UIAbility的UI完全不可见之后，如UIAbility切换至后台时候触发。可以在onBackground()回调中释放UI不可见时无用的资源，或者在此回调中执行较为耗时的操作，例如状态保存等。
例如应用在使用过程中需要使用用户定位时，假设应用已获得用户的定位权限授权。在UI显示之前，可以在onForeground()回调中开启定位功能，从而获取到当前的位置信息。
当应用切换到后台状态，可以在onBackground()回调中停止定位功能，以节省系统的资源消耗。
```typescript
import { UIAbility } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
// ...
onForeground(): void {
// 申请系统需要的资源，或者重新申请在onBackground()中释放的资源
}
onBackground(): void {
// 释放UI不可见时无用的资源，或者在此回调中执行较为耗时的操作
// 例如状态保存等
}
}
```
当应用的UIAbility实例已创建，且UIAbility配置为singleton启动模式时，再次调用startAbility()方法启动该UIAbility实例时，只会进入该UIAbility的onNewWant()回调，不会进入其onCreate()和onWindowStageCreate()生命周期回调。应用可以在该回调中更新要加载的资源和数据等，用于后续的UI展示。
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
// ...
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
// 更新资源、数据
}
}
```
Destroy状态
Destroy状态在UIAbility实例销毁时触发。可以在onDestroy()回调中进行系统资源的释放、数据的保存等操作。
例如，调用terminateSelf()方法停止当前UIAbility实例，执行onDestroy()回调，并完成UIAbility实例的销毁。
从API 13开始，如果用户使用最近任务列表一键清理来关闭该UIAbility实例，将不会执行onDestroy()回调，而是会直接终止进程。
```typescript
import { UIAbility } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
// ...
onDestroy() {
// 系统资源的释放、数据的保存等
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiability-launch-type-V14
爬取时间: 2025-04-27 22:10:04
来源: Huawei Developer
UIAbility的启动模式是指UIAbility实例在启动时的不同呈现状态。针对不同的业务场景，系统提供了三种启动模式：
-  singleton（单实例模式）
-  multiton（多实例模式）
-  specified（指定实例模式）
standard是multiton的曾用名，效果与多实例模式一致。
singleton启动模式
singleton启动模式为单实例模式，也是默认情况下的启动模式。
每次调用startAbility()方法时，如果应用进程中该类型的UIAbility实例已经存在，则复用系统中的UIAbility实例。系统中只存在唯一一个该UIAbility实例，即在最近任务列表中只存在一个该类型的UIAbility实例。
图1单实例模式演示效果
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170214.02228351746681048060454251718578:50001231000000:2800:DCC411D7332B547135815ADFF0D7C0B7F70DBBE24862F43FF7DE5CDAF319ED60.gif)
应用的UIAbility实例已创建，该UIAbility配置为单实例模式，再次调用startAbility()方法启动该UIAbility实例。由于启动的还是原来的UIAbility实例，并未重新创建一个新的UIAbility实例，此时只会进入该UIAbility的onNewWant()回调，不会进入其onCreate()和onWindowStageCreate()生命周期回调。如果已经创建的实例仍在启动过程中，调用startAbility接口启动该实例，将收到错误码16000082。
如果需要使用singleton启动模式，在module.json5配置文件中的launchType字段配置为singleton即可。
```json
{
"module": {
// ...
"abilities": [
{
"launchType": "singleton",
// ...
}
]
}
}
```
multiton启动模式
multiton启动模式为多实例模式，每次调用startAbility()方法时，都会在应用进程中创建一个新的该类型UIAbility实例。即在最近任务列表中可以看到有多个该类型的UIAbility实例。这种情况下可以将UIAbility配置为multiton（多实例模式）。
图2多实例模式演示效果
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170214.56789823274345455297431297934049:50001231000000:2800:219775A94686A991ED36D53EC9D8B82277ED37884D399B48467502F15F3F19A4.gif)
multiton启动模式的开发使用，在module.json5配置文件中的launchType字段配置为multiton即可。
```json
{
"module": {
// ...
"abilities": [
{
"launchType": "multiton",
// ...
}
]
}
}
```
specified启动模式
specified启动模式为指定实例模式，针对一些特殊场景使用（例如文档应用中每次新建文档希望都能新建一个文档实例，重复打开一个已保存的文档希望打开的都是同一个文档实例）。
图3指定实例启动模式原理
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170214.22472195400589412492215521761533:50001231000000:2800:7665BE08F34FED5D873AFD3D1F4A421F908286B8AFA5AAE1EE1138943335C1BF.png)
假设应用有两个UIAbility实例，即EntryAbility和SpecifiedAbility。EntryAbility以specified模式启动SpecifiedAbility。基本原理如下：
图4指定实例模式演示效果
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170214.18920166117931332283199705072631:50001231000000:2800:A880520C7C9C101FD9333D2D078D5B8965EBAF33D81E4F412D8987A6F3EA8AA3.gif)
1.  在SpecifiedAbility中，需要将module.json5配置文件的launchType字段配置为specified。
```json
{
"module": {
// ...
"abilities": [
{
"launchType": "specified",
// ...
}
]
}
}
```
2.  在EntryAbility中，调用startAbility()方法时，可以在want参数中传入了自定义参数instanceKey作为唯一标识符，以此来区分不同的UIAbility实例。示例中instanceKey的value值设置为字符串'KEY'。
```typescript
// 在启动指定实例模式的UIAbility时，给每一个UIAbility实例配置一个独立的Key标识
// 例如在文档使用场景中，可以用文档路径作为Key标识
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[Page_StartModel]';
const DOMAIN_NUMBER: number = 0xFF00;
function getInstance(): string {
return 'KEY';
}
@Entry
@Component
struct Page_StartModel {
private KEY_NEW = 'KEY';
build() {
Row() {
Column() {
// ...
Button()
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
// context为调用方UIAbility的UIAbilityContext;
let want: Want = {
deviceId: '', // deviceId为空表示本设备
bundleName: 'com.samples.stagemodelabilitydevelop',
abilityName: 'SpecifiedFirstAbility',
moduleName: 'entry', // moduleName非必选
parameters: {
// 自定义信息
instanceKey: this.KEY_NEW
}
};
context.startAbility(want).then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting SpecifiedAbility.');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start SpecifiedAbility. Code is ${err.code}, message is ${err.message}`);
})
this.KEY_NEW = this.KEY_NEW + 'a';
})
// ...
Button()
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
// context为调用方UIAbility的UIAbilityContext;
let want: Want = {
deviceId: '', // deviceId为空表示本设备
bundleName: 'com.samples.stagemodelabilitydevelop',
abilityName: 'SpecifiedSecondAbility',
moduleName: 'entry', // moduleName非必选
parameters: {
// 自定义信息
instanceKey: getInstance()
}
};
context.startAbility(want).then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting SpecifiedAbility.');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start SpecifiedAbility. Code is ${err.code}, message is ${err.message}`);
})
this.KEY_NEW = this.KEY_NEW + 'a';
})
// ...
}
.width('100%')
}
.height('100%')
}
}
```
3.  开发者根据业务在SpecifiedAbility的onAcceptWant()生命周期回调设置该UIAbility的标识。示例中标识设置为SpecifiedAbilityInstance_KEY。 例如在文档应用中，可以为不同的文档实例内容绑定不同的Key值。每次新建文档时，可以传入一个新的Key值（例如可以将文件的路径作为一个Key标识），此时AbilityStage中启动UIAbility时都会创建一个新的UIAbility实例；当新建的文档保存之后，回到桌面，或者新打开一个已保存的文档，回到桌面，此时再次打开该已保存的文档，此时AbilityStage中再次启动该UIAbility时，打开的仍然是之前原来已保存的文档界面。 以如下步骤所示进行举例说明。
```typescript
import { AbilityStage, Want } from '@kit.AbilityKit';
export default class MyAbilityStage extends AbilityStage {
onAcceptWant(want: Want): string {
// 在被调用方的AbilityStage中，针对启动模式为specified的UIAbility返回一个UIAbility实例对应的一个Key值
// 当前示例指的是module1 Module的SpecifiedAbility
if (want.abilityName === 'SpecifiedFirstAbility' || want.abilityName === 'SpecifiedSecondAbility') {
// 返回的字符串KEY标识为自定义拼接的字符串内容
if (want.parameters) {
return `SpecifiedAbilityInstance_${want.parameters.instanceKey}`;
}
}
// ...
return 'MyAbilityStage';
}
}
```
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiability-usage-V14
爬取时间: 2025-04-27 22:10:18
来源: Huawei Developer
UIAbility组件的基本用法包括：指定UIAbility的启动页面以及获取UIAbility的上下文UIAbilityContext。
指定UIAbility的启动页面
应用中的UIAbility在启动过程中，需要指定启动页面，否则应用启动后会因为没有默认加载页面而导致白屏。可以在UIAbility的onWindowStageCreate()生命周期回调中，通过WindowStage对象的loadContent()方法设置启动页面。
```typescript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage): void {
// Main window is created, set main page for this ability
windowStage.loadContent('pages/Index', (err, data) => {
// ...
});
}
// ...
}
```
在DevEco Studio中创建的UIAbility中，该UIAbility实例默认会加载Index页面，根据需要将Index页面路径替换为需要的页面路径即可。
获取UIAbility的上下文信息
UIAbility类拥有自身的上下文信息，该信息为UIAbilityContext类的实例，UIAbilityContext类拥有abilityInfo、currentHapModuleInfo等属性。通过UIAbilityContext可以获取UIAbility的相关配置信息，如包代码路径、Bundle名称、Ability名称和应用程序需要的环境状态等属性信息，以及可以获取操作UIAbility实例的方法（如startAbility()、connectServiceExtensionAbility()、terminateSelf()等）。
如果需要在页面中获得当前Ability的Context，可调用getContext接口获取当前页面关联的UIAbilityContext或ExtensionContext。
-  在UIAbility中可以通过this.context获取UIAbility实例的上下文信息。
```typescript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 获取UIAbility实例的上下文
let context = this.context;
// ...
}
}
```
-  在页面中获取UIAbility实例的上下文信息，包括导入依赖资源context模块和在组件中定义一个context变量两个部分。 也可以在导入依赖资源context模块后，在具体使用UIAbilityContext前进行变量定义。
```typescript
import { common, Want } from '@kit.AbilityKit';
@Entry
@Component
struct Page_EventHub {
private context = getContext(this) as common.UIAbilityContext;
startAbilityTest(): void {
let want: Want = {
// Want参数信息
};
this.context.startAbility(want);
}
// 页面展示
build() {
// ...
}
}
```
-  当业务完成后，开发者如果想要终止当前UIAbility实例，可以通过调用terminateSelf()方法实现。
```typescript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct Page_UIAbilityComponentsBasicUsage {
// 页面展示
build() {
Column() {
//...
Button('FuncAbilityB')
.onClick(() => {
let context = getContext(this) as common.UIAbilityContext;
try {
context.terminateSelf((err: BusinessError) => {
if (err.code) {
// 处理业务逻辑错误
console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
return;
}
// 执行正常业务
console.info('terminateSelf succeed');
});
} catch (err) {
// 捕获同步的参数错误
let code = (err as BusinessError).code;
let message = (err as BusinessError).message;
console.error(`terminateSelf failed, code is ${code}, message is ${message}`);
}
})
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiability-data-sync-with-ui-V14
爬取时间: 2025-04-27 22:10:32
来源: Huawei Developer
基于当前的应用模型，可以通过以下几种方式来实现UIAbility组件与UI之间的数据同步。
使用EventHub进行数据通信
EventHub为UIAbility组件提供了事件机制，使它们能够进行订阅、取消订阅和触发事件等数据通信能力。
在基类Context中，提供了EventHub对象，可用于在UIAbility组件实例内通信。使用EventHub实现UIAbility与UI之间的数据通信需要先获取EventHub对象，本章节将以此为例进行说明。
1.  在UIAbility中调用eventHub.on()方法注册一个自定义事件“event1”，eventHub.on()有如下两种调用方式，使用其中一种即可。
```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIAbility, Context, Want, AbilityConstant } from '@kit.AbilityKit';
const DOMAIN_NUMBER: number = 0xFF00;
const TAG: string = '[EventAbility]';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 获取eventHub
let eventhub = this.context.eventHub;
// 执行订阅操作
eventhub.on('event1', this.eventFunc);
eventhub.on('event1', (data: string) => {
// 触发事件，完成相应的业务操作
});
hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onCreate');
}
// ...
eventFunc(argOne: Context, argTwo: Context): void {
hilog.info(DOMAIN_NUMBER, TAG, '1. ' + `${argOne}, ${argTwo}`);
return;
}
}
```
2.  在UI中通过eventHub.emit()方法触发该事件，在触发事件的同时，根据需要传入参数信息。
```typescript
import { common } from '@kit.AbilityKit';
import { promptAction } from '@kit.ArkUI';
@Entry
@Component
struct Page_EventHub {
private context = getContext(this) as common.UIAbilityContext;
eventHubFunc(): void {
// 不带参数触发自定义“event1”事件
this.context.eventHub.emit('event1');
// 带1个参数触发自定义“event1”事件
this.context.eventHub.emit('event1', 1);
// 带2个参数触发自定义“event1”事件
this.context.eventHub.emit('event1', 2, 'test');
// 开发者可以根据实际的业务场景设计事件传递的参数
}
build() {
Column() {
// ...
List({ initialIndex: 0 }) {
ListItem() {
Row() {
// ...
}
.onClick(() => {
this.eventHubFunc();
promptAction.showToast({
message: 'EventHubFuncA'
});
})
}
// ...
ListItem() {
Row() {
// ...
}
.onClick(() => {
this.context.eventHub.off('event1');
promptAction.showToast({
message: 'EventHubFuncB'
});
})
}
// ...
}
// ...
}
// ...
}
}
```
3.  在UIAbility的注册事件回调中可以得到对应的触发事件结果，运行日志结果如下所示。
```json
[Example].[Entry].[EntryAbility] 1. []
[Example].[Entry].[EntryAbility] 1. [1]
[Example].[Entry].[EntryAbility] 1. [2,"test"]
```
4.  在自定义事件“event1”使用完成后，可以根据需要调用eventHub.off()方法取消该事件的订阅。
```typescript
import { UIAbility } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
// ...
onDestroy(): void {
this.context.eventHub.off('event1');
}
}
```
使用AppStorage/LocalStorage进行数据同步
ArkUI提供了AppStorage和LocalStorage两种应用级别的状态管理方案，可用于实现应用级别和UIAbility级别的数据同步。使用这些方案可以方便地管理应用状态，提高应用性能和用户体验。其中，AppStorage是一个全局的状态管理器，适用于多个UIAbility共享同一状态数据的情况；而LocalStorage则是一个局部的状态管理器，适用于单个UIAbility内部使用的状态数据。通过这两种方案，开发者可以更加灵活地控制应用状态，提高应用的可维护性和可扩展性。详细请参见应用级变量的状态管理。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiability-intra-device-interaction-V14
爬取时间: 2025-04-27 22:11:26
来源: Huawei Developer
UIAbility是系统调度的最小单元。在设备内的功能模块之间跳转时，会涉及到启动特定的UIAbility，包括应用内的其他UIAbility、或者其他应用的UIAbility（例如启动三方支付UIAbility）。
本文主要介绍启动应用内的UIAbility组件的方式。应用间的组件跳转详见应用间跳转。
启动应用内的UIAbility
当一个应用内包含多个UIAbility时，存在应用内启动UIAbility的场景。例如在支付应用中从入口UIAbility启动收付款UIAbility。
假设应用中有两个UIAbility：EntryAbility和FuncAbility（可以在同一个Module中，也可以在不同的Module中），需要从EntryAbility的页面中启动FuncAbility。
1.  在EntryAbility中，通过调用startAbility()方法启动UIAbility，want为UIAbility实例启动的入口参数，其中bundleName为待启动应用的Bundle名称，abilityName为待启动的Ability名称，moduleName在待启动的UIAbility属于不同的Module时添加，parameters为自定义信息参数。示例中的context的获取方式请参见获取UIAbility的上下文信息。
```typescript
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[Page_UIAbilityComponentsInteractive]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Page_UIAbilityComponentsInteractive {
private context = getContext(this) as common.UIAbilityContext;
build() {
Column() {
//...
List({ initialIndex: 0 }) {
ListItem() {
Row() {
//...
}
.onClick(() => {
// context为Ability对象的成员，在非Ability对象内部调用需要
// 将Context对象传递过去
let wantInfo: Want = {
deviceId: '', // deviceId为空表示本设备
bundleName: 'com.samples.stagemodelabilitydevelop',
moduleName: 'entry', // moduleName非必选
abilityName: 'FuncAbilityA',
parameters: {
// 自定义信息
info: '来自EntryAbility Page_UIAbilityComponentsInteractive页面'
},
};
// context为调用方UIAbility的UIAbilityContext
this.context.startAbility(wantInfo).then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
}).catch((error: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, 'startAbility failed.');
});
})
}
//...
}
//...
}
//...
}
}
```
2.  在FuncAbility的onCreate()或者onNewWant()生命周期回调文件中接收EntryAbility传递过来的参数。 在被拉起的FuncAbility中，可以通过获取传递过来的want参数的parameters来获取拉起方UIAbility的PID、Bundle Name等信息。
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
export default class FuncAbilityA extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 接收调用方UIAbility传过来的参数
let funcAbilityWant = want;
let info = funcAbilityWant?.parameters?.info;
}
//...
}
```
3.  在FuncAbility业务完成之后，如需要停止当前UIAbility实例，在FuncAbility中通过调用terminateSelf()方法实现。 调用terminateSelf()方法停止当前UIAbility实例时，默认会保留该实例的快照（Snapshot），即在最近任务列表中仍然能查看到该实例对应的任务。如不需要保留该实例的快照，可以在其对应UIAbility的module.json5配置文件中，将abilities标签的removeMissionAfterTerminate字段配置为true。
```typescript
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[Page_FromStageModel]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Page_FromStageModel {
build() {
Column() {
//...
Button('FuncAbilityB')
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext; // UIAbilityContext
// context为需要停止的UIAbility实例的AbilityContext
context.terminateSelf((err) => {
if (err.code) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to terminate self. Code is ${err.code}, message is ${err.message}`);
return;
}
});
})
}
//...
}
}
```
4.  如需要关闭应用所有的UIAbility实例，可以调用ApplicationContext的killAllProcesses()方法实现关闭应用所有的进程。
启动应用内的UIAbility并获取返回结果
在一个EntryAbility启动另外一个FuncAbility时，希望在被启动的FuncAbility完成相关业务后，能将结果返回给调用方。例如在应用中将入口功能和账号登录功能分别设计为两个独立的UIAbility，在账号登录UIAbility中完成登录操作后，需要将登录的结果返回给入口UIAbility。
1.  在EntryAbility中，调用startAbilityForResult()接口启动FuncAbility，异步回调中的data用于接收FuncAbility停止自身后返回给EntryAbility的信息。示例中的context的获取方式请参见获取UIAbility的上下文信息。
```typescript
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[Page_UIAbilityComponentsInteractive]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Page_UIAbilityComponentsInteractive {
build() {
Column() {
//...
List({ initialIndex: 0 }) {
ListItem() {
Row() {
//...
}
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext; // UIAbilityContext
const RESULT_CODE: number = 1001;
let want: Want = {
deviceId: '', // deviceId为空表示本设备
bundleName: 'com.samples.stagemodelabilitydevelop',
moduleName: 'entry', // moduleName非必选
abilityName: 'FuncAbilityA',
parameters: {
// 自定义信息
info: '来自EntryAbility UIAbilityComponentsInteractive页面'
}
};
context.startAbilityForResult(want).then((data) => {
if (data?.resultCode === RESULT_CODE) {
// 解析被调用方UIAbility返回的信息
let info = data.want?.parameters?.info;
hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(info) ?? '');
if (info !== null) {
promptAction.showToast({
message: JSON.stringify(info)
});
}
}
hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(data.resultCode) ?? '');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability for result. Code is ${err.code}, message is ${err.message}`);
});
})
}
//...
}
//...
}
//...
}
}
```
2.  在FuncAbility停止自身时，需要调用terminateSelfWithResult()方法，入参abilityResult为FuncAbility需要返回给EntryAbility的信息。
```typescript
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[Page_FuncAbilityA]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Page_FuncAbilityA {
build() {
Column() {
//...
List({ initialIndex: 0 }) {
ListItem() {
Row() {
//...
}
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext; // UIAbilityContext
const RESULT_CODE: number = 1001;
let abilityResult: common.AbilityResult = {
resultCode: RESULT_CODE,
want: {
bundleName: 'com.samples.stagemodelabilitydevelop',
moduleName: 'entry', // moduleName非必选
abilityName: 'FuncAbilityB',
parameters: {
info: '来自FuncAbility Index页面'
},
},
};
context.terminateSelfWithResult(abilityResult, (err) => {
if (err.code) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to terminate self with result. Code is ${err.code}, message is ${err.message}`);
return;
}
});
})
}
//...
}
//...
}
//...
}
}
```
3.  FuncAbility停止自身后，EntryAbility通过startAbilityForResult()方法回调接收被FuncAbility返回的信息，RESULT_CODE需要与前面的数值保持一致。
```typescript
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[Page_UIAbilityComponentsInteractive]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Page_UIAbilityComponentsInteractive {
build() {
Column() {
//...
List({ initialIndex: 0 }) {
ListItem() {
Row() {
//...
}
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext; // UIAbilityContext
const RESULT_CODE: number = 1001;
let want: Want = {
deviceId: '', // deviceId为空表示本设备
bundleName: 'com.samples.stagemodelabilitydevelop',
moduleName: 'entry', // moduleName非必选
abilityName: 'FuncAbilityA',
parameters: {
// 自定义信息
info: '来自EntryAbility UIAbilityComponentsInteractive页面'
}
};
context.startAbilityForResult(want).then((data) => {
if (data?.resultCode === RESULT_CODE) {
// 解析被调用方UIAbility返回的信息
let info = data.want?.parameters?.info;
hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(info) ?? '');
if (info !== null) {
promptAction.showToast({
message: JSON.stringify(info)
});
}
}
hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(data.resultCode) ?? '');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability for result. Code is ${err.code}, message is ${err.message}`);
});
})
}
//...
}
//...
}
//...
}
}
```
启动UIAbility的指定页面
概述
一个UIAbility可以对应多个页面，在不同的场景下启动该UIAbility时需要展示不同的页面，例如从一个UIAbility的页面中跳转到另外一个UIAbility时，希望启动目标UIAbility的指定页面。
UIAbility的启动分为两种情况：UIAbility冷启动和UIAbility热启动。
本文主要讲解目标UIAbility冷启动和目标UIAbility热启动两种启动指定页面的场景，以及在讲解启动指定页面之前会讲解到在调用方如何指定启动页面。
调用方UIAbility指定启动页面
调用方UIAbility启动另外一个UIAbility时，通常需要跳转到指定的页面。例如FuncAbility包含两个页面（Index对应首页，Second对应功能A页面），此时需要在传入的want参数中配置指定的页面路径信息，可以通过want中的parameters参数增加一个自定义参数传递页面跳转信息。示例中的context的获取方式请参见获取UIAbility的上下文信息。
```typescript
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[Page_UIAbilityComponentsInteractive]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Page_UIAbilityComponentsInteractive {
build() {
Column() {
//...
List({ initialIndex: 0 }) {
ListItem() {
Row() {
//...
}
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext; // UIAbilityContext
let want: Want = {
deviceId: '', // deviceId为空表示本设备
bundleName: 'com.samples.stagemodelabilityinteraction',
moduleName: 'entry', // moduleName非必选
abilityName: 'FuncAbility',
parameters: { // 自定义参数传递页面信息
router: 'funcA'
}
};
// context为调用方UIAbility的UIAbilityContext
context.startAbility(want).then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting ability.');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability. Code is ${err.code}, message is ${err.message}`);
});
})
}
//...
}
//...
}
//...
}
}
```
目标UIAbility冷启动
目标UIAbility冷启动时，在目标UIAbility的onCreate()生命周期回调中，接收调用方传过来的参数。然后在目标UIAbility的onWindowStageCreate()生命周期回调中，解析调用方传递过来的want参数，获取到需要加载的页面信息url，传入windowStage.loadContent()方法。
```typescript
import { AbilityConstant, Want, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window, UIContext } from '@kit.ArkUI';
const DOMAIN_NUMBER: number = 0xFF00;
const TAG: string = '[EntryAbility]';
export default class EntryAbility extends UIAbility {
funcAbilityWant: Want | undefined = undefined;
uiContext: UIContext | undefined = undefined;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 接收调用方UIAbility传过来的参数
this.funcAbilityWant = want;
}
onWindowStageCreate(windowStage: window.WindowStage): void {
// Main window is created, set main page for this ability
hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');
// Main window is created, set main page for this ability
let url = 'pages/Index';
if (this.funcAbilityWant?.parameters?.router && this.funcAbilityWant.parameters.router === 'funcA') {
url = 'pages/Page_ColdStartUp';
}
windowStage.loadContent(url, (err, data) => {
// ...
});
}
}
```
目标UIAbility热启动
在应用开发中，会遇到目标UIAbility实例之前已经启动过的场景，这时再次启动目标UIAbility时，不会重新走初始化逻辑，只会直接触发onNewWant()生命周期方法。为了实现跳转到指定页面，需要在onNewWant()中解析参数进行处理。
例如短信应用和联系人应用配合使用的场景。
图1 目标UIAbility热启动
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170215.96901269900600816647802158643659:50001231000000:2800:54AA4B16A8933101506F132C2503182DE645AF296D0D381535D273C2B1E19D29.png)
开发步骤如下所示。
1.  冷启动短信应用的UIAbility实例时，在onWindowStageCreate()生命周期回调中，通过调用getUIContext()接口获取UI上下文实例UIContext对象。
```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Want, UIAbility } from '@kit.AbilityKit';
import { window, UIContext } from '@kit.ArkUI';
const DOMAIN_NUMBER: number = 0xFF00;
const TAG: string = '[EntryAbility]';
export default class EntryAbility extends UIAbility {
funcAbilityWant: Want | undefined = undefined;
uiContext: UIContext | undefined = undefined;
// ...
onWindowStageCreate(windowStage: window.WindowStage): void {
// Main window is created, set main page for this ability
hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');
let url = 'pages/Index';
if (this.funcAbilityWant?.parameters?.router && this.funcAbilityWant.parameters.router === 'funcA') {
url = 'pages/Page_ColdStartUp';
}
windowStage.loadContent(url, (err, data) => {
if (err.code) {
return;
}
let windowClass: window.Window;
windowStage.getMainWindow((err, data) => {
if (err.code) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to obtain the main window. Code is ${err.code}, message is ${err.message}`);
return;
}
windowClass = data;
this.uiContext = windowClass.getUIContext();
});
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
});
}
}
```
2.  在短信应用UIAbility的onNewWant()回调中解析调用方传递过来的want参数，通过调用UIContext中的getRouter()方法获取Router对象，并进行指定页面的跳转。此时再次启动该短信应用的UIAbility实例时，即可跳转到该短信应用的UIAbility实例的指定页面。
```typescript
import { AbilityConstant, Want, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import type { Router, UIContext } from '@kit.ArkUI';
import type { BusinessError } from '@kit.BasicServicesKit';
const DOMAIN_NUMBER: number = 0xFF00;
const TAG: string = '[EntryAbility]';
export default class EntryAbility extends UIAbility {
funcAbilityWant: Want | undefined = undefined;
uiContext: UIContext | undefined = undefined;
// ...
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
if (want?.parameters?.router && want.parameters.router === 'funcA') {
let funcAUrl = 'pages/Page_HotStartUp';
if (this.uiContext) {
let router: Router = this.uiContext.getRouter();
router.pushUrl({
url: funcAUrl
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to push url. Code is ${err.code}, message is ${err.message}`);
});
}
}
}
}
```
当被调用方UIAbility组件启动模式设置为multiton启动模式时，每次启动都会创建一个新的实例，那么onNewWant()回调就不会被用到。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ability-recover-guideline-V14
爬取时间: 2025-04-27 22:11:40
来源: Huawei Developer
场景介绍
当应用后台运行时，可能由于系统资源管控等原因导致应用关闭、进程退出，应用直接退出可能会导致用户数据丢失。如果应用在UIAbilityContext中启用了UIAbility备份恢复功能，并对临时数据进行保存，则可以在应用退出后的下一次启动时恢复先前的状态和数据（包括应用的页面栈以及onSaveState接口中保存的数据），从而保证用户体验的连贯性。
应用正常关闭时，不会触发UIAbility备份流程。应用正常启动（例如通过startAbility接口启动或点击图标启动），不触发UIAbility恢复流程。
运行机制
约束限制
-  UIAbility备份恢复支持多实例，备份数据保存7天，以文件的形式存储在应用的沙箱路径中。
-  备份数据以WantParams形式存储，由于序列化大小限制，支持的最大数据量为200KB。
-  重启设备不支持还原备份。
-  UIExtensionAbility不支持备份恢复。
接口说明
UIAbility备份恢复接口由UIAbilityContext模块提供，开发者可以通过在UIAbility中通过this.context直接调用，详见开发步骤。
| 接口名称 | 说明 |
| --- | --- |
| setRestoreEnabled(enabled: boolean): void | 设置当UIAbility从后台切换回时是否启用恢复。 |
setRestoreEnabled:需要在应用初始化阶段调用（onForeground前），比如UIAbility的onCreate调用。
开发步骤
开发者需要在应用模块初始化时启用UIAbility备份恢复功能。示例如下。
```typescript
import { UIAbility } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate() {
console.info("[Demo] EntryAbility onCreate");
this.context.setRestoreEnabled(true);
}
}
```
开发者主动保存数据，在UIAbility启动时恢复。下面为示例。
```typescript
import { AbilityConstant，UIAbility，Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
console.info("[Demo] EntryAbility onCreate");
this.context.setRestoreEnabled(true);
if (want && want.parameters) {
let recoveryMyData = want.parameters["myData"];
}
}
onSaveState(state:AbilityConstant.StateType, wantParams: Record<string, Object>) {
// Ability has called to save app data
console.log("[Demo] EntryAbility onSaveState");
wantParams["myData"] = "my1234567";
return AbilityConstant.OnSaveResult.ALL_AGREE;
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/extensionability-overview-V14
爬取时间: 2025-04-27 22:11:53
来源: Huawei Developer
ExtensionAbility组件是基于特定场景（例如服务卡片、输入法等）提供的应用组件，以便满足更多的使用场景。
每一个具体场景对应一个ExtensionAbilityType，开发者只能使用（包括实现和访问）系统已定义的类型。各类型的ExtensionAbility组件均由相应的系统服务统一管理，例如InputMethodExtensionAbility组件由输入法管理服务统一管理。
当前系统已定义的ExtensionAbility类型如下表所示。
说明：
对于系统应用，不受下表约束，允许实现系统已定义的各类ExtensionAbility，也允许访问提供的各类对外服务。
| ExtensionAbility类型 | 功能描述 | 是否允许三 方应用实现 | 是否允许三 方应用访问 | 是否有独立 Extension沙箱 | 启动Extension 传递共享数据 是否严格模式访问 |
| --- | --- | --- | --- | --- | --- |
| FormExtensionAbility | FORM类型的ExtensionAbility组件，用于提供服务卡片的相关能力。 | 是 | 否 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |
| WorkSchedulerExtensionAbility | WORK_SCHEDULER类型的ExtensionAbility组件，用于提供延迟任务的相关能力。 | 是 | 不涉及 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |
| InputMethodExtensionAbility | INPUT_METHOD类型的ExtensionAbility组件，用于实现输入法应用的开发。 | 是 | 是 | 是 | 开发者在输入法管理中启用完整体验模式，即开启非严格模式，可读写共享数据；不启用完整体验模式，默认为严格模式，只能读取共享数据。 |
| BackupExtensionAbility | BACKUP类型的ExtensionAbility组件，用于提供备份及恢复应用数据的能力。 | 是 | 不涉及 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |
| DriverExtensionAbility | DRIVER类型的ExtensionAbility组件，用于提供驱动相关扩展框架。 | 是 | 是 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |
| EmbeddedUIExtensionAbility | EMBEDDED_UI类型的ExtensionAbility组件，用于提供跨进程界面嵌入的能力。 | 是 | 是 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |
| ShareExtensionAbility | SHARE类型的ExtensionAbility组件，用于提供分享模板服务扩展的能力。 | 是 | 是 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |
| FenceExtension | FENCE类型的ExtensionAbility组件，用于提供地理围栏扩展的能力。 | 是 | 否 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |
是否允许三
方应用实现
是否允许三
方应用访问
是否有独立
Extension沙箱
启动Extension
传递共享数据
是否严格模式访问
访问指定类型的ExtensionAbility组件
所有类型的ExtensionAbility组件均不能被应用直接启动，而是由相应的系统管理服务拉起，以确保其生命周期受系统管控，使用时拉起，使用完销毁。ExtensionAbility组件的调用方无需关心目标ExtensionAbility组件的生命周期。
以InputMethodExtensionAbility组件为例进行说明，如下图所示，调用方应用发起对InputMethodExtensionAbility组件的调用，此时将先调用输入法管理服务，由输入法管理服务拉起InputMethodExtensionAbility组件，返回给调用方，同时开始管理其生命周期。
图1使用InputMethodExtensionAbility组件
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170215.31623391114081941523241187146029:50001231000000:2800:5243CC6D9D574B09E31B7608CB67ACB3960012A888E053952DD069A6CF728A9E.png)
实现指定类型的ExtensionAbility组件
以实现卡片FormExtensionAbility为例进行说明。卡片框架提供了FormExtensionAbility基类，开发者通过派生此基类（如MyFormExtensionAbility），实现回调（如创建卡片的onCreate()回调、更新卡片的onUpdateForm()回调等）来实现具体卡片功能，具体见开发指导见服务卡片。
卡片FormExtensionAbility实现方不用关心使用方何时去请求添加、删除卡片，FormExtensionAbility实例及其所在的ExtensionAbility进程的整个生命周期，都是由卡片管理系统服务FormManagerService进行调度管理。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170215.86201798234903420655001413270159:50001231000000:2800:FDA55429B3F7DF6E4784DB2B35DFF854F9E88815ABDC480102AFA6AA08248CEC.png)
同一应用内的所有同类型的ExtensionAbility运行在同一独立进程（除ServiceExtensionAbility、DataShareExtensionAbility外），跟UIAbility组件不在同一进程，Stage模型的进程模型请参见进程模型。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiserviceextension-V14
爬取时间: 2025-04-27 22:12:07
来源: Huawei Developer
概述
UIServiceExtension是UIService类型的ExtensionAbility浮窗类组件，提供UI界面（例如预览界面）和后台服务能力。组件内部持有了一个UIServiceExtensionContext，通过UIServiceExtensionContext提供了丰富的接口供外部使用。
本文描述中称被启动的UIServiceExtension为服务端，称启动UIServiceExtension的组件为客户端。
应用可以通过启动和连接两种形式使用UIServiceExtension：
1.  三方应用可以使用UIServiceExtension，不支持实现UIServiceExtension（需要系统权限）。
2.  三方应用需要在前台获焦的情况下才能连接系统提供的UIServiceExtension。
3.  UIServiceExtension的生命周期与绑定的窗口强关联，窗口销毁后UIServiceExtension也一起销毁。
启动UIServiceExtension
应用通过startUIServiceExtensionAbility()方法启动一个UIServiceExtension。UIServiceExtension启动后，其生命周期独立于客户端，即使客户端已经销毁，该后台服务仍可继续运行，窗口创建失败或销毁后该服务会被销毁。
示例中的context的获取方式请参见获取UIAbility的上下文信息。
```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct Index {
build() {
Column() {
Row() {
// 创建启动按钮
Button('start ability')
.enabled(true)
.onClick(() => {
let context = getContext(this) as common.UIAbilityContext;
let startWant: Want = {
bundleName: 'com.acts.uiserviceextensionability',
abilityName: 'UiServiceExtAbility',
};
try {
// 启动UIServiceExtensionAbility
context.startUIServiceExtensionAbility(startWant).then(() => {
console.log('startUIServiceExtensionAbility success');
}).catch((error: BusinessError) => {
console.log('startUIServiceExtensionAbility error', JSON.stringify(error));
})
} catch (err) {
console.log('startUIServiceExtensionAbility failed', JSON.stringify(err));
}
})
}
}
}
}
```
客户端连接服务端
客户端通过connectUIServiceExtensionAbility()连接服务端，获取并保存UIServiceProxy对象。通过该proxy对象的sendData()方法发送数据给服务端。服务端通过UIServiceExtensionAbility类onData()（系统接口）方法接收客户端数据。
```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct Index {
comProxy: common.UIServiceProxy | null = null;
connectCallback : common.UIServiceExtensionConnectCallback = {
onData:(data: Record<string, Object>) => {
console.log("received data", JSON.stringify(data));
},
onDisconnect:() => {
console.log("onDisconnect ");
}
}
build() {
Column() {
Row() {
// 创建连接按钮
Button("connect ability")
.enabled(true)
.onClick(() => {
let context = getContext(this) as common.UIAbilityContext;
let startWant:Want = {
bundleName: 'com.acts.uiserviceextensionability',
abilityName: 'UiServiceExtAbility',
};
try {
// 连接UIServiceExtensionAbility
context.connectUIServiceExtensionAbility(startWant, this.connectCallback).then((proxy: common.UIServiceProxy) => {
this.comProxy = proxy;
let formData: Record<string, string> = {
'test': 'test'
};
try {
this.comProxy.sendData(formData);
} catch (err) {
console.log('sendData failed', JSON.stringify(err));
};
}).catch((err: BusinessError) => {
console.log("connectUIServiceExtensionAbility failed", JSON.stringify(err));
});
} catch(err) {
console.log("connectUIServiceExtensionAbility failed", JSON.stringify(err));
};
})
}
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/embeddeduiextensionability-V14
爬取时间: 2025-04-27 22:12:21
来源: Huawei Developer
概述
EmbeddedUIExtensionAbility是EMBEDDED_UI类型的ExtensionAbility组件，提供了跨进程界面嵌入的能力。
EmbeddedUIExtensionAbility需要和EmbeddedComponent一起配合使用，开发者可以在UIAbility的页面中通过EmbeddedComponent嵌入本应用的EmbeddedUIExtensionAbility提供的UI。EmbeddedUIExtensionAbility会在独立于UIAbility的进程中运行，完成其页面的布局和渲染。通常用于有进程隔离诉求的模块化开发场景。
EmbeddedUIExtensionAbility通过UIExtensionContext和UIExtensionContentSession提供相关能力。本文描述中称被启动的EmbeddedUIExtensionAbility为提供方，称启动EmbeddedUIExtensionAbility的EmbeddedComponent组件为使用方。
开发EmbeddedUIExtensionAbility提供方
生命周期
EmbeddedUIExtensionAbility提供了onCreate、onSessionCreate、onSessionDestroy、onForeground、onBackground和onDestroy生命周期回调，根据需要重写对应的回调方法。
开发步骤
开发者在实现一个EmbeddedUIExtensionAbility提供方时，需要在DevEco Studio工程中手动新建一个EmbeddedUIExtensionAbility，具体步骤如下。
1.  在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为EmbeddedUIExtAbility。
2.  在EmbeddedUIExtAbility目录，右键选择“New > File”，新建一个.ets文件并命名为EmbeddedUIExtAbility.ets。
3.  打开EmbeddedUIExtAbility.ets文件，导入EmbeddedUIExtensionAbility的依赖包，自定义类继承EmbeddedUIExtensionAbility并实现onCreate、onSessionCreate、onSessionDestroy、onForeground、onBackground和onDestroy生命周期回调。
```typescript
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
const TAG: string = '[ExampleEmbeddedAbility]'
export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {
onCreate() {
console.log(TAG, `onCreate`);
}
onForeground() {
console.log(TAG, `onForeground`);
}
onBackground() {
console.log(TAG, `onBackground`);
}
onDestroy() {
console.log(TAG, `onDestroy`);
}
onSessionCreate(want: Want, session: UIExtensionContentSession) {
console.log(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
let param: Record<string, UIExtensionContentSession> = {
'session': session
};
let storage: LocalStorage = new LocalStorage(param);
session.loadContent('pages/extension', storage);
}
onSessionDestroy(session: UIExtensionContentSession) {
console.log(TAG, `onSessionDestroy`);
}
}
```
4.  EmbeddedUIExtensionAbility的onSessionCreate中加载了入口页面文件pages/extension.ets内容如下：
```typescript
import { UIExtensionContentSession } from '@kit.AbilityKit';
let storage = LocalStorage.getShared()
@Entry(storage)
@Component
struct Extension {
@State message: string = 'EmbeddedUIExtensionAbility Index';
private session: UIExtensionContentSession | undefined = storage.get<UIExtensionContentSession>('session');
build() {
Column() {
Text(this.message)
.fontSize(20)
.fontWeight(FontWeight.Bold)
Button("terminateSelfWithResult").fontSize(20).onClick(() => {
this.session?.terminateSelfWithResult({
resultCode: 1,
want: {
bundleName: "com.example.embeddeddemo",
abilityName: "ExampleEmbeddedAbility",
}});
})
}.width('100%').height('100%')
}
}
```
5.  在工程Module对应的module.json5配置文件中注册EmbeddedUIExtensionAbility，type标签需要设置为“embeddedUI”，srcEntry标签表示当前EmbeddedUIExtensionAbility组件所对应的代码路径。
```json
{
"module": {
"extensionAbilities": [
{
"name": "EmbeddedUIExtAbility",
"icon": "$media:icon",
"description": "EmbeddedUIExtAbility",
"type": "embeddedUI",
"srcEntry": "./ets/EmbeddedUIExtAbility/EmbeddedUIExtAbility.ets"
},
]
}
}
```
开发EmbeddedUIExtensionAbility使用方
开发者可以在UIAbility的页面中通过EmbeddedComponent容器加载自己应用内的EmbeddedUIExtensionAbility。此外，EmbeddedUIExtensionAbility在want.parameters中新增了两个字段ohos.extension.processMode.hostSpecified和ohos.extension.processMode.hostInstance。
ohos.extension.processMode.hostSpecified和ohos.extension.processMode.hostInstance同时配置时，hostSpecified优先，会运行在指定的进程中。
如在首页文件：pages/Index.ets中添加如下内容：
```typescript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct Index {
@State message: string = 'Message: '
private want: Want = {
bundleName: "com.example.embeddeddemo",
abilityName: "EmbeddedUIExtAbility",
parameters: {
'ohos.extension.processMode.hostInstance': 'true'
}
}
build() {
Row() {
Column() {
Text(this.message).fontSize(30)
EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
.width('100%')
.height('90%')
.onTerminated((info: TerminationInfo) => {
this.message = 'Terminarion: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
})
.onError((error: BusinessError) => {
this.message = 'Error: code = ' + error.code;
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/abilitystage-V14
爬取时间: 2025-04-27 22:12:35
来源: Huawei Developer
AbilityStage是一个Module级别的组件容器，应用的HAP在首次加载时会创建一个AbilityStage实例，可以对该Module进行初始化等操作。
AbilityStage与Module一一对应，即一个Module拥有一个AbilityStage。
DevEco Studio默认工程中未自动生成AbilityStage，如需要使用AbilityStage的能力，可以手动新建一个AbilityStage文件，具体步骤如下。
1.  在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为myabilitystage。
2.  在myabilitystage目录，右键选择“New > ArkTS File”，新建一个文件并命名为MyAbilityStage.ets。
3.  打开MyAbilityStage.ets文件，导入AbilityStage的依赖包，自定义类继承AbilityStage并加上需要的生命周期回调，示例中增加了一个onCreate()生命周期回调。
```typescript
import { AbilityStage, Want } from '@kit.AbilityKit';
export default class MyAbilityStage extends AbilityStage {
onCreate(): void {
// 应用HAP首次加载时触发，可以在此执行该Module的初始化操作（例如资源预加载、线程创建等）。
}
onAcceptWant(want: Want): string {
// 仅specified模式下触发
return 'MyAbilityStage';
}
}
```
4.  在module.json5配置文件中，通过配置 srcEntry 参数来指定模块对应的代码路径，以作为HAP加载的入口。
```json
{
"module": {
"name": "entry",
"type": "entry",
"srcEntry": "./ets/myabilitystage/MyAbilityStage.ets",
// ...
}
}
```
AbilityStage拥有onCreate()生命周期回调和onAcceptWant()、onConfigurationUpdated()、onMemoryLevel()事件回调。
-  onCreate()生命周期回调：在开始加载对应Module的第一个UIAbility实例之前会先创建AbilityStage，并在AbilityStage创建完成之后执行其onCreate()生命周期回调。AbilityStage模块提供在Module加载的时候，通知开发者，可以在此进行该Module的初始化（如资源预加载，线程创建等）能力。
-  onAcceptWant()事件回调：UIAbility指定实例模式（specified）启动时候触发的事件回调，具体使用请参见UIAbility启动模式综述。
-  onConfigurationUpdated()事件回调：当系统全局配置发生变更时触发的事件，系统语言、深浅色等，配置项目前均定义在Configuration类中。
-  onMemoryLevel()事件回调：当系统调整内存时触发的事件。
应用被切换到后台时，系统会将在后台的应用保留在缓存中。即使应用处于缓存中，也会影响系统整体性能。当系统资源不足时，系统会通过多种方式从应用中回收内存，必要时会完全停止应用，从而释放内存用于执行关键任务。为了进一步保持系统内存的平衡，避免系统停止用户的应用进程，可以在AbilityStage中的onMemoryLevel()生命周期回调中订阅系统内存的变化情况，释放不必要的资源。
```typescript
import { AbilityStage, AbilityConstant } from '@kit.AbilityKit';
export default class MyAbilityStage extends AbilityStage {
onMemoryLevel(level: AbilityConstant.MemoryLevel): void {
// 根据系统可用内存的变化情况，释放不必要的内存
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/application-context-stage-V14
爬取时间: 2025-04-27 22:12:49
来源: Huawei Developer
概述
Context是应用中对象的上下文，其提供了应用的一些基础信息，例如resourceManager（资源管理）、applicationInfo（当前应用信息）、dir（应用文件路径）、area（文件分区）等，以及应用的一些基本方法，例如createBundleContext()、getApplicationContext()等。UIAbility组件和各种ExtensionAbility派生类组件都有各自不同的Context类。分别有基类Context、ApplicationContext、AbilityStageContext、UIAbilityContext、ExtensionContext、ServiceExtensionContext等Context。
-  各类Context的继承关系
-  各类Context的持有关系
-  各类Context的获取方式 获取UIAbilityContext。每个UIAbility中都包含了一个Context属性，提供操作应用组件、获取应用组件的配置信息等能力。 页面中获取UIAbility实例的上下文信息请参见获取UIAbility的上下文信息。 获取特定场景ExtensionContext。以ServiceExtensionContext为例，表示后台服务的上下文环境，继承自ExtensionContext，提供后台服务相关的接口能力。 获取AbilityStageContext（Module级别的Context）。和基类Context相比，额外提供HapModuleInfo、Configuration等信息。 获取ApplicationContext（应用级别的Context）。ApplicationContext在基类Context的基础上提供了订阅应用内应用组件的生命周期的变化、订阅系统内存变化、订阅应用内系统环境变化、设置应用语言、设置应用颜色模式、清除应用自身数据的同时撤销应用向用户申请的权限等能力，在UIAbility、ExtensionAbility、AbilityStage中均可以获取。
```typescript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
let uiAbilityContext = this.context;
//...
}
}
```
-  获取UIAbilityContext。每个UIAbility中都包含了一个Context属性，提供操作应用组件、获取应用组件的配置信息等能力。 页面中获取UIAbility实例的上下文信息请参见获取UIAbility的上下文信息。
```typescript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
let uiAbilityContext = this.context;
//...
}
}
```
-  获取特定场景ExtensionContext。以ServiceExtensionContext为例，表示后台服务的上下文环境，继承自ExtensionContext，提供后台服务相关的接口能力。
```typescript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';
export default class ServiceExtAbility extends ServiceExtensionAbility {
onCreate(want: Want) {
let serviceExtensionContext = this.context;
//...
}
}
```
-  获取AbilityStageContext（Module级别的Context）。和基类Context相比，额外提供HapModuleInfo、Configuration等信息。
```typescript
import { AbilityStage } from '@kit.AbilityKit';
export default class MyAbilityStage extends AbilityStage {
onCreate(): void {
let abilityStageContext = this.context;
//...
}
}
```
-  获取ApplicationContext（应用级别的Context）。ApplicationContext在基类Context的基础上提供了订阅应用内应用组件的生命周期的变化、订阅系统内存变化、订阅应用内系统环境变化、设置应用语言、设置应用颜色模式、清除应用自身数据的同时撤销应用向用户申请的权限等能力，在UIAbility、ExtensionAbility、AbilityStage中均可以获取。
```typescript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
let applicationContext = this.context.getApplicationContext();
//...
}
}
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170216.10970827891126706889346084735207:50001231000000:2800:6D8939D9282DFF6C01E3127A36AF107DE025C1C79ED9E53C2CD2BA2F784CE312.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170216.21065870475150092549461104815522:50001231000000:2800:3D94790F0D41C87D158A8293F9708BF702192A87C8F4673B171204A7A72D2F3C.png)
-  获取UIAbilityContext。每个UIAbility中都包含了一个Context属性，提供操作应用组件、获取应用组件的配置信息等能力。 页面中获取UIAbility实例的上下文信息请参见获取UIAbility的上下文信息。
```typescript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
let uiAbilityContext = this.context;
//...
}
}
```
-  获取特定场景ExtensionContext。以ServiceExtensionContext为例，表示后台服务的上下文环境，继承自ExtensionContext，提供后台服务相关的接口能力。
```typescript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';
export default class ServiceExtAbility extends ServiceExtensionAbility {
onCreate(want: Want) {
let serviceExtensionContext = this.context;
//...
}
}
```
-  获取AbilityStageContext（Module级别的Context）。和基类Context相比，额外提供HapModuleInfo、Configuration等信息。
```typescript
import { AbilityStage } from '@kit.AbilityKit';
export default class MyAbilityStage extends AbilityStage {
onCreate(): void {
let abilityStageContext = this.context;
//...
}
}
```
-  获取ApplicationContext（应用级别的Context）。ApplicationContext在基类Context的基础上提供了订阅应用内应用组件的生命周期的变化、订阅系统内存变化、订阅应用内系统环境变化、设置应用语言、设置应用颜色模式、清除应用自身数据的同时撤销应用向用户申请的权限等能力，在UIAbility、ExtensionAbility、AbilityStage中均可以获取。
```typescript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
let applicationContext = this.context.getApplicationContext();
//...
}
}
```
Context的典型使用场景
本章节通过如下典型场景来介绍Context的用法：
获取应用文件路径
基类Context提供了获取应用文件路径的能力，ApplicationContext、AbilityStageContext、UIAbilityContext和ExtensionContext均继承该能力。不同类型的Context获取的路径可能存在差异。
-  通过ApplicationContext可以获取应用级的文件路径。该路径用于存放应用全局信息，路径下的文件会跟随应用的卸载而删除。
-  通过AbilityStageContext、UIAbilityContext、ExtensionContext，可以获取Module级的文件路径。该路径用于存放Module相关信息，路径下的文件会跟随HAP/HSP的卸载而删除。HAP/HSP的卸载不会影响应用级路径下的文件，除非该应用的HAP/HSP已全部卸载。
应用文件路径属于应用沙箱路径，具体请参见应用沙箱目录。
表1不同级别Context获取的应用文件路径说明
| 属性 | 说明 | ApplicationContext获取的路径 | AbilityStageContext、UIAbilityContext、ExtensionContext获取的路径 |
| --- | --- | --- | --- |
| bundleCodeDir | 安装包目录。 | <路径前缀>/el1/bundle | <路径前缀>/el1/bundle |
| cacheDir | 缓存目录。 | <路径前缀>/<加密等级>/base/cache | <路径前缀>/<加密等级>/base/haps/<module-name>/cache |
| filesDir | 文件目录。 | <路径前缀>/<加密等级>/base/files | <路径前缀>/<加密等级>/base/haps/<module-name>/files |
| preferencesDir | preferences目录。 | <路径前缀>/<加密等级>/base/preferences | <路径前缀>/<加密等级>/base/haps/<module-name>/preferences |
| tempDir | 临时目录。 | <路径前缀>/<加密等级>/base/temp | <路径前缀>/<加密等级>/base/haps/<module-name>/temp |
| databaseDir | 数据库目录。 | <路径前缀>/<加密等级>/database | <路径前缀>/<加密等级>/database/<module-name> |
| distributedFilesDir | 分布式文件目录。 | <路径前缀>/el2/distributedFiles | <路径前缀>/el2/distributedFiles/ |
| resourceDir11+ | 资源目录。 说明： 需要开发者手动在\<module-name>\resource路径下创建resfile目录。 | 不涉及 | <路径前缀>/el1/bundle/<module-name>/resources/resfile |
| cloudFileDir12+ | 云文件目录。 | <路径前缀>/el2/cloud | <路径前缀>/el2/cloud/ |
资源目录。
说明：
需要开发者手动在\<module-name>\resource路径下创建resfile目录。
本节以使用ApplicationContext获取filesDir为例，介绍如何获取应用文件路径，并在对应文件路径下新建文件和读写文件。示例代码如下：
```typescript
import { common } from '@kit.AbilityKit';
import { buffer } from '@kit.ArkTS';
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[Page_Context]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
private context = getContext(this) as common.UIAbilityContext;
build() {
Row() {
Column() {
Text(this.message)
// ...
Button() {
Text('create file')
// ...
.onClick(() => {
let applicationContext = this.context.getApplicationContext();
// 获取应用文件路径
let filesDir = applicationContext.filesDir;
hilog.info(DOMAIN_NUMBER, TAG, `filePath: ${filesDir}`);
// 文件不存在时创建并打开文件，文件存在时打开文件
let file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
// 写入一段内容至文件
let writeLen = fileIo.writeSync(file.fd, "Try to write str.");
hilog.info(DOMAIN_NUMBER, TAG, `The length of str is: ${writeLen}`);
// 创建一个大小为1024字节的ArrayBuffer对象，用于存储从文件中读取的数据
let arrayBuffer = new ArrayBuffer(1024);
// 设置读取的偏移量和长度
let readOptions: ReadOptions = {
offset: 0,
length: arrayBuffer.byteLength
};
// 读取文件内容到ArrayBuffer对象中，并返回实际读取的字节数
let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
// 将ArrayBuffer对象转换为Buffer对象，并转换为字符串输出
let buf = buffer.from(arrayBuffer, 0, readLen);
hilog.info(DOMAIN_NUMBER, TAG, `the content of file: ${buf.toString()}`);
// 关闭文件
fileIo.closeSync(file);
})
}
// ...
}
// ...
}
// ...
}
}
```
获取和修改加密分区
应用文件加密是一种保护数据安全的方法，可以使得文件在未经授权访问的情况下得到保护。在不同的场景下，应用需要不同程度的文件保护。
在实际应用中，开发者需要根据不同场景的需求选择合适的加密分区，从而保护应用数据的安全。通过合理使用不同级别的加密分区，可以有效提高应用数据的安全性。关于不同分区的权限说明，详见ContextConstant的AreaMode。
要实现获取和设置当前加密分区，可以通过读写Context的area属性来实现。
```typescript
// EntryAbility.ets
import { UIAbility, contextConstant, AbilityConstant, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
// 存储普通信息前，切换到EL1设备级加密
this.context.area = contextConstant.AreaMode.EL1; // 切换area
// 存储普通信息
// 存储敏感信息前，切换到EL2用户级加密
this.context.area = contextConstant.AreaMode.EL2; // 切换area
// 存储敏感信息
// 存储敏感信息前，切换到EL3用户级加密
this.context.area = contextConstant.AreaMode.EL3; // 切换area
// 存储敏感信息
// 存储敏感信息前，切换到EL4用户级加密
this.context.area = contextConstant.AreaMode.EL4; // 切换area
// 存储敏感信息
// 存储敏感信息前，切换到EL5应用级加密
this.context.area = contextConstant.AreaMode.EL5; // 切换area
// 存储敏感信息
}
}
```
```typescript
// Index.ets
import { contextConstant, common } from '@kit.AbilityKit';
import { promptAction } from '@kit.ArkUI';
@Entry
@Component
struct Page_Context {
private context = getContext(this) as common.UIAbilityContext;
build() {
Column() {
//...
List({ initialIndex: 0 }) {
//...
ListItem() {
Row() {
//...
}
.onClick(() => {
// 存储普通信息前，切换到EL1设备级加密
if (this.context.area === contextConstant.AreaMode.EL2) { // 获取area
this.context.area = contextConstant.AreaMode.EL1; // 修改area
promptAction.showToast({
message: 'SwitchToEL1'
});
}
// 存储普通信息
})
}
//...
ListItem() {
Row() {
//...
}
.onClick(() => {
// 存储敏感信息前，切换到EL2用户级加密
if (this.context.area === contextConstant.AreaMode.EL1) { // 获取area
this.context.area = contextConstant.AreaMode.EL2; // 修改area
promptAction.showToast({
message: 'SwitchToEL2'
});
}
// 存储敏感信息
})
}
//...
}
//...
}
//...
}
}
```
获取本应用中其他Module的Context
调用createModuleContext(context: Context, moduleName: string)方法，获取本应用中其他Module的Context。获取到其他Module的Context之后，即可获取到相应Module的资源信息。
```typescript
import { common, application } from '@kit.AbilityKit';
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
let storageEventCall = new LocalStorage();
@Entry(storageEventCall)
@Component
struct Page_Context {
private context = getContext(this) as common.UIAbilityContext;
build() {
Column() {
//...
List({ initialIndex: 0 }) {
ListItem() {
Row() {
//...
}
.onClick(() => {
let moduleName2: string = 'entry';
application.createModuleContext(this.context, moduleName2)
.then((data: common.Context) => {
console.info(`CreateModuleContext success, data: ${JSON.stringify(data)}`);
if (data !== null) {
promptAction.showToast({
message: ('成功获取Context')
});
}
})
.catch((err: BusinessError) => {
console.error(`CreateModuleContext failed, err code:${err.code}, err msg: ${err.message}`);
});
})
}
//...
}
//...
}
//...
}
}
```
订阅进程内UIAbility生命周期变化
在应用内的DFX统计场景中，如需要统计对应页面停留时间和访问频率等信息，可以使用订阅进程内UIAbility生命周期变化功能。
通过ApplicationContext提供的能力，可以订阅进程内UIAbility生命周期变化。当进程内的UIAbility生命周期变化时，如创建、可见/不可见、获焦/失焦、销毁等，会触发相应的回调函数。每次注册回调函数时，都会返回一个监听生命周期的ID，此ID会自增+1。当超过监听上限数量2^63-1时，会返回-1。以UIAbilityContext中的使用为例进行说明。
```typescript
import { AbilityConstant, AbilityLifecycleCallback, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import  { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[LifecycleAbility]';
const DOMAIN_NUMBER: number = 0xFF00;
export default class LifecycleAbility extends UIAbility {
// 定义生命周期ID
lifecycleId: number = -1;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 定义生命周期回调对象
let abilityLifecycleCallback: AbilityLifecycleCallback = {
// 当UIAbility创建时被调用
onAbilityCreate(uiAbility) {
hilog.info(DOMAIN_NUMBER, TAG, `onAbilityCreate uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
},
// 当窗口创建时被调用
onWindowStageCreate(uiAbility, windowStage: window.WindowStage) {
hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageCreate uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageCreate windowStage: ${JSON.stringify(windowStage)}`);
},
// 当窗口处于活动状态时被调用
onWindowStageActive(uiAbility, windowStage: window.WindowStage) {
hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageActive uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageActive windowStage: ${JSON.stringify(windowStage)}`);
},
// 当窗口处于非活动状态时被调用
onWindowStageInactive(uiAbility, windowStage: window.WindowStage) {
hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageInactive uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageInactive windowStage: ${JSON.stringify(windowStage)}`);
},
// 当窗口被销毁时被调用
onWindowStageDestroy(uiAbility, windowStage: window.WindowStage) {
hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageDestroy uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageDestroy windowStage: ${JSON.stringify(windowStage)}`);
},
// 当UIAbility被销毁时被调用
onAbilityDestroy(uiAbility) {
hilog.info(DOMAIN_NUMBER, TAG, `onAbilityDestroy uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
},
// 当UIAbility从后台转到前台时触发回调
onAbilityForeground(uiAbility) {
hilog.info(DOMAIN_NUMBER, TAG, `onAbilityForeground uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
},
// 当UIAbility从前台转到后台时触发回调
onAbilityBackground(uiAbility) {
hilog.info(DOMAIN_NUMBER, TAG, `onAbilityBackground uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
},
// 当UIAbility迁移时被调用
onAbilityContinue(uiAbility) {
hilog.info(DOMAIN_NUMBER, TAG, `onAbilityContinue uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
}
};
// 获取应用上下文
let applicationContext = this.context.getApplicationContext();
try {
// 注册应用内生命周期回调
this.lifecycleId = applicationContext.on('abilityLifecycle', abilityLifecycleCallback);
} catch (err) {
let code = (err as BusinessError).code;
let message = (err as BusinessError).message;
hilog.error(DOMAIN_NUMBER, TAG, `Failed to register applicationContext. Code is ${code}, message is ${message}`);
}
hilog.info(DOMAIN_NUMBER, TAG, `register callback number: ${this.lifecycleId}`);
}
//...
onDestroy(): void {
// 获取应用上下文
let applicationContext = this.context.getApplicationContext();
try {
// 取消应用内生命周期回调
applicationContext.off('abilityLifecycle', this.lifecycleId);
} catch (err) {
let code = (err as BusinessError).code;
let message = (err as BusinessError).message;
hilog.error(DOMAIN_NUMBER, TAG, `Failed to unregister applicationContext. Code is ${code}, message is ${message}`);
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/want-V14
爬取时间: 2025-04-27 22:13:02
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/want-overview-V14
爬取时间: 2025-04-27 22:13:16
来源: Huawei Developer
Want的定义与用途
Want是一种对象，用于在应用组件之间传递信息。
其中，一种常见的使用场景是作为startAbility()方法的参数。例如，当UIAbilityA需要启动UIAbilityB并向UIAbilityB传递一些数据时，可以使用Want作为一个载体，将数据传递给UIAbilityB。
图1Want用法示意
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170216.81618824642132227642834230393552:50001231000000:2800:533483B449D5681025322E0ECEECA25AF3F42ABDBC769A19281B6D8AC7B188B5.png)
Want的类型
-  显式Want：在启动目标应用组件时，调用方传入的want参数中指定了abilityName和bundleName，称为显式Want。 显式Want通常用于应用内组件启动，通过在Want对象内指定本应用Bundle名称信息（bundleName）和abilityName来启动应用内目标组件。当有明确处理请求的对象时，显式Want是一种简单有效的启动目标应用组件的方式。 从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用，推荐通过指定应用链接的方式来实现。
```typescript
import { Want } from '@kit.AbilityKit';
let wantInfo: Want = {
deviceId: '', // deviceId为空表示本设备
bundleName: 'com.example.myapplication',
abilityName: 'FuncAbility',
}
```
-  隐式Want：在启动目标应用组件时，调用方传入的want参数中未指定abilityName，称为隐式Want。 当需要处理的对象不明确时，可以使用隐式Want，在当前应用中使用其他应用提供的某个能力，而不关心提供该能力的具体应用。隐式Want使用skills标签来定义需要使用的能力，并由系统匹配声明支持该请求的所有应用来处理请求。例如，需要打开一个链接的请求，系统将匹配所有声明支持该请求的应用，然后让用户选择使用哪个应用打开链接。 根据系统中待匹配应用组件的匹配情况不同，使用隐式Want启动应用组件时会出现以下三种情况。 对于启动ServiceExtensionAbility的场景。
```typescript
import { Want } from '@kit.AbilityKit';
let wantInfo: Want = {
// uncomment line below if wish to implicitly query only in the specific bundle.
// bundleName: 'com.example.myapplication',
action: 'ohos.want.action.search',
// entities can be omitted
entities: [ 'entity.system.browsable' ],
uri: 'https://www.test.com:8080/query/student',
type: 'text/plain',
};
```
-  根据系统中待匹配应用组件的匹配情况不同，使用隐式Want启动应用组件时会出现以下三种情况。
-  对于启动ServiceExtensionAbility的场景。
-  根据系统中待匹配应用组件的匹配情况不同，使用隐式Want启动应用组件时会出现以下三种情况。
-  对于启动ServiceExtensionAbility的场景。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/explicit-implicit-want-mappings-V14
爬取时间: 2025-04-27 22:13:29
来源: Huawei Developer
在启动目标应用组件时，会通过显式Want或者隐式Want进行目标应用组件的匹配，这里说的匹配规则就是调用方传入的want参数中设置的参数如何与目标应用组件声明的配置文件进行匹配。
显式Want匹配原理
显式Want匹配原理如下表所示。
| 名称 | 类型 | 匹配项 | 必选 | 规则 |
| --- | --- | --- | --- | --- |
| deviceId | string | 是 | 否 | 留空将仅匹配本设备内的应用组件。 |
| bundleName | string | 是 | 是 | 如果指定abilityName，而不指定bundleName，则匹配失败。 |
| moduleName | string | 是 | 否 | 留空时当同一个应用内存在多个模块且模块间存在重名应用组件，将默认匹配第一个。 |
| abilityName | string | 是 | 是 | 该字段必须设置表示显式匹配。 |
| uri | string | 否 | 否 | 系统匹配时将忽略该参数，但仍可作为参数传递给目标应用组件。 |
| type | string | 否 | 否 | 系统匹配时将忽略该参数，但仍可作为参数传递给目标应用组件。 |
| action | string | 否 | 否 | 系统匹配时将忽略该参数，但仍可作为参数传递给目标应用组件。 |
| entities | Array<string> | 否 | 否 | 系统匹配时将忽略该参数，但仍可作为参数传递给目标应用组件。 |
| flags | number | 否 | 否 | 不参与匹配，直接传递给系统处理，一般用来设置运行态信息，例如URI数据授权等。 |
| parameters | {[key: string]: Object} | 否 | 否 | 不参与匹配，应用自定义数据将直接传递给目标应用组件。 |
隐式Want匹配原理
隐式Want匹配原理如下表所示。
| 名称 | 类型 | 匹配项 | 必选 | 规则 |
| --- | --- | --- | --- | --- |
| deviceId | string | 是 | 否 | 跨设备目前不支持隐式调用。 |
| abilityName | string | 否 | 否 | 该字段必须留空表示隐式匹配。 |
| bundleName | string | 是 | 否 | 匹配对应应用包内的目标应用组件。 |
| moduleName | string | 是 | 否 | 匹配对应Module内的目标应用组件。 |
| uri | string | 是 | 否 | 参见want参数的uri和type匹配规则。 |
| type | string | 是 | 否 | 参见want参数的uri和type匹配规则。 |
| action | string | 是 | 否 | 参见want参数的action匹配规则。 |
| entities | Array<string> | 是 | 否 | 参见want参数的entities匹配规则。 |
| flags | number | 否 | 否 | 不参与匹配，直接传递给系统处理，一般用来设置运行态信息，例如URI数据授权等。 |
| parameters | {[key: string]: Object} | 是 | 否 | 应用自定义数据将直接传递给目标应用组件。当前支持使用key为linkFeature的参数进行匹配，当linkFeature字段取值不为空时，优先进行linkFeature匹配。 |
从隐式Want的定义，可得知：
-  调用方传入的want参数，表明调用方需要执行的操作，并提供相关数据以及其他应用类型限制。
-  待匹配应用组件的skills配置，声明其具备的能力（module.json5配置文件中的skills标签参数）。
系统将调用方传入的want参数（包含action、entities、uri、type和parameters属性）与已安装待匹配应用组件的skills配置（包含actions、entities、uris和type属性）进行匹配。当want参数五个属性匹配均未配置，隐式匹配失败。
want参数的action匹配规则
将调用方传入的want参数的action与待匹配应用组件的skills配置中的actions进行匹配。
-  调用方传入的want参数的action为空，待匹配Ability的skills配置中的actions为空，则action匹配失败。
-  调用方传入的want参数的action不为空，待匹配应用组件的skills配置中的actions为空，则action匹配失败。
-  调用方传入的want参数的action为空，待匹配应用组件的skills配置中的actions不为空，则action匹配成功。
-  调用方传入的want参数的action不为空，待匹配应用组件的skills配置中的actions不为空且包含调用方传入的want参数的action，则action匹配成功。
-  调用方传入的want参数的action不为空，待匹配应用组件的skills配置中的actions不为空且不包含调用方传入的want参数的action，则action匹配失败。 图1want参数的action匹配规则
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170216.17405030989714700233684374328956:50001231000000:2800:C8C107000C929CAF8FFE384E2B0841AE4A5F8F53BAFB2076A54FBB2A79908032.png)
want参数的entities匹配规则
将调用方传入的want参数的entities与待匹配应用组件的skills配置中的entities进行匹配。
-  调用方传入的want参数的entities为空，待匹配应用组件的skills配置中的entities不为空，则entities匹配成功。
-  调用方传入的want参数的entities为空，待匹配应用组件的skills配置中的entities为空，则entities匹配成功。
-  调用方传入的want参数的entities不为空，待匹配应用组件的skills配置中的entities为空，则entities匹配失败。
-  调用方传入的want参数的entities不为空，待匹配应用组件的skills配置中的entities不为空且包含调用方传入的want参数的entities，则entities匹配成功。
-  调用方传入的want参数的entities不为空，待匹配应用组件的skills配置中的entities不为空且不完全包含调用方传入的want参数的entities，则entities匹配失败。 图2want参数的entities匹配规则
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170216.60612162729276625855678142832158:50001231000000:2800:F28142F90EC5C6DDA2A6A4C84E17655400589CDDABE806A3F0071E30C51493F3.png)
want参数的uri和type匹配规则
调用方传入的want参数中设置uri和type参数发起启动应用组件的请求，系统会遍历当前系统已安装的组件列表，并逐个匹配待匹配应用组件的skills配置中的uris数组，如果待匹配应用组件的skills配置中的uris数组中只要有一个可以匹配调用方传入的want参数中设置的uri和type即为匹配成功。
实际应用中，uri和type共存在四种情况，下面将讲解四种情况的具体匹配规则：
-  调用方传入的want参数的uri和type都为空。
-  调用方传入的want参数的uri不为空，type为空。
-  调用方传入的want参数的uri为空，type不为空。
-  调用方传入的want参数的uri和type都不为空，如下图所示。
最左uri匹配：当配置文件待匹配应用组件的skills配置中的uris数组中只配置scheme；或者只配置scheme和host；或者只配置scheme、host和port时。传入want参数的uri的最左边依次需要和scheme，或者scheme和host，或者scheme、host和port都匹配，才满足最左uri匹配。
图3want参数中uri和type皆不为空时的匹配规则
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170216.00839159530277363547598366798888:50001231000000:2800:D6883DF58818621AA3DCD3A8818EA0A2BA764F0B4486AC0DC3793FADCDD06444.png)
为了简化描述：
图4want参数中uri和type的具体匹配规则
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170217.72735696928193780274497763969696:50001231000000:2800:E0E4E7B2AF1A8C465B1C06F9360316F014A56AAF73877430AA6576099BEB4CC5.png)
uri匹配规则
具体的匹配规则如下：
-  如果s_uri的scheme为空，当w_uri为空时匹配成功，否则匹配失败。
-  如果s_uri的host为空，当w_uri和s_uri的scheme相同时匹配成功，否则匹配失败。
-  如果s_uri的port为空，当w_uri和s_uri中的scheme和host相同时匹配成功，否则匹配失败。
-  如果s_uri的path、pathStartWith和pathRegex都为空，当w_uri和s_uri中的scheme，host和port相同时匹配成功，否则匹配失败。
-  如果s_uri的path不为空，当w_uri和s_uri全路径表达式相同时匹配成功，否则继续进行pathStartWith的匹配。
-  如果s_uri的pathStartWith不为空，当w_uri包含s_uri前缀表达式时匹配成功，否则继续进行pathRegex的匹配。
-  如果s_uri的pathRegex不为空，当w_uri满足s_uri正则表达式时匹配成功，否则匹配失败。
待匹配应用组件的skills配置的uris中scheme、host、port、path、pathStartWith和pathRegex属性拼接，如果依次声明了path、pathStartWith和pathRegex属性时，uris将分别拼接为如下四种表达式：
系统应用预留uri的scheme统一以ohos开头，例如ohosclock://。三方应用组件配置的uri不能与系统应用重复，否则会导致无法通过该uri拉起三方应用组件。
图5want参数中uri的匹配规则示例
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170217.62097257469911575704711213903425:50001231000000:2800:AB757AFE74621B2A3291E40832F9604AD9ED3787EFFC3C6C6E0D1DB223BF1ED0.png)
type匹配规则
本章节所述的type匹配规则的适用性需建立在want参数内type不为空的基础上。当want参数内type为空时请参见want参数的uri和type匹配规则。
具体的匹配规则如下：
-  如果s_type为空，则匹配失败。
-  如果s_type或者w_type为通配符*/*，则匹配成功。
-  如果s_type最后一个字符为通配符*，如prefixType/*，则当w_type包含prefixType/时匹配成功，否则匹配失败。
-  如果w_type最后一个字符为通配符*，如prefixType/*，则当s_type包含prefixType/时匹配成功，否则匹配失败。
linkFeature匹配规则
本章节所述的linkFeature匹配规则适用于want参数中的parameters包含linkFeature键，且对应取值不为空的场景。
将调用方传入的want参数的parameters与待匹配应用组件的skills配置中的uris进行匹配。为了简化描述, 称调用方传入的want参数中的linkFeature参数为w_linkFeature, 具体的匹配规则如下：
图6want参数中linkFeature具体匹配规则
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170217.64880292431144822299305792985330:50001231000000:2800:E1D3E184DB363F29E41467E0BE4BCA4E1DC731BE52941C7E80EA1CEDEA8EAC94.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170217.89972224472057995939318725640164:50001231000000:2800:DE4A1B458640628B74EA25B5C79B0CF0340EF52AA156A757DA5E1D37C00D3548.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ability-startup-with-explicit-want-V14
爬取时间: 2025-04-27 22:13:43
来源: Huawei Developer
在应用使用场景中，当用户在应用内点击某个按钮时，经常需要拉起指定UIAbility组件来完成某些特定任务。在启动UIAbility时，指定了abilityName和bundleName参数，可以使用显式Want方式启动UIAbility。
针对应用的特定任务，用户需要通过点击应用内的按钮来启动指定的UIAbility组件。在启动UIAbility时，需要提供abilityName和bundleName参数，并使用显式Want方式来启动。关于如何使用显式Want方式启动应用内的UIAbility，请参见启动应用内的UIAbility。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/actions-entities-V14
爬取时间: 2025-04-27 22:13:57
来源: Huawei Developer
由于action/entity被泛化使用，系统对应用申明action/entity的行为缺少管控，恶意应用虚假申明，抢占流量，导致跳转后功能不可用。后续系统会逐步废弃非必要action/entity，建议通过指定类型的方式拉起应用。
action：表示调用方要执行的通用操作（如查看、分享、应用详情）。在隐式Want中，您可定义该字段，配合uri或parameters来表示对数据要执行的操作。如打开，查看该uri数据。例如，当uri为一段网址，action为ACTION_VIEW_DATA则表示匹配可访问该网址的应用组件。在Want内声明action字段表示希望被调用方应用支持声明的操作。在被调用方应用配置文件的skills字段内声明actions表示该应用支持声明操作。常见的action如下，具体的action取值请见action常数说明。
常见action
-  ACTION_HOME：启动应用入口组件的动作，需要和ENTITY_HOME配合使用；系统桌面应用图标就是显式的入口组件，点击也是启动入口组件；入口组件可以配置多个。
-  ACTION_CHOOSE：选择本地资源数据，例如联系人、相册等；系统一般对不同类型的数据有对应的Picker应用，例如联系人和图库。
-  ACTION_VIEW_DATA：查看数据，当使用网址uri时，则表示显示该网址对应的内容。具体操作流程请见通过startAbility拉起文件处理类应用。
-  ACTION_VIEW_MULTIPLE_DATA：发送多个数据记录的操作。
entities：表示目标应用组件的类别信息（如浏览器、视频播放器），在隐式Want中是对action的补充。在隐式Want中，开发者可定义该字段，来过滤匹配应用的类别，例如必须是浏览器。在Want内声明entities字段表示希望被调用方应用属于声明的类别。在被调用方应用配置文件的skills字段内声明entites表示该应用支持的类别。常见的entities如下，具体的entity取值及说明请见entity常数说明。
常见entities
-  ENTITY_DEFAULT：默认类别无实际意义。
-  ENTITY_HOME：主屏幕有图标点击入口类别。
-  ENTITY_BROWSABLE：指示浏览器类别。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/component-startup-rules-V14
爬取时间: 2025-04-27 22:14:51
来源: Huawei Developer
启动组件是指一切启动或连接应用组件的行为：
-  启动UIAbility、ServiceExtensionAbility、DataShareExtensionAbility，如使用startAbility()、startServiceExtensionAbility()、startAbilityByCall()、openLink()等相关接口。
-  连接ServiceExtensionAbility、DataShareExtensionAbility，如使用connectServiceExtensionAbility()、createDataShareHelper()等相关接口。
组件启动总体规则
为了保证用户具有更好的使用体验，对以下几种易影响用户体验与系统安全的行为做了限制：
-  后台应用任意弹框，如各种广告弹窗，影响用户使用。
-  后台应用相互唤醒，不合理的占用系统资源，导致系统功耗增加或系统卡顿。
-  前台应用任意跳转至其他应用，如随意跳转到其他应用的支付页面，存在安全风险。
鉴于此，制订了一套组件启动规则，主要包括：
-  跨应用启动组件，需校验目标组件是否可以被其他应用调用。 若目标组件exported字段配置为true，表示可以被其他应用调用；若目标组件exported字段配置为false，表示不可以被其他应用调用，还需进一步校验ohos.permission.START_INVISIBLE_ABILITY权限（该权限仅系统应用可申请）。组件exported字段说明可参考abilities标签。
-  位于后台的UIAbility应用，启动组件需校验BACKGROUND权限ohos.permission.START_ABILITIES_FROM_BACKGROUND（该权限仅系统应用可申请）。 说明： 前后台应用的判断依据：若应用进程获焦或所属的UIAbility组件位于前台则判定为前台应用，否则为后台应用。
-  跨设备使用startAbilityByCall接口，需校验分布式权限ohos.permission.DISTRIBUTED_DATASYNC。
上述组件启动规则自API 9版本开始生效。开发者需熟知组件启动规则，避免业务功能异常。启动组件的具体校验流程见下文。
同设备组件启动规则
设备内启动组件，不同场景下的规则不同，可分为如下三种场景：
-  启动UIAbility。
-  启动ServiceExtensionAbility、DataShareExtensionAbility。
-  通过startAbilityByCall接口启动UIAbility。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170217.45245351331804525550798413322593:50001231000000:2800:78134EAB8F9CA27390CDD95BD67C4CC169564922BF4CB3D7617110EE2D0A2BFB.png)
分布式跨设备组件启动规则
跨设备启动组件，不同场景下的规则不同，可分为如下三种场景：
-  启动UIAbility。
-  启动ServiceExtensionAbility、DataShareExtensionAbility。
-  通过startAbilityByCall接口启动UIAbility。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170217.13634329795767369419408888423887:50001231000000:2800:4369ED5C249F14ED7D7FE115B2043CEB88FECAD2A524743F23CE8DA6A3CEF5FE.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-startup-V14
爬取时间: 2025-04-27 22:15:05
来源: Huawei Developer
概述
应用启动时通常需要执行一系列初始化启动任务，如果将启动任务都放在应用主模块（即entry类型的Module）的UIAbility组件的onCreate生命周期中，那么只能在主线程中依次执行，不但影响应用的启动速度，而且当启动任务过多时，任务之间复杂的依赖关系还会使得代码难以维护。
AppStartup提供了一种简单高效的应用启动方式，可以支持任务的异步启动，加快应用启动速度。同时，通过在一个配置文件中统一设置多个启动任务的执行顺序以及依赖关系，让执行启动任务的代码变得更加简洁清晰、容易维护。
启动框架支持以自动模式或手动模式执行启动任务，默认采用自动模式。在构造AbilityStage组件容器过程中开始加载开发者配置的启动任务，并执行自动模式的启动任务。开发者也可以在UIAbility创建完后调用startupManager.run方法，执行手动模式的启动任务。
图1启动框架执行时机
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094244.35235638349263925455302949748379:50001231000000:2800:89BA5F5B07A62B3479F6D5D7869BA7FAD14E8924F59E68C111DC28212395BC40.png)
约束限制
-  启动框架只支持在entry类型的Module下的UIAbility中使用。
-  启动任务之间不允许存在循环依赖。
开发流程
开发步骤
定义启动框架配置文件
1.  在应用主模块（即entry类型的Module）的“resources/base/profile”路径下，新建启动框架配置文件。文件名可以自定义，本文以"startup_config.json"为例。
2.  在启动框架配置文件startup_config.json中，依次添加各个启动任务的配置信息。 假设当前应用启动框架共包含6个启动任务，任务之间的依赖关系如下图所示。为了便于并发执行启动任务，单个启动任务文件包含的启动任务应尽量单一，本例中每个启动任务对应一个启动任务文件。 图2启动任务依赖关系图 在“ets/startup”路径下，依次创建6个启动任务文件、以及一个公共的启动参数配置文件。文件名称必须确保唯一性。 在启动框架配置文件startup_config.json中，添加所有启动任务以及启动参数配置文件的相关信息。 startup_config.json文件示例如下： 表1startup_config.json配置文件标签说明 表2startupTasks标签说明 是否排除自动模式，详细介绍可以查看修改启动模式。 - true：手动模式。 - false：自动模式。 执行初始化所在的线程。 - mainThread：在主线程中执行。 - taskPool：在异步线程中执行。 主线程是否需要等待启动框架执行。当runOnThread取值为taskPool时，该字段生效。 - true：主线程等待启动框架执行完之后，才会加载应用首页。 - false：主线程不等待启动任务执行。 在module.json5配置文件的appStartup标签中，添加启动框架配置文件的索引。 module.json5示例代码如下。
```json
{
"startupTasks": [
{
"name": "StartupTask_001",
"srcEntry": "./ets/startup/StartupTask_001.ets",
"dependencies": [
"StartupTask_002",
"StartupTask_003"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_002",
"srcEntry": "./ets/startup/StartupTask_002.ets",
"dependencies": [
"StartupTask_003",
"StartupTask_004"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_003",
"srcEntry": "./ets/startup/StartupTask_003.ets",
"dependencies": [
"StartupTask_004"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_004",
"srcEntry": "./ets/startup/StartupTask_004.ets",
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_005",
"srcEntry": "./ets/startup/StartupTask_005.ets",
"dependencies": [
"StartupTask_006"
],
"runOnThread": "mainThread",
"waitOnMainThread": true,
"excludeFromAutoStart": true
},
{
"name": "StartupTask_006",
"srcEntry": "./ets/startup/StartupTask_006.ets",
"runOnThread": "mainThread",
"waitOnMainThread": false,
"excludeFromAutoStart": true
}
],
"configEntry": "./ets/startup/StartupConfig.ets"
}
```
3.  在“ets/startup”路径下，依次创建6个启动任务文件、以及一个公共的启动参数配置文件。文件名称必须确保唯一性。
4.  在启动框架配置文件startup_config.json中，添加所有启动任务以及启动参数配置文件的相关信息。 startup_config.json文件示例如下： 表1startup_config.json配置文件标签说明 表2startupTasks标签说明 是否排除自动模式，详细介绍可以查看修改启动模式。 - true：手动模式。 - false：自动模式。 执行初始化所在的线程。 - mainThread：在主线程中执行。 - taskPool：在异步线程中执行。 主线程是否需要等待启动框架执行。当runOnThread取值为taskPool时，该字段生效。 - true：主线程等待启动框架执行完之后，才会加载应用首页。 - false：主线程不等待启动任务执行。
```json
{
"startupTasks": [
{
"name": "StartupTask_001",
"srcEntry": "./ets/startup/StartupTask_001.ets",
"dependencies": [
"StartupTask_002",
"StartupTask_003"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_002",
"srcEntry": "./ets/startup/StartupTask_002.ets",
"dependencies": [
"StartupTask_003",
"StartupTask_004"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_003",
"srcEntry": "./ets/startup/StartupTask_003.ets",
"dependencies": [
"StartupTask_004"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_004",
"srcEntry": "./ets/startup/StartupTask_004.ets",
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_005",
"srcEntry": "./ets/startup/StartupTask_005.ets",
"dependencies": [
"StartupTask_006"
],
"runOnThread": "mainThread",
"waitOnMainThread": true,
"excludeFromAutoStart": true
},
{
"name": "StartupTask_006",
"srcEntry": "./ets/startup/StartupTask_006.ets",
"runOnThread": "mainThread",
"waitOnMainThread": false,
"excludeFromAutoStart": true
}
],
"configEntry": "./ets/startup/StartupConfig.ets"
}
```
5.  在module.json5配置文件的appStartup标签中，添加启动框架配置文件的索引。 module.json5示例代码如下。
```json
{
"module": {
"name": "entry",
"type": "entry",
// ...
"appStartup": "$profile:startup_config", // 启动框架的配置文件
// ...
}
}
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094244.32829883130358404208962974555140:50001231000000:2800:0DAF447C0F2E8463F6DB1CC6C820BB1FB3D3B80FE45F90C58858239C0AB0F823.png)
1.  在“ets/startup”路径下，依次创建6个启动任务文件、以及一个公共的启动参数配置文件。文件名称必须确保唯一性。
2.  在启动框架配置文件startup_config.json中，添加所有启动任务以及启动参数配置文件的相关信息。 startup_config.json文件示例如下： 表1startup_config.json配置文件标签说明 表2startupTasks标签说明 是否排除自动模式，详细介绍可以查看修改启动模式。 - true：手动模式。 - false：自动模式。 执行初始化所在的线程。 - mainThread：在主线程中执行。 - taskPool：在异步线程中执行。 主线程是否需要等待启动框架执行。当runOnThread取值为taskPool时，该字段生效。 - true：主线程等待启动框架执行完之后，才会加载应用首页。 - false：主线程不等待启动任务执行。
```json
{
"startupTasks": [
{
"name": "StartupTask_001",
"srcEntry": "./ets/startup/StartupTask_001.ets",
"dependencies": [
"StartupTask_002",
"StartupTask_003"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_002",
"srcEntry": "./ets/startup/StartupTask_002.ets",
"dependencies": [
"StartupTask_003",
"StartupTask_004"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_003",
"srcEntry": "./ets/startup/StartupTask_003.ets",
"dependencies": [
"StartupTask_004"
],
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_004",
"srcEntry": "./ets/startup/StartupTask_004.ets",
"runOnThread": "taskPool",
"waitOnMainThread": false
},
{
"name": "StartupTask_005",
"srcEntry": "./ets/startup/StartupTask_005.ets",
"dependencies": [
"StartupTask_006"
],
"runOnThread": "mainThread",
"waitOnMainThread": true,
"excludeFromAutoStart": true
},
{
"name": "StartupTask_006",
"srcEntry": "./ets/startup/StartupTask_006.ets",
"runOnThread": "mainThread",
"waitOnMainThread": false,
"excludeFromAutoStart": true
}
],
"configEntry": "./ets/startup/StartupConfig.ets"
}
```
3.  在module.json5配置文件的appStartup标签中，添加启动框架配置文件的索引。 module.json5示例代码如下。
```json
{
"module": {
"name": "entry",
"type": "entry",
// ...
"appStartup": "$profile:startup_config", // 启动框架的配置文件
// ...
}
}
```
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| startupTasks | 启动任务配置信息，标签说明详见下表。 | 对象数组 | 该标签不可缺省。 |
| configEntry | 启动参数配置文件所在路径。 | 字符串 | 该标签不可缺省。 |
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 启动任务名称，可自定义，推荐与类名保持一致。 | 字符串 | 该标签不可缺省。 |
| srcEntry | 启动任务对应的文件路径。 | 字符串 | 该标签不可缺省。 |
| dependencies | 启动任务依赖的其他启动任务的类名数组。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| excludeFromAutoStart | 是否排除自动模式，详细介绍可以查看修改启动模式。 - true：手动模式。 - false：自动模式。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| runOnThread | 执行初始化所在的线程。 - mainThread：在主线程中执行。 - taskPool：在异步线程中执行。 | 字符串 | 该标签可缺省，缺省值为mainThread。 |
| waitOnMainThread | 主线程是否需要等待启动框架执行。当runOnThread取值为taskPool时，该字段生效。 - true：主线程等待启动框架执行完之后，才会加载应用首页。 - false：主线程不等待启动任务执行。 | 布尔值 | 该标签可缺省，缺省值为true。 |
设置启动参数
在启动参数配置文件（本文为“ets/startup/StartupConfig.ets”文件）中，使用StartupConfigEntry接口实现启动框架公共参数的配置，包括超时时间和启动任务的监听器等参数，其中需要用到如下接口：
```typescript
import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
export default class MyStartupConfigEntry extends StartupConfigEntry {
onConfig() {
hilog.info(0x0000, 'testTag', `onConfig`);
let onCompletedCallback = (error: BusinessError<void>) => {
hilog.info(0x0000, 'testTag', `onCompletedCallback`);
if (error) {
hilog.info(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code, error.message);
} else {
hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
}
};
let startupListener: StartupListener = {
'onCompleted': onCompletedCallback
};
let config: StartupConfig = {
'timeoutMs': 10000,
'startupListener': startupListener
};
return config;
}
}
```
为每个待初始化组件添加启动任务
上述操作中已完成启动框架配置文件、启动参数的配置，还需要在每个组件对应的启动任务文件中，通过实现StartupTask来添加启动任务。其中，需要用到下面的两个方法：
下面以startup_config.json中的StartupTask_001.ets文件为例，示例代码如下。开发者需要分别为每个待初始化组件添加启动任务。
由于StartupTask采用了Sendable协议，在继承该接口时，必须添加Sendable注解。
```typescript
import { StartupTask, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
@Sendable
export default class StartupTask_001 extends StartupTask {
constructor() {
super();
}
async init(context: common.AbilityStageContext) {
hilog.info(0x0000, 'testTag', 'StartupTask_001 init.');
return 'StartupTask_001';
}
onDependencyCompleted(dependence: string, result: Object): void {
hilog.info(0x0000, 'testTag', 'StartupTask_001 onDependencyCompleted, dependence: %{public}s, result: %{public}s',
dependence, JSON.stringify(result));
}
}
```
（可选）修改启动模式
AppStartup分别提供了自动和手动两种方式来执行启动任务，默认采用自动模式。开发者可以根据需要修改为手动模式。
下面以UIAbility的onCreate生命周期中为例，介绍如何采用手动模式来启动任务，示例代码如下。
```typescript
import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
let startParams = ["StartupTask_005", "StartupTask_006"];
try {
startupManager.run(startParams).then(() => {
console.log('StartupTest startupManager run then, startParams = ');
}).catch((error: BusinessError) => {
console.info('StartupTest promise catch error, error = ' + JSON.stringify(error));
console.info('StartupTest promise catch error, startParams = '
+ JSON.stringify(startParams));
})
} catch (error) {
let errMsg = JSON.stringify(error);
let errCode: number = error.code;
console.log('Startup catch error , errCode= ' + errCode);
console.log('Startup catch error ,error= ' + errMsg);
}
}
// ...
}
```
开发者还可以在页面加载完成后，在页面中调用启动框架手动模式，示例代码如下。
```typescript
import { startupManager } from '@kit.AbilityKit';
@Entry
@Component
struct Index {
@State message: string = '手动模式';
@State startParams: Array<string> = ["StartupTask_006"];
build() {
RelativeContainer() {
Button(this.message)
.id('AppStartup')
.fontSize(20)
.fontWeight(FontWeight.Bold)
.onClick(() => {
if (!startupManager.isStartupTaskInitialized("StartupTask_006")) { // 判断是否已经完成初始化
startupManager.run(this.startParams)
}
})
.alignRules({
center: {anchor: '__container__', align: VerticalAlign.Center},
middle: {anchor: '__container__', align: HorizontalAlign.Center}
})
}
.height('100%')
.width('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/subscribe-system-environment-variable-changes-V14
爬取时间: 2025-04-27 22:15:58
来源: Huawei Developer
系统环境变量是指：在应用程序运行期间，终端设备的系统设置（例如系统的语言环境、屏幕方向等）发生变化。
开发者通过订阅系统环境变化，可以使应用程序及时感知这种变化，并作出相应处理，从而提供更好的用户体验。例如，用户更改系统语言设置时，应用程序可以自动根据新的语言设置更新用户界面的语言；当用户将设备旋转到横屏或者竖屏时，应用程序可以重新布局用户界面，以适应屏幕方向和尺寸。
系统配置的变化通常由“设置”中的选项或“控制中心”中的图标触发。订阅系统环境变量变化，可以使应用程序更加智能地响应系统环境变化，从而提供更好的用户体验。查看当前支持订阅变化的系统环境变量，请参见Configuration。
基于当前的应用模型，可以通过以下几种方式来实现订阅系统环境变量的变化。
使用ApplicationContext订阅回调
ApplicationContext提供了注册回调函数以订阅系统环境变量的变化，并且可以通过调用相应的方法来撤销该回调。这有助于在资源不再需要时释放相关资源，从而提高系统的可靠性和性能。
1.  使用on方法，应用程序可以通过在非应用组件模块中订阅系统环境变量的变化来动态响应这些变化。例如，使用该方法在页面中监测系统语言的变化。
```typescript
import { common, EnvironmentCallback, Configuration } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[CollaborateAbility]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Index {
private context = getContext(this) as common.UIAbilityContext;
private callbackId: number = 0; // 注册订阅系统环境变化的ID
subscribeConfigurationUpdate(): void {
let systemLanguage: string | undefined = this.context.config.language; // 获取系统当前语言
// 1.获取ApplicationContext
let applicationContext = this.context.getApplicationContext();
// 2.通过applicationContext订阅环境变量变化
let environmentCallback: EnvironmentCallback = {
onConfigurationUpdated(newConfig: Configuration) {
hilog.info(DOMAIN_NUMBER, TAG, `onConfigurationUpdated systemLanguage is ${systemLanguage}, newConfig: ${JSON.stringify(newConfig)}`);
if (systemLanguage !== newConfig.language) {
hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage from ${systemLanguage} changed to ${newConfig.language}`);
systemLanguage = newConfig.language; // 将变化之后的系统语言保存，作为下一次变化前的系统语言
}
},
onMemoryLevel(level) {
hilog.info(DOMAIN_NUMBER, TAG, `onMemoryLevel level: ${level}`);
}
}
try {
this.callbackId = applicationContext.on('environment', environmentCallback);
} catch (err) {
let code = (err as BusinessError).code;
let message = (err as BusinessError).message;
hilog.error(DOMAIN_NUMBER, TAG, `Failed to register applicationContext. Code is ${code}, message is ${message}`);
}
}
// 页面展示
build() {
//...
}
}
```
2.  在资源使用完成之后，可以通过调用off方法释放相关资源。
```typescript
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[CollaborateAbility]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Index {
private context = getContext(this) as common.UIAbilityContext;
private callbackId: number = 0; // 注册订阅系统环境变化的ID
unsubscribeConfigurationUpdate() {
let applicationContext = this.context.getApplicationContext();
try {
applicationContext.off('environment', this.callbackId);
} catch (err) {
let code = (err as BusinessError).code;
let message = (err as BusinessError).message;
hilog.error(DOMAIN_NUMBER, TAG, `Failed to unregister applicationContext. Code is ${code}, message is ${message}`);
}
}
// 页面展示
build() {
//...
}
}
```
在AbilityStage组件容器中订阅回调
使用AbilityStage.onConfigurationUpdate()回调方法订阅系统环境变量的变化。当系统环境变量发生变化时，会调用该回调方法。在该方法中，通过Configuration对象获取最新的系统环境配置信息。可以进行相应的界面适配等操作，从而提高系统的灵活性和可维护性。
例如，在AbilityStage.onConfigurationUpdate()回调方法中实现监测系统语言的变化。
```typescript
import { AbilityStage, Configuration } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[MyAbilityStage]';
const DOMAIN_NUMBER: number = 0xFF00;
let systemLanguage: string | undefined; // 系统当前语言
export default class MyAbilityStage extends AbilityStage {
onCreate(): void {
systemLanguage = this.context.config.language; // Module首次加载时，获取系统当前语言
hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage is ${systemLanguage}`);
//...
}
onConfigurationUpdate(newConfig: Configuration): void {
hilog.info(DOMAIN_NUMBER, TAG, `onConfigurationUpdate, language: ${newConfig.language}`);
hilog.info(DOMAIN_NUMBER, TAG, `onConfigurationUpdated systemLanguage is ${systemLanguage}, newConfig: ${JSON.stringify(newConfig)}`);
if (systemLanguage !== newConfig.language) {
hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage from ${systemLanguage} changed to ${newConfig.language}`);
systemLanguage = newConfig.language; // 将变化之后的系统语言保存，作为下一次变化前的系统语言
}
}
}
```
在UIAbility组件中订阅回调
UIAbility组件提供了UIAbility.onConfigurationUpdate()回调方法用于订阅系统环境变量的变化。当系统环境变量发生变化时，会调用该回调方法。在该方法中，通过Configuration对象获取最新的系统环境配置信息，而无需重启UIAbility。
当使用回调方法订阅系统环境变量的变化时，该回调方法会随着UIAbility的生命周期而存在，在UIAbility销毁时一并销毁。
例如，在onConfigurationUpdate()回调方法中实现监测系统语言的变化。
```typescript
import { AbilityConstant, Configuration, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[EntryAbility]';
const DOMAIN_NUMBER: number = 0xFF00;
let systemLanguage: string | undefined; // 系统当前语言
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
systemLanguage = this.context.config.language; // UIAbility实例首次加载时，获取系统当前语言
hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage is ${systemLanguage}`);
}
onConfigurationUpdate(newConfig: Configuration): void {
hilog.info(DOMAIN_NUMBER, TAG, `onConfigurationUpdated systemLanguage is ${systemLanguage}, newConfig: ${JSON.stringify(newConfig)}`);
if (systemLanguage !== newConfig.language) {
hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage from ${systemLanguage} changed to ${newConfig.language}`);
systemLanguage = newConfig.language; // 将变化之后的系统语言保存，作为下一次变化前的系统语言
}
}
// ...
}
```
在ExtensionAbility组件中订阅回调
ExtensionAbility组件提供了onConfigurationUpdate()回调方法用于订阅系统环境变量的变化。当系统环境变量发生变化时，会调用该回调方法。在该方法中，通过Configuration对象获取最新的系统环境配置信息。
当使用回调方法订阅系统环境变量的变化时，该回调方法会随着ExtensionAbility的生命周期而存在，在ExtensionAbility销毁时一并销毁。
以FormExtensionAbility为例说明。例如，在onConfigurationUpdate()回调方法中实现系统环境变量的变化。
```typescript
import { FormExtensionAbility } from '@kit.FormKit';
import { Configuration } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[EntryAbility]';
const DOMAIN_NUMBER: number = 0xFF00;
export default class EntryFormAbility extends FormExtensionAbility {
onConfigurationUpdate(config: Configuration) {
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onConfigurationUpdate:' + JSON.stringify(config));
}
// ...
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/inter-app-redirection-V14
爬取时间: 2025-04-27 22:16:12
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/link-between-apps-overview-V14
爬取时间: 2025-04-27 22:16:25
来源: Huawei Developer
应用跳转是指从一个应用跳转至另外一个应用，传递相应的数据、执行特定的功能。通过应用跳转可以满足用户更为真实丰富的场景诉求、提升交互体验的便捷性和流畅性。
应用场景
应用间跳转在社交分享、推广营销等场景广泛使用。举例如下：
应用跳转的两种类型
-  拉起指定应用：拉起方应用明确指定跳转的目标应用，来实现应用跳转。指向性跳转可以分为指定应用链接、指定Ability两种方式。 从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用。关于如何从指定Ability方式切换到指定应用链接方式，详见显式Want跳转切换应用链接跳转适配指导。 指定应用链接（推荐）：通过openLink或startAbility接口来指定应用链接，拉起目标应用页面。 指定Ability（不推荐）：通过startAbility接口指定具体的Ability（即显式Want方式），拉起目标应用页面。
-  指定应用链接（推荐）：通过openLink或startAbility接口来指定应用链接，拉起目标应用页面。
-  指定Ability（不推荐）：通过startAbility接口指定具体的Ability（即显式Want方式），拉起目标应用页面。
-  拉起指定类型的应用：拉起方应用通过指定应用类型，拉起垂类应用面板。该面板将展示目标方接入的垂域应用，由用户选择打开指定应用。
-  指定应用链接（推荐）：通过openLink或startAbility接口来指定应用链接，拉起目标应用页面。
-  指定Ability（不推荐）：通过startAbility接口指定具体的Ability（即显式Want方式），拉起目标应用页面。
典型场景：拉起系统应用
拉起系统应用是应用间跳转的一种典型场景。系统提供了一些能力和接口，在确保访问安全的前提下，可以让开发者快捷地实现系统应用跳转，详见拉起系统应用。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/directional-redirection-V14
爬取时间: 2025-04-27 22:16:39
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-startup-overview-V14
爬取时间: 2025-04-27 22:16:53
来源: Huawei Developer
本章节主要介绍如何通过应用链接跳转的方式拉起指定应用。
从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用。关于如何从指定Ability方式切换到指定应用链接方式，详见显式Want跳转切换应用链接跳转适配指导。
应用链接
应用链接是指可以将用户引导至应用内特定位置或相关网页的URL，常见的格式如下。更多关于应用链接格式与字段含义的说明，详见应用链接说明。
运作机制
应用链接分类
按照应用链接的scheme以及校验机制的不同，可以分为Deep Linking与App Linking两种方式。
-  Deep Linking：是一种通过链接跳转至应用特定页面的技术，其特点是支持开发者定义任意形式的scheme。由于缺乏域名校验机制，容易被其他应用所仿冒。
-  App Linking：其限定了scheme必须为https，同时通过增加域名校验机制，可以从已匹配到的应用中筛选过滤出目标应用，消除应用查询和定位中产生的歧义，直达受信的目标应用。
相比Deep Linking，App Linking具有更高的安全性和可靠性，用户体验更佳。推荐开发者将App Linking作为首选方案。
| 类型 | App Linking（推荐） | Deep Linking |
| --- | --- | --- |
| 实现方案 | 目标应用需要在module.json5中声明应用链接；同时需要向系统注册域名并通过域名认证。 | 目标应用需要在module.json5中声明应用链接。 |
| 链接格式 | scheme必须为https。 | scheme可以自定义。通常不为https、http、file，否则会拉起默认的系统浏览器。 |
| 是否可用于分享或直接在网页中访问 | 可以 | 不可以，需在代码中调用。 |
| 是否可以直接拉起目标应用 | 可以 | 可以，但不推荐使用，存在被仿冒风险。 |
Deep Linking与App Linking均可以使用openLink接口实现，不同条件下的跳转效果如下。
该接口中的appLinkingOnly字段表示是否必须以App Linking的方式启动UIAbility，默认为false。appLinkingOnly为true一般只用于浏览器等应用。
| 应用链接类型 | App Linking（推荐） | Deep Linking |
| --- | --- | --- |
| appLinkingOnly为false且目标应用已安装 | 直接跳转打开目标应用。 | 跳转目标应用（如果有多个符合条件的应用时，展示应用选择弹框）。 |
| appLinkingOnly为false且目标应用未安装 | 跳转默认浏览器打开网页。 | 返回失败，系统不跳转，由应用自行处理；当前会展示“链接无法打开”弹框。 |
| appLinkingOnly为true且目标应用已安装 | 直接跳转打开目标应用。 | 返回失败，系统不跳转，由应用自行处理。 |
| appLinkingOnly为true且目标应用未安装 | 返回失败，系统不跳转由应用自行处理。 | 返回失败，系统不跳转，由应用自行处理。 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/canopenlink-V14
爬取时间: 2025-04-27 22:17:07
来源: Huawei Developer
使用场景
在应用A想要拉起应用B的场景中，应用A可先调用canOpenLink接口判断应用B是否可访问，如果可访问，再拉起应用B。
约束限制
在entry模块的module.json5文件中的querySchemes字段中，最多允许配置50个URL scheme。
接口说明
canOpenLink是bundleManager提供的支持判断目标应用是否可访问的接口。
匹配规则请参考显式Want与隐式Want匹配规则。
操作步骤
调用方操作步骤
1.  在entry模块的module.json5文件中配置querySchemes属性，声明想要查询的URL scheme。
```json
{
"module": {
//...
"querySchemes": [
"app1Scheme"
]
}
}
```
2.  导入ohos.bundle.bundleManager模块。
3.  调用canOpenLink接口。
```typescript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
let link = 'app1Scheme://test.example.com/home';
let canOpen = bundleManager.canOpenLink(link);
hilog.info(0x0000, 'testTag', 'canOpenLink successfully: %{public}s', JSON.stringify(canOpen));
} catch (err) {
let message = (err as BusinessError).message;
hilog.error(0x0000, 'testTag', 'canOpenLink failed: %{public}s', message);
}
```
目标方操作步骤
在module.json5文件中配置uris属性。
```json
{
"module": {
//...
"abilities": [
{
//...
"skills": [
{
"uris": [
{
"scheme": "app1Scheme",
"host": "test.example.com",
"pathStartWith": "home"
}
]
}
]
}
]
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/deep-linking-startup-V14
爬取时间: 2025-04-27 22:17:21
来源: Huawei Developer
采用Deep Linking进行跳转时，系统会根据接口中传入的uri信息，在本地已安装的应用中寻找到符合条件的应用并进行拉起。当匹配到多个应用时，会拉起应用选择框。
实现原理
Deep Linking基于隐式Want匹配机制中的uri匹配来查询、拉起目标应用。隐式Want的uri匹配规则详见uri匹配规则。
目标应用操作指导
配置module.json5文件
为了能够支持被其他应用访问，目标应用需要在module.json5配置文件中配置skills标签。
skills标签下默认包含一个skill对象，用于标识应用入口。应用跳转链接不能在该skill对象中配置，需要创建独立的skill对象。如果存在多个跳转场景，需要在skills标签下创建不同的skill对象，否则会导致配置无法生效。
Deep Linking中的scheme取值支持自定义，可以为任意不包含特殊字符、非ohos开头的字符串。通常不为https、http、file，否则会拉起默认的系统浏览器。
配置示例如下：
```json
{
"module": {
// ...
"abilities": [
{
// ...
"skills": [
{
"entities": [
"entity.system.home"
],
"actions": [
"action.system.home"
]
},
{
"actions": [
// actions不能为空，actions为空会造成目标方匹配失败。
"ohos.want.action.viewData"
],
"uris": [
{
// scheme必选，可以自定义，以link为例，需要替换为实际的scheme
"scheme": "link",
// host必选，配置待匹配的域名
"host": "www.example.com"
}
]
} // 新增一个skill对象，用于跳转场景。如果存在多个跳转场景，需配置多个skill对象。
]
}
]
}
}
```
获取并解析拉起方传入的应用链接
在目标应用的UIAbility的onCreate()或者onNewWant()生命周期回调中，获取、解析拉起方传入的应用链接。
```typescript
// 以EntryAbility.ets为例
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { url } from '@kit.ArkTS';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 从want中获取传入的链接信息。
// 如传入的url为：link://www.example.com/programs?action=showall
let uri = want?.uri;
if (uri) {
// 从链接中解析query参数，拿到参数后，开发者可根据自己的业务需求进行后续的处理。
let urlObject = url.URL.parseURL(want?.uri);
let action = urlObject.params.get('action');
// 例如，当action为showall时，展示所有的节目。
if (action === "showall") {
// ...
}
}
}
}
```
拉起方应用实现应用跳转
下面通过三个案例，分别介绍如何使用openLink()与startAbility()接口实现应用跳转，以及如何在Web组件中实现应用跳转。
使用openLink实现应用跳转
在openLink接口的link字段中传入目标应用的URL信息，并将options字段中的appLinkingOnly配置为false。
示例代码如下：
```typescript
import { common, OpenLinkOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[UIAbilityComponentsOpenLink]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Index {
build() {
Button('start link', { type: ButtonType.Capsule, stateEffect: true })
.width('87%')
.height('5%')
.margin({ bottom: '12vp' })
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
let link: string = "link://www.example.com";
let openLinkOptions: OpenLinkOptions = {
appLinkingOnly: false
};
try {
context.openLink(link, openLinkOptions)
.then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'open link success.');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `open link failed. Code is ${err.code}, message is ${err.message}`);
});
} catch (paramError) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
}
})
}
}
```
使用startAbility实现应用跳转
startAbility接口是将应用链接放入want中，通过调用隐式want匹配的方法触发应用跳转。通过startAbility接口启动时，还需要调用方传入待匹配的action和entity。
示例代码如下：
```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[UIAbilityComponentsOpenLink]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Index {
build() {
Button('start ability', { type: ButtonType.Capsule, stateEffect: true })
.width('87%')
.height('5%')
.margin({ bottom: '12vp' })
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
let want: Want = {
uri: "link://www.example.com"
};
try {
context.startAbility(want).then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'start ability success.');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `start ability failed. Code is ${err.code}, message is ${err.message}`);
});
} catch (paramError) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability. Code is ${paramError.code}, message is ${paramError.message}`);
}
})
}
}
```
使用Web组件实现应用跳转
Web组件需要跳转DeepLink链接应用时，可通过拦截回调onLoadIntercept中对定义的事件进行处理，实现应用跳转。
示例代码如下：
```typescript
// index.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onLoadIntercept((event) => {
const url: string = event.data.getRequestUrl();
if (url === 'link://www.example.com') {
(getContext() as common.UIAbilityContext).openLink(url)
.then(() => {
console.log('openLink success');
}).catch((err: BusinessError) => {
console.error('openLink failed, err:' + JSON.stringify(err));
});
return true;
}
// 返回true表示阻止此次加载，否则允许此次加载
return false;
})
}
}
}
```
前端页面代码：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-linking-startup-V14
爬取时间: 2025-04-27 22:17:36
来源: Huawei Developer
简介
使用App Linking进行跳转时，系统会根据接口传入的uri信息（HTTPS链接）将用户引导至目标应用中的特定内容，无论应用是否已安装，用户都可以访问到链接对应的内容，跳转体验相比Deep Linking方式更加顺畅。
例如：当开发者使用App Linking接入“扫码直达”服务后，用户可通过控制中心扫一扫等系统级扫码入口，扫描应用的二维码、条形码并跳转到开发者应用对应服务页，实现一步直达的体验。
该能力目前仅适用于API 12及以上版本的HarmonyOS应用，如果您开发的是元服务，请参考使用App Linking实现元服务跳转。
适用场景
实现原理
开发指导概述
若要实现App Linking跳转体验，需目标方和拉起方的不同角色相互配合，共同完成。
各个角色的分工如下。
-  序号 ⾓⾊ 职责 1 云端开发 在AGC控制台开通App Linking服务。 2 云端开发 在开发者网站上关联应用。 3 云端开发 在AGC控制台关联网址域名。 4 客户端开发 在DevEco Studio中配置关联的网址域名。 5 客户端开发 处理传入的链接。 6 前端开发 开发链接对应的H5网页，应用未安装时呈现网页版内容。 本指南侧重于HarmonyOS应用相关的开发指导，网页的开发不在本指导范围内，开发者请依据自己的业务需求自行实现。
-  序号 ⾓⾊ 职责 1 客户端开发 调用系统接口，触发链接跳转。
| 序号  | ⾓⾊  | 职责  |
| --- | --- | --- |
| 1  | 云端开发  | 在AGC控制台开通App Linking服务。  |
| 2  | 云端开发  | 在开发者网站上关联应用。  |
| 3  | 云端开发  | 在AGC控制台关联网址域名。  |
| 4  | 客户端开发  | 在DevEco Studio中配置关联的网址域名。  |
| 5  | 客户端开发  | 处理传入的链接。  |
| 6  | 前端开发  | 开发链接对应的H5网页，应用未安装时呈现网页版内容。 说明本指南侧重于HarmonyOS应用相关的开发指导，网页的开发不在本指导范围内，开发者请依据自己的业务需求自行实现。   |
| 序号  | ⾓⾊  | 职责  |
| --- | --- | --- |
| 1  | 客户端开发  | 调用系统接口，触发链接跳转。  |
目标方应用开发指导
在AGC控制台开通App Linking服务
请先参考“应用开发准备”完成基本准备工作，再继续进行以下开发活动。
1.
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094248.60307699935065212086443804563153:50001231000000:2800:B81EA02F395DFE90566C5101111A8A96DFDDBE3BF39ACA1B382855B5680CEA26.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094248.63850029217246047932285763460073:50001231000000:2800:6A677D2583D80F50A306CB9B812497212608F9FA797027E8D0DE044AE4D6D146.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094248.80792236002795677450669113988797:50001231000000:2800:2D8731A41FDC26433646C3FD1FD3E80431327EF67F1F9CC79DAC136C7A36478B.png)
在开发者网站上关联应用
在开发者的网站域名服务器上做如下配置。后续当您配置该网站域名时，系统会通过此文件确认哪些应用才是合法归属于此域名的，使链接更加安全可靠。
```typescript
{
"applinking": {
"apps": [
{
"appIdentifier": "1234567"
}
]
}
}
```
1.  https://domain.name/.well-known/applinking.json 例如：开发者的服务器域名为www.example.com，则必须将applinking.json文件放在如下位置： https://www.example.com/.well-known/applinking.json
在AGC控制台关联网址域名
基于HarmonyOS应用链接能力，需要为HarmonyOS应用创建关联的网址域名。如果用户已安装HarmonyOS应用，则用户点击域名下网址链接后，系统会默认打开该HarmonyOS应用内的相关页面。
1.
2.  不可以在域名后面添加/，即不支持“https://www.example.com/”形式。
3.  应用链接发布完成后，如果距离上次更新超过24小时，系统会去域名服务器上重新获取配置文件进行交集校验。 例如：您在4月7日17:21创建了应用链接，系统会在4月8日17:30去域名服务器上重新获取配置文件，然后进行交集校验，更新发布状态。
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094248.76847003811263410520727985578077:50001231000000:2800:64AF8751995217444BB5DE016586B9CA884705B1133FAE651864662AFD4D6FA4.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094248.96296115547121231189705398561042:50001231000000:2800:8CD8CD9655A88F86A1D3BAD445CFE59C4333C1E8567187961BF0B3A4687303BB.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094248.36589790403121605792420272062184:50001231000000:2800:E0A0C7E9994E8D017C002E04727151F58B4C5C17161214541C820266958A8D63.png)
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094249.48833027604354540081958851740316:50001231000000:2800:1A9B83F799A3A393F306C824EAC4380909E10D90D4B6714C823A22272F12A2BD.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094249.10533627054544284900502244778406:50001231000000:2800:589C97DC3F22A998B49E83784D09E5E2A4A62D45B9D7BFAD14CBC85F8631E6FC.png)
在DevEco Studio中配置关联的网址域名
在应用的module.json5文件中进行如下配置，以声明应用关联的域名地址，并开启域名校验开关。
skills标签下默认包含一个skill对象，用于标识应用入口。应用跳转链接不能在该skill对象中配置，需要创建独立的skill对象。
如果存在多个跳转场景，需要在skills标签下创建不同的skill对象，否则会导致配置无法生效。
例如，声明应用关联的域名是www.example.com，则需进行如下配置。
```typescript
{
"module": {
"abilities": [
{
"name": "EntryAbility",
"srcEntry": "./ets/entryability/EntryAbility.ts",
"icon": "$media:icon",
"label": "$string:EntryAbility_label",
// 请将exported配置为true；如果exported为false，仅具有权限的系统应用能够拉起该应用，否则无法拉起应用
"exported": true,
"startWindowIcon": "$media:icon",
"startWindowBackground": "$color:start_window_background",
"skills": [
{
"entities": [
"entity.system.home"
],
"actions": [
"action.system.home"
]
},
{
"entities": [
// entities必须包含"entity.system.browsable"
"entity.system.browsable"
],
"actions": [
// actions必须包含"ohos.want.action.viewData"
"ohos.want.action.viewData"
],
"uris": [
{
// scheme须配置为https
"scheme": "https",
// host须配置为关联的域名
"host": "www.example.com",
// path可选，表示域名服务器上的目录或文件路径，例如www.example.com/path1中的path1
// 如果应用只能处理部分特定的path，则此处应该配置应用所支持的path，避免出现应用不能处理的path链接也被引流到应用中的问题
"path": "path1"
}
],
// domainVerify须设置为true
"domainVerify": true
}
// 若有其他跳转能力，如推送消息跳转、NFC跳转，可新增一个skill对象，防止与App Linking业务冲突
]
}
]
}
}
```
处理传入的链接
在应用的Ability（如EntryAbility）的onCreate()或者onNewWant()生命周期回调中添加如下代码，以处理传入的链接。
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { url } from '@kit.ArkTS';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 从want中获取传入的链接信息。
// 如传入的url为：https://www.example.com/programs?action=showall
let uri = want?.uri
if (uri) {
// 从链接中解析query参数，拿到参数后，开发者可根据自己的业务需求进行后续的处理。
let urlObject = url.URL.parseURL(want?.uri);
let action = urlObject.params.get('action')
// 例如，当action为showall时，展示所有的节目。
if (action === "showall"){
//...
}
//...
}
}
}
```
若要根据链接参数启动UIAbility的指定页面组件，请参考“启动UIAbility的指定页面”。
验证应用被拉起效果
1.  不能使用DevEco Studio的自动签名功能，必须使用手动签名，否则无法拉起应用。
2.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094249.31057686508408313411627907621748:50001231000000:2800:1A0A5FFD2E6390D83279E52BC46950B91EE769A3A302132D8A97DFE43F0C8A97.gif)
拉起方实现跳转指导
支持App Linking的应用可以通过如下方式被拉起：
1.  拉起方应用通过UIAbilityContext.openLink()接口，传入目标应用的链接，拉起目标应用。 openLink接口提供了两种拉起目标应用的方式，开发者可根据业务需求进行选择。 将appLinkingOnly参数设为true，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则抛异常给开发者进行处理。 适用于无法打开目标应用时，开发者做了相应的异常处理。例如：拉起方应用集成了ArkWeb，当目标应用不存在时，可通过ArkWeb打开链接。 将appLinkingOnly参数设为false或者不传，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则尝试以浏览器打开链接的方式打开应用。 适用于无法打开目标应用时，开发者未做任何处理。此时目标应用不存在时，会通过系统浏览器打开链接。 本文为了方便验证App Linking的配置是否正确，选择方式一，示例如下。 在拉起方应用中执行上述代码，如果拉起方应用成功拉起目标应用，则成功配置App Linking。
```typescript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct Index {
build() {
Button('start link', { type: ButtonType.Capsule, stateEffect: true })
.width('87%')
.height('5%')
.margin({ bottom: '12vp' })
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
let link: string = "https://www.example.com/programs?action=showall";
// 仅以App Linking的方式打开应用
context.openLink(link, { appLinkingOnly: true })
.then(() => {
console.info('openlink success.');
})
.catch((error: BusinessError) => {
console.error(`openlink failed. error:${JSON.stringify(error)}`);
});
})
}
}
```
2.  将appLinkingOnly参数设为true，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则抛异常给开发者进行处理。 适用于无法打开目标应用时，开发者做了相应的异常处理。例如：拉起方应用集成了ArkWeb，当目标应用不存在时，可通过ArkWeb打开链接。
3.  将appLinkingOnly参数设为false或者不传，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则尝试以浏览器打开链接的方式打开应用。 适用于无法打开目标应用时，开发者未做任何处理。此时目标应用不存在时，会通过系统浏览器打开链接。
-  将appLinkingOnly参数设为true，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则抛异常给开发者进行处理。 适用于无法打开目标应用时，开发者做了相应的异常处理。例如：拉起方应用集成了ArkWeb，当目标应用不存在时，可通过ArkWeb打开链接。
-  将appLinkingOnly参数设为false或者不传，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则尝试以浏览器打开链接的方式打开应用。 适用于无法打开目标应用时，开发者未做任何处理。此时目标应用不存在时，会通过系统浏览器打开链接。
FAQ
应用的module.json5文件skills设置不正确，如何处理？
检查"host"字段中应用所对应的域名是否设置正确。
开发者网站服务器配置不正确，如何处理？
系统尚未完成域名校验，如何处理？
按照以下步骤排查：
如何确认域名校验是否成功？
如需查看应用域名验证结果，请在Deveco Studio中打开终端，并使用以下命令查询验证结果：
hdc shell hidumper -s AppDomainVerifyManager
运行hidumper命令后，即可在控制台上看到success消息。
设备首次启动，若无法通过AppLinking拉起系统预装应用，如何处理？
设备首次启动后，系统将在20分钟内尝试对预装应用进行域名校验，若在20分钟内设备一直无法访问网络，则可能导致预装应用域名校验失败。若出现此类问题，请重启设备，或者等待24小时后重试。系统将在下次开机或24小时后对预装应用重新尝试进行域名校验。
访问CDN时发现内容未及时更新，如何处理？
CDN缓存时间为10分钟，请您耐心等待一段时间后再次访问。
应用和域名的对应关系如何？
应用和域名的关系是多对多的关系：一个应用可以关联多个不同的域名，同样地，一个域名也可以关联多个不同的应用。
如果同一域名关联了多个应用，那么该域名的链接将拉起哪个应用？
开发者可以通过配置applinking.json以关联多个应用。如果每个应用的module.json5的uris字段配置的都是一样的，那么系统将弹出列表框供用户选择要拉起的目标应用。 为了更好的体验，开发者也可以通过链接的path去区分拉起的目标应用，如链接https://www.example.com/path1拉起目标应用1，链接https://www.example.com/path2拉起目标应用2。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/uiability-startup-adjust-V14
爬取时间: 2025-04-27 22:17:50
来源: Huawei Developer
从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用，推荐通过指定应用链接的方式来实现。
本章节介绍如何从显式Want跳转切换到应用链接跳转。
启动其他应用的UIAbility
1.  将待跳转的应用安装到设备，在其对应UIAbility的module.json5配置文件中配置skills标签的entities字段、actions字段和uri字段：
```json
{
"module": {
// ...
"abilities": [
{
// ...
"skills": [
{
"entities": [
"entity.system.browsable"
],
"actions": [
"ohos.want.action.viewData"
],
"uris": [
{
"scheme": "https",
"host": "www.example.com",
}
],
"domainVerify": true
}
]
}
]
}
}
```
2.  调用方通过openLink接口执行跳转，在接口入参需要传入转换后的link和配置options, 不再传入bundleName、moduleName和abilityName。系统会根据传入的link匹配到符合skill配置的应用。
```typescript
import { common } from '@kit.AbilityKit';
import OpenLinkOptions from '@ohos.app.ability.OpenLinkOptions';
import { BusinessError } from '@ohos.base';
import hilog from '@ohos.hilog';
const TAG: string = '[UIAbilityComponentsOpenLink]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Index {
build() {
Button('start link', { type: ButtonType.Capsule, stateEffect: true })
.width('87%')
.height('5%')
.margin({ bottom: '12vp' })
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
// 通过startAbility接口显式启动其他UIAbility，推荐使用openLink接口。
// let want: Want = {
//   bundleName: "com.test.example",
//   moduleName: "entry",
//   abilityName: "EntryAbility"
// };
// try {
//   context.startAbility(want)
//     .then(() => {
//       hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
//     }).catch((err: BusinessError) => {
//       hilog.error(DOMAIN_NUMBER, TAG, `startAbility failed. Code is ${err.code}, message is ${err.message}`);
//     })
// } catch (paramError) {
//   hilog.error(DOMAIN_NUMBER, TAG, `Failed to startAbility. Code is ${paramError.code}, message is ${paramError.message}`);
// }
let link: string = "https://www.example.com";
let openLinkOptions: OpenLinkOptions = {
// 匹配的abilities选项是否需要通过AppLinking域名校验，匹配到唯一配置过的应用ability
appLinkingOnly: true,
// 同want中的parameter，用于传递的参数
parameters: {demo_key: "demo_value"}
};
try {
context.openLink(link, openLinkOptions)
.then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'open link success.');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `open link failed. Code is ${err.code}, message is ${err.message}`);
})
} catch (paramError) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
}
})
}
}
```
启动其他应用的UIAbility并获取返回结果
1.  将待跳转的应用安装到设备，在其对应UIAbility的module.json5配置文件中配置skills标签的entities字段、actions字段和uri字段：
```json
{
"module": {
// ...
"abilities": [
{
// ...
"skills": [
{
"entities": [
"entity.system.browsable"
],
"actions": [
"ohos.want.action.viewData"
],
"uris": [
{
"scheme": "https",
"host": "www.example.com",
}
],
"domainVerify": true
}
]
}
]
}
}
```
2.  调用方通过openLink接口执行跳转，在接口入参需要传入转换后的link和配置options, 不再传入bundleName、moduleName和abilityName。系统会根据传入的link匹配到符合skills配置的应用。AbilityResult回调结果返回通过入参传入回调函数，在启动ability停止自身后返回给调用方的信息。启动成功和失败结果仍通过Promise返回。
```typescript
import { common } from '@kit.AbilityKit';
import OpenLinkOptions from '@ohos.app.ability.OpenLinkOptions';
import { BusinessError } from '@ohos.base';
import hilog from '@ohos.hilog';
const TAG: string = '[UIAbilityComponentsOpenLink]';
const DOMAIN_NUMBER: number = 0xFF00;
@Entry
@Component
struct Index {
build() {
Button('start link', { type: ButtonType.Capsule, stateEffect: true })
.width('87%')
.height('5%')
.margin({ bottom: '12vp' })
.onClick(() => {
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
// 通过startAbility接口显式启动其他UIAbility，推荐使用openLink接口。
// let want: Want = {
//   bundleName: "com.test.example",
//   moduleName: "entry",
//   abilityName: "EntryAbility"
// };
// try {
//   context.startAbilityForResult(want)
//     .then((data) => {
//       hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success. data:' + JSON.stringify(data));
//     }).catch((err: BusinessError) => {
//       hilog.error(DOMAIN_NUMBER, TAG, `startAbility failed. Code is ${err.code}, message is ${err.message}`);
//     })
// } catch (paramError) {
//   hilog.error(DOMAIN_NUMBER, TAG, `Failed to startAbility. Code is ${paramError.code}, message is ${paramError.message}`);
// }
let link: string = "https://www.example.com";
let openLinkOptions: OpenLinkOptions = {
// 匹配的abilities选项是否需要通过AppLinking域名校验，匹配到唯一配置过的应用ability
appLinkingOnly: true,
// 同want中的parameter，用于传递的参数
parameters: {demo_key: "demo_value"}
};
try {
context.openLink(link, openLinkOptions, (err, data) => {
// AbilityResult callback回调，仅在被拉起ability死亡时触发
hilog.info(DOMAIN_NUMBER, TAG, 'open link success. Callback result:' + JSON.stringify(data));
}).then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'open link success.');
}).catch((err: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `open link failed. Code is ${err.code}, message is ${err.message}`);
})
} catch (paramError) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
}
})
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-uri-config-V14
爬取时间: 2025-04-27 22:18:03
来源: Huawei Developer
uris标签说明
当在module.json5文件的skills字段中声明uris时，主要包含如下字段。
-  scheme：协议名称。常见的取值有http、https、file、ftp等，也可以自定义。
-  host：域名或IP地址。例如域名developer.huawei.com或IP地址127.0.0.1。
-  port：端口号。例如developer.huawei.com:80后面的80即为端口号。
-  path：路径，表示域名服务器上的目录或文件路径，该字段在scheme存在时才有意义。path字段不支持通配符，如果需要使用通配符，可以采用pathRegex字段。
-  pathStartWith：路径前缀，该字段在scheme存在时才有意义，表示域名服务器上的目录或文件路径的前缀，用于前缀匹配。
-  pathRegex：路径正则，该字段在scheme存在时才有意义，表示域名服务器上的目录或文件路径的正则表达式，用于正则匹配。
-  linkFeature：应用的功能类型（如文件打开、分享、导航等）。取值为长度不超过127字节的字符串，不支持中文。
URL的基本格式
按照配置的字段不同，uris可以拼接为不同的URL表达式。其中，scheme为必选字段，其他字段仅当scheme存在时才有意义。
-  当配置了path、pathStartWith或pathRegex字段时，组成的表达式如下。 三方应用组件配置的scheme不能与系统应用重复，否则会导致无法通过该uri拉起三方应用组件。
linkFeature标签说明
同一Bundle中声明的linkFeature数量不能超过150个。
目标应用在linkFeature字段中申明功能类型，并通过应用市场上架审核后，可以提升应用跳转体验。主要用于以下两种场景：
1.  支持系统识别同类应用：当调用方拉起垂类应用（例如导航类应用）时，系统会根据linkFeature字段识别到匹配的应用，并在应用面板中展现。
2.  跳转一键返回能力：用户从A应用跳转至B应用的某个功能界面后，B应用调用一键返回能力，可以支持用户直接返回A应用，无问询弹窗。例如：A应用跳转至B应用的支付界面，若B应用已申请了支付的linkfeature，则用户在B应用内完成操作后，可一键返回A应用。
| 值 | 说明 |
| --- | --- |
| AppStorageMgmt | 指示清理应用沙箱目录中缓存数据的功能 |
| FileOpen | 指示打开处理文件的功能 |
| Navigation | 指示导航功能 |
| RoutePlan | 指示路线规划功能 |
| PlaceSearch | 指示地点搜索功能 |
| 值 | 说明 |
| --- | --- |
| Login | 指示登录、授权登录等功能 |
| Pay | 指示支付页面、收银台等功能 |
| Share | 指示分享功能 |
配置示例
下面以授权登录场景举例说明：
```json
"uris": [
{
"scheme": "https",
"host": "developer.huawei.com",
"path": "consumer",
"linkFeature": "Login"
}
]
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/specified-type-app-redirection-V14
爬取时间: 2025-04-27 22:18:18
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-intent-panel-V14
爬取时间: 2025-04-27 22:18:31
来源: Huawei Developer
本章节主要介绍拉起方应用如何通过指定应用类型、而非某个具体的应用，来实现应用跳转。通常有以下几种方式：
通过startAbilityByType接口拉起垂类面板
实现机制
开发者可通过特定的业务类型如导航、金融、邮件等，调用startAbilityByType接口拉起对应的垂域面板，该面板将展示目标方接入的垂域应用，由用户选择打开指定应用以实现相应的垂类意图。
垂域面板为调用方提供统一的安全、可信的目标方应用，同时降低调用方的接入成本。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170220.50932620333324186981095606941287:50001231000000:2800:191B8AAC44D1F0B973B6DD25B2B32BE8E875EFBF16F25BE38092E0DA0C162398.png)
匹配规则
UIAbilityContext.startAbilityByType和UIExtensionContentSession.startAbilityByType接口支持基于业务类型拉起垂域面板。调用方通过指定业务类型即可拉起对应的垂域面板，在垂域面板上将展示目标方接入的垂域应用。
系统会根据调用方在startAbilityByType接口传入的type与wantParams.sceneType取值，按照如下映射关系，匹配到在module.json5配置文件中声明了对应linkFeature的目标应用。
| 支持的功能 | 调用方（startAbilityByType接口入参） | 目标方（配置文件linkFeature取值） |
| --- | --- | --- |
| 路线规划功能 | - type：navigation - wantParams.sceneType：1 | RoutePlan |
| 导航功能 | - type：navigation - wantParams.sceneType：2 | Navigation |
| 位置搜索功能 | - type：navigation - wantParams.sceneType：3 | PlaceSearch |
| 转账汇款功能 | - type：finance - wantParams.sceneType：1 | Transfer |
| 信用卡还款功能 | - type：finance - wantParams.sceneType：2 | CreditCardRepayment |
| 撰写邮件功能 | - type：mail - wantParams.sceneType：1 | ComposeMail |
| 按航班号查询航班功能 | - type：flight - wantParams.sceneType：1 | QueryByFlightNo |
| 按起降地查询航班功能 | - type：flight - wantParams.sceneType：2 | QueryByLocation |
| 快递查询功能 | - type：express - wantParams.sceneType：1 | QueryExpress |
- type：navigation
- wantParams.sceneType：1
- type：navigation
- wantParams.sceneType：2
- type：navigation
- wantParams.sceneType：3
- type：finance
- wantParams.sceneType：1
- type：finance
- wantParams.sceneType：2
- type：mail
- wantParams.sceneType：1
- type：flight
- wantParams.sceneType：1
- type：flight
- wantParams.sceneType：2
- type：express
- wantParams.sceneType：1
通过mailto方式跳转电子邮件应用
通过mailto电子邮件协议，可以创建指向电子邮件地址的超链接，方便用户通过网页或应用中的超链接直接跳转电子邮件应用。详见拉起邮件类应用（mailto方式）。
通过startAbility接口打开文件
开发者可以通过调用startAbility接口，由系统从已安装的应用中寻找符合要求的应用，打开特定类型的文件。详见拉起文件处理类应用。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-navigation-apps-V14
爬取时间: 2025-04-27 22:18:45
来源: Huawei Developer
本章节介绍如何拉起导航类应用扩展面板。
导航类应用扩展面板参数说明
startAbilityByType接口中type字段为navigation，支持路线规划、导航、位置搜索三种意图场景，对应的wantParam参数如下：
本文中的经纬度均采用GCJ-02坐标系统。
-  路线规划场景
-  导航场景
-  位置搜索场景
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。默认为1，路线规划场景填1或不填 |
| originName | string | 否 | 起点名称 |
| originLatitude | number | 否 | 起点纬度 |
| originLongitude | number | 否 | 起点经度 |
| originPoiIds | Record<number, string> | 否 | 起点POI ID列表，当前仅支持传入花瓣地图和高德地图的POI ID |
| destinationName | string | 否 | 终点名称 |
| destinationLatitude | number | 是 | 终点纬度 |
| destinationLongitude | number | 是 | 终点经度 |
| destinationPoiIds | Record<number, string> | 否 | 终点POI ID列表，当前仅支持传入花瓣地图和高德地图的POI ID |
| vehicleType | number | 否 | 交通出行工具，取值：0-驾车，1-步行，2-骑行，3-公交； |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 是 | 意图场景，表明本次请求对应的操作意图。导航场景填2 |
| destinationName | string | 否 | 终点名称 |
| destinationLatitude | number | 是 | 终点纬度 |
| destinationLongitude | number | 是 | 终点经度 |
| destinationPoiIds | Record<number, string> | 否 | 终点POI ID列表，当前仅支持传入花瓣地图和高德地图的POI ID |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 是 | 意图场景，表明本次请求对应的操作意图。位置搜索场景填3 |
| destinationName | string | 是 | 地点名称 |
拉起方开发步骤
1.  导入相关模块。
```typescript
import { common } from '@kit.AbilityKit';
```
2.  构造接口参数并调用startAbilityByType接口。 终点POI ID列表（destinationPoiIds）和起点POI ID列表（originPoiIds）需开发者自行从各地图系统中获取，并按照对应关系传参。 效果示例图：
```typescript
let context = getContext(this) as common.UIAbilityContext;
let wantParam: Record<string, Object> = {
'sceneType': 1,
'destinationLatitude': 32.060844,
'destinationLongitude': 118.78315,
'destinationName': 'xx市xx路xx号',
'destinationPoiIds': {
1: '1111',  // key为1代表花瓣地图，value需为花瓣地图POI
2: '2222'   // key为2代表高德地图，value需为高德地图POI
} as Record<number, string>,
'originName': 'xx市xx公园',
'originLatitude': 31.060844,
'originLongitude': 120.78315,
'originPoiIds': {
1: '3333',  // key为1代表花瓣地图，value需为花瓣地图POI
2: '4444'   // key为2代表高德地图，value需为高德地图POI
} as Record<number, string>,
'vehicleType': 0
};
let abilityStartCallback: common.AbilityStartCallback = {
onError: (code: number, name: string, message: string) => {
console.log(`onError code ${code} name: ${name} message: ${message}`);
},
onResult: (result)=>{
console.log(`onResult result: ${JSON.stringify(result)}`);
}
}
context.startAbilityByType("navigation", wantParam, abilityStartCallback,
(err) => {
if (err) {
console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
} else {
console.log(`success`);
}
});
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170220.72915863229032682584594090020489:50001231000000:2800:1FD7E4A7D5753FCC51D9D9AA1811A25D9ECFFE20C8CF7B46D1B6FE465C134596.png)
目标方开发步骤
1.  在module.json5中配置uris，步骤如下：
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "maps", // 这里仅示意，应用需确保这里声明的的uri能被外部正常拉起
"host": "navigation",
"path": "",
"linkFeature": "Navigation" // 声明应用支持导航功能
},
{
"scheme": "maps", // 这里仅示意，应用需确保这里声明的的uri能被外部正常拉起
"host": "routePlan",
"path": "",
"linkFeature": "RoutePlan" // 声明应用支持路线规划功能
},
{
"scheme": "maps", // 这里仅示意，应用需确保这里声明的的uri能被外部正常拉起
"host": "search",
"path": "",
"linkFeature": "PlaceSearch" // 声明应用支持位置搜索功能
}
]
}
]
}
]
}
```
2.  解析参数并做对应处理。 在参数want.uri中会携带目标方配置的linkFeature对应的uri。 在参数want.parameters中会携带Caller方传入的参数，不同场景参数如下所示。 路线规划场景 导航场景 位置搜索场景 应用可根据linkFeature中定义的特性功能，比如路线规划、导航和位置搜索，结合接收到的uri和参数开发不同的样式页面。
```typescript
UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
```
3.  路线规划场景
4.  导航场景
5.  位置搜索场景
| 取值 | 含义 |
| --- | --- |
| Navigation | 声明应用支持导航功能 |
| RoutePlan | 声明应用支持路线规划功能 |
| PlaceSearch | 声明应用支持位置搜索功能 |
-  路线规划场景
-  导航场景
-  位置搜索场景
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originName | string | 否 | 起点名称 |
| originLatitude | number | 否 | 起点纬度 |
| originLongitude | number | 否 | 起点经度 |
| originPoiId | string | 否 | 起点POI ID，当前仅支持花瓣地图和高德地图获取此参数 |
| destinationName | string | 否 | 终点名称 |
| destinationLatitude | number | 是 | 终点纬度 |
| destinationLongitude | number | 是 | 终点经度 |
| destinationPoiId | string | 否 | 终点POI ID，当前仅支持花瓣地图和高德地图获取此参数 |
| vehicleType | number | 否 | 交通出行工具，取值：0-驾车，1-步行，2-骑行，3-公交； |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destinationName | string | 否 | 终点名称 |
| destinationLatitude | number | 是 | 终点纬度 |
| destinationLongitude | number | 是 | 终点经度 |
| destinationPoiId | string | 否 | 终点POI ID，当前仅支持花瓣地图和高德地图获取此参数 |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destinationName | string | 是 | 地点名称 |
完整示例：
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
const TAG = 'EntryAbility'
export default class EntryAbility extends UIAbility {
windowStage: window.WindowStage | null = null;
uri?: string;
destinationLatitude?: number;
destinationLongitude?: number;
destinationName?: string;
originName?: string;
originLatitude?: number;
originLongitude?: number;
vehicleType?: number;
destinationPoiId?: string;
originPoiId?: string;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
super.onCreate(want, launchParam);
this.parseWant(want);
}
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
super.onNewWant(want, launchParam);
this.parseWant(want);
if (!this.windowStage) {
hilog.error(0x0000, TAG, 'windowStage is null');
this.context.terminateSelf();
return;
}
this.loadPage(this.windowStage);
}
private parseWant(want: Want): void {
this.uri = want.uri as string | undefined;
this.destinationLatitude = want.parameters?.destinationLatitude as number | undefined;
this.destinationLongitude = want.parameters?.destinationLongitude as number | undefined;
this.destinationName = want.parameters?.destinationName as string | undefined;
this.originName = want.parameters?.originName as string | undefined;
this.originLatitude = want.parameters?.originLatitude as number | undefined;
this.originLongitude = want.parameters?.originLongitude as number | undefined;
this.vehicleType = want.parameters?.vehicleType as number | undefined;
this.destinationPoiId = want.parameters?.destinationPoiId as string | undefined;
this.originPoiId = want.parameters?.originPoiId as string | undefined;
}
private loadPage(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `loadPage, uri=${this.uri}`);
if (this.uri === 'maps://navigation') {
// 构建导航场景参数
const storage: LocalStorage = new LocalStorage({
"destinationLatitude": this.destinationLatitude,
"destinationLongitude": this.destinationLongitude,
"destinationPoiId": this.destinationPoiId
} as Record<string, Object>);
// 拉起导航页面
windowStage.loadContent('pages/NavigationPage', storage)
} else if (this.uri === 'maps://routePlan') {
// 构建路径规划场景参数
const storage: LocalStorage = new LocalStorage({
"destinationLatitude": this.destinationLatitude,
"destinationLongitude": this.destinationLongitude,
"destinationName": this.destinationName,
"originName": this.originName,
"originLatitude": this.originLatitude,
"originLongitude": this.originLongitude,
"vehicleType": this.vehicleType,
"destinationPoiId": this.destinationPoiId,
"originPoiId": this.originPoiId
} as Record<string, Object>);
// 拉起路径规划页面
windowStage.loadContent('pages/RoutePlanPage', storage)
}  else if (this.uri === 'maps://search') {
// 构建位置搜索场景参数
const storage: LocalStorage = new LocalStorage({
"destinationName": this.destinationName
} as Record<string, Object>);
// 拉起位置搜索页面
windowStage.loadContent('pages/PlaceSearchPage', storage)
} else {
// 默认拉起首页
windowStage.loadContent('pages/Index', (err) => {
if (err.code) {
hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s',
JSON.stringify(err) ?? '');
return;
}
hilog.info(0x0000, TAG, 'Succeeded in loading the content.');
});
}
}
onDestroy(): void {
hilog.info(0x0000, TAG, `onDestroy`);
}
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `onWindowStageCreate`);
this.windowStage = windowStage;
this.loadPage(this.windowStage);
}
onWindowStageDestroy(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onWindowStageDestroy');
}
onForeground(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onForeground');
}
onBackground(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onBackground');
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-email-apps-V14
爬取时间: 2025-04-27 22:18:58
来源: Huawei Developer
本章节介绍如何拉起邮件类应用扩展面板。
邮件类应用扩展面板参数说明
startAbilityByType接口中type字段为mail，对应的wantParam参数：
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string[ ] | 否 | 收件人邮箱地址（支持多个且以逗号分隔） |
| cc | string[ ] | 否 | 抄收人邮箱地址（支持多个且以逗号分隔） |
| bcc | string[ ] | 否 | 密送人邮箱地址（支持多个且以逗号分隔） |
| subject | string | 否 | 邮件主题 |
| body | string | 否 | 邮件内容 |
| ability.params.stream | string[ ] | 否 | 邮件附件（附件的uri地址列表） |
| ability.want.params.uriPermissionFlag | wantConstant.Flags | 否 | 给邮件附件赋予至少读权限。邮件附件参数存在时，该参数也必须要传 |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。1：发邮件。默认为1。 |
-  邮件类应用扩展面板中的类型为string的参数，都要经过encodeURI编码。
-  邮件类应用扩展面板中的类型为string[]的参数，数组中的元素都要经过encodeURI编码。
拉起方开发步骤
1.  导入相关模块。
```typescript
import { common, wantConstant } from '@kit.AbilityKit';
```
2.  构造接口参数并调用startAbilityByType接口。 效果示例图：
```typescript
let context = getContext(this) as common.UIAbilityContext;
let wantParam: Record<string, Object> = {
'sceneType': 1,
'email': [encodeURI('xxx@example.com'),encodeURI('xxx@example.com')], // 收件人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码
'cc': [encodeURI('xxx@example.com'),encodeURI('xxx@example.com')], // 抄收人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码
'bcc': [encodeURI('xxx@example.com'),encodeURI('xxx@example.com')], // 密送人邮箱地址，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码
'subject': encodeURI('邮件主题'), // 邮件主题，对内容使用encodeURI()方法进行url编码
'body': encodeURI('邮件正文'), // 邮件正文，对内容使用encodeURI()方法进行url编码
'ability.params.stream': [encodeURI('附件uri1'),encodeURI('附件uri2')], // 附件uri，多值以逗号分隔，对数组内容使用encodeURI()方法进行url编码
'ability.want.params.uriPermissionFlag': wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION
};
let abilityStartCallback: common.AbilityStartCallback = {
onError: (code: number, name: string, message: string) => {
console.log(`onError code ${code} name: ${name} message: ${message}`);
},
onResult: (result)=>{
console.log(`onResult result: ${JSON.stringify(result)}`);
}
}
context.startAbilityByType("mail", wantParam, abilityStartCallback,
(err) => {
if (err) {
console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
} else {
console.log(`success`);
}
});
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170221.56367440252215330970793611227311:50001231000000:2800:DB90B383D1D59BD5A65C0C1A3EF325C687FE968459BFE4BE5E80CBC30ED6C7F5.png)
目标方开发步骤
1.  在module.json5中新增linkFeature属性并设置声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "mailto", // 这里仅示意，应用需确保这里声明的的uri能被外部正常拉起
"host": "",
"path": "",
"linkFeature": "ComposeMail" // 声明应用支持撰写邮件功能
}
]
}
]
}
]
}
```
2.  解析面板传过来的参数并做对应处理。 在参数want.parameters中会携带Caller方传入的参数（与调用方传入的有些差异），如下表所示： 目标方接收的类型为string的参数，都要经过decodeURI解码。 目标方接收的类型为string[]的参数，数组中的元素都要经过decodeURI解码。
```typescript
UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
```
3.  目标方接收的类型为string的参数，都要经过decodeURI解码。
4.  目标方接收的类型为string[]的参数，数组中的元素都要经过decodeURI解码。
| 取值 | 含义 |
| --- | --- |
| ComposeMail | 声明应用支持撰写邮件功能 |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string[ ] | 否 | 收件人邮箱地址（支持多个且以逗号分隔） |
| cc | string[ ] | 否 | 抄收人邮箱地址（支持多个且以逗号分隔） |
| bcc | string[ ] | 否 | 密送人邮箱地址（支持多个且以逗号分隔） |
| subject | string | 否 | 邮件主题 |
| body | string | 否 | 邮件内容 |
| stream | string[ ] | 否 | 邮件附件列表（附件的uri地址列表） |
-  目标方接收的类型为string的参数，都要经过decodeURI解码。
-  目标方接收的类型为string[]的参数，数组中的元素都要经过decodeURI解码。
完整示例：
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
const TAG = 'MailTarget1.EntryAbility'
export default class EntryAbility extends UIAbility {
windowStage: window.WindowStage | null = null;
email: string[] | undefined;
cc: string[] | undefined;
bcc: string[] | undefined;
subject: string | undefined;
body: string | undefined;
stream: string[] | undefined;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
super.onCreate(want, launchParam);
this.parseWant(want);
}
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
super.onNewWant(want, launchParam);
this.parseWant(want);
if (!this.windowStage) {
hilog.error(0x0000, TAG, 'windowStage is null');
this.context.terminateSelf();
return;
}
this.loadPage(this.windowStage);
}
private parseWant(want: Want): void {
this.email = this.decodeStringArr(want.parameters?.email as string[]);
this.cc = this.decodeStringArr(want.parameters?.cc as string[]);
this.bcc = this.decodeStringArr(want.parameters?.bcc as string[]);
this.subject = decodeURI(want.parameters?.subject as string);// 使用decodeURI()方法对邮件主题进行url解码，其他字段处理方法相同
this.body = decodeURI(want.parameters?.body as string);// 使用decodeURI()方法对邮件内容进行url解码，其他字段处理方法相同
this.stream = this.decodeStringArr(want.parameters?.stream as string[]);
}
// 使用decodeURI()方法对string数组内容进行解码
private decodeStringArr(source: string[] | undefined): string[] {
let target: string[] = [];
source?.forEach(e => {
target.push(decodeURI(e));
})
return target;
}
private loadPage(windowStage: window.WindowStage): void {
const storage: LocalStorage = new LocalStorage({
"email": this.email,
"cc": this.cc,
"bcc": this.bcc,
"subject": this.subject,
"body": this.body,
"stream": this.stream
} as Record<string, Object>);
windowStage.loadContent('pages/ComposeMailPage', storage);
}
onDestroy(): void {
hilog.info(0x0000, TAG, `onDestroy`);
}
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `onWindowStageCreate`);
this.windowStage = windowStage;
this.loadPage(this.windowStage);
}
onWindowStageDestroy(): void {
hilog.info(0x0000, TAG, `onWindowStageDestroy`);
}
onForeground(): void {
hilog.info(0x0000, TAG, `onForeground`);
}
onBackground(): void {
hilog.info(0x0000, TAG, `onBackground`);
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-email-apps-by-mailto-V14
爬取时间: 2025-04-27 22:19:12
来源: Huawei Developer
使用场景
通过mailto电子邮件协议，可以创建指向电子邮件地址的超链接，方便用户通过网页或应用中的超链接直接跳转电子邮件应用。同时，支持在mailto:的相关字段中定义邮件的收件人、主题、正文内容等，节省用户编辑邮件的时间。
常见的应用场景举例如下：
mailto协议格式
mailto协议标准格式如下：
-  mailto:：mailto scheme，必填。
-  someone@example.com：收件人地址，选填。如果存在多个地址，用英文逗号分隔。
-  ?：邮件头声明开始符号。如果带邮件头参数，则必填。
-  key-value：邮件头参数，详细参数见下表。
| 邮件头 | 含义 | 数据类型 | 是否必填 |
| --- | --- | --- | --- |
| subject | 邮件主题 | string | 否 |
| body | 邮件正文 | string | 否 |
| cc | 抄送人，多个用逗号分隔 | string | 否 |
| bcc | 密送人，多个用逗号分隔 | string | 否 |
拉起方开发步骤
从网页拉起
网页中的超链接需要满足mailto协议。示例如下：
实际开发时，需要将邮箱地址替换为真实的邮箱，邮件内容可以根据需要进行配置。
实现效果如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170221.81202232891202693882038481427173:50001231000000:2800:D1BC9FE8A38011094B8269B78E4851945B0F71F121A7FB300D45B5B6D553E5C3.gif)
从应用拉起
保证mailto字符串传入uri参数即可，在应用中page页面可通过 getContext(this) 获取context，在ability中可通过this.context获取context。
```typescript
@Entry
@Component
struct Index {
build() {
Column() {
Button('反馈')
.onClick(() => {
let ctx = getContext(this) as common.UIAbilityContext;
ctx.startAbility({
action: 'ohos.want.action.sendToData',
uri: 'mailto:feedback@example.com?subject=App Feedback&body=Please describe your feedback here...'
})
})
}
}
}
```
实现效果如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170221.70766149886102162134266056632887:50001231000000:2800:6CD7451A217A8B0B17F51588BBFC6924BF80AAD6EB688AD0072264E069A02F5C.gif)
目标方开发步骤
1.  为了能够支持被其他应用通过mailto协议拉起，目标应用需要在module.json5配置文件中声明mailto。
```json
{
"module": {
// ...
"abilities": [
{
// ...
"skills": [
{
"actions": [
'ohos.want.action.sendToData'
],
"uris": [
{
"scheme": "mailto",
// linkFeature 用于适配垂类面板拉起
"linkFeature": 'ComposeMail'
}
]
}
]
}
]
}
}
```
2.  目标应用在代码中取出uri参数进行解析。
```typescript
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 应用冷启动生命周期回调，其他业务处理...
parseMailto(want);
}
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 应用热启动生命周期回调，其他业务处理...
parseMailto(want);
}
public parseMailto(want: Want) {
const uri = want?.uri;
if (!uri || uri.length <= 0) {
return;
}
// 开始解析 mailto...
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-finance-apps-V14
爬取时间: 2025-04-27 22:19:26
来源: Huawei Developer
本章节介绍如何拉起金融类应用扩展面板。
金融类应用扩展面板参数说明
startAbilityByType接口中type字段为finance，对应的wantParam参数：
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。1：转账汇款 2：信用卡还款。默认为1 |
| bankCardNo | string | 否 | 银行卡卡号 |
拉起方开发步骤
1.  导入相关模块。
```typescript
import { common } from '@kit.AbilityKit';
```
2.  构造接口参数并调用startAbilityByType接口。 效果示例图：
```typescript
let context = getContext(this) as common.UIAbilityContext;
let wantParam: Record<string, Object> = {
'sceneType': 1,
"bankCardNo": '123456789'
};
let abilityStartCallback: common.AbilityStartCallback = {
onError: (code: number, name: string, message: string) => {
console.log(`onError code ${code} name: ${name} message: ${message}`);
},
onResult: (result)=>{
console.log(`onResult result: ${JSON.stringify(result)}`);
}
}
context.startAbilityByType("finance", wantParam, abilityStartCallback,
(err) => {
if (err) {
console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
} else {
console.log(`success`);
}
});
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170221.12637636207279534549442145934524:50001231000000:2800:104B916837FCE4215F09B4ACE397B04C3AADAAEB0F24AF6ED732ACAA6BFD388C.png)
目标方开发步骤
1.  在module.json5中配置uris，步骤如下： 设置linkFeature属性以声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下： 设置scheme、host、port、path/pathStartWith属性，与Want中URI相匹配，以便区分不同功能。
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "finance", // 这里仅示意，应用需确保这里声明的的uri能被外部正常拉起
"host": "transfer",
"path": "",
"linkFeature": "Transfer" // 声明应用支持转账汇款功能
},
{
"scheme": "finance", // 这里仅示意，应用需确保这里声明的的uri能被外部正常拉起
"host": "credit_card_repayment",
"path": "",
"linkFeature": "CreditCardRepayment" // 声明应用支持信用卡还款功能
}
]
}
]
}
]
}
```
2.  设置linkFeature属性以声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：
3.  设置scheme、host、port、path/pathStartWith属性，与Want中URI相匹配，以便区分不同功能。
4.  解析面板传过来的参数并做对应处理。 在参数want.uri中会携带目标方配置的linkFeature对应的uri; 在参数want.parameters中会携带Caller方传入的参数，如下表所示： 应用可根据linkFeature中定义的特性功能，比如转账汇款和信用卡还款，结合接收到的uri开发不同的样式页面。
```typescript
UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
```
1.  设置linkFeature属性以声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：
2.  设置scheme、host、port、path/pathStartWith属性，与Want中URI相匹配，以便区分不同功能。
| 取值 | 含义 |
| --- | --- |
| Transfer | 声明应用支持转账汇款功能 |
| CreditCardRepayment | 声明应用支持信用卡还款功能 |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bankCardNo | string | 否 | 银行卡卡号 |
完整示例：
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
const TAG = 'EntryAbility'
export default class EntryAbility extends UIAbility {
windowStage: window.WindowStage | null = null;
uri?: string;
bankCardNo?: string;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
super.onCreate(want, launchParam);
this.parseWant(want);
}
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
super.onNewWant(want, launchParam);
this.parseWant(want);
if (!this.windowStage) {
hilog.error(0x0000, TAG, 'windowStage is null');
this.context.terminateSelf();
return;
}
this.loadPage(this.windowStage);
}
private parseWant(want: Want): void {
this.uri = want.uri as string | undefined;
this.bankCardNo = want.parameters?.bankCardNo as string | undefined;
}
private loadPage(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `loadPage, uri=${this.uri}`);
if (this.uri === 'finance://transfer') {
// 构建转账场景参数
const storage: LocalStorage = new LocalStorage({
"bankCardNo": this.bankCardNo
} as Record<string, Object>);
// 拉起转账页面
windowStage.loadContent('pages/TransferPage', storage)
} else if (this.uri === 'finance://credit_card_repayment') {
// 构建信用卡还款场景参数
const storage: LocalStorage = new LocalStorage({
"bankCardNo": this.bankCardNo
} as Record<string, Object>);
// 拉起信用卡还款页面
windowStage.loadContent('pages/CreditCardRepaymentPage', storage)
} else {
// 默认拉起首页
windowStage.loadContent('pages/Index', (err) => {
if (err.code) {
hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s',
JSON.stringify(err) ?? '');
return;
}
hilog.info(0x0000, TAG, 'Succeeded in loading the content.');
});
}
}
onDestroy(): void {
hilog.info(0x0000, TAG, `onDestroy`);
}
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `onWindowStageCreate`);
this.windowStage = windowStage;
this.loadPage(this.windowStage);
}
onWindowStageDestroy(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onWindowStageDestroy');
}
onForeground(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onForeground');
}
onBackground(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onBackground');
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-flight-apps-V14
爬取时间: 2025-04-27 22:19:39
来源: Huawei Developer
本章节介绍如何拉起航班类应用扩展面板。
例如，在行程安排类App中，当用户记录了某次行程的航班号，应用能够识别航班号信息并提供航班动态查询的链接。用户点击链接后，应用将通过调用UIAbilityContext.startAbilityByType或UIExtensionContentSession.startAbilityByType接口，拉起航班类应用的扩展面板。面板上将展示设备上所有支持航班查询的应用，供用户选择并跳转至所需应用。
航班类应用扩展面板参数说明
startAbilityByType接口中type字段为flight，支持按航班号查询、按起降地查询两种意图场景，对应的wantParam参数如下：
-  按航班号查询场景
-  按起降地查询场景
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。默认为1，按航班号查询场景填1或不填。 |
| flightNo | string | 是 | 航班号，航司二位代码+数字。 |
| departureDate | string | 否 | 航班出发时间：YYYY-MM-DD。 |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 是 | 意图场景，表明本次请求对应的操作意图。按起降地查询场景填2。 |
| originLocation | string | 是 | 出发地。 |
| destinationLocation | string | 是 | 目的地。 |
| departureDate | string | 否 | 航班出发时间：YYYY-MM-DD。 |
拉起方开发步骤
1.  导入相关模块。
```typescript
import { common } from '@kit.AbilityKit';
```
2.  构造接口参数并调用startAbilityByType接口。 效果示例图：
```typescript
let context = getContext(this) as common.UIAbilityContext;
let wantParam: Record<string, Object> = {
'sceneType': 1,
'flightNo': 'ZH1509',
'departureDate': '2024-10-01'
};
let abilityStartCallback: common.AbilityStartCallback = {
onError: (code: number, name: string, message: string) => {
console.log(`onError code ${code} name: ${name} message: ${message}`);
},
onResult: (result)=>{
console.log(`onResult result: ${JSON.stringify(result)}`);
}
}
context.startAbilityByType("flight", wantParam, abilityStartCallback,
(err) => {
if (err) {
console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
} else {
console.log(`success`);
}
});
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170221.15922289338057069639430236476268:50001231000000:2800:BA3E17CECCFAD10ADB9CDD512E1665D5A917D51A449B3265D37A9570D60D7E2B.png)
目标方开发步骤
1.  在module.json5中配置uris：
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "flight",
"host": "queryByFlightNo",
"path": "",
"linkFeature": "QueryByFlightNo"
},
{
"scheme": "flight",
"host": "queryByLocation",
"path": "",
"linkFeature": "QueryByLocation"
}
]
}
]
}
]
}
```
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "flight",
"host": "queryByFlightNo",
"path": "",
"linkFeature": "QueryByFlightNo"
},
{
"scheme": "flight",
"host": "queryByLocation",
"path": "",
"linkFeature": "QueryByLocation"
}
]
}
]
}
]
}
```
2.  解析参数并做对应处理。 在参数want.uri中会携带目标方配置的linkFeature对应的uri; 在参数want.parameters中会携带Caller方传入的参数，不同场景参数如下所示 按航班号查询场景 按起降地查询场景 应用可根据linkFeature中定义的特性功能，比如按航班号查询和按起降地查询，结合接收到的uri和参数开发不同的样式页面。
```typescript
UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
```
3.  按航班号查询场景
4.  按起降地查询场景
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "flight",
"host": "queryByFlightNo",
"path": "",
"linkFeature": "QueryByFlightNo"
},
{
"scheme": "flight",
"host": "queryByLocation",
"path": "",
"linkFeature": "QueryByLocation"
}
]
}
]
}
]
}
```
| 取值 | 含义 |
| --- | --- |
| QueryByFlightNo | 声明应用支持按航班号查询航班。 |
| QueryByLocation | 声明应用支持按起降地查询航班。 |
-  按航班号查询场景
-  按起降地查询场景
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flightNo | string | 是 | 航班号，航司二位代码+数字。 |
| departureDate | string | 否 | 航班出发时间：YYYY-MM-DD。不填时，Target可按当天处理。 |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originLocation | string | 是 | 出发地。 |
| destinationLocation | string | 是 | 目的地。 |
| departureDate | string | 否 | 航班出发时间：YYYY-MM-DD。不填时，Target可按当天处理。 |
完整示例：
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
const TAG = 'EntryAbility'
export default class EntryAbility extends UIAbility {
windowStage: window.WindowStage | null = null;
uri?: string;
flightNo?: string;
departureDate?: string;
originLocation?: string;
destinationLocation?: string;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
super.onCreate(want, launchParam);
this.parseWant(want);
}
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
super.onNewWant(want, launchParam);
this.parseWant(want);
if (!this.windowStage) {
hilog.error(0x0000, TAG, 'windowStage is null');
this.context.terminateSelf();
return;
}
this.loadPage(this.windowStage);
}
private parseWant(want: Want): void {
this.uri = want.uri as string | undefined;
this.flightNo = want.parameters?.flightNo as string | undefined;
this.departureDate = want.parameters?.departureDate as string | undefined;
this.originLocation = want.parameters?.originLocation as string | undefined;
this.destinationLocation = want.parameters?.destinationLocation as string | undefined;
}
private loadPage(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `loadPage, uri=${this.uri}`);
if (this.uri === 'flight://queryByFlightNo') {
// 构建按航班号查询场景参数
const storage: LocalStorage = new LocalStorage({
"flightNo": this.flightNo,
"departureDate": this.departureDate
} as Record<string, Object>);
// 拉起按航班号查询页面
windowStage.loadContent('pages/QueryByFlightNoPage', storage)
} else if (this.uri === 'flight://queryByLocation') {
// 构建按起降地查询场景参数
const storage: LocalStorage = new LocalStorage({
"originLocation": this.originLocation,
"destinationLocation": this.destinationLocation,
"departureDate": this.departureDate
} as Record<string, Object>);
// 拉起按起降地查询页面
windowStage.loadContent('pages/QueryByLocationPage', storage)
} else {
// 默认拉起首页
windowStage.loadContent('pages/Index', (err) => {
if (err.code) {
hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s',
JSON.stringify(err) ?? '');
return;
}
hilog.info(0x0000, TAG, 'Succeeded in loading the content.');
});
}
}
onDestroy(): void {
hilog.info(0x0000, TAG, `onDestroy`);
}
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `onWindowStageCreate`);
this.windowStage = windowStage;
this.loadPage(this.windowStage);
}
onWindowStageDestroy(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onWindowStageDestroy');
}
onForeground(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onForeground');
}
onBackground(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onBackground');
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-express-apps-V14
爬取时间: 2025-04-27 22:19:53
来源: Huawei Developer
本章节介绍如何拉起快递类应用扩展面板。
例如，在消息类App中，用户收到快递单号，应用能够识别快递单号信息并提供快递查询的链接。用户点击链接后，应用将通过调用UIAbilityContext.startAbilityByType或UIExtensionContentSession.startAbilityByType接口，拉起快递类应用的扩展面板。面板上将展示设备上所有支持快递查询的应用，供用户选择并跳转至所需应用。
快递类应用扩展面板参数说明
startAbilityByType接口中type字段为express，支持查询快递意图，对应的wantParam参数如下：
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。默认为1，查询快递填场景填1或不填。 |
| expressNo | string | 是 | 快递单号。 |
拉起方开发步骤
1.  导入相关模块。
```typescript
import { common } from '@kit.AbilityKit';
```
2.  构造接口参数并调用startAbilityByType接口。 效果示例图：
```typescript
let context = getContext(this) as common.UIAbilityContext;
let wantParam: Record<string, Object> = {
'sceneType': 1,
'expressNo': 'SF123456'
};
let abilityStartCallback: common.AbilityStartCallback = {
onError: (code: number, name: string, message: string) => {
console.log(`onError code ${code} name: ${name} message: ${message}`);
},
onResult: (result)=>{
console.log(`onResult result: ${JSON.stringify(result)}`);
}
}
context.startAbilityByType("express", wantParam, abilityStartCallback,
(err) => {
if (err) {
console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
} else {
console.log(`success`);
}
});
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170221.75806210899854810526584674729334:50001231000000:2800:64932484E9D69F6C74935896251585DEAA8D9D617CF672E2F0CE0D750E8B6394.png)
目标方开发步骤
1.  在module.json5中配置uris：
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "express",
"host": "queryExpress",
"path": "",
"linkFeature": "QueryExpress"
}
]
}
]
}
]
}
```
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "express",
"host": "queryExpress",
"path": "",
"linkFeature": "QueryExpress"
}
]
}
]
}
]
}
```
2.  解析参数并做对应处理。 在参数want.uri中会携带目标方配置的linkFeature对应的uri; 在参数want.parameters中会携带Caller方传入的参数，如下所示：
```typescript
UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
```
```json
{
"abilities": [
{
"skills": [
{
"uris": [
{
"scheme": "express",
"host": "queryExpress",
"path": "",
"linkFeature": "QueryExpress"
}
]
}
]
}
]
}
```
| 取值 | 含义 |
| --- | --- |
| QueryExpress | 声明应用支持快递查询。 |
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expressNo | string | 是 | 快递单号。 |
完整示例：
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
const TAG = 'EntryAbility'
export default class EntryAbility extends UIAbility {
windowStage: window.WindowStage | null = null;
uri?: string;
expressNo?: string;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
super.onCreate(want, launchParam);
this.parseWant(want);
}
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
super.onNewWant(want, launchParam);
this.parseWant(want);
if (!this.windowStage) {
hilog.error(0x0000, TAG, 'windowStage is null');
this.context.terminateSelf();
return;
}
this.loadPage(this.windowStage);
}
private parseWant(want: Want): void {
this.uri = want.uri as string | undefined;
this.expressNo = want.parameters?.expressNo as string | undefined;
}
private loadPage(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `loadPage, uri=${this.uri}`);
if (this.uri === 'express://queryExpress') {
// 构建快递查询参数
const storage: LocalStorage = new LocalStorage({
"expressNo": this.expressNo
} as Record<string, Object>);
// 拉起快递查询页面
windowStage.loadContent('pages/QueryExpressPage', storage)
} else {
// 默认拉起首页
windowStage.loadContent('pages/Index', (err) => {
if (err.code) {
hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s',
JSON.stringify(err) ?? '');
return;
}
hilog.info(0x0000, TAG, 'Succeeded in loading the content.');
});
}
}
onDestroy(): void {
hilog.info(0x0000, TAG, `onDestroy`);
}
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(0x0000, TAG, `onWindowStageCreate`);
this.windowStage = windowStage;
this.loadPage(this.windowStage);
}
onWindowStageDestroy(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onWindowStageDestroy');
}
onForeground(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onForeground');
}
onBackground(): void {
hilog.info(0x0000, TAG, '%{public}s', 'Ability onBackground');
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/photoeditorextensionability-V14
爬取时间: 2025-04-27 22:20:06
来源: Huawei Developer
使用场景
当应用自身不具备图片编辑能力、但存在图片编辑的场景时，可以通过startAbilityByType拉起图片编辑类应用扩展面板，由对应的应用完成图片编辑操作。图片编辑类应用可以通过PhotoEditorExtensionAbility实现图片编辑页面，并将该页面注册到图片编辑面板，从而将图片编辑能力开放给其他应用。
流程示意图如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170221.16256227041121993537498565830147:50001231000000:2800:D804B3FAA53BB935565D5C7FC5B93802B7E993A5AAD81A91A33A825E8322A02C.png)
例如：用户在图库App中选择编辑图片时，图库App可以通过startAbilityByType拉起图片编辑类应用扩展面板。用户可以从已实现PhotoEditorExtensionAbility应用中选择一款，并进行图片编辑。
接口说明
接口详情参见PhotoEditorExtensionAbility和PhotoEditorExtensionContext。
| 接口名 | 描述 |
| --- | --- |
| onStartContentEditing(uri: string, want:Want, session: UIExtensionContentSession):void | 可以执行读取原始图片、加载页面等操作。 |
| saveEditedContentWithImage(pixelMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult> | 传入编辑过的图片的PixelMap对象并保存。 |
图片编辑类应用实现图片编辑页面
1.  在DevEco Studio工程中手动新建一个PhotoEditorExtensionAbility。
2.  在ExamplePhotoEditorAbility.ets中重写onCreate、onForeground、onBackground、onDestroy和onStartContentEditing的生命周期回调。 其中，需要在onStartContentEditing中加载入口页面文件pages/Index.ets，并将session、uri、实例对象等保存在LocalStorage中传递给页面。
```typescript
import { PhotoEditorExtensionAbility,UIExtensionContentSession,Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG = '[ExamplePhotoEditorAbility]';
export default class ExamplePhotoEditorAbility extends PhotoEditorExtensionAbility {
onCreate() {
hilog.info(0x0000, TAG, 'onCreate');
}
// 获取图片，加载页面并将需要的参数传递给页面
onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession): void {
hilog.info(0x0000, TAG, `onStartContentEditing want: ${JSON.stringify(want)}, uri: ${uri}`);
const storage: LocalStorage = new LocalStorage({
"session": session,
"uri": uri
} as Record<string, Object>);
session.loadContent('pages/Index', storage);
}
onForeground() {
hilog.info(0x0000, TAG, 'onForeground');
}
onBackground() {
hilog.info(0x0000, TAG, 'onBackground');
}
onDestroy() {
hilog.info(0x0000, TAG, 'onDestroy');
}
}
```
3.  在page中实现图片编辑功能。 图片编辑完成后调用saveEditedContentWithImage保存图片，并将回调结果通过terminateSelfWithResult返回给调用方。
```typescript
import { common } from '@kit.AbilityKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
const storage = LocalStorage.getShared()
const TAG = '[ExamplePhotoEditorAbility]';
@Entry
@Component
struct Index {
@State message: string = 'editImg';
@State originalImage: PixelMap | null = null;
@State editedImage: PixelMap | null = null;
private newWant ?: Want;
aboutToAppear(): void {
let originalImageUri = storage?.get<string>("uri") ?? "";
hilog.info(0x0000, TAG, `OriginalImageUri: ${originalImageUri}.`);
this.readImageByUri(originalImageUri).then(imagePixMap => {
this.originalImage = imagePixMap;
})
}
// 根据uri读取图片内容
async readImageByUri(uri: string): Promise < PixelMap | null > {
hilog.info(0x0000, TAG, "uri: " + uri);
let file: fileIo.File | undefined;
try {
file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
hilog.info(0x0000, TAG, "Original image file id: " + file.fd);
let imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
if(!imageSourceApi) {
hilog.info(0x0000, TAG, "ImageSourceApi failed");
return null;
}
let pixmap: image.PixelMap = await imageSourceApi.createPixelMap();
if(!pixmap) {
hilog.info(0x0000, TAG, "createPixelMap failed");
return null;
}
this.originalImage = pixmap;
return pixmap;
} catch(e) {
hilog.info(0x0000, TAG, `ReadImage failed:${e}`);
} finally {
fileIo.close(file);
}
return null;
}
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
Button("RotateAndSaveImg").onClick(event => {
hilog.info(0x0000, TAG, `Start to edit image and save.`);
// 编辑图片功能实现
this.originalImage?.rotate(90).then(() => {
let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
try {
// 调用saveEditedContentWithImage保存图片
(getContext(this) as common.PhotoEditorExtensionContext).saveEditedContentWithImage(this.originalImage as image.PixelMap,
packOpts).then(data => {
if (data.resultCode == 0) {
hilog.info(0x0000, TAG, `Save succeed.`);
}
hilog.info(0x0000, TAG,
`saveContentEditingWithImage result: ${JSON.stringify(data)}`);
this.newWant = data.want;
// data.want.uri存有编辑过图片的uri
this.readImageByUri(this.newWant?.uri ?? "").then(imagePixMap => {
this.editedImage = imagePixMap;
})
})
} catch (e) {
hilog.error(0x0000, TAG, `saveContentEditingWithImage failed:${e}`);
return;
}
})
}).margin({ top: 10 })
Button("terminateSelfWithResult").onClick((event => {
hilog.info(0x0000, TAG, `Finish the current editing.`);
let session = storage.get('session') as UIExtensionContentSession;
// 关闭并回传修改结果给调用方
session.terminateSelfWithResult({ resultCode: 0, want: this.newWant });
})).margin({ top: 10 })
Image(this.originalImage).width("100%").height(200).margin({ top: 10 }).objectFit(ImageFit.Contain)
Image(this.editedImage).width("100%").height(200).margin({ top: 10 }).objectFit(ImageFit.Contain)
}
.width('100%')
}
.height('100%')
.backgroundColor(Color.Pink)
.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
}
}
```
4.  在工程Module对应的module.json5配置文件中注册PhotoEditorExtensionAbility。 type标签需要配置为"photoEditor"，srcEntry需要配置为PhotoEditorExtensionAbility组件所对应的代码路径。
```json
{
"module": {
"extensionAbilities": [
{
"name": "ExamplePhotoEditorAbility",
"icon": "$media:icon",
"description": "ExamplePhotoEditorAbility",
"type": "photoEditor",
"exported": true,
"srcEntry": "./ets/PhotoEditorExtensionAbility/ExamplePhotoEditorAbility.ets",
"label": "$string:EntryAbility_label",
"extensionProcessMode": "bundle"
},
]
}
}
```
调用方拉起图片编辑类应用编辑图片
开发者可以在UIAbility或者UIExtensionAbility的页面中通过接口startAbilityByType拉起图片编辑类应用扩展面板，系统将自动查找并在面板上展示基于PhotoEditorExtensionAbility实现的图片编辑应用，由用户选择某个应用来完成图片编辑的功能，最终将编辑的结果返回给到调用方，具体步骤如下：
```typescript
import { common, wantConstant } from '@kit.AbilityKit';
import { fileUri, picker } from '@kit.CoreFileKit';
```
```typescript
async photoPickerGetUri(): Promise < string > {
try {
let PhotoSelectOptions = new picker.PhotoSelectOptions();
PhotoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
PhotoSelectOptions.maxSelectNumber = 1;
let photoPicker = new picker.PhotoViewPicker();
let photoSelectResult: picker.PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
return photoSelectResult.photoUris[0];
} catch(error) {
let err: BusinessError = error as BusinessError;
hilog.info(0x0000, TAG, 'PhotoViewPicker failed with err: ' + JSON.stringify(err));
}
return "";
}
```
```typescript
let context = getContext(this) as common.UIAbilityContext;
let file: fileIo.File | undefined;
try {
file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
hilog.info(0x0000, TAG, "file: " + file.fd);
let timeStamp = Date.now();
// 将用户图片拷贝到应用沙箱路径
fileIo.copyFileSync(file.fd, context.filesDir + `/original-${timeStamp}.jpg`);
this.filePath = context.filesDir + `/original-${timeStamp}.jpg`;
this.originalImage = fileUri.getUriFromPath(this.filePath);
} catch (e) {
hilog.info(0x0000, TAG, `readImage failed:${e}`);
} finally {
fileIo.close(file);
}
```
```typescript
let context = getContext(this) as common.UIAbilityContext;
let abilityStartCallback: common.AbilityStartCallback = {
onError: (code, name, message) => {
const tip: string = `code:` + code + ` name:` + name + ` message:` + message;
hilog.error(0x0000, TAG, "startAbilityByType:", tip);
},
onResult: (result) => {
// 获取到回调结果中编辑后的图片uri并做对应的处理
let uri = result.want?.uri ?? "";
hilog.info(0x0000, TAG, "PhotoEditorCaller result: " + JSON.stringify(result));
this.readImage(uri).then(imagePixMap => {
this.editedImage = imagePixMap;
});
}
}
```
```typescript
let uri = fileUri.getUriFromPath(this.filePath);
context.startAbilityByType("photoEditor", {
"ability.params.stream": [uri], // 原始图片的uri,只支持传入一个uri
"ability.want.params.uriPermissionFlag": wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION // 至少需要分享读权限给到图片编辑面板
} as Record<string, Object>, abilityStartCallback, (err) => {
let tip: string;
if (err) {
tip = `Start error: ${JSON.stringify(err)}`;
hilog.error(0x0000, TAG, `startAbilityByType: fail, err: ${JSON.stringify(err)}`);
} else {
tip = `Start success`;
hilog.info(0x0000, TAG, "startAbilityByType: ", `success`);
}
});
```
示例：
```typescript
import { common, wantConstant } from '@kit.AbilityKit';
import { fileUri, picker } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';
const TAG = 'PhotoEditorCaller';
@Entry
@Component
struct Index {
@State message: string = 'selectImg';
@State originalImage: ResourceStr = "";
@State editedImage: PixelMap | null = null;
private filePath: string = "";
// 根据uri读取图片内容
async readImage(uri: string): Promise < PixelMap | null > {
hilog.info(0x0000, TAG, "image uri: " + uri);
let file: fileIo.File | undefined;
try {
file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
hilog.info(0x0000, TAG, "file: " + file.fd);
let imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
if(!imageSourceApi) {
hilog.info(0x0000, TAG, "imageSourceApi failed");
return null;
}
let pixmap: image.PixelMap = await imageSourceApi.createPixelMap();
if(!pixmap) {
hilog.info(0x0000, TAG, "createPixelMap failed");
return null;
}
this.editedImage = pixmap;
return pixmap;
} catch(e) {
hilog.info(0x0000, TAG, `readImage failed:${e}`);
} finally {
fileIo.close(file);
}
return null;
}
// 图库中选取图片
async photoPickerGetUri(): Promise < string > {
try {
let PhotoSelectOptions = new picker.PhotoSelectOptions();
PhotoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
PhotoSelectOptions.maxSelectNumber = 1;
let photoPicker = new picker.PhotoViewPicker();
let photoSelectResult: picker.PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
hilog.info(0x0000, TAG,
'PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(photoSelectResult));
return photoSelectResult.photoUris[0];
} catch(error) {
let err: BusinessError = error as BusinessError;
hilog.info(0x0000, TAG, 'PhotoViewPicker failed with err: ' + JSON.stringify(err));
}
return "";
}
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
Button("selectImg").onClick(event => {
// 图库中选取图片
this.photoPickerGetUri().then(uri => {
hilog.info(0x0000, TAG, "uri: " + uri);
let context = getContext(this) as common.UIAbilityContext;
let file: fileIo.File | undefined;
try {
file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
hilog.info(0x0000, TAG, "file: " + file.fd);
let timeStamp = Date.now();
// 将用户图片拷贝到应用沙箱路径
fileIo.copyFileSync(file.fd, context.filesDir + `/original-${timeStamp}.jpg`);
this.filePath = context.filesDir + `/original-${timeStamp}.jpg`;
this.originalImage = fileUri.getUriFromPath(this.filePath);
} catch (e) {
hilog.info(0x0000, TAG, `readImage failed:${e}`);
} finally {
fileIo.close(file);
}
})
}).width('200').margin({ top: 20 })
Button("editImg").onClick(event => {
let context = getContext(this) as common.UIAbilityContext;
let abilityStartCallback: common.AbilityStartCallback = {
onError: (code, name, message) => {
const tip: string = `code:` + code + ` name:` + name + ` message:` + message;
hilog.error(0x0000, TAG, "startAbilityByType:", tip);
},
onResult: (result) => {
// 获取到回调结果中编辑后的图片uri并做对应的处理
let uri = result.want?.uri ?? "";
hilog.info(0x0000, TAG, "PhotoEditorCaller result: " + JSON.stringify(result));
this.readImage(uri).then(imagePixMap => {
this.editedImage = imagePixMap;
});
}
}
// 将图片转换为图片uri，并调用startAbilityByType拉起图片编辑应用面板
let uri = fileUri.getUriFromPath(this.filePath);
context.startAbilityByType("photoEditor", {
"ability.params.stream": [uri], // 原始图片的uri,只支持传入一个uri
"ability.want.params.uriPermissionFlag": wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION // 至少需要分享读权限给到图片编辑面板
} as Record<string, Object>, abilityStartCallback, (err) => {
let tip: string;
if (err) {
tip = `Start error: ${JSON.stringify(err)}`;
hilog.error(0x0000, TAG, `startAbilityByType: fail, err: ${JSON.stringify(err)}`);
} else {
tip = `Start success`;
hilog.info(0x0000, TAG, "startAbilityByType: ", `success`);
}
});
}).width('200').margin({ top: 20 })
Image(this.originalImage).width("100%").height(200).margin({ top: 20 }).objectFit(ImageFit.Contain)
Image(this.editedImage).width("100%").height(200).margin({ top: 20 }).objectFit(ImageFit.Contain)
}
.width('100%')
}
.height('100%')
.backgroundColor(Color.Orange)
.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/file-processing-apps-startup-V14
爬取时间: 2025-04-27 22:20:19
来源: Huawei Developer
使用场景
开发者可以通过调用startAbility接口，由系统从已安装的应用中寻找符合要求的应用，打开特定文件。
例如，浏览器下应用下载PDF文件，可以调用此接口选择文件处理应用打开此PDF文件。开发者需要在请求中设置待打开文件的URI路径（uri）、文件格式（type）等字段，以便系统能够识别，直接拉起文件打开应用或弹出一个选择框，让用户选择合适的应用来打开文件，效果示意如下图所示。
图1 效果示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170222.37372885871435149133103192828970:50001231000000:2800:D562F1AD07FC4B4B0F06578228FD9A31A784936291DD3E7C6368C32A685D43F9.jpeg)
接口关键参数说明
开发者通过调用startAbility接口即可实现由已安装的垂域应用来打开文件。
表1 startAbility请求中want相关参数说明
| 参数名称 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待打开文件的URI路径，一般配合type使用。 uri格式为：file://bundleName/path - file：文件URI的标志。 - bundleName：该文件资源的属主。 - path：文件资源在应用沙箱中的路径。 |
| type | string | 否 | 表示打开文件的类型，推荐使用UTD类型，比如：'general.plain-text'、'general.image'。目前也可以兼容使用MIME type类型，如：'text/xml' 、 'image/*'等。 说明： 1. type为可选字段，如果不传type，系统会尝试根据uri后缀名判断文件类型进行匹配；如果传入type，必须确保与uri的文件类型一致，否则会导致无法匹配到合适的应用。文件后缀与文件类型的映射关系参见Uniform Type Descriptor(UTD)预置列表。 2. 不支持传*/*。 |
| parameters | Record<string, Object> | 否 | 表示由系统定义，由开发者按需赋值的自定义参数，文件打开场景请参考表2。 |
| flags | number | 否 | 表示处理方式，文件打开场景请参考表3。 |
表示待打开文件的URI路径，一般配合type使用。
uri格式为：file://bundleName/path
- file：文件URI的标志。
- bundleName：该文件资源的属主。
- path：文件资源在应用沙箱中的路径。
表示打开文件的类型，推荐使用UTD类型，比如：'general.plain-text'、'general.image'。目前也可以兼容使用MIME type类型，如：'text/xml' 、 'image/*'等。
说明：
1. type为可选字段，如果不传type，系统会尝试根据uri后缀名判断文件类型进行匹配；如果传入type，必须确保与uri的文件类型一致，否则会导致无法匹配到合适的应用。文件后缀与文件类型的映射关系参见Uniform Type Descriptor(UTD)预置列表。
2. 不支持传*/*。
表2parameters相关参数说明
| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| ability.params.stream | string | 指示携带的文件URI要授权给目标方，用于待打开的文件存在其他文件依赖的场景。例如打开本地html文件依赖本地其余资源文件的场景等。对应的value必须是string类型的文件URI数组。文件URI的获取参考表1中uri参数。 |
| ohos.ability.params.showDefaultPicker | boolean | 表示是否强制展示文件打开方式的选择弹框，缺省为false。 - false：表示由系统策略或默认应用设置决定直接拉起文件打开应用还是展示弹框。 - true：表示始终展示弹框。 |
| showCaller | boolean | 表示调用方本身是否作为目标方应用之一参与匹配，缺省为false。 - false：不参与匹配。 - true：参与匹配。 |
表示是否强制展示文件打开方式的选择弹框，缺省为false。
- false：表示由系统策略或默认应用设置决定直接拉起文件打开应用还是展示弹框。
- true：表示始终展示弹框。
表示调用方本身是否作为目标方应用之一参与匹配，缺省为false。
- false：不参与匹配。
- true：参与匹配。
表3flags相关参数说明
| 参数名称 | 值 | 说明 |
| --- | --- | --- |
| FLAG_AUTH_READ_URI_PERMISSION | 0x00000001 | 指对URI执行读取操作的授权。 |
| FLAG_AUTH_WRITE_URI_PERMISSION | 0x00000002 | 指对URI执行写入操作的授权。 |
接入步骤
调用方接入步骤
1.  导入相关模块。
```typescript
// xxx.ets
import { fileUri } from '@kit.CoreFileKit';
import { UIAbility, Want, common, wantConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
```
2.  获取应用文件路径。
```typescript
// xxx.ets
// 假设应用bundleName值为com.example.demo
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage) {
// 获取文件沙箱路径
let filePath = this.context.filesDir + '/test1.txt';
// 将沙箱路径转换为uri
let uri = fileUri.getUriFromPath(filePath);
// 获取的uri为"file://com.example.demo/data/storage/el2/base/files/test.txt"
}
// ...
}
```
3.  构造请求数据。
```typescript
// xxx.ets
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage) {
// 获取文件沙箱路径
let filePath = this.context.filesDir + '/test.txt';
// 将沙箱路径转换为uri
let uri = fileUri.getUriFromPath(filePath);
// 构造请求数据
let want: Want = {
action: 'ohos.want.action.viewData', // 表示查看数据的操作，文件打开场景固定为此值
uri: uri,
type: 'general.plain-text', // 表示待打开文件的类型
// 配置被分享文件的读写权限，例如对文件打开应用进行读写授权
flags: wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION | wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION
};
}
// ...
}
```
4.  调用接口启动。
```typescript
// xxx.ets
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage) {
// 获取文件沙箱路径
let filePath = this.context.filesDir + '/test.txt';
// 将沙箱路径转换为uri
let uri = fileUri.getUriFromPath(filePath);
// 构造请求数据
let want: Want = {
action: 'ohos.want.action.viewData', // 表示查看数据的操作，文件打开场景固定为此值
uri: uri,
type: 'general.plain-text', // 表示待打开文件的类型
// 配置被分享文件的读写权限，例如对文件打开应用进行读写授权
flags: wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION | wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION
};
// 调用接口启动
this.context.startAbility(want)
.then(() => {
console.info('Succeed to invoke startAbility.');
})
.catch((err: BusinessError) => {
console.error(`Failed to invoke startAbility, code: ${err.code}, message: ${err.message}`);
});
}
// ...
}
```
目标方接入步骤
1.  声明文件打开能力。 支持打开文件的应用需要在module.json5配置文件中声明文件打开能力。其中uris字段表示接收URI的类型，其中scheme固定为file。type字段表示支持打开的文件类型（参见UTD类型（推荐）或MIME type类型），如下举例中类型为txt文件。
```json
{
"module": {
// ...
"abilities": [
{
// ...
"skills": [
{
"actions": [
"ohos.want.action.viewData" // 必填，声明数据处理能力
],
"uris": [
{
// 允许打开uri中以file://协议开头标识的本地文件
"scheme": "file", // 必填，声明协议类型为文件
"type": "general.plain-text", // 必填，表示支持打开的文件类型
"linkFeature": "FileOpen" // 必填且大小写敏感，表示此URI的功能为文件打开
}
// ...
]
// ...
}
]
}
]
}
}
```
2.  应用处理待打开文件。 声明了文件打开的应用在被拉起后，获取传入的Want参数信息，从中获取待打开文件的URI，在打开文件并获取对应的file对象后，可对文件进行读写操作。
```typescript
// xxx.ets
import fs from '@ohos.file.fs';
import { Want, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
// 从want信息中获取uri字段
let uri = want.uri;
if (uri == null || uri == undefined) {
console.info('uri is invalid');
return;
}
try {
// 根据待打开文件的URI进行相应操作。例如同步读写的方式打开URI获取file对象
let file = fs.openSync(uri, fs.OpenMode.READ_WRITE);
console.info('Succeed to open file.');
} catch (err) {
let error: BusinessError = err as BusinessError;
console.error(`Failed to open file openSync, code: ${error.code}, message: ${error.message}`);
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/system-app-startup-V14
爬取时间: 2025-04-27 22:20:33
来源: Huawei Developer
本章节介绍拉起系统应用的方式，以及支持跳转系统应用的能力清单。
拉起系统应用的方式
拉起系统应用除了采用使用前面章节介绍的方式（比如使用openlink拉起指定应用、使用startAbilitybyType指定类型的应用），还可以采用如下方式。
-  使用系统Picker组件 相机、文件管理、联系人等系统应用提供了系统Picker组件，支持开发者无需申请权限、即可使用系统应用的一些常用功能，比如访问用户的资源文件。 应用拉起系统Picker组件（文件选择器、照片选择器、联系人选择器等）后，由用户在Picker上选择对应的文件、照片、联系人等资源，应用即可获取到Picker的返回结果。例如，一个音频播放器应用可以通过AudioViewPicker让用户选择音频文件，然后获取所选的音频文件路径进行播放。 由于系统Picker已经获取了对应权限的预授权，开发者使用系统Picker时，无需再次申请权限也可临时受限访问对应的资源。例如，当应用需要读取用户图片时，可通过使用照片Picker，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限。 系统Picker由系统独立进程实现。
-  使用特定接口 设置、电话、日历等应用提供了一些接口，通过这些接口可以直接跳转系统应用。
支持跳转系统应用的能力清单
设置
当前支持直接拉起设置应用中如下功能界面，未列出的暂不支持。
-  权限设置：当应用通过requestPermissionsFromUser()接口拉起权限申请弹框时，如果用户拒绝授权，将无法使用该接口再次拉起弹框，需要调用requestPermissionOnSetting接口拉起权限设置弹窗。 二次向用户申请授权中以申请麦克风权限为例，介绍了如何拉起权限设置弹窗。该文档中的示例代码同样适用于应用权限组列表中的所有权限，只需将对应的权限名进行替换即可。以下为开发者经常用到的一些场景。
-  通知管理：当应用通过requestEnableNotification()接口拉起通知授权弹框时，如果用户拒绝授权，将无法使用该接口再次拉起弹框，需要调用openNotificationSettings()接口，支持拉起通知管理弹窗。
应用市场
Store Kit提供了loadProduct()接口，支持直接跳转应用详情页；也可以通过startAbility()隐式拉起应用市场详情页。详见应用详情页展示。
钱包
Payment Kit提供了requestPayment接口，可以实现单次支付、支付并签约。
电话
Telephony Kit提供makeCall()接口，支持跳转到拨号界面，并显示待拨出的号码。
日历
Calendar Kit提供addEvent接口，用于创建日程。
联系人
Contacts Kit提供联系人Picker（Contacts Picker），用于拉起联系人应用，读取联系人数据人。详见选择联系人。
地图
Map Kit提供了地图Picker，支持地点详情展示、地点选取、区划选择。
相机
文件管理
Core File Kit提供了文件Picker和音频Picker。
图库（媒体库）
Media Library Kit提供了照片Picker（PhotoViewPicker），用于访问、保存公共目录的图片或视频文件。详见选择媒体库资源、创建媒体资源。
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/process-model-stage-V14
爬取时间: 2025-04-27 22:20:46
来源: Huawei Developer
进程是系统进行资源分配的基本单位，是操作系统结构的基础。系统的进程模型如下图所示。
仅2in1设备支持将HAP和UIAbility设置为独立进程，设置方法如下：
图1进程模型示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170222.70191490880598715012425444606812:50001231000000:2800:ADA4BD64FD5E16A3CF069F7117A553DEBD21C820E76E06DF633C093A8376B571.png)
说明：
在上述模型基础上，对于系统应用可以通过申请多进程权限（如下图所示），为指定HAP配置一个自定义进程名，该HAP中的UIAbility就会运行在自定义进程中。不同的HAP可以通过配置module.json5中的process属性，使HAP运行在不同进程中。
图2多进程示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170222.68461664346645955490452523094536:50001231000000:2800:CB58355D91C6B93A8E1BC8E0A03E45FE63BB161858FC6FC3EB1F43B844349F81.png)
基于当前的进程模型，针对应用间和应用内存在多个进程的情况，系统提供了如下进程间通信机制：
公共事件机制：多用于一对多的通信场景，公共事件发布者可能存在多个订阅者同时接收事件。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/thread-model-stage-V14
爬取时间: 2025-04-27 22:21:00
来源: Huawei Developer
线程是操作系统进行运算调度的基本单位，是进程中的执行流，共享进程的资源。一个进程可以包含多个线程。
线程类型
Stage模型下的线程主要有如下三类：
-  用于执行耗时操作，支持线程间通信。 TaskPool与Worker的运作机制、通信手段和使用方法可以参考TaskPool和Worker的对比。
-  用于执行耗时操作，支持线程间通信。 TaskPool与Worker的运作机制、通信手段和使用方法可以参考TaskPool和Worker的对比。
-  用于执行耗时操作，支持线程间通信。 TaskPool与Worker的运作机制、通信手段和使用方法可以参考TaskPool和Worker的对比。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170222.11459478850903802993017717125533:50001231000000:2800:0817FAB482CDB0E3DF25D83BDC5E17F2C3121120D9A50653D6758147070CFCBD.png)
使用EventHub进行线程内通信
EventHub提供了线程内发送和处理事件的能力，包括对事件订阅、取消订阅、触发事件等。以UIAbility组件与UI之间的数据同步为例，具体使用方法可以参考UIAbility组件与UI的数据同步。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/config-file-stage-V14
爬取时间: 2025-04-27 22:21:13
来源: Huawei Developer
应用配置文件中包含应用配置信息、应用组件信息、权限信息、开发者自定义信息等，这些信息在编译构建、分发和运行解决分别提供给编译工具、应用市场和操作系统使用。
在基于Stage模型开发的应用项目代码下，都存在app.json5（一个）及module.json5（一个或多个）两种配置文件，常用配置项请参见应用/组件级配置。对于这两种配置文件的更多介绍，请参见应用配置文件概述（Stage模型）。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/fa-model-development-V14
爬取时间: 2025-04-27 22:21:27
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/fa-model-development-overview-V14
爬取时间: 2025-04-27 22:21:40
来源: Huawei Developer
基于FA模型开发应用时，在应用模型部分，涉及如下开发过程。
表1FA模型开发流程
| 任务 | 简介 | 相关指导 |
| --- | --- | --- |
| 应用组件开发 | 本章节介绍了如何使用FA模型的PageAbility、ServiceAbility、DataAbility以及服务卡片进行应用开发。 | 应用/组件级配置 PageAbility开发指导 ServiceAbility开发指导 DataAbility开发指导 服务卡片开发指导 FA模型的Context 信息传递载体Want  |
| 了解进程模型 | 本章节介绍了FA模型的进程模型以及几种常用的进程间通信方式。 | 进程模型概述 |
| 了解线程模型 | 本章节介绍了FA模型的线程模型以及几种常用的线程间通信方式。 | 线程模型概述 |
| 应用配置文件 | 本章节介绍FA模型中应用配置文件的开发要求。 | FA模型应用配置文件 |
应用/组件级配置
PageAbility开发指导
ServiceAbility开发指导
DataAbility开发指导
服务卡片开发指导
FA模型的Context
信息传递载体Want

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/fa-model-application-components-V14
爬取时间: 2025-04-27 22:21:53
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/application-component-configuration-fa-V14
爬取时间: 2025-04-27 22:22:07
来源: Huawei Developer
开发者在开发应用时，需要配置应用的一些标签，例如应用的Bundle名称、图标等标识特征的属性。这一章节描述了开发者在开发应用时需要配置的一些关键标签。
应用包名配置
应用包名需在config.json文件中app标签下配置bundleName字段，该字段用于指定应用的包名，需保证唯一性。包名是由字母、数字、下划线（_）和点号（.）组成的字符串，必须以字母开头。支持的字符串长度为7~127字节。包名通常采用反向域名形式表示（例如，"com.example.myapplication"）。建议第一级为域名后缀"com"，第二级为厂商/个人名，也可以采用多级。应用名称配置可以参考app标签说明。
图标和标签配置
图标和标签通常一起配置，可以分为应用图标、应用标签和入口图标、入口标签。
应用图标和标签通常用于标识整个应用，可以在标识应用的界面使用该类型图标和标签。比如：
入口图标和标签是应用安装完成后可以在设备桌面上显示出来的。入口图标是以Page类型的Ability为粒度，支持同一个应用存在一个入口图标和入口标签（存在多个入口Ability时，仅entry类型HAP中的mainAbility会生效），点击后进入对应的Ability界面。比如：
应用图标和标签配置
FA模型不支持直接配置应用图标和标签，会以符合规则的PageAbility的图标和标签作为应用图标和标签。存在多个时，则取位置靠前的Ability的icon和label作为应用的icon和label。
入口图标和标签配置
入口图标和标签配置方法
FA模型的入口图标和标签是Page类型的Ability配置的icon和label。
PageAbility的图标和标签配置请参见PageAbility组件配置。需在config.json文件的abilities标签下做如下配置：
如果在该PageAbility的skills属性中，actions的取值包含 "action.system.home"，entities取值中包含"entity.system.home"，则该Ability的icon和label将同时作为应用的icon和label。如果存在多个符合条件的Ability，则取位置靠前的Ability的icon和label作为应用的icon和label。图标和标签配置可以参考abilities标签说明。
```json
{
...
"module": {
...
"abilities": [
{
"skills": [
{
"entities": [
"entity.system.home"
],
"actions": [
"action.system.home"
]
}
],
"orientation": "unspecified",
"formsEnabled": false,
"name": ".MainAbility",
"srcLanguage": "ets",
"srcPath": "MainAbility",
"icon": "$media:icon",
"description": "$string:MainAbility_desc",
"label": "$string:MainAbility_label",
"type": "page",
"visible": true,
"launchType": "singleton"
},
...
]
...
}
}
```
入口图标和标签管控规则
系统对无图标应用实施严格管控，防止一些恶意应用故意配置无入口图标，导致用户找不到软件所在的位置，无法操作卸载应用，在一定程度上保证用户终端设备的安全。
如果应用确需隐藏入口图标，需要配置AllowAppDesktopIconHide应用特权。详细的入口图标及入口标签的显示规则如下。
-  HAP中包含PageAbility
-  HAP中不包含PageAbility
应用版本声明配置
应用版本声明配置需在config.json中的app标签下配置version字段，以说明应用当前的版本号和版本名称以及应用能够兼容的最低历史版本号。应用版本配置说明可以参考version对象内部结构。
Module支持的设备类型配置
Module支持的设备类型需要在config.json文件中配置deviceType字段，如果deviceType标签中添加了某种设备，则表明当前的module支持在该设备上运行。具体的deviceType配置规则可以参考deviceType标签。
组件权限申请配置
组件权限申请配置需在config.json中的module标签下配置reqPermissions字段。来声明需要申请权限的名称，申请权限的原因以及权限使用的场景。组件权限申请可以参考reqPermissions权限申请。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pageability-V14
爬取时间: 2025-04-27 22:22:20
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pageability-overview-V14
爬取时间: 2025-04-27 22:22:33
来源: Huawei Developer
PageAbility是包含UI、提供展示UI能力的应用组件，主要用于与用户交互。
开发者通过DevEco Studio开发平台创建PageAbility时，DevEco Studio会自动创建相关模板代码。PageAbility相关能力通过单独的featureAbility实现，生命周期相关回调则通过app.js/app.ets中各个回调函数实现。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pageability-configuration-V14
爬取时间: 2025-04-27 22:22:47
来源: Huawei Developer
PageAbility的相关配置在config.json配置文件的"module"对象的"abilities"对象中，"icon"属性表示Ability图标资源文件的索引，"lable"属性表示Ability对用户显示的名称，"skills"属性表示Ability能够接收的want的特征。
表1PageAbility部分配置项说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| icon | 表示Ability图标资源文件的索引。取值示例：$media:ability_icon。如果在该Ability的skills属性中，actions的取值包含 "action.system.home"，entities取值中包含"entity.system.home"，则该Ability的icon将同时作为应用的icon。如果存在多个符合条件的Ability，则取位置靠前的Ability的icon作为应用的icon。 说明：应用的"icon"和"label"是用户可感知配置项，需要区别于当前所有已有的应用"icon"或"label"（至少有一个不同）。  | 字符串 | 可缺省，缺省值为空。 |
| label | 表示Ability对用户显示的名称。取值可以是Ability名称，也可以是对该名称的资源索引，以支持多语言。如果在该Ability的skills属性中，actions的取值包含 "action.system.home"，entities取值中包含"entity.system.home"，则该Ability的label将同时作为应用的label。如果存在多个符合条件的Ability，则取位置靠前的Ability的label作为应用的label。 说明： 应用的"icon"和"label"是用户可感知配置项，需要区别于当前所有已有的应用"icon"或"label"（至少有一个不同）。该标签为资源文件中定义的字符串的引用，或以"{}"包括的字符串。该标签最大长度为255字节。  | 字符串 | 可缺省，缺省值为空。 |
| skills | 表示Ability能够接收的want的特征。 | 对象数组 | 可缺省，缺省值为空。 |
表示Ability图标资源文件的索引。取值示例：$media:ability_icon。如果在该Ability的skills属性中，actions的取值包含 "action.system.home"，entities取值中包含"entity.system.home"，则该Ability的icon将同时作为应用的icon。如果存在多个符合条件的Ability，则取位置靠前的Ability的icon作为应用的icon。
说明：应用的"icon"和"label"是用户可感知配置项，需要区别于当前所有已有的应用"icon"或"label"（至少有一个不同）。
表示Ability对用户显示的名称。取值可以是Ability名称，也可以是对该名称的资源索引，以支持多语言。如果在该Ability的skills属性中，actions的取值包含 "action.system.home"，entities取值中包含"entity.system.home"，则该Ability的label将同时作为应用的label。如果存在多个符合条件的Ability，则取位置靠前的Ability的label作为应用的label。
说明： 应用的"icon"和"label"是用户可感知配置项，需要区别于当前所有已有的应用"icon"或"label"（至少有一个不同）。该标签为资源文件中定义的字符串的引用，或以"{}"包括的字符串。该标签最大长度为255字节。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pageability-lifecycle-V14
爬取时间: 2025-04-27 22:23:00
来源: Huawei Developer
PageAbility生命周期是PageAbility被调度到INACTIVE、ACTIVE、BACKGROUND等各个状态的统称。PageAbility生命周期流转及状态说明见如下图1、表1所示。
图1PageAbility生命周期流转
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170223.15303907466969416484530649807350:50001231000000:2800:2CB6A8395887AF6780F0F69FEF0B31556EF9BC6B01462E263B1CB61F8DC26862.png)
表1PageAbility生命周期状态说明
| 生命周期状态 | 生命周期状态说明 |
| --- | --- |
| UNINITIALIZED | 未初始状态，为临时状态，PageAbility被创建后会由UNINITIALIZED状态进入INITIAL状态。 |
| INITIAL | 初始化状态，也表示停止状态，表示当前PageAbility未运行，PageAbility被启动后由INITIAL态进入INACTIVE状态。 |
| INACTIVE | 失去焦点状态，表示当前窗口已显示但是无焦点状态。 |
| ACTIVE | 前台激活状态，表示当前窗口已显示，并获取焦点。 |
| BACKGROUND | 后台状态，表示当前PageAbility退到后台，PageAbility在被销毁后由BACKGROUND状态进入INITIAL状态，或者重新被激活后由BACKGROUND状态进入ACTIVE状态。 |
应用开发者可以在app.js/app.ets中实现生命周期相关回调函数，PageAbility生命周期相关回调函数见下表。
表2PageAbility生命周期回调接口说明
| 接口名 | 接口描述 |
| --- | --- |
| onCreate() | Ability第一次启动创建Ability时调用onCreate方法，开发者可以在该方法里做一些应用初始化工作。 |
| onDestroy() | 应用退出，销毁Ability对象前调用onDestroy方法，开发者可以在该方法里做一些回收资源、清空缓存等应用退出前的准备工作。 |
| onActive() | Ability切换到前台，并且已经获取焦点时调用onActive方法。 |
| onInactive() | Ability失去焦点时调用onInactive方法，Ability在进入后台状态时会先失去焦点，再进入后台。 |
| onShow() | Ability由后台不可见状态切换到前台可见状态调用onShow方法，此时用户在屏幕可以看到该Ability。 |
| onHide() | Ability由前台切换到后台不可见状态时调用onHide方法，此时用户在屏幕看不到该Ability。 |
PageAbility生命周期回调与生命周期状态的关系如下图所示。
图2PageAbility生命周期回调与生命周期状态的关系
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170223.74781572220046224371880470386411:50001231000000:2800:8B9906F5DBBC3BA3C4522981ED46C93D69FA33D9493F537C1019EF3ABAD7A5CF.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pageability-launch-type-V14
爬取时间: 2025-04-27 22:23:14
来源: Huawei Developer
启动模式对应PageAbility被启动时的行为，支持单实例模式、多实例模式两种启动模式。
表1PageAbility的启动模式
| 启动模式 | 描述 | 说明 |
| --- | --- | --- |
| singleton | 单实例模式 | 每次调用startAbility方法时，如果应用进程中该类型的Ability实例已经存在，则复用已有的实例，系统中只存在唯一一个实例。表现为在最近任务列表中只有一个Ability实例。 典型场景：当用户打开视频播放应用并观看视频，回到桌面后，再次打开视频播放应用，应用仍为回到桌面之前正在观看的视频。  |
| multiton | 多实例模式 | 缺省启动模式。每次调用startAbility方法时，都会在应用进程中创建一个新的Ability实例。表现为在最近任务列表中可以看到有多个该类型的Ability实例。 典型场景：当用户打开文档应用，选择新建文档的时候，每次点击新建文档，都会创建一个新的文档任务，在最近任务列表中可以看到多个新建的文档任务。  |
每次调用startAbility方法时，如果应用进程中该类型的Ability实例已经存在，则复用已有的实例，系统中只存在唯一一个实例。表现为在最近任务列表中只有一个Ability实例。
典型场景：当用户打开视频播放应用并观看视频，回到桌面后，再次打开视频播放应用，应用仍为回到桌面之前正在观看的视频。
缺省启动模式。每次调用startAbility方法时，都会在应用进程中创建一个新的Ability实例。表现为在最近任务列表中可以看到有多个该类型的Ability实例。
典型场景：当用户打开文档应用，选择新建文档的时候，每次点击新建文档，都会创建一个新的文档任务，在最近任务列表中可以看到多个新建的文档任务。
应用开发者可在config.json配置文件中通过“launchType”配置启动模式。示例如下：
```json
{
"module": {
...
"abilities": [
{
// singleton: 单实例模式
// multiton: 多实例模式
"launchType": "multiton",
...
}
]
}
}
```
启动PageAbility时，对于多实例模式启动，以及单实例模式进行首次启动时，PageAbility生命周期回调均会被触发。单实例非首次启动时不会再触发onCreate()接口，而是触发onNewWant()，onNewWant()的说明如下表2所示。
表2单实例启动模式特有的回调函数说明
| 接口名 | 接口描述 |
| --- | --- |
| onNewWant(want: Want) | 单实例启动模式，PageAbility非首次启动时调用onNewWant方法，开发者可以在该方法中获取want，进而根据want做进一步处理。例如，单实例PageAbility迁移场景，指定页面拉起PageAbility场景。 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/create-pageability-V14
爬取时间: 2025-04-27 22:23:27
来源: Huawei Developer
通过DevEco Studio开发平台创建PageAbility时，DevEco Studio会在app.js/app.ets中默认生成onCreate()和onDestroy()方法，其他方法需要开发者自行实现。接口说明参见前述章节，创建PageAbility示例如下：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import hilog from '@ohos.hilog';
const TAG: string = 'MainAbility';
const domain: number = 0xFF00;
class MainAbility {
onCreate() {
// 获取context并调用相关方法
let context = featureAbility.getContext();
context.getBundleName((data, bundleName) => {
hilog.info(domain, TAG, 'ability bundleName:' ,bundleName);
});
hilog.info(domain, TAG, 'Application onCreate');
}
onDestroy() {
hilog.info(domain, TAG, 'Application onDestroy');
}
onShow(): void {
hilog.info(domain, TAG, 'Application onShow');
}
onHide(): void {
hilog.info(domain, TAG, 'Application onHide');
}
onActive(): void {
hilog.info(domain, TAG, 'Application onActive');
}
onInactive(): void {
hilog.info(domain, TAG, 'Application onInactive');
}
onNewWant() {
hilog.info(domain, TAG, 'Application onNewWant');
}
}
export default new MainAbility();
```
PageAbility创建成功后，其abilities相关的配置项在config.json中体现，一个名字为EntryAbility的config.json配置文件示例如下：
```json
{
...
"module": {
...
"abilities": [
{
"skills": [
{
"entities": [
"entity.system.home"
],
"actions": [
"action.system.home"
]
}
],
"orientation": "unspecified",
"formsEnabled": false,
"name": ".MainAbility",
"srcLanguage": "ets",
"srcPath": "MainAbility",
"icon": "$media:icon",
"description": "$string:MainAbility_desc",
"label": "$string:MainAbility_label",
"type": "page",
"visible": true,
"launchType": "singleton"
},
...
]
...
}
}
```
FA模型中，可以通过featureAbility的getContext接口获取应用上下文，进而使用上下文提供的能力。
表1featureAbility接口说明
| 接口名 | 接口描述 |
| --- | --- |
| getContext() | 获取应用上下文。 |
通过getContext获取应用上下文并获取分布式目录的示例如下：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import fs from '@ohos.file.fs';
import promptAction from '@ohos.promptAction';
import hilog from '@ohos.hilog';
const TAG: string = 'PagePageAbilityFirst';
const domain: number = 0xFF00;
```
```typescript
(async (): Promise<void> => {
let dir: string;
try {
hilog.info(domain, TAG, 'Begin to getOrCreateDistributedDir');
dir = await featureAbility.getContext().getOrCreateDistributedDir();
promptAction.showToast({
message: dir
});
hilog.info(domain, TAG, 'distribute dir is ' + dir);
let fd: number;
let path = dir + '/a.txt';
fd = fs.openSync(path, fs.OpenMode.READ_WRITE).fd;
fs.close(fd);
} catch (error) {
hilog.error(domain, TAG, 'getOrCreateDistributedDir failed with : ' + error);
}
})()
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-local-pageability-V14
爬取时间: 2025-04-27 22:23:40
来源: Huawei Developer
PageAbility相关的能力通过featureAbility提供，启动本地Ability通过featureAbility中的startAbility接口实现。
表1featureAbility接口说明
| 接口名 | 接口描述 |
| --- | --- |
| startAbility(parameter: StartAbilityParameter) | 启动Ability。 |
| startAbilityForResult(parameter: StartAbilityParameter) | 启动Ability，并在该Ability被销毁时返回执行结果。 |
如下示例通过startAbility显式启动PageAbility。启动Ability的参数包含want，关于want的说明详见对象间信息传递载体Want，相应的，隐式启动与显式启动也不在此赘述。
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import Want from '@ohos.app.ability.Want';
import hilog from '@ohos.hilog';
const TAG: string = 'PagePageAbilityFirst';
const domain: number = 0xFF00;
```
```typescript
(async (): Promise<void> => {
try {
hilog.info(domain, TAG, 'Begin to start ability');
let want: Want = {
bundleName: 'com.samples.famodelabilitydevelop',
moduleName: 'entry',
abilityName: 'com.samples.famodelabilitydevelop.PageAbilitySingleton'
};
await featureAbility.startAbility({ want: want });
hilog.info(domain, TAG, `Start ability succeed`);
}
catch (error) {
hilog.error(domain, TAG, 'Start ability failed with ' + error);
}
})()
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/stop-pageability-V14
爬取时间: 2025-04-27 22:23:53
来源: Huawei Developer
停止PageAbility通过featureAbility中的terminateSelf接口实现。
表1featureAbility接口说明
| 接口名 | 接口描述 |
| --- | --- |
| terminateSelf() | 停止Ability。 |
| terminateSelfWithResult(parameter: AbilityResult) | 设置该PageAbility停止时返回给调用者的结果及数据并停止Ability。 |
如下示例展示了停止Ability的方法。
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import hilog from '@ohos.hilog';
const TAG: string = 'PagePageAbilityFirst';
const domain: number = 0xFF00;
```
```typescript
//...
(async (): Promise<void> => {
try {
hilog.info(domain, TAG, 'Begin to terminateSelf');
await featureAbility.terminateSelf();
hilog.info(domain, TAG, 'terminateSelf succeed');
} catch (error) {
hilog.error(domain, TAG, 'terminateSelf failed with ' + error);
}
})()
//...
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-page-V14
爬取时间: 2025-04-27 22:24:08
来源: Huawei Developer
当PageAbility的启动模式设置为单例时（具体设置方法和典型场景示例见PageAbility的启动模式，缺省情况下是单实例模式），若PageAbility已被拉起，再次启动PageAbility会触发onNewWant回调（即非首次拉起）。应用开发者可以通过want传递启动参数，例如开发者希望指定页面启动PageAbility，可以通过want中的parameters参数传递pages信息，具体示例代码如下：
调用方PageAbility的app.ets中或者page中，使用startAbility再次拉起PageAbility，通过want中的uri参数传递页面信息：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import Want from '@ohos.app.ability.Want';
import hilog from '@ohos.hilog';
const TAG: string = 'PagePageAbilityFirst';
const domain: number = 0xFF00;
```
```typescript
(async (): Promise<void> => {
let wantInfo: Want = {
bundleName: 'com.samples.famodelabilitydevelop',
abilityName: 'com.samples.famodelabilitydevelop.PageAbilitySingleton',
parameters: { page: 'pages/second' }
};
featureAbility.startAbility({ want: wantInfo }).then((data) => {
hilog.debug(domain, TAG, `restartAbility success : ${data}`);
});
})()
```
在目标端PageAbility的onNewWant回调中获取包含页面信息的want参数：
```typescript
// GlobalContext.ts 构造单例对象
export class GlobalContext {
private constructor() {
}
private static instance: GlobalContext;
private _objects = new Map<string, Object>();
public static getContext(): GlobalContext {
if (!GlobalContext.instance) {
GlobalContext.instance = new GlobalContext();
}
return GlobalContext.instance;
}
getObject(value: string): Object | undefined {
return this._objects.get(value);
}
setObject(key: string, objectClass: Object): void {
this._objects.set(key, objectClass);
}
}
```
```typescript
import Want from '@ohos.app.ability.Want';
import featureAbility from '@ohos.ability.featureAbility';
import { GlobalContext } from '../utils/GlobalContext';
class PageAbilitySingleton {
onNewWant(want: Want) {
featureAbility.getWant().then((want) => {
GlobalContext.getContext().setObject('newWant', want);
})
}
}
export default new PageAbilitySingleton();
```
在目标端页面的自定义组件中获取包含页面信息的want参数并根据uri做路由处理：
```typescript
import Want from '@ohos.app.ability.Want';
import router from '@ohos.router';
import { GlobalContext } from '../../utils/GlobalContext';
@Entry
@Component
struct First {
onPageShow() {
let newWant = GlobalContext.getContext().getObject('newWant') as Want;
if (newWant) {
if (newWant.parameters) {
if (newWant.parameters.page) {
router.pushUrl({ url: newWant.parameters.page as string});
GlobalContext.getContext().setObject("newWant", undefined)
}
}
}
}
build() {
Column() {
Row() {
Text('singleton_first_title')
.fontSize(24)
.fontWeight(FontWeight.Bold)
.textAlign(TextAlign.Start)
.margin({ top: 12, bottom: 11, right: 24, left: 24 })
}
.width('100%')
.height(56)
.justifyContent(FlexAlign.Start)
Image('pic_empty')
.width(120)
.height(120)
.margin({ top: 224 })
Text('no_content')
.fontSize(14)
.margin({ top: 8, bottom: 317, right: 152, left: 152 })
.fontColor('text_color')
.opacity(0.4)
}
.width('100%')
.height('100%')
.backgroundColor('backGrounding')
}
}
```
当PageAbility的启动模式设置为多实例模式或为首次启动单例模式的PageAbility时（具体设置方法和典型场景示例见PageAbility的启动模式），在调用方PageAbility中，通过want中的parameters参数传递要启动的指定页面的pages信息，调用startAbility()方法启动PageAbility。被调用方可以在onCreate中使用featureAbility的getWant方法获取want，再通过调用router.pushUrl实现启动指定页面。
调用方的页面中实现按钮点击触发startAbility方法启动目标端PageAbility，startAbility方法的入参want中携带指定页面信息，示例代码如下：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import Want from '@ohos.app.ability.Want';
import { BusinessError } from '@ohos.base';
import fs from '@ohos.file.fs';
import promptAction from '@ohos.promptAction';
import worker from '@ohos.worker';
import hilog from '@ohos.hilog';
const TAG: string = 'PagePageAbilityFirst';
const domain: number = 0xFF00;
@Entry
@Component
struct PagePageAbilityFirst {
build() {
Column() {
//...
List({ initialIndex: 0 }) {
//...
ListItem() {
Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
//...
}
.onClick(() => {
let want: Want = {
bundleName: 'com.samples.famodelabilitydevelop',
abilityName: 'com.samples.famodelabilitydevelop.PageAbilityStandard',
parameters: { page: 'pages/first' }
};
featureAbility.startAbility({ want: want }).then((data) => {
hilog.info(domain, TAG, `startAbility finish:${data}`);
}).catch((err: BusinessError) => {
hilog.info(domain, TAG, `startAbility failed errcode:${err.code}`);
})
})
}
//...
ListItem() {
Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
//...
}
.onClick(() => {
let want: Want = {
bundleName: 'com.samples.famodelabilitydevelop',
abilityName: 'com.samples.famodelabilitydevelop.PageAbilityStandard',
parameters: { page: 'pages/second' }
};
featureAbility.startAbility({ want: want }).then((data) => {
hilog.info(domain, TAG, `startAbility finish:${data}`);
}).catch((err: BusinessError) => {
hilog.info(domain, TAG, `startAbility failed errcode:${err.code}`);
})
})
}
//...
}
//...
}
//...
}
}
```
目标端PageAbility的onCreate生命周期回调中通过featureAbility的getWant方法获取want，并对参数进行解析，实现指定页面拉起：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import router from '@ohos.router';
class PageAbilityStandard {
onCreate() {
featureAbility.getWant().then((want) => {
if (want.parameters) {
if (want.parameters.page) {
router.pushUrl({ url: want.parameters.page as string });
}
}
})
}
}
export default new PageAbilityStandard();
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/window-properties-V14
爬取时间: 2025-04-27 22:24:24
来源: Huawei Developer
具体获取窗口实例、设置窗口属性的接口描述及示例见接口文档。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/request-permissions-V14
爬取时间: 2025-04-27 22:24:37
来源: Huawei Developer
应用需要获取用户的隐私信息或使用系统能力时，例如获取位置信息、使用相机拍摄照片或录制视频等，需要向用户申请授权。
在开发过程中，首先需要明确涉及的敏感权限并在config.json中声明需要的权限，同时通过接口requestPermissionsFromUser以动态弹窗的方式向用户申请授权。
在config.json声明需要的权限，在module下添加"reqPermissions"，并写入对应权限。
例如申请访问日历权限：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/redirection-rules-V14
爬取时间: 2025-04-27 22:24:51
来源: Huawei Developer
一般情况下，应用中的界面跳转由用户触发，应用本身通过startAbility启动跳转其他界面。
PageAbility作为可见Ability，可以通过startAbility启动有界面的且对外可见的Ability。
应用可通过在config.json中设置"abilities"中的"visible"属性设置Ability是否可由其他应用的组件启动，"visible"属性的具体参数和意义如下表所示。
表1visible属性说明
| 属性名称 | 描述 | 是否可缺省 |
| --- | --- | --- |
| visible | 表示Ability是否可以被其他应用调用。 true：该Ability可以被任何应用调用。 false：该Ability只能被同一应用的其他组件调用。  | 可缺省，缺省时默认属性值为"false"。 |
表示Ability是否可以被其他应用调用。
true：该Ability可以被任何应用调用。
false：该Ability只能被同一应用的其他组件调用。
如果需设置当前Ability可由任何应用访问，对应config.json文件的示例代码如下所示：
```json
{
"module": {
...
"abilities": [
{
"visible": "true",
...
}
]
}
}
```
如果应用中的Ability包含skills过滤器，建议此属性设置为"true"，以允许其他应用通过隐式调用启动该Ability。如果此属性设为"false"，其他应用尝试启动该Ability时系统会返回PERMISSION_DENIED。这种情况下系统应用可以通过申请START_INVISIBLE_ABILITY权限启动visible为false的组件，例如系统桌面、语音助手、搜索助手等。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/serviceability-V14
爬取时间: 2025-04-27 22:25:05
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/serviceability-overview-V14
爬取时间: 2025-04-27 22:25:19
来源: Huawei Developer
ServiceAbility，即"基于Service模板的Ability"，主要用于后台运行任务（如执行音乐播放、文件下载等），不提供用户交互界面。ServiceAbility可由其他应用或PageAbility启动，即使用户切换到其他应用，ServiceAbility仍将在后台继续运行。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/serviceability-configuration-V14
爬取时间: 2025-04-27 22:25:33
来源: Huawei Developer
与PageAbility类似，ServiceAbility的相关配置在config.json配置文件的"module"对象的"abilities"对象中，与PageAbility的区别在于"type"属性及"backgroundModes"属性。
表1ServiceAbility部分配置项说明
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| type | 表示Ability的类型。取值为"service"时表示该Ability是基于Service模板开发的Ability。 | 字符串 | 否 |
| backgroundModes | 表示后台服务的类型，可以为一个服务配置多个后台服务类型。该标签仅适用于service类型的Ability。取值范围如下： dataTransfer：通过网络/对端设备进行数据下载、备份、分享、传输等业务。 audioPlayback：音频输出业务。 audioRecording：音频输入业务。 pictureInPicture：画中画、小窗口播放视频业务。 voip：音视频电话、VOIP业务。 location：定位、导航业务。 bluetoothInteraction：蓝牙扫描、连接、传输业务。 wifiInteraction：WLAN扫描、连接、传输业务。 screenFetch：录屏、截屏业务。 multiDeviceConnection：多设备互联业务。 | 字符串数组 | 可缺省，缺省值为空。 |
表示后台服务的类型，可以为一个服务配置多个后台服务类型。该标签仅适用于service类型的Ability。取值范围如下：
dataTransfer：通过网络/对端设备进行数据下载、备份、分享、传输等业务。
audioPlayback：音频输出业务。
audioRecording：音频输入业务。
pictureInPicture：画中画、小窗口播放视频业务。
voip：音视频电话、VOIP业务。
location：定位、导航业务。
bluetoothInteraction：蓝牙扫描、连接、传输业务。
wifiInteraction：WLAN扫描、连接、传输业务。
screenFetch：录屏、截屏业务。
multiDeviceConnection：多设备互联业务。
ServiceAbility支持的配置项及详细说明详见module对象内部结构。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/serviceability-lifecycle-V14
爬取时间: 2025-04-27 22:25:46
来源: Huawei Developer
开发者可以根据业务场景实现service.js/service.ets中的生命周期相关接口。ServiceAbility生命周期接口说明见下表。
表1ServiceAbility生命周期接口说明
| 接口名 | 描述 |
| --- | --- |
| onStart(): void | 该方法在创建ServiceAbility的时候调用，用于Service的初始化，在ServiceAbility的整个生命周期只会调用一次。 |
| onCommand(want: Want, startId: number): void | 在Service创建完成之后调用，该方法在客户端每次启动该Service时都会调用，开发者可以在该方法中做一些调用统计、初始化类的操作。 |
| onConnect(want: Want): rpc.RemoteObject | 在连接ServiceAbility时调用。 |
| onDisconnect(want: Want): void | 在与已连接的ServiceAbility断开连接时调用。 |
| onStop(): void | 在ServiceAbility销毁时调用。开发者应通过实现此方法来清理资源，如关闭线程、注册的侦听器等。 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/create-serviceability-V14
爬取时间: 2025-04-27 22:26:00
来源: Huawei Developer
1.  创建ServiceAbility。 通过DevEco Studio开发平台创建ServiceAbility时，DevEco Studio会默认生成onStart、onStop、onCommand方法，其他方法需要开发者自行实现，接口说明参见前述章节。开发者也可以添加其他Ability请求与ServiceAbility交互时的处理方法，示例如下：
```typescript
import { Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[Sample_FAModelAbilityDevelop]';
const domain: number = 0xFF00;
class FirstServiceAbilityStub extends rpc.RemoteObject {
constructor(des: Object) {
if (typeof des === 'string') {
super(des);
} else {
return;
}
}
onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
hilog.info(domain, TAG, 'ServiceAbility onRemoteRequest called');
if (code === 1) {
let string = data.readString();
hilog.info(domain, TAG, `ServiceAbility string=${string}`);
let result = Array.from(string).sort().join('');
hilog.info(domain, TAG, `ServiceAbility result=${result}`);
reply.writeString(result);
} else {
hilog.info(domain, TAG, 'ServiceAbility unknown request code');
}
return true;
}
}
class ServiceAbility {
onStart(): void {
hilog.info(domain, TAG, 'ServiceAbility onStart');
}
onStop(): void {
hilog.info(domain, TAG, 'ServiceAbility onStop');
}
onCommand(want: Want, startId: number): void {
hilog.info(domain, TAG, 'ServiceAbility onCommand');
}
onConnect(want: Want): rpc.RemoteObject {
hilog.info(domain, TAG, 'ServiceAbility onDisconnect' + want);
return new FirstServiceAbilityStub('test');
}
onDisconnect(want: Want): void {
hilog.info(domain, TAG, 'ServiceAbility onDisconnect' + want);
}
}
export default new ServiceAbility();
```
2.  注册ServiceAbility。 ServiceAbility需要在应用配置文件config.json中进行注册，注册类型type需要设置为service。"visible"属性表示ServiceAbility是否可以被其他应用调用，true表示可以被其他应用调用，false表示不能被其他应用调用（仅应用内可以调用）。若ServiceAbility需要被其他应用调用，注册ServiceAbility时需要设置"visible"为true，同时需要设置支持关联启动。ServiceAbility的启动规则详见组件启动规则章节。
```json
{
...
"module": {
...
"abilities": [
...
{
"name": ".ServiceAbility",
"srcLanguage": "ets",
"srcPath": "ServiceAbility",
"icon": "$media:icon",
"description": "$string:ServiceAbility_desc",
"type": "service",
"visible": true
},
...
]
...
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-serviceability-V14
爬取时间: 2025-04-27 22:26:14
来源: Huawei Developer
ServiceAbility的启动与其他Ability并无区别，应用开发者可以在PageAbility中通过featureAbility的startAbility接口拉起ServiceAbility，在ServiceAbility中通过particleAbility的startAbility接口拉起ServiceAbility。ServiceAbility的启动规则详见组件启动规则章节。
如下示例展示了在PageAbility中通过startAbility启动bundleName为"com.example.myapplication"，abilityName为"ServiceAbility"的ServiceAbility的方法。启动FA模型的ServiceAbility时，需要在abilityName前拼接bundleName字符串。
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import Want from '@ohos.app.ability.Want';
import promptAction from '@ohos.promptAction';
import hilog from '@ohos.hilog';
const TAG: string = 'PageServiceAbility';
const domain: number = 0xFF00;
@Entry
@Component
struct PageServiceAbility {
async startServiceAbility(): Promise<void> {
try {
hilog.info(domain, TAG, 'Begin to start ability');
let want: Want = {
bundleName: 'com.samples.famodelabilitydevelop',
abilityName: 'com.samples.famodelabilitydevelop.ServiceAbility'
};
await featureAbility.startAbility({ want });
promptAction.showToast({
message: 'start_service_success_toast'
});
hilog.info(domain, TAG, `Start ability succeed`);
} catch (error) {
hilog.error(domain, TAG, 'Start ability failed with ' + error);
}
}
build() {
// ...
}
}
```
执行上述代码后，Ability将通过startAbility()方法来启动ServiceAbility。
-  如果ServiceAbility尚未运行，则系统会先调用onStart()来初始化ServiceAbility，再回调Service的onCommand()方法来启动ServiceAbility。
-  如果ServiceAbility正在运行，则系统会直接回调ServiceAbility的onCommand()方法来启动ServiceAbility。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/connect-serviceability-V14
爬取时间: 2025-04-27 22:26:28
来源: Huawei Developer
如果ServiceAbility需要与PageAbility或其他应用的ServiceAbility进行交互，则须创建用于连接的Connection。ServiceAbility支持其他Ability通过connectAbility()方法与其进行连接。PageAbility的connectAbility()方法定义在featureAbility中，ServiceAbility的connectAbility()方法定义在particleAbility中。连接ServiceAbility的规则详见组件启动规则章节。在使用connectAbility()处理回调时，需要传入目标Service的Want与IAbilityConnection的实例。IAbilityConnection提供了以下方法供开发者实现。
表1IAbilityConnection接口说明
| 接口名 | 描述 |
| --- | --- |
| onConnect() | 用于处理连接Service成功的回调。 |
| onDisconnect() | 用来处理Service异常死亡的回调。 |
| onFailed() | 用来处理连接Service失败的回调。 |
PageAbility创建连接本地ServiceAbility回调实例的代码以及连接本地ServiceAbility的示例代码如下：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import common from '@ohos.app.ability.common';
import Want from '@ohos.app.ability.Want';
import promptAction from '@ohos.promptAction';
import rpc from '@ohos.rpc';
import hilog from '@ohos.hilog';
```
```typescript
const TAG: string = 'PageServiceAbility';
const domain: number = 0xFF00;
@Entry
@Component
struct PageServiceAbility {
//...
build() {
Column() {
//...
List({ initialIndex: 0 }) {
ListItem() {
Row() {
//...
}
.onClick(() => {
let option: common.ConnectOptions = {
onConnect: (element, proxy) => {
hilog.info(domain, TAG, `onConnectLocalService onConnectDone element:` + JSON.stringify(element));
if (proxy === null) {
promptAction.showToast({
message: 'connect_service_failed_toast'
});
return;
}
let data = rpc.MessageParcel.create();
let reply = rpc.MessageParcel.create();
let option = new rpc.MessageOption();
data.writeInterfaceToken('connect.test.token');
proxy.sendRequest(0, data, reply, option);
promptAction.showToast({
message: 'connect_service_success_toast'
});
},
onDisconnect: (element) => {
hilog.info(domain, TAG, `onConnectLocalService onDisconnectDone element:${element}`);
promptAction.showToast({
message: 'disconnect_service_success_toast'
});
},
onFailed: (code) => {
hilog.info(domain, TAG, `onConnectLocalService onFailed errCode:${code}`);
promptAction.showToast({
message: 'connect_service_failed_toast'
});
}
};
let request: Want = {
bundleName: 'com.samples.famodelabilitydevelop',
abilityName: 'com.samples.famodelabilitydevelop.ServiceAbility',
};
let connId = featureAbility.connectAbility(request, option);
hilog.info(domain, TAG, `onConnectLocalService onFailed errCode:${connId}`);
})
}
//...
}
//...
}
//...
}
}
```
同时，Service侧也需要在onConnect()时返回IRemoteObject，从而定义与Service进行通信的接口。onConnect()需要返回一个IRemoteObject对象。系统提供了IRemoteObject的默认实现，开发者可以通过继承rpc.RemoteObject来创建自定义的实现类。
Service侧把自身的实例返回给调用侧的示例代码如下：
```typescript
import type Want from '@ohos.app.ability.Want';
import rpc from '@ohos.rpc';
import hilog from '@ohos.hilog';
const TAG: string = '[Sample_FAModelAbilityDevelop]';
const domain: number = 0xFF00;
class FirstServiceAbilityStub extends rpc.RemoteObject {
constructor(des: Object) {
if (typeof des === 'string') {
super(des);
} else {
return;
}
}
onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
hilog.info(domain, TAG, 'ServiceAbility onRemoteRequest called');
if (code === 1) {
let string = data.readString();
hilog.info(domain, TAG, `ServiceAbility string=${string}`);
let result = Array.from(string).sort().join('');
hilog.info(domain, TAG, `ServiceAbility result=${result}`);
reply.writeString(result);
} else {
hilog.info(domain, TAG, 'ServiceAbility unknown request code');
}
return true;
}
}
//...
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/dataability-V14
爬取时间: 2025-04-27 22:26:43
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/dataability-overview-V14
爬取时间: 2025-04-27 22:26:57
来源: Huawei Developer
DataAbility，即"使用Data模板的Ability"，主要用于对外部提供统一的数据访问抽象，不提供用户交互界面。DataAbility可由PageAbility、ServiceAbility或其他应用启动，即使用户切换到其他应用，DataAbility仍将在后台继续运行。
使用DataAbility有助于应用管理其自身和其他应用存储数据的访问，并提供与其他应用共享数据的方法。DataAbility既可用于同设备不同应用的数据共享，也支持跨设备不同应用的数据共享。
数据的存放形式多样，可以是数据库，也可以是磁盘上的文件。DataAbility对外提供对数据的增、删、改、查，以及打开文件等接口，这些接口的具体实现由开发者提供。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/dataability-configuration-V14
爬取时间: 2025-04-27 22:27:11
来源: Huawei Developer
URI介绍
DataAbility的提供方和使用方都通过URI（Uniform Resource Identifier）来标识一个具体的数据，例如数据库中的某个表或磁盘上的某个文件。此处的URI仍基于URI通用标准，格式如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170224.04937034493543347301217457585139:50001231000000:2800:2A071ADC26EF5D22B583C4D480A00AA7E83B38ABC00C0828F53B9DEC047B1868.png)
-  scheme：协议方案名，固定为"dataability"，代表Data Ability所使用的协议类型。
-  authority：设备ID。如果为跨设备场景，则为目标设备的ID；如果为本地设备场景，则不需要填写。
-  path：资源的路径信息，代表特定资源的位置信息。
-  query：查询参数。
-  fragment：可以用于指示要访问的子资源。
URI示例：
-  跨设备场景：dataability://device_id/com.domainname.dataability.persondata/person/10
-  本地设备：dataability:///com.domainname.dataability.persondata/person/1
本地设备的"device_id"字段为空，因此在"dataability:"后面有三个"/"。
部分配置项介绍
与PageAbility类似，DataAbility的相关配置在config.json配置文件的"module"对象的"abilities"对象中，与PageAbility的区别在于"type"属性及"uri"属性。
表1DataAbility的部分配置项说明
| Json重要字段 | 备注说明 |
| --- | --- |
| "name" | Ability名称。 |
| "type" | UIAbility类型，DataAbility的类型为"data"。 |
| "uri" | 通信使用的URI。 |
| "visible" | 对其他应用是否可见，设置为true时，DataAbility才能与其他应用进行通信传输数据。 |
config.json配置样例
```json
"abilities": [
...
{
"name": ".DataAbility",
"srcLanguage": "ets",
"srcPath": "DataAbility",
"icon": "$media:icon",
"description": "$string:DataAbility_desc",
"type": "data",
"visible": true,
"uri": "dataability://com.samples.famodelabilitydevelop.DataAbility",
"readPermission": "ohos.permission.READ_CONTACTS",
"writePermission": "ohos.permission.WRITE_CONTACTS"
},
...
]
```
DataAbility支持的配置项及详细说明详见module对象内部结构。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/dataability-lifecycle-V14
爬取时间: 2025-04-27 22:27:25
来源: Huawei Developer
应用开发者可以根据业务场景实现data.js/data.ets中的生命周期相关接口。DataAbility生命周期接口说明见下表。
表1DataAbility相关生命周期API功能介绍
| 接口名 | 描述 |
| --- | --- |
| onInitialized?(info: AbilityInfo): void | 在Ability初始化调用，通过此回调方法执行RDB等初始化操作。 |
| update?(uri: string, valueBucket: rdb.ValuesBucket, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void | 更新数据库中的数据。 |
| query?(uri: string, columns: Array<string>, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<ResultSet>): void | 查询数据库中的数据。 |
| delete?(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void | 删除一条或多条数据。 |
| normalizeUri?(uri: string, callback: AsyncCallback<string>): void | 对URI进行规范化。一个规范化的URI可以支持跨设备使用、持久化、备份和还原等，当上下文改变时仍然可以引用到相同的数据项。 |
| batchInsert?(uri: string, valueBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback<number>): void | 向数据库中插入多条数据。 |
| denormalizeUri?(uri: string, callback: AsyncCallback<string>): void | 将一个由normalizeUri生产的规范化URI转换成非规范化的URI。 |
| insert?(uri: string, valueBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void | 向数据中插入一条数据。 |
| openFile?(uri: string, mode: string, callback: AsyncCallback<number>): void | 打开一个文件。 |
| getFileTypes?(uri: string, mimeTypeFilter: string, callback: AsyncCallback<Array<string>>): void | 获取文件的MIME类型。 |
| getType?(uri: string, callback: AsyncCallback<string>): void | 获取URI指定数据相匹配的MIME类型。 |
| executeBatch?(ops: Array<DataAbilityOperation>, callback: AsyncCallback<Array<DataAbilityResult>>): void | 批量操作数据库中的数据。 |
| call?(method: string, arg: string, extras: PacMap, callback: AsyncCallback<PacMap>): void | 自定义方法。 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/create-dataability-V14
爬取时间: 2025-04-27 22:27:39
来源: Huawei Developer
实现DataAbility中Insert、Query、Update、Delete接口的业务内容。保证能够满足数据库存储业务的基本需求。BatchInsert与ExecuteBatch接口已经在系统中实现遍历逻辑，依赖Insert、Query、Update、Delete接口逻辑，来实现数据的批量处理。
创建DataAbility的代码示例如下：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import type common from '@ohos.app.ability.common';
import type Want from '@ohos.app.ability.Want';
import type { AsyncCallback, BusinessError } from '@ohos.base';
import dataAbility from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';
import hilog from '@ohos.hilog';
let TABLE_NAME = 'book';
let STORE_CONFIG: rdb.StoreConfig = { name: 'book.db' };
let SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, introduction TEXT NOT NULL)';
let rdbStore: rdb.RdbStore | undefined = undefined;
const TAG: string = '[Sample_FAModelAbilityDevelop]';
const domain: number = 0xFF00;
class DataAbility {
onInitialized(want: Want): void {
hilog.info(domain, TAG, 'DataAbility onInitialized, abilityInfo:' + want.bundleName);
let context: common.BaseContext = { stageMode: featureAbility.getContext().stageMode };
rdb.getRdbStore(context, STORE_CONFIG, 1, (err, store) => {
hilog.info(domain, TAG, 'DataAbility getRdbStore callback');
store.executeSql(SQL_CREATE_TABLE, []);
rdbStore = store;
});
}
insert(uri: string, valueBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void {
hilog.info(domain, TAG, 'DataAbility insert start');
if (rdbStore) {
rdbStore.insert(TABLE_NAME, valueBucket, callback);
}
}
batchInsert(uri: string, valueBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback<number>): void {
hilog.info(domain, TAG, 'DataAbility batch insert start');
if (rdbStore) {
for (let i = 0; i < valueBuckets.length; i++) {
hilog.info(domain, TAG, 'DataAbility batch insert i=' + i);
if (i < valueBuckets.length - 1) {
rdbStore.insert(TABLE_NAME, valueBuckets[i], (err: BusinessError, num: number) => {
hilog.info(domain, TAG, 'DataAbility batch insert ret=' + num);
});
} else {
rdbStore.insert(TABLE_NAME, valueBuckets[i], callback);
}
}
}
}
query(uri: string, columns: Array<string>, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<rdb.ResultSet>): void {
hilog.info(domain, TAG, 'DataAbility query start');
let rdbPredicates = dataAbility.createRdbPredicates(TABLE_NAME, predicates);
if (rdbStore) {
rdbStore.query(rdbPredicates, columns, callback);
}
}
update(uri: string, valueBucket: rdb.ValuesBucket, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void {
hilog.info(domain, TAG, 'DataAbility update start');
let rdbPredicates = dataAbility.createRdbPredicates(TABLE_NAME, predicates);
if (rdbStore) {
rdbStore.update(valueBucket, rdbPredicates, callback);
}
}
delete(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void {
hilog.info(domain, TAG, 'DataAbility delete start');
let rdbPredicates = dataAbility.createRdbPredicates(TABLE_NAME, predicates);
if (rdbStore) {
rdbStore.delete(rdbPredicates, callback);
}
}
}
export default new DataAbility();
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-dataability-V14
爬取时间: 2025-04-27 22:27:53
来源: Huawei Developer
启动DataAbility会获取一个工具接口类对象（DataAbilityHelper）。启动DataAbility的示例代码如下：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import ability from '@ohos.ability.ability';
let uri: string = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(uri);
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/access-dataability-V14
爬取时间: 2025-04-27 22:28:07
来源: Huawei Developer
访问DataAbility需导入基础依赖包，以及获取与DataAbility子模块通信的URI字符串。
其中，基础依赖包包括：
-  @ohos.ability.featureAbility
-  @ohos.data.dataAbility
访问DataAbility的示例代码如下：
1.  创建工具接口类对象。
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import ohos_data_ability from '@ohos.data.dataAbility';
import ability from '@ohos.ability.ability';
// 作为参数传递的URI,与config中定义的URI的区别是多了一个"/",有三个"/"
let uri: string = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(uri);
```
2.  构建数据库相关的RDB数据。 注：关于DataAbilityPredicates的详细内容，请参考DataAbility谓词。
```typescript
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';
let valuesBucket_insert: rdb.ValuesBucket = { name: 'Rose', introduction: 'insert' };
let valuesBucket_update: rdb.ValuesBucket = { name: 'Rose', introduction: 'update' };
let crowd = new Array({ name: 'Rose', introduction: 'batchInsert_one' } as rdb.ValuesBucket,
{ name: 'Rose', introduction: 'batchInsert_two' } as rdb.ValuesBucket);
let columnArray = new Array('id', 'name', 'introduction');
let predicates = new ohos_data_ability.DataAbilityPredicates();
```
3.  调用insert方法向指定的DataAbility子模块插入数据。
```typescript
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';
import promptAction from '@ohos.promptAction';
import hilog from '@ohos.hilog';
const TAG: string = 'PageDataAbility';
// callback方式调用:
const domain: number = 0xFF00;
@Entry
@Component
struct PageDataAbility {
private valuesBucket_insert: rdb.ValuesBucket = { name: 'Rose', introduction: 'insert' };
private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);
build() {
Column() {
// ...
List({ initialIndex: 0 }) {
// ...
ListItemGroup() {
ListItem() {
Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
// ...
}
.onClick(() => {
// callback方式调用:
this.DAHelper.insert(this.uri, this.valuesBucket_insert, (error: BusinessError, data: number) => {
if (error && error.code !== 0) {
promptAction.showToast({
message: 'insert_failed_toast'
});
} else {
promptAction.showToast({
message: 'insert_success_toast'
});
}
hilog.info(domain, TAG, 'DAHelper insert result: ' + data + ', error: ' + JSON.stringify(error));
}
);
})
}
// ...
}
// ...
}
// ...
}
// ...
}
}
```
4.  调用delete方法删除DataAbility子模块中指定的数据。
```typescript
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';
import promptAction from '@ohos.promptAction';
import hilog from '@ohos.hilog';
const TAG: string = 'PageDataAbility';
const domain: number = 0xFF00;
@Entry
@Component
struct PageDataAbility {
private predicates = new ohos_data_ability.DataAbilityPredicates();
private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);
build() {
Column() {
// ...
List({ initialIndex: 0 }) {
// ...
ListItemGroup() {
ListItem() {
Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
// ...
}
.onClick(() => {
// callback方式调用:
this.DAHelper.delete(this.uri, this.predicates, (error, data) => {
if (error && error.code !== 0) {
promptAction.showToast({
message: 'delete_failed_toast'
});
} else {
promptAction.showToast({
message: 'delete_success_toast'
});
}
hilog.info(domain, TAG, 'DAHelper delete result: ' + data + ', error: ' + JSON.stringify(error));
}
);
})
}
// ...
}
// ...
}
// ...
}
// ...
}
}
```
5.  调用update方法更新指定DataAbility子模块中的数据。
```typescript
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';
import promptAction from '@ohos.promptAction';
import hilog from '@ohos.hilog';
const TAG: string = 'PageDataAbility';
const domain: number = 0xFF00;
@Entry
@Component
struct PageDataAbility {
private valuesBucket_update: rdb.ValuesBucket = { name: 'Rose', introduction: 'update' };
private predicates = new ohos_data_ability.DataAbilityPredicates();
private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);
build() {
Column() {
// ...
List({ initialIndex: 0 }) {
// ...
ListItemGroup() {
ListItem() {
Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
// ...
}
.onClick(() => {
// callback方式调用:
this.predicates.equalTo('name', 'Rose');
this.DAHelper.update(this.uri, this.valuesBucket_update, this.predicates, (error, data) => {
if (error && error.code !== 0) {
promptAction.showToast({
message: 'update_failed_toast'
});
} else {
promptAction.showToast({
message: 'update_success_toast'
});
}
hilog.info(domain, TAG, 'DAHelper update result: ' + data + ', error: ' + JSON.stringify(error));
}
);
})
}
// ...
}
// ...
}
// ...
}
// ...
}
}
```
6.  调用query方法在指定的DataAbility子模块中查找数据。
```typescript
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';
import promptAction from '@ohos.promptAction';
import hilog from '@ohos.hilog';
const TAG: string = 'PageDataAbility';
const domain: number = 0xFF00;
@Entry
@Component
struct PageDataAbility {
private columnArray = new Array('id', 'name', 'introduction');
private predicates = new ohos_data_ability.DataAbilityPredicates();
private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);
build() {
Column() {
// ...
List({ initialIndex: 0 }) {
// ...
ListItemGroup() {
ListItem() {
Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
// ...
}
.onClick(() => {
// callback方式调用:
this.predicates.equalTo('name', 'Rose');
this.DAHelper.query(this.uri, this.columnArray, this.predicates, (error, data) => {
if (error && error.code !== 0) {
promptAction.showToast({
message: 'query_failed_toast'
});
hilog.error(domain, TAG, `DAHelper query failed. Cause: ${error.message}`);
} else {
promptAction.showToast({
message: 'query_success_toast'
});
}
// ResultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
while (data.goToNextRow()) {
const id = data.getLong(data.getColumnIndex('id'));
const name = data.getString(data.getColumnIndex('name'));
const introduction = data.getString(data.getColumnIndex('introduction'));
hilog.info(domain, TAG, `DAHelper query result:id = [${id}], name = [${name}], introduction = [${introduction}]`);
}
// 释放数据集的内存
data.close();
}
);
})
}
// ...
}
// ...
}
// ...
}
// ...
}
}
```
7.  调用batchInsert方法向指定的DataAbility子模块批量插入数据。
```typescript
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';
import promptAction from '@ohos.promptAction';
import hilog from '@ohos.hilog';
const TAG: string = 'PageDataAbility';
const domain: number = 0xFF00;
@Entry
@Component
struct PageDataAbility {
private crowd = new Array({ name: 'Rose', introduction: 'batchInsert_one' } as rdb.ValuesBucket,
{ name: 'Rose', introduction: 'batchInsert_two' } as rdb.ValuesBucket);
private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);
build() {
Column() {
// ...
List({ initialIndex: 0 }) {
// ...
ListItemGroup() {
ListItem() {
Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
// ...
}
.onClick(() => {
// callback方式调用:
this.DAHelper.batchInsert(this.uri, this.crowd, (error, data) => {
if (error && error.code !== 0) {
promptAction.showToast({
message: 'batchInsert_failed_toast'
});
} else {
promptAction.showToast({
message: 'batchInsert_success_toast'
});
}
hilog.info(domain, TAG, 'DAHelper batchInsert result: ' + data + ', error: ' + JSON.stringify(error));
}
);
})
}
// ...
}
// ...
}
// ...
}
// ...
}
}
```
8.  调用executeBatch方法向指定的DataAbility子模块进行数据的批量处理。
```typescript
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';
import promptAction from '@ohos.promptAction';
import hilog from '@ohos.hilog';
const TAG: string = 'PageDataAbility';
const domain: number = 0xFF00;
@Entry
@Component
struct PageDataAbility {
private predicates = new ohos_data_ability.DataAbilityPredicates();
private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);
build() {
Column() {
// ...
List({ initialIndex: 0 }) {
// ...
ListItemGroup() {
ListItem() {
Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
// ...
}
.onClick(() => {
// callback方式调用:
let operations: Array<ability.DataAbilityOperation> = [{
uri: this.uri,
type: featureAbility.DataAbilityOperationType.TYPE_INSERT,
valuesBucket: { name: 'Rose', introduction: 'executeBatch' },
predicates: this.predicates,
expectedCount: 0,
predicatesBackReferences: undefined,
interrupted: true,
}];
this.DAHelper.executeBatch(this.uri, operations, (error, data) => {
if (error && error.code !== 0) {
promptAction.showToast({
message: 'executeBatch_failed_toast'
});
} else {
promptAction.showToast({
message: 'executeBatch_success_toast'
});
}
hilog.info(domain, TAG, `DAHelper executeBatch, result: ` + JSON.stringify(data) + ', error: ' + JSON.stringify(error));
});
})
}
// ...
}
// ...
}
// ...
}
// ...
}
}
```
DataAbility的客户端的接口是由工具接口类对象DataAbilityHelper向外提供，相关接口可参考DataAbilityHelper模块。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/dataability-permission-control-V14
爬取时间: 2025-04-27 22:28:20
来源: Huawei Developer
DataAbility提供数据服务，并不是所有的Ability都有权限读写它，DataAbility有一套权限控制机制来保证数据安全。分为静态权限控制和动态权限控制两部分。
静态权限控制
DataAbility作为服务端，在被拉起的时候，会根据config.json里面配置的权限来进行校验，有"readPermission"、"writePermission"和"Permission"三个配置项，可以不配或者为空。示例如下:
```json
"abilities": [
...
{
"name": ".DataAbility",
"srcLanguage": "ets",
"srcPath": "DataAbility",
"icon": "$media:icon",
"description": "$string:DataAbility_desc",
"type": "data",
"visible": true,
"uri": "dataability://com.samples.famodelabilitydevelop.DataAbility",
"readPermission": "ohos.permission.READ_CONTACTS",
"writePermission": "ohos.permission.WRITE_CONTACTS"
},
...
]
```
客户端在拉起DataAbility的时候，需要校验客户端是否有权限拉起该DataAbility。客户端的权限配置在config.json配置文件的"module"对象的"reqPermissions"对象中，示例如下：
```json
{
...
"module": {
...
"reqPermissions": [
{
"name": "ohos.permission.READ_CONTACTS"
},
{
"name": "ohos.permission.WRITE_CONTACTS"
},
...
],
...
}
}
```
动态权限控制
静态权限校验只能控制某个DataAbility是否能被另一个Ability或应用拉起，无法精确校验每个读写接口的权限，因为拉起DataAbility的时候，还不知道应用是否需要读写它的数据。
动态权限控制是校验每个数据操作的接口是否有对应的权限。客户端调用数据操作接口所需的权限如下表所示。
表1接口对应的读写权限配置
| 需要配置读权限的接口 | 需要配置写权限的接口 | 据实际操作配置读写权限的接口 |
| --- | --- | --- |
| query、normalizeUri、denormalizeUri、openfile（传入mode有'r'） | insert、batchInsert、delete、update、openfile（传入mode有'w'） | executeBatch |
对于需要配置读权限的接口，服务端需要配置readPermission，客户端必须申请相应的读权限才能调用相关的接口。
对于需要配置写权限的接口，服务端需要配置writePermission，客户端必须申请相应的写权限才能调用相关的接口。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/application-context-fa-V14
爬取时间: 2025-04-27 22:28:34
来源: Huawei Developer
FA模型下只有一个Context。Context中的所有功能都是通过方法来提供的，它提供了一些featureAbility中不存在的方法，相当于featureAbility的一个扩展和补全。
接口说明
FA模型下使用Context，需要通过featureAbility下的接口getContext来获取，而在此之前，需要先导入对应的包：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
```
然后使用如下方式获取对应的Context对象：
```typescript
import featureAbility from '@ohos.ability.featureAbility';
let context = featureAbility.getContext();
```
最终返回的对象为Context，其对应的接口说明请参见接口文档。
开发步骤
1.  查询Bundle信息。
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import hilog from '@ohos.hilog';
const TAG: string = 'MainAbility';
const domain: number = 0xFF00;
class MainAbility {
onCreate() {
// 获取context并调用相关方法
let context = featureAbility.getContext();
context.getBundleName((data, bundleName) => {
hilog.info(domain, TAG, 'ability bundleName:' + bundleName);
});
hilog.info(domain, TAG, 'Application onCreate');
}
//...
}
export default new MainAbility();
```
2.  设置当前featureAbility的显示方向。
```typescript
import featureAbility from '@ohos.ability.featureAbility';
import bundle from '@ohos.bundle';
import hilog from '@ohos.hilog';
const TAG: string = 'PageAbilitySingleton';
const domain: number = 0xFF00;
class PageAbilitySingleton {
onCreate() {
// 获取context并调用相关方法
let context = featureAbility.getContext();
context.setDisplayOrientation(bundle.DisplayOrientation.PORTRAIT).then(() => {
hilog.info(domain, TAG, 'Set display orientation.');
})
hilog.info(domain, TAG, 'Application onCreate');
}
onDestroy() {
hilog.info(domain, TAG, 'Application onDestroy');
}
//...
}
export default new PageAbilitySingleton();
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/want-fa-V14
爬取时间: 2025-04-27 22:28:48
来源: Huawei Developer
请参见Stage模型的"信息传递载体Want"。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/component-startup-rules-fa-V14
爬取时间: 2025-04-27 22:29:02
来源: Huawei Developer
启动组件是指一切启动或连接应用组件的行为：
-  启动PageAbility、ServiceAbility，如使用startAbility()等相关接口。
-  连接ServiceAbility、DataAbility，如使用connectAbility()、acquireDataAbilityHelper()等相关接口。
为了保证用户具有更好的使用体验，对以下几种易影响用户体验与系统安全的行为做了限制：
-  后台应用任意弹框，如各种广告弹窗，影响用户使用。
-  后台应用相互唤醒，不合理的占用系统资源，导致系统功耗增加或系统卡顿。
-  前台应用任意跳转至其他应用，如随意跳转到其他应用的支付页面，存在安全风险。
鉴于此，系统制订了一套组件启动规则，主要包括：
-  跨应用启动组件，需校验目标组件Visible
-  位于后台的应用，启动组件需校验BACKGROUND权限 基于API 8或更早版本SDK开发的应用在启动ServiceAbility组件或DataAbility组件时不受此限制的约束。
-  跨应用启动FA模型的ServiceAbility组件或DataAbility组件，对端应用需配置关联启动
1.  组件启动管控自v3.2 Release版本开始落地。
2.  与原本的启动规则不同，新的组件启动规则较为严格，开发者需熟知启动规则，避免业务功能异常。
启动组件的具体校验流程见下文。
同设备组件启动规则
设备内启动组件，不同场景下的规则不同，可分为如下两种场景：
-  启动PageAbility。
-  启动ServiceAbility或DataAbility。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170224.90187078130607964315735800334350:50001231000000:2800:3D66280F49963E17AB89AB127AFBA77AD3BAEFCD416431A13214DC0606536FFD.png)
分布式跨设备组件启动规则
跨设备启动组件，不同场景下的规则不同，可分为如下两种场景：
-  启动PageAbility。
-  启动ServiceAbility。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170224.04833532665652521321689550639361:50001231000000:2800:3AEF8E894F25A49632FB90F02684CC56C35913B3DC021E95FAD1AA9E92A2076D.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/process-model-fa-V14
爬取时间: 2025-04-27 22:29:15
来源: Huawei Developer
系统的进程模型如下图所示：
-  应用中（同一包名）的所有PageAbility、ServiceAbility、DataAbility、FormAbility运行在同一个独立进程中，即图中绿色部分的“Main Process”。
-  WebView拥有独立的渲染进程，即图中黄色部分的“Render Process”。 图1进程模型示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170225.54076171427818851418650904239678:50001231000000:2800:F8432391E675916AAFCFE01A7FEE8B55E27893F227B944D34C3810727308E9EB.png)
基于当前的进程模型，针对应用间存在多个进程的情况，系统提供了如下进程间通信机制：
公共事件机制：多用于一对多的通信场景，公共事件发布者可能存在多个订阅者同时接收事件。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/thread-model-fa-V14
爬取时间: 2025-04-27 22:29:29
来源: Huawei Developer
FA模型下的线程主要有如下三类：
-  主线程： 负责管理其他线程。
-  Ability线程：
-  Worker线程： 执行耗时操作。
基于当前的线程模型，不同的业务功能运行在不同的线程上，业务功能的交互就需要线程间通信。线程间通信目前主要有Emitter和Worker两种方式，其中Emitter主要适用于线程间的事件同步， Worker主要用于新开一个线程执行耗时任务。
FA模型每个Ability都有一个独立的线程，Emitter可用于Ability线程内、Ability线程间、Ability线程与Worker线程的事件同步。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/config-file-fa-V14
爬取时间: 2025-04-27 22:30:23
来源: Huawei Developer
应用配置文件中包含应用配置信息、应用组件信息、权限信息、开发者自定义信息等，这些信息在编译构建、分发和运行解决分别提供给编译工具、应用市场和操作系统使用。
在基于FA模型开发的应用项目代码下，都存在一个config.json配置文件，常用配置项请参见应用/组件级配置。对于这两种配置文件的更多介绍，请参见应用配置文件概述(FA模型)。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/capi_nativechildprocess_development_guideline-V14
爬取时间: 2025-04-27 22:30:37
来源: Huawei Developer
本模块提供了两种创建子进程的方式，开发者可根据需要进行选择。
创建支持IPC回调的子进程
场景介绍
本章节介绍如何在主进程中创建Native子进程，并在父子进程间建立IPC通道，方便开发者在Native层进行多进程编程。
接口说明
| 名称 | 描述 |
| --- | --- |
| int OH_Ability_CreateNativeChildProcess (const char *libName, OH_Ability_OnNativeChildProcessStarted onProcessStarted) | 创建子进程并加载参数中指定的动态链接库文件，进程启动结果通过回调参数异步通知，需注意回调通知为独立线程，回调函数实现需要注意线程同步，且不能执行高耗时操作避免长时间阻塞。 |
当前仅支持2in1设备，且单个进程只能启动一个Native子进程。
开发步骤
基于已创建完成的Native应用开发工程，在此基础上介绍如何使用AbilityKit提供的C API接口，创建Native子进程，并同时在父子进程间建立IPC通道。
动态库文件
头文件
1.  子进程-实现必要的导出方法。 在子进程中，实现必要的两个函数NativeChildProcess_OnConnect及NativeChildProcess_MainProc并导出（假设代码所在的文件名为ChildProcessSample.cpp）。其中NativeChildProcess_OnConnect方法返回的OHIPCRemoteStub对象负责主进程进行IPC通信，具体实现方法请参考IPC通信开发指导（C/C++)，本文不再赘述。 子进程启动后会先调用NativeChildProcess_OnConnect获取IPC Stub对象，之后再调用NativeChildProcess_MainProc移交主线程控制权，该函数返回后子进程随即退出。
2.  子进程-编译为动态链接库。 修改CMakeList.txt文件，编译为动态链接库（假设需要编译出的库文件名称为libchildprocesssample.so），并添加IPC动态库依赖。
3.  主进程-实现子进程启动结果回调函数。 回调函数传递的第二个参数OHIPCRemoteProxy对象，会与子进程实现的NativeChildProcess_OnConnect方法返回的OHIPCRemoteStub对象间建立IPC通道，具体使用方法参考IPC通信开发指导（C/C++)，本文不再赘述；OHIPCRemoteProxy对象使用完毕后，需要调用OH_IPCRemoteProxy_Destroy函数释放。
4.  主进程-启动Native子进程。 调用API启动Native子进程，需要注意返回值为NCP_NO_ERROR仅代表成功调用native子进程启动逻辑，实际的启动结果通过第二个参数中指定的回调函数异步通知。需注意仅允许在主进程中创建子进程。
5.  主进程-添加编译依赖项。 修改CMaklist.txt添加必要的依赖库，假设主进程所在的so名称为libmainprocesssample.so（主进程和子进程的实现也可以选择编译到同一个动态库文件）。
创建支持参数传递的子进程
场景介绍
本章节介绍如何创建Native子进程，并传递参数到子进程。
接口说明
| 名称 | 描述 |
| --- | --- |
| Ability_NativeChildProcess_ErrCode OH_Ability_StartNativeChildProcess (const char *entry, NativeChildProcess_Args args, NativeChildProcess_Options options, int32_t *pid) | 启动子进程并返回子进程pid。 |
开发步骤
动态库文件
头文件
1.  子进程-实现必要的导出方法。 在子进程中，实现参数为NativeChildProcess_Args入口函数并导出（假设代码所在的文件名为ChildProcessSample.cpp）。子进程启动后会调用该入口函数，该函数返回后子进程随即退出。
2.  子进程-编译为动态链接库。 修改CMakeList.txt文件，编译为动态链接库（假设需要编译出的库文件名称为libchildprocesssample.so），并添加元能力动态库依赖。
3.  主进程-启动Native子进程。 调用API启动Native子进程，返回值为NCP_NO_ERROR代表成功启动native子进程。
4.  主进程-添加编译依赖项。 修改CMaklist.txt添加必要的依赖库，假设主进程所在的so名称为libmainprocesssample.so（主进程和子进程的实现也可以选择编译到同一个动态库文件）。

