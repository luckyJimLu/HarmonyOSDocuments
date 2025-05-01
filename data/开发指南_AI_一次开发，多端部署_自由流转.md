# 合并文件
合并时间: 2025-04-30 06:10:15

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-speech-kit-guide-V14
爬取时间: 2025-04-30 04:22:16
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-speech-introduction-V14
爬取时间: 2025-04-30 04:22:29
来源: Huawei Developer
Core Speech Kit（基础语音服务）集成了语音类基础AI能力，包括文本转语音（TextToSpeech）及语音识别（SpeechRecognizer）能力，便于用户与设备进行互动，实现将实时输入的语音与文本之间相互转换。
场景介绍
约束与限制
| AI能力  | 约束  |
| --- | --- |
| 文本转语音  | 支持的语种类型：中文。（简体中文、繁体中文、中文语境下的英文）支持的音色类型：聆小珊女声音色。文本长度：不超过10000字符。  |
| 语音识别  | 支持的语种类型：中文普通话。支持的模型类型：离线。语音时长：短语音模式不超过60s，长语音模式不超过8h。  |
AI能力
约束
文本转语音
语音识别

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/texttospeech-guide-V14
爬取时间: 2025-04-30 04:22:43
来源: Huawei Developer
Core Speech Kit支持将一篇不超过10000字符的中文文本（简体中文、繁体中文、数字、中文语境下的英文）合成为语音，并以聆小珊女声音色中文播报。
开发者可对播报的策略进行设置，包括单词播报、数字播报、静音停顿、汉字发音策略。
场景介绍
手机/平板等设备在无网状态下，系统应用无障碍（屏幕朗读）接入文本转语音能力，为视障人士或不方便阅读场景提供播报能力。
约束与限制
该能力当前不支持模拟器。
开发步骤
1.
```typescript
import { textToSpeech } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.  createEngine接口提供了两种调用形式，当前以其中一种作为示例，其他方式可参考API参考。
```typescript
let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置创建引擎参数
let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName'};
let initParamsInfo: textToSpeech.CreateEngineParams = {
language: 'zh-CN',
person: 0,
online: 1,
extraParams: extraParam
};
// 调用createEngine方法
textToSpeech.createEngine(initParamsInfo, (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
if (!err) {
console.info('Succeeded in creating engine');
// 接收创建引擎的实例
ttsEngine = textToSpeechEngine;
} else {
console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
}
});
```
3.
```typescript
// 设置speak的回调信息
let speakListener: textToSpeech.SpeakListener = {
// 开始播报回调
onStart(requestId: string, response: textToSpeech.StartResponse) {
console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
},
// 合成完成及播报完成回调
onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
},
// 停止播报回调
onStop(requestId: string, response: textToSpeech.StopResponse) {
console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
},
// 返回音频流
onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
},
// 错误回调
onError(requestId: string, errorCode: number, errorMessage: string) {
console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
}
};
// 设置回调
ttsEngine.setListener(speakListener);
let originalText: string = 'Hello HarmonyOS';
// 设置播报相关参数
let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN',
"audioType": "pcm", "soundChannel": 3, "playType": 1 };
let speakParams: textToSpeech.SpeakParams = {
requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
extraParams: extraParam
};
// 调用播报方法
// 开发者可以通过修改speakParams主动设置播报策略
ttsEngine.speak(originalText, speakParams);
```
4.
```typescript
ttsEngine.stop();
```
5.
```typescript
ttsEngine.isBusy();
```
6.
```typescript
// 在组件中声明并初始化字符串voiceInfo
@State voiceInfo: string = "";
// 设置查询相关参数
let voicesQuery: textToSpeech.VoiceQuery = {
requestId: '12345678', // requestId在同一实例内仅能用一次，请勿重复设置
online: 1
};
// 调用listVoices方法，以callback返回
ttsEngine.listVoices(voicesQuery, (err: BusinessError, voiceInfo: textToSpeech.VoiceInfo[]) => {
if (!err) {
// 接收目前支持的语种音色等信息
this.voiceInfo = JSON.stringify(voiceInfo);
console.info(`Succeeded in listing voices, voiceInfo is ${this.voiceInfo}`);
} else {
console.error(`Failed to list voices. Code: ${err.code}, message: ${err.message}`);
}
});
```
设置播报策略
由于不同场景下，模型自动判断所选择的播报策略可能与实际需求不同，此章节提供对于播报策略进行主动设置的方法。
以下取值说明均为有效取值，若所使用的数值在有效取值之外则播报结果可能与预期不符，并产生错误的播报结果。
设置单词播报方式
文本格式：[hN] (N=0/1/2)
N取值说明：
| 取值 | 说明 |
| --- | --- |
| 0 | 智能判断单词播放方式。默认值为0。 |
| 1 | 逐个字母进行播报。 |
| 2 | 以单词方式进行播报。 |
取值
说明
0
智能判断单词播放方式。默认值为0。
1
逐个字母进行播报。
2
以单词方式进行播报。
文本示例：
hello使用单词发音，world及后续单词将会逐个字母进行发音。
设置数字播报策略
格式：[nN] (N=0/1/2)
N取值说明：
| 取值 | 说明 |
| --- | --- |
| 0 | 智能判断数字处理策略。默认值为0。 |
| 1 | 作为号码逐个数字播报。 |
| 2 | 作为数值播报。超过18位数字不支持，自动按逐个数字进行播报。 |
取值
说明
0
智能判断数字处理策略。默认值为0。
1
作为号码逐个数字播报。
2
作为数值播报。超过18位数字不支持，自动按逐个数字进行播报。
文本示例：
其中，123将会按照数值播报，456则会按照号码播报，而后的文本中的数字，均会自动判断。
插入静音停顿
格式：[pN]
描述：N为无符号整数，单位为ms。
文本示例：
该句播报时，将会在“你好”后插入500ms的静音停顿。
指定汉字发音
汉字声调用后接一位数字1~5分别表示阴平、阳平、上声、去声和轻声5个声调。
格式：[=MN]
描述：M表示拼音，N表示声调。
N取值说明：
| 取值 | 说明 |
| --- | --- |
| 1 | 阴平 |
| 2 | 阳平 |
| 3 | 上声 |
| 4 | 去声 |
| 5 | 轻声 |
取值
说明
1
阴平
2
阳平
3
上声
4
去声
5
轻声
文本示例：
“着”字将读作“zhuó”。
开发实例
```typescript
import { textToSpeech } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
let ttsEngine: textToSpeech.TextToSpeechEngine;
@Entry
@Component
struct Index {
@State createCount: number = 0;
@State voiceInfo: string = "";
@State originalText: string = "\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t" +
"纸上得来终觉浅，绝知此事要躬行。\n\t\t";
build() {
Column() {
Scroll() {
Column() {
TextArea({ placeholder: 'Please enter tts original text', text: `${this.originalText}` })
.margin(20)
.focusable(false)
.border({ width: 5, color: 0x317AE7, radius: 10, style: BorderStyle.Solid })
.onChange((value: string) => {
this.originalText = value;
console.info(`original text: ${this.originalText}`);
})
Button() {
Text("CreateEngineByCallback")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
this.createCount++;
console.info(`CreateTtsEngine：createCount:${this.createCount}`);
this.createByCallback();
})
Button() {
Text("speak")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
this.createCount++;
this.speak();
})
Button() {
Text("listVoicesCallback")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
this.listVoicesCallback();
})
Button() {
Text("stop")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
// 停止播报
console.info("Stop button clicked.");
ttsEngine.stop();
})
Button() {
Text("isBusy")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
// 查询播报状态
let isBusy = ttsEngine.isBusy();
console.info(`isBusy: ${isBusy}`);
})
Button() {
Text("shutdown")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AA7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
// 释放引擎
ttsEngine.shutdown();
})
}
.layoutWeight(1)
}
.width('100%')
.height('100%')
}
}
// 创建引擎，通过callback形式返回
private createByCallback() {
// 设置创建引擎参数
let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName'};
let initParamsInfo: textToSpeech.CreateEngineParams = {
language: 'zh-CN',
person: 0,
online: 1,
extraParams: extraParam
};
// 调用createEngine方法
textToSpeech.createEngine(initParamsInfo, (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
if (!err) {
console.info('Succeeded in creating engine.');
// 接收创建引擎的实例
ttsEngine = textToSpeechEngine;
} else {
console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
}
});
};
// 调用speak播报方法
private speak() {
let speakListener: textToSpeech.SpeakListener = {
// 开始播报回调
onStart(requestId: string, response: textToSpeech.StartResponse) {
console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
},
// 完成播报回调
onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
},
// 停止播报完成回调，调用stop方法并完成时会触发此回调
onStop(requestId: string, response: textToSpeech.StopResponse) {
console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
},
// 返回音频流
onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
},
// 错误回调，播报过程发生错误时触发此回调
onError(requestId: string, errorCode: number, errorMessage: string) {
console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
}
};
// 设置回调
ttsEngine.setListener(speakListener);
// 设置播报相关参数
let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm", "soundChannel": 3, "playType":1}
let speakParams: textToSpeech.SpeakParams = {
requestId: '123456-a', // requestId在同一实例内仅能用一次，请勿重复设置
extraParams: extraParam
};
// 调用speak播报方法
ttsEngine.speak(this.originalText, speakParams);
};
// 查询语种音色信息，以callback形式返回
private listVoicesCallback() {
// 设置查询相关参数
let voicesQuery: textToSpeech.VoiceQuery = {
requestId: '123456-b', // requestId在同一实例内仅能用一次，请勿重复设置
online: 1
};
// 调用listVoices方法，以callback返回语种音色查询结果
ttsEngine.listVoices(voicesQuery, (err: BusinessError, voiceInfo: textToSpeech.VoiceInfo[]) => {
if (!err) {
// 接收目前支持的语种音色等信息
this.voiceInfo = JSON.stringify(voiceInfo);
console.info(`Succeeded in listing voices, voiceInfo is ${voiceInfo}`);
} else {
console.error(`Failed to list voices. Code: ${err.code}, message: ${err.message}`);
}
});
};
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/speechrecognizer-guide-V14
爬取时间: 2025-04-30 04:22:56
来源: Huawei Developer
将一段中文音频信息（中文、中文语境下的英文；短语音模式不超过60s，长语音模式不超过8h）转换为文本，音频信息可以为pcm音频文件或者实时语音。
场景介绍
手机/平板等设备在无网状态下，为听障人士或不方便收听音频场景提供音频转文本能力。
约束与限制
该能力当前不支持模拟器。
开发步骤
1.
```typescript
import { speechRecognizer } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.  createEngine方法提供了两种调用形式，当前以其中一种作为示例，其他方式可参考API参考。
```typescript
let asrEngine: speechRecognizer.SpeechRecognitionEngine;
let sessionId: string = '123456';
// 创建引擎，通过callback形式返回
// 设置创建引擎参数
let extraParam: Record<string, Object> = {"locate": "CN", "recognizerMode": "short"};
let initParamsInfo: speechRecognizer.CreateEngineParams = {
language: 'zh-CN',
online: 1,
extraParams: extraParam
};
// 调用createEngine方法
speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine: speechRecognizer.SpeechRecognitionEngine) => {
if (!err) {
console.info('Succeeded in creating engine.');
// 接收创建引擎的实例
asrEngine = speechRecognitionEngine;
} else {
console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
}
});
```
3.
```typescript
// 创建回调对象
let setListener: speechRecognizer.RecognitionListener = {
// 开始识别成功回调
onStart(sessionId: string, eventMessage: string) {
console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
},
// 事件回调
onEvent(sessionId: string, eventCode: number, eventMessage: string) {
console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
},
// 识别结果回调，包括中间结果和最终结果
onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
console.info(`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}`);
},
// 识别完成回调
onComplete(sessionId: string, eventMessage: string) {
console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
},
// 错误回调，错误码通过本方法返回
// 返回错误码1002200002，开始识别失败，重复启动startListening方法时触发
// 更多错误码请参考错误码参考
onError(sessionId: string, errorCode: number, errorMessage: string) {
console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
},
}
// 设置回调
asrEngine.setListener(setListener);
```
4.
5.
```typescript
let uint8Array: Uint8Array = new Uint8Array();
// 可以通过如下方式获取音频流：1、通过录音获取音频流；2、从音频文件中读取音频流
// 两种方式示例均已实现:demo参考
// 写入音频流，音频流长度仅支持640或1280
asrEngine.writeAudio(sessionId, uint8Array);
```
6.
```typescript
// 设置查询相关的参数
let languageQuery: speechRecognizer.LanguageQuery = {
sessionId: sessionId
};
// 调用listLanguages方法
asrEngine.listLanguages(languageQuery).then((res: Array<string>) => {
console.info(`Succeeded in listing languages, result: ${JSON.stringify(res)}.`);
}).catch((err: BusinessError) => {
console.error(`Failed to list languages. Code: ${err.code}, message: ${err.message}.`);
});
```
7.
```typescript
// 结束识别
asrEngine.finish(sessionId);
```
8.
```typescript
// 取消识别
asrEngine.cancel(sessionId);
```
9.
```typescript
// 释放识别引擎资源
asrEngine.shutdown();
```
10.
开发实例
```typescript
import { speechRecognizer } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import AudioCapturer from './AudioCapturer';
const TAG = 'CoreSpeechKitDemo';
let asrEngine: speechRecognizer.SpeechRecognitionEngine;
@Entry
@Component
struct Index {
@State createCount: number = 0;
@State result: boolean = false;
@State voiceInfo: string = "";
@State sessionId: string = "123456";
@State sessionId2: string = "1234567";
private mAudioCapturer = new AudioCapturer();
build() {
Column() {
Scroll() {
Column() {
Button() {
Text("CreateEngineByCallback")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
this.createCount++;
hilog.info(0x0000, TAG, `CreateAsrEngine：createCount:${this.createCount}`);
this.createByCallback();
})
Button() {
Text("setListener")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
this.setListener();
})
Button() {
Text("startRecording")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
this.startRecording();
})
Button() {
Text("writeAudio")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
this.writeAudio();
})
Button() {
Text("queryLanguagesCallback")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
this.queryLanguagesCallback();
})
Button() {
Text("finish")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
// 结束识别
hilog.info(0x0000, TAG, "finish click:-->");
asrEngine.finish(this.sessionId);
})
Button() {
Text("cancel")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AE7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
// 取消识别
hilog.info(0x0000, TAG, "cancel click:-->");
asrEngine.cancel(this.sessionId);
})
Button() {
Text("shutdown")
.fontColor(Color.White)
.fontSize(20)
}
.type(ButtonType.Capsule)
.backgroundColor("#0x317AA7")
.width("80%")
.height(50)
.margin(10)
.onClick(() => {
// 释放引擎
asrEngine.shutdown();
})
}
.layoutWeight(1)
}
.width('100%')
.height('100%')
}
}
// 创建引擎，通过callback形式返回
private createByCallback() {
// 设置创建引擎参数
let extraParam: Record<string, Object> = {"locate": "CN", "recognizerMode": "short"};
let initParamsInfo: speechRecognizer.CreateEngineParams = {
language: 'zh-CN',
online: 1,
extraParams: extraParam
};
// 调用createEngine方法
speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine:
speechRecognizer.SpeechRecognitionEngine) => {
if (!err) {
hilog.info(0x0000, TAG, 'Succeeded in creating engine.');
// 接收创建引擎的实例
asrEngine = speechRecognitionEngine;
} else {
// 无法创建引擎时返回错误码1002200001，原因：语种不支持、模式不支持、初始化超时、资源不存在等导致创建引擎失败
// 无法创建引擎时返回错误码1002200006，原因：引擎正在忙碌中，一般多个应用同时调用语音识别引擎时触发
// 无法创建引擎时返回错误码1002200008，原因：引擎已被销毁
hilog.error(0x0000, TAG, `Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
}
});
}
// 查询语种信息，以callback形式返回
private queryLanguagesCallback() {
// 设置查询相关参数
let languageQuery: speechRecognizer.LanguageQuery = {
sessionId: this.sessionId
};
// 调用listLanguages方法
asrEngine.listLanguages(languageQuery, (err: BusinessError, languages: Array<string>) => {
if (!err) {
// 接收目前支持的语种信息
hilog.info(0x0000, TAG, `Succeeded in listing languages, result: ${JSON.stringify(languages)}`);
} else {
hilog.error(0x0000, TAG, `Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
}
});
};
// 开始识别
private startListeningForWriteAudio() {
// 设置开始识别的相关参数
let recognizerParams: speechRecognizer.StartParams = {
sessionId: this.sessionId,
audioInfo: { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 } //audioInfo参数配置请参考AudioInfo
}
// 调用开始识别方法
asrEngine.startListening(recognizerParams);
};
private startListeningForRecording() {
let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 }
let extraParam: Record<string, Object> = {
"recognitionMode": 0,
"vadBegin": 2000,
"vadEnd": 3000,
"maxAudioDuration": 20000
}
let recognizerParams: speechRecognizer.StartParams = {
sessionId: this.sessionId,
audioInfo: audioParam,
extraParams: extraParam
}
hilog.info(0x0000, TAG, 'startListening start');
asrEngine.startListening(recognizerParams);
};
// 写音频流
private async writeAudio() {
this.startListeningForWriteAudio();
hilog.error(0x0000, TAG, `Failed to read from file. Code`);
let ctx = getContext(this);
let filenames: string[] = fileIo.listFileSync(ctx.filesDir);
if (filenames.length <= 0) {
hilog.error(0x0000, TAG, `Failed to read from file. Code`);
return;
}
hilog.error(0x0000, TAG, `Failed to read from file. Code`);
let filePath: string = `${ctx.filesDir}/${filenames[0]}`;
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
try {
let buf: ArrayBuffer = new ArrayBuffer(1280);
let offset: number = 0;
while (1280 == fileIo.readSync(file.fd, buf, {
offset: offset
})) {
let uint8Array: Uint8Array = new Uint8Array(buf);
asrEngine.writeAudio(this.sessionId, uint8Array);
await this.countDownLatch(1);
offset = offset + 1280;
}
} catch (err) {
hilog.error(0x0000, TAG, `Failed to read from file. Code: ${err.code}, message: ${err.message}.`);
} finally {
if (null != file) {
fileIo.closeSync(file);
}
}
}
// 麦克风语音转文本
private async startRecording() {
this.startListeningForRecording();
// 录音获取音频
let data: ArrayBuffer;
hilog.info(0x0000, TAG, 'create capture success');
this.mAudioCapturer.init((dataBuffer: ArrayBuffer) => {
hilog.info(0x0000, TAG, 'start write');
hilog.info(0x0000, TAG, 'ArrayBuffer ' + JSON.stringify(dataBuffer));
data = dataBuffer
let uint8Array: Uint8Array = new Uint8Array(data);
hilog.info(0x0000, TAG, 'ArrayBuffer uint8Array ' + JSON.stringify(uint8Array));
// 写入音频流
asrEngine.writeAudio(this.sessionId2, uint8Array);
});
};
// 计时
public async countDownLatch(count: number) {
while (count > 0) {
await this.sleep(40);
count--;
}
}
// 睡眠
private sleep(ms: number):Promise<void> {
return new Promise(resolve => setTimeout(resolve, ms));
}
// 设置回调
private setListener() {
// 创建回调对象
let setListener: speechRecognizer.RecognitionListener = {
// 开始识别成功回调
onStart(sessionId: string, eventMessage: string) {
hilog.info(0x0000, TAG, `onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
},
// 事件回调
onEvent(sessionId: string, eventCode: number, eventMessage: string) {
hilog.info(0x0000, TAG, `onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
},
// 识别结果回调，包括中间结果和最终结果
onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
hilog.info(0x0000, TAG, `onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}`);
},
// 识别完成回调
onComplete(sessionId: string, eventMessage: string) {
hilog.info(0x0000, TAG, `onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
},
// 错误回调，错误码通过本方法返回
// 返回错误码1002200002，开始识别失败，重复启动startListening方法时触发
// 更多错误码请参考错误码参考
onError(sessionId: string, errorCode: number, errorMessage: string) {
hilog.error(0x0000, TAG, `onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
},
}
// 设置回调
asrEngine.setListener(setListener);
};
}
```
添加AudioCapturer.ts文件用于获取麦克风音频流。
```typescript
'use strict';
/*
* Copyright (c) Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.
*/
import {audio} from '@kit.AudioKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG = 'AudioCapturer';
/**
* Audio collector tool
*/
export default class AudioCapturer {
/**
* Collector object
*/
private mAudioCapturer = null;
/**
* Audio Data Callback Method
*/
private mDataCallBack: (data: ArrayBuffer) => void = null;
/**
* Indicates whether recording data can be obtained.
*/
private mCanWrite: boolean = true;
/**
* Audio stream information
*/
private audioStreamInfo = {
samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_16000,
channels: audio.AudioChannel.CHANNEL_1,
sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
}
/**
* Audio collector information
*/
private audioCapturerInfo = {
source: audio.SourceType.SOURCE_TYPE_MIC,
capturerFlags: 0
}
/**
* Audio Collector Option Information
*/
private audioCapturerOptions = {
streamInfo: this.audioStreamInfo,
capturerInfo: this.audioCapturerInfo
}
/**
*  Initialize
* @param audioListener
*/
public async init(dataCallBack: (data: ArrayBuffer) => void) {
if (null != this.mAudioCapturer) {
hilog.error(0x0000, TAG, 'AudioCapturerUtil already init');
return;
}
this.mDataCallBack = dataCallBack;
this.mAudioCapturer = await audio.createAudioCapturer(this.audioCapturerOptions).catch(error => {
hilog.error(0x0000, TAG, `AudioCapturerUtil init createAudioCapturer failed, code is ${error.code}, message is ${error.message}`);
});
}
/**
* start recording
*/
public async start() {
hilog.error(0x0000, TAG, `AudioCapturerUtil start`);
let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
if (stateGroup.indexOf(this.mAudioCapturer.state) === -1) {
hilog.error(0x0000, TAG, `AudioCapturerUtil start failed`);
return;
}
this.mCanWrite = true;
await this.mAudioCapturer.start();
while (this.mCanWrite) {
let bufferSize = await this.mAudioCapturer.getBufferSize();
let buffer = await this.mAudioCapturer.read(bufferSize, true);
this.mDataCallBack(buffer)
}
}
/**
* stop recording
*/
public async stop() {
if (this.mAudioCapturer.state !== audio.AudioState.STATE_RUNNING && this.mAudioCapturer.state !== audio.AudioState.STATE_PAUSED) {
hilog.error(0x0000, TAG, `AudioCapturerUtil stop Capturer is not running or paused`);
return;
}
this.mCanWrite = false;
await this.mAudioCapturer.stop();
if (this.mAudioCapturer.state === audio.AudioState.STATE_STOPPED) {
hilog.info(0x0000, TAG, `AudioCapturerUtil Capturer stopped`);
} else {
hilog.error(0x0000, TAG, `Capturer stop failed`);
}
}
/**
* release
*/
public async release() {
if (this.mAudioCapturer.state === audio.AudioState.STATE_RELEASED || this.mAudioCapturer.state === audio.AudioState.STATE_NEW) {
hilog.error(0x0000, TAG, `Capturer already released`);
return;
}
await this.mAudioCapturer.release();
this.mAudioCapturer = null;
if (this.mAudioCapturer.state == audio.AudioState.STATE_RELEASED) {
hilog.info(0x0000, TAG, `Capturer released`);
} else {
hilog.error(0x0000, TAG, `Capturer release failed`);
}
}
}
```
在EntryAbility.ets文件中添加麦克风权限。
```typescript
import { abilityAccessCtrl, AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
}
onDestroy(): void {
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
}
onWindowStageCreate(windowStage: window.WindowStage): void {
// Main window is created, set main page for this ability
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
let atManager = abilityAccessCtrl.createAtManager();
atManager.requestPermissionsFromUser(this.context, ['ohos.permission.MICROPHONE']).then((data) => {
hilog.info(0x0000, 'testTag', 'data:' + JSON.stringify(data));
hilog.info(0x0000, 'testTag', 'data permissions:' + data.permissions);
hilog.info(0x0000, 'testTag', 'data authResults:' + data.authResults);
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + 'errMessage: ' + err.message);
});
windowStage.loadContent('pages/Index', (err, data) => {
if (err.code) {
hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
});
}
onWindowStageDestroy(): void {
// Main window is destroyed, release UI related resources
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
}
onForeground(): void {
// Ability has brought to foreground
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
}
onBackground(): void {
// Ability has back to background
hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-vision-kit-guide-V14
爬取时间: 2025-04-30 04:23:10
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-vision-introduction-V14
爬取时间: 2025-04-30 04:23:23
来源: Huawei Developer
Core Vision Kit（基础视觉服务）提供了机器视觉相关的基础能力，例如通用文字识别（即OCR，Optical Character Recognition，也称为光学字符识别）、人脸检测、人脸比对以及主体分割等能力。
用户可以结合Vision Kit的UI控件能力（例如：活体检测），提升应用的智能化、便捷化交互体验。
场景介绍
Core Vision Kit可应用于各种场景，提升用户体验和应用效率。以下是一些典型的应用场景：
约束与限制
| AI能力  | 约束  |
| --- | --- |
| 文字识别  | 支持的图片格式：JPEG、JPG、PNG。支持的语言：简体中文、英文、日文、韩文、繁体中文。文本长度：不超过10000字符。支持文档印刷体识别，在识别手写字体方面能力有所欠缺。输入图像具有合适成像的质量（建议720p以上），100px<高度<15210px，100px<宽度<10000px，高宽比例建议10:1以下，接近手机屏幕高宽比例为宜。文本与拍摄角度夹角在正负30度范围内。  |
| 人脸检测  | 输入图像具有合适的成像质量（建议720p以上），224px<高度<15210px，100px<宽度<10000px，高宽比例建议10:1以下，接近手机屏幕高宽比例为宜。不支持同一用户启用多个线程。  |
| 人脸比对  | 当前功能只支持1v1人脸比对。输入的两张图像都需要合适的成像质量（建议720p以上），224px<高度<15210px，100px<宽度<10000px，高宽比例建议10:1以下，接近手机屏幕高宽比例为宜。  |
| 主体分割  | 某个物体占比不小于原图大小的千分之五才会被认定为“主体”，才会支持分割。不建议用于处理包含较多文字内容的图片分析场景。输入图像具有合适成像的质量（建议720p以上），20px<高度<9000px，20px<宽度<9000px，高宽比例建议3:1以下，接近手机屏幕高宽比例为宜。  |
| 多目标识别  | 输入图像具有合适成像的质量（建议720p以上），100px<高度<10000px，100px<宽度<10000px，高宽比例建议5:1以下，接近手机屏幕高宽比例为宜。图片中的物体占比需要大于0.1%。  |
| 骨骼点检测  | 输入图像具有合适成像的质量（建议720p以上），100px<高度<10000px，100px<宽度<10000px，高宽比例建议5:1以下，接近手机屏幕高宽比例为宜。  |
AI能力
约束
文字识别
人脸检测
人脸比对
主体分割
多目标识别
骨骼点检测
Core Vision Kit的特性支持多用户同时接入，但是不支持同一用户并发调用同一个特性，如同一个特性被同一进程同一时间多次调用，则返回系统繁忙错误，不同进程调用同一特性，则同一时间只有一个进程业务在处理，其他进程进入队列排队。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-vision-text-recognition-V14
爬取时间: 2025-04-30 04:23:38
来源: Huawei Developer
适用场景
通用文字识别，是通过拍照、扫描等光学输入方式，将各种票据、卡证、表格、报刊、书籍等印刷品文字转化为图像信息，再利用文字识别技术将图像信息转化为计算机等设备可以使用的字符信息的技术。
约束与限制
该能力当前不支持模拟器。
详细限制请参考约束与限制
开发步骤
1.
```typescript
import { textRecognition } from '@kit.CoreVisionKit';
```
2.
```typescript
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库，获取图片资源
this.selectImage();
})
```
3.
```typescript
async aboutToAppear(): Promise<void> {
const initResult = await textRecognition.init();
hilog.info(0x0000, 'OCRDemo', `OCR service initialization result:${initResult}`);
}
async aboutToDisappear(): Promise<void> {
await textRecognition.release();
hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
}
private async selectImage() {
let uri = await this.openPhoto();
if (uri === undefined) {
hilog.error(0x0000, 'OCRDemo', "Failed to get uri.");
return;
}
this.loadImage(uri);
}
private openPhoto(): Promise<string> {
return new Promise<string>((resolve) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
maxSelectNumber: 1
}).then((res: photoAccessHelper.PhotoSelectResult) => {
resolve(res.photoUris[0]);
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. code：${err.code}，message：${err.message}`);
resolve('');
})
})
}
private loadImage(name: string) {
setTimeout(async () => {
let imageSource: image.ImageSource | undefined = undefined;
let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await imageSource.createPixelMap();
}, 100)
}
```
4.
```typescript
let visionInfo: textRecognition.VisionInfo = {
pixelMap: this.chooseImage
};
```
5.
```typescript
let textConfiguration: textRecognition.TextRecognitionConfiguration = {
isDirectionDetectionSupported: false
};
```
6.  当调用成功时，获取文字识别的结果；调用失败时，将返回对应错误码。
```typescript
textRecognition.recognizeText(visionInfo, textConfiguration)
.then((data: textRecognition.TextRecognitionResult) => {
// 识别成功，获取对应的结果
let recognitionString = JSON.stringify(data);
hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text：${recognitionString}`);
// 将结果更新到Text中显示
this.dataValues = data.value;
})
.catch((error: BusinessError) => {
hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
this.dataValues = `Error: ${error.message}`;
});
```
开发实例
```typescript
import { textRecognition } from '@kit.CoreVisionKit'
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
@Entry
@Component
struct Index {
private imageSource: image.ImageSource | undefined = undefined;
@State chooseImage: PixelMap | undefined = undefined;
@State dataValues: string = '';
async aboutToAppear(): Promise<void> {
const initResult = await textRecognition.init();
hilog.info(0x0000, 'OCRDemo', `OCR service initialization result:${initResult}`);
}
async aboutToDisappear(): Promise<void> {
await textRecognition.release();
hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
}
build() {
Column() {
Image(this.chooseImage)
.objectFit(ImageFit.Fill)
.height('60%')
Text(this.dataValues)
.copyOption(CopyOptions.LocalDevice)
.height('15%')
.margin(10)
.width('60%')
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库，获取图片资源
this.selectImage();
})
Button('开始识别')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(async () => {
this.textRecognitionTest();
})
}
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
private textRecognitionTest() {
if (!this.chooseImage) {
return;
}
// 调用文本识别接口
let visionInfo: textRecognition.VisionInfo = {
pixelMap: this.chooseImage
};
let textConfiguration: textRecognition.TextRecognitionConfiguration = {
isDirectionDetectionSupported: false
};
textRecognition.recognizeText(visionInfo, textConfiguration)
.then((data: textRecognition.TextRecognitionResult) => {
// 识别成功，获取对应的结果
let recognitionString = JSON.stringify(data);
hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text：${recognitionString}`);
// 将结果更新到Text中显示
this.dataValues = data.value;
})
.catch((error: BusinessError) => {
hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
this.dataValues = `Error: ${error.message}`;
});
}
private async selectImage() {
let uri = await this.openPhoto();
if (uri === undefined) {
hilog.error(0x0000, 'OCRDemo', "Failed to get uri.");
return;
}
this.loadImage(uri);
}
private openPhoto(): Promise<string> {
return new Promise<string>((resolve) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
maxSelectNumber: 1
}).then((res: photoAccessHelper.PhotoSelectResult) => {
resolve(res.photoUris[0]);
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. Code：${err.code}，message：${err.message}`);
resolve('');
})
})
}
private loadImage(name: string) {
setTimeout(async () => {
let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
this.imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await this.imageSource.createPixelMap();
}, 100)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-vision-face-detector-V14
爬取时间: 2025-04-30 04:23:51
来源: Huawei Developer
适用场景
检测图片中的人脸，返回高精度人脸矩形框坐标、人脸五官位置、人脸朝向、人脸置信度。可通过对人脸的定位，实现对人脸特定位置的美化修饰。广泛应用于各类人脸识别场景，如人脸解锁、人脸聚类、美颜等场景中。
约束与限制
该能力当前不支持模拟器。
详细限制请参考约束与限制
世界坐标系
以下方图片指示坐标系辅助表示人脸朝向。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164839.07269629349776551229851244748950:50001231000000:2800:114A232268AE7EA5BEC9F002F208125AD526CFD335D74FCA7D4AB01327A329E1.png)
开发步骤
1.
```typescript
import { faceDetector } from '@kit.CoreVisionKit';
```
2.
```typescript
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库，获取图片资源
this.selectImage();
})
```
3.
```typescript
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, 'faceDetector', "Failed to get uri.");
}
this.loadImage(uri)
}
private openPhoto(): Promise<string> {
return new Promise<string>((resolve) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
maxSelectNumber: 1
}).then(res => {
resolve(res.photoUris[0])
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'faceDetector', `Failed to get photo image uri.code：${err.code}，message：${err.message}`);
resolve('');
})
})
}
private loadImage(name: string) {
setTimeout(async () => {
let imageSource: image.ImageSource | undefined = undefined;
let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await imageSource.createPixelMap();
this.dataValues = "";
hilog.info(0x0000, 'faceDetectorSample', 'this.chooseImage:', this.chooseImage);
}, 100
)
}
```
4.
```typescript
// 初始化并调用人脸检测接口
faceDetector.init();
let visionInfo: faceDetector.VisionInfo = {
pixelMap: this.chooseImage,
};
let data:faceDetector.Face[] = await faceDetector.detect(visionInfo);
```
5.
```typescript
let data:faceDetector.Face[] = await faceDetector.detect(visionInfo);
if (data.length === 0) {
this.dataValues = "No face is detected in the image. Select an image that contains a face.";
} else {
let faceString = JSON.stringify(data);
hilog.info(0x0000, 'testTag', "faceString data is " + faceString);
this.dataValues = faceString;
}
```
开发实例
点击“选择图片”按钮，触发AI人脸检测功能。
```typescript
import { faceDetector } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
@Entry
@Component
struct Index {
@State chooseImage: PixelMap | undefined = undefined
@State dataValues: string = ''
build() {
Column() {
Image(this.chooseImage)
.objectFit(ImageFit.Fill)
.height('60%')
Text(this.dataValues)
.copyOption(CopyOptions.LocalDevice)
.height('15%')
.margin(10)
.width('60%')
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库
this.selectImage()
})
Button('人脸检测')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
if(!this.chooseImage) {
hilog.error(0x0000, 'faceDetectorSample', "Failed to detect face.");
return;
}
// 调用人脸检测接口
faceDetector.init();
let visionInfo: faceDetector.VisionInfo = {
pixelMap: this.chooseImage,
};
faceDetector.detect(visionInfo)
.then((data: faceDetector.Face[]) => {
if (data.length === 0) {
this.dataValues = "No face is detected in the image. Select an image that contains a face.";
} else {
let faceString = JSON.stringify(data);
hilog.info(0x0000, 'faceDetectorSample', "faceString data is " + faceString);
this.dataValues = faceString;
}
})
.catch((error: BusinessError) => {
hilog.error(0x0000, 'faceDetectorSample', `Face detection failed. Code: ${error.code}, message: ${error.message}`);
this.dataValues = `Error: ${error.message}`;
});
faceDetector.release();
})
}
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, 'faceDetectorSample', "Failed to get uri.");
}
this.loadImage(uri);
}
private openPhoto(): Promise<string> {
return new Promise<string>((resolve) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
maxSelectNumber: 1
}).then(res => {
resolve(res.photoUris[0])
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'faceDetectorSample', `Failed to get photo image uri.code：${err.code}，message：${err.message}`);
resolve('');
})
})
}
private loadImage(name: string) {
setTimeout(async () => {
let imageSource: image.ImageSource | undefined = undefined;
let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await imageSource.createPixelMap();
this.dataValues = "";
hilog.info(0x0000, 'faceDetectorSample', 'this.chooseImage:', this.chooseImage);
}, 100
)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-vision-face-comparator-V14
爬取时间: 2025-04-30 04:24:04
来源: Huawei Developer
适用场景
输入的两张比对图片是同一个人的照片时，可以看见其比对结果为同一个人，置信分数比较高；当两张比对图片不是同一个人的照片时，可以看见其比对结果为非同一个人，置信分数很低。可以用于APP中需要用到人脸比对功能的场景，比如娱乐类APP中比较两个人的相似度，与明星的相似度等等。
约束与限制
该能力当前不支持模拟器。
详细限制请参考约束与限制
开发步骤
1.
```typescript
import { faceComparator } from '@kit.CoreVisionKit';
```
2.
```typescript
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库，获取图片资源
this.selectImage();
})
```
3.
```typescript
async aboutToAppear(): Promise<void> {
const initResult = await faceComparator.init();
hilog.info(0x0000, TAG, `Face comparator initialization result:${initResult}`);
}
async aboutToDisappear(): Promise<void> {
await faceComparator.release();
hilog.info(0x0000, TAG, 'Face comparator released successfully');
}
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, 'faceCompare', "Failed to get two image uris.");
}
this.loadImage(uri);
}
private openPhoto(): Promise<string[]> {
return new Promise<string[]>((resolve, reject) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
maxSelectNumber: 2
}).then(res => {
resolve(res.photoUris);
}).catch((err: BusinessError) => {
hilog.error(0x0000, TAG, `Failed to get photo image uris. code: ${err.code}, message: ${err.message}`);
reject();
});
});
}
private loadImage(names: string[]) {
setTimeout(async () => {
let imageSource: image.ImageSource | undefined = undefined;
let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await imageSource.createPixelMap();
fileSource = await fileIo.open(names[1], fileIo.OpenMode.READ_ONLY);
imageSource = image.createImageSource(fileSource.fd);
this.chooseImage1 = await imageSource.createPixelMap();
hilog.info(0x0000, 'faceCompare', 'this.chooseImage:', this.chooseImage, 'this.chooseImage1:', this.chooseImage1);
}, 100
)
}
```
4.
```typescript
// 调用人脸比对接口
let visionInfo: faceComparator.VisionInfo = {
pixelMap: this.chooseImage,
};
let visionInfo1: faceComparator.VisionInfo = {
pixelMap: this.chooseImage1,
};
let data:faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
```
5.
```typescript
let data:faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
let faceString = "degree of similarity："+ this.toPercentage(data.similarity)+((data.isSamePerson)?". is":". no")+ " same person";
hilog.info(0x0000, 'testTag', "faceString data is " + faceString);
this.dataValues = faceString;
```
开发实例
```typescript
import { faceComparator } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
const TAG: string = "FaceCompareSample";
@Entry
@Component
struct Index {
@State chooseImage: PixelMap | undefined = undefined
@State chooseImage1: PixelMap | undefined = undefined
@State dataValues: string = ''
async aboutToAppear(): Promise<void> {
const initResult = await faceComparator.init();
hilog.info(0x0000, TAG, `Face comparator initialization result:${initResult}`);
}
async aboutToDisappear(): Promise<void> {
await faceComparator.release();
hilog.info(0x0000, TAG, 'Face comparator released successfully');
}
build() {
Column() {
Image(this.chooseImage)
.objectFit(ImageFit.Fill)
.height('30%')
.accessibilityDescription("默认图片1")
Image(this.chooseImage1)
.objectFit(ImageFit.Fill)
.height('30%')
.accessibilityDescription("默认图片2")
Text(this.dataValues)
.copyOption(CopyOptions.LocalDevice)
.height('15%')
.margin(10)
.width('60%')
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库
this.selectImage()
})
Button('人脸比对')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
if(!this.chooseImage || !this.chooseImage1) {
hilog.error(0x0000, TAG, "Failed to choose image");
return;
}
// 调用人脸比对接口
let visionInfo: faceComparator.VisionInfo = {
pixelMap: this.chooseImage,
};
let visionInfo1: faceComparator.VisionInfo = {
pixelMap: this.chooseImage1,
};
faceComparator.compareFaces(visionInfo, visionInfo1)
.then((data: faceComparator.FaceCompareResult) => {
let faceString = "degree of similarity："+ this.toPercentage(data.similarity)+((data.isSamePerson)?". is":". no")+ " same person";
hilog.info(0x0000, TAG, "faceString data is " + faceString);
this.dataValues = faceString;
})
.catch((error: BusinessError) => {
hilog.error(0x0000, TAG, `Face comparison failed. Code: ${error.code}, message: ${error.message}`);
this.dataValues = `Error: ${error.message}`;
});
})
}
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
private toPercentage(num: number): string {
return `${(num * 100).toFixed(2)}%`;
}
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, TAG, "Failed to get two image uris.");
}
this.loadImage(uri);
}
private openPhoto(): Promise<string[]> {
return new Promise<string[]>((resolve, reject) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
maxSelectNumber: 2
}).then(res => {
resolve(res.photoUris);
}).catch((err: BusinessError) => {
hilog.error(0x0000, TAG, `Failed to get photo image uris. code: ${err.code}, message: ${err.message}`);
reject();
});
});
}
private loadImage(names: string[]) {
setTimeout(async () => {
let imageSource: image.ImageSource | undefined = undefined;
let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await imageSource.createPixelMap();
fileSource = await fileIo.open(names[1], fileIo.OpenMode.READ_ONLY);
imageSource = image.createImageSource(fileSource.fd);
this.chooseImage1 = await imageSource.createPixelMap();
hilog.info(0x0000, TAG, 'this.chooseImage:', this.chooseImage, 'this.chooseImage1:', this.chooseImage1);
}, 100
)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-vision-subject-segmentation-V14
爬取时间: 2025-04-30 04:24:17
来源: Huawei Developer
适用场景
主体分割，可以检测出图片中区别于背景的前景物体或区域（即“显著主体”），并将其从背景中分离出来，适用于需要识别和提取图像主要信息的场景，广泛使用于前景目标检测和前景主体分离的场景。例如：
约束与限制
该能力当前不支持模拟器。
详细限制请参考约束与限制
开发步骤
1.
```typescript
import { subjectSegmentation } from '@kit.CoreVisionKit';
```
2.
```typescript
async aboutToAppear(): Promise<void> {
const initResult = await subjectSegmentation.init();
hilog.info(0x0000, 'subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);
}
async aboutToDisappear(): Promise<void> {
await subjectSegmentation.release();
hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
}
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, TAG, "uri is undefined");
}
this.loadImage(uri);
}
private openPhoto(): Promise<Array<string>> {
return new Promise<Array<string>>((resolve, reject) => {
let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
PhotoSelectOptions.maxSelectNumber = 1;
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
hilog.info(0x0000, TAG, 'PhotoViewPicker.select successfully, PhotoSelectResult uri: ');
photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
hilog.info(0x0000, TAG, `PhotoViewPicker.select successfully, PhotoSelectResult uri: ${PhotoSelectResult.photoUris}`);
resolve(PhotoSelectResult.photoUris)
}).catch((err: BusinessError) => {
hilog.error(0x0000, TAG, `PhotoViewPicker.select failed with errCode: ${err.code}, errMessage: ${err.message}`);
reject();
});
})
}
private loadImage(names: string[]) {
setTimeout(async () => {
let imageSource: image.ImageSource | undefined = undefined
let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY)
imageSource = image.createImageSource(fileSource.fd)
this.chooseImage = await imageSource.createPixelMap()
hilog.info(0x0000, TAG, `this.chooseImage===${this.chooseImage}`);
}, 100
)
}
```
3.
```typescript
let visionInfo: subjectSegmentation.VisionInfo = {
pixelMap: this.chooseImage,
};
```
4.
```typescript
let config: subjectSegmentation.SegmentationConfig = {
maxCount: parseInt(this.maxNum),
enableSubjectDetails: true,
enableSubjectForegroundImage: true,
};
```
5.
```typescript
let data: subjectSegmentation.SegmentationResult = await subjectSegmentation.doSegmentation(visionInfo, config);
let outputString = `Subject count: ${data.subjectCount}\n`;
outputString += `Max subject count: ${config.maxCount}\n`;
outputString += `Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
let segBoxString = `Full subject box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;
outputString += segBoxString;
if (config.enableSubjectDetails) {
outputString += 'Individual subject boxes:\n';
if (data.subjectDetails) {
for (let i = 0; i < data.subjectDetails.length; i++) {
let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
}
}
}
```
开发实例
```typescript
import { subjectSegmentation } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
const TAG: string = "ImageSegmentationSample";
@Entry
@Component
struct Index {
@State chooseImage: PixelMap | undefined = undefined
@State dataValues: string = ''
@State segmentedImage: PixelMap | undefined = undefined
@State maxNum: string = '20'
build() {
Column() {
Image(this.chooseImage)
.objectFit(ImageFit.Fill)
.height('30%')
.accessibilityDescription("Image to be segmented")
Scroll() {
Text(this.dataValues)
.copyOption(CopyOptions.LocalDevice)
.margin(10)
.width('100%')
}
.height('20%')
Image(this.segmentedImage)
.objectFit(ImageFit.Fill)
.height('30%')
.accessibilityDescription("Segmented subject image")
Row() {
Text('Max subject count:')
.fontSize(16)
TextInput({ placeholder: 'Enter max subject count', text: this.maxNum })
.type(InputType.Number)
.placeholderColor(Color.Gray)
.fontSize(16)
.backgroundColor(Color.White)
.onChange((value: string) => {
this.maxNum = value
})
}
.width('80%')
.margin(10)
Button('Select Image')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
this.selectImage()
})
Button('Image Segmentation')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
if (!this.chooseImage) {
hilog.error(0x0000, TAG, "imageSegmentation not have chooseImage");
return
}
let visionInfo: subjectSegmentation.VisionInfo = {
pixelMap: this.chooseImage,
};
let config: subjectSegmentation.SegmentationConfig = {
maxCount: parseInt(this.maxNum),
enableSubjectDetails: true,
enableSubjectForegroundImage: true,
};
subjectSegmentation.doSegmentation(visionInfo, config)
.then((data: subjectSegmentation.SegmentationResult) => {
let outputString = `Subject count: ${data.subjectCount}\n`;
outputString += `Max subject count: ${config.maxCount}\n`;
outputString += `Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
let segBoxString = `Full subject box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;
outputString += segBoxString;
if (config.enableSubjectDetails) {
outputString += 'Individual subject boxes:\n';
if (data.subjectDetails) {
for (let i = 0; i < data.subjectDetails.length; i++) {
let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
}
}
}
hilog.info(0x0000, TAG, "Segmentation result: " + outputString);
this.dataValues = outputString;
if (data.fullSubject && data.fullSubject.foregroundImage) {
this.segmentedImage = data.fullSubject.foregroundImage;
} else {
hilog.warn(0x0000, TAG, "No foreground image in segmentation result");
}
})
.catch((error: BusinessError) => {
hilog.error(0x0000, TAG, `Image segmentation failed errCode: ${error.code}, errMessage: ${error.message}`);
this.dataValues = `Error: ${error.message}`;
this.segmentedImage = undefined;
});
})
}
.width('100%')
.height('80%')
.justifyContent(FlexAlign.Center)
}
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, TAG, "uri is undefined");
}
this.loadImage(uri);
}
private openPhoto(): Promise<Array<string>> {
return new Promise<Array<string>>((resolve, reject) => {
let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
PhotoSelectOptions.maxSelectNumber = 1;
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
hilog.info(0x0000, TAG, 'PhotoViewPicker.select successfully, PhotoSelectResult uri: ');
photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
hilog.info(0x0000, TAG, `PhotoViewPicker.select successfully, PhotoSelectResult uri: ${PhotoSelectResult.photoUris}`);
resolve(PhotoSelectResult.photoUris)
}).catch((err: BusinessError) => {
hilog.error(0x0000, TAG, `PhotoViewPicker.select failed with errCode: ${err.code}, errMessage: ${err.message}`);
reject();
});
})
}
private loadImage(names: string[]) {
setTimeout(async () => {
let imageSource: image.ImageSource | undefined = undefined
let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY)
imageSource = image.createImageSource(fileSource.fd)
this.chooseImage = await imageSource.createPixelMap()
hilog.info(0x0000, TAG, `this.chooseImage===${this.chooseImage}`);
}, 100
)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-vision-object-detection-V14
爬取时间: 2025-04-30 04:24:30
来源: Huawei Developer
适用场景
可同时检测出给定图片中的各种物体，包括风景、动物、植物、建筑、人脸、表格、文本等位置，并框选出物体。
约束与限制
该能力当前不支持模拟器。
详细限制请参考约束与限制
开发步骤
1.
```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { objectDetection, visionBase } from '@kit.CoreVisionKit';
```
2.
```typescript
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库，获取图片资源
this.selectImage();
})
```
3.
```typescript
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, 'objectDetectSample', "Failed to defined uri.");
}
this.loadImage(uri)
}
private openPhoto(): Promise<string> {
return new Promise<string>((resolve, reject) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
}).then(res => {
resolve(res.photoUris[0])
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'objectDetectSample', `Failed to get photo image uri. code：${err.code}，message：${err.message}`);
reject('')
})
})
}
private loadImage(name: string) {
setTimeout(async () => {
let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
this.imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await this.imageSource.createPixelMap();
}, 100)
}
```
4.
```typescript
// 调用多目标检测接口
let request: visionBase.Request = {
inputData: { pixelMap: this.chooseImage }
};
let data: objectDetection.ObjectDetectionResponse = await (await objectDetection.ObjectDetector.create()).process(request);
```
5.
```typescript
let objectJson = JSON.stringify(data);
hilog.info(0x0000, 'objectDetectSample', `Succeeded in object detection：${objectJson}`);
this.dataValues = objectJson;
```
开发实例
点击“选择图片”按钮，触发AI多目标识别功能。
```typescript
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { objectDetection, visionBase } from '@kit.CoreVisionKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
@Entry
@Component
struct Index {
private imageSource: image.ImageSource | undefined = undefined;
@State chooseImage: PixelMap | undefined = undefined
@State dataValues: string = ''
build() {
Column() {
Image(this.chooseImage)
.objectFit(ImageFit.Fill)
.height('60%')
Text(this.dataValues)
.copyOption(CopyOptions.LocalDevice)
.height('15%')
.margin(10)
.width('60%')
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库
this.selectImage()
})
Button('开始多目标识别')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(async () => {
if(!this.chooseImage) {
hilog.error(0x0000, 'objectDetectSample', `Failed to choose image. chooseImage: ${this.chooseImage}`);
return;
}
let request: visionBase.Request = {
inputData: { pixelMap: this.chooseImage }
};
let data: objectDetection.ObjectDetectionResponse = await (await objectDetection.ObjectDetector.create()).process(request);
let objectJson = JSON.stringify(data);
hilog.info(0x0000, 'objectDetectSample', `Succeeded in object detection：${objectJson}`);
this.dataValues = objectJson;
})
}
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
private async selectImage() {
try {
let uri = await this.openPhoto();
if (uri === undefined) {
hilog.error(0x0000, 'objectDetectSample', "Failed to defined uri.");
return;
}
this.loadImage(uri);
} catch (err) {
hilog.error(0x0000, 'objectDetectSample', `Failed to get photo image uri. code：${err.code}, message：${err.message}`);
}
}
private openPhoto(): Promise<string> {
return new Promise<string>((resolve, reject) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
}).then(res => {
resolve(res.photoUris[0]);
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'objectDetectSample', `Failed to get photo image uri. code：${err.code}, message：${err.message}`);
reject(err);
})
})
}
private loadImage(name: string) {
setTimeout(async () => {
let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
this.imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await this.imageSource.createPixelMap();
}, 100)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/core-vision-skeleton-detection-V14
爬取时间: 2025-04-30 04:24:44
来源: Huawei Developer
适用场景
人体骨骼关键点检测，主要检测人体的一些关键点，通过关键点描述人体骨骼信息。具体应用主要集中在智能视频监控，病人监护系统，人机交互，虚拟现实，人体动画，智能家居，智能安防，运动员辅助训练等等。
支持17个关键点的识别，具体为鼻子，左右眼，左右耳，左右肩，左右肘、左右手腕、左右髋、左右膝、左右脚踝。
约束与限制
该能力当前不支持模拟器。
详细限制请参考约束与限制
开发步骤
1.
```typescript
import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.
```typescript
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库，获取图片资源
this.selectImage();
})
```
3.
```typescript
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, 'skeletonDetectSample', "Failed to defined uri.");
}
this.loadImage(uri)
}
private openPhoto(): Promise<string> {
return new Promise<string>((resolve, reject) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
}).then(res => {
resolve(res.photoUris[0])
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'skeletonDetectSample', `Failed to get photo image uri. code：${err.code}，message：${err.message}`);
reject('')
})
})
}
private loadImage(name: string) {
setTimeout(async () => {
let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
this.imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await this.imageSource.createPixelMap();
}, 100)
}
```
4.
```typescript
// 调用骨骼点识别接口
let request: visionBase.Request = {
inputData: { pixelMap: this.chooseImage }
};
let data: skeletonDetection.SkeletonDetectionResponse = await (await skeletonDetection.SkeletonDetector.create()).process(request);
```
5.
```typescript
let data: skeletonDetection.SkeletonDetectionResponse = await (await skeletonDetection.SkeletonDetector.create()).process(request);
let poseJson = JSON.stringify(data);
hilog.info(0x0000, 'skeletonDetectSample', `Succeeded in face detect：${poseJson}`);
this.dataValues = poseJson;
```
开发实例
```typescript
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
@Entry
@Component
struct Index {
private imageSource: image.ImageSource | undefined = undefined;
@State chooseImage: PixelMap | undefined = undefined
@State dataValues: string = ''
build() {
Column() {
Image(this.chooseImage)
.objectFit(ImageFit.Fill)
.height('60%')
Text(this.dataValues)
.copyOption(CopyOptions.LocalDevice)
.height('15%')
.margin(10)
.width('60%')
Button('选择图片')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(() => {
// 拉起图库
this.selectImage()
})
Button('开始骨骼点识别')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.alignSelf(ItemAlign.Center)
.width('80%')
.margin(10)
.onClick(async () => {
if(!this.chooseImage) {
hilog.error(0x0000, 'skeletonDetectSample', `Failed to choose image. chooseImage: ${this.chooseImage}`);
return;
}
// 调用骨骼点识别接口
let request: visionBase.Request = {
inputData: { pixelMap: this.chooseImage }
};
let data: skeletonDetection.SkeletonDetectionResponse = await (await skeletonDetection.SkeletonDetector.create()).process(request);
let poseJson = JSON.stringify(data);
hilog.info(0x0000, 'skeletonDetectSample', `Succeeded in face detect：${poseJson}`);
this.dataValues = poseJson;
})
}
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
private async selectImage() {
let uri = await this.openPhoto()
if (uri === undefined) {
hilog.error(0x0000, 'skeletonDetectSample', "Failed to defined uri.");
}
this.loadImage(uri)
}
private openPhoto(): Promise<string> {
return new Promise<string>((resolve, reject) => {
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
}).then(res => {
resolve(res.photoUris[0])
}).catch((err: BusinessError) => {
hilog.error(0x0000, 'skeletonDetectSample', `Failed to get photo image uri. code：${err.code}，message：${err.message}`);
reject('')
})
})
}
private loadImage(name: string) {
setTimeout(async () => {
let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
this.imageSource = image.createImageSource(fileSource.fd);
this.chooseImage = await this.imageSource.createPixelMap();
}, 100)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiai-foundation-kit-guide-V14
爬取时间: 2025-04-30 04:24:57
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-introduction-V14
爬取时间: 2025-04-30 04:25:10
来源: Huawei Developer
使用HiAI Foundation Kit将人工智能能力集成到您的鸿蒙应用中。HiAI Foundation Kit是面向麒麟硬件平台为各种人工智能模型和算法提供统一的接入和运行环境。您的应用程序使用HiAI Foundation Kit的API和用户数据，在设备端实现智能推理、模型训练以及模型优化等操作，充分发挥设备的本地智能处理能力。
模型是将人工智能算法应用于大量训练数据后得到的结果。您可以使用模型依据新的输入数据进行智能推理和预测。模型能够完成许多用常规代码实现起来难度较大或效率较低的复杂任务。例如，你可以训练模型对图像进行语义分割，识别图像中的不同物体类别并精确划分其区域或者对语音数据进行处理，实现语音唤醒、语音识别以及语音合成等功能。
您可以使用华为昇腾提供的CANN开发平台进行模型的构建和训练。将CANN上训练好的模型转换为适合HiAI Foundation Kit的模型格式，以便集成到您的应用中。此外，您也可以基于其他开源或自研的机器学习框架进行模型开发，然后借助HiAI Foundation Kit提供的工具链将模型适配到鸿蒙生态中。
HiAI Foundation Kit通过协同调度设备的NPU（神经网络处理单元）、 CPU等硬件资源，实现高效的设备端智能计算性能优化。在提升计算效率的同时，尽可能降低对内存和电量的消耗。在设备端直接运行模型，减少了对网络的依赖，不仅保障了用户数据的隐私安全，还使应用程序在各种网络环境下都能保持快速响应，为用户提供流畅的智能交互体验。
HiAI Foundation Kit构建在底层的硬件驱动和优化的计算库之上，面向华为自研的达芬奇架构NPU的计算核心，与云侧昇腾芯片统一支持Ascend C自定义算子编程语言和相关工具链，确保开发者面向NPU的开发优化可以一次开发、多端运行。
HiAI Foundation Kit是鸿蒙智能生态的重要基石，为众多领域的智能应用提供核心支撑。例如：支持图像视觉相关的Core Vision Kit、用于自然语言处理的Natural Language Kit等AI计算加速能力，同时支持鸿蒙的MindSpore Lite Kit、Neural Network Runtime Kit，三方的MNN、PaddleLite等推理框架能力，共同打造丰富的智能应用场景。
场景
模型优化
模型转换
端侧部署
单算子
在三方应用框架加载其原始模型阶段，根据算子的输入、输出、权重信息等参数创建相应的单算子执行器对象并完成加载。三方应用框架执行模型推理时，在其中算子计算过程中调用单算子推理接口，完成算子计算。
基本概念
在进行HiAI Foundation开发前，开发者应了解以下基本概念：
-  NPU（Neural-network Processing Unit，神经网络处理器）是一种专门用于进行深度学习计算的芯片。
-  深度学习算法由一个个计算单元组成，我们称这些计算单元为算子（Operator，简称OP）。
-  异构计算（Heterogeneous Computing），又译异质运算，主要是指使用不同类型指令集或体系架构的计算单元组成系统的计算方式。HiAI Foundation使用到的计算单元类别包括CPU、NPU等。
-  AIPP是针对AI推理的输入数据进行预处理的模块。HiAI模型推理一般需要标准化输入数据格式，而一般模型推理场景数据是一张图片，在格式上存在多样性，AIPP可实现不同格式图片数据到NPU标准输入数据格式的转换。对已训练好的模型，不用重新训练匹配推理计算平台需要的数据格式，而只通过AIPP参数配置或者在软件上调用AIPP接口即可完成适配。由于AIPP硬件专用，可以获得较好的推理性能收益，又可以称为“硬件图像预处理”。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-preparations-V14
爬取时间: 2025-04-30 04:25:24
来源: Huawei Developer
环境准备
下载Tools
| Tools名称  | Tools说明  | Tools下载  | SHA256校验码  |
| --- | --- | --- | --- |
| 轻量化工具 包名：tools_dopt  | 对原始模型进行轻量化，以减少模型体积及加快模型推理速度。  | DDK_tools_5.0.1.0 next  | 3a7190aa56cff27f1135c4892ee57cfac955a820d150924a8a3fa9333dc85a18  |
| OMG工具 包名：tools_omg  | 模型转换工具。  |
Tools名称
Tools说明
Tools下载
SHA256校验码
轻量化工具
包名：tools_dopt
对原始模型进行轻量化，以减少模型体积及加快模型推理速度。
DDK_tools_5.0.1.0 next
3a7190aa56cff27f1135c4892ee57cfac955a820d150924a8a3fa9333dc85a18
OMG工具
包名：tools_omg
模型转换工具。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-model-optimization-V14
爬取时间: 2025-04-30 04:25:37
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-model-zoo-V14
爬取时间: 2025-04-30 04:25:51
来源: Huawei Developer
概述
Model Zoo提供了可直接调用的硬件最优模型库，集成图片分类、物体检测、语义分割、超分等典型场景的网络模型，包含HiAI性能调优使用指导、性能友好模型结构和推荐指数。帮助开发者快速了解算子的参数取值如何在硬件上获得更好的性能和能效收益，以及如何优化模型结构可以实现高性能与低功耗。
Model Zoo模型下载
Model Zoo中模型的名称、性能、模型下载信息如下表所示。模型下载中的.caffemodel、.pb、.onnx是原始浮点模型文件，通过参考对应论文来实现。.om是标准IR算子构建的OM模型文件，其中quant8_8.om是量化生成的OM模型文件，所有模型可通过Netron工具可视化。
| 场景  | 网络模型（单batch）  | 浮点性能[1]（耗时ms）  | 量化性能[1]（耗时ms）  | 模型下载  | SHA256校验码  | 参考[2]  |
| --- | --- | --- | --- | --- | --- | --- |
| 图片分类  | Alexnet  | 9.92  | 4.49  | CAFFE&OM  | 7b01980acf0d16dadc6c9c326cdf757d2166928ae49cfd4091df154a5c512640  | 论文&实现  |
| Resnet18  | 2.63  | 1.24  | CAFFE&OM  | 4aa7caaa112f5280cb5c0ab5eed6edf84a16fe9a0b92b9ee333a808c9f07e886  | 论文&实现  |
| Vgg16  | 16.56  | 8.55  | TF&OM  | f9193765889077e5997ddc8c1e75a563c8a1205e613da9634d3d83277962dd42  | 论文&实现  |
| Vgg19  | 18.34  | 8.73  | TF&OM  | d19f363602740ff5859380c40ca6f0bed0cb3744f469873cdf862c71c7007a94  | 论文&实现  |
| Resnet50  | 5.15  | 3.54  | TF&OM  | 6dedf4b5c3bfdaf70410236f1f73d942a5231f217e18c51918ba39b3b740b2df  | 论文&实现  |
| Inception_v3  | 6.56  | 3.76  | TF&OM  | d06c88a79acd19b10d5f7eddaae6aba3c02372cfdb036296b845aa3a9ccf46be  | 论文&实现  |
| Inception_v4  | 11.90  | 7.29  | TF&OM  | e042f489e6915eb6de5daa4b3200462e76f1bedca7147e2a19e8311a4b05afde  | 论文&实现  |
| Inception_Resnet_v2  | 15.91  | 5.59  | TF&OM  | 229164e49753126357f4a587694ca925afa60d1bfec184dba00085d69b5fc47b  | 论文&实现  |
| Mobilenet_v1  | 2.16  | 0.52  | TF&OM  | 864ef1d651e7f2cb9de69ce34d81e40783bdac47069b6db22aefb6f4ae17f24b  | 论文&实现  |
| Mobilenet_v2  | 2.49  | 1.18  | TF&OM  | 362c0169917122e45f4c5aed69ad3b9c8509b51a0531e6912360eff6c8b81cbc  | 论文&实现  |
| Mobilenet_v2_1.4  | 3.16  | 1.67  | TF&OM  | 8f1a05a83e813fac16e958ad5436569fe83f75f88137819d52ce2e268ad04126  | 论文&实现  |
| Mobilenet_v3_Large  | 3.29  | 2.33  | TF&OM  | 086640ff192629b6dba33d905ddb0925d612e395703948c6c7221f2e4126b85d  | 论文&实现  |
| Googlenet  | 34.69  | 1.64  | ONNX&OM  | 97ef0325be2c3b8824a903abaeea943260d2f349da63d193168c96eff735ad0e  | 论文&实现  |
| Squeezenet_v1  | 2.13  | 1.24  | ONNX&OM  | e20be44bdaa30b9fa4a22ef876c1e7bd88db49b5d063992ef1595b34d3544997  | 论文&实现  |
| 物体检测  | SSD_mobilenetv2_voc  | 5.02  | 2.84  | CAFFE&OM  | 1d273130a07a6f888f6df1088b478049da9a961a3dbeaca7bfa92e616f0f01e9  | 论文1&实现1、论文2&实现2  |
| Yolo_v5  | 4.74  | 4.33  | ONNX&OM  | 83a205d70fcd9b31c13530da0b8752a6976b125b02ac07091fd088f58cd5a80f  | 论文&实现  |
| 语义分割  | FCN  | 131.23  | 62.76  | CAFFE&OM  | 0cd87a51c1ea978a68e9cd4790106e99d910f78d5e68ec06e2bdd637aae5a73c  | 论文&实现  |
| DeepLab_v3  | 17.40  | 13.87  | TF&OM  | 381f830f6b0154bf086dbc5b15575465a34c1b3d233a6d27bc417077832697c7  | 论文&实现  |
| 超分  | VDSR  | 17.71  | 10.67  | CAFFE&OM  | bf5a699ea55b2d2e42ac40884f2697d807b5b3f37e655ecb342e873c6ba6b844  | 论文&实现  |
| FSRCNN  | 17.24  | 17.02  | TF&OM  | 03775c806d8d166fd29753ea8eaa3db377246fa469487b7e161a9e405a6ffa1c  | 论文&实现  |
场景
网络模型（单batch）
浮点性能[1]（耗时ms）
量化性能[1]（耗时ms）
模型下载
SHA256校验码
参考[2]
图片分类
Alexnet
9.92
4.49
CAFFE&OM
7b01980acf0d16dadc6c9c326cdf757d2166928ae49cfd4091df154a5c512640
论文&实现
Resnet18
2.63
1.24
CAFFE&OM
4aa7caaa112f5280cb5c0ab5eed6edf84a16fe9a0b92b9ee333a808c9f07e886
论文&实现
Vgg16
16.56
8.55
TF&OM
f9193765889077e5997ddc8c1e75a563c8a1205e613da9634d3d83277962dd42
论文&实现
Vgg19
18.34
8.73
TF&OM
d19f363602740ff5859380c40ca6f0bed0cb3744f469873cdf862c71c7007a94
论文&实现
Resnet50
5.15
3.54
TF&OM
6dedf4b5c3bfdaf70410236f1f73d942a5231f217e18c51918ba39b3b740b2df
论文&实现
Inception_v3
6.56
3.76
TF&OM
d06c88a79acd19b10d5f7eddaae6aba3c02372cfdb036296b845aa3a9ccf46be
论文&实现
Inception_v4
11.90
7.29
TF&OM
e042f489e6915eb6de5daa4b3200462e76f1bedca7147e2a19e8311a4b05afde
论文&实现
Inception_Resnet_v2
15.91
5.59
TF&OM
229164e49753126357f4a587694ca925afa60d1bfec184dba00085d69b5fc47b
论文&实现
Mobilenet_v1
2.16
0.52
TF&OM
864ef1d651e7f2cb9de69ce34d81e40783bdac47069b6db22aefb6f4ae17f24b
论文&实现
Mobilenet_v2
2.49
1.18
TF&OM
362c0169917122e45f4c5aed69ad3b9c8509b51a0531e6912360eff6c8b81cbc
论文&实现
Mobilenet_v2_1.4
3.16
1.67
TF&OM
8f1a05a83e813fac16e958ad5436569fe83f75f88137819d52ce2e268ad04126
论文&实现
Mobilenet_v3_Large
3.29
2.33
TF&OM
086640ff192629b6dba33d905ddb0925d612e395703948c6c7221f2e4126b85d
论文&实现
Googlenet
34.69
1.64
ONNX&OM
97ef0325be2c3b8824a903abaeea943260d2f349da63d193168c96eff735ad0e
论文&实现
Squeezenet_v1
2.13
1.24
ONNX&OM
e20be44bdaa30b9fa4a22ef876c1e7bd88db49b5d063992ef1595b34d3544997
论文&实现
物体检测
SSD_mobilenetv2_voc
5.02
2.84
CAFFE&OM
1d273130a07a6f888f6df1088b478049da9a961a3dbeaca7bfa92e616f0f01e9
论文1&实现1、论文2&实现2
Yolo_v5
4.74
4.33
ONNX&OM
83a205d70fcd9b31c13530da0b8752a6976b125b02ac07091fd088f58cd5a80f
论文&实现
语义分割
FCN
131.23
62.76
CAFFE&OM
0cd87a51c1ea978a68e9cd4790106e99d910f78d5e68ec06e2bdd637aae5a73c
论文&实现
DeepLab_v3
17.40
13.87
TF&OM
381f830f6b0154bf086dbc5b15575465a34c1b3d233a6d27bc417077832697c7
论文&实现
超分
VDSR
17.71
10.67
CAFFE&OM
bf5a699ea55b2d2e42ac40884f2697d807b5b3f37e655ecb342e873c6ba6b844
论文&实现
FSRCNN
17.24
17.02
TF&OM
03775c806d8d166fd29753ea8eaa3db377246fa469487b7e161a9e405a6ffa1c
论文&实现
除Model Zoo中推荐的网络模型，还可以构建自定义的网络模型。性能优势的算子和计算结构如下。
HiAI算子性能指导
从易用性角度上来说，提供的算子功能不存在限制，但是从性能的使用角度上来说，是基于算子实现方式给出对应的性能使用指导。
NN算子
| IR算子  | 性能使用指导  | 推荐使用指数  |
| --- | --- | --- |
| Activation  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| HardSwish  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| PRelu  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| BNInference  | 当前性能硬件最优。 Conv(depthwise)+Bn组合使用时，会进行图融合优化抵消。  | ☆☆☆☆☆  |
| Convolution  | 当Cin和Cout都是16的倍数时性能最优。  | ☆☆☆☆☆  |
| QuantizedConvolution  | 当Cin和Cout都是32的倍数时性能最优。  | ☆☆☆☆☆  |
| ConvTranspose  | 当Cin和Cout都是16的倍数时性能最优。 当前针对kernel 1*1，2*2，3*3，8*8优化性能最优。  | ☆☆☆☆☆  |
| BiasAdd  | 当前性能硬件最优。 Conv(depthwise)+BiasAdd组合使用时，会进行图融合优化抵消。  | ☆☆☆☆☆  |
| Eltwise  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| LRN  | 当前性能硬件较优。 计算过程中计算均值方差，计算量较大，性能差于batchNorm。主要用于图像增强，对精度计算较敏感，NPU使用FP16计算存在精度风险。  | ☆☆☆  |
| ConvolutionDepthwise  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| QuantizedConvolutionDepthwise  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| FullyConnection  | 性能受DDR带宽限制，非算力受限算子，算法设计时合理配置权重大小。  | ☆☆☆☆☆  |
| QuantizedFullyConnection  | 性能受DDR带宽限制，非算力受限算子，算法设计时合理配置权重大小。  | ☆☆☆☆☆  |
| PoolingD  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Scale  | 当前性能硬件最优。 Conv(depthwise)+Scale组合使用时，会进行图融合优化抵消。  | ☆☆☆☆☆  |
| ShuffleChannel  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| ShuffleChannelV2  | 为了适配支持ANN场景算子，性能较差，仅支持功能。  | ☆  |
| Softmax  | 当前性能硬件最优。 4维输入，axis=1，基于C通道做softmax时性能最优。  | ☆☆☆☆☆  |
| TopK  | 为了适配支持ANN场景算子，性能较差，仅支持功能。  | ☆  |
| LogSoftmax  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Rank  | shape推导类算子，模型构建时即可抵消。  | ☆☆☆☆☆  |
| ScatterNd  | 非规则数据搬移，性能较差，不建议模型过多使用。  | ☆☆☆  |
| LogicalXor  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Threshold  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| AxisAlignedBboxTransform  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Normalize  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| SVDF  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| ReduceMean  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| LayerNorm  | 当前性能硬件最优。 计算过程中计算均值方差，计算量较大，性能差于batchNorm。主要用于图像增强，对精度计算较敏感，NPU使用FP16计算存在精度风险。  | ☆☆☆  |
| InstanceNorm  | 当前性能硬件较优。 计算过程中计算均值方差，计算量较大，性能差于batchNorm。主要用于图像增强，对精度计算较敏感，NPU使用FP16计算存在精度风险。  | ☆☆☆  |
| PriorBox  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| LSTM  | 当前性能硬件较优，功能支持较窄。  | ☆☆☆☆  |
IR算子
性能使用指导
推荐使用指数
Activation
当前性能硬件最优。
☆☆☆☆☆
HardSwish
当前性能硬件最优。
☆☆☆☆☆
PRelu
当前性能硬件最优。
☆☆☆☆☆
BNInference
当前性能硬件最优。
Conv(depthwise)+Bn组合使用时，会进行图融合优化抵消。
☆☆☆☆☆
Convolution
当Cin和Cout都是16的倍数时性能最优。
☆☆☆☆☆
QuantizedConvolution
当Cin和Cout都是32的倍数时性能最优。
☆☆☆☆☆
ConvTranspose
☆☆☆☆☆
BiasAdd
当前性能硬件最优。
Conv(depthwise)+BiasAdd组合使用时，会进行图融合优化抵消。
☆☆☆☆☆
Eltwise
当前性能硬件最优。
☆☆☆☆☆
LRN
当前性能硬件较优。
☆☆☆
ConvolutionDepthwise
当前性能硬件最优。
☆☆☆☆☆
QuantizedConvolutionDepthwise
当前性能硬件最优。
☆☆☆☆☆
FullyConnection
性能受DDR带宽限制，非算力受限算子，算法设计时合理配置权重大小。
☆☆☆☆☆
QuantizedFullyConnection
性能受DDR带宽限制，非算力受限算子，算法设计时合理配置权重大小。
☆☆☆☆☆
PoolingD
当前性能硬件最优。
☆☆☆☆☆
Scale
当前性能硬件最优。
Conv(depthwise)+Scale组合使用时，会进行图融合优化抵消。
☆☆☆☆☆
ShuffleChannel
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
ShuffleChannelV2
为了适配支持ANN场景算子，性能较差，仅支持功能。
☆
Softmax
当前性能硬件最优。
4维输入，axis=1，基于C通道做softmax时性能最优。
☆☆☆☆☆
TopK
为了适配支持ANN场景算子，性能较差，仅支持功能。
☆
LogSoftmax
当前性能硬件最优。
☆☆☆☆☆
Rank
shape推导类算子，模型构建时即可抵消。
☆☆☆☆☆
ScatterNd
非规则数据搬移，性能较差，不建议模型过多使用。
☆☆☆
LogicalXor
当前性能硬件最优。
☆☆☆☆☆
Threshold
当前性能硬件最优。
☆☆☆☆☆
AxisAlignedBboxTransform
当前性能硬件最优。
☆☆☆☆☆
Normalize
当前性能硬件最优。
☆☆☆☆☆
SVDF
当前性能硬件最优。
☆☆☆☆☆
ReduceMean
当前性能硬件最优。
☆☆☆☆☆
LayerNorm
当前性能硬件最优。
☆☆☆
InstanceNorm
当前性能硬件较优。
☆☆☆
PriorBox
当前性能硬件最优。
☆☆☆☆☆
LSTM
当前性能硬件较优，功能支持较窄。
☆☆☆☆
Math算子
| IR算子  | 性能使用指导  | 推荐使用指数  |
| --- | --- | --- |
| Add  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Mul  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Expm1  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Ceil  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Sin  | 性能较差。  | ☆  |
| Cos  | 性能较差。  | ☆  |
| Floor  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Log1p  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| LogicalAnd  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| LogicalNot  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Maximum  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| Minimum  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| Equal  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Reciprocal  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Sqrt  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Square  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| CastT  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| Sign  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Exp  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| FloorMod  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| GreaterEqual  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Greater  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Less  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| MatMul  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| RealDiv  | 性能较差，建议等效成mul或者Reciprocal+mul。  | ☆  |
| Rint  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| Round  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| Rsqrt  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| Sub  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Range  | 模型构建时最优。  | ☆☆☆☆☆  |
| Acos  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Asin  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Log  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| LogicalOr  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Neg  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| ReduceProdD  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| ReduceSum  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Tan  | 性能较差。  | ☆  |
| Power  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Pow  | 性能较差。  | ☆  |
| ArgMaxExt2  | 当前性能硬件最优。  | ☆☆☆☆  |
| FloorDiv  | 性能较差，不建议使用。  | ☆  |
| NotEqual  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| LessEqual  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| SquaredDifference  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Atan  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| BatchMatMul  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| ClipByValue  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| L2Normalize  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| ReduceMax  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
| ReduceMin  | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。  | ☆  |
IR算子
性能使用指导
推荐使用指数
Add
当前性能硬件最优。
☆☆☆☆☆
Mul
当前性能硬件最优。
☆☆☆☆☆
Expm1
当前性能硬件最优。
☆☆☆☆☆
Ceil
当前性能硬件最优。
☆☆☆☆☆
Sin
性能较差。
☆
Cos
性能较差。
☆
Floor
当前性能硬件最优。
☆☆☆☆☆
Log1p
当前性能硬件最优。
☆☆☆☆☆
LogicalAnd
当前性能硬件最优。
☆☆☆☆☆
LogicalNot
当前性能硬件最优。
☆☆☆☆☆
Maximum
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
Minimum
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
Equal
当前性能硬件最优。
☆☆☆☆☆
Reciprocal
当前性能硬件最优。
☆☆☆☆☆
Sqrt
当前性能硬件最优。
☆☆☆☆☆
Square
当前性能硬件最优。
☆☆☆☆☆
CastT
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
Sign
当前性能硬件最优。
☆☆☆☆☆
Exp
当前性能硬件最优。
☆☆☆☆☆
FloorMod
当前性能硬件最优。
☆☆☆☆☆
GreaterEqual
当前性能硬件最优。
☆☆☆☆☆
Greater
当前性能硬件最优。
☆☆☆☆☆
Less
当前性能硬件最优。
☆☆☆☆☆
MatMul
当前性能硬件最优。
☆☆☆☆☆
RealDiv
性能较差，建议等效成mul或者Reciprocal+mul。
☆
Rint
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
Round
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
Rsqrt
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
Sub
当前性能硬件最优。
☆☆☆☆☆
Range
模型构建时最优。
☆☆☆☆☆
Acos
当前性能硬件最优。
☆☆☆☆☆
Asin
当前性能硬件最优。
☆☆☆☆☆
Log
当前性能硬件最优。
☆☆☆☆☆
LogicalOr
当前性能硬件最优。
☆☆☆☆☆
Neg
当前性能硬件最优。
☆☆☆☆☆
ReduceProdD
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
ReduceSum
当前性能硬件最优。
☆☆☆☆☆
Tan
性能较差。
☆
Power
当前性能硬件最优。
☆☆☆☆☆
Pow
性能较差。
☆
ArgMaxExt2
当前性能硬件最优。
☆☆☆☆
FloorDiv
性能较差，不建议使用。
☆
NotEqual
当前性能硬件最优。
☆☆☆☆☆
LessEqual
当前性能硬件最优。
☆☆☆☆☆
SquaredDifference
当前性能硬件最优。
☆☆☆☆☆
Atan
当前性能硬件最优。
☆☆☆☆☆
BatchMatMul
当前性能硬件最优。
☆☆☆☆☆
ClipByValue
当前性能硬件最优。
☆☆☆☆☆
L2Normalize
当前性能硬件最优。
☆☆☆☆☆
ReduceMax
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
ReduceMin
kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。
☆
Array算子
| IR算子  | 性能使用指导  | 推荐使用指数  |
| --- | --- | --- |
| ConcatD  | 当前性能硬件最优。 当Cin是16的倍数且Cout是16的倍数时，做图融合抵消，性能最优。  | ☆☆☆☆☆  |
| FakeQuantWithMinMaxVars  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Reshape  | 当前性能硬件最优。 有些场景算子会被融合抵消掉。  | ☆☆☆☆☆  |
| SplitD  | 当前性能硬件最优。 当Cin是16的倍数且Cout是16的倍数时，做图融合抵消，性能最优。  | ☆☆☆☆☆  |
| SplitV  | 由于是乱序的数据重排，性能较差。  | ☆  |
| Unpack  | 由于是乱序的数据重排，性能较差。  | ☆  |
| Flatten  | 由于是乱序的数据重排，性能较差。  | ☆  |
| Slice  | 由于是乱序的数据重排，性能较差。  | ☆  |
| ExpandDims  | shape推导类算子，模型构建时即可抵消。  | ☆☆☆☆☆  |
| GatherV2D  | 由于是乱序的数据重排，性能较差。  | ☆  |
| GatherNd  | 由于是乱序的数据重排，性能较差。  | ☆  |
| Pack  | 由于是乱序的数据重排，性能较差。  | ☆  |
| SpaceToDepth  | 由于是乱序的数据重排，性能较差。  | ☆  |
| DepthToSpace  | 由于是乱序的数据重排，大部分场景性能较差。 针对4宫格场景（Cin=4，block=1）有特殊优化，性能较优。  | ☆☆  |
| StridedSlice  | 由于是乱序的数据重排，性能较差。  | ☆  |
| SpaceToBatchND  | 由于是乱序的数据重排，性能较差。  | ☆  |
| BatchToSpaceND  | 由于是乱序的数据重排，性能较差。  | ☆  |
| Tile  | 由于是乱序的数据重排，性能较差。  | ☆  |
| Size  | shape推导类算子，模型构建时即可抵消。  | ☆☆☆☆☆  |
| Fill  | 由于是乱序的数据重排，性能较差。  | ☆  |
| Select  | 仅支持功能。  | ☆☆  |
| PadV2  | 针对HW方向补0的场景性能较优。 其他场景由于乱序的数据重排，性能较差。  | ☆☆☆  |
| Squeeze  | shape推导类算子，模型构建时即可抵消。  | ☆☆☆☆☆  |
| Pad  | 针对HW方向补0的场景性能较优。 其他场景由于乱序的数据重排，性能较差。  | ☆☆☆  |
| MirrorPad  | 其他场景由于乱序的数据重排，性能较差。  | ☆  |
| OneHot  | 其他场景由于乱序的数据重排，性能较差。  | ☆  |
| Shape  | shape推导类算子，模型构建时即可抵消。  | ☆☆☆☆☆  |
| Dequantize  | 当前性能硬件最优。  | ☆☆☆☆☆  |
| Quantize  | 当前性能硬件最优。  | ☆☆☆☆☆  |
IR算子
性能使用指导
推荐使用指数
ConcatD
当前性能硬件最优。
当Cin是16的倍数且Cout是16的倍数时，做图融合抵消，性能最优。
☆☆☆☆☆
FakeQuantWithMinMaxVars
当前性能硬件最优。
☆☆☆☆☆
Reshape
当前性能硬件最优。
有些场景算子会被融合抵消掉。
☆☆☆☆☆
SplitD
当前性能硬件最优。
当Cin是16的倍数且Cout是16的倍数时，做图融合抵消，性能最优。
☆☆☆☆☆
SplitV
由于是乱序的数据重排，性能较差。
☆
Unpack
由于是乱序的数据重排，性能较差。
☆
Flatten
由于是乱序的数据重排，性能较差。
☆
Slice
由于是乱序的数据重排，性能较差。
☆
ExpandDims
shape推导类算子，模型构建时即可抵消。
☆☆☆☆☆
GatherV2D
由于是乱序的数据重排，性能较差。
☆
GatherNd
由于是乱序的数据重排，性能较差。
☆
Pack
由于是乱序的数据重排，性能较差。
☆
SpaceToDepth
由于是乱序的数据重排，性能较差。
☆
DepthToSpace
由于是乱序的数据重排，大部分场景性能较差。
针对4宫格场景（Cin=4，block=1）有特殊优化，性能较优。
☆☆
StridedSlice
由于是乱序的数据重排，性能较差。
☆
SpaceToBatchND
由于是乱序的数据重排，性能较差。
☆
BatchToSpaceND
由于是乱序的数据重排，性能较差。
☆
Tile
由于是乱序的数据重排，性能较差。
☆
Size
shape推导类算子，模型构建时即可抵消。
☆☆☆☆☆
Fill
由于是乱序的数据重排，性能较差。
☆
Select
仅支持功能。
☆☆
PadV2
针对HW方向补0的场景性能较优。
其他场景由于乱序的数据重排，性能较差。
☆☆☆
Squeeze
shape推导类算子，模型构建时即可抵消。
☆☆☆☆☆
Pad
针对HW方向补0的场景性能较优。
其他场景由于乱序的数据重排，性能较差。
☆☆☆
MirrorPad
其他场景由于乱序的数据重排，性能较差。
☆
OneHot
其他场景由于乱序的数据重排，性能较差。
☆
Shape
shape推导类算子，模型构建时即可抵消。
☆☆☆☆☆
Dequantize
当前性能硬件最优。
☆☆☆☆☆
Quantize
当前性能硬件最优。
☆☆☆☆☆
Detection算子
| IR算子  | 性能使用指导  | 推荐使用指数  |
| --- | --- | --- |
| Permute  | 由于乱序的数据重排，虽然做了相关优化，但是硬件不适合过多此类操作。  | ☆☆☆  |
| SSDDetectionOutput  | 当前性能最优。  | ☆☆☆☆☆  |
IR算子
性能使用指导
推荐使用指数
Permute
由于乱序的数据重排，虽然做了相关优化，但是硬件不适合过多此类操作。
☆☆☆
SSDDetectionOutput
当前性能最优。
☆☆☆☆☆
Image算子
| IR算子  | 性能使用指导  | 推荐使用指数  |
| --- | --- | --- |
| ImageData DynamicImageData ImageCrop ImageChannelSwap ImageColorSpaceConvertion ImageResize ImageDataTypeConversion ImagePadding  | AIPP相关图形处理算子，性能硬件最优。  | ☆☆☆☆☆  |
| CropAndResize  | 仅功能支持，性能较差。  | ☆  |
| ResizeBilinear ResizeBilinearV2 Interp  | 大部分场景性能硬件最优，个别场景待优化。  | ☆☆☆☆☆  |
| ResizeNearestNeighbor Upsample  | 大部分场景性能硬件最优，个别场景待优化。  | ☆☆☆☆☆  |
| Crop  | 仅功能支持，性能较差。  | ☆  |
| NonMaxSuppressionV3D  | 仅功能支持，性能较差。  | ☆  |
IR算子
性能使用指导
推荐使用指数
ImageData
DynamicImageData
ImageCrop
ImageChannelSwap
ImageColorSpaceConvertion
ImageResize
ImageDataTypeConversion
ImagePadding
AIPP相关图形处理算子，性能硬件最优。
☆☆☆☆☆
CropAndResize
仅功能支持，性能较差。
☆
ResizeBilinear
ResizeBilinearV2
Interp
大部分场景性能硬件最优，个别场景待优化。
☆☆☆☆☆
ResizeNearestNeighbor
Upsample
大部分场景性能硬件最优，个别场景待优化。
☆☆☆☆☆
Crop
仅功能支持，性能较差。
☆
NonMaxSuppressionV3D
仅功能支持，性能较差。
☆
性能友好计算结构
| 应用场景  | 网络类型  | 推荐指数  | 推荐说明  |
| --- | --- | --- | --- |
| 分类网络  | AlexNet  | ☆☆☆☆  | 全连接层权重较大，推理过程带宽受限，可从Model Zoo中下载。  |
| VGG16  | ☆☆☆☆  | 全连接层权重较大，推理过程带宽受限，可从Model Zoo中下载。  |
| VGG19  | ☆☆☆  | 全连接层权重较大，推理过程带宽受限，可从Model Zoo中下载。  |
| ResNet18/34/50/101/152  | ☆☆☆☆☆  | 模型权重大小适中，硬件算力利用率接近100%，ResNet50可从Model Zoo下载。  |
| GoogleNet  | ☆☆☆☆  | 硬件算力利用率接近75%，可从Model Zoo中下载。  |
| InceptionV3  | ☆☆☆☆  | 硬件算力利用率接近85%，可从Model Zoo中下载。  |
| InceptionV4  | ☆☆☆☆  | 硬件算力利用率接近85%，可从Model Zoo中下载。  |
| Inception_Resnet_v2  | ☆☆☆☆  | 硬件算力利用率接近90%，可从Model Zoo中下载。  |
| Xception  | ☆☆☆☆  | 硬件算力利用率接近85%，可从Model Zoo中下载。  |
| MobileNet_v1  | ☆☆☆☆☆  | 模型权重大小适中，硬件算力利用率接近95%，可从Model Zoo中下载。  |
| MobileNet_v2  | ☆☆☆☆☆  | 模型权重大小适中，硬件算力利用率接近95%，可从Model Zoo中下载。  |
| MobileNet_v3  | ☆☆☆☆☆  | 模型权重大小适中，硬件算力利用率接近95%，可从Model Zoo中下载。  |
| SqueezeNet  | ☆☆☆☆☆  | 模型权重大小适中，硬件算力利用率接近95%，可从Model Zoo中下载。  |
| DenseNet  | ☆☆☆☆☆  | 模型权重大小适中，硬件算力利用率接近95%。  |
| ShuffleNet_v1 ShuffleNet_v2  | ☆  | 存在大量shuffleChannel操作，本身是内存搬移操作，非计算受限。 此网络为带宽受限网络，shuffleChannel仅支持功能，性能不保证较优。  |
| Resnext  | ☆☆☆☆  | 硬件算力利用率接近85%。  |
| EfficientNet  | ☆☆☆☆☆  | 模型权重大小适中，硬件算力利用率接近95%。  |
| SENet  | ☆☆☆☆  | 硬件算力利用率接近75%。  |
| 物体检测  | Faster_RCNN  | ☆☆☆☆☆  | 硬件算力利用率接近85%。  |
| SSD  | ☆☆☆☆  | 硬件算力利用率接近85%，当前仅支持通过omg流程生成。  |
| FPN  | ☆☆☆☆☆  | 硬件算力利用率接近90%，后处理不在模型中，由算法单独完成。  |
| 语义分割  | FCN  | ☆☆☆☆☆  | 硬件算力利用率接近85%，由于模型计算量较大，实际部署时要做参数裁剪，可从Model Zoo中下载 。  |
| DeeplabV3  | ☆☆☆  | 硬件算力利用率接近60%，可从Model Zoo中下载。  |
| Unet  | ☆☆☆  | 硬件算力利用率接近60%。  |
| MaskRcnn  | ☆☆  | 硬件算力利用率接近80%（仅限tf->om版本，IR对接方式不支持）。  |
| PSPNet  | ☆☆☆  | 不支持pyramid pooling算子，可以通过多个pool等效，性能一般。  |
| 超分  | VDSR  | ☆☆☆☆☆  | 硬件算力利用率接近85%，可以达到实时超分要求，可从Model Zoo中下载。  |
| FSRCNN  | ☆☆☆☆  | 硬件算力利用率接近70%，可以达到部分实时超分要求，可从Model Zoo中下载。  |
| SRCNN  | ☆☆☆☆  | 硬件算力利用率接近70%，可以达到部分实时超分要求。  |
| DnCNN  | ☆☆☆☆  | 硬件算力利用率接近65%，计算量较大，可以达到部分实时超分要求。  |
| DRCN  | ☆☆☆☆  | 硬件算力利用率接近65%，计算量较大，可以达到部分实时超分要求。  |
| DRRN  | ☆☆☆  | 硬件算力利用率接近60%，计算量较大，可以达到部分实时超分要求。  |
| EnhanceNet  | ☆☆☆  | 硬件算力利用率接近60%，计算量较大，可以达到部分实时超分要求。  |
| 语音语义  | RNN  | ☆☆  | 功能支持较为单一。  |
| LSTM  | ☆☆  | 功能支持较为单一。  |
| Transformer  | ☆☆☆☆  | 硬件算力利用率接近70%。  |
| Bert  | ☆☆☆☆  | 硬件算力利用率接近70%。  |
应用场景
网络类型
推荐指数
推荐说明
分类网络
AlexNet
☆☆☆☆
全连接层权重较大，推理过程带宽受限，可从Model Zoo中下载。
VGG16
☆☆☆☆
全连接层权重较大，推理过程带宽受限，可从Model Zoo中下载。
VGG19
☆☆☆
全连接层权重较大，推理过程带宽受限，可从Model Zoo中下载。
ResNet18/34/50/101/152
☆☆☆☆☆
模型权重大小适中，硬件算力利用率接近100%，ResNet50可从Model Zoo下载。
GoogleNet
☆☆☆☆
硬件算力利用率接近75%，可从Model Zoo中下载。
InceptionV3
☆☆☆☆
硬件算力利用率接近85%，可从Model Zoo中下载。
InceptionV4
☆☆☆☆
硬件算力利用率接近85%，可从Model Zoo中下载。
Inception_Resnet_v2
☆☆☆☆
硬件算力利用率接近90%，可从Model Zoo中下载。
Xception
☆☆☆☆
硬件算力利用率接近85%，可从Model Zoo中下载。
MobileNet_v1
☆☆☆☆☆
模型权重大小适中，硬件算力利用率接近95%，可从Model Zoo中下载。
MobileNet_v2
☆☆☆☆☆
模型权重大小适中，硬件算力利用率接近95%，可从Model Zoo中下载。
MobileNet_v3
☆☆☆☆☆
模型权重大小适中，硬件算力利用率接近95%，可从Model Zoo中下载。
SqueezeNet
☆☆☆☆☆
模型权重大小适中，硬件算力利用率接近95%，可从Model Zoo中下载。
DenseNet
☆☆☆☆☆
模型权重大小适中，硬件算力利用率接近95%。
ShuffleNet_v1
ShuffleNet_v2
☆
存在大量shuffleChannel操作，本身是内存搬移操作，非计算受限。
此网络为带宽受限网络，shuffleChannel仅支持功能，性能不保证较优。
Resnext
☆☆☆☆
硬件算力利用率接近85%。
EfficientNet
☆☆☆☆☆
模型权重大小适中，硬件算力利用率接近95%。
SENet
☆☆☆☆
硬件算力利用率接近75%。
物体检测
Faster_RCNN
☆☆☆☆☆
硬件算力利用率接近85%。
SSD
☆☆☆☆
硬件算力利用率接近85%，当前仅支持通过omg流程生成。
FPN
☆☆☆☆☆
硬件算力利用率接近90%，后处理不在模型中，由算法单独完成。
语义分割
FCN
☆☆☆☆☆
硬件算力利用率接近85%，由于模型计算量较大，实际部署时要做参数裁剪，可从Model Zoo中下载 。
DeeplabV3
☆☆☆
硬件算力利用率接近60%，可从Model Zoo中下载。
Unet
☆☆☆
硬件算力利用率接近60%。
MaskRcnn
☆☆
硬件算力利用率接近80%（仅限tf->om版本，IR对接方式不支持）。
PSPNet
☆☆☆
不支持pyramid pooling算子，可以通过多个pool等效，性能一般。
超分
VDSR
☆☆☆☆☆
硬件算力利用率接近85%，可以达到实时超分要求，可从Model Zoo中下载。
FSRCNN
☆☆☆☆
硬件算力利用率接近70%，可以达到部分实时超分要求，可从Model Zoo中下载。
SRCNN
☆☆☆☆
硬件算力利用率接近70%，可以达到部分实时超分要求。
DnCNN
☆☆☆☆
硬件算力利用率接近65%，计算量较大，可以达到部分实时超分要求。
DRCN
☆☆☆☆
硬件算力利用率接近65%，计算量较大，可以达到部分实时超分要求。
DRRN
☆☆☆
硬件算力利用率接近60%，计算量较大，可以达到部分实时超分要求。
EnhanceNet
☆☆☆
硬件算力利用率接近60%，计算量较大，可以达到部分实时超分要求。
语音语义
RNN
☆☆
功能支持较为单一。
LSTM
☆☆
功能支持较为单一。
Transformer
☆☆☆☆
硬件算力利用率接近70%。
Bert
☆☆☆☆
硬件算力利用率接近70%。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-lightweight-tool-instructions-V14
爬取时间: 2025-04-30 04:26:05
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-model-conversion-V14
爬取时间: 2025-04-30 04:26:18
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-offline-model-conversion-V14
爬取时间: 2025-04-30 04:26:32
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-overall-parameter-V14
爬取时间: 2025-04-30 04:26:46
来源: Huawei Developer
| 参数名称  | 参数描述  | 是否必选  | 默认值  |
| --- | --- | --- | --- |
| --h/help  | 显示帮助信息。  | 否  | 不涉及  |
| --mode  | 运行模式。 0：生成DaVinci模型。1：模型转json。json可查看模型结构的文本格式。 3：仅做预检，检查模型文件的内容是否合法。  | 否  | 0  |
| --model  | 原始框架模型文件路径。  | 是  | 不涉及  |
| --framework  | 原始框架类型。 0：Caffe。3：TensorFlow。5：ONNX。6：MindSpore。 说明当mode为1时，该参数可选，可以指定Caffe、TensorFlow、ONNX、MindSpore，不指定时默认为离线模型转json。当mode为0或3时，该参数必选，可以指定Caffe或TensorFlow或ONNX或MindSpore。   | 是  | 不涉及  |
| --weight  | 权值文件路径。当原始模型是Caffe时需要指定。当原始模型是其他框架时不需要指定。  | 否  | 不涉及  |
| --output  | 存放转换后的离线模型文件的路径（包含文件名），例如“out/caffe_resnet18”。转换后的模型文件，会自动以.om的后缀结尾。  | 是  | 不涉及  |
| --hiai_version  | 指定使用OMG的版本，当前支持：v300|v310|IR。  | 否  | IR  |
| --om  | 模型文件路径。当mode为1时必填。  | 否  | 不涉及  |
| --json  | 模型文件转换为json格式文件的路径。  | 否  | 不涉及  |
| --input_shape  | 输入数据的shape。 例如：“input_name1: n1, c1, h1, w1; input_name2: n2, c2, h2, w2”。input_name必须是转换前的网络模型中的节点名称。 当原始模型是ONNX时，input_name必须是模型转换前的网络模型中input算子的name。 说明当原始模型是ONNX，并且ONNX模型输入维度为动态时，此参数必须指定。当原始模型是TensorFlow，并且TensorFlow模型输入维度为动态时，此参数必须指定。   | 否  | 不涉及  |
| --input_format  | 输入数据格式：NCHW和NHWC。 说明当原始框架是Caffe时或ONNX或MindSpore时，此参数不生效。当原始框架是TensorFlow时，绝大多数场景不需要指定，如果转换时提示需要指定，根据实际情况指定。   | 否  | 不涉及  |
| --input_type  | 支持设定模型输入格式，支持指定为FP32、FP16、 INT32、UINT8等，包括多输入和单输入。具体是否能成功生成离线模型，取决于原始模型是否支持指定为该格式的输入。模型输入支持场景详见非AIPP场景设定输入类型支持情况和AIPP场景设定输入类型支持情况。 例如："input_name1:FP16;input_name2:UINT8"。 input_name必须是转换前的网络模型中的节点名称。 当原始模型是ONNX时，input_name必须是模型转换前的网络模型中input算子的name。  | 否  | FP32  |
| --input_fp16_nodes  | 不支持与--input_type同时设置。 指定数据类型为“fp16nchw”的输入节点名称。 例如：“node_name1;node_name2”。 说明当原始框架是ONNX或MindSpore时，此参数不生效。   | 否  | 不涉及  |
| --out_nodes  | 指定输出节点。 如果原始模型是TensorFlow或者Caffe，按照以下格式指定：“node_name1:0;node_name1:1;node_name2:0”。node_name必须是模型转换前的网络模型中的节点名称。同一个节点的输出从0开始，如果该节点有多个输出，依次往后累加。  如果原始模型是ONNX，按照以下格式指定：“tensor_name1;tensor_name2”。tensor_name必须是模型转换前的网络模型中的节点输出Tensor名称。   | 否  | 不涉及  |
| --output_type  | 支持设定模型的输出数据类型，支持指定为FP32、FP16、INT32、UINT8等，包括多输出和单输出。具体是否能成功生成离线模型，取决于原始模型是否支持指定为该类型的输出。模型输出支持场景详见非AIPP场景设定输入类型支持情况。 例如："output_name1：FP16；output_name2：UINT8"。 output_name必须是转换前的网络模型中的节点名称。 当原始框架是ONNX时，output_name可以是模型转换前的网络模型中output算子的name或者是用户指定out_nodes中所用到的tensor_name。  | 否  | FP32  |
| --is_output_fp16  | 不支持与--output_type同时设置。 标注输出的数据类型是否为“fp16 nchw”。 例如：false, true, false, true。 说明当原始框架是ONNX或MindSpore时，此参数不生效。   | 否  | False  |
| --stream_num  | 模型使用的stream数量，当前仅支持1。  | 否  | 1  |
| --check_report  | 预检结果保存文件路径。若不指定该路径，在模型转换失败或mode为3（仅做预检）时，将预检结果保存在当前路径下。  | 否  | 不涉及  |
| --net_format  | 指定网络算子优先选用的数据格式。 说明注：该参数现已不推荐使用，可通过网络推导得出。   | 否  | 不涉及  |
| --insert_op_conf  | AIPP配置文件路径。详情参见模型转换AIPP配置文件说明。  | 否  | 不涉及  |
| --op_name_map  | 算子映射配置文件路径。包含DetectionOutput网络时需要指定。 例如：不同的网络中DetectionOutput算子的功能不同，指定DetectionOutput到FSRDetectionOutput或者SSDDetectionOutput的映射。 说明算子映射配置文件的内容示例如下： DetectionOutput：SSDDetectionOutput。   | 否  | 不涉及  |
| --compress_conf  | 轻量化配置文件路径。该参数需与轻量化工具搭配使用，由轻量化工具自动生成。具体参见模型轻量化。  | 否  | 不涉及  |
| --weight_data_type  | 支持设定模型权值数据类型，支持指定为FP32或FP16。 该参数仅针对模型中权值数据类型为FP32时生效，根据设定将权值数据类型由FP32转为FP16存储或维持FP32不变。该参数默认值为FP16。 例如："weight_data_type:FP16"。 说明由于CPUCL不支持FP16的权重进行计算，如果模型需要兼容CPU计算库，需要指定该参数为FP32。   | 否  | FP16  |
| --weight_merge  | 离线模型权值归并开关，支持指定在离线模型生成时权值是否进行归并存储操作；该参数为true时，模型权值归并存储。该参数为false时，权值维持非归并存储方式，对性能无影响。该参数默认为true。  | 否  | True  |
| --use_origin_format  | 支持设定模型的输入输出和原始模型保持一致的format。 说明本参数仅支持基于yolo、inception的业务网络转换设置为true，其它网络转换使用默认值false。   | 否  | false  |
| --dynamic_dims  | 支持同一个原始模型生成能支持不同shape输入档位的Davinci模型，该参数指定可以变化的dim值。和--input_shape参数配合使用，在input_shape参数中可以变化的dim使用-1代替。 该参数中每一种可以变化的dims值使用分号分隔（也称为一档），如果一档中有多个维度，每个维度之间使用逗号分隔。举例： 动态batch--input_shape = "input_name1:-1,c,h,w" --dynamic_dims = "n1;n2;n3"  动态分辨率--input_shape = "input_name1:n,-1,-1,c" --dynamic_dims =  "h1,w1;h2,w2"  说明使用约束：支持可以变化的shape种类最多16种。   | 否  | 不涉及  |
参数名称
参数描述
是否必选
默认值
--h/help
显示帮助信息。
否
不涉及
--mode
运行模式。
否
0
--model
原始框架模型文件路径。
是
不涉及
--framework
原始框架类型。
是
不涉及
--weight
权值文件路径。当原始模型是Caffe时需要指定。当原始模型是其他框架时不需要指定。
否
不涉及
--output
存放转换后的离线模型文件的路径（包含文件名），例如“out/caffe_resnet18”。转换后的模型文件，会自动以.om的后缀结尾。
是
不涉及
--hiai_version
指定使用OMG的版本，当前支持：v300|v310|IR。
否
IR
--om
模型文件路径。当mode为1时必填。
否
不涉及
--json
模型文件转换为json格式文件的路径。
否
不涉及
--input_shape
输入数据的shape。
例如：“input_name1: n1, c1, h1, w1; input_name2: n2, c2, h2, w2”。input_name必须是转换前的网络模型中的节点名称。
当原始模型是ONNX时，input_name必须是模型转换前的网络模型中input算子的name。
否
不涉及
--input_format
输入数据格式：NCHW和NHWC。
否
不涉及
--input_type
支持设定模型输入格式，支持指定为FP32、FP16、 INT32、UINT8等，包括多输入和单输入。具体是否能成功生成离线模型，取决于原始模型是否支持指定为该格式的输入。模型输入支持场景详见非AIPP场景设定输入类型支持情况和AIPP场景设定输入类型支持情况。
例如："input_name1:FP16;input_name2:UINT8"。
input_name必须是转换前的网络模型中的节点名称。
当原始模型是ONNX时，input_name必须是模型转换前的网络模型中input算子的name。
否
FP32
--input_fp16_nodes
不支持与--input_type同时设置。
指定数据类型为“fp16nchw”的输入节点名称。
例如：“node_name1;node_name2”。
当原始框架是ONNX或MindSpore时，此参数不生效。
否
不涉及
--out_nodes
指定输出节点。
-  node_name必须是模型转换前的网络模型中的节点名称。同一个节点的输出从0开始，如果该节点有多个输出，依次往后累加。
-  tensor_name必须是模型转换前的网络模型中的节点输出Tensor名称。
否
不涉及
--output_type
支持设定模型的输出数据类型，支持指定为FP32、FP16、INT32、UINT8等，包括多输出和单输出。具体是否能成功生成离线模型，取决于原始模型是否支持指定为该类型的输出。模型输出支持场景详见非AIPP场景设定输入类型支持情况。
例如："output_name1：FP16；output_name2：UINT8"。
output_name必须是转换前的网络模型中的节点名称。
当原始框架是ONNX时，output_name可以是模型转换前的网络模型中output算子的name或者是用户指定out_nodes中所用到的tensor_name。
否
FP32
--is_output_fp16
不支持与--output_type同时设置。
标注输出的数据类型是否为“fp16 nchw”。
例如：false, true, false, true。
当原始框架是ONNX或MindSpore时，此参数不生效。
否
False
--stream_num
模型使用的stream数量，当前仅支持1。
否
1
--check_report
预检结果保存文件路径。若不指定该路径，在模型转换失败或mode为3（仅做预检）时，将预检结果保存在当前路径下。
否
不涉及
--net_format
指定网络算子优先选用的数据格式。
注：该参数现已不推荐使用，可通过网络推导得出。
否
不涉及
--insert_op_conf
AIPP配置文件路径。详情参见模型转换AIPP配置文件说明。
否
不涉及
--op_name_map
算子映射配置文件路径。包含DetectionOutput网络时需要指定。
例如：不同的网络中DetectionOutput算子的功能不同，指定DetectionOutput到FSRDetectionOutput或者SSDDetectionOutput的映射。
算子映射配置文件的内容示例如下：
DetectionOutput：SSDDetectionOutput。
否
不涉及
--compress_conf
轻量化配置文件路径。该参数需与轻量化工具搭配使用，由轻量化工具自动生成。具体参见模型轻量化。
否
不涉及
--weight_data_type
支持设定模型权值数据类型，支持指定为FP32或FP16。
该参数仅针对模型中权值数据类型为FP32时生效，根据设定将权值数据类型由FP32转为FP16存储或维持FP32不变。该参数默认值为FP16。
例如："weight_data_type:FP16"。
由于CPUCL不支持FP16的权重进行计算，如果模型需要兼容CPU计算库，需要指定该参数为FP32。
否
FP16
--weight_merge
离线模型权值归并开关，支持指定在离线模型生成时权值是否进行归并存储操作；该参数为true时，模型权值归并存储。该参数为false时，权值维持非归并存储方式，对性能无影响。该参数默认为true。
否
True
--use_origin_format
支持设定模型的输入输出和原始模型保持一致的format。
本参数仅支持基于yolo、inception的业务网络转换设置为true，其它网络转换使用默认值false。
否
false
--dynamic_dims
支持同一个原始模型生成能支持不同shape输入档位的Davinci模型，该参数指定可以变化的dim值。和--input_shape参数配合使用，在input_shape参数中可以变化的dim使用-1代替。
该参数中每一种可以变化的dims值使用分号分隔（也称为一档），如果一档中有多个维度，每个维度之间使用逗号分隔。举例：
-  --input_shape = "input_name1:-1,c,h,w" --dynamic_dims = "n1;n2;n3"
-  --input_shape = "input_name1:n,-1,-1,c" --dynamic_dims =  "h1,w1;h2,w2"
使用约束：支持可以变化的shape种类最多16种。
否
不涉及
当前只支持下表列出的情况。
-  原始模型实际输入 离线模型期望输入（用户设定） 针对OMG参数 FP32 FP16 --input_type FP32 FP32 --input_type FP16 FP16 --input_type UINT8 UINT8 --input_type INT32 INT32 --input_type INT8 INT8 --input_type
| 原始模型实际输入  | 离线模型期望输入（用户设定）  | 针对OMG参数  |
| --- | --- | --- |
| FP32  | FP16  | --input_type  |
| FP32  | FP32  | --input_type  |
| FP16  | FP16  | --input_type  |
| UINT8  | UINT8  | --input_type  |
| INT32  | INT32  | --input_type  |
| INT8  | INT8  | --input_type  |
-  原始模型实际输入 离线模型期望输入 是否有AIPP 针对OMG参数 FP32 UINT8 有 --input_type FP16 UINT8 有 --input_type UINT8 UINT8 有 --input_type
-  原始模型 离线模型输出 针对OMG参数 FP32 UINT8 --output_type FP16 UINT8 --output_type UINT8 UINT8 --output_type FP16 FP16 --output_type FP32 FP32 --output_type FP32 FP16 --output_type FP16 FP32 --output_type INT8 INT8 --output_type INT32 INT32 --output_type INT64 INT64 --output_type
| 原始模型实际输入  | 离线模型期望输入  | 是否有AIPP  | 针对OMG参数  |
| --- | --- | --- | --- |
| FP32  | UINT8  | 有  | --input_type  |
| FP16  | UINT8  | 有  | --input_type  |
| UINT8  | UINT8  | 有  | --input_type  |
| 原始模型  | 离线模型输出  | 针对OMG参数  |
| --- | --- | --- |
| FP32  | UINT8  | --output_type  |
| FP16  | UINT8  | --output_type  |
| UINT8  | UINT8  | --output_type  |
| FP16  | FP16  | --output_type  |
| FP32  | FP32  | --output_type  |
| FP32  | FP16  | --output_type  |
| FP16  | FP32  | --output_type  |
| INT8  | INT8  | --output_type  |
| INT32  | INT32  | --output_type  |
| INT64  | INT64  | --output_type  |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-preparing-for-model-conversion-V14
爬取时间: 2025-04-30 04:26:59
来源: Huawei Developer
若TensorFlow或Caffe模型过大，可以在OMG转换之前使用Tools下载的轻量化工具，使用方式请参见模型轻量化。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-model-conversion-example-V14
爬取时间: 2025-04-30 04:27:13
来源: Huawei Developer
使用HiAI Foundation SDK时，可以预先使用OMG工具将Caffe、TensorFlow、ONNX、MindSpore模型转换为OM离线模型，移动端AI程序直接读取离线模型进行推理。OMG工具位于Tools下载的tools/tools_omg下，可运行在64位Linux平台上。
Caffe模型转换
当前支持Caffe1.0版本。
命令行中的参数说明请参见OMG参数，转换命令：
转换示例：
当看到OMG generate offline model success时，则说明转换成功，会在当前目录下生成squeezenet.om。
TensorFlow模型转换
当前支持TensorFlow2.x版本。
命令行中的参数说明请参见OMG参数，转换命令：
```shell
./omg --model xxx.pb --framework 3 --output ./modelname --input_shape "xxx:n,h,w,c" --out_nodes "node_name1:0"
```
转换示例：
```shell
./omg --model mobilenet_v2_1.0_224_frozen.pb --framework 3 --output ./mobilenet_v2 --input_shape "input:1,224,224,3" --out_nodes "MobilenetV2/Predictions/Reshape_1:0"
```
当看到OMG generate offline model success时，则说明转换成功，会在当前目录下生成mobilenet_v2.om。
ONNX模型转换
当前支持ONNXopset版本7~18（最高支持到V1.13.1）。
命令行中的参数说明请参见OMG参数，转换命令：
```shell
./omg --model xxx.onnx --framework 5 --output ./modelname
```
转换示例:
```shell
./omg --model resnet18.onnx --framework 5 --output ./resnet18
```
当看到如下log时，则说明转换成功，会在当前目录下生成resnet18.om。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094333.54265506594918437060277103364447:50001231000000:2800:1B0FC138D367B68AEBBCD91897FF05A4FA6CABDC5E558C5CA6BA03842C0AFD85.png)
量化模型转换（以Caffe模型为例）
目前大部分模型在NPU上都是使用16bit float类型进行计算的，使用量化既可以减少模型的体积，也可以加快模型推理速度。
量化模型转换依赖轻量化工具，利用轻量化工具生成模型及轻量化配置，通过“compress_conf”参数传递给OMG并生成量化模型，更多说明请参见模型轻量化。
命令行中的参数说明请参见OMG参数，转换命令：
```shell
./omg --model xxx.prototxt --weight xxx.caffemodel --framework 0 --output ./modelname  --compress_conf=param
```
转换示例：
```shell
./omg --model deploy.prototxt --weight squeezenet_v1.1.caffemodel --framework 0 --output ./squeezenet --compress_conf=param
```
当看到OMG generate offline model success时，说明模型量化成功，会在当前目录下生成量化模型squeezenet.om。
推理前可变Shape模型转换（以ONNX模型为例）
如果一个模型需要支持一次加载，然后不同次的推理会遇到不同的batch，或者不同的分辨率，那么可以使用推理前可变Shape的模型转换。
在模型转换时，将推理过程可能遇到的所有Shape种类预先通过dynamic_dims和input_shape指定出来，生成一个标准IR模型，其携带多种shape输入。
命令行中的参数说明请参见OMG参数。
转换示例：
```shell
./omg --model=./1batch.onnx --input_shape="inputName:-1,3,128,128" --dynamic_dims="1;2;5" --framework=5 --output=./FlexibleShapeModelName
```
不同shape输入对应的不同输出shape，可在模型转换日志中，通过 "Graph:" 关键字查找对应的shape信息，方便在模型推理时指定对应的输出描述。
MindSpore模型转换
MindSpore支持的算子数量有限，建议通过TensorFlow模型转换或者ONNX模型转换。
AIPP模型转换（以Caffe模型为例）
如果模型推理需要对图像或其他输入数据进行变换（如图像尺寸变换、色域转换、减均值/乘系数等），可使用AIPP模型转换功能。转换后的模型增加算子替换此类操作，可提升效率。
命令行中的参数说明请参见OMG参数，转换命令：
```shell
./omg --model xxx.prototxt --weight xxx.caffemodel --framework 0 --insert_op_conf aipp_conf_static.cfg --output ./modelname
```
转换示例：
```shell
./omg --model deploy.prototxt --weight squeezenet_v1.1.caffemodel --framework 0 --insert_op_conf aipp_conf_static.cfg --output ./squeezenet
```
当出现OMG generate offline model success时，说明AIPP模型转换成功，会在当前目录下生成AIPP squeezenet.om模型。
aipp_conf_static.cfg是AIPP的配置文件，位置存放在“tools/tools_omg/sample”文件夹中，具体说明参见AIPP配置文件说明。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-aipp-V14
爬取时间: 2025-04-30 04:27:26
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-aipp-overview-V14
爬取时间: 2025-04-30 04:27:39
来源: Huawei Developer
AIPP（AI Pre-Process）是针对AI推理的输入数据进行预处理的模块。HiAI模型推理一般需要标准化输入数据格式，而一般模型推理场景数据是一张图片，在格式上存在多样性，AIPP可实现不同格式图片数据到NPU标准输入数据格式的转换。对已训练好的模型，不用重新训练匹配推理计算平台需要的数据格式，而只通过AIPP参数配置或者在软件上调用AIPP接口即可完成适配。由于AIPP硬件专用，可以获得较好的推理性能收益，又可以称为“硬件图像预处理”。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-aipp-parameters-V14
爬取时间: 2025-04-30 04:27:52
来源: Huawei Developer
AIPP分为静态AIPP和动态AIPP，两者使用严格区分，静态AIPP模型不能接收模型推理时传入的AIPP参数，不兼容动态AIPP场景，静态与动态AIPP区别详见下表。
| AIPP  | 设置AIPP参数方式  | 优点  |
| --- | --- | --- |
| 静态AIPP  | 在模型生成时通过配置文件或者IR构图预置。  | 更高效率，模型加载阶段即可完成AIPP初始化。  |
| 动态AIPP  | 仅标记该模型具备AIPP处理功能。  | 更灵活，每次推理可传入不同AIPP参数。  |
AIPP
设置AIPP参数方式
优点
静态AIPP
在模型生成时通过配置文件或者IR构图预置。
更高效率，模型加载阶段即可完成AIPP初始化。
动态AIPP
仅标记该模型具备AIPP处理功能。
更灵活，每次推理可传入不同AIPP参数。
AIPP支持的输入格式
AIPP可配置的图片格式如下：
格式后缀U8表示图片像素点为Uint8类型，范围为0到255。当图片的输入为YUV类型时，无论是YUV420还是YUV422或者YUYV，AIPP自动将图片数据补齐为YUV444格式。
除以上列举的图片类型，AIPP还可以通过开启Channel Swap通道交换功能，支持更加丰富的图片输入格式。
AIPP支持的功能
AIPP按照芯片的处理顺序，支持的功能如下：
Crop
AIPP的Crop功能用于对输入图片进行裁剪，涉及参数如下：
| 名称  | 描述  | 取值范围  |
| --- | --- | --- |
| switch  | 裁剪使能开关。  | false/true  |
| load_start_pos_w  | 裁剪起始位置水平方向坐标。  | load_start_pos_w < src_image_size_w  |
| load_start_pos_h  | 裁剪起始位置垂直方向坐标。  | load_start_pos_h < src_image_size_h  |
| crop_size_w  | 裁剪出的图像宽度。  | load_start_pos_w + crop_size_w <= src_image_size_w  |
| crop_size_h  | 裁剪出的图像高度。  | load_start_pos_h + crop_size_h <= src_image_size_h  |
名称
描述
取值范围
switch
裁剪使能开关。
false/true
load_start_pos_w
裁剪起始位置水平方向坐标。
load_start_pos_w < src_image_size_w
load_start_pos_h
裁剪起始位置垂直方向坐标。
load_start_pos_h < src_image_size_h
crop_size_w
裁剪出的图像宽度。
load_start_pos_w + crop_size_w <= src_image_size_w
crop_size_h
裁剪出的图像高度。
load_start_pos_h + crop_size_h <= src_image_size_h
YUV类型的图片受图片自身类型的限制，当输入图片类型为YUV420SP、YUYV、YUV422SP和AYUV444时，裁剪的起始坐标和裁剪的宽高都应该是偶数，系统会进行校验。
Channel Swap
AIPP支持两种类型的通道交换：RB/UV通道交换和AX通道交换。
RB/UV通道交换丰富了输入图片的格式，开启RB/UV通道交换后，AIPP支持的图片输入格式比可配置的输入类型丰富了一倍。
| 配置类型  | 可接受图片类型  |
| --- | --- |
| YUV420SP_U8  | YUV420，YVU420 + rbuv_swap_switch  |
| XRGB8888_U8  | XRGB，XBGR + rbuv_swap_switch  |
| ARGB8888_U8  | ARGB，ABGR + rbuv_swap_switch  |
| RGB888_U8  | BGR + rbuv_swap_switch  |
| YUYV_U8  | YUYV，YVYU + rbuv_swap_switch  |
| YUV422SP_U8  | YUV422，YVU422 + rbuv_swap_switch  |
| AYUV444_U8  | AYUV + rbuv_swap_switch  |
配置类型
可接受图片类型
YUV420SP_U8
YUV420，YVU420 + rbuv_swap_switch
XRGB8888_U8
XRGB，XBGR + rbuv_swap_switch
ARGB8888_U8
ARGB，ABGR + rbuv_swap_switch
RGB888_U8
BGR + rbuv_swap_switch
YUYV_U8
YUYV，YVYU + rbuv_swap_switch
YUV422SP_U8
YUV422，YVU422 + rbuv_swap_switch
AYUV444_U8
AYUV + rbuv_swap_switch
当配置的图片输入格式为XRGB、ARGB或AYUV时，支持开启AX通道交换。开启通道交换后，图片第一个通道的输入被搬移到第四个通道上，即当XRGB、ARGB和AYUV开启AX通道交换后，转变为RGBX、RGBA和YUVA。
当模型训练集为RGB格式的图片，而推理时的图片输入为XRGB或者ARGB时，可以通过使能AX通道交换，将RGB通道前移，实现兼容。
Color Space Conversion
色域转换（Color Space Conversion，以下简称CSC），特指在YUV444和RGB888两种图片格式之间进行转换。涉及如下配置参数。
| 名称  | 描述  | 类型  | 取值范围  |
| --- | --- | --- | --- |
| csc_switch  | CSC开关。  | bool  | true/false  |
| matrix_r0c0 matrix_r0c1 matrix_r0c2 matrix_r1c0 matrix_r1c1 matrix_r1c2 matrix_r2c0 matrix_r2c1 matrix_r2c2  | CSC矩阵元素。  | int16  | [-32677, 32676]  |
| output_bias_0 output_bias_1 output_bias_2  | RGB转YUV时的输出偏移。  | uint8  | [0, 255]  |
| input_bias_0 input_bias_1 input_bias_2  | YUV转RGB时的输入偏移。  | uint8  | [0, 255]  |
名称
描述
类型
取值范围
csc_switch
CSC开关。
bool
true/false
matrix_r0c0
matrix_r0c1
matrix_r0c2
matrix_r1c0
matrix_r1c1
matrix_r1c2
matrix_r2c0
matrix_r2c1
matrix_r2c2
CSC矩阵元素。
int16
[-32677, 32676]
output_bias_0
output_bias_1
output_bias_2
RGB转YUV时的输出偏移。
uint8
[0, 255]
input_bias_0
input_bias_1
input_bias_2
YUV转RGB时的输入偏移。
uint8
[0, 255]
参考1：YUV和BGR的转换公式。
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094333.07495415975932857316981999978269:50001231000000:2800:F990C2E567A7B05B61E989801B97F6AF4767091E7034560732F32CE2B4EAB1D8.png)
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094333.95626784600911385586453413781991:50001231000000:2800:177A991300555CB370F319B8E7293D8253FA24A6AD766A30EDE22AB3E005EF4C.png)
参考2：BT-601 narrow、JPEG和BT-709 narrow三种类型图片的转换公式。
-
-
-
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094333.58438464118991338578465591135349:50001231000000:2800:9B2C6DAD2B7C03C98E9E838C9C5E7B911879C997F62EE3CD79B9D4E80920D71D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094334.00120205498150969409561107910466:50001231000000:2800:30ACBF5F7C42D1EC120D20B1B42484E30D79DC1A14267557881A416113DBE2E8.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094334.60595983506796107529128117518104:50001231000000:2800:70CCCAA4079948AB6926B38FF658CE45BC7DF3C86006E92C01BD037F85F185E9.png)
使用配置文件生成静态AIPP模型时，需要根据以上的公式配置CSC矩阵以及“input_bias”或者“output_bias”的值。使用IR定义AIPP CSC功能算子，以及使用HiAI Foundation接口配置CSC参数时，支持传入目标类型，由系统来填充CSC配置参数。
以下为JPEG和BT-601NARROW两种图片类型下的CSC配置参考。
-  JPEG BT-601NARROW BT-601FULL BT-709NARROW matrix_r0c0 : 256 matrix_r0c1 : 0 matrix_r0c2 : 359 matrix_r1c0 : 256 matrix_r1c1 : -88 matrix_r1c2 : -183 matrix_r2c0 : 256 matrix_r2c1 : 454 matrix_r2c2 : 0 input_bias_0 : 0 input_bias_1 : 128 input_bias_2 : 128 matrix_r0c0 : 298 matrix_r0c1 : 0 matrix_r0c2 : 409 matrix_r1c0 : 298 matrix_r1c1 : -100 matrix_r1c2 : -208 matrix_r2c0 : 298 matrix_r2c1 : 516 matrix_r2c2 : 0 input_bias_0 : 16 input_bias_1 : 128 input_bias_2 : 128 matrix_r0c0 : 256 matrix_r0c1 : 0 matrix_r0c2 : 359 matrix_r1c0 : 256 matrix_r1c1 : -88 matrix_r1c2 : -183 matrix_r2c0 : 256 matrix_r2c1 : 454 matrix_r2c2 : 0 input_bias_0 : 0 input_bias_1 : 128 input_bias_2 : 128 matrix_r0c0 : 298 matrix_r0c1 : 0 matrix_r0c2 : 460 matrix_r1c0 : 298 matrix_r1c1 : -55 matrix_r1c2 : -137 matrix_r2c0 : 298 matrix_r2c1 : 541 matrix_r2c2 : 0 input_bias_0 : 16 input_bias_1 : 128 input_bias_2 : 128
-  JPEG BT-601NARROW BT-601FULL BT-709NARROW matrix_r0c0 : 256 matrix_r0c1 : 454 matrix_r0c2 : 0 matrix_r1c0 : 256 matrix_r1c1 : -88 matrix_r1c2 : -183 matrix_r2c0 : 256 matrix_r2c1 : 0 matrix_r2c2 : 359 input_bias_0 : 0 input_bias_1 : 128 input_bias_2 : 128 matrix_r0c0 : 298 matrix_r0c1 : 516 matrix_r0c2 : 0 matrix_r1c0 : 298 matrix_r1c1 : -100 matrix_r1c2 : -208 matrix_r2c0 : 298 matrix_r2c1 : 0 matrix_r2c2 : 409 input_bias_0 : 16 input_bias_1 : 128 input_bias_2 : 128 matrix_r0c0 : 256 matrix_r0c1 : 454 matrix_r0c2 : 0 matrix_r1c0 : 256 matrix_r1c1 : -88 matrix_r1c2 : -183 matrix_r2c0 : 256 matrix_r2c1 : 0 matrix_r2c2 : 359 input_bias_0 : 0 input_bias_1 : 128 input_bias_2 : 128 matrix_r0c0 : 298 matrix_r0c1 : 541 matrix_r0c2 : 0 matrix_r1c0 : 298 matrix_r1c1 : -55 matrix_r1c2 : -137 matrix_r2c0 : 298 matrix_r2c1 : 0 matrix_r2c2 : 460 input_bias_0 : 16 input_bias_1 : 128 input_bias_2 : 128
-  matrix_r0c0 : 256 matrix_r0c1 : 0 matrix_r0c2 : 0 matrix_r1c0 : 0 matrix_r1c1 : 0 matrix_r1c2 : 0 matrix_r2c0 : 0 matrix_r2c1 : 0 matrix_r2c2 : 0
-  matrix_r0c0 : 76 matrix_r0c1 : 150 matrix_r0c2 : 30 matrix_r1c0 : 0 matrix_r1c1 : 0 matrix_r1c2 : 0 matrix_r2c0 : 0 matrix_r2c1 : 0 matrix_r2c2 : 0
-  JPEG BT-601NARROW BT-601FULL BT-709NARROW matrix_r0c0 : 77 matrix_r0c1 : 150 matrix_r0c2 : 29 matrix_r1c0 : -43 matrix_r1c1 : -85 matrix_r1c2 : 128 matrix_r2c0 : 128 matrix_r2c1 : -107 matrix_r2c2 : -21 output_bias_0 : 0 output_bias_1 : 128 output_bias_2 : 128 matrix_r0c0 : 66 matrix_r0c1 : 129 matrix_r0c2 : 25 matrix_r1c0 : -38 matrix_r1c1 : -74 matrix_r1c2 : 112 matrix_r2c0 : 112 matrix_r2c1 : -94 matrix_r2c2 : -18 output_bias_0 : 16 output_bias_1 : 128 output_bias_2 : 128 matrix_r0c0 : 77 matrix_r0c1 : 150 matrix_r0c2 : 29 matrix_r1c0 : -43 matrix_r1c1 : -85 matrix_r1c2 : 128 matrix_r2c0 : 128 matrix_r2c1 : -107 matrix_r2c2 : -21 output_bias_0 : 0 output_bias_1 : 128 output_bias_2 : 128 matrix_r0c0 : 47 matrix_r0c1 : 157 matrix_r0c2 : 16 matrix_r1c0 : -26 matrix_r1c1 : -87 matrix_r1c2 : 112 matrix_r2c0 : 112 matrix_r2c1 : -102 matrix_r2c2 : -10 output_bias_0 : 16 output_bias_1 : 128 output_bias_2 : 128
-  JPEG BT-601NARROW BT-601FULL BT-709NARROW matrix_r0c0 : 77 matrix_r0c1 : 150 matrix_r0c2 : 29 matrix_r1c0 : 128 matrix_r1c1 : -107 matrix_r1c2 : -21 matrix_r2c0 : -43 matrix_r2c1 : -85 matrix_r2c2 : 128 output_bias_0 : 0 output_bias_1 : 128 output_bias_2 : 128 matrix_r0c0 : 66 matrix_r0c1 : 129 matrix_r0c2 : 25 matrix_r1c0 : 112 matrix_r1c1 : -94 matrix_r1c2 : -18 matrix_r2c0 : -38 matrix_r2c1 : -74 matrix_r2c2 : 112 output_bias_0 : 16 output_bias_1 : 128 output_bias_2 : 128 matrix_r0c0 : 77 matrix_r0c1 : 150 matrix_r0c2 : 29 matrix_r1c0 : 128 matrix_r1c1 : -107 matrix_r1c2 : -21 matrix_r2c0 : -43 matrix_r2c1 : -85 matrix_r2c2 : 128 output_bias_0 : 0 output_bias_1 : 128 output_bias_2 : 128 matrix_r0c0 : 47 matrix_r0c1 : 157 matrix_r0c2 : 16 matrix_r1c0 : 112 matrix_r1c1 : -102 matrix_r1c2 : -10 matrix_r2c0 : -26 matrix_r2c1 : -87 matrix_r2c2 : 112 output_bias_0 : 16 output_bias_1 : 128 output_bias_2 : 128
| JPEG  | BT-601NARROW  | BT-601FULL  | BT-709NARROW  |
| --- | --- | --- | --- |
| matrix_r0c0 : 256 matrix_r0c1 : 0 matrix_r0c2 : 359 matrix_r1c0 : 256 matrix_r1c1 : -88 matrix_r1c2 : -183 matrix_r2c0 : 256 matrix_r2c1 : 454 matrix_r2c2 : 0 input_bias_0 : 0 input_bias_1 : 128 input_bias_2 : 128  | matrix_r0c0 : 298 matrix_r0c1 : 0 matrix_r0c2 : 409 matrix_r1c0 : 298 matrix_r1c1 : -100 matrix_r1c2 : -208 matrix_r2c0 : 298 matrix_r2c1 : 516 matrix_r2c2 : 0 input_bias_0 : 16 input_bias_1 : 128 input_bias_2 : 128  | matrix_r0c0 : 256 matrix_r0c1 : 0 matrix_r0c2 : 359 matrix_r1c0 : 256 matrix_r1c1 : -88 matrix_r1c2 : -183 matrix_r2c0 : 256 matrix_r2c1 : 454 matrix_r2c2 : 0 input_bias_0 : 0 input_bias_1 : 128 input_bias_2 : 128  | matrix_r0c0 : 298 matrix_r0c1 : 0 matrix_r0c2 : 460 matrix_r1c0 : 298 matrix_r1c1 : -55 matrix_r1c2 : -137 matrix_r2c0 : 298 matrix_r2c1 : 541 matrix_r2c2 : 0 input_bias_0 : 16 input_bias_1 : 128 input_bias_2 : 128  |
| JPEG  | BT-601NARROW  | BT-601FULL  | BT-709NARROW  |
| --- | --- | --- | --- |
| matrix_r0c0 : 256 matrix_r0c1 : 454 matrix_r0c2 : 0 matrix_r1c0 : 256 matrix_r1c1 : -88 matrix_r1c2 : -183 matrix_r2c0 : 256 matrix_r2c1 : 0 matrix_r2c2 : 359 input_bias_0 : 0 input_bias_1 : 128 input_bias_2 : 128  | matrix_r0c0 : 298 matrix_r0c1 : 516 matrix_r0c2 : 0 matrix_r1c0 : 298 matrix_r1c1 : -100 matrix_r1c2 : -208 matrix_r2c0 : 298 matrix_r2c1 : 0 matrix_r2c2 : 409 input_bias_0 : 16 input_bias_1 : 128 input_bias_2 : 128  | matrix_r0c0 : 256 matrix_r0c1 : 454 matrix_r0c2 : 0 matrix_r1c0 : 256 matrix_r1c1 : -88 matrix_r1c2 : -183 matrix_r2c0 : 256 matrix_r2c1 : 0 matrix_r2c2 : 359 input_bias_0 : 0 input_bias_1 : 128 input_bias_2 : 128  | matrix_r0c0 : 298 matrix_r0c1 : 541 matrix_r0c2 : 0 matrix_r1c0 : 298 matrix_r1c1 : -55 matrix_r1c2 : -137 matrix_r2c0 : 298 matrix_r2c1 : 0 matrix_r2c2 : 460 input_bias_0 : 16 input_bias_1 : 128 input_bias_2 : 128  |
| matrix_r0c0 : 256 matrix_r0c1 : 0 matrix_r0c2 : 0 matrix_r1c0 : 0 matrix_r1c1 : 0 matrix_r1c2 : 0 matrix_r2c0 : 0 matrix_r2c1 : 0 matrix_r2c2 : 0  |
| --- |
| matrix_r0c0 : 76 matrix_r0c1 : 150 matrix_r0c2 : 30 matrix_r1c0 : 0 matrix_r1c1 : 0 matrix_r1c2 : 0 matrix_r2c0 : 0 matrix_r2c1 : 0 matrix_r2c2 : 0  |
| --- |
| JPEG  | BT-601NARROW  | BT-601FULL  | BT-709NARROW  |
| --- | --- | --- | --- |
| matrix_r0c0 : 77 matrix_r0c1 : 150 matrix_r0c2 : 29 matrix_r1c0 : -43 matrix_r1c1 : -85 matrix_r1c2 : 128 matrix_r2c0 : 128 matrix_r2c1 : -107 matrix_r2c2 : -21 output_bias_0 : 0 output_bias_1 : 128 output_bias_2 : 128  | matrix_r0c0 : 66 matrix_r0c1 : 129 matrix_r0c2 : 25 matrix_r1c0 : -38 matrix_r1c1 : -74 matrix_r1c2 : 112 matrix_r2c0 : 112 matrix_r2c1 : -94 matrix_r2c2 : -18 output_bias_0 : 16 output_bias_1 : 128 output_bias_2 : 128  | matrix_r0c0 : 77 matrix_r0c1 : 150 matrix_r0c2 : 29 matrix_r1c0 : -43 matrix_r1c1 : -85 matrix_r1c2 : 128 matrix_r2c0 : 128 matrix_r2c1 : -107 matrix_r2c2 : -21 output_bias_0 : 0 output_bias_1 : 128 output_bias_2 : 128  | matrix_r0c0 : 47 matrix_r0c1 : 157 matrix_r0c2 : 16 matrix_r1c0 : -26 matrix_r1c1 : -87 matrix_r1c2 : 112 matrix_r2c0 : 112 matrix_r2c1 : -102 matrix_r2c2 : -10 output_bias_0 : 16 output_bias_1 : 128 output_bias_2 : 128  |
| JPEG  | BT-601NARROW  | BT-601FULL  | BT-709NARROW  |
| --- | --- | --- | --- |
| matrix_r0c0 : 77 matrix_r0c1 : 150 matrix_r0c2 : 29 matrix_r1c0 : 128 matrix_r1c1 : -107 matrix_r1c2 : -21 matrix_r2c0 : -43 matrix_r2c1 : -85 matrix_r2c2 : 128 output_bias_0 : 0 output_bias_1 : 128 output_bias_2 : 128  | matrix_r0c0 : 66 matrix_r0c1 : 129 matrix_r0c2 : 25 matrix_r1c0 : 112 matrix_r1c1 : -94 matrix_r1c2 : -18 matrix_r2c0 : -38 matrix_r2c1 : -74 matrix_r2c2 : 112 output_bias_0 : 16 output_bias_1 : 128 output_bias_2 : 128  | matrix_r0c0 : 77 matrix_r0c1 : 150 matrix_r0c2 : 29 matrix_r1c0 : 128 matrix_r1c1 : -107 matrix_r1c2 : -21 matrix_r2c0 : -43 matrix_r2c1 : -85 matrix_r2c2 : 128 output_bias_0 : 0 output_bias_1 : 128 output_bias_2 : 128  | matrix_r0c0 : 47 matrix_r0c1 : 157 matrix_r0c2 : 16 matrix_r1c0 : 112 matrix_r1c1 : -102 matrix_r1c2 : -10 matrix_r2c0 : -26 matrix_r2c1 : -87 matrix_r2c2 : 112 output_bias_0 : 16 output_bias_1 : 128 output_bias_2 : 128  |
从使用的角度，将灰度图转成RGB没有意义，系统约束当输入格式配置为YUV400_U8时，不支持CSC。
Resize
图片缩放参数及约束如下：
| 名称  | 描述  | 取值范围（静态）  | 取值范围（动态）  |
| --- | --- | --- | --- |
| switch  | 缩放使能开关  | false/true  | false/true  |
| resize_input_w  | 缩放前图像宽度  | [16, 4096]  | [16, 1280]  |
| resize_input_h  | 缩放前图像高度  | [16, 4096]  | [16, 4096]  |
| resize_output_w  | 缩放后图像宽度  | [16, 1280]  | [16, 448]  |
| resize_output_h  | 缩放后图像高度  | [16, 4096]  | [16, 4096]  |
名称
描述
取值范围（静态）
取值范围（动态）
switch
缩放使能开关
false/true
false/true
resize_input_w
缩放前图像宽度
[16, 4096]
[16, 1280]
resize_input_h
缩放前图像高度
[16, 4096]
[16, 4096]
resize_output_w
缩放后图像宽度
[16, 1280]
[16, 448]
resize_output_h
缩放后图像高度
[16, 4096]
[16, 4096]
图片缩放倍数约束如下：
| 名称  | 描述  | 范围（动态&静态）  |
| --- | --- | --- |
| resize_output_w / resize_input_w  | 图像宽度缩放倍数  | [1/16, 16]  |
| resize_output_h / resize_input_h  | 图像高度缩放倍数  | [1/16, 16]  |
名称
描述
范围（动态&静态）
resize_output_w / resize_input_w
图像宽度缩放倍数
[1/16, 16]
resize_output_h / resize_input_h
图像高度缩放倍数
[1/16, 16]
Resize类型为双线性插值。Resize子功能的“resize_input_w”和“resize_input_h”两个参数对用户不可见。
通过配置文件转换静态AIPP模型时，Crop之后的大小“crop_size_w”和“crop_size_h”，以及Resize之后的大小“resize_output_w”和“resize_output_h”可以省去不配置，前提是这两个参数可以通过计算获取。省略“resize_output_w”和“resize_output_h”时，Resize功能这两个值取模型训练集的图片尺寸减去AIPP Padding之后的结果；当Resize不使用时，同理可省略Crop功能“crop_size_w”和“crop_size_h”。
Data Type Conversion
数据类型转换（Data Type Conversion，以下简称DTC），DTC用于将输入图片中像素值转换为模型训练时的数据类型。AIPP允许用户设置DTC参数，使得转换之后的数据在一个预期的范围，避免强制转换。
将Uint8类型的数据转换为Int8类型的数据，计算规则如下：
pixel_out_chx(i) = pixel_in_chx(i)–mean_chn_i
将Uint8类型的数据转换为Float16类型的数据，计算规则如下：
pixel_out_chx(i) = [pixel_in_chx(i)–mean_chn_i–min_chn_i] * var_reci_chn
DTC涉及的配置参数如下表。
| 名称  | 描述  | 取值范围  |
| --- | --- | --- |
| switch  | DTC使能开关。  | false/true  |
| mean_chn_0  | 通道0均值。  | [0, 255]  |
| mean_chn_1  | 通道1均值。  | [0, 255]  |
| mean_chn_2  | 通道2均值。  | [0, 255]  |
| mean_chn_3  | 通道3均值。  | [0, 255]  |
| min_chn_0  | 通道0最小值。  | [-65504, 65504]  |
| min_chn_1  | 通道1最小值。  | [-65504, 65504]  |
| min_chn_2  | 通道2最小值。  | [-65504, 65504]  |
| min_chn_3  | 通道3最小值。  | [-65504, 65504]  |
| var_reci_chn_0  | 通道0方差。  | [-65504, 65504]  |
| var_reci_chn_1  | 通道1方差。  | [-65504, 65504]  |
| var_reci_chn_2  | 通道2方差。  | [-65504, 65504]  |
| var_reci_chn_3  | 通道3方差。  | [-65504, 65504]  |
名称
描述
取值范围
switch
DTC使能开关。
false/true
mean_chn_0
通道0均值。
[0, 255]
mean_chn_1
通道1均值。
[0, 255]
mean_chn_2
通道2均值。
[0, 255]
mean_chn_3
通道3均值。
[0, 255]
min_chn_0
通道0最小值。
[-65504, 65504]
min_chn_1
通道1最小值。
[-65504, 65504]
min_chn_2
通道2最小值。
[-65504, 65504]
min_chn_3
通道3最小值。
[-65504, 65504]
var_reci_chn_0
通道0方差。
[-65504, 65504]
var_reci_chn_1
通道1方差。
[-65504, 65504]
var_reci_chn_2
通道2方差。
[-65504, 65504]
var_reci_chn_3
通道3方差。
[-65504, 65504]
当DTC开关为false时，或者用户调用HiAI Foundation接口未传入DTC参数时，系统默认对图片输入数据进行类型强转，效果同通道均值和最小值均为0，通道方差为1。
Rotation
AIPP的Rotation功能用于对输入图片进行旋转，涉及的参数如下：
| 名称  | 描述  | 取值范围  |
| --- | --- | --- |
| switch  | Rotation使能开关  | false/true  |
| rotation_angle  | 图像旋转角度  | [0, 90, 180, 270]  |
名称
描述
取值范围
switch
Rotation使能开关
false/true
rotation_angle
图像旋转角度
[0, 90, 180, 270]
Padding
AIPP的Padding功能用于对输入图片进行补边，涉及的参数如下。
| 名称  | 描述  | 取值范围  |
| --- | --- | --- |
| switch  | Padding使能开关。  | false/true  |
| left_padding_size  | 图像左侧Padding像素数。  | -  |
| right_padding_size  | 图像右侧Padding像素数。  | -  |
| top_padding_size  | 图像上侧Padding像素数。  | -  |
| bottom_padding_size  | 图像下侧Padding像素数。  | -  |
| padding_value_chn_0  | 通道0 Padding的值。  | [-65504, 65504]  |
| padding_value_chn_1  | 通道1 Padding的值。  | [-65504, 65504]  |
| padding_value_chn_2  | 通道2 Padding的值。  | [-65504, 65504]  |
| padding_value_chn_3  | 通道3 Padding的值。  | [-65504, 65504]  |
名称
描述
取值范围
switch
Padding使能开关。
false/true
left_padding_size
图像左侧Padding像素数。
-
right_padding_size
图像右侧Padding像素数。
-
top_padding_size
图像上侧Padding像素数。
-
bottom_padding_size
图像下侧Padding像素数。
-
padding_value_chn_0
通道0 Padding的值。
[-65504, 65504]
padding_value_chn_1
通道1 Padding的值。
[-65504, 65504]
padding_value_chn_2
通道2 Padding的值。
[-65504, 65504]
padding_value_chn_3
通道3 Padding的值。
[-65504, 65504]

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-aipp-configuration-file-V14
爬取时间: 2025-04-30 04:28:06
来源: Huawei Developer
模型转换AIPP配置文件说明
一份功能完整的AIPP配置文件示例如下：
AIPP配置多输入支持
AIPP支持对一个多输入模型的多个输入分别配置AIPP，也支持在一个输入Data算子有多个输出分支的情况下，对不同的输出分支分别配置AIPP。
AIPP配置的多输入支持由2组共4个配置参数控制：input_name和related_input_rank用于指定对哪一个输入进行AIPP处理，node_after_aipp和input_edge_idx用于指定对Data算子的多个输出中的哪一个输出进行AIPP处理。
input_name和related_input_rank两个参数推荐使用input_name，related_input_rank参数用于模型输入名称不确定的场景，如果同时配置这两个参数，则两个参数互为校验；如果两个参数都没有被配置，默认对模型的第一个输入进行AIPP处理。
node_after_aipp和input_edge_idx两个参数推荐使用node_after_aipp，input_edge_idx用于Data算子的多个输出分支衔接的算子名称重复或不确定的场景，如果同时配置这两个参数，则两个参数互为校验；如果两个参数都没有被配置，则该Data算子的所有输出分支使用同一个AIPP处理。
AIPP配置区分动态AIPP与静态AIPP
只要有一个AIPP子功能的dynamic开关配置为true，或者没有打开任何一个子功能的开关，则生成的DaVinci模型为动态AIPP模型，需要在模型推理阶段传入AIPP配置参数；相反没有任何子功能的dynamic开关配置为true，并且至少有一个子功能的开关是打开的，则生成的DaVinci模型为静态AIPP模型，模型推理阶段使用配置文件中定义的AIPP配置参数。
对于动态AIPP的场景，AIPP可以允许输入图片的长宽，以及图片类型不确定，对应即src_image_size_w、src_image_size_h和input_format三个参数不配置，此时用户需要指定动态AIPP处理时的最大图片尺寸，配置max_src_image_size。
图片裁剪(Crop)
图片裁剪功能是指在原始图片中从指定的起点裁剪出指定大小的子图。
dynamic不写或者写成“false”表示静态配置，写成“true”表示动态配置。
静态配置
动态配置
通道交换功能(axSwap/uvSwap/rbSwap)
交换图片的通道支持AX通道交换、UV通道交换、RB通道交换。
dynamic不写或者写成“false”表示静态配置，写成“true”表示动态配置。
静态配置
动态配置
可以不写具体的参数，在动态创建input tensor时指定。
色域转换功能(CSC)
dynamic不写或者写成“false”表示静态配置，写成“true”表示动态配置。
支持的转换格式如下：
静态配置
静态AIPP配置色域转化矩阵示例如下。
动态配置
指定输出的色域格式，动态场景下，inputFormat可以改变，但是output_format不可变，否则会报错，因为输出的格式一般是固定的。
图片缩放(Resize)
图片缩放功能支持图片放大缩小，采用双线性插值方式进行缩放。缩放输出图片最小为16x16，缩放输出最大为448x448。
dynamic不写或者写成“false”表示静态配置，写成“true”表示动态配置。
静态配置
动态配置
resize_output_w、resize_output_h为预分配最大size。
数据类型转换(DTC)
数据类型转化功能是指将输入的图片数据类型通过转化公式转换为FP16类型送给后续模块计算，实际为依次执行减均值、减最小值和乘方差操作。
dynamic不写或者写成“false”表示静态配置，写成“true”表示动态配置。
静态配置
动态配置
可以不写具体的参数，在动态创建input tensor时指定。
图片旋转(Rotation)
旋转功能支持图片旋转90°、180°和270°，以适配手机在不同方向时的用户数据。当前旋转功能只支持静态单算子场景，动态场景以及卷积融合场景不支持。静态配置如下。
图片补边
图片补边功能支持在图片上下左右padding指定大小的数据。 padding的数据可以按通道来设置不同的值，最多补四个通道，如果有的通道没有设置的话，就默认补0，上下左右Padding的大小最大为32，即最多上下各补32行，左右各补32列。
dynamic不写或者写成“false”表示静态配置，写成“true”表示动态配置。
静态配置
动态配置
padding算子是动态的，padding算子的四个padding值就写0，padding value的值在动态创建input tensor时指定。
完整AIPP动态配置示例
完整AIPP静态配置
动静态混合配置示例
动静混合场景不支持配置rotate旋转参数，因为此时模型是动态的，动态场景暂不支持rotate旋转参数的配置。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-variable-data_type-V14
爬取时间: 2025-04-30 04:28:19
来源: Huawei Developer
概述
可变data_type是OMG工具支持的一个功能，用于模型输入输出数据类型多样性的场景，无需修改训练好的模型，在使用OMG工具进行模型转换时，通过指定输入、输出数据类型使得同一个模型适用于不同输入输出的场景。
使用说明
在进行模型转换时，输入输出数据类型指定分别需要通过OMG参数的input_type、output_type来实现。
使用示例：
```shell
./omg --model=./model.pb --framework=3 --output=./model --input_shape="inputs:1,512,512,1" --out_nodes="outputs:0" --input_type="inputs:FP16" --output_type="outputs:UINT8"
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-on-device-deployment-V14
爬取时间: 2025-04-30 04:28:32
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-whole-deployment-process-V14
爬取时间: 2025-04-30 04:28:45
来源: Huawei Developer
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094334.53101641618867489198712455661240:50001231000000:2800:5010B288B95442D70AF20457767CC9C12BEA38577C3AB3338AB734BA2C34EEE6.png)
离线模型转换
离线模型转换需要将Caffe、TensorFlow、ONNX、MindSpore模型转换为HiAI Foundation平台支持的模型格式，并可以按需进行AIPP操作、量化操作，使用场景及方法如下：
-  AIPP用于在硬件上完成图像预处理，包括改变图像尺寸、色域转换（转换图像格式）、减均值/乘系数（改变图像像素），运用后可避免重新训练匹配推理计算平台需要的数据格式，只通过AIPP参数配置或者在软件层面上调用AIPP接口即可完成适配，同时由于硬件专用，可以获得较好的推理性能收益，具体操作可参见AIPP模型转换。
-  量化是一种可以把FP32模型转化为低bit模型的操作，以节约网络存储空间、降低传输时延以及提高运算执行效率，量化操作可参见量化模型转换。
App集成
App集成流程包含创建项目、配置项目里的NAPI、集成模型，集成模型又包含加载模型、编译模型、模型输入数据预处理、运行模型、模型输出数据后处理流程。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-model-inference-V14
爬取时间: 2025-04-30 04:28:59
来源: Huawei Developer
基本概念
该场景是基本模型的使用场景，主要包含模型的编译和推理，其他场景是基础场景的一个扩展和功能增强。
业务流程
模型推理的主要开发流程如下图所示：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094334.61916818343307560850886717342080:50001231000000:2800:E028E283338198229DF87CCEE2C0EAB2F0DA017A4D19C8F5BAB355D82A1E01D2.png)
接口说明
以下接口为主要流程接口，如要使用更丰富的编译、加载和执行时的配置，请参见API参考。
| 接口名  | 描述  |
| --- | --- |
| OH_NNCompilation* OH_NNCompilation_ConstructWithOfflineModelBuffer(const void *modelBuffer, size_t modelSize);  | 根据模型buffer创建模型编译实例。  |
| OH_NN_ReturnCode OH_NNCompilation_SetDevice(OH_NNCompilation *compilation, size_t deviceID);  | 设置模型编译和执行的目标设备。  |
| OH_NN_ReturnCode OH_NNCompilation_Build(OH_NNCompilation *compilation);  | 执行模型编译，生成编译后的模型保存在compilation中。  |
| OH_NNExecutor* OH_NNExecutor_Construct(OH_NNCompilation *compilation);  | 根据编译后的模型，创建模型推理的执行器。  |
| NN_Tensor* OH_NNTensor_Create(size_t deviceID, NN_TensorDesc* tensorDesc);  | 构造输入输出Tensor。  |
| OH_NN_ReturnCode OH_NNExecutor_RunSync(OH_NNExecutor *executor, NN_Tensor *inputTensor[], size_t inputCount, NN_Tensor *outputTensor[], size_t outputCount);  | 执行模型的同步推理。  |
| void OH_NNCompilation_Destroy(OH_NNCompilation **compilation);  | 销毁模型编译实例。  |
| OH_NN_ReturnCode OH_NNTensor_Destroy(NN_Tensor** tensor);  | 销毁输入输出Tensor。  |
| void OH_NNExecutor_Destroy(OH_NNExecutor **executor);  | 销毁模型推理的执行器。  |
接口名
描述
OH_NNCompilation* OH_NNCompilation_ConstructWithOfflineModelBuffer(const void *modelBuffer, size_t modelSize);
根据模型buffer创建模型编译实例。
OH_NN_ReturnCode OH_NNCompilation_SetDevice(OH_NNCompilation *compilation, size_t deviceID);
设置模型编译和执行的目标设备。
OH_NN_ReturnCode OH_NNCompilation_Build(OH_NNCompilation *compilation);
执行模型编译，生成编译后的模型保存在compilation中。
OH_NNExecutor* OH_NNExecutor_Construct(OH_NNCompilation *compilation);
根据编译后的模型，创建模型推理的执行器。
NN_Tensor* OH_NNTensor_Create(size_t deviceID, NN_TensorDesc* tensorDesc);
构造输入输出Tensor。
OH_NN_ReturnCode OH_NNExecutor_RunSync(OH_NNExecutor *executor, NN_Tensor *inputTensor[], size_t inputCount, NN_Tensor *outputTensor[], size_t outputCount);
执行模型的同步推理。
void OH_NNCompilation_Destroy(OH_NNCompilation **compilation);
销毁模型编译实例。
OH_NN_ReturnCode OH_NNTensor_Destroy(NN_Tensor** tensor);
销毁输入输出Tensor。
void OH_NNExecutor_Destroy(OH_NNExecutor **executor);
销毁模型推理的执行器。
开发步骤
以下为模型推理的主要开发步骤，具体实现请参见SampleCode。
1.
1.  调用OH_NNCompilation_ConstructWithOfflineModelBuffer读取模型buffer，创建模型编译实例。或者通过调用OH_NNCompilation_ConstructWithOfflineModelFile直接读取模型文件，创建模型编译实例。
2.  调用OH_NNDevice_GetAllDevicesID，获取所有的设备ID，查找name为"HIAI_F"字段的设备ID，记录并通过OH_NNCompilation_SetDevice设置到步骤3创建的编译实例中。
1.  调用OH_NNCompilation_Build，传入步骤3创建的模型编译实例，即可执行模型编译，编译后的模型数据仍然保存在模型编译实例中。
1.  调用OH_NNExecutor_Construct，创建编译后模型对应的执行器实例。执行器创建完成后即可调用OH_NNCompilation_Destroy销毁模型编译实例。
1.  调用OH_NNExecutor_GetInputCount，查询输入的个数，通过OH_NNExecutor_CreateInputTensorDesc获取到对应索引的TensorDesc，根据该TensorDesc通过OH_NNTensor_Create创建Tensor，即可向Tensor中写入实际数据。输出Tensor的构造与输入Tensor的构造过程一致。
1.  调用OH_NNExecutor_RunSync，执行模型的同步推理功能，模型的输出数据保存在outputTensors中。开发者可根据需要对输出数据做相应的处理以得到期望的内容。
1.

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-aipp-deployment-V14
爬取时间: 2025-04-30 04:29:12
来源: Huawei Developer
基本概念
AIPP部署是指动态AIPP推理时用户按需配置动态AIPP参数，从而达到使能AIPP功能。
业务流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094335.15280532698376619670744121036429:50001231000000:2800:1C44882A53627C6A2996D18F5337110C73D3BE4C53C93451DBBFE19F2D9CC4E0.png)
接口说明
以下接口为AIPP参数设置接口，如要使用更丰富的设置和查询接口，请参见API参考。
| 接口名  | 描述  |
| --- | --- |
| HiAI_AippParam* HMS_HiAIAippParam_Create(uint32_t batchNum);  | 动态AIPP配置实例创建。  |
| void HMS_HiAIAippParam_Destroy(HiAI_AippParam** aippParam);  | 动态AIPP配置实例销毁。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputIndex(HiAI_AippParam* aippParam, uint32_t inputIndex);  | 设置动态AIPP配置作用于输入上的索引。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputAippIndex(HiAI_AippParam* aippParam, uint32_t inputAippIndex);  | 设置动态AIPP配置作用于该输入的多个输出分支上的索引。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputFormat(HiAI_AippParam* aippParam, HiAI_ImageFormat inputFormat);  | 设置输入图片的格式。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputShape(HiAI_AippParam* aippParam, uint32_t srcImageW, uint32_t srcImageH);  | 设置输入图片的原始宽高。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetCscConfig(HiAI_AippParam* aippParam, HiAI_ImageFormat inputFormat, HiAI_ImageFormat outputFormat, HiAI_ImageColorSpace space);  | 设置图片色域转换参数。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelSwapConfig(HiAI_AippParam* aippParam, bool rbuvSwapSwitch, bool axSwapSwitch);  | 设置图片通道交换参数。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetCropConfig(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t startPosW, uint32_t startPosH, uint32_t croppedW, uint32_t croppedH);  | 设置图片裁剪参数。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetResizeConfig(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t resizedW, uint32_t resizedH);  | 设置图片缩放大小参数。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetPadConfig(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t leftPadSize, uint32_t rightPadSize, uint32_t topPadSize, uint32_t bottomPadSize);  | 设置图片左右上下填充的像素数。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelPadding(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount);  | 设置通道填充值。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetRotationAngle(HiAI_AippParam* aippParam, uint32_t batchIndex, float rotationAngle);  | 设置图片旋转参数。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMeanPixel(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount);  | 设置图片数据类型转换的通道像素平均值。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMinPixel(HiAI_AippParam* aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount);  | 设置图片数据类型转换的通道像素最小值。  |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcVarReciPixel(HiAI_AippParam* aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount);  | 设置图片数据类型转换的通道像素方差。  |
| OH_NN_ReturnCode HMS_HiAITensor_SetAippParams(NN_Tensor* tensor, HiAI_AippParam* aippParams[], size_t aippNum);  | 给输入Tensor设置AIPP参数。  |
接口名
描述
HiAI_AippParam* HMS_HiAIAippParam_Create(uint32_t batchNum);
动态AIPP配置实例创建。
void HMS_HiAIAippParam_Destroy(HiAI_AippParam** aippParam);
动态AIPP配置实例销毁。
OH_NN_ReturnCode HMS_HiAIAippParam_SetInputIndex(HiAI_AippParam* aippParam, uint32_t inputIndex);
设置动态AIPP配置作用于输入上的索引。
OH_NN_ReturnCode HMS_HiAIAippParam_SetInputAippIndex(HiAI_AippParam* aippParam, uint32_t inputAippIndex);
设置动态AIPP配置作用于该输入的多个输出分支上的索引。
OH_NN_ReturnCode HMS_HiAIAippParam_SetInputFormat(HiAI_AippParam* aippParam, HiAI_ImageFormat inputFormat);
设置输入图片的格式。
OH_NN_ReturnCode HMS_HiAIAippParam_SetInputShape(HiAI_AippParam* aippParam, uint32_t srcImageW, uint32_t srcImageH);
设置输入图片的原始宽高。
OH_NN_ReturnCode HMS_HiAIAippParam_SetCscConfig(HiAI_AippParam* aippParam, HiAI_ImageFormat inputFormat, HiAI_ImageFormat outputFormat, HiAI_ImageColorSpace space);
设置图片色域转换参数。
OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelSwapConfig(HiAI_AippParam* aippParam, bool rbuvSwapSwitch, bool axSwapSwitch);
设置图片通道交换参数。
OH_NN_ReturnCode HMS_HiAIAippParam_SetCropConfig(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t startPosW, uint32_t startPosH, uint32_t croppedW, uint32_t croppedH);
设置图片裁剪参数。
OH_NN_ReturnCode HMS_HiAIAippParam_SetResizeConfig(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t resizedW, uint32_t resizedH);
设置图片缩放大小参数。
OH_NN_ReturnCode HMS_HiAIAippParam_SetPadConfig(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t leftPadSize, uint32_t rightPadSize, uint32_t topPadSize, uint32_t bottomPadSize);
设置图片左右上下填充的像素数。
OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelPadding(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount);
设置通道填充值。
OH_NN_ReturnCode HMS_HiAIAippParam_SetRotationAngle(HiAI_AippParam* aippParam, uint32_t batchIndex, float rotationAngle);
设置图片旋转参数。
OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMeanPixel(HiAI_AippParam* aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount);
设置图片数据类型转换的通道像素平均值。
OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMinPixel(HiAI_AippParam* aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount);
设置图片数据类型转换的通道像素最小值。
OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcVarReciPixel(HiAI_AippParam* aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount);
设置图片数据类型转换的通道像素方差。
OH_NN_ReturnCode HMS_HiAITensor_SetAippParams(NN_Tensor* tensor, HiAI_AippParam* aippParams[], size_t aippNum);
给输入Tensor设置AIPP参数。
开发步骤
1.
2.
3.
4.  通过构造输入输出Tensor后，调用HMS_HiAITensor_SetAippParams给输入Tensor设置AIPP参数。
示例说明
假定当前有一个模型，训练时采用的训练集为BRG888的图片，使能了动态AIPP之后，可以接收YUYV类型的图片作为模型推理的输入。当用于模型推理的图片尺寸与训练集图片的尺寸不一致时，还可以使用AIPP的裁剪、缩放和填充功能，改变输入图片尺寸。以下示例代码基于NDK接口，使能AIPP的裁剪、缩放和填充等功能，将一张YUYV尺寸为480x480的图片预处理为224x224的输入。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-optimization-V14
爬取时间: 2025-04-30 04:29:25
来源: Huawei Developer
概述
异构是HiAI Foundation提供的异构计算能力，能够使用户App在华为平台上充分享受到硬件平台的计算加速性能，同时提供非华为硬件平台的模型计算兼容性和计算加速，使用户App开发过程归一化，不再需要为不同硬件平台适配不同模型或者计算框架，减少App开发及维护的难度。
异构的原理如下图所示，指定OP1、OP2、OP5~OPn在CPU上进行推理，OP3、OP4在NPU上进行推理。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094335.58575181640617200092363632938110:50001231000000:2800:64FFF6AC2FB5C70FBC736E8F0B048FA8C7DF0113F5F16ABB123CED6389AFC80A.png)
实现异构可以通过在线调优方式，以下为在线调优参数设置接口，接口使用见在线调优开发步骤。如要使用更丰富的设置和查询接口，请参见API参考。
| 接口名  | 描述  |
| --- | --- |
| OH_NN_ReturnCode HMS_HiAIOptions_SetTuningMode(OH_NNCompilation* compilation, HiAI_TuningMode tuningMode);  | 芯片调优模式配置。  |
| OH_NN_ReturnCode HMS_HiAIOptions_SetTuningCacheDir(OH_NNCompilation* compilation, const char* cacheDir);  | 芯片调优缓存目录配置。  |
接口名
描述
OH_NN_ReturnCode HMS_HiAIOptions_SetTuningMode(OH_NNCompilation* compilation, HiAI_TuningMode tuningMode);
芯片调优模式配置。
OH_NN_ReturnCode HMS_HiAIOptions_SetTuningCacheDir(OH_NNCompilation* compilation, const char* cacheDir);
芯片调优缓存目录配置。
在线调优开发步骤
1.
1.  设置好所需调优选项参数后，通过调用OH_NNCompilation_Build，传入创建模型编译实例，即可执行模型编译，编译成功则返回编译后的模型指针。后续流程同模型推理。
在线调优示例说明
以下示例代码设置调优参数SetTuningMode及SetTuningCacheDir，实现在线调优。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-zero-memory-copy-V14
爬取时间: 2025-04-30 04:29:39
来源: Huawei Developer
概述
对于GPU的纹理数据或模型的输入数据等已经存在于ION内存中的场景，就可以使用“内存零拷贝方式”，即将存放数据的ION内存封装为输入输出张量，直接进行推理，不需要进行输入张量和输出张量的数据拷贝，以便节省内存以及推理时间。
使用说明
对于零拷贝使用场景，在模型加载完成后，使用OH_NNTensor_CreateWithFd，将ION内存封装为输入张量“input_tensor”，输出张量"output_tensor"，执行推理。
若size为模型输出大小，对于输出张量，建议用户申请ION内存的大小为。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094335.98212757445854923072108022727642:50001231000000:2800:79E036AABBE9038271160FF51D30EBF07659C6D1D438BF73CE1DF5575C24E43F.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-in-depth-convergence-V14
爬取时间: 2025-04-30 04:29:52
来源: Huawei Developer
模型推理时结合硬件深度融合，减少对DDR的访问，提升能效比。目前仅支持编译前可变shape场景，调用HMS_HiAIOptions_SetTuningStrategy设置模型优化策略为“HIAI_TUNING_STRATEGY_ON_DEVICE_TUNING”。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-app-integration-V14
爬取时间: 2025-04-30 04:30:05
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-single-operator-application-V14
爬取时间: 2025-04-30 04:30:19
来源: Huawei Developer
概述
HiAI Foundation提供独立的算子创建和计算通路，三方框架可以在模型加载、推理过程中，将卷积、深度卷积等算子通过单算子对接的方式迁移至NPU，经过硬件平台的加速计算，与整网模式对比灵活度更高，相比于整网CPU计算性能更优。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094336.82097572445218927438728355475197:50001231000000:2800:89550F67D0CDA2800988E6C4C508F69D105D05DE3807F5DD494ACC3FD5ADD80F.png)
以下为单算子Tensor创建，单算子执行器创建、加载、执行接口，接口使用请参见开发步骤。如要使用更丰富的设置和查询接口，请参见API参考。
| 接口名  | 描述  |
| --- | --- |
| HiAI_SingleOpTensorDesc * HMS_HiAISingleOpTensorDesc_Create (const int64_t *dims, size_t dimNum, HiAI_SingleOpDataType dataType, HiAI_SingleOpFormat format, bool isVirtual);  | 创建HiAI_SingleOpTensorDesc对象。  |
| void HMS_HiAISingleOpTensorDesc_Destroy (HiAI_SingleOpTensorDesc **tensorDesc);  | 释放HiAI_SingleOpTensorDesc对象。  |
| HiAI_SingleOpBuffer * HMS_HiAISingleOpBuffer_Create (size_t dataSize);  | 按照指定的内存大小创建HiAI_SingleOpBuffer对象。  |
| size_t HMS_HiAISingleOpBuffer_GetSize (const HiAI_SingleOpBuffer *buffer);  | 查询HiAI_SingleOpBuffer的字节大小。  |
| void * HMS_HiAISingleOpBuffer_GetData (const HiAI_SingleOpBuffer *buffer);  | 查询HiAI_SingleOpBuffer的内存地址。  |
| OH_NN_ReturnCode HMS_HiAISingleOpBuffer_Destroy (HiAI_SingleOpBuffer **buffer);  | 释放HiAI_SingleOpBuffer对象。  |
| HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromTensorDesc (const HiAI_SingleOpTensorDesc *desc);  | 根据HiAI_SingleOpTensorDesc创建HiAI_SingleOpTensor对象。  |
| HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromConst (const HiAI_SingleOpTensorDesc *desc, void *data, size_t dataSize);  | 根据HiAI_SingleOpTensorDesc、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建HiAI_SingleOpTensor对象。  |
| HiAI_SingleOpTensorDesc * HMS_HiAISingleOpTensor_GetTensorDesc (const HiAI_SingleOpTensor *tensor);  | 获取HiAI_SingleOpTensor的Tensor描述。  |
| HiAI_SingleOpBuffer * HMS_HiAISingleOpTensor_GetBuffer (const HiAI_SingleOpTensor *tensor);  | 获取HiAI_SingleOpTensor的Buffer。  |
| OH_NN_ReturnCode HMS_HiAISingleOpTensor_Destroy (HiAI_SingleOpTensor **tensor);  | 释放HiAI_SingleOpTensor对象。  |
| HiAI_SingleOpOptions * HMS_HiAISingleOpOptions_Create (void);  | 创建HiAI_SingleOpOptions对象。  |
| void HMS_HiAISingleOpOptions_Destroy (HiAI_SingleOpOptions **options);  | 释放HiAI_SingleOpOptions对象。  |
| HiAI_SingleOpDescriptor* HMS_HiAISingleOpDescriptor_CreateConvolution(HiAISingleOpDescriptor_ConvolutionParamvolutionParam param);  | 创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。  |
| void HMS_HiAISingleOpDescriptor_Destroy (HiAI_SingleOpDescriptor **opDesc);  | 释放HiAI_SingleOpDescriptor对象。  |
| HiAI_SingleOpExecutor* HMS_HiAISingleOpExecutor_CreateConvolution(HiAI_SingleOpExecutorConvolutionParam param);  | 创建卷积类算子对应的HiAI_SingleOpExecutor对象。  |
| size_t HMS_HiAISingleOpExecutor_GetWorkspaceSize (const HiAI_SingleOpExecutor *executor);  | 查询HiAI_SingleOpExecutor所需的ION内存工作空间的字节大小。  |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Init (HiAI_SingleOpExecutor *executor, void *workspace, size_t workspaceSize);  | 加载HiAI_SingleOpExecutor。  |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Execute (HiAI_SingleOpExecutor *executor, HiAI_SingleOpTensor *input[], int32_t inputNum, HiAI_SingleOpTensor *output[], int32_t outputNum);  | 执行同步运算推理。  |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Destroy (HiAI_SingleOpExecutor **executor);  | 销毁HiAI_SingleOpExecutor对象，释放执行器占用的内存。  |
接口名
描述
HiAI_SingleOpTensorDesc * HMS_HiAISingleOpTensorDesc_Create (const int64_t *dims, size_t dimNum, HiAI_SingleOpDataType dataType, HiAI_SingleOpFormat format, bool isVirtual);
创建HiAI_SingleOpTensorDesc对象。
void HMS_HiAISingleOpTensorDesc_Destroy (HiAI_SingleOpTensorDesc **tensorDesc);
释放HiAI_SingleOpTensorDesc对象。
HiAI_SingleOpBuffer * HMS_HiAISingleOpBuffer_Create (size_t dataSize);
按照指定的内存大小创建HiAI_SingleOpBuffer对象。
size_t HMS_HiAISingleOpBuffer_GetSize (const HiAI_SingleOpBuffer *buffer);
查询HiAI_SingleOpBuffer的字节大小。
void * HMS_HiAISingleOpBuffer_GetData (const HiAI_SingleOpBuffer *buffer);
查询HiAI_SingleOpBuffer的内存地址。
OH_NN_ReturnCode HMS_HiAISingleOpBuffer_Destroy (HiAI_SingleOpBuffer **buffer);
释放HiAI_SingleOpBuffer对象。
HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromTensorDesc (const HiAI_SingleOpTensorDesc *desc);
根据HiAI_SingleOpTensorDesc创建HiAI_SingleOpTensor对象。
HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromConst (const HiAI_SingleOpTensorDesc *desc, void *data, size_t dataSize);
根据HiAI_SingleOpTensorDesc、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建HiAI_SingleOpTensor对象。
HiAI_SingleOpTensorDesc * HMS_HiAISingleOpTensor_GetTensorDesc (const HiAI_SingleOpTensor *tensor);
获取HiAI_SingleOpTensor的Tensor描述。
HiAI_SingleOpBuffer * HMS_HiAISingleOpTensor_GetBuffer (const HiAI_SingleOpTensor *tensor);
获取HiAI_SingleOpTensor的Buffer。
OH_NN_ReturnCode HMS_HiAISingleOpTensor_Destroy (HiAI_SingleOpTensor **tensor);
释放HiAI_SingleOpTensor对象。
HiAI_SingleOpOptions * HMS_HiAISingleOpOptions_Create (void);
创建HiAI_SingleOpOptions对象。
void HMS_HiAISingleOpOptions_Destroy (HiAI_SingleOpOptions **options);
释放HiAI_SingleOpOptions对象。
HiAI_SingleOpDescriptor* HMS_HiAISingleOpDescriptor_CreateConvolution(HiAISingleOpDescriptor_ConvolutionParamvolutionParam param);
创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。
void HMS_HiAISingleOpDescriptor_Destroy (HiAI_SingleOpDescriptor **opDesc);
释放HiAI_SingleOpDescriptor对象。
HiAI_SingleOpExecutor* HMS_HiAISingleOpExecutor_CreateConvolution(HiAI_SingleOpExecutorConvolutionParam param);
创建卷积类算子对应的HiAI_SingleOpExecutor对象。
size_t HMS_HiAISingleOpExecutor_GetWorkspaceSize (const HiAI_SingleOpExecutor *executor);
查询HiAI_SingleOpExecutor所需的ION内存工作空间的字节大小。
OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Init (HiAI_SingleOpExecutor *executor, void *workspace, size_t workspaceSize);
加载HiAI_SingleOpExecutor。
OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Execute (HiAI_SingleOpExecutor *executor, HiAI_SingleOpTensor *input[], int32_t inputNum, HiAI_SingleOpTensor *output[], int32_t outputNum);
执行同步运算推理。
OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Destroy (HiAI_SingleOpExecutor **executor);
销毁HiAI_SingleOpExecutor对象，释放执行器占用的内存。
开发步骤
以下开发步骤以卷积单算子为例。
1.  如果需要创建卷积算子与激活算子的融合算子执行器，还需要调用HMS_HiAISingleOpDescriptor_CreateActivation，创建激活类算子描述符对象，然后调用HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation创建融合算子执行器。
2.  如果需要创建卷积算子与激活算子的融合算子执行器，还需要调用HMS_HiAISingleOpDescriptor_CreateActivation，创建激活类算子描述符对象，然后调用HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation创建融合算子执行器。
3.
4.
5.  调用HMS_HiAISingleOpExecutor_Execute，执行同步运算推理。
6.
1.  如果需要创建卷积算子与激活算子的融合算子执行器，还需要调用HMS_HiAISingleOpDescriptor_CreateActivation，创建激活类算子描述符对象，然后调用HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation创建融合算子执行器。
示例说明
假定现在有一个深度卷积算子，输入维度为1x8x224x224，输入NCHW格式排布的float32类型数据，准备好NCHW排布的权重与偏置数据，调用单算子接口推理运算获得NCHW格式float32类型的输出可以参考如下示例代码：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-faqs-V14
爬取时间: 2025-04-30 04:30:33
来源: Huawei Developer
判断模型能否在手机上运行？
通过调用接口HMS_HiAICompatibility_CheckFromFile或者HMS_HiAICompatibility_CheckFromBuffer，传入编译后的模型文件或者模型buffer，如果返回“HIAI_COMPATIBILITY_COMPATIBLE”表示兼容性检查通过，模型可以在手机上运行。
如何选择使用同步接口还是异步接口？
由业务场景决定，目前两者均支持，从性能考虑推荐使用异步接口。
推理函数支持的数据格式有哪些？
推理时传入的inputTensor的数据格式当前只支持nchw。
如何处理OMG离线模型输出算子类型错误？
Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则OMG生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094336.97202647677545950815881171103485:50001231000000:2800:F5EF43AC107537FB93557B383C976A69EE124E1631BA47F3464E7484D9AFF232.png)
算法在设计模型时，如何确认哪些算子在HiAI上性能较优？
您可参考Model Zoo中的HiAI算子性能指导，根据需要选择性能较优的算子。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/hiaifoundation-appendixes-V14
爬取时间: 2025-04-30 04:30:46
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-kit-guide-V14
爬取时间: 2025-04-30 04:30:59
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-introduction-V14
爬取时间: 2025-04-30 04:31:12
来源: Huawei Developer
Intents Kit（意图框架服务）是HarmonyOS级的意图标准体系 ，意图连接了应用/元服务内的业务功能。
意图框架能帮开发者将应用/元服务内的业务功能，智能分发到各系统入口，这个过程即智慧分发。其中系统入口包括：小艺对话、小艺搜索、小艺建议。
系统入口、意图框架、鸿蒙生态的关系如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094338.58602764926765897733253807437994:50001231000000:2800:484146EB8DFC3B7EB00B70C7DB5F02BB9FECEF897C7F7908FDD52F739C02D6EB.png)
Intents Kit优势
利用HarmonyOS的大模型、多维设备感知等AI能力，准确且及时地获取到用户显性、潜在意图，从而实现个性化、多模态、精准的智慧分发。
智慧分发
为方便开发者接入，智慧分发提供了多种特性类别，当前已开放习惯推荐、事件推荐、技能调用-语音、本地搜索，后续会陆续开放其他特性类别。每种特性类型支持的典型系统入口、分发逻辑见下表：
| 特性类型  | 系统入口  | 分发逻辑  |
| --- | --- | --- |
| 习惯推荐  | 小艺建议  | 应用或元服务向系统共享意图，系统学习意图规律，在合适的时机推荐服务。比如向系统共享用户浏览资讯意图的数据，经过习惯规律性学习后，小艺建议会合适的时机给用户推荐合适的浏览资讯服务与内容。  |
| 事件推荐  | 小艺建议  | 应用或元服务向系统共享意图，系统提取意图内容中的事件，结合时间、位置等信息向用户推荐提醒服务。比如向系统共享用户购买的电影票订单数据，由系统提取订单数据中的关键特征如时间、位置等，小艺建议会在合适的时机给用户推荐观影提醒服务。  |
| 技能调用-语音  | 小艺对话  | 系统基于AI大模型对理解用户显示或隐性的输入，帮用户完成应用或元服务的功能调用。比如用户在小艺对话中询问“从深圳去北京的飞机要多少钱”，可以理解用户搜索机票的意图，调用应用或元服务提供的搜索机票意图获取机票数据并向用户呈现。  |
| 本地搜索  | 小艺搜索  | 应用或元服务向系统共享意图，系统对意图的实体内容构建本地索引，满足用户搜索的需求。比如向系统共享“华为开发者大会”相关报道资讯后，用户在该入口输入相关关键词，即可将应用或元服务内的资讯内容检索出来。  |
特性类型
系统入口
分发逻辑
习惯推荐
小艺建议
应用或元服务向系统共享意图，系统学习意图规律，在合适的时机推荐服务。比如向系统共享用户浏览资讯意图的数据，经过习惯规律性学习后，小艺建议会合适的时机给用户推荐合适的浏览资讯服务与内容。
事件推荐
小艺建议
应用或元服务向系统共享意图，系统提取意图内容中的事件，结合时间、位置等信息向用户推荐提醒服务。比如向系统共享用户购买的电影票订单数据，由系统提取订单数据中的关键特征如时间、位置等，小艺建议会在合适的时机给用户推荐观影提醒服务。
技能调用-语音
小艺对话
系统基于AI大模型对理解用户显示或隐性的输入，帮用户完成应用或元服务的功能调用。比如用户在小艺对话中询问“从深圳去北京的飞机要多少钱”，可以理解用户搜索机票的意图，调用应用或元服务提供的搜索机票意图获取机票数据并向用户呈现。
本地搜索
小艺搜索
应用或元服务向系统共享意图，系统对意图的实体内容构建本地索引，满足用户搜索的需求。比如向系统共享“华为开发者大会”相关报道资讯后，用户在该入口输入相关关键词，即可将应用或元服务内的资讯内容检索出来。
为了满足更细粒度的分发诉求，每类特性类别下提供多个具体特性，具体特性的分发系统入口、开发依赖见各垂域智慧分发特性列表。具体特性开发依赖的意图相关字段见各垂域意图Schema。
意图的运行逻辑
HarmonyOS、应用/元服务的交互中，意图运行方式分为意图调用和意图共享：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094338.85502314501891402447625872168302:50001231000000:2800:088B849EDD2BCD626FDAEFA3B11C2D109BE016660BC6BBFBF78CF816BD49D797.png)
| “意图”运行方式  | 发起者  | 定义  |
| --- | --- | --- |
| 意图共享  | 应用/元服务  | 指应用/元服务主动向HarmonyOS共享意图，可用于HarmonyOS构建本地内容索引、学习用户的行为规律，以支持本地搜索和主动建议。 意图共享包含动作和实体两个部分，动作支持完成时和将来时两种机制。 完成时：用户意图已执行，共享的数据可用于本地搜索和系统建议。将来时：意图是基于用户行为预测的，共享的数据可用于本地搜索。 意图框架还支持开发者向系统进行辅助实体共享，例如位置信息等，用于场景推荐和其他智慧分发功能的增强。  |
| 意图调用  | HarmonyOS  | 指HarmonyOS主动调用应用/元服务的功能。 用户在系统入口输入信息或者系统主动推荐后，系统可向应用/元服务发起意图调用，例如播放音乐、查看旅游攻略、搜索视频等。  |
“意图”运行方式
发起者
定义
意图共享
应用/元服务
指应用/元服务主动向HarmonyOS共享意图，可用于HarmonyOS构建本地内容索引、学习用户的行为规律，以支持本地搜索和主动建议。
意图共享包含动作和实体两个部分，动作支持完成时和将来时两种机制。
意图框架还支持开发者向系统进行辅助实体共享，例如位置信息等，用于场景推荐和其他智慧分发功能的增强。
意图调用
HarmonyOS
指HarmonyOS主动调用应用/元服务的功能。
用户在系统入口输入信息或者系统主动推荐后，系统可向应用/元服务发起意图调用，例如播放音乐、查看旅游攻略、搜索视频等。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-access-flow-V14
爬取时间: 2025-04-30 04:31:26
来源: Huawei Developer
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094338.27517350471256864214633872910041:50001231000000:2800:0A51ADDB9C95E7943C82E0C3A8F7547239C4E2BD22DFF2CCA595ED3C5D6C0B51.png)
| 阶段  | 任务  | 任务描述  | 示例  | 指导文档  |
| --- | --- | --- | --- | --- |
| 意向  | 选择特性确定意图  | 开发者在已发布的特性列表中根据想达成的用户体验选择特性，根据特性来确定需实现的意图。  | 开发者想实现“歌曲续听推荐”的特性，则根据智慧分发特性描述，需要实现“播放歌曲”意图。  | 歌曲续听推荐  |
| 开发  | 调试白名单申请  | 确定开发意向后，开发者发送邮件到邮箱（hagservice@huawei.com）或者联系华为意图框架接口同事，向华为提供测试应用的信息，用于申请调试白名单。  | 1. 应用名称：华为音乐。 2. AppID：1234567。 3. 申请接入意图：“播放歌曲”。 4. 调试设备ID：1234567。 ......  | 见各特性类型 习惯推荐：开发者测试方案 事件推荐：开发者测试方案  |
| 端侧意图调用调试工具申请  | 华为可提供调试工具，用于开发者自验证端侧意图调用。若需申请工具使用，请开发者联系华为意图框架接口同事，向华为提供接收调试工具的公司人员信息。  | 1.公司全称：xxx技术有限公司 2.接收人姓名：张三 3.接收人邮箱：zhangsan@xxx.com  | 见各特性类型 习惯推荐：开发者测试方案 事件推荐：开发者测试方案  |
| 意图声明文件中注册意图  | 在DevEco Studio中开发时，注册对应的意图。  | 注册“播放歌曲”意图。  | 意图注册  |
| 开发实现意图调用/意图共享  | 开发应用/元服务的意图共享接口，使其可以通过HarmonyOS接口完成意图数据共享。  | 开发“播放歌曲”意图中的意图共享接口。  | 端侧意图共享  |
| 开发应用/元服务的意图调用接口，使其可以通过HarmonyOS接口被正确调用。  | 开发“播放歌曲”意图中的意图调用接口。  | 端侧意图调用  |
| 验证  | 端到端验证特性  | 使用华为侧提供的测试能力完成目标特性的端到端联调测试，联调测试完成后，提交智慧分发配置至审核。  | 在设备上对应入口进行“华为音乐-歌曲续听推荐”的特性端到端测试，测试完成后点击提交智慧分发配置。  | -  |
| 上架  | 应用市场上架软件包（应用/元服务）  | 开发完成并打包好软件包后，在应用市场上传软件包。  | 打包“华为音乐”软件包并通过应用市场上架。  | 应用市场上架流程  |
| 意图框架注册  | 在小艺开放平台进行意图注册配置并提交审核。由华为工程师审核，一般情况在3个工作日内完成。  | 注册“播放歌曲”意图。  | 意图框架上架配置指导  |
阶段
任务
任务描述
示例
指导文档
意向
选择特性确定意图
开发者在已发布的特性列表中根据想达成的用户体验选择特性，根据特性来确定需实现的意图。
开发者想实现“歌曲续听推荐”的特性，则根据智慧分发特性描述，需要实现“播放歌曲”意图。
歌曲续听推荐
开发
调试白名单申请
确定开发意向后，开发者发送邮件到邮箱（hagservice@huawei.com）或者联系华为意图框架接口同事，向华为提供测试应用的信息，用于申请调试白名单。
1. 应用名称：华为音乐。
2. AppID：1234567。
3. 申请接入意图：“播放歌曲”。
4. 调试设备ID：1234567。
......
见各特性类型
习惯推荐：开发者测试方案
事件推荐：开发者测试方案
端侧意图调用调试工具申请
华为可提供调试工具，用于开发者自验证端侧意图调用。若需申请工具使用，请开发者联系华为意图框架接口同事，向华为提供接收调试工具的公司人员信息。
1.公司全称：xxx技术有限公司
2.接收人姓名：张三
3.接收人邮箱：zhangsan@xxx.com
见各特性类型
习惯推荐：开发者测试方案
事件推荐：开发者测试方案
意图声明文件中注册意图
在DevEco Studio中开发时，注册对应的意图。
注册“播放歌曲”意图。
意图注册
开发实现意图调用/意图共享
开发应用/元服务的意图共享接口，使其可以通过HarmonyOS接口完成意图数据共享。
开发“播放歌曲”意图中的意图共享接口。
端侧意图共享
开发应用/元服务的意图调用接口，使其可以通过HarmonyOS接口被正确调用。
开发“播放歌曲”意图中的意图调用接口。
端侧意图调用
验证
端到端验证特性
使用华为侧提供的测试能力完成目标特性的端到端联调测试，联调测试完成后，提交智慧分发配置至审核。
在设备上对应入口进行“华为音乐-歌曲续听推荐”的特性端到端测试，测试完成后点击提交智慧分发配置。
-
上架
应用市场上架软件包（应用/元服务）
开发完成并打包好软件包后，在应用市场上传软件包。
打包“华为音乐”软件包并通过应用市场上架。
应用市场上架流程
意图框架注册
在小艺开放平台进行意图注册配置并提交审核。由华为工程师审核，一般情况在3个工作日内完成。
注册“播放歌曲”意图。
意图框架上架配置指导

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-habit-rec-V14
爬取时间: 2025-04-30 04:31:39
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-habit-rec-introduction-V14
爬取时间: 2025-04-30 04:31:53
来源: Huawei Developer
习惯推荐是HarmonyOS学习用户的行为习惯后做出的主动预测推荐。
以听音乐为例，意图框架设计了统一的意图——播放歌单意图，该意图可以让应用/元服务与HarmonyOS交互。
当用户使用应用/元服务播放歌单时，应用/元服务可以向Intents Kit共享该意图，并提供一些用于学习的特征，例如播放开始/结束时间、播放时长、歌单名等。HarmonyOS会结合底层采集的时间、空间、设备状态等数据共同理解用户行为上下文。最后HarmonyOS结合应用/元服务历史上共享过的数据重建响应意图任务并进行预测推荐，例如在用户每天早上上车后，为其推荐“每日推荐”歌单卡片，用户点击实现一键播放。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-habit-rec-scene-experience-V14
爬取时间: 2025-04-30 04:32:06
来源: Huawei Developer
典型场景
当前习惯推荐可在小艺建议入口分发，在不同垂域中，填充功能详细参数或内容的逻辑不同，主要典型场景可分为常用接续、常用复访、常用推新三类。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094339.14964855992528196866078976062878:50001231000000:2800:31800A06484CC4019F79E3591C9ADDE747FD9C4F9EF077FFC51405F8097D74BD.png)
以常看视频续播为例，系统预测当前用户使用华为视频的播放视频功能概率较高，会选择用户最近观看且还没看完的视频内容来补充功能细节，在小艺建议中以模板卡形式推荐展示，用户点击卡片后，实现一步跳转进应用的视频播放页。
卡片展示效果
意图框架提供各垂域习惯推荐在小艺建议中展示使用的标准模板卡片，开发者无需开发展示卡片。在展示模板上，会展示应用/元服务名称与logo和内容必要信息，比如音乐名、音乐图片，这类参数需要开发者共享到系统。
以下为播放歌曲-习惯推荐的卡片示例。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094339.57692522264772423779799708057156:50001231000000:2800:39D84BDCA6A4180F176383321EF010E0079B243D4FC3A3F54FD0B69BB33108D7.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-habit-rec-access-programme-V14
爬取时间: 2025-04-30 04:32:19
来源: Huawei Developer
方案概述
当用户在应用/元服务内使用功能时，开发者需要按照标准意图Schema向系统共享行为数据，并支持意图调用（空调用与传参调用），以实现用户点击模板卡后跳转回对应页面。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094339.92739924218405871399081572688671:50001231000000:2800:F24B2DD6416160B50900A1C38E9F0D2718176D8293BFB2563416F449240E3265.png)
意图注册
以歌曲续听推荐特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见各垂域意图Schema。开发者需要编辑对应的意图配置 PROJECT_HOME/entry/src/main/resources/base/profile/insight_intent.json文件，实现意图注册。
```json
{
// 应用支持的意图列表
// 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
"insightIntents": [
{
// 意图名称
// 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
// 应用内意图名称唯一，不允许出现相同的名称定义
"intentName": "PlayMusic",
// 意图所属的垂域
"domain": "MusicDomain",
// 意图版本号
// 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
"intentVersion": "1.0.1",
// 意图调用逻辑入口
// 根据意图调用文件实际路径和实际名称进行填写，此处文件仅做示意
"srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
"uiAbility": {
// 意图所在module、ability，以及代码相对路径入口
"ability": "EntryAbility",
// UIAbility支持前后台两种执行模式
"executeMode": [
"background",
"foreground"
]
}
}
]
}
```
端侧意图共享
构建意图对象，并且调用shareIntent()，实现意图共享。可同时构建多个PlayMusic或PlayMusicList的意图对象。
PlayMusic的意图共享字段定义见各垂域意图Schema定义，代码示例如下：
```typescript
import { insightIntent } from '@kit.IntentsKit';
let playMusicIntent: insightIntent.InsightIntent = {
intentName: "PlayMusic",
intentVersion: "1.0",
identifier: "52dac3b0-6520-4974-81e5-25f0879449b5",
intentActionInfo: {
actionMode: "EXECUTED",
executedTimeSlots: {
executedStartTime: 1637393212000,
executedEndTime: 1637393112000,
},
currentPercentage: 50,
},
intentEntityInfo: {
entityName: "Music",
entityId: "C10194368",
entityGroupId: "C10194321312",
displayName: "测试歌曲1",
description: "NA",
logoURL: "https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png",
keywords: ["华为音乐", "化妆"],
rankingHint: 99,
expirationTime: 1637393212000,
metadataModificationTime: 1637393212000,
activityType: ["1", "2", "3"],
artist: ["测试歌手1", "测试歌手2"],
lyricist: ["测试词作者1", "测试词作者2"],
composer: ["测试曲作者1", "测试曲作者2"],
albumName: "测试专辑",
duration: 244000,
playCount: 100000,
musicalGenre: ["流行", "华语", "金曲", "00后"],
isPublicData: false,
}
}
```
完整的意图共享示例如下所示，该示例构建了一个PlayMusic意图，并进行了shareIntent调用。
端侧意图调用
意图执行组件为uiAbility的意图调用
如上文意图注册，当开发者注册的意图承载的运行组件为uiAbility时，开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）的能力，PlayMusic的意图调用字段定义见各垂域意图Schema。
步骤如下：
```typescript
import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
/**
* 意图调用样例
*/
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
private static readonly PLAY_MUSIC = 'PlayMusic';
/**
* override 执行前台UIAbility意图
*
* @param name 意图名称
* @param param 意图参数
* @param pageLoader 窗口
* @returns 意图调用结果
*/
onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
Promise<insightIntent.ExecuteResult> {
//根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
switch (name) {
case InsightIntentExecutorImpl.PLAY_MUSIC:
return this.playMusic(param, pageLoader);
default:
break;
}
return Promise.resolve({
code: -1,
result: {
message: 'unknown intent'
}
} as insightIntent.ExecuteResult)
}
/**
* 实现调用播放歌曲功能
*
* @param param 意图参数
* @param pageLoader 窗口
*/
private playMusic(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
return new Promise((resolve, reject) => {
let para: Record<string, string> = {
'result': JSON.stringify(param)
};
let localStorage: LocalStorage = new LocalStorage(para);
// TODO 实现意图调用，loadContent的入参为歌曲落地页路径，例如：pages/Index
pageLoader.loadContent('pages/Index', localStorage)
.then(() => {
let entityId: string = (param.items as Array<object>)?.[0]?.['entityId'];
// TODO 调用成功的情况，此处可以打印日志
resolve({
code: 0,
result: {
message: 'Intent execute succeed'
}
});
})
.catch((err: BusinessError) => {
// TODO 调用失败的情况
resolve({
code: -1,
result: {
message: 'Intent execute failed'
}
})
});
})
}
}
```
意图执行组件为form的意图调用
如上文意图注册，当开发者注册的意图承载的运行组件为form（运行组件FormExtensionAbility）时，则需要开发者在实现的FormExtensionAbility中从want中获取并解析意图名和执行参数，用于卡片展示。
步骤如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-habit-rec-dp-self-validation-V14
爬取时间: 2025-04-30 04:32:33
来源: Huawei Developer
意图框架向开发者提供真机测试能力，即开发者可连接设备进行调测。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS NEXT设备上面进行自验证，打磨体验。真机测试分为三个步骤：基础信息提供，环境准备，联调验证。
基础信息提供
达成开发意向后，开发者发送邮件到邮箱（hagservice@huawei.com）或者联系华为意图框架接口同事，向华为提供测试应用的信息。
| 序号 | 基础信息 | 描述 |
| --- | --- | --- |
| 1 | 应用名称 | 应用市场上架的应用名称。 |
| 2 | 应用包名 | 应用市场上架的应用包名。 |
| 3 | 接入意图名称 | 开发者意向接入的意图名称（中英文）。 |
| 4 | 应用图标 | 应用的图标，具体要求如下： 图标背景：非透明。 比例&尺寸：1:1，72px*72px。 大小：不超过1M。 格式：png、jpg、jpeg。 |
| 5 | APP ID | 登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 应用-APP ID”中获取。 |
| 6 | Client ID | 登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 应用 > OAuth 2.0客户端ID(凭据) > Client ID”中获取。 |
| 7 | 华为账号（UID） | 开发者用于调试的华为账号；登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 开发者 > developer ID"中获取。 |
| 8 | 设备ID | 开发者用于调试的设备ID；开启设备的意图框架测试开关(测试设备路径：设置 -> 系统 -> 开发者选项 -> 意图框架调试)，界面展示的意图框架测试ID。 |
序号
基础信息
描述
1
应用名称
应用市场上架的应用名称。
2
应用包名
应用市场上架的应用包名。
3
接入意图名称
开发者意向接入的意图名称（中英文）。
4
应用图标
应用的图标，具体要求如下：
图标背景：非透明。
比例&尺寸：1:1，72px*72px。
大小：不超过1M。
格式：png、jpg、jpeg。
5
APP ID
登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 应用-APP ID”中获取。
6
Client ID
登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 应用 >OAuth 2.0客户端ID(凭据)>Client ID”中获取。
7
华为账号（UID）
开发者用于调试的华为账号；登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 开发者 > developer ID"中获取。
8
设备ID
开发者用于调试的设备ID；开启设备的意图框架测试开关(测试设备路径：设置 -> 系统 -> 开发者选项 -> 意图框架调试)，界面展示的意图框架测试ID。
环境准备
准备一台装有HarmonyOS Next版本的手机设备，系统版本最低要求为 Developer Beta 3。需要按照以下顺序依次执行，不能更换执行顺序。
1.
2.
3.
4.
5.  【提示】如果出现意图框架调试打开后，设备长时间无法出现“已切换至真机模式”或者出现“已切换至真机模式”但没有包名的时候，可以尝试以下操作：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094340.68634411587234667652173816081367:50001231000000:2800:53F8A7B03756C06A21BC8310181053EC57FAE22D04C79BF8B5611D44B33FD9DE.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094340.67162449770883435126009884680968:50001231000000:2800:A379771022D7F91FBDE5781198A5EAA3FE4BCE49166FBCB993A4A1370C0CB3AD.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094340.90446368117446180847206602078037:50001231000000:2800:076A8335D4BC40647A3DA1CA718DC0CEFE709440477A8F6DB855926E6BCF6FE9.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094340.49862309564786763008253940267157:50001231000000:2800:BBBDEFF71825EF1CE3E847264D9C869CAF41F946239C28535DAFC040C1393A34.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094340.37867101390576725351169438287931:50001231000000:2800:C9CB21230D54C78D0562F1695F60CA7834B2090491CEC2B6695CD764CB534CF2.png)
联调验证
1.  【举例】某音乐APP接入意图框架音乐续播的特性。通过播放某一首歌曲的用户操作，触发某音乐APP调用系统接口shareIntent()。某音乐APP的开发者通过日志确认shareIntent()接口调用成功，则可以认为某音乐APP本次意图共享是成功的。
2.  【提示】重复意图共享和卡片渲染两步，可以触发卡片上文字元素和图片元素的刷新。
端云结合的习惯推荐
涉及习惯推荐叠加上云搜索场景的开发者优先完成习惯推荐在设备上联调，确保测试应用的意图共享和意图调用的业务逻辑正确。后端接口开发完毕，需自行检查接口的出参是否满足意图框架云侧接口规范。以上两步完成之后，可联系华为意图框架接口同事提交后端接口文档，华为同事会配合开发者进行联调。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-event-rec-V14
爬取时间: 2025-04-30 04:32:47
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-event-rec-introduction-V14
爬取时间: 2025-04-30 04:33:00
来源: Huawei Developer
事件推荐是应用/元服务有新的动态产生且满足推荐规则时给用户做出的主动推荐。实现事件推荐需要开发者将事件信息共享给意图框架，当满足事件推送规则时，会在小艺建议入口向指定用户推荐该事件提醒卡片，也支持通过对话或关键字搜索的方式查询事件内容状态。
事件根据是否指定用户ID可分为两种：用户事件和公共事件。
用户事件：由用户主动行为触发，根据用户标识对某一个指定用户ID单独进行推送或某一批指定用户ID批量进行推送。例如，附近优惠服务向智慧分发平台推送某用户购买了某优惠券的事件，意图框架在优惠券到期前X天提醒该用户优惠券即将到期。
公共事件：不指定用户ID推送的事件，将向同一画像的人群进行推送。例如，气象局将台风预警事件共享给意图框架，意图框架在台风到达前3天，将台风预警事件推送给可能受台风影响的用户群。公共事件包括灾害或故障警示警告、节目安排、赛事赛程等信息。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-event-rec-scene-experience-V14
爬取时间: 2025-04-30 04:33:14
来源: Huawei Developer
典型场景
事件推荐典型场景包括：
各垂域也可根据垂域的实际情况定义具体的事件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094341.95082954681846178277170966727315:50001231000000:2800:6C8757D7036A689FBD2E6CC179BB23DDF13B7B2E94C21BC4E4985C076C0ABC2A.png)
电影开场提醒为例，用户在应用/元服务中购买了电影票，在电影开场前半小时（具体生效时间将根据具体垂域的情况和用户最佳体验确定），用户可在小艺建议入口看到电影取票提醒的卡片，点击卡片可跳转到应用/元服务的订单详情页，用户可在该页面完成电影取票。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094341.86632912500942386879355594877072:50001231000000:2800:A9908DABE3F4D35280691212E2109AFDE835E4BC05E55BC5E4242BAC67526462.png)
卡片展示效果
意图框架将提供系统标准的事件模板卡片，无需开发者开发，开发者只需按照具体垂域事件的意图Schema将事件推送至智慧分发平台服务器即可。各垂域事件卡片样式的示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094341.71766200848812571870306504891855:50001231000000:2800:CF1801E6D5D4C61D23F52B3CD2DA5C9F017DB79AC485129AA7BF24E5CF798590.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-event-rec-access-programme-V14
爬取时间: 2025-04-30 04:33:27
来源: Huawei Developer
方案概述
当开发者有事件想要通知到用户时，可通过应用/元服务的云侧服务器向智慧分发平台推送事件内容（意图共享）。系统通过智慧决策判断事件发生的条件，在满足条件时，向用户推荐事件提醒卡片，当用户点击卡片后，可跳转到应用/元服务的详情页查看事件详情（意图调用）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094341.76131319378052217615470307028458:50001231000000:2800:CE020DF1A607C4864001DD21A77E07FC1E39EE389655E063589C367FC7A950E6.png)
流程图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094341.46712517052460675544960899287263:50001231000000:2800:2CFFD0AD8779D9B153F5C4B52AD35AD5EB24A6CA9455412DA6DA3EAF65BE9828.png)
意图注册
以还款待办事件提醒特性为例，首先要注册查看还款意图（ViewRepayment），详见各垂域意图Schema。开发者需要编辑对应的意图配置#PROJECT_HOME/entry/src/main/resources/base/profile/insight_intent.json文件，实现意图注册。
```json
{
// 应用支持的意图列表
// 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
"insightIntents": [
{
// 意图名称
// 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
// 应用内意图名称唯一，不允许出现相同的名称定义
"intentName": "ViewRepayment",
// 意图所属的垂域
"domain": "BankingDomain",
// 意图版本号
// 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
"intentVersion": "1.0.1",
// 意图调用逻辑入口
"srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
"uiAbility": {
// 意图所在module、ability，以及代码相对路径入口
"ability": "EntryAbility",
// UIAbility支持前后台两种执行模式
"executeMode": [
"background",
"foreground"
]
}
}
]
}
```
获取SID
API文档参见：意图框架API参考 > getSid。
```typescript
import { insightIntent } from '@kit.IntentsKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 根据实际代码上下文自行传入合适的context
insightIntent.getSid(context, false) // 优先获取缓存SID，改为true则强制从云侧获取新SID
.then((sid: string) => {
// 获取SID成功
console.info('getSid succeed!');
}).catch((error: BusinessError) => {
// 获取SID失败
console.error(`getSid failed! error=${error.code} reason=${error.message}`);
});
```
云侧意图共享
服务上架配置
云侧意图需要服务承载，需要先在AppGallery Connect上架应用/元服务，然后在小艺开放平台配置意图，具体步骤如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094341.77404931123246046746638938959085:50001231000000:2800:283C88EEB1234C92C46DF49431C054177B12273F683DB63AB5ACB4BA493F43F6.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094341.22320659038895516380462657349947:50001231000000:2800:6079F1B9436816A8958B03A45C2679AB9E6D65AB5260D5AA2433F7B79370805F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094342.99853778717965788729794788366522:50001231000000:2800:BB4A1C0535F982F07F9E83A0676A25650EF53B39C2B12881106DAAC2B74943B4.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094342.42559636923629694924474970582479:50001231000000:2800:B12A2607A5DD75EA775C963B3C19344CEBA365A6760A26D8E643DC37B8765A5F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094342.89539243921872583520221176770096:50001231000000:2800:C1A1B390654A9D1DC467A6E2FDCF676B02E47AA0A2D74143A622BC6346250BC4.png)
服务上架配置完成后，进入意图共享和意图调用环节。
意图共享接口调用
应用/元服务通过云侧意图共享接口，把对应意图的相关事件数据共享给Intents Kit，用于事件提醒服务。
事件撤销接口调用
当应用/元服务共享的意图相关事件数据超过时效期，Intents Kit需要通过云侧事件撤销接口把相关事件数据撤销，以避免触发超过时效期的事件提醒。
端侧意图调用
开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）的能力，ViewRepayment的意图调用字段定义见对应垂域意图Schema定义表。
步骤如下：
```typescript
import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
/**
* 意图调用样例 */
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
private static readonly VIEW_REPAYMENT = 'ViewRepayment';
/**
* override 执行前台UIAbility意图
*
* @param name 意图名称
* @param param 意图参数
* @param pageLoader 窗口
* @returns 意图调用结果
*/
onExecuteInUIAbilityForegroundMode(intentName: string, param: Record<string, Object>, pageLoader: window.WindowStage):
Promise<insightIntent.ExecuteResult> {
// 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
switch (intentName) {
case InsightIntentExecutorImpl.VIEW_REPAYMENT:
return this.viewRepayment(param, pageLoader);
default:
break;
}
return Promise.resolve({
code: -1,
result: {
message: 'unknown intent'
}
} as insightIntent.ExecuteResult)
}
/**
* 实现调用查看还款功能
*
* @param param 意图参数
* @param pageLoader 窗口
*/
private viewRepayment(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
return new Promise((resolve, reject) => {
let para: Record<string, string> = {
'result': JSON.stringify(param)
};
let localStorage: LocalStorage = new LocalStorage(para);
// TODO 实现意图调用，loadContent的入参为查看还款落地页路径，例如：'pages/Index'
pageLoader.loadContent('pages/Index', localStorage)
.then(() => {
let entityId: string = (param.items as Array<object>)?.[0]?.['entityId'];
// TODO 调用成功的情况，此处可以打印日志
resolve({
code: 0,
result: {
message: 'Intent execute succeed'
}
});
})
.catch((err: BusinessError) => {
// TODO 调用失败的情况
resolve({
code: -1,
result: {
message: 'Intent execute failed'
}
})
});
})
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-event-rec-dp-self-validation-V14
爬取时间: 2025-04-30 04:33:40
来源: Huawei Developer
意图框架向开发者提供真机测试能力，即开发者可连接设备进行调测。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS NEXT设备上面进行自验证，打磨体验。真机测试分为三个步骤：基础信息提供，环境准备，联调验证。
基础信息提供
达成开发意向后，开发者发送邮件到邮箱（hagservice@huawei.com）或者联系华为意图框架接口同事，向华为提供测试应用的信息。
| 序号  | 基础信息  | 描述  |
| --- | --- | --- |
| 1  | 应用名称  | 应用市场上架的应用名称。  |
| 2  | 应用包名  | 应用市场上架的应用包名。  |
| 3  | 接入意图名称  | 开发者意向接入的意图名称（中英文）。  |
| 4  | 应用图标  | 应用的图标，具体要求如下： 图标背景：非透明。 比例&尺寸：1:1，72px*72px。 大小：不超过1M。 格式：png、jpg、jpeg。  |
| 5  | APP ID  | 登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 应用-APP ID”中获取。  |
| 6  | Client ID  | 登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 应用 > OAuth 2.0客户端ID(凭据) > Client ID”中获取。  |
| 7  | 华为账号（UID）  | 开发者用于调试的华为账号；登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 开发者 > developer ID"中获取。  |
| 8  | 设备ID  | 开发者用于调试的设备ID；开启设备的意图框架测试开关(测试设备路径：设置 -> 系统 -> 开发者选项 -> 意图框架调试)，界面展示的意图框架测试ID。  |
序号
基础信息
描述
1
应用名称
应用市场上架的应用名称。
2
应用包名
应用市场上架的应用包名。
3
接入意图名称
开发者意向接入的意图名称（中英文）。
4
应用图标
应用的图标，具体要求如下：
图标背景：非透明。
比例&尺寸：1:1，72px*72px。
大小：不超过1M。
格式：png、jpg、jpeg。
5
APP ID
登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 应用-APP ID”中获取。
6
Client ID
登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 应用 >OAuth 2.0客户端ID(凭据)>Client ID”中获取。
7
华为账号（UID）
开发者用于调试的华为账号；登录华为开发者联盟，在“我的项目 > 项目设置 > 常规 > 开发者 > developer ID"中获取。
8
设备ID
开发者用于调试的设备ID；开启设备的意图框架测试开关(测试设备路径：设置 -> 系统 -> 开发者选项 -> 意图框架调试)，界面展示的意图框架测试ID。
环境准备
准备一台装有HarmonyOS Next版本的手机设备，系统版本最低要求为 Developer Beta 3。需要按照以下顺序依次执行，不能更换执行顺序。
1.
2.
3.
4.
5.  【提示】如果出现意图框架调试打开后，设备长时间无法出现“已切换至真机模式”或者出现“已切换至真机模式”但没有包名的时候，可以尝试以下操作：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094343.55881308697457622849330803303394:50001231000000:2800:4FFDDAF5490A097E3F8ED127F097C59DF1B59D3C9FC197FB275779F11150917D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094343.93063156783433688046810803584508:50001231000000:2800:65946BEAE954B8A9865CC3CB3E94D0BCBED155C915896A3AFF763E9299719BE2.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094343.58568578093062110285702558845762:50001231000000:2800:0CB98ED031D5952470C32DFE976F9A79F53CAFF59A75F1FF1AA646E44AE1BDD5.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094343.82143732064692443240487274455050:50001231000000:2800:7EFE618495BB701CD6044ED1845B597044CB31E467C26873849A3D8862CDB75A.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094343.50016165294583448198909520504185:50001231000000:2800:D67D7D020179D08A9B25E44A32147CF72E7DA42DCD68D0579D27CAC5724AF048.png)
联调验证
1.  【举例】某出行类APP接入意图框架航班提醒的特性。用户通过APP购买了机票，触发开发者云调用华为事件通知接口（https://insightintent-simenv.cloud.huawei.com/open-ability/v2/service-events/notify），将用户航班事件推送至华为云，接口响应成功。
2.  【举例】航班提醒是提前24小时提醒用户，如果用户航班起飞时间是8月15日20:00，则8月14号20:00起可查询到该事航班信息，在此之前无法查询到信息。
3.  【举例】点击小艺建议卡片中的模板卡片，会跳转至该用户的购票详情页面。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-skill-all-rec-V14
爬取时间: 2025-04-30 04:33:54
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-skill-all-rec-introduction-V14
爬取时间: 2025-04-30 04:34:07
来源: Huawei Developer
技能调用是意图框架依托系统AI多模态大模型能力做深度用户输入理解，并通过解析的用户意图对接应用或元服务内的功能和内容。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-skill-all-rec-scene-experience-V14
爬取时间: 2025-04-30 04:34:20
来源: Huawei Developer
用户通过对小艺对话进行自然语言输入实现内容查询，知识问答，以及通过对图片选定识别问答进行服务获取。技能调用场景分为两种：
典型场景
功能服务类
信息交互类

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-skill-all-rec-access-programme-V14
爬取时间: 2025-04-30 04:34:34
来源: Huawei Developer
方案概述
开发者需要按照意图定义，进行意图注册并实现意图调用；用户通过对小艺对话进行自然语言输入，小艺理解语义转换成意图调用（含意图参数），执行意图调用实现对应交互体验。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094344.30327231202263676306151021077631:50001231000000:2800:21E52E78E3F5CF289F4E819C876A8E6059B8E507F2BB92EF14714DA48C3E1CF6.png)
端侧意图注册
以“搜索旅游攻略”特性为例，开发者首先要注册“查看旅游攻略”（ViewTravelGuides），其他意图见各垂域意图Schema。开发者需要编辑对应的意图配置PROJECT_HOME/entry/src/main/resources/base/profile/insight_intent.json文件，实现意图注册。
```json
{
"insightIntents": [
{
"intentName": "ViewTravelGuides",
"domain": "TravelDomain",
"intentVersion": "1.0.1",
"srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
"uiAbility": {
"ability": "EntryAbility",
"executeMode": [
"background",
"foreground"
]
},
"uiExtension": {
"ability": "insightIntentUIExtensionAbility"
}
}
]
}
```
| 字段 | 说明 | 约束 |
| --- | --- | --- |
| insightIntents | 应用支持的意图API列表 | 必须声明应用支持插件包含的必选API，应用上架时会进行校验。 |
| intentName | 意图API名称 |   名称应当遵循意图框架规范，当前仅支持预置意图API，不允许自定义。 应用内意图名称唯一，不允许出现相同的名称定义。  |
| domain | 意图所属的垂域 | - |
| intentVersion | 意图API版本号 | 意图引用API时会校验该版本号，只有和意图定义的版本号一致才能正常调用。具体版本定义参考预置意图API。 |
| srcEntry | 意图API入口代码文件相对路径 | 根据意图API实现业务文件填写。 |
| uiAbility | UIAbility执行配置 | 提供意图执行的前台界面或后台无界面执行时需要进行声明配置。 |
| uiExtension | InsightIntentUIExtensionAbility执行配置 | 提供意图执行的窗口化界面时需要进行声明配置。 |
| ability | 意图调用API所在ability名称 | 本意图API所在的实现ability名称，可根据实际业务命名。 |
| executeMode | 意图执行支持的模式 | 在UIAbility组件中特有属性，包含如下枚举值：  background：后台执行，指UIAbility组件的后台执行（无界面）。 foreground：前台执行，指UIAbility组件的前台执行（界面）。  |
字段
说明
约束
insightIntents
应用支持的意图API列表
必须声明应用支持插件包含的必选API，应用上架时会进行校验。
intentName
意图API名称
domain
意图所属的垂域
-
intentVersion
意图API版本号
意图引用API时会校验该版本号，只有和意图定义的版本号一致才能正常调用。具体版本定义参考预置意图API。
srcEntry
意图API入口代码文件相对路径
根据意图API实现业务文件填写。
uiAbility
UIAbility执行配置
提供意图执行的前台界面或后台无界面执行时需要进行声明配置。
uiExtension
InsightIntentUIExtensionAbility执行配置
提供意图执行的窗口化界面时需要进行声明配置。
ability
意图调用API所在ability名称
本意图API所在的实现ability名称，可根据实际业务命名。
executeMode
意图执行支持的模式
在UIAbility组件中特有属性，包含如下枚举值：
端侧前台意图调用
开发者需自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面，如旅游攻略落页面）的能力，ViewTravelGuides的意图调用字段定义见查看旅游攻略 （ViewTravelGuides）。
步骤如下：
端侧前台窗口意图调用
开发者需自己实现InsightIntentExecutor，并在对应回调实现窗口页面内容加载的能力。
步骤如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-search-rec-V14
爬取时间: 2025-04-30 04:34:47
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-search-rec-introduction-V14
爬取时间: 2025-04-30 04:35:01
来源: Huawei Developer
本地搜索是在HarmonyOS归一化搜索特性，开发者将应用/元服务内的功能和内容通过意图框架共享到HarmonyOS，即可实现“一步搜索，内容直达”。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-search-rec-scene-experience-V14
爬取时间: 2025-04-30 04:35:14
来源: Huawei Developer
典型场景
以“音乐垂域”的“歌曲本地搜索”特性为例，当用户在使用音乐应用/元服务产生行为时，应用/元服务可以将音乐的数据通过意图框架API接口共享到HarmonyOS。这里的音乐数据可以是用户收听过的歌曲，也可以是应用/元服务预测用户感兴趣的歌曲，那么后续用户在小艺搜索入口中搜索歌名时，系统将会在应用/元服务共享的数据中检索对应内容，并使用卡片的形式展示内容结果，当用户点击对应卡片热区时，可以跳转进具体音乐播放页或者直接后台执行播放。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094344.32959257322738643981592250361645:50001231000000:2800:DA8868385DAB55FF9059A01136213E15ABD990BE1F3907F22F576A4195CD030E.png)
卡片展示效果
意图框架提供各垂域在小艺搜索展示使用的标准模板卡片，开发者无需开发展示卡片。模板卡片包含应用/元服务和内容必要信息，比如歌曲名称、歌曲封面图、歌曲描述，这类参数需要开发者共享到系统。各垂域适用的风格卡片不同，以实际特性场景要求为准。以下为歌曲本地搜索的模板卡样式的示例：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094344.35360390490100989327124189425592:50001231000000:2800:999ACE312736F64A0FDDA1F3952E3B9AA4AB1437CC0F0DE10DB67B5C68503F79.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-search-rec-access-programme-V14
爬取时间: 2025-04-30 04:35:27
来源: Huawei Developer
方案概述
当用户使用应用/元服务时，开发者可以按照标准意图Schema（具体意图详见各垂域意图Schema）向系统共享数据，并支持意图调用（空调用与传参调用），以实现用户点击卡片后，可后台执行功能（例如播放指定歌曲）或跳转至指定内容页面（例如指定的歌曲播放页面）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094345.22018679766680282884539591202771:50001231000000:2800:2FB5686EEF6A26C1141A22735FC18DA69DCA0C227F1E16ACC5C9E05016ADD226.png)
意图注册
以歌曲本地搜索特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见各垂域意图Schema。开发者需要编辑对应的意图配置PROJECT_HOME/entry/src/main/resources/base/profile/insight_intent.json文件，实现意图注册。
```json
{
// 应用支持的意图列表
// 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
"insightIntents": [
{
// 意图名称
// 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
// 应用内意图名称唯一，不允许出现相同的名称定义
"intentName": "PlayMusic",
// 意图所属的垂域
"domain": "MusicDomain",
// 意图版本号
// 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
"intentVersion": "1.0.1",
// 意图调用逻辑入口
"srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
"uiAbility": {
// 意图所在module、ability，以及代码相对路径入口
"ability": "EntryAbility",
// UIAbility支持前后台两种执行模式
"executeMode": [
"background",
"foreground"
]
}
}
]
}
```
端侧意图共享
构建意图对象，并且调用shareIntent()，实现意图共享。可同时构建多个PlayMusic或PlayMusicList的意图对象。
PlayMusic的意图共享字段定义见各垂域意图Schema定义，代码示例如下：
```typescript
import { insightIntent } from '@kit.IntentsKit';
let playMusicIntent: insightIntent.InsightIntent = {
intentName: "PlayMusic",
intentVersion: "1.0",
identifier: "52dac3b0-6520-4974-81e5-25f0879449b5",
intentActionInfo: {
actionMode: "EXECUTED",
executedTimeSlots: {
executedStartTime: 1637393212000,
executedEndTime: 1637393112000,
},
currentPercentage: 50,
},
intentEntityInfo: {
entityName: "Music",
entityId: "C10194368",
entityGroupId: "C10194321312",
displayName: "测试歌曲1",
description: "NA",
logoURL: "https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png",
keywords: ["华为音乐", "化妆"],
rankingHint: 99,
expirationTime: 1637393212000,
metadataModificationTime: 1637393212000,
activityType: ["1", "2", "3"],
artist: ["测试歌手1", "测试歌手2"],
lyricist: ["测试词作者1", "测试词作者2"],
composer: ["测试曲作者1", "测试曲作者2"],
albumName: "测试专辑",
duration: 244000,
playCount: 100000,
musicalGenre: ["流行", "华语", "金曲", "00后"],
isPublicData: false,
}
}
```
完整的意图共享示例如下所示，该示例构建了一个PlayMusic意图，并进行了shareIntent调用。
端侧意图调用
开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）或后台执行的能力，PlayMusic的意图调用字段定义见各垂域意图Schema。
步骤如下：
```typescript
import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
/**
* 意图调用样例
*/
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
private static readonly PLAY_MUSIC = 'PlayMusic';
/**
* override 执行前台UIAbility意图
*
* @param name 意图名称
* @param param 意图参数
* @param pageLoader 窗口
* @returns 意图调用结果
*/
onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
Promise<insightIntent.ExecuteResult> {
// 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
switch (name) {
case InsightIntentExecutorImpl.PLAY_MUSIC:
return this.playMusic(param, pageLoader);
default:
break;
}
return Promise.resolve({
code: -1,
result: {
message: 'unknown intent'
}
} as insightIntent.ExecuteResult)
}
/**
* 实现调用播放歌曲功能
*
* @param param 意图参数
* @param pageLoader 窗口
*/
private playMusic(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
return new Promise((resolve, reject) => {
let para: Record<string, string> = {
'result': JSON.stringify(param)
};
let localStorage: LocalStorage = new LocalStorage(para);
// TODO 实现意图调用，loadContent的入参为歌曲落地页路径，例如：pages/Index
pageLoader.loadContent('pages/Index', localStorage)
.then(() => {
let entityId: string = (param.items as Array<object>)?.[0]?.['entityId'];
// TODO 调用成功的情况，此处可以打印日志
resolve({
code: 0,
result: {
message: 'Intent execute succeed'
}
});
})
.catch((err: BusinessError) => {
// TODO 调用失败的情况
resolve({
code: -1,
result: {
message: 'Intent execute failed'
}
})
});
})
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-kit-listing-configuration-V14
爬取时间: 2025-04-30 04:35:41
来源: Huawei Developer
开发者完成开发者测试后需在小艺开放平台进行意图注册配置并提交审核，审核通过后完成意图的正式上线。意图注册配置之前，APP需要先在AppGallery Connect（以下简称AGC）完成应用上架，具体操作步骤参见应用开发准备。意图注册配置操作步骤如下：
1.
2.
3.
4.
5.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094345.51907530836170963729786365355587:50001231000000:2800:6BFD597C80DE9B152B17FC8C6D651BC01616D38A135F3DA12D029B272B286122.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094345.92705573085693825613764545952415:50001231000000:2800:CD048F6F474F916A0E87F2F957CD5744C653C723E1D0B724EDC5F1E4448CF584.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094345.03730491009935811840256029275488:50001231000000:2800:00E5E482647E9D8D040A16958E3F84124DC7281247263C8A9B633D3522A3FAAD.png)
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094345.90150106722816299452543082481906:50001231000000:2800:193C0E95B6BDDE269C53889590F7D75A124353C6EAE4C86DE0C7C01F8865E95A.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094345.70256506514631586950517426142124:50001231000000:2800:B8B9474BD89709802810831C445AB881C71FE0BEF24A1644FD8E8231B1AF6270.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094345.76125385508849112518894157041464:50001231000000:2800:B35C9DDEC9896D0502E4FFA63A9F030E0313EFF1311DF707DDFC4518D6532468.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094346.86111055270605418619828970306120:50001231000000:2800:3312F70EEE4C67B4C3C9438B767010D2908CEEAE3E408D2C04C6458F15281AD4.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094346.60362414038856729475589257383484:50001231000000:2800:FD72920B6630426D7213B390329B65AF644954A0FB4C6348EFE1E1EE62139F73.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094346.03140978885302687098750135239346:50001231000000:2800:E17CC6AB52779D659F3CCE87D063E5391E24B87F495CE66A8E611E9B2AE47EFB.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094346.03475408754145469007857421201480:50001231000000:2800:227B82343BF66B08B5D6D72DCAA90CBB5C2AB62F5577A1360B30E7F419BA362B.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094346.99747850616808774952488898238333:50001231000000:2800:646FB7782C3FBDFB7EE22505BDC25B24FEF2FB70CDA52932CBBBDB5AA835FC56.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094346.74300700782666533968600392416222:50001231000000:2800:409A6211D1B5251A05F90850C754898A921869F61836A2DEAF2A316139DD07EA.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/intents-appendix-a-get-uid-V14
爬取时间: 2025-04-30 04:35:54
来源: Huawei Developer
1.
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094346.49902779571963619773027238035188:50001231000000:2800:7EFC82C38B77D06ECCEFA25D6D066ECB7DD0EB86942BE8E57DBB885936366899.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250414094346.29149110710865947143128216005627:50001231000000:2800:E48A8499EC48E11A4508345F718241E3F648FC104D499E7635F4BD7CAD488021.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/mindspore-lite-kit-V14
爬取时间: 2025-04-30 04:36:07
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/mindspore-lite-kit-introduction-V14
爬取时间: 2025-04-30 04:36:21
来源: Huawei Developer
使用场景
MindSpore Lite是HarmonyOS内置的轻量化AI引擎，面向全场景构建支持多处理器架构的开放AI架构，使能全场景智能应用，为开发者提供端到端的解决方案，为算法工程师和数据科学家提供开发友好、运行高效、部署灵活的体验，帮助人工智能软硬件应用生态繁荣发展。
目前已经在图像分类、目标识别、人脸识别、文字识别等应用中广泛使用。常用场景如：
约束与限制
亮点/优势
MindSpore Lite提供面向不同硬件设备的AI模型推理能力，使能全场景智能应用，为开发者提供端到端的解决方案，使用MindSpore Lite的优势如下：
开发流程
图 1使用MindSpore Lite进行模型推理的开发流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164857.79580165966287184761383199522654:50001231000000:2800:B478A71D35116F052FB914571A0CE4135E5AF7F07B5A12170B4B2A0AA435ED44.png)
MindSpore Lite开发流程分为两个阶段：
-  模型转换 MindSpore Lite使用.ms格式模型进行推理。对于第三方框架模型，比如 TensorFlow、TensorFlow Lite、Caffe、ONNX等，可以使用MindSpore Lite提供的模型转换工具转换为.ms模型，使用方法可参考推理模型转换。
-  模型部署 调用MindSpore Lite运行时接口，实现模型推理/训练，大致步骤如下：
开发方式
MindSpore Lite已作为系统部件在HarmonyOS标准系统内置，基于MindSpore Lite开发AI应用的开发方式有：
与其他Kit的关系
Neural Network Runtime（NNRt, 神经网络运行时）是面向AI领域的跨芯片推理计算运行时，作为中间桥梁连通上层AI推理框架和底层加速芯片，实现AI模型的跨芯片推理计算。
MindSpore Lite原生支持配置Neural Network Runtime使能AI专用芯片（如NPU）加速推理，开发者可直接配置MindSpore Lite来使用NNRt硬件。因此，这里不再对NNRt具体展开说明，主要针对MindSpore开发AI应用提供指导。关于更多NNRt的Native使用，请参见NNRt Native模块。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/mindspore-lite-converter-guidelines-V14
爬取时间: 2025-04-30 04:36:34
来源: Huawei Developer
基本概念
-  MindSpore Lite：HarmonyOS内置AI推理引擎，提供深度学习模型的推理部署能力。
-  Neural Network Runtime：神经网络运行时，简称NNRt。作为中间桥梁，连通上层 AI 推理框架和底层加速芯片，实现 AI 模型的跨芯片推理计算。
-  通用的神经网络模型格式，如MindSpore、ONNX、TensorFlow、CAFFE等。
-  离线模型：使用硬件厂商的离线模型转换工具转换得到的模型，由硬件厂商负责解析和推理。
场景介绍
MindSpore Lite AI模型部署流程是：
环境准备
获取模型转换工具
对于MindSpore Lite模型转换工具，有以下两种方式可以获取：
通过下载获取
| 组件 | 硬件平台 | 操作系统 | 链接 | SHA-256 |
| --- | --- | --- | --- | --- |
| 端侧推理和训练benchmark工具、converter工具、cropper工具 | CPU | Linux-x86_64 | mindspore-lite-2.1.0-linux-x64.tar.gz | b267e5726720329200389e47a178c4f882bf526833b714ba6e630c8e2920fe89 |
由于支持转换PyTorch模型的编译选项默认关闭，因此下载的安装包不支持转换PyTorch模型，只能通过源码编译方式获取。
通过源码编译
1.  编译环境要求如下：
2.  取MindSpore Lite源码。此代码仓采用 “压缩包 + 补丁”的方式管理源码。首先执行以下命令解压源码，打入补丁。 执行完毕，MindSpore Lite完整源码位于：mindspore-src/source/。
3.  执行编译。 如要获取支持转换PyTorch模型的转换工具，编译前需要先export MSLITE_ENABLE_CONVERT_PYTORCH_MODEL=on && export LIB_TORCH_PATH="/home/user/libtorch"。转换前加入libtorch的环境变量：export LD_LIBRARY_PATH="/home/user/libtorch/lib:${LD_LIBRARY_PATH}"。用户可以下载CPU版本libtorch后解压到/home/user/libtorch的目录下。 编译完成后，可从源码根目录的output/子目录取得MindSpore Lite发布件。解压后，转换工具位于tools/converter/converter/。
配置环境变量
获取到模型转换工具之后，还需要将转换工具需要的动态链接库加入环境变量LD_LIBRARY_PATH。
其中，${PACKAGE_ROOT_PATH}对应为编译或下载得到的MindSpore Lite发布件解压后的路径。
参数说明
MindSpore Lite模型转换工具提供了多种参数设置，用户可根据需要来选择使用。此外，用户可输入./converter_lite --help获取实时帮助。
下面提供详细的参数说明。
| 参数 | 是否必选 | 参数说明 | 取值范围 |
| --- | --- | --- | --- |
| --help | 否 | 打印全部帮助信息。 | - |
| --fmk | 是 | 输入模型的原始格式。只有在MS模型转换为Micro代码场景时，才支持设置为MSLITE。 | MINDIR、CAFFE、TFLITE、TF、ONNX、PYTORCH、MSLITE |
| --modelFile | 是 | 输入模型的路径。 | - |
| --outputFile | 是 | 输出模型的路径，不需加后缀，可自动生成.ms后缀。 | - |
| --weightFile | 转换CAFFE模型时必选 | 输入模型权重文件的路径。 | - |
| --configFile | 否 | 1）可作为训练后量化配置文件路径；2）可作为扩展功能配置文件路径。 | - |
| --fp16 | 否 | 设定在模型序列化时是否需要将float32数据格式的权重存储为float16数据格式。 默认值为off。  | on、off |
| --inputShape | 否 | 设定模型输入的维度，输入维度的顺序和原始模型保持一致。对某些特定的模型可以进一步优化模型结构，但是转化后的模型将可能失去动态shape的特性。输入名和shape之间用:分割，多个输入用;分割，同时加上双引号""。例如配置为"inTensorName_1: 1,32,32,4;inTensorName_2:1,64,64,4;"。 | - |
| --inputDataFormat | 否 | 设定导出模型的输入format，只对四维输入有效。 默认值为NHWC。  | NHWC、NCHW |
| --inputDataType | 否 | 设定量化模型输入tensor的数据类型。仅当模型输入tensor的量化参数（scale和zero point）配置时有效。默认与原始模型输入tensor的数据类型保持一致。 默认值为DEFAULT。  | FLOAT32、INT8、UINT8、DEFAULT |
| --outputDataType | 否 | 设定量化模型输出tensor的数据类型。仅当模型输出tensor的量化参数（scale和zero point）配置时有效。默认与原始模型输出tensor的数据类型保持一致。 默认值为DEFAULT。  | FLOAT32、INT8、UINT8、DEFAULT |
| --outputDataFormat | 否 | 设定导出模型的输出format，只对四维输出有效。 | NHWC、NCHW |
设定在模型序列化时是否需要将float32数据格式的权重存储为float16数据格式。
默认值为off。
设定导出模型的输入format，只对四维输入有效。
默认值为NHWC。
设定量化模型输入tensor的数据类型。仅当模型输入tensor的量化参数（scale和zero point）配置时有效。默认与原始模型输入tensor的数据类型保持一致。
默认值为DEFAULT。
设定量化模型输出tensor的数据类型。仅当模型输出tensor的量化参数（scale和zero point）配置时有效。默认与原始模型输出tensor的数据类型保持一致。
默认值为DEFAULT。
使用示例
以CAFFE模型LeNet为例，执行转换命令。
本例中，因为采用了CAFFE模型，所以需要模型结构、模型权值两个输入文件。再加上其他必需的fmk类型和输出路径两个参数，即可成功执行。
结果显示为：
这表示已经成功将CAFFE模型转化为MindSpore Lite模型，获得新文件lenet.ms。
离线模型转换（可选）
当部署场景对加载时延要求严格时，开发者希望进一步降低加载时延，可采用另一种部署方案，即基于离线模型的推理。
执行推理时，MindSpore Lite会直接将离线模型传给接入NNRt的 AI 硬件，无需在线构图即可加载，大幅降低模型加载时延，并且可携带额外的硬件特定信息，协助 AI 硬件推理。
约束与限制
扩展配置文件说明
扩展配置样例如下：
字段说明：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/deployment-V14
爬取时间: 2025-04-30 04:36:47
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/mindspore-lite-guidelines-V14
爬取时间: 2025-04-30 04:37:01
来源: Huawei Developer
场景介绍
MindSpore Lite是一款AI引擎，它提供了面向不同硬件设备AI模型推理的功能，目前已经在图像分类、目标识别、人脸识别、文字识别等应用中广泛使用。
本文介绍使用MindSpore Lite推理引擎进行模型推理的通用开发流程。
基本概念
在进行开发前，请先了解以下概念。
张量：它与数组和矩阵非常相似，是MindSpore Lite网络运算中的基本数据结构。
Float16推理模式： Float16又称半精度，它使用16比特表示一个数。Float16推理模式表示推理的时候用半精度进行推理。
接口说明
这里给出MindSpore Lite推理的通用开发流程中涉及的一些接口，具体请见下列表格。
Context 相关接口
| 接口名称 | 描述 |
| --- | --- |
| OH_AI_ContextHandle OH_AI_ContextCreate() | 创建一个上下文的对象。注意：此接口需跟OH_AI_ContextDestroy配套使用。 |
| void OH_AI_ContextSetThreadNum(OH_AI_ContextHandle context, int32_t thread_num) | 设置运行时的线程数量。 |
| void OH_AI_ContextSetThreadAffinityMode(OH_AI_ContextHandle context, int mode) | 设置运行时线程绑定CPU核心的策略，按照CPU物理核频率分为大、中、小三种类型的核心，并且仅需绑大核或者绑中核，不需要绑小核。 |
| OH_AI_DeviceInfoHandle OH_AI_DeviceInfoCreate(OH_AI_DeviceType device_type) | 创建一个运行时设备信息对象。 |
| void OH_AI_ContextDestroy(OH_AI_ContextHandle *context) | 释放上下文对象。 |
| void OH_AI_DeviceInfoSetEnableFP16(OH_AI_DeviceInfoHandle device_info, bool is_fp16) | 设置是否开启Float16推理模式，仅CPU/GPU设备可用。 |
| void OH_AI_ContextAddDeviceInfo(OH_AI_ContextHandle context, OH_AI_DeviceInfoHandle device_info) | 添加运行时设备信息。 |
Model 相关接口
| 接口名称 | 描述 |
| --- | --- |
| OH_AI_ModelHandle OH_AI_ModelCreate() | 创建一个模型对象。 |
| OH_AI_Status OH_AI_ModelBuildFromFile(OH_AI_ModelHandle model, const char *model_path,OH_AI_ModelType odel_type, const OH_AI_ContextHandle model_context) | 通过模型文件加载并编译MindSpore模型。 |
| void OH_AI_ModelDestroy(OH_AI_ModelHandle *model) | 释放一个模型对象。 |
Tensor 相关接口
| 接口名称 | 描述 |
| --- | --- |
| OH_AI_TensorHandleArray OH_AI_ModelGetInputs(const OH_AI_ModelHandle model) | 获取模型的输入张量数组结构体。 |
| int64_t OH_AI_TensorGetElementNum(const OH_AI_TensorHandle tensor) | 获取张量元素数量。 |
| const char *OH_AI_TensorGetName(const OH_AI_TensorHandle tensor) | 获取张量的名称。 |
| OH_AI_DataType OH_AI_TensorGetDataType(const OH_AI_TensorHandle tensor) | 获取张量数据类型。 |
| void *OH_AI_TensorGetMutableData(const OH_AI_TensorHandle tensor) | 获取可变的张量数据指针。 |
开发步骤
使用MindSpore Lite进行模型推理的开发流程如下图所示。
图 1使用MindSpore Lite进行模型推理的开发流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164857.49073187217951489716180974204643:50001231000000:2800:BECCFB5440A34F8AC9A474FF250399A70ABD7847AEFAB6D898E37DFF161BD4DC.png)
进入主要流程之前需要先引用相关的头文件，并编写函数生成随机的输入，具体如下：
然后进入主要的开发步骤，具括包括模型的准备、读取、编译、推理和释放，具体开发过程及细节请见下文的开发步骤及示例。
1.  模型准备。 需要的模型可以直接下载，也可以通过模型转换工具获得。
2.  创建上下文，设置线程数、设备类型等参数。 以下介绍两种典型情形。 情形1：仅创建CPU推理上下文。 情形2：创建NNRT（Neural Network Runtime）和CPU异构推理上下文。 NNRT是面向AI领域的跨芯片推理计算运行时，一般来说，NNRT对接的加速硬件如NPU，推理能力较强，但支持的算子规格少；而通用CPU推理能力较弱，但支持算子规格更全面。MindSpore Lite支持配置NNRT硬件和CPU异构推理：优先将模型算子调度到NNRT推理，若某些算子NNRT不支持，将其调度到CPU进行推理。通过下面的操作即可配置NNRT/CPU异构推理。
3.  创建、加载与编译模型。 调用OH_AI_ModelBuildFromFile加载并编译模型。 本例中传入OH_AI_ModelBuildFromFile的argv[1]参数是从控制台中输入的模型文件路径。
4.  输入数据。 模型执行之前需要向输入的张量中填充数据。本例使用随机的数据对模型进行填充。
5.  执行推理。 使用OH_AI_ModelPredict接口进行模型推理。
6.  获取输出。 模型推理结束之后，可以通过输出张量得到推理结果。
7.  释放模型。 不再使用MindSpore Lite推理框架时，需要释放已经创建的模型。
调测验证
1.  编写CMakeLists.txt。 使用ohos-sdk交叉编译，需要对CMake设置native工具链路径，即：-DCMAKE_TOOLCHAIN_FILE="/xxx/native/build/cmake/ohos.toolchain.cmake"。 工具链默认编译64位的程序，如果要编译32位，需要添加：-DOHOS_ARCH="armeabi-v7a"。
2.  使用ohos-sdk交叉编译，需要对CMake设置native工具链路径，即：-DCMAKE_TOOLCHAIN_FILE="/xxx/native/build/cmake/ohos.toolchain.cmake"。
3.  工具链默认编译64位的程序，如果要编译32位，需要添加：-DOHOS_ARCH="armeabi-v7a"。
4.  运行。 得到如下输出:
```shell
./demo mobilenetv2.ms
```
-  使用ohos-sdk交叉编译，需要对CMake设置native工具链路径，即：-DCMAKE_TOOLCHAIN_FILE="/xxx/native/build/cmake/ohos.toolchain.cmake"。
-  工具链默认编译64位的程序，如果要编译32位，需要添加：-DOHOS_ARCH="armeabi-v7a"。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/mindspore-lite-train-guidelines-V14
爬取时间: 2025-04-30 04:37:14
来源: Huawei Developer
场景介绍
MindSpore Lite是一款AI引擎，它提供了面向不同硬件设备AI模型推理的功能，目前已经在图像分类、目标识别、人脸识别、文字识别等应用中广泛使用，同时支持在端侧设备上进行部署训练，让模型在实际业务场景中自适应用户的行为。
本文介绍使用MindSpore Lite端侧AI引擎进行模型训练的通用开发流程。
接口说明
此处给出使用MindSpore Lite进行模型训练相关的部分接口，具体请见下方表格
| 接口名称 | 描述 |
| --- | --- |
| OH_AI_ContextHandle OH_AI_ContextCreate() | 创建一个上下文的对象。注意：此接口需跟OH_AI_ContextDestroy配套使用。 |
| OH_AI_DeviceInfoHandle OH_AI_DeviceInfoCreate(OH_AI_DeviceType device_type) | 创建一个运行时设备信息对象。 |
| void OH_AI_ContextDestroy(OH_AI_ContextHandle *context) | 释放上下文对象。 |
| void OH_AI_ContextAddDeviceInfo(OH_AI_ContextHandle context, OH_AI_DeviceInfoHandle device_info) | 添加运行时设备信息。 |
| OH_AI_TrainCfgHandle OH_AI_TrainCfgCreate() | 创建训练配置对象指针。 |
| void OH_AI_TrainCfgDestroy(OH_AI_TrainCfgHandle *train_cfg) | 销毁训练配置对象指针。 |
| OH_AI_ModelHandle OH_AI_ModelCreate() | 创建一个模型对象。 |
| OH_AI_Status OH_AI_TrainModelBuildFromFile(OH_AI_ModelHandle model, const char *model_path, OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context, const OH_AI_TrainCfgHandle train_cfg) | 通过模型文件加载并编译MindSpore训练模型。 |
| OH_AI_Status OH_AI_RunStep(OH_AI_ModelHandle model, const OH_AI_KernelCallBack before, const OH_AI_KernelCallBack after) | 单步训练模型。 |
| OH_AI_Status OH_AI_ModelSetTrainMode(OH_AI_ModelHandle model, bool train) | 设置训练模式。 |
| OH_AI_Status OH_AI_ExportModel(OH_AI_ModelHandle model, OH_AI_ModelType model_type, const char *model_file, OH_AI_QuantizationType quantization_type, bool export_inference_only, char **output_tensor_name, size_t num) | 导出训练后的ms模型。 |
| void OH_AI_ModelDestroy(OH_AI_ModelHandle *model) | 释放一个模型对象。 |
开发步骤
使用MindSpore Lite进行模型训练的开发流程如下图所示。
图 1使用MindSpore Lite进行模型训练的开发流程
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164857.92746808133273280682873121296923:50001231000000:2800:75F5425B0E66534770AF97002748EF3000F231B850F1B4BB5F5AD9B8E95A23F2.png)
进入主要流程之前需要先引用相关的头文件，并编写函数生成随机的输入，具体如下：
然后进入主要的开发步骤，包括模型的准备、读取、编译、训练、模型导出和释放，具体开发过程及细节请见下文的开发步骤及示例。
1.  模型准备。 准备的模型格式为.ms，本文以lenet_train.ms为例（此模型是提前准备的ms模型）。如果开发者需要使用自己准备的模型，可以按如下步骤操作：
2.  创建上下文，设置设备类型、训练配置等参数。
3.  创建、加载与编译模型。 调用OH_AI_TrainModelBuildFromFile加载并编译模型。
4.  输入数据。 模型执行之前需要向输入的张量中填充数据。本例使用随机的数据对模型进行填充。
5.  执行训练。 使用OH_AI_ModelSetTrainMode接口设置训练模式，使用OH_AI_RunStep接口进行模型训练。
6.  导出训练后模型。 使用OH_AI_ExportModel接口导出训练后模型。
7.  释放模型。 不再使用MindSpore Lite推理框架时，需要释放已经创建的模型。
调测验证
1.  编写CMakeLists.txt。 使用ohos-sdk交叉编译，需要对CMake设置native工具链路径，即：-DCMAKE_TOOLCHAIN_FILE="/xxx/native/build/cmake/ohos.toolchain.camke"。 编译命令如下，其中OHOS_NDK需要设置为native工具链路径：
2.  使用ohos-sdk交叉编译，需要对CMake设置native工具链路径，即：-DCMAKE_TOOLCHAIN_FILE="/xxx/native/build/cmake/ohos.toolchain.camke"。
3.  编译命令如下，其中OHOS_NDK需要设置为native工具链路径：
```shell
mkdir -p build
cd ./build || exit
OHOS_NDK=""
cmake -G "Unix Makefiles" \
-S ../ \
-DCMAKE_TOOLCHAIN_FILE="$OHOS_NDK/build/cmake/ohos.toolchain.cmake" \
-DOHOS_ARCH=arm64-v8a \
-DCMAKE_BUILD_TYPE=Release
make
```
4.  运行编译的可执行程序。 得到如下输出： 在train_demo所在目录可以看到导出的两个模型文件：export_train_model.ms和export_infer_model.ms。
```shell
./train_demo ./lenet_train.ms export_train_model export_infer_model
```
-  使用ohos-sdk交叉编译，需要对CMake设置native工具链路径，即：-DCMAKE_TOOLCHAIN_FILE="/xxx/native/build/cmake/ohos.toolchain.camke"。
-  编译命令如下，其中OHOS_NDK需要设置为native工具链路径：
```shell
mkdir -p build
cd ./build || exit
OHOS_NDK=""
cmake -G "Unix Makefiles" \
-S ../ \
-DCMAKE_TOOLCHAIN_FILE="$OHOS_NDK/build/cmake/ohos.toolchain.cmake" \
-DOHOS_ARCH=arm64-v8a \
-DCMAKE_BUILD_TYPE=Release
make
```
完整示例

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/mindspore-guidelines-based-js-V14
爬取时间: 2025-04-30 04:37:28
来源: Huawei Developer
场景说明
开发者可以使用@ohos.ai.mindSporeLite，在UI代码中集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现图像分类的应用。
图像分类可实现对图像中物体的识别，在医学影像分析、自动驾驶、电子商务、人脸识别等有广泛的应用。
基本概念
在进行开发前，请先了解以下概念。
张量：它与数组和矩阵非常相似，是MindSpore Lite网络运算中的基本数据结构。
Float16推理模式： Float16又称半精度，它使用16比特表示一个数。Float16推理模式表示推理的时候用半精度进行推理。
接口说明
这里给出MindSpore Lite推理的通用开发流程中涉及的一些接口，具体请见下列表格。更多接口及详细内容，请见@ohos.ai.mindSporeLite (推理能力)。
| 接口名 | 描述 |
| --- | --- |
| loadModelFromFile(model: string, context?: Context): Promise<Model> | 从路径加载模型。 |
| getInputs(): MSTensor[] | 获取模型的输入。 |
| predict(inputs: MSTensor[]): Promise<MSTensor[]> | 推理模型。 |
| getData(): ArrayBuffer | 获取张量的数据。 |
| setData(inputArray: ArrayBuffer): void | 设置张量的数据。 |
开发流程
环境准备
安装DevEco Studio，要求版本 >= 4.1，并更新SDK到API 11或以上。
开发步骤
本文以对相册的一张图片进行推理为例，提供使用MindSpore Lite实现图像分类的开发指导。
选择模型
本示例程序中使用的图像分类模型文件为mobilenetv2.ms，放置在entry/src/main/resources/rawfile工程目录下。
如果开发者有其他图像分类的预训练模型，请参考MindSpore Lite 模型转换介绍，将原始模型转换成.ms格式。
编写代码
图像输入和预处理
1.  此处以获取相册图片为例，调用@ohos.file.picker实现相册图片文件的选择。
```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
let uris: Array<string> = [];
// 创建图片文件选择实例
let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
// 设置选择媒体文件类型为IMAGE，设置选择媒体文件的最大数目
photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoSelectOptions.maxSelectNumber = 1;
// 创建图库选择器实例，调用select()接口拉起图库界面进行文件选择。文件选择成功后，返回photoSelectResult结果集。
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoSelectOptions, async (
err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
if (err) {
console.error('MS_LITE_ERR: PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
return;
}
console.info('MS_LITE_LOG: PhotoViewPicker.select successfully, ' +
'photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
uris = photoSelectResult.photoUris;
console.info('MS_LITE_LOG: uri: ' + uris);
})
```
2.  根据模型的输入尺寸，调用@ohos.multimedia.image（实现图片处理）、@ohos.file.fs（实现基础文件操作） API对选择图片进行裁剪、获取图片buffer数据，并进行标准化处理。
```typescript
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
let modelInputHeight: number = 224;
let modelInputWidth: number = 224;
// 使用fileIo.openSync接口，通过uri打开这个文件得到fd
let file = fileIo.openSync(this.uris[0], fileIo.OpenMode.READ_ONLY);
console.info('MS_LITE_LOG: file fd: ' + file.fd);
// 通过fd使用fileIo.readSync接口读取这个文件内的数据
let inputBuffer = new ArrayBuffer(4096000);
let readLen = fileIo.readSync(file.fd, inputBuffer);
console.info('MS_LITE_LOG: readSync data to file succeed and inputBuffer size is:' + readLen);
// 通过PixelMap预处理
let imageSource = image.createImageSource(file.fd);
imageSource.createPixelMap().then((pixelMap) => {
pixelMap.getImageInfo().then((info) => {
console.info('MS_LITE_LOG: info.width = ' + info.size.width);
console.info('MS_LITE_LOG: info.height = ' + info.size.height);
// 根据模型输入的尺寸，将图片裁剪为对应的size，获取图片buffer数据readBuffer
pixelMap.scale(256.0 / info.size.width, 256.0 / info.size.height).then(() => {
pixelMap.crop(
{ x: 16, y: 16, size: { height: modelInputHeight, width: modelInputWidth } }
).then(async () => {
let info = await pixelMap.getImageInfo();
console.info('MS_LITE_LOG: crop info.width = ' + info.size.width);
console.info('MS_LITE_LOG: crop info.height = ' + info.size.height);
// 需要创建的像素buffer大小
let readBuffer = new ArrayBuffer(modelInputHeight * modelInputWidth * 4);
await pixelMap.readPixelsToBuffer(readBuffer);
console.info('MS_LITE_LOG: Succeeded in reading image pixel data, buffer: ' +
readBuffer.byteLength);
// 处理readBuffer，转换成float32格式，并进行标准化处理
const imageArr = new Uint8Array(
readBuffer.slice(0, modelInputHeight * modelInputWidth * 4));
console.info('MS_LITE_LOG: imageArr length: ' + imageArr.length);
let means = [0.485, 0.456, 0.406];
let stds = [0.229, 0.224, 0.225];
let float32View = new Float32Array(modelInputHeight * modelInputWidth * 3);
let index = 0;
for (let i = 0; i < imageArr.length; i++) {
if ((i + 1) % 4 == 0) {
float32View[index] = (imageArr[i - 3] / 255.0 - means[0]) / stds[0]; // B
float32View[index+1] = (imageArr[i - 2] / 255.0 - means[1]) / stds[1]; // G
float32View[index+2] = (imageArr[i - 1] / 255.0 - means[2]) / stds[2]; // R
index += 3;
}
}
console.info('MS_LITE_LOG: float32View length: ' + float32View.length);
let printStr = 'float32View data:';
for (let i = 0; i < 20; i++) {
printStr += ' ' + float32View[i];
}
console.info('MS_LITE_LOG: float32View data: ' + printStr);
})
})
});
});
```
编写推理代码
1.  工程默认设备定义的能力集可能不包含MindSporeLite。需在DevEco Studio工程的entry/src/main目录下，手动创建syscap.json文件，内容如下：
```json
{
"devices": {
"general": [
// 需跟module.json5中deviceTypes保持一致。
"default"
]
},
"development": {
"addedSysCaps": [
"SystemCapability.AI.MindSporeLite"
]
}
}
```
2.  调用@ohos.ai.mindSporeLite实现端侧推理。具体开发过程及细节如下：
```typescript
// model.ets
import { mindSporeLite } from '@kit.MindSporeLiteKit'
export default async function modelPredict(
modelBuffer: ArrayBuffer, inputsBuffer: ArrayBuffer[]): Promise<mindSporeLite.MSTensor[]> {
// 1.创建上下文，设置线程数、设备类型等参数。
let context: mindSporeLite.Context = {};
context.target = ['cpu'];
context.cpu = {}
context.cpu.threadNum = 2;
context.cpu.threadAffinityMode = 1;
context.cpu.precisionMode = 'enforce_fp32';
// 2.从内存加载模型。
let msLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromBuffer(modelBuffer, context);
// 3.设置输入数据。
let modelInputs: mindSporeLite.MSTensor[] = msLiteModel.getInputs();
for (let i = 0; i < inputsBuffer.length; i++) {
let inputBuffer = inputsBuffer[i];
if (inputBuffer != null) {
modelInputs[i].setData(inputBuffer as ArrayBuffer);
}
}
// 4.执行推理。
console.info('=========MS_LITE_LOG: MS_LITE predict start=====');
let modelOutputs: mindSporeLite.MSTensor[] = await msLiteModel.predict(modelInputs);
return modelOutputs;
}
```
进行推理并输出结果
加载模型文件，调用推理函数，对相册选择的图片进行推理，并对推理结果进行处理。
```typescript
import modelPredict from './model';
import { resourceManager } from '@kit.LocalizationKit'
let modelName: string = 'mobilenetv2.ms';
let max: number = 0;
let maxIndex: number = 0;
let maxArray: Array<number> = [];
let maxIndexArray: Array<number> = [];
// 完成图像输入和预处理后的buffer数据保存在float32View，具体可见上文图像输入和预处理中float32View的定义和处理。
let inputs: ArrayBuffer[] = [float32View.buffer];
let resMgr: resourceManager.ResourceManager = getContext().getApplicationContext().resourceManager;
resMgr.getRawFileContent(modelName).then(modelBuffer => {
// predict
modelPredict(modelBuffer.buffer.slice(0), inputs).then(outputs => {
console.info('=========MS_LITE_LOG: MS_LITE predict success=====');
// 结果打印
for (let i = 0; i < outputs.length; i++) {
let out = new Float32Array(outputs[i].getData());
let printStr = outputs[i].name + ':';
for (let j = 0; j < out.length; j++) {
printStr += out[j].toString() + ',';
}
console.info('MS_LITE_LOG: ' + printStr);
// 取分类占比的最大值
this.max = 0;
this.maxIndex = 0;
this.maxArray = [];
this.maxIndexArray = [];
let newArray = out.filter(value => value !== max)
for (let n = 0; n < 5; n++) {
max = out[0];
maxIndex = 0;
for (let m = 0; m < newArray.length; m++) {
if (newArray[m] > max) {
max = newArray[m];
maxIndex = m;
}
}
maxArray.push(Math.round(max * 10000))
maxIndexArray.push(maxIndex)
// filter函数，数组过滤函数
newArray = newArray.filter(value => value !== max)
}
console.info('MS_LITE_LOG: max:' + maxArray);
console.info('MS_LITE_LOG: maxIndex:' + maxIndexArray);
}
console.info('=========MS_LITE_LOG END=========');
})
})
```
调测验证
1.  在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：
```shell
Launching com.samples.mindsporelitearktsdemo
$ hdc shell aa force-stop com.samples.mindsporelitearktsdemo
$ hdc shell mkdir data/local/tmp/xxx
$ hdc file send C:\Users\xxx\MindSporeLiteArkTSDemo\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx"
$ hdc shell bm install -p data/local/tmp/xxx
$ hdc shell rm -rf data/local/tmp/xxx
$ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitearktsdemo
```
2.  在设备屏幕点击photo按钮，选择图片，点击确定。设备屏幕显示所选图片的分类结果，在日志打印结果中，过滤关键字”MS_LITE“，可得到如下结果：
效果示意
在设备上，点击photo按钮，选择相册中的一张图片，点击确定。在图片下方显示此图片占比前4的分类信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164857.88769939196590083413195981383660:50001231000000:2800:F7A4046F782A7AC36CE690D8927902A396DD805D888B74DCEBA25319A6F284EE.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164857.81176428718214919592276526117470:50001231000000:2800:ACFE8A0B9623D0859BA07E95F04A264BF09E4BD126A4AD2270072ABE34BB8399.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164857.67339283998442943974015549011955:50001231000000:2800:65C7BDBDE46416DFC8B85519178AC89FA5685512A94E6F0D3223FCB51275DF28.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164857.15413374489705035560872076988523:50001231000000:2800:877C6A5F36A9AA49E9297C9BDB9BD21066834ECCBA1C5E4367BAE50E1206721D.png)
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/mindspore-guidelines-based-native-V14
爬取时间: 2025-04-30 04:37:41
来源: Huawei Developer
场景说明
开发者可以使用MindSpore，在UI代码中直接集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现图像分类的应用。
图像分类可实现对图像中物体的识别，在医学影像分析、自动驾驶、电子商务、人脸识别等有广泛的应用。
基本概念
开发流程
环境准备
安装DevEco Studio，要求版本 >= 4.1，并更新SDK到API 11或以上。
开发步骤
本文以对相册的一张图片进行推理为例，提供使用MindSpore Lite实现图像分类的开发指导。
选择模型
本示例程序中使用的图像分类模型文件为mobilenetv2.ms，放置在entry/src/main/resources/rawfile工程目录下。
如果开发者有其他图像分类的预训练模型，请参考MindSpore Lite 模型转换介绍，将原始模型转换成.ms格式。
编写代码
图像输入和预处理
1.  此处以获取相册图片为例，调用@ohos.file.picker实现相册图片文件的选择。
```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
let uris: Array<string> = [];
// 创建图片文件选择实例
let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
// 设置选择媒体文件类型为IMAGE，设置选择媒体文件的最大数目
photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoSelectOptions.maxSelectNumber = 1;
// 创建图库选择器实例，调用select()接口拉起图库界面进行文件选择。文件选择成功后，返回photoSelectResult结果集。
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoSelectOptions, async (
err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
if (err) {
console.error('MS_LITE_ERR: PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
return;
}
console.info('MS_LITE_LOG: PhotoViewPicker.select successfully, ' +
'photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
uris = photoSelectResult.photoUris;
console.info('MS_LITE_LOG: uri: ' + uris);
})
```
2.  根据模型的输入尺寸，调用@ohos.multimedia.image（实现图片处理）、@ohos.file.fs（实现基础文件操作） API对选择图片进行裁剪、获取图片buffer数据，并进行标准化处理。
```typescript
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
let modelInputHeight: number = 224;
let modelInputWidth: number = 224;
// 使用fileIo.openSync接口，通过uri打开这个文件得到fd
let file = fileIo.openSync(this.uris[0], fileIo.OpenMode.READ_ONLY);
console.info('MS_LITE_LOG: file fd: ' + file.fd);
// 通过fd使用fileIo.readSync接口读取这个文件内的数据
let inputBuffer = new ArrayBuffer(4096000);
let readLen = fileIo.readSync(file.fd, inputBuffer);
console.info('MS_LITE_LOG: readSync data to file succeed and inputBuffer size is:' + readLen);
// 通过PixelMap预处理
let imageSource = image.createImageSource(file.fd);
imageSource.createPixelMap().then((pixelMap) => {
pixelMap.getImageInfo().then((info) => {
console.info('MS_LITE_LOG: info.width = ' + info.size.width);
console.info('MS_LITE_LOG: info.height = ' + info.size.height);
// 根据模型输入的尺寸，将图片裁剪为对应的size，获取图片buffer数据readBuffer
pixelMap.scale(256.0 / info.size.width, 256.0 / info.size.height).then(() => {
pixelMap.crop(
{ x: 16, y: 16, size: { height: modelInputHeight, width: modelInputWidth } }
).then(async () => {
let info = await pixelMap.getImageInfo();
console.info('MS_LITE_LOG: crop info.width = ' + info.size.width);
console.info('MS_LITE_LOG: crop info.height = ' + info.size.height);
// 需要创建的像素buffer大小
let readBuffer = new ArrayBuffer(modelInputHeight * modelInputWidth * 4);
await pixelMap.readPixelsToBuffer(readBuffer);
console.info('MS_LITE_LOG: Succeeded in reading image pixel data, buffer: ' +
readBuffer.byteLength);
// 处理readBuffer，转换成float32格式，并进行标准化处理
const imageArr = new Uint8Array(
readBuffer.slice(0, modelInputHeight * modelInputWidth * 4));
console.info('MS_LITE_LOG: imageArr length: ' + imageArr.length);
let means = [0.485, 0.456, 0.406];
let stds = [0.229, 0.224, 0.225];
let float32View = new Float32Array(modelInputHeight * modelInputWidth * 3);
let index = 0;
for (let i = 0; i < imageArr.length; i++) {
if ((i + 1) % 4 == 0) {
float32View[index] = (imageArr[i - 3] / 255.0 - means[0]) / stds[0]; // B
float32View[index+1] = (imageArr[i - 2] / 255.0 - means[1]) / stds[1]; // G
float32View[index+2] = (imageArr[i - 1] / 255.0 - means[2]) / stds[2]; // R
index += 3;
}
}
console.info('MS_LITE_LOG: float32View length: ' + float32View.length);
let printStr = 'float32View data:';
for (let i = 0; i < 20; i++) {
printStr += ' ' + float32View[i];
}
console.info('MS_LITE_LOG: float32View data: ' + printStr);
})
})
});
});
```
编写推理代码
调用MindSpore实现端侧推理，推理代码流程如下。
1.  引用对应的头文件
2.  读取模型文件
3.  创建上下文，设置线程数、设备类型等参数，并加载模型。
4.  设置模型输入数据，执行模型推理。
5.  调用以上方法，实现完整的模型推理流程。
6.  编写CMake脚本，链接MindSpore Lite动态库。
使用N-API将C++动态库封装成ArkTS模块
1.  在 entry/src/main/cpp/types/libentry/Index.d.ts，定义ArkTS接口runDemo() 。内容如下：
```typescript
export const runDemo: (a: number[], b:Object) => Array<number>;
```
2.  在 oh-package.json5 文件，将API与so相关联，成为一个完整的ArkTS模块：
```json
{
"name": "libentry.so",
"types": "./Index.d.ts",
"version": "1.0.0",
"description": "MindSpore Lite inference module"
}
```
调用封装的ArkTS模块进行推理并输出结果
在 entry/src/main/ets/pages/Index.ets 中，调用封装的ArkTS模块，最后对推理结果进行处理。
```typescript
import msliteNapi from 'libentry.so'
import { resourceManager } from '@kit.LocalizationKit';
let resMgr: resourceManager.ResourceManager = getContext().getApplicationContext().resourceManager;
let max: number = 0;
let maxIndex: number = 0;
let maxArray: Array<number> = [];
let maxIndexArray: Array<number> = [];
// 调用c++的runDemo方法，完成图像输入和预处理后的buffer数据保存在float32View，具体可见上文图像输入和预处理中float32View的定义和处理。
console.info('MS_LITE_LOG: *** Start MSLite Demo ***');
let output: Array<number> = msliteNapi.runDemo(Array.from(float32View), resMgr);
// 取分类占比的最大值
this.max = 0;
this.maxIndex = 0;
this.maxArray = [];
this.maxIndexArray = [];
let newArray = output.filter(value => value !== max);
for (let n = 0; n < 5; n++) {
max = output[0];
maxIndex = 0;
for (let m = 0; m < newArray.length; m++) {
if (newArray[m] > max) {
max = newArray[m];
maxIndex = m;
}
}
maxArray.push(Math.round(this.max * 10000));
maxIndexArray.push(this.maxIndex);
// filter函数数组过滤函数
newArray = newArray.filter(value => value !== max);
}
console.info('MS_LITE_LOG: max:' + this.maxArray);
console.info('MS_LITE_LOG: maxIndex:' + this.maxIndexArray);
console.info('MS_LITE_LOG: *** Finished MSLite Demo ***');
```
调测验证
1.  在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：
```shell
Launching com.samples.mindsporelitecdemo
$ hdc shell aa force-stop com.samples.mindsporelitecdemo
$ hdc shell mkdir data/local/tmp/xxx
$ hdc file send C:\Users\xxx\MindSporeLiteCDemo\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx"
$ hdc shell bm install -p data/local/tmp/xxx
$ hdc shell rm -rf data/local/tmp/xxx
$ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitecdemo
```
2.  在设备屏幕点击photo按钮，选择图片，点击确定。设备屏幕显示所选图片的分类结果，在日志打印结果中，过滤关键字”MS_LITE“，可得到如下结果：
效果示意
在设备上，点击photo按钮，选择相册中的一张图片，点击确定。在图片下方显示此图片占比前4的分类信息。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164858.95694894288711013818600511720449:50001231000000:2800:8434B2F648E35208BE114E3C238BF13F250DAB7A25B58ACC71903222152F34F9.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164858.91530436483252239251642932967447:50001231000000:2800:4B615A6899840083FEB9D4BE100EF0417A44F66B9CCCEE8503251DBF8ACB8132.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164858.54657614020192146145556223109056:50001231000000:2800:B717516C6772B2C29548F4D77993E1B712B213093090F0D951256FF75430AA91.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164858.41060839509446036196242342073092:50001231000000:2800:1E4D0759D0AF5A2F48CFCFA361FD3B73FCD4BDE1D1FFAE419EFCC62FCA777EC4.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/natural-language-kit-guide-V14
爬取时间: 2025-04-30 04:37:55
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/natural-language-introduction-V14
爬取时间: 2025-04-30 04:38:08
来源: Huawei Developer
Natural Language Kit（自然语言理解服务）提供了多项文本语义理解相关的基础能力，帮助开发者更好地处理和分析文本数据。具体包括以下几个方面：
1.  开发者可以利用上述能力，结合自身业务场景，开发出各种智能化应用，进一步完成业务实现。
约束与限制
| AI能力  | 约束  |
| --- | --- |
| 分词  | 支持的语言：简体中文、英文、繁体中文。文本长度：不超过1000字符。  |
| 实体抽取  | 支持的语言：简体中文、英文、繁体中文。支持的实体：时间、地点、邮箱、快递单号、航班号、人名、电话号码、网址链接、验证码、证件号。文本长度：不超过1000字符。  |
AI能力
约束
分词
实体抽取
Natural Language Kit的特性支持多用户同时接入，但是不支持同一用户并发调用同一个特性，如同一个特性被同一进程同一时间多次调用，则返回系统繁忙错误，不同进程调用同一特性，则同一时间只有一个进程业务在处理，其他进程进入队列排队。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/natural-language-getwordsegmentation-V14
爬取时间: 2025-04-30 04:38:21
来源: Huawei Developer
适用场景
分词的目的是让文本文件的中文、英文、数字内容变成一个一个的单词或者词组，从而为后续的转变为词向量提供基础。使用场景例如搜索引擎会将用户输入的文本分词处理后提取关键词送搜索。
约束与限制
该能力当前不支持模拟器。
开发步骤
1.
```typescript
import { textProcessing } from '@kit.NaturalLanguageKit';
```
2.
```typescript
let inputText: string = '';
TextInput({ placeholder: '请输入文本' })
.height(40)
.fontSize(16)
.width('90%')
.margin(10)
.onChange((value: string) => {
this.inputText = value;
})
Button('获取分词结果')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.width('45%')
.margin(10)
.onClick(async () => {
try {
let result = await textProcessing.getWordSegment(this.inputText);
this.outputText = this.formatWordSegmentResult(result);
} catch (err) {
console.error(`getWordSegment errorCode: ${err.code}, errorMessage: ${err.message}`);
}
})
```
3.
```typescript
private formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
let output = 'Word Segments:\n';
segments.forEach((segment, index) => {
output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
});
return output;
}
```
开发实例
```typescript
import { textProcessing } from '@kit.NaturalLanguageKit';
@Entry
@Component
struct Index {
private inputText: string = '';
@State outputText: string = '';
build() {
Column() {
TextInput({ placeholder: '请输入文本' })
.height(40)
.fontSize(16)
.width('90%')
.margin(10)
.onChange((value: string) => {
this.inputText = value;
})
Scroll() {
Text(this.outputText)
.fontSize(16)
.width('90%')
.margin(10)
}
.height('40%')
//调用分词接口
Row() {
Button('获取分词结果')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.width('45%')
.margin(10)
.onClick(async () => {
try {
let result = await textProcessing.getWordSegment(this.inputText);
this.outputText = this.formatWordSegmentResult(result);
} catch (err) {
console.error(`getWordSegment errorCode: ${err.code}, errorMessage: ${err.message}`);
}
})
}
}
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
//分词结果转义
private formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
let output = 'Word Segments:\n';
segments.forEach((segment, index) => {
output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
});
return output;
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/natural-language-getentity-V14
爬取时间: 2025-04-30 04:38:35
来源: Huawei Developer
适用场景
实体抽取是自然语言处理服务的一项关键能力。以综合上下文信息,从文本中准确识别出多种类型的实体：
1.  通过准确抽取以上多种类型的实体信息，该项能力可以广泛应用于新闻阅读、信息检索、客户服务、社交聊天、金融运营等多种场景。例如，在新闻阅读场景中，可以对新闻正文进行实体抽取，并对人名、地名、时间、网址等关键实体信息进行高亮标识，帮助读者快速获取文章要点;在客服场景，通过抽取用户留言中的手机号、快递单号、验证码等信息，客服人员能够更高效地定位问题并给出解决方案。实体抽取为各行业的智能化应用提供了坚实的基础支持。
约束与限制
该能力当前不支持模拟器。
开发步骤
1.
```typescript
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
```
2.
```typescript
let inputText: string = '';
TextInput({ placeholder: '请输入文本' })
.height(40)
.fontSize(16)
.width('90%')
.margin(10)
.onChange((value: string) => {
this.inputText = value;
})
```
3.
```typescript
Button('获取实体结果')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.width('45%')
.margin(10)
.onClick(async () => {
try {
let result = await textProcessing.getEntity(this.inputText, {entityTypes: [EntityType.NAME, EntityType.PHONE_NO]});
this.outputText = this.formatEntityResult(result);
} catch (err) {
console.error(`getEntity errorCode: ${err.code}, errorMessage: ${err.message}`);
this.outputText = 'Error occurred while getting entities.';
}
})
```
4.
```typescript
private formatEntityResult(entities: textProcessing.Entity[]): string {
if (!entities || !entities.length) {
return 'No entities found.';
}
let output = 'Entities:\n';
for (let i = 0; i < entities.length; i++) {
let entity = entities[i];
output += `Entity[${i}]:\n`;
output += `  oriText: ${entity.text}\n`;
output += `  charOffset: ${entity.charOffset}\n`;
output += `  entityType: ${entity.type}\n`;
output += `  jsonObject: ${entity.jsonObject}\n\n`;
}
return output;
}
```
开发实例
```typescript
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
@Entry
@Component
struct Index {
private inputText: string = '';
@State outputText: string = '';
build() {
Column() {
TextInput({ placeholder: '请输入文本' })
.height(40)
.fontSize(16)
.width('90%')
.margin(10)
.onChange((value: string) => {
this.inputText = value;
})
Scroll() {
Text(this.outputText)
.fontSize(16)
.width('90%')
.margin(10)
}
.height('40%')
//调用实体抽取接口
Row() {
Button('获取实体结果')
.type(ButtonType.Capsule)
.fontColor(Color.White)
.width('45%')
.margin(10)
.onClick(async () => {
try {
let result = await textProcessing.getEntity(this.inputText, {entityTypes: [EntityType.NAME, EntityType.PHONE_NO]});
this.outputText = this.formatEntityResult(result);
} catch (err) {
console.error(`getEntity errorCode: ${err.code}, errorMessage: ${err.message}`);
this.outputText = 'Error occurred while getting entities.';
}
})
}
}
.width('100%')
.height('100%')
.justifyContent(FlexAlign.Center)
}
//实体结果转义
private formatEntityResult(entities: textProcessing.Entity[]): string {
if (!entities || !entities.length) {
return 'No entities found.';
}
let output = 'Entities:\n';
for (let i = 0; i < entities.length; i++) {
let entity = entities[i];
output += `Entity[${i}]:\n`;
output += `  oriText: ${entity.text}\n`;
output += `  charOffset: ${entity.charOffset}\n`;
output += `  entityType: ${entity.type}\n`;
output += `  jsonObject: ${entity.jsonObject}\n\n`;
}
return output;
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/neural-network-runtime-kit-V14
爬取时间: 2025-04-30 04:38:48
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/neural-network-runtime-kit-introduction-V14
爬取时间: 2025-04-30 04:39:02
来源: Huawei Developer
使用场景
Neural Network Runtime（NNRt, 神经网络运行时）是面向AI领域的跨芯片推理计算运行时，作为中间桥梁连通上层AI推理框架和底层加速芯片，实现AI模型的跨芯片推理计算。
Neural Network Runtime的Native接口主要面向AI推理框架的开发者，或者希望直接使用AI加速硬件实现模型推理加速的应用开发者。
AI推理框架可以调用NNRt的构图接口将推理框架的模型图转换为NNRt内部使用的模型图，然后调用NNRt的编译和执行接口在NNRt底层对接的AI加速硬件上进行模型推理。该方式可以实现无感知的跨AI硬件推理，但是首次加载模型速度较慢。
AI推理框架和应用开发者也可以无需调用NNRt构图接口，直接使用某款具体硬件对应的离线模型在NNRt上执行模型推理。该方式仅能实现在特定AI硬件上执行推理，但是首次加载模型速度较快。
NNRt架构
如图1所示，除了Native开放接口，NNRt软件架构包含如下几个功能模块：
图1Neural Network Runtime架构图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164858.02237728304537076998852001500431:50001231000000:2800:3139B86B8A23F97703A569F51CAAEEC17ED40FD021E0C8CB71FEBF60B7D4FDEE.jpg)
亮点特征
能力范围
与相关Kit的关系
Neural Network Runtime Kit可支持系统内置的MindSpore Lite推理框架（MindSpore Lite Kit），MindSpore Lite已开放了配置NNRt的Native接口。
MindSpore Lite对接NNRt可无需构图，两者共享同一份模型图格式（MindIR），因此使用MindSpore Lite在NNRt上加载模型将快于其他AI推理框架。
此外，MindSpore Lite也支持通用硬件CPU/GPU与NNRt AI加速硬件之间的模型异构推理功能。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/neural-network-runtime-guidelines-V14
爬取时间: 2025-04-30 04:39:15
来源: Huawei Developer
场景介绍
Neural Network Runtime作为AI推理引擎和加速芯片的桥梁，为AI推理引擎提供精简的Native接口，满足推理引擎通过加速芯片执行端到端推理的需求。
本文以图1展示的Add单算子模型为例，介绍Neural Network Runtime的开发流程。Add算子包含两个输入、一个参数和一个输出，其中的activation参数用于指定Add算子中激活函数的类型。
图1Add单算子网络示意图
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164858.79238930097886589739348856323216:50001231000000:2800:9D30E99C3AC17A4D9A023A37CB40350F1356ADA02FF066BCD9AA25C022332482.png)
环境准备
环境要求
Neural Network Runtime部件的环境要求如下：
由于Neural Network Runtime通过Native API对外开放，需要通过Native开发套件编译Neural Network Runtime应用。在社区的每日构建中下载对应系统版本的ohos-sdk压缩包，从压缩包中提取对应平台的Native开发套件。以Linux为例，Native开发套件的压缩包命名为native-linux-{版本号}.zip。
环境搭建
1.  打开Ubuntu编译服务器的终端。
2.  把下载好的Native开发套件压缩包拷贝至当前用户根目录下。
3.  执行以下命令解压Native开发套件的压缩包。 解压缩后的内容如下（随版本迭代，目录下的内容可能发生变化，请以最新版本的Native API为准）：
```shell
unzip native-linux-{版本号}.zip
```
接口说明
这里给出Neural Network Runtime开发流程中通用的接口，具体请见下列表格。
结构体
| 结构体名称 | 描述 |
| --- | --- |
| typedef struct OH_NNModel OH_NNModel | Neural Network Runtime的模型句柄，用于构造模型。 |
| typedef struct OH_NNCompilation OH_NNCompilation | Neural Network Runtime的编译器句柄，用于编译AI模型。 |
| typedef struct OH_NNExecutor OH_NNExecutor | Neural Network Runtime的执行器句柄，用于在指定设备上执行推理计算。 |
| typedef struct NN_QuantParam NN_QuantParam | Neural Network Runtime的量化参数句柄，用于在构造模型时指定张量的量化参数。 |
| typedef struct NN_TensorDesc NN_TensorDesc | Neural Network Runtime的张量描述句柄，用于描述张量的各类属性，例如数据布局、数据类型、形状等。 |
| typedef struct NN_Tensor NN_Tensor | Neural Network Runtime的张量句柄，用于设置执行器的推理输入和输出张量。 |
模型构造接口
| 接口名称 | 描述 |
| --- | --- |
| OH_NNModel_Construct() | 创建OH_NNModel类型的模型实例。 |
| OH_NN_ReturnCode OH_NNModel_AddTensorToModel(OH_NNModel *model, const NN_TensorDesc *tensorDesc) | 向模型实例中添加张量。 |
| OH_NN_ReturnCode OH_NNModel_SetTensorData(OH_NNModel *model, uint32_t index, const void *dataBuffer, size_t length) | 设置张量的数值。 |
| OH_NN_ReturnCode OH_NNModel_AddOperation(OH_NNModel *model, OH_NN_OperationType op, const OH_NN_UInt32Array *paramIndices, const OH_NN_UInt32Array *inputIndices, const OH_NN_UInt32Array *outputIndices) | 向模型实例中添加算子。 |
| OH_NN_ReturnCode OH_NNModel_SpecifyInputsAndOutputs(OH_NNModel *model, const OH_NN_UInt32Array *inputIndices, const OH_NN_UInt32Array *outputIndices) | 指定模型的输入和输出张量的索引值。 |
| OH_NN_ReturnCode OH_NNModel_Finish(OH_NNModel *model) | 完成模型构图。 |
| void OH_NNModel_Destroy(OH_NNModel **model) | 销毁模型实例。 |
模型编译接口
| 接口名称 | 描述 |
| --- | --- |
| OH_NNCompilation *OH_NNCompilation_Construct(const OH_NNModel *model) | 基于模型实例创建OH_NNCompilation类型的编译实例。 |
| OH_NNCompilation *OH_NNCompilation_ConstructWithOfflineModelFile(const char *modelPath) | 基于离线模型文件路径创建OH_NNCompilation类型的编译实例。 |
| OH_NNCompilation *OH_NNCompilation_ConstructWithOfflineModelBuffer(const void *modelBuffer, size_t modelSize) | 基于离线模型文件内存创建OH_NNCompilation类型的编译实例。 |
| OH_NNCompilation *OH_NNCompilation_ConstructForCache() | 创建一个空的编译实例，以便稍后从模型缓存中恢复。 |
| OH_NN_ReturnCode OH_NNCompilation_ExportCacheToBuffer(OH_NNCompilation *compilation, const void *buffer, size_t length, size_t *modelSize) | 将模型缓存写入到指定内存区域。 |
| OH_NN_ReturnCode OH_NNCompilation_ImportCacheFromBuffer(OH_NNCompilation *compilation, const void *buffer, size_t modelSize) | 从指定内存区域读取模型缓存。 |
| OH_NN_ReturnCode OH_NNCompilation_AddExtensionConfig(OH_NNCompilation *compilation, const char *configName, const void *configValue, const size_t configValueSize) | 为自定义硬件属性添加扩展配置，具体硬件的扩展属性名称和属性值需要从硬件厂商的文档中获取。 |
| OH_NN_ReturnCode OH_NNCompilation_SetDevice(OH_NNCompilation *compilation, size_t deviceID) | 指定模型编译和计算的硬件，可通过设备管理接口获取。 |
| OH_NN_ReturnCode OH_NNCompilation_SetCache(OH_NNCompilation *compilation, const char *cachePath, uint32_t version) | 设置编译模型的缓存目录和版本。 |
| OH_NN_ReturnCode OH_NNCompilation_SetPerformanceMode(OH_NNCompilation *compilation, OH_NN_PerformanceMode performanceMode) | 设置模型计算的性能模式。 |
| OH_NN_ReturnCode OH_NNCompilation_SetPriority(OH_NNCompilation *compilation, OH_NN_Priority priority) | 设置模型计算的优先级。 |
| OH_NN_ReturnCode OH_NNCompilation_EnableFloat16(OH_NNCompilation *compilation, bool enableFloat16) | 是否以float16的浮点数精度计算。 |
| OH_NN_ReturnCode OH_NNCompilation_Build(OH_NNCompilation *compilation) | 执行模型编译。 |
| void OH_NNCompilation_Destroy(OH_NNCompilation **compilation) | 销毁编译实例。 |
张量描述接口
| 接口名称 | 描述 |
| --- | --- |
| NN_TensorDesc *OH_NNTensorDesc_Create() | 创建一个张量描述实例，用于后续创建张量。 |
| OH_NN_ReturnCode OH_NNTensorDesc_SetName(NN_TensorDesc *tensorDesc, const char *name) | 设置张量描述的名称。 |
| OH_NN_ReturnCode OH_NNTensorDesc_GetName(const NN_TensorDesc *tensorDesc, const char **name) | 获取张量描述的名称。 |
| OH_NN_ReturnCode OH_NNTensorDesc_SetDataType(NN_TensorDesc *tensorDesc, OH_NN_DataType dataType) | 设置张量描述的数据类型。 |
| OH_NN_ReturnCode OH_NNTensorDesc_GetDataType(const NN_TensorDesc *tensorDesc, OH_NN_DataType *dataType) | 获取张量描述的数据类型。 |
| OH_NN_ReturnCode OH_NNTensorDesc_SetShape(NN_TensorDesc *tensorDesc, const int32_t *shape, size_t shapeLength) | 设置张量描述的形状。 |
| OH_NN_ReturnCode OH_NNTensorDesc_GetShape(const NN_TensorDesc *tensorDesc, int32_t **shape, size_t *shapeLength) | 获取张量描述的形状。 |
| OH_NN_ReturnCode OH_NNTensorDesc_SetFormat(NN_TensorDesc *tensorDesc, OH_NN_Format format) | 设置张量描述的数据布局。 |
| OH_NN_ReturnCode OH_NNTensorDesc_GetFormat(const NN_TensorDesc *tensorDesc, OH_NN_Format *format) | 获取张量描述的数据布局。 |
| OH_NN_ReturnCode OH_NNTensorDesc_GetElementCount(const NN_TensorDesc *tensorDesc, size_t *elementCount) | 获取张量描述的元素个数。 |
| OH_NN_ReturnCode OH_NNTensorDesc_GetByteSize(const NN_TensorDesc *tensorDesc, size_t *byteSize) | 获取基于张量描述的形状和数据类型计算的数据占用字节数。 |
| OH_NN_ReturnCode OH_NNTensorDesc_Destroy(NN_TensorDesc **tensorDesc) | 销毁张量描述实例。 |
张量接口
| 接口名称 | 描述 |
| --- | --- |
| NN_Tensor* OH_NNTensor_Create(size_t deviceID, NN_TensorDesc *tensorDesc) | 从张量描述创建张量实例，会申请设备共享内存。 |
| NN_Tensor* OH_NNTensor_CreateWithSize(size_t deviceID, NN_TensorDesc *tensorDesc, size_t size) | 按照指定内存大小和张量描述创建张量实例，会申请设备共享内存。 |
| NN_Tensor* OH_NNTensor_CreateWithFd(size_t deviceID, NN_TensorDesc *tensorDesc, int fd, size_t size, size_t offset) | 按照指定共享内存的文件描述符和张量描述创建张量实例，从而可以复用其他张量的设备共享内存。 |
| NN_TensorDesc* OH_NNTensor_GetTensorDesc(const NN_Tensor *tensor) | 获取张量内部的张量描述实例指针，从而可读取张量的属性，例如数据类型、形状等。 |
| void* OH_NNTensor_GetDataBuffer(const NN_Tensor *tensor) | 获取张量数据的内存地址，可以读写张量数据。 |
| OH_NN_ReturnCode OH_NNTensor_GetFd(const NN_Tensor *tensor, int *fd) | 获取张量数据所在共享内存的文件描述符，文件描述符fd对应了一块设备共享内存。 |
| OH_NN_ReturnCode OH_NNTensor_GetSize(const NN_Tensor *tensor, size_t *size) | 获取张量数据所在共享内存的大小。 |
| OH_NN_ReturnCode OH_NNTensor_GetOffset(const NN_Tensor *tensor, size_t *offset) | 获取张量数据所在共享内存上的偏移量，张量数据可使用的大小为所在共享内存的大小减去偏移量。 |
| OH_NN_ReturnCode OH_NNTensor_Destroy(NN_Tensor **tensor) | 销毁张量实例。 |
执行推理接口
| 接口名称 | 描述 |
| --- | --- |
| OH_NNExecutor *OH_NNExecutor_Construct(OH_NNCompilation *compilation) | 创建OH_NNExecutor类型的执行器实例。 |
| OH_NN_ReturnCode OH_NNExecutor_GetOutputShape(OH_NNExecutor *executor, uint32_t outputIndex, int32_t **shape, uint32_t *shapeLength) | 获取输出张量的维度信息，用于输出张量具有动态形状的情况。 |
| OH_NN_ReturnCode OH_NNExecutor_GetInputCount(const OH_NNExecutor *executor, size_t *inputCount) | 获取输入张量的数量。 |
| OH_NN_ReturnCode OH_NNExecutor_GetOutputCount(const OH_NNExecutor *executor, size_t *outputCount) | 获取输出张量的数量。 |
| NN_TensorDesc* OH_NNExecutor_CreateInputTensorDesc(const OH_NNExecutor *executor, size_t index) | 由指定索引值创建一个输入张量的描述，用于读取张量的属性或创建张量实例。 |
| NN_TensorDesc* OH_NNExecutor_CreateOutputTensorDesc(const OH_NNExecutor *executor, size_t index) | 由指定索引值创建一个输出张量的描述，用于读取张量的属性或创建张量实例。 |
| OH_NN_ReturnCode OH_NNExecutor_GetInputDimRange(const OH_NNExecutor *executor, size_t index, size_t **minInputDims, size_t **maxInputDims, size_t *shapeLength) | 获取所有输入张量的维度范围。当输入张量具有动态形状时，不同设备可能支持不同的维度范围。 |
| OH_NN_ReturnCode OH_NNExecutor_SetOnRunDone(OH_NNExecutor *executor, NN_OnRunDone onRunDone) | 设置异步推理结束后的回调处理函数，回调函数定义详见接口文档。 |
| OH_NN_ReturnCode OH_NNExecutor_SetOnServiceDied(OH_NNExecutor *executor, NN_OnServiceDied onServiceDied) | 设置异步推理执行期间设备驱动服务突然死亡时的回调处理函数，回调函数定义详见接口文档。 |
| OH_NN_ReturnCode OH_NNExecutor_RunSync(OH_NNExecutor *executor, NN_Tensor *inputTensor[], size_t inputCount, NN_Tensor *outputTensor[], size_t outputCount) | 执行同步推理。 |
| OH_NN_ReturnCode OH_NNExecutor_RunAsync(OH_NNExecutor *executor, NN_Tensor *inputTensor[], size_t inputCount, NN_Tensor *outputTensor[], size_t outputCount, int32_t timeout, void *userData) | 执行异步推理。 |
| void OH_NNExecutor_Destroy(OH_NNExecutor **executor) | 销毁执行器实例。 |
设备管理接口
| 接口名称 | 描述 |
| --- | --- |
| OH_NN_ReturnCode OH_NNDevice_GetAllDevicesID(const size_t **allDevicesID, uint32_t *deviceCount) | 获取对接到Neural Network Runtime的所有硬件ID。 |
| OH_NN_ReturnCode OH_NNDevice_GetName(size_t deviceID, const char **name) | 获取指定硬件的名称。 |
| OH_NN_ReturnCode OH_NNDevice_GetType(size_t deviceID, OH_NN_DeviceType *deviceType) | 获取指定硬件的类别信息。 |
开发步骤
Neural Network Runtime的开发流程主要包含模型构造、模型编译和推理执行三个阶段。以下开发步骤以Add单算子模型为例，介绍调用Neural Network Runtime接口，开发应用的过程。
1.  创建应用样例文件。 首先，创建Neural Network Runtime应用样例的源文件。在项目目录下执行以下命令，创建nnrt_example/目录，并在目录下创建 nnrt_example.cpp 源文件。
```shell
mkdir ~/nnrt_example && cd ~/nnrt_example
touch nnrt_example.cpp
```
2.  导入Neural Network Runtime。 在 nnrt_example.cpp 文件的开头添加以下代码，引入Neural Network Runtime。
3.  定义日志打印、设置输入数据、数据打印等辅助函数。
4.  构造模型。 使用Neural Network Runtime的模型构造接口，构造Add单算子样例模型。
5.  查询Neural Network Runtime已经对接的AI加速芯片。 Neural Network Runtime支持通过HDI接口，对接多种AI加速芯片。在执行模型编译前，需要查询当前设备下，Neural Network Runtime已经对接的AI加速芯片。每个AI加速芯片对应唯一的ID值，在编译阶段需要通过设备ID，指定模型编译的芯片。
6.  在指定的设备上编译模型。 Neural Network Runtime使用抽象的模型表达描述AI模型的拓扑结构。在AI加速芯片上执行前，需要通过Neural Network Runtime提供的编译模块来创建编译实例，并由编译实例将抽象的模型表达下发至芯片驱动层，转换成可以直接推理计算的格式，即模型编译。
7.  创建执行器。 完成模型编译后，需要调用Neural Network Runtime的执行模块，通过编译实例创建执行器。模型推理阶段中的设置模型输入、触发推理计算以及获取模型输出等操作均需要围绕执行器完成。
8.  执行推理计算，并打印推理结果。 通过执行模块提供的接口，将推理计算所需要的输入数据传递给执行器，触发执行器完成一次推理计算，获取模型的推理结果并打印。
9.  构建端到端模型构造-编译-执行流程。 步骤4-步骤8实现了模型的模型构造、编译和执行流程，并封装成多个函数，便于模块化开发。以下示例代码将串联这些函数， 形成一个完整的Neural Network Runtime使用流程。
调测验证
1.  准备应用样例的编译配置文件。 新建一个 CMakeLists.txt 文件，为开发步骤中的应用样例文件 nnrt_example.cpp 添加编译配置。以下提供简单的 CMakeLists.txt 示例：
2.  编译应用样例。 执行以下命令，在当前目录下新建build/目录，在build/目录下编译 nnrt_example.cpp，得到二进制文件 nnrt_example。
```shell
mkdir build && cd build
cmake -DCMAKE_TOOLCHAIN_FILE={交叉编译工具链的路径}/build/cmake/ohos.toolchain.cmake -DOHOS_ARCH=arm64-v8a -DOHOS_PLATFORM=OHOS -DOHOS_STL=c++_static ..
make
```
3.  执行以下代码，将样例推送到设备上执行。 如果样例执行正常，应该得到以下输出。
```shell
# 将编译得到的 `nnrt_example` 推送到设备上，执行样例。
hdc_std file send ./nnrt_example /data/local/tmp/.
# 给测试用例可执行文件加上权限。
hdc_std shell "chmod +x /data/local/tmp/nnrt_example"
# 执行测试用例
hdc_std shell "/data/local/tmp/nnrt_example"
```
4.  检查模型缓存（可选）。 如果在调测环境下，Neural Network Runtime对接的HDI服务支持模型缓存功能，执行完 nnrt_example, 可以在 /data/local/tmp 目录下找到生成的缓存文件。 模型的IR需要传递到硬件驱动层，由HDI服务将统一的IR图，编译成硬件专用的计算图，编译的过程非常耗时。Neural Network Runtime支持计算图缓存的特性，可以将HDI服务编译生成的计算图，缓存到设备存储中。当下一次在同一个加速芯片上编译同一个模型时，通过指定缓存的路径，Neural Network Runtime可以直接加载缓存文件中的计算图，减少编译消耗的时间。 检查缓存目录下的缓存文件： 以下为打印结果： 如果缓存不再使用，需要手动删除缓存，可以参考以下命令，删除缓存文件。
```shell
ls /data/local/tmp
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/speech-kit-guide-V14
爬取时间: 2025-04-30 04:39:29
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/speech-production-V14
爬取时间: 2025-04-30 04:39:46
来源: Huawei Developer
Speech Kit（场景化语音服务）集成了语音类AI能力，包括朗读控件（TextReader）和AI字幕控件（AICaptionComponent）能力，便于用户与设备进行互动，为用户实现朗读文章。
场景介绍
约束与限制
| AI能力  | 约束  |
| --- | --- |
| 朗读控件  | 支持的语种类型：中文。  |
| AI字幕控件  | 支持的语种类型：中英文。 支持的音频流： 音频类型：当前仅支持 "pcm"编码。音频采样率：当前仅支持16000采样率。音频声道：当前仅支持1个通道。音频采样字节：当前仅支持16位。  |
AI能力
约束
朗读控件
支持的语种类型：中文。
AI字幕控件
支持的语种类型：中英文。
支持的音频流：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/speech-textreader-guide-V14
爬取时间: 2025-04-30 04:40:00
来源: Huawei Developer
适用场景
朗读控件应用广泛，例如在用户不方便或者无法查看屏幕文字的时候，为用户朗读新闻，提供资讯。
本章节将向您介绍如何使用朗读组件，效果如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164859.43642019407267631916782459054824:50001231000000:2800:0EB4B1CCD4EEEB724CE13A68F92C4DD0F3CE5E9F67524C1A6312B60A9A300A51.png)
接口说明
以下仅列出demo中调用的部分主要接口，具体API说明详见API参考。
| 接口名 | 描述 |
| --- | --- |
| init(context: common.BaseContext, readParams: ReaderParam): Promise<void> | 初始化TextReader。 |
| start(readInfoList: ReadInfo[], articleId?: string): Promise<void> | 启动TextReader。 |
| on(type: string, callback: function): void | 注册所有事件回调，具体事件类型详见API参考。 |
| ReaderParam(isVoiceBrandVisible: boolean, businessBrandInfo?: BusinessBrandInfo, isFastForward?: boolean, keepBackgroundRunning?: boolean, online?: number) | 朗读参数。 keepBackgroundRunning参数配置，决定是否使用保持后台运行的功能。  默认false：不保持后台运行， 配置为true：保持后台运行  |
接口名
描述
init(context:common.BaseContext, readParams:ReaderParam): Promise<void>
初始化TextReader。
start(readInfoList:ReadInfo[], articleId?: string): Promise<void>
启动TextReader。
on(type: string, callback: function): void
注册所有事件回调，具体事件类型详见API参考。
ReaderParam(isVoiceBrandVisible: boolean, businessBrandInfo?:BusinessBrandInfo, isFastForward?: boolean, keepBackgroundRunning?: boolean, online?: number)
朗读参数。
keepBackgroundRunning参数配置，决定是否使用保持后台运行的功能。
开发步骤
1.
```typescript
import { WindowManager } from '@kit.SpeechKit';
```
2.
```typescript
onWindowStageCreate(windowStage: window.WindowStage): void {
console.info('Ability onWindowStageCreate');
WindowManager.setWindowStage(windowStage);
windowStage.loadContent('pages/Index', (err, data) => {
if (err) {
console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
return;
}
console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}.` );
});
}
```
3.
```typescript
import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';
```
4.
```typescript
/**
* 播放状态
*/
@State readState: ReadStateCode = ReadStateCode.WAITING;
build() {
Column() {
TextReaderIcon({ readState: this.readState })
.margin({ right: 20 })
.width(32)
.height(32)
.onClick(async () => {
// 设置点击事件
// ...
})
}
}
```
5.
```typescript
// 用于显示当前页的按钮状态
@State isInit: boolean = false;
// 初始化朗读控件
const readerParam: TextReader.ReaderParam = {
isVoiceBrandVisible: true,
businessBrandInfo: {
panelName: '小艺朗读'
}
}
try{
await TextReader.init(getContext(this), readerParam);
// 是否初始化，用于显示听筒按钮的状态
this.isInit = true;
} catch (err) {
console.error(`TextReader failed to init. Code: ${err.code}, message: ${err.message}`);
}
```
6.
```typescript
// 设置监听
setActionListener() {
TextReader.on('setArticle', async (id: string) => { console.info(`setArticle ${id}`) });
TextReader.on('clickArticle', (id: string) => {console.info(`onClickArticle ${id}`) });
TextReader.on('clickAuthor', (id: string) => { console.info(`onClickAuthor ${id}`) });
TextReader.on('clickNotification',  (id: string) => { console.info(`onClickNotification ${id}`) });
TextReader.on('showPanel', () => { console.info(`onShowPanel`) });
TextReader.on('hidePanel', () => { console.info(`onHidePanel`) });
TextReader.on('stateChange', (state: TextReader.ReadState) => {
this.onStateChanged(state)
});
// 在列表页无更多内容时，会显示加载失败，需要设置requestMore监听，调用loadMore函数以获得正确的显示信息。
TextReader.on('requestMore', () => {
TextReader.loadMore(this.newData, true)
});
}
// 注销监听
releaseActionListener() {
TextReader.off('setArticle');
TextReader.off('clickArticle');
TextReader.off('clickAuthor');
TextReader.off('clickNotification');
TextReader.off('showPanel');
TextReader.off('hidePanel');
TextReader.off('stateChange');
TextReader.off('requestMore');
}
```
7.
```typescript
// 加载文章列表，启动朗读控件
const readInfoList: TextReader.ReadInfo[] = [{
id: '001',
title: {
text:'水调歌头.明月几时有',
isClickable:true
},
author:{
text:'宋.苏轼',
isClickable:true
},
date: {
text:'2024/01/01',
isClickable:false
},
bodyInfo: '明月几时有？把酒问青天。'
}];
TextReader.start(readInfoList).then(() => {
console.info(`TextReader succeeded in starting.`);
}).catch((err: BusinessError) => {
console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
})
```
8.
```json
{
"module": {
// ...
"requestPermissions": [
// 后台权限，按需添加
{
"name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
"usedScene": {
"abilities": [
"FormAbility"
],
"when": "inuse"
}
},
// 联网权限，按需添加
{
"name": "ohos.permission.INTERNET",
"usedScene": {
"abilities": [
"FormAbility"
],
"when": "inuse"
}
}
],
"abilities": [
{
// ...
"backgroundModes": [
"audioPlayback"
],
// ...
}
]
}
}
```
开发实例
EntryAbility.ets
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { WindowManager } from '@kit.SpeechKit';
export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
console.info('Ability onCreate');
}
onDestroy(): void {
console.info('Ability onDestroy');
}
onWindowStageCreate(windowStage: window.WindowStage): void {
console.info('Ability onWindowStageCreate');
WindowManager.setWindowStage(windowStage);
windowStage.loadContent('pages/Index', (err, data) => {
if (err.code) {
console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
return;
}
console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}.` );
});
}
onWindowStageDestroy(): void {
console.info('Ability onWindowStageDestroy');
}
onForeground(): void {
console.info('Ability onForeground');
}
onBackground(): void {
console.info('Ability onBackground');
}
}
```
Index.ets
```typescript
import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';
@Entry
@Component
struct Index {
/**
* 待加载的文章
*/
@State readInfoList: TextReader.ReadInfo[] = [];
@State selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];
/**
* 播放状态
*/
@State readState: ReadStateCode = ReadStateCode.WAITING;
/**
* 用于显示当前页的按钮状态
*/
@State isInit: boolean = false;
async aboutToAppear(){
/**
* 加载数据
*/
let readInfoList: TextReader.ReadInfo[] = [{
id: '001',
title: {
text:'水调歌头.明月几时有',
isClickable:true
},
author:{
text:'宋.苏轼',
isClickable:true
},
date: {
text:'2024/01/01',
isClickable:false
},
bodyInfo: '明月几时有？把酒问青天。'
}];
this.readInfoList = readInfoList;
this.selectedReadInfo = this.readInfoList[0];
this.init();
}
/**
* 初始化
*/
async init() {
const readerParam: TextReader.ReaderParam = {
isVoiceBrandVisible: true,
businessBrandInfo: {
panelName: '小艺朗读',
panelIcon: $r('app.media.startIcon')
}
}
try{
await TextReader.init(getContext(this), readerParam);
this.isInit = true;
} catch (err) {
console.error(`TextReader failed to init. Code: ${err.code}, message: ${err.message}`);
}
}
// 设置操作监听
setActionListener() {
TextReader.on('stateChange', (state: TextReader.ReadState) => {
this.onStateChanged(state)
});
TextReader.on('requestMore', () => this.onStateChanged);
}
onStateChanged = (state: TextReader.ReadState) => {
if (this.selectedReadInfo?.id === state.id) {
this.readState = state.state;
} else {
this.readState = ReadStateCode.WAITING;
}
}
build() {
Column() {
TextReaderIcon({ readState: this.readState })
.margin({ right: 20 })
.width(32)
.height(32)
.onClick(async () => {
try {
this.setActionListener();
await TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
} catch (err) {
console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
}
})
}
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/speech-aicaption-guide-V14
爬取时间: 2025-04-30 04:40:13
来源: Huawei Developer
适用场景
AI字幕控件应用广泛，例如在用户不熟悉音频源语言或者静音的时候，为用户提供字幕服务。
本章节将向您介绍如何使用AI字幕组件AICaptionComponent和AICaptionController展示AI字幕，效果如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164859.60560425633371406728526451639336:50001231000000:2800:040D52258EA52E201A3B49EEEE559FB072A13D4119A631FB7E975992378DB749.jpg)
接口说明
AI字幕功能主要由AICaptionComponent提供，更多接口及使用方法请参见接口文档。
| 接口 | 描述 |
| --- | --- |
| AICaptionComponent | AI字幕组件。 |
| AICaptionOptions | AI字幕初始化参数。 |
| AICaptionController | AI字幕组件的控制器，是AI字幕组件的主要功能入口类，用来操作AI字幕。它所承载的工作包括：写音频数据、获取音频流信息等。 |
接口
描述
AICaptionComponent
AI字幕组件。
AICaptionOptions
AI字幕初始化参数。
AICaptionController
AI字幕组件的控制器，是AI字幕组件的主要功能入口类，用来操作AI字幕。它所承载的工作包括：写音频数据、获取音频流信息等。
开发步骤
1.
```typescript
import { AICaptionComponent, AICaptionController, AICaptionOptions } from '@kit.SpeechKit';
```
2.
```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG = 'AI_CAPTION_DEMO'
class Logger {
static info(...msg: string[]) {
hilog.info(0x0000, TAG, msg.join())
}
static error(...msg: string[]) {
hilog.error(0x0000, TAG, msg.join())
}
}
@Entry
@Component
struct Index {
private captionOption ?: AICaptionOptions;
private controller = new AICaptionController();
@State isShown: boolean = false;
aboutToAppear(): void {
// AI字幕初始化参数，设置字幕的不透明度和回调函数
this.captionOption = {
initialOpacity: 1,
onPrepared: () => {
Logger.info('onPrepared')
},
onError: (error) => {
Logger.error(`onError, code: ${error.code}, msg: ${error.message}`)
}
}
}
build() {
Column({ space: 20 }) {
// 调用AICaptionComponent组件初始化字幕
AICaptionComponent({
isShown: this.isShown,
controller: this.controller,
options: this.captionOption
})
.width('80%')
.height(100)
Divider()
if (this.isShown) {
Text('上面是字幕区域')
.fontColor(Color.White)
}
}
.width('100%')
.height('100%')
.padding(10)
.backgroundColor('#7A7D6A')
}
}
```
3.
```typescript
import { AudioData } from '@kit.SpeechKit';
@Entry
@Component
struct Index {
isReading: boolean = false;
async readPcmAudio() {
this.isReading = true;
const fileDate: Uint8Array = await getContext(this).resourceManager.getMediaContent($r("app.media.chineseAudio"));
const bufferSize = 640;
const byteLength = fileDate.byteLength;
let offset = 0;
Logger.info('byteLength', byteLength.toString())
let starTime = new Date().getTime();
while (offset < byteLength) {
//模拟实际情况，读文件比录音机返回流快，所以要等待一段时间
let nextOffset = offset + bufferSize
if (offset > byteLength) {
this.isReading = false;
return
}
const arrayBuffer = fileDate.buffer.slice(offset, nextOffset);
let data = new Uint8Array(arrayBuffer);
Logger.info('data byteLength', data.byteLength.toString())
const audioData: AudioData = {
data: data
}
Logger.info(`offset: ${offset} | byteLength: ${byteLength} | bufferSize: ${bufferSize}`)
if (this.controller) {
Logger.info(`writeAudio： ${audioData.data.byteLength}`)
this.controller.writeAudio(audioData)
}
offset = offset + bufferSize;
const waitTime = bufferSize / 32
await this.sleep(waitTime)
}
let endTime = new Date().getTime()
this.isReading = false;
Logger.info('playtime', JSON.stringify(endTime - starTime))
}
sleep(time: number): Promise<void> {
return new Promise(resolve => setTimeout(resolve, time))
}
build() {
Column({ space: 20 }) {
// ...
Button('切换字幕显示状态:' + (this.isShown ? '显示' : '隐藏'))
.backgroundColor('#B8BDA0')
.width(200)
.onClick(() => {
this.isShown = !this.isShown;
})
Button('读取PCM音频')
.backgroundColor('#B8BDA0')
.width(200)
.onClick(() => {
if (!this.isReading) {
this.readPcmAudio()
}
})
// ...
}
}
}
```
开发实例
Index.ets
```typescript
import { AICaptionComponent, AICaptionOptions, AICaptionController, AudioData } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG = 'AI_CAPTION_DEMO'
class Logger {
static info(...msg: string[]) {
hilog.info(0x0000, TAG, msg.join())
}
static error(...msg: string[]) {
hilog.error(0x0000, TAG, msg.join())
}
}
@Entry
@Component
struct Index {
private captionOption?: AICaptionOptions;
private controller: AICaptionController = new AICaptionController();
@State isShown: boolean = false;
isReading: boolean = false;
aboutToAppear(): void {
// AI字幕初始化参数，设置字幕的不透明度
this.captionOption = {
initialOpacity: 1,
onPrepared: () => {
Logger.info('onPrepared')
},
onError: (error: BusinessError) => {
Logger.error(`AICaption component error. Error code: ${error.code}, message: ${error.message}`)
}
}
}
async readPcmAudio() {
this.isReading = true;
// chineseAudio.pcm文件放在entry\src\main\resources\base\media路径下
const fileData: Uint8Array = await getContext(this).resourceManager.getMediaContent($r('app.media.chineseAudio'));
const bufferSize = 640;
const byteLength = fileData.byteLength;
let offset = 0;
Logger.info(`Pcm data total bytes: ${byteLength.toString()}`)
let startTime = new Date().getTime();
while (offset < byteLength) {
//模拟实际情况，读文件比录音机返回流快，所以要等待一段时间
let nextOffset = offset + bufferSize
if (offset > byteLength) {
this.isReading = false;
return
}
const arrayBuffer = fileData.buffer.slice(offset, nextOffset);
let data = new Uint8Array(arrayBuffer);
const audioData: AudioData = {
data: data
}
if (this.controller) {
this.controller.writeAudio(audioData)
}
offset = offset + bufferSize;
const waitTime = bufferSize / 32
await this.sleep(waitTime)
}
let endTime = new Date().getTime()
this.isReading = false;
Logger.info(`Audio play time: ${JSON.stringify(endTime - startTime)}`)
}
sleep(time: number): Promise<void> {
return new Promise(resolve => setTimeout(resolve, time))
}
build() {
Column({ space: 20 }) {
Button('切换字幕显示状态:' + (this.isShown ? '显示' : '隐藏'))
.backgroundColor('#B8BDA0')
.width(200)
.onClick(() => {
this.isShown = !this.isShown;
})
Button('读取PCM音频')
.backgroundColor('#B8BDA0')
.width(200)
.onClick(() => {
if (!this.isReading) {
this.readPcmAudio()
}
})
Divider()
// 调用AICaptionComponent组件初始化字幕
AICaptionComponent({
isShown: this.isShown,
controller: this.controller,
options: this.captionOption
})
.width('80%')
.height(100)
Divider()
if (this.isShown) {
Text('上面是字幕区域')
.fontColor(Color.White)
}
}
.width('100%')
.height('100%')
.padding(10)
.backgroundColor('#7A7D6A')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/vision-kit-guide-V14
爬取时间: 2025-04-30 04:40:27
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/vision-introduction-V14
爬取时间: 2025-04-30 04:40:40
来源: Huawei Developer
Vision Kit（场景化视觉服务）集成了视觉类AI能力，包括人脸活体检测（interactiveLiveness）能力、卡证识别（CardRecognition）能力、文档扫描（DocumentScanner）能力、AI识图控件（visionImageAnalyzer）能力。人脸活体检测能力便于用户与设备进行互动，验证用户是否为真实活体；卡证识别能力可提供身份证、行驶证、驾驶证、护照、银行卡等证件的结构化识别服务；文档扫描控件可提供拍摄文档并转换为高清扫描件的服务；AI识图控件可提供场景化的文本识别、主体分割、识图搜索功能。其中动作活体检测能力、卡证识别能力实施试用期免费的计费政策，试用期至2026年12月31日。开始正式收费前，华为将会提前通过正式途径发布计费调整通告。
场景介绍
Vision Kit提供了人脸活体检测能力、卡证识别能力、文档扫描能力和AI识图能力，具体如下：
人脸活体检测、卡证识别和文档扫描不支持2in1设备。
约束与限制
| AI能力  | 约束  |
| --- | --- |
| 人脸活体检测  | 支持的文本语种类型：简体中文、繁体中文、英文、维吾尔文、藏文。支持的播报语种类型：简体中文、英文。人脸活体检测服务暂不支持横屏、分屏进行检测。  |
| 卡证识别  | 支持的语种类型：简体中文、英文。卡证识别暂时只支持身份证、行驶证、驾驶证、护照、银行卡5种卡证。不允许被其他组件或窗口遮挡。  |
| 文档扫描  | 支持的语种类型：简体中文、英文。文档扫描暂时只支持手机、平板设备。不允许被其他组件或窗口遮挡。  |
| AI识图  | 支持的文本语种类型：简体中文、繁体中文、英文、维吾尔文、藏文。支持图片最小规格100*100分辨率。分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入PixelMap进行分析，目前仅支持RGBA_8888类型。支持翻译的图片宽高最小比例为1:3，支持文本识别的图片宽高最小比例为1:7。  |
AI能力
约束
人脸活体检测
卡证识别
文档扫描
AI识图

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/vision-interactiveliveness-V14
爬取时间: 2025-04-30 04:40:53
来源: Huawei Developer
场景介绍
人脸活体检测支持动作活体检测模式。
活体检测是一项纯端侧算法、试用期免费的系统基础服务，推荐开发者使用在考勤打卡、辅助登录和实名认证等低危业务场景中。
端侧算法在HarmonyOS NEXT/5.0.x已完成权威机构（CFCA）检测认证。鉴于支付和金融应用的高风险性，建议开发者基于现有的安全性，针对不同的功能场景进行风险评估和风控策略评估，并采取必要的安全措施。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164859.66944248175194212852839522870676:50001231000000:2800:1EC85D20D37352C2BCE9AD953FA10C1A37778D4566C2216821338687A6D3CC63.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164859.56507216551629874248409963516639:50001231000000:2800:9290250D9FE148C7C3F66404278D58CF1693B7D88C0AF2C5CFB5E29720C06AB6.png)
约束与限制
该能力当前不支持模拟器。
接口说明
以下仅列出demo中调用的部分主要接口，具体API说明详见API参考。
| 接口名 | 描述 |
| --- | --- |
| startLivenessDetection(config: InteractiveLivenessConfig): Promise<boolean>; | 跳转到人脸活体检测页面的入口 |
| getInteractiveLivenessResult(): Promise<InteractiveLivenessResult> | 获取人脸活体检测的结果。使用Promise异步回调 |
接口名
描述
startLivenessDetection(config:InteractiveLivenessConfig): Promise<boolean>;
跳转到人脸活体检测页面的入口
getInteractiveLivenessResult(): Promise<InteractiveLivenessResult>
获取人脸活体检测的结果。使用Promise异步回调
开发步骤
1.
```typescript
import { interactiveLiveness } from '@kit.VisionKit';
```
2.
```typescript
"requestPermissions":[
{
"name": "ohos.permission.CAMERA",
"reason": "$string:camera_desc",
"usedScene": {"abilities": []}
}
]
```
3.
```typescript
Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
Text("验证完的跳转模式：")
.fontSize(18)
.width("25%")
Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
Row() {
Radio({ value: "replace", group: "routeMode" }).checked(true)
.height(24)
.width(24)
.onChange((isChecked: boolean) => {
this.routeMode = "replace"
})
Text("replace")
.fontSize(16)
}
.margin({ right: 15 })
Row() {
Radio({ value: "back", group: "routeMode" }).checked(false)
.height(24)
.width(24)
.onChange((isChecked: boolean) => {
this.routeMode = "back";
})
Text("back")
.fontSize(16)
}
}
.width("75%")
}
```
4.
```typescript
Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
Text("动作数量：")
.fontSize(18)
.width("25%")
TextInput({
placeholder: this.actionsNum != 0 ? this.actionsNum.toString() : "动作数量为3或4个"
})
.type(InputType.Number)
.placeholderFont({
size: 18,
weight: FontWeight.Normal,
family: "HarmonyHeiTi",
style: FontStyle.Normal
})
.fontSize(18)
.fontWeight(FontWeight.Bold)
.fontFamily("HarmonyHeiTi")
.fontStyle(FontStyle.Normal)
.width("65%")
.onChange((value: string) => {
this.actionsNum = Number(value) as interactiveLiveness.ActionsNumber;
})
}
```
5.
```typescript
Button("开始检测", { type: ButtonType.Normal, stateEffect: true })
.width(192)
.height(40)
.fontSize(16)
.backgroundColor(0x317aff)
.borderRadius(20)
.margin({
bottom: 56
})
.onClick(() => {
this.privateStartDetection();
})
```
6.
```typescript
// 校验CAMERA权限
private privateStartDetection() {
abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.array).then((res) => {
for (let i = 0; i < res.permissions.length; i++) {
if (res.permissions[i] === "ohos.permission.CAMERA" && res.authResults[i] === 0) {
this.privateRouterLibrary();
}
}
}).catch((err: BusinessError) => {
hilog.error(0x0001, "LivenessCollectionIndex", `Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
})
}
```
7.
```typescript
let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
isSilentMode: this.isSilentMode as interactiveLiveness.DetectionMode,
routeMode: this.routeMode as interactiveLiveness.RouteRedirectionMode,
actionsNum: this.actionsNum
};
```
8.
```typescript
// 跳转到人脸活体检测控件
private privateRouterLibrary() {
if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
interactiveLiveness.startLivenessDetection(routerOptions).then((DetectState: boolean) => {
hilog.info(0x0001, "LivenessCollectionIndex", `Succeeded in jumping.`);
}).catch((err: BusinessError) => {
hilog.error(0x0001, "LivenessCollectionIndex", `Failed to jump. Code：${err.code}，message：${err.message}`);
})
} else {
hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
}
}
```
9.
```typescript
// 获取验证结果
private getDetectionResultInfo() {
// getInteractiveLivenessResult接口调用完会释放资源
if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
let resultInfo = interactiveLiveness.getInteractiveLivenessResult();
resultInfo.then(data => {
this.resultInfo = data;
}).catch((err: BusinessError) => {
this.failResult = {
"code": err.code,
"message": err.message
}
})
} else {
hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
}
}
```
开发实例
```typescript
import { common, abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct LivenessIndex {
private context: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
private array: Array<Permissions> = ["ohos.permission.CAMERA"];
@State actionsNum: number = 0;
@State isSilentMode: string = "INTERACTIVE_MODE";
@State routeMode: string = "replace";
@State resultInfo: interactiveLiveness.InteractiveLivenessResult = {
livenessType: 0
};
@State failResult: Record<string, number | string> = {
"code": 1008302000,
"message": ""
};
build() {
Stack({
alignContent: Alignment.Top
}) {
Column() {
Row() {
Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
Text("验证完的跳转模式：")
.fontSize(18)
.width("25%")
Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
Row() {
Radio({ value: "replace", group: "routeMode" }).checked(true)
.height(24)
.width(24)
.onChange((isChecked: boolean) => {
this.routeMode = "replace"
})
Text("replace")
.fontSize(16)
}
.margin({ right: 15 })
Row() {
Radio({ value: "back", group: "routeMode" }).checked(false)
.height(24)
.width(24)
.onChange((isChecked: boolean) => {
this.routeMode = "back";
})
Text("back")
.fontSize(16)
}
}
.width("75%")
}
}
.margin({ bottom: 30 })
Row() {
Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
Text("动作数量：")
.fontSize(18)
.width("25%")
TextInput({
placeholder: this.actionsNum != 0 ? this.actionsNum.toString() : "动作数量为3或4个"
})
.type(InputType.Number)
.placeholderFont({
size: 18,
weight: FontWeight.Normal,
family: "HarmonyHeiTi",
style: FontStyle.Normal
})
.fontSize(18)
.fontWeight(FontWeight.Bold)
.fontFamily("HarmonyHeiTi")
.fontStyle(FontStyle.Normal)
.width("65%")
.onChange((value: string) => {
this.actionsNum = Number(value) as interactiveLiveness.ActionsNumber;
})
}
}
}
.margin({ left: 24, top: 80 })
.zIndex(1)
Stack({
alignContent: Alignment.Bottom
}) {
if (this.resultInfo?.mPixelMap) {
Image(this.resultInfo?.mPixelMap)
.width(260)
.height(260)
.align(Alignment.Center)
.margin({ bottom: 260 })
Circle()
.width(300)
.height(300)
.fillOpacity(0)
.strokeWidth(60)
.stroke(Color.White)
.margin({ bottom: 250, left: 0 })
}
Text(this.resultInfo.mPixelMap ?
"检测成功" :
this.failResult.code != 1008302000 ?
"检测失败" :
"")
.width("100%")
.height(26)
.fontSize(20)
.fontColor("#000000")
.fontFamily("HarmonyHeiTi")
.margin({ top: 50 })
.textAlign(TextAlign.Center)
.fontWeight("Medium")
.margin({ bottom: 240 })
if(this.failResult.code != 1008302000) {
Text(this.failResult.message as string)
.width("100%")
.height(26)
.fontSize(16)
.fontColor(Color.Gray)
.textAlign(TextAlign.Center)
.fontFamily("HarmonyHeiTi")
.fontWeight("Medium")
.margin({ bottom: 200 })
}
Button("开始检测", { type: ButtonType.Normal, stateEffect: true })
.width(192)
.height(40)
.fontSize(16)
.backgroundColor(0x317aff)
.borderRadius(20)
.margin({
bottom: 56
})
.onClick(() => {
this.privateStartDetection();
})
}
.height("100%")
}
}
onPageShow() {
this.resultRelease();
this.getDetectionResultInfo();
}
// 跳转到人脸活体检测控件
private privateRouterLibrary() {
let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
isSilentMode: this.isSilentMode as interactiveLiveness.DetectionMode,
routeMode: this.routeMode as interactiveLiveness.RouteRedirectionMode,
actionsNum: this.actionsNum
}
if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
interactiveLiveness.startLivenessDetection(routerOptions).then((DetectState: boolean) => {
hilog.info(0x0001, "LivenessCollectionIndex", `Succeeded in jumping.`);
}).catch((err: BusinessError) => {
hilog.error(0x0001, "LivenessCollectionIndex", `Failed to jump. Code：${err.code}，message：${err.message}`);
})
} else {
hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
}
}
// 校验CAMERA权限
private privateStartDetection() {
abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.array).then((res) => {
for (let i = 0; i < res.permissions.length; i++) {
if (res.permissions[i] === "ohos.permission.CAMERA" && res.authResults[i] === 0) {
this.privateRouterLibrary();
}
}
}).catch((err: BusinessError) => {
hilog.error(0x0001, "LivenessCollectionIndex", `Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
})
}
// 获取验证结果
private getDetectionResultInfo() {
// getInteractiveLivenessResult接口调用完会释放资源
if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
let resultInfo = interactiveLiveness.getInteractiveLivenessResult();
resultInfo.then(data => {
this.resultInfo = data;
}).catch((err: BusinessError) => {
this.failResult = {
"code": err.code,
"message": err.message
}
})
} else {
hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
}
}
// result release
private resultRelease() {
this.resultInfo = {
livenessType: 0
}
this.failResult = {
"code": 1008302000,
"message": ""
}
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/vision-cardrecognition-V14
爬取时间: 2025-04-30 04:41:07
来源: Huawei Developer
场景介绍
卡证识别控件提供身份证（目前仅支持中国大陆二代身份证，且不包含民汉双文身份证）、行驶证、驾驶证、护照、银行卡等证件的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。
对于需要填充卡证信息的场景，如身份证、银行卡信息等，可使用卡证识别控件读取OCR（Optical Character Recognition）信息，将结果信息返回后进行填充。支持单独识别正面、反面，或同时进行双面识别。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250328145936.07358877876376708762752413579751:50001231000000:2800:0B7E86F7F12B8526C2972483B86CF532261191E0D7A892E958A02F5A010CA636.png)
约束与限制
该能力当前不支持模拟器。
开发步骤
1.
```typescript
//其中CardRecognitionConfig,CardContentConfig,BankCardConfig从API12开始支持
import { CardRecognition, CallbackParam, CardType, CardSide, CardRecognitionConfig, ShootingMode, CardContentConfig, BankCardConfig } from "@kit.VisionKit";
```
2.
```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG = 'CardRecognition'
@Entry
@Component
struct Index {
build() {
Column() {
//身份证
CardRecognition({
supportType: CardType.CARD_ID,
// 身份证可双面识别
cardSide: CardSide.DEFAULT,
cardRecognitionConfig: {
defaultShootingMode: ShootingMode.MANUAL,
isPhotoSelectionSupported: true
},
callback: ((params: CallbackParam) => {
hilog.info(0x0001, TAG, `params code: ${params.code}`)
hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`)
hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`)
hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`)
})
})
}
.height('100%')
.width('100%')
}
}
```
开发实例
```typescript
// 卡证识别开发实例分两页实现，一页为卡证识别入口页，一页为卡证识别实现页
// 卡证识别入口页，需引入卡证识别实现页，以下文实例为例，实现页文件名为CardDemoPage
import { CardDemoPage } from './CardDemoPage'
@Entry
@Component
struct MainPage {
@Provide('pathStack') pathStack: NavPathStack = new NavPathStack()
@Builder
PageMap(name: string) {
if (name === 'cardRecognition') {
CardDemoPage()
}
}
//卡证识别入口按钮
build() {
Navigation(this.pathStack) {
Button('CardRecognition', { stateEffect: true, type: ButtonType.Capsule })
.width('50%')
.height(40)
.onClick(() => {
this.pathStack.pushPath({ name: 'cardRecognition' })
})
}.title('卡证识别控件demo').navDestination(this.PageMap)
.mode(NavigationMode.Stack)
}
}
```
```typescript
//卡证识别实现页，文件名为CardDemoPage，需被引入至入口页
import { CardRecognition, CallbackParam, CardType, CardSide, ShootingMode } from "@kit.VisionKit"
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'CardRecognitionPage'
//卡证识别页，用于加载uiExtensionAbility
@Entry
@Component
export struct CardDemoPage {
@State cardDataSource: Record<string, string>[] = []
@Consume('pathStack') pathStack: NavPathStack
build() {
NavDestination() {
Stack({ alignContent: Alignment.Top }) {
Stack() {
this.cardDataShowBuilder()
}
.width('80%')
.height('80%')
CardRecognition({
// 此处选择身份证类型作为示例
supportType: CardType.CARD_ID,
cardSide: CardSide.DEFAULT,
cardRecognitionConfig: {
defaultShootingMode: ShootingMode.MANUAL,
isPhotoSelectionSupported: true
},
callback: ((params: CallbackParam) => {
hilog.info(0x0001, TAG, `params code: ${params.code}`)
if (params.code === -1) {
this.pathStack.pop()
}
hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`)
if (params.cardInfo?.front !== undefined) {
this.cardDataSource.push(params.cardInfo?.front)
}
if (params.cardInfo?.back !== undefined) {
this.cardDataSource.push(params.cardInfo?.back)
}
if (params.cardInfo?.main !== undefined) {
this.cardDataSource.push(params.cardInfo?.main)
}
hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`)
hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`)
})
})
}
.width('100%')
.height('100%')
}
.width('100%')
.height('100%')
.hideTitleBar(true)
}
@Builder
cardDataShowBuilder() {
List() {
ForEach(this.cardDataSource, (cardData: Record<string, string>) => {
ListItem() {
Column() {
Image(cardData.cardImageUri)
.objectFit(ImageFit.Contain)
.width(100)
.height(100)
Text(JSON.stringify(cardData))
.width('100%')
.fontSize(12)
}
}
})
}
.listDirection(Axis.Vertical)
.alignListItem(ListItemAlign.Center)
.margin({
top: 50
})
.width('100%')
.height('100%')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/vision-documentscanner-V14
爬取时间: 2025-04-30 04:41:20
来源: Huawei Developer
场景介绍
文档扫描控件提供拍摄文档并转换为高清扫描件的服务。仅需使用手机拍摄文档，即可自动裁剪和优化，并支持图片保存和分享；同时支持拍摄或从图库选择图片识别表格，生成表格文档。
可广泛用于教育办公场景，扫描文档、票据、课堂PPT和书籍等输出图片供用户完成发送、存档等操作。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164900.42123605008361178331482081526824:50001231000000:2800:CCA0F09E4929DF5BDD2D788C0ED8610B3616B2BF31311B1349088ED56359FDD4.png)
约束与限制
该能力当前不支持模拟器。
开发步骤
1.
```typescript
import { DocType, DocumentScanner, DocumentScannerConfig, SaveOption, FilterId, ShootingMode } from "@kit.VisionKit";
```
2.
```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG = 'DocumentScanner'
@Entry
@Component
struct Index {
private docScanConfig = new DocumentScannerConfig()
aboutToAppear() {
this.docScanConfig.supportType = [DocType.DOC, DocType.SHEET]
this.docScanConfig.isGallerySupported = true
this.docScanConfig.editTabs = []
this.docScanConfig.maxShotCount = 3
this.docScanConfig.defaultFilterId = FilterId.ORIGINAL
this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL
this.docScanConfig.isShareable = true
this.docScanConfig.originalUris = []
}
build() {
Column() {
DocumentScanner({
scannerConfig: this.docScanConfig,
onResult: (code: number, saveType: SaveOption, uris: string[]) => {
hilog.info(0x0001, TAG, `result code: ${code}, save: ${saveType}`)
uris.forEach(uriString => {
hilog.info(0x0001, TAG, `uri: ${uriString}`)
})
}
}).size({ width: '100%', height: '100%' })
}
.height('100%')
.width('100%')
}
}
```
开发实例
```typescript
//开发实例分两页实现，一页为文档扫描入口页，一页为文档扫描实现页
//文档扫描入口页，需引入文档扫描实现页，以下文实例为例，实现页文件名为DocDemoPage
import { DocDemoPage } from './DocDemoPage'
@Entry
@Component
struct MainPage {
@Provide('pathStack') pathStack: NavPathStack = new NavPathStack()
@Builder
PageMap(name: string) {
if (name === 'documentScanner') {
DocDemoPage()
}
}
//文档扫描入口按钮，可替换为业务入口
build() {
Navigation(this.pathStack) {
Button('DocumentScanner', { stateEffect: true, type: ButtonType.Capsule })
.width('50%')
.height(40)
.onClick(() => {
this.pathStack.pushPath({ name: 'documentScanner' })
})
}.title('文档扫描控件demo').navDestination(this.PageMap)
.mode(NavigationMode.Stack)
}
}
```
```typescript
//文档扫描实现页，文件名为DocDemoPage，需被引入至入口页
import {
DocType,
DocumentScanner,
DocumentScannerConfig,
SaveOption,
FilterId,
ShootingMode
} from "@kit.VisionKit"
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = 'DocDemoPage'
//文档扫描页，用于加载uiExtensionAbility
@Entry
@Component
export struct DocDemoPage {
@State docImageUris: string[] = []
@Consume('pathStack') pathStack: NavPathStack
private docScanConfig = new DocumentScannerConfig()
aboutToAppear() {
this.docScanConfig.supportType = [DocType.DOC, DocType.SHEET]
this.docScanConfig.isGallerySupported = true
this.docScanConfig.editTabs = []
this.docScanConfig.maxShotCount = 3
this.docScanConfig.defaultFilterId = FilterId.ORIGINAL
this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL
this.docScanConfig.isShareable = true
this.docScanConfig.originalUris = []
}
build() {
NavDestination() {
Stack({ alignContent: Alignment.Top }) {
//展示文档扫描结果
List() {
ForEach(this.docImageUris, (uri: string) => {
ListItem() {
Image(uri)
.objectFit(ImageFit.Contain)
.width(100)
.height(100)
}
})
}
.listDirection(Axis.Vertical)
.alignListItem(ListItemAlign.Center)
.margin({
top: 50
})
.width('80%')
.height('80%')
//文档扫描
DocumentScanner({
scannerConfig: this.docScanConfig,
onResult: (code: number, saveType: SaveOption, uris: string[]) => {
hilog.info(0x0001, TAG, `result code: ${code}, save: ${saveType}`)
if (code === -1) {
this.pathStack.pop()
}
uris.forEach(uriString => {
hilog.info(0x0001, TAG, `uri: ${uriString}`)
})
this.docImageUris = uris
}
})
.size({ width: '100%', height: '100%' })
}
.width('100%')
.height('100%')
}
.width('100%')
.height('100%')
.hideTitleBar(true)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/vision-imageanalyzer-V14
爬取时间: 2025-04-30 04:41:34
来源: Huawei Developer
场景介绍
AI识图是通过聚合OCR（Optical Character Recognition）、主体分割、实体识别、多目标识别等AI能力，提供场景化的文本识别、主体分割、识图搜索功能。AI识图功能主开关入口在基础控件API列表中，如果您接受AI识图默认的交互和功能，仅需使用基础控件提供的相关使能接口打开功能开关即可。该文档配套的API配合基础控件使用，主要满足您的定制诉求，帮助您完成AI识图功能交互上的细粒度控制，获取文本识别、图像分割等分析结果以便您进行扩展业务的开发，目前支持的基础控件范围包括Image、Video、XComponent。其中，配合Image控件可完成静态图片上的识图功能，配合Video控件可完成视频播放暂停帧的识图功能，配合XComponent可完成自定义渲染等场景下的图像的识图功能。
识图功能提供如下能力：
-  用户长按文本选取文字或持续长按文本中的电话号码、邮箱、网址、地址、时间等实体，可触发对应实体的快捷操作，如持续长按文本中的时间，可触发"新建日程"快捷操作入口。
-  用户抠图后可基于抠出的主体进行识图搜索，开发者也可以主动触发目标标识，触发后会识别图中的动物、植物、建筑物等目标并用相应的ICON标识，用户点击ICON也可以进行识图搜索，搜索结果会以模态窗的方式为用户呈现。
-  用户长按主体分割，分割后用户可以完成复制，分享，全选，识图搜索等功能。
-  AIButton承载了电话号码、邮箱、网址、地址、时间等实体的显性下划线标识（点击后出现快捷操作菜单），原图翻译（系统设置语种与图片上文本语种不一致且能将图中文本翻译为系统当前设置的语种时出现），表格提取（图片中存在表格时出现）等功能特性。配置AIButton属性可见后，会对图片进行预分析，当图片中存在文本且文本区域大于图片区域的5%时AIButton才会显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314164900.08271518559892208209130230931387:50001231000000:2800:EA293CA000B3F90124300CF5CFCE3B43BA8222360D489F837CDB5EC2A521CD79.png)
约束与限制
该能力当前不支持模拟器。
开发步骤
1.
```typescript
import { visionImageAnalyzer } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
```
2.
```typescript
private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController();
```
3.
```typescript
aboutToAppear(): void {
this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
console.info("DEMO_TAG", `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
})
this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
console.info("DEMO_TAG", `textAnalysis result: ${JSON.stringify(text)}`)
})
this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
console.info("DEMO_TAG", `selectedTextChange result: ${JSON.stringify(selectedText)}`)
})
this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
})
this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
console.info("DEMO_TAG", `selectedSubjectsChange result: ${JSON.stringify(subjects)}`)
})
this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
console.error("DEMO_TAG", `analyzerFailed result: ${JSON.stringify(error)}`)
})
}
```
4.
```typescript
build() {
Stack() {
// 需要替换您自己的资源图片，存放在resources/base/media目录下
Image($r('app.media.img'), {
types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
aiController: this.visionImageAnalyzerController
})
.width('100%')
.height('100%')
.enableAnalyzer(true)
.objectFit(ImageFit.Contain)
}.width('100%').height('100%')
}
```
5.
```typescript
aboutToDisappear(): void {
this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
this.visionImageAnalyzerController.off('textAnalysis')
this.visionImageAnalyzerController.off('selectedTextChange')
this.visionImageAnalyzerController.off('subjectAnalysis')
this.visionImageAnalyzerController.off('selectedSubjectsChange')
this.visionImageAnalyzerController.off('analyzerFailed')
}
```
开发实例
```typescript
import { visionImageAnalyzer } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit'
@Entry
@Component
export struct ImageDemo {
private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController()
aboutToAppear(): void {
this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
console.info("DEMO_TAG", `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
})
this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
console.info("DEMO_TAG", `textAnalysis result: ${JSON.stringify(text)}`)
})
this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
console.info("DEMO_TAG", `selectedTextChange result: ${JSON.stringify(selectedText)}`)
})
this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
console.info("DEMO_TAG", `selectedSubjectsChange result: ${JSON.stringify(subjects)}`)
})
this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
console.error("DEMO_TAG", `analyzerFailed result: ${JSON.stringify(error)}`)
})
}
build() {
Stack() {
Image($r('app.media.img'), {
types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
aiController: this.visionImageAnalyzerController
})
.width('100%')
.height('100%')
.enableAnalyzer(true)
.objectFit(ImageFit.Contain)
}.width('100%').height('100%')
}
aboutToDisappear(): void {
this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
this.visionImageAnalyzerController.off('textAnalysis')
this.visionImageAnalyzerController.off('selectedTextChange')
this.visionImageAnalyzerController.off('subjectAnalysis')
this.visionImageAnalyzerController.off('selectedSubjectsChange')
this.visionImageAnalyzerController.off('analyzerFailed')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/foreword-V14
爬取时间: 2025-04-30 04:41:47
来源: Huawei Developer
本文介绍了“一次开发，多端部署”（后文中简称为“一多”）的定义、目标等，同时从UX设计、工程管理、页面开发、功能开发等角度，端到端的给出了指导，帮助开发者快速开发出适配多种类型设备的应用。在应用开发前，开发者应尽可能全面考虑应用支持多设备的情况，避免在后期加入新的类型设备时对应用架构进行大幅调整。
本文面向的读者
本文适合开发应用的UX设计师及开发人员。当然，也欢迎任何对“一多”感兴趣的读者阅读本文，相信读者们都可以从中获益。
推荐尽量按照章节顺序阅读本文。如果时间有限，按照角色区分，建议至少阅读如下章节：
-  UX设计师：简介、从一个例子开始、应用UX设计。
-  开发人员：简介、从一个例子开始、工程管理、页面开发的一多能力介绍、功能开发的一多能力介绍。
章节概要
应用在需求明确后，开发过程大致分为：应用设计（包含界面UX设计、业务功能设计）->工程设计和创建->功能代码实现。本指导也是基于这个流程进行的内容编排。
本文档各章节简介如下：
-  前言说明本文的目的以及本文面向的读者，指引读者更好地阅读。
-  简介简短介绍了“一多”的背景、定义、目标、以及用于指导后续开发的一些基础知识。
-  从一个例子开始通过示例介绍“一多”应用的开发过程，让读者对“一多”有个直观认识。
-  应用UX设计介绍了应用UX设计理念。主要阐述了应用设计之初UX设计的原则和要点。该章节主要面向应用的UX设计师。 UX设计原则应该考虑多设备的“差异性” 、“一致性”、“灵活性”和“兼容性”。
-  工程管理介绍了从工程角度如何开始开发应用，让读者可以直接上手创建多设备应用的工程，是后面学习“一多”能力的上手基础。
-  页面开发的一多能力介绍和功能开发的一多能力介绍介绍了“一多”能力，其中每个能力都提供了代码示例和UX效果，让读者可以快速学习“一多”能力。
-  案例应用阐述了从应用设计到开发这一过程中如何实践前面章节介绍的设计思路或“一多”能力，让读者可以整体掌握“一多”在应用开发过程中的知识。
-  常见问题提供了常见的问题（FAQ），方便读者查阅。
本指导在介绍过程中还包括一些“说明”。这些“说明”，表示例外情况或者额外信息的补充。“说明”在文中如下所示：
此处承载说明内容。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/introduction-V14
爬取时间: 2025-04-30 04:42:01
来源: Huawei Developer
背景
随着终端设备形态日益多样化，分布式技术逐渐打破单一硬件边界，一个应用或服务，可以在不同的硬件设备之间随意调用、互助共享，让用户享受无缝的全场景体验。而作为应用开发者，广泛的设备类型也能为应用带来广大的潜在用户群体。但是如果一个应用需要在多个设备上提供同样的内容，则需要适配不同的屏幕尺寸和硬件，开发成本较高。HarmonyOS系统面向多终端提供了“一次开发，多端部署”（后文中简称为“一多”）的能力，让开发者可以基于一种设计，高效构建多端可运行的应用。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250328150007.27969428126277688195114795221959:50001231000000:2800:FE7769461470B52AE66264CFBE26AA9893F23C4AF9F2E8071B188C6B850E044E.jpg)
定义及目标
定义：一套代码工程，一次开发上架，多端按需部署。
目标：支撑开发者快速高效的开发支持多种终端设备形态的应用，实现对不同设备兼容的同时，提供跨设备的流转、迁移和协同的分布式体验。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250328150007.06146988655076237743510124884397:50001231000000:2800:A042468113F994AFD0FCDEF4A5C0B74E88072A01288F9B4463016804674D6521.jpg)
为了实现“一多”的目标，需要解决两个基础问题：
-  不同设备间的屏幕尺寸、色彩风格等存在差异，页面如何适配。
-  不同设备的系统能力有差异，如智能穿戴设备是否具备定位能力、智慧屏是否具备摄像头等，功能如何兼容。
从第4章开始将从UX设计、系统能力等角度，详尽的解答上述问题。
-  应用开发不仅包含应用页面开发，还包括应用后端功能开发以及服务器端开发等。
-  本文旨在指导开发者如何开发“一多”应用，服务器端开发不在本文探讨范围内。
基础知识
为了更好的阅读后面的章节，本小节主要介绍了一些基础知识，方便读者理解内容。
方舟开发框架
方舟开发框架（简称：ArkUI）提供开发者进行应用UI开发时所必须的能力。
方舟开发框架提供了两种开发范式，分别是基于JS扩展的类Web开发范式（后文中简称为“类Web开发范式”）和基于ArkTS的声明式开发范式（后文中简称为“声明式开发范式”）。
-  声明式开发范式：采用TS语言并进行声明式UI语法扩展，从组件、动效和状态管理三个维度提供了UI绘制能力。UI开发更接近自然语义的编程方式，让开发者直观地描述UI界面，不必关心框架如何实现UI绘制和渲染，实现极简高效开发。同时，选用有类型标注的TS语言，引入编译期的类型校验，更适用大型的应用开发。
-  类Web开发范式：采用经典的HML、CSS、JavaScript三段式开发方式。使用HML标签文件进行布局搭建，使用CSS文件进行样式描述，使用JavaScript文件进行逻辑处理。UI组件与数据之间通过单向数据绑定的方式建立关联，当数据发生变化时，UI界面自动触发更新。此种开发方式，更接近Web前端开发者的使用习惯，快速将已有的Web应用改造成方舟开发框架应用。主要适用于界面较为简单的中小型应用开发。
两种开发范式的对比如下。
| 开发范式名称 | 语言生态 | UI更新方式 | 适用场景 | 适用人群 |
| --- | --- | --- | --- | --- |
| 声明式开发范式 | ArkTS语言 | 数据驱动更新 | 复杂度较大、团队合作度较高的程序 | 移动系统应用开发人员、系统应用开发人员 |
| 类Web开发范式 | JS语言 | 数据驱动更新 | 界面较为简单的中小型应用和卡片 | Web前端开发人员 |
声明式开发范式占用内存更少，更推荐开发者选用声明式开发范式来搭建应用UI界面。
应用程序包结构
在进行应用开发时，一个应用通常包含一个或多个Module。Module是应用/服务的基本功能单元，包含了源代码、资源文件、第三方库及应用/服务配置文件，每一个Module都可以独立进行编译和运行。
Module分为“Ability”和“Library”两种类型：
-  “Ability”类型的Module编译后生成HAP包。
-  “Library”类型的Module编译后生成HAR包或HSP包。
应用以APP Pack形式发布，其包含一个或多个HAP包。HAP是应用安装的基本单位，HAP可以分为Entry和Feature两种类型：
-  Entry类型的HAP：应用的主模块。在同一个应用中，同一设备类型只支持一个Entry类型的HAP，通常用于实现应用的入口界面、入口图标、主特性功能等。
-  Feature类型的HAP：应用的动态特性模块。Feature类型的HAP通常用于实现应用的特性功能，一个应用程序包可以包含一个或多个Feature类型的HAP，也可以不包含。
关于Entry类型的HAP包、Feature类型的HAP包、HAR包、HSP包以及APP Pack的详细介绍请参考应用程序包结构说明。
部署模型
“一多”有两种部署模型：
-  部署模型A：不同类型的设备上按照一定的工程结构组织方式，通过一次编译生成相同的HAP（或HAP组合）。
-  部署模型B：不同类型的设备上按照一定的工程结构组织方式，通过一次编译生成不同的HAP（或HAP组合）。
开发者可以从应用UX设计及应用功能两个维度，结合具体的业务场景，考虑选择哪种部署模型。当然，也可以借助设备类型分类，快速做出判断。
从屏幕尺寸、输入方式及交互距离三个维度考虑，可以将常用类型的设备分为不同泛类：
-  手机、平板
-  车机、智慧屏
-  智能穿戴
-  ……
对于相同泛类的设备，优先选择部署模型A，对于不同泛类设备，优先选择部署模型B。
-  应用在不同泛类设备上的UX设计或功能相似时，可以使用部署模型A。
-  应用在同一泛类不同类型设备上UX设计或功能差异非常大时，可以使用部署模型B，但同时也应审视应用的UX设计及功能规划是否合理。
-  本小节引入部署模型A和部署模型B的概念是为了方便开发者理解。实际上在开发多设备应用时，如果目标设备类型较多，往往是部署模型A和部署模型B混合使用。
-  不管采用哪种部署模型，都应该采用一次编译。
工程结构
“一多”推荐在应用开发过程中使用如下的“三层工程结构”。
-  common（公共能力层）：用于存放公共基础能力集合（如工具库、公共配置等）。 common层可编译成一个或多个HAR包或HSP包（HAR中的代码和资源跟随使用方编译，如果有多个使用方，它们的编译产物中会存在多份相同拷贝；而HSP中的代码和资源可以独立编译，运行时在一个进程中代码也只会存在一份），其只可以被products和features依赖，不可以反向依赖。
-  features（基础特性层）：用于存放基础特性集合（如应用中相对独立的各个功能的UI及业务逻辑实现等）。 各个feature高内聚、低耦合、可定制，供产品灵活部署。不需要单独部署的feature通常编译为HAR包或HSP包，供products或其它feature使用，但是不能反向依赖products层。需要单独部署的feature通常编译为Feature类型的HAP包，和products下Entry类型的HAP包进行组合部署。features层可以横向调用及依赖common层。
-  products（产品定制层）：用于针对不同设备形态进行功能和特性集成。 products层各个子目录各自编译为一个Entry类型的HAP包，作为应用主入口。products层不可以横向调用。
代码工程结构抽象后一般如下所示：
-  部署模型不同，相应的代码工程结构也有差异。部署模型A和部署模型B的主要差异点集中在products层：部署模型A在products目录下同一子目录中做功能和特性集成；部署模型B在products目录下不同子目录中对不同的产品做差异化的功能和特性集成。
-  开发阶段应考虑不同类型设备间最大程度的复用代码，以减少开发及后续维护的工作量。
-  整个代码工程最终构建出一个APP包，应用以APP包的形式发布到应用市场中。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/start-with-a-example-V14
爬取时间: 2025-04-30 04:42:15
来源: Huawei Developer
本章通过一个天气应用，介绍一多应用的整体开发过程，包括UX设计、工程管理及调试、页面开发等。
UX设计
本示例中的天气应用包含主页、管理城市和添加城市三个页面，其中主页中又包含菜单和更新间隔两个弹窗，基本业务逻辑如下所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.19422257573861587947564334971658:50001231000000:2800:C8522D057D19776B95CF07B6C6E3B508DB2DC062F018D3A6075E9EC83656941A.png)
“一多”建议从最初的设计阶段开始就拉通多设备综合考虑。考虑实际智能终端设备种类繁多，设计师无法针对每种具体设备各自出一份UX设计图。“一多”建议从设备屏幕宽度的维度，将设备划分为四大类。设计师只需要针对这四大类设备做设计，而无需关心具体的设备形态。
| 设备类型 | 屏幕宽度（vp） |
| --- | --- |
| 超小设备 | [0, 320) |
| 小设备 | [320, 600) |
| 中设备 | [600, 840) |
| 大设备 | [840, +∞) |
-  vp是virtual pixel（虚拟像素）的缩写，是常用的长度单位。
-  此处基于设备屏幕宽度划分不同设备是为了方便理解。通常智能设备上的应用都是以全屏的形式运行，但随着移动技术的发展，当前部分智能设备支持应用以自由窗口模式运行（即用户可以通过拖拽等操作自由调整应用运行窗口的尺寸），故以应用窗口尺寸为基准进行划分更为合适，本文后续的响应式布局章节中将详细介绍相关内容。
-  HarmonyOS当前仅有默认设备和平板两种设备形态，DevEco Studio在创建HarmonyOS工程时也仅可以选择默认设备和平板。随着演进，其支持的设备形态会不断丰富，本文也会定期刷新相关介绍。
默认设备和平板对应于小设备、中设备及大设备，本示例以这三类设备场景为例，介绍不同设备上的UX设计。天气主页在不同设备上的设计图如下所示。
|  | 小设备 | 中设备 | 大设备 |
| --- | --- | --- | --- |
| 主页 |  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.73712406255994564692642549920533:50001231000000:2800:96B34544C4318355B43C2DBF002BE1F8D97933DB9F5487EFDFC8BA57659FE848.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.67595402102836154194584898864093:50001231000000:2800:A4930104A2DBDA950DF169C5A6E9D538D5F8DD643F39C3CECF5C7FE7EEA0F9D6.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.67234241151064348701563141824703:50001231000000:2800:6912A8D7CEA3DA1D107BD40F11E187069B23F0945D7692D12410A0BEE316D0D0.jpg)
另外，大设备中天气主页还允许用户开启或者隐藏侧边栏。
| 开启侧边栏 | 隐藏侧边栏 |
| --- | --- |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.03865266356256930225205142154316:50001231000000:2800:00E6F8E47F0AC6589E9EBA994504417D482450866C809F70001B7328C7833F02.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.31776546603118712092745814625739:50001231000000:2800:9E818A590C51B0B662C6B947740DDA1939E0CC6C85349DEE694C171B5EEAB03A.jpg)
从天气应用在各设备上的UX设计图中，可以观察到如下UX的一些“规律”：
-  在不同的屏幕宽度下，应用的整体风格基本保持一致。
-  在相近的屏幕宽度范围内，应用的布局基本不变；在不同的屏幕宽度范围内，应用的布局有较大差异。
-  应用在小屏幕下显示的元素，是大屏幕中显示元素的子集。
如此，既在各设备上体现了UX的一致性，也在各设备上体现了UX的差异性，从而既可以保障各设备上应用界面的体验，也可以最大程度复用界面代码。
工程管理及调试
在本文DevEco Studio使用章节中，将详细介绍一多的工程创建及管理等，本小节仅介绍最基础的工程创建及多设备预览调试。
工程创建
一多应用的工程创建过程，与传统应用并无较大差异。只需在工程创建过程中，注意在“Device Type”选项中勾选所有该应用期望运行的目标设备类型，保证后续该应用可以在所有目标设备上正确安装即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.51361291345675391179377102128453:50001231000000:2800:376B43FB3EB8B71B45B107FEF948792BCD792053C20B9D67DDEB0A400B7B8176.png)
预览调试
在代码开发过程中，可以开启预览器，并打开“Multi-profile preview”开关，实时观察应用在不同设备下的表现。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.60501282663949645373077897190499:50001231000000:2800:A24003E87B82510E651144572D94CD2A8EC362CA6E41B8C7B3DAD381E7C90C38.jpg)
特别的，还可以点击“+ New Profile”按钮，新增自定义预览器。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165821.70719373101623934708634291874041:50001231000000:2800:5B049088AC811CC47FFD2B389BDF60F6DCC44C0A30AE617976E8D1227315F09B.jpg)
页面开发
天气应用中涉及较多的页面和弹窗，本小节以天气主页为例，简单介绍不同设备下的页面实现思路。
观察天气主页在不同设备上的UX设计图，可以进行如下设计：
-  将天气主页划分为9个基础区域，如：
-  基础区域9仅在大设备上显示，基础区域1-8虽然在各设备上始终展示但其尺寸及区域内的布局基本保持不变，可以结合自适应布局能力以自定义组件的形式分别实现这9个基础区域。
-  基础区域1-8之间的布局在不同设备上有较大差异，可以使用响应式布局中的栅格布局能力实现组件间的布局效果。
-  展开和隐藏侧边栏的功能可以通过侧边栏组件来实现。侧边栏是大设备上独有的，借助响应式布局中的媒体查询能力，控制仅在大设备上展示侧边栏即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165822.74084491595999441327215718501300:50001231000000:2800:33777CA7ADDA78AC05CF84C8CDF4C83633AB12AFCD34CCC637C995FBD5DC0E12.png)
|  | 小设备 | 中设备 | 大设备 |
| --- | --- | --- | --- |
| 主页 |  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165822.78554293987469068399525964837226:50001231000000:2800:B0187B7B7065A3F07CE17AA5362D1E66FE214817CF9F8F9FBF0A8B8B12B9DCAB.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165822.05301762305662997168970782518932:50001231000000:2800:47DA7C93E897A2D2BAE322D05038A2946E8138B41EBB3F671CABED619B5F5D3D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165822.42920629138615197095587673630872:50001231000000:2800:718DDA187FD17A02A576DA97F136CA1C7277212189CD684AC5140DF9788D8A48.png)
主页基础区域
天气主页中的9个基础区域介绍及实现方案如下表所示。
| 编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 标题栏 | 自适应布局拉伸能力。 |
| 2 | 天气概览 | Row和Column组件，并指定其子组件按照主轴起始方向对齐或居中对齐。 |
| 3 | 每小时天气 | 自适应布局延伸能力 。 |
| 4 | 每日天气 | 自适应布局延伸能力 。 |
| 5 | 空气质量 | Canvas画布组件绘制空气质量图，并使用Row组件和Column组件控制内部元素的布局。 |
| 6 | 生活指数 | 自适应布局均分能力。 |
| 7 | 日出日落 | Canvas画布组件绘制日出日落图 。 |
| 8 | 应用信息 | Row和Column组件，并指定其子组件居中对齐。 |
| 9 | 侧边导航栏 | 综合运用自适应布局中的拉伸能力、占比能力和延伸能力 。 |
天气主页涉及的内容较多，因篇幅限制，本小节仅介绍区域3（每小时天气）的实现。
延伸能力是指容器组件内的子组件，按照其在列表中的先后顺序，随容器组件尺寸变化显示或隐藏。随着可用显示区域的增加，用户可以看到的“每小时天气”信息也不断增加，故“每小时天气”可以通过延伸能力实现，其核心代码如下所示。
```typescript
import { Forecast, getHoursData, MyDataSource, Style } from '@ohos/common';
@Component
export default struct HoursWeather {
private hoursData: Forecast[] = getHoursData(0);
@State hoursDataResource: MyDataSource = new MyDataSource(this.hoursData);
build() {
// 通过列表组件实现延伸能力
List() {
LazyForEach(this.hoursDataResource, (hoursItem:IDataSource) => {
ListItem() {
// 具体每个小时的天气情况
Column() {
// ...
}
}
})
}
.height(Style.CARD_HEIGHT)
.borderRadius(Style.NORMAL_RADIUS)
.backgroundColor(Style.CARD_BACKGROUND_COLOR)
// 将列表方向设置为水平方向
.listDirection(Axis.Horizontal)
}
}
```
城市天气详情
天气主页右侧的城市天气详情由区域1-8组成，区域1（标题栏）始终固定在页面顶部，区域2-8在不同设备下的布局不同且可以随页面上下滚动。本小节介绍如何实现城市天气详情中区域2~8的布局效果。
设备屏幕可能无法一次性显示区域2-8的所有内容，故需要在外层增加滚动组件（即Scroll组件）以支持上下滚动。不同设备下区域2-8的相对位置一共有三套不同的布局，可以借助响应式布局中的栅格布局实现这一效果。本示例中将栅格在不同场景下分别划分为4列、8列和12列，区域2-8在不同场景下的布局如下表所示。
| 小设备 | 中设备 或 大设备（侧边栏显示状态） | 大设备（侧边栏隐藏状态） |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165822.09017438293267010324219157191360:50001231000000:2800:B4C94A391E998A964F39CE47C941314D80FCD7D715CE5D1F3B871C6F095251D1.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165822.03922363715532260629901772123871:50001231000000:2800:20ACBA4974A2EE40836973B9709BC0007EDDB81474472674ED5176C7F056B936.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165822.20443648371986176879735239751658:50001231000000:2800:6DC8DB23B56AABCB2DF344A0E69C021C51387D66D31EE4368F567889F5194CD0.png)
为提升用户体验，大设备侧边栏隐藏状态下，每日天气与空气质量的相对顺序发生了改变。可以通过调整GridCol栅格子组件的order属性，实现目标效果。
```typescript
import AirQuality from './AirQuality'; //组件请参考相关实例
import HoursWeather from './HoursWeather';
import IndexHeader from './IndexHeader';
import IndexEnd from './IndexEnd';
import LifeIndex from './LifeIndex';
import MultidayWeather from './MultidayWeather';
import SunCanvas from './SunCanvas';
import { CityListData, Style } from '@ohos/common';
@Component
export default struct HomeContent {
private cityListData: CityListData | undefined = undefined;
private index: number = 1;
@Prop showSideBar: boolean;
@State headerOpacity: number = 1;
build() {
// 支持滚动
Scroll() {
GridRow({
columns: { sm: 4, md: 8, lg: this.showSideBar ? 8 : 12 },
gutter: { x: Style.GRID_GUTTER, y: Style.GRID_GUTTER },
breakpoints: { reference: BreakpointsReference.WindowSize } }) {
// 天气概览
GridCol({ span: { sm: 4, md: 8, lg: this.showSideBar ? 8 : 12 }, order: 1 }) {
IndexHeader({ headerDate: this.cityListData.header, index: this.index })
.opacity(this.headerOpacity)
}
// 每小时天气
GridCol({ span: { sm: 4, md: 8, lg: 8 }, order: 2 }) {
HoursWeather({ hoursData: this.cityListData.hoursData })
}
// 每日天气
GridCol({ span: 4, order: {sm: 3, md: 3, lg: this.showSideBar ? 3 : 4} }) {
MultidayWeather({ weekData: this.cityListData.weekData })
}
// 空气质量
GridCol({ span: 4, order: {sm: 4, md: 4, lg: this.showSideBar ? 4 : 3} }) {
AirQuality({ airData: this.cityListData.airData, airIndexData: this.cityListData.airIndex })
}
// 生活指数
GridCol({ span: 4, order: 5 }) {
LifeIndex({ lifeData: this.cityListData.suitDate })
}
// 日出日落
GridCol({ span: 4, order: 6 }) {
SunCanvas()
}
// 应用信息
GridCol({ span: { sm: 4, md: 8, lg: this.showSideBar ? 8 : 12 }, order: 7 }) {
IndexEnd()
}
}
}
.width('100%')
}
}
```
主页整体实现
综合考虑各设备下的效果，天气主页的根节点使用侧边栏组件：
-  小设备和中设备既不展示侧边栏，也不提供控制侧边栏显示和隐藏的按钮。
-  大设备默认展示侧边栏，同时提供控制侧边栏显示和隐藏的按钮。
另外主页右侧的城市天气详情，支持左右滑动切换城市，可以使用Swiper组件实现目标效果。
-  小设备和中设备开启Swiper组件的导航点，引导用户通过左右滑动切换不同城市。
-  大设备中用户通过点击侧边栏中的城市列表即可高效的切换不同城市，此时需要关闭Swiper组件的导航点。
```typescript
import HomeContent from './home/HomeContent'; //组件请参考相关实例
import IndexTitleBar from './home/IndexTitleBar';
import SideContent from './home/SideContent';
import { CityListData,  getCityListWeatherData } from '@ohos/common';
@Entry
@Component
struct Home {
@State cityListWeatherData: CityListData[] = getCityListWeatherData();
@State curBp: string = 'md';
@State showSideBar: boolean = false;
build() {
SideBarContainer(SideBarContainerType.Embed) {
// 左侧侧边栏
SideContent({ showSideBar: $showSideBar })
// 右侧内容区
Flex({direction: FlexDirection.Column}) {
// 基础区域1标题栏
IndexTitleBar({ curBp: this.curBp, showSideBar: $showSideBar })
.height(56)
// 天气详情，通过Swiper组件实现左右滑动切换城市的效果
Swiper() {
ForEach(this.cityListWeatherData, (item:CityListData, index) => {
HomeContent({ showSideBar: this.showSideBar, cityListData: item, index: index })
})
}
// 大设备关闭导航点
.indicator(this.curBp !== 'lg')
.width('100%')
}
}
.height('100%')
.sideBarWidth('33.3%')
// 通过状态变量，控制不同设备下侧边栏的显隐状态
.showSideBar(this.showSideBar)
}
}
```
最终，天气首页的运行效果如下图所示。
| 小设备 | 中设备 | 大设备（隐藏侧边栏） | 大设备（显示侧边栏） |
| --- | --- | --- | --- |
|  |  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.78767808815511269189660522372823:50001231000000:2800:F37FCD70C168F9B850EDA55440076993E1896FFA414FDE17B4C20435BFB4854E.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.71109453150160102087293668957099:50001231000000:2800:7B95DC9EE9314744FDB8B1FDFDF81253ACB521C2C5D02ECA5D2D529C3DB65E42.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.20758822382849577602856906344499:50001231000000:2800:3A9642CFFCBC3478DD354A86A71DE8A45AF42DB6D55898D6B0099A878CF53C4D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.12380057543335888447738578311649:50001231000000:2800:34EFCD8BAB6F0FC48B666407FD7D5EFCBF2E956FBB6E75A177E6EAF85B1A4473.jpg)
功能开发
应用开发不仅包含应用页面开发，还包括应用后端功能开发以及服务器端开发等。服务器端开发不在本文的讨论范围内，本小节仅介绍多设备上应用功能开发的注意事项。
如前文所示，本示例的目标运行设备是小设备、中设备和大设备，对应实际的设备类型为默认设备和平板等。这些设备运行的都是标准系统，其系统能力一致，所以无需做特别考虑。但是在超小设备（对应的实际设备类型为智能穿戴设备等）上，考虑CPU、内存、硬盘等硬件限制，往往会对系统进行裁剪。如果在应用后端功能开发时调用当前系统没有的能力，就可能会引发异常。
通常有两种方式解决上述问题：
-  在应用安装包中描述其需要的系统能力，保证本应用仅被分发和安装到可以满足其诉求的系统中。
-  在使用特定系统能力前，通过canIUse接口判断系统能力是否存在，进而执行不同的逻辑。
在本文的功能开发的一多能力介绍章节中，将详细展开介绍。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/design-principles-V14
爬取时间: 2025-04-30 04:42:29
来源: Huawei Developer
应用UX设计：一多的应用UX设计需遵循通用设计规则，应该考虑多设备的“差异性”、“一致性”、“灵活性”和“兼容性。详细规范请参见应用UX设计原则。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/ide-using-V14
爬取时间: 2025-04-30 04:42:42
来源: Huawei Developer
本章主要介绍如何使用DevEco Studio进行多设备应用开发。
本章的内容基于DevEco Studio 3.1.1 Release版本进行介绍，如您使用DevEco Studio其它版本，可能存在文档与产品功能界面、操作不一致的情况，请以实际功能界面为准。
工程创建
可以看到DevEco Studio创建出的默认工程，仅包含一个的entry类型的模块。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.27852073610380591405652611202850:50001231000000:2800:852A8A803C96834EAF8079BB1BEC806399D986E33AC99EB6F4783B71A0417347.png)
如果直接使用如下所示的平级目录进行模块管理，工程逻辑结构较混乱且模块间的依赖关系不够清晰，不利于开发及后期维护。
更推荐使用本文部署模型小节中介绍的common、features、product三层工程结构。工程结构示例如下所示：
接下来将依次介绍如何新建Module、修改配置文件以及调整目录，以实现“一多”推荐的“三层工程结构”。
新建Module
参考开发ohpm包，新建三个ohpm模块，分别命名为common、feature1、feature2。参考添加/删除Module，新建一个entry类型的模块，假设命名为“wearable”（仅仅为了说明某一类产品）。示例如下：
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.36819882811130019987699042678981:50001231000000:2800:011443C07560BDCDD9272BB9E53350E0BEA0A6A921F5021460B12C6331D3269F.png)
-  在一个工程中同一个设备类型只支持一个Entry类型的模块。
-  在下一个小节，我们将介绍如何修改Module的配置，包括Module的类型以及其支持的设备类型等。
修改Module配置
修改Module名称
修改创建工程时默认的entry模块名称。在该模块上点击鼠标右键，依次选择”Refactor -> Rename”，将名称修改为default。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.89562406718032630644150484192817:50001231000000:2800:AD3A236E30A172CDF6A1ADC9396EBBB3D638591CB4365633E7D2AFA3C35DDB70.png)
修改Module类型及其设备类型
通过修改每个模块中的配置文件（module.json5）对模块进行配置，配置文件中各字段含义详见配置文件说明。
将default模块的deviceTypes配置为["phone", "tablet"]，同时将其type字段配置为entry。 即default模块编译出的HAP在手机和平板上安装和运行。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.29285410913669645417037104203383:50001231000000:2800:D1C7E6A27DD19C6C5310EBD3E7685FD2D46537319F0DC012496BA0B63EA1976E.png)
-  将wearable模块的deviceTypes配置为["wearable"]，同时将其type字段配置为entry。 即wearable模块编译出的HAP仅在智能穿戴设备上安装和运行。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.32758693379126244457924052077443:50001231000000:2800:08C2C6026415FCF7D2ED5E867E884CCA3DA92C2C5794A42D3147126461294427.png)
调整目录结构
调整目录结构
在工程根目录（MyApplication）上点击鼠标右键，依次选择“New -> Directory”新建子目录。创建product和features两个子目录。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.07831489709251867001299767413482:50001231000000:2800:087E8C4664DD516F22D8CF59B6AAD0D1FF17C1F6F456EACD688488D836E180A9.png)
用鼠标左键将default目录拖拽到新建的product目录中，在DevEco Studio弹出的确认窗口中，点击“Refactor”即可。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.49095817035299558000593232694839:50001231000000:2800:15C6E3A322CD9B1A26B31C008773CAC903F84241B907A43BBB4761CE92C01FF2.png)
按照同样的步骤，将wearable目录放到product目录中，将feature1和feature2放到features目录中。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165823.01384862694312281106365456752631:50001231000000:2800:B045F1605ABC3076FB3149569FA44C727C5B8A265344AB7F86A39B80F9A28C34.png)
修改依赖关系
回顾之前小节中关于“工程结构”的介绍，我们推荐在common目录中存放基础公共代码，features目录中存放相对独立的功能模块代码，product目录中存放完全独立的产品代码。这样在product目录中依赖features和common中的公共代码来实现功能，可以最大程度实现代码复用。
配置依赖关系可以通过修改模块中的oh-package.json5文件。如下图所示，通过修改default模块中的oh-package.json5文件，使其可以使用common、feature1和feature2模块中的代码。更多详情参考配置系统ohpm包依赖。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165824.99940934896949818214924723857464:50001231000000:2800:E292D69C391D181EEE40802854A2D81EBB25A2F6009EACF745EE8D921C5EC91C.png)
同样的，修改feature1和feature2模块中的oh-package.json5文件，使其可以使用common模块中的代码。
修改oh-package.json5文件后，请点击右上角的“Sync Now”，否则改动不会生效。
引用ohpm包中的代码
在开发ohpm包中，仅介绍了如何使用ohpm包中的页面和资源，本小节以例子的形式补充介绍如何使用ohpm包中的类和函数。
示例如下：
-  在common模块中新增ComplexNumber类，用于表征复数（数学概念，由实部和虚部组成），该类包含toString()方法，将复数转换为字符形式。
-  在common模块中新增Add函数，用于计算并返回两个数字的和。
-  在default模块中，使用common模块新增的ComplexNumber类和Add函数。
1.  在”common/src/main/ets”目录中，按照需要新增文件和自定义类和函数。
2.  在”common/index.ets”文件中，申明需要export的类、函数的名称及在当前模块中的位置，否则其它模块无法使用。
3.  在default模块中import和使用这些类和函数。注意提前在default模块的oh-package.json5文件中配置对common模块的依赖关系。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165824.56115084610518093203969700108567:50001231000000:2800:87F0110A1720EBCD1AD3B3D81ABD2B1687F7EBD50C185AB76943690775291DA6.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165824.81106655103925474126349989427914:50001231000000:2800:A4FD823CA30CBECC4B32A12C0E9A18CEE0FE8A638D57A06522AE5FC486F602C3.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165824.72078575136667930332869646641797:50001231000000:2800:4263493B31C6039FB6E444E88B003906F3AB1703CEF1527B51C41C607F262F6A.png)
如果需要将ohpm包发布供其他开发者使用，具体可参考发布ohpm包。
总结
本章主要介绍了如何实现推荐的工程结构，以便更好的进行多设备应用开发。
关于DevEco Studio的基本使用，比如如何进行编译构建、如何签名、如何使用预览器等，DevEco Studio使用指南中已经有非常详尽的介绍，本文不再重复介绍。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/page-development-V14
爬取时间: 2025-04-30 04:42:55
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/page-development-intro-V14
爬取时间: 2025-04-30 04:43:09
来源: Huawei Developer
本章介绍如何使用方舟开发框架“一多”能力，开发出在多设备上正常显示的页面。方舟开发框架推荐开发者使用声明式开发范式开发应用，故本章的内容和示例都主要基于声明式开发范式。本章主要包含如下内容：
-  布局能力 布局决定了页面中的元素按照何种方式排布及显示，是页面设计及开发过程中首先需要考虑的问题。一般情况下，可以通过页面（或自定义组件）内的组件结构（组件个数、组件的父子/兄弟关系、组件类型、组件的相对位置）来判断使用何种布局能力。
-  交互归一
-  多态组件
-  资源使用
开发多设备上同一页面时，建议开发者多使用自定义组件，既可以增加代码的可读性和可维护性，同时也可以尽可能的实现代码复用。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/layout-V14
爬取时间: 2025-04-30 04:43:22
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/layout-intro-V14
爬取时间: 2025-04-30 04:43:36
来源: Huawei Developer
布局可以分为自适应布局和响应式布局，二者的介绍如下表所示。
| 名称 | 简介 |
| --- | --- |
| 自适应布局 | 当外部容器大小发生变化时，元素可以根据相对关系自动变化以适应外部容器变化的布局能力。相对关系如占比、固定宽高比、显示优先级等。当前自适应布局能力有7种：拉伸能力、均分能力、占比能力、缩放能力、延伸能力、隐藏能力、折行能力。自适应布局能力可以实现界面显示随外部容器大小连续变化。 |
| 响应式布局 | 当外部容器大小发生变化时，元素可以根据断点、栅格或特定的特征（如屏幕方向、窗口宽高等）自动变化以适应外部容器变化的布局能力。当前响应式布局能力有3种：断点、媒体查询、栅格布局。响应式布局可以实现界面随外部容器大小有不连续变化，通常不同特征下的界面显示会有较大的差异。 |
自适应布局多用于解决页面各区域内的布局差异，响应式布局多用于解决页面各区域间的布局差异。
自适应布局和响应式布局常常需要借助容器类组件实现，或与容器类组件搭配使用。
-  自适应布局常常需要借助Row组件、Column组件或Flex组件实现。 将组件wrap属性， 设置为FlexWrap.Wrap
-  响应式布局常常与GridRow组件、Grid组件、List组件、Swiper组件或Tabs组件搭配使用。 使用断点和栅格方式布局子组件的容器。 需配合GridCol子组件使用。 使用“行”和“列”分割的单元格方式布局子组件的网格容器。 需配合GridItem子组件使用。 包含一系列相同宽度列表项的容器。 需配合ListItem子组件使用。 使用页签控制内容切换的容器，每个页签对应一个内容视图。 需配合TabContent子组件使用。
| 容器组件 | 组件说明 | 拉伸能力 | 均分能力 | 占比能力 |
| --- | --- | --- | --- | --- |
| Row | 沿水平方向布局子组件的容器 | 增加Blank子组件 | 将组件justifyContent属性设置为FlexAlign.SpaceEvenly | 通过百分比设置子组件宽高，或配置子组件layoutWeight属性 |
| Column | 沿垂直方向布局子组件的容器 | 增加Blank子组件 | 将组件justifyContent属性设置为FlexAlign.SpaceEvenly | 通过百分比设置子组件宽高，或配置子组件layoutWeight属性 |
| Flex | 使用弹性方式布局子组件的容器 | 增加Blank子组件，或配置子组件flexGrow和flexShrink属性 | 将组件justifyContent属性设置为FlexAlign.SpaceEvenly | 通过百分比设置子组件宽高，或配置子组件layoutWeight属性 |
| 容器组件 | 组件说明 | 缩放能力 | 延伸能力 | 隐藏能力 | 折行能力 |
| --- | --- | --- | --- | --- | --- |
| Row | 沿水平方向布局子组件的容器 | 配置组件aspectRatio属性 | 增加Scroll父组件 | 配置子组件displayPriority属性 | — |
| Column | 沿垂直方向布局子组件的容器 | 配置组件aspectRatio属性 | 增加Scroll父组件 | 配置子组件displayPriority属性 | — |
| Flex | 使用弹性方式布局子组件的容器 | 配置组件aspectRatio属性 | — | 配置子组件displayPriority属性 | 将组件wrap属性， 设置为FlexWrap.Wrap |
| 容器组件 | 组件说明 | 响应式布局 |
| --- | --- | --- |
| GridRow | 使用断点和栅格方式布局子组件的容器。 需配合GridCol子组件使用。 | 栅格组件自身具有响应式布局能力。 |
| Grid | 使用“行”和“列”分割的单元格方式布局子组件的网格容器。 需配合GridItem子组件使用。 | 需配合断点使用，通过改变不同断点下的rowsTemplate和columnsTemplate等属性，实现不同的布局效果。 |
| List | 包含一系列相同宽度列表项的容器。 需配合ListItem子组件使用。 | 需配合断点使用，通过改变不同断点下的lanes等属性，实现不同的布局效果。 |
| Swiper | 轮播展示子组件的容器。 | 需配合断点使用，通过改变不同断点下的displayCount和indicator等属性，实现不同的布局效果。 |
| Tabs | 使用页签控制内容切换的容器，每个页签对应一个内容视图。 需配合TabContent子组件使用。 | 需配合断点使用，通过改变不同断点下的vertical和barPosition等属性，实现不同的布局效果。 |
接下来将依次介绍自适应布局和响应式布局，同时结合实际，通过典型布局场景以及典型页面场景详细介绍两种布局能力的用法。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/adaptive-layout-V14
爬取时间: 2025-04-30 04:43:51
来源: Huawei Developer
针对常见的开发场景，方舟开发框架提炼了七种自适应布局能力，这些布局可以独立使用，也可多种布局叠加使用。
| 自适应布局类别 | 自适应布局能力 | 使用场景 | 实现方式 |
| --- | --- | --- | --- |
| 自适应拉伸 | 拉伸能力 | 容器组件尺寸发生变化时，增加或减小的空间全部分配给容器组件内指定区域。 | Flex布局的flexGrow和flexShrink属性 |
|  | 均分能力 | 容器组件尺寸发生变化时，增加或减小的空间均匀分配给容器组件内所有空白区域。 | Row组件、Column组件或Flex组件的justifyContent属性设置为FlexAlign.SpaceEvenly |
| 自适应缩放 | 占比能力 | 子组件的宽或高按照预设的比例，随容器组件发生变化。 | 基于通用属性的两种实现方式： - 将子组件的宽高设置为父组件宽高的百分比 - layoutWeight属性 |
|  | 缩放能力 | 子组件的宽高按照预设的比例，随容器组件发生变化，且变化过程中子组件的宽高比不变。 | 布局约束的aspectRatio属性 |
| 自适应延伸 | 延伸能力 | 容器组件内的子组件，按照其在列表中的先后顺序，随容器组件尺寸变化显示或隐藏。 | 基于容器组件的两种实现方式： - 通过List组件实现 - 通过Scroll组件配合Row组件或Column组件实现 |
|  | 隐藏能力 | 容器组件内的子组件，按照其预设的显示优先级，随容器组件尺寸变化显示或隐藏。相同显示优先级的子组件同时显示或隐藏。 | 布局约束的displayPriority属性 |
| 自适应折行 | 折行能力 | 容器组件尺寸发生变化时，如果布局方向尺寸不足以显示完整内容，自动换行。 | Flex组件的wrap属性设置为FlexWrap.Wrap |
基于通用属性的两种实现方式：
- 将子组件的宽高设置为父组件宽高的百分比
- layoutWeight属性
基于容器组件的两种实现方式：
- 通过List组件实现
- 通过Scroll组件配合Row组件或Column组件实现
下面我们依次介绍这几种自适应布局能力。
拉伸能力
拉伸能力是指容器组件尺寸发生变化时，增加或减小的空间全部分配给容器组件内指定区域。
拉伸能力通常通过Flex布局中的flexGrow和flexShrink属性实现，flexGrow和flexShrink属性常与flexBasis属性搭配使用，故将这三个属性放在一起介绍。
| 属性 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| flexGrow | number | 0 | 仅当父容器宽度大于所有子组件宽度的总和时，该属性生效。配置了此属性的子组件，按照比例拉伸，分配父容器的多余空间。 |
| flexShrink | number | 1 | 仅当父容器宽度小于所有子组件宽度的总和时，该属性生效。配置了此属性的子组件，按照比例收缩，分配父容器的不足空间。 |
| flexBasis | 'auto' | Length | 'auto' | 设置组件在Flex容器中主轴方向上基准尺寸。'auto'意味着使用组件原始的尺寸，不做修改。 flexBasis属性不是必须的，通过width或height也可以达到同样的效果。当flexBasis属性与width或height发生冲突时，以flexBasis属性为准。 |
设置组件在Flex容器中主轴方向上基准尺寸。'auto'意味着使用组件原始的尺寸，不做修改。
flexBasis属性不是必须的，通过width或height也可以达到同样的效果。当flexBasis属性与width或height发生冲突时，以flexBasis属性为准。
-  开发者期望将父容器的剩余空间全部分配给某空白区域时，也可以通过Blank组件实现。注意仅当父组件为Row\Column\Flex组件时，Blank组件才会生效。
-  类Web开发范式也是通过flex-grow和flex-shrink实现拉伸能力，同时也支持配置flex-basis，详见通用样式。
-  类Web开发范式没有提供blank组件，但可以通过div组件模拟blank组件的行为，如“<div style='flex-grow: 1; flex-shrink: 0; flex-basis: 0'></div>”。
示例1
本示例中的页面由中间的内容区（包含一张图片）以及两侧的留白区组成，各区域的属性配置如下。
-  中间内容区的宽度设置为400vp，同时将flexGrow属性设置为1，flexShrink属性设置为0。
-  两侧留白区的宽度设置为150vp，同时将flexGrow属性设置为0，flexShrink属性设置为1。
由上可知，父容器的基准尺寸是700vp（150vp+400vp+150vp）。
可以通过拖动底部的滑动条改变父容器的尺寸，查看布局变化。
-  当父容器的尺寸大于700vp时，父容器中多余的空间全部分配给中间内容区。
-  当父容器的尺寸小于700vp时，左右两侧的留白区按照“1:1”的比例收缩（即平均分配父容器的不足空间）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165824.81882329769342804791751279024636:50001231000000:2800:F326001A83EA5D15EC60B6DD08045497C869647782235AED453BA341E45681B1.gif)
```typescript
@Entry
@Component
struct FlexibleCapabilitySample1 {
@State containerWidth: number = 402
// 底部滑块，可以通过拖拽滑块改变容器尺寸。
@Builder slider() {
Slider({ value: this.containerWidth, min: 402, max: 1000, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.onChange((value: number) => {
this.containerWidth = value;
})
.position({ x: '20%', y: '80%' })
}
build() {
Column() {
Column() {
Row() {
// 通过flexGrow和flexShrink属性，将多余的空间全部分配给图片，将不足的空间全部分配给两侧空白区域。
Row().width(150).height(400).backgroundColor('#FFFFFF')
.flexGrow(0).flexShrink(1)
Image($r("app.media.illustrator")).width(400).height(400)
.objectFit(ImageFit.Contain)
.backgroundColor("#66F1CCB8")
.flexGrow(1).flexShrink(0)
Row().width(150).height(400).backgroundColor('#FFFFFF')
.flexGrow(0).flexShrink(1)
}
.width(this.containerWidth)
.justifyContent(FlexAlign.Center)
.alignItems(VerticalAlign.Center)
}
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
}
```
示例2
文字和开关的尺寸固定，仅有中间空白区域（Blank组件）随父容器尺寸变化而伸缩。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165824.72834674448253201431937430008969:50001231000000:2800:180000F995357C509F190C83074EBD385EDBE0860F00105A4FB2040FDC34671B.gif)
```typescript
@Entry
@Component
struct FlexibleCapabilitySample2 {
@State rate: number = 0.8
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: this.rate * 100, min: 30, max: 80, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.onChange((value: number) => {
this.rate = value / 100;
})
.position({ x: '20%', y: '80%' })
}
build() {
Column() {
Column() {
Row() {
Text('飞行模式')
.fontSize(16)
.width(135)
.height(22)
.fontWeight(FontWeight.Medium)
.lineHeight(22)
Blank()      // 通过Blank组件实现拉伸能力
Toggle({ type: ToggleType.Switch })
.width(36)
.height(20)
}
.height(55)
.borderRadius(12)
.padding({ left: 13, right: 13 })
.backgroundColor('#FFFFFF')
.width(this.rate * 100 + '%')
}
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
}
```
均分能力
均分能力是指容器组件尺寸发生变化时，增加或减小的空间均匀分配给容器组件内所有空白区域。它常用于内容数量固定、均分显示的场景，比如工具栏、底部菜单栏等。
均分能力可以通过将Row组件、Column组件或Flex组件的justifyContent属性设置为FlexAlign.SpaceEvenly实现，即子元素在父容器主轴方向等间距布局，相邻元素之间的间距、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。
-  均分能力还可以通过其它方式实现，如使用Grid网格组件或在每个组件间添加Blank组件等。
-  类Web开发范式中，通过将div组件的justify-content属性设置为space-evenly来实现均分布局。
示例：
父容器尺寸变化过程中，图标及文字的尺寸不变，图标间的间距及图标离左右边缘的距离同时均等改变。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.21945802135931520968595914989357:50001231000000:2800:D936A2192505F6E89A57AE62A174C08216E03D576349F1E68F45B72FB5811AF7.gif)
```typescript
@Entry
@Component
struct EquipartitionCapabilitySample {
readonly list: number [] = [0, 1, 2, 3]
@State rate: number = 0.6
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: this.rate * 100, min: 30, max: 60, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.onChange((value: number) => {
this.rate = value / 100
})
.position({ x: '20%', y: '80%' })
}
build() {
Column() {
Column() {
// 均匀分配父容器主轴方向的剩余空间
Row() {
ForEach(this.list, (item:number) => {
Column() {
Image($r("app.media.startIcon")).width(48).height(48).margin({ top: 8 })
Text('App name')
.width(64)
.height(30)
.lineHeight(15)
.fontSize(12)
.textAlign(TextAlign.Center)
.margin({ top: 8 })
.padding({ bottom: 15 })
}
.width(80)
.height(102)
.flexShrink(1)
})
}
.width('100%')
.justifyContent(FlexAlign.SpaceEvenly)
// 均匀分配父容器主轴方向的剩余空间
Row() {
ForEach(this.list, (item:number) => {
Column() {
Image($r("app.media.startIcon")).width(48).height(48).margin({ top: 8 })
Text('App name')
.width(64)
.height(30)
.lineHeight(15)
.fontSize(12)
.textAlign(TextAlign.Center)
.margin({ top: 8 })
.padding({ bottom: 15 })
}
.width(80)
.height(102)
.flexShrink(1)
})
}
.width('100%')
.justifyContent(FlexAlign.SpaceEvenly)
}
.width(this.rate * 100 + '%')
.height(222)
.padding({ top: 16 })
.backgroundColor('#FFFFFF')
.borderRadius(16)
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
}
```
占比能力
占比能力是指子组件的宽高按照预设的比例，随父容器组件发生变化。
占比能力通常有两种实现方式：
-  将子组件的宽高设置为父组件宽高的百分比，详见尺寸设置及长度类型。
-  通过layoutWeight属性配置互为兄弟关系的组件在父容器主轴方向的布局权重，详见尺寸设置。
layoutWeight存在使用限制，所以实际使用过程中大多通过将子组件宽高设置为父组件的百分比来实现占比能力。
-  占比能力在实际开发中使用的非常广泛，可以通过很多不同的方式实现占比能力，如还可以通过Grid组件的columnsTemplate属性设置网格容器中列的数量及其宽度比例，或通过配置子组件在栅格（本章后文将详细介绍栅格系统）中占据不同的列数来实现占比能力。本小节仅介绍最基础和常用的实现方式，局限性较大或比非常小众的实现方式，本文不做展开介绍。
-  类Web开发范式同样支持以百分比的形式设置组件的宽高，详见通用样式中关于width和height的介绍以及长度类型介绍。
-  与声明式开发范式中的layoutWeight属性类似，类Web开发范式提供了flex-weight样式用于配置互为兄弟关系的组件在父容器主轴方向的布局权重。
示例：
简单的播放控制栏，其中“上一首”、“播放/暂停”、“下一首”的layoutWeight属性都设置为1，因此它们按照“1:1:1”的比例均分父容器主轴方向的空间。
将三个按钮的.layoutWeight(1)分别替换为.width('33%')、.width('34%')、.width('33%')，也可以实现与当前同样的显示效果。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.48461087791840236281805357060177:50001231000000:2800:3E442500962A9AA59099B61BE975AAA1CE3BD568D5453C2AD9CE9C2B2ADDEA33.gif)
```typescript
@Entry
@Component
struct ProportionCapabilitySample {
@State rate: number = 0.5
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: 100, min: 25, max: 50, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.height(50)
.onChange((value: number) => {
this.rate = value / 100
})
.position({ x: '20%', y: '80%' })
}
build() {
Column() {
Column() {
Row() {
Column() {
Image($r("app.media.down"))
.width(48)
.height(48)
}
.height(96)
.layoutWeight(1)  // 设置子组件在父容器主轴方向的布局权重
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
Column() {
Image($r("app.media.pause"))
.width(48)
.height(48)
}
.height(96)
.layoutWeight(1)  // 设置子组件在父容器主轴方向的布局权重
.backgroundColor('#66F1CCB8')
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
Column() {
Image($r("app.media.next"))
.width(48)
.height(48)
}
.height(96)
.layoutWeight(1)  // 设置子组件在父容器主轴方向的布局权重
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
.width(this.rate * 100 + '%')
.height(96)
.borderRadius(16)
.backgroundColor('#FFFFFF')
}
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
}
```
缩放能力
缩放能力是指子组件的宽高按照预设的比例，随容器组件发生变化，且变化过程中子组件的宽高比不变。
缩放能力通过使用百分比布局配合固定宽高比（aspectRatio属性）实现当容器尺寸发生变化时，内容自适应调整。
可以访问布局约束，了解aspectRatio属性的详细信息。
类Web开发范式同样提供了aspect-ratio样式，用于固定组件的宽高比。
示例：
为方便查看效果，示例中特意给Column组件加了边框。可以看到Column组件随着其Flex父组件尺寸变化而缩放的过程中，始终保持预设的宽高比，其中的图片也始终正常显示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.92730599965316773105593423617387:50001231000000:2800:26E647076BEC14BA0AA3D459C8D97DE5A2FB428CCB354540D02D3927E5597B4F.gif)
```typescript
@Entry
@Component
struct ScaleCapabilitySample {
@State sliderWidth: number = 400
@State sliderHeight: number = 400
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: this.sliderHeight, min: 100, max: 400, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.height(50)
.onChange((value: number) => {
this.sliderHeight = value
})
.position({ x: '20%', y: '80%' })
Slider({ value: this.sliderWidth, min: 100, max: 400, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.height(50)
.onChange((value: number) => {
this.sliderWidth = value;
})
.position({ x: '20%', y: '87%' })
}
build() {
Column() {
Column() {
Column() {
Image($r("app.media.illustrator")).width('100%').height('100%')
}
.aspectRatio(1)                           // 固定宽高比
.border({ width: 2, color: "#66F1CCB8"})  // 边框，仅用于展示效果
}
.backgroundColor("#FFFFFF")
.height(this.sliderHeight)
.width(this.sliderWidth)
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor("#F1F3F5")
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
}
```
延伸能力
延伸能力是指容器组件内的子组件，按照其在列表中的先后顺序，随容器组件尺寸变化显示或隐藏。它可以根据显示区域的尺寸，显示不同数量的元素。
延伸能力通常有两种实现方式：
-  通过List组件实现。
-  通过Scroll组件配合Row组件或Column组件实现。
-  List、Row或Column组件中子节点的在页面显示时就已经全部完成了布局计算及渲染，只不过受限于父容器尺寸，用户只能看到一部分。随着父容器尺寸增大，用户可以看到的子节点数目也相应的增加。用户还可以通过手指滑动触发列表滑动，查看被隐藏的子节点。
-  类Web开发范式同样可以使用list组件实现延伸能力。
-  类Web开发范式没有提供scroll组件，但可以将div组件的overflow样式设置为scroll（即div组件主轴方向上子元素的尺寸超过div组件本身的尺寸时进行滚动显示）来模拟scroll组件的行为。
示例：
当父容器的尺寸发生改变时，页面中显示的图标数量随之发生改变。
分别通过List组件实现及通过Scroll组件配合Row组件实现。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.75754965669735181385510017006479:50001231000000:2800:FE77A82140259C93F9EE6620C58493669FAD9A4DC9F54CA177DE3F13226C9AD3.gif)
（1）通过List组件实现。
```typescript
@Entry
@Component
struct ExtensionCapabilitySample1 {
@State rate: number = 0.60
readonly appList: number [] = [0, 1, 2, 3, 4, 5, 6, 7]
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: this.rate * 100, min: 8, max: 60, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.height(50)
.onChange((value: number) => {
this.rate = value / 100
})
.position({ x: '20%', y: '80%' })
}
build() {
Column() {
Row({ space: 10 }) {
// 通过List组件实现隐藏能力
List({ space: 10 }) {
ForEach(this.appList, (item:number) => {
ListItem() {
Column() {
Image($r("app.media.startIcon")).width(48).height(48).margin({ top: 8 })
Text('App name')
.width(64)
.height(30)
.lineHeight(15)
.fontSize(12)
.textAlign(TextAlign.Center)
.margin({ top: 8 })
.padding({ bottom: 15 })
}.width(80).height(102)
}.width(80).height(102)
})
}
.padding({ top: 16, left: 10 })
.listDirection(Axis.Horizontal)
.width('100%')
.height(118)
.borderRadius(16)
.backgroundColor(Color.White)
}
.width(this.rate * 100 + '%')
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
}
```
（2）通过Scroll组件配合Row组件实现。
```typescript
@Entry
@Component
struct ExtensionCapabilitySample2 {
private scroller: Scroller = new Scroller()
@State rate: number = 0.60
@State appList: number [] = [0, 1, 2, 3, 4, 5, 6, 7]
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: this.rate * 100, min: 8, max: 60, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.height(50)
.onChange((value: number) => {
this.rate = value / 100;
})
.position({ x: '20%', y: '80%' })
}
build() {
Column() {
// 通过Scroll和Row组件实现隐藏能力
Scroll(this.scroller) {
Row({ space: 10 }) {
ForEach(this.appList, () => {
Column() {
Image($r("app.media.startIcon")).width(48).height(48).margin({ top: 8 })
Text('App name')
.width(64)
.height(30)
.lineHeight(15)
.fontSize(12)
.textAlign(TextAlign.Center)
.margin({ top: 8 })
.padding({ bottom: 15 })
}.width(80).height(102)
})
}
.padding({ top: 16, left: 10 })
.height(118)
.backgroundColor(Color.White)
}
.scrollable(ScrollDirection.Horizontal)
.borderRadius(16)
.width(this.rate * 100 + '%')
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
}
```
隐藏能力
隐藏能力是指容器组件内的子组件，按照其预设的显示优先级，随容器组件尺寸变化显示或隐藏，其中相同显示优先级的子组件同时显示或隐藏。它是一种比较高级的布局方式，常用于分辨率变化较大，且不同分辨率下显示内容有所差异的场景。主要思想是通过增加或减少显示内容，来保持最佳的显示效果。
隐藏能力通过设置布局优先级（displayPriority属性）来控制显隐，当布局主轴方向剩余尺寸不足以满足全部元素时，按照布局优先级大小，从小到大依次隐藏，直到容器能够完整显示剩余元素。具有相同布局优先级的元素将同时显示或者隐藏。
可以访问布局约束，了解displayPriority属性的详细信息。
类Web开发范式同样支持display-index样式，用于设置布局优先级。
示例：
父容器尺寸发生变化时，其子元素按照预设的优先级显示或隐藏。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.83134120291364097455916483402807:50001231000000:2800:D230B4FD757F65A065FFFB7EA7145881ECFD3EC3CD69FB4A4B37B09F96C9C524.gif)
```typescript
@Entry
@Component
struct HiddenCapabilitySample {
@State rate: number = 0.45
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: this.rate * 100, min: 10, max: 45, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.height(50)
.onChange((value: number) => {
this.rate = value / 100
})
.position({ x: '20%', y: '80%' })
}
build() {
Column() {
Row({ space:24 }) {
Image($r("app.media.favorite"))
.width(48)
.height(48)
.objectFit(ImageFit.Contain)
.displayPriority(1)  // 布局优先级
Image($r("app.media.down"))
.width(48)
.height(48)
.objectFit(ImageFit.Contain)
.displayPriority(2)  // 布局优先级
Image($r("app.media.pause"))
.width(48)
.height(48)
.objectFit(ImageFit.Contain)
.displayPriority(3)  // 布局优先级
Image($r("app.media.next"))
.width(48)
.height(48)
.objectFit(ImageFit.Contain)
.displayPriority(2)  // 布局优先级
Image($r("app.media.list"))
.width(48)
.height(48)
.objectFit(ImageFit.Contain)
.displayPriority(1)  // 布局优先级
}
.width(this.rate * 100 + '%')
.height(96)
.borderRadius(16)
.backgroundColor('#FFFFFF')
.justifyContent(FlexAlign.Center)
.alignItems(VerticalAlign.Center)
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
.alignItems(HorizontalAlign.Center)
}
}
```
折行能力
折行能力是指容器组件尺寸发生变化，当布局方向尺寸不足以显示完整内容时自动换行。它常用于横竖屏适配或默认设备向平板切换的场景。
折行能力通过使用Flex折行布局（将wrap属性设置为FlexWrap.Wrap）实现，当横向布局尺寸不足以完整显示内容元素时，通过折行的方式，将元素显示在下方。
可以访问Flex组件，了解Flex组件的详细用法。
类Web开发范式通过将div组件的flex-warp样式设置为wrap来使用折行能力。
示例：
父容器中的图片尺寸固定，当父容器尺寸发生变化，其中的内容做自适应换行。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.32314046272097698021814244926169:50001231000000:2800:5E501454B2E24959E696E17BB7F8D386BB1A260F548D2AAABBC76AD4DDF332E5.gif)
```typescript
@Entry
@Component
struct WrapCapabilitySample {
@State rate: number = 0.7
readonly imageList: Resource [] = [
$r('app.media.flexWrap1'),
$r('app.media.flexWrap2'),
$r('app.media.flexWrap3'),
$r('app.media.flexWrap4'),
$r('app.media.flexWrap5'),
$r('app.media.flexWrap6')
]
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: this.rate * 100, min: 50, max: 70, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.onChange((value: number) => {
this.rate = value / 100
})
.position({ x: '20%', y: '87%' })
}
build() {
Flex({ justifyContent: FlexAlign.Center, direction: FlexDirection.Column }) {
Column() {
// 通过Flex组件warp参数实现自适应折行
Flex({
direction: FlexDirection.Row,
alignItems: ItemAlign.Center,
justifyContent: FlexAlign.Center,
wrap: FlexWrap.Wrap
}) {
ForEach(this.imageList, (item:Resource) => {
Image(item).width(183).height(138).padding(10)
})
}
.backgroundColor('#FFFFFF')
.padding(20)
.width(this.rate * 100 + '%')
.borderRadius(16)
}
.width('100%')
this.slider()
}.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/responsive-layout-V14
爬取时间: 2025-04-30 04:44:05
来源: Huawei Developer
自适应布局可以保证窗口尺寸在一定范围内变化时，页面的显示是正常的。但是将窗口尺寸变化较大时（如窗口宽度从400vp变化为1000vp），仅仅依靠自适应布局可能出现图片异常放大或页面内容稀疏、留白过多等问题，此时就需要借助响应式布局能力调整页面结构。
响应式布局是指页面内的元素可以根据特定的特征（如窗口宽度、屏幕方向等）自动变化以适应外部容器变化的布局能力。响应式布局中最常使用的特征是窗口宽度，可以将窗口宽度划分为不同的范围（下文中称为断点）。当窗口宽度从一个断点变化到另一个断点时，改变页面布局（如将页面内容从单列排布调整为双列排布甚至三列排布等）以获得更好的显示效果。
当前系统提供了如下三种响应式布局能力，后文中我们将依次展开介绍。
| 响应式布局能力 | 简介 |
| --- | --- |
| 断点 | 将窗口宽度划分为不同的范围（即断点），监听窗口尺寸变化，当断点改变时同步调整页面布局。 |
| 媒体查询 | 媒体查询支持监听窗口宽度、横竖屏、深浅色、设备类型等多种媒体特征，当媒体特征发生改变时同步调整页面布局。 |
| 栅格布局 | 栅格组件将其所在的区域划分为有规律的多列，通过调整不同断点下的栅格组件的参数以及其子组件占据的列数等，实现不同的布局效果。 |
断点
断点以应用窗口宽度为切入点，将应用窗口在宽度维度上分成了几个不同的区间即不同的断点，在不同的区间下，开发者可根据需要实现不同的页面布局效果。具体的断点如下所示。
| 断点名称 | 取值范围（vp） |
| --- | --- |
| xs | [0, 320） |
| sm | [320, 600) |
| md | [600, 840) |
| lg | [840, +∞) |
-  以设备屏幕宽度作为参照物，也可以实现类似的效果。考虑到应用可能以非全屏窗口的形式显示，以应用窗口宽度为参照物更为通用。
-  开发者可以根据实际使用场景决定适配哪些断点。如xs断点对应的一般是智能穿戴类设备，如果确定某页面不会在智能穿戴设备上显示，则可以不适配xs断点。
-  可以根据实际需要在lg断点后面新增xl、xxl等断点，但注意新增断点会同时增加UX设计师及应用开发者的工作量，除非必要否则不建议盲目新增断点。
系统提供了多种方法，判断应用当前处于何种断点，进而可以调整应用的布局。常见的监听断点变化的方法如下所示：
-  获取窗口对象并监听窗口尺寸变化
-  通过媒体查询监听应用窗口尺寸变化
-  借助栅格组件能力监听不同断点的变化
本小节中，先介绍如何通过窗口对象监听断点变化，后续的媒体查询及栅格章节中，将进一步展开介绍另外两种方法。
通过窗口对象监听断点变化的核心是获取窗口对象及注册窗口尺寸变化的回调函数。
1.  在UIAbility的onWindowStageCreate生命周期回调中，通过窗口对象获取启动时的应用窗口宽度并注册回调函数监听窗口尺寸变化。将窗口尺寸的长度单位由px换算为vp后，即可基于前文中介绍的规则得到当前断点值，此时可以使用状态变量记录当前的断点值方便后续使用。
```typescript
// MainAbility.ts
import { window, display } from '@kit.ArkUI'
import { UIAbility } from '@kit.AbilityKit'
export default class MainAbility extends UIAbility {
private windowObj?: window.Window
private curBp: string = ''
//...
// 根据当前窗口尺寸更新断点
private updateBreakpoint(windowWidth: number) :void{
// 将长度的单位由px换算为vp
let windowWidthVp = windowWidth / display.getDefaultDisplaySync().densityPixels
let newBp: string = ''
if (windowWidthVp < 320) {
newBp = 'xs'
} else if (windowWidthVp < 600) {
newBp = 'sm'
} else if (windowWidthVp < 840) {
newBp = 'md'
} else {
newBp = 'lg'
}
if (this.curBp !== newBp) {
this.curBp = newBp
// 使用状态变量记录当前断点值
AppStorage.setOrCreate('currentBreakpoint', this.curBp)
}
}
onWindowStageCreate(windowStage: window.WindowStage) :void{
windowStage.getMainWindow().then((windowObj) => {
this.windowObj = windowObj
// 获取应用启动时的窗口尺寸
this.updateBreakpoint(windowObj.getWindowProperties().windowRect.width)
// 注册回调函数，监听窗口尺寸变化
windowObj.on('windowSizeChange', (windowSize)=>{
this.updateBreakpoint(windowSize.width)
})
});
// ...
}
//...
}
```
2.  在页面中，获取及使用当前的断点。
```typescript
@Entry
@Component
struct Index {
@StorageProp('currentBreakpoint') curBp: string = 'sm'
build() {
Flex({justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center}) {
Text(this.curBp).fontSize(50).fontWeight(FontWeight.Medium)
}
.width('100%')
.height('100%')
}
}
```
3.  运行及验证效果。
|  |  |  |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.38119163710727113644090607072723:50001231000000:2800:3B9FA6F1FB4DF23C3F94286DA6ABE4F22ECE6FEBF96E71BEB4B6B97A39819C81.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.04702999277074109547899935404029:50001231000000:2800:7DEDA46F54A2EACEF9FD964C276DFA223C10FC9A33078BA4EB49E5B38D51B08C.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165825.60300575886612987164231605743606:50001231000000:2800:A602494F4BDA06192CEB3D64A5C194C7A5CBA32F1B92E91DFDE3FE24F25B5ADB.jpg)
媒体查询
在实际应用开发过程中，开发者常常需要针对不同类型设备或同一类型设备的不同状态来修改应用的样式。媒体查询提供了丰富的媒体特征监听能力，可以监听应用显示区域变化、横竖屏、深浅色、设备类型等等，因此在应用开发过程中使用的非常广泛。
本小节仅介绍媒体查询跟断点的结合，即如何借助媒体查询能力，监听断点的变化，读者可以自行查阅官网中关于媒体查询的相关介绍了解更详细的用法。
类Web开发范式，支持在js文件和css文件中使用媒体查询，请查看js媒体查询和css媒体查询了解详细用法。
示例：
通过媒体查询，监听应用窗口宽度变化，获取当前应用所处的断点值。
|  |  |  |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.81796759722826646199937124415664:50001231000000:2800:C63A8A590981116A2B25BB7181621B7B82BBAED5689340AD737B3309DE864872.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.18217666858886941771393532528437:50001231000000:2800:7AD88AFE436CD3B96B5C130ECE35A45B00DE2490103C77B0A0A8091EC021EEC4.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.33434241607781909704413891526706:50001231000000:2800:78864B2A9A82AE07D063EEC6C6A399F830D20119B0D1CACEF3296E99A6AE9D2A.jpg)
1.对通过媒体查询监听断点的功能做简单的封装，方便后续使用
```typescript
// common/breakpointsystem.ets
import { mediaquery } from '@kit.ArkUI'
export type BreakpointType = 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl'
export interface Breakpoint {
name: BreakpointType
size: number
mediaQueryListener?: mediaquery.MediaQueryListener
}
export class BreakpointSystem {
private static instance: BreakpointSystem
private readonly breakpoints: Breakpoint[] = [
{ name: 'xs', size: 0 },
{ name: 'sm', size: 320 },
{ name: 'md', size: 600 },
{ name: 'lg', size: 840 }
]
private states: Set<BreakpointState<Object>>
private constructor() {
this.states = new Set()
}
public static getInstance(): BreakpointSystem {
if (!BreakpointSystem.instance) {
BreakpointSystem.instance = new BreakpointSystem();
}
return BreakpointSystem.instance
}
public attach(state: BreakpointState<Object>): void {
this.states.add(state)
}
public detach(state: BreakpointState<Object>): void {
this.states.delete(state)
}
public start() {
this.breakpoints.forEach((breakpoint: Breakpoint, index) => {
let condition: string
if (index === this.breakpoints.length - 1) {
condition = `(${breakpoint.size}vp<=width)`
} else {
condition = `(${breakpoint.size}vp<=width<${this.breakpoints[index + 1].size}vp)`
}
breakpoint.mediaQueryListener = mediaquery.matchMediaSync(condition)
if (breakpoint.mediaQueryListener.matches) {
this.updateAllState(breakpoint.name)
}
breakpoint.mediaQueryListener.on('change', (mediaQueryResult) => {
if (mediaQueryResult.matches) {
this.updateAllState(breakpoint.name)
}
})
})
}
private updateAllState(type: BreakpointType): void {
this.states.forEach(state => state.update(type))
}
public stop() {
this.breakpoints.forEach((breakpoint: Breakpoint, index) => {
if (breakpoint.mediaQueryListener) {
breakpoint.mediaQueryListener.off('change')
}
})
this.states.clear()
}
}
export interface BreakpointOptions<T> {
xs?: T
sm?: T
md?: T
lg?: T
xl?: T
xxl?: T
}
export class BreakpointState<T extends Object> {
public value: T | undefined = undefined;
private options: BreakpointOptions<T>
constructor(options: BreakpointOptions<T>) {
this.options = options
}
static of<T extends Object>(options: BreakpointOptions<T>): BreakpointState<T> {
return new BreakpointState(options)
}
public update(type: BreakpointType): void {
if (type === 'xs') {
this.value = this.options.xs
} else if (type === 'sm') {
this.value = this.options.sm
} else if (type === 'md') {
this.value = this.options.md
} else if (type === 'lg') {
this.value = this.options.lg
} else if (type === 'xl') {
this.value = this.options.xl
} else if (type === 'xxl') {
this.value = this.options.xxl
} else {
this.value = undefined
}
}
}
```
2.在页面中，通过媒体查询，监听应用窗口宽度变化，获取当前应用所处的断点值
```typescript
// MediaQuerySample.ets
import { BreakpointSystem, BreakpointState } from '../common/breakpointsystem'
@Entry
@Component
struct MediaQuerySample {
@State compStr: BreakpointState<string> = BreakpointState.of({ sm: "sm", md: "md", lg: "lg" })
@State compImg: BreakpointState<Resource> = BreakpointState.of({
sm: $r('app.media.sm'),
md: $r('app.media.md'),
lg: $r('app.media.lg')
});
aboutToAppear() {
BreakpointSystem.getInstance().attach(this.compStr)
BreakpointSystem.getInstance().attach(this.compImg)
BreakpointSystem.getInstance().start()
}
aboutToDisappear() {
BreakpointSystem.getInstance().detach(this.compStr)
BreakpointSystem.getInstance().detach(this.compImg)
BreakpointSystem.getInstance().stop()
}
build() {
Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
Column()
.height(100)
.width(100)
.backgroundImage(this.compImg.value)
.backgroundImagePosition(Alignment.Center)
.backgroundImageSize(ImageSize.Contain)
Text(this.compStr.value)
.fontSize(24)
.margin(10)
}
.width('100%')
.height('100%')
}
}
```
栅格布局
简介
栅格是多设备场景下通用的辅助定位工具，通过将空间分割为有规律的栅格。栅格可以显著降低适配不同屏幕尺寸的设计及开发成本，使得整体设计和开发流程更有秩序和节奏感，同时也保证多设备上应用显示的协调性和一致性，提升用户体验。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.66535014447447632104856657359088:50001231000000:2800:0D9EA8C82835E00B2BE2A9F610196343C6F28AD2CAC8FA7C7A19061BA2477DB7.png)
栅格的样式由Margin、Gutter、Columns三个属性决定。
-  Margin是相对应用窗口、父容器的左右边缘的距离，决定了内容可展示的整体宽度。
-  Gutter是相邻的两个Column之间的距离，决定内容间的紧密程度。
-  Columns是栅格中的列数，其数值决定了内容的布局复杂度。
单个Column的宽度是系统结合Margin、Gutter和Columns自动计算的，不需要也不允许开发者手动配置。
栅格布局就是栅格结合了断点，实现栅格布局能力的组件叫栅格组件。在实际使用场景中，可以根据需要配置不同断点下栅格组件中元素占据的列数，同时也可以调整Margin、Gutter、Columns的取值，从而实现不同的布局效果。
| sm断点 | md断点 |
| --- | --- |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.78208421300650266649062639256330:50001231000000:2800:68BBEB54BF8F454D1324BB4C8FC8AE165421972D1898BC7413F535A10084A06D.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.16944641126436252242518812278543:50001231000000:2800:738F5191291A94D3B8FDABC89E8C2045A2C400C11F71B170092FD0BD2772E4D4.jpg)
-  ArkUI在API 9对栅格组件做了重构，推出了新的栅格组件GridRow和GridCol，同时原有的GridContainer组件及栅格设置已经废弃。
-  本文中提到的栅格组件，如无特别说明，都是指GridRow和GridCol组件。
栅格组件的断点
栅格组件提供了丰富的断点定制能力。
（一）开发者可以修改断点的取值范围，支持启用最多6个断点。
-  基于本文断点小节介绍的推荐值，栅格组件默认提供xs、sm、md、lg四个断点。
-  栅格组件支持开发者修改断点的取值范围，除了默认的四个断点，还支持开发者启用xl和xxl两个额外的断点。
断点并非越多越好，通常每个断点都需要开发者“精心适配”以达到最佳显示效果。
示例1：
修改默认的断点范围，同时启用xl和xxl断点。
图片右下角显示了当前设备屏幕的尺寸（即应用窗口尺寸），可以看到随着窗口尺寸发生变化，栅格的断点也相应发生了改变（为了便于理解，下图中将设备的DPI设置为160，此时1vp=1px）。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.99546074585583507354391009262621:50001231000000:2800:5B83417E3C0EAF042D1F86EBD3AC7A5465F5C364FC1E4E01E0ACE6C6E752E04B.gif)
```typescript
@Entry
@Component
struct GridRowSample1 {
@State private currentBreakpoint: string = 'unknown'
build() {
// 修改断点的取值范围同时启用更多断点，注意，修改的断点值后面必须加上vp单位。
GridRow({breakpoints: {value: ['600vp', '700vp', '800vp', '900vp', '1000vp'],
reference: BreakpointsReference.WindowSize}}) {
GridCol({span:{xs: 12, sm: 12, md: 12, lg:12, xl: 12, xxl:12}}) {
Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
Text(this.currentBreakpoint).fontSize(50).fontWeight(FontWeight.Medium)
}
}
}.onBreakpointChange((currentBreakpoint: string) => {
this.currentBreakpoint = currentBreakpoint
})
}
}
```
（二）栅格断点默认以窗口宽度为参照物，同时还允许开发者配置为以栅格组件本身的宽度为参照物。
栅格既可以用于页面整体布局的场景，也可以用于页面局部布局的场景。考虑到在实际场景中，存在应用窗口尺寸不变但是局部区域尺寸发生了变化的情况，栅格组件支持以自身宽度为参照物响应断点变化具有更大的灵活性。
示例2：
以栅格组件宽度为参考物响应断点变化。满足窗口尺寸不变，而部分内容区需要做响应式变化的场景。
为了便于理解，下图中自定义预览器的设备屏幕宽度设置为650vp。示例代码中将侧边栏的变化范围控制在[100vp, 600vp]，那么右侧的栅格组件宽度相对应在[550vp, 50vp]之间变化。根据代码中对栅格断点的配置，栅格组件宽度发生变化时，其断点相应的发生改变。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.99986599380952361976000018531986:50001231000000:2800:0E7A4AA879006EAE1666C9CA87C818A7730A50873864C126D10C4A1ED670FE07.gif)
```typescript
@Entry
@Component
struct GridRowSample2 {
@State private currentBreakpoint: string = 'unknown';
build() {
// 用户可以通过拖拽侧边栏组件中的分隔线，调整侧边栏和内容区的宽度。
SideBarContainer(SideBarContainerType.Embed)
{
// 侧边栏，尺寸变化范围 [100vp, 600vp]
Column(){}.width('100%').backgroundColor('#19000000')
// 内容区，尺寸变化范围 [550vp, 50vp]
GridRow({breakpoints: {value: ['100vp', '200vp', '300vp', '400vp', '500vp'],
reference: BreakpointsReference.ComponentSize}}) {
GridCol({span:{xs: 12, sm: 12, md: 12, lg:12, xl: 12, xxl:12}}) {
Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
Text(this.currentBreakpoint).fontSize(50).fontWeight(FontWeight.Medium)
}
}
}.onBreakpointChange((currentBreakpoint: string) => {
this.currentBreakpoint = currentBreakpoint;
}).width('100%')
}
// 侧边栏拖拽到最小宽度时，不自动隐藏
.autoHide(false)
.sideBarWidth(100)
// 侧边栏的最小宽度
.minSideBarWidth(100)
// 侧边栏的最大宽度
.maxSideBarWidth(600)
}
}
```
（三）栅格组件的断点发生变化时，会通过onBreakPointChange事件通知开发者。
在之前的两个例子中，已经演示了onBreakpointChange事件的用法，此处不再赘述。
栅格组件的columns、gutter和margin
栅格组件columns默认为12列，gutter默认为0，同时支持开发者根据实际需要定义不同断点下的columns数量以及gutter长度。特别的，在栅格组件实际使用过程中，常常会发生多个元素占据的列数相加超过总列数而折行的场景。栅格组件还允许开发者分别定义水平方向的gutter（相邻两列之间的间距）和垂直方向的gutter（折行时相邻两行之间的间距）。
考虑到组件通用属性中已经有margin和padding，栅格组件不再单独提供额外的margin属性，直接使用通用属性即可。借助margin或者padding属性，均可以控制栅格组件与父容器左右边缘的距离，但是二者也存在一些差异：
-  margin区域在栅格组件的边界外，padding区域在栅格组件的边界内。
-  栅格组件的backgroundColor会影响padding区域，但不会影响margin区域。
总的来讲，margin在组件外而padding在组件内，开发者可以根据实际需要进行选择及实现目标效果。
示例3：
不同断点下，定义不同的columns和gutter。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.81438879306035186529360755726898:50001231000000:2800:4750CB05C55AF57849B946CB1CF094059B838A82661AEB168C9ED473FB929B23.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.54908429762226318363747550982082:50001231000000:2800:361DDF9F8E315F7DA3C3CBAA959DF1C084B668EEAF184FEDE9FE613293DEEE19.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165826.27137230510885632152013353422207:50001231000000:2800:928508ABFEF7B60A744435A6971BB6EAA643678081B292C104E86913E14F815D.jpg)
```typescript
@Entry
@Component
struct GridRowSample3 {
private bgColors: ResourceColor[] = [
$r('sys.color.ohos_id_color_palette_aux1'),
$r('sys.color.ohos_id_color_palette_aux2'),
$r('sys.color.ohos_id_color_palette_aux3'),
$r('sys.color.ohos_id_color_palette_aux4'),
$r('sys.color.ohos_id_color_palette_aux5'),
$r('sys.color.ohos_id_color_palette_aux6')
]
build() {
// 配置不同断点下columns和gutter的取值
GridRow({columns: {sm: 4, md: 8, lg: 12},
gutter: {x: {sm: 8, md: 16, lg: 24}, y: {sm: 8, md: 16, lg: 24}}}) {
ForEach(this.bgColors, (bgColor:ResourceColor)=>{
GridCol({span: {sm: 2, md: 2, lg: 2}}) {
Row().backgroundColor(bgColor).height(30).width('100%')
}
})
}
}
}
```
示例4：
通过通用属性margin或者padding，均可以控制栅格组件与其父容器左右两侧的距离，但padding区域计算在栅格组件内而margin区域计算在栅格组件外。此外，借助onBreakpointChange事件，还可以改变不同断点下margin或padding值。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.16042823471567242953180039821049:50001231000000:2800:E67503E6349DB0267C1302FEB1F565CED184F87EEE2F976D00D8DC6666841EA6.png)
```typescript
@Entry
@Component
struct GridRowSample4 {
@State private gridMargin: number = 0
build() {
Column() {
Row().width('100%').height(30)
// 使用padding控制栅格左右间距
GridRow() {
GridCol({span:{xs: 12, sm: 12, md: 12, lg:12}}) {
Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
Text("padding").fontSize(24).fontWeight(FontWeight.Medium)
}.backgroundColor('#19000000').width('100%')
}
}
.height(50)
.borderWidth(2)
.borderColor('#F1CCB8')
.padding({left: this.gridMargin, right: this.gridMargin})
// 借助断点变化事件配置不同断点下栅格组件的左右间距值
.onBreakpointChange((currentBreakpoint: string) => {
if (currentBreakpoint === 'lg' || currentBreakpoint === 'md') {
this.gridMargin = 24
} else {
this.gridMargin = 12
}
})
Row().width('100%').height(30)
// 使用margin控制栅格左右间距
GridRow() {
GridCol({span:{xs: 12, sm: 12, md: 12, lg:12}}) {
Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
Text("margin").fontSize(24).fontWeight(FontWeight.Medium)
}.backgroundColor('#19000000').width('100%')
}
}
.height(50)
.borderWidth(2)
.borderColor('#F1CCB8')
.margin({left: this.gridMargin, right: this.gridMargin})
}
}
}
```
栅格组件的span、offset和order
栅格组件（GridRow）的直接孩子节点只可以是栅格子组件（GridCol），GridCol组件支持配置span、offset和order三个参数。这三个参数的取值按照"xs -> sm -> md -> lg -> xl -> xxl"的向后方向具有继承性（不支持向前方向的继承性），例如将sm断点下span的值配置为3，不配置md断点下span的值，则md断点下span的取值也是3。
| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| span | {xs?: number, sm?: number, md?: number, lg?: number, xl?: number, xxl?:number} | 是 | - | 在栅格中占据的列数。span为0，意味着该元素既不参与布局计算，也不会被渲染。 |
| offset | {xs?: number, sm?: number, md?: number, lg?: number, xl?: number, xxl?:number} | 否 | 0 | 相对于前一个栅格子组件偏移的列数。 |
| order | {xs?: number, sm?: number, md?: number, lg?: number, xl?: number, xxl?:number} | 否 | 0 | 元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。 |
示例5：
通过span参数配置GridCol在不同断点下占据不同的列数。特别的，将md断点下3和6的span配置为0，这样在md断点下3和6不会渲染和显示。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.30741709371982491005166187226869:50001231000000:2800:F3BED7D2360BF2376B1DA4E28B10E3CB2058D1D47459D809E8EC9669866E633F.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.09544712086539173007129678363982:50001231000000:2800:AAE62B653F56F64F6CD2BA4042CD31783743356DCC554C65F0523204B101B8C5.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.99407942284233711164006916215883:50001231000000:2800:B80778F7EFDC1EE1F285F8D7CDFF1775FF45AF8E8CEFC1D5019E0CB6920D4340.jpg)
```typescript
class Obj {
public index: number = 1;
public color: Resource = $r('sys.color.ohos_id_color_palette_aux1')
}
@Entry
@Component
struct GridRowSample5 {
private elements: Obj[] = [
{index: 1, color: $r('sys.color.ohos_id_color_palette_aux1')},
{index: 2, color: $r('sys.color.ohos_id_color_palette_aux2')},
{index: 3, color: $r('sys.color.ohos_id_color_palette_aux3')},
{index: 4, color: $r('sys.color.ohos_id_color_palette_aux4')},
{index: 5, color: $r('sys.color.ohos_id_color_palette_aux5')},
{index: 6, color: $r('sys.color.ohos_id_color_palette_aux6')},
]
build() {
GridRow() {
ForEach(this.elements, (item:Obj)=>{
GridCol({span: {sm: 6, md: (item.index % 3 === 0) ? 0 : 4, lg: 3}}) {
Row() {
Text('' + item.index).fontSize(24)
}
.justifyContent(FlexAlign.Center)
.backgroundColor(item.color).height(30).width('100%')
}
})
}
}
}
```
示例6：
通过offset参数，配置GridCol相对其前一个兄弟间隔的列数。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.75807753468481307359051771752885:50001231000000:2800:364FB2DE6592BDAB5DC8CC58A307AE07D8E4C728E20718AEEB6106EA4F5EB26D.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.37393350904464677936868699051700:50001231000000:2800:01C74DA66E31350AF6FCAA77A8393C5AC99D41D581BCBD53E011617221B6CA2F.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.64769349762739978704021099742147:50001231000000:2800:A51C61DE9681F1FFD9A7380BB54D6EC815B91DEB01942B1E15108A89E0F5719C.jpg)
```typescript
class Obj {
public index: number = 1;
public color: Resource = $r('sys.color.ohos_id_color_palette_aux1')
}
@Entry
@Component
struct GridRowSample6 {
private elements: Obj[] = [
{index: 1, color: $r('sys.color.ohos_id_color_palette_aux1')},
{index: 2, color: $r('sys.color.ohos_id_color_palette_aux2')},
{index: 3, color: $r('sys.color.ohos_id_color_palette_aux3')},
{index: 4, color: $r('sys.color.ohos_id_color_palette_aux4')},
{index: 5, color: $r('sys.color.ohos_id_color_palette_aux5')},
{index: 6, color: $r('sys.color.ohos_id_color_palette_aux6')},
]
build() {
GridRow() {
ForEach(this.elements, (item:Obj)=>{
GridCol({span: {sm: 6, md: 4, lg: 3}, offset: {sm: 0, md: 2, lg: 1} }) {
Row() {
Text('' + item.index).fontSize(24)
}
.justifyContent(FlexAlign.Center)
.backgroundColor(item.color).height(30).width('100%')
}
})
}
}
}
```
示例7：
通过order属性，控制GridCol的顺序。在sm和md断点下，按照1至6的顺序排列显示；在lg断点下，按照6至1的顺序排列显示。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.31359668599133344033023878390985:50001231000000:2800:9351773E82A082869F8F9471BB8A98499F60A0FF383AB531075E465D5E8986CF.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.83378256252174688808056499261651:50001231000000:2800:F5538081CEC8AF6A72964DEF01312E236B9150A5DEEF92AAE112B8EA68E338C9.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.65869658420596694849046138352394:50001231000000:2800:D8635BFF389B2D45485E58EBAE0BA746275C9B3481D1C877F9977851D01ABDF7.jpg)
```typescript
class Obj {
public index: number = 1;
public color: Resource = $r('sys.color.ohos_id_color_palette_aux1')
}
@Entry
@Component
struct GridRowSample7 {
private elements: Obj[] = [
{index: 1, color: $r('sys.color.ohos_id_color_palette_aux1')},
{index: 2, color: $r('sys.color.ohos_id_color_palette_aux2')},
{index: 3, color: $r('sys.color.ohos_id_color_palette_aux3')},
{index: 4, color: $r('sys.color.ohos_id_color_palette_aux4')},
{index: 5, color: $r('sys.color.ohos_id_color_palette_aux5')},
{index: 6, color: $r('sys.color.ohos_id_color_palette_aux6')},
]
build() {
GridRow() {
ForEach(this.elements, (item:Obj)=>{
GridCol({span: {sm: 6, md: 4, lg: 3}, order: {lg: (6-item.index)}}) {
Row() {
Text('' + item.index).fontSize(24)
}
.justifyContent(FlexAlign.Center)
.backgroundColor(item.color).height(30).width('100%')
}
})
}
}
}
```
示例8：
仅配置sm和lg断点下span、offset和order参数的值，则md断点下这三个参数的取值与sm断点相同（按照“sm->md->lg”的向后方向继承）。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.41610130669847898286088617716219:50001231000000:2800:D3353776C0B375CB27716950B10105B358A7A7ADF6AB691F1D87C1C11D0A3B45.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.58499095032343876336315738584999:50001231000000:2800:B99A4FC20FADD53EAF59A74C19A6AF5C2A536DDE5D71C1233D4C340247DFCF83.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.51499039560300942611461536186724:50001231000000:2800:C5A650192E0089185202247719605024C798463C9454AB2EC3513755A037A5F8.jpg)
```typescript
class Obj {
public index: number = 1;
public color: Resource = $r('sys.color.ohos_id_color_palette_aux1')
}
@Entry
@Component
struct GridRowSample8 {
private elements: Obj[] = [
{index: 1, color: $r('sys.color.ohos_id_color_palette_aux1')},
{index: 2, color: $r('sys.color.ohos_id_color_palette_aux2')},
{index: 3, color: $r('sys.color.ohos_id_color_palette_aux3')},
{index: 4, color: $r('sys.color.ohos_id_color_palette_aux4')},
{index: 5, color: $r('sys.color.ohos_id_color_palette_aux5')},
{index: 6, color: $r('sys.color.ohos_id_color_palette_aux6')},
]
build() {
GridRow() {
ForEach(this.elements, (item:Obj)=>{
// 不配置md断点下三个参数的值，则其取值与sm断点相同
GridCol({span: {sm:4, lg: 3}, offset: {sm: 2, lg: 1},
order: {sm: (6-item.index), lg: item.index}}) {
Row() {
Text('' + item.index).fontSize(24)
}
.justifyContent(FlexAlign.Center)
.backgroundColor(item.color).height(30).width('100%')
}
})
}
}
}
```
栅格组件的嵌套使用
栅格组件可以嵌套使用以满足复杂场景的需要。
示例9：
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.48169070444396099698576643832955:50001231000000:2800:9A18C0C622307FB8B49FFD4AB78747BF35DAD9F1ABDA566810C515EE511B905B.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.63806287213420486249888069106175:50001231000000:2800:E7DAF4406215194261987FB6A367BA1C81A86C2B4CE27276DE8A21E50509486D.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165827.20173103156377058498404612039613:50001231000000:2800:BFC4C28B9127CBD966B909357A843143DA6E1D5D4A2067D3B7E34FFDEC71B48B.jpg)
```typescript
class Obj {
public index: number = 1;
public color: Resource = $r('sys.color.ohos_id_color_palette_aux1')
}
@Entry
@Component
struct GridRowSample9 {
private elements: Obj[] = [
{index: 1, color: $r('sys.color.ohos_id_color_palette_aux1')},
{index: 2, color: $r('sys.color.ohos_id_color_palette_aux2')},
{index: 3, color: $r('sys.color.ohos_id_color_palette_aux3')},
{index: 4, color: $r('sys.color.ohos_id_color_palette_aux4')},
{index: 5, color: $r('sys.color.ohos_id_color_palette_aux5')},
{index: 6, color: $r('sys.color.ohos_id_color_palette_aux6')},
]
build() {
GridRow() {
GridCol({span: {sm: 12, md: 10, lg: 8}, offset: {sm: 0, md: 1, lg: 2}}) {
GridRow() {
ForEach(this.elements, (item:Obj)=>{
GridCol({span: {sm: 6, md: 4, lg: 3}}) {
Row() {
Text('' + item.index).fontSize(24)
}
.justifyContent(FlexAlign.Center)
.backgroundColor(item.color).height(30).width('100%')
}
})
}
.backgroundColor('#19000000')
.height('100%')
}
}
}
}
```
总结
如前所述，栅格组件提供了丰富的自定义能力，功能异常灵活和强大。只需要明确栅格在不同断点下的Columns、Margin、Gutter及span等参数，即可确定最终布局，无需关心具体的设备类型及设备状态（如横竖屏）等。栅格可以节约设计团队与开发团队的沟通成本，提升整体开发效率。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/typical-layout-scenario-V14
爬取时间: 2025-04-30 04:44:20
来源: Huawei Developer
虽然不同应用的页面千变万化，但对其进行拆分和分析，页面中的很多布局场景是相似的。本小节将介绍如何借助自适应布局、响应式布局以及常见的容器类组件，实现应用中的典型布局场景。
| 布局场景 | 实现方案 |
| --- | --- |
| 页签栏 | Tab组件 + 响应式布局 |
| 运营横幅（Banner） | Swiper组件 + 响应式布局 |
| 网格 | Grid组件 / List组件 + 响应式布局 |
| 侧边栏 | SideBar组件 + 响应式布局 |
| 单/双栏 | Navigation组件 + 响应式布局 |
| 三分栏 | SideBar组件 + Navigation组件 + 响应式布局 |
| 自定义弹窗 | CustomDialogController组件 + 响应式布局 |
| 大图浏览 | Image组件 |
| 操作入口 | Scroll组件+Row组件横向均分 |
| 顶部 | 栅格组件 |
| 缩进布局 | 栅格组件 |
| 挪移布局 | 栅格组件 |
| 重复布局 | 栅格组件 |
在本文媒体查询小节中已经介绍了如何通过媒体查询监听断点变化，后续的示例中不再重复介绍此部分代码。
页签栏
布局效果
| sm | md | lg |
| --- | --- | --- |
| 页签在底部 页签的图标和文字垂直布局 页签宽度均分 页签高度固定72vp | 页签在底部 页签的图标和文字水平布局 页签宽度均分 页签高度固定56vp | 页签在左边 页签的图标和文字垂直布局 页签宽度固定96vp 页签高度总占比‘60%’后均分 |
|  |  |  |
页签在底部
页签的图标和文字垂直布局
页签宽度均分
页签高度固定72vp
页签在底部
页签的图标和文字水平布局
页签宽度均分
页签高度固定56vp
页签在左边
页签的图标和文字垂直布局
页签宽度固定96vp
页签高度总占比‘60%’后均分
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.63999133546796415969129994381292:50001231000000:2800:A093BE5D50513624DFDB80C38E265D088C7ADFF78A50F2420216D50CAA18B9A9.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.34100153709218580754048665293397:50001231000000:2800:12784DB5A8371017C2F9FB22BFA615A24E5ECA37A7C9D0E103F3A13725D16C26.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.50217324930962684738165473963931:50001231000000:2800:F051DAAC79585CA6D89C97B3CB69C5A4A66AC37999D42E71376085EC6314A802.png)
实现方案
不同断点下，页签在页面中的位置及尺寸都有差异，可以结合响应式布局能力，设置不同断点下Tab组件的barPosition、vertical、barWidth和barHeight属性实现目标效果。
另外，页签栏中的文字和图片的相对位置不同，同样可以通过设置不同断点下tabBar对应的CustomBuilder中的布局方向，实现目标效果。
参考代码
```typescript
import { BreakpointSystem, BreakpointState } from '../common/breakpointsystem'
interface TabBar  {
name: string
icon: Resource
selectIcon: Resource
}
interface marginGenerate {
top: number,
left?:number
}
@Entry
@Component
struct Home {
@State currentIndex: number = 0
@State tabs: Array<TabBar> = [{
name: '首页',
icon: $r('app.media.ic_music_home'),
selectIcon: $r('app.media.ic_music_home_selected')
}, {
name: '排行榜',
icon: $r('app.media.ic_music_ranking'),
selectIcon: $r('app.media.ic_music_ranking_selected')
}, {
name: '我的',
icon: $r('app.media.ic_music_me_nor'),
selectIcon: $r('app.media.ic_music_me_selected')
}]
@State compStr: BreakpointState<string> = BreakpointState.of({ sm: "sm", md: "md", lg: "lg" })
@State compDirection: BreakpointState<FlexDirection> = BreakpointState.of({
sm: FlexDirection.Column,
md: FlexDirection.Row,
lg: FlexDirection.Column
});
@State compBarPose: BreakpointState<BarPosition> = BreakpointState.of({
sm: BarPosition.End,
md: BarPosition.End,
lg: BarPosition.Start
});
@State compVertical: BreakpointState<boolean> = BreakpointState.of({
sm: false,
md: false,
lg: true
});
@State compBarWidth: BreakpointState<string> = BreakpointState.of({
sm: '100%', md: '100%', lg: '96vp'
});
@State compBarHeight: BreakpointState<string> = BreakpointState.of({
sm: '72vp', md: '56vp', lg: '60%'
});
@State compMargin: BreakpointState<marginGenerate> = BreakpointState.of({
sm: ({ top: 4 } as marginGenerate),
md: ({ left: 8 } as marginGenerate),
lg: ({ top: 4 } as marginGenerate)
});
@Builder TabBarBuilder(index: number, tabBar: TabBar) {
Flex({
direction: this.compDirection.value,
justifyContent: FlexAlign.Center,
alignItems: ItemAlign.Center
}) {
Image(this.currentIndex === index ? tabBar.selectIcon : tabBar.icon)
.size({ width: 36, height: 36 })
Text(tabBar.name)
.fontColor(this.currentIndex === index ? '#FF1948' : '#999')
.margin(this.compMargin.value)
.fontSize(16)
}
.width('100%')
.height('100%')
}
aboutToAppear() {
BreakpointSystem.getInstance().attach(this.compStr)
BreakpointSystem.getInstance().attach(this.compDirection)
BreakpointSystem.getInstance().attach(this.compBarPose)
BreakpointSystem.getInstance().attach(this.compVertical)
BreakpointSystem.getInstance().attach(this.compBarWidth)
BreakpointSystem.getInstance().attach(this.compBarHeight)
BreakpointSystem.getInstance().attach(this.compMargin)
BreakpointSystem.getInstance().start()
}
aboutToDisappear() {
BreakpointSystem.getInstance().detach(this.compStr)
BreakpointSystem.getInstance().detach(this.compDirection)
BreakpointSystem.getInstance().detach(this.compBarPose)
BreakpointSystem.getInstance().detach(this.compVertical)
BreakpointSystem.getInstance().detach(this.compBarWidth)
BreakpointSystem.getInstance().detach(this.compBarHeight)
BreakpointSystem.getInstance().detach(this.compMargin)
BreakpointSystem.getInstance().stop()
}
build() {
Tabs({
barPosition:this.compBarPose.value
}) {
ForEach(this.tabs, (item:TabBar, index) => {
TabContent() {
Stack() {
Text(item.name).fontSize(30)
}.width('100%').height('100%')
}.tabBar(this.TabBarBuilder(index!, item))
})
}
.vertical(this.compVertical.value)
.barWidth(this.compBarWidth.value)
.barHeight(this.compBarHeight.value)
.animationDuration(0)
.onChange((index: number) => {
this.currentIndex = index
})
}
}
```
运营横幅（Banner）
布局效果
| sm | md | lg |
| --- | --- | --- |
| 展示一个内容项 | 展示两个内容项 | 展示三个内容项 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.82688915050979555335283196983457:50001231000000:2800:0422EB9F898043F1B50E898F0780D0CC8FACC146FDC5A588ECFA4D871A7467CC.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.98083185306339769961221104207600:50001231000000:2800:CDE8EC040DD7BCC818D7A6198DB2A0D2168CA45A3258DEF9AD4BC8AE986F65AF.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.02042517769426012957161738008979:50001231000000:2800:81E8244C1BDFF6B1FAF33144CC391CCF61983B0904E197FF8F144565CB4D2CCB.png)
实现方案
运营横幅通常使用Swiper组件实现。不同断点下，运营横幅中展示的图片数量不同。只需要结合响应式布局，配置不同断点下Swiper组件的displayCount属性，即可实现目标效果。
参考代码
```typescript
import { BreakpointSystem, BreakPointType } from '../common/breakpointsystem'
@Entry
@Component
export default struct Banner {
private data: Array<Resource> = [
$r('app.media.banner1'),
$r('app.media.banner2'),
$r('app.media.banner3'),
$r('app.media.banner4'),
$r('app.media.banner5'),
$r('app.media.banner6'),
]
private breakpointSystem: BreakpointSystem = new BreakpointSystem()
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'md'
aboutToAppear() {
this.breakpointSystem.register()
}
aboutToDisappear() {
this.breakpointSystem.unregister()
}
build() {
Swiper() {
ForEach(this.data, (item:Resource) => {
Image(item)
.size({ width: '100%', height: 200 })
.borderRadius(12)
.padding(8)
})
}
.indicator(new BreakPointType({ sm: true, md: false, lg: false }).getValue(this.currentBreakpoint)!)
.displayCount(new BreakPointType({ sm: 1, md: 2, lg: 3 }).getValue(this.currentBreakpoint)!)
}
}
```
网格
布局效果
| sm | md | lg |
| --- | --- | --- |
| 展示两列 | 展示四列 | 展示六列 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.01642574294854795976415279049849:50001231000000:2800:5209599DA9DA6A5D3CEE63EA483BFA5B71C30D0587147BDA0D34A7DBA1E67A0D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.62635693038369717433870264181480:50001231000000:2800:3F318471D17C03AD50C411FA9B243356A509545AE24CC93F1C1777E6D4138DF0.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.87846976271190898203222400815966:50001231000000:2800:71494B5AAFEB8B7CD1DA437C12B5275A2FA449BC8216E57656B5B39FE9E811DD.png)
实现方案
不同断点下，页面中图片的排布不同，此场景可以通过响应式布局能力结合Grid组件实现，通过调整不同断点下的Grid组件的columnsTemplate属性即可实现目标效果。
另外，由于本例中各列的宽度相同，也可以通过响应式布局能力结合List组件实现，通过调整不同断点下的List组件的lanes属性也可实现目标效果。
参考代码
通过Grid组件实现
```typescript
import { BreakpointSystem, BreakPointType } from '../common/breakpointsystem'
interface GridItemInfo {
name: string
image: Resource
}
@Entry
@Component
struct MultiLaneList {
private data: GridItemInfo[] = [
{ name: '歌单集合1', image: $r('app.media.1') },
{ name: '歌单集合2', image: $r('app.media.2') },
{ name: '歌单集合3', image: $r('app.media.3') },
{ name: '歌单集合4', image: $r('app.media.4') },
{ name: '歌单集合5', image: $r('app.media.5') },
{ name: '歌单集合6', image: $r('app.media.6') },
{ name: '歌单集合7', image: $r('app.media.7') },
{ name: '歌单集合8', image: $r('app.media.8') },
{ name: '歌单集合9', image: $r('app.media.9') },
{ name: '歌单集合10', image: $r('app.media.10') },
{ name: '歌单集合11', image: $r('app.media.11') },
{ name: '歌单集合12', image: $r('app.media.12') }
]
private breakpointSystem: BreakpointSystem = new BreakpointSystem()
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'md'
aboutToAppear() {
this.breakpointSystem.register()
}
aboutToDisappear() {
this.breakpointSystem.unregister()
}
build() {
Grid() {
ForEach(this.data, (item: GridItemInfo) => {
GridItem() {
Column() {
Image(item.image)
.aspectRatio(1.8)
Text(item.name)
.margin({ top: 8 })
.fontSize(20)
}.padding(4)
}
})
}
.columnsTemplate(new BreakPointType({
sm: '1fr 1fr',
md: '1fr 1fr 1fr 1fr',
lg: '1fr 1fr 1fr 1fr 1fr 1fr'
}).getValue(this.currentBreakpoint)!)
}
}
```
通过List组件实现
```typescript
import { BreakpointSystem, BreakPointType } from '../common/breakpointsystem'
interface ListItemInfo {
name: string
image: Resource
}
@Entry
@Component
struct MultiLaneList {
private data: ListItemInfo[] = [
{ name: '歌单集合1', image: $r('app.media.1') },
{ name: '歌单集合2', image: $r('app.media.2') },
{ name: '歌单集合3', image: $r('app.media.3') },
{ name: '歌单集合4', image: $r('app.media.4') },
{ name: '歌单集合5', image: $r('app.media.5') },
{ name: '歌单集合6', image: $r('app.media.6') },
{ name: '歌单集合7', image: $r('app.media.7') },
{ name: '歌单集合8', image: $r('app.media.8') },
{ name: '歌单集合9', image: $r('app.media.9') },
{ name: '歌单集合10', image: $r('app.media.10') },
{ name: '歌单集合11', image: $r('app.media.11') },
{ name: '歌单集合12', image: $r('app.media.12') }
]
private breakpointSystem: BreakpointSystem = new BreakpointSystem()
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'md'
aboutToAppear() {
this.breakpointSystem.register()
}
aboutToDisappear() {
this.breakpointSystem.unregister()
}
build() {
List() {
ForEach(this.data, (item: ListItemInfo) => {
ListItem() {
Column() {
Image(item.image)
Text(item.name)
.margin({ top: 8 })
.fontSize(20)
}.padding(4)
}
})
}
.lanes(new BreakPointType({ sm: 2, md: 4, lg: 6 }).getValue(this.currentBreakpoint)!)
.width('100%')
}
}
```
侧边栏
布局效果
| sm | md | lg |
| --- | --- | --- |
| 默认隐藏侧边栏，同时提供侧边栏控制按钮，用户可以通过按钮控制侧边栏显示或隐藏。 | 始终显示侧边栏，不提供控制按钮，用户无法隐藏侧边栏。 | 始终显示侧边栏，不提供控制按钮，用户无法隐藏侧边栏。 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.88558368434199510803938555343229:50001231000000:2800:77BC87DFE53570CDAC9F5270E09D7E8DB8817BC2E805BE12AA7F991FDFD3CD2B.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.04726941817374935678610059350338:50001231000000:2800:2F40639BB91262DE4B7D494C3B278E60BF2921DC170D4810FFB14622DB053561.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.23760688318427823443253969611739:50001231000000:2800:155501F419D0F088282EF8A150C8C74FF9E34B3762669499C2CFC17BEC87DEBA.png)
实现方案
侧边栏通常通过SideBarContainer组件实现，结合响应式布局能力，在不同断点下为SideBarConContainer组件的sideBarWidth、showControlButton等属性配置不同的值，即可实现目标效果。
参考代码
```typescript
import { BreakpointSystem, BreakPointType } from '../common/breakpointsystem'
interface imagesInfo{
label:string,
imageSrc:Resource
}
const images:imagesInfo[]=[
{
label:'moon',
imageSrc:$r('app.media.my_image_moon')
},
{
label:'sun',
imageSrc:$r('app.media.my_image')
}
]
@Entry
@Component
struct SideBarSample {
@StorageLink('currentBreakpoint') private currentBreakpoint: string = "md";
private breakpointSystem: BreakpointSystem = new BreakpointSystem()
@State selectIndex: number = 0;
@State showSideBar:boolean=false;
aboutToAppear() {
this.breakpointSystem.register()
}
aboutToDisappear() {
this.breakpointSystem.unregister()
}
@Builder itemBuilder(index: number) {
Text(images[index].label)
.fontSize(24)
.fontWeight(FontWeight.Bold)
.borderRadius(5)
.margin(20)
.backgroundColor('#ffffff')
.textAlign(TextAlign.Center)
.width(180)
.height(36)
.onClick(() => {
this.selectIndex = index;
if(this.currentBreakpoint === 'sm'){
this.showSideBar=false
}
})
}
build() {
SideBarContainer(this.currentBreakpoint === 'sm' ? SideBarContainerType.Overlay : SideBarContainerType.Embed) {
Column() {
this.itemBuilder(0)
this.itemBuilder(1)
}.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
Column() {
Image(images[this.selectIndex].imageSrc)
.objectFit(ImageFit.Contain)
.height(300)
.width(300)
}
.justifyContent(FlexAlign.Center)
.width('100%')
.height('100%')
}
.height('100%')
.sideBarWidth(this.currentBreakpoint === 'sm' ? '100%' : '33.33%')
.minSideBarWidth(this.currentBreakpoint === 'sm' ? '100%' : '33.33%')
.maxSideBarWidth(this.currentBreakpoint === 'sm' ? '100%' : '33.33%')
.showControlButton(this.currentBreakpoint === 'sm')
.autoHide(false)
.showSideBar(this.currentBreakpoint !== 'sm'||this.showSideBar)
.onChange((isBarShow: boolean) => {
if(this.currentBreakpoint === 'sm'){
this.showSideBar=isBarShow
}
})
}
}
```
单/双栏
布局效果
| sm | md | lg |
| --- | --- | --- |
| 单栏显示，在首页中点击选项可以显示详情。 点击详情上方的返回键图标或使用系统返回键可以返回到主页。 | 双栏显示，点击左侧不同的选项可以刷新右侧的显示。 | 双栏显示，点击左侧不同的选项可以刷新右侧的显示。 |
|  |  |  |
单栏显示，在首页中点击选项可以显示详情。
点击详情上方的返回键图标或使用系统返回键可以返回到主页。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165828.98333068355007877481416422489296:50001231000000:2800:15C6920C4A059CAAE8C7B2E832B4C8B5D1655ACFD70DE4738FCEC5DB7AE826D9.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.80483535406444903675800487429834:50001231000000:2800:A91606B5D18DD401E361A43D51090AD47DF65BDECABC90074DB740FB641F1A69.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.19239572113679540187417333567444:50001231000000:2800:6FA947061A7A1D3128A9545DD5214E448FF75EA1E5DF527D3667C4428C65DE33.png)
实现方案
单/双栏场景可以使用Navigation组件实现，Navigation组件可以根据窗口宽度自动切换单/双栏显示，减少开发工作量。
参考代码
```typescript
// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}
// route_map.json
{
"routerMap": [
{
"name": "Moon",
"pageSourceFile": "src/main/ets/pages/Moon.ets",
"buildFunction": "MoonBuilder",
"data": {
"description": "this is Moon"
}
},
{
"name": "Sun",
"pageSourceFile": "src/main/ets/pages/Sun.ets",
"buildFunction": "SunBuilder"
}
]
}
// Moon.ets
@Builder
export function MoonBuilder(name: string, param: Object) {
Moon()
}
@Component
export struct Moon {
private imageSrc: Resource=$r('app.media.my_image_moon')
private label: string='moon'
build() {
Column(){
NavDestination(){
Column() {
Image(this.imageSrc)
.objectFit(ImageFit.Contain)
.height(300)
.width(300)
}
.justifyContent(FlexAlign.Center)
.width('100%')
.height('100%')
}.title(this.label)
}
}
}
// Sun.ets
@Builder
export function SunBuilder(name: string, param: Object) {
Sun()
}
@Component
export struct Sun {
private imageSrc: Resource=$r('app.media.my_image')
private label: string='Sun'
build() {
Column(){
NavDestination(){
Column() {
Image(this.imageSrc)
.objectFit(ImageFit.Contain)
.height(300)
.width(300)
}
.justifyContent(FlexAlign.Center)
.width('100%')
.height('100%')
}.title(this.label)
}
}
}
//NavigationSample.ets
interface arrSample{
label:string,
pagePath:string
}
@Entry
@Component
struct NavigationSample {
pageInfos: NavPathStack = new NavPathStack();
private arr:arrSample[]=[
{
label:'moon',
pagePath:'Moon'
},
{
label:'sun',
pagePath:'Sun'
}
]
build() {
Navigation(this.pageInfos) {
Column({space: 30}) {
ForEach(this.arr, (item: arrSample) => {
Text(item.label)
.fontSize(24)
.fontWeight(FontWeight.Bold)
.borderRadius(5)
.backgroundColor('#FFFFFF')
.textAlign(TextAlign.Center)
.width(180)
.height(36)
.onClick(()=>{
this.pageInfos.clear();
this.pageInfos.pushPath({name:item.pagePath})
})
})
}
.justifyContent(FlexAlign.Center)
.height('100%')
.width('100%')
}
.mode(NavigationMode.Auto)
.backgroundColor('#F1F3F5')
.height('100%')
.width('100%')
.navBarWidth(360)
.hideToolBar(true)
.title('Sample')
}
}
```
三分栏
布局效果
| sm | md | lg |
| --- | --- | --- |
| 单栏显示。 点击侧边栏控制按钮控制侧边栏的显示/隐藏。 点击首页的选项可以进入到内容区，内容区点击返回按钮可返回首页。 | 双栏显示。 点击侧边栏控制按钮控制侧边栏的显示/隐藏。 点击左侧导航区不同的选项可以刷新右侧内容区的显示。 | 三分栏显示。 点击侧边栏控制按钮控制侧边栏的显示/隐藏，来回切换二分/三分栏显示。 点击左侧导航区不同的选项可以刷新右侧内容区的显示。 窗口宽度变化时，优先变化右侧内容区的宽度大小。 |
|  |  |  |
|  |  |  |
单栏显示。
点击侧边栏控制按钮控制侧边栏的显示/隐藏。
点击首页的选项可以进入到内容区，内容区点击返回按钮可返回首页。
双栏显示。
点击侧边栏控制按钮控制侧边栏的显示/隐藏。
点击左侧导航区不同的选项可以刷新右侧内容区的显示。
三分栏显示。
点击侧边栏控制按钮控制侧边栏的显示/隐藏，来回切换二分/三分栏显示。
点击左侧导航区不同的选项可以刷新右侧内容区的显示。
窗口宽度变化时，优先变化右侧内容区的宽度大小。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.75550557348435779307016256355166:50001231000000:2800:D00F8E972381C3E0A3666ADFE2132095F59D1488A7C5049905DB1D544713E129.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.69126393307030448414709038175042:50001231000000:2800:240BF53B3ACF7E1D9349396D6C6EE3DB1990ABB640E7C17898A567E837AEE1B1.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.19033765159803414116749723323699:50001231000000:2800:30E7DE56F8489B49DC19A7EEE3BAED3B799205828E00DDB30025E95E259C62D4.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.33575252723447456261567917978245:50001231000000:2800:E0CFA8310B9D20B7BC6708986AE8DF919777668B2D5CCD29A3664F340E9BFF94.gif)
场景说明
为充分利用设备的屏幕尺寸优势，应用在大屏设备上常常有二分栏或三分栏的设计，即“A+C”，“B+C”或“A+B+C”的组合，其中A是侧边导航区，B是列表导航区，C是内容区。在用户动态改变窗口宽度时，当窗口宽度大于或等于840vp时页面呈现A+B+C三列，放大缩小优先变化C列；当窗口宽度小于840vp大于等于600vp时呈现B+C列，放大缩小时优先变化C列；当窗口宽度小于600vp大于等于360vp时，仅呈现C列。
实现方案
三分栏场景可以组合使用SideBarContainer组件与Navigation组件实现，SideBarContainer组件可以通过侧边栏控制按钮控制显示/隐藏，Navigation组件可以根据窗口宽度自动切换该组件内单/双栏显示，结合响应式布局能力，在不同断点下为SideBarConContainer组件的minContentWidth属性配置不同的值，即可实现目标效果。设置minContentWidth属性的值可以通过断点监听窗口尺寸变化的同时设置不同的值并储存成一个全局对象。
参考代码
```typescript
// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}
// route_map.json
{
"routerMap": [
{
"name": "B1Page",
"pageSourceFile": "src/main/ets/pages/B1Page.ets",
"buildFunction": "B1PageBuilder",
"data": {
"description": "this is B1Page"
}
},
{
"name": "B2Page",
"pageSourceFile": "src/main/ets/pages/B2Page.ets",
"buildFunction": "B2PageBuilder"
}
]
}
// EntryAbility.ts
import { window, display } from '@kit.ArkUI'
import { Ability,UIAbility } from '@kit.AbilityKit'
export default class EntryAbility extends UIAbility {
private windowObj?: window.Window
private curBp?: string
private myWidth?: number
// ...
// 根据当前窗口尺寸更新断点
private updateBreakpoint(windowWidth:number) :void{
// 将长度的单位由px换算为vp
let windowWidthVp = windowWidth / (display.getDefaultDisplaySync().densityDPI / 160)
let newBp: string = ''
let newWd: number
if (windowWidthVp < 320) {
newBp = 'xs'
newWd = 360
} else if (windowWidthVp < 600) {
newBp = 'sm'
newWd = 360
} else if (windowWidthVp < 840) {
newBp = 'md'
newWd = 600
} else {
newBp = 'lg'
newWd = 600
}
if (this.curBp !== newBp) {
this.curBp = newBp
this.myWidth = newWd
// 使用状态变量记录当前断点值
AppStorage.setOrCreate('currentBreakpoint', this.curBp)
// 使用状态变量记录当前minContentWidth值
AppStorage.setOrCreate('myWidth', this.myWidth)
}
}
onWindowStageCreate(windowStage: window.WindowStage) :void{
windowStage.getMainWindow().then((windowObj) => {
this.windowObj = windowObj
// 获取应用启动时的窗口尺寸
this.updateBreakpoint(windowObj.getWindowProperties().windowRect.width)
// 注册回调函数，监听窗口尺寸变化
windowObj.on('windowSizeChange', (windowSize)=>{
this.updateBreakpoint(windowSize.width)
})
});
// ...应用启动页面
windowStage.loadContent('pages/Index', (err) => {
if (err.code) {
return;
}
});
}
// 窗口销毁时，取消窗口尺寸变化监听
onWindowStageDestroy() :void {
if (this.windowObj) {
this.windowObj.off('windowSizeChange')
}
}
//...
}
// B1Page.ets
@Builder
export function B1PageBuilder() {
B1Page()
}
@Component
export struct B1Page {
private imageSrc: Resource = $r('app.media.startIcon');
private label: string = "B1"
build() {
Column() {
NavDestination() {
Column() {
Image(this.imageSrc)
.objectFit(ImageFit.Contain)
.height(300)
.width(300)
}
.justifyContent(FlexAlign.Center)
.width('100%')
.height('100%')
}.title(this.label)
}
}
}
// B2Page.ets
@Builder
export function B2PageBuilder() {
B2Page()
}
@Component
export struct B2Page {
private imageSrc: Resource = $r('app.media.startIcon');
private label: string = "B2"
build() {
Column() {
NavDestination() {
Column() {
Image(this.imageSrc)
.objectFit(ImageFit.Contain)
.height(300)
.width(300)
}
.justifyContent(FlexAlign.Center)
.width('100%')
.height('100%')
}.title(this.label)
}
}
}
//TripleColumnSample.ets
interface arrSampleObj{
label:string,
pagePath:string
}
@Entry
@Component
struct TripleColumnSample {
@State arr: number[] = [1, 2, 3];
@StorageProp('myWidth') myWidth: number = 360;
pageInfos:NavPathStack = new NavPathStack();
@State arrSample: arrSampleObj[] = [
{
label:'B1',
pagePath:'B1Page'
},
{
label:'B2',
pagePath:'B2Page'
}
];
@Builder NavigationTitle() {
Column() {
Text('Sample')
.fontColor('#000000')
.fontSize(24)
.width('100%')
.height('100%')
.align(Alignment.BottomStart)
.margin({left:'5%'})
}.alignItems(HorizontalAlign.Start)
}
build() {
SideBarContainer() {
Column() {
List() {
ForEach(this.arr, (item: number, index) => {
ListItem() {
Text('A' + item)
.width('100%')
.height("20%")
.fontSize(24)
.fontWeight(FontWeight.Bold)
.textAlign(TextAlign.Center)
.backgroundColor('#66000000')
}
})
}.divider({ strokeWidth: 5, color: '#F1F3F5' })
}.width('100%')
.height('100%')
.justifyContent(FlexAlign.SpaceEvenly)
.backgroundColor('#F1F3F5')
Column() {
Navigation(this.pageInfos) {
List() {
ListItem() {
Column() {
ForEach(this.arrSample, (item: arrSampleObj, index) => {
ListItem() {
Text(item.label)
.fontSize(24)
.fontWeight(FontWeight.Bold)
.backgroundColor('#66000000')
.textAlign(TextAlign.Center)
.width('100%')
.height('30%')
.margin({
bottom:10
})
}.onClick(() => {
this.pageInfos.clear();
this.pageInfos.pushPath({ name: item.pagePath })
})
})
}
}.width('100%')
}
}
.mode(NavigationMode.Auto)
.minContentWidth(360)
.navBarWidth(240)
.backgroundColor('#FFFFFF')
.height('100%')
.width('100%')
.hideToolBar(true)
.title(this.NavigationTitle)
}.width('100%').height('100%')
}.sideBarWidth(240)
.minContentWidth(this.myWidth)
}
}
```
自定义弹窗
布局效果
| sm | md | lg |
| --- | --- | --- |
| 弹窗横向居中，纵向位于底部显示，与窗口左右两侧各间距24vp。 | 弹窗横向居中，纵向位于底部显示。 | 弹窗居中显示，其宽度约为窗口宽度的1/3。 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.69849900684722397278848232642438:50001231000000:2800:1D959CFA85557E9C75F52BF6F9DFF2CBEDFC7B31CB3675244CEB80A5F3E6F3EF.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.89335409447957994693740151108333:50001231000000:2800:FDC5E73452E79405F26395ED1C9F8EBD615CB7B8EC4B00D815968C1227408743.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.21590219930710773311616547954220:50001231000000:2800:294BAAA5E81872120CCA922AA25436BA756DC93DCEF048C916D9BD766F9B915E.png)
实现方案
自定义弹窗通常通过CustomDialogController实现，有两种方式实现本场景的目标效果：
-  通过gridCount属性配置自定义弹窗的宽度。 系统默认对不同断点下的窗口进行了栅格化：sm断点下为4栅格，md断点下为8栅格，lg断点下为12栅格。通过gridCount属性可以配置弹窗占据栅格中的多少列，将该值配置为4即可实现目标效果。
-  将customStyle设置为true，即弹窗的样式完全由开发者自定义。 开发者自定义弹窗样式时，开发者可以根据需要配置弹窗的宽高和背景色（非弹窗区域保持默认的半透明色）。自定义弹窗样式配合栅格组件同样可以实现目标效果。
参考代码
```typescript
@Entry
@Component
struct CustomDialogSample {
// 通过gridCount配置弹窗的宽度
dialogControllerA: CustomDialogController = new CustomDialogController({
builder: CustomDialogA ({
cancel: this.onCancel,
confirm: this.onConfirm
}),
cancel: this.onCancel,
autoCancel: true,
gridCount: 4,
customStyle: false
})
// 自定义弹窗样式
dialogControllerB: CustomDialogController = new CustomDialogController({
builder: CustomDialogB ({
cancel: this.onCancel,
confirm: this.onConfirm
}),
cancel: this.onCancel,
autoCancel: true,
customStyle: true
})
onCancel() {
console.info('callback when dialog is canceled')
}
onConfirm() {
console.info('callback when dialog is confirmed')
}
build() {
Column() {
Button('CustomDialogA').margin(12)
.onClick(() => {
this.dialogControllerA.open()
})
Button('CustomDialogB').margin(12)
.onClick(() => {
this.dialogControllerB.open()
})
}.width('100%').height('100%').justifyContent(FlexAlign.Center)
}
}
@CustomDialog
struct CustomDialogA {
controller?: CustomDialogController
cancel?: () => void
confirm?: () => void
build() {
Column() {
Text('是否删除此联系人?')
.fontSize(16)
.fontColor('#E6000000')
.margin({bottom: 8, top: 24, left: 24, right: 24})
Row() {
Text('取消')
.fontColor('#007DFF')
.fontSize(16)
.layoutWeight(1)
.textAlign(TextAlign.Center)
.onClick(()=>{
if(this.controller){
this.controller.close()
}
this.cancel!()
})
Line().width(1).height(24).backgroundColor('#33000000').margin({left: 4, right: 4})
Text('删除')
.fontColor('#FA2A2D')
.fontSize(16)
.layoutWeight(1)
.textAlign(TextAlign.Center)
.onClick(()=>{
if(this.controller){
this.controller.close()
}
this.confirm!()
})
}.height(40)
.margin({left: 24, right: 24, bottom: 16})
}.borderRadius(24)
}
}
@CustomDialog
struct CustomDialogB {
controller?: CustomDialogController
cancel?: () => void
confirm?: () => void
build() {
GridRow({columns: {sm: 4, md: 8, lg: 12}}) {
GridCol({span: 4, offset: {sm: 0, md: 2, lg: 4}}) {
Column() {
Text('是否删除此联系人?')
.fontSize(16)
.fontColor('#E6000000')
.margin({bottom: 8, top: 24, left: 24, right: 24})
Row() {
Text('取消')
.fontColor('#007DFF')
.fontSize(16)
.layoutWeight(1)
.textAlign(TextAlign.Center)
.onClick(()=>{
if(this.controller){
this.controller.close()
}
this.cancel!()
})
Line().width(1).height(24).backgroundColor('#33000000').margin({left: 4, right: 4})
Text('删除')
.fontColor('#FA2A2D')
.fontSize(16)
.layoutWeight(1)
.textAlign(TextAlign.Center)
.onClick(()=>{
if(this.controller){
this.controller.close()
}
this.confirm!()
})
}.height(40)
.margin({left: 24, right: 24, bottom: 16})
}.borderRadius(24).backgroundColor('#FFFFFF')
}
}.margin({left: 24, right: 24})
}
}
```
大图浏览
布局效果
| sm | md | lg |
| --- | --- | --- |
| 图片长宽比不变，最长边充满全屏。 | 图片长宽比不变，最长边充满全屏。 | 图片长宽比不变，最长边充满全屏。 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.02778741167116505370290712165890:50001231000000:2800:FF749FE136545BD4E1D0061DC3A857CF499CE36CB844E5DB46CF6CFEC4E3E34E.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.75209691992851194533963703714131:50001231000000:2800:F460733D22DB46873C74E2F7890CEC42D333DD9F24544CEAE44612671B4608DD.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.56314982785847669040618265766620:50001231000000:2800:00C0C1B710BB64043DE0F5EA29589AC7A97A8D76A5088CF55ED156B28CCC4F48.png)
实现方案
图片通常使用Image组件展示，Image组件的objectFit属性默认为ImageFit.Cover，即保持宽高比进行缩小或者放大以使得图片两边都大于或等于显示边界。在大图浏览场景下，因屏幕与图片的宽高比可能有差异，常常会发生图片被截断的问题。此时只需将Image组件的objectFit属性设置为ImageFit.Contain，即保持宽高比进行缩小或者放大并使得图片完全显示在显示边界内，即可解决该问题。
参考代码
```typescript
@Entry
@Component
struct BigImage {
build() {
Row() {
Image($r("app.media.image"))
.objectFit(ImageFit.Contain)
}
}
}
```
操作入口
布局效果
| sm | md | lg |
| --- | --- | --- |
| 列表项尺寸固定，超出内容可滚动查看。 | 列表项尺寸固定，剩余空间均分。 | 列表项尺寸固定，剩余空间均分。 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.46121450007601589521967161458181:50001231000000:2800:38C81F03F2BB90C057CB1C4AC8ED3D76C845DE7116FB63039709EC83AD584C2F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165829.60385062625217039737398386808597:50001231000000:2800:8714ACBA533F96E575B769AA4DA8FAF75292CDA51A521474C49BE7A4A3E51F79.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.67475862853159809143800067368621:50001231000000:2800:E129DCE19E580EEA0B87F229088E603A8662EB5C5038CC67DA0A96B334CE39DF.png)
实现方案
Scroll（内容超出宽度时可滚动） + Row（横向均分：justifyContent（FlexAlign.SpaceAround）、 最小宽度约束：constraintSize({ minWidth: '100%' }）
参考代码
```typescript
interface OperationItem {
name: string
icon: Resource
}
@Entry
@Component
export default struct OperationEntries {
@State listData: Array<OperationItem> = [
{ name: '私人FM', icon: $r('app.media.self_fm') },
{ name: '歌手', icon: $r('app.media.singer') },
{ name: '歌单', icon: $r('app.media.song_list') },
{ name: '排行榜', icon: $r('app.media.rank') },
{ name: '热门', icon: $r('app.media.hot') },
{ name: '运动音乐', icon: $r('app.media.sport') },
{ name: '音乐FM', icon: $r('app.media.audio_fm') },
{ name: '福利', icon: $r('app.media.bonus') }]
build() {
Scroll() {
Row() {
ForEach(this.listData, (item:OperationItem) => {
Column() {
Image(item.icon)
.width(48)
.aspectRatio(1)
Text(item.name)
.margin({ top: 8 })
.fontSize(16)
}
.justifyContent(FlexAlign.Center)
.height(104)
.padding({ left: 12, right: 12 })
})
}
.constraintSize({ minWidth: '100%' }).justifyContent(FlexAlign.SpaceAround)
}
.width('100%')
.scrollable(ScrollDirection.Horizontal)
}
}
```
顶部
布局效果
| sm | md | lg |
| --- | --- | --- |
| 标题和搜索框两行显示。 | 标题和搜索框一行显示。 | 标题和搜索框一行显示。 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.63814003985355099231385974995858:50001231000000:2800:F4033194E7B08D769E8F215BE1A7F1E046E7E43C408F78DB0D77840CC046832D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.96048304618439876470067797477905:50001231000000:2800:91E5933B5DCB8F8E1F508E16D23B022C0807A0AD9CDA76018CE348AE52076DB5.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.21381173790286619977209277552320:50001231000000:2800:DE5FB690772D45FA54F9EB2247DE956278907D33893C88C66AD9701E66E93AAF.png)
实现方案
最外层使用栅格行组件GridRow布局
文本标题使用栅格列组件GridCol
搜索框使用栅格列组件GridCol
参考代码
```typescript
@Entry
@Component
export default struct Header {
@State needWrap: boolean = true
build() {
GridRow() {
GridCol({ span: { sm: 12, md: 6, lg: 7 } }) {
Row() {
Text('推荐').fontSize(24)
Blank()
Image($r('app.media.ic_public_more'))
.width(32)
.height(32)
.objectFit(ImageFit.Contain)
.visibility(this.needWrap ? Visibility.Visible : Visibility.None)
}
.width('100%').height(40)
.alignItems(VerticalAlign.Center)
}
GridCol({ span: { sm: 12, md: 6, lg: 5 } }) {
Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
Search({ placeholder: '猜您喜欢: 万水千山' })
.placeholderFont({ size: 16 })
.margin({ top: 4, bottom: 4 })
Image($r('app.media.audio_fm'))
.width(32)
.height(32)
.objectFit(ImageFit.Contain)
.flexShrink(0)
.margin({ left: 12 })
Image($r('app.media.ic_public_more'))
.width(32)
.height(32)
.objectFit(ImageFit.Contain)
.flexShrink(0)
.margin({ left: 12 })
.visibility(this.needWrap ? Visibility.None : Visibility.Visible)
}
}
}.onBreakpointChange((breakpoint: string) => {
if (breakpoint === 'sm') {
this.needWrap = true
} else {
this.needWrap = false
}
})
.padding({ left: 12, right: 12 })
}
}
```
缩进布局
布局效果
| sm | md | lg |
| --- | --- | --- |
| 栅格总列数为4，内容占满所有列。 | 栅格总列数为8，内容占中间6列。 | 栅格总列数为12，内容占中间8列。 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.33068049156788314501385891465696:50001231000000:2800:18FC31FE39E686DAE71FEC2ADD1E575F290FBFFDF51E7706D65C1679CDFDB59D.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.23814157156704782970946121309814:50001231000000:2800:333FA23FDCFD6F5FA9AF68A3D429880A2BB475299F87818B2B0F855308E4535B.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.62589106472273900108602734490954:50001231000000:2800:0482CCD2FD2D1A9C84C80D853166B92E7D48E9F686C3554B87D4CAF08EE00AAD.jpg)
实现方案
借助栅格组件，控制待显示内容在不同的断点下占据不同的列数，即可实现不同设备上的缩进效果。另外还可以调整不同断点下栅格组件与两侧的间距，获得更好的显示效果。
参考代码
```typescript
@Entry
@Component
struct IndentationSample {
@State private gridMargin: number = 24
build() {
Row() {
GridRow({columns: {sm: 4, md: 8, lg: 12}, gutter: 24}) {
GridCol({span: {sm: 4, md: 6, lg: 8}, offset: {md: 1, lg: 2}}) {
Column() {
ForEach([0, 1, 2, 4], () => {
Column() {
ItemContent()
}
})
}.width('100%')
}
}
.margin({left: this.gridMargin, right: this.gridMargin})
.onBreakpointChange((breakpoint: string) => {
if (breakpoint === 'lg') {
this.gridMargin = 48
} else if (breakpoint === 'md') {
this.gridMargin = 32
} else {
this.gridMargin = 24
}
})
}
.height('100%')
.alignItems((VerticalAlign.Center))
.backgroundColor('#F1F3f5')
}
}
@Component
struct ItemContent {
build() {
Column() {
Row() {
Row() {
}
.width(28)
.height(28)
.borderRadius(14)
.margin({ right: 15 })
.backgroundColor('#E4E6E8')
Row() {
}
.width('30%').height(20).borderRadius(4)
.backgroundColor('#E4E6E8')
}.width('100%').height(28)
Row() {
}
.width('100%')
.height(68)
.borderRadius(16)
.margin({ top: 12 })
.backgroundColor('#E4E6E8')
}
.height(128)
.borderRadius(24)
.backgroundColor('#FFFFFF')
.padding({ top: 12, bottom: 12, left: 18, right: 18 })
.margin({ bottom: 12 })
}
}
```
挪移布局
布局效果
| sm | md | lg |
| --- | --- | --- |
| 图片和文字上下布局。 | 图片和文字左右布局。 | 图片和文字左右布局。 |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.39903875039941810879797722503795:50001231000000:2800:37FF50F263939D0413241FF9BF3F0CB8211A1D0FD5585F44C106B3FC7118CB11.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.99221819838994902336975450898871:50001231000000:2800:7817253D12450866855794A20FB501C83D8A4338B48A99BC287F02A24A70D64A.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.74364670639227228078757526141624:50001231000000:2800:35E56A0FB3E394676404F8B1C88DB620A67C5968D56970A31560EAEDA9854AC0.jpg)
实现方案
不同断点下，栅格子元素占据的列数会随着开发者的配置发生改变。当一行中的列数超过栅格组件在该断点的总列数时，可以自动换行，即实现”上下布局”与”左右布局”之间切换的效果。
参考代码
```typescript
@Entry
@Component
struct DiversionSample {
@State private currentBreakpoint: string = 'md'
@State private imageHeight: number = 0
build() {
Row() {
GridRow() {
GridCol({span: {sm: 12, md: 6, lg: 6}}) {
Image($r('app.media.illustrator'))
.aspectRatio(1)
.onAreaChange((oldValue: Area, newValue: Area) => {
this.imageHeight = Number(newValue.height)
})
.margin({left: 12, right: 12})
}
GridCol({span: {sm: 12, md: 6, lg: 6}}) {
Column(){
Text($r('app.string.user_improvement'))
.textAlign(TextAlign.Center)
.fontSize(20)
.fontWeight(FontWeight.Medium)
Text($r('app.string.user_improvement_tips'))
.textAlign(TextAlign.Center)
.fontSize(14)
.fontWeight(FontWeight.Medium)
}
.margin({left: 12, right: 12})
.justifyContent(FlexAlign.Center)
.height(this.currentBreakpoint === 'sm' ? 100 : this.imageHeight)
}
}.onBreakpointChange((breakpoint: string) => {
this.currentBreakpoint = breakpoint;
})
}
.height('100%')
.alignItems((VerticalAlign.Center))
.backgroundColor('#F1F3F5')
}
}
```
重复布局
布局效果
| sm | md | lg |
| --- | --- | --- |
| 单列显示，共8个元素 可以通过上下滑动查看不同的元素。 | 双列显示，共8个元素。 | 双列显示，共8个元素。 |
|  |  |  |
单列显示，共8个元素
可以通过上下滑动查看不同的元素。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.85649068663817201355525771131229:50001231000000:2800:10468D999DD321A8725AE57077D4554ECE76148A827BD3E453F669488E6E9D86.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.54331715272300956852932326606729:50001231000000:2800:A16EB4D859A34CEAE428966DF95CFC8AF94CC928273C1656BA3383F64A8CFE9F.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165830.93983789814311359189923944243874:50001231000000:2800:0898CF454724FD93C4524A594336071E82905E56F12160EDA5C3AA19B39241CB.jpg)
实现方案
不同断点下，配置栅格子组件占据不同的列数，即可实现“小屏单列显示、大屏双列显示”的效果。另外，还可以通过栅格组件的onBreakpointChange事件，调整页面中显示的元素数量。
参考代码
```typescript
@Entry
@Component
struct RepeatSample {
@State private currentBreakpoint: string = 'md'
@State private listItems: number[] = [1, 2, 3, 4, 5, 6, 7, 8]
@State private gridMargin: number = 24
build() {
Row() {
// 当目标区域不足以显示所有元素时，可以通过上下滑动查看不同的元素
Scroll() {
GridRow({gutter: 24}) {
ForEach(this.listItems, () => {
// 通过配置元素在不同断点下占的列数，实现不同的布局效果
GridCol({span: {sm: 12, md: 6, lg: 6}}) {
Column() {
RepeatItemContent()
}
}
})
}
.margin({left: this.gridMargin, right: this.gridMargin})
.onBreakpointChange((breakpoint: string) => {
this.currentBreakpoint = breakpoint;
if (breakpoint === 'lg') {
this.gridMargin = 48
} else if (breakpoint === 'md') {
this.gridMargin = 32
} else {
this.gridMargin = 24
}
})
}.height(348)
}
.height('100%')
.backgroundColor('#F1F3F5')
}
}
@Component
struct RepeatItemContent {
build() {
Flex() {
Row() {
}
.width(43)
.height(43)
.borderRadius(12)
.backgroundColor('#E4E6E8')
.flexGrow(0)
Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceAround }) {
Row() {
}
.height(10)
.width('80%')
.backgroundColor('#E4E6E8')
Row() {
}
.height(10)
.width('50%')
.backgroundColor('#E4E6E8')
}
.flexGrow(1)
.margin({ left: 13 })
}
.padding({ top: 13, bottom: 13, left: 13, right: 37 })
.height(69)
.backgroundColor('#FFFFFF')
.borderRadius(24)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/typical-scenarios-V14
爬取时间: 2025-04-30 04:44:34
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/appgallery-home-page-V14
爬取时间: 2025-04-30 04:44:47
来源: Huawei Developer
本小节将以应用市场首页为例，介绍如何使用自适应布局能力和响应式布局能力适配不同尺寸窗口。
页面设计
一个典型的应用市场首页的UX设计如下所示。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.88494168618519405020215395817119:50001231000000:2800:034ED8ABC27A1D3B3960E52104C246D6860424A67AB410DFF11BE2BE7C396195.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.20246626716149392673415679999065:50001231000000:2800:DB976DD1262569D16234A8E0AE17E70428F70A6C5BCFB5D0BFA1994701F8846D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.09678728097012613304602545837197:50001231000000:2800:3C685A0C8C9DDB0967B5F15A65386419DBE9866E47BD6717430321899A70F3CE.png)
观察应用市场首页的页面设计，不同断点下的页面设计有较多相似的地方。
据此，我们可以将页面分拆为多个组成部分。
1.  底部/侧边导航栏
2.  标题栏与搜索栏
3.  运营横幅
4.  快捷入口
5.  精品应用
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.34892608005495758572949628240835:50001231000000:2800:9F42D70F15C50F448EC119BB8FF4A787D3E5961C80ABD57A73B8F4A8A0B733E8.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.53099723415856332451674852191236:50001231000000:2800:D7A26214CCCB43DBB9FAD8133DC26783369375995FE8C04BA19FC41C7865CF89.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.68408674886320683162374975494454:50001231000000:2800:209BE41DF01026C84CE3A47BCF8A04EAECA2962570DC278A990EC806049A2A33.png)
接下来我们逐一分析各部分的实现。
底部/侧边导航栏
在sm和md断点下，导航栏在底部；在lg断点下，导航栏在左侧。可以通过Tab组件的barPosition和vertical属性控制TabBar的位置，同时还可以通过barWidth和barHeight属性控制TabBar的尺寸。
```typescript
//BreakpointSystem.ets
import mediaQuery from '@ohos.mediaquery'
export default class BreakpointSystem {
private currentBreakpoint: string = 'md'
private smListener?: mediaQuery.MediaQueryListener
private mdListener?:mediaQuery.MediaQueryListener
private lgListener?: mediaQuery.MediaQueryListener
private updateCurrentBreakpoint(breakpoint: string) {
if (this.currentBreakpoint !== breakpoint) {
this.currentBreakpoint = breakpoint
AppStorage.Set<string>('currentBreakpoint', this.currentBreakpoint)
}
}
private isBreakpointSM = (mediaQueryResult:mediaQuery.MediaQueryResult) => {
if (mediaQueryResult.matches) {
this.updateCurrentBreakpoint('sm')
}
}
private isBreakpointMD = (mediaQueryResult:mediaQuery.MediaQueryResult) => {
if (mediaQueryResult.matches) {
this.updateCurrentBreakpoint('md')
}
}
private isBreakpointLG = (mediaQueryResult:mediaQuery.MediaQueryResult) => {
if (mediaQueryResult.matches) {
this.updateCurrentBreakpoint('lg')
}
}
public register() {
this.smListener = mediaQuery.matchMediaSync('(320vp<=width<600vp)')
this.smListener.on('change', this.isBreakpointSM)
this.mdListener = mediaQuery.matchMediaSync('(600vp<=width<840vp)')
this.mdListener.on('change', this.isBreakpointMD)
this.lgListener = mediaQuery.matchMediaSync('(840vp<=width)')
this.lgListener.on('change', this.isBreakpointLG)
}
public unregister() {
this.smListener?.off('change', this.isBreakpointSM)
this.mdListener?.off('change', this.isBreakpointMD)
this.lgListener?.off('change', this.isBreakpointLG)
}
}
```
```typescript
import Home from '../common/Home'; //组件请参考相关实例
import TabBarItem from '../common/TabBarItem';
import BreakpointSystem from '../common/BreakpointSystem'
@Entry
@Component
struct Index {
@State currentIndex: number = 0
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'md'
private breakpointSystem: BreakpointSystem = new BreakpointSystem()
private onTabChange = (index: number) => {
this.currentIndex = index
}
aboutToAppear() {
this.breakpointSystem.register()
}
aboutToDisappear() {
this.breakpointSystem.unregister()
}
@Builder
tabItem(index: number, title: Resource, icon: Resource, iconSelected: Resource) {
TabBarItem({
index: index,
currentIndex: this.currentIndex,
title: title,
icon: icon,
iconSelected: iconSelected
})
}
build() {
// 设置TabBar在主轴方向起始或结尾位置
Tabs({ barPosition: this.currentBreakpoint === "lg" ? BarPosition.Start : BarPosition.End }) {
// 首页
TabContent() {
Home()
}
.tabBar(this.tabItem(0, $r('app.string.tabBar1'), $r('app.media.ic_home_normal'),
$r('app.media.ic_home_actived')))
TabContent() {
}.tabBar(this.tabItem(1, $r('app.string.tabBar2'), $r('app.media.ic_app_normal'), $r('app.media.ic_app_actived')))
TabContent() {
}
.tabBar(this.tabItem(2, $r('app.string.tabBar3'), $r('app.media.ic_game_normal'),
$r('app.media.ic_mine_actived')))
TabContent() {
}
.tabBar(this.tabItem(3, $r('app.string.tabBar4'), $r('app.media.ic_search_normal'),
$r('app.media.ic_search_actived')))
TabContent() {
}
.tabBar(this.tabItem(4, $r('app.string.tabBar4'), $r('app.media.ic_mine_normal'),
$r('app.media.ic_mine_actived')))
}
.backgroundColor('#F1F3F5')
.barMode(BarMode.Fixed)
.barWidth(this.currentBreakpoint === "lg" ? 96 : '100%')
.barHeight(this.currentBreakpoint === "lg" ? '60%' : 56)
// 设置TabBar放置在水平或垂直方向
.vertical(this.currentBreakpoint === "lg")
}
}
```
另外在sm及lg断点下，TabBar中各个Item的图标和文字是按照垂直方向排布的，在md断点下，TabBar中各个Item的图标和文字是按照水平方向排布的。
```typescript
interface GeneratedObjectLiteralInterface_1 {
NORMAL: string;
SELECTED: string;
}
const TitleColor: GeneratedObjectLiteralInterface_1 = {
NORMAL: '#999',
SELECTED: '#0A59F7'
}
@Component
export default struct TabBarItem {
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'md'
@Prop currentIndex: number
private index?:number
private icon?:Resource
private iconSelected?:Resource
private title?:Resource
private getIcon() {
return this.currentIndex === this.index ? this.iconSelected : this.icon
}
private getFontColor() {
return this.currentIndex === this.index ? TitleColor.SELECTED : TitleColor.NORMAL
}
build() {
if (this.currentBreakpoint !== 'md' ) {
Column() {
Image(this.getIcon())
.width(24)
.height(24)
.margin(5)
.objectFit(ImageFit.Contain)
Text(this.title)
.fontColor(this.getFontColor())
.fontSize(12)
.fontWeight(500)
}.justifyContent(FlexAlign.Center).height('100%').width('100%')
} else {
Row() {
Image(this.getIcon())
.width(24)
.height(24)
.margin(5)
.objectFit(ImageFit.Contain)
Text(this.title)
.fontColor(this.getFontColor())
.fontSize(12)
.fontWeight(500)
}.justifyContent(FlexAlign.Center).height('100%').width('100%')
}
}
}
```
标题栏与搜索栏
标题栏和搜索栏，在sm和md断点下分两行显示，在lg断点下单行显示，可以通过栅格实现。在sm和md断点下，标题栏和搜索栏占满12列，此时会自动换行显示。在lg断点下，标题栏占8列而搜索栏占4列，此时标题栏和搜索栏在同一行中显示。
|  | sm/md | lg |
| --- | --- | --- |
| 效果图 |  |  |
| 栅格布局图 |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.01823686901860863287592007860666:50001231000000:2800:18DEAA55686DF7F96A132D28892BD9B6F7E4E8D70210AA5E83D7730F07EA6116.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.41918517314136237411990133411259:50001231000000:2800:BE4EEE42453013F82CCE1E77A8342D73C9C4A72E8630F98524D2C259FB44F9C5.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165831.44199802418661573706438420150998:50001231000000:2800:BB7A03C2F99327BB29BEC08495C1D9C1C23B9727E5E0171D4F75B24BE400DE36.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.59023996455074551714016399829407:50001231000000:2800:CC53117F368FF2646E215C5C8A00B2BD5FF942C36F005CB216E2C73FFF57C2B5.png)
```typescript
@Component
export default struct IndexHeader {
@Builder searchBar() {
Stack({alignContent: Alignment.End}) {
TextInput({ placeholder: $r('app.string.search') })
.placeholderColor('#FF000000')
.placeholderFont({ size: 16, weight: 400 })
.textAlign(TextAlign.Start)
.caretColor('#FF000000')
.width('100%')
.height(40)
.fontWeight(400)
.padding({ top: 9, bottom: 9 })
.fontSize(16)
.backgroundColor(Color.White)
Image($r('app.media.ic_public_search'))
.width(16)
.height(16)
.margin({ right: 20 })
}.height(56).width('100%')
}
@Builder titleBar() {
Text($r('app.string.tabBar1'))
.fontSize(24)
.fontWeight(500)
.fontColor('#18181A')
.textAlign(TextAlign.Start)
.height(56)
.width('100%')
}
build() {
// 借助栅格实现标题栏和搜索栏在不同断点下的不同布局效果。
GridRow() {
GridCol({ span: { xs: 12, lg: 8 } }) {
this.titleBar()
}
GridCol({ span: { xs: 12, lg: 4 } }) {
this.searchBar()
}
}
.width('100%')
}
}
```
运营横幅
不同断点下的运营横幅，sm断点下显示一张图片，md断点下显示两张图片，lg断点下显示三张图片。可以通过Swiper组件的displayCount属性实现目标效果。
```typescript
@Component
export default struct IndexSwiper {
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'md';
@Builder swiperItem(imageSrc:Resource) {
Image(imageSrc)
.width('100%')
.aspectRatio(2.5)
.objectFit(ImageFit.Fill)
}
build() {
Swiper() {
this.swiperItem($r('app.media.ic_public_swiper1'))
this.swiperItem($r('app.media.ic_public_swiper2'))
this.swiperItem($r('app.media.ic_public_swiper3'))
// ...
}
.autoPlay(true)
.indicator(false)
.itemSpace(10)
// 配置不同断点下运行横幅中展示的图片数量
.displayCount(this.currentBreakpoint === 'sm' ? 1 : (this.currentBreakpoint === 'md' ? 2 : 3))
.width('100%')
.padding({ left: 12, right: 12, bottom: 16, top: 16 })
}
}
```
快捷入口
在不同的断点下，快捷入口的5个图标始终均匀排布，这是典型的均分能力使用场景。图标资源文件获取。
```typescript
// /model/HomeData   在resourse文件中放置以下资源文件，
interface AppItem{
id:string;
title:Resource;
image:Resource;
}
const appList:AppItem[] = [
{ id: '0', title: $r('app.string.public_app1'), image: $r('app.media.ic_public_app1') },
{ id: '1', title: $r('app.string.public_app2'), image: $r('app.media.ic_public_app2') },
{ id: '2', title: $r('app.string.public_app3'), image: $r('app.media.ic_public_app3') },
{ id: '3', title: $r('app.string.public_app4'), image: $r('app.media.ic_public_app4') },
{ id: '4', title: $r('app.string.public_app5'), image: $r('app.media.ic_public_app5') },
{ id: '5', title: $r('app.string.public_app6'), image: $r('app.media.ic_public_app6') },
{ id: '6', title: $r('app.string.public_app7'), image: $r('app.media.ic_public_app7') },
{ id: '7', title: $r('app.string.public_app8'), image: $r('app.media.ic_public_app8') },
{ id: '8', title: $r('app.string.public_app9'), image: $r('app.media.ic_public_app9') },
{ id: '9', title: $r('app.string.public_app10'), image: $r('app.media.ic_public_app10') },
{ id: '10', title: $r('app.string.public_app1'), image: $r('app.media.ic_public_app1') },
{ id: '11', title: $r('app.string.public_app1'), image: $r('app.media.ic_public_app1') },
{ id: '12', title: $r('app.string.public_app2'), image: $r('app.media.ic_public_app2') },
{ id: '13', title: $r('app.string.public_app3'), image: $r('app.media.ic_public_app3') },
{ id: '14', title: $r('app.string.public_app4'), image: $r('app.media.ic_public_app4') },
{ id: '15', title: $r('app.string.public_app5'), image: $r('app.media.ic_public_app5') },
{ id: '16', title: $r('app.string.public_app6'), image: $r('app.media.ic_public_app6') },
{ id: '17', title: $r('app.string.public_app7'), image: $r('app.media.ic_public_app7') },
{ id: '18', title: $r('app.string.public_app8'), image: $r('app.media.ic_public_app8') },
{ id: '19', title: $r('app.string.public_app9'), image: $r('app.media.ic_public_app9') },
{ id: '20', title: $r('app.string.public_app10'), image: $r('app.media.ic_public_app10') }
]
const gameList:AppItem[] = [
{ id: '21', title: $r('app.string.public_game1'), image: $r('app.media.ic_public_game1') },
{ id: '22', title: $r('app.string.public_game2'), image: $r('app.media.ic_public_game2') },
{ id: '23', title: $r('app.string.public_game3'), image: $r('app.media.ic_public_game3') },
{ id: '24', title: $r('app.string.public_game4'), image: $r('app.media.ic_public_game4') },
{ id: '25', title: $r('app.string.public_game5'), image: $r('app.media.ic_public_game5') },
{ id: '26', title: $r('app.string.public_game6'), image: $r('app.media.ic_public_game6') },
{ id: '27', title: $r('app.string.public_game7'), image: $r('app.media.ic_public_game7') },
{ id: '28', title: $r('app.string.public_game8'), image: $r('app.media.ic_public_game8') },
{ id: '29', title: $r('app.string.public_game9'), image: $r('app.media.ic_public_game9') },
{ id: '30', title: $r('app.string.public_game10'), image: $r('app.media.ic_public_game10') },
{ id: '31', title: $r('app.string.public_game1'), image: $r('app.media.ic_public_game1') },
{ id: '32', title: $r('app.string.public_game2'), image: $r('app.media.ic_public_game2') },
{ id: '33', title: $r('app.string.public_game3'), image: $r('app.media.ic_public_game3') },
{ id: '34', title: $r('app.string.public_game4'), image: $r('app.media.ic_public_game4') },
{ id: '35', title: $r('app.string.public_game5'), image: $r('app.media.ic_public_game5') },
{ id: '36', title: $r('app.string.public_game6'), image: $r('app.media.ic_public_game6') },
{ id: '37', title: $r('app.string.public_game7'), image: $r('app.media.ic_public_game7') },
{ id: '38', title: $r('app.string.public_game8'), image: $r('app.media.ic_public_game8') },
{ id: '39', title: $r('app.string.public_game9'), image: $r('app.media.ic_public_game9') },
{ id: '40', title: $r('app.string.public_game10'), image: $r('app.media.ic_public_game10') }
]
const entranceIcons:AppItem[]= [
{ id: '41',title: $r('app.string.home_categories'), image: $r('app.media.ic_home_categories') },
{ id: '42',title: $r('app.string.home_top'), image: $r('app.media.ic_home_top') },
{ id: '43',title: $r('app.string.home_fast'), image: $r('app.media.ic_home_fast') },
{ id: '44',title: $r('app.string.home_flower'), image: $r('app.media.ic_home_flower') },
{ id: '45',title: $r('app.string.home_education'), image: $r('app.media.ic_home_education') },
]
export { entranceIcons, appList, gameList }
```
```typescript
//model/HomeDataType
interface AllIcons {
image: Resource,
title: Resource,
}
interface AppItem  {
id: string,
title: Resource,
image: Resource
}
class MyAppSource implements IDataSource {
private dataArray: AppItem[] = []
private listeners: DataChangeListener[] = []
constructor(element: AppItem[]) {
for (let index = 0; index < element.length; index++) {
this.dataArray.push(element[index])
}
}
public totalCount(): number {
return this.dataArray.length
}
public getData(index: number): AppItem {
return this.dataArray[index]
}
public addData(index: number, data: AppItem): void {
this.dataArray.splice(index, 0, data)
this.notifyDataAdd(index)
}
public pushData(data: AppItem): void {
this.dataArray.push(data)
this.notifyDataAdd(this.dataArray.length - 1)
}
registerDataChangeListener(listener: DataChangeListener): void {
if (this.listeners.indexOf(listener) < 0) {
this.listeners.push(listener)
}
}
unregisterDataChangeListener(listener: DataChangeListener): void {
const pos = this.listeners.indexOf(listener);
if (pos >= 0) {
this.listeners.splice(pos, 1)
}
}
notifyDataReload(): void {
this.listeners.forEach(listener => {
listener.onDataReloaded()
})
}
notifyDataAdd(index: number): void {
this.listeners.forEach(listener => {
listener.onDataAdd(index)
})
}
notifyDataChange(index: number): void {
this.listeners.forEach(listener => {
listener.onDataChange(index)
})
}
notifyDataDelete(index: number): void {
this.listeners.forEach(listener => {
listener.onDataDelete(index)
})
}
notifyDataMove(from: number, to: number): void {
this.listeners.forEach(listener => {
listener.onDataMove(from, to)
})
}
}
export { AllIcons, MyAppSource, AppItem }
```
```typescript
import { entranceIcons } from '../model/HomeData';
import { AllIcons } from '../model/HomeDataType';
@Component
export default struct IndexEntrance {
build() {
// 将justifyContent参数配置为FlexAlign.SpaceEvenly实现均分布局
Row() {
ForEach(entranceIcons, (icon: AllIcons) => {
// 各快捷入口的图标及名称
Column() {
// ...
}
})
}
.width('100%')
.height(64)
.justifyContent(FlexAlign.SpaceEvenly)
.padding({ left: 12, right: 12 })
}
}
```
精品应用
随着可用显示区域的增加，精品应用中显示的图标数量也不断增加，这是典型的延伸能力使用场景。精品游戏的实现与精品应用类似，不再展开分析。
```typescript
import { AppItem, MyAppSource } from '../model/HomeDataType';
@Component
export default struct IndexApps {
private title?: Resource;
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'md';
private apps: AppItem[] = [];
@Builder
appListHeader() {
Row() {
Text(this.title)
.width(100)
.fontSize(16)
.textAlign(TextAlign.Start)
.fontWeight(500)
Blank()
Text($r('app.string.more'))
.fontSize(14)
.textAlign(TextAlign.End)
.fontWeight(400)
.margin({ right: 2 })
Image($r('app.media.ic_public_arrow_right'))
.width(12)
.height(18)
.opacity(0.9)
.objectFit(ImageFit.Fill)
}
.margin({ bottom: 9, top: 9 })
.width('100%')
.alignItems(VerticalAlign.Bottom)
}
@Builder
appListItem(app:AppItem) {
Column() {
Image(app.image)
.width(this.currentBreakpoint === 'lg' ? 80 : 56)
.height(this.currentBreakpoint === 'lg' ? 80 : 56)
.margin({ bottom: 8 })
Text(app.title)
.width(this.currentBreakpoint === 'lg' ? 80 : 56)
.height(16)
.fontSize(12)
.textAlign(TextAlign.Center)
.fontColor('#18181A')
.margin({ bottom: 8 })
Text($r('app.string.install'))
.width(this.currentBreakpoint === 'lg' ? 80 : 56)
.height(28)
.fontColor('#0A59F7')
.textAlign(TextAlign.Center)
.borderRadius(this.currentBreakpoint === 'lg' ? 26 : 20)
.fontWeight(500)
.fontSize(12)
.padding({ top: 6, bottom: 6, left: 8, right: 8 })
.backgroundColor('rgba(0,0,0,0.05)')
}
}
build() {
Column() {
this.appListHeader()
// 借助List组件能力，实现延伸能力场景
List({ space: this.currentBreakpoint === 'lg' ? 44 : 20}) {
LazyForEach(new MyAppSource(this.apps), (app: AppItem)=> {
ListItem() {
// 每个应用的图标、名称及安装按钮
this.appListItem(app)
}
})
}
.width('100%')
.height(this.currentBreakpoint === 'lg' ? 140 : 120)
.listDirection(Axis.Horizontal)
}
.width('100%')
.height(this.currentBreakpoint === 'lg' ? 188 : 164)
.padding({ bottom: 8, left: 12, right: 12 })
}
}
```
运行效果
将上述各页面主要部分组合在一起后，即可完成整体页面开发。
```typescript
entry/src/main/ets                         // 代码区
|---model
|   |---HomeData.ets                       // 主页用到的图片资源
|   |---HomeDataType.ets                   // 事件监听函数
|---pages
|   |---index.ets                          // 首页
|---common
|   |---BreakpointSystem.ets               // 媒体查询
|   |---Home.ets                           // 主容器
|   |---IndexApps.ets                      // app模块(包含安装，展示图片，更多功能)
|   |---IndexContent.ets                   // 内容模块
|   |---IndexEntrance.ets                  // 下一步模块(箭头跳转组件)
|   |---IndexHeader.ets                    // 头部组件
|   |---IndexSwiper.ets                    // 轮播图
|   |---TabBarItem.ets                     // 导航栏
entry/src/main/resources                   // 资源文件
```
```typescript
import IndexSwiper from './IndexSwiper';
import IndexEntrance from './IndexEntrance';
import IndexApps from './IndexApps';
import { appList, gameList } from '../model/HomeData';
import IndexHeader from './IndexHeader';
@Component
struct IndexContent {
// ...
build() {
List() {
// 运营横幅
ListItem() {
IndexSwiper()
}
// 快捷入口
ListItem() {
IndexEntrance()
}
// 精品应用
ListItem() {
IndexApps({ title: $r('app.string.boutique_application'), apps: appList })
}
// 精品游戏
ListItem() {
IndexApps({ title: $r('app.string.boutique_game'), apps: gameList })
}
}
.width("100%")
}
}
@Entry
@Component
export default struct Home {
// ...
build() {
Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Start }) {
// 标题栏和搜索栏
IndexHeader()
// 运营横幅、快捷入口、精品应用、精品游戏等
IndexContent()
}
.height('100%')
.backgroundColor("#F1F3F5")
}
}
```
本页面的实际运行效果如下图所示。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.21218771214402990678549283416544:50001231000000:2800:54AF6A6D2B0D2E3831E008643C5E4743E2AE09D871D8483B1D31F1114DF7EFFB.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.52196051570864841871075937807600:50001231000000:2800:D46F7F8F950FD71A086C6A2A875BD556FDF79A87CE0C75339E7B806BCCD7CD28.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.75097149527897056454973725168479:50001231000000:2800:E047BA6735774F993694DCC1C5D3065CEF1D475B9A7F70A73341D9532D760453.jpg)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/music-album-page-V14
爬取时间: 2025-04-30 04:45:01
来源: Huawei Developer
本小节将以音乐专辑页为例，介绍如何使用自适应布局能力和响应式布局能力适配不同尺寸窗口。
页面设计
音乐专辑页的页面设计如下。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.52436317219359485473153520319470:50001231000000:2800:0584051D461AEEFD336C961002C21FC7666B4FA5DFA00EFB2B98EA15ABBE5095.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.76692990522815917544551986393034:50001231000000:2800:38A542DDC149C8C6D9CA50181B513C28F124623D20D7F3A1D7EDAAD8570B3572.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.01502050150682001109661515670997:50001231000000:2800:EB469FB51415A93A236A597E888CA5EADCC495FCF30D6920AA361E6154EC7D39.png)
同样观察音乐专辑的页面设计，不同断点下的页面设计有较多相似的地方。
据此，我们可以将页面分拆为多个组成部分。
1.  标题栏
2.  歌单封面
3.  歌单列表
4.  播放控制栏
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.51855725632234189825938840560042:50001231000000:2800:1320C72F7B596BFF57D3CADF6C0D80214BFE8654F2014BD3D723A38A394A3ACA.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165832.40670414790836276072100298263461:50001231000000:2800:7EE1261A6A9E66CA9FFFD5A0875B5D47C75C6B0578711BBDDD65528F3FED8000.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.55542687626982969853163580418696:50001231000000:2800:7D2976D062CDBE1FF6071AAB590984334B41B7645B28D11480F2C1096B5624BA.jpg)
标题栏
不同断点下，标题栏始终只显示“返回按钮”、“歌单”以及“更多按钮”，但“歌单”与“更多按钮”之间的间距不同。由于不同断点下标题栏的背景色也有较大差异，因此无法使用拉伸能力实现，此场景更适合使用栅格实现。我们可以将标题栏划分为“返回按钮及歌单”和“更多按钮”两部分，这两部分在不同断点下占据的列数如下图所示。另外，还可以借助OnBreakpointChange事件，调整不同断点下这两部分的背景色。
|  | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |
| 栅格布局图 |  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.57775465208018320257144701251727:50001231000000:2800:FCEFC0518FC610F8CB79ACADF7D9FE93BB460CBFD6F18170FC7172DB78544D75.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.44727896884612038432183468986539:50001231000000:2800:E544F286B26F67D80A9440715AE8209C726E6AB7CAE8CEFF3DB9D0C2D42A1E5B.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.40575412007976575260818464600442:50001231000000:2800:A00DC56453CE0FCA9DCED298F26FCB7F232B9A65CF5CC7A0FFEE5E75B9986207.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.82491826857964657876839938721755:50001231000000:2800:2EB616B9D67542D06056C1056C3DB06AC49204082EE7BCB2234C9AC6F2A1D7B5.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.22884030638313663190879602979279:50001231000000:2800:0888AACC4CAB4510B11F9390EC23391EE7FE6DB733A4C13AC35FC316F1B1211C.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.71748491786913247469660546165436:50001231000000:2800:E153EFDA46648F14AE90B3FCB0504540025DCD6EADEDAC87CC5760CEAFFFD7C1.png)
```typescript
@Component
export struct Header {
@State moreBackgroundColor: Resource = $r('app.color.play_list_cover_background_color');
build() {
GridRow() {
GridCol({span: {sm:6, md: 6, lg:4}}) {
Row() {
Image($r('app.media.ic_back')).height('24vp').width('24vp')
}
.width('100%')
.height('50vp')
.justifyContent(FlexAlign.Start)
.alignItems(VerticalAlign.Center)
.padding({left:$r('app.float.default_margin')})
.backgroundColor($r('app.color.play_list_cover_background_color'))
}
GridCol({span: {sm:6, md: 6, lg:8}}) {
Row() {
Image($r('app.media.ic_add')).height('24vp').width('24vp')
}
.width('100%')
.height('50vp')
.justifyContent(FlexAlign.End)
.alignItems(VerticalAlign.Center)
.padding({right:$r('app.float.default_margin')})
.backgroundColor(this.moreBackgroundColor)
}
}.onBreakpointChange((currentBreakpoint) => {
// 调整不同断点下返回按钮及歌单的背景色
if (currentBreakpoint === 'sm') {
this.moreBackgroundColor = $r('app.color.play_list_cover_background_color');
} else {
this.moreBackgroundColor = $r('app.color.play_list_songs_background_color');
}
}).height('100%').width('100%')
}
}
```
歌单封面
歌单封面由封面图片、歌单介绍及常用操作三部分组成，这三部分的布局在md和lg断点下完全相同，但在sm断点下有较大差异。此场景同样可以用栅格实现。
|  | sm | md/lg |
| --- | --- | --- |
| 效果图 |  |  |
| 栅格布局图 |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.86879649783171650976360794330882:50001231000000:2800:C17D8FB696EDA7E5FACE598A58E70F324274C2E1A299BEFAFDCF11A8CF3404BE.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.40205699971675070485003941636911:50001231000000:2800:C4097AF56E6011204A94B3870F481DB1E99D98DF357C64B419835572AD7BF393.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.06308358478654781589234153506221:50001231000000:2800:D24866ADE0CF93A69E06239E12C4D19340F8058B10DA85B47064D9B3DE24C542.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.87460109892554784487934964126355:50001231000000:2800:C28A3B61FB74C790B1454278AE70CA2A85B9F8FE6065861A23653F83A28EC2B2.png)
```typescript
import { optionList } from '../model/SongList'
@Component
export default struct PlayListCover {
@State imgHeight: number = 0;
@StorageProp('coverMargin') coverMargin: number = 0;
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'sm';
@StorageProp('fontSize') fontSize: number = 0;
@Builder
CoverImage() {
Stack({ alignContent: Alignment.BottomStart }) {
Image($r('app.media.pic_album'))
.width('100%')
.aspectRatio(1)
.borderRadius(8)
.onAreaChange((oldArea: Area, newArea: Area) => {
this.imgHeight = newArea.height as number
})
Text($r('app.string.collection_num'))
.letterSpacing(1)
.fontColor('#fff')
.fontSize(this.fontSize - 4)
.translate({ x: 10, y: '-100%' })
}
.width('100%')
.height('100%')
.aspectRatio(1)
}
@Builder
CoverIntroduction() {
Column() {
Text($r('app.string.list_name'))
.opacity(0.9)
.fontWeight(500)
.fontColor('#556B89')
.fontSize(this.fontSize + 2)
.margin({ bottom: 10 })
Text($r('app.string.playlist_Introduction'))
.opacity(0.6)
.width('100%')
.fontWeight(400)
.fontColor('#556B89')
.fontSize(this.fontSize - 2)
}
.width('100%')
.height(this.currentBreakpoint === 'sm' ? this.imgHeight : 70)
.alignItems(HorizontalAlign.Start)
.justifyContent(FlexAlign.Center)
.padding({ left: this.currentBreakpoint === 'sm' ? 20 : 0 })
.margin({
top: this.currentBreakpoint === 'sm' ? 0 : 30,
bottom: this.currentBreakpoint === 'sm' ? 0 : 20
})
}
@Builder
CoverOptions() {
Row() {
ForEach(optionList, item => {
Column({ space: 4 }) {
Image(item.image).height(30).width(30)
Text(item.text)
.fontColor('#556B89')
.fontSize(this.fontSize - 1)
}
})
}
.width('100%')
.height(70)
.padding({
left: this.currentBreakpoint === 'sm' ? 20 : 0,
right: this.currentBreakpoint === 'sm' ? 20 : 0
})
.margin({
top: this.currentBreakpoint === 'sm' ? 15 : 0,
bottom: this.currentBreakpoint === 'sm' ? 15 : 0
})
.justifyContent(FlexAlign.SpaceBetween)
}
build() {
Column() {
// 借助栅格组件实现总体布局
GridRow() {
// 歌单图片
GridCol({ span: { sm: 4, md: 10 }, offset: { sm: 0, md: 1, lg: 1 } }) {
this.CoverImage()
}
// 歌单介绍
GridCol({ span: { sm: 8, md: 10 }, offset: { sm: 0, md: 2, lg: 2 } }) {
this.CoverIntroduction()
}
// 歌单操作
GridCol({ span: { sm: 12, md: 10 }, offset: { sm: 0, md: 2, lg: 2 } }) {
this.CoverOptions()
}.margin({
top: this.currentBreakpoint === 'sm' ? 15 : 0,
bottom: this.currentBreakpoint === 'sm' ? 15 : 0
})
}
.margin({ left: this.coverMargin, right: this.coverMargin })
}
.height('100%')
.padding({ top: this.currentBreakpoint === 'sm' ? 50 : 70 })
}
}
```
歌单列表
不同断点下，歌单列表的样式基本一致，但sm和md断点下是歌单列表是单列显示，lg断点下是双列显示。可以通过List组件的lanes属性实现这一效果。
```typescript
import { songList } from '../model/SongList';
import MyDataSource from '../model/SongModule'
@Component
export default struct PlayList {
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'sm';
@StorageProp('fontSize') fontSize: number = 0;
@Consume coverHeight: number;
@Builder
PlayAll() {
Row() {
Image($r("app.media.ic_play_all"))
.height(23)
.width(23)
Text($r('app.string.play_all'))
.maxLines(1)
.padding({ left: 10 })
.fontColor('#000000')
.fontSize(this.fontSize)
Blank()
Image($r('app.media.ic_order_play'))
.width(24)
.height(24)
.margin({ right: 16 })
Image($r('app.media.ic_sort_list'))
.height(24)
.width(24)
}
.height(60)
.width('100%')
.padding({ left: 12, right: 12 })
}
@Builder
SongItem(title: string, label: Resource, singer: string) {
Row() {
Column() {
Text(title)
.fontColor('#000000')
.fontSize(this.fontSize)
.margin({ bottom: 4 })
Row() {
Image(label)
.width(16)
.height(16)
.margin({ right: 4 })
Text(singer)
.opacity(0.38)
.fontColor('#000000')
.fontSize(this.fontSize - 4)
}
}
.alignItems(HorizontalAlign.Start)
Blank()
Image($r('app.media.ic_list_more'))
.height(24)
.width(24)
}
.height(60)
.width('100%')
}
build() {
Column() {
this.PlayAll()
Scroll() {
List() {
LazyForEach(new MyDataSource(songList), item => {
ListItem() {
this.SongItem(item.title, item.label, item.singer)
}
})
}
.width('100%')
.height('100%')
// 配置不同断点下歌单列表的列数
.lanes(this.currentBreakpoint === 'lg' ? 2 : 1)
}
.backgroundColor('#fff')
.margin({ top: 50, bottom: this.currentBreakpoint === 'sm' ? this.coverHeight : 0 })
}
.padding({top: 50,bottom: 48})
}
}
```
播放控制栏
在不同断点下，播放控制栏显示的内容完全一致，唯一的区别是歌曲信息与播放控制按钮之间的间距有差异，这是典型的拉伸能力的使用场景。
```typescript
@Component
export default struct Player {
@StorageProp('fontSize') fontSize: number = 0;
build() {
Row() {
Image($r('app.media.pic_album')).height(32).width(32).margin({right: 12})
Column() {
Text($r('app.string.song_name'))
.fontColor('#000000')
.fontSize(this.fontSize - 1)
Row() {
Image($r('app.media.ic_vip'))
.height(16)
.width(16)
.margin({ right: 4 })
Text($r('app.string.singer'))
.fontColor('#000000')
.fontSize(this.fontSize - 4)
.opacity(0.38)
}
}
.alignItems(HorizontalAlign.Start)
// 通过Blank组件实现拉伸能力
Blank()
Image($r('app.media.icon_play')).height(26).width(26).margin({right: 16})
Image($r('app.media.ic_next')).height(24).width(24).margin({right: 16})
Image($r('app.media.ic_Music_list')).height(24).width(24)
}
.width('100%')
.height(48)
.backgroundColor('#D8D8D8')
.alignItems(VerticalAlign.Center)
.padding({left: 16, right: 16})
}
}
```
运行效果
将页面中的四部分组合在一起，即可显示完整的页面。
其中歌单封面和歌单列表这两部分的相对位置，在sm断点下是上下排布，在md和lg断点下是左右排布，也可以用栅格来实现目标效果。
|  | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |
| 栅格布局图 |  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.40808823498704181862375114416080:50001231000000:2800:19CFFE3B2220CB9482F8D586039F4701773FC9DF0746DAB864B1B18E958D3825.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.96290264173317581226273590770930:50001231000000:2800:452B3CB8F98DD1A95A4531E408FD52D15C0E49EEFA3AB8AB90D20F2383EB3652.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.71238650559234091591378981414712:50001231000000:2800:011C14280088C9C5CABC135E7E5964669EE869DE3852AF8C69E906FAC7217ACF.jpg)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165833.13341457450822052622994812257422:50001231000000:2800:00FA639ED33CDB57617C34A3B0FF17AF38D6890B1032E65C2BC777402051E22F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165834.04705463889691763084723340397869:50001231000000:2800:AB86F0FE9BD7D34EB33CAEA4AD1129C2BCABE4E78A5048842D42F8B868721B6D.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165834.20257425359398796788305379384392:50001231000000:2800:BDAEC8E4EF2A8FA54382CD6EC3DDAAC2A72826FE7F7FE6E896CD7802D2D59A82.png)
```typescript
import PlayListCover from '../common/PlayListCover';
import PlayList from '../common/PlayList';
@Component
export default struct Content {
// ...
build() {
GridRow() {
// 歌单封面
GridCol({ span: { xs: 12, sm: 12, md: 6, lg: 4 } }) {
PlayListCover()
}
// 歌单列表
GridCol({ span: { xs: 12, sm: 12, md: 6, lg: 8 } }) {
PlayList()
}
}
.height('100%')
}
}
```
最后将页面各部分组合在一起即可。
```typescript
import Header from '../common/Header';
import Player from '../common/Player';
import Content from '../common/Content';
@Entry
@Component
struct Index {
build() {
Column() {
// 标题栏
Header()
// 歌单
Content()
// 播放控制栏
Player()
}.width('100%').height('100%')
}
}
```
音乐专辑页面的运行效果如下所示。
| sm | md | lg |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165834.50390543842610365852941461140994:50001231000000:2800:D19947C3DDE10EB72BFED85B84B3A4F91F91320A48C5331694AD3C084A421E83.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165834.14669918226367392251623638189888:50001231000000:2800:85CE375C1ED4577ED023510302B9E6DED6FE78BA40C26AF8B1D5F258FDB9E6B5.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165834.30360721634665991716472010908021:50001231000000:2800:77F77DA816A4F07954D4E5CB0BDF40E4174A7A53BE5EE9EEBB934114D3F8CF12.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/settings-application-page-V14
爬取时间: 2025-04-30 04:45:14
来源: Huawei Developer
本小节以“设置”应用页面为例，介绍如何使用自适应布局能力和响应式布局能力适配不同尺寸窗口。
页面设计
为充分利用屏幕尺寸优势，应用常常有在小屏设备上单栏显示，大屏设备上左右分两栏显示的设计，设置应用页面设计如下。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165834.48245191601925181788149185870149:50001231000000:2800:E9EDCF88143EE95C1664D18A3D28F832D46566147A932DF8EA354E3D3F8A29D7.png)
观察“设置”应用页面设计，不同断点下“设置主页”、“WLAN页面”和“更多WLAN设置页面”几乎完全一致，只是在sm断点下采用单栏显示，在md和lg断点下采用双栏显示。
在前面的典型页面场景中，已经介绍了如何分析及实现不同断点下设计相似的单个页面，本小节将展开介绍如何实现不同断点下存在单栏和双栏设计的场景。
为了方便读者理解，本小节将围绕以下三个问题进行介绍。
如何实现单/双栏的显示效果
开发者可以使用Row、Column、RowSplit等基础的组件，实现分栏显示的效果，但是需要较多的开发工作量。方舟开发框架在API 9重构了Navigation组件，开发者可以通过配置Navigation组件的属性，控制其按照单栏或双栏的效果进行显示。
Navigation组件由NavBar和Content两部分区域组成，Navigation组件支持Stack、Split以及Auto三种模式。Stack及Split模式下Navigation组件的表现如下图所示。
-  Stack模式
-  Split模式
-  Auto模式 Auto模式是指Navigation组件可以根据应用窗口尺寸，自动选择合适的模式：窗口宽度小于520vp时，采用Stack模式显示；窗口宽度大于等于520vp时，采用Split模式显示。当窗口尺寸发生改变时，Navigation组件也会自动在Stack模式和Split模式之间切换。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165834.60833618823822238874639302447176:50001231000000:2800:2D047FEA311E974B7A62D4B2BBC09B0123B0096C49CC93D06811E4C8A3683402.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165834.15610951497067136450539598118412:50001231000000:2800:0D16A3CDB1787827B864F22C845AB2C4FD8B6A8CCBD47E87D9A29821B3781C22.png)
设置主页的核心代码如下所示。Navigation组件默认处于Auto模式，其样式会根据应用窗口尺寸在单栏和双栏之间自动切换。
```typescript
import { SettingList } from '@ohos/settingItems';
@Entry
@Component
struct Index {
build() {
Navigation() {
SettingList()
}
.title($r('app.string.settings'))
.navBarWidth('40%')
.width('100%')
.height('100%')
.backgroundColor($r("sys.color.ohos_id_color_sub_background"))
}
}
```
```typescript
//核心代码 SettingList.ets
import { MainItem } from '../components/MainItem';
import { ItemGroup } from '../components/ItemGroup';
import { SearchBox } from '../components/SearchBox';
import { MoreConnectionsItem } from '../moreconnections/MoreConnectionsItem';
import { WlanSettingItem } from '../wlan/WlanSettingItem';
class  ItemObj {
title?: Resource
tag?: Resource
icon?:Resource
}
let bluetoothTab:ItemObj={
title: $r('app.string.bluetoothTab'),
tag: $r('app.string.enabled'),
icon: $r('app.media.blueTooth'),
}
let mobileData:ItemObj={
title: $r('app.string.mobileData'),
icon: $r('app.media.mobileData'),
}
let brightnessTab:ItemObj={
title: $r('app.string.brightnessTab'),
icon: $r('app.media.displayAndBrightness'),
}
let volumeControlTab:ItemObj={
title: $r('app.string.volumeControlTab'),
icon: $r('app.media.volume'),
}
let biometricsAndPassword:ItemObj={
title: $r('app.string.biometricsAndPassword'),
icon: $r('app.media.biometricsAndPassword'),
}
let applyTab:ItemObj={
title: $r('app.string.applyTab'),
icon: $r('app.media.application'),
}
let storageTab:ItemObj={
title: $r('app.string.storageTab'),
icon: $r('app.media.storage'),
}
let security:ItemObj={
title: $r('app.string.security'),
icon: $r('app.media.security'),
}
let privacy:ItemObj={
title: $r('app.string.privacy'),
icon: $r('app.media.privacy'),
}
let usersAccountsTab:ItemObj={
title: $r('app.string.usersAccountsTab'),
icon: $r('app.media.userAccounts'),
}
let systemTab:ItemObj={
title: $r('app.string.systemTab'),
icon: $r('app.media.system'),
}
let aboutTab:ItemObj={
title: $r('app.string.aboutTab'),
icon: $r('app.media.aboutDevice'),
}
@Component
export struct SettingList {
@Builder
CustomDivider() {
Divider()
.strokeWidth('1px')
.color($r('sys.color.ohos_id_color_list_separator'))
.margin({ left: 48, right: 8 })
}
build() {
List({ space: 12 }) {
ListItem() {
SearchBox()
}
.padding({ top: 8, bottom: 8 })
.width('100%')
ListItem() {
ItemGroup() {
WlanSettingItem()
this.CustomDivider()
MainItem(bluetoothTab)
this.CustomDivider()
MainItem(mobileData)
this.CustomDivider()
MoreConnectionsItem()
}
}
ListItem() {
ItemGroup() {
MainItem(brightnessTab)
}
}
ListItem() {
ItemGroup() {
MainItem(volumeControlTab)
}
}
ListItem() {
ItemGroup() {
MainItem(biometricsAndPassword)
this.CustomDivider()
MainItem(applyTab)
this.CustomDivider()
MainItem(storageTab)
this.CustomDivider()
MainItem(security)
this.CustomDivider()
MainItem(privacy)
}
}
ListItem() {
ItemGroup() {
MainItem(usersAccountsTab)
this.CustomDivider()
MainItem(systemTab)
this.CustomDivider()
MainItem(aboutTab)
}
}
}
.padding({ left: 12, right: 12 })
.width('100%')
.height('100%')
.backgroundColor($r('sys.color.ohos_id_color_sub_background'))
}
}
```
如何实现点击跳转或刷新
Navigation组件通常搭配NavRouter组件以及NavDestination组件一起使用：
刷新控制
NavRouter组件用于控制Navigation组件中Content区域的刷新逻辑，其必须包含两个子节点。
|  | 节点类型 | 节点功能 |
| --- | --- | --- |
| 第一个子节点 | 容器类组件 | 直接控制NavRouter的显示效果 |
| 第二个子节点 | NavDestination组件 | 刷新Navigation组件Content区域的显示 |
NavRouter组件默认提供了点击响应处理，不需要开发者自定义点击事件逻辑。另外，NavRouter组件还提供了onStateChange回调事件，用于通知开发者NavRouter的状态：用户点击NavRouter，激活NavRouter并加载对应的NavDestination子组件时，回调onStateChange(true)；NavRouter对应的NavDestination子组件不再显示时，回调onStateChange(false)。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165835.44231408652016904876307333789360:50001231000000:2800:77CA7BD353F67143F5FF3144DB5B2EAF746AFAFA2EEC8154063FDEAB1823B33F.png)
结合设置应用的具体场景来看，上图1号小红框是NavRouter的第一个子节点，2号红框是NavRouter的第二个子节点，相应的核心代码实现如下。
```typescript
import { MainItem } from '../components/MainItem';
import { WlanMoreSettingItem } from '../components/WlanMoreSettingItem';
import { SubItemToggle } from '../components/SubItemToggle';
import { SubItemWifi } from '../components/SubItemWifi';
import { ItemDescription } from '../components/ItemDescription';
import { ItemGroup } from '../components/ItemGroup';
class  MainItemObj {
title?: Resource
tag?: string
icon?:Resource
label?: string
}
let mainItem:MainItemObj={
title: $r('app.string.wifiTab'),
tag: 'UX',
icon: $r('app.media.wlan'),
label: 'WLAN'
}
@Component
export struct WlanSettingItem {
@LocalStorageLink('selectedLabel') selectedLabel: string  = ''
build() {
Column() {
NavRouter() {
MainItem(mainItem)
NavDestination() {
WlanSetting()
}
.title($r('app.string.wifiTab'))
.backgroundColor($r('sys.color.ohos_id_color_sub_background'))
}
}
}
}
@Component
struct WlanSetting {
@Builder CustomDivider() {
Divider()
.strokeWidth('1px')
.color($r('sys.color.ohos_id_color_list_separator'))
.margin({left: 12, right: 8})
}
build() {
Column() {
Column() {
ItemGroup() {
SubItemToggle({title: $r('app.string.wifiTab'), isOn: true})
}
Row().height(16)
ItemGroup() {
WlanMoreSettingItem()
}
}
.margin({bottom: 19.5})
.flexShrink(0)
Scroll() {
Column() {
ItemDescription({description: $r('app.string.wifiTipConnectedWLAN')})
.padding({
left: 12,
right: 12,
bottom: 9.5
})
ItemGroup() {
SubItemWifi({
title: 'UX',
subTitle: $r('app.string.wifiSummaryConnected'),
isConnected: true,
icon: $r('app.media.ic_wifi_signal_4_dark')
})
}
Column() {
ItemDescription({description: $r('app.string.wifiTipValidWLAN')})
.margin({
left: 12,
right: 12,
top: 19.5,
bottom: 9.5
})
ItemGroup() {
SubItemWifi({
title: 'Huwe-yee',
subTitle: $r('app.string.wifiSummaryEncrypted'),
isConnected: false,
icon: $r('app.media.ic_wifi_lock_signal_4_dark')
})
this.CustomDivider()
SubItemWifi({
title: 'UX-5G',
subTitle: $r('app.string.wifiSummaryOpen'),
isConnected: false,
icon: $r('app.media.ic_wifi_signal_4_dark')
})
this.CustomDivider()
SubItemWifi({
title: 'E1-AP',
subTitle: $r('app.string.wifiSummarySaveOpen'),
isConnected: false,
icon: $r('app.media.ic_wifi_signal_4_dark')
})
}
}
}
}
.scrollable(ScrollDirection.Vertical)
.scrollBar(BarState.Off)
.width('100%')
.flexShrink(1)
}
.width('100%')
.height('100%')
.padding({left: 12, right: 12})
}
}
```
显示刷新
NavDestination组件用于实际刷新Navigation组件Content区域的显示。激活后的NavRouter对应的NavDestination组件，会占满整个Content区域并刷新其显示。
开发者可以通过NavDestination组件提供的如下属性，调整其最终显示效果：
特别的，Navigation组件会根据当前的状态决定是否在NavDestination组件标题栏起始部分自动添加返回键图标。当Navigation组件添加了返回键图标时，还可以自动响应及处理系统三键导航中的返回键事件。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165835.61415815496046752574743902166814:50001231000000:2800:438E413AFF7DE98B3A7C151B97614D7832FE807F23ACDBF3349144A519F746F9.png)
如何实现多级跳转
可以在NavDesination组件中，继续使用NavRouter组件，以实现多级跳转。多级跳转场景下，Navigation组件同样会根据当前的状态决定是否自动添加返回键图标及响应系统三键导航中的返回键事件。
| 一级页面 | 二级页面 |
| --- | --- |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165835.00698940467325708338820801141148:50001231000000:2800:9616591601CC79F751045ACEACBC5F62D4D7924EA8FB580A19AA8EED24EA887F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165835.05161844013865490432731082095550:50001231000000:2800:8A63EA6EF17BD4F6A59AD8418A8D333A0C8B8A33830B17FA47BDA38467473517.png)
结合具体场景，红框3是一个NavRouter组件，点击后可以控制Navigation组件中的Content区域刷新为红框4对应的NavDestination组件吗，其核心代码实现如下所示。
```typescript
import { SubItemArrow } from '../components/SubItemArrow';//组件请参考相关示例
import { SubItemToggle } from '../components/SubItemToggle';
import { ItemGroup } from '../components/ItemGroup';
import { ItemDescription } from '../components/ItemDescription';
class SubItemArrowObj{
title?: Resource
}
let subItemArrow:SubItemArrowObj={
title: $r('app.string.moreWlanSettings')
}
@Component
export struct WlanMoreSettingItem {
@LocalStorageLink('selectedLabel') selectedLabel: string = ''
build() {
NavRouter() {
SubItemArrow(subItemArrow)
NavDestination() {
WlanMoreSetting()
}
.title($r('app.string.moreWlanSettings'))
.backgroundColor($r('sys.color.ohos_id_color_sub_background'))
}
}
}
@Component
export struct WlanMoreSetting {
build() {
Scroll() {
Column() {
ItemGroup() {
SubItemArrow({
title: $r('app.string.wlanPlus'),
tag: $r('app.string.enabled')
})
}
ItemDescription({description: $r('app.string.wlanPlusTip')})
.margin({
top: 8,
bottom: 24,
left: 12,
right: 12
})
ItemGroup() {
SubItemArrow({ title: $r('app.string.wlanDirect') })
}
Blank().height(12)
ItemGroup() {
SubItemToggle({title: $r('app.string.wlanSecurityCheck')})
}
ItemDescription({description: $r('app.string.wlanSecurityCheckTip')})
.margin({
top: 8,
bottom: 24,
left: 12,
right: 12
})
ItemGroup() {
SubItemArrow({title: $r('app.string.savedWlan')})
Divider()
.strokeWidth('1px')
.color($r('sys.color.ohos_id_color_list_separator'))
.margin({left: 12, right: 8})
SubItemArrow({title: $r('app.string.installCertificates')})
}
}
.backgroundColor($r('sys.color.ohos_id_color_sub_background'))
.padding({left: 12, right: 12})
}
.scrollBar(BarState.Off)
.width('100%')
}
}
```
总结
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165835.84742318119966828636160814250469:50001231000000:2800:EF55AE4EF8C5A49C6D37B0981CB888C88348466A0748A2D7C5226AE992FD1FFC.png)
本示例的基础导航结构上图所示：
Navigation组件支持自动切换单栏和双栏的显示效果，同时可以根据当前状态自动添加返回键及响应系统的返回键事件。借助Navigation组件，开发者不用关心单栏和双栏场景的差异而更关注于应用本身，极大的减少开发工作量及提高开发效率。
示例代码

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/interaction-event-normalization-V14
爬取时间: 2025-04-30 04:45:28
来源: Huawei Developer
对于不同类型的智能设备，用户可能有不同的交互方式，如通过触摸屏、鼠标、触控板等。如果针对不同的交互方式单独做适配，会增加开发工作量同时产生大量重复代码。为解决这一问题，我们统一了各种交互方式的API，即实现了交互归一。
基础输入
常见的基础输入方式及其在各输入设备上的表现如下图所示。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165835.23457551497757544388510032072665:50001231000000:2800:F43280D8471A177AF141FDAC3C190008006A9BE86FB5AC83C26AAE7B16111DE0.jpg)
基础输入对应的开发接口，以及当前支持情况如下表所示。
| 输入 | 开发接口 | 触控屏 | 触控板 | 鼠标 |
| --- | --- | --- | --- | --- |
| 悬浮 | onHover | NA | √ | √ |
| 点击 | onClick | √ | √ | √ |
| 双击 | TapGesture | √ | √ | √ |
| 长按 | LongPressGesture | √ | × | √ |
| 上下文菜单 | ContentMenu | √ | √ | √ |
| 拖拽 | Drag | √ | √ | √ |
| 轻扫 | SwipeGesture | √ | √ | √ |
| 滚动及平移 | PanGesture | √ | √ | √ |
| 缩放 | PinchGesture | √ | √ | √ |
| 旋转 | RotationGesture | √ | √ | NA |
-  点击事件（onClick）其实是点击手势（TapGesture）的一个特殊场景（单指单次点击）。该场景使用的非常广泛，为了方便开发者使用及符合传统开发习惯，所以专门提供了开发接口。
-  触控板支持长按输入的功能正在开发中。
拖拽事件
拖拽是应用开发中经常碰到的场景。拖拽发生在两个组件之间，它不是简单的单次输入，而是一个”过程”，通常包含如下步骤（以将组件A拖拽到组件B中为例）。
-  长按或点击组件A，触发拖拽。
-  保持按压或点击，持续将组件A向组件B拖拽。
-  抵达组件B中，释放按压点击，完成拖拽。
-  也可以在未抵达组件B的中途，释放按压点击，取消拖拽。
一个完整的拖拽事件，包含多个拖拽子事件，如下表所示（请访问拖拽事件了解详细用法）。当前触控屏和鼠标的拖拽事件已经实现”交互归一”，对手写笔的支持正在开发中。
| 名称 | 功能描述 |
| --- | --- |
| onDragStart | 绑定A组件，触控屏长按/鼠标左键按下后移动触发 |
| onDragEnter | 绑定B组件，触控屏手指、鼠标移动进入B组件瞬间触发 |
| onDragMove | 绑定B组件，触控屏手指、鼠标在B组件内移动触发 |
| onDragLeave | 绑定B组件，触控屏手指、鼠标移动退出B组件瞬间触发 |
| onDrop | 绑定B组件，在B组件内，触控屏手指抬起、鼠标左键松开时触发 |

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/polymorphic-controls-V14
爬取时间: 2025-04-30 04:45:41
来源: Huawei Developer
方舟开发框架不仅提供了多种基础组件（如文本显示、图片显示、按键交互等），并且针对不同类型设备分别进行了适配。同一组件在不同的设备上会呈现出不同的形态（即视觉、交互、动效等可能有差异），称为“多态组件”。开发者在使用多态组件时，无需考虑设备差异，只需关注功能实现即可。
多态组件能力正在逐步补齐中。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/resource-usage-V14
爬取时间: 2025-04-30 04:45:54
来源: Huawei Developer
在页面开发过程中，经常需要用到颜色、字体、间距、图片等资源，在不同的设备或配置中，这些资源的值可能不同。有两种方式处理：
-  应用资源：借助资源文件能力，开发者在应用中自定义资源，自行管理这些资源在不同的设备或配置中的表现。
-  系统资源：开发者直接使用系统预置的资源定义（即分层参数）。
应用资源
资源文件介绍
应用开发中使用的各类自定义资源文件，需要统一存放于应用的resources目录下，便于使用和维护。resources目录包括两大类目录，一类为base目录与限定词目录，另一类为rawfile目录，其基础目录结构如下所示。
base目录默认存在，而限定词目录需要开发者自行创建，其名称可以由一个或多个表征应用场景或设备特征的限定词组合而成。应用使用某资源时，系统会根据当前设备状态优先从相匹配的限定词目录中寻找该资源。只有当resources目录中没有与设备状态匹配的限定词目录，或者在限定词目录中找不到该资源时，才会去base目录中查找。rawfile是原始文件目录，它不会根据设备状态去匹配不同的资源，故不在本文的讨论范文内。
-  请访问声明式开发范式资源文件分类，了解限定词目录的命名规则、创建流程、匹配规则等，本文不展开介绍。
-  没有设备状态匹配的限定词目录，或者在限定词目录中找不到目标资源时，会继续在base目录中查找。强烈建议对于所有应用自定义资源都在base目录中定义默认值，防止出现找不到资源值的异常场景。
-  类Web开发范式的资源文件路径及资源限定词的使用与声明式范式不同，详情请参考类Web开发范式资源限定与访问及类Web开发范式文件组织。
base目录与限定词目录下面可以创建资源组目录（包括element、media等），用于存放特定类型的资源文件。
| 资源组目录 | 目录说明 | 资源文件 |
| --- | --- | --- |
| element | 表示元素资源，以下每一类数据都采用相应的JSON文件来表征。 - boolean，布尔型 - color，颜色 - float，浮点型 - intarray，整型数组 - integer，整型 - pattern，样式 - plural，复数形式 - strarray，字符串数组 - string，字符串 | element目录中的文件名称建议与下面的文件名保持一致。每个文件中只能包含同一类型的数据。 - boolean.json - color.json - float.json - intarray.json - integer.json - pattern.json - plural.json - strarray.json - string.json |
| media | 表示媒体资源，包括图片、音频、视频等非文本格式的文件。 | 文件名可自定义，例如：icon.png。 |
表示元素资源，以下每一类数据都采用相应的JSON文件来表征。
- boolean，布尔型
- color，颜色
- float，浮点型
- intarray，整型数组
- integer，整型
- pattern，样式
- plural，复数形式
- strarray，字符串数组
- string，字符串
element目录中的文件名称建议与下面的文件名保持一致。每个文件中只能包含同一类型的数据。
- boolean.json
- color.json
- float.json
- intarray.json
- integer.json
- pattern.json
- plural.json
- strarray.json
- string.json
在element目录的各个资源文件中，以“name-value”的形式定义资源，如下所示。而在media目录中，直接以文件名作为name，故开发者将文件放入media目录即可，无需再额外定义name。
```json
// color.json
{
"color": [
{
"name": "color_red",
"value": "#ffff0000"
},
{
"name": "color_blue",
"value": "#ff0000ff"
}
]
}
```
访问应用资源
在工程中，通过 "$r('app.type.name')" 的形式引用应用资源。app代表是应用内resources目录中定义的资源；type 代表资源类型（或资源的存放位置），可以取 color、float、string、plural和media，name代表资源命名，由开发者添加资源时确定。
可以查看声明式范式访问应用资源，了解资源访问的更多细节。
示例
在应用的resources目录下，创建名为tablet的限定词子目录，并按照下表所示，在base目录和tablet限定词目录中添加相应的资源。
| 资源名称 | 资源类型 | base目录中资源值 | 限定词目录（tablet）中资源值 |
| --- | --- | --- | --- |
| my_string | string | default | tablet |
| my_color | color | #ff0000 | #0000ff |
| my_float | float | 60vp | 80vp |
| my_image | media | my_image.png（太阳图标） | my_image.png（月亮图标） |
在代码中通过 "$r('app.type.name')" 的形式使用应用资源，并分别在默认设备和平板上查看代码的运行效果，可以发现同一资源在不同设备上的取值不同。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165835.03209303326691045316232077870923:50001231000000:2800:D9B966E92034DFE9C3FCFB38FF85D8DB9AB0B06BBB0F3D39F234CD8D4CA84E29.png)
```typescript
@Entry
@Component
struct Index {
build() {
Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
Text($r("app.string.my_string"))
.fontSize($r("app.float.my_float"))
.fontColor($r("app.color.my_color"))
Image($r("app.media.my_image"))
.width(100)
.height(100)
}
.width('100%')
.height('100%')
}
}
```
系统资源
除了自定义资源，开发者也可以使用系统中预定义的资源（即分层参数，同一资源ID在设备类型、深浅色等不同配置下有不同的取值）。
在开发过程中，分层参数的用法与资源限定词基本一致。开发者可以通过"$r('sys.type.resource_id')"的形式引用系统资源。sys代表是系统资源；type代表资源类型，值可以取color、float、string和media；resource_id代表资源id。
-  仅声明式开发范式支持使用分层参数，类Web开发范式不支持。
-  系统资源可以保证不同团队开发出的应用有较为一致的视觉风格。对于系统预置应用，强烈建议使用系统资源；对于三方应用，可以根据需要选择使用系统资源或自定义应用资源。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/development-intro-V14
爬取时间: 2025-04-30 04:46:08
来源: Huawei Developer
应用开发至少包含两部分工作： UI页面开发和底层功能开发（部分需要联网的应用还会涉及服务端开发）。前面章节介绍了如何解决页面适配的问题，本章节主要介绍应用如何解决设备系统能力差异的兼容问题。
系统能力
系统能力（即SystemCapability，缩写为SysCap）指操作系统中每一个相对独立的特性，如蓝牙，WIFI，NFC，摄像头等，都是系统能力之一。每个系统能力对应多个API，随着目标设备是否支持该系统能力共同存在或消失。
与系统能力相关的，有支持能力集、联想能力集和要求能力集三个核心概念。
多设备应用开发
开发多设备应用时，工程中默认的要求能力集是多个设备支持能力集的交集，默认的联想能力集是多个设备支持能力集的并集。
-  开发者可以在运行时动态判断某设备是否支持特定的系统能力。
-  开发者可以自行修改联想能力集和要求能力集。
动态逻辑判断
如果某个系统能力没有写入应用的要求能力集中，那么在使用前需要判断设备是否支持该系统能力。
-  方法1：canIUse接口帮助开发者来判断该设备是否支持某个特定的syscap。
```typescript
if (canIUse("SystemCapability.Communication.NFC.Core")) {
console.log("该设备支持SystemCapability.Communication.NFC.Core");
} else {
console.log("该设备不支持SystemCapability.Communication.NFC.Core");
}
```
-  方法2：开发者可通过import的方式将模块导入，若当前设备不支持该模块，import的结果为undefined，开发者在使用其API时，需要判断其是否存在。
```typescript
import { nfcController } from '@kit.ConnectivityKit';
try {
nfcController.enableNfc();
console.log("nfcController enableNfc success");
} catch (busiError) {
console.log("nfcController enableNfc busiError: " + busiError);
}
```
配置联想能力集和要求能力集
DevEco Studio会根据创建的工程所支持的设备自动配置联想能力集和要求能力集，同时也支持开发者修改。
```json
// syscap.json
{
"devices": {
"general": [            // 每一个典型设备对应一个syscap支持能力集，可配置多个典型设备
"default",
"tablet"
],
"custom": [             // 厂家自定义设备
{
"某自定义设备": [
"SystemCapability.Communication.SoftBus.Core"
]
}
]
},
"development": {             // addedSysCaps内的sycap集合与devices中配置的各设备支持的syscap集合的并集共同构成联想能力集
"addedSysCaps": [
"SystemCapability.Communication.NFC.Core"
]
},
"production": {              // 用于生成rpcid，慎重添加，可能导致应用无法分发到目标设备上
"addedSysCaps": [],      // devices中配置的各设备支持的syscap集合的交集，添加addedSysCaps集合再除去removedSysCaps集合，共同构成要求能力集
"removedSysCaps": []     // 当该要求能力集为某设备的子集时，应用才可被分发到该设备上
}
}
```
总结
从应用开发到用户使用，通常要经历应用分发和下载、应用安装、应用运行等环节。借助SysCap机制，可以在各个环节中加以拦截或管控，保证应用可以在设备上正常安装和使用。
SysCap机制可以帮助开发者仅关注设备的系统能力，而不用考虑成百上千种具体的设备类型，降低多设备应用开发难度。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/multi-faq-V14
爬取时间: 2025-04-30 04:46:23
来源: Huawei Developer
如何查询设备类型
设备类型分为default（默认设备）、tablet、tv、wearable、2in1等，有多种查询设备类型的方式。
1.  通过命令行的方式查询设备类型。 通过命令行查询指定系统参数（const.product.devicetype）进而确定设备类型。
```shell
# 方法一
hdc shell param get "const.product.devicetype"
# 方法二
hdc shell cat /etc/param/ohos.para | grep const.product.devicetype
```
2.  在应用开发过程中查询设备类型。 通过deviceInfo查询设备类型，deviceInfo中各个字段的含义请参考设备信息。
```typescript
import { deviceInfo } from'@kit.BasicServicesKit'
@Entry
@Component
struct GetDeviceTypeSample {
@State deviceType:string='unknown'
aboutToAppear() {
this.deviceType= deviceInfo.deviceType
}
build() {
Column() {
Text(this.deviceType).fontSize(24)
}
.width('100%')
.height('100%')
}
}
```
3.  通过deviceInfo查询设备类型，deviceInfo中各个字段的含义请参考设备信息。
```typescript
import { deviceInfo } from'@kit.BasicServicesKit'
@Entry
@Component
struct GetDeviceTypeSample {
@State deviceType:string='unknown'
aboutToAppear() {
this.deviceType= deviceInfo.deviceType
}
build() {
Column() {
Text(this.deviceType).fontSize(24)
}
.width('100%')
.height('100%')
}
}
```
-  通过deviceInfo查询设备类型，deviceInfo中各个字段的含义请参考设备信息。
```typescript
import { deviceInfo } from'@kit.BasicServicesKit'
@Entry
@Component
struct GetDeviceTypeSample {
@State deviceType:string='unknown'
aboutToAppear() {
this.deviceType= deviceInfo.deviceType
}
build() {
Column() {
Text(this.deviceType).fontSize(24)
}
.width('100%')
.height('100%')
}
}
```
如何在不同设备上为Ability配置不同的启动模式
应用由一个或多个Ability组成，Ability支持单实例、多实例和指定实例3种启动模式，启动模式可以在配置文件（module.json5）中通过launchType字段配置。启动模式对应Ability被启动时的行为，对启动模式的详细说明如下：
| 启动模式 | 描述 | 说明 |
| --- | --- | --- |
| multiton | 多实例 | 每次startAbility都会启动一个新的实例。 |
| singleton | 单实例 | 系统中最多只可以存在一个实例，startAbility时，如果系统中已存在相应的Ability实例，则复用该实例。 |
| specified | 指定实例 | 运行时由Ability内部业务决定是否创建多实例。 |
默认设备屏幕尺寸较小，采用multiton启动模式不仅无法给用户提供便利，反而可能消耗更多系统资源，故通常采用singleton启动模式。平板屏幕尺寸较大且可能支持自由窗口，对于文档编辑、网页浏览等场景，使用multiton启动模式可以提升用户体验。
本文中将默认设备和平板等归为同一泛类，推荐同一泛类的设备共用HAP，同时本文也介绍了如何通过自适应布局能力和响应式布局能力开发出适配不同设备的页面。这里将补充介绍，如何实现Ability在不同设备上以不同的模式启动。
launchType字段配置为specified时，系统会根据AbilityStage的onAcceptWant的返回值确定是否创建新的实例。对于同一个应用，如果key已经存在，则复用该key对应的Ability，如果key不存在则新创建Ability。
可以将配置文件中的launchType字段配置为specified，同时在应用中加入如下代码以实现目标效果。
-  非平板设备，直接将设备类型作为key，保证每次启动的key相同，即以单实例模式运行。
-  平板设备，将设备类型与毫秒级时间戳叠加作为key，保证每次启动的key不同，即以多实例模式运行。
```typescript
// MyAbilityStage.ts
import { AbilityStage, Want } from "@kit.AbilityKit"
import { deviceInfo } from'@kit.BasicServicesKit'
export default class MyAbilityStage extends AbilityStage {
//...
private generateKey(): string {
// 如果是平板，则将设备类型和毫秒级时间戳叠加作为key，保证每次启动的key都不同
if (deviceInfo.deviceType === 'tablet') {
return deviceInfo.deviceType + (new Date()).valueOf()
}
// 如果不是平板，直接以设备类型作为key，每次启动的key相同
return deviceInfo.deviceType
}
onAcceptWant(want: Want) : string{
return this.generateKey()
}
}
```
如何开启自由窗口
自由窗口功能默认是关闭的，可以通过如下方式开启自由窗口功能。
```shell
# 取出窗口配置文件，并将文件中的<decor enable="false"></decor>修改为<decor enable="true"></decor>
hdc file recv system/etc/window/resources/window_manager_config.xml ./
# 以可读写的模式重新挂载根目录，并更新配置文件
hdc shell mount -o rw,remount /
hdc file send window_manager_config.xml system/etc/window/resources/window_manager_config.xml
# 重启设备，配置生效
hdc shell reboot
```
屏幕较小，通过手指操作窗口较为不便时，建议外接鼠标进行操作。
-  鼠标在应用顶部悬停，即可召唤出窗口工具栏。
-  点击窗口工具栏中的缩放按钮（从左到右第二个），即可让应用以自由窗口的模式显示。
-  在自由窗口模式下，可以通过拖动应用窗口的边框或顶角，改变窗口尺寸同时触发应用显示刷新。 在调整窗口尺寸的过程中，窗口尺寸可能超出屏幕尺寸。此时应用显示正常，但受限于屏幕尺寸，在屏幕中只能看到应用部分区域的显示。可以通过移动窗口位置，查看应用其它区域的显示。
| 窗口操作按钮 | 悬浮窗口显示 | 调整窗口尺寸及位置查看不同的效果 |
| --- | --- | --- |
|  |  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165836.23206587827396387365967759676677:50001231000000:2800:39FDF597B58A28869DF04333D5425A2D52C9AD3CADD6A5D3002C06F8ACF2163B.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165836.29288514032683216021488328524505:50001231000000:2800:19EED8E7BC34903D2FE84F4F2E812EA6C26E787EA548AFEF877BC678E8B7442F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165836.22185658822028817322614328048537:50001231000000:2800:62CF54C7FED2E56779D9E16EC68C2D8723BFF3DF1327BEDA277DC9DAAE15A31D.png)
如何限制自由窗口的尺寸调节范围
自适应布局可以保证窗口尺寸在一定范围内变化时，页面的显示是正常的。当窗口尺寸变化较大时，就需要额外借助响应式布局能力（如断点等）调整页面结构以保证显示正常。通常每个断点都需要开发者精心适配以获得最佳的显示效果，考虑到设计及开发成本等实际因素的限制，应用不可能适配从零到正无穷的所有窗口宽度。
不同设备或不同设备状态，系统默认的自由窗口尺寸的调节范围可能不同。开发者可以在应用配置文件中限制应用中各个Ability的自由窗口尺寸调节范围，配置文件中影响自由窗口尺寸调节范围的字段如下表所示。
| 配置文件字段 | 数据类型 | 描述 |
| --- | --- | --- |
| minWindowWidth | 数值 | 标识该ability支持的最小的窗口宽度, 宽度单位为vp。 |
| minWindowHeight | 数值 | 标识该ability支持的最小的窗口高度, 高度单位为vp。 |
| maxWindowWidth | 数值 | 标识该ability支持的最大的窗口宽度，宽度单位为vp。 |
| maxWindowHeight | 数值 | 标识该ability支持的最大的窗口高度, 高度单位为vp。 |
| minWindowRatio | 数值 | 标识该ability支持的最小的宽高比。 |
| maxWindowRatio | 数值 | 标识该ability支持的最大的宽高比。 |
如下所示，通过配置文件分别限制自由窗口的最大和最小尺寸。
```json
{
"module": {
//...
"abilities": [
{
//...
"minWindowWidth": 320,
"minWindowHeight": 240,
"maxWindowWidth": 1440,
"maxWindowHeight": 900,
"minWindowRatio": 0.5,
"maxWindowRatio": 2,
}
]
}
}
```
如何获取组件的尺寸
实际开发过程中，开发者可能有获取页面中某个组件或某块区域的尺寸的诉求，以便通过手动计算等进行更精确的布局计算及优化。
开发者可以通过组件区域变化事件（即组件显示的尺寸、位置等发生变化时触发的事件）来获取指定组件的尺寸。
如下所示，通过onAreaChange事件获取Row组件（页面中白色区域）的尺寸。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165836.60415531745793901515731256788674:50001231000000:2800:6DD017164FE0A343FDFE5E4A4F63572F2936CFE9C8F7CC818794CED2F3502EE6.gif)
```typescript
@Entry
@Component
struct OnAreaChangeSample {
@State rate: number = 0.8
@State info: string = ''
// 底部滑块，可以通过拖拽滑块改变容器尺寸
@Builder slider() {
Slider({ value: this.rate * 100, min: 30, max: 80, style: SliderStyle.OutSet })
.blockColor(Color.White)
.width('60%')
.onChange((value: number) => {
this.rate = value / 100;
})
.position({ x: '20%', y: '80%' })
}
build() {
Column() {
Column() {
Row() {
Text(this.info).fontSize(20).lineHeight(22)
}
.borderRadius(12)
.padding(24)
.backgroundColor('#FFFFFF')
.width(this.rate * 100 + '%')
.onAreaChange((oldValue: Area, newValue: Area) => {
this.info = JSON.stringify(newValue)
})
}
this.slider()
}
.width('100%')
.height('100%')
.backgroundColor('#F1F3F5')
.justifyContent(FlexAlign.Center)
}
}
```
如何解决顶部单张大图问题
解决方案
顶部背景图被拉伸时，可以通过设置背景图片的backgroundImageSize属性，使得图片大小能够合理显示，达到适配效果。
布局效果
| sm | md |
| --- | --- |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165836.81591705683169560389216689991601:50001231000000:2800:2DA9E5274E18A6785CE076E5D0B7B026119BD2D9997357300F0C9F3E320197AF.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165836.93616940133431669218039163931853:50001231000000:2800:6797545402C7E5D7E9423B7C03587C255A58EA59D006910128DCC21C2ECE6835.png)
参考代码
```typescript
@Entry
@Component
struct ImageClip {
build() {
// 设置背景图片的backgroundImageSize属性，使得图片大小能够合理显示
Column()
.width('100%')
.height(300)
.backgroundColor('#ccc')
.backgroundImage($r('app.media.ImageOne'))
.backgroundImageSize(ImageSize.Cover)
.backgroundImagePosition(Alignment.Center)
}
}
```
如何解决Item内容过大
解决方案
在大屏上，Listitem内容会过大，页面整体浏览内容减少。可通过以下两种方法解决：
布局效果
| sm | md |
| --- | --- |
| 展示1列 | 展示2列 |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165836.56850181652280242908482237511078:50001231000000:2800:9676CC711740ADD0681E6B561E717DF3C14971670F46934CC1F6EAD8C2353498.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.02334373795287027615432444122784:50001231000000:2800:077AFF6987C174B49DF33AB8EEEFC1D730B4F51A11CBCAE43DA75C7D13687970.png)
参考代码
```typescript
@Entry
@Component
struct ListLayout {
@State data: Resource[] = new Array(5).fill($r("app.media.image"))
@State breakPoint: string = 'sm'
build() {
GridRow() {
GridCol({ span: { sm: 12, md: 12, lg: 12 } }) {
List({ space: 24 }) {
ForEach(this.data, (item: Resource) => {
ListItem() {
Image(item).margin({ left: 12, right: 12 })
}
})
}
// 设置列最小宽度和最大宽度
.lanes({ minLength: 300, maxLength: 360 }).padding(12)
}
}.onBreakpointChange((breakpoint: string) => {
this.breakPoint = breakpoint
})
}
}
```
```typescript
List() {
// ...
}
// 根据断点设置List列数
.lanes(this.breakPoint === 'sm' ? 1 : 2)
```
如何解决Banner图片过大
解决方案
在大屏上，Swiper图片显示内容过大，可以通过增加Swiper展示图片数来调整图片显示大小。外层可以使用栅格组件GridRow，通过调用OnBreakpointChange事件，调整不同的断点下Swiper的前后边距，实现在不同屏幕尺寸上的显示不同Swiper图片数。
布局效果
| sm | md |
| --- | --- |
| 展示一个内容项 | 展示一个完整的内容项 + 左右相邻的部分内容项 |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.78992492974161287995662492593898:50001231000000:2800:55A86CB2421F8132F7C069B7F771F9ED88434AF6A1AB2E5C8299EBB9B92AF0BB.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.72561200656040916458109571393342:50001231000000:2800:3573CAB91CEB9AC2797B6DEF698858EC8215870E19656AB88481E0E795152698.png)
参考代码
```typescript
@Entry
@Component
struct SwiperLayout {
@State data: Resource[] = new Array(5).fill($r("app.media.sky"))
@State breakPoint: string = 'sm'
build() {
Row() {
GridRow() {
GridCol({ span: { sm: 12, md: 12, lg: 12 } }) {
Swiper() {
ForEach(this.data, (item: Resource) => {
Image(item).width('100%').height(180)
})
}
.width('100%')
.itemSpace(24)
// 根据断点设置Swiper前后边距
.prevMargin(this.breakPoint === 'sm' ? 0 : 100)
.nextMargin(this.breakPoint === 'sm' ? 0 : 100)
}
}.onBreakpointChange((breakpoint: string) => {
this.breakPoint = breakpoint
})
.height("60%")
.borderWidth(2)
}
}
}
```
如何解决信息流图片过大
解决方案
针对信息流单张图片过大的情况，设置aspectRatio和constrainSize属性，可以通过对图片的布局和尺寸进行约束，达到适配效果。
布局效果
| sm | md |
| --- | --- |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.91373603175789815947448722918896:50001231000000:2800:5C02FC31817598E95A4324B646B700ADF0E039FAB13784063E4D295830591B2F.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.71747204372936910202284828101293:50001231000000:2800:2DFD1E13E04D96C6C953DBE269C8A4567C9B1E0B5D1A384D8C539B92C3C6A648.png)
参考代码
```typescript
@Entry
@Component
struct ImageConstrainSize {
@State breakPoint: string = 'sm'
build() {
GridRow(){
GridCol({ span: { sm: 12, md: 12, lg: 12 } }){
Column(){
Text('一次开发，多端部署，让开发者可以基于一种设计，高效构建多端可运行的应用。一次开发，多端部署，让开发者可以基于一种设计，高效构建多端可运行的应用。')
// 设置aspectRatio和constrainSize属性，可以对图片的布局和尺寸进行约束
Image($r('app.media.ImageTwo'))
.width('30%')
.aspectRatio(0.5)
.constraintSize({ maxWidth: 240, minWidth: 180 })
Text('一次开发，多端部署，让开发者可以基于一种设计，高效构建多端可运行的应用。一次开发，多端部署，让开发者可以基于一种设计，高效构建多端可运行的应用。')
}.alignItems(HorizontalAlign.Start)
}
}.onBreakpointChange((breakpoint: string) => {
this.breakPoint = breakpoint
})
}
}
```
如何解决信息流_4宫格图片过大
解决方案
在大屏上，Grid组件里的4宫格图片大小过大，页面浏览区域变少。可以借助栅格行组件GridRow来调整不同的断点下Grid的宽度，解决大屏上Grid组件4宫格图片过大的问题。
布局效果
| sm | md |
| --- | --- |
| 宽度占满屏幕 | 宽度占屏幕的60% |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.74116603309496315485675590698028:50001231000000:2800:173771A447F81DC2B656BF5C9FF84208186BEEF52C6EF90698FDFE33330BA11E.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.20968039396142870751227808075660:50001231000000:2800:B47BC24D72A2DF376D836EBEC5AEA9CC2F2826A004966421E1EFF8C91E914104.png)
参考代码
```typescript
@Entry
@Component
struct GridLayout {
@State data: Resource[] = new Array(4).fill($r("app.media.image"))
@State breakPoint: string = 'sm'
build() {
GridRow() {
GridCol({ span: { sm: 12, md: 12, lg: 12 } }) {
Column() {
Text('一次开发，多端部署，让开发者可以基于一种设计，高效构建多端可运行的应用。')
Grid() {
ForEach(this.data, (item: Resource) => {
GridItem() {
Image(item).width('100%').aspectRatio(1)
}
})
}.columnsTemplate('1fr 1fr')
.columnsGap(24)
.rowsGap(24)
// 根据断点设置Grid宽度
.width(this.breakPoint === 'md' ? '60%' : '100%')
}.width('100%').alignItems(HorizontalAlign.Start)
}
}.onBreakpointChange((breakpoint: string) => {
this.breakPoint = breakpoint
})
}
}
```
如何解决信息流_9宫格图片过大
解决方案
在大屏上，Grid组件里的9宫格图片大小过大，页面整体浏览内容减少，可以设置Grid组件宽度和宽高比，使Grid组件保持固定大小，不会随着屏幕尺寸变化而变化。
布局效果
| sm | md |
| --- | --- |
| 图片宽高不变 | 图片宽高不变 |
|  |  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.79002593664853565194737617410136:50001231000000:2800:2E9BEBC865716123AD72C723D01BEC5D8A0AAED800850B46319D3D237DEA5C02.png)
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314165837.25056786890429554681780592763296:50001231000000:2800:8E114240BFA75023EC1FD2A7B685DE68BCEEB8CC302C641A6EC3223C3028E775.png)
参考代码
```typescript
@Entry
@Component
struct GridWidth {
@State data: Resource[] = new Array(9).fill($r("app.media.sky"))
build() {
Column() {
Text('一次开发，多端部署，让开发者可以基于一种设计，高效构建多端可运行的应用。')
Grid() {
ForEach(this.data, (item: Resource) => {
GridItem() {
Image(item).width('100%').aspectRatio(1)
}
})
}
.columnsTemplate('1fr 1fr 1fr')
.columnsGap(12)
.rowsGap(12)
// 设置固定宽度和宽高比
.width(360)
.aspectRatio(1)
.padding(12)
}
.alignItems(HorizontalAlign.Start)
}
}
```

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/multi-cases-V14
爬取时间: 2025-04-30 04:46:36
来源: Huawei Developer
案例应用阐述了从应用设计到开发这一过程中如何实践前面章节介绍的设计思路或“一多”能力，让读者可以整体掌握“一多”在应用开发过程中的知识。
还请参考以下案例进行开发。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-overview-V14
爬取时间: 2025-04-30 04:46:50
来源: Huawei Developer
场景介绍
随着全场景多设备的生活方式不断深入，用户拥有的设备越来越多，不同设备都能在适合的场景下提供良好的体验，例如手表可以提供及时的信息查看能力，电视可以带来沉浸的观影体验。但是，每个设备也有使用场景的局限，例如在电视上输入文本相对移动设备来说是非常糟糕的体验。当多个设备通过分布式操作系统能够相互感知、进而整合成一个超级终端时，设备与设备之间就可以取长补短、相互帮助，为用户提供更加自然流畅的分布式体验。
在HarmonyOS中，将跨多设备的分布式操作统称为流转；根据使用场景的不同，流转又分为跨端迁移和多端协同两种具体场景。
基本概念
-  流转 在HarmonyOS中泛指跨多设备的分布式操作。流转能力打破设备界限，多设备联动，使用户应用程序可分可合、可流转，实现如邮件跨设备编辑、多设备协同健身、多屏游戏等分布式业务。流转为开发者提供更广的使用场景和更新的产品视角，强化产品优势，实现体验升级。流转按照使用场景可分为跨端迁移和多端协同。
-  跨端迁移 在用户使用设备的过程中，当使用情境发生变化时（例如从室内走到户外或者周围有更合适的设备等），之前使用的设备可能已经不适合继续当前的任务，此时，用户可以选择新的设备来继续当前的任务，原设备可按需决定是否退出任务，这就是跨端迁移场景。 常见的跨端迁移场景实例：在平板上播放的视频，迁移到智慧屏继续播放，从而获得更佳的观看体验；平板上的视频应用退出。 在应用开发层面，跨端迁移指在A端运行的UIAbility迁移到B端上，完成迁移后，B端UIAbility继续任务，而A端UIAbility可按需决定是否退出。
-  多端协同 用户拥有的多个设备，可以作为一个整体，为用户提供比单设备更加高效、沉浸的体验，这就是多端协同场景。 常见的多端协同场景实例： 场景一：两台设备A和B打开备忘录同一篇笔记进行双端协同编辑，在设备A上可以使用本地图库中的图片资源插入编辑，设备B上进行文字内容编辑。 场景二：设备A上正在和客户进行聊天，客户需要的资料在设备B上，可以通过聊天软件打开设备B上的文档应用选择到想要的资料回传到设备A上，然后通过聊天软件发送给客户。 在应用开发层面，多端协同指多端上的不同UIAbility/ServiceExtensionAbility同时运行、或者交替运行实现完整的业务；或者多端上的相同UIAbility/ServiceExtensionAbility同时运行实现完整的业务。
典型场景

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-continuation-V14
爬取时间: 2025-04-30 04:47:03
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-continuation-overview-V14
爬取时间: 2025-04-30 04:47:17
来源: Huawei Developer
应用接续，指当用户在一个设备上操作某个应用时，可以在另一个设备的同一个应用中快速切换，并无缝衔接上一个设备的应用体验。
比如在用户使用过程中，使用情景发生了变化，之前使用的设备不再适合继续当前任务，或者周围有更合适的设备，此时用户可以选择使用新的设备来继续当前的任务。接续完成后，之前设备的应用可退出或保留，用户可以将注意力集中在被拉起的设备上，继续执行任务。
如图所示，在手机上编辑备忘录，到办公室后切换到平板上继续编辑，完成任务的无缝衔接。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170539.54042082626577094892758197706923:50001231000000:2800:5E6802D3E181DB8BC803F23EC7FC7FCBFDE64C974B09B84E70A59D6EBE8BFB7D.gif)
运作机制
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170539.80370021183002929073712677377670:50001231000000:2800:6FFA83B7EAA1BD65FA113CCEE4BF754616D1AA5C6845A5F4E01FAF2AC769BAC9.png)
1.  例如，浏览器应用完成应用接续，在源端浏览一个页面，到对端继续浏览。系统将自动保存页面状态，如当前页面的浏览进度；开发者需要通过onContinue接口保存页面url等业务内容。
发起接续的场景
针对不同类型的应用，推荐的应用接续发起的界面及接续同步内容如下：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/app-continuation-guide-V14
爬取时间: 2025-04-30 04:47:30
来源: Huawei Developer
通过应用接续，可以实现将应用当前任务（包括页面控件状态变量等）迁移到目标设备，并在目标设备上接续使用。
可以实现的功能包括：
-  支持应用根据实际使用场景动态设置迁移状态（默认迁移状态为ACTIVE激活状态）。 如编辑类应用在编辑文本的页面下才需要迁移，其他页面不需要迁移，则可以通过setMissionContinueState进行控制。
-  支持应用动态选择是否进行页面栈恢复（默认进行页面栈信息恢复）。 如应用希望自定义迁移到其他设备后显示的页面，则可以通过wantConstant.Params进行控制。
-  支持应用动态选择流转成功后是否退出迁移源端应用（默认流转成功后退出迁移源端应用）。则可以通过@ohos.app.ability.wantConstant (wantConstant)进行控制。
约束与限制
需同时满足以下条件，才能使用该功能：
-  HarmonyOS NEXT Developer Preview0及以上版本的设备。
-  条件允许时，建议双端设备接入同一个局域网，可提升数据传输的速度。
-  条件允许时，建议双端设备接入同一个局域网，可提升数据传输的速度。
-  条件允许时，建议双端设备接入同一个局域网，可提升数据传输的速度。
接口说明
以下为实现应用接续的主要接口，详细的接口说明可查阅参考文档。
| 接口名  | 描述  |
| --- | --- |
| onContinue(wantParam : {[key: string]: Object}): OnContinueResult  | 接续源端在该回调中保存迁移所需要的数据，同时返回是否同意迁移： AGREE：表示同意。REJECT：表示拒绝，如应用在onContinue中异常可以直接REJECT。MISMATCH：表示版本不匹配，接续源端应用可以在onContinue中获取到迁移对端应用的版本号，进行协商后，如果版本不匹配导致无法迁移，可以返回该错误。  |
| onCreate(want: Want, param: AbilityConstant.LaunchParam): void;  | 接续目的端为冷启动或多实例应用热启动时，在该回调中完成数据恢复，并触发页面恢复。  |
| onNewWant(want: Want, launchParams: AbilityConstant.LaunchParam): void;  | 接续目的端为单实例应用热启动时，在该回调中完成数据恢复，并触发页面恢复。  |
接口名
描述
onContinue(wantParam : {[key: string]: Object}): OnContinueResult
接续源端在该回调中保存迁移所需要的数据，同时返回是否同意迁移：
onCreate(want: Want, param: AbilityConstant.LaunchParam): void;
接续目的端为冷启动或多实例应用热启动时，在该回调中完成数据恢复，并触发页面恢复。
onNewWant(want: Want, launchParams: AbilityConstant.LaunchParam): void;
接续目的端为单实例应用热启动时，在该回调中完成数据恢复，并触发页面恢复。
开发步骤
1.  在module.json5文件的abilities中，将continuable标签配置为“true”，表示该UIAbility可被迁移。配置为false的UIAbility将被系统识别为无法迁移且该配置默认值为false。
```json
{
"module": {
...
"abilities": [
{
...
"continuable": true,
}
]
}
}
```
2.  当应用触发迁移时，onContinue()接口在源端被调用，开发者可以在该接口中保存迁移数据，实现应用兼容性检测，决定是否支持此次迁移。 如果迁移过程中的兼容性问题对于应用迁移体验影响较小或无影响，可以跳过该步骤。 onContinue()接口传入的wantParam参数中，有部分字段由系统预置，开发者可以使用这些字段用于业务处理。同时，应用在保存自己的wantParam参数时，也应注意不要使用同样的key值，避免被系统覆盖导致数据获取异常。详见下表： 字段 含义 version 对端应用的版本号 targetDevice 对端设备的networkId
```typescript
import { AbilityConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { promptAction } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
onContinue(wantParam: Record<string, Object>) {
let targetVersion  = wantParam.version;  // 获取迁移对端应用的版本号
// 应用可根据源端版本号设置支持接续的最小兼容版本号，源端版本号可从app.json5文件中的versionCode字段获取；防止目标端版本号过低导致不兼容。
let versionThreshold: number = 0; // 替换为应用自己支持兼容的最小版本号
// 兼容性校验
if (targetVersion < versionThreshold) {
// 建议在校验版本兼容性失败后，提示用户拒绝迁移的原因
promptAction.showToast({
message: '目标端应用版本号过低，不支持接续，请您升级应用版本后再试',
duration: 2000
})
// 在兼容性校验不通过时返回MISMATCH
return AbilityConstant.OnContinueResult.MISMATCH;
}
console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`)
// 迁移数据保存
let continueInput = '迁移的数据';
if (continueInput) {
// 将要迁移的数据保存在wantParam的自定义字段（如：data）中;
wantParam["data"] = continueInput;
}
return AbilityConstant.OnContinueResult.AGREE;
}
}
```
3.  如果迁移过程中的兼容性问题对于应用迁移体验影响较小或无影响，可以跳过该步骤。
4.  onContinue()接口传入的wantParam参数中，有部分字段由系统预置，开发者可以使用这些字段用于业务处理。同时，应用在保存自己的wantParam参数时，也应注意不要使用同样的key值，避免被系统覆盖导致数据获取异常。详见下表： 字段 含义 version 对端应用的版本号 targetDevice 对端设备的networkId
5.  不同情况下的函数调用如下图所示： 目的端设备上，在onCreate中根据launchReason判断该次启动是否为迁移LaunchReason.CONTINUATION。 开发者可以从want中获取保存的迁移数据。 若开发者使用系统页面栈恢复功能，则需要在onCreate()/onNewWant()执行完成前，调用restoreWindowStage()，来触发带有页面栈的页面恢复，如果不需要迁移页面栈可以参考按需迁移页面栈部分。 接口restoreWindowStage(this.storage)必须在同步接口方法中执行，如果在异步回调中执行，可能会导致应用迁移后页面加载失败。 在onNewWant()中判断迁移场景，恢复数据，并触发页面恢复
6.  目的端设备上，在onCreate中根据launchReason判断该次启动是否为迁移LaunchReason.CONTINUATION。 开发者可以从want中获取保存的迁移数据。 若开发者使用系统页面栈恢复功能，则需要在onCreate()/onNewWant()执行完成前，调用restoreWindowStage()，来触发带有页面栈的页面恢复，如果不需要迁移页面栈可以参考按需迁移页面栈部分。 接口restoreWindowStage(this.storage)必须在同步接口方法中执行，如果在异步回调中执行，可能会导致应用迁移后页面加载失败。
7.  目的端设备上，在onCreate中根据launchReason判断该次启动是否为迁移LaunchReason.CONTINUATION。
8.  开发者可以从want中获取保存的迁移数据。
9.  若开发者使用系统页面栈恢复功能，则需要在onCreate()/onNewWant()执行完成前，调用restoreWindowStage()，来触发带有页面栈的页面恢复，如果不需要迁移页面栈可以参考按需迁移页面栈部分。
10.  在onNewWant()中判断迁移场景，恢复数据，并触发页面恢复
1.  如果迁移过程中的兼容性问题对于应用迁移体验影响较小或无影响，可以跳过该步骤。
-  onContinue()接口传入的wantParam参数中，有部分字段由系统预置，开发者可以使用这些字段用于业务处理。同时，应用在保存自己的wantParam参数时，也应注意不要使用同样的key值，避免被系统覆盖导致数据获取异常。详见下表： 字段 含义 version 对端应用的版本号 targetDevice 对端设备的networkId
| 字段  | 含义  |
| --- | --- |
| version  | 对端应用的版本号  |
| targetDevice  | 对端设备的networkId  |
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170539.16339368586270126317158236310263:50001231000000:2800:D6D1CF7D21DADB7F124AF8062C380D21E2F2ED90010E976C0DF4271CC573C8EB.png)
-  目的端设备上，在onCreate中根据launchReason判断该次启动是否为迁移LaunchReason.CONTINUATION。 开发者可以从want中获取保存的迁移数据。 若开发者使用系统页面栈恢复功能，则需要在onCreate()/onNewWant()执行完成前，调用restoreWindowStage()，来触发带有页面栈的页面恢复，如果不需要迁移页面栈可以参考按需迁移页面栈部分。 接口restoreWindowStage(this.storage)必须在同步接口方法中执行，如果在异步回调中执行，可能会导致应用迁移后页面加载失败。
-  目的端设备上，在onCreate中根据launchReason判断该次启动是否为迁移LaunchReason.CONTINUATION。
-  开发者可以从want中获取保存的迁移数据。
-  若开发者使用系统页面栈恢复功能，则需要在onCreate()/onNewWant()执行完成前，调用restoreWindowStage()，来触发带有页面栈的页面恢复，如果不需要迁移页面栈可以参考按需迁移页面栈部分。
-  在onNewWant()中判断迁移场景，恢复数据，并触发页面恢复
-  目的端设备上，在onCreate中根据launchReason判断该次启动是否为迁移LaunchReason.CONTINUATION。
-  开发者可以从want中获取保存的迁移数据。
-  若开发者使用系统页面栈恢复功能，则需要在onCreate()/onNewWant()执行完成前，调用restoreWindowStage()，来触发带有页面栈的页面恢复，如果不需要迁移页面栈可以参考按需迁移页面栈部分。
迁移功能可选配置
动态配置迁移能力
从API version 10起，提供了支持动态配置迁移能力的功能。即应用可以根据实际使用场景，在需要迁移功能时，设置开启应用迁移能力；在业务不需要迁移时，则可以关闭迁移能力。开发者可以通过调用setMissionContinueState接口对迁移能力进行设置。
| 接口状态值  | 含义  |
| --- | --- |
| AbilityConstant.ContinueState.ACTIVE  | 应用当前可迁移能力开启  |
| AbilityConstant.ContinueState.INACTIVE  | 应用当前可迁移能力关闭  |
接口状态值
含义
AbilityConstant.ContinueState.ACTIVE
应用当前可迁移能力开启
AbilityConstant.ContinueState.INACTIVE
应用当前可迁移能力关闭
设置迁移能力的时机
默认状态下，应用的迁移能力为ACTIVE状态，即可以迁移。
如果需要实现某些特殊场景，比如只在具体某个页面下支持迁移，或者只在某个事件发生时才支持迁移，可以按照如下步骤进行配置。
```typescript
// PageName.ets
import { AbilityConstant, common } from '@kit.AbilityKit';
@Entry
@Component
struct PageName {
private context = getContext(this) as common.UIAbilityContext;
build() {
// ...
}
// ...
onPageShow(){
// 进入该页面时，将应用设置为可迁移状态
this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
console.info('setMissionContinueState ACTIVE result: ', JSON.stringify(result));
});
}
}
```
```typescript
// PageName.ets
import { AbilityConstant, common } from '@kit.AbilityKit';
@Entry
@Component
struct PageName {
private context = getContext(this) as common.UIAbilityContext;
build() {
// ...
Button() {
//...
}.onClick(()=>{
//点击该按钮时，将应用设置为可迁移状态
this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
console.info('setMissionContinueState ACTIVE result: ', JSON.stringify(result));
});
})
}
}
```
保证迁移连续性
由于迁移加载时，目标端拉起的应用可能执行过自己的迁移状态设置命令（如：冷启动时目标端在onCreate中设置了INACTIVE；热启动时对端已打开了不可迁移的页面，迁移状态为INACTIVE等情况）。为了保证迁移过后的应用依然具有可以迁移回源端的能力，应在onCreate和onNewWant的迁移调用判断中，将迁移状态设置为ACTIVE。
按需迁移页面栈
支持应用动态选择是否进行页面栈恢复（默认进行页面栈信息恢复）。如果应用不想使用系统默认恢复的页面栈，则可以设置不进行页面栈迁移，而需要在onWindowStageRestore设置迁移后进入的页面，参数定义见SUPPORT_CONTINUE_PAGE_STACK_KEY。
应用在源端的页面栈中存在Index和Second路由，而在目标端恢复时不需要按照源端页面栈进行恢复，需要恢复到指定页面。
示例：应用迁移不需要自动迁移页面栈信息
```typescript
// EntryAbility.ets
import { AbilityConstant, UIAbility, wantConstant } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
// ...
onContinue(wantParam: Record<string, Object>) {
console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`);
wantParam[wantConstant.Params.SUPPORT_CONTINUE_PAGE_STACK_KEY] = false;
return AbilityConstant.OnContinueResult.AGREE;
}
// ...
onWindowStageRestore(windowStage: window.WindowStage) {
// 若不需要自动迁移页面栈信息，则需要在此处设置应用迁移后进入的页面
windowStage.loadContent('pages/Index', (err, data) => {
if (err.code) {
console.info('Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
return;
}
console.info('Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
});
}
}
```
按需退出
支持应用动态选择迁移成功后是否退出迁移源端应用（默认迁移成功后退出迁移源端应用）。如果应用不想让系统自动退出迁移源端应用，则可以设置不退出，参数定义见SUPPORT_CONTINUE_SOURCE_EXIT_KEY。
示例：应用迁移设置不需要迁移成功后退出迁移源端应用
```typescript
import { AbilityConstant, UIAbility, wantConstant } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
// ...
onContinue(wantParam: Record<string, Object>) {
console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`);
wantParam[wantConstant.Params.SUPPORT_CONTINUE_SOURCE_EXIT_KEY] = false;
return AbilityConstant.OnContinueResult.AGREE;
}
// ...
}
```
支持同应用中不同Ability跨端迁移
一般情况下，跨端迁移的双端是同Ability之间，但有些应用在不同设备类型下的同一个业务Ability名称不同（即异Ability），为了支持该场景下的两个Ability之间能够完成迁移，可以通过在module.json5文件的abilities标签中配置迁移类型continueType进行关联。 需要迁移的两个Ability的continueType字段取值必须保持一致，示例如下：
快速启动目标应用
默认情况下，发起迁移后不会立即拉起对端的目标应用，而是等待迁移数据从源端传输到对端后才会拉起应用。若应用希望在用户发起接续后立即被拉起，减少等待时间，提升体验，可以在module.json5文件的continueType标签中添加“_ContinueQuickStart”后缀，配置快速启动目标应用能力。示例如下：
配置了快速拉起的应用，在用户发起接续时会立即收到一次launchReason为提前拉起（PREPARE_CONTINUATION）的onCreate()/onNewWant()请求，随后再收到一次launchReason为接续拉起（CONTINUATION）的onNewWant()请求。如下所示：
| 场景  | 生命周期函数  | launchParam.launchReason  |
| --- | --- | --- |
| 第一次启动请求  | onCreate (冷启动) 或 onNewWant (热启动)  | AbilityConstant.LaunchReason.PREPARE_CONTINUATION  |
| 第二次启动请求  | onNewWant  | AbilityConstant.LaunchReason.CONTINUATION  |
场景
生命周期函数
launchParam.launchReason
第一次启动请求
onCreate (冷启动)
或 onNewWant (热启动)
AbilityConstant.LaunchReason.PREPARE_CONTINUATION
第二次启动请求
onNewWant
AbilityConstant.LaunchReason.CONTINUATION
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170540.73189237793168890498615327292292:50001231000000:2800:5A7C83EF942A92B57A742FA9288E4E0E53CFA53F93E480D484C4CCB43EFAE3E0.png)
如果没有配置快速拉起，则触发迁移时只会收到一次启动请求：
| 场景  | 生命周期函数  | launchParam.launchReason  |
| --- | --- | --- |
| 一次启动请求  | onCreate (冷启动) 或 onNewWant (热启动)  | AbilityConstant.LaunchReason.CONTINUATION  |
场景
生命周期函数
launchParam.launchReason
一次启动请求
onCreate (冷启动)
或 onNewWant (热启动)
AbilityConstant.LaunchReason.CONTINUATION
配置快速拉起后，对应的 onCreate()/onNewWant() 接口实现可参考如下示例：
使用分布式数据对象迁移数据
当需要迁移的数据较大（100KB以上）或需要迁移文件时，可以使用分布式数据对象。原理与接口说明详见分布式数据对象跨设备数据同步。
自API 12起，由于直接使用跨设备文件访问实现文件的迁移，难以获取文件同步完成的时间。为了保证更高的成功率，文件的迁移不建议继续通过该方式实现，推荐使用分布式数据对象携带资产的方式。开发者此前通过跨设备文件访问实现的文件迁移依然生效。
申请权限
基础数据迁移
使用分布式数据对象，与上述开发步骤类似，需要在源端onContinue()接口中进行数据保存，并在对端的onCreate()/onNewWant()接口中进行数据恢复。
1.  示例代码如下：
2.  示例代码如下：
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { distributedDataObject } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '[MigrationAbility]';
const DOMAIN_NUMBER: number = 0xFF00;
// 示例数据对象定义与上同
export default class MigrationAbility extends UIAbility {
d_object?: distributedDataObject.DataObject;
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
// ...
// 调用封装好的分布式数据对象处理函数
this.handleDistributedData(want);
}
}
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
if (want.parameters !== undefined) {
// ...
// 调用封装好的分布式数据对象处理函数
this.handleDistributedData(want);
}
}
}
handleDistributedData(want: Want) {
// 创建空的分布式数据对象
let remoteSource: SourceObject = new SourceObject(undefined, undefined, undefined, undefined);
this.d_object = distributedDataObject.create(this.context, remoteSource);
// 读取分布式数据对象组网id
let dataSessionId = '';
if (want.parameters !== undefined) {
dataSessionId = want.parameters.dataSessionId as string;
}
// 添加数据变更监听
this.d_object.on("status", (sessionId: string, networkId: string, status: 'online' | 'offline' | 'restored') => {
hilog.info(DOMAIN_NUMBER, TAG, "status changed " + sessionId + " " + status + " " + networkId);
if (status == 'restored') {
if (this.d_object) {
// 收到迁移恢复的状态时，可以从分布式数据对象中读取数据
hilog.info(DOMAIN_NUMBER, TAG, "restored name:" + this.d_object['name']);
hilog.info(DOMAIN_NUMBER, TAG, "restored parents:" + JSON.stringify(this.d_object['parent']));
}
}
});
// 激活分布式数据对象
this.d_object.setSessionId(dataSessionId);
}
}
```
文件资产迁移
对于图片、文档等文件类数据，需要先将其转换为资产commonType.Asset类型，再封装到分布式数据对象中进行迁移。迁移实现方式与普通的分布式数据对象类似，下面仅针对差异部分进行说明。
随后，与普通数据对象的迁移的源端实现相同，可以使用该数据对象加入组网，并进行持久化保存。
示例如下：
对端创建分布式数据对象时，SourceObject对象中的资产不能直接使用undefined初始化，需要创建一个各属性为空的Asset资产对象，否则会导致资产同步失败。
示例代码如下：
若应用想要同步多个资产，可采用两种方式实现：
其中方式1的实现可以直接参照添加一个资产的方式添加更多资产。方式2的示例如下所示：

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-drag-V14
爬取时间: 2025-04-30 04:47:43
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-drag-overview-V14
爬取时间: 2025-04-30 04:47:57
来源: Huawei Developer
跨端拖拽提供跨设备的键鼠共享能力，支持在平板或2in1类型的任意两台设备之间拖拽文件、文本。
例如，当用户拥有两台平板设备时，可以共享一套键鼠，通过跨设备拖拽，一步将设备A的素材拖拽到设备B快速创作，实现跨设备的协同工作体验。
当前系统应用中，文件管理器、浏览器支持拖出；备忘录支持拖入。用户可以体验以下场景：
开发者可以根据实际需求，实现组件的拖入或拖出，即可接入跨设备拖拽。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170540.50697680446361462409515383509033:50001231000000:2800:425C70ABC87D3061A91FF91822880B97E113C837E67C06DF713748FCA24AB216.gif)
运作机制
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170540.45644269083925302980947370904523:50001231000000:2800:6A4C8FB5FC8DF605063EA205496065D7EA7134178819E4E6FFAA537ED428AE52.png)

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-drag-guide-V14
爬取时间: 2025-04-30 04:48:10
来源: Huawei Developer
在开发跨设备拖拽的功能时，系统将自动完成键鼠穿越和跨设备的数据传递，应用可按照本设备上的开发示例，完成拖拽事件的开发。
约束与限制
需同时满足以下条件，才能使用该功能：
-  HarmonyOS NEXT Developer Preview0及以上版本的平板或2in1设备。
接口说明
在开发具体功能前，请先查阅参考文档，获取详细的接口说明。
-  当前部分组件默认支持拖拽控制。应用使用这些组件时，只需要将draggable设置为true，系统将根据组件的支持情况，自动实现onDragStart的写信息或onDrop的读信息。
-  应用应根据实际需求，实现组件拖入或拖出。
开发示例
拖拽事件通过鼠标左键来操作和响应，开发示例请参考：拖拽事件。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-pasteboard-V14
爬取时间: 2025-04-30 04:48:23
来源: Huawei Developer

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-pasteboard-overview-V14
爬取时间: 2025-04-30 04:48:37
来源: Huawei Developer
剪贴板分为本地剪贴板和跨设备剪贴板，本地剪贴板提供设备内的内容复制粘贴，跨设备剪贴板提供跨设备的内容复制粘贴。
当用户拥有多台设备时，可以通过跨设备剪贴板的功能，在A设备的应用上复制一段文本，粘贴到B设备的应用中，高效地完成多设备间的内容共享。
当开发者正在开发一款浏览器类应用，或是备忘录、笔记、邮件等富文本编辑类应用时，均可接入跨设备剪贴板，提升用户体验。
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170541.05177682814552785284396474827914:50001231000000:2800:5B7DFC4104717B6FC1CB8EB050FA8702FC8F8DEA5CDE98CB08CD37437DD6AFB5.gif)
运作机制
![Image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250314170541.13537576978371815758364144342044:50001231000000:2800:C2B9CE1769B05CA4A13171FB20AC78085D48FEF0A3F1FE4B67A301E3C3B18A74.png)
1. 用户在设备A复制数据。
2. 系统剪贴板服务将处理相关数据，并完成数据同步。此过程开发者不感知。
3. 用户在设备B粘贴来自设备A的数据。

URL: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V14/distributed-pasteboard-guide-V14
爬取时间: 2025-04-30 04:48:50
来源: Huawei Developer
在开发跨设备剪贴板的功能时，系统将自动完成跨设备的数据传递，应用可按照本设备上的开发示例，完成跨设备剪贴板的开发。
约束与限制
| 设备版本  | 使用限制  |
| --- | --- |
| HarmonyOS NEXT Developer Preview0及以上  | 双端设备需要登录同一华为账号。双端设备需要打开Wi-Fi和蓝牙开关。条件允许时，建议双端设备接入同一个局域网，可提升数据传输的速度。 双端设备在过程中需解锁、亮屏。  |
| HarmonyOS版本3.2及以上  | 双端设备需要登录同一华为账号。双端设备需要打开Wi-Fi和蓝牙开关，并接入同一个局域网。双端设备在过程中需解锁、亮屏。  |
设备版本
使用限制
HarmonyOS NEXT Developer Preview0及以上
-  条件允许时，建议双端设备接入同一个局域网，可提升数据传输的速度。
HarmonyOS版本3.2及以上
接口说明
在开发具体功能前，请先查阅参考文档，获取详细的接口说明。
| 接口  | 说明  |
| --- | --- |
| getSystemPasteboard(): SystemPasteboard  | 获取系统剪贴板对象。  |
| createData(mimeType: string, value: ValueType): PasteData  | 构建一个自定义类型的剪贴板内容对象。  |
| setData(data: PasteData): Promise<void>  | 将数据写入系统剪贴板，使用Promise异步回调。  |
| getData( callback: AsyncCallback<PasteData>): void  | 读取系统剪贴板内容，使用callback异步回调。 应用使用自定义控件后台访问剪贴板需要申请ohos.permission.READ_PASTEBOARD。  |
| getRecordCount(): number  | 获取剪贴板内容中条目的个数。  |
| getPrimaryMimeType(): string  | 获取剪贴板内容中首个条目的数据类型。  |
| getPrimaryText(): string  | 获取首个条目的纯文本内容。  |
接口
说明
getSystemPasteboard(): SystemPasteboard
获取系统剪贴板对象。
createData(mimeType: string, value: ValueType): PasteData
构建一个自定义类型的剪贴板内容对象。
setData(data: PasteData): Promise<void>
将数据写入系统剪贴板，使用Promise异步回调。
getData( callback: AsyncCallback<PasteData>): void
读取系统剪贴板内容，使用callback异步回调。
应用使用自定义控件后台访问剪贴板需要申请ohos.permission.READ_PASTEBOARD。
getRecordCount(): number
获取剪贴板内容中条目的个数。
getPrimaryMimeType(): string
获取剪贴板内容中首个条目的数据类型。
getPrimaryText(): string
获取首个条目的纯文本内容。
开发示例
跨设备复制的数据两分钟内有效。

