# 合并文件
合并时间: 2025-04-28 00:59:06

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkweb-V14
爬取时间: 2025-04-28 00:15:53
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-component-overview-V14
爬取时间: 2025-04-28 00:16:07
来源: Huawei Developer
使用场景
ArkWeb（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。常见使用场景包括：
-  应用集成Web页面：应用可以在页面中使用Web组件，嵌入Web页面内容，以降低开发成本，提升开发、运营效率。
-  浏览器网页浏览场景：浏览器类应用可以使用Web组件，打开三方网页，使用无痕模式浏览Web页面，设置广告拦截等。
-  小程序：小程序类宿主应用可以使用Web组件，渲染小程序的页面。
能力范围
Web组件为开发者提供了丰富的控制Web页面能力。包括：
-  Web页面加载：声明式加载Web页面和离屏加载Web页面等。
-  生命周期管理：组件生命周期状态变化，通知Web页面的加载状态变化等。
-  常用属性与事件：UserAgent管理、Cookie与存储管理、字体与深色模式管理、权限管理等。
-  与应用界面交互：自定义文本选择菜单、上下文菜单、文件上传界面等与应用界面交互能力。
-  App通过JavaScriptProxy，与Web页面进行JavaScript交互。
-  安全与隐私：无痕浏览模式、广告拦截、坚盾守护模式等。
-  维测能力：DevTools工具调试能力，使用crashpad收集Web组件崩溃信息。
-  其他高阶能力：与原生组件同层渲染、Web组件的网络托管、Web组件的媒体播放托管、Web组件输入框拉起自定义输入法、网页接入密码保险箱等。
约束与限制

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web_component_process-V14
爬取时间: 2025-04-28 00:16:20
来源: Huawei Developer
ArkWeb是多进程模型，分为应用进程、Web渲染进程、Web GPU进程、Web孵化进程和Foundation进程。
Web内核没有明确的内存大小申请约束，理论上可以无限大，直到被资源管理释放。
图1ArkWeb进程模型图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170356.76422790683165746953872576049855:50001231000000:2800:890AD840EB2410949A016996B9A6CA6D8668795B4231D6B29F9C003DE887D61F.png)
-  应用进程中Web相关线程（应用唯一） 应用进程为主进程。包含网络线程、Video线程、Audio线程和IO线程等。 负责Web组件的北向接口与回调处理，网络请求、媒体服务等需要与其他系统服务交互的功能。
-  应用进程为主进程。包含网络线程、Video线程、Audio线程和IO线程等。
-  负责Web组件的北向接口与回调处理，网络请求、媒体服务等需要与其他系统服务交互的功能。
-  Foundation进程（系统唯一） 负责接收应用进程进行孵化进程的请求，管理应用进程和Web渲染进程的绑定关系。
-  Web孵化进程（系统唯一） 负责接收Foundation进程的请求，执行孵化Web渲染进程与Web GPU进程。 执行孵化后处理安全沙箱降权、预加载动态库，以提升性能。
-  负责接收Foundation进程的请求，执行孵化Web渲染进程与Web GPU进程。
-  执行孵化后处理安全沙箱降权、预加载动态库，以提升性能。
-  Web渲染进程（应用可指定多Web实例间共享或独立进程） 负责运行Web渲染进程引擎（HTML解析、排版、绘制、渲染）。 负责运行ArkWeb执行引擎（JavaScript、Web Assembly）。 提供接口供应用选择多Web实例间是否共享渲染进程，满足不同场景对安全性、稳定性、内存占用的诉求。 默认策略：移动设备上共享渲染进程以节省内存，2in1设备上独立渲染进程提升安全与稳定性。
-  负责运行Web渲染进程引擎（HTML解析、排版、绘制、渲染）。
-  负责运行ArkWeb执行引擎（JavaScript、Web Assembly）。
-  提供接口供应用选择多Web实例间是否共享渲染进程，满足不同场景对安全性、稳定性、内存占用的诉求。
-  默认策略：移动设备上共享渲染进程以节省内存，2in1设备上独立渲染进程提升安全与稳定性。
-  Web GPU进程（应用唯一） 负责光栅化、合成送显等与GPU、RenderService交互功能。提升应用进程稳定性、安全性。
-  应用进程为主进程。包含网络线程、Video线程、Audio线程和IO线程等。
-  负责Web组件的北向接口与回调处理，网络请求、媒体服务等需要与其他系统服务交互的功能。
-  负责接收Foundation进程的请求，执行孵化Web渲染进程与Web GPU进程。
-  执行孵化后处理安全沙箱降权、预加载动态库，以提升性能。
-  负责运行Web渲染进程引擎（HTML解析、排版、绘制、渲染）。
-  负责运行ArkWeb执行引擎（JavaScript、Web Assembly）。
-  提供接口供应用选择多Web实例间是否共享渲染进程，满足不同场景对安全性、稳定性、内存占用的诉求。
-  默认策略：移动设备上共享渲染进程以节省内存，2in1设备上独立渲染进程提升安全与稳定性。
1.  可通过setRenderProcessMode设置渲染子进程的模式，从而控制渲染过程的单进程或多进程状态。 移动设备默认为单进程渲染，而2in1设备则默认采用多进程渲染。通过调用getRenderProcessMode可查询当前的渲染子进程模式，其中枚举值0表示单进程模式，枚举值1对应多进程模式。若获取的值超出RenderProcessMode枚举范围，系统将自动采用多进程渲染模式作为默认设置。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('getRenderProcessMode')
.onClick(() => {
let mode = webview.WebviewController.getRenderProcessMode();
console.log("getRenderProcessMode: " + mode);
})
Button('setRenderProcessMode')
.onClick(() => {
try {
webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as     BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
2.  可通过terminateRenderProcess来主动关闭渲染进程。若渲染进程尚未启动或已销毁，此操作将不会产生任何影响。此外，销毁渲染进程将同时影响所有与之关联的其他实例。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('terminateRenderProcess')
.onClick(() => {
let result = this.controller.terminateRenderProcess();
console.log("terminateRenderProcess result: " + result);
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
3.  可通过onRenderExited来监听渲染进程的退出事件，从而获知退出的具体原因（如内存OOM、crash或正常退出等）。由于多个Web组件可能共用同一个渲染进程，因此，每当渲染进程退出时，每个受此影响的Web组件均会触发相应的回调。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'chrome://crash/', controller: this.controller })
.onRenderExited((event) => {
if (event) {
console.log('reason:' + event.renderExitReason);
}
})
}
}
}
```
4.  可通过onRenderProcessNotResponding、onRenderProcessResponding来监听渲染进程的无响应状态。 当Web组件无法处理输入事件，或未能在预期时间内导航至新URL时，系统会判定网页进程为无响应状态，并触发onRenderProcessNotResponding回调。在网页进程持续无响应期间，该回调可能反复触发，直至进程恢复至正常运行状态，此时将触发onRenderProcessResponding回调。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
.onRenderProcessNotResponding((data) => {
console.log("onRenderProcessNotResponding: [jsStack]= " + data.jsStack +
", [process]=" + data.pid + ", [reason]=" + data.reason);
})
}
}
}
```
5.  Web组件创建参数涵盖了多进程模型的运用。其中，sharedRenderProcessToken标识了当前Web组件所指定的共享渲染进程的token。在多渲染进程模式下，拥有相同token的Web组件将优先尝试重用与该token绑定的渲染进程。token与渲染进程的绑定关系，在渲染进程的初始化阶段形成。一旦渲染进程不再关联任何Web组件，它与token的绑定关系将被解除。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller, sharedRenderProcessToken: "111" })
Web({ src: 'www.w3.org', controller: this.controller, sharedRenderProcessToken: "111" })
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-event-sequence-V14
爬取时间: 2025-04-28 00:16:33
来源: Huawei Developer
概述
开发者可以使用Web组件加载本地或者在线网页。
Web组件提供了丰富的组件生命周期回调接口，通过这些回调接口，开发者可以感知Web组件的生命周期状态变化，进行相关的业务处理。
Web组件的状态主要包括：Controller绑定到Web组件、网页加载开始、网页加载进度、网页加载结束、页面即将可见等。
图1Web组件网页正常加载过程中的回调事件
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170357.49454507976459718406317260777642:50001231000000:2800:C6F720FACDA80715F10748FC8D45139585B35D3ABDE29B1A1DD546978A2EF34C.png)
Web组件网页加载的状态说明
-  aboutToAppear函数：在创建自定义组件的新实例后，在执行其build函数前执行。一般建议在此设置WebDebug调试模式setWebDebuggingAccess、设置Web内核自定义协议URL的跨域请求与fetch请求的权限customizeSchemes、设置Cookie(configCookie)等。
-  onControllerAttached事件：当Controller成功绑定到Web组件时触发该回调，且禁止在该事件回调前调用Web组件相关的接口，否则会抛出js-error异常。推荐在此事件中注入JS对象registerJavaScriptProxy、设置自定义用户代理setCustomUserAgent，可以在回调中使用loadUrl，getWebId等操作网页不相关的接口。但因该回调调用时网页还未加载，因此无法在回调中使用有关操作网页的接口，例如zoomIn、zoomOut等。
-  onLoadIntercept事件：当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。默认允许加载。
-  onOverrideUrlLoading事件：当URL将要加载到当前Web中时，让宿主应用程序有机会获得控制权，回调函数返回true将导致当前Web中止加载URL，而返回false则会导致Web继续照常加载URL。onLoadIntercept接口和onOverrideUrlLoading接口行为不一致，触发时机也不同，所以在应用场景上存在一定区别。主要是在LoadUrl和iframe（HTML标签，表示HTML内联框架元素，用于将另一个页面嵌入到当前页面中）加载时，onLoadIntercept事件会正常回调到，但onOverrideUrlLoading事件在LoadUrl加载时不会触发，在iframe加载HTTP(s)协议或about:blank时也不会触发。详细介绍请见onLoadIntercept和onOverrideUrlLoading的说明。
-  onInterceptRequest事件：当Web组件加载url之前触发该回调，用于拦截url并返回响应数据。
-  onPageBegin事件：网页开始加载时触发该回调，且只在主frame（表示一个HTML元素，用于展示HTML页面的HTML元素）触发。如果是iframe或者frameset（用于包含frame的HTML标签）的内容加载时则不会触发此回调。多frame页面有可能同时开始加载，即使主frame已经加载结束，子frame也有可能才开始或者继续加载中。同一页面导航（片段、历史状态等）或者在提交前失败、被取消的导航等也不会触发该回调。
-  onProgressChange事件：告知开发者当前页面加载的进度。多frame页面或者子frame有可能还在继续加载而主frame可能已经加载结束，所以在onPageEnd事件后依然有可能收到该事件。
-  onPageEnd事件：网页加载完成时触发该回调，且只在主frame触发。多frame页面有可能同时开始加载，即使主frame已经加载结束，子frame也有可能才开始或者继续加载中。同一页面导航（片段、历史状态等）或者在提交前失败、被取消的导航等也不会触发该回调。推荐在此回调中执行JavaScript脚本loadUrl等。需要注意的是收到该回调并不能保证Web绘制的下一帧将反映此时DOM的状态。
-  onPageVisible事件：Web回调事件。渲染流程中当HTTP响应的主体开始加载，新页面即将可见时触发该回调。此时文档加载还处于早期，因此链接的资源比如在线CSS、在线图片等可能尚不可用。
-  onRenderExited事件：应用渲染进程异常退出时触发该回调，可以在此回调中进行系统资源的释放、数据的保存等操作。如果应用希望异常恢复，需要调用loadUrl接口重新加载页面。
-  onDisAppear事件：组件卸载消失时触发此回调。该事件为通用事件，指组件从组件树上卸载时触发的事件。
应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { promptAction } from '@kit.ArkUI';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
responseWeb: WebResourceResponse = new WebResourceResponse();
heads: Header[] = new Array();
@State webData: string = "<!DOCTYPE html>\n" +
"<html>\n" +
"<head>\n" +
"<title>intercept test</title>\n" +
"</head>\n" +
"<body>\n" +
"<h1>intercept test</h1>\n" +
"</body>\n" +
"</html>";
aboutToAppear(): void {
try {
webview.WebviewController.setWebDebuggingAccess(true);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
}
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onControllerAttached(() => {
// 推荐在此loadUrl、设置自定义用户代理、注入JS对象等
console.log('onControllerAttached execute')
})
.onLoadIntercept((event) => {
if (event) {
console.log('onLoadIntercept url:' + event.data.getRequestUrl())
console.log('url:' + event.data.getRequestUrl())
console.log('isMainFrame:' + event.data.isMainFrame())
console.log('isRedirect:' + event.data.isRedirect())
console.log('isRequestGesture:' + event.data.isRequestGesture())
}
// 返回true表示阻止此次加载，否则允许此次加载
return false;
})
.onOverrideUrlLoading((webResourceRequest: WebResourceRequest) => {
if (webResourceRequest && webResourceRequest.getRequestUrl() == "about:blank") {
return true;
}
return false;
})
.onInterceptRequest((event) => {
if (event) {
console.log('url:' + event.request.getRequestUrl());
}
let head1: Header = {
headerKey: "Connection",
headerValue: "keep-alive"
}
let head2: Header = {
headerKey: "Cache-Control",
headerValue: "no-cache"
}
let length = this.heads.push(head1);
length = this.heads.push(head2);
this.responseWeb.setResponseHeader(this.heads);
this.responseWeb.setResponseData(this.webData);
this.responseWeb.setResponseEncoding('utf-8');
this.responseWeb.setResponseMimeType('text/html');
this.responseWeb.setResponseCode(200);
this.responseWeb.setReasonMessage('OK');
// 返回响应数据则按照响应数据加载，无响应数据则返回null表示按照原来的方式加载
return this.responseWeb;
})
.onPageBegin((event) => {
if (event) {
console.log('onPageBegin url:' + event.url);
}
})
.onFirstContentfulPaint(event => {
if (event) {
console.log("onFirstContentfulPaint:" + "[navigationStartTick]:" +
event.navigationStartTick + ", [firstContentfulPaintMs]:" +
event.firstContentfulPaintMs);
}
})
.onProgressChange((event) => {
if (event) {
console.log('newProgress:' + event.newProgress);
}
})
.onPageEnd((event) => {
// 推荐在此事件中执行JavaScript脚本
if (event) {
console.log('onPageEnd url:' + event.url);
}
})
.onPageVisible((event) => {
console.log('onPageVisible url:' + event.url);
})
.onRenderExited((event) => {
if (event) {
console.log('onRenderExited reason:' + event.renderExitReason);
}
})
.onDisAppear(() => {
promptAction.showToast({
message: 'The web is hidden',
duration: 2000
})
})
}
}
}
```
前端index.html。
Web组件网页加载的性能指标
网页加载过程中需要关注一些重要的性能指标。例如，FCP(First Contentful Paint)首次内容绘制，FMP(First Meaningful Paint)首次有效绘制，LCP(Largest Contentful Paint)最大内容绘制等。Web组件提供了如下接口来通知开发者。
-  onFirstContentfulPaint事件：网页首次内容绘制的回调函数。首次绘制文本、图像、非空白Canvas或者SVG的时间点。
-  onFirstMeaningfulPaint事件：网页首次有效绘制的回调函数。首次绘制页面主要内容的时间点。
-  onLargestContentfulPaint事件：网页绘制页面最大内容的回调函数。可视区域内容最大的可见元素开始出现在页面上的时间点。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-set-attributes-events-V14
爬取时间: 2025-04-28 00:16:47
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-default-useragent-V14
爬取时间: 2025-04-28 00:17:00
来源: Huawei Developer
UserAgent（简称UA）是一个特殊的字符串，它包含了设备类型、操作系统及版本等关键信息。如果页面无法正确识别UA，可能会导致一系列异常情况，例如页面布局错误、渲染问题以及逻辑错误等。
默认UserAgent结构
-  默认UserAgent定义
-  举例说明
-  字段说明 当前的设备类型。 取值范围： - Phone：手机设备 - Tablet：平板设备 - PC：2in1设备 基础操作系统名称。 默认取值：OpenHarmony 基础操作系统版本，两位数字，M.S。 通过系统参数const.ohos.fullname解析版本号得到，取版本号部分M.S前两位。 默认取值：例如5.0 发行版操作系统名称。 默认取值：HarmonyOS 发行版操作系统版本，两位数字，M.S。 通过系统参数const.product.os.dist.apiname解析版本号得到，如果该参数值为空，通过系统参数const.product.os.dist.version解析版本号得到，取M.S前两位。 默认取值：例如5.0 兼容Chrome主版本的版本号，从114版本开始演进。 默认取值：114 HarmonyOS版本Web内核名称。 默认取值：ArkWeb ArkWeb版本号，格式a.b.c.d。 默认取值：例如4.1.6.1 前向兼容字段。 默认取值：Mobile 三方应用可以扩展的字段。 三方应用使用ArkWeb组件时，可以做UA扩展，例如加入应用相关信息标识。
| 字段 | 含义 |
| --- | --- |
| DeviceType | 当前的设备类型。 取值范围： - Phone：手机设备 - Tablet：平板设备 - PC：2in1设备  |
| OSName | 基础操作系统名称。 默认取值：OpenHarmony  |
| OSVersion | 基础操作系统版本，两位数字，M.S。 通过系统参数const.ohos.fullname解析版本号得到，取版本号部分M.S前两位。 默认取值：例如5.0  |
| DistributionOSName | 发行版操作系统名称。 默认取值：HarmonyOS  |
| DistributionOSVersion | 发行版操作系统版本，两位数字，M.S。 通过系统参数const.product.os.dist.apiname解析版本号得到，如果该参数值为空，通过系统参数const.product.os.dist.version解析版本号得到，取M.S前两位。 默认取值：例如5.0  |
| ChromeCompatibleVersion | 兼容Chrome主版本的版本号，从114版本开始演进。 默认取值：114  |
| ArkWeb | HarmonyOS版本Web内核名称。 默认取值：ArkWeb  |
| ArkWeb VersionCode | ArkWeb版本号，格式a.b.c.d。 默认取值：例如4.1.6.1  |
| DeviceCompat | 前向兼容字段。 默认取值：Mobile  |
| 扩展区 | 三方应用可以扩展的字段。 三方应用使用ArkWeb组件时，可以做UA扩展，例如加入应用相关信息标识。  |
自定义UserAgent结构
在下面的示例中，通过getUserAgent()接口获取当前默认用户代理，支持开发者基于默认的UserAgent去定制UserAgent。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('getUserAgent')
.onClick(() => {
try {
let userAgent = this.controller.getUserAgent();
console.log("userAgent: " + userAgent);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
以下示例通过setCustomUserAgent()接口设置自定义用户代理，会覆盖系统的用户代理。建议将扩展字段追加在默认用户代理的末尾。
当Web组件src设置了url时，建议在onControllerAttached回调事件中设置UserAgent，设置方式请参考示例。如果未在onControllerAttached回调事件中设置UserAgent，再调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置UserAgent不符的异常现象。
当Web组件src设置为空字符串时，建议先调用setCustomUserAgent方法设置UserAgent，再通过loadUrl加载具体页面。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
// 三方应用相关信息标识
@State customUserAgent: string = ' DemoApp';
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
.onControllerAttached(() => {
console.log("onControllerAttached");
try {
let userAgent = this.controller.getUserAgent() + this.customUserAgent;
this.controller.setCustomUserAgent(userAgent);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
}
}
}
```
在下面的示例中，通过getCustomUserAgent()接口获取自定义用户代理。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
@State userAgent: string = '';
build() {
Column() {
Button('getCustomUserAgent')
.onClick(() => {
try {
this.userAgent = this.controller.getCustomUserAgent();
console.log("userAgent: " + this.userAgent);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
常见问题
如何通过UserAgent来识别HarmonyOS操作系统中不同设备
HarmonyOS设备的识别主要通过UserAgent中的系统、系统版本和设备类型三个维度来判断。建议同时检查系统、系统版本和设备类型，以确保更准确的设备识别。
1.  系统识别 通过UserAgent中的{OSName}字段识别HarmonyOS系统。
```typescript
const isHarmonyOS = () => /OpenHarmony/i.test(navigator.userAgent);
```
2.  系统版本识别 通过UserAgent中的{OSName}和{OSVersion}字段识别HarmonyOS系统。格式为：OpenHarmony + 版本号。
```typescript
const matches = navigator.userAgent.match(/OpenHarmony (\d+\.?\d*)/);
matches?.length && Number(matches[1]) >= 5;
```
3.  设备类型识别 通过DeviceType字段来识别不同设备类型。
```typescript
// 检测是否为手机设备
const isPhone = () => /Phone/i.test(navigator.userAgent);
// 检测是否为平板设备
const isTablet = () => /Tablet/i.test(navigator.userAgent);
// 检测是否为2in1设备
const is2in1 = () => /PC/i.test(navigator.userAgent);
```
如何模拟HarmonyOS操作系统的UserAgent进行前端调试
在Windows/Mac/Linux等操作系统中，可以通过Chrome/Edge/Firefox等浏览器DevTools提供的UserAgent复写能力，模拟HarmonyOS UserAgent。
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-cookie-and-data-storage-mgmt-V14
爬取时间: 2025-04-28 00:17:13
来源: Huawei Developer
Cookie管理
Cookie是网络访问过程中，由服务端发送给客户端的一小段数据。客户端可持有该数据，并在后续访问该服务端时，方便服务端快速对客户端身份、状态等进行识别。
当Cookie SameSite属性未指定时，默认值为SameSite=Lax，只在用户导航到cookie的源站点时发送cookie，不会在跨站请求中被发送。
Web组件提供了WebCookieManager类，用于管理Web组件的Cookie信息。Cookie信息保存在应用沙箱路径下/proc/{pid}/root/data/storage/el2/base/cache/web/Cookiesd的文件中。
下面以configCookieSync()接口举例，为“www.example.com”设置单个Cookie的值“value=test”。其他Cookie的相关功能及使用，请参考WebCookieManager()接口文档。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('configCookieSync')
.onClick(() => {
try {
webview.WebCookieManager.configCookieSync('https://www.example.com', 'value=test');
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
缓存与存储管理
在访问网站时，网络资源请求是相对比较耗时的。开发者可以通过Cache、Dom Storage等手段将资源保存到本地，以提升访问同一网站的速度。
Cache
使用cacheMode()配置页面资源的缓存模式，Web组件为开发者提供四种缓存模式，分别为：
-  Default : 优先使用未过期的缓存，如果缓存不存在，则从网络获取。
-  None : 加载资源使用cache，如果cache中无该资源则从网络中获取。
-  Online : 加载资源不使用cache，全部从网络中获取。
-  Only ：只从cache中加载资源。
在下面的示例中，选用缓存设置为None模式。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
@State mode: CacheMode = CacheMode.None;
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
.cacheMode(this.mode)
}
}
}
```
同时，为了获取最新资源，开发者可以通过removeCache()接口清除已经缓存的资源，示例代码如下：
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
@State mode: CacheMode = CacheMode.None;
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('removeCache')
.onClick(() => {
try {
// 设置为true时同时清除rom和ram中的缓存，设置为false时只清除ram中的缓存
this.controller.removeCache(true);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
.cacheMode(this.mode)
}
}
}
```
Dom Storage
Dom Storage包含了Session Storage和Local Storage两类。前者为临时数据，其存储与释放跟随会话生命周期；后者为可持久化数据，落盘在应用目录下。两者的数据均通过Key-Value的形式存储，通常在访问需要客户端存储的页面时使用。开发者可以通过Web组件的属性接口domStorageAccess()进行使能配置，示例如下：
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
.domStorageAccess(true)
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-set-dark-mode-V14
爬取时间: 2025-04-28 00:17:27
来源: Huawei Developer
Web组件支持对前端页面进行深色模式配置。
-  通过darkMode()接口可以配置不同的深色模式，默认关闭。当深色模式开启时，Web将启用媒体查询prefers-color-scheme中网页所定义的深色样式，若网页未定义深色样式，则保持原状。如需开启强制深色模式，建议配合forceDarkAccess()使用。WebDarkMode.Off模式表示关闭深色模式。WebDarkMode.On表示开启深色模式，并且深色模式跟随前端页面。WebDarkMode.Auto表示开启深色模式，并且深色模式跟随系统。 在下面的示例中，通过darkMode()接口将页面深色模式配置为跟随系统。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
@State mode: WebDarkMode = WebDarkMode.Auto;
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.darkMode(this.mode)
}
}
}
```
-  通过forceDarkAccess()接口可将前端页面强制配置深色模式，强制深色模式无法保证所有颜色转换符合预期，且深色模式不跟随前端页面和系统。配置该模式时候，需要将深色模式配置成WebDarkMode.On。 在下面的示例中，通过forceDarkAccess()接口将页面强制配置为深色模式。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
@State mode: WebDarkMode = WebDarkMode.On;
@State access: boolean = true;
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.darkMode(this.mode)
.forceDarkAccess(this.access)
}
}
}
```
-  index.html页面代码。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-open-in-new-window-V14
爬取时间: 2025-04-28 00:17:40
来源: Huawei Developer
Web组件提供了在新窗口打开页面的能力，开发者可以通过multiWindowAccess()接口来设置是否允许网页在新窗口打开。当有新窗口打开时，应用侧会在onWindowNew()接口中收到Web组件新窗口事件，开发者需要在此接口事件中，新建窗口来处理Web组件窗口请求。
-  allowWindowOpenMethod()接口设置为true时，前端页面通过JavaScript函数调用的方式打开新窗口。
-  如果开发者在onWindowNew()接口通知中没有创建新窗口，需要将ControllerHandler.setWebController()接口参数设置成null。
如下面的本地示例，当用户点击“新窗口中打开网页”按钮时，应用侧会在onWindowNew()接口中收到Web组件新窗口事件。
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
// 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
@CustomDialog
struct NewWebViewComp {
controller?: CustomDialogController;
webviewController1: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: "", controller: this.webviewController1 })
.javaScriptAccess(true)
.multiWindowAccess(false)
.onWindowExit(() => {
console.info("NewWebViewComp onWindowExit");
if (this.controller) {
this.controller.close();
}
})
}
}
}
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
dialogController: CustomDialogController | null = null;
build() {
Column() {
Web({ src: $rawfile("window.html"), controller: this.controller })
.javaScriptAccess(true)
// 需要使能multiWindowAccess
.multiWindowAccess(true)
.allowWindowOpenMethod(true)
.onWindowNew((event) => {
if (this.dialogController) {
this.dialogController.close()
}
let popController: webview.WebviewController = new webview.WebviewController();
this.dialogController = new CustomDialogController({
builder: NewWebViewComp({ webviewController1: popController })
})
this.dialogController.open();
// 将新窗口对应WebviewController返回给Web内核。
// 若不调用event.handler.setWebController接口，会造成render进程阻塞。
// 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
event.handler.setWebController(popController);
})
}
}
}
```
-  window.html页面代码。
图1新窗口中打开页面效果图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170357.38616167694121261511234991629427:50001231000000:2800:6CA229A2593F0C5FFB1BB3F82F0EBC39AA5F0E5C8BE49F91090EEB9C42CA884B.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-geolocation-permission-V14
爬取时间: 2025-04-28 00:17:53
来源: Huawei Developer
Web组件提供位置权限管理能力。开发者可以通过onGeolocationShow()接口对某个网站进行位置权限管理。Web组件根据接口响应结果，决定是否赋予前端页面权限。
-  使用获取设备位置功能前请在module.json5中添加位置相关权限，权限的添加方法请参考在配置文件中声明权限。
在下面的示例中，用户点击前端页面"获取位置"按钮，Web组件通过弹窗的形式通知应用侧位置权限请求消息。
-  前端页面代码。
-  应用代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
let context = getContext(this) as common.UIAbilityContext;
let atManager = abilityAccessCtrl.createAtManager();
// 向用户请求位置权限设置。
atManager.requestPermissionsFromUser(context, ["ohos.permission.APPROXIMATELY_LOCATION"]).then((data) => {
console.info('data:' + JSON.stringify(data));
console.info('data permissions:' + data.permissions);
console.info('data authResults:' + data.authResults);
}).catch((error: BusinessError) => {
console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
})
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: $rawfile('getLocation.html'), controller: this.controller })
.geolocationAccess(true)
.onGeolocationShow((event) => { // 地理位置权限申请通知
AlertDialog.show({
title: '位置权限请求',
message: '是否允许获取位置信息',
primaryButton: {
value: 'cancel',
action: () => {
if (event) {
event.geolocation.invoke(event.origin, false, false); // 不允许此站点地理位置权限请求
}
}
},
secondaryButton: {
value: 'ok',
action: () => {
if (event) {
event.geolocation.invoke(event.origin, true, false); // 允许此站点地理位置权限请求
}
}
},
cancel: () => {
if (event) {
event.geolocation.invoke(event.origin, false, false); // 不允许此站点地理位置权限请求
}
}
})
})
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-incognito-mode-V14
爬取时间: 2025-04-28 00:18:07
来源: Huawei Developer
开发者在创建Web组件时，可以将可选参数incognitoMode设置为true，来开启Web组件的隐私模式。 当使用隐私模式时，浏览网页时的Cookie、 Cache Data等数据不会保存在本地的持久化文件，当隐私模式的Web组件被销毁时，Cookie、 Cache Data等数据将不被记录下来。
-  创建隐私模式的Web组件。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
}
}
}
```
-  通过isIncogntoMode判断当前Web组件是否是隐私模式。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('isIncognitoMode')
.onClick(() => {
try {
let result = this.controller.isIncognitoMode();
console.log('isIncognitoMode' + result);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
隐私模式提供了一系列接口，用于操作地理位置、Cookie以及Cache Data。
-  通过allowGeolocation设置隐私模式下的Web组件允许指定来源使用地理位置。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
origin: string = "file:///";
build() {
Column() {
Button('allowGeolocation')
.onClick(() => {
try {
// allowGeolocation第二个参数表示隐私模式（true）或非隐私模式（false）下，允许指定来源使用地理位置。
webview.GeolocationPermissions.allowGeolocation(this.origin, true);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
}
}
}
```
-  通过deleteGeolocation清除隐私模式下指定来源的地理位置权限状态。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
origin: string = "file:///";
build() {
Column() {
Button('deleteGeolocation')
.onClick(() => {
try {
// deleteGeolocation第二个参数表示隐私模式（true）或非隐私模式（false）下，清除指定来源的地理位置权限状态。
webview.GeolocationPermissions.deleteGeolocation(this.origin, true);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
}
}
}
```
-  通过getAccessibleGeolocation以回调方式异步获取隐私模式下指定源的地理位置权限状态。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
origin: string = "file:///";
build() {
Column() {
Button('getAccessibleGeolocation')
.onClick(() => {
try {
// getAccessibleGeolocation第三个参数表示隐私模式（true）或非隐私模式（false）下，以回调方式异步获取指定源的地理位置权限状态。
webview.GeolocationPermissions.getAccessibleGeolocation(this.origin, (error, result) => {
if (error) {
console.log('getAccessibleGeolocationAsync error: ' + JSON.stringify(error));
return;
}
console.log('getAccessibleGeolocationAsync result: ' + result);
}, true);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
}
}
}
```
-  通过deleteAllData清除隐私模式下Web SQL当前使用的所有存储。 加载的html文件。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('deleteAllData')
.onClick(() => {
try {
// deleteAllData参数表示删除所有隐私模式（true）或非隐私模式（false）下，内存中的web数据。
webview.WebStorage.deleteAllData(true);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.controller, incognitoMode: true })
.databaseAccess(true)
}
}
}
```
-  通过fetchCookieSync获取隐私模式下指定url对应cookie的值。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('fetchCookieSync')
.onClick(() => {
try {
// fetchCookieSync第二个参数表示获取隐私模式（true）或非隐私模式（false）下，webview的内存cookies。
let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com', true);
console.log("fetchCookieSync cookie = " + value);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
}
}
}
```
-  通过configCookieSync设置隐私模式下指定url的单个cookie的值。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('configCookieSync')
.onClick(() => {
try {
// configCookieSync第三个参数表示获取隐私模式（true）或非隐私模式（false）下，对应url的cookies。
webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b', true);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
}
}
}
```
-  通过existCookie查询隐私模式下是否存在cookie。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('existCookie')
.onClick(() => {
// existCookie参数表示隐私模式（true）或非隐私模式（false）下，查询是否存在cookies。
let result = webview.WebCookieManager.existCookie(true);
console.log("result: " + result);
})
Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
}
}
}
```
-  通过clearAllCookiesSync清除隐私模式下所有cookie。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('clearAllCookiesSync')
.onClick(() => {
// clearAllCookiesSync参数表示清除隐私模式（true）或非隐私模式（false）下，webview的所有内存cookies。
webview.WebCookieManager.clearAllCookiesSync(true);
})
Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-sensor-V14
爬取时间: 2025-04-28 00:18:20
来源: Huawei Developer
概述
运动和方向传感器，如加速度计、陀螺仪等，能够监测设备的运动状态和方向变化，例如设备的旋转、倾斜等。
通过W3C标准协议接口，Web组件能够访问这些传感器的数据，进而实现更加丰富的用户交互功能。例如，开发者在网页应用中可以利用加速度计识别运动模式，指导用户进行健身运动，利用陀螺仪捕获玩家手中设备的倾斜和旋转动作，实现无按钮操控的游戏体验。
通过在JavaScript中调用以下支持的W3C标准协议接口，可以访问运动和方向传感器。
| 接口 | 名称 | 说明 |
| --- | --- | --- |
| Accelerometer | 加速度 | 可获取设备X、Y、Z轴方向的加速度数据。 |
| Gyroscope | 陀螺仪 | 可获取设备X、Y、Z轴方向的角速度数据。 |
| AbsoluteOrientationSensor | 绝对定位 | 可获取表示设备绝对定位方向的四元数，包含X、Y、Z和W分量。 |
| RelativeOrientationSensor | 相对定位 | 可获取表示设备相对定位方向的四元数，包含X、Y、Z和W分量。 |
| DeviceMotionEvent | 设备运动事件 | 通过监听该事件，可获取设备在X、Y、Z轴方向上的加速度数据，设备在X、Y、Z轴方向上包含重力的加速度数据，以及设备在alpha、beta、gamma轴方向上旋转的速率数据。 |
| DeviceOrientationEvent | 设备方向事件 | 通过监听该事件，可获取设备绕X、Y、Z轴的角度。 |
需要权限
使用加速度、陀螺仪及设备运动事件接口时，需在配置文件module.json5中声明相应的传感器权限。具体配置方法请参考在配置文件中声明权限。
Web组件在对接运动和方向传感器时，需配置onPermissionRequest接口，通过该接口接收权限请求通知。
开发步骤
1.  应用侧代码中，Web组件配置onPermissionRequest接口，可通过PermissionRequest的getAccessibleResource接口获取请求权限的资源类型，当资源类型为TYPE_SENSOR时，进行传感器授权处理。
```typescript
import { webview } from '@kit.ArkWeb';
import { abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController()
aboutToAppear() {
// 配置Web开启调试模式
webview.WebviewController.setWebDebuggingAccess(true);
// 访问控制管理, 获取访问控制模块对象。
let atManager = abilityAccessCtrl.createAtManager();
try {
atManager.requestPermissionsFromUser(getContext(this), ['ohos.permission.ACCELEROMETER', 'ohos.permission.GYROSCOPE']
, (err: BusinessError, data: PermissionRequestResult) => {
console.info('data:' + JSON.stringify(data));
console.info('data permissions:' + data.permissions);
console.info('data authResults:' + data.authResults);
})
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
}
}
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onPermissionRequest((event) => {
if (event) {
AlertDialog.show({
title: 'title',
message: 'text',
primaryButton: {
value: 'deny',
action: () => {
event.request.deny();
}
},
secondaryButton: {
value: 'onConfirm',
action: () => {
event.request.grant(event.request.getAccessibleResource());
}
},
autoCancel: false,
cancel: () => {
event.request.deny();
}
})
}
})
}
}
}
```
2.  在前端页面代码中，利用JavaScript调用传感器相关的W3C标准协议接口。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-render-layout--V14
爬取时间: 2025-04-28 00:18:33
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-render-mode-V14
爬取时间: 2025-04-28 00:18:46
来源: Huawei Developer
Web组件支持两种渲染模式。
异步渲染模式（默认）
renderMode: RenderMode.ASYNC_RENDER
异步渲染模式下，Web组件作为图形surface节点，独立送显。建议在仅由Web组件构成的应用页面中使用此模式，有更好的性能和更低的功耗表现。
同步渲染模式
renderMode: RenderMode.SYNC_RENDER
同步渲染模式下，Web组件作为图形canvas节点，Web渲染跟随系统组件一起送显。可以渲染更长Web组件内容，但会消耗更多的性能资源。
接口枚举值定义请查看RenderMode枚举说明。
规格与约束
异步渲染模式
同步渲染模式
使用场景
```typescript
// renderMode.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebHeightPage {
private webviewController: WebviewController = new webview.WebviewController()
build() {
Column() {
Web({
src: "https://www.example.com/",
controller: this.webviewController,
renderMode: RenderMode.ASYNC_RENDER // 设置渲染模式
})
}
}
}
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170357.05320219385063740671546825598190:50001231000000:2800:A19DED5054448039F8085265C959E35557B92B949DAD1B9384D82B41D6304AF0.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-fit-content-V14
爬取时间: 2025-04-28 00:19:00
来源: Huawei Developer
使用Web组件大小自适应页面内容布局模式layoutMode(WebLayoutMode.FIT_CONTENT)时，能使Web组件的大小根据页面内容自适应变化。
适用于Web组件需要根据网页高度撑开，与其他原生组件一起滚动的场景，如：
规格与约束
使用场景
```typescript
// fit_content_test.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebHeightPage {
private webviewController: WebviewController = new webview.WebviewController()
private scroller: Scroller = new Scroller()
build() {
Navigation() {
Column() {
Scroll(this.scroller) {
Column() {
Web({
src: $rawfile("fit_content.html"),
controller: this.webviewController,
renderMode: RenderMode.SYNC_RENDER // 设置为同步渲染模式
})
.layoutMode(WebLayoutMode.FIT_CONTENT) // 设置为Web组件大小自适应页面内容
.overScrollMode(OverScrollMode.NEVER) // 设置过滚动模式为关闭状态
Text("评论区")
.fontSize(28)
.fontColor("#FF0F0F")
.height(100)
.width("100%")
.backgroundColor("#f89f0f")
}
}
}
}
.title("标题栏")
}
}
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170357.94330906211232899029019858442708:50001231000000:2800:65E5BA975DB38C6248AA0D2246D71A5FECBEFCA7554FE993EA3D21C386306B0D.gif)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-router-flash-optimization-V14
爬取时间: 2025-04-28 00:19:14
来源: Huawei Developer
当应用采用Navigation等路由策略导航至Web组件页面时，在网页加载过程中，页面底部可能会出现闪烁现象，这有损用户体验。
闪烁原因
当应用采用Navigation等路由策略导航至Web组件页面时，通常会依据网页端的回调通知来判断是否应隐藏应用侧的原生导航栏。若决定隐藏原生导航栏，Web组件的布局将随即进行调整。这一布局调整过程可简化为如下四个阶段：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170358.91324062943777161830814183954562:50001231000000:2800:E0F2C199D54C7305363F088A2746E81587BA02BE311E9B959D6DED808B9A087D.png)
图中四个状态的说明（从左至右）。
1.  将应用路由至Web页面，页面顶部为原生导航栏，底部则是Web组件，在此情况下，网页能够正常加载。
2.  在网页加载过程中，系统会回调通知应用侧隐藏原生导航栏，以便切换至网页端的导航栏。此时，原生导航栏被隐藏，Web组件的布局随即进行调整。页面底部最初会显露出Web组件的背景色，假设这一颜色为灰色。
3.  网页继续根据新的尺寸加载并显示，首先呈现的是HTML网页的背景色，此处假设为白色。
4.  最后，网页内容完全加载，展现出完整的HTML网页内容。
在以上流程中，如果Web组件的背景色与网页的背景色有差异，在这种跳转过程中就有概率闪烁，闪烁产生的概率大小取决于网页的复杂程度与网络条件。
优化方法
应用可以通过设置Web组件的背景颜色，使其与网页背景颜色保持一致，从而避免视觉闪烁，提升用户体验（如上图示例，可将Web组件的背景色设置为白色）。
在其他类似情况下，例如Web组件默认背景为白色，若网页背景为灰色，则在导航至新的Web页面时可能会出现白色闪烁，将Web组件背景色设置为灰色即可解决此问题。
以下为设置Web组件背景色的接口示例（示例中将Web组件背景色设置为灰色，若不设置，Web组件背景色默认为白色）：
```typescript
Web({ src: $rawfile('xxx.html'),  controller: this.webController})
.backgroundColor(Color.Gray)
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-use-frontend-page-js-V14
爬取时间: 2025-04-28 00:19:27
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-in-app-frontend-page-function-invoking-V14
爬取时间: 2025-04-28 00:19:40
来源: Huawei Developer
应用侧可以通过runJavaScript()和runJavaScriptExt()方法调用前端页面的JavaScript相关函数。
runJavaScript()和runJavaScriptExt()在参数类型上有些差异。runJavaScriptExt()入参类型不仅支持string还支持ArrayBuffer（从文件中获取JavaScript脚本数据），另外可以通过AsyncCallback的方式获取执行结果。
在下面的示例中，点击应用侧的“runJavaScript”按钮时，来触发前端页面的htmlTest()方法。
-  前端页面代码。
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
aboutToAppear() {
// 配置Web开启调试模式
webview.WebviewController.setWebDebuggingAccess(true);
}
build() {
Column() {
Button('runJavaScript')
.onClick(() => {
// 前端页面函数无参时，将param删除。
this.webviewController.runJavaScript('htmlTest(param)');
})
Button('runJavaScriptCodePassed')
.onClick(() => {
// 传递runJavaScript侧代码方法。
this.webviewController.runJavaScript(`function changeColor(){document.getElementById('text').style.color = 'red'}`);
})
Web({ src: $rawfile('index.html'), controller: this.webviewController })
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-in-page-app-function-invoking-V14
爬取时间: 2025-04-28 00:19:53
来源: Huawei Developer
开发者使用Web组件将应用侧代码注册到前端页面中，注册完成之后，前端页面中使用注册的对象名称就可以调用应用侧的函数，实现在前端页面中调用应用侧方法。
注册应用侧代码有两种方式，一种在Web组件初始化调用，使用javaScriptProxy()接口。另外一种在Web组件初始化完成后调用，使用registerJavaScriptProxy()接口, 需要和deleteJavaScriptRegister接口配合使用，防止内存泄漏。
在下面的示例中，将test()方法注册在前端页面中， 该函数可以在前端页面触发运行。
-  javaScriptProxy()接口使用示例如下。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
class testClass {
constructor() {
}
test(): string {
return 'ArkTS Hello World!';
}
}
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
// 声明需要注册的对象
@State testObj: testClass = new testClass();
build() {
Column() {
Button('deleteJavaScriptRegister')
.onClick(() => {
try {
this.webviewController.deleteJavaScriptRegister("testObjName");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
// Web组件加载本地index.html页面
Web({ src: $rawfile('index.html'), controller: this.webviewController})
// 将对象注入到web端
.javaScriptProxy({
object: this.testObj,
name: "testObjName",
methodList: ["test"],
controller: this.webviewController,
// 可选参数
asyncMethodList: [],
permission: '{"javascriptProxyPermission":{"urlPermissionList":[{"scheme":"resource","host":"rawfile","port":"","path":""},' +
'{"scheme":"e","host":"f","port":"g","path":"h"}],"methodList":[{"methodName":"test","urlPermissionList":' +
'[{"scheme":"https","host":"xxx.com","port":"","path":""},{"scheme":"resource","host":"rawfile","port":"","path":""}]},' +
'{"methodName":"test11","urlPermissionList":[{"scheme":"q","host":"r","port":"","path":"t"},' +
'{"scheme":"u","host":"v","port":"","path":""}]}]}}'
})
}
}
}
```
-  应用侧使用registerJavaScriptProxy()接口注册。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
class testClass {
constructor() {
}
test(): string {
return "ArkUI Web Component";
}
toString(): void {
console.log('Web Component toString');
}
}
@Entry
@Component
struct Index {
webviewController: webview.WebviewController = new webview.WebviewController();
@State testObj: testClass = new testClass();
build() {
Column() {
Button('refresh')
.onClick(() => {
try {
this.webviewController.refresh();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('Register JavaScript To Window')
.onClick(() => {
try {
this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"],
// 可选参数, asyncMethodList
[],
// 可选参数, permission
'{"javascriptProxyPermission":{"urlPermissionList":[{"scheme":"resource","host":"rawfile","port":"","path":""},' +
'{"scheme":"e","host":"f","port":"g","path":"h"}],"methodList":[{"methodName":"test","urlPermissionList":' +
'[{"scheme":"https","host":"xxx.com","port":"","path":""},{"scheme":"resource","host":"rawfile","port":"","path":""}]},' +
'{"methodName":"test11","urlPermissionList":[{"scheme":"q","host":"r","port":"","path":"t"},' +
'{"scheme":"u","host":"v","port":"","path":""}]}]}}'
);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('deleteJavaScriptRegister')
.onClick(() => {
try {
this.webviewController.deleteJavaScriptRegister("testObjName");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.webviewController })
}
}
}
```
-  可选参数permission是一个json字符串，示例如下：
```json
{
"javascriptProxyPermission": {
"urlPermissionList": [       // Object级权限，如果匹配，所有Method都授权
{
"scheme": "resource",    // 精确匹配，不能为空
"host": "rawfile",       // 精确匹配，不能为空
"port": "",              // 精确匹配，为空不检查
"path": ""               // 前缀匹配，为空不检查
},
{
"scheme": "https",       // 精确匹配，不能为空
"host": "xxx.com",       // 精确匹配，不能为空
"port": "8080",          // 精确匹配，为空不检查
"path": "a/b/c"          // 前缀匹配，为空不检查
}
],
"methodList": [
{
"methodName": "test",
"urlPermissionList": [   // Method级权限
{
"scheme": "https",   // 精确匹配，不能为空
"host": "xxx.com",   // 精确匹配，不能为空
"port": "",          // 精确匹配，为空不检查
"path": ""           // 前缀匹配，为空不检查
},
{
"scheme": "resource",// 精确匹配，不能为空
"host": "rawfile",   // 精确匹配，不能为空
"port": "",          // 精确匹配，为空不检查
"path": ""           // 前缀匹配，为空不检查
}
]
},
{
"methodName": "test11",
"urlPermissionList": [   // Method级权限
{
"scheme": "q",       // 精确匹配，不能为空
"host": "r",         // 精确匹配，不能为空
"port": "",          // 精确匹配，为空不检查
"path": "t"          // 前缀匹配，为空不检查
},
{
"scheme": "u",       // 精确匹配，不能为空
"host": "v",         // 精确匹配，不能为空
"port": "",          // 精确匹配，为空不检查
"path": ""           // 前缀匹配，为空不检查
}
]
}
]
}
}
```
-  index.html前端页面触发应用侧代码。
复杂类型使用方法
-  应用侧和前端页面之间传递Array。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
class testClass {
constructor() {
}
test(): Array<Number> {
return [1, 2, 3, 4]
}
toString(param: String): void {
console.log('Web Component toString' + param);
}
}
@Entry
@Component
struct Index {
webviewController: webview.WebviewController = new webview.WebviewController();
@State testObj: testClass = new testClass();
build() {
Column() {
Button('refresh')
.onClick(() => {
try {
this.webviewController.refresh();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('Register JavaScript To Window')
.onClick(() => {
try {
this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('deleteJavaScriptRegister')
.onClick(() => {
try {
this.webviewController.deleteJavaScriptRegister("testObjName");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.webviewController })
}
}
}
```
-  应用侧和前端页面之间传递基础类型，非Function等复杂类型。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
class student {
name: string = '';
age: string = '';
}
class testClass {
constructor() {
}
// 传递的基础类型name:"jeck", age:"12"。
test(): student {
let st: student = { name: "jeck", age: "12" };
return st;
}
toString(param: ESObject): void {
console.log('Web Component toString' + param["name"]);
}
}
@Entry
@Component
struct Index {
webviewController: webview.WebviewController = new webview.WebviewController();
@State testObj: testClass = new testClass();
build() {
Column() {
Button('refresh')
.onClick(() => {
try {
this.webviewController.refresh();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('Register JavaScript To Window')
.onClick(() => {
try {
this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('deleteJavaScriptRegister')
.onClick(() => {
try {
this.webviewController.deleteJavaScriptRegister("testObjName");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.webviewController })
}
}
}
```
-  应用侧调用前端页面的Callback。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
class testClass {
constructor() {
}
test(param: Function): void {
param("call callback");
}
toString(param: String): void {
console.log('Web Component toString' + param);
}
}
@Entry
@Component
struct Index {
webviewController: webview.WebviewController = new webview.WebviewController();
@State testObj: testClass = new testClass();
build() {
Column() {
Button('refresh')
.onClick(() => {
try {
this.webviewController.refresh();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('Register JavaScript To Window')
.onClick(() => {
try {
this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('deleteJavaScriptRegister')
.onClick(() => {
try {
this.webviewController.deleteJavaScriptRegister("testObjName");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.webviewController })
}
}
}
```
-  应用侧调用前端页面Object里的Function。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
class testClass {
constructor() {
}
test(param: ESObject): void {
param.hello("call obj func");
}
toString(param: String): void {
console.log('Web Component toString' + param);
}
}
@Entry
@Component
struct Index {
webviewController: webview.WebviewController = new webview.WebviewController();
@State testObj: testClass = new testClass();
build() {
Column() {
Button('refresh')
.onClick(() => {
try {
this.webviewController.refresh();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('Register JavaScript To Window')
.onClick(() => {
try {
this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('deleteJavaScriptRegister')
.onClick(() => {
try {
this.webviewController.deleteJavaScriptRegister("testObjName");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.webviewController })
}
}
}
```
-  前端页面调用应用侧Object里的Function。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
class ObjOther {
methodNameListForJsProxy: string[]
constructor(list: string[]) {
this.methodNameListForJsProxy = list
}
testOther(json: string): void {
console.info(json)
}
}
class testClass {
ObjReturn: ObjOther
constructor() {
this.ObjReturn = new ObjOther(["testOther"]);
}
test(): ESObject {
return this.ObjReturn
}
toString(param: string): void {
console.log('Web Component toString' + param);
}
}
@Entry
@Component
struct Index {
webviewController: webview.WebviewController = new webview.WebviewController();
@State testObj: testClass = new testClass();
build() {
Column() {
Button('refresh')
.onClick(() => {
try {
this.webviewController.refresh();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('Register JavaScript To Window')
.onClick(() => {
try {
this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('deleteJavaScriptRegister')
.onClick(() => {
try {
this.webviewController.deleteJavaScriptRegister("testObjName");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.webviewController })
}
}
}
```
-  Promise场景。 第一种使用方法，在应用侧new Promise。 第二种使用方法，在前端页面new Promise。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
class testClass {
constructor() {
}
test(): Promise<string> {
let p: Promise<string> = new Promise((resolve, reject) => {
setTimeout(() => {
console.log('执行完成');
reject('fail');
}, 10000);
});
return p;
}
toString(param: String): void {
console.log(" " + param);
}
}
@Entry
@Component
struct Index {
webviewController: webview.WebviewController = new webview.WebviewController();
@State testObj: testClass = new testClass();
build() {
Column() {
Button('refresh')
.onClick(() => {
try {
this.webviewController.refresh();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('Register JavaScript To Window')
.onClick(() => {
try {
this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('deleteJavaScriptRegister')
.onClick(() => {
try {
this.webviewController.deleteJavaScriptRegister("testObjName");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.webviewController })
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-app-page-data-channel-V14
爬取时间: 2025-04-28 00:20:07
来源: Huawei Developer
前端页面和应用侧之间可以用createWebMessagePorts()接口创建消息端口来实现两端的通信。
在下面的示例中，应用侧页面中通过createWebMessagePorts方法创建消息端口，再把其中一个端口通过postMessage()接口发送到前端页面，便可以在前端页面和应用侧之间互相发送消息。
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
ports: webview.WebMessagePort[] = [];
@State sendFromEts: string = 'Send this message from ets to HTML';
@State receivedFromHtml: string = 'Display received message send from HTML';
build() {
Column() {
// 展示接收到的来自HTML的内容
Text(this.receivedFromHtml)
// 输入框的内容发送到HTML
TextInput({ placeholder: 'Send this message from ets to HTML' })
.onChange((value: string) => {
this.sendFromEts = value;
})
// 该内容可以放在onPageEnd生命周期中调用。
Button('postMessage')
.onClick(() => {
try {
// 1、创建两个消息端口。
this.ports = this.controller.createWebMessagePorts();
// 2、在应用侧的消息端口(如端口1)上注册回调事件。
this.ports[1].onMessageEvent((result: webview.WebMessage) => {
let msg = 'Got msg from HTML:';
if (typeof (result) === 'string') {
console.info(`received string message from html5, string is: ${result}`);
msg = msg + result;
} else if (typeof (result) === 'object') {
if (result instanceof ArrayBuffer) {
console.info(`received arraybuffer from html5, length is: ${result.byteLength}`);
msg = msg + 'length is ' + result.byteLength;
} else {
console.info('not support');
}
} else {
console.info('not support');
}
this.receivedFromHtml = msg;
})
// 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
this.controller.postMessage('__init_port__', [this.ports[0]], '*');
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
// 4、使用应用侧的端口给另一个已经发送到html的端口发送消息。
Button('SendDataToHTML')
.onClick(() => {
try {
if (this.ports && this.ports[1]) {
this.ports[1].postMessageEvent(this.sendFromEts);
} else {
console.error(`ports is null, Please initialize first`);
}
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.controller })
}
}
}
```
-  前端页面代码。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkweb-ndk-jsbridge-V14
爬取时间: 2025-04-28 00:20:20
来源: Huawei Developer
本指导适用于ArkWeb应用侧与前端网页通信场景，开发者可根据应用架构选择使用ArkWeb Native接口完成业务通信机制（以下简称Native JSBridge）。
适用的应用架构
应用使用ArkTS、C++语言混合开发，或本身应用架构较贴近于小程序架构，自带C++侧环境，推荐使用ArkWeb在Native侧提供的ArkWeb_ControllerAPI、ArkWeb_ComponentAPI实现JSBridge功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170358.26969212465920000883102292846931:50001231000000:2800:FA658FD4A3C1DB5A7464984638AB3ACD348B939962EE44F2DF514550FFF4755A.png)
上图展示了具有普遍适用性的小程序的通用架构。在这一架构中，逻辑层依赖于应用程序自带的JavaScript运行时，该运行时在一个已有的C++环境中运行。通过Native接口，逻辑层能够直接在C++环境中与视图层（其中ArkWeb充当渲染器）进行通信，无需回退至ArkTS环境使用ArkTS JSBridge接口。
左图是使用ArkTS JSBridge接口构建小程序的方案，如红框所示，应用需要先调用到ArkTS环境，再调用到C++环境。右图是使用Native JSBridge接口构建小程序的方案，不需要ArkTS环境和C++环境的切换，执行效率更高。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170358.43190478897138633792149714671347:50001231000000:2800:7A5C5D455E3DAE0154C987D682851C6CA6FD5833A8E84E0078D7AFF4C083D1EA.png)
Native JSBridge方案可以解决ArkTS环境的冗余切换，同时允许回调在非UI线程上运行，避免造成UI阻塞。
使用Native接口实现JSBridge通信
使用Native接口绑定ArkWeb
-  ArkWeb组件声明在ArkTS侧，需要用户自定义一个标识webTag，并将webTag通过Node-API传至应用Native侧，后续ArkWeb Native接口使用，均需webTag作为对应组件的唯一标识。
-  ArkTS侧
-  C++侧
使用Native接口获取API结构体
ArkWeb Native侧得先获取API结构体，才能调用结构体里的Native API。ArkWeb Native侧API通过函数OH_ArkWeb_GetNativeAPI获取，根据入参type不同，可分别获取ArkWeb_ControllerAPI、ArkWeb_ComponentAPI函数指针结构体。其中ArkWeb_ControllerAPI对应ArkTS侧web_webview.WebviewController API，ArkWeb_ComponentAPI对应ArkTS侧ArkWeb组件API。
Native侧注册组件生命周期回调
通过ArkWeb_ComponentAPI注册组件生命周期回调，在调用API前建议通过ARKWEB_MEMBER_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。
前端页面调用应用侧函数
通过registerJavaScriptProxy将应用侧函数注册至前端页面，推荐在onControllerAttached回调中注册，其它时机注册需要手动调用refresh才能生效。
应用侧调用前端页面函数
通过runJavaScript调用前端页面函数。
完整示例
-  前端页面代码
-  ArkTS侧代码
-  Node-API侧暴露ArkTS接口
-  Node-API侧编译配置entry/src/main/cpp/CMakeLists.txt
-  Node-API层代码
-  Native侧业务代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkweb-ndk-page-data-channel-V14
爬取时间: 2025-04-28 00:20:34
来源: Huawei Developer
前端页面和应用侧之间可以使用Native方法实现两端通信（以下简称Native PostWebMessage），可解决ArkTS环境的冗余切换，同时允许发送消息、回调在非UI线程上运行，避免造成UI阻塞。当前只支持string和buffer数据类型。
适用的应用架构
应用使用ArkTS、C++语言混合开发，或本身应用架构较贴近于小程序架构，自带C++侧环境，推荐使用ArkWeb在Native侧提供的ArkWeb_ControllerAPI、ArkWeb_WebMessageAPI、ArkWeb_WebMessagePortAPI实现PostWebMessage功能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170358.66970860898686510786901296393931:50001231000000:2800:3AD097A66A9F5BEAF503407D29D570A0A10F1437F49B4290CA5755CAAADEBFE9.png)
上图展示了具有普遍适用性的小程序的通用架构。在这一架构中，逻辑层依赖于应用程序自带的JavaScript运行时，该运行时在一个已有的C++环境中运行。通过Native接口，逻辑层能够直接在C++环境中与视图层（其中ArkWeb充当渲染器）进行通信，无需回退至ArkTS环境使用ArkTS PostWebMessage接口。
左图是使用ArkTS PostWebMessage接口构建小程序的方案，，如红框所示，应用需要先调用到ArkTS环境，再调用到C++环境。右图是使用Native PostWebMessage接口构建小程序的方案，不需要ArkTS环境和C++环境的切换，执行效率更高。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170358.48615412255435311981702575743649:50001231000000:2800:7F2EBC1746B421EF6C2EB12794E98376775C593D5BEC2D1C414760B55FABD2CB.png)
使用Native接口实现PostWebMessage通信
使用Native接口绑定ArkWeb
-  ArkWeb组件声明在ArkTS侧，需要用户自定义一个标识webTag，并将webTag通过Node-API传至应用C++侧。后续ArkWeb Native接口使用时，均需webTag作为对应组件的唯一标识。
-  ArkTS侧
```typescript
import { webview } from '@kit.ArkWeb';
// 自定义webTag，在WebviewController创建时作为入参传入，建立controller与webTag的映射关系
webTag: string = 'ArkWeb1';
controller: webview.WebviewController = new webview.WebviewController(this.webTag);
...
// aboutToAppear中将webTag通过Node-API接口传入C++侧，作为C++侧ArkWeb组件的唯一标识
aboutToAppear() {
console.info("aboutToAppear")
// 初始化web ndk
testNapi.nativeWebInit(this.webTag);
}
...
```
使用Native接口获取API结构体
ArkWeb Native侧得先获取API结构体，才能调用结构体里的Native API。ArkWeb Native侧API通过函数OH_ArkWeb_GetNativeAPI获取，根据入参type不同，可获取对应的函数指针结构体。其中本指导涉及ArkWeb_ControllerAPI、ArkWeb_WebMessageAPI、ArkWeb_WebMessagePortAPI。
完整示例
在调用API前建议通过ARKWEB_MEMBER_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。createWebMessagePorts、postWebMessage、close需运行在UI线程。
-  前端页面代码
-  ArkTS侧代码
-  Node-API侧暴露ArkTS接口
-  Node-API侧编译配置
-  Node-API层代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-manage-page-interaction-V14
爬取时间: 2025-04-28 00:20:48
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-nested-scrolling-V14
爬取时间: 2025-04-28 00:21:02
来源: Huawei Developer
Web组件嵌套滚动的典型应用场景为，在一个页面中，有多个独立的区域需要进行滚动，当用户滚动Web区域内容时，可带动其他滚动区域进行滚动，以达到上下滑动页面的用户体验。
内嵌在可滚动容器（Scroll、List...）中的Web组件，接收到滑动手势事件，需要对接ArkUI框架的NestedScrollMode枚举类型，使得Web组件可以嵌套ArkUI可滚动容器，进行嵌套滚动。开发者可以在Web组件创建时，使用nestedScroll属性接口指定默认的嵌套滚动模式，也允许在过程中动态改变嵌套滚动的模式。
nestedScroll入参为一个NestedScrollOptions对象，该对象具有两个属性，分别为scrollForward和scrollBackward，每一个属性都为一个NestedScrollMode枚举类型。
当Web组件被多个可滚动容器组件嵌套时，未被Web组件消费的与父组件方向一致的偏移量、速度值将被传递给距Web组件最近且方向一致的父组件，使得父组件可以继续滚动。一次手势滑动只能沿X轴或Y轴一个方向嵌套滚动，当手势斜向滑动时，滚动方向为偏移量或速度在X轴、Y轴绝对值较大的方向；当偏移量或速度绝对值在X轴、Y轴绝对值相同时，滚动方向为距Web组件最近的可滚动组件的方向。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct NestedScroll {
private scrollerForScroll: Scroller = new Scroller();
controller: webview.WebviewController = new webview.WebviewController();
controller2: webview.WebviewController = new webview.WebviewController();
// NestedScrollMode设置成SELF_ONLY时，Web网页滚动到页面边缘后，不与父组件联动，父组件仍无法滚动。
@State NestedScrollMode0: NestedScrollMode = NestedScrollMode.SELF_ONLY;
// NestedScrollMode设置成SELF_FIRST时，Web网页滚动到页面边缘后，父组件继续滚动。
@State NestedScrollMode1: NestedScrollMode = NestedScrollMode.SELF_FIRST;
// NestedScrollMode设置为PARENT_FIRST时，父组件先滚动，滚动至边缘后通知Web继续滚动。
@State NestedScrollMode2: NestedScrollMode = NestedScrollMode.PARENT_FIRST;
// NestedScrollMode设置为PARALLEL时，父组件与Web同时滚动。
@State NestedScrollMode3: NestedScrollMode = NestedScrollMode.PARALLEL;
@State NestedScrollModeF: NestedScrollMode = NestedScrollMode.SELF_FIRST;
@State NestedScrollModeB: NestedScrollMode = NestedScrollMode.SELF_FIRST;
// scroll竖向的滚动
@State ScrollDirection: ScrollDirection = ScrollDirection.Vertical;
build() {
Flex() {
Scroll(this.scrollerForScroll) {
Column({ space: 5 }) {
Row({}) {
Text('切换前滚动模式').fontSize(5)
Button('SELF_ONLY').onClick((event: ClickEvent) => {
this.NestedScrollModeF = this.NestedScrollMode0
}).fontSize(5)
Button('SELF_FIRST').onClick((event: ClickEvent) => {
this.NestedScrollModeF = this.NestedScrollMode1
}).fontSize(5)
Button('PARENT_FIRST').onClick((event: ClickEvent) => {
this.NestedScrollModeF = this.NestedScrollMode2
}).fontSize(5)
Button('PARALLEL').onClick((event: ClickEvent) => {
this.NestedScrollModeF = this.NestedScrollMode3
}).fontSize(5)
}
Row({}) {
Text('切换后滚动模式').fontSize(5)
Button('SELF_ONLY').onClick((event: ClickEvent) => {
this.NestedScrollModeB = this.NestedScrollMode0
}).fontSize(5)
Button('SELF_FIRST').onClick((event: ClickEvent) => {
this.NestedScrollModeB = this.NestedScrollMode1
}).fontSize(5)
Button('PARENT_FIRST').onClick((event: ClickEvent) => {
this.NestedScrollModeB = this.NestedScrollMode2
}).fontSize(5)
Button('PARALLEL').onClick((event: ClickEvent) => {
this.NestedScrollModeB = this.NestedScrollMode3
}).fontSize(5)
}
Text('当前内嵌前滚动模式 scrollForward ---' + `${this.NestedScrollModeF}`).fontSize(10)
Text('当前内嵌后滚动模式  scrollBackward ---' + `${this.NestedScrollModeB}`).fontSize(10)
Text("Scroll Area")
.width("100%")
.height("10%")
.backgroundColor(0X330000FF)
.fontSize(16)
.textAlign(TextAlign.Center)
Text("Scroll Area")
.width("100%")
.height("10%")
.backgroundColor(0X330000FF)
.fontSize(16)
.textAlign(TextAlign.Center)
Text("Scroll Area")
.width("100%")
.height("10%")
.backgroundColor(0X330000FF)
.fontSize(16)
.textAlign(TextAlign.Center)
Web({ src: "www.example.com", controller: this.controller })
.nestedScroll({
scrollForward: this.NestedScrollModeF,
scrollBackward: this.NestedScrollModeB,
})
.height("40%")
.width("100%")
Text("Scroll Area")
.width("100%")
.height("20%")
.backgroundColor(0X330000FF)
.fontSize(16)
.textAlign(TextAlign.Center)
Text("Scroll Area")
.width("100%")
.height("20%")
.backgroundColor(0X330000FF)
.fontSize(16)
.textAlign(TextAlign.Center)
Web({ src: "www.example.com", controller: this.controller2 })
.nestedScroll({
scrollForward: this.NestedScrollModeF,
scrollBackward: this.NestedScrollModeB,
})
.height("40%")
.width("90%")
Text("Scroll Area")
.width("100%")
.height("20%")
.backgroundColor(0X330000FF)
.fontSize(16)
.textAlign(TextAlign.Center)
}.width("95%").border({ width: 5 })
}
.width("100%").height("120%").border({ width: 5 }).scrollable(this.ScrollDirection)
}.width('100%').height('100%').backgroundColor(0xDCDCDC).padding(20)
}
}
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170359.45702106444955873144151995449035:50001231000000:2800:DF6BB3DAC4EF3A72AA4BB4AD90360B15C2A28D2008428A6AD8D2E80B74FD8AFF.gif)
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-content-scrolling-V14
爬取时间: 2025-04-28 00:21:16
来源: Huawei Developer
ArkWeb中的Webview.WebviewController提供scrollTo和scrollBy接口。
当Web显示的内容大小远远大于组件大小时，用户可以通过scrollTo和scrollBy对Web页面中显示的内容进行滚动来显示没有显示的部分，且可以生成动画滚动效果。目前动画效果不支持手势打断，可以通过再次执行一个时间约为0的动画进行强制打断。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('scrollTo')
.onClick(() => {
try {
this.controller.scrollTo(50, 50, 500);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
.margin(10)
Button('scrollBy')
.onClick(() => {
try {
this.controller.scrollBy(50, 50, 500);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
.margin(10)
Button('scrollStop')
.onClick(() => {
try {
this.controller.scrollBy(0, 0, 1);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
.margin(10)
Web({ src: $rawfile('index.html'), controller: this.controller })
}
}
}
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170359.62298695720818085584838524335759:50001231000000:2800:3C5B69812D516A7147A7873D3FCB53CF32F73AF7EAF84DC9999DA889B23284E3.gif)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-docking-softkeyboard-V14
爬取时间: 2025-04-28 00:21:29
来源: Huawei Developer
开发者能够通过Web组件对接软键盘，来处理系统软键盘的显示与交互问题，同时实现软键盘的自定义功能。主要有以下场景。
Web页面输入框输入与软键盘交互的W3C标准支持
为支持Web页面与系统软键盘、自定义软键盘等的良好交互，ArkWeb遵循并实现了W3C规范中的以下输入控制属性：
-  type属性 type属性定义了input元素的类型，影响输入的验证、显示方式和键盘类型。常见的type值包括：
-  inputmode属性 inputmode属性用于配置输入法类型。
-  enterkeyhint属性 enterkeyhint属性用于指定移动设备虚拟键盘上回车键的显示方式。
| type值 | 描述 |
| --- | --- |
| text | 默认值。普通文本输入 |
| number | 数字输入 |
| email | 电子邮件地址输入 |
| password | 密码输入 |
| tel | 电话号码输入 |
| url | URL输入 |
| date | 日期选择器 |
| time | 时间选择器 |
| checkbox | 复选框 |
| radio | 单选按钮 |
| file | 文件上传 |
| submit | 提交按钮 |
| reset | 重置按钮 |
| button | 普通按钮 |
| inputmode | 描述 |
| --- | --- |
| decimal | 只显示数字键盘，通常还有一个逗号键 |
| email | 文本键盘，键通常用于电子邮件地址，如[@]。 |
| none | 不应出现键盘 |
| numeric | 只显示数字键盘 |
| search | 文本键盘，[enter]键通常显示为[go] |
| tel | 只显示数字键盘，通常还有[+]、[*]和[#]键。 |
| text | 默认。文本键盘 |
| url | 文本键盘，键通常用于网址，如[.]和[/]，以及特殊的[.com]键，或者其他通常用于本地设置的域名结束符。 |
| enterkeyhint值 | 描述 |
| --- | --- |
| enter | 显示默认的回车键 |
| done | 表示输入完成 |
| go | 表示跳转或执行 |
| next | 进入下一个输入字段 |
| previous | 返回上一个输入字段 |
| search | 执行搜索 |
| send | 发送信息 |
用户在点击网页输入框时，会在屏幕下方弹出系统默认的软键盘（输入法），并可进行文字输入上屏。
type属性更广泛，不仅影响键盘显示，还会影响输入验证和元素的外观。
inputmode主要用于优化移动设备上的键盘输入体验，不会改变input的基本行为或验证。
设置软键盘避让模式
在移动设备上，支持设置Web页面的软键盘避让模式。
（1）在应用代码中设置UIContext的软键盘避让模式。
```typescript
// EntryAbility.ets
import { KeyboardAvoidMode } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
onWindowStageCreate(windowStage: window.WindowStage) {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
windowStage.loadContent('pages/Index', (err, data) => {
let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
// 设置虚拟键盘抬起时压缩页面大小为减去键盘的高度
windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
if (err.code) {
hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
});
}
```
（2）再在Web组件中拉起软键盘。
```typescript
//Index.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct KeyboardAvoidExample {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Row().height("50%").width("100%").backgroundColor(Color.Gray)
Web({ src: $rawfile("index.html"),controller: this.controller})
Text("I can see the bottom of the page").width("100%").textAlign(TextAlign.Center).backgroundColor(Color.Pink).layoutWeight(1)
}.width('100%').height("100%")
}
}
```
此时ArkWeb组件跟随ArkUI重新布局，效果如图1、图2所示。
图1Web组件网页默认软键盘避让模式
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170359.99845191519623526954314120787792:50001231000000:2800:B1D7280CA54AF56B89D0F2FDA0BF56CB3F4F35D37D5C2C8E402BA6C99F83D34E.png)
图2Web组件网页跟随Arkui软键盘避让模式
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170359.97299348473425646983692179987357:50001231000000:2800:240B21F172F34F191ADDF018269C04E19E2F1E5F55074221B456E0CC768BA22A.png)
2.在UIContext的键盘避让模式为Offset模式情况下，应用可通过WebKeyboardAvoidMode()设置ArkWeb组件的键盘避让模式。Web组件的WebKeyboardAvoidMode()接口优先级高于W3C侧virtualKeyboard.overlayContens。
可视视口指用户正在看到的网站的区域，该区域的宽度等于移动设备的浏览器窗口的宽度。
布局视口指网页本身的宽度。
（1）在应用代码中设置ArkWeb的软键盘避让模式。
```typescript
// Index.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct KeyboardAvoidExample {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Row().height("50%").width("100%").backgroundColor(Color.Gray)
Web({ src: $rawfile("index.html"),controller: this.controller})
.keyboardAvoidMode(WebKeyboardAvoidMode.OVERLAYS_CONTENT) //此时ArkWeb组件不会调整任何视口的大小大小
Text("I can see the bottom of the page").width("100%").textAlign(TextAlign.Center).backgroundColor(Color.Pink).layoutWeight(1)
}.width('100%').height("100%")
}
}
```
此时ArkWeb组件根据自身的避让模式进行避让，效果如图3所示。
图3Web组件网页自身软键盘避让模式
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170359.98797456106956116096593074657621:50001231000000:2800:B2F123F06A3FFB7FD2FE935DB130465D061256B6EF7F02390695CB22CCBD12D9.png)
与其他Web组件行为的交叉场景：
| 交叉场景 | 规格 |
| --- | --- |
| 同层渲染 | 同层Web：软键盘避让行为与普通场景行为一致 同层原生组件：由ArkUI负责软键盘避让模式。 |
| 离屏创建组件 | 默认使用与非离屏创建一致的软键盘避让模式 在上树前设置其他避让模式可需生效。 |
| customDialog | customDialog自身避让。 |
| 折叠屏 | 软键盘避让行为与普通场景行为一致 软件键盘需跟随屏幕开合状态进展开合变化。 |
| 软键盘托管 | 软键盘避让行为与普通场景行为一致。 |
| Web嵌套滚动 | 嵌套滚动场景下不推荐使用Web软键盘避让，包括RESIZE_VISUAL与RESIZE_CONTENT。 |
拦截系统软键盘与自定义软键盘输入
应用能够通过调用onInterceptKeyboardAttach来拦截系统软键盘的弹出。在网页中，当可编辑元素如input标签即将触发软键盘显示时，onInterceptKeyboardAttach会被回调。应用可利用此接口来控制软键盘的显示，包括使用系统默认软键盘、定制带有特定Enter键的软键盘，或是完全自定义软键盘。借助这一功能，开发者能够实现对软键盘的灵活管理。
```typescript
// Index.ets
import { webview } from '@kit.ArkWeb';
import { inputMethodEngine } from '@kit.IMEKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
webKeyboardController: WebKeyboardController = new WebKeyboardController()
inputAttributeMap: Map<string, number> = new Map([
['UNSPECIFIED', inputMethodEngine.ENTER_KEY_TYPE_UNSPECIFIED],
['GO', inputMethodEngine.ENTER_KEY_TYPE_GO],
['SEARCH', inputMethodEngine.ENTER_KEY_TYPE_SEARCH],
['SEND', inputMethodEngine.ENTER_KEY_TYPE_SEND],
['NEXT', inputMethodEngine.ENTER_KEY_TYPE_NEXT],
['DONE', inputMethodEngine.ENTER_KEY_TYPE_DONE],
['PREVIOUS', inputMethodEngine.ENTER_KEY_TYPE_PREVIOUS]
])
/**
* 自定义键盘组件Builder
*/
@Builder
customKeyboardBuilder() {
// 这里实现自定义键盘组件，对接WebKeyboardController实现输入、删除、关闭等操作。
Row() {
Text("完成")
.fontSize(20)
.fontColor(Color.Blue)
.onClick(() => {
this.webKeyboardController.close();
})
// 插入字符。
Button("insertText").onClick(() => {
this.webKeyboardController.insertText('insert ');
}).margin({
bottom: 200,
})
// 从后往前删除length参数指定长度的字符。
Button("deleteForward").onClick(() => {
this.webKeyboardController.deleteForward(1);
}).margin({
bottom: 200,
})
// 从前往后删除length参数指定长度的字符。
Button("deleteBackward").onClick(() => {
this.webKeyboardController.deleteBackward(1);
}).margin({
left: -220,
})
// 插入功能按键。
Button("sendFunctionKey").onClick(() => {
this.webKeyboardController.sendFunctionKey(6);
})
}
}
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onInterceptKeyboardAttach((KeyboardCallbackInfo) => {
// option初始化，默认使用系统默认键盘
let option: WebKeyboardOptions = {
useSystemKeyboard: true,
};
if (!KeyboardCallbackInfo) {
return option;
}
// 保存WebKeyboardController，使用自定义键盘时候，需要使用该handler控制输入、删除、软键盘关闭等行为
this.webKeyboardController = KeyboardCallbackInfo.controller
let attributes: Record<string, string> = KeyboardCallbackInfo.attributes
// 遍历attributes
let attributeKeys = Object.keys(attributes)
for (let i = 0; i < attributeKeys.length; i++) {
console.log('WebCustomKeyboard key = ' + attributeKeys[i] + ', value = ' + attributes[attributeKeys[i]])
}
if (attributes) {
if (attributes['data-keyboard'] == 'customKeyboard') {
// 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有data-keyboard，且值为customKeyboard，则使用自定义键盘
console.log('WebCustomKeyboard use custom keyboard')
option.useSystemKeyboard = false;
// 设置自定义键盘builder
option.customKeyboard = () => {
this.customKeyboardBuilder()
}
return option;
}
if (attributes['keyboard-return'] != undefined) {
// 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有keyboard-return，使用系统键盘，并且指定系统软键盘enterKey类型
option.useSystemKeyboard = true;
let enterKeyType: number | undefined = this.inputAttributeMap.get(attributes['keyboard-return'])
if (enterKeyType != undefined) {
option.enterKeyType = enterKeyType
}
return option;
}
}
return option;
})
}
}
}
```
ArkWeb自定义键盘示例效果如图4、图5、图6所示。
图4ArkWeb自定义键盘数字键盘
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170359.58301950797701569243259428370196:50001231000000:2800:442210FB000CBBCFB09628382BE17E55B9CBB3E2252A0FBBC27F08A98D139205.png)
图5ArkWeb自定义键盘字母键盘
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170359.46606841191323737152300175750652:50001231000000:2800:75908F4A24DE43D182D1A5B41B4F4C6B74A5A3C8823CFD54050DBA4C002618B8.png)
图6ArkWeb自定义键盘符号键盘
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170359.31702640984901702201001623098741:50001231000000:2800:47A71BA5BDDA45875AE3E52EF2FB7252C09ADB058BC21C34B0B9A5DE8405E535.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-focus-V14
爬取时间: 2025-04-28 00:21:42
来源: Huawei Developer
开发者可利用Web组件的焦点管理功能，有效管理Web组件的聚焦与失焦，同时利用H5侧的W3C标准接口，管理网页界面上唯一可交互的元素聚焦与失焦。
-  Web组件与ArkUI组件焦点控制的常用接口及其使用场景：
-  Web组件内H5元素焦点控制的常用接口及其使用场景：
基础概念
Web组件焦点、焦点链和走焦的详情说明请参考ArkUI焦点基础概念。
Web组件走焦规范
根据走焦的触发方式，可以分为主动走焦和被动走焦，Web组件走焦规范详情参考ArkUI走焦规范。
主动走焦
指开发者或用户主观行为导致的焦点移动。包括：使用requestFocus申请焦点、外接键盘的按键走焦（TAB键/Shift+TAB键）、点击申请焦点（手势/鼠标/触摸板）等导致的焦点转移。
-  requestFocus 详见Web组件与ArkUI组件焦点控制，可以主动将焦点转移到Web组件上。
-  按键走焦
-  点击申请获焦 开发者或用户可通过手势、鼠标或触摸板点击Web组件，使其主动获得焦点。当具体点击到Web组件内的某个元素时，该元素能够获得焦点，例如，点击网页内的输入框，可使其从不可编辑状态转变为可编辑状态，并激活输入法。
被动走焦
被动走焦指焦点因系统获其他操作而转移，无需开发者直接干预，是焦点系统的默认行为。
目前会被动走焦的场景有：
-  组件删除：当焦点所在的Web组件被移除时，系统会按照先向后再向前的原则，将焦点转移至相邻的同级组件。倘若所有同级组件均无法获取焦点，则焦点将被释放，并提示其父级组件接管焦点处理。
-  属性变更：如果将处于焦点状态的组件的focusable或enabled属性设置为false，或者将visibility属性设置为不可见，系统会自动将焦点转移到其他可获得焦点的组件上，转移方式同组件删除。
-  Web组件不可见：ArkWeb获焦后，应用前后台切换、页面切换、Navigation导航等场景，ArkWeb会失焦再获焦。
-  Web组件加载网页：ArkWeb通过src、loadUrl、loadData加载网页，默认会获取焦点，但如果此时web组件为不可获焦状态则会获焦失败（常见的不可获焦状态原因有：过场动画过程中父组件不可获焦、应用侧设置了web组件或其父组件不可获焦属性等），应用侧可以调用主动请求焦点接口requestFocus再次尝试使web组件获焦。当获焦成功后，应用侧onFocus、w3c focus事件均会上报。
-  autofocus样式：设置了autofocus样式的元素网页完成加载时默认获焦。若该元素支持文字输入，则输入框会有光标闪烁，但不拉起软键盘。
-  菜单弹出：ArkUI的overlay属性类型组件默认抢焦，在与此类组件结合的ArkWeb场景中（menu、datepicker、timepicker、下拉框、弹窗等），ArkWeb均会失焦。
Web组件与ArkUI组件焦点控制
示例：
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
controller2: webview.WebviewController = new webview.WebviewController();
@State webborderColor: Color = Color.Red;
@State webborderColor2: Color = Color.Red;
build() {
Column() {
Row() {
Button('web1 requestFocus')
.onClick(() => {
try {
this.controller.requestFocus();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
});
Button('web2 requestFocus')
.onClick(() => {
try {
this.controller2.requestFocus();
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
});
}
Web({ src: 'www.example.com', controller: this.controller })
.onFocus(() => {
this.webborderColor = Color.Green;
})
.onBlur(() => {
this.webborderColor = Color.Red;
})
.margin(3)
.borderWidth(10)
.borderColor(this.webborderColor)
.height("45%")
Web({ src: 'www.example.com', controller: this.controller2 })
.onFocus(() => {
this.webborderColor2 = Color.Green;
})
.onBlur(() => {
this.webborderColor2 = Color.Red;
})
.margin(3)
.borderWidth(10)
.borderColor(this.webborderColor2)
.height("45%")
}
}
}
```
示例图1组件焦点获焦/失焦事件
通过requestfocus接口主动请求获焦，并监听通用接口onFocus、onBlur事件，改变Web组件边框颜色。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170400.37785183330891830387313911397767:50001231000000:2800:8734FA0676E1F10C36B7B57B56F2E56782C37BD268BF25F3262354CC3E659E08.gif)
Web组件内H5元素焦点控制
在文档或对话框中，最多只能有一个元素具有 autofocus 属性。如果应用于多个元素，第一个元素将获得焦点。
示例：
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: $rawfile("test.html"), controller: this.controller })
}
}
}
```
示例图2Web组件内元素焦点获焦/失焦事件
通过监听W3C接口focus、blur事件，改变输入背景色。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170400.44343861097209745611332019593208:50001231000000:2800:EBA0910B85125042507E75304EE52C96126DDA5C225E9DA6EC36C7256039B049.gif)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-manage-cyber-security-privacy-V14
爬取时间: 2025-04-28 00:21:55
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-cross-origin-V14
爬取时间: 2025-04-28 00:22:08
来源: Huawei Developer
拦截本地资源跨域
为了提高安全性，ArkWeb内核不允许file协议或者resource协议访问URL上下文中来自跨域的请求。因此，在使用Web组件加载本地离线资源的时候，Web组件会拦截file协议和resource协议的跨域访问。可以通过方法二设置一个路径列表，再使用file协议访问该路径列表中的资源，允许跨域访问本地文件。当Web组件无法访问本地跨域资源时，开发者可以在DevTools控制台中看到类似以下报错信息：
本地资源跨域问题解决方法
-  方法一 为了使Web组件能够成功访问跨域资源，开发者应采用http或https等协议，替代原先使用的file或resource协议进行加载。其中，替代的url域名为自定义构造的仅供个人或者组织使用的域名，以避免与互联网上实际存在的域名产生冲突。同时，开发者需利用Web组件的onInterceptRequest方法，对本地资源进行拦截和相应的替换。 以下结合示例说明如何解决本地资源跨域访问失败的问题。其中，index.html和js/script.js置于工程中的rawfile目录下。如果使用resource协议访问index.html，js/script.js将因跨域而被拦截，无法加载。在示例中，使用https://www.example.com/域名替换了原本的resource协议，同时利用onInterceptRequest接口替换资源，使得js/script.js可以成功加载，从而解决了跨域拦截的问题。
```typescript
// main/ets/pages/Index.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
webviewController: webview.WebviewController = new webview.WebviewController();
// 构造域名和本地文件的映射表
schemeMap = new Map([
["https://www.example.com/index.html", "index.html"],
["https://www.example.com/js/script.js", "js/script.js"],
])
// 构造本地文件和构造返回的格式mimeType
mimeTypeMap = new Map([
["index.html", 'text/html'],
["js/script.js", "text/javascript"]
])
build() {
Row() {
Column() {
// 针对本地index.html,使用http或者https协议代替file协议或者resource协议，并且构造一个属于自己的域名。
// 本例中构造www.example.com为例。
Web({ src: "https://www.example.com/index.html", controller: this.webviewController })
.javaScriptAccess(true)
.fileAccess(true)
.domStorageAccess(true)
.geolocationAccess(true)
.width("100%")
.height("100%")
.onInterceptRequest((event) => {
if (!event) {
return;
}
// 此处匹配自己想要加载的本地离线资源，进行资源拦截替换，绕过跨域
if (this.schemeMap.has(event.request.getRequestUrl())) {
let rawfileName: string = this.schemeMap.get(event.request.getRequestUrl())!;
let mimeType = this.mimeTypeMap.get(rawfileName);
if (typeof mimeType === 'string') {
let response = new WebResourceResponse();
// 构造响应数据，如果本地文件在rawfile下，可以通过如下方式设置
response.setResponseData($rawfile(rawfileName));
response.setResponseEncoding('utf-8');
response.setResponseMimeType(mimeType);
response.setResponseCode(200);
response.setReasonMessage('OK');
response.setResponseIsReady(true);
return response;
}
}
return null;
})
}
.width('100%')
}
.height('100%')
}
}
```
-  方法二 通过setPathAllowingUniversalAccess设置一个路径列表。当使用file协议访问该列表中的资源时，允许进行跨域访问本地文件。此外，一旦设置了路径列表，file协议将仅限于访问列表内的资源(此时，fileAccess的行为将会被此接口行为覆盖)。路径列表中的路径必须符合以下任一路径格式： 1.应用文件目录通过Context.filesDir获取，其子目录示例如下： 2.应用资源目录通过Context.resourceDir获取，其子目录示例如下： 当路径列表中的任一路径不满足上述条件时，系统将抛出异常码401，并判定路径列表设置失败。若设置的路径列表为空，file协议的可访问范围将遵循fileAccess的规则，具体示例如下。
```typescript
// main/ets/pages/Index.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: WebviewController = new webview.WebviewController();
build() {
Row() {
Web({ src: "", controller: this.controller })
.onControllerAttached(() => {
try {
// 设置允许可以跨域访问的路径列表
this.controller.setPathAllowingUniversalAccess([
getContext().resourceDir,
getContext().filesDir + "/example"
])
this.controller.loadUrl("file://" + getContext().resourceDir + "/index.html")
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as   BusinessError).message}`);
}
})
.javaScriptAccess(true)
.fileAccess(true)
.domStorageAccess(true)
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-intelligent-tracking-prevention-V14
爬取时间: 2025-04-28 00:22:22
来源: Huawei Developer
Web组件支持智能防跟踪功能，即跟踪型网站作为三方插入别的网页时，其发送的网络请求禁止携带cookie。
-  通过调用enableIntelligentTrackingPrevention接口使能或者关闭相应Web组件的智能防跟踪功能，默认情况下该功能未启用。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('enableIntelligentTrackingPrevention')
.onClick(() => {
try {
this.controller.enableIntelligentTrackingPrevention(true);
console.log("enableIntelligentTrackingPrevention: true");
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
-  通过调用isIntelligentTrackingPreventionEnabled接口判断当前Web组件是否开启了智能防跟踪功能。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('isIntelligentTrackingPreventionEnabled')
.onClick(() => {
try {
let result = this.controller.isIntelligentTrackingPreventionEnabled();
console.log("result: " + result);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
-  通过调用onIntelligentTrackingPreventionResult接口，以回调的方式异步获取拦截的跟踪型网站的域名和访问的网站域名信息。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
// 需要打开智能防跟踪功能，才会触发onIntelligentTrackingPreventionResult回调
Button('enableIntelligentTrackingPrevention')
.onClick(() => {
try {
this.controller.enableIntelligentTrackingPrevention(true);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
.onIntelligentTrackingPreventionResult((details) => {
console.log("onIntelligentTrackingPreventionResult: [websiteHost]= " + details.host +
", [trackerHost]=" + details.trackerHost);
})
}
}
}
```
同时，智能防跟踪功能提供了一组接口，用于设置需要绕过智能防跟踪功能的域名列表。这些接口设置的域名列表是整个应用生效，而非某个Web组件。
-  通过调用addIntelligentTrackingPreventionBypassingList接口设置需要绕过智能防跟踪功能的域名列表。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('addIntelligentTrackingPreventionBypassingList')
.onClick(() => {
try {
let hostList = ["www.test1.com", "www.test2.com", "www.test3.com"];
webview.WebviewController.addIntelligentTrackingPreventionBypassingList(hostList);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
-  通过调用removeIntelligentTrackingPreventionBypassingList接口移除通过addIntelligentTrackingPreventionBypassingList接口设置的部分域名列表。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('removeIntelligentTrackingPreventionBypassingList')
.onClick(() => {
try {
let hostList = [ "www.test1.com", "www.test2.com" ];
webview.WebviewController.removeIntelligentTrackingPreventionBypassingList(hostList);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
-  通过调用clearIntelligentTrackingPreventionBypassingList接口清除通过addIntelligentTrackingPreventionBypassingList接口设置的所有域名。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('clearIntelligentTrackingPreventionBypassingList')
.onClick(() => {
webview.WebviewController.clearIntelligentTrackingPreventionBypassingList();
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-adsblock-V14
爬取时间: 2025-04-28 00:22:35
来源: Huawei Developer
ArkWeb为应用提供广告过滤功能，支持通过云端推送默认的easylist规则，或允许应用通过接口设定自定义规则文件。它在网络层拦截广告资源的下载，或在网页中注入CSS规则以隐藏特定的广告元素。
当前配置文件格式为easylist语法规则。
常用easylist语法规则
| 规则类别 | 说明 | 示例 |
| --- | --- | --- |
| URL拦截规则 | 拦截所有网站中url能匹配"example.com/js/*_tv.js"的子资源请求。用于定义域名过滤规则，用于匹配特定的域名及其所有子域名。 | ||example.com/js/*_tv.js |
| URL拦截规则 | 拦截非alimama.com、非taobao.com域名网站中的url匹配"alimama.cn"的第三方资源。$third_party是一种options语法，表示匹配第三方资源；域名前使用'~'表示不包括该域名。 | ||alimama.cn^$third-party,domain=alimama.com|\taobao.com |
| 例外规则 | 关闭example.com网页内的广告过滤。@@是例外规则的语法关键字，表示不过滤。 | @@||example.com^$document |
| 例外规则 | 在域名为litv.tv的网页中，不过滤能匹配上".adserver."的子资源。 | @@.adserver.$domain=litv.tv |
| 元素隐藏规则 | 隐藏myabandonware.com和myware.com域名中所有class="i528"的元素。##用于表示元素隐藏。 | myabandonware.com, myware.com##.i528 |
| 元素隐藏例外规则 | 不隐藏sdf-event.sakura.ne.jp网站中id="ad_1"的元素。 | sdf-event.sakura.ne.jp#@##ad_1 |
例外规则，通常是配合普通规则一起使用的，使普通规则在某些场景下不起作用，单独应用例外规则没有意义。
例如先配置了一条过滤所有网站的拦截规则，||abc.com/js/123.js，但是某些网站中出现了误拦截或者不能拦截的场景，就可以针对这些网站配置新的例外规则。
约束与限制
-  在WebviewController类中，增加开启/关闭广告过滤特性的接口enableAdsBlock()，支持Web实例级的特性开关。
-  新增AdsBlockManager全局单例类，提供自定义广告过滤配置、控制网站级特性开关的能力。
-  Web实例上提供了onAdsBlocked()回调通知方法，支持将拦截信息通知到上层应用。
-  AdsBlockManager接口setAdsBlockRules()接口仅能设置一份自定义配置，此配置会持久化，应用冷启动无需重新配置，可避免每次冷启动配置规则都触发广告过滤配置的编译解析。
-  AdsBlockManager接口addAdsBlockDisallowedList()、removeAdsBlockDisallowedList()、clearAdsBlockDisallowedList()、addAdsBlockAllowedList()、removeAdsBlockAllowedList()、clearAdsBlockAllowedList()操作的数据不会持久化，应用冷启动需要重新设置。
-  如果1个Web实例启用了广告过滤特性，但未调用AdsBlockManager接口addAdsBlockDisallowedList()、removeAdsBlockDisallowedList()、clearAdsBlockDisallowedList()、addAdsBlockAllowedList()、removeAdsBlockAllowedList()、clearAdsBlockAllowedList()配置disallowlist和allowlist数据，则默认所有网站均启用广告过滤。
-  allowlist和disallowlist数据共同使用时，allowlist的优先级高于disallowlist，即先使用allowlist匹配，如果匹配成功就不再使用disallowlist匹配，该网站会启用广告过滤特性。
-  如果应用没有使能广告过滤特性，那么确保Web组件不会向服务器请求默认的内置easylist配置文件。
-  disallowlist和allowlist数据采用后缀匹配，例如应用的设置的域名"xxyy.com"，可以匹配上url为"wwsstt.xxyy.com"的网站。
使用场景
开启广告过滤
应用可以通过AdsBlockManager提供的setAdsBlockRules()接口设置自定义的easylist过滤规则，并通过Web组件的enableAdsBlock()接口使能广告过滤特性。
在下面的示例中，演示了一个应用通过文件选择器选择easylist规则文件，并开启广告过滤功能。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { picker, fileUri } from '@kit.CoreFileKit';
// 演示点击按钮，通过filepicker打开一个easylist规则文件并设置到Web组件中
@Entry
@Component
struct WebComponent {
main_url: string = 'https://www.example.com';
controller: webview.WebviewController = new webview.WebviewController();
@State input_text: string = 'https://www.example.com';
build() {
Column() {
Row() {
Flex() {
Button({type: ButtonType.Capsule}) {
Text("setAdsBlockRules")
}
.onClick(() => {
try {
let documentSelectionOptions: ESObject = new picker.DocumentSelectOptions();
let documentPicker: ESObject = new picker.DocumentViewPicker();
documentPicker.select(documentSelectionOptions).then((documentSelectResult: ESObject) => {
if (documentSelectResult && documentSelectResult.length > 0) {
let fileRealPath = new fileUri.FileUri(documentSelectResult[0]);
console.info('DocumentViewPicker.select successfully, uri: ' + fileRealPath);
webview.AdsBlockManager.setAdsBlockRules(fileRealPath.path, true);
}
})
} catch (err) {
console.error('DocumentViewPicker.select failed with err:' + err);
}
})
}
}
Web({ src: this.main_url, controller: this.controller })
.onControllerAttached(()=>{
this.controller.enableAdsBlock(true);
})
}
}
}
```
如果存在内置的easylist规则文件，setAdsBlockRules()接口的replace参数可用于设置规则文件的使用策略，replace为true表示不使用内置的easylist规则文件，replace为false表示自定义规则和内置的规则将会同时工作，如果发现内置规则与自定义规则冲突，可使用replace=true禁用内置规则效果。
设置的自定义规则文件将在应用进程内对所有的Web组件生效，是一个应用级全局配置文件，并将持久化，应用重启后可继续工作。
关闭特定域名页面的广告过滤
在Web组件的广告过滤开关开启后，应用有时候会期望关闭一些特定页面的广告过滤功能，除了可以使用自定义的easylist规则，AdsBlockManager还提供了addAdsBlockDisallowedList()接口完成此功能。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
// 演示通过一个按钮的点击向Web组件设置广告过滤的域名策略
@Entry
@Component
struct WebComponent {
main_url: string = 'https://www.example.com';
text_input_controller: TextInputController = new TextInputController();
controller: webview.WebviewController = new webview.WebviewController();
@State input_text: string = 'https://www.example.com';
build() {
Column() {
Row() {
Flex() {
TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
.id("input_url")
.height(40)
.margin(5)
.borderColor(Color.Blue)
.onChange((value: string) => {
this.input_text = value;
})
Button({type: ButtonType.Capsule}) { Text("Go") }
.onClick(() => {
this.controller.loadUrl(this.input_text);
})
Button({type: ButtonType.Capsule}) { Text("addAdsBlockDisallowedList") }
.onClick(() => {
let arrDomainSuffixes = new Array<string>();
arrDomainSuffixes.push('example.com');
arrDomainSuffixes.push('abcdefg.cn');
webview.AdsBlockManager.addAdsBlockDisallowedList(arrDomainSuffixes);
})
}
}
Web({ src: this.main_url, controller: this.controller })
.onControllerAttached(()=>{
this.controller.enableAdsBlock(true);
})
}
}
}
```
addAdsBlockDisallowedList()接口将域名设置到AdsBlockManager的DisallowedList中，下次页面加载时会使用网页url和DisallowedList中的域名进行后缀匹配，匹配成功则不会对此页面进行广告过滤。此外，还提供了addAdsBlockAllowedList()接口配合DisallowedList进行域名设置，控制是否开启广告过滤。
AdsBlockManager中缓存有2组域名列表，分别为DisallowedList和AllowList，其中DisallowedList用于禁用网页的广告过滤，而AllowList用于重新开启被DisallowedList关闭的广告过滤开关，其中AllowList优先级更高。页面加载时会先使用网页url和AllowList进行匹配，匹配成功的网页广告过滤将保持开启，否则将会继续使用DisallowedList进行匹配，匹配成功将关闭网页的广告过滤。如果访问的网页不在AllowList和DisallowedList中，那么默认网页的广告过滤会保持开启状态。
例如，应用想要开启域名为'news.example.com'和'sport.example.com'的广告过滤，但需要关闭'example.com'的其他域名下网页的广告过滤，就可以先使用addAdsBlockDisallowedList()接口添加'example.com'域名到DisallowedList，再使用addAdsBlockDisallowedList()接口添加'news.example.com'和'sport.example.com'域名。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
// 演示addAdsBlockAllowedList和addAdsBlockAllowedList配套使用，设置网页级的广告过滤开关。
@Entry
@Component
struct WebComponent {
main_url: string = 'https://www.example.com';
text_input_controller: TextInputController = new TextInputController();
controller: webview.WebviewController = new webview.WebviewController();
@State input_text: string = 'https://www.example.com';
build() {
Column() {
Row() {
Flex() {
TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
.id("input_url")
.height(40)
.margin(5)
.borderColor(Color.Blue)
.onChange((value: string) => {
this.input_text = value;
})
Button({type: ButtonType.Capsule}) { Text("Go") }
.onClick(() => {
this.controller.loadUrl(this.input_text);
})
Button({type: ButtonType.Capsule}) { Text("addAdsBlockAllowedList") }
.onClick(() => {
let arrDisallowDomainSuffixes = new Array<string>();
arrDisallowDomainSuffixes.push('example.com');
webview.AdsBlockManager.addAdsBlockDisallowedList(arrDisallowDomainSuffixes);
let arrAllowedDomainSuffixes = new Array<string>();
arrAllowedDomainSuffixes.push('news.example.com');
arrAllowedDomainSuffixes.push('sport.example.com');
webview.AdsBlockManager.addAdsBlockAllowedList(arrAllowedDomainSuffixes);
})
}
}
Web({ src: this.main_url, controller: this.controller })
.onControllerAttached(()=>{
this.controller.enableAdsBlock(true);
})
}
}
}
```
需要注意的是，AdsBlockManager的DisallowedList和AllowedList列表不会持久化，因此重启应用后会重置为空。
如果Web组件未通过enableAdsBlock()接口开启广告过滤功能，上述接口设置在此Web组件中将不起作用。
收集广告过滤的信息
在Web组件的广告过滤开关开启后，访问的网页如果发生了广告过滤，会通过Web组件的onAdsBlocked()回调接口通知到应用，应用可根据需要进行过滤信息的收集和统计。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
@State totalAdsBlockCounts: number = 0;
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'https://www.example.com', controller: this.controller })
.onAdsBlocked((details: AdsBlockedDetails) => {
if (details) {
console.log(' Blocked ' + details.adsBlocked.length + ' in ' + details.url);
let adList: Array<string> = Array.from(new Set(details.adsBlocked));
this.totalAdsBlockCounts += adList.length;
console.log('Total blocked counts :' + this.totalAdsBlockCounts);
}
})
}
}
}
```
由于页面可能随时发生变化并不断产生网络请求，为了减少通知频次、降低对页面加载过程的影响，仅在页面加载完成时进行首次通知，此后发生的过滤将间隔1秒钟上报，无广告过滤则无通知。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-secure-shield-mode-V14
爬取时间: 2025-04-28 00:22:48
来源: Huawei Developer
坚盾守护模式是HarmonyOS 5.0.0 Release版本开始，提供给高安全需求用户的系统级别安全模式。该模式通过限制设备基础功能，增强安全性，有效抵御远程攻击面的针对性攻击。
ArkWeb限制的HTML5特性
坚盾守护模式开启时，ArkWeb通过限制以下HTML5特性减少攻击面。
-  禁止使用WebAssembly能力。
-  禁止使用WebGL、WebGL2能力。
-  禁止使用PDF Viewer预览功能。
-  禁止使用MathML能力。
-  禁止使用Web Speech API语音识别能力。
-  禁止使用RTCDataChannel接口。
-  禁止使用MediaDevices.getUserMedia接口提示用户允许访问媒体输入设备。
-  禁止使用Service Worker能力。
-  禁止使用非代理UDP流量，防止WebRTC泄露真实源ip。
-  禁止即时编译（JIT）能力。
评估对应用的影响
如果要评估应用在坚盾守护模式下的受影响程度及兼容性，可前往“设置 > 隐私和安全 > 坚盾守护模式”开启该模式。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170400.95146457614989348590818456017734:50001231000000:2800:8FF0D4046151E1ECDE968572F04F68A32B94CAB9D7BAE173A1AB6638551327AC.png)
如果需要评估调试版本（未上架应用市场）应用的兼容性，需要先开启开发者选项后再开启坚盾守护模式。
运行应用的相应功能后，可通过以下方式确认是否受影响。
-  排查前端代码是否存在WebAssembly相关接口调用，WebAssembly提供了一种在Web上运行C/C++等低级语言编译目标的能力，通常用于游戏、编解码等高性能场景。坚盾守护模式下，无法调用WebAssembly。
-  排查前端代码是否存在WebGL相关接口调用，WebGL提供了3D图形绘制能力，坚盾守护模式下，相关接口无法调用。
-  排查是否有在线显示PDF的功能场景，坚盾守护模式开启下无法在线显示PDF，例如通过loadUrl接口加载pdf链接等场景。
-  排查HTML页面是否存在<math>标签嵌入的MathML语法，坚盾守护模式下，MathML语法不能正常解析，导致显示异常。
-  排查前端代码是否存在SpeechRecognition（语言识别）、SpeechSynthesis（语音合成）等接口调用，坚盾守护模式下，相关接口无法调用。
-  排查前端代码是否存在RTCDataChannel/createDataChannel等接口调用，该类接口是WebRTC API的特性，可以建立一条双向数据通道的连接，实现WebRTC 中对等端之间的实时数据交换，坚盾守护模式下，相关接口无法调用。
-  排查前端代码是否存在MediaDevices.getUserMedia接口调用，该接口用于向用户请求访问流媒体设备（例如：摄像头、麦克风），坚盾守护模式下，相关接口调用会抛出异常信息“can't use getUserMedia on advancedSecurityMode!”。
-  排查前端代码是否存在ServiceWorker相关接口调用，该机制用于实现离线缓存、网络请求拦截和推送通知等功能，坚盾守护模式下无法创建成功。
-  坚盾守护模式下WebRTC禁止使用非代理UDP传输，涉及到网络连通性，应用需要验证评估WebRTC场景下的网络功能和性能表现。
-  JIT涉及性能优化，坚盾守护模式下应用需要评估JS性能表现。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-manage-loading-browsing-V14
爬取时间: 2025-04-28 00:23:02
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-page-loading-with-web-components-V14
爬取时间: 2025-04-28 00:23:15
来源: Huawei Developer
页面加载是Web组件的基本功能。根据页面加载数据来源可以分为三种常用场景，包括加载网络页面、加载本地页面、加载HTML格式的富文本数据。
页面加载过程中，若涉及网络资源获取，请在module.json5中配置网络访问权限，添加方法请参考在配置文件中声明权限。
加载网络页面
开发者可以在Web组件创建时，指定默认加载的网络页面 。在默认页面加载完成后，如果开发者需要变更此Web组件显示的网络页面，可以通过调用loadUrl()接口加载指定的网页。Web组件的第一个参数变量src不能通过状态变量（例如：@State）动态更改地址，如需更改，请通过loadUrl()重新加载。
在下面的示例中，在Web组件加载完“www.example.com”页面后，开发者可通过loadUrl接口将此Web组件显示页面变更为“www.example1.com”。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('loadUrl')
.onClick(() => {
try {
// 点击按钮时，通过loadUrl，跳转到www.example1.com
this.controller.loadUrl('www.example1.com');
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
// 组件创建时，加载www.example.com
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
加载本地页面
在下面的示例中展示加载本地页面文件的方法：
将本地页面文件放在应用的rawfile目录下，开发者可以在Web组件创建的时候指定默认加载的本地页面 ，并且加载完成后可通过调用loadUrl()接口变更当前Web组件的页面。
加载本地html文件时引用本地css样式文件可以通过下面方法实现。
-  将资源文件放置在应用的resources/rawfile目录下。 图1资源文件路径
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('loadUrl')
.onClick(() => {
try {
// 点击按钮时，通过loadUrl，跳转到local1.html
this.controller.loadUrl($rawfile("local1.html"));
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
// 组件创建时，通过$rawfile加载本地文件local.html
Web({ src: $rawfile("local.html"), controller: this.controller })
}
}
}
```
-  local.html页面代码。
-  local1.html页面代码。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170400.99425635519545923125211311289956:50001231000000:2800:0A0FC9C91978A3027A6D1D765C866BF18658E97AA15BEB3615C6BE1CDF58BBE3.png)
加载沙箱路径下的本地页面文件。
1.  通过构造的单例对象GlobalContext获取沙箱路径，需要开启应用中文件系统的访问fileAccess权限。
```typescript
// GlobalContext.ets
export class GlobalContext {
private constructor() {}
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
2.  修改EntryAbility.ets。 以filesDir为例，获取沙箱路径。若想获取其他路径，请参考应用文件路径。 加载的html文件。
```typescript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { GlobalContext } from '../GlobalContext';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
// 通过在GlobalContext对象上绑定filesDir，可以实现UIAbility组件与UI之间的数据同步。
GlobalContext.getContext().setObject("filesDir", this.context.filesDir);
console.log("Sandbox path is " + GlobalContext.getContext().getObject("filesDir"));
}
}
```
加载HTML格式的文本数据
Web组件可以通过loadData()接口实现加载HTML格式的文本数据。当开发者不需要加载整个页面，只需要显示一些页面片段时，可通过此功能来快速加载页面，当加载大量html文件时，需设置第四个参数baseUrl为"data"。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('loadData')
.onClick(() => {
try {
// 点击按钮时，通过loadData，加载HTML格式的文本数据
this.controller.loadData(
"<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
"text/html",
"UTF-8"
);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
// 组件创建时，加载www.example.com
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
Web组件可以通过data url方式直接加载HTML字符串。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
htmlStr: string = "data:text/html, <html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>";
build() {
Column() {
// 组件创建时，加载htmlStr
Web({ src: this.htmlStr, controller: this.controller })
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-redirection-and-browsing-history-mgmt-V14
爬取时间: 2025-04-28 00:23:28
来源: Huawei Developer
历史记录导航
在前端页面点击网页中的链接时，Web组件默认会自动打开并加载目标网址。当前端页面替换为新的加载链接时，会自动记录已经访问的网页地址。可以通过forward()和backward()接口向前/向后浏览上一个/下一个历史记录。
页面加载过程中，若涉及网络资源获取，需要在module.json5中配置网络访问权限，添加方法请参考在配置文件中声明权限。
在下面的示例中，点击应用的按钮来触发前端页面的后退操作。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('loadData')
.onClick(() => {
if (this.webviewController.accessBackward()) {
this.webviewController.backward();
}
})
Web({ src: 'https://www.example.com/cn/', controller: this.webviewController })
}
}
}
```
如果存在历史记录，accessBackward()接口会返回true。同样，您可以使用accessForward()接口检查是否存在前进的历史记录。如果您不执行检查，那么当用户浏览到历史记录的末尾时，调用forward()和backward()接口时将不执行任何操作。
页面跳转
当点击网页中的链接需要跳转到应用内其他页面时，可以通过使用Web组件的onLoadIntercept()接口来实现。
在下面的示例中，应用首页Index.ets加载前端页面route.html，在前端route.html页面点击超链接，可跳转到应用的ProfilePage.ets页面。
-  应用首页Index.ets页面代码。
```typescript
// index.ets
import { webview } from '@kit.ArkWeb';
import { router } from '@kit.ArkUI';
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
// 资源文件route.html存放路径src/main/resources/rawfile
Web({ src: $rawfile('route.html'), controller: this.webviewController })
.onLoadIntercept((event) => {
if (event) {
let url: string = event.data.getRequestUrl();
if (url.indexOf('native://') === 0) {
// 跳转其他界面
router.pushUrl({ url: url.substring(9) });
return true;
}
}
return false;
})
}
}
}
```
-  route.html前端页面代码。
-  跳转页面ProfilePage.ets代码。
```typescript
@Entry
@Component
struct ProfilePage {
@State message: string = 'Hello World';
build() {
Column() {
Text(this.message)
.fontSize(20)
}
}
}
```
跨应用跳转
Web组件可以实现点击前端页面超链接跳转到其他应用。
在下面的示例中，点击call.html前端页面中的超链接，跳转到电话应用的拨号界面。
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { call } from '@kit.TelephonyKit';
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: $rawfile('call.html'), controller: this.webviewController })
.onLoadIntercept((event) => {
if (event) {
let url: string = event.data.getRequestUrl();
// 判断链接是否为拨号链接
if (url.indexOf('tel://') === 0) {
// 跳转拨号界面
call.makeCall(url.substring(6), (err) => {
if (!err) {
console.info('make call succeeded.');
} else {
console.info('make call fail, err is:' + JSON.stringify(err));
}
});
return true;
}
}
return false;
})
}
}
}
```
-  前端页面call.html代码。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-scheme-handler-V14
爬取时间: 2025-04-28 00:23:42
来源: Huawei Developer
通过网络拦截接口(arkweb_scheme_handler.h)对Web组件发出的请求进行拦截，并可以为被拦截的请求提供自定义的响应头以及响应体。
为Web组件设置网络拦截器
为指定的Web组件或者ServiceWorker设置ArkWeb_SchemeHandler，当Web内核发出相应scheme请求的时候，会触发ArkWeb_SchemeHandler的回调。需要在Web组件初始化之后设置网络拦截器。
当请求开始的时候会回调ArkWeb_OnRequestStart，请求结束的时候会回调ArkWeb_OnRequestStop。
如果想要拦截Web组件发出的第一个请求，可以通过initializeWebEngine对Web组件提前进行初始化，然后设置拦截器进行拦截。
也可以拦截非Web组件内置scheme的请求。
设置自定义scheme需要遵循的规则
如果要拦截自定义scheme的请求，需要提前将自定义scheme注册到Web内核。需要在Web组件初始化之前进行注册，Web组件初始化后再注册会失败。
由于注册scheme需要在Web组件初始化之前进行注册，而网络拦截器需要在Web组件初始化之后设置，建议在EntryAbility的onCreate中调用c++接口注册scheme。
scheme注册完毕后，通过initializeWebEngine对Web组件进行初始化，初始化完成后再设置网络拦截器。
```typescript
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 注册scheme的配置。
testNapi.registerCustomSchemes();
// 初始化Web组件内核，该操作会初始化Browser进程以及创建BrowserContext。
webview.WebviewController.initializeWebEngine();
// 创建并设置ArkWeb_SchemeHandler。
testNapi.setSchemeHandler();
}
...
};
```
获取被拦截请求的请求信息
通过OH_ArkWebResourceRequest_*接口获取被拦截请求的信息。可以获取url、method、referrer、headers、resourceType等信息。
支持获取PUT/POST类请求的上传数据。数据类型支持BYTES、FILE、BLOB和CHUNKED。
为被拦截的请求提供自定义的响应体
Web组件的网络拦截支持在worker线程以流的方式为被拦截的请求提供自定义的响应体。也可以以特定的网络错误码(arkweb_net_error_list.h)结束当前被拦截的请求。
完整示例
使用DevEco Studio创建一个默认的Native C++工程，需要提前准备一个mp4文件，命名为test.mp4，将test.mp4放到main/resources/rawfile下。
main/ets/pages/index.ets
```typescript
import testNapi from 'libentry.so';
import { webview } from '@kit.ArkWeb';
import { resourceManager } from '@kit.LocalizationKit';
@Entry
@Component
struct Index {
mycontroller: webview.WebviewController = new webview.WebviewController("scheme-handler");
build() {
Row() {
Column() {
Button("goback").onClick( event => {
this.mycontroller.backward();
})
Web({ src: $rawfile("test.html"), controller: this.mycontroller})
.javaScriptAccess(true)
.width('100%')
.height('100%')
.databaseAccess(true)
.fileAccess(false)
.domStorageAccess(true)
.cacheMode(CacheMode.Default)
.onPageBegin( event => {
testNapi.initResourceManager(getContext().resourceManager);
})
}
.width('100%')
}
.height('100%')
}
}
```
main/ets/entryability/EntryAbility.ets
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import testNapi from 'libentry.so';
import { webview } from '@kit.ArkWeb';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 注册三方协议的配置。
testNapi.registerCustomSchemes();
// 初始化Web组件内核，该操作会初始化Browser进程以及创建BrowserContext。
webview.WebviewController.initializeWebEngine();
// 设置SchemeHandler。
testNapi.setSchemeHandler();
}
onDestroy(): void {
}
onWindowStageCreate(windowStage: window.WindowStage): void {
windowStage.loadContent('pages/Index', (err, data) => {
if (err.code) {
return;
}
});
}
onWindowStageDestroy(): void {
}
onForeground(): void {
}
onBackground(): void {
}
};
```
main/cpp/hello.cpp
main/cpp/CMakeLists.txt
main/cpp/types/index.d.ts
```typescript
export const registerCustomSchemes: () => void;
export const setSchemeHandler: () => void;
export const initResourceManager: (resmgr: resourceManager.ResourceManager) => void;
```
main/cpp/rawfile_request.h
main/cpp/rawfile_request.cpp
main/resources/rawfile/test.html
main/resources/rawfile/cat.svg
main/resources/rawfile/csp_bypassing.html
main/resources/rawfile/csp_script.js
main/resources/rawfile/isolated_script.js
main/resources/rawfile/isolated.html
main/resources/rawfile/local_script.js
main/resources/rawfile/local.html
main/resources/rawfile/post_data.html
main/resources/rawfile/service_worker.html
main/resources/rawfile/sw.js
main/resources/rawfile/video.html
main/resources/rawfile/chunked_post_stream.html
main/resources/rawfile/xhr

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-resource-interception-request-mgmt-V14
爬取时间: 2025-04-28 00:23:55
来源: Huawei Developer
Web组件支持在应用拦截到页面请求后自定义响应请求能力。开发者通过onInterceptRequest()接口来实现自定义资源请求响应 。自定义请求能力可以用于开发者自定义Web页面响应、自定义文件资源响应等场景。
Web网页上发起资源加载请求，应用层收到资源请求消息。应用层构造本地资源响应消息发送给Web内核。Web内核解析应用层响应信息，根据此响应信息进行页面资源加载。
在下面的示例中，Web组件通过拦截页面请求“https://www.example.com/test.html”， 在应用侧代码构建响应资源，实现自定义页面响应场景。
-  前端页面index.html代码。
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
responseResource: WebResourceResponse = new WebResourceResponse();
// 开发者自定义响应数据
@State webData: string = '<!DOCTYPE html>\n' +
'<html>\n' +
'<head>\n' +
'<title>intercept test</title>\n' +
'</head>\n' +
'<body>\n' +
'<h1>intercept ok</h1>\n' +
'</body>\n' +
'</html>'
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onInterceptRequest((event) => {
if (event) {
console.info('url:' + event.request.getRequestUrl());
// 拦截页面请求
if (event.request.getRequestUrl() !== 'https://www.example.com/test.html') {
return null;
}
}
// 构造响应数据
this.responseResource.setResponseData(this.webData);
this.responseResource.setResponseEncoding('utf-8');
this.responseResource.setResponseMimeType('text/html');
this.responseResource.setResponseCode(200);
this.responseResource.setReasonMessage('OK');
return this.responseResource;
})
}
}
}
```
为自定义的JavaScript请求响应生成 CodeCache：自定义请求响应的资源类型如果是JavaScript脚本，可以在响应头中添加“ResponseDataID”字段，Web内核读取到该字段后会在为该JS资源生成CodeCache，加速JS执行，并且ResponseData如果有更新时必须更新该字段。不添加“ResponseDataID”字段的情况下默认不生成CodeCache。
在下面的示例中，Web组件通过拦截页面请求“https://www.example.com/test.js”， 应用侧代码构建响应资源，在响应头中添加“ResponseDataID”字段，开启生成CodeCache的功能。
-  前端页面index.html代码。
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
responseResource: WebResourceResponse = new WebResourceResponse();
// 开发者自定义响应数据（响应数据长度需大于等于1024才会生成codecache）
@State jsData: string = 'let text_msg = "the modified content:version 0000000000001";\n' +
'let element1 = window.document.getElementById("div-1");\n' +
'let element2 = window.document.getElementById("div-2");\n' +
'let element3 = window.document.getElementById("div-3");\n' +
'let element4 = window.document.getElementById("div-4");\n' +
'let element5 = window.document.getElementById("div-5");\n' +
'let element6 = window.document.getElementById("div-6");\n' +
'let element7 = window.document.getElementById("div-7");\n' +
'let element8 = window.document.getElementById("div-8");\n' +
'let element9 = window.document.getElementById("div-9");\n' +
'let element10 = window.document.getElementById("div-10");\n' +
'let element11 = window.document.getElementById("div-11");\n' +
'element1.innerHTML = text_msg;\n' +
'element2.innerHTML = text_msg;\n' +
'element3.innerHTML = text_msg;\n' +
'element4.innerHTML = text_msg;\n' +
'element5.innerHTML = text_msg;\n' +
'element6.innerHTML = text_msg;\n' +
'element7.innerHTML = text_msg;\n' +
'element8.innerHTML = text_msg;\n' +
'element9.innerHTML = text_msg;\n' +
'element10.innerHTML = text_msg;\n' +
'element11.innerHTML = text_msg;\n';
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onInterceptRequest((event) => {
// 拦截页面请求
if (event?.request.getRequestUrl() == 'https://www.example.com/test.js') {
// 构造响应数据
this.responseResource.setResponseHeader([
{
// 格式：不超过13位纯数字。js识别码，Js有更新时必须更新该字段
headerKey: "ResponseDataID",
headerValue: "0000000000001"
}]);
this.responseResource.setResponseData(this.jsData);
this.responseResource.setResponseEncoding('utf-8');
this.responseResource.setResponseMimeType('application/javascript');
this.responseResource.setResponseCode(200);
this.responseResource.setReasonMessage('OK');
return this.responseResource;
}
return null;
})
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-predictor-V14
爬取时间: 2025-04-28 00:24:09
来源: Huawei Developer
当Web页面加载缓慢时，可以使用预连接、预加载和预获取post请求的能力加速Web页面的访问。
预解析和预连接
可以通过prepareForPageLoad()来预解析或者预连接将要加载的页面。
在下面的示例中，在Web组件的onAppear中对要加载的页面进行预连接。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('loadData')
.onClick(() => {
if (this.webviewController.accessBackward()) {
this.webviewController.backward();
}
})
Web({ src: 'https://www.example.com/', controller: this.webviewController })
.onAppear(() => {
// 指定第二个参数为true，代表要进行预连接，如果为false该接口只会对网址进行dns预解析
// 第三个参数为要预连接socket的个数。最多允许6个。
webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 2);
})
}
}
}
```
也可以通过initializeWebEngine()来提前初始化内核，然后在初始化内核后调用
prepareForPageLoad()对即将要加载的页面进行预解析、预连接。这种方式适合提前对首页进行
预解析、预连接。
在下面的示例中，Ability的onCreate中提前初始化Web内核并对首页进行预连接。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
console.log("EntryAbility onCreate");
webview.WebviewController.initializeWebEngine();
// 预连接时，需要將'https://www.example.com'替换成真实要访问的网站地址。
webview.WebviewController.prepareForPageLoad("https://www.example.com/", true, 2);
AppStorage.setOrCreate("abilityWant", want);
console.log("EntryAbility onCreate done");
}
}
```
预加载
如果能够预测到Web组件将要加载的页面或者即将要跳转的页面。可以通过prefetchPage()来预加载即将要加载页面。
预加载会提前下载页面所需的资源，包括主资源子资源，但不会执行网页JavaScript代码。预加载是WebviewController的实例方法，需要一个已经关联好Web组件的WebviewController实例。
在下面的示例中，在onPageEnd的时候触发下一个要访问的页面的预加载。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'https://www.example.com/', controller: this.webviewController })
.onPageEnd(() => {
// 预加载https://www.iana.org/help/example-domains。
this.webviewController.prefetchPage('https://www.iana.org/help/example-domains');
})
}
}
}
```
预获取post请求
可以通过prefetchResource()预获取将要加载页面中的post请求。在页面加载结束时，可以通过clearPrefetchedResource()清除后续不再使用的预获取资源缓存。
以下示例，在Web组件onAppear中，对要加载页面中的post请求进行预获取。在onPageEnd中，可以清除预获取的post请求缓存。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: "https://www.example.com/", controller: this.webviewController })
.onAppear(() => {
// 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
webview.WebviewController.prefetchResource(
{
url: "https://www.example1.com/post?e=f&g=h",
method: "POST",
formData: "a=x&b=y",
},
[{
headerKey: "c",
headerValue: "z",
},],
"KeyX", 500);
})
.onPageEnd(() => {
// 清除后续不再使用的预获取资源缓存。
webview.WebviewController.clearPrefetchedResource(["KeyX",]);
})
}
}
}
```
如果能够预测到Web组件将要加载页面或者即将要跳转页面中的post请求。可以通过prefetchResource()预获取即将要加载页面的post请求。
以下示例，在onPageEnd中，触发预获取一个要访问页面的post请求。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
webviewController: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'https://www.example.com/', controller: this.webviewController })
.onPageEnd(() => {
// 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
webview.WebviewController.prefetchResource(
{
url: "https://www.example1.com/post?e=f&g=h",
method: "POST",
formData: "a=x&b=y",
},
[{
headerKey: "c",
headerValue: "z",
},],
"KeyX", 500);
})
}
}
}
```
也可以通过initializeWebEngine()提前初始化内核，然后在初始化内核后调用prefetchResource()预获取将要加载页面中的post请求。这种方式适合提前预获取首页的post请求。
以下示例，在Ability的onCreate中，提前初始化Web内核并预获取首页的post请求。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
console.log("EntryAbility onCreate");
webview.WebviewController.initializeWebEngine();
// 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
webview.WebviewController.prefetchResource(
{
url: "https://www.example1.com/post?e=f&g=h",
method: "POST",
formData: "a=x&b=y",
},
[{
headerKey: "c",
headerValue: "z",
},],
"KeyX", 500);
AppStorage.setOrCreate("abilityWant", want);
console.log("EntryAbility onCreate done");
}
}
```
预编译生成编译缓存
可以通过precompileJavaScript()在页面加载前提前生成脚本文件的编译缓存。
推荐配合动态组件使用，使用离线的Web组件用于生成字节码缓存，并在适当的时机加载业务用Web组件使用这些字节码缓存。下方是代码示例：
1.  首先，在EntryAbility中将UIContext存到localStorage中。
```typescript
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
const localStorage: LocalStorage = new LocalStorage('uiContext');
export default class EntryAbility extends UIAbility {
storage: LocalStorage = localStorage;
onWindowStageCreate(windowStage: window.WindowStage) {
windowStage.loadContent('pages/Index', this.storage, (err, data) => {
if (err.code) {
return;
}
this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
});
}
}
```
2.  编写动态组件所需基础代码。
```typescript
// DynamicComponent.ets
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
export interface BuilderData {
url: string;
controller: WebviewController;
}
const storage = LocalStorage.getShared();
export class NodeControllerImpl extends NodeController {
private rootNode: BuilderNode<BuilderData[]> | null = null;
private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;
constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>) {
super();
this.wrappedBuilder = wrappedBuilder;
}
makeNode(): FrameNode | null {
if (this.rootNode != null) {
return this.rootNode.getFrameNode();
}
return null;
}
initWeb(url: string, controller: WebviewController) {
if(this.rootNode != null) {
return;
}
const uiContext: UIContext = storage.get<UIContext>("uiContext") as UIContext;
if (!uiContext) {
return;
}
this.rootNode = new BuilderNode(uiContext);
this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
}
}
export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
const baseNode = new NodeControllerImpl(wrappedBuilder);
baseNode.initWeb(data.url, data.controller);
return baseNode;
}
```
3.  编写用于生成字节码缓存的组件，本例中的本地Javascript资源内容通过文件读取接口读取rawfile目录下的本地文件。
```typescript
// PrecompileWebview.ets
import { BuilderData } from "./DynamicComponent";
import { Config, configs } from "./PrecompileConfig";
@Builder
function WebBuilder(data: BuilderData) {
Web({ src: data.url, controller: data.controller })
.onControllerAttached(() => {
precompile(data.controller, configs);
})
.fileAccess(true)
}
export const precompileWebview = wrapBuilder<BuilderData[]>(WebBuilder);
export const precompile = async (controller: WebviewController, configs: Array<Config>) => {
for (const config of configs) {
let content = await readRawFile(config.localPath);
try {
controller.precompileJavaScript(config.url, content, config.options)
.then(errCode => {
console.error("precompile successfully! " + errCode);
}).catch((errCode: number) => {
console.error("precompile failed. " + errCode);
});
} catch (err) {
console.error("precompile failed. " + err.code + " " + err.message);
}
}
}
async function readRawFile(path: string) {
try {
return await getContext().resourceManager.getRawFileContent(path);;
} catch (err) {
return new Uint8Array(0);
}
}
```
JavaScript资源的获取方式也可通过网络请求的方式获取，但此方法获取到的http响应头非标准HTTP响应头格式，需额外将响应头转换成标准HTTP响应头格式后使用。如通过网络请求获取到的响应头是e-tag，则需要将其转换成E-Tag后使用。
1.  编写业务用组件代码。
```typescript
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";
@Builder
function WebBuilder(data: BuilderData) {
// 此处组件可根据业务需要自行扩展
Web({ src: data.url, controller: data.controller })
.cacheMode(CacheMode.Default)
}
export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
```
2.  编写资源配置信息。
```typescript
// PrecompileConfig.ets
import { webview } from '@kit.ArkWeb'
export interface Config {
url:  string,
localPath: string, // 本地资源路径
options: webview.CacheOptions
}
export let configs: Array<Config> = [
{
url: "https://www.example.com/example.js",
localPath: "example.js",
options: {
responseHeaders: [
{ headerKey: "E-Tag", headerValue: "aWO42N9P9dG/5xqYQCxsx+vDOoU="},
{ headerKey: "Last-Modified", headerValue: "Wed, 21 Mar 2024 10:38:41 GMT"}
]
}
}
]
```
3.  在页面中使用。
```typescript
// Index.ets
import { webview } from '@kit.ArkWeb';
import { NodeController } from '@kit.ArkUI';
import { createNode } from "./DynamicComponent"
import { precompileWebview } from "./PrecompileWebview"
import { businessWebview } from "./BusinessWebview"
@Entry
@Component
struct Index {
@State precompileNode: NodeController | undefined = undefined;
precompileController: webview.WebviewController = new webview.WebviewController();
@State businessNode: NodeController | undefined = undefined;
businessController: webview.WebviewController = new webview.WebviewController();
aboutToAppear(): void {
// 初始化用于注入本地资源的Web组件
this.precompileNode = createNode(precompileWebview,
{ url: "https://www.example.com/empty.html", controller: this.precompileController});
}
build() {
Column() {
// 在适当的时机加载业务用Web组件，本例以Button点击触发为例
Button("加载页面")
.onClick(() => {
this.businessNode = createNode(businessWebview, {
url:  "https://www.example.com/business.html",
controller: this.businessController
});
})
// 用于业务的Web组件
NodeContainer(this.businessNode);
}
}
}
```
当需要更新本地已经生成的编译字节码时，修改cacheOptions参数中responseHeaders中的E-Tag或Last-Modified响应头对应的值，再次调用接口即可。
离线资源免拦截注入
可以通过injectOfflineResources()在页面加载前提前将图片、样式表或脚本资源注入到应用的内存缓存中。
推荐配合动态组件使用，使用离线的Web组件用于将资源注入到内核的内存缓存中，并在适当的时机加载业务用Web组件使用这些资源。下方是代码示例：
1.  首先，在EntryAbility中将UIContext存到localStorage中。
```typescript
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
const localStorage: LocalStorage = new LocalStorage('uiContext');
export default class EntryAbility extends UIAbility {
storage: LocalStorage = localStorage;
onWindowStageCreate(windowStage: window.WindowStage) {
windowStage.loadContent('pages/Index', this.storage, (err, data) => {
if (err.code) {
return;
}
this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
});
}
}
```
2.  编写动态组件所需基础代码。
```typescript
// DynamicComponent.ets
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
export interface BuilderData {
url: string;
controller: WebviewController;
}
const storage = LocalStorage.getShared();
export class NodeControllerImpl extends NodeController {
private rootNode: BuilderNode<BuilderData[]> | null = null;
private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;
constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>) {
super();
this.wrappedBuilder = wrappedBuilder;
}
makeNode(): FrameNode | null {
if (this.rootNode != null) {
return this.rootNode.getFrameNode();
}
return null;
}
initWeb(url: string, controller: WebviewController) {
if(this.rootNode != null) {
return;
}
const uiContext: UIContext = storage.get<UIContext>("uiContext") as UIContext;
if (!uiContext) {
return;
}
this.rootNode = new BuilderNode(uiContext);
this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
}
}
export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
const baseNode = new NodeControllerImpl(wrappedBuilder);
baseNode.initWeb(data.url, data.controller);
return baseNode;
}
```
3.  编写用于注入资源的组件代码，本例中的本地资源内容通过文件读取接口读取rawfile目录下的本地文件。
```typescript
// InjectWebview.ets
import { webview } from '@kit.ArkWeb';
import { resourceConfigs } from "./Resource";
import { BuilderData } from "./DynamicComponent";
@Builder
function WebBuilder(data: BuilderData) {
Web({ src: data.url, controller: data.controller })
.onControllerAttached(async () => {
try {
data.controller.injectOfflineResources(await getData ());
} catch (err) {
console.error("error: " + err.code + " " + err.message);
}
})
.fileAccess(true)
}
export const injectWebview = wrapBuilder<BuilderData[]>(WebBuilder);
export async function getData() {
const resourceMapArr: Array<webview.OfflineResourceMap> = [];
// 读取配置，从rawfile目录中读取文件内容
for (let config of resourceConfigs) {
let buf: Uint8Array = new Uint8Array(0);
if (config.localPath) {
buf = await readRawFile(config.localPath);
}
resourceMapArr.push({
urlList: config.urlList,
resource: buf,
responseHeaders: config.responseHeaders,
type: config.type,
})
}
return resourceMapArr;
}
export async function readRawFile(url: string) {
try {
return await getContext().resourceManager.getRawFileContent(url);
} catch (err) {
return new Uint8Array(0);
}
}
```
4.  编写业务用组件代码。
```typescript
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";
@Builder
function WebBuilder(data: BuilderData) {
// 此处组件可根据业务需要自行扩展
Web({ src: data.url, controller: data.controller })
.cacheMode(CacheMode.Default)
}
export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
```
5.  编写资源配置信息。
```typescript
// Resource.ets
import { webview } from '@kit.ArkWeb';
export interface ResourceConfig {
urlList: Array<string>,
type: webview.OfflineResourceType,
responseHeaders: Array<Header>,
localPath: string, // 本地资源存放在rawfile目录下的路径
}
export const resourceConfigs: Array<ResourceConfig> = [
{
localPath: "example.png",
urlList: [
"https://www.example.com/",
"https://www.example.com/path1/example.png",
"https://www.example.com/path2/example.png",
],
type: webview.OfflineResourceType.IMAGE,
responseHeaders: [
{ headerKey: "Cache-Control", headerValue: "max-age=1000" },
{ headerKey: "Content-Type", headerValue: "image/png" },
]
},
{
localPath: "example.js",
urlList: [ // 仅提供一个url，这个url既作为资源的源，也作为资源的网络请求地址
"https://www.example.com/example.js",
],
type: webview.OfflineResourceType.CLASSIC_JS,
responseHeaders: [
// 以<script crossorigin="anoymous" />方式使用，提供额外的响应头
{ headerKey: "Cross-Origin", headerValue:"anonymous" }
]
},
];
```
6.  在页面中使用。
```typescript
// Index.ets
import { webview } from '@kit.ArkWeb';
import { NodeController } from '@kit.ArkUI';
import { createNode } from "./DynamicComponent"
import { injectWebview } from "./InjectWebview"
import { businessWebview } from "./BusinessWebview"
@Entry
@Component
struct Index {
@State injectNode: NodeController | undefined = undefined;
injectController: webview.WebviewController = new webview.WebviewController();
@State businessNode: NodeController | undefined = undefined;
businessController: webview.WebviewController = new webview.WebviewController();
aboutToAppear(): void {
// 初始化用于注入本地资源的Web组件, 提供一个空的html页面作为url即可
this.injectNode = createNode(injectWebview,
{ url: "https://www.example.com/empty.html", controller: this.injectController});
}
build() {
Column() {
// 在适当的时机加载业务用Web组件，本例以Button点击触发为例
Button("加载页面")
.onClick(() => {
this.businessNode = createNode(businessWebview, {
url: "https://www.example.com/business.html",
controller: this.businessController
});
})
// 用于业务的Web组件
NodeContainer(this.businessNode);
}
}
}
```
7.  加载的HTML网页示例。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-set-back-forward-cache-V14
爬取时间: 2025-04-28 00:24:22
来源: Huawei Developer
Web组件为开发者提供了启用和配置前进后退缓存（以下简称BFCache）的功能。启用此功能后，能够显著提升用户返回至先前浏览网页的速度，尤其对于网络条件不佳的用户，可提供更为流畅的浏览体验。
BFCache功能启用后，Web组件会在用户离开当前页面时在内存中保存该页面的快照。当用户在短期内通过Web组件的前进或后退功能重新访问同一页面时，能够迅速恢复页面状态，避免重复发起HTTP请求。
Web组件开启BFCache
开发者需要在调用initializeWebEngine()初始化ArkWeb内核之前调用enableBackForwardCache()来开启BFCache。enableBackForwardCache可以接收一个BackForwardCacheSupportedFeatures参数，用于控制是否允许具备同层渲染特性和视频托管特性的页面进入BFCache。
```typescript
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
let features = new webview.BackForwardCacheSupportedFeatures();
features.nativeEmbed = true;
features.mediaTakeOver = true;
webview.WebviewController.enableBackForwardCache(features);
webview.WebviewController.initializeWebEngine();
AppStorage.setOrCreate("abilityWant", want);
}
}
```
设置缓存的页面数量和页面留存的时间
启用BFCache后仅能存储一个页面，Web组件默认进入BFCache的页面可保持存活状态600秒。开发者可通过调用setBackForwardCacheOptions()设置每个Web实例的前进后退缓存策略。包括调整缓存中页面的最大数量，使BFCache能够容纳更多页面，从而在用户连续进行前进后退操作时，提供更快的加载速度。同时，开发者还能修改每个页面在缓存中的停留时间，延长页面在BFCache中的驻留期限，进而优化用户的浏览体验。
在下面的示例中，设置Web组件可以缓存的最大数量为10，每个页面在缓存中停留300s。
```typescript
// Index.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct Index {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Row() {
Button("Add options").onClick((event: ClickEvent) => {
let options = new webview.BackForwardCacheOptions();
options.size = 10;
options.timeToLive = 300;
this.controller.setBackForwardCacheOptions(options);
})
Button("Backward").onClick((event: ClickEvent) => {
this.controller.backward();
})
Button("Forward").onClick((event: ClickEvent) => {
this.controller.forward();
})
}
Web({ src: "https://www.example.com", controller: this.controller })
}
.height('100%')
.width('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-component-migrate-V14
爬取时间: 2025-04-28 00:24:35
来源: Huawei Developer
Web组件能够实现在不同窗口的组件树上进行挂载或移除操作，这一能力使得开发者可以将同一个Web组件在不同窗口间迁移。例如，将浏览器的Tab页拖出成独立窗口，或拖入浏览器的另一个窗口。
Web组件在不同窗口间迁移，是基于自定义节点能力实现的。实现的基本原理是：通过BuilderNode，开发者可创建Web组件的离线节点，并结合自定义占位节点控制Web节点的挂载与移除。当从一个窗口上移除Web节点，并挂载到另一个窗口中，即完成Web组件在窗口间的迁移。
在以下示例中，主窗Ability启动时，通过命令式的方式创建了一个Web组件。开发者可以利用common.ets中提供的方法和类，实现Web组件的挂载和移除。Index.ets则提供了一种挂载和移除Web组件的实现方法。通过这种方式，开发者能够实现Web组件在不同窗口中页面的挂载与移除，即实现了Web组件在不同窗口间的迁移。下图是展示了这一迁移过程的示意图。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170401.03446001254382157760890621368895:50001231000000:2800:578D7CE588C6134065D899E250AB1F76615C93055F6F8BE4A63DDE918D4B9757.png)
不要将一个Web组件同时挂载在两个父节点下，这会导致非预期行为。
```typescript
// 主窗Ability
// EntryAbility.ets
import { createNWeb, defaultUrl } from '../pages/common'
// ...
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
windowStage.loadContent('pages/Index', (err) => {
if (err.code) {
hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
// 创建Web动态组件（需传入UIContext），loadContent之后的任意时机均可创建，应用仅创建一个Web组件
createNWeb(defaultUrl, windowStage.getMainWindowSync().getUIContext());
hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
});
}
// ...
```
```typescript
// 提供动态挂载Web组件能力
// pages/common.ets
import { UIContext, NodeController, BuilderNode, FrameNode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { hilog } from '@kit.PerformanceAnalysisKit';
export const defaultUrl : string = 'https://www.example.com';
// Data为入参封装类
class Data{
url: string = '';
webController: webview.WebviewController | null = null;
constructor(url: string, webController: webview.WebviewController) {
this.url = url;
this.webController = webController;
}
}
// @Builder中为动态组件的具体组件内容
@Builder
function WebBuilder(data:Data) {
Web({ src: data.url, controller: data.webController })
.width("100%")
.height("100%")
.borderStyle(BorderStyle.Dashed)
.borderWidth(2)
}
let wrap = wrapBuilder<[Data]>(WebBuilder);
// 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用
export class MyNodeController extends NodeController {
private builderNode: BuilderNode<[Data]> | null | undefined = null;
private webController : webview.WebviewController | null | undefined = null;
private rootNode : FrameNode | null = null;
constructor(builderNode : BuilderNode<[Data]> | undefined, webController : webview.WebviewController | undefined) {
super();
this.builderNode = builderNode;
this.webController = webController;
}
// 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContainer中
// 在对应NodeContainer创建的时候调用或者通过rebuild方法调用刷新
makeNode(uiContext: UIContext): FrameNode | null {
// 该节点会被挂载在NodeContainer的父节点下
return this.rootNode;
}
// 挂载Webview
attachWeb() : void {
if (this.builderNode) {
let frameNode : FrameNode | null = this.builderNode.getFrameNode();
if (frameNode?.getParent() != null) {
// 挂载自定义节点前判断该节点是否已经被挂载
hilog.error(0x0000, 'testTag', '%{public}s', 'The frameNode is already attached');
return;
}
this.rootNode = this.builderNode.getFrameNode();
}
}
// 卸载Webview
detachWeb() : void {
this.rootNode = null;
}
getWebController() : webview.WebviewController | null | undefined {
return this.webController;
}
}
// 创建Map保存所需要的BuilderNode
let builderNodeMap : Map<string, BuilderNode<[Data]> | undefined> = new Map();
// 创建Map保存所需要的webview.WebviewController
let webControllerMap : Map<string, webview.WebviewController | undefined> = new Map();
// 初始化需要UIContext对象，UIContext对象可通过窗口或自定义组件的getUIContext方法获取
export const createNWeb = (url: string, uiContext: UIContext) => {
// 创建WebviewController
let webController = new webview.WebviewController() ;
// 创建BuilderNode
let builderNode : BuilderNode<[Data]> = new BuilderNode(uiContext);
// 创建动态Web组件
builderNode.build(wrap, new Data(url, webController));
// 保存BuilderNode
builderNodeMap.set(url, builderNode);
// 保存WebviewController
webControllerMap.set(url, webController);
}
// 自定义获取BuilderNode的接口
export const getBuilderNode = (url : string) : BuilderNode<[Data]> | undefined => {
return builderNodeMap.get(url);
}
// 自定义获取WebviewController的接口
export const getWebviewController = (url : string) : webview.WebviewController | undefined => {
return webControllerMap.get(url);
}
```
```typescript
// 使用NodeController的Page页
// pages/Index.ets
import { getBuilderNode, MyNodeController, defaultUrl, getWebviewController } from "./common"
@Entry
@Component
struct Index {
private nodeController : MyNodeController =
new MyNodeController(getBuilderNode(defaultUrl), getWebviewController(defaultUrl));
build() {
Row() {
Column() {
Button("Attach Webview")
.onClick(() => {
// 注意不要将同一个节点同时挂载在不同的页面上！
this.nodeController.attachWeb();
this.nodeController.rebuild();
})
Button("Detach Webview")
.onClick(() => {
this.nodeController.detachWeb();
this.nodeController.rebuild();
})
// NodeContainer用于与NodeController节点绑定，rebuild会触发makeNode
// Page页通过NodeContainer接口绑定NodeController，实现动态组件页面显示
NodeContainer(this.nodeController)
.height("80%")
.width("80%")
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-manage-upload-download-V14
爬取时间: 2025-04-28 00:24:49
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-file-upload-V14
爬取时间: 2025-04-28 00:25:02
来源: Huawei Developer
Web组件支持前端页面选择文件上传功能，应用开发者可以使用onShowFileSelector()接口来处理前端页面文件上传的请求，如果应用开发者不做任何处理，Web会提供默认行为来处理前端页面文件上传的请求。
下面的示例中，当用户在前端页面点击文件上传按钮，应用侧在onShowFileSelector()接口中收到文件上传请求，在此接口中开发者将上传的本地文件路径设置给前端页面。
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: $rawfile('local.html'), controller: this.controller })
.onShowFileSelector((event) => {
console.log('MyFileUploader onShowFileSelector invoked');
const documentSelectOptions = new picker.DocumentSelectOptions();
let uri: string | null = null;
const documentViewPicker = new picker.DocumentViewPicker();
documentViewPicker.select(documentSelectOptions).then((documentSelectResult) => {
uri = documentSelectResult[0];
console.info('documentViewPicker.select to file succeed and uri is:' + uri);
if (event) {
event.result.handleFileList([uri]);
}
}).catch((err: BusinessError) => {
console.error(`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
})
return true;
})
}
}
}
```
-  local.html页面代码。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-download-V14
爬取时间: 2025-04-28 00:25:16
来源: Huawei Developer
Web组件的下载功能要求应用通过调用WebDownloadItem.start来指定下载文件的保存路径。值得注意的是，WebDownloadItem.start并非启动下载，下载过程实际上在用户点击页面链接时即已开始。WebDownloadItem.start的作用是将已经下载到临时文件的部分移动到指定目标路径，后续未完成的下载的内容将直接保存到指定目标路径，临时目录位于/data/storage/el2/base/cache/web/Temp/。如果决定取消当前下载，应调用WebDownloadItem.cancel，此时临时文件将被删除。
如果不希望在WebDownloadItem.start之前将文件下载到临时目录，可以通过WebDownloadItem.cancel中断下载，后续可通过WebDownloadManager.resumeDownload恢复中断的下载。
监听页面触发的下载
通过setDownloadDelegate()向Web组件注册一个DownloadDelegate来监听页面触发的下载任务。资源由Web组件来下载，Web组件会通过DownloadDelegate将下载的进度通知给应用。
下面的示例中，在应用的rawfile中创建index.html以及download.html。应用启动后会创建一个Web组件并加载index.html，点击setDownloadDelegate按钮向Web组件注册一个DownloadDelegate，点击页面里的下载按钮的时候会触发一个下载任务，在DownloadDelegate中可以监听到下载的进度。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
build() {
Column() {
Button('setDownloadDelegate')
.onClick(() => {
try {
this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
console.log("will start a download.");
// 传入一个下载路径，并开始下载。
// 如果传入一个不存在的路径，则会下载到默认/data/storage/el2/base/cache/web/目录。
webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
})
this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
// 下载任务的唯一标识。
console.log("download update guid: " + webDownloadItem.getGuid());
// 下载的进度。
console.log("download update guid: " + webDownloadItem.getPercentComplete());
// 当前的下载速度。
console.log("download update speed: " + webDownloadItem.getCurrentSpeed())
})
this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
console.log("download failed guid: " + webDownloadItem.getGuid());
// 下载任务失败的错误码。
console.log("download failed guid: " + webDownloadItem.getLastErrorCode());
})
this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
console.log("download finish guid: " + webDownloadItem.getGuid());
})
this.controller.setDownloadDelegate(this.delegate);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: $rawfile('index.html'), controller: this.controller })
}
}
}
```
加载的html文件。
待下载的html文件。
使用Web组件发起一个下载任务
使用startDownload()接口发起一个下载。
Web组件发起的下载会根据当前显示的url以及Web组件默认的Referrer Policy来计算referrer。
在下面的示例中，先点击setDownloadDelegate按钮向Web注册一个监听类，然后点击startDownload主动发起了一个下载，
该下载任务也会通过设置的DownloadDelegate来通知app下载的进度。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
build() {
Column() {
Button('setDownloadDelegate')
.onClick(() => {
try {
this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
console.log("will start a download.");
// 传入一个下载路径，并开始下载。
webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
})
this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
console.log("download update guid: " + webDownloadItem.getGuid());
})
this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
console.log("download failed guid: " + webDownloadItem.getGuid());
})
this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
console.log("download finish guid: " + webDownloadItem.getGuid());
})
this.controller.setDownloadDelegate(this.delegate);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('startDownload')
.onClick(() => {
try {
// 这里指定下载地址为 https://www.example.com/，Web组件会发起一个下载任务将该页面下载下来。
// 开发者需要替换为自己想要下载的内容的地址。
this.controller.startDownload('https://www.example.com/');
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
使用Web组件恢复进程退出时未下载完成的任务
在Web组件启动时，可通过resumeDownload()接口恢复未完成的下载任务。
在以下示例中，通过“record”按钮将当前下载任务保存至持久化文件中，应用重启后，可借助“recovery”按钮恢复持久化的下载任务。示例代码实现了将当前下载任务持久化保存至文件的功能，若需保存多个下载任务，应用可根据需求调整持久化的时机与方式。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { downloadUtil, fileName, filePath } from './downloadUtil'; // downloadUtil.ets 见下文
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
download: webview.WebDownloadItem = new webview.WebDownloadItem();
// 用于记录失败的下载任务。
failedData: Uint8Array = new Uint8Array();
build() {
Column() {
Button('setDownloadDelegate')
.onClick(() => {
try {
this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
console.log("will start a download.");
// 传入一个下载路径，并开始下载。
webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
})
this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
console.log("download update percent complete: " + webDownloadItem.getPercentComplete());
this.download = webDownloadItem;
})
this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
console.log("download failed guid: " + webDownloadItem.getGuid());
// 序列化失败的下载任务到一个字节数组。
this.failedData = webDownloadItem.serialize();
})
this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
console.log("download finish guid: " + webDownloadItem.getGuid());
})
this.controller.setDownloadDelegate(this.delegate);
webview.WebDownloadManager.setDownloadDelegate(this.delegate);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Button('startDownload')
.onClick(() => {
try {
// 这里指定下载地址为 https://www.example.com/，Web组件会发起一个下载任务将该页面下载下来。
// 开发者需要替换为自己想要下载的内容的地址。
this.controller.startDownload('https://www.example.com/');
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
// 将当前的下载任务信息序列化保存，用于后续恢复下载任务。
// 当前用例仅展示下载一个任务的场景，多任务场景请按需扩展。
Button('record')
.onClick(() => {
try {
// 保存当前下载数据到持久化文档中。
downloadUtil.saveDownloadInfo(downloadUtil.uint8ArrayToStr(this.download.serialize()));
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
// 从序列化的下载任务信息中，恢复下载任务。
// 按钮触发时必须保证WebDownloadManager.setDownloadDelegate设置完成。
Button('recovery')
.onClick(() => {
try {
// 当前默认持久化文件存在，用户根据实际情况增加判断。
let webDownloadItem =
webview.WebDownloadItem.deserialize(downloadUtil.strToUint8Array(downloadUtil.readFileSync(filePath, fileName)));
webview.WebDownloadManager.resumeDownload(webDownloadItem);
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
下载任务信息持久化工具类文件。
```typescript
// downloadUtil.ets
import { util } from '@kit.ArkTS';
import fileStream from '@ohos.file.fs';
const helper = new util.Base64Helper();
export const filePath = getContext().filesDir;
export const fileName = 'demoFile.txt';
export namespace  downloadUtil {
export function uint8ArrayToStr(uint8Array: Uint8Array): string {
return helper.encodeToStringSync(uint8Array);
}
export function strToUint8Array(str: string): Uint8Array {
return helper.decodeSync(str);
}
export function saveDownloadInfo(downloadInfo: string): void {
if (!fileExists(filePath)) {
mkDirectorySync(filePath);
}
writeToFileSync(filePath, fileName, downloadInfo);
}
export function fileExists(filePath: string): boolean {
try {
return fileStream.accessSync(filePath);
} catch (error) {
return false;
}
}
export function mkDirectorySync(directoryPath: string, recursion?: boolean): void {
try {
fileStream.mkdirSync(directoryPath, recursion ?? false);
} catch (error) {
console.error(`mk dir error. err message: ${error.message}, err code: ${error.code}`);
}
}
export function writeToFileSync(dir: string, fileName: string, msg: string): void {
let file = fileStream.openSync(dir + '/' + fileName, fileStream.OpenMode.WRITE_ONLY | fileStream.OpenMode.CREATE);
fileStream.writeSync(file.fd, msg);
}
export function readFileSync(dir: string, fileName: string): string {
return fileStream.readTextSync(dir + '/' + fileName);
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-use-multimedia-V14
爬取时间: 2025-04-28 00:25:29
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-rtc-V14
爬取时间: 2025-04-28 00:25:42
来源: Huawei Developer
Web组件可以通过W3C标准协议接口拉起摄像头和麦克风，通过onPermissionRequest接口接收权限请求通知，需在配置文件中声明相应的音频权限。
-  使用摄像头和麦克风功能前请在module.json5中添加音频相关权限，权限的添加方法请参考在配置文件中声明权限。
```json
// src/main/resources/base/element/string.json
{
"name": "reason_for_camera",
"value": "reason_for_camera"
},
{
"name": "reason_for_microphone",
"value": "reason_for_microphone"
}
```
通过在JavaScript中调用W3C标准协议接口navigator.mediaDevices.getUserMedia()，该接口用于拉起摄像头和麦克风。constraints参数是一个包含了video和audio两个成员的MediaStreamConstraints对象，用于说明请求的媒体类型。
在下面的示例中，点击前端页面中的开起摄像头按钮再点击onConfirm，打开摄像头和麦克风。
-  应用侧代码。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl } from '@kit.AbilityKit';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController()
aboutToAppear() {
// 配置Web开启调试模式
webview.WebviewController.setWebDebuggingAccess(true);
// 获取权限请求通知，点击onConfirm按钮后，拉起摄像头和麦克风。
let atManager = abilityAccessCtrl.createAtManager();
atManager.requestPermissionsFromUser(getContext(this), ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'])
.then((data) => {
console.info('data:' + JSON.stringify(data));
console.info('data permissions:' + data.permissions);
console.info('data authResults:' + data.authResults);
}).catch((error: BusinessError) => {
console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
})
}
build() {
Column() {
Web({ src: $rawfile('index.html'), controller: this.controller })
.onPermissionRequest((event) => {
if (event) {
AlertDialog.show({
title: 'title',
message: 'text',
primaryButton: {
value: 'deny',
action: () => {
event.request.deny();
}
},
secondaryButton: {
value: 'onConfirm',
action: () => {
event.request.grant(event.request.getAccessibleResource());
}
},
cancel: () => {
event.request.deny();
}
})
}
})
}
}
}
```
-  前端页面index.html代码。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-takeovers-web-media-V14
爬取时间: 2025-04-28 00:25:55
来源: Huawei Developer
Web组件提供了应用接管网页中媒体播放的能力，用来支持应用增强网页的媒体播放，如画质增强等。
使用场景
网页播放媒体时，存在着网页视频不够清晰、网页的播放器界面简陋功能少、一些视频不能播放的问题。
此时，应用开发者可以使用该功能，通过自己或者第三方的播放器，接管网页媒体播放来改善网页的媒体播放体验。
实现原理
ArkWeb内核播放媒体的框架
不开启该功能时，ArkWeb内核的播放架构如下所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170401.52432682125397446251646536470806:50001231000000:2800:51B949904A64E5FDABE63AFAD0CA8D92B827E5504EE349A7FC8B6F534076B68C.png)
开启该功能后，ArkWeb内核的播放架构如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170401.08262903558908967929898538035485:50001231000000:2800:2E3E7AC1D5AE3C53BB17EDD837541C617214C9F4091FEE6EB0E5F71695C7F7B6.png)
ArkWeb内核与应用的交互
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170401.50049304322972231185328493776598:50001231000000:2800:A842646A6502D24626F55B27F2AA286A4346A7E751A13D22FC4AF211482A0903.png)
开发指导
开启接管网页媒体播放
需要先通过enableNativeMediaPlayer接口，开启接管网页媒体播放的功能。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
.enableNativeMediaPlayer({ enable: true, shouldOverlay: false })
}
}
}
```
创建本地播放器(NativeMediaPlayer)
该功能开启后，每当网页中有媒体需要播放时，ArkWeb内核会触发由onCreateNativeMediaPlayer注册的回调函数。
开发者则需要调用 onCreateNativeMediaPlayer 来注册一个创建本地播放器的回调函数。
该回调函数需要根据媒体信息来判断是否要创建一个本地播放器来接管当前的网页媒体资源。
本地播放器需要实现NativeMediaPlayerBridge接口，以便ArkWeb内核对本地播放器进行播控操作。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
// 实现 webview.NativeMediaPlayerBridge 接口。
// ArkWeb 内核调用该类的方法来对 NativeMediaPlayer 进行播控。
class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
// ... 实现 NativeMediaPlayerBridge 里的接口方法 ...
constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {}
updateRect(x: number, y: number, width: number, height: number) {}
play() {}
pause() {}
seek(targetTime: number) {}
release() {}
setVolume(volume: number) {}
setMuted(muted: boolean) {}
setPlaybackRate(playbackRate: number) {}
enterFullscreen() {}
exitFullscreen() {}
}
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
.enableNativeMediaPlayer({ enable: true, shouldOverlay: false })
.onPageBegin((event) => {
this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
// 判断需不需要接管当前的媒体。
if (!shouldHandle(mediaInfo)) {
// 本地播放器不接管该媒体。
// 返回 null 。ArkWeb 内核将用自己的播放器来播放该媒体。
return null;
}
// 接管当前的媒体。
// 返回一个本地播放器实例给 ArkWeb 内核。
let nativePlayer: webview.NativeMediaPlayerBridge = new NativeMediaPlayerImpl(handler, mediaInfo);
return nativePlayer;
});
})
}
}
}
// stub
function shouldHandle(mediaInfo: webview.MediaInfo) {
return true;
}
```
绘制本地播放器组件
应用接管网页的媒体后，开发者需要将本地播放器组件及视频画面绘制到ArkWeb内核提供的Surface上。ArkWeb内核再将Surface与网页进行合成，最后上屏显示。
该流程与同层渲染绘制相同。
1.  在应用启动阶段，应保存UIContext，以便后续的同层渲染绘制流程能够使用该UIContext。
```typescript
// xxxAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage): void {
windowStage.loadContent('pages/Index', (err, data) => {
if (err.code) {
return;
}
// 保存UIContext， 在后续的同层渲染绘制中使用。
AppStorage.setOrCreate<UIContext>("UIContext", windowStage.getMainWindowSync().getUIContext());
});
}
// ... 其他需要重写的方法 ...
}
```
2.  使用ArkWeb内核创建的Surface进行同层渲染绘制。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BuilderNode, FrameNode, NodeController, NodeRenderType } from '@kit.ArkUI';
interface ComponentParams {}
class MyNodeController extends NodeController {
private rootNode: BuilderNode<[ComponentParams]> | undefined;
constructor(surfaceId: string, renderType: NodeRenderType) {
super();
// 获取之前保存的 UIContext 。
let uiContext = AppStorage.get<UIContext>("UIContext");
this.rootNode = new BuilderNode(uiContext as UIContext, { surfaceId: surfaceId, type: renderType });
}
makeNode(uiContext: UIContext): FrameNode | null {
if (this.rootNode) {
return this.rootNode.getFrameNode() as FrameNode;
}
return null;
}
build() {
// 构造本地播放器组件
}
}
@Entry
@Component
struct WebComponent {
node_controller?: MyNodeController;
controller: webview.WebviewController = new webview.WebviewController();
@State show_native_media_player: boolean = false;
build() {
Column() {
Stack({ alignContent: Alignment.TopStart }) {
if (this.show_native_media_player) {
NodeContainer(this.node_controller)
.width(300)
.height(150)
.backgroundColor(Color.Transparent)
.border({ width: 2, color: Color.Orange })
}
Web({ src: 'www.example.com', controller: this.controller })
.enableNativeMediaPlayer({ enable: true, shouldOverlay: false })
.onPageBegin((event) => {
this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo:    webview.MediaInfo) => {
// 接管当前的媒体。
// 使用同层渲染流程提供的 surface 来构造一个本地播放器组件。
this.node_controller = new MyNodeController(mediaInfo.surfaceInfo.id, NodeRenderType.RENDER_TYPE_TEXTURE);
this.node_controller.build();
// 展示本地播放器组件。
this.show_native_media_player = true;
// 返回一个本地播放器实例给 ArkWeb 内核。
return null;
});
})
}
}
}
}
```
动态创建组件并绘制到Surface上的详细介绍见同层渲染绘制。
执行ArkWeb内核发送给本地播放器的播控指令
为了方便ArkWeb内核对本地播放器进行播控操作，应用开发者需要令本地播放器实现NativeMediaPlayerBridge接口，并根据每个接口方法的功能对本地播放器进行相应操作。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
class ActualNativeMediaPlayerListener {
constructor(handler: webview.NativeMediaPlayerHandler) {}
}
class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
// 1. 创建一个本地播放器的状态监听。
let listener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
// 2. 创建一个本地播放器。
// 3. 监听该本地播放器。
// ...
}
updateRect(x: number, y: number, width: number, height: number) {
// <video> 标签的位置和大小发生了变化。
// 根据该信息变化，作出相应的改变。
}
play() {
// 启动本地播放器播放。
}
pause() {
// 暂停本地播放器播放。
}
seek(targetTime: number) {
// 本地播放器跳转到指定的时间点。
}
release() {
// 销毁本地播放器。
}
setVolume(volume: number) {
// ArkWeb 内核要求调整本地播放器的音量。
// 设置本地播放器的音量。
}
setMuted(muted: boolean) {
// 将本地播放器静音或取消静音。
}
setPlaybackRate(playbackRate: number) {
// 调整本地播放器的播放速度。
}
enterFullscreen() {
// 将本地播放器设置为全屏播放。
}
exitFullscreen() {
// 将本地播放器退出全屏播放。
}
}
```
将本地播放器的状态信息通知给ArkWeb内核
ArkWeb内核需要本地播放器的状态信息来更新到网页（例如：视频的宽高、播放时间、缓存时间等），因此，应用开发者需要将本地播放器的状态信息通知给ArkWeb内核。
在onCreateNativeMediaPlayer接口中， ArkWeb内核传递给应用一个NativeMediaPlayerHandler对象。应用开发者需要通过该对象，将本地播放器的最新状态信息通知给ArkWeb内核。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
class ActualNativeMediaPlayerListener {
handler: webview.NativeMediaPlayerHandler;
constructor(handler: webview.NativeMediaPlayerHandler) {
this.handler = handler;
}
onPlaying() {
// 本地播放器开始播放。
this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
}
onPaused() {
// 本地播放器暂停播放。
this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
}
onSeeking() {
// 本地播放器开始执行跳转到目标时间点。
this.handler.handleSeeking();
}
onSeekDone() {
// 本地播放器 seek 完成。
this.handler.handleSeekFinished();
}
onEnded() {
// 本地播放器播放完成。
this.handler.handleEnded();
}
onVolumeChanged() {
// 获取本地播放器的音量。
let volume: number = getVolume();
this.handler.handleVolumeChanged(volume);
}
onCurrentPlayingTimeUpdate() {
// 更新播放时间。
let currentTime: number = getCurrentPlayingTime();
// 将时间单位换算成秒。
let currentTimeInSeconds = convertToSeconds(currentTime);
this.handler.handleTimeUpdate(currentTimeInSeconds);
}
onBufferedChanged() {
// 缓存发生了变化。
// 获取本地播放器的缓存时长。
let bufferedEndTime: number = getCurrentBufferedTime();
// 将时间单位换算成秒。
let bufferedEndTimeInSeconds = convertToSeconds(bufferedEndTime);
this.handler.handleBufferedEndTimeChanged(bufferedEndTimeInSeconds);
// 检查缓存状态。
// 如果缓存状态发生了变化，则向 ArkWeb 内核通知缓存状态。
let lastReadyState: webview.ReadyState = getLastReadyState();
let currentReadyState: webview.ReadyState = getCurrentReadyState();
if (lastReadyState != currentReadyState) {
this.handler.handleReadyStateChanged(currentReadyState);
}
}
onEnterFullscreen() {
// 本地播放器进入了全屏状态。
let isFullscreen: boolean = true;
this.handler.handleFullscreenChanged(isFullscreen);
}
onExitFullscreen() {
// 本地播放器退出了全屏状态。
let isFullscreen: boolean = false;
this.handler.handleFullscreenChanged(isFullscreen);
}
onUpdateVideoSize(width: number, height: number) {
// 当本地播放器解析出视频宽高时， 通知 ArkWeb 内核。
this.handler.handleVideoSizeChanged(width, height);
}
onDurationChanged(duration: number) {
// 本地播放器解析到了新的媒体时长， 通知 ArkWeb 内核。
this.handler.handleDurationChanged(duration);
}
onError(error: webview.MediaError, errorMessage: string) {
// 本地播放器出错了，通知 ArkWeb 内核。
this.handler.handleError(error, errorMessage);
}
onNetworkStateChanged(state: webview.NetworkState) {
// 本地播放器的网络状态发生了变化， 通知 ArkWeb 内核。
this.handler.handleNetworkStateChanged(state);
}
onPlaybackRateChanged(playbackRate: number) {
// 本地播放器的播放速率发生了变化， 通知 ArkWeb 内核。
this.handler.handlePlaybackRateChanged(playbackRate);
}
onMutedChanged(muted: boolean) {
// 本地播放器的静音状态发生了变化， 通知 ArkWeb 内核。
this.handler.handleMutedChanged(muted);
}
// ... 监听本地播放器其他的状态 ...
}
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
@State show_native_media_player: boolean = false;
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
.enableNativeMediaPlayer({enable: true, shouldOverlay: false})
.onPageBegin((event) => {
this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
// 接管当前的媒体。
// 创建一个本地播放器实例。
// let nativePlayer: NativeMediaPlayerImpl = new NativeMediaPlayerImpl(handler, mediaInfo);
// 创建一个本地播放器状态监听对象。
let nativeMediaPlayerListener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
// 监听本地播放器状态。
// nativePlayer.setListener(nativeMediaPlayerListener);
// 返回这个本地播放器实例给 ArkWeb 内核。
return null;
});
})
}
}
}
// stub
function getVolume() {
return 1;
}
function getCurrentPlayingTime() {
return 1;
}
function getCurrentBufferedTime() {
return 1;
}
function convertToSeconds(input: number) {
return input;
}
function getLastReadyState() {
return webview.ReadyState.HAVE_NOTHING;
}
function getCurrentReadyState() {
return webview.ReadyState.HAVE_NOTHING;
}
```
完整示例
-  使用前请在module.json5添加如下权限。
```typescript
"ohos.permission.INTERNET"
```
-  应用侧代码，在应用启动阶段保存UIContext。
```typescript
// xxxAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage): void {
windowStage.loadContent('pages/Index', (err, data) => {
if (err.code) {
return;
}
// 保存 UIContext， 在后续的同层渲染绘制中会用到。
AppStorage.setOrCreate<UIContext>("UIContext", windowStage.getMainWindowSync().getUIContext());
});
}
// ... 其他需要重写的方法 ...
}
```
-  应用侧代码，视频托管使用示例。
```typescript
// Index.ets
import { webview } from '@kit.ArkWeb';
import { BuilderNode, FrameNode, NodeController, NodeRenderType, UIContext } from '@kit.ArkUI';
import { AVPlayerDemo, AVPlayerListener } from './PlayerDemo';
// 实现 webview.NativeMediaPlayerBridge 接口。
// ArkWeb 内核调用该类的方法来对 NativeMediaPlayer 进行播控。
class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
private surfaceId: string;
mediaSource: string;
private mediaHandler: webview.NativeMediaPlayerHandler;
nativePlayerInfo: NativePlayerInfo;
nativePlayer: AVPlayerDemo;
httpHeaders: Record<string, string>;
constructor(nativePlayerInfo: NativePlayerInfo, handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
console.log(`NativeMediaPlayerImpl.constructor, surface_id[${mediaInfo.surfaceInfo.id}]`);
this.nativePlayerInfo = nativePlayerInfo;
this.mediaHandler = handler;
this.surfaceId = mediaInfo.surfaceInfo.id;
this.mediaSource = mediaInfo.mediaSrcList.find((item)=>{item.source.indexOf('.mp4') > 0})?.source
|| mediaInfo.mediaSrcList[0].source;
this.httpHeaders = mediaInfo.headers;
this.nativePlayer = new AVPlayerDemo();
// 使用同层渲染功能，将视频及其播控组件绘制到网页中
this.nativePlayerInfo.node_controller = new MyNodeController(
this.nativePlayerInfo, this.surfaceId, this.mediaHandler, this, NodeRenderType.RENDER_TYPE_TEXTURE);
this.nativePlayerInfo.node_controller.build();
this.nativePlayerInfo.show_native_media_player = true;
console.log(`NativeMediaPlayerImpl.mediaSource: ${this.mediaSource}, headers: ${JSON.stringify(this.httpHeaders)}`);
}
updateRect(x: number, y: number, width: number, height: number): void {
let width_in_vp = px2vp(width);
let height_in_vp = px2vp(height);
console.log(`updateRect(${x}, ${y}, ${width}, ${height}), vp:{${width_in_vp}, ${height_in_vp}}`);
this.nativePlayerInfo.updateNativePlayerRect(x, y, width, height);
}
play() {
console.log('NativeMediaPlayerImpl.play');
this.nativePlayer.play();
}
pause() {
console.log('NativeMediaPlayerImpl.pause');
this.nativePlayer.pause();
}
seek(targetTime: number) {
console.log(`NativeMediaPlayerImpl.seek(${targetTime})`);
this.nativePlayer.seek(targetTime);
}
setVolume(volume: number) {
console.log(`NativeMediaPlayerImpl.setVolume(${volume})`);
this.nativePlayer.setVolume(volume);
}
setMuted(muted: boolean) {
console.log(`NativeMediaPlayerImpl.setMuted(${muted})`);
}
setPlaybackRate(playbackRate: number) {
console.log(`NativeMediaPlayerImpl.setPlaybackRate(${playbackRate})`);
this.nativePlayer.setPlaybackRate(playbackRate);
}
release() {
console.log('NativeMediaPlayerImpl.release');
this.nativePlayer?.release();
this.nativePlayerInfo.show_native_media_player = false;
this.nativePlayerInfo.node_width = 300;
this.nativePlayerInfo.node_height = 150;
this.nativePlayerInfo.destroyed();
}
enterFullscreen() {
console.log('NativeMediaPlayerImpl.enterFullscreen');
}
exitFullscreen() {
console.log('NativeMediaPlayerImpl.exitFullscreen');
}
}
// 监听NativeMediaPlayer的状态，然后通过 webview.NativeMediaPlayerHandler 将状态上报给 ArkWeb 内核。
class AVPlayerListenerImpl implements AVPlayerListener {
handler: webview.NativeMediaPlayerHandler;
component: NativePlayerComponent;
constructor(handler: webview.NativeMediaPlayerHandler, component: NativePlayerComponent) {
this.handler = handler;
this.component = component;
}
onPlaying() {
console.log('AVPlayerListenerImpl.onPlaying');
this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
}
onPaused() {
console.log('AVPlayerListenerImpl.onPaused');
this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
}
onDurationChanged(duration: number) {
console.log(`AVPlayerListenerImpl.onDurationChanged(${duration})`);
this.handler.handleDurationChanged(duration);
}
onBufferedTimeChanged(buffered: number) {
console.log(`AVPlayerListenerImpl.onBufferedTimeChanged(${buffered})`);
this.handler.handleBufferedEndTimeChanged(buffered);
}
onTimeUpdate(time: number) {
this.handler.handleTimeUpdate(time);
}
onEnded() {
console.log('AVPlayerListenerImpl.onEnded');
this.handler.handleEnded();
}
onError() {
console.log('AVPlayerListenerImpl.onError');
this.component.has_error = true;
setTimeout(()=>{
this.handler.handleError(1, "Oops!");
}, 200);
}
onVideoSizeChanged(width: number, height: number) {
console.log(`AVPlayerListenerImpl.onVideoSizeChanged(${width}, ${height})`);
this.handler.handleVideoSizeChanged(width, height);
this.component.onSizeChanged(width, height);
}
onDestroyed(): void {
console.log('AVPlayerListenerImpl.onDestroyed');
}
}
interface ComponentParams {
text: string;
text2: string;
playerInfo: NativePlayerInfo;
handler: webview.NativeMediaPlayerHandler;
player: NativeMediaPlayerImpl;
}
// 自定义的播放器组件
@Component
struct NativePlayerComponent {
params?: ComponentParams;
@State bgColor: Color = Color.Red;
mXComponentController: XComponentController = new XComponentController();
videoController: VideoController = new VideoController();
offset_x: number = 0;
offset_y: number = 0;
@State video_width_percent: number = 100;
@State video_height_percent: number = 100;
view_width: number = 0;
view_height: number = 0;
video_width: number = 0;
video_height: number = 0;
fullscreen: boolean = false;
@State has_error: boolean = false;
onSizeChanged(width: number, height: number) {
this.video_width = width;
this.video_height = height;
let scale: number = this.view_width / width;
let scaled_video_height: number = scale * height;
this.video_height_percent = scaled_video_height / this.view_height * 100;
console.log(`NativePlayerComponent.onSizeChanged(${width},${height}), video_height_percent[${this.video_height_percent }]`);
}
build() {
Column() {
Stack() {
XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.mXComponentController })
.width(this.video_width_percent + '%')
.height(this.video_height_percent + '%')
.onLoad(()=>{
if (!this.params) {
console.log('this.params is null');
return;
}
console.log('NativePlayerComponent.onLoad, params[' + this.params
+ '], text[' + this.params.text + '], text2[' + this.params.text2
+ '], web_tab[' + this.params.playerInfo + '], handler[' + this.params.handler + ']');
this.params.player.nativePlayer.setSurfaceID(this.mXComponentController.getXComponentSurfaceId());
this.params.player.nativePlayer.avPlayerLiveDemo({
url: this.params.player.mediaSource,
listener: new AVPlayerListenerImpl(this.params.handler, this),
httpHeaders: this.params.player.httpHeaders,
});
})
Column() {
Row() {
Button(this.params?.text)
.height(50)
.border({ width: 2, color: Color.Red })
.backgroundColor(this.bgColor)
.onClick(()=>{
console.log(`NativePlayerComponent.Button[${this.params?.text}] is clicked`);
this.params?.player.nativePlayer?.play();
})
.onTouch((event: TouchEvent) => {
event.stopPropagation();
})
Button(this.params?.text2)
.height(50)
.border({ width: 2, color: Color.Red })
.onClick(()=>{
console.log(`NativePlayerComponent.Button[${this.params?.text2}] is clicked`);
this.params?.player.nativePlayer?.pause();
})
.onTouch((event: TouchEvent) => {
event.stopPropagation();
})
}
.width('100%')
.justifyContent(FlexAlign.SpaceEvenly)
}
if (this.has_error) {
Column() {
Text('Error')
.fontSize(30)
}
.backgroundColor('#eb5555')
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
}
}
.width('100%')
.height('100%')
.onAreaChange((oldValue: Area, newValue: Area) => {
console.log(`NativePlayerComponent.onAreaChange(${JSON.stringify(oldValue)}, ${JSON.stringify(newValue)})`);
this.view_width = new Number(newValue.width).valueOf();
this.view_height = new Number(newValue.height).valueOf();
this.onSizeChanged(this.video_width, this.video_height);
})
}
}
@Builder
function NativePlayerComponentBuilder(params: ComponentParams) {
NativePlayerComponent({ params: params })
.backgroundColor(Color.Green)
.border({ width: 1, color: Color.Brown })
.width('100%')
.height('100%')
}
// 通过 NodeController 来动态创建自定义的播放器组件， 并将组件内容绘制到 surfaceId 指定的 surface 上。
class MyNodeController extends NodeController {
private rootNode: BuilderNode<[ComponentParams]> | undefined;
playerInfo: NativePlayerInfo;
listener: webview.NativeMediaPlayerHandler;
player: NativeMediaPlayerImpl;
constructor(playerInfo: NativePlayerInfo,
surfaceId: string,
listener: webview.NativeMediaPlayerHandler,
player: NativeMediaPlayerImpl,
renderType: NodeRenderType) {
super();
this.playerInfo = playerInfo;
this.listener = listener;
this.player = player;
let uiContext = AppStorage.get<UIContext>("UIContext");
this.rootNode = new BuilderNode(uiContext as UIContext, { surfaceId: surfaceId, type: renderType });
console.log(`MyNodeController, rootNode[${this.rootNode}], playerInfo[${playerInfo}], listener[${listener}], surfaceId[${surfaceId}]`);
}
makeNode(): FrameNode | null {
if (this.rootNode) {
return this.rootNode.getFrameNode() as FrameNode;
}
return null;
}
build() {
let params: ComponentParams = {
"text": "play",
"text2": "pause",
playerInfo: this.playerInfo,
handler: this.listener,
player: this.player
};
if (this.rootNode) {
this.rootNode.build(wrapBuilder(NativePlayerComponentBuilder), params);
}
}
postTouchEvent(event: TouchEvent) {
return this.rootNode?.postTouchEvent(event);
}
}
class Rect {
x: number = 0;
y: number = 0;
width: number = 0;
height: number = 0;
static toNodeRect(rectInPx: webview.RectEvent) : Rect {
let rect = new Rect();
rect.x = px2vp(rectInPx.x);
rect.y = px2vp(rectInPx.x);
rect.width = px2vp(rectInPx.width);
rect.height = px2vp(rectInPx.height);
return rect;
}
}
@Observed
class NativePlayerInfo {
public web: WebComponent;
public embed_id: string;
public player: webview.NativeMediaPlayerBridge;
public node_controller?: MyNodeController;
public show_native_media_player: boolean = false;
public node_pos_x: number;
public node_pos_y: number;
public node_width: number;
public node_height: number;
playerComponent?: NativeMediaPlayerComponent;
constructor(web: WebComponent, handler: webview.NativeMediaPlayerHandler, videoInfo: webview.MediaInfo) {
this.web = web;
this.embed_id = videoInfo.embedID;
let node_rect = Rect.toNodeRect(videoInfo.surfaceInfo.rect);
this.node_pos_x = node_rect.x;
this.node_pos_y = node_rect.y;
this.node_width = node_rect.width;
this.node_height = node_rect.height;
this.player = new NativeMediaPlayerImpl(this, handler, videoInfo);
}
updateNativePlayerRect(x: number, y: number, width: number, height: number) {
this.playerComponent?.updateNativePlayerRect(x, y, width, height);
}
destroyed() {
let info_list = this.web.native_player_info_list;
console.log(`NativePlayerInfo[${this.embed_id}] destroyed, list.size[${info_list.length}]`);
this.web.native_player_info_list = info_list.filter((item) => item.embed_id != this.embed_id);
console.log(`NativePlayerInfo after destroyed, new_list.size[${this.web.native_player_info_list.length}]`);
}
}
@Component
struct NativeMediaPlayerComponent {
@ObjectLink playerInfo: NativePlayerInfo;
aboutToAppear() {
this.playerInfo.playerComponent = this;
}
build() {
NodeContainer(this.playerInfo.node_controller)
.width(this.playerInfo.node_width)
.height(this.playerInfo.node_height)
.offset({x: this.playerInfo.node_pos_x, y: this.playerInfo.node_pos_y})
.backgroundColor(Color.Transparent)
.border({ width: 2, color: Color.Orange })
.onAreaChange((oldValue, newValue) => {
console.log(`NodeContainer[${this.playerInfo.embed_id}].onAreaChange([${oldValue.width} x ${oldValue.height}]->[${newValue.width} x ${newValue.height}]`);
})
}
updateNativePlayerRect(x: number, y: number, width: number, height: number) {
let node_rect = Rect.toNodeRect({x, y, width, height});
this.playerInfo.node_pos_x = node_rect.x;
this.playerInfo.node_pos_y = node_rect.y;
this.playerInfo.node_width = node_rect.width;
this.playerInfo.node_height = node_rect.height;
}
}
@Entry
@Component
struct WebComponent {
controller: WebviewController = new webview.WebviewController();
page_url: Resource = $rawfile('main.html');
@State native_player_info_list: NativePlayerInfo[] = [];
area?: Area;
build() {
Column() {
Stack({alignContent: Alignment.TopStart}) {
ForEach(this.native_player_info_list, (item: NativePlayerInfo) => {
if (item.show_native_media_player) {
NativeMediaPlayerComponent({ playerInfo: item })
}
}, (item: NativePlayerInfo) => {
return item.embed_id;
})
Web({ src: this.page_url, controller: this.controller })
.enableNativeMediaPlayer({ enable: true, shouldOverlay: true })
.onPageBegin(() => {
this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
console.log('onCreateNativeMediaPlayer(' + JSON.stringify(mediaInfo) + ')');
let nativePlayerInfo = new NativePlayerInfo(this, handler, mediaInfo);
this.native_player_info_list.push(nativePlayerInfo);
return nativePlayerInfo.player;
});
})
.onNativeEmbedGestureEvent((event)=>{
if (!event.touchEvent || !event.embedId) {
event.result?.setGestureEventResult(false);
return;
}
console.log(`WebComponent.onNativeEmbedGestureEvent, embedId[${event.embedId}]`);
let native_player_info = this.getNativePlayerInfoByEmbedId(event.embedId);
if (!native_player_info) {
console.log(`WebComponent.onNativeEmbedGestureEvent, embedId[${event.embedId}], no native_player_info`);
event.result?.setGestureEventResult(false);
return;
}
if (!native_player_info.node_controller) {
console.log(`WebComponent.onNativeEmbedGestureEvent, embedId[${event.embedId}], no node_controller`);
event.result?.setGestureEventResult(false);
return;
}
let ret = native_player_info.node_controller.postTouchEvent(event.touchEvent);
console.log(`WebComponent.postTouchEvent, ret[${ret}], touchEvent[${JSON.stringify(event.touchEvent)}]`);
event.result?.setGestureEventResult(ret);
})
.width('100%')
.height('100%')
.onAreaChange((oldValue: Area, newValue: Area) => {
oldValue;
this.area = newValue;
})
}
}
}
getNativePlayerInfoByEmbedId(embedId: string) : NativePlayerInfo | undefined {
return this.native_player_info_list.find((item)=> item.embed_id == embedId);
}
}
```
-  应用侧代码，视频播放示例, ./PlayerDemo.ets。
```typescript
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
export interface AVPlayerListener {
onPlaying() : void;
onPaused() : void;
onDurationChanged(duration: number) : void;
onBufferedTimeChanged(buffered: number) : void;
onTimeUpdate(time: number) : void;
onEnded() : void;
onError() : void;
onVideoSizeChanged(width: number, height: number): void;
onDestroyed(): void;
}
interface PlayerParam {
url: string;
listener?: AVPlayerListener;
httpHeaders?: Record<string, string>;
}
interface PlayCommand {
func: Function;
name?: string;
}
interface CheckPlayCommandResult {
ignore: boolean;
index_to_remove: number;
}
export class AVPlayerDemo {
private surfaceID: string = ''; // surfaceID用于播放画面显示，具体的值需要通过Xcomponent接口获取，相关文档链接见上面Xcomponent创建方法
avPlayer?: media.AVPlayer;
prepared: boolean = false;
commands: PlayCommand[] = [];
setSurfaceID(surface_id: string) {
console.log(`AVPlayerDemo.setSurfaceID : ${surface_id}`);
this.surfaceID = surface_id;
}
// 注册avplayer回调函数
setAVPlayerCallback(avPlayer: media.AVPlayer, listener?: AVPlayerListener) {
// seek操作结果回调函数
avPlayer.on('seekDone', (seekDoneTime: number) => {
console.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
});
// error回调监听函数,当avPlayer在操作过程中出现错误时调用reset接口触发重置流程
avPlayer.on('error', (err: BusinessError) => {
console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
listener?.onError();
avPlayer.reset(); // 调用reset重置资源，触发idle状态
});
// 状态机变化回调函数
avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
switch (state) {
case 'idle': // 成功调用reset接口后触发该状态机上报
console.info('AVPlayer state idle called.');
avPlayer.release(); // 调用release接口销毁实例对象
break;
case 'initialized': // avplayer 设置播放源后触发该状态上报
console.info('AVPlayer state initialized called.');
avPlayer.surfaceId = this.surfaceID; // 设置显示画面，当播放的资源为纯音频时无需设置
avPlayer.prepare();
break;
case 'prepared': // prepare调用成功后上报该状态机
console.info('AVPlayer state prepared called.');
this.prepared = true;
this.schedule();
break;
case 'playing': // play成功调用后触发该状态机上报
console.info('AVPlayer state playing called.');
listener?.onPlaying();
break;
case 'paused': // pause成功调用后触发该状态机上报
console.info('AVPlayer state paused called.');
listener?.onPaused();
break;
case 'completed': // 播放结束后触发该状态机上报
console.info('AVPlayer state completed called.');
avPlayer.stop(); //调用播放结束接口
break;
case 'stopped': // stop接口成功调用后触发该状态机上报
console.info('AVPlayer state stopped called.');
listener?.onEnded();
break;
case 'released':
this.prepared = false;
listener?.onDestroyed();
console.info('AVPlayer state released called.');
break;
default:
console.info('AVPlayer state unknown called.');
break;
}
});
avPlayer.on('durationUpdate', (duration: number) => {
console.info(`AVPlayer state durationUpdate success,new duration is :${duration}`);
listener?.onDurationChanged(duration/1000);
});
avPlayer.on('timeUpdate', (time:number) => {
listener?.onTimeUpdate(time/1000);
});
avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
console.info(`AVPlayer state bufferingUpdate success,and infoType value is:${infoType}, value is : ${value}`);
if (infoType == media.BufferingInfoType.BUFFERING_PERCENT) {
}
listener?.onBufferedTimeChanged(value);
})
avPlayer.on('videoSizeChange', (width: number, height: number) => {
console.info(`AVPlayer state videoSizeChange success,and width is:${width}, height is : ${height}`);
listener?.onVideoSizeChanged(width, height);
})
}
// 以下demo为通过url设置网络地址来实现播放直播码流的demo
async avPlayerLiveDemo(playerParam: PlayerParam) {
// 创建avPlayer实例对象
this.avPlayer = await media.createAVPlayer();
// 创建状态机变化回调函数
this.setAVPlayerCallback(this.avPlayer, playerParam.listener);
let mediaSource: media.MediaSource = media.createMediaSourceWithUrl(playerParam.url, playerParam.httpHeaders);
let strategy: media.PlaybackStrategy = {
preferredWidth: 100,
preferredHeight: 100,
preferredBufferDuration: 100,
preferredHdr: false
};
this.avPlayer.setMediaSource(mediaSource, strategy);
console.log(`AVPlayer url:[${playerParam.url}]`);
}
schedule() {
if (!this.avPlayer) {
return;
}
if (!this.prepared) {
return;
}
if (this.commands.length > 0) {
let command = this.commands.shift();
if (command) {
command.func();
}
if (this.commands.length > 0) {
setTimeout(() => {
this.schedule();
});
}
}
}
private checkCommand(selfName: string, oppositeName: string) {
let index_to_remove = -1;
let ignore_this_action = false;
let index = this.commands.length - 1;
while (index >= 0) {
if (this.commands[index].name == selfName) {
ignore_this_action = true;
break;
}
if (this.commands[index].name == oppositeName) {
index_to_remove = index;
break;
}
index--;
}
let result : CheckPlayCommandResult = {
ignore: ignore_this_action,
index_to_remove: index_to_remove,
};
return result;
}
play() {
let commandName = 'play';
let checkResult = this.checkCommand(commandName, 'pause');
if (checkResult.ignore) {
console.log(`AVPlayer ${commandName} ignored.`);
this.schedule();
return;
}
if (checkResult.index_to_remove >= 0) {
let removedCommand = this.commands.splice(checkResult.index_to_remove, 1);
console.log(`AVPlayer ${JSON.stringify(removedCommand)} removed.`);
return;
}
this.commands.push({ func: ()=>{
console.info('AVPlayer.play()');
this.avPlayer?.play();
}, name: commandName});
this.schedule();
}
pause() {
let commandName = 'pause';
let checkResult = this.checkCommand(commandName, 'play');
console.log(`checkResult:${JSON.stringify(checkResult)}`);
if (checkResult.ignore) {
console.log(`AVPlayer ${commandName} ignored.`);
this.schedule();
return;
}
if (checkResult.index_to_remove >= 0) {
let removedCommand = this.commands.splice(checkResult.index_to_remove, 1);
console.log(`AVPlayer ${JSON.stringify(removedCommand)} removed.`);
return;
}
this.commands.push({ func: ()=>{
console.info('AVPlayer.pause()');
this.avPlayer?.pause();
}, name: commandName});
this.schedule();
}
release() {
this.commands.push({ func: ()=>{
console.info('AVPlayer.release()');
this.avPlayer?.release();
}});
this.schedule();
}
seek(time: number) {
this.commands.push({ func: ()=>{
console.info(`AVPlayer.seek(${time})`);
this.avPlayer?.seek(time * 1000);
}});
this.schedule();
}
setVolume(volume: number) {
this.commands.push({ func: ()=>{
console.info(`AVPlayer.setVolume(${volume})`);
this.avPlayer?.setVolume(volume);
}});
this.schedule();
}
setPlaybackRate(playbackRate: number) {
let speed = media.PlaybackSpeed.SPEED_FORWARD_1_00_X;
let delta = 0.05;
playbackRate += delta;
if (playbackRate < 1) {
speed = media.PlaybackSpeed.SPEED_FORWARD_0_75_X;
} else if (playbackRate < 1.25) {
speed = media.PlaybackSpeed.SPEED_FORWARD_1_00_X;
} else if (playbackRate < 1.5) {
speed = media.PlaybackSpeed.SPEED_FORWARD_1_25_X;
} else if (playbackRate < 2) {
speed = media.PlaybackSpeed.SPEED_FORWARD_1_75_X;
} else {
speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
}
this.commands.push({ func: ()=>{
console.info(`AVPlayer.setSpeed(${speed})`);
this.avPlayer?.setSpeed(speed);
}});
this.schedule();
}
}
```
-  前端页面示例。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-process-page-content-V14
爬取时间: 2025-04-28 00:26:08
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-print-V14
爬取时间: 2025-04-28 00:26:22
来源: Huawei Developer
Web组件打印html页面时可通过W3C标准协议接口和应用接口两种方式实现。
使用打印功能前，请在module.json5中配置相关权限，添加方法请参考在配置文件中声明权限。
使用W3C标准协议接口拉起打印
通过创建打印适配器，拉起打印应用，并对当前Web页面内容进行渲染，渲染后生成的PDF文件信息通过fd传递给打印框架。W3C标准协议接口window.print()方法用于打印当前页面或弹出打印对话框。该方法没有任何参数，只需要在JavaScript中调用即可。
可通过前端css样式控制是否打印，例如@media print。再通过web加载该html页面的方式运行。
-  print.html页面代码。
-  应用侧代码。
```typescript
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct Index {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Row() {
Column() {
Web({ src: $rawfile("print.html"), controller: this.controller })
.javaScriptAccess(true)
}
.width('100%')
}
.height('100%')
}
}
```
通过调用应用侧接口拉起打印。
应用侧通过调用createWebPrintDocumentAdapter创建打印适配器，通过将适配器传入打印的print接口调起打印。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { print } from '@kit.BasicServicesKit'
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Button('createWebPrintDocumentAdapter')
.onClick(() => {
try {
let webPrintDocadapter = this.controller.createWebPrintDocumentAdapter('example.pdf');
print.print('example_jobid', webPrintDocadapter, null, getContext());
} catch (error) {
console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
}
})
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-pdf-preview-V14
爬取时间: 2025-04-28 00:26:36
来源: Huawei Developer
Web组件提供了在网页中预览PDF的能力。应用可以通过Web组件的src参数和loadUrl()接口中传入PDF文件，来加载PDF文档。根据PDF文档来源不同，可以分为三种常用场景：加载网络PDF文档、加载本地PDF文档、加载应用内resource资源PDF文档。
PDF文档预览加载过程中，若涉及网络文档获取，请在module.json5中配置网络访问权限，添加方法请参考在配置文件中声明权限。
在下面的示例中，Web组件创建时指定默认加载的网络PDF文档 www.example.com/test.pdf，该地址为示例，使用时需替换为真实可访问地址:
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({
src:
"https://www.example.com/test.pdf",                     // 方式一 加载网络PDF文档
// getContext(this).filesDir + "/test.pdf", // 方式二 加载本地应用沙箱内PDF文档
// "resource://rawfile/test.pdf",                         // 方式三 应用内resource资源PDF文档
// $rawfile('test.pdf'),                                 // 方式四 应用内resource资源PDF文档
controller: this.controller
})
.domStorageAccess(true)
}
}
}
```
上述示例中，由于PDF预览页面对于侧边导航栏是否展开会根据用户操作使用window.localStorage进行持久化记录，所以需开启文档对象模型存储domStorageAccess权限:
在Web组件创建时，指定默认加载的PDF文档。在默认PDF文档加载完成后，如果需要变更此Web组件显示的PDF文档，可以通过调用loadUrl()接口加载指定的PDF文档。Web组件的第一个参数变量src不能通过状态变量（例如：@State）动态更改地址，如需更改，请通过loadUrl()重新加载。
同时包含三种PDF文档加载预览场景:
-  预览加载网络PDF文件。
```typescript
Web({
src: "https://www.example.com/test.pdf",
controller: this.controller
})
.domStorageAccess(true)
```
-  预览加载应用沙箱内PDF文件，需要开启应用中文件系统的访问fileAccess权限。
```typescript
Web({
src: getContext(this).filesDir + "/test.pdf",
controller: this.controller
})
.domStorageAccess(true)
.fileAccess(true)
```
-  预览加载应用内PDF资源文件，有两种使用形式。$rawfile('test.pdf')形式无法指定下面介绍的预览参数。
```typescript
Web({
src: "resource://rawfile/test.pdf", // 或 $rawfile('test.pdf')
controller: this.controller
})
.domStorageAccess(true)
```
此外，通过配置PDF文件预览参数，可以控制打开预览时页面状态。
当前支持如下参数:
| 语法 | 描述 |
| --- | --- |
| nameddest=destination | 指定PDF文档中的命名目标。 |
| page=pagenum | 使用整数指定文档中的页码，文档第一页的pagenum值为1。 |
| zoom=scale zoom=scale,left,top | 使用浮点或整数值设置缩放和滚动系数。 例如：缩放值100表示缩放值为100%。 向左和向上滚动值位于坐标系中，0,0 表示可见页面的左上角，无论文档如何旋转。 |
| toolbar=1 | 0 | 打开或关闭顶部工具栏。 |
| navpanes=1 | 0 | 打开或关闭侧边导航窗格。 |
URL示例:
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-safe-area-insets-V14
爬取时间: 2025-04-28 00:26:49
来源: Huawei Developer
概述
安全区域定义为页面的显示区域，其默认不与系统设置的非安全区域（如状态栏、导航栏）重叠，以确保开发者设计的界面均布局于安全区域内。然而，当Web组件启用沉浸式模式时，网页元素可能会出现与状态栏或导航栏重叠的问题。具体示例如图1所示，红色虚线框划定的区域即为安全区域，而顶部状态栏、屏幕挖孔区域和底部导航条则被界定为非安全区域，Web组件开启沉浸式效果时，网页内底部元素与导航条发生重叠。
图1Web组件开启沉浸式效果时网页内底部元素与导航条发生重叠
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170402.82344136893610244897702865574763:50001231000000:2800:A6FD8DB7660ADFC6B3E09D56474DD6D48E500DB0782ED002B9DAA0BC2CEFB236.png)
Web组件提供了利用W3C CSS进行安全区域计算并避让适配的能力，用来支持异形屏幕设备在沉浸式效果下页面的正常显示，网页开发者可以使用该能力对重叠元素进行避让。ArkWeb内核将持续监测Web组件及系统安全区域的位置与尺寸，依据两者的重叠部分，计算出当前Web组件的安全区域，以及在各个方向上所需避让的具体距离。
实现场景
开启Web组件沉浸式效果
开发者可以通过expandSafeArea来开启沉浸式效果。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
.width('100%').height('100%')
.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
}
}
}
```
设置网页在可视窗口中的布局方式
viewport-fit用于限制网页在安全区域内的展示形态。默认为auto，与contain表现一致，表示可视窗口完全包含网页内容，即网页全部内容展示于安全区域内。而cover则表示网页内容完全覆盖可视窗口，即网页内容不仅展示于安全区域，还包含非安全区域，即可能与状态栏和导航栏发生重叠，只有这种场景下网页需要进行避让适配，设置方式如下：
对网页元素进行避让
网页元素的避让适配主要依赖于env() CSS函数，该函数用于在CSS中插入由用户代码定义的变量。这使得开发人员能够将内容置于可视窗口（viewport）的安全区域内。在规范中定义的safe-area-inset-*值，确保了即使在非矩形视区中，内容也能得到完全显示。其语法如下：
safe-area-inset-*由四个环境变量组成，分别定义了可视窗口边缘内矩形的top、right、bottom和left，确保内容可以安全地放置，避免被非矩形显示区域切断。在矩形视口（如普通2in1设备的显示器）中，这些值等于零。而对于非矩形显示器（例如圆形表盘、移动设备屏幕等），所有内容都将在用户代理设定的四个值所形成的矩形区域内可见。
不同于其他的CSS属性，用户代理定义的属性名字对大小写敏感。同时，需要注意env()必须配合viewport-fit=cover使用。
对于一些购物网站，首页网页底部为Tab形式的绝对布局元素，在沉浸式状态下这些绝对布局元素就需要进行底部避让，以防止绝对布局元素与系统导航条发生重叠遮挡，避让效果见图2：
同时，上述env()使用还能基于部分数学计算函数calc(),min(),max()组合计算，如：
图2Web组件开启沉浸式效果时网页内底部元素避让导航条区域
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170402.39336780719324194234193839167819:50001231000000:2800:896839560C0E32F95363335D78A5A238E5F597089B915644D10C15FD4BCEB707.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-same-layer-V14
爬取时间: 2025-04-28 00:27:03
来源: Huawei Developer
在系统中，应用可以使用Web组件加载Web网页。在非原生框架的UI组件功能或性能不如原生组件时，可使用同层渲染，使用ArkUI组件渲染这些组件（简称为同层组件）。
使用场景
Web网页
小程序的地图组件，可以使用ArkUI的XComponent组件渲染来提升性能。小程序的输入框组件，可以使用ArkUI的TextInput组件渲染，达到与原生应用一致的输入体验。
-  在网页侧，应用开发者可将<embed>、<object>的网页UI组件（简称为同层标签），按一定规则进行同层渲染，详细规格见同层渲染规格小节。
-  在应用侧，应用开发者可以通过Web组件的同层渲染事件上报接口，感知到H5同层标签的生命周期以及输入事件，进行同层渲染组件的相应业务逻辑处理。
-  在应用侧，应用开发者可以使用ArkUI的NodeContainer等接口，构建H5同层标签对应的同层渲染组件。可支持同层渲染的ArkUI常用组件包括：TextInput,XComponent,Canvas,Video,Web。具体规格可参见同层渲染规格小节。
三方UI框架
Flutter提供了PlatformView与Texture抽象组件，这些组件可使用原生组件渲染，用来支持Flutter组件功能不足的部分。Weex2.0框架的Camera、Video、Canvas组件。
-  在三方框架页面侧，由于Flutter、Weex等三方框架不在操作系统范围，本文不列举可被同层渲染的三方框架UI组件的范围与使用方式。
-  在应用侧，应用开发者可以使用ArkUI的NodeContainer等接口，构建三方框架同层标签对应的同层渲染组件。可支持同层渲染的ArkUI常用组件包括：TextInput,XComponent,Canvas,Video,Web。具体规格可参见同层渲染规格。
整体架构
ArkWeb同层渲染特性主要提供两种能力：同层标签生命周期和事件命中转发处理。
同层标签生命周期主要关联前端标签（<embed>/<object>），同时命中到同层标签的事件会被上报到开发者侧，由开发者分发到对应组件树。整体框架如下图所示：
图1同层渲染整体架构
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170402.94960031639806927520124462879757:50001231000000:2800:C6815BEBAF6980E0FC7CEE8486040A5117E8DD930C2B0F5E19BAE9E08A7615A0.png)
规格约束
可被同层渲染的ArkUI组件
以下规格对Web网页和三方框架场景均生效。
支持的组件范围:
-  基础组件：AlphabetIndexer,Blank,Button,CalendarPicker,Checkbox,CheckboxGroup,ContainerSpan,DataPanel,DatePicker,Divider,Gauge,Hyperlink,Image,ImageAnimator,ImageSpan,LoadingProgress,Marquee,PatternLock,Progress,QRCode,Radio,Rating,Refresh,ScrollBar,Search,Span,Select,Slider,Text,TextArea,TextClock,TextInput,TextPicker,TextTimer,TimePicker,Toggle
-  容器类组件：Badge,Column,ColumnSplit,Counter,Flex,GridCol,GridRow,Grid,GridItem，List,ListItem,ListItemGroup,RelativeContainer,Row,RowSplit,Scroll,Stack,Swiper,Tabs,TabContent,NodeContainer,SideBarContainer,Stepper,StepperItem,WaterFlow,FlowItem
-  自绘制类组件：XComponent,Canvas,Video,Web
-  命令式自定义绘制节点：BuilderNode,ComponentContent,ContentSlot,FrameNode,Graphics,NodeController,RenderNode,XComponentNode,AttributeUpdater，CAPI（支持同层渲染的组件范围同ArkTS）
支持的组件通用属性与事件:
-  不支持的通用属性：分布式迁移标识，特效绘制合并。
-  其他未明确标注不支持的属性与事件及组件能力，均默认支持。
Web网页的同层渲染标签
此规格仅针对Web网页，不适用于三方框架场景。
如果应用需要在Web组件加载的网页中使用同层渲染，需要按照以下规格将网页中的<embed>、<object>标签指定为同层渲染组件。
支持的产品形态：
当前仅支持移动设备和平板形态。
支持的H5标签：
-  支持<embed>标签：在开启同层渲染后，仅支持type类型为native前缀的标签识别为同层组件，不支持自定义属性。
-  支持<object>标签：在开启同层渲染后，支持将非标准MIME type的object标签识别为同层组件，支持通过param/value的自定义属性解析。
-  不支持W3C规范标准标签（如<input>、<video>）定义为同层标签。
-  不支持同时配置<object>标签和<embed>标签作为同层标签。
-  标签类型只支持英文字符，不区分大小写。
同层标签的属性支持范围：
支持满足W3C标准的CSS样式属性。
同层标签的生命周期管理：
当Embed标签生命周期变化时触发onNativeEmbedLifecycleChange()回调。
-  支持创建、销毁、位置宽高变化、不支持可见状态变化。
-  支持同层组件所在Web页面进入前进后退缓存。
同层标签的输入事件分发处理：
-  支持触摸事件TouchEvent的DOWN/UP/MOVE/CANCEL。支持配置触摸事件消费结果，默认为应用侧消费。
-  不支持同层标签所在的应用页面缩放和initialScale、zoom、zoomIn、zoomOut等缩放接口。
-  暂不支持鼠标、键盘、触摸板事件。
约束限制：
-  Web页面内不建议超过5个同层标签。超过5个后，渲染性能将会下降。
-  受GPU限制，同层标签最大高度不超过8000px，最大纹理大小为8000px。
-  开启同层渲染后，Web组件打开的所有Web页面将不支持同步渲染模式RenderMode。
-  Video组件：在非全屏Video变为全屏时，Video组件变为非纹理导出模式，视频播放状态保持延续；恢复为非全屏时，变为纹理导出模式，视频播放状态保持延续。
-  Web组件：仅支持一层同层渲染嵌套，不支持多层同层渲染嵌套。输入事件只支持滑动、点击、缩放、长按 ，不支持拖拽、旋转。
-  涉及界面交互的ArkUI组件（如TextInput等）：建议在页面布局中使用Stack包裹同层组件容器与BuilderNode，并使两者位置一致，NodeContainer要与<embed>/<object>标签对齐，以保障组件正常交互。如两者位置不一致，可能出现的问题有：TextInput/TextArea等附属的文本选择框位置错位（如下图）、LoadingProgress/Marquee等组件的动画启停与组件可见状态不匹配。 图2未使用Stack包裹，TextInput的位置错位 图3使用Stack包裹，TextInput的位置正常
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170402.02182124607041712645777557853815:50001231000000:2800:736BD960FE58F3114CE4EAD8D6ADCAE24A5CAA7222C667BCD75F424AD27C7BCE.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170402.81187720886117816565033460999938:50001231000000:2800:994C1AB20AFDD9A8FC21B4FCBA226DAC46F9B3EE9CC2C9740B01149EFD2D8C50.png)
Web页面中同层渲染输入框
在Web页面中，可以使用ArkUI原生的TextInput组件进行同层渲染。此处利用同层渲染展示三个输入框，渲染效果图如下：
图4同层渲染输入框
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170402.52773136459994236892936492446042:50001231000000:2800:4EC79BC022E80259FCCA185E1EED1BE47E77DCEF7B014ED17F588C47BAFF4308.png)
1.  在Web页面中标记需要同层渲染的HTML标签。 同层渲染支持<embed>/<object>两种标签。type类型可任意指定，两个字符串参数均不区分大小写，ArkWeb内核将会统一转换为小写。其中，tag字符串使用全字符串匹配，type使用字符串前缀匹配。 若开发者不使用该接口或该接口接收的为非法字符串（空字符串）时，ArkWeb内核将使用默认设置，即"embed" + "native/"前缀模式。若指定类型与w3c定义的object或embed标准类型重合，如registerNativeEmbedRule("object", "application/pdf")，ArkWeb将遵循w3c标准行为，不会将其识别为同层标签。 采用<embed>标签。 采用<object>标签。 需要使用registerNativeEmbedRule注册object标签。 与registerNativeEmbedRule相对应的前端页面代码，类型可使用"test"及以"test"为前缀的字串。
2.  采用<embed>标签。
3.  采用<object>标签。 需要使用registerNativeEmbedRule注册object标签。 与registerNativeEmbedRule相对应的前端页面代码，类型可使用"test"及以"test"为前缀的字串。
```typescript
// ...
Web({src: $rawfile("text.html"), controller: this.browserTabController})
// 注册同层标签为"object"，类型为"test"前缀
.registerNativeEmbedRule("object", "test")
// ...
```
4.  在应用侧开启同层渲染功能。 同层渲染功能默认不开启，如果要使用同层渲染的功能，可通过enableNativeEmbedMode来开启。
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
// 配置同层渲染开关开启。
.enableNativeEmbedMode(true)
}
}
}
```
5.  创建自定义组件。 同层渲染功能开启后，展示在对应区域的原生组件。
```typescript
@Component
struct TextInputComponent {
@Prop params: Params
@State bkColor: Color = Color.White
build() {
Column() {
TextInput({text: '', placeholder: 'please input your word...'})
.placeholderColor(Color.Gray)
.id(this.params?.elementId)
.placeholderFont({size: 13, weight: 400})
.caretColor(Color.Gray)
.width(this.params?.width)
.height(this.params?.height)
.fontSize(14)
.fontColor(Color.Black)
}
//自定义组件中的最外层容器组件宽高应该为同层标签的宽高
.width(this.params.width)
.height(this.params.height)
}
}
@Builder
function TextInputBuilder(params:Params) {
TextInputComponent({params: params})
.width(params.width)
.height(params.height)
.backgroundColor(Color.White)
}
```
6.  创建节点控制器。 用于控制和反馈对应NodeContainer上的节点行为。
```typescript
class MyNodeController extends NodeController {
private rootNode: BuilderNode<[Params]> | undefined | null;
private embedId_: string = "";
private surfaceId_: string = "";
private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
private width_: number = 0;
private height_: number = 0;
private type_: string = "";
private isDestroy_: boolean = false;
setRenderOption(params: NodeControllerParams) {
this.surfaceId_ = params.surfaceId;
this.renderType_ = params.renderType;
this.embedId_ = params.embedId;
this.width_ = params.width;
this.height_ = params.height;
this.type_ = params.type;
}
// 必须要重写的方法，用于构建节点数、返回节点数挂载在对应NodeContainer中。
// 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
makeNode(uiContext: UIContext): FrameNode | null {
if (this.isDestroy_) { // rootNode为null
return null;
}
if (!this.rootNode) {// rootNode 为undefined时
this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
if(this.rootNode) {
this.rootNode.build(wrapBuilder(TextInputBuilder), {  textOne: "myTextInput", width: this.width_, height: this.height_  })
return this.rootNode.getFrameNode();
}else{
return null;
}
}
// 返回FrameNode节点。
return this.rootNode.getFrameNode();
}
setBuilderNode(rootNode: BuilderNode<Params[]> | null): void {
this.rootNode = rootNode;
}
getBuilderNode(): BuilderNode<[Params]> | undefined | null {
return this.rootNode;
}
updateNode(arg: Object): void {
this.rootNode?.update(arg);
}
getEmbedId(): string {
return this.embedId_;
}
setDestroy(isDestroy: boolean): void {
this.isDestroy_ = isDestroy;
if (this.isDestroy_) {
this.rootNode = null;
}
}
postEvent(event: TouchEvent | undefined): boolean {
return this.rootNode?.postTouchEvent(event) as boolean
}
}
```
7.  监听同层渲染的生命周期变化。 开启该功能后，每当网页中存在同层渲染支持的标签时，ArkWeb内核会触发由onNativeEmbedLifecycleChange注册的回调函数。 开发者则需要调用onNativeEmbedLifecycleChange来监听同层渲染标签的生命周期变化。
```typescript
build() {
Row() {
Column() {
Stack() {
ForEach(this.componentIdArr, (componentId: string) => {
NodeContainer(this.nodeControllerMap.get(componentId))
.position(this.positionMap.get(componentId))
.width(this.widthMap.get(componentId))
.height(this.heightMap.get(componentId))
}, (embedId: string) => embedId)
// Web组件加载本地text.html页面
Web({src: $rawfile("text.html"), controller: this.browserTabController})
// 配置同层渲染开关开启
.enableNativeEmbedMode(true)
// 注册同层标签为"object"，类型为"test"前缀
.registerNativeEmbedRule("object", "test")
// 获取embed标签的生命周期变化数据
.onNativeEmbedLifecycleChange((embed) => {
console.log("NativeEmbed surfaceId" + embed.surfaceId);
// 如果使用embed.info.id作为映射nodeController的key，请在h5页面显式指定id
const componentId = embed.info?.id?.toString() as string
if (embed.status == NativeEmbedStatus.CREATE) {
console.log("NativeEmbed create" + JSON.stringify(embed.info));
// 创建节点控制器、设置参数并rebuild
let nodeController = new MyNodeController()
// embed.info.width和embed.info.height单位是px格式，需要转换成ets侧的默认单位vp
nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
type : embed.info?.type as string,
renderType : NodeRenderType.RENDER_TYPE_TEXTURE,
embedId : embed.embedId as string,
width : px2vp(embed.info?.width),
height : px2vp(embed.info?.height)})
this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`}
nodeController.setDestroy(false);
//根据web传入的embed的id属性作为key，将nodeController存入Map
this.nodeControllerMap.set(componentId, nodeController);
this.widthMap.set(componentId, px2vp(embed.info?.width));
this.heightMap.set(componentId, px2vp(embed.info?.height));
this.positionMap.set(componentId, this.edges);
// 将web传入的embed的id属性存入@State状态数组变量中，用于动态创建nodeContainer节点容器,需要将push动作放在set之后
this.componentIdArr.push(componentId)
} else if (embed.status == NativeEmbedStatus.UPDATE) {
let nodeController = this.nodeControllerMap.get(componentId);
console.log("NativeEmbed update" + JSON.stringify(embed));
this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`}
this.positionMap.set(componentId, this.edges);
this.widthMap.set(componentId, px2vp(embed.info?.width));
this.heightMap.set(componentId, px2vp(embed.info?.height));
nodeController?.updateNode({textOne: 'update', width: px2vp(embed.info?.width), height: px2vp(embed.info?.height)} as ESObject)
} else if (embed.status == NativeEmbedStatus.DESTROY) {
console.log("NativeEmbed destroy" + JSON.stringify(embed));
let nodeController = this.nodeControllerMap.get(componentId);
nodeController?.setDestroy(true)
this.nodeControllerMap.clear();
this.positionMap.delete(componentId);
this.widthMap.delete(componentId);
this.heightMap.delete(componentId);
this.componentIdArr.filter((value: string) => value != componentId)
} else {
console.log("NativeEmbed status" + embed.status);
}
})
}.height("80%")
}
}
}
```
8.  同层渲染手势事件。 开启该功能后，每当在同层渲染的区域进行触摸操作时，ArkWeb内核会触发onNativeEmbedGestureEvent注册的回调函数。 开发者则需要调用onNativeEmbedGestureEvent来监听同层渲染同层渲染区域的手势事件。
```typescript
build() {
Row() {
Column() {
Stack() {
ForEach(this.componentIdArr, (componentId: string) => {
NodeContainer(this.nodeControllerMap.get(componentId))
.position(this.positionMap.get(componentId))
.width(this.widthMap.get(componentId))
.height(this.heightMap.get(componentId))
}, (embedId: string) => embedId)
// Web组件加载本地text.html页面。
Web({src: $rawfile("text.html"), controller: this.browserTabController})
// 配置同层渲染开关开启。
.enableNativeEmbedMode(true)
// 获取embed标签的生命周期变化数据。
.onNativeEmbedLifecycleChange((embed) => {
// 生命周期变化实现
})
.onNativeEmbedGestureEvent((touch) => {
console.log("NativeEmbed onNativeEmbedGestureEvent" + JSON.stringify(touch.touchEvent));
this.componentIdArr.forEach((componentId: string) => {
let nodeController = this.nodeControllerMap.get(componentId);
// 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上
if(nodeController?.getEmbedId() == touch.embedId) {
let ret = nodeController?.postEvent(touch.touchEvent)
if(ret) {
console.log("onNativeEmbedGestureEvent success " + componentId);
} else {
console.log("onNativeEmbedGestureEvent fail " + componentId);
}
if(touch.result) {
// 通知Web组件手势事件消费结果
touch.result.setGestureEventResult(ret);
}
}
})
})
}
}
}
}
```
-  采用<embed>标签。
-  采用<object>标签。 需要使用registerNativeEmbedRule注册object标签。 与registerNativeEmbedRule相对应的前端页面代码，类型可使用"test"及以"test"为前缀的字串。
```typescript
// ...
Web({src: $rawfile("text.html"), controller: this.browserTabController})
// 注册同层标签为"object"，类型为"test"前缀
.registerNativeEmbedRule("object", "test")
// ...
```
完整示例：
使用前请在module.json5中添加网络权限，添加方法请参考在配置文件中声明权限。
应用侧代码。
```typescript
// 创建NodeController
import webview from '@ohos.web.webview';
import { UIContext } from '@ohos.arkui.UIContext';
import { NodeController, BuilderNode, NodeRenderType, FrameNode } from "@ohos.arkui.node";
@Observed
declare class Params{
elementId: string
textOne: string
textTwo: string
width: number
height: number
}
declare class NodeControllerParams {
surfaceId: string
type: string
renderType: NodeRenderType
embedId: string
width: number
height: number
}
// 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。
class MyNodeController extends NodeController {
private rootNode: BuilderNode<[Params]> | undefined | null;
private embedId_: string = "";
private surfaceId_: string = "";
private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
private width_: number = 0;
private height_: number = 0;
private type_: string = "";
private isDestroy_: boolean = false;
setRenderOption(params: NodeControllerParams) {
this.surfaceId_ = params.surfaceId;
this.renderType_ = params.renderType;
this.embedId_ = params.embedId;
this.width_ = params.width;
this.height_ = params.height;
this.type_ = params.type;
}
// 必须要重写的方法，用于构建节点数、返回节点数挂载在对应NodeContainer中。
// 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
makeNode(uiContext: UIContext): FrameNode | null {
if (this.isDestroy_) { // rootNode为null
return null;
}
if (!this.rootNode) {// rootNode 为undefined时
this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
if(this.rootNode) {
this.rootNode.build(wrapBuilder(TextInputBuilder), {  textOne: "myTextInput", width: this.width_, height: this.height_  })
return this.rootNode.getFrameNode();
}else{
return null;
}
}
// 返回FrameNode节点。
return this.rootNode.getFrameNode();
}
setBuilderNode(rootNode: BuilderNode<Params[]> | null): void {
this.rootNode = rootNode;
}
getBuilderNode(): BuilderNode<[Params]> | undefined | null {
return this.rootNode;
}
updateNode(arg: Object): void {
this.rootNode?.update(arg);
}
getEmbedId(): string {
return this.embedId_;
}
setDestroy(isDestroy: boolean): void {
this.isDestroy_ = isDestroy;
if (this.isDestroy_) {
this.rootNode = null;
}
}
postEvent(event: TouchEvent | undefined): boolean {
return this.rootNode?.postTouchEvent(event) as boolean
}
}
@Component
struct TextInputComponent {
@Prop params: Params
@State bkColor: Color = Color.White
build() {
Column() {
TextInput({text: '', placeholder: 'please input your word...'})
.placeholderColor(Color.Gray)
.id(this.params?.elementId)
.placeholderFont({size: 13, weight: 400})
.caretColor(Color.Gray)
.fontSize(14)
.fontColor(Color.Black)
}
//自定义组件中的最外层容器组件宽高应该为同层标签的宽高
.width(this.params.width)
.height(this.params.height)
}
}
// @Builder中为动态组件的具体组件内容。
@Builder
function TextInputBuilder(params:Params) {
TextInputComponent({params: params})
.width(params.width)
.height(params.height)
.backgroundColor(Color.White)
}
@Entry
@Component
struct Page{
browserTabController: WebviewController = new webview.WebviewController()
private nodeControllerMap: Map<string, MyNodeController> = new Map();
@State componentIdArr: Array<string> = [];
@State posMap: Map<string, Position | undefined> = new Map();
@State widthMap: Map<string, number> = new Map();
@State heightMap: Map<string, number> = new Map();
@State positionMap: Map<string, Edges> = new Map();
@State edges: Edges = {};
build() {
Row() {
Column() {
Stack() {
ForEach(this.componentIdArr, (componentId: string) => {
NodeContainer(this.nodeControllerMap.get(componentId))
.position(this.positionMap.get(componentId))
.width(this.widthMap.get(componentId))
.height(this.heightMap.get(componentId))
}, (embedId: string) => embedId)
// Web组件加载本地text.html页面。
Web({src: $rawfile("text.html"), controller: this.browserTabController})
// 配置同层渲染开关开启。
.enableNativeEmbedMode(true)
// 获取embed标签的生命周期变化数据。
.onNativeEmbedLifecycleChange((embed) => {
console.log("NativeEmbed surfaceId" + embed.surfaceId);
// 如果使用embed.info.id作为映射nodeController的key，请在h5页面显式指定id
const componentId = embed.info?.id?.toString() as string
if (embed.status == NativeEmbedStatus.CREATE) {
console.log("NativeEmbed create" + JSON.stringify(embed.info));
// 创建节点控制器、设置参数并rebuild
let nodeController = new MyNodeController()
// embed.info.width和embed.info.height单位是px格式，需要转换成ets侧的默认单位vp
nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
type : embed.info?.type as string,
renderType : NodeRenderType.RENDER_TYPE_TEXTURE,
embedId : embed.embedId as string,
width : px2vp(embed.info?.width),
height : px2vp(embed.info?.height)})
this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`}
nodeController.setDestroy(false);
//根据web传入的embed的id属性作为key，将nodeController存入Map
this.nodeControllerMap.set(componentId, nodeController);
this.widthMap.set(componentId, px2vp(embed.info?.width));
this.heightMap.set(componentId, px2vp(embed.info?.height));
this.positionMap.set(componentId, this.edges);
// 将web传入的embed的id属性存入@State状态数组变量中，用于动态创建nodeContainer节点容器,需要将push动作放在set之后
this.componentIdArr.push(componentId)
} else if (embed.status == NativeEmbedStatus.UPDATE) {
let nodeController = this.nodeControllerMap.get(componentId);
console.log("NativeEmbed update" + JSON.stringify(embed));
this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`}
this.positionMap.set(componentId, this.edges);
this.widthMap.set(componentId, px2vp(embed.info?.width));
this.heightMap.set(componentId, px2vp(embed.info?.height));
nodeController?.updateNode({textOne: 'update', width: px2vp(embed.info?.width), height: px2vp(embed.info?.height)} as ESObject)
} else if (embed.status == NativeEmbedStatus.DESTROY) {
console.log("NativeEmbed destroy" + JSON.stringify(embed));
let nodeController = this.nodeControllerMap.get(componentId);
nodeController?.setDestroy(true)
this.nodeControllerMap.clear();
this.positionMap.delete(componentId);
this.widthMap.delete(componentId);
this.heightMap.delete(componentId);
this.componentIdArr.filter((value: string) => value != componentId)
} else {
console.log("NativeEmbed status" + embed.status);
}
})// 获取同层渲染组件触摸事件信息。
.onNativeEmbedGestureEvent((touch) => {
console.log("NativeEmbed onNativeEmbedGestureEvent" + JSON.stringify(touch.touchEvent));
this.componentIdArr.forEach((componentId: string) => {
let nodeController = this.nodeControllerMap.get(componentId);
// 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上
if(nodeController?.getEmbedId() == touch.embedId) {
let ret = nodeController?.postEvent(touch.touchEvent)
if(ret) {
console.log("onNativeEmbedGestureEvent success " + componentId);
} else {
console.log("onNativeEmbedGestureEvent fail " + componentId);
}
if(touch.result) {
// 通知Web组件手势事件消费结果
touch.result.setGestureEventResult(ret);
}
}
})
})
}
}
}
}
}
```
绘制XComponent+AVPlayer和Button组件
开发者可通过enableNativeEmbedMode()控制同层渲染开关。Html文件中需要显式使用embed标签，并且embed标签内type必须以“native/”开头。同层标签对应的元素区域的背景为透明。
-  应用侧代码组件使用示例。
```typescript
// HAP's src/main/ets/pages/Index.ets
// 创建NodeController
import { webview } from '@kit.ArkWeb';
import { UIContext, NodeController, BuilderNode, NodeRenderType, FrameNode } from "@kit.ArkUI";
import { AVPlayerDemo } from './PlayerDemo';
@Observed
declare class Params {
textOne : string
textTwo : string
width : number
height : number
}
declare class NodeControllerParams {
surfaceId : string
type : string
renderType : NodeRenderType
embedId : string
width : number
height : number
}
// 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。
class MyNodeController extends NodeController {
private rootNode: BuilderNode<[Params]> | undefined | null;
private embedId_ : string = "";
private surfaceId_ : string = "";
private renderType_ :NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
private width_ : number = 0;
private height_ : number = 0;
private type_ : string = "";
private isDestroy_ : boolean = false;
setRenderOption(params : NodeControllerParams) {
this.surfaceId_ = params.surfaceId;
this.renderType_ = params.renderType;
this.embedId_ = params.embedId;
this.width_ = params.width;
this.height_ = params.height;
this.type_ = params.type;
}
// 必须要重写的方法，用于构建节点数、返回节点数挂载在对应NodeContainer中。
// 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
makeNode(uiContext: UIContext): FrameNode | null{
if (this.isDestroy_) { // rootNode为null
return null;
}
if (!this.rootNode) { // rootNode 为undefined时
this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_});
if (this.type_ === 'native/video') {
this.rootNode.build(wrapBuilder(VideoBuilder), {textOne: "myButton", width : this.width_, height : this.height_});
} else {
// other
}
}
// 返回FrameNode节点。
return this.rootNode.getFrameNode();
}
setBuilderNode(rootNode: BuilderNode<Params[]> | null): void{
this.rootNode = rootNode;
}
getBuilderNode(): BuilderNode<[Params]> | undefined | null{
return this.rootNode;
}
updateNode(arg: Object): void {
this.rootNode?.update(arg);
}
getEmbedId() : string {
return this.embedId_;
}
setDestroy(isDestroy : boolean) : void {
this.isDestroy_ = isDestroy;
if (this.isDestroy_) {
this.rootNode = null;
}
}
postEvent(event: TouchEvent | undefined) : boolean {
return this.rootNode?.postTouchEvent(event) as boolean
}
}
@Component
struct VideoComponent {
@ObjectLink params: Params
@State bkColor: Color = Color.Red
mXComponentController: XComponentController = new XComponentController();
@State player_changed: boolean = false;
player?: AVPlayerDemo;
build() {
Column() {
Button(this.params.textOne)
XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.mXComponentController})
.border({width: 1, color: Color.Red})
.onLoad(() => {
this.player = new AVPlayerDemo();
this.player.setSurfaceID(this.mXComponentController.getXComponentSurfaceId());
this.player_changed = !this.player_changed;
this.player.avPlayerLiveDemo()
})
.width(300)
.height(200)
}
//自定义组件中的最外层容器组件宽高应该为同层标签的宽高
.width(this.params.width)
.height(this.params.height)
}
}
// @Builder中为动态组件的具体组件内容。
@Builder
function VideoBuilder(params: Params) {
VideoComponent({ params: params })
.backgroundColor(Color.Gray)
}
@Entry
@Component
struct WebIndex {
browserTabController: WebviewController = new webview.WebviewController()
private nodeControllerMap: Map<string, MyNodeController> = new Map();
@State componentIdArr: Array<string> = [];
aboutToAppear() {
// 配置web开启调试模式。
webview.WebviewController.setWebDebuggingAccess(true);
}
build(){
Row() {
Column() {
Stack() {
ForEach(this.componentIdArr, (componentId: string) => {
NodeContainer(this.nodeControllerMap.get(componentId))
}, (embedId: string) => embedId)
// Web组件加载本地test.html页面。
Web({ src: $rawfile("test.html"), controller: this.browserTabController })
// 配置同层渲染开关开启。
.enableNativeEmbedMode(true)
// 获取embed标签的生命周期变化数据。
.onNativeEmbedLifecycleChange((embed) => {
console.log("NativeEmbed surfaceId" + embed.surfaceId);
// 1. 如果使用embed.info.id作为映射nodeController的key，请在h5页面显式指定id
const componentId = embed.info?.id?.toString() as string
if (embed.status == NativeEmbedStatus.CREATE) {
console.log("NativeEmbed create" + JSON.stringify(embed.info))
// 创建节点控制器，设置参数并rebuild。
let nodeController = new MyNodeController()
// 1. embed.info.width和embed.info.height单位是px格式，需要转换成ets侧的默认单位vp
nodeController.setRenderOption({surfaceId : embed.surfaceId as string, type : embed.info?.type as string,
renderType : NodeRenderType.RENDER_TYPE_TEXTURE, embedId : embed.embedId as string,
width : px2vp(embed.info?.width), height : px2vp(embed.info?.height)})
nodeController.setDestroy(false);
// 根据web传入的embed的id属性作为key，将nodeController存入map。
this.nodeControllerMap.set(componentId, nodeController)
// 将web传入的embed的id属性存入@State状态数组变量中，用于动态创建nodeContainer节点容器，需要将push动作放在set之后。
this.componentIdArr.push(componentId)
} else if (embed.status == NativeEmbedStatus.UPDATE) {
let nodeController = this.nodeControllerMap.get(componentId)
nodeController?.updateNode({textOne: 'update', width: px2vp(embed.info?.width), height: px2vp(embed.info?.height)} as ESObject)
} else {
let nodeController = this.nodeControllerMap.get(componentId);
nodeController?.setDestroy(true)
this.nodeControllerMap.clear();
this.componentIdArr.length = 0;
}
})// 获取同层渲染组件触摸事件信息。
.onNativeEmbedGestureEvent((touch) => {
console.log("NativeEmbed onNativeEmbedGestureEvent" + JSON.stringify(touch.touchEvent));
this.componentIdArr.forEach((componentId: string) => {
let nodeController = this.nodeControllerMap.get(componentId)
// 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上
if (nodeController?.getEmbedId() === touch.embedId) {
let ret = nodeController?.postEvent(touch.touchEvent)
if (ret) {
console.log("onNativeEmbedGestureEvent success " + componentId)
} else {
console.log("onNativeEmbedGestureEvent fail " + componentId)
}
if (touch.result) {
// 通知Web组件手势事件消费结果
touch.result.setGestureEventResult(ret);
}
}
})
})
}
}
}
}
}
```
-  应用侧代码，视频播放示例，使用时需替换正确的视频链接地址。
```typescript
// HAP's src/main/ets/pages/PlayerDemo.ets
import { media } from '@kit.MediaKit';
import { BusinessError } from '@ohos.base';
export class AVPlayerDemo {
private count: number = 0;
private surfaceID: string = ''; // surfaceID用于播放画面显示，具体的值需要通过Xcomponent接口获取，相关文档链接见上面Xcomponent创建方法。
private isSeek: boolean = true; // 用于区分模式是否支持seek操作。
setSurfaceID(surface_id: string){
console.log('setSurfaceID : ' + surface_id);
this.surfaceID = surface_id;
}
// 注册avplayer回调函数。
setAVPlayerCallback(avPlayer: media.AVPlayer) {
// seek操作结果回调函数。
avPlayer.on('seekDone', (seekDoneTime: number) => {
console.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
})
// error回调监听函数，当avplayer在操作过程中出现错误时，调用reset接口触发重置流程。
avPlayer.on('error', (err: BusinessError) => {
console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
avPlayer.reset();
})
// 状态机变化回调函数。
avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
switch (state) {
case 'idle': // 成功调用reset接口后触发该状态机上报。
console.info('AVPlayer state idle called.');
avPlayer.release(); // 调用release接口销毁实例对象。
break;
case 'initialized': // avplayer 设置播放源后触发该状态上报。
console.info('AVPlayer state initialized called.');
avPlayer.surfaceId = this.surfaceID; // 设置显示画面，当播放的资源为纯音频时无需设置。
avPlayer.prepare();
break;
case 'prepared': // prepared调用成功后上报该状态机。
console.info('AVPlayer state prepared called.');
avPlayer.play(); // 调用播放接口开始播放。
break;
case 'playing': // play成功调用后触发该状态机上报。
console.info('AVPlayer state prepared called.');
if(this.count !== 0) {
if (this.isSeek) {
console.info('AVPlayer start to seek.');
avPlayer.seek(avPlayer.duration); // seek到视频末尾。
} else {
// 当播放模式不支持seek操作时继续播放到结尾。
console.info('AVPlayer wait to play end.');
}
} else {
avPlayer.pause(); // 调用暂停接口暂停播放。
}
this.count++;
break;
case 'paused': // pause成功调用后触发该状态机上报。
console.info('AVPlayer state paused called.');
avPlayer.play(); // 再次播放接口开始播放。
break;
case 'completed': //播放接口后触发该状态机上报。
console.info('AVPlayer state paused called.');
avPlayer.stop(); // 调用播放接口接口。
break;
case 'stopped': // stop接口后触发该状态机上报。
console.info('AVPlayer state stopped called.');
avPlayer.reset(); // 调用reset接口初始化avplayer状态。
break;
case 'released': //播放接口后触发该状态机上报。
console.info('AVPlayer state released called.');
break;
default:
break;
}
})
}
// 通过url设置网络地址来实现播放直播码流。
async avPlayerLiveDemo(){
// 创建avPlayer实例对象
let avPlayer: media.AVPlayer = await media.createAVPlayer();
// 创建状态机变化回调函数。
this.setAVPlayerCallback(avPlayer);
this.isSeek = false; // 不支持seek操作。
// 使用时需要自行替换视频链接
avPlayer.url = 'https://xxx.xxx/demo.mp4';
}
}
```
-  前端页面示例。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170402.14523630139749790713470978170894:50001231000000:2800:AAF9C14B133EF904063210B6BE6D744AB3B829212772807A6805AA9DCC896261.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-offline-mode-V14
爬取时间: 2025-04-28 00:27:16
来源: Huawei Developer
Web组件能够实现在不同窗口的组件树上进行挂载或移除操作，这一能力使得开发者可以预先创建Web组件，从而实现性能优化。例如，当Tab页为Web组件时，页面可以预先渲染，以便于即时显示。
创建离线Web组件，是基于自定义占位组件NodeContainer实现的。其基本原理为：构建支持命令式创建的Web组件，此类组件创建后不会立即挂载到组件树中，因此不会立即对用户呈现（其组件状态为Hidden和InActive）。开发者可以在后续使用中按需动态挂载这些组件，以实现更灵活的使用方式。
使用离线Web组件可以优化预启动渲染进程和预渲染Web页面。
整体架构
如下图所示，在需要离屏创建Web组件时，定义一个自定义组件以封装Web组件，此Web组件在离线状态下被创建，封装于无状态的NodeContainer节点中，并与相应的NodeController组件绑定。Web组件在后台预渲染完毕后，当需要展示时，通过NodeController将其挂载到ViewTree的NodeContainer中，即与对应的NodeContainer组件绑定，即可挂载上树并显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170402.82687722071913120617181319459379:50001231000000:2800:DDCDA32ED06DE21FCD5993FAA9A63A20A675FF7D6FDF919B16DADBF75A4EDB78.png)
创建离线Web组件
本示例展示了如何预先创建离线Web组件，并在需要的时候进行挂载和显示。在后续内容中，预启动渲染进程和预渲染Web页面作为性能优化措施，均是利用离线Web组件实现的。
创建Web组件将占用内存（每个Web组件大约200MB）和计算资源，建议避免一次性创建过多的离线Web组件，以减少资源消耗。
```typescript
// 载体Ability
// EntryAbility.ets
import { createNWeb } from "../pages/common"
onWindowStageCreate(windowStage: window.WindowStage): void {
windowStage.loadContent('pages/Index', (err, data) => {
// 创建Web动态组件（需传入UIContext），loadContent之后的任意时机均可创建
createNWeb("https://www.example.com", windowStage.getMainWindowSync().getUIContext());
if (err.code) {
return;
}
});
}
```
```typescript
// 创建NodeController
// common.ets
import { UIContext, NodeController, BuilderNode, Size, FrameNode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
// @Builder中为动态组件的具体组件内容
// Data为入参封装类
class Data{
url: ResourceStr = "https://www.example.com";
controller: WebviewController = new webview.WebviewController();
}
@Builder
function WebBuilder(data:Data) {
Column() {
Web({ src: data.url, controller: data.controller })
.width("100%")
.height("100%")
}
}
let wrap = wrapBuilder<Data[]>(WebBuilder);
// 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用
export class myNodeController extends NodeController {
private rootnode: BuilderNode<Data[]> | null = null;
// 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContainer中
// 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新
makeNode(uiContext: UIContext): FrameNode | null {
console.log(" uicontext is undefined : "+ (uiContext === undefined));
if (this.rootnode != null) {
// 返回FrameNode节点
return this.rootnode.getFrameNode();
}
// 返回null控制动态组件脱离绑定节点
return null;
}
// 当布局大小发生变化时进行回调
aboutToResize(size: Size) {
console.log("aboutToResize width : " + size.width  +  " height : " + size.height );
}
// 当controller对应的NodeContainer在Appear的时候进行回调
aboutToAppear() {
console.log("aboutToAppear");
}
// 当controller对应的NodeContainer在Disappear的时候进行回调
aboutToDisappear() {
console.log("aboutToDisappear");
}
// 此函数为自定义函数，可作为初始化函数使用
// 通过UIContext初始化BuilderNode，再通过BuilderNode中的build接口初始化@Builder中的内容
initWeb(url:ResourceStr, uiContext:UIContext, control:WebviewController) {
if(this.rootnode != null)
{
return;
}
// 创建节点，需要uiContext
this.rootnode = new BuilderNode(uiContext);
// 创建动态Web组件
this.rootnode.build(wrap, { url:url, controller:control });
}
}
// 创建Map保存所需要的NodeController
let NodeMap:Map<ResourceStr, myNodeController | undefined> = new Map();
// 创建Map保存所需要的WebViewController
let controllerMap:Map<ResourceStr, WebviewController | undefined> = new Map();
// 初始化需要UIContext，需在Ability获取
export const createNWeb = (url: ResourceStr, uiContext: UIContext) => {
// 创建NodeController
let baseNode = new myNodeController();
let controller = new webview.WebviewController() ;
// 初始化自定义Web组件
baseNode.initWeb(url, uiContext, controller);
controllerMap.set(url, controller)
NodeMap.set(url, baseNode);
}
// 自定义获取NodeController接口
export const getNWeb = (url: ResourceStr) : myNodeController | undefined => {
return NodeMap.get(url);
}
```
```typescript
// 使用NodeController的Page页
// Index.ets
import { getNWeb } from "./common"
@Entry
@Component
struct Index {
build() {
Row() {
Column() {
// NodeContainer用于与NodeController节点绑定，rebuild会触发makeNode
// Page页通过NodeContainer接口绑定NodeController，实现动态组件页面显示
NodeContainer(getNWeb("https://www.example.com"))
.height("90%")
.width("100%")
}
.width('100%')
}
.height('100%')
}
}
```
预启动渲染进程
在后台预先创建一个Web组件，以启动用于渲染的Web渲染进程，这样可以节省后续Web组件加载时启动Web渲染进程所需的时间。
仅在采用单渲染进程模式的应用中，即全局共享一个Web渲染进程时，优化效果显著。Web渲染进程仅在所有Web组件均被销毁后才会终止，因此建议应用至少保持一个Web组件处于活动状态。
该示例在onWindowStageCreate时期预创建了一个Web组件加载blank页面，从而提前启动了Render进程，从index跳转到index2时，优化了Web的Render进程启动和初始化的耗时。
由于创建额外的Web组件会产生内存开销，建议在此方案的基础上复用该Web组件。
```typescript
// 载体Ability
// EntryAbility.ets
import { createNWeb } from "../pages/common"
onWindowStageCreate(windowStage: window.WindowStage): void {
windowStage.loadContent('pages/Index', (err, data) => {
// 创建空的Web动态组件（需传入UIContext），loadContent之后的任意时机均可创建
createNWeb("about：blank", windowStage.getMainWindowSync().getUIContext());
if (err.code) {
return;
}
});
}
```
```typescript
// 创建NodeController
// common.ets
import { UIContext, NodeController, BuilderNode, Size, FrameNode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
// @Builder中为动态组件的具体组件内容
// Data为入参封装类
class Data{
url: ResourceStr = "https://www.example.com";
controller: WebviewController = new webview.WebviewController();
}
@Builder
function WebBuilder(data:Data) {
Column() {
Web({ src: data.url, controller: data.controller })
.width("100%")
.height("100%")
}
}
let wrap = wrapBuilder<Data[]>(WebBuilder);
// 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用
export class myNodeController extends NodeController {
private rootnode: BuilderNode<Data[]> | null = null;
// 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContainer中
// 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新
makeNode(uiContext: UIContext): FrameNode | null {
console.log(" uicontext is undefined : "+ (uiContext === undefined));
if (this.rootnode != null) {
// 返回FrameNode节点
return this.rootnode.getFrameNode();
}
// 返回null控制动态组件脱离绑定节点
return null;
}
// 当布局大小发生变化时进行回调
aboutToResize(size: Size) {
console.log("aboutToResize width : " + size.width  +  " height : " + size.height );
}
// 当controller对应的NodeContainer在Appear的时候进行回调
aboutToAppear() {
console.log("aboutToAppear");
}
// 当controller对应的NodeContainer在Disappear的时候进行回调
aboutToDisappear() {
console.log("aboutToDisappear");
}
// 此函数为自定义函数，可作为初始化函数使用
// 通过UIContext初始化BuilderNode，再通过BuilderNode中的build接口初始化@Builder中的内容
initWeb(url:ResourceStr, uiContext:UIContext, control:WebviewController) {
if(this.rootnode != null)
{
return;
}
// 创建节点，需要uiContext
this.rootnode = new BuilderNode(uiContext);
// 创建动态Web组件
this.rootnode.build(wrap, { url:url, controller:control });
}
}
// 创建Map保存所需要的NodeController
let NodeMap:Map<ResourceStr, myNodeController | undefined> = new Map();
// 创建Map保存所需要的WebViewController
let controllerMap:Map<ResourceStr, WebviewController | undefined> = new Map();
// 初始化需要UIContext 需在Ability获取
export const createNWeb = (url: ResourceStr, uiContext: UIContext) => {
// 创建NodeController
let baseNode = new myNodeController();
let controller = new webview.WebviewController() ;
// 初始化自定义Web组件
baseNode.initWeb(url, uiContext, controller);
controllerMap.set(url, controller)
NodeMap.set(url, baseNode);
}
// 自定义获取NodeController接口
export const getNWeb = (url: ResourceStr) : myNodeController | undefined => {
return NodeMap.get(url);
}
```
```typescript
import router from '@ohos.router'
@Entry
@Component
struct Index1 {
WebviewController: webview.WebviewController = new webview.WebviewController();
build() {
Column() {
//已经预启动Render进程
Button("跳转到Web页面").onClick(()=>{
router.pushUrl({url: "pages/index2"})
})
.width('100%')
.height('100%')
}
}
}
```
```typescript
import web_webview from '@ohos.web.webview'
@Entry
@Component
struct index2 {
WebviewController: webview.WebviewController = new webview.WebviewController();
build() {
Row() {
Column() {
Web({src: 'https://www.example.com', controller: this.webviewController})
.width('100%')
.height('100%')
}
.width('100%')
}
.height('100%')
}
}
```
预渲染Web页面
预渲染Web页面优化方案适用于Web页面启动和跳转场景，例如，进入首页后，跳转到其他子页。建议在高命中率的页面使用该方案。
预渲染Web页面的实现方案是提前创建离线Web组件，并设置Web为Active状态来开启渲染引擎，进行后台渲染。
```typescript
// 载体Ability
// EntryAbility.ets
import {createNWeb} from "../pages/common";
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage): void {
windowStage.loadContent('pages/Index', (err, data) => {
// 创建ArkWeb动态组件（需传入UIContext），loadContent之后的任意时机均可创建
createNWeb("https://www.example.com", windowStage.getMainWindowSync().getUIContext());
if (err.code) {
return;
}
});
}
}
```
```typescript
// 创建NodeController
// common.ets
import { UIContext } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, Size, FrameNode }  from '@kit.ArkUI';
// @Builder中为动态组件的具体组件内容
// Data为入参封装类
class Data{
url: string = 'https://www.example.com';
controller: WebviewController = new webview.WebviewController();
}
// 通过布尔变量shouldInactive控制网页在后台完成预渲染后停止渲染
let shouldInactive: boolean = true;
@Builder
function WebBuilder(data:Data) {
Column() {
Web({ src: data.url, controller: data.controller })
.onPageBegin(() => {
// 调用onActive，开启渲染
data.controller.onActive();
})
.onFirstMeaningfulPaint(() =>{
if (!shouldInactive) {
return;
}
// 在预渲染完成时触发，停止渲染
data.controller.onInactive();
shouldInactive = false;
})
.width("100%")
.height("100%")
}
}
let wrap = wrapBuilder<Data[]>(WebBuilder);
// 用于控制和反馈对应的NodeContianer上的节点的行为，需要与NodeContainer一起使用
export class myNodeController extends NodeController {
private rootnode: BuilderNode<Data[]> | null = null;
// 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContianer中
// 在对应NodeContianer创建的时候调用、或者通过rebuild方法调用刷新
makeNode(uiContext: UIContext): FrameNode | null {
console.info(" uicontext is undifined : "+ (uiContext === undefined));
if (this.rootnode != null) {
// 返回FrameNode节点
return this.rootnode.getFrameNode();
}
// 返回null控制动态组件脱离绑定节点
return null;
}
// 当布局大小发生变化时进行回调
aboutToResize(size: Size) {
console.info("aboutToResize width : " + size.width  +  " height : " + size.height )
}
// 当controller对应的NodeContainer在Appear的时候进行回调
aboutToAppear() {
console.info("aboutToAppear")
// 切换到前台后，不需要停止渲染
shouldInactive = false;
}
// 当controller对应的NodeContainer在Disappear的时候进行回调
aboutToDisappear() {
console.info("aboutToDisappear")
}
// 此函数为自定义函数，可作为初始化函数使用
// 通过UIContext初始化BuilderNode，再通过BuilderNode中的build接口初始化@Builder中的内容
initWeb(url:string, uiContext:UIContext, control:WebviewController) {
if(this.rootnode != null)
{
return;
}
// 创建节点，需要uiContext
this.rootnode = new BuilderNode(uiContext)
// 创建动态Web组件
this.rootnode.build(wrap, { url:url, controller:control })
}
}
// 创建Map保存所需要的NodeController
let NodeMap:Map<string, myNodeController | undefined> = new Map();
// 创建Map保存所需要的WebViewController
let controllerMap:Map<string, WebviewController | undefined> = new Map();
// 初始化需要UIContext 需在Ability获取
export const createNWeb = (url: string, uiContext: UIContext) => {
// 创建NodeController
let baseNode = new myNodeController();
let controller = new webview.WebviewController() ;
// 初始化自定义Web组件
baseNode.initWeb(url, uiContext, controller);
controllerMap.set(url, controller)
NodeMap.set(url, baseNode);
}
// 自定义获取NodeController接口
export const getNWeb = (url : string) : myNodeController | undefined => {
return NodeMap.get(url);
}
```
```typescript
// 使用NodeController的Page页
// Index.ets
import {createNWeb, getNWeb} from "./common"
@Entry
@Component
struct Index {
build() {
Row() {
Column() {
// NodeContainer用于与NodeController节点绑定，rebuild会触发makeNode
// Page页通过NodeContainer接口绑定NodeController，实现动态组件页面显示
NodeContainer(getNWeb("https://www.example.com"))
.height("90%")
.width("100%")
}
.width('100%')
}
.height('100%')
}
}
```
常见白屏问题排查
1.排查应用上网权限配置。
检查是否已在module.json5中添加网络权限，添加方法请参考在配置文件中声明权限。
```typescript
"requestPermissions":[
{
"name" : "ohos.permission.INTERNET"
}
]
```
2.排查NodeContainer与节点绑定的逻辑。
检查节点是否已上组件树，建议在已有的Web组件上方加上Text（请参考以下例子），如果白屏的时候没有出现Text，建议检查NodeContainer与节点绑定的情况。
```typescript
@Builder
function WebBuilder(data:Data) {
Column() {
Text('test')
Web({ src: data.url, controller: data.controller })
.width("100%")
.height("100%")
}
}
```
3.排查Web可见性状态。
如果整个节点已上树，可通过日志WebPattern::OnVisibleAreaChange查看Web组件可见性状态是否正确，不可见的Web组件可能会造成白屏。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-debugging-V14
爬取时间: 2025-04-28 00:27:29
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-debugging-with-devtools-V14
爬取时间: 2025-04-28 00:27:43
来源: Huawei Developer
Web组件支持使用DevTools工具调试前端页面。DevTools是一个 Web前端开发调试工具，提供了电脑上调试移动设备前端页面的能力。开发者通过setWebDebuggingAccess()接口开启Web组件前端页面调试能力，利用DevTools工具可以在电脑上调试移动设备上的前端网页，设备需为4.1.0及以上版本。
调试步骤
应用代码开启Web调试开关
调试网页前，需要应用侧代码调用setWebDebuggingAccess()接口开启Web调试开关。
如果没有开启Web调试开关，则DevTools无法发现被调试的网页。
1.  在应用代码中开启Web调试开关，具体如下：
```typescript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
aboutToAppear() {
// 配置Web开启调试模式
webview.WebviewController.setWebDebuggingAccess(true);
}
build() {
Column() {
Web({ src: 'www.example.com', controller: this.controller })
}
}
}
```
2.  开启调试功能需要在DevEco Studio应用工程hap模块的module.json5文件中增加如下权限，添加方法请参考在配置文件中声明权限。
将设备连接至电脑
请将设备连接至电脑，随后开启开发者模式，为后续的端口转发操作做好准备。
1.  请开启设备上的开发者模式，并启用USB调试功能。 (1) 终端系统查看“设置 > 系统”中是否有“开发者选项”，如果不存在，可在“设置 > 关于本机”连续七次单击“版本号”，直到提示“开启开发者模式”，点击“确认开启”后输入PIN码（如果已设置），设备将自动重启。 (2) USB数据线连接终端和电脑，在“设置 > 系统 > 开发者选项”中，打开“USB调试”开关，弹出的“允许USB调试”的弹框，点击“允许”。
2.  使用hdc命令连接上设备。 打开命令行执行如下命令，查看hdc能否发现设备。 如果命令有返回设备的ID，则说明hdc已连接上设备。 如果命令返回 [Empty]，则说明hdc还没有发现设备。
```shell
hdc list targets
```
3.  如果命令有返回设备的ID，则说明hdc已连接上设备。
4.  如果命令返回 [Empty]，则说明hdc还没有发现设备。
5.  进入hdc shell。 当hdc命令连接上设备后，执行如下命令，进入hdc shell。
```shell
hdc shell
```
-  如果命令有返回设备的ID，则说明hdc已连接上设备。
-  如果命令返回 [Empty]，则说明hdc还没有发现设备。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.29620402517136674329626900362453:50001231000000:2800:1D20650188A979B0A534A2C4B40ECDE699730C6B89A94D815ABB11AB7BD43A64.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.55823482612385644992817484770257:50001231000000:2800:5A28BD1651018731B7DD9B23C62109793FA68DB747EC93301CD9499F053FB744.jpg)
端口转发
当应用代码调用setWebDebuggingAccess接口开启Web调试开关后，ArkWeb内核将启动一个domain socket的监听，以此实现DevTools对网页的调试功能。
但是Chrome浏览器无法直接访问到设备上的domain socket， 所以需要将设备上的domain socket转发到电脑上。
1.  先在hdc shell里执行如下命令，查询ArkWeb在设备里创建的domain socket。 如果前几步操作无误，该命令的执行结果将显示用于查询的domain socket端口。 如果没有查询到结果， 请再次确认。 (1) 应用开启了Web调试开关。 (2) 应用使用Web组件加载了网页。
```shell
cat /proc/net/unix | grep devtools
```
2.  如果前几步操作无误，该命令的执行结果将显示用于查询的domain socket端口。
3.  如果没有查询到结果， 请再次确认。 (1) 应用开启了Web调试开关。 (2) 应用使用Web组件加载了网页。
4.  将查询到的domain socket转发至电脑的TCP 9222端口。 执行exit退出hdc shell。 在命令行里执行如下命令转发端口。 "webview_devtools_remote_" 后面的数字，代表ArkWeb所在应用的进程号， 该数字不是固定的。请将数字改为自己查询到的值。 如果应用的进程号发生变化（例如，应用重新启动），则需要重新进行端口转发。 命令执行成功示意图：
```shell
exit
```
5.  在命令行里执行如下命令，检查端口是否转发成功。 如果有返回端口转发的任务，则说明端口转发成功。 如果返回 [Empty]， 则说明端口转发失败。
```shell
hdc fport ls
```
6.  如果有返回端口转发的任务，则说明端口转发成功。
7.  如果返回 [Empty]， 则说明端口转发失败。
-  如果前几步操作无误，该命令的执行结果将显示用于查询的domain socket端口。
-  如果没有查询到结果， 请再次确认。 (1) 应用开启了Web调试开关。 (2) 应用使用Web组件加载了网页。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.20179836099766589994033684065594:50001231000000:2800:1E55BC4ED48BD44B6B2A89BAA191BDD32D9E8A5DEF36630B6577E2322D3BCA7C.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.11808975923170530246620539310416:50001231000000:2800:99D4C66EEF124502534C45C75F793FA05B0C0A686E56DCBA2491D507CA3550A9.jpg)
-  如果有返回端口转发的任务，则说明端口转发成功。
-  如果返回 [Empty]， 则说明端口转发失败。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.15022120114646776694863218764097:50001231000000:2800:529EB3285399EB743FB5AECBF82DF59BCF7EDCF2A58D010245AC2EF6DB37ACDE.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.44693344391326849042602382584535:50001231000000:2800:CC5972CB8E41E78A36C8BFC8AFC9822E2EF01C61740C5060EA28B97D4970C2C2.jpg)
在Chrome浏览器上打开调试工具页面
1.  在电脑端Chrome浏览器地址栏中输入调试工具地址 chrome://inspect/#devices 并打开该页面。
2.  修改Chrome调试工具的配置。 需要从本地的TCP 9222端口发现被调试网页，所以请确保已勾选 "Discover network targets"。然后再进行网络配置。 (1) 点击 "Configure" 按钮。 (2) 在 "Target discovery settings" 中添加要监听的本地端口localhost:9222。
3.  为了同时调试多个应用，请在Chrome浏览器的调试工具网页内，于“Devices”选项中的“configure”部分添加多个端口号。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.11131760691637327910268485994717:50001231000000:2800:DCD53073D62869E1E1255427B90E15B865EEB694C7968EA15C53D34DDAC067DE.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.23846013290242239464823515824723:50001231000000:2800:563FF9BC5758A58C087E7D5A94E70B1731518BD654500F45BF462D92C0470165.png)
等待发现被调试页面
如果前面的步骤执行成功，稍后，Chrome的调试页面将显示待调试的网页。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.23689599413374029461397586972378:50001231000000:2800:D77200D0E276411555341F0809912C2D42DB72C014BBC8D1F51E6A2BC284E919.jpg)
开始网页调试
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.91084529778210180498026535824050:50001231000000:2800:9BB38567393BD7BB798112A1764F69D1A6423C3F0B72AE09A12DFF5B910D557A.png)
便捷脚本
Windows平台
请复制以下信息建立bat文件，开启调试应用后执行。
Linux或Mac平台
请复制以下信息建立sh文件，注意chmod以及格式转换，开启调试应用后执行。
本脚本会先删除所有的端口转发，如果有其他的工具(如：DevEco Studio)也在使用端口转发功能，会受到影响。
常见问题与解决方法
hdc无法发现设备
问题现象
在命令行里执行如下命令后，没有列出设备ID。
```shell
hdc list targets
```
解决方法
hdc的命令显示设备"未授权"或"unauthorized"
问题现象
执行hdc命令时，提示设备"未授权"或"unauthorized"。
问题原因
设备没有授权该台电脑进行调试。
解决方法
开启USB调试开关的设备连接没有授权的电脑后，会弹框提示"是否允许USB调试？"，请选择允许。
找不到DevTools的domain socket
问题现象
在hdc shell里执行如下命令后，没有结果。
```shell
cat /proc/net/unix | grep devtools
```
解决方法
端口转发不成功
问题现象
在命令行里执行如下命令后，没有列出之前设置过转发任务。
```shell
hdc fport ls
```
解决方法
-  请确保电脑端的tcp:9222没有被占用。 如果tcp:9222被占用，可以将domain socket转发到其他未被占用的TCP端口， 比如9223等。 如果转发到了新的TCP端口， 需要同步修改电脑端Chrome浏览器"Target discovery settings"中的端口号。
端口转发成功后，电脑端Chrome无法发现被调试网页
问题现象
电脑端Chrome浏览器无法发现被调试网页。
问题原因
端口转发失效可能是以下原因：
解决方法
-  请确保电脑端的本地tcp:9222（其他TCP端口同理）没有被占用。
-  请确保设备端的domain socket还存在。
-  请确保domain socket名称里的进程号与被调试的应用的进程号相同。
-  请删除hdc里其他不必要的转发任务。
-  转发成功后，请用电脑端的Chrome浏览器打开网址http://localhost:9222/json，URL里的9222需要改为自己实际配置的TCP端口。 如果网页有内容， 说明端口转发成功，请在Chrome的调试页面等待被调试页面的出现。 如果展示的是错误网页， 说明端口转发失败， 解决方法见上面的端口转发不成功。
-  如果网页有内容， 说明端口转发成功，请在Chrome的调试页面等待被调试页面的出现。
-  如果展示的是错误网页， 说明端口转发失败， 解决方法见上面的端口转发不成功。
-  电脑端Chrome浏览器打开http://localhost:9222/json页面有内容，但是Chrome的调试工具界面还是无法发现调试目标。 在本文档中，默认使用的TCP端口号为9222。 如果开发者使用了其他的TCP端口号(比如9223)，请同时修改端口转发中的TCP端口号和Chrome调试工具界面"Configure"配置中的端口号。
-  在本文档中，默认使用的TCP端口号为9222。 如果开发者使用了其他的TCP端口号(比如9223)，请同时修改端口转发中的TCP端口号和Chrome调试工具界面"Configure"配置中的端口号。
-  如果网页有内容， 说明端口转发成功，请在Chrome的调试页面等待被调试页面的出现。
-  如果展示的是错误网页， 说明端口转发失败， 解决方法见上面的端口转发不成功。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170403.42981230005850025465231898412604:50001231000000:2800:D93C01BA28ADDF33F776AA51F4F41A194DFB7BDB6675B85875A5CED1FF56B270.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170404.64013180535959034679641697573917:50001231000000:2800:9FCFDAD7F9F84CAE8869A835EB90F3607DC3919D11490AB41BEBC04B5AE799A1.jpg)
-  在本文档中，默认使用的TCP端口号为9222。 如果开发者使用了其他的TCP端口号(比如9223)，请同时修改端口转发中的TCP端口号和Chrome调试工具界面"Configure"配置中的端口号。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/web-crashpad-V14
爬取时间: 2025-04-28 00:27:56
来源: Huawei Developer
Web组件支持使用crashpad记录进程崩溃信息。crashpad是chromium内核提供的进程崩溃信息处理工具，在应用使用Web组件导致的进程崩溃出现后（包括应用主进程与Web渲染进程），crashpad会在应用主进程沙箱目录写入minidump文件。该文件为二进制格式，后缀为dmp，其记录了进程崩溃的原因、线程信息、寄存器信息等，应用可以使用该文件分析Web组件相关进程崩溃问题。
使用步骤如下：
1.  在应用使用Web组件导致的进程崩溃出现后，会在应用主进程沙箱目录下产生对应的dmp文件，对应的沙箱路径如下：
2.  应用可以访问该路径拿到目录下的dmp文件，然后进行解析，具体步骤如下： 通过minidump_stackwalk工具解析dmp文件，可以得到上述dmp文件对应的进程崩溃信息（崩溃的原因、线程信息、寄存器信息等），示例如下（Linux环境）： minidump_stackwalk由breakpad项目源码编译得到，编译方法见项目仓库：breakpad仓库地址。 查看解析后的文件，以下示例列出部分内容： 使用llvm工具链解析crash源码位置，示例如下（Linux环境）： llvm-addr2line工具链位于sdk中。
3.  通过minidump_stackwalk工具解析dmp文件，可以得到上述dmp文件对应的进程崩溃信息（崩溃的原因、线程信息、寄存器信息等），示例如下（Linux环境）： minidump_stackwalk由breakpad项目源码编译得到，编译方法见项目仓库：breakpad仓库地址。
4.  查看解析后的文件，以下示例列出部分内容：
5.  使用llvm工具链解析crash源码位置，示例如下（Linux环境）： llvm-addr2line工具链位于sdk中。
-  通过minidump_stackwalk工具解析dmp文件，可以得到上述dmp文件对应的进程崩溃信息（崩溃的原因、线程信息、寄存器信息等），示例如下（Linux环境）： minidump_stackwalk由breakpad项目源码编译得到，编译方法见项目仓库：breakpad仓库地址。
-  查看解析后的文件，以下示例列出部分内容：
-  使用llvm工具链解析crash源码位置，示例如下（Linux环境）： llvm-addr2line工具链位于sdk中。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/background-task-kit-V14
爬取时间: 2025-04-28 00:28:09
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/background-task-overview-V14
爬取时间: 2025-04-28 00:28:22
来源: Huawei Developer
功能介绍
设备返回主界面、锁屏、应用切换等操作会使应用退至后台。应用退至后台后，如果继续活动，可能会造成设备耗电快、用户界面卡顿等现象。为了降低设备耗电速度、保障用户使用流畅度，系统会对退至后台的应用进行管控，包括进程挂起和进程终止。
挂起后，应用进程无法使用软件资源（如公共事件、定时器等）和硬件资源（CPU、网络、GPS、蓝牙等）。如何合理使用请参考合理使用后台硬件资源。
-  应用退至后台一小段时间（由系统定义），应用进程会被挂起。
-  应用退至后台，在后台被访问一小段时间（由系统定义）后，应用进程会被挂起。
-  资源不足时，系统会终止部分应用进程（即回收该进程的所有资源）。
同时，为了保障后台音乐播放、日历提醒等功能的正常使用，系统提供了规范内受约束的后台任务，扩展应用在后台运行时间。
资源使用约束
对于运行的进程，系统会给予一定的资源配额约束，包括进程在连续一段时间内内存的使用、CPU使用占比，以及24小时磁盘写的IO量，均有对应的配额上限。超过配额上限时，如果进程处于前台，系统会有对应的warning日志，如果进程处于后台，系统会终止该进程。
后台任务类型
标准系统支持规范内受约束的后台任务，包括短时任务、长时任务、延迟任务、代理提醒和能效资源。
开发者可以根据如下的功能介绍，选择合适的后台任务，以满足应用退至后台后继续运行的需求。
-  短时任务：适用于实时性要求高、耗时不长的任务，例如状态保存。
-  长时任务：适用于长时间运行在后台、用户可感知的任务，例如后台播放音乐、导航、设备连接等，使用长时任务避免应用进程被挂起。
-  延迟任务：对于实时性要求不高、可延迟执行的任务，系统提供了延迟任务，即满足条件的应用退至后台后被放入执行队列，系统会根据内存、功耗等统一调度。
-  代理提醒：代理提醒是指应用退后台或进程终止后，系统会代理应用做相应的提醒。适用于定时提醒类业务，当前支持的提醒类型包括倒计时、日历和闹钟三类。 图1后台任务类型选择
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170404.39863241290731841194496604184720:50001231000000:2800:80CB6C1F5CEBE6367FAA769882E5B697501FB9F70873F70735B240CCEB10B442.png)
1.  系统仅支持规范内受约束的后台任务。应用退至后台后，若未使用规范内的后台任务或选择的后台任务类型不正确，对应的应用进程会被挂起或终止。
2.  应用申请了规范内的后台任务，仅会提升应用进程被回收的优先级。当系统资源严重不足时，即使应用进程申请了规范内的后台任务，系统仍会终止部分进程，用以保障系统稳定性。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/transient-task-V14
爬取时间: 2025-04-28 00:28:36
来源: Huawei Developer
概述
应用退至后台一小段时间后，应用进程会被挂起，无法执行对应的任务。如果应用在后台仍需要执行耗时不长的任务，如状态保存等，可以通过本文申请短时任务，扩展应用在后台的运行时间。
约束与限制
-  申请时机：应用需要在前台或onBackground回调内，申请短时任务，否则会申请失败。
-  数量限制：一个应用同一时刻最多申请3个短时任务。以图1为例，在①②③时间段内的任意时刻，应用申请了2个短时任务；在④时间段内的任意时刻，应用申请了1个短时任务。
-  配额机制：一个应用会有一定的短时任务配额（根据系统状态和用户习惯调整），单日（24小时内）配额默认为10分钟，单次配额最大为3分钟，低电量时单次配额默认为1分钟，配额消耗完后不允许再申请短时任务。同时，系统提供获取对应短时任务剩余时间的查询接口，用以查询本次短时任务剩余时间，以确认是否继续运行其他业务。
-  配额计算：仅当应用在后台时，对应用下的短时任务计时；同一个应用下的同一个时间段的短时任务，不重复计时。以下图为例：应用有两个短时任务A和B，在前台时申请短时任务A，应用退至后台后开始计时为①，应用进入前台②后不计时，再次进入后台③后开始计时，短时任务A结束后，由于阶段④仍然有短时任务B，所以该阶段继续计时。因此，在这个过程中，该应用短时任务总耗时为①+③+④。 图1短时任务配额计算原理图 任务完成后，应用需主动取消短时任务，否则会影响应用当日短时任务的剩余配额。
-  超时：短时任务即将超时时，系统会回调应用，应用需要取消短时任务。如果超时不取消，系统会终止对应的应用进程。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170404.23403794530544841504475105791227:50001231000000:2800:7D75DE51E0DD7DA24CE09FB4E3C78042EA4CB0ABEA6312D2C2797BD24EC8C04A.png)
接口说明
表1主要接口
以下是短时任务开发使用的主要接口，更多接口及使用方式请见后台任务管理。
| 接口名 | 描述 |
| --- | --- |
| requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo | 申请短时任务。 |
| getRemainingDelayTime(requestId: number): Promise<number> | 获取对应短时任务的剩余时间。 |
| cancelSuspendDelay(requestId: number): void | 取消短时任务。 |
开发步骤
1.  导入模块。
```typescript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.  申请短时任务并实现回调。此处回调在短时任务即将结束时触发，与应用的业务功能不耦合，短时任务申请成功后，正常执行应用本身的任务。
```typescript
let id: number;         // 申请短时任务ID
let delayTime: number;  // 本次申请短时任务的剩余时间
// 申请短时任务
function requestSuspendDelay() {
let myReason = 'test requestSuspendDelay';   // 申请原因
let delayInfo = backgroundTaskManager.requestSuspendDelay(myReason, () => {
// 回调函数。应用申请的短时任务即将超时，通过此函数回调应用，执行一些清理和标注工作，并取消短时任务
console.info('suspend delay task will timeout');
backgroundTaskManager.cancelSuspendDelay(id);
})
id = delayInfo.requestId;
delayTime = delayInfo.actualDelayTime;
}
// 执行应用本身业务
```
3.  获取短时任务剩余时间。查询本次短时任务的剩余时间，用以判断是否继续运行其他业务，例如应用有两个小任务，在执行完第一个小任务后，可以判断本次短时任务是否还有剩余时间来决定是否执行第二个小任务。
```typescript
let id: number; // 申请短时任务ID
async function getRemainingDelayTime() {
backgroundTaskManager.getRemainingDelayTime(id).then((res: number) => {
console.info('Succeeded in getting remaining delay time.');
}).catch((err: BusinessError) => {
console.error(`Failed to get remaining delay time. Code: ${err.code}, message: ${err.message}`);
})
}
```
4.  取消短时任务。
```typescript
let id: number; // 申请短时任务ID
function cancelSuspendDelay() {
backgroundTaskManager.cancelSuspendDelay(id);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/native-transient-task-V14
爬取时间: 2025-04-28 00:28:50
来源: Huawei Developer
场景介绍
应用退至后台一小段时间后，应用进程会被挂起，无法执行对应的任务。如果应用在后台仍需要执行耗时不长的任务，如状态保存等，可以通过本文申请短时任务，扩展应用在后台的运行时间。
接口说明
常用接口如下表所示。
| 接口名 | 描述 |
| --- | --- |
| int32_t OH_BackgroundTaskManager_RequestSuspendDelay(const char *reason, TransientTask_Callback callback, TransientTask_DelaySuspendInfo *info); | 申请短时任务。 |
| int32_t OH_BackgroundTaskManager_GetRemainingDelayTime(int32_t requestId, int32_t *delayTime); | 获取对应短时任务的剩余时间。 |
| int32_t OH_BackgroundTaskManager_CancelSuspendDelay(int32_t requestId); | 取消短时任务。 |
开发步骤
在napi_init.cpp文件中封装接口并注册模块
1.  封装函数
2.  注册函数
3.  注册模块
在index.d.ts文件中声明函数
```typescript
export const RequestSuspendDelay: () => number;
export const GetRemainingDelayTime: () => number;
export const CancelSuspendDelay: () => number;
```
在index.ets文件中调用函数
```typescript
import testTransientTask from 'libentry.so';
@Entry
@Component
struct Index {
@State message: string = '';
build() {
Row() {
Column() {
Text(this.message)
.fontSize(50)
.fontWeight(FontWeight.Bold)
Button('申请短时任务').onClick(event => {
this.RequestSuspendDelay();
})
Button('获取剩余时间').onClick(event =>{
this.GetRemainingDelayTime();
})
Button('取消短时任务').onClick(event =>{
this.CancelSuspendDelay();
})
}
.width('100%')
}
.height('100%')
}
RequestSuspendDelay() {
let requestId = testTransientTask.RequestSuspendDelay();
console.log("The return requestId is " + requestId);
}
GetRemainingDelayTime() {
let time = testTransientTask.GetRemainingDelayTime();
console.log("The time is " + time);
}
CancelSuspendDelay() {
let ret = testTransientTask.CancelSuspendDelay();
console.log("The ret is " + ret);
}
}
```
配置库依赖
配置CMakeLists.txt，本模块需要用到的共享库是libtransient_task.so，在工程自动生成的CMakeLists.txt中的target_link_libraries中添加此共享库。
测试步骤
1.  连接设备并运行程序。
2.  点击 申请短时任务 按钮，控制台会打印日志，示例如下：
3.  点击 获取剩余时间 按钮，控制台会打印日志，示例如下：
4.  点击 取消短时任务 按钮，控制台会打印日志，示例如下：
申请短时任务的按钮，不可连续点击超过3次，否则会报错。使用过程中更多的约束与限制请参考短时任务(ArkTS)。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/continuous-task-V14
爬取时间: 2025-04-28 00:29:03
来源: Huawei Developer
概述
功能介绍
应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。在长时任务中，支持同时申请多种类型的任务，也可以对任务类型进行更新。应用退至后台执行业务时，系统会做一致性校验，确保应用在执行相应的长时任务。应用在申请长时任务成功后，通知栏会显示与长时任务相关联的消息，用户删除通知栏消息时，系统会自动停止长时任务。
使用场景
下表给出了当前长时任务支持的类型，包含数据传输、音视频播放、录制、定位导航、蓝牙相关业务、多设备互联、音视频通话和计算任务。可以参考下表中的场景举例，选择合适的长时任务类型。
表1长时任务类型
| 参数名 | 描述 | 配置项 | 场景举例 |
| --- | --- | --- | --- |
| DATA_TRANSFER | 数据传输 | dataTransfer | 非托管形式的上传、下载，如在浏览器后台上传或下载数据。 |
| AUDIO_PLAYBACK | 音视频播放 | audioPlayback | 音频、视频在后台播放，音视频投播。 说明： 支持在元服务中使用。 |
| AUDIO_RECORDING | 录制 | audioRecording | 录音、录屏退后台。 |
| LOCATION | 定位导航 | location | 定位、导航。 |
| BLUETOOTH_INTERACTION | 蓝牙相关业务 | bluetoothInteraction | 通过蓝牙传输文件时退后台。 |
| MULTI_DEVICE_CONNECTION | 多设备互联 | multiDeviceConnection | 分布式业务连接、投播。 说明： 支持在元服务中使用。 |
| VOIP13+ | 音视频通话 | voip | 某些聊天类应用（具有音视频业务）音频、视频通话时退后台。 |
| TASK_KEEPING | 计算任务（仅对2in1设备开放） | taskKeeping | 如杀毒软件。 |
音频、视频在后台播放，音视频投播。
说明：支持在元服务中使用。
分布式业务连接、投播。
说明：支持在元服务中使用。
关于DATA_TRANSFER（数据传输）说明：
-  在数据传输时，若应用使用上传下载代理接口托管给系统，即使申请DATA_TRANSFER的后台任务，应用退后台时还是会被挂起。
-  在数据传输时，应用需要更新进度。如果进度长时间（超过10分钟）不更新，数据传输的长时任务会被取消。更新进度实现可参考startBackgroundRunning()中的示例。
关于AUDIO_PLAYBACK（音视频播放）说明：
-  若要通过AUDIO_PLAYBACK实现后台播放，须使用媒体会话服务（AVSession）进行音视频开发。
-  音视频投播，是指将一台设备的音视频投至另一台设备播放。投播退至后台，长时任务会检测音视频播放和投屏两个业务，只要有其一正常运行，长时任务就不会终止。
约束与限制
申请限制：Stage模型中，长时任务仅支持UIAbility申请；FA模型中，长时任务仅支持ServiceAbility申请。长时任务支持设备当前应用申请，也支持跨设备或跨应用申请，跨设备或跨应用仅对系统应用开放。
数量限制：一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持申请一个长时任务，即在一个长时任务结束后才可能继续申请。如果一个应用同时需要申请多个长时任务，需要创建多个UIAbility；一个应用的一个UIAbility申请长时任务后，整个应用下的所有进程均不会被挂起。
运行限制：
-  申请长时任务后，应用未执行相应的业务，系统会对应用进行管控。如系统检测到应用申请了AUDIO_PLAYBACK（音视频播放），但实际未播放音乐，长时任务会被取消。
-  申请长时任务后，应用执行的业务类型与申请的不一致，系统会对应用进行管控。如系统检测到应用只申请了AUDIO_PLAYBACK（音视频播放），但实际上除了播放音乐（对应AUDIO_PLAYBACK类型），还在进行录制（对应AUDIO_RECORDING类型）。
-  申请长时任务后，应用的业务已执行完，系统会对应用进行管控。
-  若运行长时任务的进程后台负载持续高于所申请类型的典型负载，系统会对应用进行管控。
应用按需求申请长时任务，当应用无需在后台运行（任务结束）时，要及时主动取消长时任务，否则系统会强行取消。例如用户主动点击音乐暂停播放时，应用需及时取消对应的长时任务；用户再次点击音乐播放时，需重新申请长时任务。
若音频在后台播放时被打断，系统会自行检测和停止长时任务，音频重启播放时，需要再次申请长时任务。
后台播放音频的应用，在后台停止长时任务的同时，需要暂停或停止音频流，否则应用会被系统强制终止。
接口说明
表2主要接口
以下是长时任务开发使用的相关接口，下表均以Promise形式为例，更多接口及使用方式请见后台任务管理。
| 接口名 | 描述 |
| --- | --- |
| startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void> | 申请长时任务 |
| stopBackgroundRunning(context: Context): Promise<void> | 取消长时任务 |
开发步骤
本文以申请录制长时任务为例，实现如下功能：
-  点击“申请长时任务”按钮，应用申请录制长时任务成功，通知栏显示“正在运行录制任务”通知。
-  点击“取消长时任务”按钮，取消长时任务，通知栏撤销相关通知。
Stage模型
1.  需要申请ohos.permission.KEEP_BACKGROUND_RUNNING权限，配置方式请参见声明权限。
2.  声明后台模式类型。在module.json5文件中为需要使用长时任务的UIAbility声明相应的长时任务类型，配置文件中填写长时任务类型的配置项。
```json
"module": {
"abilities": [
{
"backgroundModes": [
// 长时任务类型的配置项
"audioRecording"
]
}
],
// ...
}
```
3.  导入模块。 长时任务相关的模块为@ohos.resourceschedule.backgroundTaskManager和@ohos.app.ability.wantAgent，其余模块按实际需要导入。
```typescript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { rpc } from '@kit.IPCKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
```
4.  申请和取消长时任务。 设备当前应用申请长时任务示例代码如下：
```typescript
@Entry
@Component
struct Index {
@State message: string = 'ContinuousTask';
// 通过getContext方法，来获取page所在的UIAbility上下文。
private context: Context = getContext(this);
startContinuousTask() {
let wantAgentInfo: wantAgent.WantAgentInfo = {
// 点击通知后，将要执行的动作列表
// 添加需要被拉起应用的bundleName和abilityName
wants: [
{
bundleName: "com.example.myapplication",
abilityName: "MainAbility"
}
],
// 指定点击通知栏消息后的动作是拉起ability
actionType: wantAgent.OperationType.START_ABILITY,
// 使用者自定义的一个私有值
requestCode: 0,
// 点击通知后，动作执行属性
actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};
try {
// 通过wantAgent模块下getWantAgent方法获取WantAgent对象
wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
try {
let list: Array<string> = ["audioRecording"];
backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
console.info("Operation startBackgroundRunning succeeded");
// 此处执行具体的长时任务逻辑，如录音，录制等。
}).catch((error: BusinessError) => {
console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
});
} catch (error) {
console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
});
} catch (error) {
console.error(`Failed to Operation getWantAgent. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
}
stopContinuousTask() {
backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
console.info(`Succeeded in operationing stopBackgroundRunning.`);
}).catch((err: BusinessError) => {
console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
});
}
build() {
Row() {
Column() {
Text("Index")
.fontSize(50)
.fontWeight(FontWeight.Bold)
Button() {
Text('申请长时任务').fontSize(25).fontWeight(FontWeight.Bold)
}
.type(ButtonType.Capsule)
.margin({ top: 10 })
.backgroundColor('#0D9FFB')
.width(250)
.height(40)
.onClick(() => {
// 通过按钮申请长时任务
this.startContinuousTask();
})
Button() {
Text('取消长时任务').fontSize(25).fontWeight(FontWeight.Bold)
}
.type(ButtonType.Capsule)
.margin({ top: 10 })
.backgroundColor('#0D9FFB')
.width(250)
.height(40)
.onClick(() => {
// 此处结束具体的长时任务的执行
// 通过按钮取消长时任务
this.stopContinuousTask();
})
}
.width('100%')
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/work-scheduler-V14
爬取时间: 2025-04-28 00:29:16
来源: Huawei Developer
概述
功能介绍
应用退至后台后，需要执行实时性要求不高的任务，例如有网络时不定期主动获取邮件等，可以使用延迟任务。当应用满足设定条件（包括网络类型、充电类型、存储状态、电池状态、定时状态等）时，将任务添加到执行队列，系统会根据内存、功耗、设备温度、用户使用习惯等统一调度拉起应用。
运行原理
图1延迟任务实现原理
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170404.97731554972620391128732687565908:50001231000000:2800:70A87BC799CE952AC69F381D691EA90C1639F4FAB43EEBCD27DBB5B55F7E36AD.png)
应用调用延迟任务接口添加、删除、查询延迟任务，延迟任务管理模块会根据任务设置的条件（通过WorkInfo参数设置，包括网络类型、充电类型、存储状态等）和系统状态（包括内存、功耗、设备温度、用户使用习惯等）统一决策调度时机。
当满足调度条件或调度结束时，系统会回调应用WorkSchedulerExtensionAbility中 onWorkStart() 或 onWorkStop() 的方法，同时会为应用单独创建一个Extension扩展进程用以承载WorkSchedulerExtensionAbility，并给WorkSchedulerExtensionAbility一定的活动周期，开发者可以在对应回调方法中实现自己的任务逻辑。
约束与限制
-  数量限制：一个应用同一时刻最多申请10个延迟任务。
-  执行频率限制：系统会根据应用的活跃分组，对延迟任务做分级管控，限制延迟任务调度的执行频率。 表1应用活跃程度分组
-  超时：WorkSchedulerExtensionAbility单次回调最长运行2分钟。如果超时不取消，系统会终止对应的Extension进程。
-  调度延迟：系统会根据内存、功耗、设备温度、用户使用习惯等统一调度，如当系统内存资源不足或温度达到一定挡位时，系统将延迟调度该任务。
-  WorkSchedulerExtensionAbility接口调用限制：为实现对WorkSchedulerExtensionAbility能力的管控，在WorkSchedulerExtensionAbility中限制以下接口的调用： @ohos.resourceschedule.backgroundTaskManager (后台任务管理) @ohos.backgroundTaskManager (后台任务管理) @ohos.multimedia.camera (相机管理) @ohos.multimedia.audio (音频管理) @ohos.multimedia.media (媒体服务)
| 应用活跃分组 | 延迟任务执行频率 |
| --- | --- |
| 活跃分组 | 最小间隔2小时 |
| 经常使用分组 | 最小间隔4小时 |
| 常用使用 | 最小间隔24小时 |
| 极少使用分组 | 最小间隔48小时 |
| 受限使用分组 | 禁止 |
| 从未使用分组 | 禁止 |
接口说明
表2延迟任务主要接口
以下是延迟任务开发使用的相关接口，更多接口及使用方式请见延迟任务调度文档。
| 接口名 | 接口描述 |
| --- | --- |
| startWork(work: WorkInfo): void; | 申请延迟任务 |
| stopWork(work: WorkInfo, needCancel?: boolean): void; | 取消延迟任务 |
| getWorkStatus(workId: number, callback: AsyncCallback<WorkInfo>): void; | 获取延迟任务状态（Callback形式） |
| getWorkStatus(workId: number): Promise<WorkInfo>; | 获取延迟任务状态（Promise形式） |
| obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void; | 获取所有延迟任务（Callback形式） |
| obtainAllWorks(): Promise<Array<WorkInfo>>; | 获取所有延迟任务（Promise形式） |
| stopAndClearWorks(): void; | 停止并清除任务 |
| isLastWorkTimeOut(workId: number, callback: AsyncCallback<boolean>): void; | 获取上次任务是否超时（针对RepeatWork，Callback形式） |
| isLastWorkTimeOut(workId: number): Promise<boolean>; | 获取上次任务是否超时（针对RepeatWork，Promise形式） |
表3WorkInfo参数
| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| workId | number | 是 | 延迟任务ID。 |
| bundleName | string | 是 | 延迟任务所在应用的包名。 |
| abilityName | string | 是 | 包内ability名称。 |
| networkType | NetworkType | 否 | 网络类型。 |
| isCharging | boolean | 否 | 是否充电。 - true表示充电触发延迟回调。 - false表示不充电触发延迟回调。 |
| chargerType | ChargingType | 否 | 充电类型。 |
| batteryLevel | number | 否 | 电量。 |
| batteryStatus | BatteryStatus | 否 | 电池状态。 |
| storageRequest | StorageRequest | 否 | 存储状态。 |
| isRepeat | boolean | 否 | 是否循环任务。 - true表示循环任务。 - false表示非循环任务。 |
| repeatCycleTime | number | 否 | 循环间隔，单位为毫秒。 |
| repeatCount | number | 否 | 循环次数。 |
| isPersisted | boolean | 否 | 注册的延迟任务是否可保存在系统中。 - true表示可保存，即系统重启后，任务可恢复。 - false表示不可保存。 |
| isDeepIdle | boolean | 否 | 是否要求设备进入空闲状态。 - true表示需要。 - false表示不需要。 |
| idleWaitTime | number | 否 | 空闲等待时间，单位为毫秒。 |
| parameters | [key: string]: number | string | boolean | 否 | 携带参数信息。 |
是否充电。
- true表示充电触发延迟回调。
- false表示不充电触发延迟回调。
是否循环任务。
- true表示循环任务。
- false表示非循环任务。
注册的延迟任务是否可保存在系统中。
- true表示可保存，即系统重启后，任务可恢复。
- false表示不可保存。
是否要求设备进入空闲状态。
- true表示需要。
- false表示不需要。
WorkInfo参数用于设置应用条件，参数设置时需遵循以下规则：
-  workId、bundleName、abilityName为必填项，bundleName需为本应用包名。
-  携带参数信息仅支持number、string、boolean三种类型。
-  至少设置一个满足的条件，包括网络类型、充电类型、存储状态、电池状态、定时状态等。
-  对于重复任务，任务执行间隔至少2小时。设置重复任务时间间隔时，须同时设置是否循环或循环次数中的一个。
表4延迟任务回调接口
以下是延迟任务回调开发使用的相关接口，更多接口及使用方式请见延迟任务调度回调文档。
| 接口名 | 接口描述 |
| --- | --- |
| onWorkStart(work: workScheduler.WorkInfo): void | 延迟调度任务开始的回调 |
| onWorkStop(work: workScheduler.WorkInfo): void | 延迟调度任务结束的回调 |
开发步骤
延迟任务调度开发步骤分为两步：实现延迟任务调度扩展能力、实现延迟任务调度。
1.  延迟任务调度扩展能力：实现WorkSchedulerExtensionAbility开始和结束的回调接口。
2.  延迟任务调度：调用延迟任务接口，实现延迟任务申请、取消等功能。
实现延迟任务回调拓展能力
1.  新建工程目录。 在工程entry Module对应的ets目录(./entry/src/main/ets)下，新建目录及ArkTS文件，例如新建一个目录并命名为WorkSchedulerExtension。在WorkSchedulerExtension目录下，新建一个ArkTS文件并命名为WorkSchedulerExtension.ets，用以实现延迟任务回调接口。
2.  导入模块。
```typescript
import { WorkSchedulerExtensionAbility, workScheduler } from '@kit.BackgroundTasksKit';
```
3.  实现WorkSchedulerExtension生命周期接口。
```typescript
export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
// 延迟任务开始回调
onWorkStart(workInfo: workScheduler.WorkInfo) {
console.info(`onWorkStart, workInfo = ${JSON.stringify(workInfo)}`);
// 打印 parameters中的参数，如：参数key1
// console.info(`work info parameters: ${JSON.parse(workInfo.parameters?.toString()).key1}`)
}
// 延迟任务结束回调
onWorkStop(workInfo: workScheduler.WorkInfo) {
console.info(`onWorkStop, workInfo is ${JSON.stringify(workInfo)}`);
}
}
```
4.  在module.json5配置文件中注册WorkSchedulerExtensionAbility，并设置如下标签： type标签设置为“workScheduler”。 srcEntry标签设置为当前ExtensionAbility组件所对应的代码路径。
```json
{
"module": {
"extensionAbilities": [
{
"name": "MyWorkSchedulerExtensionAbility",
"srcEntry": "./ets/WorkSchedulerExtension/WorkSchedulerExtension.ets",
"type": "workScheduler"
}
]
}
}
```
5.  type标签设置为“workScheduler”。
6.  srcEntry标签设置为当前ExtensionAbility组件所对应的代码路径。
-  type标签设置为“workScheduler”。
-  srcEntry标签设置为当前ExtensionAbility组件所对应的代码路径。
实现延迟任务调度
1.  导入模块。
```typescript
import { workScheduler } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.  申请延迟任务。
```typescript
// 创建workinfo
const workInfo: workScheduler.WorkInfo = {
workId: 1,
networkType: workScheduler.NetworkType.NETWORK_TYPE_WIFI,
bundleName: 'com.example.application',
abilityName: 'MyWorkSchedulerExtensionAbility'
}
try {
workScheduler.startWork(workInfo);
console.info(`startWork success`);
} catch (error) {
console.error(`startWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```
3.  取消延迟任务。
```typescript
// 创建workinfo
const workInfo: workScheduler.WorkInfo = {
workId: 1,
networkType: workScheduler.NetworkType.NETWORK_TYPE_WIFI,
bundleName: 'com.example.application',
abilityName: 'MyWorkSchedulerExtensionAbility'
}
try {
workScheduler.stopWork(workInfo);
console.info(`stopWork success`);
} catch (error) {
console.error(`stopWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/agent-powered-reminder-V14
爬取时间: 2025-04-28 00:29:30
来源: Huawei Developer
概述
功能介绍
应用退到后台或进程终止后，仍然有一些提醒用户的定时类任务，例如购物类应用抢购提醒等，为满足此类功能场景，系统提供了代理提醒（reminderAgentManager）的能力。当应用退至后台或进程终止后，系统会代理应用做相应的提醒。当前支持的提醒类型包括：倒计时、日历和闹钟。为了防止代理提醒被滥用于广告、营销类提醒，影响用户体验，代理增加了管控机制，管控后的使用方法请参考管控限制。
-  倒计时类：基于倒计时的提醒功能。
-  日历类：基于日历的提醒功能。
-  闹钟类：基于时钟的提醒功能。
约束与限制
当到达设置的提醒时间点时，通知中心会弹出相应提醒。若未点击提醒上的关闭/CLOSE按钮，则代理提醒是有效/未过期的；若点击了关闭/CLOSE按钮，则代理提醒过期。
当代理提醒是周期性提醒时，如设置每天提醒，无论是否点击关闭/CLOSE按钮，代理提醒都是有效的。
-  跳转限制：点击提醒通知后跳转的应用必须是申请代理提醒的本应用。
-  管控限制：管控后可通过日历Calendar Kit 替代代理提醒，实现相应的提醒功能，具体请参考开发指南；或者参考如下邮件格式向华为侧申请代理提醒权限，申请通过后会开通权益，即可正常调用代理提醒接口，当前仅对纯工具类应用开放申请。 邮件格式： 通过hwpush@huawei.com邮箱向华为侧申请，邮件会在10个工作日内回复（含权益开通结果），邮件提示申请通过后1天权益生效，请留意邮箱消息。邮件的规定格式如下： 邮件主题：【代理提醒权限申请】 邮件正文： 申请权限名称：代理提醒 企业名称： 应用名称：*** 应用包名：com.. 使用场景：提供申请理由/用途/尽可能附上图片，及使用代理提醒发通知/提醒的必要性。 通知标题：*** 通知文本：*** 通知场景：*** 通知频率：***
接口说明
表1主要接口
以下是代理提醒的相关接口，下表均以Promise形式为例，更多接口及使用方式请见后台代理提醒文档。
| 接口名 | 描述 |
| --- | --- |
| publishReminder(reminderReq: ReminderRequest): Promise<number> | 发布一个定时提醒类通知。 |
| cancelReminder(reminderId: number): Promise<void> | 取消一个指定的提醒类通知。 |
| getValidReminders(): Promise<Array<ReminderRequest>> | 获取当前应用设置的所有有效的提醒。 |
| cancelAllReminders(): Promise<void> | 取消当前应用设置的所有提醒。 |
| addNotificationSlot(slot: NotificationSlot): Promise<void> | 注册一个提醒类需要使用的通知通道（NotificationSlot）。 |
| removeNotificationSlot(slotType: notification.SlotType): Promise<void> | 删除指定的通知通道（NotificationSlot）。 |
开发步骤
1.  申请ohos.permission.PUBLISH_AGENT_REMINDER权限，配置方式请参阅声明权限。
2.  请求通知授权。获得用户授权后，才能使用代理提醒功能。
3.  导入模块。
```typescript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
4.  定义目标提醒代理。开发者根据实际需要，选择定义如下类型的提醒。 定义倒计时实例。 定义日历实例。 定义闹钟实例。
```typescript
let targetReminderAgent: reminderAgentManager.ReminderRequestTimer = {
reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,   // 提醒类型为倒计时类型
triggerTimeInSeconds: 10,
actionButton: [ // 设置弹出的提醒通知信息上显示的按钮类型和标题
{
title: 'close',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
}
],
wantAgent: {     // 点击提醒通知后跳转的目标UIAbility信息
pkgName: 'com.example.myapplication',
abilityName: 'EntryAbility'
},
title: 'this is title', // 指明提醒标题
content: 'this is content', // 指明提醒内容
expiredContent: 'this reminder has expired', // 指明提醒过期后需要显示的内容
notificationId: 100, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION // 指明提醒的Slot类型
}
```
5.  定义倒计时实例。
```typescript
let targetReminderAgent: reminderAgentManager.ReminderRequestTimer = {
reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,   // 提醒类型为倒计时类型
triggerTimeInSeconds: 10,
actionButton: [ // 设置弹出的提醒通知信息上显示的按钮类型和标题
{
title: 'close',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
}
],
wantAgent: {     // 点击提醒通知后跳转的目标UIAbility信息
pkgName: 'com.example.myapplication',
abilityName: 'EntryAbility'
},
title: 'this is title', // 指明提醒标题
content: 'this is content', // 指明提醒内容
expiredContent: 'this reminder has expired', // 指明提醒过期后需要显示的内容
notificationId: 100, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION // 指明提醒的Slot类型
}
```
6.  定义日历实例。
```typescript
let targetReminderAgent: reminderAgentManager.ReminderRequestCalendar = {
reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_CALENDAR, // 提醒类型为日历类型
dateTime: {   // 指明提醒的目标时间
year: 2023,
month: 1,
day: 1,
hour: 11,
minute: 14,
second: 30
},
repeatMonths: [1], // 指明重复提醒的月份
repeatDays: [1], // 指明重复提醒的日期
actionButton: [ // 设置弹出的提醒通知信息上显示的按钮类型和标题
{
title: 'close',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
},
{
title: 'snooze',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE
},
],
wantAgent: { // 点击提醒通知后跳转的目标UIAbility信息
pkgName: 'com.example.myapplication',
abilityName: 'EntryAbility'
},
ringDuration: 5, // 指明响铃时长（单位：秒）
snoozeTimes: 2, // 指明延迟提醒次数
timeInterval: 5*60, // 执行延迟提醒间隔（单位：秒）
title: 'this is title', // 指明提醒标题
content: 'this is content', // 指明提醒内容
expiredContent: 'this reminder has expired', // 指明提醒过期后需要显示的内容
snoozeContent: 'remind later', // 指明延迟提醒时需要显示的内容
notificationId: 100, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION // 指明提醒的Slot类型
}
```
7.  定义闹钟实例。
```typescript
let targetReminderAgent: reminderAgentManager.ReminderRequestAlarm = {
reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_ALARM, // 提醒类型为闹钟类型
hour: 23, // 指明提醒的目标时刻
minute: 9, // 指明提醒的目标分钟
daysOfWeek: [2], // 指明每周哪几天需要重复提醒
actionButton: [ // 设置弹出的提醒通知信息上显示的按钮类型和标题
{
title: 'close',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
},
{
title: 'snooze',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE
},
],
wantAgent: { // 点击提醒通知后跳转的目标UIAbility信息
pkgName: 'com.example.myapplication',
abilityName: 'EntryAbility'
},
ringDuration: 5, // 指明响铃时长（单位：秒）
snoozeTimes: 2, // 指明延迟提醒次数
timeInterval: 5*60, // 执行延迟提醒间隔（单位：秒）
title: 'this is title', // 指明提醒标题
content: 'this is content', // 指明提醒内容
expiredContent: 'this reminder has expired', // 指明提醒过期后需要显示的内容
snoozeContent: 'remind later', // 指明延迟提醒时需要显示的内容
notificationId: 99, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION // 指明提醒的Slot类型
}
```
8.  发布相应的提醒代理。代理发布后，应用即可使用后台代理提醒功能。
```typescript
reminderAgentManager.publishReminder(targetReminderAgent).then((res: number) => {
console.info('Succeeded in publishing reminder. ');
let reminderId: number = res; // 发布的提醒ID
}).catch((err: BusinessError) => {
console.error(`Failed to publish reminder. Code: ${err.code}, message: ${err.message}`);
})
```
9.  根据需要删除提醒任务。
```typescript
let reminderId: number = 1;
// reminderId的值从发布提醒代理成功之后的回调中获得
reminderAgentManager.cancelReminder(reminderId).then(() => {
console.log('Succeeded in canceling reminder.');
}).catch((err: BusinessError) => {
console.error(`Failed to cancel reminder. Code: ${err.code}, message: ${err.message}`);
});
```
-  定义倒计时实例。
```typescript
let targetReminderAgent: reminderAgentManager.ReminderRequestTimer = {
reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,   // 提醒类型为倒计时类型
triggerTimeInSeconds: 10,
actionButton: [ // 设置弹出的提醒通知信息上显示的按钮类型和标题
{
title: 'close',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
}
],
wantAgent: {     // 点击提醒通知后跳转的目标UIAbility信息
pkgName: 'com.example.myapplication',
abilityName: 'EntryAbility'
},
title: 'this is title', // 指明提醒标题
content: 'this is content', // 指明提醒内容
expiredContent: 'this reminder has expired', // 指明提醒过期后需要显示的内容
notificationId: 100, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION // 指明提醒的Slot类型
}
```
-  定义日历实例。
```typescript
let targetReminderAgent: reminderAgentManager.ReminderRequestCalendar = {
reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_CALENDAR, // 提醒类型为日历类型
dateTime: {   // 指明提醒的目标时间
year: 2023,
month: 1,
day: 1,
hour: 11,
minute: 14,
second: 30
},
repeatMonths: [1], // 指明重复提醒的月份
repeatDays: [1], // 指明重复提醒的日期
actionButton: [ // 设置弹出的提醒通知信息上显示的按钮类型和标题
{
title: 'close',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
},
{
title: 'snooze',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE
},
],
wantAgent: { // 点击提醒通知后跳转的目标UIAbility信息
pkgName: 'com.example.myapplication',
abilityName: 'EntryAbility'
},
ringDuration: 5, // 指明响铃时长（单位：秒）
snoozeTimes: 2, // 指明延迟提醒次数
timeInterval: 5*60, // 执行延迟提醒间隔（单位：秒）
title: 'this is title', // 指明提醒标题
content: 'this is content', // 指明提醒内容
expiredContent: 'this reminder has expired', // 指明提醒过期后需要显示的内容
snoozeContent: 'remind later', // 指明延迟提醒时需要显示的内容
notificationId: 100, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION // 指明提醒的Slot类型
}
```
-  定义闹钟实例。
```typescript
let targetReminderAgent: reminderAgentManager.ReminderRequestAlarm = {
reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_ALARM, // 提醒类型为闹钟类型
hour: 23, // 指明提醒的目标时刻
minute: 9, // 指明提醒的目标分钟
daysOfWeek: [2], // 指明每周哪几天需要重复提醒
actionButton: [ // 设置弹出的提醒通知信息上显示的按钮类型和标题
{
title: 'close',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
},
{
title: 'snooze',
type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE
},
],
wantAgent: { // 点击提醒通知后跳转的目标UIAbility信息
pkgName: 'com.example.myapplication',
abilityName: 'EntryAbility'
},
ringDuration: 5, // 指明响铃时长（单位：秒）
snoozeTimes: 2, // 指明延迟提醒次数
timeInterval: 5*60, // 执行延迟提醒间隔（单位：秒）
title: 'this is title', // 指明提醒标题
content: 'this is content', // 指明提醒内容
expiredContent: 'this reminder has expired', // 指明提醒过期后需要显示的内容
snoozeContent: 'remind later', // 指明延迟提醒时需要显示的内容
notificationId: 99, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION // 指明提醒的Slot类型
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-file-kit-V14
爬取时间: 2025-04-28 00:29:43
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-file-kit-intro-V14
爬取时间: 2025-04-28 00:29:56
来源: Huawei Developer
Core File Kit（文件基础服务）为开发者提供一套访问和管理应用文件和用户文件的能力。帮助用户更高效地管理、查找和备份各类文件，使用户能够轻松应对各种文件管理的需求。
Core File Kit概述
在Core File Kit套件中，按文件所有者的不同，有如下文件分类模型，其示意图如下面文件分类模型示意图：
-  应用文件：文件所有者为应用，包括应用安装文件、应用资源文件、应用缓存文件等。
-  用户文件：文件所有者为登录到该终端设备的用户，包括用户私有的图片、视频、音频、文档等。
-  系统文件：与应用和用户无关的其它文件，包括公共库、设备文件、系统资源文件等。这类文件不需要开发者进行文件管理，本文不展开介绍。
按文件系统管理的文件存储位置（数据源位置）的不同，有如下文件系统分类模型：
-  本地文件系统：提供本地设备或外置存储设备（如U盘、移动硬盘）的文件访问能力。本地文件系统是最基本的文件系统，本文不展开介绍。
-  分布式文件系统：提供跨设备的文件访问能力。所谓跨设备，指文件不一定存储在本地设备或外置存储设备，而是通过计算机网络与其它分布式设备相连。
图1文件分类模型示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170405.80600113338374744295298562068307:50001231000000:2800:D8259F60C7D96BB4B19A995C02567BF396CBB1BC253372C4718239A2EC32A55A.png)
Kit使用场景
Core File Kit常见的使用场景：
能力范围
亮点/特征
-  沙箱隔离： 访问和管理应用文件，对于每个应用，系统会在内部存储空间映射出一个专属的“应用沙箱目录”，它是“应用文件目录”与一部分系统文件（应用运行必需的少量系统文件）所在的目录组成的集合。有以下优点：
-  应用分享： 应用之间可以通过分享URI（Uniform Resource Identifier）或文件描述符FD（File Descriptor）的方式，进行文件共享。有以下优点：
框架原理
应用文件访问框架
应用文件访问框架是通过基础文件操作接口（ohos.file.fs）实现。开发者无需了解内部实现，基础文件操作接口功能详情请参考接口说明。
用户文件访问框架
用户文件访问框架（File Access Framework）是一套提供给开发者访问和管理用户文件的基础框架。该框架依托于HarmonyOS的ExtensionAbility组件机制，提供了一套统一访问用户文件的方法和接口。
图2用户文件访问框架示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170405.13663685595685024783462209642335:50001231000000:2800:210FC455E1DBEC82E46E839EB8C58299C9B6273BD4D3ED08FB0FA177AF8C8226.png)
-  各类系统应用或三方应用（即图中的文件访问客户端）若需访问用户文件，如选择一张照片或保存多个文档等，可以通过拉起“文件选择器应用”来实现。
-  FilePicker：系统预置应用，提供文件访问客户端选择和保存文件的能力，且不需要配置任何权限。FilePicker的使用指导请参见选择用户文件。
-  FileManager：对于设备开发者，还可以按需开发自己的文件选择器或文件管理器应用。该功能不向三方应用开放。
-  File Access Framework（用户文件访问框架）的主要功能模块如下：
与相关Kit的关系
Ability Kit: Core File Kit中用户文件访问框架依赖Ability Kit提供的Extension基础能力，受Ability Kit服务调度管理。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-file-V14
爬取时间: 2025-04-28 00:30:09
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-file-overview-V14
爬取时间: 2025-04-28 00:30:23
来源: Huawei Developer
应用文件：文件所有者为应用，包括应用安装文件、应用资源文件、应用缓存文件等。
-  设备上应用所使用及存储的数据，以文件、键值对、数据库等形式保存在一个应用专属的目录内。该专属目录我们称为“应用文件目录”，该目录下所有数据以不同的文件格式存放，这些文件即应用文件。
-  “应用文件目录”与一部分系统文件（应用运行必须使用的系统文件）所在的目录组成了一个集合，该集合称为“应用沙箱目录”，代表应用可见的所有目录范围。因此“应用文件目录”是在“应用沙箱目录”内的。
-  系统文件及其目录对于应用是只读的；应用仅能保存文件到“应用文件目录”下，根据目录的使用规范和注意事项来选择将数据保存到不同的子目录中。
下文将详细介绍应用沙箱、应用文件目录、应用文件访问与管理、应用文件分享等相关内容。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-sandbox-directory-V14
爬取时间: 2025-04-28 00:30:36
来源: Huawei Developer
应用沙箱是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“应用沙箱目录”。
-  对于每个应用，系统会在内部存储空间映射出一个专属的“应用沙箱目录”，它是“应用文件目录”与一部分系统文件（应用运行必需的少量系统文件）所在的目录组成的集合。
-  应用沙箱限制了应用可见的数据范围。在“应用沙箱目录”中，应用仅能看到自己的应用文件以及少量的系统文件（应用运行必需的少量系统文件）。因此，本应用的文件也不为其他应用可见，从而保护了应用文件的安全。
-  应用可以在“应用文件目录”下保存和处理自己的应用文件；系统文件及其目录对于应用是只读的；而应用若需访问用户文件，则需要通过特定API同时经过用户的相应授权才能进行。
下图展示了应用沙箱下，应用可访问的文件范围和方式。
图1应用沙箱文件访问关系图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170405.62279128843173203083050472398611:50001231000000:2800:24D5231E6CE491B55E670171292DBB76BB340876EEDF20089642BD109DC41EC0.png)
应用沙箱目录与应用沙箱路径
在应用沙箱保护机制下，应用无法获知除自身应用文件目录之外的其他应用或用户的数据目录位置及存在。同时，所有应用的目录可见范围均经过权限隔离与文件路径挂载隔离，形成了独立的路径视图，屏蔽了实际物理路径：
-  如下图所示，在普通应用（也称三方应用）视角下，不仅可见的目录与文件数量限制了范围，并且可见的目录与文件路径也与系统进程等其他进程看到的不同。我们将普通应用视角下看到的“应用沙箱目录”下某个文件或某个具体目录的路径，称为“应用沙箱路径”。
-  开发者在应用开发调试时，可能需要向应用沙箱下推送一些文件以期望在应用内访问或测试。可以通过DevEco Studio向应用安装路径中放入目标文件，详见应用安装资源访问。
-  实际物理路径与沙箱路径并非1:1的映射关系，沙箱路径总是少于系统进程视角可见的物理路径。部分调试进程视角下的物理路径在对应的应用沙箱目录下没有对应路径。
图2应用沙箱路径（不同权限与角色的进程下可见的文件路径不同）
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170405.92958318473063726717636340943858:50001231000000:2800:40F07FF2CB8C6B2E70A486C3CA08D534E610BB77575E4A2145DCA2F3770FEA1D.png)
应用文件目录与应用文件路径
如前文所述，“应用沙箱目录”内分为两类：应用文件目录和系统文件目录。
系统文件目录对应用的可见范围由HarmonyOS系统预置，开发者无需关注。
在此主要介绍应用文件目录，如下图所示。应用文件目录下某个文件或某个具体目录的路径称为应用文件路径。应用文件目录下的各个文件路径，具备不同的属性和特征。
图3应用文件目录结构图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170405.26442936357772382900522345161375:50001231000000:2800:720F40F2A8577743C5D948C85AA3728682A61A76C48671BBCEB588C78197D5D2.png)
1.  一级目录data/：代表应用文件目录。
2.  二级目录storage/：代表本应用持久化文件目录。
3.  三级目录el1/~el5/：代表不同文件加密类型。 EL1(Encryption Level 1): EL2(Encryption Level 2): EL3(Encryption Level 3): EL4(Encryption Level 4): EL5(Encryption Level 5): 应用如无特殊需要，应将数据存放在el2加密目录下，以尽可能保证数据安全。但是对于某些场景，一些应用文件需要在用户首次认证前就可被访问，例如时钟、闹铃、壁纸等，此时应用需要将这些文件存放到设备级加密区（el1）。 开发者可通过监听COMMON_EVENT_USER_UNLOCKED事件感知当前用户首次认证完成。 切换应用文件加密类型目录的方法请参见获取和修改加密分区。
4.  四级、五级目录： 通过ApplicationContext可以获取distributedfiles目录或base下的files、cache、preferences、temp等目录的应用文件路径，应用全局信息可以存放在这些目录下。 通过UIAbilityContext、AbilityStageContext、ExtensionContext可以获取HAP级别应用文件路径。HAP信息可以存放在这些目录下，存放在此目录的文件会跟随HAP的卸载而删除，不会影响App级别目录下的文件。在开发态，一个应用包含一个或者多个HAP，详见Stage模型应用程序包结构。 应用文件路径具体说明及生命周期如下表所示。 表1应用文件路径详细说明 应用安装后的App的HAP资源包所在目录；随应用卸载而清理。 不能拼接路径访问资源文件，请使用资源管理接口访问资源。 可以用于存储应用的代码资源数据，主要包括应用安装的HAP资源包、可重复使用的库文件以及插件资源等。此路径下存储的代码资源数据可以被用于动态加载。 应用在el2加密条件下存放通过分布式数据库服务操作的文件目录；随应用卸载而清理。 仅用于保存应用的私有数据库数据，主要包括数据库文件等。此路径下仅适用于存储分布式数据库相关文件数据。 应用在el2加密条件下存放分布式文件的目录，应用将文件放入该目录可分布式跨设备直接访问；随应用卸载而清理。 可以用于保存应用分布式场景下的数据，主要包括应用多设备共享文件、应用多设备备份文件、应用多设备群组协助文件。此路径下存储这些数据，使得应用更加适合多设备使用场景。 应用在本设备内部存储上通用的存放默认长期保存的文件路径；随应用卸载而清理。 可以用于保存应用的任何私有数据，主要包括用户持久性文件、图片、媒体文件以及日志文件等。此路径下存储这些数据，使得数据保持私有、安全且持久有效。 应用在本设备内部存储上用于缓存下载的文件或可重新生成的缓存文件的路径，应用cache目录大小超过配额或者系统空间达到一定条件，自动触发清理该目录下文件；用户通过系统空间管理类应用也可能触发清理该目录。应用需判断文件是否仍存在，决策是否需重新缓存该文件；随应用卸载而清理。 可以用于保存应用的缓存数据，主要包括离线数据、图片缓存、数据库备份以及临时文件等。此路径下存储的数据可能会被系统自动清理，因此不要存储重要数据。 应用在本设备内部存储上通过数据库API存储配置类或首选项的目录；随应用卸载而清理。详见通过用户首选项实现数据持久化。 可以用于保存应用的首选项数据，主要包括应用首选项文件以及配置文件等。此路径下仅适用于存储小量数据。 应用在本设备内部存储上仅在应用运行期间产生和需要的文件，应用退出后即清理。 可以用于保存应用的临时生成的数据，主要包括数据库缓存、图片缓存、临时日志文件、以及下载的应用安装包文件等。此路径下存储使用后即可删除的数据。
| 目录名 | Context属性名称 | 类型 | 说明 |
| --- | --- | --- | --- |
| bundle | bundleCodeDir | 安装文件路径 | 应用安装后的App的HAP资源包所在目录；随应用卸载而清理。 不能拼接路径访问资源文件，请使用资源管理接口访问资源。 可以用于存储应用的代码资源数据，主要包括应用安装的HAP资源包、可重复使用的库文件以及插件资源等。此路径下存储的代码资源数据可以被用于动态加载。 |
| base | NA | 本设备文件路径 | 应用在本设备上存放持久化数据的目录，子目录包含files/、cache/、temp/和haps/；随应用卸载而清理。 |
| database | databaseDir | 数据库路径 | 应用在el2加密条件下存放通过分布式数据库服务操作的文件目录；随应用卸载而清理。 仅用于保存应用的私有数据库数据，主要包括数据库文件等。此路径下仅适用于存储分布式数据库相关文件数据。 |
| distributedfiles | distributedFilesDir | 分布式文件路径 | 应用在el2加密条件下存放分布式文件的目录，应用将文件放入该目录可分布式跨设备直接访问；随应用卸载而清理。 可以用于保存应用分布式场景下的数据，主要包括应用多设备共享文件、应用多设备备份文件、应用多设备群组协助文件。此路径下存储这些数据，使得应用更加适合多设备使用场景。 |
| files | filesDir | 应用通用文件路径 | 应用在本设备内部存储上通用的存放默认长期保存的文件路径；随应用卸载而清理。 可以用于保存应用的任何私有数据，主要包括用户持久性文件、图片、媒体文件以及日志文件等。此路径下存储这些数据，使得数据保持私有、安全且持久有效。 |
| cache | cacheDir | 应用缓存文件路径 | 应用在本设备内部存储上用于缓存下载的文件或可重新生成的缓存文件的路径，应用cache目录大小超过配额或者系统空间达到一定条件，自动触发清理该目录下文件；用户通过系统空间管理类应用也可能触发清理该目录。应用需判断文件是否仍存在，决策是否需重新缓存该文件；随应用卸载而清理。 可以用于保存应用的缓存数据，主要包括离线数据、图片缓存、数据库备份以及临时文件等。此路径下存储的数据可能会被系统自动清理，因此不要存储重要数据。 |
| preferences | preferencesDir | 应用首选项文件路径 | 应用在本设备内部存储上通过数据库API存储配置类或首选项的目录；随应用卸载而清理。详见通过用户首选项实现数据持久化。 可以用于保存应用的首选项数据，主要包括应用首选项文件以及配置文件等。此路径下仅适用于存储小量数据。 |
| temp | tempDir | 应用临时文件路径 | 应用在本设备内部存储上仅在应用运行期间产生和需要的文件，应用退出后即清理。 可以用于保存应用的临时生成的数据，主要包括数据库缓存、图片缓存、临时日志文件、以及下载的应用安装包文件等。此路径下存储使用后即可删除的数据。 |
应用沙箱路径和真实物理路径的对应关系
在应用沙箱路径下读写文件，经过映射转换，实际读写的是真实物理路径中的应用文件，应用沙箱路径与真实物理路径对应关系如下表所示。
其中<USERID>为当前用户ID，从100开始递增，<EXTENSIONPATH>为moduleName-extensionName。应用是否以Extension独立沙箱运行可参考ExtensionAbility组件。
| 应用沙箱路径 | 物理路径 |
| --- | --- |
| /data/storage/el1/bundle | 应用安装包目录： /data/app/el1/bundle/public/<PACKAGENAME> |
| /data/storage/el1/base | 应用el1级别加密数据目录： - 非独立沙箱运行的应用：/data/app/el1/<USERID>/base/<PACKAGENAME> - 以独立沙箱运行的Extension应用： /data/app/el1/<USERID>/base/+extension-<EXTENSIONPATH>+<PACKAGENAME> |
| /data/storage/el2/base | 应用el2级别加密数据目录： - 非独立沙箱运行的应用：/data/app/el2/<USERID>/base/<PACKAGENAME> - 以独立沙箱运行的Extension应用： /data/app/el2/<USERID>/base/+extension-<EXTENSIONPATH>+<PACKAGENAME> |
| /data/storage/el1/database | 应用el1级别加密数据库目录： - 非独立沙箱运行的应用：/data/app/el1/<USERID>/database/<PACKAGENAME> - 以独立沙箱运行的Extension应用：/data/app/el1/<USERID>/database/+extension-<EXTENSIONPATH>+<PACKAGENAME> |
| /data/storage/el2/database | 应用el2级别加密数据库目录： - 非独立沙箱运行的应用：/data/app/el2/<USERID>/database/<PACKAGENAME> - 以独立沙箱运行的Extension应用：/data/app/el2/<USERID>/database/+extension-<EXTENSIONPATH>+<PACKAGENAME> |
| /data/storage/el2/distributedfiles | /mnt/hmdfs/<USERID>/account/merge_view/data/<PACKAGENAME> |
应用安装包目录：
/data/app/el1/bundle/public/<PACKAGENAME>
应用el1级别加密数据目录：
- 非独立沙箱运行的应用：/data/app/el1/<USERID>/base/<PACKAGENAME>
- 以独立沙箱运行的Extension应用： /data/app/el1/<USERID>/base/+extension-<EXTENSIONPATH>+<PACKAGENAME>
应用el2级别加密数据目录：
- 非独立沙箱运行的应用：/data/app/el2/<USERID>/base/<PACKAGENAME>
- 以独立沙箱运行的Extension应用： /data/app/el2/<USERID>/base/+extension-<EXTENSIONPATH>+<PACKAGENAME>
应用el1级别加密数据库目录：
- 非独立沙箱运行的应用：/data/app/el1/<USERID>/database/<PACKAGENAME>
- 以独立沙箱运行的Extension应用：/data/app/el1/<USERID>/database/+extension-<EXTENSIONPATH>+<PACKAGENAME>
应用el2级别加密数据库目录：
- 非独立沙箱运行的应用：/data/app/el2/<USERID>/database/<PACKAGENAME>
- 以独立沙箱运行的Extension应用：/data/app/el2/<USERID>/database/+extension-<EXTENSIONPATH>+<PACKAGENAME>

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-file-access-management-V14
爬取时间: 2025-04-28 00:30:49
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-file-access-V14
爬取时间: 2025-04-28 00:31:02
来源: Huawei Developer
应用需要对应用文件目录下的应用文件进行查看、创建、读写、删除、移动、复制、获取属性等访问操作，下文介绍具体方法。
接口说明
开发者通过基础文件操作接口（ohos.file.fs）实现应用文件访问能力，主要功能如下表所示。
表1基础文件操作接口功能
| 接口名 | 功能 | 接口类型 | 支持同步 | 支持异步 |
| --- | --- | --- | --- | --- |
| access | 检查文件是否存在 | 方法 | √ | √ |
| close | 关闭文件 | 方法 | √ | √ |
| copyFile | 复制文件 | 方法 | √ | √ |
| createStream | 基于文件路径打开文件流 | 方法 | √ | √ |
| listFile | 列出文件夹下所有文件名 | 方法 | √ | √ |
| mkdir | 创建目录 | 方法 | √ | √ |
| moveFile | 移动文件 | 方法 | √ | √ |
| open | 打开文件 | 方法 | √ | √ |
| read | 从文件读取数据 | 方法 | √ | √ |
| rename | 重命名文件或文件夹 | 方法 | √ | √ |
| rmdir | 删除整个目录 | 方法 | √ | √ |
| stat | 获取文件详细属性信息 | 方法 | √ | √ |
| unlink | 删除单个文件 | 方法 | √ | √ |
| write | 将数据写入文件 | 方法 | √ | √ |
| Stream.close | 关闭文件流 | 方法 | √ | √ |
| Stream.flush | 刷新文件流 | 方法 | √ | √ |
| Stream.write | 将数据写入流文件 | 方法 | √ | √ |
| Stream.read | 从流文件读取数据 | 方法 | √ | √ |
| File.fd | 获取文件描述符 | 属性 | - | - |
| OpenMode | 设置文件打开标签 | 属性 | - | - |
| Filter | 设置文件过滤配置项 | 类型 | - | - |
使用基础文件操作接口时，耗时较长的操作，例如：read、write等，建议使用异步接口，避免应用崩溃。
开发示例
在对应用文件开始访问前，开发者需要获取应用文件路径。以从UIAbilityContext获取HAP级别的文件路径为例进行说明，UIAbilityContext的获取方式请参见获取UIAbility的上下文信息。
下面介绍几种常用操作示例。
新建并读写一个文件
以下示例代码演示了如何新建一个文件并对其读写。
```typescript
// pages/xxx.ets
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { buffer } from '@kit.ArkTS';
// 获取应用文件路径
let context = getContext(this) as common.UIAbilityContext;
let filesDir = context.filesDir;
function createFile(): void {
// 文件不存在时创建并打开文件，文件存在时打开文件
let file = fs.openSync(filesDir + '/test.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
// 写入一段内容至文件
let writeLen = fs.writeSync(file.fd, "Try to write str.");
console.info("The length of str is: " + writeLen);
// 创建一个大小为1024字节的ArrayBuffer对象，用于存储从文件中读取的数据
let arrayBuffer = new ArrayBuffer(1024);
// 设置读取的偏移量和长度
let readOptions: ReadOptions = {
offset: 0,
length: arrayBuffer.byteLength
};
// 读取文件内容到ArrayBuffer对象中，并返回实际读取的字节数
let readLen = fs.readSync(file.fd, arrayBuffer, readOptions);
// 将ArrayBuffer对象转换为Buffer对象，并转换为字符串输出
let buf = buffer.from(arrayBuffer, 0, readLen);
console.info("the content of file: " + buf.toString());
// 关闭文件
fs.closeSync(file);
}
```
读取文件内容并写入到另一个文件
以下示例代码演示了如何从一个文件读写内容到另一个文件。
```typescript
// pages/xxx.ets
import { fileIo as fs, ReadOptions, WriteOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
// 获取应用文件路径
let context = getContext(this) as common.UIAbilityContext;
let filesDir = context.filesDir;
function readWriteFile(): void {
// 打开文件
let srcFile = fs.openSync(filesDir + '/test.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let destFile = fs.openSync(filesDir + '/destFile.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
// 读取源文件内容并写入至目的文件
let bufSize = 4096;
let readSize = 0;
let buf = new ArrayBuffer(bufSize);
let readOptions: ReadOptions = {
offset: readSize,
length: bufSize
};
let readLen = fs.readSync(srcFile.fd, buf, readOptions);
while (readLen > 0) {
readSize += readLen;
let writeOptions: WriteOptions = {
length: readLen
};
fs.writeSync(destFile.fd, buf, writeOptions);
readOptions.offset = readSize;
readLen = fs.readSync(srcFile.fd, buf, readOptions);
}
// 关闭文件
fs.closeSync(srcFile);
fs.closeSync(destFile);
}
```
使用读写接口时，需注意可选项参数offset的设置。对于已存在且读写过的文件，文件偏移指针默认在上次读写操作的终止位置。
以流的形式读写文件
以下示例代码演示了如何使用流接口读取test.txt的文件内容并写入到destFile.txt文件中。
```typescript
// pages/xxx.ets
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
// 获取应用文件路径
let context = getContext(this) as common.UIAbilityContext;
let filesDir = context.filesDir;
async function readWriteFileWithStream(): Promise<void> {
// 创建并打开输入文件流
let inputStream = fs.createStreamSync(filesDir + '/test.txt', 'r+');
// 创建并打开输出文件流
let outputStream = fs.createStreamSync(filesDir + '/destFile.txt', "w+");
let bufSize = 4096;
let readSize = 0;
let buf = new ArrayBuffer(bufSize);
let readOptions: ReadOptions = {
offset: readSize,
length: bufSize
};
// 以流的形式读取源文件内容并写入到目标文件
let readLen = await inputStream.read(buf, readOptions);
readSize += readLen;
while (readLen > 0) {
const writeBuf = readLen < bufSize ? buf.slice(0, readLen) : buf;
await outputStream.write(writeBuf);
readOptions.offset = readSize;
readLen = await inputStream.read(buf, readOptions);
readSize += readLen;
}
// 关闭文件流
inputStream.closeSync();
outputStream.closeSync();
}
```
使用流接口时，需注意流的及时关闭。同时流的异步接口应严格遵循异步接口使用规范，避免同步、异步接口混用。流接口不支持并发读写。
查看文件列表
以下示例代码演示了如何查看文件列表。
```typescript
import { fileIo as fs, Filter, ListFileOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
// 获取应用文件路径
let context = getContext(this) as common.UIAbilityContext;
let filesDir = context.filesDir;
// 查看文件列表
function getListFile(): void {
let listFileOption: ListFileOptions = {
recursion: false,
listNum: 0,
filter: {
suffix: [".png", ".jpg", ".txt"],
displayName: ["test*"],
fileSizeOver: 0,
lastModifiedAfter: new Date(0).getTime()
}
};
let files = fs.listFileSync(filesDir, listFileOption);
for (let i = 0; i < files.length; i++) {
console.info(`The name of file: ${files[i]}`);
}
}
```
使用文件流
以下示例代码演示了如何使用文件可读流，文件可写流。
```typescript
// pages/xxx.ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
// 获取应用文件路径
let context = getContext(this) as common.UIAbilityContext;
let filesDir = context.filesDir;
function copyFileWithReadable(): void {
// 创建文件可读流
const rs = fs.createReadStream(`${filesDir}/read.txt`);
// 创建文件可写流
const ws = fs.createWriteStream(`${filesDir}/write.txt`);
// 暂停模式拷贝文件。在拷贝数据时，将原始数据暂停，然后将数据复制到另一个位置，适用于对数据完整性和一致性要求较高的场景
rs.on('readable', () => {
const data = rs.read();
if (!data) {
return;
}
ws.write(data);
});
}
function copyFileWithData(): void {
// 创建文件可读流
const rs = fs.createReadStream(`${filesDir}/read.txt`);
// 创建文件可写流
const ws = fs.createWriteStream(`${filesDir}/write.txt`);
// 流动模式拷贝文件。数据的读取和写入是同时进行的，不需要暂停原始数据的访问，适用于对数据实时性要求较高的场景
rs.on('data', (emitData) => {
const data = emitData?.data;
if (!data) {
return;
}
ws.write(data as Uint8Array);
});
}
```
使用文件哈希流
哈希流是一种数据传输和存储技术，可以将任意长度的数据转换为固定长度的哈希值来验证数据的完整性和一致性。以下代码演示了如何使用文件哈希处理接口（ohos.file.hash）来处理文件哈希流。
```typescript
// pages/xxx.ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { hash } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
// 获取应用文件路径
let context = getContext(this) as common.UIAbilityContext;
let filesDir = context.filesDir;
function hashFileWithStream() {
const filePath = `${filesDir}/test.txt`;
// 创建文件可读流
const rs = fs.createReadStream(filePath);
// 创建哈希流
const hs = hash.createHash('sha256');
rs.on('data', (emitData) => {
const data = emitData?.data;
hs.update(new Uint8Array(data?.split('').map((x: string) => x.charCodeAt(0))).buffer);
});
rs.on('close', async () => {
const hashResult = hs.digest();
const fileHash = await hash.hash(filePath, 'sha256');
console.info(`hashResult: ${hashResult}, fileHash: ${fileHash}`);
});
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/native-fileio-guidelines-V14
爬取时间: 2025-04-28 00:31:16
来源: Huawei Developer
场景介绍
FileIO模块提供了部分文件基础操作能力，其他能力请参考libc标准库/标准C++库。
基本概念
结果集：满足使用场景正确的 uri。
约束限制
进行文件操作之前，必须保证传入正确有效的uri或path。
接口说明
接口的详细说明，请参考FileIO。
| 接口名称 | 描述 |
| --- | --- |
| FileManagement_ErrCode OH_FileIO_GetFileLocation(char *uri, int uriLength, FileIO_FileLocation *location) | 获取文件存储位置。 |
| enum FileIO_FileLocation FileIO_FileLocation | 文件存储位置枚举值。 |
| enum enum FileManagement_ErrCode FileManagement_ErrCode | 文件管理模块错误码。 |
开发步骤
在CMake脚本中链接动态库
CMakeLists.txt中添加以下lib。
添加头文件
调用OH_FileIO_GetFileLocation接口获取文件存储位置。示例代码如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-fs-space-statistics-V14
爬取时间: 2025-04-28 00:31:29
来源: Huawei Developer
在系统中，可能出现系统空间不够或者cacheDir等目录受系统配额限制等情况，需要应用开发者关注系统剩余空间，同时控制应用自身占用的空间大小。
接口说明
API的详细介绍请参见ohos.file.statvfs、ohos.file.storageStatistics。
表1文件系统空间和应用空间统计
| 模块 | 接口名 | 功能 |
| --- | --- | --- |
| @ohos.file.storageStatistics | getCurrentBundleStats | 获取当前应用的存储空间大小（单位为Byte）。 |
| @ohos.file.statvfs | getFreeSize | 获取指定文件系统的剩余空间大小（单位为Byte）。 |
| @ohos.file.statvfs | getTotalSize | 获取指定文件系统的总空间大小（单位为Byte）。 |
表2应用空间统计
| BundleStats属性 | 含义 | 统计路径 |
| --- | --- | --- |
| appSize | 应用安装文件大小（单位为Byte） | 应用安装文件保存在以下目录： /data/storage/el1/bundle |
| cacheSize | 应用缓存文件大小（单位为Byte） | 应用的缓存文件保存在以下目录： /data/storage/el1/base/cache /data/storage/el1/base/haps/entry/cache /data/storage/el2/base/cache /data/storage/el2/base/haps/entry/cache |
| dataSize | 应用文件存储大小（除应用安装文件和缓存文件）（单位为Byte） | 应用文件由本地文件、分布式文件以及数据库文件组成。 本地文件保存在以下目录（注意缓存文件目录为以下目录的子目录）： /data/storage/el1/base /data/storage/el2/base 分布式文件保存在以下目录： /data/storage/el2/distributedfiles 数据库文件保存在以下目录： /data/storage/el1/database /data/storage/el2/database |
应用安装文件保存在以下目录：
/data/storage/el1/bundle
应用的缓存文件保存在以下目录：
/data/storage/el1/base/cache
/data/storage/el1/base/haps/entry/cache
/data/storage/el2/base/cache
/data/storage/el2/base/haps/entry/cache
应用文件由本地文件、分布式文件以及数据库文件组成。
本地文件保存在以下目录（注意缓存文件目录为以下目录的子目录）：
/data/storage/el1/base
/data/storage/el2/base
分布式文件保存在以下目录：
/data/storage/el2/distributedfiles
数据库文件保存在以下目录：
/data/storage/el1/database
/data/storage/el2/database
开发示例
-  获取文件系统数据分区剩余空间大小。
```typescript
import { statfs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
let context = getContext(this) as common.UIAbilityContext;
let path = context.filesDir;
statfs.getFreeSize(path, (err: BusinessError, number: number) => {
if (err) {
console.error(`Invoke getFreeSize failed, code is ${err.code}, message is ${err.message}`);
} else {
console.info(`Invoke getFreeSize succeeded, size is ${number}`);
}
});
```
-  获取当前应用的存储空间大小。
```typescript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getCurrentBundleStats((err: BusinessError, bundleStats: storageStatistics.BundleStats) => {
if (err) {
console.error(`Invoke getCurrentBundleStats failed, code is ${err.code}, message is ${err.message}`);
} else {
console.info(`Invoke getCurrentBundleStats succeeded, appsize is ${bundleStats.appSize}`);
}
});
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/share-app-file-V14
爬取时间: 2025-04-28 00:31:42
来源: Huawei Developer
应用文件分享是应用之间通过分享URI（Uniform Resource Identifier）或文件描述符FD（File Descriptor）的方式，进行文件共享的过程。
-  基于URI分享方式，应用可分享单个文件，通过ohos.app.ability.wantConstant的wantConstant.Flags接口以只读或读写权限授权给其他应用。应用可通过ohos.file.fs的fs.open打开URI，并进行读写操作。当前仅支持临时授权，分享给其他应用的文件在被分享应用退出时权限被收回。
-  基于FD分享方式，应用可分享单个文件，通过ohos.file.fs的open接口以指定权限授权给其他应用。应用从want中解析拿到FD后可通过ohos.file.fs的读写接口对文件进行读写。 由于FD分享的文件关闭FD后，无法再打开分享文件，因此不推荐使用，本文重点介绍基于URI分享文件给其他应用或使用其他应用分享的文件。
应用可分享目录
| 沙箱路径 | 物理路径 | 说明 |
| --- | --- | --- |
| /data/storage/el1/base | /data/app/el1/<currentUserId>/base/<PackageName> | 应用el1级别加密数据目录 |
| /data/storage/el2/base | /data/app/el2/<currentUserId>/base/<PackageName> | 应用el2级别加密数据目录 |
| /data/storage/el2/distributedfiles | /mnt/hmdfs/<currentUserId>/account/device_view/<networkId>/data/<PackageName> | 应用el2加密级别有账号分布式数据融合目录 |
文件URI规范
文件URI的格式为：
格式为file://<bundleName>/<path>
-  file：文件URI的标志。
-  bundleName：该文件资源的属主。
-  path：文件资源在应用沙箱中的路径。
分享文件给其他应用
在分享文件给其他应用前，开发者需要先获取应用文件路径。
1.  获取文件在应用沙箱中的路径，并转换为文件URI。
```typescript
import { UIAbility } from '@kit.AbilityKit';
import { fileUri } from '@kit.CoreFileKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage) {
// 获取文件的沙箱路径
let pathInSandbox = this.context.filesDir + "/test1.txt";
// 将沙箱路径转换为uri
let uri = fileUri.getUriFromPath(pathInSandbox);
// 获取的uri为"file://com.example.demo/data/storage/el2/base/files/test1.txt"
}
}
```
2.  设置获取文件的权限以及选择要分享的应用。 分享文件给其他应用需要使用startAbility接口，将获取到的URI填充在want的参数URI中，标注URI的文件类型，type字段可参考want属性，并通过设置want的flag来设置对应的读写权限，action字段配置为"ohos.want.action.sendData"表示进行应用文件分享，开发示例如下。 写权限分享时，同时授予读权限。
```typescript
import { fileUri } from '@kit.CoreFileKit';
import { window } from '@kit.ArkUI';
import { wantConstant } from '@kit.AbilityKit';
import { UIAbility } from '@kit.AbilityKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
export default class EntryAbility extends UIAbility {
onWindowStageCreate(windowStage: window.WindowStage) {
// 获取文件沙箱路径
let filePath = this.context.filesDir + '/test1.txt';
// 将沙箱路径转换为uri
let uri = fileUri.getUriFromPath(filePath);
let want: Want  = {
// 配置被分享文件的读写权限，例如对被分享应用进行读写授权
flags: wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION | wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
// 配置分享应用的隐式拉起规则
action: 'ohos.want.action.sendData',
uri: uri,
type: 'text/plain'
}
this.context.startAbility(want)
.then(() => {
console.info('Invoke getCurrentBundleStats succeeded.');
})
.catch((err: BusinessError) => {
console.error(`Invoke startAbility failed, code is ${err.code}, message is ${err.message}`);
});
}
// ...
}
```
图1效果示意图：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170406.90324351722834975279837030281841:50001231000000:2800:034FE34CEBC2A02AA4C3A384C503E07C94BF8C0292BB6917718F7351D096696B.png)
使用其他应用分享的文件
被分享应用需要在module.json5配置文件的actions标签的值配置为"ohos.want.action.sendData"，表示接收应用分享文件，配置uris字段，表示接收URI的类型，即只接收其他应用分享该类型的URI，如下表示本应用只接收scheme为file，类型为txt的文件，示例如下。
```json
{
"module": {
//...
"abilities": [
{
//...
"skills": [
{
//...
"actions": [
"ohos.want.action.sendData"
],
"uris": [
{
"scheme": "file",
"type": "text/plain"
}
]
}
]
}
]
}
}
```
被分享方的UIAbility被启动后，可以在其onCreate()或者onNewWant回调中获取传入的want参数信息。
通过接口want的参数获取分享文件的URI，获取文件URI后通过fs.open接口打开文件，获取对应的file对象后，可对文件进行读写操作。
```typescript
// xxx.ets
import { fileIo as fs } from '@kit.CoreFileKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
function getShareFile() {
try {
let want: Want = {}; // 此处实际使用时应该修改为获取到的分享方传递过来的want信息
// 从want信息中获取uri字段
let uri = want.uri;
if (uri == null || uri == undefined) {
console.info('uri is invalid');
return;
}
try {
// 根据需要对被分享文件的URI进行相应操作。例如读写的方式打开URI获取file对象
let file = fs.openSync(uri, fs.OpenMode.READ_WRITE);
console.info('open file successfully!');
} catch (err) {
let error: BusinessError = err as BusinessError;
console.error(`Invoke openSync failed, code is ${error.code}, message is ${error.message}`);
}
} catch (error) {
let err: BusinessError = error as BusinessError;
console.error(`Invoke openSync failed, code is ${err.code}, message is ${err.message}`);
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-file-backup-restore-V14
爬取时间: 2025-04-28 00:31:56
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-file-backup-overview-V14
爬取时间: 2025-04-28 00:32:09
来源: Huawei Developer
用户在使用应用的过程中，会产生对应的应用数据，如配置信息、业务数据等。为了保证用户数据不会因为应用升级、迁移等操作而丢失，应用需要接入数据备份恢复。
在开发前，需要先了解ExtensionAbility组件，建议参考ExtensionAbility组件概述。
BackupExtensionAbility是Stage模型中扩展组件ExtensionAbility的派生类，用于提供备份及恢复应用数据的能力。它是一种无界面的扩展组件，随着备份恢复任务的启动而运行，随着备份恢复任务的结束而退出。
不同应用所需实现的场景不同，分为：
-  应用接入数据备份恢复：应用均可以接入数据备份恢复，在接入后，应用可通过修改配置文件定制备份恢复框架的行为，包括是否允许备份恢复、备份哪些数据。 应用本身无法触发数据的备份和恢复，仅能进行备份恢复的配置。
-  应用触发数据备份恢复（仅对系统应用开放）

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-file-backup-extension-V14
爬取时间: 2025-04-28 00:32:22
来源: Huawei Developer
应用接入数据备份恢复需要通过BackupExtensionAbility实现。
BackupExtensionAbility，是Stage模型中扩展组件ExtensionAbility的派生类。开发者可以通过修改配置文件定制备份恢复框架的行为，包括是否允许备份恢复，备份哪些文件等。
接口说明
备份恢复扩展能力API的接口使用指导请参见BackupExtensionAbility API参考和BackupExtensionContext API参考。
约束与限制
开发步骤
1.  在应用配置文件module.json5中注册extensionAbilities相关配置 新增"extensionAbilities"字段，其中注册类型"type"设置为"backup"，元数据信息"metadata"新增一个"name"为"ohos. extension. backup"的条目。 BackupExtensionAbility配置文件示例：
```json
{
"extensionAbilities": [
{
"description": "$string:ServiceExtAbility",
"icon": "$media:icon",
"name": "BackupExtensionAbility",
"type": "backup",
"exported": false,
"metadata": [
{
"name": "ohos.extension.backup",
"resource": "$profile:backup_config"
}
],
// 在BackupExtension.ets文件里自定义继承BackupExtensionAbility，重写其中的onBackup/onBackupEx和
// onRestore/onRestoreEx方法，推荐使用onBackupEx/onRestoreEx。
// 如果没有特殊要求可以空实现，则备份恢复服务会按照统一的备份恢复数据规则进行备份恢复。
"srcEntry": "./ets/BackupExtension/BackupExtension.ets",
}
]
}
```
2.  新增元数据资源配置文件 在元数据资源配置文件中，定义备份恢复时需要传输的文件。元数据资源配置文件名称需要与module.json5中"metadata.resource"例如"backup_config.json"名称保持一致，其保存位置在工程的resources/base/profile文件夹下。 元数据资源配置文件示例：
```json
{
"allowToBackupRestore": true,
"includes": [
"/data/storage/el2/base/files/users/"
],
"excludes": [
"/data/storage/el2/base/files/users/hidden/"
],
"fullBackupOnly": false,
"restoreDeps": ""
}
```
3.  开发者可以在BackupExtension.ets文件中自定义类继承的BackupExtensionAbility，通过重写其onBackup/onBackupEx和onRestore/onRestoreEx方法，使其达到在备份预加工应用数据或者在恢复阶段加工待恢复文件。 如果没有特殊要求可以空实现，则备份恢复服务会按照统一的备份恢复数据规则进行备份恢复。 下面的示例展示了一个空实现的BackupExtension.ets文件：
```typescript
//onBackup && onRestore
import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
import {hilog} from '@kit.PerformanceAnalysisKit';
const TAG = `FileBackupExtensionAbility`;
export default class BackupExtension extends  BackupExtensionAbility {
//onBackup
async onBackup ()   {
hilog.info(0x0000, TAG, `onBackup ok`);
}
//onRestore
async onRestore (bundleVersion : BundleVersion) {
hilog.info(0x0000, TAG, `onRestore ok ${JSON.stringify(bundleVersion)}`);
hilog.info(0x0000, TAG, `onRestore end`);
}
}
```
元数据资源配置文件说明
| 属性名称 | 数据类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| allowToBackupRestore | 布尔值 | 是 | 是否允许备份恢复，默认为false。 |
| includes | 字符串数组 | 否 | 应用沙箱中需要备份的文件和目录。 当模式串以非/开始时，表示一个相对于根路径的相对路径。 includes支持的路径清单列表如下述代码段内容所示，当配置includes时请确保配置路径范围包含在其中。 当includes已配置时，备份恢复框架会采用开发者配置的模式串，否则将会采用下述代码段内容作为默认值。 |
| excludes | 字符串数组 | 否 | includes中无需备份的例外项。格式同includes。 在配置excludes时，请确保其范围在includes的子集中。 当excludes已配置时，备份恢复框架会采用开发者配置的模式串，否则将会采用空数组作为默认值。 |
| fullBackupOnly | 布尔值 | 否 | 是否使用应用默认恢复目录，默认值为false。当值为true时，恢复数据时会通过临时路径进行缓存，临时路径可通过backupDir获取。当值为false或者不配置该字段时，恢复数据会以'/'为根目录解压数据。 |
| restoreDeps | 字符串 | 否 | 不推荐使用，应用恢复时依赖其他应用数据，默认值为""，需要配置依赖应用名称。当前仅支持最多一个依赖项。配置的依赖仅在一次恢复任务上下文生效，如果一次恢复任务中没有检测到依赖应用，则忽略该依赖描述继续执行恢复任务。依赖应用未恢复或者恢复失败都会导致本应用恢复失败。 |
| extraInfo | json串 | 否 | 额外信息可通过该字段传递。 |
应用沙箱中需要备份的文件和目录。
当模式串以非/开始时，表示一个相对于根路径的相对路径。
includes支持的路径清单列表如下述代码段内容所示，当配置includes时请确保配置路径范围包含在其中。
当includes已配置时，备份恢复框架会采用开发者配置的模式串，否则将会采用下述代码段内容作为默认值。
includes中无需备份的例外项。格式同includes。
在配置excludes时，请确保其范围在includes的子集中。
当excludes已配置时，备份恢复框架会采用开发者配置的模式串，否则将会采用空数组作为默认值。
1、有关fullBackupOnly字段的说明
开发者可根据自身的业务场景，选择对应的恢复数据方式。
示例：
假设应用的数据备份路径为：data/storage/el2/base/files/A/。那么在恢复时，如果配置了fullBackupOnly为false，数据会被直接解压到：**/data/storage/el2/base/files/A/**目录下，如果配置了fullBackupOnly为true，数据则会被解压到：临时路径backupDir+ /restore/data/storage/el2/base/files/A/目录下。
includes支持的路径清单列表如下：
```json
{
"includes": [
"data/storage/el1/database/",
"data/storage/el1/base/files/",
"data/storage/el1/base/preferences/",
"data/storage/el1/base/haps/*/files/",
"data/storage/el1/base/haps/*/preferences/",
"data/storage/el2/database/",
"data/storage/el2/base/files/",
"data/storage/el2/base/preferences/",
"data/storage/el2/base/haps/*/files/",
"data/storage/el2/base/haps/*/preferences/",
"data/storage/el2/distributedfiles/",
"data/storage/el5/database/",
"data/storage/el5/base/files/",
"data/storage/el5/base/preferences/",
"data/storage/el5/base/haps/*/files/",
"data/storage/el5/base/haps/*/preferences/"
]
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-data-migration-guidelines-V14
爬取时间: 2025-04-28 00:32:35
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-data-migration-overview-V14
爬取时间: 2025-04-28 00:32:49
来源: Huawei Developer
使用场景
终端设备从HarmonyOS 3.1 Release API 9及之前版本（简称HarmonyOS）升级到HarmonyOS NEXT Developer Preview1及之后版本（简称HarmonyOS NEXT）时，原HarmonyOS中运行的APK应用，升级后需要切换为HarmonyOS NEXT中的HarmonyOS应用。APK应用的部分数据需要转换并迁移到指定位置后，才能被HarmonyOS应用访问。HarmonyOS NEXT提供了“数据迁移框架”和“备份恢复框架”，为开发者提供应用数据的迁移和转换能力。开发者完成适配，APK应用切换为HarmonyOS应用后，可继承原APK应用中适配HarmonyOS应用的数据。
如下图所示，应用需要的数据，包含云端服务器中的数据，本地应用沙箱中的数据和本地公共媒体库中的数据。为了应用的数据可以继承，开发者需要保证云端数据定义兼容APK应用和HarmonyOS应用，确保系统升级后同一账号下的数据可识别。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094249.08379527625680387814163958724588:50001231000000:2800:1BB07012090521AC980501C6DB3E488CBFA38DAD07FA46913FC2EC30EADF2F77.png)
数据迁移机制
应用沙箱数据迁移机制
终端设备从HarmonyOS升级到HarmonyOS NEXT后，APK应用沙箱数据被搬迁到中间目录。针对应用沙箱数据，HarmonyOS NEXT提供“数据迁移框架”统一调度应用数据迁移任务。
应用数据迁移任务需要执行的步骤包括：应用安装，数据迁移和数据恢复。
1.  在HarmonyOS应用安装完成之后，“数据迁移框架”将应用沙箱数据从中间目录搬迁到备份恢复目录。
后续HarmonyOS应用通过访问HarmonyOS应用沙箱获取应用的数据。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094249.72115830875499618429041826369486:50001231000000:2800:C7E2E5CED1016AE06969E7A012938F39322681FB3F61015656D9D6B18373EDEC.png)
公共媒体库中数据迁移机制
公共媒体库中的数据，在终端设备从HarmonyOS升级到HarmonyOS NEXT后，会整体搬迁直接继承。应用可以使用HarmonyOS NEXT提供的API，访问公共媒体库中的数据。媒体库的使用指导可以参考：媒体文件管理服务。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094249.65409584489072022938919788836519:50001231000000:2800:6140F7C2AE65ED3D63F3E0FAC289BBB0649F630D3C0D1250AB4362C955CBD0FB.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/adaptation-process-V14
爬取时间: 2025-04-28 00:33:02
来源: Huawei Developer
适配流程包括：适配准备、应用适配、开发者自验证、应用上架和端到端验证。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170406.61010316276377384630100279809959:50001231000000:2800:A67FACCC4516BB20DA841A2F004E1ECD26C783086BA943A9D656EF64CDE4C824.png)
适配准备阶段
在适配准备阶段，开发者需要分析清楚HarmonyOS中APK应用和HarmonyOS NEXT中HarmonyOS应用的数据范围和差异。
在开发之前，需要通过OTA升级的形式，将终端设备升级到HarmonyOS NEXT Developer Preview1及之后版本。
应用适配
在适配准备工作完成后，进入应用适配阶段。开发者需要在HarmonyOS应用的代码中，实现“BackupExtensionAbility”，使应用接入到“备份恢复框架”中，完成应用数据的转换和迁移。更多适配指导可参考：应用接入数据备份恢复。
应用的“BackupExtensionAbility”执行完后，“备份恢复框架”会清空备份恢复目录，开发者请在应用的“BackupExtensionAbility”执行结束前，完成所有所需数据的转换和迁移。
后续HarmonyOS应用通过访问HarmonyOS应用沙箱获取应用的数据。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170407.97076363414355029751473871240751:50001231000000:2800:349DA4E088DDB99B99D5E247E3B14162E4FD249A337CA0E6CD55825C9E7B0724.png)
备份恢复目录如下表中所示：
| 备份恢复目录  |
| --- |
| /data/storage/el1/base/.backup/restore/{APK包名}/de/  |
| /data/storage/el2/base/.backup/restore/{APK包名}/ce/  |
| /data/storage/el2/base/.backup/restore/{APK包名}/A/data/  |
| /data/storage/el2/base/.backup/restore/{APK包名}/A/obb/  |
备份恢复目录
/data/storage/el1/base/.backup/restore/{APK包名}/de/
/data/storage/el2/base/.backup/restore/{APK包名}/ce/
/data/storage/el2/base/.backup/restore/{APK包名}/A/data/
/data/storage/el2/base/.backup/restore/{APK包名}/A/obb/
HarmonyOS应用沙箱目录请参考应用沙箱目录。
开发者自验证
开发者完成应用适配后，需要完成自验证HarmonyOS应用数据迁移适配结果。更多自验证指导可参考：开发者自验证。
其中自验证所需“迁移调试”工具获取方式如下：
应用上架
HarmonyOS应用适配成功后，在进行端到端验证之前，需要将HarmonyOS应用上架到华为应用市场。HarmonyOS应用上架指导请参考：发布HarmonyOS应用指导。
HarmonyOS应用上架应用市场的时候，需要配置HarmonyOS应用和APK应用映射关系。HarmonyOS应用关联APK应用指导请参考：关联APK应用。
端到端验证
在HarmonyOS应用上架到华为应用市场之后，华为方技术支撑人员会为开发者推送回退版本。如果终端设备为HarmonyOS NEXT，开发者需要将终端设备回退到HarmonyOS，在HarmonyOS中使用APK应用生成数据。应用数据准备完成后，请通过OTA升级形式，将终端设备升级到华为方提供的HarmonyOS NEXT。验证HarmonyOS NEXT中的HarmonyOS应用是否成功继承原APK应用的数据。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-data-migration-adaptation-V14
爬取时间: 2025-04-28 00:33:17
来源: Huawei Developer
环境准备
开发者需要通过OTA升级的形式，将终端设备升级到HarmonyOS NEXT Developer Beta1及之后版本。
| 工具  | 版本  | 说明  |
| --- | --- | --- |
| “迁移调试”工具  | 205.0.0.115及之后版本  | 模拟验证数据迁移  |
| DevEco Studio  | DevEco Studio NEXT Developer Beta3及之后版本  | 请参考：DevEco Studio使用指南  |
| Compatible SDK  | 5.0.0(12)  | 请参考：版本说明  |
工具
版本
说明
“迁移调试”工具
205.0.0.115及之后版本
模拟验证数据迁移
DevEco Studio
DevEco Studio NEXT Developer Beta3及之后版本
请参考：DevEco Studio使用指南
Compatible SDK
5.0.0(12)
请参考：版本说明
应用数据迁移适配流程
创建新工程
本章节从创建新工程开始，指导开发者接入“备份恢复框架”，已经创建工程的开发者可以跳过本节。
BackupExtensionAbility的实现
开发者可以在BackupExtension.ts文件中自定义类继承BackupExtensionAbility，通过重写其中的onBackup和onRestore方法，自定义应用数据的转换和迁移。终端设备从HarmonyOS升级到HarmonyOS NEXT数据迁移场景中，onRestore回调接口中的参数bundleVersion.name的前缀为“0.0.0.0”。
onRestore 接口是同步接口，其内部所有的异步操作请进行同步等待。
以下步骤以空工程为例，介绍如何实现BackupExtensionAbility：
1.
2.
3.  1、单个应用设定的最长数据迁移时间为十五分钟，超过十五分钟还未完成应用数据迁移的应用，应用数据迁移会失败。 2、应用的“BackupExtensionAbility”执行完后，“备份恢复框架”会清空备份恢复目录，开发者请在应用的“BackupExtensionAbility”执行结束前，完成所有所需数据的转换和迁移。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170407.35004955207411697019781512076974:50001231000000:2800:EAE0D8DA57E3922EF3F4A2C332F6F774748D38059C3043FEF628A41D43AC3821.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170407.39124623673373786823618957236488:50001231000000:2800:8E39E3AA75F830FB14C71B1CD0655C08FA2132D70ED8B30C5E7558B8E534D71F.png)
元数据资源配置文件适配
开发者通过元数据资源配置文件backup_config.json，启用备份恢复，并定义备份恢复框架需要传输的文件。
以下步骤以空工程为例，介绍如何配置元数据资源文件：
1.
2.
module.json5适配
开发者需要在应用配置文件module.json5中进行注册，其中注册类型type需要设置为backup，元数据信息metadata需要新增一个name为ohos.extension.backup的条目。
extensionAbilities需要配置在entry内的module.json5才能正常访问。
以下步骤以空工程为例，介绍如何配置module.json5文件：
1.
APK应用沙箱目录与备份恢复目录映射关系
APK应用沙箱目录与备份恢复目录映射关系见下表中所示：
| APK应用沙箱目录  | 备份恢复目录示例  | 备份恢复目录获取方式  |
| --- | --- | --- |
| /data/user_de/{userId}/{APK包名}/  | /data/storage/el1/base/.backup/restore/{APK包名}/de/  | this.context.area = contextConstant.AreaMode.EL1; let deSourcePath = this.context.backupDir + "restore/{APK包名}/de/"  |
| /data/user/{userId}/{APK包名}/  | /data/storage/el2/base/.backup/restore/{APK包名}/ce/  | this.context.area = contextConstant.AreaMode.EL2; let ceSourcePath = this.context.backupDir + "restore/{APK包名}/ce/"  |
| /data/media/{userId}/Android/data/{APK包名}/  | /data/storage/el2/base/.backup/restore/{APK包名}/A/data/  | this.context.area = contextConstant.AreaMode.EL2; let dataSourcePath = this.context.backupDir + "restore/{APK包名}/A/data/"  |
| /data/media/{userId}/Android/obb/{APK包名}/  | /data/storage/el2/base/.backup/restore/{APK包名}/A/obb/  | this.context.area = contextConstant.AreaMode.EL2; let obbSourcePath = this.context.backupDir + "restore/{APK包名}/A/obb/"  |
APK应用沙箱目录
备份恢复目录示例
备份恢复目录获取方式
/data/user_de/{userId}/{APK包名}/
/data/storage/el1/base/.backup/restore/{APK包名}/de/
this.context.area = contextConstant.AreaMode.EL1;
let deSourcePath = this.context.backupDir + "restore/{APK包名}/de/"
/data/user/{userId}/{APK包名}/
/data/storage/el2/base/.backup/restore/{APK包名}/ce/
this.context.area = contextConstant.AreaMode.EL2;
let ceSourcePath = this.context.backupDir + "restore/{APK包名}/ce/"
/data/media/{userId}/Android/data/{APK包名}/
/data/storage/el2/base/.backup/restore/{APK包名}/A/data/
this.context.area = contextConstant.AreaMode.EL2;
let dataSourcePath = this.context.backupDir + "restore/{APK包名}/A/data/"
/data/media/{userId}/Android/obb/{APK包名}/
/data/storage/el2/base/.backup/restore/{APK包名}/A/obb/
this.context.area = contextConstant.AreaMode.EL2;
let obbSourcePath = this.context.backupDir + "restore/{APK包名}/A/obb/"

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-data-migration-verification-V14
爬取时间: 2025-04-28 00:33:30
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/self-verification-V14
爬取时间: 2025-04-28 00:33:44
来源: Huawei Developer
简介
在开发的过程中，当开发者完成所需适配流程后，可导入提前准备好的APK应用沙箱数据，自验证HarmonyOS应用数据迁移适配结果。
在HarmonyOS应用适配完成并上架到华为应用市场之后，开发者仍需要将终端设备从HarmonyOS升级到HarmonyOS NEXT，端到端验证应用数据迁移结果。
开发者自验证流程
应用沙箱数据准备
| APK应用沙箱目录  | {APK包名}.zip目录  |
| --- | --- |
| /data/user_de/{userId}/{APK包名}/  | {APK包名}/de  |
| /data/user/{userId}/{APK包名}/  | {APK包名}/ce  |
| /data/media/{userId}/Android/data/{APK包名}/  | {APK包名}/A/data  |
| /data/media/{userId}/Android/obb/{APK包名}/  | {APK包名}/A/obb  |
APK应用沙箱目录
{APK包名}.zip目录
/data/user_de/{userId}/{APK包名}/
{APK包名}/de
/data/user/{userId}/{APK包名}/
{APK包名}/ce
/data/media/{userId}/Android/data/{APK包名}/
{APK包名}/A/data
/data/media/{userId}/Android/obb/{APK包名}/
{APK包名}/A/obb
打包好的“{APK包名}.zip”解压后，要满足包含一个“APK包名”根目录，根目录下包含对应沙箱目录文件夹，文件结构如下。
1.  当前终端设备支持识别NTFS格式的外部存储设备，请使用NTFS格式的外部存储设备连接终端设备。
2.
3.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170407.66074091973975406270025395154304:50001231000000:2800:8E23C4306B3CF97719B1204C77A06534F67CEA829003F00F8F5FF4A89C559B3C.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170407.05850437903065360311750351965359:50001231000000:2800:D3DB7A76B89137D7499CADBF3F82775F01170646E72D5436E23F66956D7BFD19.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170408.96565459963800786094184152986906:50001231000000:2800:38E5434439287529016E0E535E958ED4EB6FD878CBF153CE2BD30F46054A2112.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170408.61313994780483020230052778569720:50001231000000:2800:764C1E547577858F97517F6CD2618B7DC0DB0CD150E3BEFB718F550C792BCD2B.png)
HarmonyOS NEXT上模拟验证应用数据迁移
在应用沙箱数据准备好之后，开发者需要先完成所需适配流程，再模拟验证应用数据迁移。
1.  “迁移调试”工具“205.0.0.110”之前的版本，仅支持调试release签名的应用。 从“205.0.0.110”版本开始，“迁移调试”工具仅支持调试debug签名的应用。请开发者升级到最新版本，并使用debug签名的包验证。 “迁移调试”工具版本查看方式：设置>应用和元服务>MigrateTool>版本
2.
3.
4.
5.
6.
7.
8.
9.  1、此处的数据迁移成功，仅表示“备份恢复框架”接入成功，APK应用的数据成功迁移到“备份恢复框架”需要的指定目录。开发者需要通过从应用的沙箱中获取数据并解析，判断应用适配“备份恢复框架”的结果。 2、单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，会导致任务执行失败。开发者需要优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。
10.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170408.81850401689002848845599376555576:50001231000000:2800:31FB2FC5DA2846B5F0AEF7352AA91CE1037CDE076A12967A0361DF1E96B68DAD.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170408.36471581871075741462227767088302:50001231000000:2800:B05E55DD319DCDAE5E0CD32B88BBE9A00C594EC1C3BA58B7D8BB7B9DC7CFD4C8.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170408.64203884557770879139562532226480:50001231000000:2800:F82A190E1BC6087FFD32D755DB63D9868526A0F32EC92FEDBD0356B712990F5C.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170409.07861517128766524401379834905495:50001231000000:2800:79A59FC361F38F4500DA8101A7C3FAC530EA6BC498B3D991328AB775C563AF1F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170409.89578078553738877359205173388724:50001231000000:2800:C25050F19B240C5C6D47CA56E7BE471EF3091A2E6465434D6D1015BE1ED158A7.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170409.58206986127011595591928014221193:50001231000000:2800:08F994A247E7A20B3602FDEF2511D70A3AEA40EE86BEB06D951075722624AFCC.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170409.64098193508151507141636374480318:50001231000000:2800:6C4DEBF451F5C7025D39B10F14CCF3ABFD55CD45F6432C680CF62C5529C11CC0.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170409.82015694776084534347975034830367:50001231000000:2800:AF5D9344F8BD10ED55243DBE2C4885EE41B3FF4DE57A9BACECAB16C9AA2D569E.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170410.76332063348922536947661620315901:50001231000000:2800:86A56B5307D8EC6558CCE34A28AEC91ACECE91BC3A79181BD9552C8A432F0FA7.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170410.73839497751566034644838507590871:50001231000000:2800:2275BF3611DE86C4B80045FA53C6DCA1C13D299F5A3208253D42C3A3F2ED1B50.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170410.09106181737930173064242473788176:50001231000000:2800:A9AFDAD2F9221FFE16E3C4B0D0251576139DF76DE0D06D06F13A66637096D60E.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170410.92248030032336822085174101399696:50001231000000:2800:45462224C73EAF0FD87BE13B45D5654477473652E1B81ABE9DEEC0174E4804CE.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170411.28022335607746276654958849568838:50001231000000:2800:A618B1B05DBFFF1F35656B73A30620BFBD33E914F8C94CE139B38C4CD2089760.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170411.63797792192211935304432074792487:50001231000000:2800:A91B6B41B792DDD095DA282F7E6858C4709D48CCFD0DE8C4A2CD7D8CA4570CDA.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/e2e-verification-V14
爬取时间: 2025-04-28 00:33:57
来源: Huawei Developer
应用适配完成并上架到华为应用市场之后，开发者需要模拟终端用户将终端设备从HarmonyOS升级到HarmonyOS NEXT的场景，端到端验证应用数据迁移结果。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-data-migration-faqs-V14
爬取时间: 2025-04-28 00:34:10
来源: Huawei Developer
无法获取已安装HarmonyOS应用列表
问题现象
单击“请选择HarmonyOS应用包名”按钮，已安装HarmonyOS应用列表未显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170411.19010372704470622877827964561870:50001231000000:2800:79F3AA434401B9201024396A9038E2DA07B9AE866464D4AA8141691EC6E1ED0E.png)
可能原因
迁移调试应用需要读取已安装应用列表的权限，在首次使用该工具时，单击了“禁止”按钮，迁移调试应用没有访问已安装HarmonyOS应用列表的权限。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170411.26664780681622976166197336475270:50001231000000:2800:833C3CF38CCC9EBD5FC9D2A7878D3BF28387668FB26989668C20B49AF7B1E5C3.png)
解决方法
将终端设备恢复出厂设置。首次使用迁移调试应用时，单击“允许”按钮，授予迁移调试应用读取已安装应用列表的权限。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170411.25361936154852746967093332572289:50001231000000:2800:A4341F778DD69EE6B3BE3AC31FACF7909A50ECDF18B4D68E436A86236F26D678.png)
应用数据迁移暂停
问题现象
在数据优化界面，应用数据迁移暂停。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170411.38126574280192602910884496031363:50001231000000:2800:DB342D847B73E4A8A8CDC144F10A272BC1D561E69A04038B5968CF5830FB3286.png)
可能原因
应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。
解决方法
单击“去桌面”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170412.11117131290962610163104908071472:50001231000000:2800:3C6DC05F8A67B8C00F7F1180451F3CE4D42A2BB93640AF11625B274A711EB1F3.png)
应用数据迁移执行十五分钟后失败
问题现象
应用数据迁移执行十五分钟后显示失败。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170412.16163231576022468144920587306521:50001231000000:2800:155B517D9263F8D2737E8FD27C21A4C2DC9A9077F5EA9D1FD2498D393F438557.png)
可能原因
单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，任务执行失败。
解决方法
请优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。
已接入“数据迁移框架”的应用完成数据迁移后，才可以被消费者使用。尽可能快的完成应用数据迁移，可以带给消费者更好的体验。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/code-precautions-V14
爬取时间: 2025-04-28 00:34:24
来源: Huawei Developer
区分升级场景和克隆场景
开发者需要区分升级场景和克隆场景时，可以重写BackupExtensionAbility中的onRestoreEx方法，通过restoreInfo预留字段进行场景区分。onRestoreEx方法详细使用指导请参考：BackupExtensionAbility API参考。
```typescript
import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
const TAG = `BackupExtensionAbility`;
interface ErrorInfo {
type: string,
errorCode: number,
errorInfo: string
}
interface DetailInfo {
type: string,
detail: string
}
export default class EntryBackupAbility extends BackupExtensionAbility {
async onBackup() {
console.log(TAG, 'onBackup ok');
}
async onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): Promise<string> {
console.log(TAG, `onRestoreEx ok ${JSON.stringify(bundleVersion)}`);
let errorInfo: ErrorInfo = {
type: "ErrorInfo",
errorCode: 0,
errorInfo: "app diy error info"
}
if (bundleVersion.name.startsWith("0.0.0.0")){
// 在此处实现终端设备从HarmonyOS 4.x到HarmonyOS NEXT的应用数据处理。
// 涉及异步操作请进行同步等待
console.log(TAG, `HarmonyOS to HarmonyOS NEXT scenario`);
// 如果升级场景与克隆场景没有差异化数据处理诉求，此处可以忽略。
if (this.IsOtaScenario(restoreInfo)) {
// 在此处实现终端设备从HarmonyOS 4.x到HarmonyOS NEXT升级场景的特有数据处理。无特殊要求，此处可以忽略。
console.log(TAG, `Ota Scenario`)
} else {
// 在此处实现终端设备从HarmonyOS 4.x到HarmonyOS NEXT克隆场景的特有数据处理。无特殊要求，此处可以忽略。
console.log(TAG, `Clone Scenario`)
}
} else {
// 在此处实现从HarmonyOS NEXT设备迁移到HarmonyOS NEXT设备后，应用数据的处理。无特殊要求，可以空实现。
// 涉及异步操作请进行同步等待
console.log(TAG, `Other scenario`);
}
return JSON.stringify(errorInfo);
}
/**
* 判断是否是升级场景
* @param restoreInfo 预留字段，应用恢复过程中需要的扩展参数
* @returns 升级场景返回true，否则返回false
*/
IsOtaScenario(restoreInfo: string): boolean {
let details:Array<DetailInfo> = JSON.parse(restoreInfo);
return details.some((detailInfo) => {
//设备从HarmonyOS 4.x升级到HarmonyOS NEXT/5.0.x场景判断条件
return detailInfo.type == 'isSameDevice' && detailInfo.detail == 'true';
});
}
}
```
公共目录文件uri继承
场景说明
应用在HarmonyOS 3.1 Release API 9及更低版本运行时，开发者可通过记录公共媒体库中文件的uri或者路径，用于后续的文件访问。 当终端设备从HarmonyOS升级到HarmonyOS NEXT后，公共媒体库中的文件会由系统整体搬迁至新位置，直接继承。导致应用记录的旧有uri或者路径不可使用。
为解决该问题，系统提供数据迁移公共目录文件继承方案，支持应用将记录的HarmonyOS公共媒体库文件uri或者路径转换为对应的HarmonyOS NEXT公共媒体库文件uri或者路径，并且返回对应文件类型。当应用需要在HarmonyOS NEXT中访问公共媒体库中的文件时，可以使用转换后的HarmonyOS NEXT公共媒体库文件uri或者路径，通过HarmonyOS NEXT提供的公共媒体库API进行授权访问。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170412.44230680905611395971688803442466:50001231000000:2800:48E6CB263B553E9F882FE97428EAB4AA4968B3567394FA9534EF8FC79CD6701F.png)
代码实现
应用可以调用Scenario Fusion Kit的接口convertFileUris()，将记录的HarmonyOS公共媒体库文件uri或者路径转换为HarmonyOS NEXT可访问的uri或者路径，并获取到对应文件类型。其中媒体文件类型请参考继承媒体文件访问权限，其他类型文件可通过基础文件接口进行操作。
开发者可以在数据迁移的过程中，通过该接口将HarmonyOS公共媒体库文件uri或者路径转换为对应的HarmonyOS NEXT公共媒体库文件uri或者路径，并重新保存，便于后续使用。
```typescript
import { fileUriService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
let sourceFileUris: Array<string> =
['100','content://media/external/files/10', '/storage/emulated/0/Pictures/test.gif',
'/storage/emulated/0/Android/media/com.test/test.mp4'];
fileUriService.convertFileUris(sourceFileUris).then(result => {
hilog.info(0x0000, 'testTag', 'succeeded in converting file uris');
result.forEach(data => {
let sourceUri: string = data.sourceUri;
let targetUri: string = data.targetUri;
let targetType: fileUriService.TargetType = data.targetType;
})
}).catch((error: BusinessError) => {
hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
});
} catch (error) {
hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/user-files-V14
爬取时间: 2025-04-28 00:34:37
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/user-file-overview-V14
爬取时间: 2025-04-28 00:34:50
来源: Huawei Developer
用户文件：登录到该终端设备的用户所拥有的文件，包括用户私有的图片、视频、音频、文档等。
1.  用户文件存放在用户目录下，归属于该设备上登录的用户。
2.  用户文件存储位置主要分为内置存储、外置存储。
3.  应用对用户文件的创建、访问、删除等行为，需要提前获取用户授权，或由用户操作完成。
用户文件存储位置
内置存储
内置存储，是指用户文件存储在终端设备的内部存储设备（空间）上。内置存储设备无法被移除。内置存储的用户文件主要有：
-  用户特有的文件：这部分文件归属于登录该设备的用户，不同用户登录后，仅可看到该用户自己的文件。 按照这些文件的特征/属性，以及用户/应用的使用习惯，可分为： 图片/视频类媒体文件 所具有的特征包括拍摄时间、地点、旋转角度、文件宽高等信息，以媒体文件的形式存储在系统中，通常是以所有文件、相册的形式对外呈现，不会展示其在系统中存储的具体位置。 音频类媒体文件 所具有的特征包括所属专辑、音频创作者、持续时间等信息，以媒体文件的形式存储在系统中，通常会以所有文件、专辑、作家等形式对外部呈现，不会展示其在系统中存储的具体位置。 其他文件（统称为文档类文件） 以普通文件的形式存储在系统中，该类文件既包括普通的文本文件、压缩文件等，又包括以普通文件形式存储的图片/视频、音频文件，该类文件通常是以目录树的形式对外展示。
-  图片/视频类媒体文件 所具有的特征包括拍摄时间、地点、旋转角度、文件宽高等信息，以媒体文件的形式存储在系统中，通常是以所有文件、相册的形式对外呈现，不会展示其在系统中存储的具体位置。
-  音频类媒体文件 所具有的特征包括所属专辑、音频创作者、持续时间等信息，以媒体文件的形式存储在系统中，通常会以所有文件、专辑、作家等形式对外部呈现，不会展示其在系统中存储的具体位置。
-  其他文件（统称为文档类文件） 以普通文件的形式存储在系统中，该类文件既包括普通的文本文件、压缩文件等，又包括以普通文件形式存储的图片/视频、音频文件，该类文件通常是以目录树的形式对外展示。
-  多用户共享的文件：用户可以通过将文件放在共享文件区，实现多个用户之间文件的共享访问。 共享文件区的文件，也是以普通文件的形式存储在系统中，以目录树的形式对外展示。
-  图片/视频类媒体文件 所具有的特征包括拍摄时间、地点、旋转角度、文件宽高等信息，以媒体文件的形式存储在系统中，通常是以所有文件、相册的形式对外呈现，不会展示其在系统中存储的具体位置。
-  音频类媒体文件 所具有的特征包括所属专辑、音频创作者、持续时间等信息，以媒体文件的形式存储在系统中，通常会以所有文件、专辑、作家等形式对外部呈现，不会展示其在系统中存储的具体位置。
-  其他文件（统称为文档类文件） 以普通文件的形式存储在系统中，该类文件既包括普通的文本文件、压缩文件等，又包括以普通文件形式存储的图片/视频、音频文件，该类文件通常是以目录树的形式对外展示。
外置存储
外置存储，是指用户文件存储在外置可插拔设备上（如SD卡、U盘等）。外置存储设备上的文件，和内置存储设备共享区文件一样，可以被所有登录到系统中的用户看到。
外置存储设备具备可插拔属性，因此系统提供了设备插拔事件的监听及挂载功能，用于管理外置存储设备，该部分功能仅对系统应用开放。
外置存储设备上的文件，全部以普通文件的形式呈现，和内置存储设备上的文档类文件一样，采用目录树的形式对外展示。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/user-file-uri-intro-V14
爬取时间: 2025-04-28 00:35:04
来源: Huawei Developer
用户文件uri是文件的唯一标识，在对用户文件进行访问与修改等操作时往往都会使用到uri，不建议开发者解析uri中的片段用于业务代码开发，不同类型的uri使用方式将在下文详细介绍。
uri的类型
uri类型可以归纳为文档类uri和媒体文件uri两类
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170412.55650270202042765718723221788948:50001231000000:2800:BF9BED4979841FB9DD3E48B0FC63F516EA41EB981B8C1E97423AF00532F8AACA.png)
文档类uri
文档类uri介绍
文档类uri的格式类型为：
'file://docs/storage/Users/currentUser/<relative_path>/test.txt'
其中各个字段表示的含义为：
| uri字段 | 说明 |
| --- | --- |
| 'file://docs/storage/Users/currentUser/' | 文件管理器的根目录。 |
| '<relative_path>/' | 文件在根目录下的相对路径。例如：'Download/'和'Documents/'。 |
| 'test.txt' | 用户文件系统中存储的文件名，支持的文件类型为文件管理器支持的所有类型，以文件管理器为准。例如txt、jpg、mp4和mp3等格式的文件。 |
文档类uri获取方式
1.  通过DocumentViewPicker接口选择或保存文件，返回选择或保存的文件uri。
2.  通过AudioViewPicker接口选择或保存文件，返回选择或保存的文件uri。
文档类uri的使用方式
normal等级的应用使用此类uri的方式只能通过fs模块进行进一步处理，其他模块使用此uri是会报没有权限的错误。示例代码参见picker中的选择文档类文件和保存文档类文件。
媒体文件uri
媒体文件uri介绍
媒体文件uri的格式类型为：
图片uri格式：
视频uri格式：
音频uri格式：
其中各个字段表示的含义为：
| uri字段 | 说明 |
| --- | --- |
| 'file://media' | 表示这个uri是媒体文件。 |
| 'Photo' | Photo表示这个uri是媒体文件中的图片或者视频类文件。 |
| 'Audio' | 表示这个uri是媒体文件中的音频类文件。 |
| '<id>' | 表示在数据库中多个表中处理后的值，并不是指表中的file_id列，注意请不要使用此id去数据库中查询具体文件。 |
| 'IMG_datetime_0001' | 表示图片文件在用户文件系统中存储的文件名去掉后缀剩下的部分。 |
| 'VID_datetime_0001' | 表示视频文件在用户文件系统中存储的文件名去掉后缀剩下的部分。 |
| 'AUD_datetime_0001' | 表示音频文件在用户文件系统中存储的文件名去掉后缀剩下的部分。 |
媒体文件uri获取方式
1.  通过PhotoAccessHelper的PhotoViewPicker选择媒体文件，返回选择的媒体文件文件的uri。
2.  通过photoAccessHelper模块中的getAssets或createAsset接口获取媒体文件对应文件的uri。
媒体文件uri的使用方式
normal等级的应用使用此类uri可以通过photoAccessHelper模块进行进一步处理。示例代码参见媒体资源使用指导中的指定URI获取图片或视频资源。此接口需要申请相册管理模块读权限'ohos.permission.READ_IMAGEVIDEO'，在使用中需要注意应用是否有此权限。
若normal等级的应用不想申请权限也可以通过临时授权的方式使用PhotoAccessHelper的PhotoViewPicker得到的uri使用photoAccessHelper.getAssets接口获取对应uri的PhotoAsset对象。这种方式获取的对象可以调用getThumbnail获取缩略图和使用get接口读取PhotoKeys中的部分信息。
以下为PhotoKeys中支持临时授权方式可以读取的信息：
| 名称 | 值 | 说明 |
| --- | --- | --- |
| URI | 'uri' | 文件uri。 |
| PHOTO_TYPE | 'media_type' | 媒体文件类型。 |
| DISPLAY_NAME | 'display_name' | 显示名字。 |
| SIZE | 'size' | 文件大小。 |
| DATE_ADDED | 'date_added' | 文件创建时的Unix时间戳（单位：秒）。 |
| DATE_MODIFIED | 'date_modified' | 文件修改时的Unix时间戳（单位：秒）。修改文件名不会改变此值，当文件内容发生修改时才会更新。 |
| DURATION | 'duration' | 持续时间（单位：毫秒）。 |
| WIDTH | 'width' | 图片宽度（单位：像素）。 |
| HEIGHT | 'height' | 图片高度（单位：像素）。 |
| DATE_TAKEN | 'date_taken' | 拍摄时的Unix时间戳（单位：秒）。 |
| ORIENTATION | 'orientation' | 图片文件的方向。 |
| TITLE | 'title' | 文件标题。 |
下面为通过临时授权方式使用媒体文件uri进行获取缩略图和读取文件部分信息的示例代码：
```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { dataSharePredicates } from '@kit.ArkData';
// 定义一个uri数组，用于接收PhotoViewPicker选择图片返回的uri
let uris: Array<string> = [];
const context = getContext(this);
// 调用PhotoViewPicker.select选择图片
async function photoPickerGetUri() {
try {
let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
PhotoSelectOptions.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
uris = PhotoSelectResult.photoUris;
}).catch((err: BusinessError) => {
console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
});
} catch (error) {
let err: BusinessError = error as BusinessError;
console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
}
}
async function uriGetAssets() {
try {
let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
// 配置查询条件，使用PhotoViewPicker选择图片返回的uri进行查询
predicates.equalTo('uri', uris[0]);
let fetchOption: photoAccessHelper.FetchOptions = {
fetchColumns: [photoAccessHelper.PhotoKeys.WIDTH, photoAccessHelper.PhotoKeys.HEIGHT, photoAccessHelper.PhotoKeys.TITLE, photoAccessHelper.PhotoKeys.DURATION],
predicates: predicates
};
let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
// 得到uri对应的PhotoAsset对象，读取文件的部分信息
const asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
console.info('asset displayName: ', asset.displayName);
console.info('asset uri: ', asset.uri);
console.info('asset photoType: ', asset.photoType);
console.info('asset width: ', asset.get(photoAccessHelper.PhotoKeys.WIDTH));
console.info('asset height: ', asset.get(photoAccessHelper.PhotoKeys.HEIGHT));
console.info('asset title: ' + asset.get(photoAccessHelper.PhotoKeys.TITLE));
// 获取缩略图
asset.getThumbnail((err, pixelMap) => {
if (err == undefined) {
console.info('getThumbnail successful ' + JSON.stringify(pixelMap));
} else {
console.error('getThumbnail fail', err);
}
});
} catch (error){
console.error('uriGetAssets failed with err: ' + JSON.stringify(error));
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/native-fileuri-guidelines-V14
爬取时间: 2025-04-28 00:35:17
来源: Huawei Developer
场景介绍
FileUri提供了关于文件uri的基本操作，将uri转换成对应的沙箱路径path、将应用沙箱路径path转换成对应应用自己的uri、获取uri所在目录路径的uri等接口能力，方便应用对文件分享业务中uri的访问。
基本概念
结果集：满足使用场景正确的路径或者uri。
约束限制
-  uri转path时，uri来源建议使用系统能力获取，例如：picker、剪切板、拖拽、及系统提供的path转uri接口等系统能力返回的uri；如果转换应用或用户拼接的uri，则转换后的path可能无法访问。
-  为保证数据的准确性，在转换或者判断过程中只允许处理一个对象。
接口说明
接口的详细说明，请参考API参考
| 接口名称 | 描述 |
| --- | --- |
| FileManagement_ErrCode OH_FileUri_GetUriFromPath(const char *path, unsigned int length, char **result) | 通过传入的路径path生成应用自己的uri(不支持媒体类型uri的获取)；将path转uri时，路径中的中文及非数字字母的特殊字符将会被编译成对应的ASCII码，拼接在uri中。 |
| FileManagement_ErrCode OH_FileUri_GetPathFromUri(const char *uri, unsigned int length, char **result) | 将uri转换成对应的沙箱路径path。 1、uri转path过程中会将uri中存在的ASCII码进行解码后拼接在原处，非系统接口生成的uri中可能存在ASCII码解析范围之外的字符，导致字符串无法正常拼接；2、转换处理为系统约定的字符串替换规则（规则随系统演进可能会发生变化），转换过程中不进行路径校验操作，无法保证转换结果的一定可以访问。 |
| FileManagement_ErrCode OH_FileUri_GetFullDirectoryUri(const char *uri, unsigned int length, char **result) | 获取所在路径uri。uri指向文件则返回所在路径的uri，uri指向目录则不处理直接返回原串；uri指向的文件不存在或属性获取失败则返回空串。 |
| bool OH_FileUri_IsValidUri(const char *uri, unsigned int length) | 判断传入的uri的格式是否正确。仅校验uri是否满足系统定义的格式规范，不校验uri的有效性。 |
| FileManagement_ErrCode OH_FileUri_GetFileName(const char *uri, unsigned int length, char **result) | 通过传入的uri获取到对应的文件名称。（如果文件名中存在ASCII码将会被解码处理后拼接在原处）。 |
开发步骤
在CMake脚本中链接动态库
CMakeLists.txt中添加以下lib。
添加头文件
1.  调用OH_FileUri_GetUriFromPath接口，在接口中malloc的内存需要在使用完后释放，因此需要free对应的内存。示例代码如下所示：
2.  调用OH_FileUri_GetPathFromUri通过URi转成对应的path，在接口中malloc的内存需要在使用完后释放，因此需要free对应的内存。示例代码如下所示：
3.  调用OH_FileUri_GetFullDirectoryUri获取uri所在路径的uri，在接口中malloc的内存需要在使用完后释放，因此需要free对应的内存。示例代码如下所示：
4.  可以调用OH_FileUri_IsValidUri接口进行uri格式验证。 示例代码如下所示：
5.  调用OH_FileUri_GetFileName获取uri中的文件名称，在接口中malloc的内存需要在使用完后释放，因此需要free对应的内存。示例代码如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/native-environment-guidelines-V14
爬取时间: 2025-04-28 00:35:31
来源: Huawei Developer
场景介绍
Environment提供了获取公共文件用户目录路径的能力，以支持三方应用在公共文件用户目录下进行文件访问操作。
约束限制
接口说明
接口的详细说明，请参考API参考
| 接口名称 | 描述 |
| --- | --- |
| FileManagement_ErrCode OH_Environment_GetUserDownloadDir (char **result) | 获取用户Download目录沙箱路径。只支持2in1设备 |
| FileManagement_ErrCode OH_Environment_GetUserDesktopDir (char **result) | 获取用户Desktop目录沙箱路径。只支持2in1设备 |
| FileManagement_ErrCode OH_Environment_GetUserDocumentDir (char **result) | 获取用户Document目录沙箱路径。只支持2in1设备 |
开发步骤
在CMake脚本中链接动态库
CMakeLists.txt中添加以下lib。
添加头文件
1.  调用OH_Environment_GetUserDownloadDir接口获取用户Download目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：
2.  调用OH_Environment_GetUserDesktopDir接口获取用户Desktop目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：
3.  调用OH_Environment_GetUserDocumentDir接口获取用户Document目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/select-save-user-file-V14
爬取时间: 2025-04-28 00:35:44
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/select-user-file-V14
爬取时间: 2025-04-28 00:35:57
来源: Huawei Developer
用户需要分享文件、保存图片、视频等用户文件时，开发者可以通过系统预置的文件选择器（FilePicker），实现该能力。通过Picker访问相关文件，将拉起对应的应用，引导用户完成界面操作，接口本身无需申请权限。picker获取的uri只具有临时权限，获取持久化权限需要通过FilePicker设置永久授权方式获取。
根据用户文件的常见类型，选择器（FilePicker）分别提供以下选项：
-  PhotoViewPicker：适用于图片或视频类型文件的选择与保存（该接口在后续版本不再演进）。请使用PhotoAccessHelper的PhotoViewPicker来选择图片文件。请使用安全控件保存媒体库资源。
-  DocumentViewPicker：适用于文件类型文件的选择与保存。DocumentViewPicker对接的选择资源来自于FilePicker, 负责文件类型的资源管理，文件类型不区分后缀，比如浏览器下载的图片、文档等，都属于文件类型。
-  AudioViewPicker：适用于音频类型文件的选择与保存。AudioViewPicker目前对接的选择资源来自于FilePicker。
选择图片或视频类文件
PhotoViewPicker在后续版本不再演进，请PhotoAccessHelper的PhotoViewPicker来选择图片文件。
选择文档类文件
1.  导入选择器模块和基础文件API模块。
```typescript
import  { picker } from '@kit.CoreFileKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.  创建文件类型、文件选择选项实例。
```typescript
const documentSelectOptions = new picker.DocumentSelectOptions();
// 选择文档的最大数目（可选）。
documentSelectOptions.maxSelectNumber = 5;
// 指定选择的文件或者目录路径（可选）。
documentSelectOptions.defaultFilePathUri = "file://docs/storage/Users/currentUser/test";
// 选择文件的后缀类型['后缀类型描述|后缀类型']（可选，不传该参数，默认不过滤，即显示所有文件），若选择项存在多个后缀名，则每一个后缀名之间用英文逗号进行分隔（可选），后缀类型名不能超过100。此外2in1设备支持通过通配符方式['所有文件(*.*)|.*']，表示为显示所有文件，手机暂不支持该配置。
documentSelectOptions.fileSuffixFilters = ['图片(.png, .jpg)|.png,.jpg', '文档|.txt', '视频|.mp4', '.pdf'];
//选择是否对指定文件或目录授权，true为授权，当为true时，defaultFilePathUri为必选参数，拉起文管授权界面；false为非授权(默认为false)，拉起常规文管界面（可选），仅支持2in1设备。
documentSelectOptions.authMode = false;
```
3.  创建文件选择器DocumentViewPicker实例。调用select()接口拉起FilePicker应用界面进行文件选择。
```typescript
let uris: Array<string> = [];
let context = getContext(this) as common.Context; // 请确保 getContext(this) 返回结果为 UIAbilityContext
// 创建文件选择器实例
const documentViewPicker = new picker.DocumentViewPicker(context);
documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
//文件选择成功后，返回被选中文档的uri结果集。
uris = documentSelectResult;
console.info('documentViewPicker.select to file succeed and uris are:' + uris);
}).catch((err: BusinessError) => {
console.error(`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
})
```
1、使用picker获取的select()返回的uri权限是临时只读权限,待退出应用后台后，获取的临时权限就会失效。
2、如果想要获取持久化权限(仅在2in1设备上生效)，请参考文件持久化授权访问。
3、开发者可以根据结果集中uri做进一步的处理。建议定义一个全局变量保存uri。
4、如有获取元数据需求，可以通过基础文件API和文件URI根据uri获取部分文件属性信息，比如文件大小、访问时间、修改时间、文件名、文件路径等。
1.  待界面从FilePicker返回后，使用基础文件API的fs.openSync接口通过uri打开这个文件得到文件描述符(fd)。
```typescript
let uri: string = '';
//这里需要注意接口权限参数是fs.OpenMode.READ_ONLY。
let file = fs.openSync(uri, fs.OpenMode.READ_ONLY);
console.info('file fd: ' + file.fd);
```
2.  通过fd使用fs.readSync接口读取这个文件内的数据。
```typescript
let buffer = new ArrayBuffer(4096);
let readLen = fs.readSync(file.fd, buffer);
console.info('readSync data to file succeed and buffer size is:' + readLen);
//读取完成后关闭fd。
fs.closeSync(file);
```
选择音频类文件
1.  导入选择器模块和基础文件API模块。
```typescript
import  { picker } from '@kit.CoreFileKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
```
2.  创建音频类型文件选择选项实例。 目前AudioSelectOptions不支持参数配置，默认可以选择所有类型的用户文件。
```typescript
const audioSelectOptions = new picker.AudioSelectOptions();
```
3.  创建音频选择器AudioViewPicker实例。调用select()接口拉起FilePicker应用界面进行文件选择。
```typescript
let uris: string = '';
// 请确保 getContext(this) 返回结果为 UIAbilityContext
let context = getContext(this) as common.Context;
const audioViewPicker = new picker.AudioViewPicker(context);
audioViewPicker.select(audioSelectOptions).then((audioSelectResult: Array<string>) => {
//文件选择成功后，返回被选中音频的uri结果集。
uris = audioSelectResult[0];
console.info('audioViewPicker.select to file succeed and uri is:' + uris);
}).catch((err: BusinessError) => {
console.error(`Invoke audioViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
})
```
1、使用picker获取的select()返回的uri权限是临时只读权限,待退出应用后台后，获取的临时权限就会失效。
2、如果想要获取持久化权限(仅在2in1设备上生效)，请参考文件持久化授权访问。
3、开发者可以根据结果集中的uri做读取文件数据操作。建议定义一个全局变量保存uri。例如通过基础文件API根据uri拿到音频资源的文件描述符(fd)，再配合媒体服务实现音频播放的开发，具体请参考音频播放开发指导。
1.  待界面从FilePicker返回后，可以使用基础文件API的fs.openSync接口通过uri打开这个文件得到文件描述符(fd)。
```typescript
let uri: string = '';
//这里需要注意接口权限参数是fs.OpenMode.READ_ONLY。
let file = fs.openSync(uri, fs.OpenMode.READ_ONLY);
console.info('file fd: ' + file.fd);
```
2.  通过fd可以使用基础文件API的fs.readSync接口读取这个文件内的数据。
```typescript
let buffer = new ArrayBuffer(4096);
let readLen = fs.readSync(file.fd, buffer);
console.info('readSync data to file succeed and buffer size is:' + readLen);
//读取完成后关闭fd。
fs.closeSync(file);
```
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/save-user-file-V14
爬取时间: 2025-04-28 00:36:11
来源: Huawei Developer
在从网络下载文件到本地或将已有用户文件另存为新的文件路径等场景下，需要使用FilePicker提供的保存用户文件的能力。需关注以下关键点：
权限说明
系统隔离说明
保存图片或视频类文件
PhotoViewPicker在后续版本不再演进，建议使用Media Library Kit（媒体文件管理服务）中能力来保存媒体库资源。
如果开发场景无法调用安全控件进行图片、视频保存，可使用相册管理模块PhotoAccessHelper.showAssetsCreationDialog接口进行保存操作。
保存文档类文件
1.  模块导入。
```typescript
import { picker } from '@kit.CoreFileKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
```
2.  配置保存选项。
```typescript
// 创建文件管理器选项实例。
const documentSaveOptions = new picker.DocumentSaveOptions();
// 保存文件名（可选）。 默认为空。
documentSaveOptions.newFileNames = ["DocumentViewPicker01.txt"];
// 保存文件类型['后缀类型描述|后缀类型'],选择所有文件：'所有文件(*.*)|.*'（可选） ，如果选择项存在多个后缀（最大限制100个过滤后缀），默认选择第一个。如果不传该参数，默认无过滤后缀。
documentSaveOptions.fileSuffixChoices = ['文档|.txt', '.pdf'];
```
3.  创建文件选择器DocumentViewPicker实例。调用save()接口拉起FilePicker界面进行文件保存。 1、URI存储建议： 避免在Picker回调中直接操作URI。 建议使用全局变量保存URI以供后续使用。 2、快捷保存: 可以通过DOWNLOAD模式直达下载目录。
```typescript
let uris: Array<string> = [];
// 请确保 getContext(this) 返回结果为 UIAbilityContext
let context = getContext(this) as common.Context;
const documentViewPicker = new picker.DocumentViewPicker(context);
documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
uris = documentSaveResult;
console.info('documentViewPicker.save to file succeed and uris are:' + uris);
}).catch((err: BusinessError) => {
console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
})
```
4.  避免在Picker回调中直接操作URI。
5.  建议使用全局变量保存URI以供后续使用。
6.  可以通过DOWNLOAD模式直达下载目录。
7.  待界面从FilePicker返回后，使用基础文件API的fs.openSync接口，通过URI打开这个文件得到文件描述符(fd)。
```typescript
const uri = '';
//这里需要注意接口权限参数是fs.OpenMode.READ_WRITE。
let file = fs.openSync(uri, fs.OpenMode.READ_WRITE);
console.info('file fd: ' + file.fd);
```
8.  通过(fd)使用基础文件API的fs.writeSync接口对这个文件进行编辑修改，编辑修改完成后关闭(fd)。
```typescript
let writeLen: number = fs.writeSync(file.fd, 'hello, world');
console.info('write data to file succeed and size is:' + writeLen);
fs.closeSync(file);
```
-  避免在Picker回调中直接操作URI。
-  建议使用全局变量保存URI以供后续使用。
-  可以通过DOWNLOAD模式直达下载目录。
保存音频类文件
1.  模块导入。
```typescript
import { picker } from '@kit.CoreFileKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
```
2.  配置保存选项。
```typescript
const audioSaveOptions = new picker.AudioSaveOptions();
// 保存文件名（可选）
audioSaveOptions.newFileNames = ['AudioViewPicker01.mp3'];
```
3.  创建音频选择器AudioViewPicker实例。调用save()接口拉起FilePicker界面进行文件保存。 1、URI存储建议： 避免在Picker回调中直接操作URI。 建议使用全局变量保存URI以供后续使用。 2、快捷保存： 可以通过DOWNLOAD模式直达下载目录。
```typescript
let uri: string = '';
// 请确保 getContext(this) 返回结果为 UIAbilityContext
let context = getContext(this) as common.Context;
const audioViewPicker = new picker.AudioViewPicker(context);
audioViewPicker.save(audioSaveOptions).then((audioSelectResult: Array<string>) => {
uri = audioSelectResult[0];
console.info('audioViewPicker.save to file succeed and uri is:' + uri);
}).catch((err: BusinessError) => {
console.error(`Invoke audioViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
})
```
4.  避免在Picker回调中直接操作URI。
5.  建议使用全局变量保存URI以供后续使用。
6.  可以通过DOWNLOAD模式直达下载目录。
7.  待界面从FilePicker返回后，可以使用基础文件API的fs.openSync接口，通过URI打开这个文件得到文件描述符(fd)。
```typescript
//这里需要注意接口权限参数是fileIo.OpenMode.READ_WRITE。
let file = fs.openSync(uri, fs.OpenMode.READ_WRITE);
console.info('file fd: ' + file.fd);
```
8.  通过(fd)使用基础文件API的fs.writeSync接口对这个文件进行编辑修改，编辑修改完成后关闭(fd)。
```typescript
let writeLen = fs.writeSync(file.fd, 'hello, world');
console.info('write data to file succeed and size is:' + writeLen);
fs.closeSync(file);
```
-  避免在Picker回调中直接操作URI。
-  建议使用全局变量保存URI以供后续使用。
-  可以通过DOWNLOAD模式直达下载目录。
DOWNLOAD模式保存文件
模式特点
1.  模块导入。
```typescript
import { fileUri, picker } from '@kit.CoreFileKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
```
2.  配置下载模式。
```typescript
const documentSaveOptions = new picker.DocumentSaveOptions();
// 配置保存的模式为DOWNLOAD，若配置了DOWNLOAD模式，此时配置的其他documentSaveOptions参数将不会生效。
documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
```
3.  保存到下载目录。
```typescript
let uri: string = '';
// 请确保 getContext(this) 返回结果为 UIAbilityContext
let context = getContext(this) as common.Context;
const documentViewPicker = new picker.DocumentViewPicker(context);
const documentSaveOptions = new picker.DocumentSaveOptions();
documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
documentViewPicker.save(documentSaveOptions ).then((documentSaveResult: Array<string>) => {
uri = documentSaveResult[0];
console.info('documentViewPicker.save succeed and uri is:' + uri);
const testFilePath = new fileUri.FileUri(uri + '/test.txt').path;
const file = fs.openSync(testFilePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
fs.writeSync(file.fd, 'Hello HarmonyOS');
fs.closeSync(file.fd);
}).catch((err: BusinessError) => {
console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
})
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/file-persistpermission-V14
爬取时间: 2025-04-28 00:36:24
来源: Huawei Developer
场景介绍
应用通过Picker获取临时授权，临时授权在应用退出后或者设备重启后会清除，如果应用重启或者设备重启后需要直接访问之前已访问过的文件，则对文件进行持久化授权。
通过Picker获取临时授权并进行授权持久化
通过Picker选择文件或文件夹进行临时授权，然后应用可以按需通过文件分享接口（ohos.fileshare）进行持久化授权。
1.应用仅临时需要访问公共目录的数据，例如：通讯类应用需要发送用户的文件或者图片。应用调用Picker的(select)接口选择需要发送的文件或者图片，此时应用获取到是该文件的临时访问权限，应用重启或者设备重启后，再次访问该文件则仍需使用Picker进行文件选择。
2.应用如果需要长期访问某个文件或目录时，可以通过Picker选择文件或文件夹进行临时授权，然后利用persistPermission接口（ohos.fileshare.persistPermission）对授权进行持久化（在授权方同意被持久化的情况下），例如：文档编辑类应用本次编辑完一个用户文件，期望在历史记录中可以直接选中打开，无需再拉起Picker进行选择授权。
可使用canIUse接口，确认设备是否具有以下系统能力：SystemCapability.FileManagement.AppFileService.FolderAuthorization。
```typescript
if (!canIUse('SystemCapability.FileManagement.AppFileService.FolderAuthorization')) {
console.error('this api is not supported on this device');
return;
}
```
需要权限
ohos.permission.FILE_ACCESS_PERSIST，具体参考访问控制-申请应用权限。
示例：
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
import { fileShare } from '@kit.CoreFileKit';
async function persistPermissionExample() {
try {
let DocumentSelectOptions = new picker.DocumentSelectOptions();
let documentPicker = new picker.DocumentViewPicker();
let uris = await documentPicker.select(DocumentSelectOptions);
let policyInfo: fileShare.PolicyInfo = {
uri: uris[0],
operationMode: fileShare.OperationMode.READ_MODE,
};
let policies: Array<fileShare.PolicyInfo> = [policyInfo];
fileShare.persistPermission(policies).then(() => {
console.info("persistPermission successfully");
}).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
console.error("persistPermission failed with error message: " + err.message + ", error code: " + err.code);
if (err.code == 13900001 && err.data) {
for (let i = 0; i < err.data.length; i++) {
console.error("error code : " + JSON.stringify(err.data[i].code));
console.error("error uri : " + JSON.stringify(err.data[i].uri));
console.error("error reason : " + JSON.stringify(err.data[i].message));
}
}
});
} catch (error) {
let err: BusinessError = error as BusinessError;
console.error('persistPermission failed with err: ' + JSON.stringify(err));
}
}
```
注意
1、持久化授权文件信息建议应用在本地存储数据，供后续按需激活持久化文件。
2、持久化授权的数据存储在系统的数据库中，应用或者设备重启后需要激活已持久化的授权才可以正常使用激活持久化授权。
3、持久化权限接口(仅在2in1上生效可以使用canIUse接口进行校验能力是否可用)，且需要申请对应的权限。
4、应用在卸载时会将之前的授权数据全部清除，重新安装后需要重新授权。
备注
C/C++持久化授权接口说明及开发指南具体参考：OH_FileShare_PersistPermission持久化授权接口。
3.可以通过revokePermission接口（ohos.fileshare.revokePermission）对已持久化的文件取消授权，同时更新应用存储的数据以删除最近访问数据。
需要权限
ohos.permission.FILE_ACCESS_PERSIST，具体参考访问控制-申请应用权限。
示例：
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
import { fileShare } from '@kit.CoreFileKit';
async function revokePermissionExample() {
try {
let uri = "file://docs/storage/Users/username/tmp.txt";
let policyInfo: fileShare.PolicyInfo = {
uri: uri,
operationMode: fileShare.OperationMode.READ_MODE,
};
let policies: Array<fileShare.PolicyInfo> = [policyInfo];
fileShare.revokePermission(policies).then(() => {
console.info("revokePermission successfully");
}).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
console.error("revokePermission failed with error message: " + err.message + ", error code: " + err.code);
if (err.code == 13900001 && err.data) {
for (let i = 0; i < err.data.length; i++) {
console.error("error code : " + JSON.stringify(err.data[i].code));
console.error("error uri : " + JSON.stringify(err.data[i].uri));
console.error("error reason : " + JSON.stringify(err.data[i].message));
}
}
});
} catch (error) {
let err: BusinessError = error as BusinessError;
console.error('revokePermission failed with err: ' + JSON.stringify(err));
}
}
```
注意
1、示例中的uri来源自应用存储的持久化数据中。
2、建议按照使用需求去激活对应的持久化权限，不要盲目的全量激活。
3、持久化权限接口(仅在2in1上生效可以使用canIUse接口进行校验能力是否可用)，且需要申请对应的权限。
备注
C/C++去持久化授权接口说明及开发指南具体参考：OH_FileShare_RevokePermission去持久化授权接口。
激活已经持久化的权限访问文件或目录
对于应用已经持久化的授权，应用每次启动时实际未加载到内存中，需要应用按需进行手动激活已持久化授权的权限，通过activatePermission接口（ohos.fileshare.activatePermission）对已经持久化授权的权限进行使能操作，否则已经持久化授权的权限仍存在不能使用的情况。
需要权限
ohos.permission.FILE_ACCESS_PERSIST，具体参考访问控制-申请应用权限。
示例：
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
import { fileShare } from '@kit.CoreFileKit';
async function activatePermissionExample() {
try {
let uri = "file://docs/storage/Users/username/tmp.txt";
let policyInfo: fileShare.PolicyInfo = {
uri: uri,
operationMode: fileShare.OperationMode.READ_MODE,
};
let policies: Array<fileShare.PolicyInfo> = [policyInfo];
fileShare.activatePermission(policies).then(() => {
console.info("activatePermission successfully");
}).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
console.error("activatePermission failed with error message: " + err.message + ", error code: " + err.code);
if (err.code == 13900001 && err.data) {
for (let i = 0; i < err.data.length; i++) {
console.error("error code : " + JSON.stringify(err.data[i].code));
console.error("error uri : " + JSON.stringify(err.data[i].uri));
console.error("error reason : " + JSON.stringify(err.data[i].message));
if (err.data[i].code == fileShare.PolicyErrorCode.PERMISSION_NOT_PERSISTED) {
//可以选择进行持久化后再激活。
}
}
}
});
} catch (error) {
let err: BusinessError = error as BusinessError;
console.error('activatePermission failed with err: ' + JSON.stringify(err));
}
}
```
1、示例中的uri来源自应用存储的持久化数据中。
2、建议按照使用需求去激活对应的持久化权限，不要盲目的全量激活。
3、如果激活失败显示未持久化的权限可以按照示例进行持久化。
4、持久化权限接口(仅在2in1上生效可以使用canIUse接口进行校验能力是否可用)，且需要申请对应的权限。
C/C++持久化授权激活接口说明及开发指南具体参考：OH_FileShare_ActivatePermission持久化授权激活接口。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/native-fileshare-guidelines-V14
爬取时间: 2025-04-28 00:36:37
来源: Huawei Developer
场景介绍
应用通过Picker获取临时授权，临时授权在应用退出后或者设备重启后会清除，如果应用重启或者设备重启后需要直接访问之前已访问过的文件，则对文件进行持久化授权。FileShare提供了支持基于URI的文件及目录授于持久化权限、权限激活、权限查询等方法。
接口说明
接口的详细介绍请参见API参考。
| 接口名称 | 描述 |
| --- | --- |
| OH_FileShare_PersistPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum) | 对所选择的多个文件或目录URI持久化授权。 |
| OH_FileShare_RevokePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum) | 对所选择的多个文件或目录URI取消持久化授权。 |
| OH_FileShare_ActivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum) | 使能多个已经永久授权过的文件或目录URI。 |
| OH_FileShare_DeactivatePermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, FileShare_PolicyErrorResult **result, unsigned int *resultNum) | 取消使能授权过的多个文件或目录URI。 |
| OH_FileShare_CheckPersistentPermission(const FileShare_PolicyInfo *policies, unsigned int policyNum, bool **result, unsigned int *resultNum) | 校验所选择的多个文件或目录URI的持久化权限结果。 |
| OH_FileShare_ReleasePolicyErrorResult(FileShare_PolicyErrorResult *errorResult, unsigned int resultNum) | 释放FileShare_PolicyErrorResult内存。 |
约束与限制
-  使用文件分享的相关接口，需确认设备具有以下系统能力：SystemCapability.FileManagement.AppFileService.FolderAuthorization。
-  在调用文件分享的相关接口前，需要申请权限："ohos.permission.FILE_ACCESS_PERSIST"，申请方式请参考访问控制-申请应用权限。
开发步骤
以下步骤描述了如何使用FileShare提供的Native API接口。
添加动态链接库
CMakeLists.txt中添加以下lib。
头文件

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/request-dir-permission-V14
爬取时间: 2025-04-28 00:36:51
来源: Huawei Developer
通过 ArkTS 接口获取并访问公共目录
目录环境能力接口（ohos.file.environment）提供获取公共目录路径的能力，支持三方应用在公共文件用户目录下进行文件访问操作。
约束限制
```typescript
if (!canIUse('SystemCapability.FileManagement.File.Environment.FolderObtain')) {
console.error('this api is not supported on this device');
return;
}
```
```json
"requestPermissions" : [
"ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY",
"ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY",
]
```
示例
1.  获取公共目录路径。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { Environment } from '@kit.CoreFileKit';
function getUserDirExample() {
try {
const downloadPath = Environment.getUserDownloadDir();
console.info(`success to getUserDownloadDir: ${downloadPath}`);
const documentsPath = Environment.getUserDocumentDir();
console.info(`success to getUserDocumentDir: ${documentsPath}`);
} catch (error) {
const err: BusinessError = error as BusinessError;
console.error(`failed to get user dir, because: ${JSON.stringify(err)}`);
}
}
```
2.  以 Download 目录为例，访问 Download 目录下的文件。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { Environment } from '@kit.CoreFileKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
function readUserDownloadDirExample() {
// 检查是否具有 READ_WRITE_DOWNLOAD_DIRECTORY 权限，无权限则需要向用户申请授予权限。
try {
// 获取 Download 目录
const downloadPath = Environment.getUserDownloadDir();
console.info(`success to getUserDownloadDir: ${downloadPath}`);
const context = getContext() as common.UIAbilityContext;
const dirPath = context.filesDir;
console.info(`success to get filesDir: ${dirPath}`);
// 查看 Download 目录下的文件并拷贝到沙箱目录中
let fileList: string[] = fs.listFileSync(downloadPath);
fileList.forEach((file, index) => {
console.info(`${downloadPath} ${index}: ${file}`);
fs.copyFileSync(`${downloadPath}/${file}`, `${dirPath}/${file}`);
});
// 查看沙箱目录下对应的文件
fileList = fs.listFileSync(dirPath);
fileList.forEach((file, index) => {
console.info(`${dirPath} ${index}: ${file}`);
});
} catch (error) {
const err: BusinessError = error as BusinessError;
console.error(`Error code: ${err.code}, message: ${err.message}`);
}
}
```
3.  以 Download 目录为例，保存文件到 Download 目录。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { Environment } from '@kit.CoreFileKit';
import { fileIo as fs } from '@kit.CoreFileKit';
function writeUserDownloadDirExample() {
// 检查是否具有 READ_WRITE_DOWNLOAD_DIRECTORY 权限，无权限则需要向用户申请授予权限。
try {
// 获取 Download 目录
const downloadPath = Environment.getUserDownloadDir();
console.info(`success to getUserDownloadDir: ${downloadPath}`);
// 保存 temp.txt 到 Download 目录下
const file = fs.openSync(`${downloadPath}/temp.txt`, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
fs.writeSync(file.fd, 'write a message');
fs.closeSync(file);
} catch (error) {
const err: BusinessError = error as BusinessError;
console.error(`Error code: ${err.code}, message: ${err.message}`);
}
}
```
通过 C/C++ 接口获取并使用公共目录
除了通过 ArkTS 访问公共目录的方式，也可通过 C/C++ 接口进行目录访问，具体可以参考Environment。
约束限制
接口说明
接口的详细说明，请参考API参考
| 接口名称 | 描述 |
| --- | --- |
| FileManagement_ErrCode OH_Environment_GetUserDownloadDir (char **result) | 获取用户Download目录沙箱路径。只支持2in1设备 |
| FileManagement_ErrCode OH_Environment_GetUserDesktopDir (char **result) | 获取用户Desktop目录沙箱路径。只支持2in1设备 |
| FileManagement_ErrCode OH_Environment_GetUserDocumentDir (char **result) | 获取用户Document目录沙箱路径。只支持2in1设备 |
开发步骤
在CMake脚本中链接动态库
CMakeLists.txt中添加以下lib。
添加头文件
1.  调用 OH_Environment_GetUserDownloadDir 接口获取用户 Download 目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：
2.  调用 OH_Environment_GetUserDownloadDir 接口获取用户 Download 目录沙箱路径，并查看 Download 目录下的文件。示例代码如下所示：
3.  调用 OH_Environment_GetUserDownloadDir 接口获取用户 Download 目录沙箱路径，并保存 temp.txt 到 Download 目录下。示例代码如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-fs-V14
爬取时间: 2025-04-28 00:37:04
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-fs-overview-V14
爬取时间: 2025-04-28 00:37:58
来源: Huawei Developer
分布式文件系统（hmdfs，HarmonyOS Distributed File System）提供跨设备的文件访问能力，适用于如下场景：
-  两台设备组网，用户可以利用一台设备上的编辑软件编辑另外一台设备上的文档。
-  平板保存的音乐，车载系统直接可见并可播放。
-  户外拍摄的照片，回家打开平板直接访问原设备拍摄的照片。
hmdfs在分布式软总线动态组网的基础上，为网络上各个设备结点提供一个全局一致的访问视图，支持开发者通过基础文件系统的接口进行读写访问，具有高性能、低延时等优点。
分布式文件系统架构
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170414.34523921836193449579132624865999:50001231000000:2800:6A0B99A68174C25CD1301254080B51CE9BCF6CEAEFC9A2EFA6EC10C8B2653BCD.png)
-  distributedfile_daemon：主要负责设备上线监听、通过软总线建立链路，并根据分布式的设备安全等级执行不同的数据流转策略。
-  hmdfs：实现在内核的网络文件系统，包括缓存管理、文件访问、元数据管理和冲突管理等。 symlink：不支持。
-  symlink：不支持。
-  symlink：不支持。
-  symlink：不支持。
-  symlink：不支持。
-  symlink：不支持。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/set-security-label-V14
爬取时间: 2025-04-28 00:38:11
来源: Huawei Developer
不同设备本身的安全能力差异较大，一些小的嵌入式设备安全能力远弱于平板等设备类型。用户或者应用不同的文件数据有不同安全诉求，例如个人的健康信息和银行卡信息等不期望被弱设备读取。因此，HarmonyOS提供一套完整的数据分级、设备分级标准，并针对不同设备制定不同的数据流转策略，具体规则请参见数据、设备安全分级。
接口说明
API详细介绍请参见ohos.file.securityLabel。
表1设置文件数据等级
| 接口名 | 功能 | 接口类型 | 支持同步 | 支持异步 |
| --- | --- | --- | --- | --- |
| setSecurityLabel | 设置文件安全标签 | 方法 | √ | √ |
| getSecurityLabel | 获取文件安全标签 | 方法 | √ | √ |
1.  对于不满足安全等级的文件，跨设备仍然可以看到该文件，但是无权限打开访问该文件。
2.  分布式文件系统的数据等级默认为S3，应用可以主动设置文件的安全等级。
开发示例
获取通用文件沙箱路径，并设置数据等级标签。示例中的context的获取方式请参见获取UIAbility的上下文信息。
```typescript
import { securityLabel } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';
// 获取需要设备数据等级的文件沙箱路径
let context = getContext(this) as common.UIAbilityContext; // 获取UIAbilityContext信息
let pathDir = context.filesDir;
let filePath = pathDir + '/test.txt';
//打开文件
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
// 设置文件的数据等级为s0
securityLabel.setSecurityLabel(filePath, 's0').then(() => {
console.info('Succeeded in setSecurityLabeling.');
fs.closeSync(file);
}).catch((err: BusinessError) => {
console.error(`Failed to setSecurityLabel. Code: ${err.code}, message: ${err.message}`);
});
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/file-access-across-devices-V14
爬取时间: 2025-04-28 00:38:24
来源: Huawei Developer
分布式文件系统为应用提供了跨设备文件访问的能力，开发者在两个设备安装同一应用时，通过基础文件接口，可跨设备读写另一个设备该应用分布式文件路径（/data/storage/el2/distributedfiles/）下的文件。例如：多设备数据流转的场景，设备组网互联之后，设备A上的应用可访问设备B同应用分布式路径下的文件，当期望应用文件被其他设备访问时，只需将文件移动到分布式文件路径即可。
开发步骤
1.  完成分布式组网。 将需要跨设备访问的两个设备登录同一账号，保证设备蓝牙和Wi-Fi功能开启，蓝牙无需互连，Wi-Fi无需接入同一个局域网。
2.  访问跨设备文件。 同一应用不同设备之间实现跨设备文件访问，只需要将对应的文件放在应用沙箱的分布式文件路径即可。 设备A上在分布式路径下创建测试文件，并写入内容。示例中的context的获取方式请参见获取UIAbility的上下文信息。 设备B主动向设备A发起建链，建链成功后设备B可在分布式路径下读取测试文件。 这里通过分布式设备管理的接口获取设备networkId，详见设备管理接口。
```typescript
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
let context = getContext(this) as common.UIAbilityContext; // 获取设备A的UIAbilityContext信息
let pathDir: string = context.distributedFilesDir;
// 获取分布式目录的文件路径
let filePath: string = pathDir + '/test.txt';
try {
// 在分布式目录下创建文件
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
console.info('Succeeded in createing.');
// 向文件中写入内容
fs.writeSync(file.fd, 'content');
// 关闭文件
fs.closeSync(file.fd);
} catch (error) {
let err: BusinessError = error as BusinessError;
console.error(`Failed to openSync / writeSync / closeSync. Code: ${err.code}, message: ${err.message}`);
}
```
3.  B设备访问跨设备文件完成，断开链路。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit'
import { fileIo as fs } from '@kit.CoreFileKit';
// 获取设备A的networkId
let dmInstance = distributedDeviceManager.createDeviceManager("com.example.hap");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
let networkId = deviceInfoList[0].networkId;
// 取消公共文件目录挂载
fs.disconnectDfs(networkId).then(() => {
console.info("Success to disconnectDfs");
}).catch((error: BusinessError) => {
let err: BusinessError = error as BusinessError;
console.error(`Failed to disconnectDfs Code: ${err.code}, message: ${err.message}`)
})
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/file-copy-across-devices-V14
爬取时间: 2025-04-28 00:38:37
来源: Huawei Developer
分布式文件系统为应用提供了跨设备文件拷贝的能力，开发者在跨设备跨应用进行文件拷贝时，通过基础文件接口，可跨设备跨应用拷贝文件。例如：多设备数据流转的场景，设备组网互联之后，设备A上的应用可在复制时，将A设备的沙箱文件，拷贝到A设备的分布式路径下，设备B在粘贴的时候，从设备B的分布式路径下，将文件拷贝到对应的沙箱文件中。
开发步骤
1.  完成分布式组网。 首先将需要进行跨设备访问的设备连接到同一局域网中，同账号认证完成组网。
2.  拷贝跨设备文件。 同一应用不同设备之间实现跨设备文件拷贝，只需要将对应的文件放在应用沙箱的分布式文件路径即可。 将A设备的待拷贝沙箱文件，拷贝到A设备的分布式路径下。 B设备在获取A端沙箱文件时，从B设备的分布式路径下将对应的文件拷贝走，以此完成跨设备拷贝。
```typescript
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
let context = getContext(this) as common.UIAbilityContext; // 获取设备A的UIAbilityContext信息
let pathDir: string = context.filesDir;
let distributedPathDir: string = context.distributedFilesDir;
// 待拷贝文件沙箱路径
let filePath: string = pathDir + '/src.txt';
try {
// 文件不存在时，需要创建文件并写入内容
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
fs.writeSync(file.fd, 'Create file success');
fs.closeSync(file);
} catch (error) {
console.error(`Failed to createFile. Code: ${error.code}, message: ${error.message}`);
}
// 获取待拷贝文件uri
let srcUri = fileUri.getUriFromPath(filePath);
// 将待拷贝的沙箱文件，拷贝到分布式目录下
let destUri: string = fileUri.getUriFromPath(distributedPathDir + '/src.txt');
try {
// 将沙箱路径下的文件拷贝到分布式路径下
fs.copy(srcUri, destUri).then(()=>{
console.info("Succeeded in copying---. ");
console.info("src: " + srcUri + "dest: " + destUri);
}).catch((error: BusinessError)=>{
let err: BusinessError = error as BusinessError;
console.info(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
})
} catch (error) {
console.error(`Failed to getData. Code: ${error.code}, message: ${error.message}`);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/form-kit-V14
爬取时间: 2025-04-28 00:38:50
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/formkit-overview-V14
爬取时间: 2025-04-28 00:39:03
来源: Huawei Developer
Form Kit（卡片开发框架）提供了一种在桌面、锁屏等系统入口嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（以下简称“卡片”）上，通过将卡片添加到桌面上，以达到信息展示、服务直达的便捷体验效果。
卡片使用场景
服务卡片架构
图1服务卡片架构
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170414.97077202041477055502927869960783:50001231000000:2800:CD24E53D9CAC649013C2A58E3E71FE36BB0208FC9D7CBE19AC06166A034C412E.png)
卡片场景中涉及到的基本概念
-  卡片使用方：如上图中的桌面，作为显示卡片内容的宿主应用，用于与用户直接进行交互，完成卡片添加、删除、显示功能，并能控制卡片在宿主中具体展示的位置。
-  卡片提供方：提供卡片的应用或元服务，是卡片功能的具体实现者，需要设计实现卡片UI、数据更新、以及点击交互处理功能。
-  卡片管理服务：操作系统内管理整机卡片信息的系统服务，作为卡片提供方和使用方的桥梁，向使用方提供卡片信息查询、添加、删除等能力，同时向提供方提供卡片被添加、被删除、刷新、点击事件等通知能力。
卡片的常见使用步骤如下：
图2卡片常见使用步骤
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170414.64852517583643411951372722262369:50001231000000:2800:353E54861F2F65305DC92D5EB279503C45E7974838F2154D4698507D0DE31293.png)
亮点/特征
-  信息呈现：将应用/元服务的重要信息以卡片形式展示在桌面，同时支持信息定时更新能力，用户可以随时查看关注的信息。
-  服务直达：通过点击卡片内按钮，就可以实现功能快捷操作，也支持点击后跳转到应用/元服务对应功能页，实现功能服务一步直达的效果。
开发模式
应用运行模式选择
当前系统中应用开发模型支持Stage和FA两种方式，所以Form Kit也同时支持开发者使用Stage模型和FA模型来开发卡片应用，但更推荐使用Stage模型。
UI开发范式选择
ArkTS卡片与JS卡片具备不同的实现原理及特征，在场景能力上的差异如下表所示：
| 类别 | JS卡片 | ArkTS卡片 |
| --- | --- | --- |
| 开发范式 | 类Web范式 | 声明式范式 |
| 组件能力 | 支持 | 支持 |
| 布局能力 | 支持 | 支持 |
| 事件能力 | 支持 | 支持 |
| 自定义动效 | 不支持 | 支持 |
| 自定义绘制 | 不支持 | 支持 |
| 逻辑代码执行 | 不支持 | 支持 |
与相关Kit的关系
约束限制
UI能力约束
卡片尺寸大小有限，适合承载简洁明了的信息和交互操作，所以卡片开发中支持使用的UI控件范围、动效能力会有一定限制。
运动能力约束
卡片能为应用和元服务提供在桌面等入口常驻的信息显示和更新的能力，系统对于更新频次和卡片后台运行能力范围会有一定的限制。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-stage-V14
爬取时间: 2025-04-28 00:39:17
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-V14
爬取时间: 2025-04-28 00:39:30
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-working-principles-V14
爬取时间: 2025-04-28 00:39:43
来源: Huawei Developer
实现原理
图1ArkTS卡片实现原理
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170414.42656242998225331388758664139226:50001231000000:2800:EB1CFF0780F3DEEE4821240C75ACB969983B94CEBCE3D6A91A609CDC55A28334.png)
-  卡片使用方：显示卡片内容的宿主应用，控制卡片在宿主中展示的位置，当前仅系统应用可以作为卡片使用方。
-  卡片提供方：提供卡片显示内容的应用，控制卡片的显示内容、控件布局以及控件点击事件。
-  卡片管理服务：用于管理系统中所添加卡片的常驻代理服务，提供formProvider的接口能力，同时提供卡片对象的管理与使用以及卡片周期性刷新等能力。
-  卡片渲染服务：用于管理卡片渲染实例，渲染实例与卡片使用方上的卡片组件一一绑定。卡片渲染服务运行卡片页面代码widgets.abc进行渲染，并将渲染后的数据发送至卡片使用方对应的卡片组件。 图2ArkTS卡片渲染服务运行原理
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170415.22934707226070543117577358050646:50001231000000:2800:3C6851E006561A826083B2F654A33DF9A83FBC942B218D84E84703C6A23FFA0E.png)
与动态卡片相比，静态卡片整体的运行框架和渲染流程是一致的，主要区别在于，卡片渲染服务将卡片内容渲染完毕后，卡片使用方会使用最后一帧渲染的数据作为静态图片显示，其次卡片渲染服务中的卡片实例会释放该卡片的所有运行资源以节省内存。因此频繁的刷新会导致静态卡片运行时资源不断的创建和销毁，增加卡片功耗。
与JS卡片相比，ArkTS卡片支持在卡片中运行逻辑代码，为确保ArkTS卡片发生问题后不影响卡片使用方应用的使用，ArkTS卡片新增了卡片渲染服务用于运行卡片页面代码widgets.abc，卡片渲染服务由卡片管理服务管理。卡片使用方的每个卡片组件都对应了卡片渲染服务里的一个渲染实例，同一应用提供方的渲染实例运行在同一个ArkTS虚拟机运行环境中，不同应用提供方的渲染实例运行在不同的ArkTS虚拟机运行环境中，通过ArkTS虚拟机运行环境隔离不同应用提供方卡片之间的资源与状态。开发过程中需要注意的是globalThis对象的使用，相同应用提供方的卡片globalThis对象是同一个，不同应用提供方的卡片globalThis对象是不同的。
ArkTS卡片的优势
卡片作为应用的一个快捷入口，ArkTS卡片相较于JS卡片具备如下几点优势：
-  统一开发范式，提升开发体验和开发效率。 提供ArkTS卡片能力后，统一了卡片和页面的开发范式，页面的布局可以直接复用到卡片布局中，提升开发体验和开发效率。 图3卡片工程结构对比
-  增强了卡片的能力，使卡片更加万能。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170415.39781696022948981899582452122680:50001231000000:2800:D914DD0E3B3DDCDFF0318A74E69E86BE2A013F7C4A7C668165321C7879AA460F.png)
ArkTS卡片的约束
ArkTS卡片相较于JS卡片具备了更加丰富的能力，但也增加了使用卡片进行恶意行为的风险。由于ArkTS卡片显示在使用方应用中，使用方应用一般为桌面应用，为确保桌面的使用体验以及功耗相关考虑，对ArkTS卡片的能力做了以下约束：
-  当导入模块时，仅支持导入标识“支持在ArkTS卡片中使用”的模块。
-  支持导入HAR静态共享包，不支持导入HSP动态共享包。
-  不支持使用native语言开发。
-  仅支持声明式范式的部分组件、事件、动效、数据管理、状态管理和API能力。
-  卡片的事件处理和使用方的事件处理是独立的，建议在使用方支持左右滑动的场景下卡片内容不要使用左右滑动功能的组件，以防手势冲突影响交互体验。
除此之外，当前ArkTS卡片还存在如下约束：
-  暂不支持极速预览。
-  暂不支持断点调试能力。
-  暂不支持Hot Reload热重载。
-  暂不支持setTimeOut。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-modules-V14
爬取时间: 2025-04-28 00:39:56
来源: Huawei Developer
图1ArkTS卡片相关模块
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170415.09932379463330736958448619791330:50001231000000:2800:998B121649C16864FA50D8CA7F0CF3FF3D84DD48F49E6E899371AF60CDABAD03.png)
-  FormExtensionAbility：卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调。
-  FormExtensionContext：FormExtensionAbility的上下文环境，提供FormExtensionAbility具有的接口和能力。
-  formProvider：提供卡片提供方相关的接口能力，可通过该模块提供接口实现更新卡片、设置卡片更新时间、获取卡片信息、请求发布卡片等。
-  formInfo：提供了卡片信息和状态等相关类型和枚举。
-  formBindingData：提供卡片数据绑定的能力，包括FormBindingData对象的创建、相关信息的描述。
-  页面布局（WidgetCard.ets）：基于ArkUI提供卡片UI开发能力。
-  卡片配置：包含FormExtensionAbility的配置和卡片的配置

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-dev-V14
爬取时间: 2025-04-28 00:40:09
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-creation-V14
爬取时间: 2025-04-28 00:40:23
来源: Huawei Developer
创建卡片当前有两种入口：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170415.79663380267001427516108127364414:50001231000000:2800:3808462A0678C94EF57C9784DFD8CEE8460BD1BD6A6E866948C087304F5E9014.png)
基于不同版本的DeEco Studio，请以实际界面为准。
在已有的应用工程中，可以通过右键新建ArkTS卡片，具体的操作方式如下。
1.  右键新建卡片。 在API 10及以上 Stage模型的工程中，在Service Widget菜单可直接选择创建动态或静态服务卡片。创建服务卡片后，也可以在卡片的form_config.json配置文件中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为"true"，则该卡片为动态卡片；isDynamic赋值为"false"，则该卡片为静态卡片。
2.  根据实际业务场景，选择一个卡片模板。
3.  在选择卡片的开发语言类型（Language）时，选择ArkTS选项，然后单击“Finish”，即可完成ArkTS卡片创建。 建议根据实际使用场景命名卡片名称，ArkTS卡片创建完成后，工程中会新增如下卡片相关文件：卡片生命周期管理文件（EntryFormAbility.ets）、卡片页面文件（WidgetCard.ets）和卡片配置文件（form_config.json）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170415.83673812926785880449485075944466:50001231000000:2800:FEFE89BBEB3EA4C855DC296C85703A25D0A1B757C5F2E471CE26B4C54FF0CE19.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170415.91185873354044941188651472964461:50001231000000:2800:B54B52A07EDB93D7F21BB8F7CF48C2B91BF7E38DC926291D6D282BF4696D7E72.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170415.90285868687422256987901425629791:50001231000000:2800:81E944A1E5D0EFB41951F8F793059B6F9E187E6DA45438D65D80F23D9310A837.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170415.11998899433813437544337377345905:50001231000000:2800:971C814779763B4B46B13F3B019E2401852F63138EF94DE62ED1D1F28708EB38.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-configuration-V14
爬取时间: 2025-04-28 00:40:36
来源: Huawei Developer
卡片相关的配置文件主要包含FormExtensionAbility的配置和卡片的配置两部分。
1.  卡片需要在module.json5配置文件中的extensionAbilities标签下，配置FormExtensionAbility相关信息。FormExtensionAbility需要填写metadata元信息标签，其中键名称为固定字符串“ohos.extension.form”，资源为卡片的具体配置信息的索引。 配置示例如下：
```json
{
"module": {
// ...
"extensionAbilities": [
{
"name": "EntryFormAbility",
"srcEntry": "./ets/entryformability/EntryFormAbility.ets",
"label": "$string:EntryFormAbility_label",
"description": "$string:EntryFormAbility_desc",
"type": "form",
"metadata": [
{
"name": "ohos.extension.form",
"resource": "$profile:form_config"
}
]
}
]
}
}
```
2.  卡片的具体配置信息。在上述FormExtensionAbility的元信息（“metadata”配置项）中，可以指定卡片具体配置信息的资源索引。例如当resource指定为$profile:form_config时，会使用开发视图的resources/base/profile/目录下的form_config.json作为卡片profile配置文件。内部字段结构说明如下表所示。 表1卡片form_config.json配置文件 表示该卡片的类型，当前支持如下两种类型： - arkts：当前卡片为ArkTS卡片。 - hml：当前卡片为JS卡片。 表示该卡片是否为默认卡片，每个UIAbility有且只有一个默认卡片。 - true：默认卡片。 - false：非默认卡片。 表示卡片的主题样式，取值范围如下： - auto：跟随系统的颜色模式值选取主题。 - dark：深色主题。 - light：浅色主题。 表示卡片支持的外观规格，取值范围： - 1 * 2：表示1行2列的二宫格。 - 2 * 2：表示2行2列的四宫格。 - 2 * 4：表示2行4列的八宫格。 - 4 * 4：表示4行4列的十六宫格。 - 1 * 1：表示1行1列的圆形卡片。 - 6 * 4：表示6行4列的二十四宫格。 表示卡片是否支持周期性刷新（包含定时刷新和定点刷新），取值范围： - true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，当两者同时配置时，定时刷新优先生效。 - false：表示不支持周期性刷新。 表示卡片的定点刷新的时刻，采用24小时制，精确到分钟。 说明： updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 表示卡片定时刷新的更新周期，单位为30分钟，取值为自然数。 当取值为0时，表示该参数不生效。 当取值为正整数N时，表示刷新周期为30*N分钟。 说明： updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 表示卡片是否支持卡片代理刷新，取值范围： - true：表示支持代理刷新。 - false：表示不支持代理刷新。 设置为true时，定时刷新和下次刷新不生效，但不影响定点刷新。 表示此卡片是否为动态卡片（仅针对ArkTS卡片生效）。 - true：为动态卡片 。 - false：为静态卡片。 表示卡片使用方设置此卡片的字体是否支持跟随系统变化。 - true：支持跟随系统字体大小变化 。 - false：不支持跟随系统字体大小变化。 表示卡片的显示形状，取值范围如下： - rect：表示方形卡片。 - circle：表示圆形卡片。
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 表示卡片的名称，字符串最大长度为127字节。 | 字符串 | 否 |
| displayName | 表示卡片的显示名称。取值可以是名称内容，也可以是对名称内容的资源索引，以支持多语言。字符串最小长度为1字节，最大长度为30字节。 | 字符串 | 否 |
| description | 表示卡片的描述。取值可以是描述性内容，也可以是对描述性内容的资源索引，以支持多语言。字符串最大长度为255字节。 | 字符串 | 可缺省，缺省为空。 |
| src | 表示卡片对应的UI代码的完整路径。当为ArkTS卡片时，完整路径需要包含卡片文件的后缀，如："./ets/widget/pages/WidgetCard.ets"。当为JS卡片时，完整路径无需包含卡片文件的后缀，如："./js/widget/pages/WidgetCard" | 字符串 | 否 |
| uiSyntax | 表示该卡片的类型，当前支持如下两种类型： - arkts：当前卡片为ArkTS卡片。 - hml：当前卡片为JS卡片。 | 字符串 | 可缺省，缺省值为“hml”。 |
| window | 用于定义与显示窗口相关的配置。 | 对象 | 可缺省，缺省值见表2。 |
| isDefault | 表示该卡片是否为默认卡片，每个UIAbility有且只有一个默认卡片。 - true：默认卡片。 - false：非默认卡片。 | 布尔值 | 否 |
| colorMode | 表示卡片的主题样式，取值范围如下： - auto：跟随系统的颜色模式值选取主题。 - dark：深色主题。 - light：浅色主题。 | 字符串 | 可缺省，缺省值为“auto”。 |
| supportDimensions | 表示卡片支持的外观规格，取值范围： - 1 * 2：表示1行2列的二宫格。 - 2 * 2：表示2行2列的四宫格。 - 2 * 4：表示2行4列的八宫格。 - 4 * 4：表示4行4列的十六宫格。 - 1 * 1：表示1行1列的圆形卡片。 - 6 * 4：表示6行4列的二十四宫格。 | 字符串数组 | 否 |
| defaultDimension | 表示卡片的默认外观规格，取值必须在该卡片supportDimensions配置的列表中。 | 字符串 | 否 |
| updateEnabled | 表示卡片是否支持周期性刷新（包含定时刷新和定点刷新），取值范围： - true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，当两者同时配置时，定时刷新优先生效。 - false：表示不支持周期性刷新。 | 布尔类型 | 否 |
| scheduledUpdateTime | 表示卡片的定点刷新的时刻，采用24小时制，精确到分钟。 说明： updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 字符串 | 可缺省，缺省时不进行定点刷新。 |
| updateDuration | 表示卡片定时刷新的更新周期，单位为30分钟，取值为自然数。 当取值为0时，表示该参数不生效。 当取值为正整数N时，表示刷新周期为30*N分钟。 说明： updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 数值 | 可缺省，缺省值为“0”。 |
| formConfigAbility | 表示卡片的配置跳转链接，采用URI格式。 | 字符串 | 可缺省，缺省值为空。 |
| metadata | 表示卡片的自定义信息，参考Metadata数组标签。 | 对象 | 可缺省，缺省值为空。 |
| dataProxyEnabled | 表示卡片是否支持卡片代理刷新，取值范围： - true：表示支持代理刷新。 - false：表示不支持代理刷新。 设置为true时，定时刷新和下次刷新不生效，但不影响定点刷新。 | 布尔类型 | 可缺省，缺省值为false。 |
| isDynamic | 表示此卡片是否为动态卡片（仅针对ArkTS卡片生效）。 - true：为动态卡片 。 - false：为静态卡片。 | 布尔类型 | 可缺省，缺省值为true。 |
| fontScaleFollowSystem | 表示卡片使用方设置此卡片的字体是否支持跟随系统变化。 - true：支持跟随系统字体大小变化 。 - false：不支持跟随系统字体大小变化。 | 布尔类型 | 可缺省，缺省值为true。 |
| supportShapes | 表示卡片的显示形状，取值范围如下： - rect：表示方形卡片。 - circle：表示圆形卡片。 | 字符串 | 可缺省，缺省值为“rect”。 |
isDynamic标签
此标签标识卡片是否为动态卡片（仅针对ArkTS卡片生效）。
| 卡片类型 | 支持的能力 | 适用场景 | 优缺点 |
| --- | --- | --- | --- |
| 静态卡片 | 仅支持UI组件和布局能力。 | 主要用于展示静态信息（UI相对固定），仅可以通过FormLink组件跳转到指定的UIAbility。 | 功能简单但可以有效控制内存开销。 |
| 动态卡片 | 除了支持UI组件和布局能力，还支持通用事件能力和自定义动效能力。 | 用于有复杂业务逻辑和交互的场景。例如：卡片页面图片的刷新、卡片内容的刷新等。 | 功能丰富但内存开销较大。 |
window标签
此标签标识window对象的内部结构说明。
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| designWidth | 标识页面设计基准宽度。以此为基准，根据实际设备宽度来缩放元素大小。 | 数值 | 可缺省，缺省值为720px。 |
| autoDesignWidth | 标识页面设计基准宽度是否自动计算。当配置为true时，designWidth将会被忽略，设计基准宽度由设备宽度与屏幕密度计算得出。 | 布尔值 | 可缺省，缺省值为false。 |
配置示例如下：
```json
{
"forms": [
{
"name": "widget",
"displayName": "$string:widget_display_name",
"description": "$string:widget_desc",
"src": "./ets/widget/pages/WidgetCard.ets",
"uiSyntax": "arkts",
"window": {
"designWidth": 720,
"autoDesignWidth": true
},
"colorMode": "auto",
"isDefault": true,
"updateEnabled": true,
"scheduledUpdateTime": "10:30",
"updateDuration": 1,
"defaultDimension": "2*2",
"supportDimensions": [
"2*2"
],
"formConfigAbility": "ability://EntryAbility",
"dataProxyEnabled": false,
"isDynamic": true,
"transparencyEnabled": false,
"metadata": []
}
]
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-lifecycle-V14
爬取时间: 2025-04-28 00:40:49
来源: Huawei Developer
创建ArkTS卡片，需实现FormExtensionAbility生命周期接口。
1.  在EntryFormAbility.ets中，导入相关模块。
```typescript
import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
import { Configuration, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```
2.  在EntryFormAbility.ets中，实现FormExtensionAbility生命周期接口，其中在onAddForm的入参want中可以通过FormParam取出卡片的相关信息。
```typescript
const TAG: string = 'EntryFormAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class EntryFormAbility extends FormExtensionAbility {
onAddForm(want: Want): formBindingData.FormBindingData {
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onAddForm');
hilog.info(DOMAIN_NUMBER, TAG, want.parameters?.[formInfo.FormParam.NAME_KEY] as string);
// ...
// 卡片使用方创建卡片时触发，提供方需要返回卡片数据绑定类
let obj: Record<string, string> = {
'title': 'titleOnAddForm',
'detail': 'detailOnAddForm'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
return formData;
}
onCastToNormalForm(formId: string): void {
// 卡片使用方将临时卡片转换为常态卡片触发，提供方需要做相应的处理。
// 1、临时卡、常态卡是卡片使用方的概念。
// 2、临时卡是短期存在的，在特定事件或用户行为后显示，完成后自动消失。
// 3、常态卡是持久存在的，在用户未进行清除或更改的情况下，会一直存在，平时开发的功能卡片属于常态卡。
// 4、目前手机上没有地方会使用临时卡。
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onCastToNormalForm');
}
onUpdateForm(formId: string): void {
// 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
let obj: Record<string, string> = {
'title': 'titleOnUpdateForm',
'detail': 'detailOnUpdateForm'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
});
}
onChangeFormVisibility(newStatus: Record<string, number>): void {
// 卡片使用方发起可见或者不可见通知触发，提供方需要做相应的处理，仅系统应用生效
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onChangeFormVisibility');
}
onFormEvent(formId: string, message: string): void {
// 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onFormEvent');
// ...
}
onRemoveForm(formId: string): void {
// 删除卡片实例数据
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
// 删除之前持久化的卡片实例数据
// 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
}
onConfigurationUpdate(config: Configuration) {
// 当前formExtensionAbility存活时更新系统配置信息时触发的回调。
// 需注意：formExtensionAbility创建后10秒内无操作将会被清理。
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onConfigurationUpdate:' + JSON.stringify(config));
}
onAcquireFormState(want: Want) {
// 卡片提供方接收查询卡片状态通知接口，默认返回卡片初始状态。
return formInfo.FormState.READY;
}
}
```
FormExtensionAbility进程不能常驻后台，即在卡片生命周期回调函数中无法处理长时间的任务，在生命周期调度完成后会继续存在10秒，如10秒内没有新的生命周期回调触发则进程自动退出。针对可能需要10秒以上才能完成的业务逻辑，建议拉起主应用进行处理，处理完成后使用updateForm通知卡片进行刷新。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-page-V14
爬取时间: 2025-04-28 00:41:02
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-page-overview-V14
爬取时间: 2025-04-28 00:41:16
来源: Huawei Developer
ArkTS卡片开发采用通用学习ArkTS语言，开发者可以使用声明式范式开发ArkTS卡片页面。
如下卡片页面由DevEco Studio模板自动生成，开发者可以根据自身的业务场景进行调整。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170416.21091268877661946134559559454665:50001231000000:2800:69AE953C6F377D5C61511E267E90FD8C0DDCFAB3A1032FC29CFDDFD5FABB7A3E.png)
ArkTS卡片支持的页面能力
ArkTS卡片具备JS卡片的全量能力，并且新增了动效能力和自定义绘制的能力，支持声明式范式的部分组件、事件、动效、数据管理、状态管理能力。
对于支持在ArkTS卡片中使用的接口，会添加“卡片能力”的标记：从API version x开始，该接口支持在ArkTS卡片中使用。同时请留意卡片场景下的能力差异说明。
例如：以下说明表示CircleShape可在ArkTS卡片中使用。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170416.35026003950116750760931709479116:50001231000000:2800:1FAD1CABC3AA6CFC1334C9A7054CDDEE19AE5B5045CA363D769F429D6B95E5C9.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-page-animation-V14
爬取时间: 2025-04-28 00:41:29
来源: Huawei Developer
ArkTS卡片开放了使用动画效果的能力，支持显式动画、属性动画、组件内转场能力。需要注意的是，ArkTS卡片使用动画效果时具有以下限制：
表1动效参数限制
| 名称 | 参数说明 | 限制描述 |
| --- | --- | --- |
| duration | 动画播放时长 | 限制最长的动效播放时长为1秒，当设置大于1秒的时间时，动效时长仍为1秒。 |
| tempo | 动画播放速度 | 卡片中禁止设置此参数，使用默认值1。 |
| delay | 动画延迟执行的时长 | 卡片中禁止设置此参数，使用默认值0。 |
| iterations | 动画播放次数 | 卡片中禁止设置此参数，使用默认值1。 |
静态卡片不支持使用动效能力。
以下示例代码实现了按钮旋转的动画效果：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170416.02052137760176100180449898052426:50001231000000:2800:D74062C5462A8C4FFF789B82A4FEB6B300ED470D1B4F9D227045AF06054DB7A7.gif)
```typescript
@Entry
@Component
struct AnimationCard {
@State rotateAngle: number = 0;
build() {
Row() {
Button('change rotate angle')
.height('20%')
.width('90%')
.margin('5%')
.onClick(() => {
this.rotateAngle = (this.rotateAngle === 0 ? 90 : 0);
})
.rotate({ angle: this.rotateAngle })
.animation({
curve: Curve.EaseOut,
playMode: PlayMode.Normal,
})
}.height('100%').alignItems(VerticalAlign.Center)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-page-custom-drawing-V14
爬取时间: 2025-04-28 00:41:42
来源: Huawei Developer
ArkTS卡片开放了自定义绘制的能力，在卡片上可以通过Canvas组件创建一块画布，然后通过CanvasRenderingContext2D对象在画布上进行自定义图形的绘制，如下示例代码实现了在画布的中心绘制了一个笑脸。
```typescript
@Entry
@Component
struct CustomCanvasDrawingCard {
private canvasWidth: number = 0;
private canvasHeight: number = 0;
// 初始化CanvasRenderingContext2D和RenderingContextSettings
private settings: RenderingContextSettings = new RenderingContextSettings(true);
private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
build() {
Column() {
Row() {
Canvas(this.context)
.width('100%')
.height('100%')
.onReady(() => {
// 在onReady回调中获取画布的实际宽和高
this.canvasWidth = this.context.width;
this.canvasHeight = this.context.height;
// 绘制画布的背景
this.context.fillStyle = '#EEF0FF';
this.context.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
// 在画布的中心绘制一个圆
this.context.beginPath();
let radius = this.context.width / 3;
let circleX = this.context.width / 2;
let circleY = this.context.height / 2;
this.context.moveTo(circleX - radius, circleY);
this.context.arc(circleX, circleY, radius, 2 * Math.PI, 0, true);
this.context.closePath();
this.context.fillStyle = '#5A5FFF';
this.context.fill();
// 绘制笑脸的左眼
let leftR = radius / 13;
let leftX = circleX - (radius / 2.3);
let leftY = circleY - (radius / 4.5);
this.context.beginPath();
this.context.arc(leftX, leftY, leftR, 0, 2 * Math.PI, true);
this.context.closePath();
this.context.strokeStyle = '#FFFFFF';
this.context.lineWidth = 15;
this.context.stroke();
// 绘制笑脸的右眼
let rightR = radius / 13;
let rightX = circleX + (radius / 2.3);
let rightY = circleY - (radius / 4.5);
this.context.beginPath();
this.context.arc(rightX, rightY, rightR, 0, 2 * Math.PI, true);
this.context.closePath();
this.context.strokeStyle = '#FFFFFF';
this.context.lineWidth = 15;
this.context.stroke();
// 绘制笑脸的鼻子
let startX = circleX;
let startY = circleY - 20;
this.context.beginPath();
this.context.moveTo(startX, startY);
this.context.lineTo(startX - 8, startY + 40);
this.context.lineTo(startX + 8, startY + 40);
this.context.strokeStyle = '#FFFFFF';
this.context.lineWidth = 15;
this.context.lineCap = 'round';
this.context.lineJoin = 'round';
this.context.stroke();
// 绘制笑脸的嘴巴
let mouthR = radius / 2;
let mouthX = circleX;
let mouthY = circleY + 10;
this.context.beginPath();
this.context.arc(mouthX, mouthY, mouthR, Math.PI / 1.4, Math.PI / 3.4, true);
this.context.strokeStyle = '#FFFFFF';
this.context.lineWidth = 15;
this.context.stroke();
this.context.closePath();
})
}
}.height('100%').width('100%')
}
}
```
运行效果如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170416.38538411091323031929435403695219:50001231000000:2800:974C0DA5139E36A5A2B3087D720451D52BC25E3334A462D1F8297CC23DF63930.jpeg)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-event-V14
爬取时间: 2025-04-28 00:41:56
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-event-overview-V14
爬取时间: 2025-04-28 00:42:09
来源: Huawei Developer
针对动态卡片，ArkTS卡片中提供了postCardAction接口用于卡片内部和提供方应用间的交互，当前支持router、message和call三种类型的事件，仅在卡片中可以调用。
针对静态卡片，ArkTS卡片提供了FormLink用于卡片内部和提供方应用间的交互。
动态卡片事件能力说明
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170416.96440323116953906205965446099394:50001231000000:2800:F0A86D161FF1211EDC27655E1F52267C2FCE8F369255F509179D239C2104B517.png)
动态卡片事件的主要使用场景如下：
静态卡片事件能力说明
请参见FormLink

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-event-router-V14
爬取时间: 2025-04-28 00:42:22
来源: Huawei Developer
在动态卡片中使用postCardAction接口的router能力，能够快速拉起动态卡片提供方应用的指定UIAbility(页面)，因此UIAbility较多的应用往往会通过卡片提供不同的跳转按钮，实现一键直达的效果。例如相机卡片，卡片上提供拍照、录像等按钮，点击不同按钮将拉起相机应用的不同UIAbility，从而提高用户的体验。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170417.01494820549313582935590592609915:50001231000000:2800:C3C1E95CD47E0C2ED225559AAC5983A82D31BA4D5293DD0FB293052C0B62CC67.png)
本文主要介绍动态卡片的事件开发。对于静态卡片，请参见FormLink。
开发步骤
1.  创建动态卡片 在工程的 entry 模块中，新建名为WidgetEventRouterCard的ArkTs卡片。
2.  构建ArkTs卡片页面代码布局 卡片页面布局中有两个按钮，点击其中一个按钮时调用postCardAction向指定UIAbility发送router事件，并在事件内定义需要传递的内容。
```typescript
//src/main/ets/widgeteventroutercard/pages/WidgetEventRouterCard.ets
@Entry
@Component
struct WidgetEventRouterCard {
build() {
Column() {
Text($r('app.string.JumpLabel'))
.fontColor('#FFFFFF')
.opacity(0.9)
.fontSize(14)
.margin({ top: '8%', left: '10%' })
Row() {
Column() {
Button() {
Text($r('app.string.ButtonA_label'))
.fontColor('#45A6F4')
.fontSize(12)
}
.width(120)
.height(32)
.margin({ top: '20%' })
.backgroundColor('#FFFFFF')
.borderRadius(16)
.onClick(() => {
postCardAction(this, {
action: 'router',
abilityName: 'EntryAbility',
params: { targetPage: 'funA' }
});
})
Button() {
Text($r('app.string.ButtonB_label'))
.fontColor('#45A6F4')
.fontSize(12)
}
.width(120)
.height(32)
.margin({ top: '8%', bottom: '15vp' })
.backgroundColor('#FFFFFF')
.borderRadius(16)
.onClick(() => {
postCardAction(this, {
action: 'router',
abilityName: 'EntryAbility',
params: { targetPage: 'funB' }
});
})
}
}.width('100%').height('80%')
.justifyContent(FlexAlign.Center)
}
.width('100%')
.height('100%')
.alignItems(HorizontalAlign.Start)
.backgroundImage($r('app.media.CardEvent'))
.backgroundImageSize(ImageSize.Cover)
}
}
```
3.  处理router事件 在UIAbility中接收router事件并获取参数，根据传递的params不同，选择拉起不同的页面。
```typescript
//src/main/ets/entryability/EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'EntryAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class EntryAbility extends UIAbility {
private selectPage: string = '';
private currentWindowStage: window.WindowStage | null = null;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
// 获取router事件中传递的targetPage参数
hilog.info(DOMAIN_NUMBER, TAG, `Ability onCreate: ${JSON.stringify(want?.parameters)}`);
if (want?.parameters?.params) {
// want.parameters.params 对应 postCardAction() 中 params 内容
let params: Record<string, Object> = JSON.parse(want.parameters.params as string);
this.selectPage = params.targetPage as string;
hilog.info(DOMAIN_NUMBER, TAG, `onCreate selectPage: ${this.selectPage}`);
}
}
// 如果UIAbility已在后台运行，在收到Router事件后会触发onNewWant生命周期回调
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(DOMAIN_NUMBER, TAG, `Ability onNewWant: ${JSON.stringify(want?.parameters)}`);
if (want?.parameters?.params) {
// want.parameters.params 对应 postCardAction() 中 params 内容
let params: Record<string, Object> = JSON.parse(want.parameters.params as string);
this.selectPage = params.targetPage as string;
hilog.info(DOMAIN_NUMBER, TAG, `onNewWant selectPage: ${this.selectPage}`);
}
if (this.currentWindowStage !== null) {
this.onWindowStageCreate(this.currentWindowStage);
}
}
onWindowStageCreate(windowStage: window.WindowStage): void {
// Main window is created, set main page for this ability
let targetPage: string;
// 根据传递的targetPage不同，选择拉起不同的页面
switch (this.selectPage) {
case 'funA':
targetPage = 'pages/FunA'; //与实际的UIAbility页面路径保持一致
break;
case 'funB':
targetPage = 'pages/FunB'; //与实际的UIAbility页面路径保持一致
break;
default:
targetPage = 'pages/Index'; //与实际的UIAbility页面路径保持一致
}
if (this.currentWindowStage === null) {
this.currentWindowStage = windowStage;
}
windowStage.loadContent(targetPage, (err, data) => {
if (err.code) {
hilog.error(DOMAIN_NUMBER, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
});
}
}
```
4.  创建跳转后的UIAbility页面 在pages文件夹下新建FunA.ets和FunB.ets，构建页面布局。
```typescript
//src/main/ets/pages/FunA.ets
@Entry
@Component
struct FunA {
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
}
.height('100%')
.width('100%')
}
}
```
5.  注册UIAbility页面 打开main_pages.json，将新建的FunA.ets和FunB.ets正确注册在src数组中。
```typescript
//src/main/resources/base/profile/main_pages.json
{
"src": [
"pages/Index",
"pages/FunA",
"pages/FunB"
]
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-event-call-V14
爬取时间: 2025-04-28 00:42:35
来源: Huawei Developer
许多应用希望借助卡片的能力，实现和应用在前台时相同的功能。例如音乐卡片，卡片上提供播放、暂停等按钮，点击不同按钮将触发音乐应用的不同功能，进而提高用户的体验。在卡片中使用postCardAction接口的call能力，能够将卡片提供方应用的指定的UIAbility拉到后台。同时，call能力提供了调用应用指定方法、传递数据的功能，使应用在后台运行时可以通过卡片上的按钮执行不同的功能。
本文主要介绍动态卡片的事件开发。对于静态卡片，请参见FormLink。
开发步骤
1.  创建动态卡片 新建一个名为WidgetEventCallCardArkTs动态卡片。
2.  页面布局代码实现 在卡片页面中布局两个按钮，点击其中一个按钮时调用postCardAction向指定UIAbility发送call事件，并在事件内定义需要调用的方法和传递的数据。需要注意的是，method参数为必选参数，且类型需要为string类型，用于触发UIAbility中对应的方法。
```typescript
//src/main/ets/widgeteventcallcard/pages/WidgetEventCallCardCard.ets
@Entry
@Component
struct WidgetEventCallCard {
@LocalStorageProp('formId') formId: string = '12400633174999288';
build() {
Column() {
//...
Row() {
Column() {
Button() {
//...
}
//...
.onClick(() => {
postCardAction(this, {
action: 'call',
abilityName: 'WidgetEventCallEntryAbility', // 只能跳转到当前应用下的UIAbility，与module.json5中定义保持
params: {
formId: this.formId,
method: 'funA' // 在EntryAbility中调用的方法名
}
});
})
Button() {
//...
}
//...
.onClick(() => {
postCardAction(this, {
action: 'call',
abilityName: 'WidgetEventCallEntryAbility', // 只能跳转到当前应用下的UIAbility，与module.json5中定义保持
params: {
formId: this.formId,
method: 'funB', // 在EntryAbility中调用的方法名
num: 1 // 需要传递的其他参数
}
});
})
}
}.width('100%').height('80%')
.justifyContent(FlexAlign.Center)
}
.width('100%')
.height('100%')
.alignItems(HorizontalAlign.Center)
}
}
```
3.  创建指定的UIAbility 在UIAbility中接收call事件并获取参数，根据传递的method不同，执行不同的方法。其余数据可以通过readString方法获取。需要注意的是，UIAbility需要onCreate生命周期中监听所需的方法。
```typescript
//src/main/ets/widgeteventcallcard/WidgetEventCallEntryAbility/WidgetEventCallEntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'WidgetEventCallEntryAbility';
const DOMAIN_NUMBER: number = 0xFF00;
const CONST_NUMBER_1: number = 1;
const CONST_NUMBER_2: number = 2;
class MyParcelable implements rpc.Parcelable {
num: number;
str: string;
constructor(num: number, str: string) {
this.num = num;
this.str = str;
}
marshalling(messageSequence: rpc.MessageSequence): boolean {
messageSequence.writeInt(this.num);
messageSequence.writeString(this.str);
return true;
}
unmarshalling(messageSequence: rpc.MessageSequence): boolean {
this.num = messageSequence.readInt();
this.str = messageSequence.readString();
return true;
}
}
export default class WidgetEventCallEntryAbility extends UIAbility {
// 如果UIAbility第一次启动，在收到call事件后会触发onCreate生命周期回调
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
try {
// 监听call事件所需的方法
this.callee.on('funA', (data: rpc.MessageSequence) => {
// 获取call事件中传递的所有参数
hilog.info(DOMAIN_NUMBER, TAG, `FunACall param:  ${JSON.stringify(data.readString())}`);
promptAction.showToast({
message: 'FunACall param:' + JSON.stringify(data.readString())
});
return new MyParcelable(CONST_NUMBER_1, 'aaa');
});
this.callee.on('funB', (data: rpc.MessageSequence) => {
// 获取call事件中传递的所有参数
hilog.info(DOMAIN_NUMBER, TAG, `FunBCall param:  ${JSON.stringify(data.readString())}`);
promptAction.showToast({
message: 'FunBCall param:' + JSON.stringify(data.readString())
});
return new MyParcelable(CONST_NUMBER_2, 'bbb');
});
} catch (err) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to register callee on. Cause: ${JSON.stringify(err as BusinessError)}`);
}
}
// 进程退出时，解除监听
onDestroy(): void | Promise<void> {
try {
this.callee.off('funA');
this.callee.off('funB');
} catch (err) {
hilog.error(DOMAIN_NUMBER, TAG, `Failed to register callee off. Cause: ${JSON.stringify(err as BusinessError)}`);
}
}
}
```
4.  配置后台运行权限 call事件含有约束限制：提供方应用需要在module.json5顶层对象module下添加后台运行权限(ohos.permission.KEEP_BACKGROUND_RUNNING)。
```typescript
//src/main/module.json5
"requestPermissions"：[
{
"name": "ohos.permission.KEEP_BACKGROUND_RUNNING"
}
]
```
5.  配置指定的UIAbility 在module.json5顶层对象module的abilities数组内添加WidgetEventCallEntryAbility对应的配置信息。
```typescript
//src/main/module.json5
"abilities": [
{
"name": 'WidgetEventCallEntryAbility',
"srcEntry": './ets/widgeteventcallcard/WidgetEventCallEntryAbility/WidgetEventCallEntryAbility.ets',
"description": '$string:WidgetEventCallCard_desc',
"icon": "$media:app_icon",
"label": "$string:WidgetEventCallCard_label",
"startWindowIcon": "$media:app_icon",
"startWindowBackground": "$color:start_window_background"
}
]
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-event-formextensionability-V14
爬取时间: 2025-04-28 00:42:49
来源: Huawei Developer
在卡片页面中可以通过postCardAction接口触发message事件拉起FormExtensionAbility，然后由FormExtensionAbility刷新卡片内容，下面是这种刷新方式的简单示例。
本文主要介绍动态卡片的事件开发。对于静态卡片，请参见FormLink。
-  在卡片页面通过注册Button的onClick点击事件回调，并在回调中调用postCardAction接口触发message事件拉起FormExtensionAbility。卡片页面中使用LocalStorageProp装饰需要刷新的卡片数据。
```typescript
let storageUpdateByMsg = new LocalStorage();
@Entry(storageUpdateByMsg)
@Component
struct UpdateByMessageCard {
@LocalStorageProp('title') title: ResourceStr = $r('app.string.default_title');
@LocalStorageProp('detail') detail: ResourceStr = $r('app.string.DescriptionDefault');
build() {
Column() {
Column() {
Text(this.title)
.fontColor('#FFFFFF')
.opacity(0.9)
.fontSize(14)
.margin({ top: '8%', left: '10%' })
Text(this.detail)
.fontColor('#FFFFFF')
.opacity(0.6)
.fontSize(12)
.margin({ top: '5%', left: '10%' })
}.width('100%').height('50%')
.alignItems(HorizontalAlign.Start)
Row() {
Button() {
Text($r('app.string.update'))
.fontColor('#45A6F4')
.fontSize(12)
}
.width(120)
.height(32)
.margin({ top: '30%', bottom: '10%' })
.backgroundColor('#FFFFFF')
.borderRadius(16)
.onClick(() => {
postCardAction(this, {
action: 'message',
params: { msgTest: 'messageEvent' }
});
})
}.width('100%').height('40%')
.justifyContent(FlexAlign.Center)
}
.width('100%')
.height('100%')
.alignItems(HorizontalAlign.Start)
.backgroundImage($r('app.media.CardEvent'))
.backgroundImageSize(ImageSize.Cover)
}
}
```
-  在FormExtensionAbility的onFormEvent生命周期中调用updateForm接口刷新卡片。 运行效果如下图所示。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'EntryFormAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class EntryFormAbility extends FormExtensionAbility {
onFormEvent(formId: string, message: string): void {
// Called when a specified message event defined by the form provider is triggered.
hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${JSON.stringify(message)}`);
class FormDataClass {
title: string = 'Title Update.'; // 和卡片布局中对应
detail: string = 'Description update success.'; // 和卡片布局中对应
}
let formData = new FormDataClass();
let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
formProvider.updateForm(formId, formInfo).then(() => {
hilog.info(DOMAIN_NUMBER, TAG, 'FormAbility updateForm success.');
}).catch((error: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, `Operation updateForm failed. Cause: ${JSON.stringify(error)}`);
})
}
//...
}
```
| 初始状态 | 点击刷新 |
| --- | --- |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170417.35327533506558944915002297951015:50001231000000:2800:9C1C4B8275247345097185905C1A056C62163292C98CE5301A0C9F10617B4073.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170417.01949358665236456951819662974787:50001231000000:2800:759F83C80DEBD95B2B27D92F0FB88F1BFB9D51D15A93D88A48FEF4C5551C97DF.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-event-uiability-V14
爬取时间: 2025-04-28 00:43:02
来源: Huawei Developer
使用router事件，点击卡片可拉起对应应用的UIAbility至前台，并刷新卡片。使用call事件，点击卡片可拉起对应应用的UIAbility至后台，并刷新卡片。在卡片页面中可以通过postCardAction接口触发router事件或者call事件拉起UIAbility，然后由UIAbility刷新卡片内容，下面是这种刷新方式的简单示例。
本文主要介绍动态卡片的事件开发。对于静态卡片，请参见FormLink。
通过router事件刷新卡片内容
-  在卡片页面代码文件中，通过注册Button的onClick点击事件回调并在回调中调用postCardAction接口，触发router事件拉起UIAbility至前台。
```typescript
let storageUpdateRouter = new LocalStorage();
@Entry(storageUpdateRouter)
@Component
struct WidgetUpdateRouterCard {
@LocalStorageProp('routerDetail') routerDetail: ResourceStr = $r('app.string.init');
build() {
Column() {
Column() {
Text(this.routerDetail)
.fontColor('#FFFFFF')
.opacity(0.9)
.fontSize(14)
.margin({ top: '8%', left: '10%', right: '10%' })
.textOverflow({ overflow: TextOverflow.Ellipsis })
.maxLines(2)
}.width('100%').height('50%')
.alignItems(HorizontalAlign.Start)
Row() {
Button() {
Text($r('app.string.JumpLabel'))
.fontColor('#45A6F4')
.fontSize(12)
}
.width(120)
.height(32)
.margin({ top: '30%', bottom: '10%' })
.backgroundColor('#FFFFFF')
.borderRadius(16)
.onClick(() => {
postCardAction(this, {
action: 'router',
abilityName: 'WidgetEventRouterEntryAbility', // 只能跳转到当前应用下的UIAbility
params: {
routerDetail: 'RouterFromCard',
}
});
})
}.width('100%').height('40%')
.justifyContent(FlexAlign.Center)
}
.width('100%')
.height('100%')
.alignItems(HorizontalAlign.Start)
.backgroundImage($r('app.media.CardEvent'))
.backgroundImageSize(ImageSize.Cover)
}
}
```
-  在UIAbility的onCreate或者onNewWant生命周期中可以通过入参want获取卡片的formID和传递过来的参数信息，然后调用updateForm接口刷新卡片。
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { formBindingData, formInfo, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'WidgetEventRouterEntryAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class WidgetEventRouterEntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
this.handleFormRouterEvent(want, 'onCreate');
}
handleFormRouterEvent(want: Want, source: string): void {
hilog.info(DOMAIN_NUMBER, TAG, `handleFormRouterEvent ${source}, Want: ${JSON.stringify(want)}`);
if (want.parameters && want.parameters[formInfo.FormParam.IDENTITY_KEY] !== undefined) {
let curFormId = want.parameters[formInfo.FormParam.IDENTITY_KEY].toString();
// want.parameters.params 对应 postCardAction() 中 params 内容
let message: string = (JSON.parse(want.parameters?.params as string))?.routerDetail;
hilog.info(DOMAIN_NUMBER, TAG, `UpdateForm formId: ${curFormId}, message: ${message}`);
let formData: Record<string, string> = {
'routerDetail': message + ' ' + source + ' UIAbility', // 和卡片布局中对应
};
let formMsg = formBindingData.createFormBindingData(formData);
formProvider.updateForm(curFormId, formMsg).then((data) => {
hilog.info(DOMAIN_NUMBER, TAG, 'updateForm success.', JSON.stringify(data));
}).catch((error: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, 'updateForm failed.', JSON.stringify(error));
});
}
}
// 如果UIAbility已在后台运行，在收到Router事件后会触发onNewWant生命周期回调
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(DOMAIN_NUMBER, TAG, 'onNewWant Want:', JSON.stringify(want));
this.handleFormRouterEvent(want, 'onNewWant');
}
onWindowStageCreate(windowStage: window.WindowStage): void {
hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');
windowStage.loadContent('pages/Index', (err, data) => {
if (err.code) {
hilog.error(DOMAIN_NUMBER, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
});
}
// ...
}
```
通过call事件刷新卡片内容
-  在卡片页面代码文件中，通过注册Button的onClick点击事件回调并在回调中调用postCardAction接口，触发call事件拉起UIAbility至后台。
```typescript
let storageUpdateCall = new LocalStorage();
@Entry(storageUpdateCall)
@Component
struct WidgetUpdateCallCard {
@LocalStorageProp('formId') formId: string = '12400633174999288';
@LocalStorageProp('calleeDetail') calleeDetail: ResourceStr = $r('app.string.init');
build() {
Column() {
Column() {
Text(this.calleeDetail)
.fontColor('#FFFFFF')
.opacity(0.9)
.fontSize(14)
.margin({ top: '8%', left: '10%' })
}.width('100%').height('50%')
.alignItems(HorizontalAlign.Start)
Row() {
Button() {
Text($r('app.string.CalleeJumpLabel'))
.fontColor('#45A6F4')
.fontSize(12)
}
.width(120)
.height(32)
.margin({ top: '30%', bottom: '10%' })
.backgroundColor('#FFFFFF')
.borderRadius(16)
.onClick(() => {
postCardAction(this, {
action: 'call',
abilityName: 'WidgetCalleeEntryAbility', // 只能拉起当前应用下的UIAbility
params: {
method: 'funA',
formId: this.formId,
calleeDetail: 'CallFrom'
}
});
})
}.width('100%').height('40%')
.justifyContent(FlexAlign.Center)
}
.width('100%')
.height('100%')
.alignItems(HorizontalAlign.Start)
.backgroundImage($r('app.media.CardEvent'))
.backgroundImageSize(ImageSize.Cover)
}
}
```
-  在UIAbility的onCreate生命周期中监听call事件所需的方法，然后在对应方法中调用updateForm接口刷新卡片。 要拉起UIAbility至后台，需要在module.json5配置文件中，配置ohos.permission.KEEP_BACKGROUND_RUNNING权限。
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { formBindingData, formProvider } from '@kit.FormKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'WidgetCalleeEntryAbility';
const DOMAIN_NUMBER: number = 0xFF00;
const MSG_SEND_METHOD: string = 'funA';
const CONST_NUMBER_1: number = 1;
class MyParcelable implements rpc.Parcelable {
num: number;
str: string;
constructor(num: number, str: string) {
this.num = num;
this.str = str;
};
marshalling(messageSequence: rpc.MessageSequence): boolean {
messageSequence.writeInt(this.num);
messageSequence.writeString(this.str);
return true;
};
unmarshalling(messageSequence: rpc.MessageSequence): boolean {
this.num = messageSequence.readInt();
this.str = messageSequence.readString();
return true;
};
}
// 在收到call事件后会触发callee监听的方法
let funACall = (data: rpc.MessageSequence): MyParcelable => {
// 获取call事件中传递的所有参数
let params: Record<string, string> = JSON.parse(data.readString());
if (params.formId !== undefined) {
let curFormId: string = params.formId;
let message: string = params.calleeDetail;
hilog.info(DOMAIN_NUMBER, TAG, `UpdateForm formId: ${curFormId}, message: ${message}`);
let formData: Record<string, string> = {
'calleeDetail': message
};
let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
formProvider.updateForm(curFormId, formMsg).then((data) => {
hilog.info(DOMAIN_NUMBER, TAG, `updateForm success. ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
hilog.error(DOMAIN_NUMBER, TAG, `updateForm failed: ${JSON.stringify(error)}`);
});
}
return new MyParcelable(CONST_NUMBER_1, 'aaa');
};
export default class WidgetCalleeEntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
try {
// 监听call事件所需的方法
this.callee.on(MSG_SEND_METHOD, funACall);
} catch (error) {
hilog.error(DOMAIN_NUMBER, TAG, `${MSG_SEND_METHOD} register failed with error ${JSON.stringify(error)}`);
}
}
onWindowStageCreate(windowStage: window.WindowStage): void {
// Main window is created, set main page for this ability
hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');
windowStage.loadContent('pages/Index', (err, data) => {
if (err.code) {
hilog.error(DOMAIN_NUMBER, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
});
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-interaction-V14
爬取时间: 2025-04-28 00:43:15
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-interaction-overview-V14
爬取时间: 2025-04-28 00:43:28
来源: Huawei Developer
ArkTS卡片框架为提供方提供了updateForm接口、为使用方提供了requestForm接口来实现主动触发卡片的页面刷新能力；另外卡片框架还会通过开发者声明的定时信息按需通知提供方进行卡片刷新。
卡片UI代码内通过LocalStorageProp可以获得提供方推送的需要刷新的卡片数据。
| 接口 | 是否系统能力 | 约束 |
| --- | --- | --- |
| updateForm | 否 | 1. 提供方调用。 2. 提供方仅允许刷新自己的卡片，其他提供方的卡片无法刷新。 |
| requestForm | 是 | 1. 使用方调用。 2. 仅允许刷新添加到当前使用方的卡片，添加到其他使用方的卡片无法刷新。 |
1. 提供方调用。
2. 提供方仅允许刷新自己的卡片，其他提供方的卡片无法刷新。
1. 使用方调用。
2. 仅允许刷新添加到当前使用方的卡片，添加到其他使用方的卡片无法刷新。
1. 提供方主动刷新卡片流程示意：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170417.05627149653657165713795095895539:50001231000000:2800:7548124CC98D7FC32FBA8AC93678791F20BB019398C07686EE2CD70B49C4F4F5.png)
卡片提供方应用运行过程中，如果识别到有要更新卡片数据的诉求，可以主动通过formProvider提供的updateForm接口更新卡片。
2. 使用方主动请求更新卡片流程示意：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170417.06657256114488230290352477524390:50001231000000:2800:4CD27695B9C6A01365722230A9DF4674645210D4A01FBC452DD082AAB4E0A468.png)
卡片使用方在运行过程中，如果检测到系统语言、深浅色有变化时，可以主动通过formHost提供的requestForm接口请求更新卡片，卡片管理服务会进而通知提供方完成卡片更新。
3. 卡片框架通知提供方定时更新卡片流程示意：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170417.08422055591953983875435696834968:50001231000000:2800:B10B1A61DB99262E38DD545F39451502A4FA96E3EC8A09DD90B4C93AAE9526D1.png)
根据卡片提供方开发者提前配置声明的定时刷新信息，卡片管理服务会根据定时信息、卡片可见状态、刷新次数等因素综合判断是否需要通知提供方更新卡片。
下面介绍卡片页面刷新的典型场景。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-update-by-time-V14
爬取时间: 2025-04-28 00:43:41
来源: Huawei Developer
当前卡片框架提供了如下几种按时间刷新卡片的方式：
-  定时刷新：表示在一定时间间隔内调用onUpdateForm的生命周期回调函数自动刷新卡片内容。可以在form_config.json配置文件的updateDuration字段中进行设置。例如，可以将updateDuration字段的值设置为2，表示刷新时间设置为每小时一次。
```json
{
"forms": [
{
"name": "UpdateDuration",
"description": "$string:widget_updateduration_desc",
"src": "./ets/updateduration/pages/UpdateDurationCard.ets",
"uiSyntax": "arkts",
"window": {
"designWidth": 720,
"autoDesignWidth": true
},
"colorMode": "auto",
"isDefault": true,
"updateEnabled": true,
"scheduledUpdateTime": "10:30",
"updateDuration": 2,
"defaultDimension": "2*2",
"supportDimensions": [
"2*2"
]
}
]
}
```
1.  在使用定时刷新时，需要在form_config.json配置文件中设置updateEnabled字段为true，以启用周期性刷新功能。
2.  为减少卡片被动周期刷新进程启动次数，降低卡片刷新功耗，应用市场在安装应用时可以为该应用配置刷新周期， 也可以为已经安装的应用动态配置刷新周期，用来限制卡片刷新周期的时长，以达到降低周期刷新进程启动次数的目的。 ● 当配置了updateDuration（定时刷新）后，若应用市场动态配置了该应用的刷新周期， 卡片框架会将form_config.json文件中配置的刷新周期与应用市场配置的刷新周期进行比较，取较长的刷新周期做为该卡片的定时刷新周期。 ● 若应用市场未动态配置该应用的刷新周期，则以form_config.json文件中配置的刷新周期为准。 ● 若该卡片取消定时刷新功能，该规则将无效。 ● 卡片定时刷新的更新周期单位为30分钟。应用市场配置的刷新周期范围是1~336，即最短为半小时(1 * 30min)刷新一次，最长为一周(336 * 30min)刷新一次。 ● 该规则从API11开始生效。若小于API11，则以form_config.json文件中配置的刷新周期为准。
-  下次刷新：表示指定卡片的下一次刷新时间。可以通过调用setFormNextRefreshTime接口来实现。最短刷新时间为5分钟。例如，可以在接口调用后的5分钟内刷新卡片内容。
```typescript
import { FormExtensionAbility, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = 'UpdateByTimeFormAbility';
const FIVE_MINUTE: number = 5;
const DOMAIN_NUMBER: number = 0xFF00;
export default class UpdateByTimeFormAbility extends FormExtensionAbility {
onFormEvent(formId: string, message: string): void {
// Called when a specified message event defined by the form provider is triggered.
hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${JSON.stringify(message)}`);
try {
// 设置过5分钟后更新卡片内容
formProvider.setFormNextRefreshTime(formId, FIVE_MINUTE, (err: BusinessError) => {
if (err) {
hilog.info(DOMAIN_NUMBER, TAG, `Failed to setFormNextRefreshTime. Code: ${err.code}, message: ${err.message}`);
return;
} else {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in setFormNextRefreshTiming.');
}
});
} catch (err) {
hilog.info(DOMAIN_NUMBER, TAG, `Failed to setFormNextRefreshTime. Code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
}
}
// ...
}
```
在触发定时、下次刷新后，系统会调用FormExtensionAbility的onUpdateForm生命周期回调，在回调中，可以使用updateForm进行提供方刷新卡片。onUpdateForm生命周期回调的使用请参见卡片生命周期管理。
约束限制：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-update-by-time-point-V14
爬取时间: 2025-04-28 00:43:55
来源: Huawei Developer
当前卡片框架提供了如下定点刷新卡片的方式：
-  定点刷新：表示在每天的某个特定时间点自动刷新卡片内容。可以在form_config.json配置文件中的scheduledUpdateTime字段中进行设置。例如，可以将刷新时间设置为每天的上午10点30分。
```json
{
"forms": [
{
"name": "ScheduledUpdateTime",
"description": "$string:widget_scheupdatetime_desc",
"src": "./ets/scheduledupdatetime/pages/ScheduledUpdateTimeCard.ets",
"uiSyntax": "arkts",
"window": {
"designWidth": 720,
"autoDesignWidth": true
},
"colorMode": "auto",
"isDefault": true,
"updateEnabled": true,
"scheduledUpdateTime": "10:30",
"updateDuration": 0,
"defaultDimension": "2*2",
"supportDimensions": [
"2*2"
]
}
]
}
```
在触发定点刷新后，系统会调用FormExtensionAbility的onUpdateForm生命周期回调，在回调中，可以使用updateForm进行提供方刷新卡片。onUpdateForm生命周期回调的使用请参见卡片生命周期管理。
当同时配置了定时刷新updateDuration和定点刷新scheduledUpdateTime时，定时刷新的优先级更高且定点刷新不会执行。如果想要配置定点刷新，则需要将updateDuration配置为0。
约束限制：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-image-update-V14
爬取时间: 2025-04-28 00:44:08
来源: Huawei Developer
在卡片上通常需要展示本地图片或从网络上下载的图片，获取本地图片和网络图片需要通过FormExtensionAbility来实现，如下示例代码介绍了如何在卡片上显示本地图片和网络图片。
1.  下载网络图片需要使用到网络能力，需要申请ohos.permission.INTERNET权限，配置方式请参见声明权限。
2.  在EntryFormAbility中的onAddForm生命周期回调中实现本地文件的刷新。
```typescript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { formBindingData, FormExtensionAbility } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'WgtImgUpdateEntryFormAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class WgtImgUpdateEntryFormAbility extends FormExtensionAbility {
// 在添加卡片时，打开一个本地图片并将图片内容传递给卡片页面显示
onAddForm(want: Want): formBindingData.FormBindingData {
// 假设在当前卡片应用的tmp目录下有一个本地图片：head.PNG
let tempDir = this.context.getApplicationContext().tempDir;
hilog.info(DOMAIN_NUMBER, TAG, `tempDir: ${tempDir}`);
let imgMap: Record<string, number> = {};
try {
// 打开本地图片并获取其打开后的fd
let file = fileIo.openSync(tempDir + '/' + 'head.PNG');
imgMap['imgBear'] = file.fd;
} catch (e) {
hilog.error(DOMAIN_NUMBER, TAG, `openSync failed: ${JSON.stringify(e as BusinessError)}`);
}
class FormDataClass {
text: string = 'Image: Bear';
loaded: boolean = true;
// 卡片需要显示图片场景, 必须和下列字段formImages 中的key 'imgBear' 相同。
imgName: string = 'imgBear';
// 卡片需要显示图片场景, 必填字段(formImages 不可缺省或改名), 'imgBear' 对应 fd
formImages: Record<string, number> = imgMap;
}
let formData = new FormDataClass();
// 将fd封装在formData中并返回至卡片页面
return formBindingData.createFormBindingData(formData);
}
//...
}
```
3.  在EntryFormAbility中的onFormEvent生命周期回调中实现网络文件的刷新。
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { http } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'WgtImgUpdateEntryFormAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class WgtImgUpdateEntryFormAbility extends FormExtensionAbility {
async onFormEvent(formId: string, message: string): Promise<void> {
let param: Record<string, string> = {
'text': '刷新中...'
};
let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
formProvider.updateForm(formId, formInfo);
// 注意：FormExtensionAbility在触发生命周期回调时被拉起，仅能在后台存在5秒
// 建议下载能快速下载完成的小文件，如在5秒内未下载完成，则此次网络图片无法刷新至卡片页面上
let netFile = 'https://cn-assets.gitee.com/assets/mini_app-e5eee5a21c552b69ae6bf2cf87406b59.jpg'; // 需要在此处使用真实的网络图片下载链接
let tempDir = this.context.getApplicationContext().tempDir;
let fileName = 'file' + Date.now();
let tmpFile = tempDir + '/' + fileName;
let imgMap: Record<string, number> = {};
class FormDataClass {
text: string = 'Image: Bear' + fileName;
loaded: boolean = true;
// 卡片需要显示图片场景, 必须和下列字段formImages 中的key fileName 相同。
imgName: string = fileName;
// 卡片需要显示图片场景, 必填字段(formImages 不可缺省或改名), fileName 对应 fd
formImages: Record<string, number> = imgMap;
}
let httpRequest = http.createHttp()
let data = await httpRequest.request(netFile);
if (data?.responseCode == http.ResponseCode.OK) {
try {
let imgFile = fileIo.openSync(tmpFile, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
imgMap[fileName] = imgFile.fd;
try{
let writeLen: number = await fileIo.write(imgFile.fd, data.result as ArrayBuffer);
hilog.info(DOMAIN_NUMBER, TAG, "write data to file succeed and size is:" + writeLen);
hilog.info(DOMAIN_NUMBER, TAG, 'ArkTSCard download complete: %{public}s', tmpFile);
try {
let formData = new FormDataClass();
let formInfo = formBindingData.createFormBindingData(formData);
await formProvider.updateForm(formId, formInfo);
hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'FormAbility updateForm success.');
} catch (error) {
hilog.error(DOMAIN_NUMBER, TAG, `FormAbility updateForm failed: ${JSON.stringify(error)}`);
}
} catch (err) {
hilog.error(DOMAIN_NUMBER, TAG, "write data to file failed with error message: " + err.message + ", error code: " + err.code);
} finally {
// 在fileIo.closeSync执行之前，确保formProvider.updateForm已执行完毕。
fileIo.closeSync(imgFile);
};
} catch (e) {
hilog.error(DOMAIN_NUMBER, TAG, `openSync failed: ${JSON.stringify(e as BusinessError)}`);
}
} else {
hilog.error(DOMAIN_NUMBER, TAG, `ArkTSCard download task failed`);
let param: Record<string, string> = {
'text': '刷新失败'
};
let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
formProvider.updateForm(formId, formInfo);
}
httpRequest.destroy();
}
}
```
4.  在卡片页面通过backgroundImage属性展示EntryFormAbility传递过来的卡片内容。
```typescript
let storageWidgetImageUpdate = new LocalStorage();
@Entry(storageWidgetImageUpdate)
@Component
struct WidgetImageUpdateCard {
@LocalStorageProp('text') text: ResourceStr = $r('app.string.loading');
@LocalStorageProp('loaded') loaded: boolean = false;
@LocalStorageProp('imgName') imgName: ResourceStr = $r('app.string.imgName');
build() {
Column() {
Column() {
Text(this.text)
.fontColor('#FFFFFF')
.opacity(0.9)
.fontSize(12)
.textOverflow({ overflow: TextOverflow.Ellipsis })
.maxLines(1)
.margin({ top: '8%', left: '10%' })
}.width('100%').height('50%')
.alignItems(HorizontalAlign.Start)
Row() {
Button() {
Text($r('app.string.update'))
.fontColor('#45A6F4')
.fontSize(12)
}
.width(120)
.height(32)
.margin({ top: '30%', bottom: '10%' })
.backgroundColor('#FFFFFF')
.borderRadius(16)
.onClick(() => {
postCardAction(this, {
action: 'message',
params: {
info: 'refreshImage'
}
});
})
}.width('100%').height('40%')
.justifyContent(FlexAlign.Center)
}
.width('100%').height('100%')
.backgroundImage(this.loaded ? 'memory://' + this.imgName : $r('app.media.ImageDisp'))
.backgroundImageSize(ImageSize.Cover)
}
}
```
-  Image组件通过入参(memory://fileName)中的(memory://)标识来进行远端内存图片显示，其中fileName需要和EntryFormAbility传递对象('formImages': {key: fd})中的key相对应。
-  Image组件通过传入的参数是否有变化来决定是否刷新图片，因此EntryFormAbility每次传递过来的imgName都需要不同，连续传递两个相同的imgName时，图片不会刷新。
-  在卡片上展示的图片，大小需要控制在2MB以内。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/arkts-ui-widget-update-by-status-V14
爬取时间: 2025-04-28 00:44:21
来源: Huawei Developer
相同的卡片可以添加到桌面上实现不同的功能，比如添加两张桌面的卡片，一张显示杭州的天气，一张显示北京的天气，设置每天早上7点触发定时刷新，卡片需要感知当前的配置是杭州还是北京，然后将对应城市的天气信息刷新到卡片上，以下示例介绍了如何根据卡片的状态动态选择需要刷新的内容。
-  卡片配置文件：配置每30分钟自动刷新。
```json
{
"forms": [
{
"name": "WidgetUpdateByStatus",
"description": "$string:UpdateByStatusFormAbility_desc",
"src": "./ets/widgetupdatebystatus/pages/WidgetUpdateByStatusCard.ets",
"uiSyntax": "arkts",
"window": {
"designWidth": 720,
"autoDesignWidth": true
},
"colorMode": "auto",
"isDefault": true,
"updateEnabled": true,
"scheduledUpdateTime": "10:30",
"updateDuration": 1,
"defaultDimension": "2*2",
"supportDimensions": [
"2*2"
]
}
]
}
```
-  卡片页面：卡片具备不同的状态选择，在不同的状态下需要刷新不同的内容，因此在状态发生变化时通过postCardAction通知EntryFormAbility。
```typescript
let storageUpdateByStatus = new LocalStorage();
@Entry(storageUpdateByStatus)
@Component
struct WidgetUpdateByStatusCard {
@LocalStorageProp('textA') textA: Resource = $r('app.string.to_be_refreshed');
@LocalStorageProp('textB') textB: Resource = $r('app.string.to_be_refreshed');
@State selectA: boolean = false;
@State selectB: boolean = false;
build() {
Column() {
Column() {
Row() {
Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
.padding(0)
.select(false)
.margin({ left: 26 })
.onChange((value: boolean) => {
this.selectA = value;
postCardAction(this, {
action: 'message',
params: {
selectA: JSON.stringify(value)
}
});
})
Text($r('app.string.status_a'))
.fontColor('#000000')
.opacity(0.9)
.fontSize(14)
.margin({ left: 8 })
}
.width('100%')
.padding(0)
.justifyContent(FlexAlign.Start)
Row() {
Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
.padding(0)
.select(false)
.margin({ left: 26 })
.onChange((value: boolean) => {
this.selectB = value;
postCardAction(this, {
action: 'message',
params: {
selectB: JSON.stringify(value)
}
});
})
Text($r('app.string.status_b'))
.fontColor('#000000')
.opacity(0.9)
.fontSize(14)
.margin({ left: 8 })
}
.width('100%')
.position({ y: 32 })
.padding(0)
.justifyContent(FlexAlign.Start)
}
.position({ y: 12 })
Column() {
Row() { // 选中状态A才会进行刷新的内容
Text($r('app.string.status_a'))
.fontColor('#000000')
.opacity(0.4)
.fontSize(12)
Text(this.textA)
.fontColor('#000000')
.opacity(0.4)
.fontSize(12)
}
.margin({ top: '12px', left: 26, right: '26px' })
Row() { // 选中状态B才会进行刷新的内容
Text($r('app.string.status_b'))
.fontColor('#000000')
.opacity(0.4)
.fontSize(12)
Text(this.textB)
.fontColor('#000000')
.opacity(0.4)
.fontSize(12)
}.margin({ top: '12px', bottom: '21px', left: 26, right: '26px' })
}
.margin({ top: 80 })
.width('100%')
.alignItems(HorizontalAlign.Start)
}.width('100%').height('100%')
.backgroundImage($r('app.media.CardUpdateByStatus'))
.backgroundImageSize(ImageSize.Cover)
}
}
```
-  EntryFormAbility：将卡片的状态存储在本地数据库中，在刷新事件回调触发时，通过formId获取当前卡片的状态，然后根据卡片的状态选择不同的刷新内容。
```typescript
import { Want } from '@kit.AbilityKit';
import { preferences } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'UpdateByStatusFormAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class UpdateByStatusFormAbility extends FormExtensionAbility {
onAddForm(want: Want): formBindingData.FormBindingData {
let formId: string = '';
let isTempCard: boolean;
if (want.parameters) {
formId = want.parameters[formInfo.FormParam.IDENTITY_KEY].toString();
isTempCard = want.parameters[formInfo.FormParam.TEMPORARY_KEY] as boolean;
if (isTempCard === false) { // 如果为常态卡片，直接进行信息持久化
hilog.info(DOMAIN_NUMBER, TAG, 'Not temp card, init db for:' + formId);
let promise: Promise<preferences.Preferences> = preferences.getPreferences(this.context, 'myStore');
promise.then(async (storeDB: preferences.Preferences) => {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences.');
await storeDB.put('A' + formId, 'false');
await storeDB.put('B' + formId, 'false');
await storeDB.flush();
}).catch((err: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
});
}
}
let formData: Record<string, Object | string> = {};
return formBindingData.createFormBindingData(formData);
}
onRemoveForm(formId: string): void {
hilog.info(DOMAIN_NUMBER, TAG, 'onRemoveForm, formId:' + formId);
let promise = preferences.getPreferences(this.context, 'myStore');
promise.then(async (storeDB) => {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences.');
await storeDB.delete('A' + formId);
await storeDB.delete('B' + formId);
}).catch((err: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
});
}
// 如果在添加时为临时卡片，则建议转为常态卡片时进行信息持久化
onCastToNormalForm(formId: string): void {
hilog.info(DOMAIN_NUMBER, TAG, 'onCastToNormalForm, formId:' + formId);
let promise: Promise<preferences.Preferences> = preferences.getPreferences(this.context, 'myStore');
promise.then(async (storeDB: preferences.Preferences) => {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences.');
await storeDB.put('A' + formId, 'false');
await storeDB.put('B' + formId, 'false');
await storeDB.flush();
}).catch((err: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
});
}
onUpdateForm(formId: string): void {
let promise: Promise<preferences.Preferences> = preferences.getPreferences(this.context, 'myStore');
promise.then(async (storeDB: preferences.Preferences) => {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences from onUpdateForm.');
let stateA = await storeDB.get('A' + formId, 'false');
let stateB = await storeDB.get('B' + formId, 'false');
// A状态选中则更新textA
if (stateA === 'true') {
let param: Record<string, string> = {
'textA': 'AAA'
};
let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
await formProvider.updateForm(formId, formInfo);
}
// B状态选中则更新textB
if (stateB === 'true') {
let param: Record<string, string> = {
'textB': 'BBB'
};
let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
await formProvider.updateForm(formId, formInfo);
}
hilog.info(DOMAIN_NUMBER, TAG, `Update form success stateA:${stateA} stateB:${stateB}.`);
}).catch((err: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
});
}
onFormEvent(formId: string, message: string): void {
// 存放卡片状态
hilog.info(DOMAIN_NUMBER, TAG, 'onFormEvent formId:' + formId + 'msg:' + message);
let promise: Promise<preferences.Preferences> = preferences.getPreferences(this.context, 'myStore');
promise.then(async (storeDB: preferences.Preferences) => {
hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences.');
let msg: Record<string, string> = JSON.parse(message);
if (msg.selectA !== undefined) {
hilog.info(DOMAIN_NUMBER, TAG, 'onFormEvent selectA info:' + msg.selectA);
await storeDB.put('A' + formId, msg.selectA);
}
if (msg.selectB !== undefined) {
hilog.info(DOMAIN_NUMBER, TAG, 'onFormEvent selectB info:' + msg.selectB);
await storeDB.put('B' + formId, msg.selectB);
}
await storeDB.flush();
}).catch((err: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
});
}
}
```
通过本地数据库进行卡片信息的持久化时，建议先在onAddForm生命周期中通过TEMPORARY_KEY判断当前添加的卡片是否为常态卡片：如果是常态卡片，则直接进行卡片信息持久化；如果为临时卡片，则可以在卡片转为常态卡片(onCastToNormalForm)时进行持久化；同时需要在卡片销毁(onRemoveForm)时删除当前卡片存储的持久化信息，避免反复添加删除卡片导致数据库文件持续变大。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/js-ui-widget-development-V14
爬取时间: 2025-04-28 00:44:34
来源: Huawei Developer
以下内容介绍基于类Web范式的JS UI卡片开发指南。
运作机制
卡片框架的运作机制如图1所示。
图1卡片框架运作机制（Stage模型）
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170418.07762351553664239918441505770547:50001231000000:2800:E780E9706EA02AC59204388A3E57FA05DF5F9CA8ABC374D6ACE4309B7B62E069.png)
卡片使用方包含以下模块：
-  卡片使用：包含卡片的创建、删除、请求更新等操作。
-  通信适配层：由HarmonyOS SDK提供，负责与卡片管理服务通信，用于将卡片的相关操作到卡片管理服务。
卡片管理服务包含以下模块：
-  周期性刷新：在卡片添加后，根据卡片的刷新策略启动定时任务周期性触发卡片的刷新。
-  卡片缓存管理：在卡片添加到卡片管理服务后，对卡片的视图信息进行缓存，以便下次获取卡片时可以直接返回缓存数据，降低时延。
-  卡片生命周期管理：对于卡片切换到后台或者被遮挡时，暂停卡片的刷新；以及卡片的升级/卸载场景下对卡片数据的更新和清理。
-  卡片使用方对象管理：对卡片使用方的RPC对象进行管理，用于使用方请求进行校验以及对卡片更新后的回调处理。
-  通信适配层：负责与卡片使用方和提供方进行RPC通信。
卡片提供方包含以下模块：
-  卡片服务：由卡片提供方开发者实现，开发者实现生命周期处理创建卡片、更新卡片以及删除卡片等请求，提供相应的卡片服务。
-  卡片提供方实例管理模块：由卡片提供方开发者实现，负责对卡片管理服务分配的卡片实例进行持久化管理。
-  通信适配层：由HarmonyOS SDK提供，负责与卡片管理服务通信，用于将卡片的更新数据主动推送到卡片管理服务。
实际开发时只需要作为卡片提供方进行卡片内容的开发，卡片使用方和卡片管理服务由系统自动处理。
接口说明
FormExtensionAbility类拥有如下API接口，具体的API介绍详见接口文档。
| 接口名 | 描述 |
| --- | --- |
| onAddForm(want: Want): formBindingData.FormBindingData | 卡片提供方接收创建卡片的通知接口。 |
| onCastToNormalForm(formId: string): void | 卡片提供方接收临时卡片转常态卡片的通知接口。 |
| onUpdateForm(formId: string): void | 卡片提供方接收更新卡片的通知接口。 |
| onChangeFormVisibility(newStatus: Record<string, number>): void | 卡片提供方接收修改可见性的通知接口。 |
| onFormEvent(formId: string, message: string): void | 卡片提供方接收处理卡片事件的通知接口。 |
| onRemoveForm(formId: string): void | 卡片提供方接收销毁卡片的通知接口。 |
| onConfigurationUpdate(newConfig: Configuration): void | 当系统配置更新时调用。 |
| onShareForm?(formId: string): Record<string, Object> | 卡片提供方接收卡片分享的通知接口。 |
formProvider类有如下API接口，具体的API介绍详见接口文档。
| 接口名 | 描述 |
| --- | --- |
| setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void | 设置指定卡片的下一次更新时间。 |
| setFormNextRefreshTime(formId: string, minute: number): Promise<void> | 设置指定卡片的下一次更新时间，以promise方式返回。 |
| updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void | 更新指定的卡片。 |
| updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void> | 更新指定的卡片，以promise方式返回。 |
formBindingData类有如下API接口，具体的API介绍详见接口文档。
| 接口名 | 描述 |
| --- | --- |
| createFormBindingData(obj?: Object | string): FormBindingData | 创建一个FormBindingData对象。 |
开发步骤
Stage卡片开发，即基于Stage模型的卡片提供方开发，主要涉及如下关键步骤：
-  创建卡片FormExtensionAbility：卡片生命周期回调函数FormExtensionAbility开发。
-  配置卡片配置文件：配置应用配置文件module.json5和profile配置文件。
-  卡片信息的持久化：对卡片信息进行持久化管理。
-  卡片数据交互：通过updateForm更新卡片显示的信息。
-  开发卡片页面：使用HML+CSS+JSON开发JS卡片页面。
-  开发卡片事件：为卡片添加router事件和message事件。
创建卡片FormExtensionAbility
创建Stage模型的卡片，需实现FormExtensionAbility生命周期接口。先参考DevEco Studio服务卡片开发指南生成服务卡片模板。
1.  在EntryFormAbility.ets中，导入相关模块。
```typescript
import { Want } from '@kit.AbilityKit';
import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = 'JsCardFormAbility';
const DOMAIN_NUMBER: number = 0xFF00;
```
2.  在EntryFormAbility.ets中，实现FormExtension生命周期接口。
```typescript
export default class EntryFormAbility extends FormExtensionAbility {
onAddForm(want: Want): formBindingData.FormBindingData {
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onAddForm');
// 使用方创建卡片时触发，提供方需要返回卡片数据绑定类
let obj: Record<string, string> = {
'title': 'titleOnCreate',
'detail': 'detailOnCreate'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
return formData;
}
onCastToNormalForm(formId: string): void {
// 使用方将临时卡片转换为常态卡片触发，提供方需要做相应的处理
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onCastToNormalForm');
}
onUpdateForm(formId: string): void {
// 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
let obj: Record<string, string> = {
'title': 'titleOnUpdate',
'detail': 'detailOnUpdate'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
});
}
onChangeFormVisibility(newStatus: Record<string, number>): void {
// 使用方发起可见或者不可见通知触发，提供方需要做相应的处理，仅系统应用生效
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onChangeFormVisibility');
//...
}
onFormEvent(formId: string, message: string): void {
// 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onFormEvent');
}
onRemoveForm(formId: string): void {
// 删除卡片实例数据
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
//...
}
onAcquireFormState(want: Want): formInfo.FormState {
return formInfo.FormState.READY;
}
}
```
FormExtensionAbility不能常驻后台，即在卡片生命周期回调函数中无法处理长时间的任务。
配置卡片配置文件
1.  卡片需要在module.json5配置文件中的extensionAbilities标签下，配置ExtensionAbility相关信息。FormExtensionAbility需要填写metadata元信息标签，其中键名称为固定字符串"ohos.extension.form"，资源为卡片的具体配置信息的索引。 配置示例如下：
```json
{
"module": {
// ...
"extensionAbilities": [
{
"name": "JsCardFormAbility",
"srcEntry": "./ets/jscardformability/JsCardFormAbility.ts",
"description": "$string:JSCardFormAbility_desc",
"label": "$string:JSCardFormAbility_label",
"type": "form",
"metadata": [
{
"name": "ohos.extension.form",
"resource": "$profile:form_jscard_config"
}
]
}
]
}
}
```
2.  卡片的具体配置信息。在上述FormExtensionAbility的元信息（"metadata"配置项）中，可以指定卡片具体配置信息的资源索引。例如当resource指定为$profile:form_config时，会使用开发视图的resources/base/profile/目录下的form_config.json作为卡片profile配置文件。内部字段结构说明如下表所示。 表1卡片profile配置文件 表示该卡片是否为默认卡片，每个UIAbility有且只有一个默认卡片。 - true：默认卡片。 - false：非默认卡片。 表示卡片的主题样式，取值范围如下： - auto：自适应。 - dark：深色主题。 - light：浅色主题。 表示卡片支持的外观规格，取值范围： - 1 * 2：表示1行2列的二宫格。 - 2 * 2：表示2行2列的四宫格。 - 2 * 4：表示2行4列的八宫格。 - 4 * 4：表示4行4列的十六宫格。 表示卡片是否支持周期性刷新，取值范围： - true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，优先选择定时刷新。 - false：表示不支持周期性刷新。 表示卡片的定点刷新的时刻，采用24小时制，精确到分钟。 updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 表示卡片定时刷新的更新周期，单位为30分钟，取值为自然数。 当取值为0时，表示该参数不生效。 当取值为正整数N时，表示刷新周期为30*N分钟。 updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 配置示例如下：
```json
{
"forms": [
{
"name": "WidgetJS",
"description": "$string:JSCardEntryAbility_desc",
"src": "./js/WidgetJS/pages/index/index",
"window": {
"designWidth": 720,
"autoDesignWidth": true
},
"colorMode": "auto",
"isDefault": true,
"updateEnabled": true,
"scheduledUpdateTime": "10:30",
"updateDuration": 1,
"defaultDimension": "2*2",
"supportDimensions": [
"2*2"
]
}
]
}
```
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 表示卡片的类名，字符串最大长度为127字节。 | 字符串 | 否 |
| description | 表示卡片的描述。取值可以是描述性内容，也可以是对描述性内容的资源索引，以支持多语言。字符串最大长度为255字节。 | 字符串 | 可缺省，缺省为空。 |
| src | 表示卡片对应的UI代码的完整路径。 | 字符串 | 否 |
| window | 用于定义与显示窗口相关的配置。 | 对象 | 可缺省。 |
| isDefault | 表示该卡片是否为默认卡片，每个UIAbility有且只有一个默认卡片。 - true：默认卡片。 - false：非默认卡片。 | 布尔值 | 否 |
| colorMode | 表示卡片的主题样式，取值范围如下： - auto：自适应。 - dark：深色主题。 - light：浅色主题。 | 字符串 | 可缺省，缺省值为“auto”。 |
| supportDimensions | 表示卡片支持的外观规格，取值范围： - 1 * 2：表示1行2列的二宫格。 - 2 * 2：表示2行2列的四宫格。 - 2 * 4：表示2行4列的八宫格。 - 4 * 4：表示4行4列的十六宫格。 | 字符串数组 | 否 |
| defaultDimension | 表示卡片的默认外观规格，取值必须在该卡片supportDimensions配置的列表中。 | 字符串 | 否 |
| updateEnabled | 表示卡片是否支持周期性刷新，取值范围： - true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，优先选择定时刷新。 - false：表示不支持周期性刷新。 | 布尔类型 | 否 |
| scheduledUpdateTime | 表示卡片的定点刷新的时刻，采用24小时制，精确到分钟。 updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 字符串 | 可缺省，缺省值为“0:0”。 |
| updateDuration | 表示卡片定时刷新的更新周期，单位为30分钟，取值为自然数。 当取值为0时，表示该参数不生效。 当取值为正整数N时，表示刷新周期为30*N分钟。 updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 数值 | 可缺省，缺省值为“0”。 |
| formConfigAbility | 表示卡片的配置跳转链接，采用URI格式。 | 字符串 | 可缺省，缺省值为空。 |
| formVisibleNotify | 标识是否允许卡片使用卡片可见性通知。 | 字符串 | 可缺省，缺省值为空。 |
| metaData | 表示卡片的自定义信息，包含customizeData数组标签。 | 对象 | 可缺省，缺省值为空。 |
卡片信息的持久化
因大部分卡片提供方都不是常驻服务，只有在需要使用时才会被拉起获取卡片信息，且卡片管理服务支持对卡片进行多实例管理，卡片ID对应实例ID，因此若卡片提供方支持对卡片数据进行配置，则需要对卡片的业务数据按照卡片ID进行持久化管理，以便在后续获取、更新以及拉起时能获取到正确的卡片业务数据。
```typescript
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { formBindingData, FormExtensionAbility } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { preferences } from '@kit.ArkData';
const TAG: string = 'JsCardFormAbility';
const DATA_STORAGE_PATH: string = '/data/storage/el2/base/haps/form_store';
const DOMAIN_NUMBER: number = 0xFF00;
let storeFormInfo = async (formId: string, formName: string, tempFlag: boolean, context: common.FormExtensionContext): Promise<void> => {
// 此处仅对卡片ID：formId，卡片名：formName和是否为临时卡片：tempFlag进行了持久化
let formInfo: Record<string, string | boolean | number> = {
'formName': formName,
'tempFlag': tempFlag,
'updateCount': 0
};
try {
const storage: preferences.Preferences = await preferences.getPreferences(context, DATA_STORAGE_PATH);
// put form info
await storage.put(formId, JSON.stringify(formInfo));
hilog.info(DOMAIN_NUMBER, TAG, `[EntryFormAbility] storeFormInfo, put form info successfully, formId: ${formId}`);
await storage.flush();
} catch (err) {
hilog.error(DOMAIN_NUMBER, TAG, `[EntryFormAbility] failed to storeFormInfo, err: ${JSON.stringify(err as BusinessError)}`);
}
}
export default class JsCardFormAbility extends FormExtensionAbility {
onAddForm(want: Want): formBindingData.FormBindingData {
hilog.info(DOMAIN_NUMBER, TAG, '[JsCardFormAbility] onAddForm');
if (want.parameters) {
let formId = JSON.stringify(want.parameters['ohos.extra.param.key.form_identity']);
let formName = JSON.stringify(want.parameters['ohos.extra.param.key.form_name']);
let tempFlag = want.parameters['ohos.extra.param.key.form_temporary'] as boolean;
// 将创建的卡片信息持久化，以便在下次获取/更新该卡片实例时进行使用
// 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
storeFormInfo(formId, formName, tempFlag, this.context);
}
let obj: Record<string, string> = {
'title': 'titleOnCreate',
'detail': 'detailOnCreate'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
return formData;
}
}
```
且需要适配onRemoveForm卡片删除通知接口，在其中实现卡片实例数据的删除。
```typescript
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { FormExtensionAbility } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { preferences } from '@kit.ArkData';
const TAG: string = 'JsCardFormAbility';
const DATA_STORAGE_PATH: string = '/data/storage/el2/base/haps/form_store';
const DOMAIN_NUMBER: number = 0xFF00;
let deleteFormInfo = async (formId: string, context: common.FormExtensionContext): Promise<void> => {
try {
const storage: preferences.Preferences = await preferences.getPreferences(context, DATA_STORAGE_PATH);
// del form info
await storage.delete(formId);
hilog.info(DOMAIN_NUMBER, TAG, `[EntryFormAbility] deleteFormInfo, del form info successfully, formId: ${formId}`);
await storage.flush();
} catch (err) {
hilog.error(DOMAIN_NUMBER, TAG, `[EntryFormAbility] failed to deleteFormInfo, err: ${JSON.stringify(err as BusinessError)}`);
};
};
export default class JsCardFormAbility extends FormExtensionAbility {
onRemoveForm(formId: string): void {
// 删除卡片实例数据
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
// 删除之前持久化的卡片实例数据
// 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
deleteFormInfo(formId, this.context);
}
}
```
具体的持久化方法可以参考轻量级数据存储开发指导。
需要注意的是，卡片使用方在请求卡片时传递给提供方应用的Want数据中存在临时标记字段，表示此次请求的卡片是否为临时卡片：
-  常态卡片：卡片使用方会持久化的卡片。
-  临时卡片：卡片使用方不会持久化的卡片。
由于临时卡片的数据具有非持久化的特殊性，某些场景例如卡片服务框架死亡重启，此时临时卡片数据在卡片管理服务中已经删除，且对应的卡片ID不会通知到提供方，所以卡片提供方需要自己负责清理长时间未删除的临时卡片数据。同时对应的卡片使用方可能会将之前请求的临时卡片转换为常态卡片。如果转换成功，卡片提供方也需要对对应的临时卡片ID进行处理，把卡片提供方记录的临时卡片数据转换为常态卡片数据，防止提供方在清理长时间未删除的临时卡片时，把已经转换为常态卡片的临时卡片信息删除，导致卡片信息丢失。
卡片数据交互
当卡片应用需要更新数据时（如触发了定时更新或定点更新），卡片应用获取最新数据，并调用updateForm()接口主动触发卡片的更新。
```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = 'JsCardFormAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class EntryFormAbility extends FormExtensionAbility {
onUpdateForm(formId: string): void {
// 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
let obj: Record<string, string> = {
'title': 'titleOnUpdate',
'detail': 'detailOnUpdate'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
});
}
}
```
开发卡片页面
开发者可以使用类Web范式（HML+CSS+JSON）开发JS卡片页面。生成如下卡片页面，可以这样配置卡片页面文件：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170418.40988829035059070137533592218625:50001231000000:2800:9C543E857EA5CC8AD2579E0A3253D159253C8E6E3CA09B31500E79975B834D89.png)
-  HML：使用类Web范式的组件描述卡片的页面信息。
-  CSS：HML中类Web范式组件的样式信息。
-  JSON：卡片页面中的数据和事件交互。
```json
{
"data": {
"title": "TitleDefault",
"detail": "TextDefault"
},
"actions": {
"routerEvent": {
"action": "router",
"abilityName": "EntryAbility",
"params": {
"message": "add detail"
}
}
}
}
```
开发卡片事件
卡片支持为组件设置交互事件（action），包括router事件和message事件，其中router事件用于UIAbility跳转，message事件用于卡片开发人员自定义点击事件。
关键步骤说明如下：
1.  在HML中为组件设置onclick属性，其值对应到JSON文件的actions字段中。
2.  设置router事件：
3.  设置message事件：
示例如下。
-  HML文件
-  CSS文件
-  JSON文件 说明： "data"中JSON Value支持多级嵌套数据，在更新数据时，需要注意携带完整数据。 例如：当前卡片显示07.18日Mr.Zhang的课程信息，示例如下。 当卡片内容需要更新为07.18日Mr.Li的课程信息时，需要传递待更新的完整数据，不能只传递单个数据项，如只传name或只传course，示例如下。
```json
{
"data": {
"title": "TitleDefault",
"detail": "TextDefault"
},
"actions": {
"routerEvent": {
"action": "router",
"abilityName": "JSCardEntryAbility",
"params": {
"info": "router info",
"message": "router message"
}
},
"messageEvent": {
"action": "message",
"params": {
"detail": "message detail"
}
}
}
}
```
-  在UIAbility中接收router事件并获取参数
```typescript
import UIAbility from '@ohos.app.ability.UIAbility';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import Want from '@ohos.app.ability.Want';
import hilog from '@ohos.hilog';
const TAG: string = 'EtsCardEntryAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class EtsCardEntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
if (want.parameters) {
let params: Record<string, Object> = JSON.parse(JSON.stringify(want.parameters.params));
// 获取router事件中传递的info参数
if (params.info === 'router info') {
// 执行业务逻辑
hilog.info(DOMAIN_NUMBER, TAG, `router info: ${params.info}`);
}
// 获取router事件中传递的message参数
if (params.message === 'router message') {
// 执行业务逻辑
hilog.info(DOMAIN_NUMBER, TAG, `router message: ${params.message}`);
}
}
}
};
```
-  在FormExtensionAbility中接收message事件并获取参数
```typescript
import FormExtension from '@ohos.app.form.FormExtensionAbility';
import hilog from '@ohos.hilog';
const TAG: string = 'FormAbility';
const DOMAIN_NUMBER: number = 0xFF00;
export default class FormAbility extends FormExtension {
onFormEvent(formId: string, message: string): void {
// 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onFormEvent');
// 获取message事件中传递的detail参数
let msg: Record<string, string> = JSON.parse(message);
if (msg.detail === 'message detail') {
// 执行业务逻辑
hilog.info(DOMAIN_NUMBER, TAG, 'message info:' + msg.detail);
}
}
};
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/widget-development-fa-V14
爬取时间: 2025-04-28 00:44:48
来源: Huawei Developer
卡片概述
服务卡片（以下简称“卡片”）是一种界面展示形式，可以将应用的重要信息或操作前置到卡片，以达到服务直达、减少体验层级的目的。
卡片常用于嵌入到其他应用（当前只支持系统应用）中作为其界面的一部分显示，并支持拉起页面、发送消息等基础的交互功能。
卡片的基本概念：
-  卡片使用方：显示卡片内容的宿主应用，控制卡片在宿主中展示的位置。
-  卡片管理服务：用于管理系统中所添加卡片的常驻代理服务，包括卡片对象的管理与使用，以及卡片周期性刷新等。
-  卡片提供方：提供卡片显示内容元服务，控制卡片的显示内容、控件布局以及控件点击事件。
运作机制
卡片框架的运作机制如图1所示。
图1卡片框架运作机制（FA模型）
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170418.00000084229039050036882519440301:50001231000000:2800:B29A03416E3436BBB28895E9006FB1038634E5B3DF2A70D48A942E82BCDE8ED0.png)
卡片使用方包含以下模块：
-  卡片使用：包含卡片的创建、删除、请求更新等操作。
-  通信适配层：由HarmonyOS SDK提供，负责与卡片管理服务通信，用于将卡片的相关操作到卡片管理服务。
卡片管理服务包含以下模块：
-  周期性刷新：在卡片添加后，根据卡片的刷新策略启动定时任务周期性触发卡片的刷新。
-  卡片缓存管理：在卡片添加到卡片管理服务后，对卡片的视图信息进行缓存，以便下次获取卡片时可以直接返回缓存数据，降低时延。
-  卡片生命周期管理：对于卡片切换到后台或者被遮挡时，暂停卡片的刷新；以及卡片的升级/卸载场景下对卡片数据的更新和清理。
-  卡片使用方对象管理：对卡片使用方的RPC对象进行管理，用于使用方请求进行校验以及对卡片更新后的回调处理。
-  通信适配层：负责与卡片使用方和提供方进行RPC通信。
卡片提供方包含以下模块：
-  卡片服务：由卡片提供方开发者实现，开发者实现生命周期处理创建卡片、更新卡片以及删除卡片等请求，提供相应的卡片服务。
-  卡片提供方实例管理模块：由卡片提供方开发者实现，负责对卡片管理服务分配的卡片实例进行持久化管理。
-  通信适配层：由HarmonyOS SDK提供，负责与卡片管理服务通信，用于将卡片的更新数据主动推送到卡片管理服务。
实际开发时只需要作为卡片提供方进行卡片内容的开发，卡片使用方和卡片管理服务由系统自动处理。
接口说明
FormAbility生命周期接口如下：
| 接口名 | 描述 |
| --- | --- |
| onCreate(want: Want): formBindingData.FormBindingData | 卡片提供方接收创建卡片的通知接口。 |
| onCastToNormal(formId: string): void | 卡片提供方接收临时卡片转常态卡片的通知接口。 |
| onUpdate(formId: string): void | 卡片提供方接收更新卡片的通知接口。 |
| onVisibilityChange(newStatus: Record<string, number>): void | 卡片提供方接收修改可见性的通知接口。 |
| onEvent(formId: string, message: string): void | 卡片提供方接收处理卡片事件的通知接口。 |
| onDestroy(formId: string): void | 卡片提供方接收销毁卡片的通知接口。 |
| onAcquireFormState?(want: Want): formInfo.FormState | 卡片提供方接收查询卡片状态的通知接口。 |
| onShare?(formId: string): {[key: string]: any} | 卡片提供方接收卡片分享的通知接口。 |
| onShareForm?(formId: string): Record<string, Object> | 卡片提供方接收卡片分享的通知接口。推荐使用该接口替代onShare接口。如果了实现该接口，onShare将不再被回调。 |
FormProvider类有如下API接口，具体的API介绍详见接口文档。
| 接口名 | 描述 |
| --- | --- |
| setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void; | 设置指定卡片的下一次更新时间。 |
| setFormNextRefreshTime(formId: string, minute: number): Promise<void>; | 设置指定卡片的下一次更新时间，以promise方式返回。 |
| updateForm(formId: string, formBindingData: FormBindingData, callback: AsyncCallback<void>): void; | 更新指定的卡片。 |
| updateForm(formId: string, formBindingData: FormBindingData): Promise<void>; | 更新指定的卡片，以promise方式返回。 |
FormBindingData类有如下API接口，具体的API介绍详见接口文档。
| 接口名 | 描述 |
| --- | --- |
| createFormBindingData(obj?: Object | string): FormBindingData | 创建一个FormBindingData对象。 |
开发步骤
FA卡片开发，即基于FA模型的卡片提供方开发，主要涉及如下关键步骤：
-  实现卡片生命周期接口：开发FormAbility生命周期回调函数。
-  配置卡片配置文件：配置应用配置文件config.json。
-  卡片信息的持久化：对卡片信息进行持久化管理。
-  卡片数据交互：通过updateForm()更新卡片显示的信息。
-  开发卡片页面：使用HML+CSS+JSON开发JS卡片页面。
-  开发卡片事件：为卡片添加router事件和message事件。
实现卡片生命周期接口
创建FA模型的卡片，需实现卡片的生命周期接口。先参考IDE开发服务卡片指南生成服务卡片模板。
1.  在form.ts中，导入相关模块
```typescript
import type featureAbility from '@ohos.ability.featureAbility';
import type Want from '@ohos.app.ability.Want';
import formBindingData from '@ohos.app.form.formBindingData';
import formInfo from '@ohos.app.form.formInfo';
import formProvider from '@ohos.app.form.formProvider';
import dataPreferences from '@ohos.data.preferences';
import hilog from '@ohos.hilog';
```
2.  在form.ts中，实现卡片生命周期接口
```typescript
const TAG: string = '[Sample_FAModelAbilityDevelop]';
const domain: number = 0xFF00;
const DATA_STORAGE_PATH: string = 'form_store';
let storeFormInfo = async (formId: string, formName: string, tempFlag: boolean, context: featureAbility.Context): Promise<void> => {
// 此处仅对卡片ID：formId，卡片名：formName和是否为临时卡片：tempFlag进行了持久化
let formInfo: Record<string, string | number | boolean> = {
'formName': 'formName',
'tempFlag': 'tempFlag',
'updateCount': 0
};
try {
const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
// put form info
await storage.put(formId, JSON.stringify(formInfo));
hilog.info(domain, TAG, `storeFormInfo, put form info successfully, formId: ${formId}`);
await storage.flush();
} catch (err) {
hilog.error(domain, TAG, `failed to storeFormInfo, err: ${JSON.stringify(err as Error)}`);
}
};
let deleteFormInfo = async (formId: string, context: featureAbility.Context) => {
try {
const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
// del form info
await storage.delete(formId);
hilog.info(domain, TAG, `deleteFormInfo, del form info successfully, formId: ${formId}`);
await storage.flush();
} catch (err) {
hilog.error(domain, TAG, `failed to deleteFormInfo, err: ${JSON.stringify(err)}`);
}
}
class LifeCycle {
onCreate: (want: Want) => formBindingData.FormBindingData = (want) => ({ data: '' });
onCastToNormal: (formId: string) => void = (formId) => {
};
onUpdate: (formId: string) => void = (formId) => {
};
onVisibilityChange: (newStatus: Record<string, number>) => void = (newStatus) => {
let obj: Record<string, number> = {
'test': 1
};
return obj;
};
onEvent: (formId: string, message: string) => void = (formId, message) => {
};
onDestroy: (formId: string) => void = (formId) => {
};
onAcquireFormState?: (want: Want) => formInfo.FormState = (want) => (0);
onShareForm?: (formId: string) => Record<string, Object> = (formId) => {
let obj: Record<string, number> = {
'test': 1
};
return obj;
};
}
let obj: LifeCycle = {
onCreate(want: Want) {
hilog.info(domain, TAG, 'FormAbility onCreate');
if (want.parameters) {
let formId = String(want.parameters['ohos.extra.param.key.form_identity']);
let formName = String(want.parameters['ohos.extra.param.key.form_name']);
let tempFlag = Boolean(want.parameters['ohos.extra.param.key.form_temporary']);
// 将创建的卡片信息持久化，以便在下次获取/更新该卡片实例时进行使用
// 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
hilog.info(domain, TAG, 'FormAbility onCreate' + formId);
storeFormInfo(formId, formName, tempFlag, this.context);
}
// 使用方创建卡片时触发，提供方需要返回卡片数据绑定类
let obj: Record<string, string> = {
'title': 'titleOnCreate',
'detail': 'detailOnCreate'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
return formData;
},
onCastToNormal(formId: string) {
// 使用方将临时卡片转换为常态卡片触发，提供方需要做相应的处理
hilog.info(domain, TAG, 'FormAbility onCastToNormal');
},
onUpdate(formId: string) {
// 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
hilog.info(domain, TAG, 'FormAbility onUpdate');
let obj: Record<string, string> = {
'title': 'titleOnUpdate',
'detail': 'detailOnUpdate'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
// 调用updateForm接口去更新对应的卡片，仅更新入参中携带的数据信息，其他信息保持不变
formProvider.updateForm(formId, formData).catch((error: Error) => {
hilog.error(domain, TAG, 'FormAbility updateForm, error:' + JSON.stringify(error));
});
},
onVisibilityChange(newStatus: Record<string, number>) {
// 使用方发起可见或者不可见通知触发，提供方需要做相应的处理，仅系统应用生效
hilog.info(domain, TAG, 'FormAbility onVisibilityChange');
},
onEvent(formId: string, message: string) {
// 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
let obj: Record<string, string> = {
'title': 'titleOnEvent',
'detail': 'detailOnEvent'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
// 调用updateForm接口去更新对应的卡片，仅更新入参中携带的数据信息，其他信息保持不变
formProvider.updateForm(formId, formData).catch((error: Error) => {
hilog.error(domain, TAG, 'FormAbility updateForm, error:' + JSON.stringify(error));
});
hilog.info(domain, TAG, 'FormAbility onEvent');
},
onDestroy(formId: string) {
// 删除卡片实例数据
hilog.info(domain, TAG, 'FormAbility onDestroy');
// 删除之前持久化的卡片实例数据
// 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
deleteFormInfo(formId, this.context);
},
onAcquireFormState(want: Want) {
hilog.info(domain, TAG, 'FormAbility onAcquireFormState');
return formInfo.FormState.READY;
}
};
export default obj;
```
FormAbility不能常驻后台，即在卡片生命周期回调函数中无法处理长时间的任务。
配置卡片配置文件
卡片需要在应用配置文件config.json中进行配置。
-  js模块，用于对应卡片的js相关资源，内部字段结构说明： 表示JS应用的类型。取值范围如下： normal：标识该JS Component为应用实例。 form：标识该JS Component为卡片实例。 配置示例如下：
```json
"js": [
// ...
{
"name": "widget",
"pages": [
"pages/index/index"
],
"window": {
"designWidth": 720,
"autoDesignWidth": true
},
"type": "form"
}
]
```
-  abilities模块，用于对应卡片的FormAbility，内部字段结构说明： 表示该卡片是否为默认卡片，每个Ability有且只有一个默认卡片。 true：默认卡片。 false：非默认卡片。 表示卡片的类型。取值范围如下： JS：JS卡片。 表示卡片的主题样式，取值范围如下： auto：自适应。 dark：深色主题。 light：浅色主题。 表示卡片支持的外观规格，取值范围： 1 * 2：表示1行2列的二宫格。 2 * 2：表示2行2列的四宫格。 2 * 4：表示2行4列的八宫格。 4 * 4：表示4行4列的十六宫格。 表示卡片是否支持周期性刷新，取值范围： true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，优先选择定时刷新。 false：表示不支持周期性刷新。 表示卡片的定点刷新的时刻，采用24小时制，精确到分钟。 updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 表示卡片定时刷新的更新周期，单位为30分钟，取值为自然数。 当取值为0时，表示该参数不生效。 当取值为正整数N时，表示刷新周期为30*N分钟。 updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 配置示例如下：
```json
"abilities": [
// ...
{
"name": ".FormAbility",
"srcPath": "FormAbility",
"description": "$string:FormAbility_desc",
"icon": "$media:icon",
"label": "$string:FormAbility_label",
"type": "service",
"formsEnabled": true,
"srcLanguage": "ets",
"forms": [
{
"jsComponentName": "widget",
"isDefault": true,
"scheduledUpdateTime": "10:30",
"defaultDimension": "2*2",
"name": "widget",
"description": "This is a service widget.",
"colorMode": "auto",
"type": "JS",
"formVisibleNotify": true,
"supportDimensions": [
"2*2"
],
"updateEnabled": true,
"updateDuration": 1
}
]
},
// ...
]
```
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 表示JS Component的名字。该标签不可缺省，默认值为default。 | 字符串 | 否 |
| pages | 表示JS Component的页面用于列举JS Component中每个页面的路由信息[页面路径+页面名称]。该标签不可缺省，取值为数组，数组第一个元素代表JS FA首页。 | 数组 | 否 |
| window | 用于定义与显示窗口相关的配置。 | 对象 | 可缺省。 |
| type | 表示JS应用的类型。取值范围如下： normal：标识该JS Component为应用实例。 form：标识该JS Component为卡片实例。 | 字符串 | 可缺省，缺省值为“normal” 。 |
| mode | 定义JS组件的开发模式。 | 对象 | 可缺省，缺省值为空。 |
| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 表示卡片的类名。字符串最大长度为127字节。 | 字符串 | 否 |
| description | 表示卡片的描述。取值可以是描述性内容，也可以是对描述性内容的资源索引，以支持多语言。字符串最大长度为255字节。 | 字符串 | 可缺省，缺省为空。 |
| isDefault | 表示该卡片是否为默认卡片，每个Ability有且只有一个默认卡片。 true：默认卡片。 false：非默认卡片。 | 布尔值 | 否 |
| type | 表示卡片的类型。取值范围如下： JS：JS卡片。 | 字符串 | 否 |
| colorMode | 表示卡片的主题样式，取值范围如下： auto：自适应。 dark：深色主题。 light：浅色主题。 | 字符串 | 可缺省，缺省值为“auto”。 |
| supportDimensions | 表示卡片支持的外观规格，取值范围： 1 * 2：表示1行2列的二宫格。 2 * 2：表示2行2列的四宫格。 2 * 4：表示2行4列的八宫格。 4 * 4：表示4行4列的十六宫格。 | 字符串数组 | 否 |
| defaultDimension | 表示卡片的默认外观规格，取值必须在该卡片supportDimensions配置的列表中。 | 字符串 | 否 |
| updateEnabled | 表示卡片是否支持周期性刷新，取值范围： true：表示支持周期性刷新，可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，优先选择定时刷新。 false：表示不支持周期性刷新。 | 布尔类型 | 否 |
| scheduledUpdateTime | 表示卡片的定点刷新的时刻，采用24小时制，精确到分钟。 updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 字符串 | 可缺省，缺省值为“0:0”。 |
| updateDuration | 表示卡片定时刷新的更新周期，单位为30分钟，取值为自然数。 当取值为0时，表示该参数不生效。 当取值为正整数N时，表示刷新周期为30*N分钟。 updateDuration参数优先级高于scheduledUpdateTime，两者同时配置时，以updateDuration配置的刷新时间为准。 | 数值 | 可缺省，缺省值为“0”。 |
| formConfigAbility | 表示卡片的配置跳转链接，采用URI格式。 | 字符串 | 可缺省，缺省值为空。 |
| formVisibleNotify | 标识是否允许卡片使用卡片可见性通知。 | 字符串 | 可缺省，缺省值为空。 |
| jsComponentName | 表示JS卡片的Component名称。字符串最大长度为127字节。 | 字符串 | 否 |
| metaData | 表示卡片的自定义信息，包含customizeData数组标签。 | 对象 | 可缺省，缺省值为空。 |
| customizeData | 表示自定义的卡片信息。 | 对象数组 | 可缺省，缺省值为空。 |
卡片信息的持久化
因大部分卡片提供方都不是常驻服务，只有在需要使用时才会被拉起获取卡片信息，且卡片管理服务支持对卡片进行多实例管理，卡片ID对应实例ID，因此若卡片提供方支持对卡片数据进行配置，则需要对卡片的业务数据按照卡片ID进行持久化管理，以便在后续获取、更新以及拉起时能获取到正确的卡片业务数据。且需要适配onDestroy卡片删除通知接口，在其中实现卡片实例数据的删除。
```typescript
const TAG: string = '[Sample_FAModelAbilityDevelop]';
const domain: number = 0xFF00;
const DATA_STORAGE_PATH: string = 'form_store';
let storeFormInfo = async (formId: string, formName: string, tempFlag: boolean, context: featureAbility.Context): Promise<void> => {
// 此处仅对卡片ID：formId，卡片名：formName和是否为临时卡片：tempFlag进行了持久化
let formInfo: Record<string, string | number | boolean> = {
'formName': 'formName',
'tempFlag': 'tempFlag',
'updateCount': 0
};
try {
const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
// put form info
await storage.put(formId, JSON.stringify(formInfo));
hilog.info(domain, TAG, `storeFormInfo, put form info successfully, formId: ${formId}`);
await storage.flush();
} catch (err) {
hilog.error(domain, TAG, `failed to storeFormInfo, err: ${JSON.stringify(err as Error)}`);
}
};
let deleteFormInfo = async (formId: string, context: featureAbility.Context) => {
try {
const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
// del form info
await storage.delete(formId);
hilog.info(domain, TAG, `deleteFormInfo, del form info successfully, formId: ${formId}`);
await storage.flush();
} catch (err) {
hilog.error(domain, TAG, `failed to deleteFormInfo, err: ${JSON.stringify(err)}`);
}
}
// ...
onCreate(want: Want) {
hilog.info(domain, TAG, 'FormAbility onCreate');
if (want.parameters) {
let formId = String(want.parameters['ohos.extra.param.key.form_identity']);
let formName = String(want.parameters['ohos.extra.param.key.form_name']);
let tempFlag = Boolean(want.parameters['ohos.extra.param.key.form_temporary']);
// 将创建的卡片信息持久化，以便在下次获取/更新该卡片实例时进行使用
// 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
hilog.info(domain, TAG, 'FormAbility onCreate' + formId);
storeFormInfo(formId, formName, tempFlag, this.context);
}
// 使用方创建卡片时触发，提供方需要返回卡片数据绑定类
let obj: Record<string, string> = {
'title': 'titleOnCreate',
'detail': 'detailOnCreate'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
return formData;
},
// ...
let deleteFormInfo = async (formId: string, context: featureAbility.Context): Promise<void> => {
try {
const storage = await dataPreferences.getPreferences(context, DATA_STORAGE_PATH);
// del form info
await storage.delete(formId);
hilog.info(domain, TAG, `deleteFormInfo, del form info successfully, formId: ${formId}`);
await storage.flush();
} catch (err) {
hilog.error(domain, TAG, `failed to deleteFormInfo, err: ${JSON.stringify(err)}`);
}
};
// ...
// 适配onDestroy卡片删除通知接口，在其中实现卡片实例数据的删除。
onDestroy(formId: string) {
// 删除卡片实例数据
hilog.info(domain, TAG, 'FormAbility onDestroy');
// 删除之前持久化的卡片实例数据
// 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
deleteFormInfo(formId, this.context);
}
// ...
```
具体的持久化方法可以参考应用数据持久化概述。
需要注意的是，卡片使用方在请求卡片时传递给提供方应用的Want数据中存在临时标记字段，表示此次请求的卡片是否为临时卡片：
-  常态卡片：卡片使用方会持久化的卡片。如添加到桌面的卡片。
-  临时卡片：卡片使用方不会持久化的卡片。如上划卡片应用时显示的卡片。
临时卡片转常态卡片：上划卡片应用后，此时会显示的卡片为临时卡片；点击卡片上的“图钉”按钮后添加到桌面，此时卡片转为常态卡片。
由于临时卡片的数据具有非持久化的特殊性，某些场景例如卡片服务框架死亡重启，此时临时卡片数据在卡片管理服务中已经删除，且对应的卡片ID不会通知到提供方，所以卡片提供方需要自己负责清理长时间未删除的临时卡片数据。同时对应的卡片使用方可能会将之前请求的临时卡片转换为常态卡片。如果转换成功，卡片提供方也需要对对应的临时卡片ID进行处理，把卡片提供方记录的临时卡片数据转换为常态卡片数据，防止提供方在清理长时间未删除的临时卡片时，把已经转换为常态卡片的临时卡片信息删除，导致卡片信息丢失。
卡片数据交互
当卡片应用需要更新数据时（如触发了定时更新或定点更新），卡片应用获取最新数据，并调用updateForm()接口更新主动触发卡片的更新。
```typescript
const TAG: string = '[Sample_FAModelAbilityDevelop]';
const domain: number = 0xFF00;
onUpdate(formId: string) {
// 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
hilog.info(domain, TAG, 'FormAbility onUpdate');
let obj: Record<string, string> = {
'title': 'titleOnUpdate',
'detail': 'detailOnUpdate'
};
let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
// 调用updateForm接口去更新对应的卡片，仅更新入参中携带的数据信息，其他信息保持不变
formProvider.updateForm(formId, formData).catch((error: Error) => {
hilog.error(domain, TAG, 'FormAbility updateForm, error:' + JSON.stringify(error));
});
}
```
开发卡片页面
开发者可以使用类Web范式（HML+CSS+JSON）开发JS卡片页面。生成如下卡片页面，可以这样配置卡片页面文件：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170419.37340988858649554011898244040419:50001231000000:2800:1797E65CC9D650F31C467D76F0076D81340594DD62B02E23EEB9EB24B41D33D1.png)
FA模型当前仅支持JS扩展的类Web开发范式来实现卡片的UI。
-  HML：使用类Web范式的组件描述卡片的页面信息。
-  CSS：HML中类Web范式组件的样式信息。
-  JSON：卡片页面中的数据和事件交互。
```json
{
"data": {
"title": "TitleDefault",
"detail": "TextDefault"
},
"actions": {
"routerEvent": {
"action": "router",
"abilityName": "com.samples.famodelabilitydevelop.MainAbility",
"params": {
"message": "add detail"
}
},
"messageEvent": {
"action": "message",
"params": {
"message": "add detail"
}
}
}
}
```
开发卡片事件
卡片支持为组件设置交互事件(action)，包括router事件和message事件，其中router事件用于Ability跳转，message事件用于卡片开发人员自定义点击事件。关键步骤说明如下：
1.  在hml中为组件设置onclick属性，其值对应到json文件的actions字段中。
2.  如何设置router事件：
3.  如何设置message事件：
示例如下：
-  hml文件
-  css文件
-  json文件
```json
{
"data": {
"title": "TitleDefault",
"detail": "TextDefault"
},
"actions": {
"routerEvent": {
"action": "router",
"abilityName": "com.samples.famodelabilitydevelop.MainAbility",
"params": {
"message": "add detail"
}
},
"messageEvent": {
"action": "message",
"params": {
"message": "add detail"
}
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ime-kit-V14
爬取时间: 2025-04-28 00:45:01
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ime-kit-intro-V14
爬取时间: 2025-04-28 00:45:14
来源: Huawei Developer
IME Kit 负责建立编辑框所在应用与输入法应用之间的通信通道，确保两者可以共同协作提供文本输入功能，也为系统应用提供管理输入法应用的能力。
Kit使用场景
IME Kit提供输入法框架和输入法服务两类API。用于实现输入法应用，也可以用于实现自绘编辑框以及实现对输入法应用的控制。
框架原理
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170419.79245980435648614072297062283726:50001231000000:2800:B73C510D8C641E9C0D39CF99BD6BDC38AD82CDC97AD185121F5B5A9B96DDB055.png)
功能特点
-  输入法应用： 支持创建固定态、悬浮态和状态栏三种类型的Panel，可支持开发一个输入法应用同时部署在手机、平板等多设备中。
-  自定义编辑框： 支持开发者自定义编辑框，实现绑定输入法应用，并实现输入法应用的文字输入、删除、选中、光标移动等操作。
能力范围
-  提供输入法服务相关API，用于输入法应用，包括：创建软键盘窗口、插入/删除字符、选中文本、监听物理键盘按键事件等。
-  提供输入法框架相关API，可用于自绘编辑框，包括绑定输入法，实现输入、删除、选中、光标移动等。
-  提供系统应用管理输入法应用能力，实现对输入法应用的控制，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表。
与相关Kit的关系
ArkUI: IME Kit在输入法软键盘和自绘编辑框时使用ArkUI提供的部分组件、事件、动效、状态管理等能力，例如Text、Button组件，onClick点击事件。
约束限制
针对切换输入法应用的系统API，需要申请系统权限，部分API仅支持当前输入法应用调用。
IME Kit API参考
-  inputMethodEngine
-  inputMethod
-  InputMethodExtensionAbility
-  InputMethodExtensionContext
-  inputMethodList
-  InputMethodSubtype
-  inputMethod.Panel

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/inputmethod-application-guide-V14
爬取时间: 2025-04-28 00:45:28
来源: Huawei Developer
InputMethodExtensionAbility提供了onCreate()和onDestroy()生命周期回调，根据需要重写对应的回调方法。InputMethodExtensionAbility的生命周期如下：
-  onCreate() 服务被首次创建时触发该回调，开发者可以在此进行一些初始化的操作，例如注册公共事件监听等。 如果服务已创建，再次启动该InputMethodExtensionAbility不会触发onCreate()回调。
-  onDestroy() 当不再使用服务且准备将该实例销毁时，触发该回调。开发者可以在该回调中清理资源，如注销监听等。
开发步骤
开发者在实现一个输入法应用时，需要在DevEco Studio工程中新建一个InputMethodExtensionAbility，具体步骤如下：
1.  在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，并命名为InputMethodExtensionAbility。
2.  在InputMethodExtensionAbility目录下，右键选择“New > File”，新建四个文件，分别为KeyboardController.ts、InputMethodService.ts、Index.ets以及KeyboardKeyData.ts。目录如下：
文件介绍
1.  InputMethodService.ts文件。 在InputMethodService.ts文件中，增加导入InputMethodExtensionAbility的依赖包，自定义类继承InputMethodExtensionAbility并加上需要的生命周期回调。
```typescript
import { Want } from '@kit.AbilityKit';
import keyboardController from './model/KeyboardController';
import { InputMethodExtensionAbility } from '@kit.IMEKit';
export default class InputDemoService extends InputMethodExtensionAbility {
onCreate(want: Want): void {
keyboardController.onCreate(this.context); // 初始化窗口并注册对输入法框架的事件监听
}
onDestroy(): void {
console.log("onDestroy.");
keyboardController.onDestroy(); // 销毁窗口并去注册事件监听
}
}
```
2.  KeyboardController.ts文件。
```typescript
import { display } from '@kit.ArkUI';
import { inputMethodEngine, InputMethodExtensionContext } from '@kit.IMEKit';
// 调用输入法框架的getInputMethodAbility方法获取实例，并由此实例调用输入法框架功能接口
const inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
export class KeyboardController {
private mContext: InputMethodExtensionContext | undefined = undefined; // 保存InputMethodExtensionAbility中的context属性
private panel: inputMethodEngine.Panel | undefined = undefined;
private textInputClient: inputMethodEngine.InputClient | undefined = undefined;
private keyboardController: inputMethodEngine.KeyboardController | undefined = undefined;
constructor() {
}
public onCreate(context: InputMethodExtensionContext): void
{
this.mContext = context;
this.initWindow(); // 初始化窗口
this.registerListener(); // 注册对输入法框架的事件监听
}
public onDestroy(): void // 应用生命周期销毁
{
this.unRegisterListener(); // 去注册事件监听
if(this.panel) { // 销毁窗口
inputMethodAbility.destroyPanel(this.panel);
}
if(this.mContext) {
this.mContext.destroy();
}
}
public insertText(text: string): void {
if(this.textInputClient) {
this.textInputClient.insertText(text);
}
}
public deleteForward(length: number): void {
if(this.textInputClient) {
this.textInputClient.deleteForward(length);
}
}
private initWindow(): void // 初始化窗口
{
if(this.mContext === undefined) {
return;
}
let dis = display.getDefaultDisplaySync();
let dWidth = dis.width;
let dHeight = dis.height;
let keyHeightRate = 0.47;
let keyHeight = dHeight * keyHeightRate;
let nonBarPosition = dHeight - keyHeight;
let panelInfo: inputMethodEngine.PanelInfo = {
type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
flag: inputMethodEngine.PanelFlag.FLG_FIXED
};
inputMethodAbility.createPanel(this.mContext, panelInfo).then(async (inputPanel: inputMethodEngine.Panel) => {
this.panel = inputPanel;
if(this.panel) {
await this.panel.resize(dWidth, keyHeight);
await this.panel.moveTo(0, nonBarPosition);
await this.panel.setUiContent('InputMethodExtensionAbility/pages/Index');
}
});
}
private registerListener(): void
{
this.registerInputListener(); // 注册对输入法框架服务的监听
// 注册隐藏键盘事件监听等
}
private registerInputListener(): void { // 注册对输入法框架服务的开启及停止事件监听
inputMethodAbility.on('inputStart', (kbController, textInputClient) => {
this.textInputClient = textInputClient; // 此为输入法客户端实例，由此调用输入法框架提供给输入法应用的功能接口
this.keyboardController = kbController;
})
inputMethodAbility.on('inputStop', () => {
this.onDestroy(); // 销毁KeyboardController
});
}
private unRegisterListener(): void
{
inputMethodAbility.off('inputStart');
inputMethodAbility.off('inputStop', () => {});
}
}
const keyboardController = new KeyboardController();
export default keyboardController;
```
3.  KeyboardKeyData.ts文件。 定义软键盘的按键显示内容。
```typescript
export interface sourceListType {
content: string,
}
export let numberSourceListData: sourceListType[] = [
{
content: '1'
},
{
content: '2'
},
{
content: '3'
},
{
content: '4'
},
{
content: '5'
},
{
content: '6'
},
{
content: '7'
},
{
content: '8'
},
{
content: '9'
},
{
content: '0'
}
]
```
4.  Index.ets文件。 主要描绘了具体按键功能。如按下数字键，就会将数字内容在输入框中打印出来，按下删除键，就会将内容删除。 同时在resources/base/profile/main_pages.json文件的src字段中添加此文件路径。
```typescript
import { numberSourceListData, sourceListType } from './KeyboardKeyData';
import keyboardController from '../model/KeyboardController';
@Component
struct keyItem {
private keyValue: sourceListType = numberSourceListData[0];
@State keyBgc: string = "#fff"
@State keyFontColor: string = "#000"
build() {
Column() {
Flex({ direction: FlexDirection.Column,
alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
Text(this.keyValue.content).fontSize(20).fontColor(this.keyFontColor)
}
}
.backgroundColor(this.keyBgc)
.borderRadius(6)
.width("8%")
.height("65%")
.onClick(() => {
keyboardController.insertText(this.keyValue.content);
})
}
}
// 删除组件
@Component
export struct deleteItem {
@State keyBgc: string = "#fff"
@State keyFontColor: string = "#000"
build() {
Column() {
Flex({ direction: FlexDirection.Column,
alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
Text("删除").fontSize(20).fontColor(this.keyFontColor)
}
}
.backgroundColor(this.keyBgc)
.width("13%")
.borderRadius(6)
.onClick(() => {
keyboardController.deleteForward(1);
})
}
}
// 数字键盘
@Component
struct numberMenu {
private numberList: sourceListType[] = numberSourceListData;
build() {
Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceEvenly }) {
Flex({ justifyContent: FlexAlign.SpaceBetween }) {
ForEach(this.numberList, (item: sourceListType) => { // 数字键盘第一行
keyItem({ keyValue: item })
}, (item: sourceListType) => item.content);
}
.padding({ top: "2%" })
.width("96%")
.height("25%")
Flex({ justifyContent: FlexAlign.SpaceBetween }) {
deleteItem()
}
.width("96%")
.height("25%")
}
}
}
@Entry
@Component
struct Index {
private numberList: sourceListType[] = numberSourceListData
build() {
Stack() {
Flex({
direction: FlexDirection.Column,
alignItems: ItemAlign.Center,
justifyContent: FlexAlign.End
}) {
Flex({
direction: FlexDirection.Column,
alignItems: ItemAlign.Center,
justifyContent: FlexAlign.SpaceBetween
}) {
numberMenu({
numberList: this.numberList
})
}
.align(Alignment.End)
.width("100%")
.height("75%")
}
.height("100%").align(Alignment.End).backgroundColor("#cdd0d7")
}
.position({ x: 0, y: 0 }).zIndex(99999)
}
}
```
5.  在工程Module对应的module.json5配置文件中注册InputMethodExtensionAbility，type标签需要设置为“inputMethod”，srcEntry标签表示当前InputMethodExtensionAbility组件所对应的代码路径。
```json
{
"module": {
...
"extensionAbilities": [
{
"description": "inputMethod",
"name": "InputMethodExtensionAbility",
"icon": "$media:app_icon",
"srcEntry": "./ets/InputMethodExtensionAbility/InputMethodService.ts",
"type": "inputMethod",
"exported": true,
}
]
}
}
```
验证方法
```typescript
import { inputMethod } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodSetting = inputMethod.getSetting();
try {
inputMethodSetting.showOptionalInputMethods((err: BusinessError, data: boolean) => {
if (err) {
console.error(`Failed to showOptionalInputMethods: ${JSON.stringify(err)}`);
return;
}
console.log('Succeeded in showing optionalInputMethods.');
});
} catch (err) {
console.error(`Failed to showOptionalInputMethods: ${JSON.stringify(err)}`);
}
```
1.  在弹窗上显示的输入法应用列表中，选择并点击demo应用，将demo应用切换为当前输入法。
2.  点击任意编辑框，即可拉起输入法demo。
约束与限制
为了降低InputMethodExtensionAbility能力被三方应用滥用的风险，现通过基础访问模式的功能约束对输入法应用进行安全管控。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-inputmethod-in-custom-edit-box-V14
爬取时间: 2025-04-28 00:45:41
来源: Huawei Developer
在输入法框架中，可以通过getController方法获取到InputMethodController实例来绑定输入法并监听输入法应用的各种操作，比如插入、删除、选择、光标移动等。这样就可以在自绘编辑框中使用输入法，并实现更加灵活和自由的编辑操作。
开发步骤
1.  开发者在自绘编辑框中使用输入法时，首先需要在DevEco Studio工程中新建一个ets文件，命名为自定义控件的名称，本示例中命名为CustomInput，在文件中定义一个自定义控件，并从@kit.IMEKit中导入inputMethod。
```typescript
import { inputMethod } from '@kit.IMEKit';
@Component
export struct CustomInput {
build() {
}
}
```
2.  在控件中，使用Text组件作为自绘编辑框的文本显示组件，使用状态变量inputText作为Text组件要显示的内容。
```typescript
import { inputMethod } from '@kit.IMEKit';
@Component
export struct CustomInput {
@State inputText: string = ''; // inputText作为Text组件要显示的内容。
build() {
Text(this.inputText) // Text组件作为自绘编辑框的文本显示组件。
.fontSize(16)
.width('100%')
.lineHeight(40)
.id('customInput')
.height(45)
.border({ color: '#554455', radius: 30, width: 1 })
.maxLines(1)
}
}
```
3.  在控件中获取inputMethodController实例，并在文本点击时调用controller示例的attach方法绑定和拉起软键盘，并注册监听输入法插入文本、删除等方法，本示例仅展示插入、删除。
```typescript
import { inputMethod } from '@kit.IMEKit';
@Component
export struct CustomInput {
@State inputText: string = ''; // inputText作为Text组件要显示的内容。
private isAttach: boolean = false;
private inputController: inputMethod.InputMethodController = inputMethod.getController();
build() {
Text(this.inputText) // Text组件作为自绘编辑框的文本显示组件。
.fontSize(16)
.width('100%')
.lineHeight(40)
.id('customInput')
.onBlur(() => {
this.off();
})
.height(45)
.border({ color: '#554455', radius: 30, width: 1 })
.maxLines(1)
.onClick(() => {
this.attachAndListener(); // 点击控件
})
}
async attachAndListener() { // 绑定和设置监听
focusControl.requestFocus('CustomInput');
await this.inputController.attach(true, {
inputAttribute: {
textInputType: inputMethod.TextInputType.TEXT,
enterKeyType: inputMethod.EnterKeyType.SEARCH
}
});
if (!this.isAttach) {
this.inputController.on('insertText', (text) => {
this.inputText += text;
})
this.inputController.on('deleteLeft', (length) => {
this.inputText = this.inputText.substring(0, this.inputText.length - length);
})
this.isAttach = true;
}
}
off() {
this.isAttach = false;
this.inputController.off('insertText')
this.inputController.off('deleteLeft')
}
}
```
4.  在应用界面布局中引入该控件即可，此处假设使用界面为Index.ets和控件CustomInput.ets在同一目录下。
```typescript
import { CustomInput } from './CustomInput'; // 导入控件
@Entry
@Component
struct Index {
build() {
Column() {
CustomInput() // 使用控件
}
}
}
```
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170419.94013576818252734824657380865329:50001231000000:2800:51BB218B09D3E5EBAB074CBA30F795046ADAC9FC7192172EF23A91667CD4D7E7.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/switch-inputmehod-guide-V14
爬取时间: 2025-04-28 00:45:55
来源: Huawei Developer
输入法框架服务提供了切换输入法应用的API，支持切换输入法、切换输入法和子类型、切换当前输入法的子类型。
1.  以下接口的使用仅允许在当前输入法应用中调用。
2.  本示例假设已经在输入法应用中执行，如果实现一个输入法应用，请参考实现一个输入法应用。
切换当前输入法子类型
1.  在已完成一个输入法应用的基础上，当输入法应用是当前输入法时，在输入法应用中使用switchCurrentInputMethodSubtype接口，传入当前输入法的子类型InputMethodSubtype作为参数即可切换当前输入法子类型。
```typescript
import { InputMethodSubtype, inputMethod } from '@kit.IMEKit';
export class KeyboardController {
async switchCurrentInputMethodSubtype() {
let subTypes = await inputMethod.getSetting().listCurrentInputMethodSubtype(); // 获取当前输入法的所有子类型
let currentSubType = inputMethod.getCurrentInputMethodSubtype(); // 获取当前输入法当前的子类型
for(let i=0;i<subTypes.length;i++) {
if(subTypes[i].id != currentSubType.id) { // 判断不是当前的子类型时切换，实际开发中可以根据需要填固定子类型
await inputMethod.switchCurrentInputMethodSubtype(subTypes[i]);
}
}
}
}
```
2.  输入法应用中注册子类型变化事件，根据不同子类型加载不同的输入界面。
```typescript
import { InputMethodSubtype, inputMethodEngine, inputMethod } from '@kit.IMEKit';
export class KeyboardController {
async switchCurrentInputMethodSubtype() {
let panel: inputMethodEngine.Panel;
let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
// 设置监听子类型事件，改变输入法应用界面
inputMethodAbility.on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
if(inputMethodSubtype.id == 'InputMethodExtAbility') {
panel.setUiContent('pages/Index'); // 假设在输入法应用中此时Panel已经在onCreate流程中创建
}
if(inputMethodSubtype.id == 'InputMethodExtAbility1') {
panel.setUiContent('pages/Index1'); // 假设在输入法应用中此时Panel已经在onCreate流程中创建
}
});
}
}
```
切换输入法应用
在已完成一个输入法应用的基础上，当输入法应用是当前输入法时，在输入法应用中使用switchInputMethod接口，传入目标输入法的InputMethodProperty信息，即可切换输入法到目标输入法应用。
```typescript
import { inputMethod } from '@kit.IMEKit';
export class KeyboardController {
async switchInputMethod(){
let inputMethods = await inputMethod.getSetting().getInputMethods(true); // 获取已使能的输入法列表
let currentInputMethod = inputMethod.getCurrentInputMethod(); // 获取当前输入法
for(let i=0;i<inputMethods.length;i++) {
if(inputMethods[i].name != currentInputMethod.name) { // 判断不是当前输入法时，切换到该输入法，实际开发中可以切换到固定输入法
await inputMethod.switchInputMethod(inputMethods[i]);
}
}
}
}
```
切换输入法应用和子类型
在已完成一个输入法应用的基础上，当输入法应用是当前输入法时，在输入法应用中使用switchCurrentInputMethodAndSubtype接口，传入目标输入法的InputMethodProperty，目标输入法的子类型InputMethodSubtype信息，即可切换输入法到目标输入法应用的目标子类型。
```typescript
import { inputMethod } from '@kit.IMEKit';
export class KeyboardController {
async switchInputMethodAndSubtype() {
let inputMethods = await inputMethod.getSetting().getInputMethods(true); // 获取已使能的输入法列表
let currentInputMethod = inputMethod.getCurrentInputMethod(); // 获取当前输入法
for (let i = 0;i < inputMethods.length; i++) {
if (inputMethods[i].name != currentInputMethod.name) { // 判断不是当前输入法时，切换到该输入法，实际开发中可以切换到固定输入法
let subTypes = await inputMethod.getSetting().listInputMethodSubtype(inputMethods[i]); // 获取目标输入法的子类型
await inputMethod.switchCurrentInputMethodAndSubtype(inputMethods[i], subTypes[0]); // 本示例默认切换到获取的第一个子类型
}
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/input-method-subtype-guide-V14
爬取时间: 2025-04-28 00:46:08
来源: Huawei Developer
输入法子类型允许输入法展现不同的输入模式或语言，用户可以根据需要在不同模式和语言中切换。如：输入法的中文键盘、英文键盘等都属于输入法的子类型。
输入法子类型的配置与实现
1.  输入法应用开发者只需要注册实现一个InputMethodExtensionAbility，所有的输入法子类型共用该InputMethodExtensionAbility，在module.json5配置文件中添加metadata，name为ohos_extension.input_method，用于配置所有子类型的资源信息。
```typescript
{
"module": {
// ...
"extensionAbilities": [
{
"description": "InputMethodExtDemo",
"icon": "$media:icon",
"name": "InputMethodExtAbility",
"srcEntry": "./ets/InputMethodExtensionAbility/InputMethodService.ts",
"type": "inputMethod",
"exported": true,
"metadata": [
{
"name": "ohos.extension.input_method",
"resource": "$profile:input_method_config"
}
]
}
]
}
}
```
2.  子类型配置文件格式如下，字段释义参照InputMethodSubtype，开发者需要严格按照配置文件格式及字段进行子类型信息配置, locale字段的配置参照BCP 47。
3.  输入法应用中监听子类型事件，根据不同的子类型，可以加载不同的软键盘界面，或者使用状态变量控制界面中的软键盘显示。
```typescript
import { InputMethodSubtype, inputMethodEngine } from '@kit.IMEKit';
let panel: inputMethodEngine.Panel;
let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility.on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
let subType = inputMethodSubtype; // 保存当前输入法子类型, 此处也可以改变状态变量的值，布局中判断状态变量，不同的子类型显示不同的布局控件
if (inputMethodSubtype.id == 'InputMethodExtAbility') { // 根据不同的子类型，可以加载不同的软键盘界面
panel.setUiContent('pages/Index');
}
if (inputMethodSubtype.id == 'InputMethodExtAbility1') { // 根据不同的子类型，可以加载不同的软键盘界面
panel.setUiContent('pages/Index1');
}
});
```
输入法子类型相关信息的获取
1.  开发者可以通过调用getCurrentInputMethodSubtype获取当前输入法应用的当前子类型。
2.  开发者可以通过调用listCurrentInputMethodSubtype获取当前输入法应用的所有子类型。
3.  开发者可以通过调用listInputMethodSubtype获取指定输入法应用的所有子类型。
输入法子类型的切换
1.  开发者可以通过调用switchCurrentInputMethodSubtype切换当前输入法应用的子类型。
2.  开发者可以通过调用switchCurrentInputMethodAndSubtype切换至指定输入法应用的指定子类型。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ime-kit-security-V14
爬取时间: 2025-04-28 00:46:22
来源: Huawei Developer
为了保护用户数据安全，系统增加了输入法安全模式功能，包括基础模式和完整体验模式。在基础模式下，输入法扩展无法调用任何可能涉及访问或泄漏用户隐私数据的系统能力；而在完整体验模式下，则没有该限制。
用户可以在设置应用中切换基础模式和完整体验模式。
基础模式介绍
完整体验模式介绍
开发指导
在输入法扩展的onCreate生命周期回调函数中通过getSecurityMode接口查询当前输入法应用的安全模式。
为了确保输入法功能的稳定性，开发者应当在基础模式下仅使用与基础输入功能相关的能力，并且不得试图绕过系统机制将数据传递到输入法扩展之外。
共享沙箱介绍
1.  应用appid：xxx 应用名称：xxx 开发者id：xxx 邮件附件中提供： ①输入法应用安装到系统，在设置的输入法列表中看到该应用的截图。 ②输入法应用中module.json5的InputMethodExtensionAbility的相关配置截图。
2.  应用appid：xxx 应用名称：xxx 开发者id：xxx 邮件附件中提供： ①输入法应用安装到系统，在设置的输入法列表中看到该应用的截图。 ②输入法应用中module.json5的InputMethodExtensionAbility的相关配置截图。
3.  应用appid：xxx 应用名称：xxx 开发者id：xxx 邮件附件中提供： ①输入法应用安装到系统，在设置的输入法列表中看到该应用的截图。 ②输入法应用中module.json5的InputMethodExtensionAbility的相关配置截图。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170420.47123670148595358326269213991549:50001231000000:2800:DD1EA41D88179C81F822325CD0C89530FF5BA1F15C9AB239C76170B5D5BC338A.png)
1.  应用appid：xxx 应用名称：xxx 开发者id：xxx 邮件附件中提供： ①输入法应用安装到系统，在设置的输入法列表中看到该应用的截图。 ②输入法应用中module.json5的InputMethodExtensionAbility的相关配置截图。
2.  应用appid：xxx 应用名称：xxx 开发者id：xxx 邮件附件中提供： ①输入法应用安装到系统，在设置的输入法列表中看到该应用的截图。 ②输入法应用中module.json5的InputMethodExtensionAbility的相关配置截图。
1.  应用appid：xxx 应用名称：xxx 开发者id：xxx 邮件附件中提供： ①输入法应用安装到系统，在设置的输入法列表中看到该应用的截图。 ②输入法应用中module.json5的InputMethodExtensionAbility的相关配置截图。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/use-inputmethod-in-custom-edit-box-ndk-V14
爬取时间: 2025-04-28 00:46:35
来源: Huawei Developer
场景介绍
IME Kit支持开发者在自绘编辑框中使用输入法，与输入法应用交互，包括显示、隐藏输入法，接收来自输入法应用的文本编辑操作通知等，本文档介绍开发者如何使用C/C++完成此功能开发。
接口说明
详细接口说明请参考InputMethod接口文档。
添加动态链接库
CMakeLists.txt中添加以下lib。
引用头文件
绑定输入法
开发者需要在输入框获焦时，通过调用接口OH_InputMethodController_Attach绑定输入法，绑定成功后用户可以通过输入法输入文字。
1.  创建InputMethod_TextEditorProxy实例，示例代码如下所示：
2.  创建InputMethod_AttachOptions实例，设置绑定输入法时的选项。示例代码如下所示：
3.  调用OH_InputMethodController_Attach发起绑定输入法服务，调用成功后，可以获取到用于和输入法交互的InputMethod_InputMethodProxy。示例代码如下所示：
显示/隐藏面板功能
绑定成功后，可以使用获取到的InputMethod_InputMethodProxy对象向输入法发送消息。示例代码如下所示：
监听输入法应用的请求/通知
1.  需要先实现对输入法应用发送的请求或通知的响应处理函数，示例代码如下所示：
2.  将实现后的响应函数，设置到InputMethod_TextEditorProxy中，再通过绑定输入法时调用的OH_InputMethodController_Attach将其设置到输入法框架中，完成监听注册。示例代码如下所示：
解绑输入法
当编辑框失焦，需要结束使用输入法，通过接口OH_InputMethodController_Detach与输入法框架解绑。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ipc-kit-V14
爬取时间: 2025-04-28 00:46:48
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ipc-rpc-overview-V14
爬取时间: 2025-04-28 00:47:01
来源: Huawei Developer
基本概念
IPC：设备内的进程间通信（Inter-Process Communication）
RPC：设备间的进程间通信（Remote Procedure Call）
IPC/RPC用于实现跨进程通信，不同的是前者使用Binder驱动，用于设备内的跨进程通信，后者使用软总线驱动，用于跨设备跨进程通信。需要跨进程通信的原因是因为每个进程都有自己独立的资源和内存空间，其他进程不能随意访问不同进程的内存和资源，IPC/RPC便是为了突破这一点。
Stage模型不能直接使用本文介绍的IPC和RPC，以下为IPC与RPC的典型使用场景：
实现原理
Client：请求服务的一端，被称为客户端
Server：提供服务的一端，被称为服务端
在IPC Kit中也经常用Proxy表示服务请求方（客户端-Client），Stub表示服务提供方（服务端-Server），后续文档中对Proxy和Stub不再做过多描述。
IPC和RPC通常采用客户端-服务端（Client-Server）模型，在使用时，请求Client端进程可获取Server端所在进程的代理（Proxy），并通过此代理读写数据来实现进程间的数据通信，更具体的讲，首先客户端会建立一个服务端的代理对象，这个代理对象具备和服务端一样的功能，若想访问服务端中的某一个方法，只需访问代理对象中对应的方法即可，代理对象会将请求发送给服务端；然后服务端处理接受到的请求，处理完之后通过驱动返回处理结果给代理对象；最后代理对象将请求结果进一步返回给客户端。
如下图所示：
通常，Stub会先注册系统能力（System Ability）到系统能力管理者（System Ability Manager，缩写SAMgr）中，SAMgr负责管理这些SA并向Client提供相关的接口。Client要和某个具体的SA通信，必须先从SAMgr中获取该SA的代理Proxy对象，然后使用代理Proxy对象和SA通信。在整个通信过程中，如果使用的是IPC通信，则依赖的是Binder驱动，使用的是RPC通信，则依赖的是软总线驱动。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170420.74007954081600558942939024666038:50001231000000:2800:68D672620DBC347F912CD929977F0155E41C5306AE9E3ACF8C994E9B88EBE785.png)
约束与限制
-  单个设备上跨进程通信时，传输的数据量最大约为1MB，过大的数据量请使用匿名共享内存。
-  不支持在RPC中订阅匿名Stub对象（没有向SAMgr注册Stub对象）的死亡通知。
-  不支持把跨设备的Proxy对象传递回该Proxy对象所指向的Stub对象所在的设备，即指向远端设备Stub的Proxy对象不能在本设备内进行二次跨进程传递。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ipc-rpc-development-guideline-V14
爬取时间: 2025-04-28 00:47:15
来源: Huawei Developer
场景介绍
IPC/RPC的主要工作是让运行在不同进程的Proxy和Stub互相通信，包括Proxy和Stub运行在不同设备的情况。
开发步骤
ArkTS侧开发步骤
-  此文档中的示例代码描述的是系统应用跨进程通信。
-  当前不支持三方应用实现ServiceExtensionAbility，三方应用的UIAbility组件可以通过Context连接系统提供的ServiceExtensionAbility。
-  当前使用场景： 仅限客户端是三方应用，服务端是系统应用。
1.  添加依赖
```typescript
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
```
2.  绑定Ability 首先，构造变量want，指定要绑定的Ability所在应用的包名、组件名，如果是跨设备的场景，还需要绑定目标设备NetworkId（组网场景下对应设备的标识符，可以使用distributedDeviceManager获取目标设备的NetworkId）；然后，构造变量connect，指定绑定成功、绑定失败、断开连接时的回调函数；最后，FA模型使用featureAbility提供的接口绑定Ability，Stage模型通过context获取服务后用提供的接口绑定Ability。
```typescript
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from "@kit.AbilityKit";
import { Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
let dmInstance: distributedDeviceManager.DeviceManager | undefined;
let proxy: rpc.IRemoteObject | undefined;
let connectId: number;
// 单个设备绑定Ability
let want: Want = {
// 包名和组件名写实际的值
bundleName: "ohos.rpc.test.server",
abilityName: "ohos.rpc.test.server.ServiceAbility",
};
let connect: common.ConnectOptions = {
onConnect: (elementName, remoteProxy) => {
hilog.info(0x0000, 'testTag', 'RpcClient: js onConnect called');
proxy = remoteProxy;
},
onDisconnect: (elementName) => {
hilog.info(0x0000, 'testTag', 'RpcClient: onDisconnect');
},
onFailed: () => {
hilog.info(0x0000, 'testTag', 'RpcClient: onFailed');
}
};
// FA模型使用此方法连接服务
// connectId = featureAbility.connectAbility(want, connect);
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext; // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
connectId = context.connectServiceExtensionAbility(want,connect);
// 跨设备绑定
try{
dmInstance = distributedDeviceManager.createDeviceManager("ohos.rpc.test");
} catch(error) {
let err: BusinessError = error as BusinessError;
hilog.error(0x0000, 'testTag', 'createDeviceManager errCode:' + err.code + ', errMessage:' + err.message);
}
// 使用distributedDeviceManager获取目标设备NetworkId
if (dmInstance != undefined) {
let deviceList = dmInstance.getAvailableDeviceListSync();
let networkId = deviceList[0].networkId;
let want: Want = {
bundleName: "ohos.rpc.test.server",
abilityName: "ohos.rpc.test.service.ServiceAbility",
deviceId: networkId,
flags: 256
};
// 建立连接后返回的Id需要保存下来，在断开连接时需要作为参数传入
// FA模型使用此方法连接服务
// connectId = featureAbility.connectAbility(want, connect);
// 第一个参数是本应用的包名，第二个参数是接收distributedDeviceManager的回调函数
connectId = context.connectServiceExtensionAbility(want,connect);
}
```
3.  服务端处理客户端请求 服务端被绑定的Ability在onConnect方法里返回继承自rpc.RemoteObject的对象，该对象需要实现onRemoteMessageRequest方法，处理客户端的请求。
```typescript
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';
class Stub extends rpc.RemoteObject {
constructor(descriptor: string) {
super(descriptor);
}
onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): boolean | Promise<boolean> {
// 根据code处理客户端的请求
return true;
}
onConnect(want: Want) {
const robj: rpc.RemoteObject = new Stub("rpcTestAbility");
return robj;
}
}
```
4.  客户端处理服务端响应 客户端在onConnect回调里接收到代理对象，调用sendMessageRequest方法发起请求，在期约（用于表示一个异步操作的最终完成或失败及其结果值）或者回调函数里接收结果。
```typescript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// 使用期约
let option = new rpc.MessageOption();
let data = rpc.MessageSequence.create();
let reply = rpc.MessageSequence.create();
// 往data里写入参数
let proxy: rpc.IRemoteObject | undefined;
if (proxy != undefined) {
proxy.sendMessageRequest(1, data, reply, option)
.then((result: rpc.RequestResult) => {
if (result.errCode != 0) {
hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
return;
}
// 从result.reply里读取结果
})
.catch((e: Error) => {
hilog.error(0x0000, 'testTag', 'sendMessageRequest got exception: ' + e);
})
.finally(() => {
data.reclaim();
reply.reclaim();
})
}
// 使用回调函数
function sendRequestCallback(err: Error, result: rpc.RequestResult) {
try {
if (result.errCode != 0) {
hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
return;
}
// 从result.reply里读取结果
} finally {
result.data.reclaim();
result.reply.reclaim();
}
}
let options = new rpc.MessageOption();
let datas = rpc.MessageSequence.create();
let replys = rpc.MessageSequence.create();
// 往data里写入参数
if (proxy != undefined) {
proxy.sendMessageRequest(1, datas, replys, options, sendRequestCallback);
}
```
5.  断开连接 IPC通信结束后，FA模型使用featureAbility的接口断开连接，Stage模型在获取context后用提供的接口断开连接。
```typescript
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from "@kit.AbilityKit";
import { Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
function disconnectCallback() {
hilog.info(0x0000, 'testTag', 'disconnect ability done');
}
// FA模型使用此方法断开连接
// featureAbility.disconnectAbility(connectId, disconnectCallback);
let proxy: rpc.IRemoteObject | undefined;
let connectId: number;
// 单个设备绑定Ability
let want: Want = {
// 包名和组件名写实际的值
bundleName: "ohos.rpc.test.server",
abilityName: "ohos.rpc.test.server.ServiceAbility",
};
let connect: common.ConnectOptions = {
onConnect: (elementName, remote) => {
proxy = remote;
},
onDisconnect: (elementName) => {
},
onFailed: () => {
proxy;
}
};
// FA模型使用此方法连接服务
// connectId = featureAbility.connectAbility(want, connect);
connectId = this.context.connectServiceExtensionAbility(want,connect);
this.context.disconnectServiceExtensionAbility(connectId);
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/subscribe-remote-state-V14
爬取时间: 2025-04-28 00:47:33
来源: Huawei Developer
IPC/RPC提供对远端Stub对象状态的订阅机制，在远端Stub对象消亡时，可触发消亡通知告诉本地Proxy对象。这种状态通知订阅需要调用特定接口完成，当不再需要订阅时也需要调用特定接口取消。使用这种订阅机制的用户，需要实现消亡通知接口DeathRecipient并实现onRemoteDied方法清理资源。该方法会在远端Stub对象所在进程消亡或所在设备离开组网时被回调。值得注意的是，调用这些接口有一定的顺序。首先，需要Proxy订阅Stub消亡通知，若在订阅期间Stub状态正常，则在不再需要时取消订阅；若在订阅期间Stub所在进程退出或者所在设备退出组网，则会自动触发Proxy自定义的后续操作。
使用场景
这种订阅机制适用于本地Proxy对象需要感知远端Stub对象所在进程消亡，或所在设备离开组网的场景。当Proxy感知到Stub端消亡后，可适当清理本地资源。此外，RPC目前不提供匿名Stub对象的消亡通知，即只有向SAMgr注册过的服务才能被订阅消亡通知，IPC则支持匿名对象的消亡通知。
ArkTS侧接口
-  此文档中的示例代码描述的是系统应用跨进程通信。
-  当前不支持三方应用实现ServiceExtensionAbility，三方应用的UIAbility组件可以通过Context连接系统提供的ServiceExtensionAbility。
-  当前使用场景： 仅限客户端是三方应用，服务端是系统应用。
| 接口名 | 返回值类型 | 功能描述 |
| --- | --- | --- |
| registerDeathRecipient | void | 注册用于接收远程对象消亡通知的回调，增加 proxy 对象上的消亡通知。 |
| unregisterDeathRecipient | void | 注销用于接收远程对象消亡通知的回调。 |
| onRemoteDied | void | 在成功添加死亡通知订阅后，当远端对象死亡时，将自动调用本方法。 |
参考代码
```typescript
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
onConnect: (elementName, remoteProxy) => {
hilog.info(0x0000, 'testTag', 'RpcClient: js onConnect called.');
proxy = remoteProxy;
},
onDisconnect: (elementName) => {
hilog.info(0x0000, 'testTag', 'RpcClient: onDisconnect');
},
onFailed: () => {
hilog.info(0x0000, 'testTag', 'RpcClient: onFailed');
}
};
let want: Want = {
bundleName: "com.ohos.server",
abilityName: "com.ohos.server.EntryAbility",
};
// FA模型通过此方法连接服务
// FA.connectAbility(want, connect);
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext; // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```
上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的unregisterDeathRecipient接口方法注销死亡回调
```typescript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
class MyDeathRecipient implements rpc.DeathRecipient{
onRemoteDied() {
hilog.info(0x0000, 'testTag', 'server died');
}
}
let deathRecipient = new MyDeathRecipient();
if (proxy != undefined) {
proxy.registerDeathRecipient(deathRecipient, 0);
proxy.unregisterDeathRecipient(deathRecipient, 0);
}
```
Stub感知Proxy消亡（匿名Stub的使用）
正向的消亡通知是Proxy感知Stub的状态，若想达到反向的死消亡通知，即Stub感知Proxy的状态，可以巧妙的利用正向消亡通知。如两个进程A（原Stub所在进程）和B（原Proxy所在进程），进程B在获取到进程A的Proxy对象后，在B进程新建一个匿名Stub对象（匿名指未向SAMgr注册），可称之为回调Stub，再通过SendRequest接口将回调Stub传给进程A的原Stub。这样一来，进程A便获取到了进程B的回调Proxy。当进程B消亡或B所在设备离开组网时，回调Stub会消亡，回调Proxy会感知，进而通知给原Stub，便实现了反向消亡通知。
注意：
反向死亡通知仅限设备内跨进程通信使用，不可用于跨设备。
当匿名Stub对象没有被任何一个Proxy指向的时候，内核会自动回收。
参考代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ipc-capi-development-guideline-V14
爬取时间: 2025-04-28 00:47:46
来源: Huawei Developer
场景介绍
IPC的主要工作是让运行在不同进程的Proxy和Stub互相通信，而IPC CAPI是提供的C接口。
IPC CAPI接口不直接提供跨进程通信能力，两个进程之间的IPC通道建立，依赖于Ability Kit。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170420.14939926554125361825309795939552:50001231000000:2800:BA0F8439C099AC2D4C7F3880C0732872C1AE8842FC663B3FE0B9207D789DDE1F.png)
进程间IPC通道建立，详情参考Native子进程开发指导（C/C++)，本文重点阐述IPC CAPI部分使用说明。
接口说明
表1CAPI侧IPC接口
| 接口名 | 描述 |
| --- | --- |
| typedef int (*OH_OnRemoteRequestCallback) (uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData); | Stub端用于处理远端数据请求的回调函数。 |
| OHIPCRemoteStub* OH_IPCRemoteStub_Create (const char *descriptor, OH_OnRemoteRequestCallback requestCallback, OH_OnRemoteDestroyCallback destroyCallback, void *userData); | 创建OHIPCRemoteStub对象。 |
| int OH_IPCRemoteProxy_SendRequest(const OHIPCRemoteProxy *proxy, uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, const OH_IPC_MessageOption *option); | IPC消息发送函数。 |
| struct OHIPCRemoteProxy; | OHIPCRemoteProxy对象，用于向远端发送请求。 需要依赖元能力接口返回。 |
| OHIPCDeathRecipient* OH_IPCDeathRecipient_Create (OH_OnDeathRecipientCallback deathRecipientCallback, OH_OnDeathRecipientDestroyCallback destroyCallback, void *userData); | 创建远端OHIPCRemoteStub对象死亡通知对象OHIPCDeathRecipient。 |
| int OH_IPCRemoteProxy_AddDeathRecipient(OHIPCRemoteProxy *proxy, OHIPCDeathRecipient *recipient); | 向OHIPCRemoteProxy对象添加死亡监听， 用于接收远端OHIPCRemoteStub对象死亡的回调通知。 |
typedef int (*OH_OnRemoteRequestCallback)
(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply,
void *userData);
OHIPCRemoteStub* OH_IPCRemoteStub_Create
(const char *descriptor, OH_OnRemoteRequestCallback requestCallback,
OH_OnRemoteDestroyCallback destroyCallback, void *userData);
int OH_IPCRemoteProxy_SendRequest(const OHIPCRemoteProxy *proxy,
uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply,
const OH_IPC_MessageOption *option);
OHIPCRemoteProxy对象，用于向远端发送请求。
需要依赖元能力接口返回。
OHIPCDeathRecipient* OH_IPCDeathRecipient_Create
(OH_OnDeathRecipientCallback deathRecipientCallback,
OH_OnDeathRecipientDestroyCallback destroyCallback,
void *userData);
int OH_IPCRemoteProxy_AddDeathRecipient(OHIPCRemoteProxy *proxy,
OHIPCDeathRecipient *recipient);
向OHIPCRemoteProxy对象添加死亡监听，
用于接收远端OHIPCRemoteStub对象死亡的回调通知。
详细的接口说明请参考IPCKit。
开发步骤
以下步骤描述了如何使用IPCKit提供的CAPI接口，创建远端Stub和使用客户端代理Proxy进行通信，同时兼备远端死亡通知接收能力。
1. 添加动态链接库
CMakeLists.txt中添加以下lib。
2. 头文件
3. 异步调用场景
3.1 公共数据及函数定义
3.2 服务端对象: IpcCApiStubTest
3.3 客户端代理对象: IpcCApiProxyTest
3.4 服务端调用入口，服务端文件"libipcCapiDemo.so"
3.5 客户端调用入口

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/localization-kit-V14
爬取时间: 2025-04-28 00:47:59
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-l10n-V14
爬取时间: 2025-04-28 00:48:13
来源: Huawei Developer
不同地区用户的语言、文化背景各不相同，且部分用户可能讲多种语言。因此，应用发布面向不同地区版本时，需要充分识别语言、地区和文化的差异。通过国际化和本地化过程，可使应用界面显示符合当地用户的使用习惯，增加应用潜在市场。
国际化（Internationalization，I18n）是系统提供的一套能力集，支持设置区域特性、时区和夏令时等，满足应用多语言多文化的设计需求。其中，区域特性能力包括设置不同地区的时间日期、数字与度量衡、电话号码、日历和历法、语言等，时区和夏令时能力包括获取时区、夏令时跳变等。国际化通常在应用设计开发阶段，设计和开发过程中不设定用户使用的语言，采用通用设计。
为使应用在不同市场可以运行，国际化为应用开发提供了一些准则，包括：不可对用户的文化和习惯进行假设，例如不能假设所有地区均以逗号作为数字分组分隔符，然后在代码里面将数字分组分隔符硬编码为逗号等；UI元素（如图片、字串）应作为应用资源从代码逻辑中分离出来，当需要提供其他地区用户版本时，仅需翻译对应资源，避免修改代码逻辑，提高效率，避免应用重新设计开发。
本地化（Localization，L10n）在应用定制阶段，是开发者为满足不同地区用户在语言和文化方面的需求，针对具体的目标语言对应用进行翻译和定制，过程包括配置多语言等资源翻译、敏感禁忌检查和测试。
配置多语言资源是为应用配置不同国家和地区、不同语言的内容，使应用界面加载显示符合所在区域使用习惯的内容。资源翻译是本地化过程的一个基本步骤，资源经翻译后才能形成多语言资源，包括UI元素翻译和代码翻译。翻译时采用UI元素与代码逻辑分离的原则，降低翻译难度。翻译完成后，会将UI元素按照类型（如图片、音视频）加载至相应语言的应用资源文件中。当界面加载资源时，根据应用语言列表加载和显示对应资源。
本地化过程还包括敏感禁忌检查和测试。敏感禁忌是开发者对用户界面显示的内容进行检查，界面中不允许显示可能导致舆情的内容，包括政治、宗教、文化等方面。测试是指开发者使用系统本地化测试能力检查应用是否存在未翻译字串、翻译是否准确、应用界面排版、界面显示是否符合本地用户习惯等问题。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-V14
爬取时间: 2025-04-28 00:48:26
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-ui-design-V14
爬取时间: 2025-04-28 00:48:40
来源: Huawei Developer
一套有效的国际化界面布局设计规则，既可以树立产品在国际化设计中产品调性，还可以保证操作的一致性，遵循以下设计规则可有效提升应用全球化质量。
界面空间预留与灵活布局
不同语言的译文长度存在较大差异，翻译可能造成界面文本长度增加，为了确保界面字串翻译成其他语言后不被截断，最佳做法是使用灵活的动态布局，即UI控件根据文本内容长度动态调整，重新排版。在实际开发过程中，若无法保证灵活布局，则应预留足够的文本空间。以英文为基础，相对于原始英语字符串，翻译需要预留的空间参考如表1。
表1界面预留空间参考表
| 英文字符数量（个） | 预留的空间比率 |
| --- | --- |
| 小于等于10 | 100%～200% |
| 大于等于11，小于等于20 | 80%~100% |
| 大于等于21，小于等于30 | 60%~80% |
| 大于等于31，小于等于50 | 40%~60% |
| 大于等于51，小于等于70 | 30%~40% |
| 大于等于71 | 30% |
界面镜像
不同国家对文本对齐方式和读取顺序有所不同，例如英语采用从左到右的顺序，阿拉伯语和希腊语则采用从右到左（RTL）的顺序。为了使界面显示的内容符合当地用户语言习惯，需确保UI元素布局支持界面镜像，如图1和图2 。UI元素界面镜像的设计要点如下：
-  用户界面 (UI)布局镜像。 用户界面排列允许从右到左的内容按其原始布局显示，满足双向市场体验。如"ABC"，按照从左到右的顺序应显示"ABC"，按照从右向左的顺序应显示为“CBA”。
-  UI元素镜像。 带有方向性的UI 元素控件和图标，遵循镜像规则，如图3、图4、图5。部分图标没有方向性或者与现实中的物体相关，不需要镜像，例如时钟表盘。
-  触控与操作。 确保界面各元素触控或操作符合从右至左的阅读顺序，例如对于多页签，一般往左划表示往后，而在RTL语言下，往右划表示往后。
-  支持混合文本。 文本方向支持可实现出色的混合文本呈现（双向版本中有英语文本，反之亦然）。
图1一般布局示例（英文）
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170421.85596501673911260349794902885804:50001231000000:2800:9BBF7DBEB3FEDABA2D01C429994EA40142A1FD890E55C3892FB7A8516C789DAB.png)
图2镜像布局示例（阿拉伯文）
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170421.33129770295452689000508584898384:50001231000000:2800:19BF4597D9D4859523B4C8F55D93121F7E53847F91DCD6FE3F5369CA5B50ABA4.png)
图3一般图标资源
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170421.18477983438605670851703039010595:50001231000000:2800:207447262D932AC021F646CB57CC17603C121AD7E52898744D5EEDADB5A56FA7.png)
图4RTL语言系统下提供的图标资源
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170421.06880238967478789004995421908616:50001231000000:2800:154D76EABAD513353F64E4C2EFF63471A7A4BC14D00664A3B7FECF6C6C273D59.png)
图5RTL语言下提供的镜像控件
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170421.96240685238252867635648365001266:50001231000000:2800:ABDC58F3083FACF894F7D89A55D9D0DD13C8ACAA49BB8F08D21B0247A35D8D20.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-locale-culture-V14
爬取时间: 2025-04-28 00:48:53
来源: Huawei Developer
功能介绍
广义地讲，区域标识是指通过数字、字母、符号或组合，作为唯一标识识别特定地理区域。
在国际化中，区域标识是对用户群体的抽象，包括用户语言、脚本（使用的文字系统，如中文可用简体字或繁体字）、所在国家或地区，以及其他一些文化习惯（如历法、数字系统）等。区域标识是应用实现国际化能力的基础，开发过程中需通过目标区域标识对象控制和实现国际化行为。
实现原理
区域标识由语言、脚本、国家地区和扩展参数四部分组成。其中，语言是必填内容，详细说明可参考表1；支持的扩展参数参考表2，不同语言对应的数字系统参考表3，表中未列出的语言均使用阿拉伯数字系统。
表1区域标识组成
| 组成成分 | 说明 |
| --- | --- |
| 语言 | 表示用户使用的语言，由2~3个小写英文字母组成。例如，中文使用”zh”表示。 更多语言代码列表请参考ISO-639标准。 |
| 脚本 | 表示用户使用的字符集，由首字母大写的4个英文字母组成。例如，简体使用”Hans”表示。 更多脚本代码列表请参考ISO-15924标准。 |
| 国家地区 | 表示用户所在的国家或地区，使用2个大写英文字母表示。例如，中国使用”CN”表示。 更多的国家地区代码列表请参考ISO-3166标准。 |
| 扩展参数 | 表示用户其他的特征，包括历法、字符串排序、数字系统、小时周期，由小写字母u开头，每一个扩展参数由key和value组成，使用中划线拼接。例如，农历拼音排序使用”u-ca-chinese-co-pinyin”。 支持的扩展参数请参考表2，更多的扩展参数取值请参考BCP 47扩展。 |
表示用户使用的语言，由2~3个小写英文字母组成。例如，中文使用”zh”表示。
更多语言代码列表请参考ISO-639标准。
表示用户使用的字符集，由首字母大写的4个英文字母组成。例如，简体使用”Hans”表示。
更多脚本代码列表请参考ISO-15924标准。
表示用户所在的国家或地区，使用2个大写英文字母表示。例如，中国使用”CN”表示。
更多的国家地区代码列表请参考ISO-3166标准。
表示用户其他的特征，包括历法、字符串排序、数字系统、小时周期，由小写字母u开头，每一个扩展参数由key和value组成，使用中划线拼接。例如，农历拼音排序使用”u-ca-chinese-co-pinyin”。
支持的扩展参数请参考表2，更多的扩展参数取值请参考BCP 47扩展。
表2扩展参数
| 参数 | 说明 |
| --- | --- |
| ca | 表示用户使用的历法系统。例如，农历使用”chinese”表示。 |
| co | 表示用户使用的字符串排序规则，包括。例如，按照拼音排序使用”pinyin”表示。 |
| hc | 表示用户使用的小时周期。例如，0~11小时周期使用”h11”表示。 |
| nu | 表示用户使用的数字系统。例如，阿拉伯数字系统使用”arab”表示，具体请参考表3。 |
| kn | 表示用户排序时对数字的处理方式。 - “true”表示将数字作为整体进行数值比较。 - “false”表示将数字作为普通字符比较。 |
| kf | 表示用户排序时是否考虑字符的大小写。 - “upper”表示将大写字母排序在前。 - “lower”表示将小写字母排序在前。 - “false”表示使用当前区域的默认值。 |
表示用户排序时对数字的处理方式。
- “true”表示将数字作为整体进行数值比较。
- “false”表示将数字作为普通字符比较。
表示用户排序时是否考虑字符的大小写。
- “upper”表示将大写字母排序在前。
- “lower”表示将小写字母排序在前。
- “false”表示使用当前区域的默认值。
表3语言和本地数字系统
| 语言 | 本地数字系统 |
| --- | --- |
| ar | arab |
| as | beng |
| bn | beng |
| fa | arabext |
| mr | deva |
| my | mymr |
| ne | deva |
| ur | latn |
| 其他语言 | arab |
开发步骤
以时间日期格式化为例，DateTimeFormat类的详细说明请参考API文档。
1.  导入模块。
```typescript
import { intl } from '@kit.LocalizationKit';
```
2.  创建区域标识对象。如下给出了三种方法。
```typescript
let date = new Date(2023, 9, 15);
// 方法一：通过区域标识字符串创建区域标识对象
let zhLocale = new intl.Locale("zh-Hans-CN-u-nu-latn");
// 方法二：通过区域标识字符串和LocaleOptions对象创建区域标识对象
let enLocale = new intl.Locale("en", {numberingSystem: "latn"});
// 方法三：通过默认Locale函数创建系统区域标识对象
let systemLocale = new intl.Locale();
```
3.  格式化时间日期。 创建区域识别对象后，将其传入时间日期格式类的构造函数，创建指定区域标识的时间日期格式化类，并实现格式化。与步骤2对应，步骤3呈现了三种实现时间日期格式化的方法。
```typescript
// 方法一
let zhDateTimeFmt = new intl.DateTimeFormat(zhLocale.toString());
let result = zhDateTimeFmt.format(date); // result = "2023/10/15"
// 方法二
let enDateTimeFmt = new intl.DateTimeFormat(enLocale.toString());
result = enDateTimeFmt.format(date); // result = "10/15/23"
// 方法三
let systemDateTimeFmt = new intl.DateTimeFormat(systemLocale.toString());
result = systemDateTimeFmt.format(date); // result = "2023/10/15" （具体显示效果依赖于当前系统环境）
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-language-user-preferences-V14
爬取时间: 2025-04-28 00:49:07
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-system-language-region-V14
爬取时间: 2025-04-28 00:49:20
来源: Huawei Developer
实现原理
在设置的“语言和地区”中可以添加多种语言，多种语言形成的列表称为语言列表，列表中的第一个语言称为系统语言。系统区域是依据区域标识划分的特定地区。
当设置/切换系统语言时，系统会检查扩展参数与系统语言是否匹配，若不匹配，则删除扩展属性。例如，当前系统语言设置为阿拉伯语“ar”，使用本地数字为“arab”。当系统语言切换为马来西亚语“my”时，本地数字属性更改为马来西亚的本地数字“mymr”。当切换为中文时，因中文不支持设置本地数字，采用阿拉伯数字，因此本地数字的扩展属性会被移除。
开发步骤
接口具体使用方法和说明请参考System的API接口文档。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.  获取系统语言、系统地区、系统区域。
```typescript
// 获取系统语言
let systemLanguage = i18n.System.getSystemLanguage();  // systemLanguage为当前系统语言
// 获取系统地区
let systemRegion = i18n.System.getSystemRegion();  // systemRegion为当前系统地区
// 获取系统区域
let systemLocale = i18n.System.getSystemLocale();  // systemLocale为当前系统区域
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-preferred-language-V14
爬取时间: 2025-04-28 00:49:33
来源: Huawei Developer
功能介绍
对于多语言用户，很多情况下会将系统语言设置为一种语言（如中文），将特定APP应用的语言设置为另一种语言（如英语）。当界面加载应用资源时，依据应用设置的语言进行显示。开发过程中，开发者需将应用国际化特性区域设置为应用偏好语言，使应用界面的国际化特性与界面加载的资源保持一致。当前，应用仅支持设置一种语言。
开发步骤
接口具体使用方法和说明请参考getAppPreferredLanguage的API接口文档。
以时间日期格式化为例说明。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.  需要获取应用的偏好语言。
```typescript
let appPreferredLanguage: string = i18n.System.getAppPreferredLanguage(); // 获取应用偏好语言
```
3.  设置应用的偏好语言。将应用偏好语言设置为目标语言后，该应用的界面会切换为目标语言。设置应用的偏好语言仅影响应用本身，不会影响系统语言设置。
```typescript
try {
i18n.System.setAppPreferredLanguage("zh-Hans"); // 设置应用偏好语言为zh-Hans
} catch(error) {
let err: BusinessError = error as BusinessError;
console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```
4.  清除应用的偏好语言。将应用偏好语言设置为"default"后，该应用的界面会跟随系统语言变化，该特性将在应用重新启动后生效。
```typescript
try {
i18n.System.setAppPreferredLanguage("default"); // 清除应用的偏好语言
} catch(error) {
let err: BusinessError = error as BusinessError;
console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-time-date-V14
爬取时间: 2025-04-28 00:49:46
来源: Huawei Developer
使用场景
在不同的国家和文化中，时间和日期格式的表示方法有所不同，使用惯例的不同点包括：日期中年月日的顺序、时间中时分秒的分隔符等。若应用中需展示时间日期，要确保界面以合适的方式显示，以便用户能够理解。
时间日期国际化包括时间日期格式化、相对时间格式化、时间段格式化。时间日期格式化是指将时间和日期转换为指定格式的字符串。相对时间格式化是指将一个时间点与另一个时间点之间的时间差转换为指定格式，时间差如“30秒前”、“1天后”。时间段格式化是指将一段时间转换为指定格式，时间段如“星期三”、“8:00--11:30”。
约束与限制
1.  日期格式和时间格式需同时设置。若设置了时间格式，未设置日期格式，只显示时间格式；若设置了日期格式，未设置时间格式，只显示日期格式。
2.  若设置了时间或日期格式，则不支持设置年、月、日、时、分、秒、工作日格式；不设置时间或日期格式时，支持独立设置年、月、日、时、分、秒、工作日格式。
开发步骤
时间日期和相对时间格式化
时间日期格式化将表示时间日期的Date对象，通过DateTimeFormat类的format接口实现格式化，具体开发步骤如下。
1.  导入模块。
```typescript
import { intl } from '@kit.LocalizationKit';
```
2.  创建DateTimeFormat对象。 传入单独的locale参数或locale列表，若传入列表使用第一个有效的locale创建对象。不传入locale参数时，使用系统当前的locale创建对象。 构造函数支持通过DateTimeOptions设置不同的时间日期格式，具体请参考表1-表10。
```typescript
let dateFormat: intl.DateTimeFormat = new intl.DateTimeFormat(locale: string | Array<string>, options?: DateTimeOptions);
let dateFormat: intl.DateTimeFormat = new intl.DateTimeFormat(); //不传入locale参数
```
3.  时间日期和相对时间格式化。
```typescript
// 时间日期格式化
let formattedDate: string = dateFormat.format(date: Date);
// 相对时间格式化
let formattedDateRange: string = dateFormat.formatRange(startDate: Date, endDate: Date);
```
4.  获取格式化选项，查看对象的设置信息。
```typescript
let options: intl.DateTimeOptions = dateFormat.resolvedOptions();
```
时间日期格式化选项
以时间：2021年9月17日 13:04:00、2021年9月17日 00:25:00，locale: zh-CN和en为例，说明DateTimeOptions不同的取值和显示结果。
表1日期显示格式(dateStyle)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示结果 | 2021年9月17日 13:04:00，locale为en显示结果 |
| --- | --- | --- | --- |
| full | 完整的日期显示，包含年份、月份、天数和星期。 | 2021年9月17日星期五 | Friday, September 17, 2021 |
| long | 详细的日期显示，包含年份、月份和天数。 | 2021年9月17日 | September 17, 2021 |
| short | 简短的日期显示，包含年份、月份和天数。 | 2021/9/17 | 9/17/21 |
| medium | 中等长度日期显示，包含年份、月份和天数。 | 2021年9月17日 | Sep 17, 2021 |
表2时间显示格式(timeStyle)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示结果 | 2021年9月17日 13:04:00，locale为en显示结果 |
| --- | --- | --- | --- |
| full | 完整的时间显示，包含时区和时间，时间精确到秒。 | 中国标准时间 13:04:00 | 13:04:00 China Standard Time |
| long | 详细的时间显示，包含时区和时间，时区以GMT+时区偏移表示，时间精确到秒。 | GMT+8 13:04:00 | 13:04:00 GMT+8 |
| short | 简短时间显示，包含小时和分钟。 | 13:04 | 13:04 |
| medium | 中等长度时间显示，包含小时、分钟和秒。 | 13:04:00 | 13:04:00 |
表3年份显示格式(year)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示结果 | 2021年9月17日 13:04:00，locale为en显示结果 |
| --- | --- | --- | --- |
| numeric | 完整的年份显示。 | 2021年 | 2021 |
| 2-digit | 用完整年份的后2位数字表示年份。 | 21年 | 21 |
表4星期显示格式(weekday)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示结果 | 2021年9月17日 13:04:00，locale为en显示结果 |
| --- | --- | --- | --- |
| long | 详细的星期显示。 | 星期五 | Friday |
| short | 简短的星期显示。 | 周五 | Fri |
| narrow | 最简短的星期显示。 | 五 | F |
表5时制格式(hourCycle)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示结果 | 2021年9月17日 00:25:00，locale为zh-CN显示结果 |
| --- | --- | --- | --- |
| h11 | 用0-11表示小时。 | 下午1:04 | 上午0:25 |
| h12 | 用1-12表示小时。 | 下午1:04 | 上午12:25 |
| h23 | 用0-23表示小时。 | 13:04 | 00:25 |
| h24 | 用1-24表示小时。 | 13:04 | 24:25 |
在不设置dateStyle或timeStyle参数时，hourCycle不同取值的显示效果如上表格。
表6时制格式(hourCycle)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示结果 | 2021年9月17日 00:25:00，locale为zh-CN显示结果 |
| --- | --- | --- | --- |
| h11 | 用1-24表示小时。 | 下午13:04 | 上午24:25 |
| h12 | 用1-12表示小时。 | 下午1:04 | 上午12:25 |
| h23 | 用0-11表示小时。 | 1:04 | 0:25 |
| h24 | 用0-23表示小时。 | 13:04 | 0:25 |
在设置dateStyle或timeStyle参数时，hourCycle不同取值的显示效果如上表格。
表7月份格式(month)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示结果 | 2021年9月17日 13:04:00，locale为en显示结果 |
| --- | --- | --- | --- |
| numeric | 以数字形式显示月份。 | 9月 | 9 |
| 2-digit | 以两位数字形式显示月份。 | 09月 | 09 |
| long | 详细的月份显示。 | 九月 | September |
| short | 简短的月份显示。 | 9月 | Sep |
| narrow | 最简短的月份显示。 | 9 | S |
表8时区名称的本地化表示(timeZoneName)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示结果 | 2021年9月17日 13:04:00，locale为en显示结果 |
| --- | --- | --- | --- |
| long | 详细的时区名称显示。 | 中国标准时间 | China Standard Time |
| short | 简短的时区名称显示。 | GMT+8 | GMT+8 |
表9纪元的显示格式(era)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示效果 | 2021年9月17日 13:04:00，locale为en显示效果 |
| --- | --- | --- | --- |
| long | 详细的纪元显示。 | 公元 | Anno Domini |
| short | 简短的纪元显示。 | 公元 | AD |
| narrow | 最简短的纪元显示。 | 公元 | A |
表10时段的显示格式(dayPeriod)
| 取值 | 描述 | 2021年9月17日 13:04:00，locale为zh-CN显示效果 | 2021年9月17日 13:04:00，locale为en显示效果 |
| --- | --- | --- | --- |
| long | 详细的时段表述。 | 下午 | in the afternoon |
| short | 简短的时段表示。 | 下午 | in the afternoon |
| narrow | 最简短的时段表示。 | 下午 | in the afternoon |
开发实例
```typescript
// 导入模块
import { intl } from '@kit.LocalizationKit';
let date = new Date(2021, 8, 17, 13, 4, 0); // 时间日期为2021.09.17 13:04:00
let startDate = new Date(2021, 8, 17, 13, 4, 0);
let endDate = new Date(2021, 8, 18, 13, 4, 0);
// 在软件上展示完整的时间信息
let dateFormat1 = new intl.DateTimeFormat('zh-CN', {dateStyle: 'full', timeStyle: 'full'});
let formattedDate1 = dateFormat1.format(date); // formattedDate1: 2021年9月17日星期五 中国标准时间 13:04:00
// 在有限的空间展示简短的时间信息
let dateFormat2 = new intl.DateTimeFormat('zh-CN', {dateStyle: 'short', timeStyle: 'short'});
let formattedDate2 = dateFormat2.format(date); // formattedDate2: 2021/9/17 13:04
// 自定义年月日时分秒的显示效果
let dateFormat3 = new intl.DateTimeFormat('zh-CN', {year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit'});
let formattedDate3 = dateFormat3.format(date); // formattedDate3: 2021/09/17 13:04:00
// 仅显示一部分时间
let dateFormat4 = new intl.DateTimeFormat('zh-CN', {month: 'long', day: 'numeric', weekday: 'long' });
let formattedDate4 = dateFormat4.format(date); // formattedDate4: 9月17日星期五
// 自定义时制格式
let dateFormat5 = new intl.DateTimeFormat('zh-CN', {dateStyle: 'short', timeStyle: 'short', hourCycle: 'h11'});
let formattedDate5 = dateFormat5.format(date); // formattedDate5: 2021/9/17 下午13:04
// 面向习惯于其他数字系统的用户
let dateFormat6 = new intl.DateTimeFormat('zh-CN', {dateStyle: 'short', timeStyle: 'short', numberingSystem: 'arab'});
let formattedDate6 = dateFormat6.format(date); // formattedDate6: ٢٠٢١/٩/١٧ ١٣:٠٤
// 格式化时间段
let dataFormat7 = new intl.DateTimeFormat('en-GB');
let formattedDateRange = dataFormat7.formatRange(startDate, endDate); // formattedDateRange: 17/09/2021 - 18/09/2021
// 获取格式化选项
let dataFormat8 = new intl.DateTimeFormat('en-GB', {dateStyle: 'full'});
let options = dataFormat8.resolvedOptions();
let dateStyle = options.dateStyle; // dateStyle: full
```
相对时间格式化
格式化相对时间将表示时间日期的Date对象，通过RelativeTimeFormat类的format接口实现格式化，具体开发步骤如下。
1.  导入模块。
```typescript
import { intl } from '@kit.LocalizationKit';
```
2.  创建RelativeTimeFormat对象。 构造函数支持通过RelativeTimeFormatInputOptions设置不同的输出消息格式和国际化消息长度，具体请参考表7-表8。
```typescript
let relativeTimeFormat: intl.RelativeTimeFormat = new intl.RelativeTimeFormat(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions);
```
3.  格式化相对时间。value为格式化的数值，unit为格式化的单位。
```typescript
let formattedRelativeTime: string = relativeTimeFormat.format(value: number, unit: string);
```
4.  自定义相对时间的格式化。
```typescript
let parts: Array<object> = relativeTimeFormat.formatToParts(value: number, unit: string);
```
5.  获取相对时间格式化选项，查看对象的设置信息。
```typescript
let options: intl.RelativeTimeFormatInputOptions = relativeTimeFormat.resolvedOptions();
```
相对时间格式化选项
以相对时间：一天前，locale: fr-FR和en-GB为例，说明RelativeTimeFormatInputOptions不同的取值和显示结果。
表11数值表示(numeric)
| 取值 | 描述 | 显示效果(fr-FR) | 显示效果(en-GB) |
| --- | --- | --- | --- |
| always | 使用数值表示相对时间。 | il y a 1 jour | 1 day ago |
| auto | 根据locale自适应的选择短语或者数值表示相对时间。 | hier | yesterday |
表12相对时间样式(style)
| 取值 | 描述 | 显示效果(fr-FR) | 显示效果(en-GB) |
| --- | --- | --- | --- |
| long | 详细的相对时间显示。 | il y a 1 jour | 1 day ago |
| short | 简短的相对时间显示。 | il y a 1 j | 1 day ago |
| narrow | 最简短的相对时间显示。 | -1 j | 1 day ago |
开发实例
```typescript
// 导入模块
import { intl } from '@kit.LocalizationKit';
// 显示相对时间
let relativeTimeFormat1 = new intl.RelativeTimeFormat('en-GB');
let formattedRelativeTime1 = relativeTimeFormat1.format(-1, 'day'); // formattedRelativeTime1: 1 day ago
// 口语化
let relativeTimeFormat2 = new intl.RelativeTimeFormat('en-GB', {numeric: "auto"});
let formattedRelativeTime2 = relativeTimeFormat2.format(-1, 'day'); // formattedRelativeTime2: yesterday
// 部分语言支持更为简短的显示风格
let relativeTimeFormat3 = new intl.RelativeTimeFormat('fr-FR'); // 默认style为long
let formattedRelativeTime3 = relativeTimeFormat3.format(-1, 'day'); // formattedRelativeTime3: il y a 1 jour
let relativeTimeFormat4 = new intl.RelativeTimeFormat('fr-FR', {style: 'narrow'});
let formattedRelativeTime4 = relativeTimeFormat4.format(-1, 'day'); // formattedRelativeTime4: -1 j
// 自定义区域设置格式的相对时间格式
let relativeTimeFormat5 = new intl.RelativeTimeFormat('en-GB', {style: 'long'});
// parts: [{type: 'literal', value: 'in'}, {type: 'integer', value: 1, unit: 'day'}, {type: 'literal', value: 'day'}]
let parts = relativeTimeFormat5.formatToParts(1, 'day');
// 获取RelativeTimeFormat对象的格式化选项
let relativeTimeFormat6 = new intl.RelativeTimeFormat('en-GB', {numeric: 'auto'});
let options = relativeTimeFormat6.resolvedOptions();
let numeric = options.numeric; // numeric: auto
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-numbers-weights-measures-V14
爬取时间: 2025-04-28 00:50:00
来源: Huawei Developer
使用场景
在不同的国家和文化中，数字、货币和度量衡的表示方法有所不同，包括什么符号作为小数分隔符、分隔符后显示几位数字、使用什么样的货币和度量衡单位等。例如，开发者需要在应用界面显示数字“1,000”（一千），用于表示一件商品的价格。若采用固定格式“1,000”，由于在欧洲某些国家（如德国）使用逗号表示小数点，用户会理解为“1”。为了使界面呈现格式符合当地人的使用习惯，需要对数字、货币和度量衡进行格式化，格式化后会根据用户当前设置的语言和地区进行显示。
开发步骤
数字格式化
数字格式化通过NumberFormat的format接口实现，具体开发步骤如下。
1.  导入模块。
```typescript
import { intl } from '@kit.LocalizationKit';
```
2.  创建NumberFormat对象。 传入locale列表时，使用第一个有效的locale创建对象。不传入locale参数时，使用系统当前的locale创建对象。 构造函数支持通过NumberOptions设置不同的数字格式化格式，具体请参考表1-表8。
```typescript
let numberFormat: intl.NumberFormat = new intl.NumberFormat(locale: string | Array<string>, options?: NumberOptions);
```
3.  数字格式化，根据numberFormat的设置格式化number。
```typescript
let formattedNumber: string = numberFormat.format(number: number);
```
4.  获取数字格式化选项，查看对象的设置信息。
```typescript
let options: intl.NumberOptions = numberFormat.resolvedOptions();
```
数字格式化选项
对于数字，通过NumberOptions参数可以设置最小整数位数、最小小数位数、最大小数位数、最低有效位数、最大有效位数、是否分组显示、数字的格式化规格、紧凑型的显示格式，以及数字的显示格式和数字系统。其中，数字的显示格式包括decimal(十进制)、percent(百分数)、currency(货币)、unit(单位)。
以123000.123为例，各属性参数取值和显示效果如下表所示。
表1最小整数位数(minimumIntegerDigits)
| 取值 | 显示效果 |
| --- | --- |
| 6 | 123,000.123 |
| 7 | 0,123,000.123 |
表2最小小数位数(minimumFractionDigits)
| 取值 | 显示效果 |
| --- | --- |
| 3 | 123,000.123 |
| 4 | 123,000.1230 |
表3最大小数位数(maximumFractionDigits)
| 取值 | 显示效果 |
| --- | --- |
| 3 | 123,000.123 |
| 2 | 123,000.12 |
表4最低有效位数(minimumSignificantDigits)
| 取值 | 显示效果 |
| --- | --- |
| 9 | 123,000.123 |
| 10 | 123,000.1230 |
表5最大有效位数(maximumSignificantDigits)
| 取值 | 显示效果 |
| --- | --- |
| 9 | 123,000.123 |
| 8 | 123,000.12 |
表6是否分组显示(useGrouping)
| 取值 | 显示效果 |
| --- | --- |
| true | 123,000.123 |
| false | 123000.123 |
表7数字的格式化规格(notation)
| 取值 | 显示效果 |
| --- | --- |
| standard | 123,000.123 |
| scientific | 1.230001E5 |
| engineering | 123.000123E3 |
| compact | 123K |
表8紧凑型的显示格式(compactDisplay)
| 取值 | 显示效果 |
| --- | --- |
| short | 123K |
| long | 123 thousand |
开发实例
```typescript
// 导入模块
import { intl } from '@kit.LocalizationKit';
// 用科学计数法显示数字
let numberFormat1 = new intl.NumberFormat('zh-CN', {notation: 'scientific', maximumSignificantDigits: 3});
let formattedNumber1 = numberFormat1.format(123400); // formattedNumber1: 1.23E5
// 用紧凑的格式显示数字
let numberFormat2 = new intl.NumberFormat('zh-CN', {notation: 'compact', compactDisplay: 'short'});
let formattedNumber2 = numberFormat2.format(123400); // formattedNumber2: 12万
// 显示数字的符号
let numberFormat3 = new intl.NumberFormat('zh-CN', {signDisplay: 'always'});
let formattedNumber3 = numberFormat3.format(123400); // formattedNumber3: +123,400
// 显示百分数
let numberFormat4 = new intl.NumberFormat('zh-CN', {style: 'percent'});
let formattedNumber4 = numberFormat4.format(0.25); // formattedNumber4: 25%
```
货币和单位格式化
货币和单位的格式化基于数字格式化，在创建货币和单元格式化对象时，将数字的显示风格分别设置为“currency(货币)”和“unit(单位)”。同样，货币和单位的构造函数也支持通过NumberOptions设置不同的格式，各属性参数取值和显示效果如下表所示。
货币格式化选项
以货币单位: USD，数值: -12300为例。
表9货币单位的符号(currencySign)
| 取值 | 显示效果 |
| --- | --- |
| standard | -US$12,300.00 |
| accounting | (US$12,300.00) |
表10货币的显示方式(currencyDisplay)
| 取值 | 显示效果 |
| --- | --- |
| symbol | -US$12,300.00 |
| narrowSymbol | -$12,300.00 |
| code | -USD 12,300.00 |
| name | -12,300.00 US dollars |
单位格式化选项
以单位名称：hectare，数字大小：-12300为例。
表11单位的显示格式(unitDisplay)
| 取值 | 显示效果 |
| --- | --- |
| long | -12,3000 hectares |
| short | -12,300 ha |
| narrow | -12,300ha |
表12单位的使用场景(unitUsage)
| 取值 | 显示效果 |
| --- | --- |
| 不设置 | -12,300 ha |
| default | -47.491 sq mi |
| area-land-agricult | -30,393.962 ac |
开发实例
```typescript
// 导入模块
import { intl } from '@kit.LocalizationKit';
// 格式化货币
let numberFormat5 = new intl.NumberFormat('zh-CN', {style: 'currency', currency: 'USD'});
let formattedNumber5 = numberFormat5.format(123400); // formattedNumber5: US$123,400.00
// 用名称表示货币
let numberFormat6 = new intl.NumberFormat('zh-CN', {style: 'currency', currency: 'USD', currencyDisplay: 'name'});
let formattedNumber6 = numberFormat6.format(123400); // formattedNumber6: 123,400.00美元
// 格式化度量衡
let numberFormat7 = new intl.NumberFormat('en-GB', {style: 'unit', unit: 'hectare'});
let formattedNumber7 = numberFormat7.format(123400); // formattedNumber7: 123,400 ha
// 格式化特定场景下度量衡，如面积-土地-农业
let numberFormat8 = new intl.NumberFormat('en-GB', {style: 'unit', unit: 'hectare', unitUsage: 'area-land-agricult'});
let formattedNumber8 = numberFormat8.format(123400); // formattedNumber8: 304,928.041 ac
```
度量衡转换
单位转换并根据区域和风格进行格式化，通过I18NUtil类的unitConvert接口实现，具体开发步骤如下。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  度量衡转换。 将度量衡从fromUnit转换到toUnit，数值为value，并根据区域和风格进行格式化。style可取不同的值，显示不用效果，具体请参考表13。
```typescript
let convertedUnit: string = i18n.I18NUtil.unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string);
```
格式化风格
以fromUnit为美制单位cup，toUnit为公制单位liter，数字大小：1000为例。
表13格式化使用的风格(style)
| 取值 | 显示效果 |
| --- | --- |
| long | 236.588 liters |
| short | 236.588 L |
| narrow | 236.588L |
开发实例
```typescript
// 导入模块
import { i18n } from '@kit.LocalizationKit';
// 设置要转换的单位和目标单位
let fromUnit: i18n.UnitInfo = {unit: 'cup', measureSystem: 'US'};
let toUnit: i18n.UnitInfo = {unit: 'liter', measureSystem: 'SI'};
// 以en-US区域参数转换度量衡
let convertedUnit1 = i18n.I18NUtil.unitConvert(fromUnit, toUnit, 1000, 'en-US'); // convertedUnit1: 236.588 L
// 显示完整的度量衡
let convertedUnit2 = i18n.I18NUtil.unitConvert(fromUnit, toUnit, 1000, 'en-US', 'long'); // convertedUnit2: 236.588 liters
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-phone-numbers-V14
爬取时间: 2025-04-28 00:50:13
来源: Huawei Developer
使用场景
不同国家和地区的电话号码在号码位数、组合方式、呈现方式等都存在差异。同时，在不同环境和条件下，电话号码可能存在不同的拨打方式和号码格式。例如，在中国境内跨地区打电话，通常需要先输入“0”，再拨打区号和八位电话号码，而在香港或澳门拨打电话时，需要不同的拨号方式。
通过号码格式化，可以根据需要给用户展示特定格式的电话号码。
开发步骤
电话号码格式化通过PhoneNumberFormat的format接口实现，具体开发步骤如下。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  创建PhoneNumberFormat对象。 构造函数支通过PhoneNumberFormatOptions设置不同的电话号码格式，具体请参考表1。
```typescript
let phoneNumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat(country: string, options?: PhoneNumberFormatOptions);
```
3.  电话号码格式化。
```typescript
let formattedPhoneNumber: string = phoneNumberFormat.format(phoneNumber: string);
```
4.  判断电话号码正确性和号码归属地。
```typescript
let isValidNumber: boolean = phoneNumberFormat.isValidNumber(phoneNumber: string); // 判断电话号码正确性
let locationName: string = phoneNumberFormat.getLocationName(number: string, locale: string); // 获取号码归属地
```
电话号码格式化选项
以电话号码158****2312，所属国家代码CN为例，说明PhoneNumberFormatOptions不同取值和显示效果。
表1电话号码格式化的类型(type)
| 取值 | 显示效果 |
| --- | --- |
| E164 | +86 158****2312 |
| INTERNATIONAL | +86 158 **** 2312 |
| NATIONAL | 158 **** 2312 |
| RFC3966 | tel:+86-158-****-2312 |
| TYPING | 158 *** |
开发实例
```typescript
// 导入模块
import { i18n } from '@kit.LocalizationKit';
// 格式化电话号码
let phoneNumberFormat1 = new i18n.PhoneNumberFormat('CN');
let formattedPhoneNumber1 = phoneNumberFormat1.format('158****2312'); // formattedPhoneNumber1: 158 **** 2312
// RFC3966类型的电话号码
let phoneNumberFormat2 = new i18n.PhoneNumberFormat('CN', {type: 'RFC3966'});
let formattedPhoneNumber2 = phoneNumberFormat2.format('158****2312'); // formattedPhoneNumber2: tel:+86-158-****-2312
// 判断电话号码是否有效
let phoneNumberFormat3 = new i18n.PhoneNumberFormat('CN');
let isValid = phoneNumberFormat3.isValidNumber('158****2312'); // isValid: true
// 以某种语言显示号码归属地
let phoneNumberFormat4 = new i18n.PhoneNumberFormat("CN");
let locationName4 = phoneNumberFormat4.getLocationName('158****2312', 'en-GB') // locationName4: XiAn, Shanxi
// 拨号中的电话号码格式化
let phoneNumberFmt = new i18n.PhoneNumberFormat('CN', {type: 'TYPING'});
let phoneNumber : string = "0755453";
let formatResult : string = "";
for (let i = 0; i < phoneNumber.length; i++) {
formatResult += phoneNumber.charAt(i);
formatResult = phoneNumberFmt.format(formatResult);
}
console.log(formatResult); // formatResult: 0755 453
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-calendar-V14
爬取时间: 2025-04-28 00:50:26
来源: Huawei Developer
使用场景
不同地区的用户使用不同的日历，大多数地区使用公历，也有些地区的用户使用其他日历，例如农历、伊斯兰历或希伯来历。此外，日历上的时间和日期也会随着时区和夏令时的不同而改变。因此，用户应设置符合本地习惯的日历。国际化提供了Calendar类，可以设置日历类型、日期、年月日、时区、一周的起始日期、一年中第一周的最小天数、判断具体某一天在日历中是否为周末、计算相差天数等。在应用开发过程中，开发者可以根据业务需求选择使用不同功能。
开发步骤
以查看公历对应的农历日期为例，说明Calendar类接口使用方法。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  公历相关用法。
```typescript
let calendar : i18n.Calendar = i18n.getCalendar("zh-Hans", "gregory");
// 设置日历对象的时间日期为2022.06.13 08:00:00
calendar.setTime(new Date(2022, 5, 13, 8, 0, 0));
calendar.setTime(10540800000);
// 设置日历对象的时间日期为2022.06.13 08:00:00
calendar.set(2022, 5, 13, 8, 0, 0);
// 设置日历对象的时区
calendar.setTimeZone("Asia/Shanghai");
// 获取日历对象的时区
let timezone: string = calendar.getTimeZone(); // Asia/Shanghai
// 获取日历对象的一周起始日
let firstDayOfWeek : number = calendar.getFirstDayOfWeek(); // 1
// 设置每一周的起始日
calendar.setFirstDayOfWeek(1);
// 获取一年中第一周的最小天数
let minimalDaysInFirstWeek : number = calendar.getMinimalDaysInFirstWeek(); // 1
// 设置一年中第一周的最小天数
calendar.setMinimalDaysInFirstWeek(3);
// 获取日历对象中与field相关联的值
let value: number = calendar.get("year"); // 2022
// 获取日历对象本地化名称
let calendarName: string = calendar.getDisplayName("zh-Hans"); // 公历
// 判断指定的日期在日历中是否为周末
let isWeekend : boolean= calendar.isWeekend(new Date(2023, 9, 15)); // true
// 在日历的给定字段进行加减操作
calendar.set(2023, 10, 15);
calendar.add("date", 2);
calendar.get("date"); // 17
// 比较日历和指定日期相差的天数
calendar.compareDays(new Date(2023, 10, 15)); // -3
```
3.  获取公历对应的农历日期。
```typescript
let calendar : i18n.Calendar = i18n.getCalendar("zh-Hans", "chinese");
//将公历信息设置到calendar对象，时间日期为2023.07.25 08:00:00
calendar.setTime(new Date(2023, 6, 25, 8, 0, 0));
//获取农历年月日
calendar.get("year"); // 返回干支纪年40，范围1-60
calendar.get("month"); // 返回值为5，指6月
calendar.get("date"); // 8日
```
表1支持的日历类型
| 类型 | 中文名称 |
| --- | --- |
| buddhist | 佛历 |
| chinese | 农历 |
| coptic | 科普特历 |
| ethiopic | 埃塞俄比亚历 |
| hebrew | 希伯来历 |
| gregory | 公历 |
| indian | 印度历 |
| islamic_civil | 伊斯兰希吉来历 |
| islamic_tbla | 伊斯兰天文历 |
| islamic_umalqura | 伊斯兰历（乌姆库拉） |
| japanese | 日本历 |
| persian | 波斯历 |
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-time-zone-dst-V14
爬取时间: 2025-04-28 00:50:39
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-time-zone-V14
爬取时间: 2025-04-28 00:50:53
来源: Huawei Developer
使用场景
全球各国家和地区的经度不同，地方时间也有所不同，因此划分了不同的时区。例如英国采用0时区，中国采用东8时区，中国时间要比英国快8个小时，中国北京中午12:00是英国伦敦凌晨4点。时区模块主要用于获取时区列表，同时，应用可基于获取的时区列表实现自身业务逻辑，如双时钟应用。
开发步骤
时区相关功能
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  开发实例，包括获取特定时区、计算固定和实际时区偏移量、获取和遍历时区列表等。
```typescript
// 获取巴西时区
let timezone = i18n.getTimeZone("America/Sao_Paulo"); // 传入特定时区，创建时区类
let timezoneId = timezone.getID();// America/Sao_Paulo
// 获取城市Id对应的时区对象
let aucklandTimezone = i18n.TimeZone.getTimezoneFromCity("Auckland");
let aucklandTzId = aucklandTimezone.getID(); // Pacific/Auckland
// 时区的本地化名称
let timeZoneName = timezone.getDisplayName("zh-Hans", true); // 巴西利亚标准时间
// 本地化城市名称
let cityDisplayName = i18n.TimeZone.getCityDisplayName("Auckland", "zh-Hans") // 奥克兰 (新西兰)
// 时区的固定偏移量
let rawOffset = timezone.getRawOffset(); // -10800000
// 时区的实际偏移量(固定偏移量+夏令时)
let offset = timezone.getOffset(1234567890);// -10800000
// 系统支持的时区Id列表
let ids = i18n.TimeZone.getAvailableIDs(); // ["America/Adak", "Asia/Hovd", "America/Sao_Paulo", "Asia/Jerusalem", "Europe/London",...]
// 系统支持的时区城市Id列表
let cityIdArray = i18n.TimeZone.getAvailableZoneCityIDs();  // ["Auckland", "Magadan", "Lord Howe Island",...]
// 遍历时区城市Id列表
let timezoneList: Array<object> = [];  // 呈现给用户的时区列表
class Item {
cityDisplayName : string = "";
timezoneId : string = "";
offset : string = "";
cityId : string = ""
}
for (let i =0 ; i < cityIdArray.length ; i++) {
let cityId = cityIdArray[i];
let timezone = i18n.TimeZone.getTimezoneFromCity(cityId); // 城市Id对应的时区对象
let cityDisplayName = i18n.TimeZone.getCityDisplayName(cityId, "zh-CN"); // 本地化城市名称
let timestamp = (new Date()).getTime()
let item : Item = {
cityDisplayName : cityDisplayName,
timezoneId : timezone.getID(),
offset : 'GMT'+ (timezone.getOffset(timestamp) / 3600*1000),
cityId : cityId
}
timezoneList.push(item);
}
// 指定地理坐标所在的时区对象数组
let timezoneArray = i18n.TimeZone.getTimezonesByLocation(-43.1, -22.5)
for (let i =0;i < timezoneArray.length; i++) {
let tzId = timezoneArray[i].getID(); // America/Sao_Paulo
}
```
双时钟应用
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  选择时区列表中的时区放入应用偏好时区列表中。
```typescript
let timezone1 = i18n.getTimeZone("America/Sao_Paulo");
let timezone2 = i18n.getTimeZone();
let appPreferredTimeZoneList: Array<i18n.TimeZone> = [] // 应用偏好时区列表
appPreferredTimeZoneList.push(timezone1);
appPreferredTimeZoneList.push(timezone2);
```
3.  遍历应用偏好时区列表，获取各时区时间。
```typescript
let locale = i18n.System.getSystemLocale();
for (let i = 0 ; i < appPreferredTimeZoneList.length ; i++) {
let timezone = appPreferredTimeZoneList[i].getID();
let calendar = i18n.getCalendar(locale);
calendar.setTimeZone(timezone); //设置日历对象的时区
//获取年月日时分秒
let year = calendar.get("year");
let month = calendar.get("month");
let day = calendar.get("date");
let hour = calendar.get("hour");
let minute = calendar.get("minute");
let second = calendar.get("second");
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-dst-transition-V14
爬取时间: 2025-04-28 00:51:06
来源: Huawei Developer
功能介绍
夏令时是一种为节约能源而人为规定地方时间的制度，即在天亮早的夏季人为将时间调快一小时，可以使人们早起早睡，减少照明时间，从而节约照明用电。
实现原理
系统会配置夏令时跳变规则，当本地时间到达跳变点时，会自动实现跳变。若应用通过一般的ts接口（例如 Date()）获取和显示时间，则到夏令时跳变时间点时，应用会同步显示夏令时时间。
夏令时跳变规则如下：
1.  计算一天的小时数。 一整天的小时数在夏令时跳变的当天会发生变化，并非24小时。夏令时开始的当天，一整天时间为23小时；夏令时结束的当天，一整天时间为25小时。 计算夏令时跳变前后同一个挂钟时间之间相差的小时数，示例代码如下：
```typescript
import { i18n } from '@kit.LocalizationKit';
let calendar = i18n.getCalendar("zh-Hans");
calendar.setTimeZone("Europe/London");
calendar.set(2021, 2, 27, 16, 0, 0); //The day before daylight saving time start
let time1 = calendar.getTimeInMillis();
calendar.set(2021, 2, 28, 16, 0, 0); //The day daylight saving time start
let time2 = calendar.getTimeInMillis();
let hours = (time2 - time1)/(3600*1000) //The hours between the same wall clock time before and after DST. Should be 23
```
2.  存储和显示数据。 按当地夏令时计时规则，存储和显示数据，需要处理夏令时跳变带来额时间空缺和重复。 夏令时跳入将导致1小时空缺，例如1:59:59→3:00:00；夏令时跳出将导致1小时重复，例如3:59:59→3:00:00。 夏令时内的本地时间显示，建议加上夏令时标识。
3.  存储和传输时间数据。 建议使用0时区标准时间（UTC或者GMT）进行时间数据的存储和传输，避免夏令时跳变带来的信息丢失或异常。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170422.25223808235434421570785203175992:50001231000000:2800:D952327332FC91574B90836255B4DB5D562B1D312785545AF917DF68FC778F51.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-sorting-V14
爬取时间: 2025-04-28 00:51:19
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-sorting-overview-V14
爬取时间: 2025-04-28 00:51:33
来源: Huawei Developer
世界各地的语言、文化不同，对相同的字符可能有不同的排序规则。为了满足用户的文化习惯，需对不同国家、地区、使用不同语言的用户提供不同的排序规则，输出具有语义特性的排序结果，而不是单纯按照字母编码码点的大小来排序，方便用户查找，在语言列表、国家/地区列表、联系人列表等多种不用场景下使用。
多语言排序分为按本地习惯排序和创建索引两种方式，具体使用场景和开发步骤请参考以下章节。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-sorting-local-V14
爬取时间: 2025-04-28 00:51:46
来源: Huawei Developer
使用场景
在用户使用到排序的场景下，提供符合用户使用习惯的排序方法展示内容。例如，设置中“系统和语言”的语言列表，列表需要按照当地用户习惯进行排序。
开发步骤
多语言列表按照本地习惯进行排序，通过Collator类的compare接口实现，具体开发步骤如下。
1.  导入模块。
```typescript
import { intl } from '@kit.LocalizationKit';
```
2.  创建collator排序对象。 构造函数支持通过CollatorOptions设置不同的排序格式，具体请参考表1。
```typescript
let collator = new intl.Collator(locale: string | Array<string>, options?: CollatorOptions);
```
3.  比较字符串。
```typescript
let compareResult = collator.compare(first: string, second: string);
// compareResult 为负数，表示第一个参数排在第二个参数之前
// compareResult 为0，表示第一个参数与第二个参数排序不分先后
// compareResult 为正数，表示第一个参数排在第二个参数之后
```
排序格式选项
表1CollatorOptions各参数取值和显示效果
| 名称 | 取值 | 描述 | 显示效果 |
| --- | --- | --- | --- |
| localeMatcher | lookup | 模糊匹配 |  |
|  | best fit | 准确匹配 |  |
| usage | sort | 用作排序 |  |
|  | search | 用作查找匹配的字符串 |  |
| sensitivity | base | 不同的字母比较不相等 | 例如: a ≠ b, a = á, a = A. |
|  | accent | 不同的字母或读音比较不相等 | 例如: a ≠ b, a ≠ á, a = A. |
|  | case | 不同的字母或同一字母大小写比较不相等 | 例如: a ≠ b, a = á, a ≠ A. |
|  | variant | 不同的字母或读音及其它有区别的标志或大小写都是不相等的 | 例如: a ≠ b, a ≠ á, a ≠ A. |
| ignorePunctuation | true | 忽略标点 | a,b = ab |
|  | false | 不忽略标点 | a,b < ab |
| numeric | true | 使用数字排序 | 1 < 2 < 10 < 11 |
|  | false | 不使用数字排序 | 1 < 10 < 11 < 2 |
| caseFirst | upper | 大写排前面 | ab,aB, AB,Ab => AB < Ab < aB < ab |
|  | lower | 小写排前面 | ab,aB, AB,Ab => ab < aB < Ab < AB |
|  | false | 不区分首字母大小写 | ab,aB, AB,Ab => ab < aB < Ab < AB |
| collation | big5han | 拉丁字母使用的拼音排序 |  |
|  | compat | 兼容性排序，仅用于阿拉伯语 |  |
|  | dict | 词典风格排序，仅用于僧伽罗语 |  |
|  | direct | 二进制码点排序 |  |
|  | ducet | Unicode排序规则元素表 |  |
|  | eor | 欧洲排序规则 |  |
|  | gb2312 | 拼音排序，仅用于中文排序 |  |
|  | phonebk | 电话本风格排序 |  |
|  | phonetic | 发音排序 |  |
|  | pinyin | 拼音排序 |  |
|  | reformed | 瑞典语排序 |  |
|  | searchjl | 韩语初始辅音搜索的特殊排序 |  |
|  | stroke | 汉语的笔画排序 |  |
|  | trad | 传统风格排序，如西班牙语 |  |
|  | unihan | 统一汉字排序，用于日语、韩语、中文等汉字排序 |  |
|  | zhuyin | 注音排序，仅用于中文排序 |  |
开发实例
```typescript
// 导入模块
import { intl } from '@kit.LocalizationKit';
// 创建排序对象
let options: intl.CollatorOptions = {
localeMatcher: "lookup",
usage: "sort",
sensitivity: "case" // 区分大小写
};
let collator = new intl.Collator("zh-CN", options);
// 区分大小写排序
let array = ["app", "App", "Apple", "ANIMAL", "animal", "apple", "APPLE"];
array.sort((a, b) => {
return collator.compare(a, b);
})
console.log("result: ", array);  // animal ANIMAL app App apple Apple APPLE
// 中文拼音排序
array = ["苹果", "梨", "香蕉", "石榴", "甘蔗", "葡萄", "橘子"];
array.sort((a, b) => {
return collator.compare(a, b);
})
console.log("result: ", array);  // 甘蔗,橘子,梨,苹果,葡萄,石榴,香蕉
// 按笔画排序
options = {
localeMatcher: "lookup",
usage: "sort",
collation: "stroke"
};
collator = new intl.Collator("zh-CN", options);
array = ["苹果", "梨", "香蕉", "石榴", "甘蔗", "葡萄", "橘子"];
array.sort((a, b) => {
return collator.compare(a, b);
})
console.log("result: ", array);  // 甘蔗,石榴,苹果,香蕉,梨,葡萄,橘子
// 搜索匹配的字符串
options = {
usage: "search",
sensitivity: "base"
};
collator = new intl.Collator("tr", options);
let sourceArray = ['Türkiye', 'TüRkiye', 'salt', 'bright'];
let s = 'türkiye';
let matches = sourceArray.filter(item => collator.compare(item, s) === 0);
console.log(matches.toString());  // Türkiye,TüRkiye
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-sorting-index-V14
爬取时间: 2025-04-28 00:51:59
来源: Huawei Developer
使用场景
当列表选项过多时，需要用户滑动窗口查找目标选项，为了快速找到目标选项，可以使用创建索引的方法。创建索引方式实质是打标签，例如，在联系人页面右侧通常会有“ABCD”的英文标记与联系人姓名首字母对应，若需寻找王同学，点击“W”可直接跳转到目标项范围。诸如“ABCD”的英文标记称为索引，通过创建索引的方式快速让窗口滑动到相应范围，找到目标选项。
开发步骤
接口具体使用方法和说明请参考IndexUtil的API接口文档。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  创建对象。
```typescript
let indexUtil = i18n.getInstance(locale?:string);  // locale 表示本地化标识符，默认值是系统当前locale
```
3.  以获取索引列表为例。
```typescript
let indexList = indexUtil.getIndexList();
```
开发实例
```typescript
// 导入模块
import { i18n } from '@kit.LocalizationKit';
// 创建索引
let indexUtil = i18n.getInstance("zh-CN");
let indexList = indexUtil.getIndexList(); // ["...", "A", "B", "C", "D", "E" ... "X", "Y", "Z", "..."]
// 多语言index混排
indexUtil.addLocale("ru-RU");
indexList = indexUtil.getIndexList(); // …,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,…,А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ы,Э,Ю,Я,…
indexUtil.getIndex("你好"); // N
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-character-processing-V14
爬取时间: 2025-04-28 00:52:12
来源: Huawei Developer
使用场景
不同语言中字符规则差异较大，通常很难从对应文本中提取需要的信息。通过字符处理，可以在不同语言规则下，以相似的逻辑处理文本。
开发步骤
字符属性
字符属性用于判断字符类别，如判断字符是否为数字、字母、空格，是否为从右到左语言的字符，是否为表意文字(主要是中文日文韩文)等。
该功能通过Unicode类的isDigit等接口实现，具体开发步骤如下。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  判断字符属性。
```typescript
let isDigit: boolean = i18n.Unicode.isDigit(char: string);
```
3.  以一般类别值为例，判断字符类类型，具体请参考getType接口文档。
```typescript
let type = i18n.Unicode.getType(char: string);
```
开发实例
```typescript
// 导入模块
import { i18n } from '@kit.LocalizationKit';
// 判断字符是否是数字
let isDigit = i18n.Unicode.isDigit('1'); // isDigit: true
// 判断字符是否是从右到左语言的字符
let isRTL = i18n.Unicode.isRTL('a'); // isRTL: false
// 判断字符是否是表意文字
let isIdeograph = i18n.Unicode.isIdeograph('华'); // isIdeograph: true
// 获取字符的一般类别值
let type = i18n.Unicode.getType('a'); // type: U_LOWERCASE_LETTER
```
音译
音译是指以当地语言发音相近的内容替换原本的内容。通过Transliterator类的transform接口实现，具体开发步骤如下。
本模块支持中文汉字转为拼音，但对于多音字无法根据上下文语义有效处理。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  创建Transliterator对象，获取音译列表。
```typescript
let transliterator: i18n.Transliterator = i18n.Transliterator.getInstance(id: string);  // 传入音译支持的ID，创建Transliterator对象
let ids: string[] = i18n.Transliterator.getAvailableIDs();  // 获取音译支持的ID列表
```
3.  音译文本。
```typescript
let res: string = transliterator.transform(text: string);  // 对text内容进行音译
```
开发实例
```typescript
// 导入模块
import { i18n } from '@kit.LocalizationKit';
// 音译成Latn格式
let transliterator = i18n.Transliterator.getInstance('Any-Latn');
let wordArray = ["中国", "德国", "美国", "法国"]
for (let i = 0; i < wordArray.length; i++) {
let res = transliterator.transform(wordArray[i]); // res: zhōng guó, dé guó, měi guó, fǎ guó
}
// 汉语音译去声调
let transliter = i18n.Transliterator.getInstance('Any-Latn;Latin-Ascii');
let result = transliter.transform('中国'); // result: zhong guo
// 汉语姓氏读音
let nameTransliter = i18n.Transliterator.getInstance('Han-Latin/Names');
let result1 = nameTransliter.transform('单老师'); // result1: shàn lǎo shī
let result2 = nameTransliter.transform('长孙无忌'); // result2: zhǎng sūn wú jì
// 获取音译支持的ID列表
let ids = i18n.Transliterator.getAvailableIDs(); // ids: ['ASCII-Latin', 'Accents-Any', ...]
```
字符标准化
字符标准化是指按指定的范式标准化字符。通过Normalizer类的normalize接口实现，具体开发步骤如下。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  创建标准化对象。传入文本标准化的范式，创建标准化对象，文本标准化的范式包括NFC、NFD、NFKC和NFKD，范式的详细介绍请参考国际标准。
```typescript
let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(mode: NormalizerMode);
```
3.  文本标准化。
```typescript
let normalizedText: string = normalizer.normalize(text: string); // 对text文本进行标准化
```
开发实例
```typescript
// 导入模块
import { i18n } from '@kit.LocalizationKit';
// 以NFC范式标准化字符
let normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
let normalizedText = normalizer.normalize('\u1E9B\u0323'); // normalizedText: \u1E9B\u0323
```
断词换行
断词换行是指根据设定的区域参数获取文本中的分割点，通过BreakIterator类的接口实现，具体开发步骤如下。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  创建用于断句的对象。 传入合法的locale参数，生成BreakIterator类型的对象，该对象将按照locale所指定的区域的规则进行断句。
```typescript
let iterator: i18n.BreakIterator = i18n.getLineInstance(locale: string);
```
3.  设置要处理的文本。
```typescript
iterator.setLineBreakText(text: string); // 设置要处理的文本
let breakText: string = iterator.getLineBreakText(); // 查看iterator正在处理的文本
```
4.  获取可断句的位置。
```typescript
let currentPos: number = iterator.current(); // 获取iterator在当前所处理文本中的位置
let firstPos: number = iterator.first(); // 设置为第一个可断句的分割点，返回该分割点的位置。第一个分割点总是在文本的起始位置，firstPos = 0
let nextPos: number = iterator.next(number); // 将iterator移动number数量个分割点，number为正数代表向后移动，number为负数代表向前移动，默认值为1。nextPos为移动后在文本中的位置，如果超出文本的长度范围，返回-1
let isBoundary: boolean = iterator.isBoundary(number); // 判断number位置是否是分割点
```
开发实例
```typescript
// 导入模块
import { i18n } from '@kit.LocalizationKit';
// 断句对象
let iterator = i18n.getLineInstance('en-GB');
// 断句文本
iterator.setLineBreakText('Apple is my favorite fruit.');
// 将BreakIterator对象移动到文本起始位置
let firstPos = iterator.first(); // firstPos: 0
// 将BreakIterator对象移动几个分割点
let nextPos = iterator.next(2); // nextPos: 9
// 判断某个位置是否是分割点
let isBoundary = iterator.isBoundary(9); // isBoundary: true
// 获取BreakIterator对象处理的文本
let breakText = iterator.getLineBreakText(); // breakText: Apple is my favorite fruit.
```
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-name-localization-V14
爬取时间: 2025-04-28 00:52:26
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-language-region-display-V14
爬取时间: 2025-04-28 00:52:39
来源: Huawei Developer
使用场景
本地化语言与地区名称是指界面的语言列表和地区列表按照本地的语言习惯显示，确保用户可识别，主要在展示语言与地区名称的场景下使用。例如，在简体中文环境下，简体中文用“简体中文”表示，英文用“英文”表示；在英文环境下，简体中文用“Simplified Chinese”表示，英文用“English”表示。
开发步骤
接口具体说明请参考getDisplayCountry和getDisplayLanguage的API文档。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  本地化语言名称。 在给用户提供语言名称的场景中，例如切换系统语言时，系统展示用户可读的本地化语言名称，以中文形式显示德语为例。
```typescript
let displayLanguage = i18n.System.getDisplayLanguage("de", "zh-Hans-CN"); // 德文
// language: 语言两字母代码，如"zh"，"de"，"fr"等
// locale: 本地化标识符，如"en-GB"、"en-US"、"zh-Hans-CN"等
// sentenceCase: 返回的语言名称是否需要首字母大写，默认值：true
```
3.  本地化国家/地区名称。 在给用户提供国家/地区名称时，getDisplayCountry()返回本地化的国家/地区名称。
```typescript
let displayCountry = i18n.System.getDisplayCountry("SA", "en-GB"); // Saudi Arabia
// country: 国家/地区两字母代码，如"CN"、"DE"、"SA"等
// locale: 本地化标识符，如"en-GB"、"en-US"、"zh-Hans-CN"等
// sentenceCase: 返回的国家/地区名称是否需要首字母大写，默认值：true
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i18n-time-zone-display-V14
爬取时间: 2025-04-28 00:52:53
来源: Huawei Developer
使用场景
多语言环境下，不同地区用户对时区的称呼可能存在差异，例如在中文环境下，中部时区称为中部时区，在英文环境下，中部时区称为Central Time Zone。为了确保时区展示当地人语言使用习惯，需要本地化时区名称。
开发步骤
接口具体使用方法和说明请参考getDisplayName的API接口文档。
1.  导入模块。
```typescript
import { i18n } from '@kit.LocalizationKit';
```
2.  本地化时区名称，以美洲/圣保罗为例。
```typescript
let timezone = i18n.getTimeZone("America/Sao_Paulo");
let timeZoneName = timezone.getDisplayName("zh-Hans", true); // 巴西利亚标准时间
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i10n-V14
爬取时间: 2025-04-28 00:53:06
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/l10n-multilingual-resources-V14
爬取时间: 2025-04-28 00:53:19
来源: Huawei Developer
功能介绍
当应用需要提供给多个地区的用户使用时，为了满足不同地区用户在语言、文化方面的需求，需要将应用进行本地化定制，使应用加载和显示符合所在地域使用习惯的内容。界面加载的内容包括文本字符、图片、音频、视频等，这些内容均称为资源。为确保应用可以加载到不同国家和地区、不同语言等类型的内容，需要创建多个不同的资源目录，放置多种资源，当用户运行应用时，根据所在的语言区域自动选择并加载与设备最匹配的资源。为更好实现应用本地化，推荐作法是将本地化的内容与核心功能尽可能分开，本地化内容放置在资源目录下。
本部分简单介绍资源文件配置方法和资源匹配规则。对于应用开发者，仅需关注资源配置，资源文件配置完成后，根据业务需求对资源进行访问，访问方式具体请参考资源访问。
资源文件配置
1.  确定本地化的目标区域，具体请参考区域标识。 针对目标区域准备本地化资源，将需要本地化的资源（包括字符串、媒体资源、文件、图片、音频等）翻译成目标区域的资源。这一步骤占据了本地化过程的大部分工作量。
2.  创建资源目录。 资源目录包括默认（base）目录和限定词目录。默认目录是创建工程时默认生成的目录，可用于存放字符串、颜色、动画、布局等内容；限定词目录由开发者创建，可根据语言、文字等自行定义，同样可存放目标区域的字符串、图片、音频等资源，自定义目录如resources/en_GB-vertical-car-mdpi。
3.  创建资源组目录。根据需要放置的资源类型，创建相应的资源组目录，如若存放媒体资源需创建media目录，目录结构为resources/en_GB-vertical-car-mdpi/media。
4.  创建资源文件。将字串、图片、音频等资源放入相应的.json资源文件中。 应用本地化的推荐作法是将本地化的内容与核心功能尽可能分开，本地化内容放置在资源目录下。 创建资源目录、资源组目录和资源文件的具体操作请参考资源分类与访问。
5.  应用本地化的推荐作法是将本地化的内容与核心功能尽可能分开，本地化内容放置在资源目录下。
6.  创建资源目录、资源组目录和资源文件的具体操作请参考资源分类与访问。
-  应用本地化的推荐作法是将本地化的内容与核心功能尽可能分开，本地化内容放置在资源目录下。
-  创建资源目录、资源组目录和资源文件的具体操作请参考资源分类与访问。
资源匹配规则
匹配原则为：将应用偏好语言列表与应用资源进行匹配，使应用显示与偏好语言最匹配的资源。例如，应用需要显示一个字串的操作如下。
1.  使用系统语言与应用配置的资源限定词目录进行匹配，找出相关的限定词目录。
2.  依据相关程度高低，对限定词目录进行排序，依次在限定词目录中搜索目标字串资源，使用最先搜索到的限定词目录下的目标字串资源进行显示。
3.  若未找到与偏好语言匹配的字串，使用应用偏好语言列表中的第二个语言按照前述步骤进行搜索。
4.  若依据应用偏好语言列表和系统语言列表，均未获取到匹配的资源，应用界面则加载应用默认资源目录下内容进行显示。因此，每个应用在资源目录下的默认目录均需填充资源，避免编译错误，应用界面加载资源失败。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i10n-translation-V14
爬取时间: 2025-04-28 00:53:32
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/l10n-hard-coding-concatenate-V14
爬取时间: 2025-04-28 00:53:46
来源: Huawei Developer
使用场景
本地化的关键操作是资源文件的翻译，为提升翻译可行性在开发过程中应避免硬编码与拼接。
不同于从外部获取数据或在运行时生成数据，硬编码是指将数据、参数、常量等直接嵌入到程序中，实现特定功能。在界面中显示的文字，包括图片中的文字、音频、字幕等，不能采用硬编码，避免难以本地化或增加本地化的工作量。同时，界面上一句完整文本，不应由多个片段直接前后拼接而成。直接拼接的文本，可能导致翻译时无法获取句子完整信息而导致翻译错误或语义表达顺序问题。例如，下图中将“Rain tomorrow”和“Bring an umbrella”两句直接拼接在一起，造成语句大小写问题。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170423.84932778710995357238439064551548:50001231000000:2800:87CB5013DCBE0AAEABFBB5B540CA49CCAE19A5AAFE3B135473DAEFFDB46186EB.png)
约束与限制
1.  避免使用硬编码，将需要翻译的字符串提取到资源文件中，与代码分离，然后使用相关的接口加载，具体请参考提供多语言资源。
2.  避免字符串直接拼接，若语句存在变化部分（如“打开华为视频”和“打开华为浏览器”，变化部分是“视频”和“浏览器”），对应变量应使用占位标识，呈现完整的语句表达。 资源占位符示例：
```typescript
{
"name": "string1",
"value": "打开%s应用"
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/l10n-translation-scene-V14
爬取时间: 2025-04-28 00:53:59
来源: Huawei Developer
同样的内容在不同场景和语境中，翻译结果可能存在差异。提供待翻译的界面字串时，应提供给译员完整的场景和足够的场景信息，避免造成翻译偏差。翻译场景信息通常包括如下两种类型：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/l10n-singular-plural-V14
爬取时间: 2025-04-28 00:54:12
来源: Huawei Developer
翻译过程中，不同语言，对于名词或单位表达式的单复数格式要求有所不用，有些语言不区分单复数，有些语言有两种形式，有些语言有多种形式。例如，在英语中，名词支持单复数两种形式；在中文，名词不分单复数，通过量词表达数量的不同。
国际上常通过如下类别区分单复数：
-  zero ：0或者0结尾
-  one：单数或者1结尾
-  two：2结尾
-  few：数值较小的数
-  many：数值较大的数
-  other：其他情况
举例，在阿拉伯语中，单复规则如下：
-  zero ：0
-  one：1
-  two：2
-  few：3 ~ 10、103 ~ 110，1003...
-  many：11 ~ 26、111，1011...
-  other：100 ~ 102、200 ~ 202、1000、10000...
开发步骤
接口具体使用方法请参考getPluralStringValueSync的API接口文档。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/i10n-testing-V14
爬取时间: 2025-04-28 00:54:25
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pseudo-i18n-testing-V14
爬取时间: 2025-04-28 00:54:40
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pseudo-i18n-testing-overview-V14
爬取时间: 2025-04-28 00:54:53
来源: Huawei Developer
伪本地化（pseudo-localization）又称伪翻译，是在正式的本地化之前，通过模拟本地化过程帮助发现本地化的潜在问题，避免功能缺陷。它是软件测试中用来测试软件是否符合本地化与国际化的方法之一。伪翻译不是在本地化过程中将软件的文本翻译成外语，而是在源语言软件的基础上，按照一定的规则，将需要本地化的文本使用本地化文字进行替换，模拟本地化过程。
对于新开发的软件，或者界面变更较大的软件，若等待翻译完成后再进行界面测试，可能会延误整个交付周期。同时，软件开发初期，界面可能会随时调整，通常不会进行界面文字翻译，而等产品成熟后，再开始界面翻译和翻译测试，可能会延误产品发布。所以，通过采用伪本地化测试的方法可以避免延误开发进程，确保产品正常发布。
伪本地化测试包括翻译伪本地化和界面镜像伪本地化。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pseudo-i18n-testing-translation-V14
爬取时间: 2025-04-28 00:55:07
来源: Huawei Developer
使用场景
翻译伪本地化测试主要是模拟在翻译应用时可导致出现界面、布局或者文字显示异常等问题。
出现文字截断或界面显示问题的主要原因是：对于软件的菜单、文字区域、按键、复选框等，设计者在做界面设计时通常先调整出适于源语言文字长度的大小（通常为英文），并进一步调整界面的对齐、位置、行距等。然而，一些源语言被翻译后，长度往往会增加，使得UI布局出现异常，或者导致文本在不合适的位置截断。例如俄文或是挪威文通常比英文长，而原始UI界面预留的空间过小，导致超出界面的文字被裁剪，最终无法正常显示完整的翻译后的文字。
文字或符号无法正常显示的可能原因是：某一语言的文字或符号因系统缺失字体或者排版整形能力，从而导致无法正常显示；开发过程中假设用户不会输入一些特殊字符或是特定语言的文字，导致用户在实际使用软件时发生问题。例如中文界面的应用，可能输入维吾尔语的相关信息后无法显示。
测试流程
1.  切换到伪本地化测试区域，如“en-XA”。 通过代码切换的方法（需要系统应用权限）：
```typescript
import { i18n } from '@kit.LocalizationKit';
i18n.System.setSystemLanguage('en-XA')
```
2.  遍历需要测试的APP。
测试事项
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170423.95434610088745668003646869618862:50001231000000:2800:DDAE9341E187FA1AF64B4FCA5896B0E672C373CDFE83608760FE20A6FE7D1012.png)
1.  检查是否有界面截断、变形、布局异常等问题。其中，界面截断可通过观察界面字符串是否以“]”正确结尾，看不到“]”说明界面字符串未完整显示。
2.  检查是否有硬编码问题。如果界面需要翻译的文字未处理为伪翻译格式，说明代码中存在对界面文字的硬编码。
3.  检查是否存在字串拼接。如果存在连续的伪翻译格式字串出现在同一个控件里，例如"[字串1][字串2]"，说明存在字串拼接。
4.  检查多语言文字显示是否异常。如果伪翻译文字未能正常显示，出现类似方块、空缺等现象，或者文字显示不完整，存在部分被截断的情况，说明多语言显示存在异常。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/pseudo-i18n-testing-mirror-V14
爬取时间: 2025-04-28 00:55:20
来源: Huawei Developer
使用场景
界面镜像测试主要检查文字阅读顺序是否出现问题。有一些语言的阅读顺序不是从左到右。例如，在阿拉伯语中，界面的阅读顺序是从右到左（RTL）。
测试流程
1.  切换到伪本地化测试区域，如“ar-XB”。 通过代码切换的方法（需要系统应用权限）：
```typescript
import { i18n } from '@kit.LocalizationKit';
i18n.System.setSystemLanguage('ar-XB')
```
2.  遍历需要测试的APP。
测试事项
1.  检查界面布局、文字方向、界面控制逻辑是否符合从右至左的阅读习惯。详细要点见界面镜像章节。
2.  检查相关功能是否存在异常无法使用。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/linguistic-testing-V14
爬取时间: 2025-04-28 00:55:33
来源: Huawei Developer
语言测试是指国际化和本地化完成后，在产品正式发布和上市前，需要本地用户专家对应用进行巡检，查看界面显示等是否符合当地应用习惯。
在多语言环境下，APP应用本地化的质量对于产品是否被接纳至关重要，界面内容的专业度、译文的一致性、用词风格、界面显示等都会影响使用体验，任何细微的错误都可能造成用户流失的风险。因此，在APP应用全球化发布前，通过语言测试识别并修复潜在问题，能够有效提升全球终端用户的使用体验。同时，需要关注敏感禁忌，任何地缘政治相关的敏感词/禁用词/慎用词都有可能给企业带来重大业务影响，拥有一道完善的敏感词解决方案，可以确保产品出海安全。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ui-design-kit-guide-V14
爬取时间: 2025-04-28 00:55:47
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ui-design-introduction-V14
爬取时间: 2025-04-28 00:56:00
来源: Huawei Developer
UI Design Kit（UI设计套件）是华为提供的符合华为HarmonyOS Design System定义的UI界面开发套件集合，包含HarmonyOS Design System设计定义的扩展UI组件及其多样化的组件样式、丰富多样的UI界面场景下的光影效果，支撑应用实现跟随HarmonyOS Design System高端精致设计效果UI界面，达成应用界面与华为HarmonyOS多设备UI设计风格完美融合（参见HarmonyOS设计理念）。
功能范围：
提供HarmonyOS设计风格控件能力，遵循HarmonyOS设计规范。
满足HarmonyOS人机交互设计，达成全场景人机交互体验一致，遵循HarmonyOS设计规范。
提供HarmonyOS视觉风格匹配的开发能力，遵循HarmonyOS设计规范。
场景介绍
UI Design Kit提供了应用图标处理能力，帮助开发者实现UX体验标准的应用图标，支持在线主题图标默认跟随主题换肤，支持应用列表、应用详情页等图标展示场景，具体如下：
基础概念
在开发前，需要先了解以下基础概念：
约束与限制
| 接口  | 约束  |
| --- | --- |
| 图标批量处理接口  | 最大支持设置10个并发数。最大支持一次性处理500个图标。  |
接口
约束
图标批量处理接口

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ui-design-icon-process-V14
爬取时间: 2025-04-28 00:56:13
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ui-design-layered-process-V14
爬取时间: 2025-04-28 00:57:08
来源: Huawei Developer
场景介绍
适用于图标为分层资源，且图标展示风格要与华为HarmonyOS Design System设计风格一致的应用场景。以下是一些典型的应用场景：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170423.72282826478500812905114153042055:50001231000000:2800:31F5D57405691AF7624F7C5E9C1FE71FD868F91F77F8EDC1B74624435352B16D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170423.63328693233516666396908487108608:50001231000000:2800:685E26CD923F2B63DC8CD3577329D6D5948316A586BE7F41EE5333DB81EDB112.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170424.07118835833156889215453843138813:50001231000000:2800:B3E8DB824522FC1A0325D35F91F01F1BA92504F33FBE4B2B1656E0C3AFC3A93B.png)
开发步骤
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170424.64065560088017726081349757597602:50001231000000:2800:C8AD065ECE17DE071149A85F80DC2C4E16C9108FCB34A4FA28574C9D7D5DD946.png)
1.  将前景资源和背景资源，放到entry\src\main\resources\base\media下，在该目录创建一个json文件（例如：drawable.json），内容为
```typescript
{
"layered-image":
{
"background" : "$media:background",
"foreground" : "$media:foreground"
}
}
```
2.
```typescript
import { LayeredDrawableDescriptor } from '@kit.ArkUI';
import { hdsDrawable } from '@kit.UIDesignKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
```
1.
```typescript
@Entry
@Component
struct Index{
bundleName: string = 'com.example.uidesignkit';
resManager: resourceManager.ResourceManager | undefined = undefined;
layeredDrawableDescriptor: LayeredDrawableDescriptor | undefined = undefined;
@State layeredIconsResult: Array<hdsDrawable.ProcessedIcon> = [];
build() {
Column() {
Column() {
Text('getHdsLayeredIcon')
.fontWeight(FontWeight.Bold)
.fontSize(16)
.margin(5)
Image(this.getHdsLayeredIcon())
.width(48)
.height(48)
}
.margin(20)
Text('getHdsLayeredIcons')
.fontWeight(FontWeight.Bold)
.fontSize(16)
.margin(5)
List() {
ForEach(this.layeredIconsResult,
(item: hdsDrawable.ProcessedIcon, index?: number) => {
ListItem() {
Column() {
Text(item.bundleName)
.fontWeight(FontWeight.Medium)
.fontSize(16)
.margin(5)
Image(item.pixelMap)
.width(48)
.height(48)
}
.margin(15)
}
.width('100%')
}, (item: string) => item.toString())
}
.scrollBar(BarState.On)
.height('60%')
}
.height('100%')
.width('100%')
}
aboutToAppear(): void {
this.resManager = getContext().resourceManager;
if (!this.resManager) {
return;
}
this.layeredDrawableDescriptor = (this.resManager.getDrawableDescriptor($r('app.media.drawable')
.id)) as LayeredDrawableDescriptor;
this.getHdsLayeredIcons();
}
private getHdsLayeredIcon(): image.PixelMap | null {
try {
return hdsDrawable.getHdsLayeredIcon(this.bundleName, this.layeredDrawableDescriptor, 48, true);
} catch (err) {
let message = (err as BusinessError).message;
let code = (err as BusinessError).code;
console.error(`getHdsLayeredIcon failed, code: ${code}, message: ${message}`);
return null;
}
}
private getHdsLayeredIcons(): void {
if (!this.layeredDrawableDescriptor) {
console.error(`getHdsLayeredIcons layeredDrawableDescriptor is undefined.`);
return;
}
let options: hdsDrawable.Options = {
size: 48,
hasBorder: true,
parallelNumber: 4
};
let layeredIcons: Array<hdsDrawable.LayeredIcon> = [];
for (let i = 0; i < 10; i++) {
layeredIcons.push({
bundleName: `${this.bundleName}-${i}`,
layeredDrawableDescriptor: this.layeredDrawableDescriptor
});
}
try {
hdsDrawable.getHdsLayeredIcons(layeredIcons, options)
.then((data: Array<hdsDrawable.ProcessedIcon>) => {
console.info(`getHdsLayeredIcons data size: ${data.length}`);
this.layeredIconsResult = data;
})
.catch((err: BusinessError) => {
console.error(`getHdsLayeredIcons return error, code: ${err.code}, msg: ${err.message}`);
});
} catch (err) {
let message = (err as BusinessError).message;
let code = (err as BusinessError).code;
console.error(`getHdsLayeredIcons failed, code: ${code}, message: ${message}`);
}
}
}
```
开发实例
```typescript
import { LayeredDrawableDescriptor } from '@kit.ArkUI';
import { hdsDrawable } from '@kit.UIDesignKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
@Entry
@Component
struct Index{
bundleName: string = 'com.example.uidesignkit';
resManager: resourceManager.ResourceManager | undefined = undefined;
layeredDrawableDescriptor: LayeredDrawableDescriptor | undefined = undefined;
@State layeredIconsResult: Array<hdsDrawable.ProcessedIcon> = [];
build() {
Column() {
Column() {
Text('getHdsLayeredIcon')
.fontWeight(FontWeight.Bold)
.fontSize(16)
.margin(5)
Image(this.getHdsLayeredIcon())
.width(48)
.height(48)
}
.margin(20)
Text('getHdsLayeredIcons')
.fontWeight(FontWeight.Bold)
.fontSize(16)
.margin(5)
List() {
ForEach(this.layeredIconsResult,
(item: hdsDrawable.ProcessedIcon, index?: number) => {
ListItem() {
Column() {
Text(item.bundleName)
.fontWeight(FontWeight.Medium)
.fontSize(16)
.margin(5)
Image(item.pixelMap)
.width(48)
.height(48)
}
.margin(15)
}
.width('100%')
}, (item: string) => item.toString())
}
.scrollBar(BarState.On)
.height('60%')
}
.height('100%')
.width('100%')
}
aboutToAppear(): void {
this.resManager = getContext().resourceManager;
if (!this.resManager) {
return;
}
this.layeredDrawableDescriptor = (this.resManager.getDrawableDescriptor($r('app.media.drawable')
.id)) as LayeredDrawableDescriptor;
this.getHdsLayeredIcons();
}
private getHdsLayeredIcon(): image.PixelMap | null {
try {
return hdsDrawable.getHdsLayeredIcon(this.bundleName, this.layeredDrawableDescriptor, 48, true);
} catch (err) {
let message = (err as BusinessError).message;
let code = (err as BusinessError).code;
console.error(`getHdsLayeredIcon failed, code: ${code}, message: ${message}`);
return null;
}
}
private getHdsLayeredIcons(): void {
if (!this.layeredDrawableDescriptor) {
console.error(`getHdsLayeredIcons layeredDrawableDescriptor is undefined.`);
return;
}
let options: hdsDrawable.Options = {
size: 48,
hasBorder: true,
parallelNumber: 4
};
let layeredIcons: Array<hdsDrawable.LayeredIcon> = [];
for (let i = 0; i < 10; i++) {
layeredIcons.push({
bundleName: `${this.bundleName}-${i}`,
layeredDrawableDescriptor: this.layeredDrawableDescriptor
});
}
try {
hdsDrawable.getHdsLayeredIcons(layeredIcons, options)
.then((data: Array<hdsDrawable.ProcessedIcon>) => {
console.info(`getHdsLayeredIcons data size: ${data.length}`);
this.layeredIconsResult = data;
})
.catch((err: BusinessError) => {
console.error(`getHdsLayeredIcons return error, code: ${err.code}, msg: ${err.message}`);
});
} catch (err) {
let message = (err as BusinessError).message;
let code = (err as BusinessError).code;
console.error(`getHdsLayeredIcons failed, code: ${code}, message: ${message}`);
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ui-design-normal-process-V14
爬取时间: 2025-04-28 00:57:21
来源: Huawei Developer
场景介绍
适用于图标为单层资源，且图标展示风格要与华为HarmonyOS Design System设计风格一致的应用场景，典型应用场景可参考分层图标场景介绍。
开发步骤
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170424.47739863791352864436019161014638:50001231000000:2800:CE22B6FF7569D5CA523A693E77EC3E042C591043AC697F0D0F14735E14EF35EF.png)
1.
```typescript
import { LayeredDrawableDescriptor, DrawableDescriptor } from '@kit.ArkUI';
import { hdsDrawable } from '@kit.UIDesignKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
```
1.
```typescript
@Entry
@Component
struct Index{
bundleName: string = 'com.example.uidesignkit';
resManager: resourceManager.ResourceManager | undefined = undefined;
layeredDrawableDescriptor: LayeredDrawableDescriptor | undefined = undefined;
drawableDescriptor: DrawableDescriptor | undefined = undefined;
@State iconsResult: Array<hdsDrawable.ProcessedIcon> = [];
build() {
Column() {
Column() {
Text('getHdsIcon')
.fontWeight(FontWeight.Bold)
.fontSize(16)
.margin(5)
Image(this.getHdsIcon())
.width(48)
.height(48)
}
.margin(20)
Text('getHdsIcons')
.fontWeight(FontWeight.Bold)
.fontSize(16)
.margin(5)
List() {
ForEach(this.iconsResult,
(item: hdsDrawable.ProcessedIcon, index?: number) => {
ListItem() {
Column() {
Text(item.bundleName)
.fontWeight(FontWeight.Medium)
.fontSize(16)
.margin(5)
Image(item.pixelMap)
.width(48)
.height(48)
}
.margin(15)
}
.width('100%')
}, (item: string) => item.toString())
}
.scrollBar(BarState.On)
.height('60%')
}
.height('100%')
.width('100%')
}
aboutToAppear(): void {
this.resManager = getContext().resourceManager;
if (!this.resManager) {
return;
}
this.layeredDrawableDescriptor = (this.resManager.getDrawableDescriptor($r('app.media.drawable')
.id)) as LayeredDrawableDescriptor;
this.drawableDescriptor =
(this.resManager?.getDrawableDescriptor($r('app.media.normal_icon'))) as DrawableDescriptor;
this.getHdsIcons();
}
private getHdsIcon(): image.PixelMap | null {
try {
return hdsDrawable.getHdsIcon(this.bundleName, this.drawableDescriptor?.getPixelMap(), 48,
this.layeredDrawableDescriptor?.getMask().getPixelMap(), true);
} catch (err) {
let message = (err as BusinessError).message;
let code = (err as BusinessError).code;
console.error(`getHdsIcon failed, code: ${code}, message: ${message}`);
return null;
}
}
getHdsIcons(): void {
if (!this.drawableDescriptor) {
console.error(`getHdsIcons drawableDescriptor is undefined.`);
return;
}
if (!this.layeredDrawableDescriptor) {
console.error(`getHdsIcons layeredDrawableDescriptor is undefined.`);
return;
}
let options: hdsDrawable.Options = {
size: 48,
hasBorder: true,
parallelNumber: 4
};
let icons: Array<hdsDrawable.Icon> = [];
for (let i = 0; i < 10; i++) {
icons.push({
bundleName: `${this.bundleName}-${i}`,
pixelMap: this.drawableDescriptor.getPixelMap()
})
}
try {
hdsDrawable.getHdsIcons(icons, this.layeredDrawableDescriptor.getMask().getPixelMap(), options)
.then((data: Array<hdsDrawable.ProcessedIcon>) => {
console.info(`getHdsIcons data size: ${data.length}`);
this.iconsResult = data;
})
.catch((err: BusinessError) => {
console.error(`getHdsIcons error, code: ${err.code}, msg: ${err.message}`);
});
} catch (err) {
let message = (err as BusinessError).message;
let code = (err as BusinessError).code;
console.error(`getHdsIcons callback failed: ${message}, code: ${code}`);
}
}
}
```
开发实例
```typescript
import { LayeredDrawableDescriptor, DrawableDescriptor } from '@kit.ArkUI';
import { hdsDrawable } from '@kit.UIDesignKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
@Entry
@Component
struct Index{
bundleName: string = 'com.example.uidesignkit';
resManager: resourceManager.ResourceManager | undefined = undefined;
layeredDrawableDescriptor: LayeredDrawableDescriptor | undefined = undefined;
drawableDescriptor: DrawableDescriptor | undefined = undefined;
@State iconsResult: Array<hdsDrawable.ProcessedIcon> = [];
build() {
Column() {
Column() {
Text('getHdsIcon')
.fontWeight(FontWeight.Bold)
.fontSize(16)
.margin(5)
Image(this.getHdsIcon())
.width(48)
.height(48)
}
.margin(20)
Text('getHdsIcons')
.fontWeight(FontWeight.Bold)
.fontSize(16)
.margin(5)
List() {
ForEach(this.iconsResult,
(item: hdsDrawable.ProcessedIcon, index?: number) => {
ListItem() {
Column() {
Text(item.bundleName)
.fontWeight(FontWeight.Medium)
.fontSize(16)
.margin(5)
Image(item.pixelMap)
.width(48)
.height(48)
}
.margin(15)
}
.width('100%')
}, (item: string) => item.toString())
}
.scrollBar(BarState.On)
.height('60%')
}
.height('100%')
.width('100%')
}
aboutToAppear(): void {
this.resManager = getContext().resourceManager;
if (!this.resManager) {
return;
}
this.layeredDrawableDescriptor = (this.resManager.getDrawableDescriptor($r('app.media.drawable')
.id)) as LayeredDrawableDescriptor;
this.drawableDescriptor =
(this.resManager?.getDrawableDescriptor($r('app.media.normal_icon'))) as DrawableDescriptor;
this.getHdsIcons();
}
private getHdsIcon(): image.PixelMap | null {
try {
return hdsDrawable.getHdsIcon(this.bundleName, this.drawableDescriptor?.getPixelMap(), 48,
this.layeredDrawableDescriptor?.getMask().getPixelMap(), true);
} catch (err) {
let message = (err as BusinessError).message;
let code = (err as BusinessError).code;
console.error(`getHdsIcon failed, code: ${code}, message: ${message}`);
return null;
}
}
getHdsIcons(): void {
if (!this.drawableDescriptor) {
console.error(`getHdsIcons drawableDescriptor is undefined.`);
return;
}
if (!this.layeredDrawableDescriptor) {
console.error(`getHdsIcons layeredDrawableDescriptor is undefined.`);
return;
}
let options: hdsDrawable.Options = {
size: 48,
hasBorder: true,
parallelNumber: 4
};
let icons: Array<hdsDrawable.Icon> = [];
for (let i = 0; i < 10; i++) {
icons.push({
bundleName: `${this.bundleName}-${i}`,
pixelMap: this.drawableDescriptor.getPixelMap()
})
}
try {
hdsDrawable.getHdsIcons(icons, this.layeredDrawableDescriptor.getMask().getPixelMap(), options)
.then((data: Array<hdsDrawable.ProcessedIcon>) => {
console.info(`getHdsIcons data size: ${data.length}`);
this.iconsResult = data;
})
.catch((err: BusinessError) => {
console.error(`getHdsIcons error, code: ${err.code}, msg: ${err.message}`);
});
} catch (err) {
let message = (err as BusinessError).message;
let code = (err as BusinessError).code;
console.error(`getHdsIcons callback failed: ${message}, code: ${code}`);
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ui-design-faq-V14
爬取时间: 2025-04-28 00:57:34
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ui-design-faq1-V14
爬取时间: 2025-04-28 00:57:47
来源: Huawei Developer
应用配置的图标和名称信息，可以通过resourceManager.getDrawableDescriptor获取。

