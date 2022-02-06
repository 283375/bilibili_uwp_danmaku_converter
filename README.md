# 哔哩哔哩 UWP 弹幕转换器

## 这是啥？

在整理自己从 [哔哩哔哩 UWP](https://www.microsoft.com/store/productId/9NBLGGH5Q5FV) 上缓存的视频时，发现这玩意儿缓存下来的弹幕不能被 [弹弹play](https://www.dandanplay.com/) 识别。

然后就有了这个转换器。

## 具体区别

以 [BV1z7411P7NJ](https://www.bilibili.com/video/BV1z7411P7NJ) 中的一条弹幕举例：

```xml
<!-- 从 bilibili api 获取的弹幕 -->
<d p="2.624,1,25,16777215,1582785415,4,c4a81af0,29173083004207107">来了来了</d>
<!-- 哔哩哔哩 UWP 缓存的弹幕 -->
<d p="29173083004207107,0,2624,1,25,16777215,1582785415,0,c4a81af0">来了来了</d>
```

从 bilibili api 获取的弹幕：

> 感谢 [B 站弹幕笔记 - Fachep's Blog](https://blog.fachep.com/2020/03/07/Danmaku/)

```xml
<d p="{time},{type},{size},{color},{timestamp},{pool},{uid_crc32},{row_id}">{Text}</d>
```

- `time` 弹幕在视频里的时间，以秒为单位
- `type` 弹幕类型
- `size` 字体大小
- `color` 十进制的 RGB 颜色
- `timestamp` 弹幕发送时间戳
- `pool` 弹幕池
- `uid_crc32` 发送者 uid 的 crc32
- `row_id` 用于标记顺序和历史弹幕

而 哔哩哔哩 UWP 缓存的弹幕：

```xml
<d p="{row_id},{?},{time},{type},{size},{color},{timestamp},{?},{uid_crc32}">{Text}</d>
```

除 `time` 以毫秒为单位、没有 `pool` 及两项一直为 `0` 的属性外，其余跟从 bilibili api 获取的弹幕格式一致。
