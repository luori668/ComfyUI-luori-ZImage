import random
import json
import os
from datetime import datetime
import folder_paths

style_templates = {
    "高冷御姐": {"气质": ["高冷疏离", "清冷感", "御姐气场", "高贵典雅"], "表情": ["高冷", "清冷", "自信", "坚定"], "眼神": ["眼神凌厉", "眼神坚定", "直视镜头", "侧目斜视"], "光线": ["侧逆光", "伦勃朗光", "硬光", "轮廓光"], "氛围": ["神秘诡异", "暗黑哥特", "冷峻", "戏剧感"]},
    "甜美可爱": {"气质": ["甜美可爱", "温柔治愈", "邻家女孩", "活泼俏皮"], "表情": ["微笑", "甜美", "俏皮", "可爱"], "眼神": ["眼神温柔", "眼中带笑", "眼神清澈", "直视镜头"], "光线": ["柔光", "自然光", "蝴蝶光", "顺光"], "氛围": ["温馨治愈", "浪漫唯美", "清新自然", "梦幻童话"]},
    "性感妩媚": {"气质": ["性感妩媚", "魅惑迷人", "成熟魅力", "风情万种"], "表情": ["性感", "妩媚", "诱惑", "迷离"], "眼神": ["含情脉脉", "眼神诱惑", "半睁眼", "迷离眼神"], "光线": ["轮廓光", "电影光", "侧光", "逆光"], "氛围": ["浪漫唯美", "暧昧", "戏剧感", "电影感"]},
    "酷飒帅气": {"气质": ["酷飒帅气", "中性帅气", "高冷", "干练"], "表情": ["高冷", "自信", "坚定", "严肃"], "眼神": ["眼神凌厉", "眼神坚定", "侧目斜视", "直视镜头"], "光线": ["硬光", "顶光", "戏剧光", "侧光"], "氛围": ["暗黑哥特", "工业风", "赛博朋克", "废土风"]},
    "文艺清新": {"气质": ["文艺清新", "温柔知性", "忧郁文艺", "恬静淡雅"], "表情": ["忧郁", "沉思", "温柔", "恬静"], "眼神": ["看向远方", "眼神忧郁", "眼神迷茫", "避开视线"], "光线": ["自然光", "柔光", "逆光", "晨光"], "氛围": ["清新自然", "温馨治愈", "复古怀旧", "文艺"]},
    "纯欲风": {"气质": ["纯真无邪", "初恋感", "清纯", "温柔"], "表情": ["无辜", "天真", "温柔", "微笑"], "眼神": ["眼神清澈", "眼中带笑", "无辜眼神", "含情脉脉"], "光线": ["柔光", "自然光", "逆光", "晨光"], "氛围": ["浪漫唯美", "清新自然", "梦幻童话", "温馨治愈"]}
}

libraries = {
    "拍摄主题": {
        "风格": ["时尚艺术写真", "商业人像摄影", "电影感肖像", "概念艺术摄影", "情绪人像", "故事感大片", "高级时装", "杂志封面", "品牌广告", "日系写真", "韩系画报", "少女日常", "糖水少女", "初恋感", "女友视角", "男友视角", "街拍", "私房", "私摄影", "情绪大片", "光影艺术", "黑白肖像", "胶片感", "复古写真", "赛博朋克", "科幻未来", "国风", "汉服写真", "二次元", "动漫风", "插画感", "暗黑风", "蒸汽朋克", "废土风", "机能风", "Y2K", "千禧风"],
        "类型": ["cosplay风格", "熟女风格", "纯欲风", "青春校园风", "轻熟风", "御姐风", "甜酷风", "中性风", "复古港风", "森系风", "暗黑系", "JK制服风", "洛丽塔", "哥特风", "波西米亚", "小香风", "法式", "英伦风", "休闲日常", "职场OL", "晚宴妆", "节日主题", "泳装", "运动风", "病娇", "高冷", "温柔", "俏皮", "知性", "优雅", "嘻哈风", "街头风", "朋克风", "民族风", "田园风", "学院风", "古装"]
    },
    "模特设定": {
        "人种特征": ["亚洲女性", "东亚面孔", "中国女性", "日系少女", "韩系风格", "中日韩混血", "韩国女性", "日本女性", "台湾女生", "香港女生", "东南亚混血", "混血感", "欧美系亚洲面孔", "新疆美女", "藏族姑娘"],
        "面部特征": ["瓜子脸", "小V脸", "圆脸", "鹅蛋脸", "方脸", "心形脸", "丹凤眼", "杏眼", "桃花眼", "狐狸眼", "下垂眼", "圆眼", "细长眼", "双眼皮", "单眼皮", "内双", "欧式大双", "高挺鼻梁", "小巧鼻子", "肉感鼻子", "精致鼻头", "饱满M形唇", "薄唇", "厚唇", "嘟嘟唇", "樱桃小嘴", "微笑唇", "酒窝", "梨涡", "苹果肌", "高颧骨", "精致下颌线", "美人尖", "一字眉", "柳叶眉", "剑眉", "野生眉", "长睫毛", "卷翘睫毛", "下睫毛明显", "卧蚕明显", "清透感", "冷白皮", "自然肤色", "暖黄皮", "小麦色", "牛奶肌", "水光肌", "零毛孔", "细腻肌肤", "光滑肤质", "透亮感", "光泽感"],
        "发型发色": ["黑长直", "黑短发", "金发", "棕发", "红发", "粉发", "蓝发", "紫发", "银发", "灰发", "渐变发", "挑染", "公主切", "齐刘海", "空气刘海", "八字刘海", "中分", "侧分", "无刘海", "长发及腰", "中长发", "齐肩发", "锁骨发", "短发", "超短发", "大波浪卷", "小卷发", "羊毛卷", "水波卷", "蛋卷头", "公主头", "高马尾", "低马尾", "双马尾", "麻花辫", "丸子头", "半扎发", "编发", "发带装饰", "蝴蝶结发饰", "发卡点缀", "发箍装饰"],
        "身材体型": ["匀称修长", "苗条身材", "S型曲线", "纤细腰肢", "丰腴身材", "高挑", "娇小", "标准比例", "修长双腿", "紧致手臂", "直角肩", "天鹅颈", "蝴蝶骨", "美背", "纤纤细腰", "蜜桃臀", "大长腿", "小腿纤细", "脚踝精致", "骨感美", "肉感美", "健康美", "运动型", "纤细型", "丰满型", "匀称型", "模特身材", "舞蹈生身材", "运动员身材", "健身型"],
        "气质神态": ["优雅气质", "清冷感", "温柔知性", "甜美可爱", "御姐气场", "慵懒随性", "阳光开朗", "忧郁神秘", "高贵典雅", "活泼俏皮", "文艺清新", "复古摩登", "性感妩媚", "酷飒帅气", "中性帅气", "邻家女孩", "初恋感", "少女感", "成熟魅力", "知性优雅", "温柔治愈", "忧郁文艺", "高冷疏离", "甜美可人", "天真烂漫", "纯真无邪", "魅惑迷人", "气场全开", "温婉可人", "恬静淡雅"]
    },
    "服装造型": {
        "上衣": ["深V吊带", "镂空针织衫", "蕾丝透视衫", "露背交叉上衣", "单肩荷叶边上衣", "抹胸上衣", "肚兜式上衣", "渔网打底衫", "绑带露脐装", "一字肩镂空衫", "挂脖吊带", "蕾丝边裹胸", "透视薄纱上衣", "后背挖空T恤", "胸衣式外穿", "白色衬衫", "黑色T恤", "条纹针织衫", "蕾丝上衣", "露肩毛衣", "泡泡袖上衣", "荷叶边上衣", "一字领上衣", "吊带上衣", "抹胸", "透视衫", "卫衣", "连帽卫衣", "POLO衫", "短袖衬衫", "长袖T恤", "雪纺衬衫", "丝绸衬衫", "缎面吊带", "针织开衫", "毛绒外套", "皮夹克", "牛仔外套", "西装外套", "风衣", "棒球服", "飞行员夹克", "摇粒绒外套", "羽绒服", "毛呢大衣", "露脐装", "背心", "马甲", "斗篷", "披肩", "旗袍上衣", "汉服上衣", "唐装", "中山装", "夹克衫", "冲锋衣", "防晒衣", "紧身衣", "渔网衫", "镂空上衣", "绑带上衣", "蝴蝶结衬衫"],
        "下装": ["热裤", "低腰牛仔裤", "侧边开叉裤", "蕾丝边短裤", "绑带皮裤", "高腰三角裤", "镂空长裤", "渔网袜打底裤", "牛仔裤", "阔腿裤", "紧身裤", "喇叭裤", "工装裤", "运动裤", "休闲裤", "西装裤", "皮裤", "格纹裤", "短裙", "半身裙", "A字裙", "包臀裙", "百褶裙", "鱼尾裙", "纱裙", "碎花裙", "牛仔裙", "皮质短裙", "高腰裤", "低腰裤", "热裤", "骑行裤", "打底裤", "阔腿短裤", "直筒裤", "哈伦裤", "萝卜裤", "灯笼裤", "背带裤", "连体裤", "健美裤", "瑜伽裤"],
        "连衣裙": ["吊带短裙", "开叉包臀裙", "露背连衣裙", "深V领连衣裙", "蕾丝透视连衣裙", "挂脖超短裙", "紧身绷带裙", "单肩亮片裙", "镂空腰连衣裙", "高开叉旗袍裙", "后背蝴蝶结连衣裙", "抹胸蓬蓬裙", "鱼骨胸衣连衣裙", "侧边绑带裙", "网纱拼接裙", "吊带连衣裙", "碎花连衣裙", "纯色连衣裙", "印花连衣裙", "蕾丝连衣裙", "丝绸连衣裙", "雪纺连衣裙", "针织连衣裙", "卫衣连衣裙", "衬衫裙", "娃娃裙", "旗袍", "汉服", "和服", "洛丽塔裙", "晚礼服", "小礼服", "婚纱", "泳衣连衣裙", "睡衣连衣裙", "高腰连衣裙", "修身连衣裙", "宽松连衣裙", "收腰连衣裙", "露背连衣裙", "开叉连衣裙", "V领连衣裙", "方领连衣裙", "圆领连衣裙", "一字肩连衣裙", "法式茶歇裙", "波西米亚长裙", "针织吊带裙", "丝绒连衣裙", "亮片连衣裙"],
        "制服校服": ["兔女郎装", "猫娘套装", "女警短裙制服", "空姐修身制服", "护士短裙装", "OL包臀裙套装", "拉拉队服", "体操服", "泳装", "比基尼", "连体泳衣", "JK制服", "水手服", "学院风套装", "白衬衫配格裙", "西式校服", "日式校服", "韩式校服", "英伦校服", "美式校服", "运动校服", "护士服", "空姐服", "女仆装", "警服", "军装", "白大褂", "实验室服", "厨师服", "服务员制服", "快递员制服"],
        "鞋袜": ["小白鞋", "帆布鞋", "运动鞋", "高跟鞋", "平底鞋", "凉鞋", "拖鞋", "靴子", "马丁靴", "雪地靴", "乐福鞋", "牛津鞋", "玛丽珍鞋", "芭蕾舞鞋", "洞洞鞋", "长筒袜", "短袜", "丝袜", "网袜", "堆堆袜", "过膝袜", "大腿袜", "小腿袜", "船袜", "隐形袜", "蕾丝袜", "网格袜", "印花袜", "条纹袜", "波点袜"],
        "配饰": ["银质流苏耳环", "珍珠耳钉", "钻石耳坠", "金属耳骨夹", "耳线", "珍珠项链", "锁骨链", "choker", "多层项链", "金币项链", "蛇骨手链", "珍珠手链", "编织手链", "手表", "手镯", "戒指", "对戒", "钻戒", "尾戒", "关节戒", "发带", "发箍", "发夹", "发簪", "发绳", "帽子", "贝雷帽", "渔夫帽", "棒球帽", "草帽", "围巾", "丝巾", "领带", "领结", "领巾", "手套", "长手套", "短手套", "蕾丝手套", "皮手套", "墨镜", "平光镜", "金丝眼镜", "方框眼镜", "圆框眼镜", "包包", "手提包", "单肩包", "双肩包", "链条包", "腰带", "腰链", "腰封", "背带", "吊带"],
        "材质": ["丝绸", "缎面", "针织", "绒面", "蕾丝", "棉麻", "雪纺", "皮革", "金属质感", "珠光面料", "透明薄纱", "网纱", "亮片面料", "毛呢", "羊毛", "羊绒", "牛仔布", "灯芯绒", "麂皮", "PVC材质", "漆皮", "天鹅绒", "金丝绒", "雪尼尔", "亚麻", "真丝", "人棉", "莫代尔", "天丝", "冰丝"],
        "颜色": ["纯白色", "米白色", "奶油白", "珍珠白", "象牙白", "纯黑色", "炭黑色", "墨黑色", "午夜黑", "高级黑", "大红色", "酒红色", "玫瑰红", "绯红色", "枣红色", "宝蓝色", "天蓝色", "湖蓝色", "午夜蓝", "克莱因蓝", "草绿色", "墨绿色", "橄榄绿", "薄荷绿", "牛油果绿", "鹅黄色", "柠檬黄", "姜黄色", "土黄色", "芥末黄", "香芋紫", "薰衣草紫", "葡萄紫", "深紫色", "淡紫色", "樱花粉", "蜜桃粉", "玫瑰粉", "裸粉色", "芭比粉", "咖啡色", "棕色", "卡其色", "驼色", "巧克力色", "灰色", "银灰色", "烟灰色", "高级灰", "水泥灰", "渐变色", "撞色", "拼色", "印花", "格纹", "条纹", "波点"],
        "古装": ["汉服", "唐装", "宋制汉服", "明制汉服", "魏晋风骨", "齐胸襦裙", "对襟襦裙", "交领襦裙", "曲裾深衣", "直裾深衣", "圆领袍", "褙子", "大袖衫", "披帛", "云肩", "马面裙", "百迭裙", "旋裙", "破裙", "诃子裙", "晋制汉服", "战国袍", "秦制汉服", "清汉女装", "旗袍改良", "武侠风衣袍", "仙女裙", "敦煌飞天", "神仙服", "帝王冕服"]
    },
    "场景环境": {
        "室内场景": ["复古丝绒沙发", "私人图书馆", "装饰艺术风格房间", "胡桃木书架", "复古唱片店", "日式茶室", "韩式咖啡馆", "现代简约客厅", "工业风工作室", "梦幻光影房间", "欧式宫廷卧室", "法式阳台", "美式乡村厨房", "北欧风书房", "中式庭院室内", "和室", "音乐教室", "舞蹈房", "画室", "摄影棚", "录音室", "温室花房", "阳光房", "阁楼", "地下室", "酒窖", "衣帽间", "浴室", "卧室飘窗", "餐厅", "厨房", "电影院包厢", "游戏厅", "网吧包厢", "KTV包间", "酒吧", "健身房", "瑜伽室", "泳池边", "桑拿房", "SPA室", "酒店套房", "民宿房间", "别墅客厅", "公寓阳台", "办公室", "美术馆", "博物馆", "画廊", "剧院后台", "录音棚", "植物园温室", "水族馆", "天文馆", "科技馆", "图书馆"],
        "室外场景": ["樱花树下", "城市天台", "海边日落", "森林小径", "古风庭院", "霓虹街道", "雨夜街角", "雪景公园", "向日葵花田", "薰衣草庄园", "枫叶林", "银杏大道", "竹林幽径", "湖边栈道", "山间溪流", "沙漠绿洲", "草原牧场", "葡萄园", "茶园", "稻田", "游乐园", "摩天轮下", "旋转木马前", "过山车旁", "海盗船边", "地铁站", "公交车站", "火车站", "机场", "码头", "古镇小巷", "老街区", "创意园区", "大学校园", "操场看台", "篮球场", "网球场", "足球场", "游泳池", "沙滩", "屋顶花园", "阳台", "露台", "庭院", "天台", "桥梁上", "隧道里", "地下通道", "天桥", "人行道", "瀑布前", "峡谷边缘", "山顶观景台", "海边悬崖", "火山口", "热带雨林", "竹林深处", "梅花林", "桃花源", "油菜花田"],
        "时间天气": ["清晨", "午后", "黄昏", "夜晚", "午夜", "晴天", "阴天", "雨天", "雪天", "雾天", "彩虹天", "台风天", "雷雨天", "沙尘天", "极光夜", "春季", "夏季", "秋季", "冬季", "梅雨季", "樱花季", "枫叶季", "圣诞季", "情人节", "万圣节", "新年", "春节", "中秋节", "端午节", "七夕"],
        "氛围感觉": ["温馨治愈", "浪漫唯美", "神秘诡异", "科幻未来", "复古怀旧", "清新自然", "梦幻童话", "暗黑哥特", "赛博朋克", "蒸汽波", "废土风", "末日感", "乌托邦", "反乌托邦", "超现实", "极简主义", "极繁主义", "巴洛克", "洛可可", "新古典", "印象派", "表现主义", "抽象派", "超现实主义", "波普艺术", "电影感", "戏剧感", "舞台感", "MV感", "广告大片感"]
    },
    "拍摄参数": {
        "镜头": ["85mm f/1.4人像镜皇", "50mm f/1.2标准镜头", "135mm f/2.0长焦", "35mm f/1.4广角", "24-70mm f/2.8变焦", "70-200mm f/2.8长焦", "24mm f/1.4广角", "100mm f/2.8微距", "200mm f/2.0空气切割机", "鱼眼镜头", "移轴镜头", "电影镜头", "复古镜头", "变形宽银幕镜头"],
        "光圈": ["f/1.2", "f/1.4", "f/1.8", "f/2.0", "f/2.8", "f/4.0", "f/5.6", "f/8.0"],
        "快门": ["1/125s", "1/250s", "1/500s", "1/1000s", "1/2000s", "慢门", "B门"],
        "ISO": ["ISO 100", "ISO 200", "ISO 400", "ISO 800", "ISO 1600", "ISO 3200", "ISO 6400"],
        "白平衡": ["日光", "阴天", "阴影", "白炽灯", "荧光灯", "自定义白平衡"],
        "对焦": ["单点对焦", "区域对焦", "追踪对焦", "眼部对焦", "人脸对焦", "手动对焦"]
    },
    "构图光影": {
        "构图": ["中心构图", "三分法构图", "引导线构图", "对称构图", "留白构图", "对角线构图", "三角形构图", "S形构图", "框架构图", "重复构图", "黄金分割", "螺旋构图", "放射状构图", "棋盘构图", "并列构图", "前景构图", "背景构图", "多层次构图", "散点构图", "倾斜构图"],
        "景深": ["浅景深", "大光圈虚化", "中等景深", "全清晰", "微距景深", "前实后虚", "前虚后实", "奶油般化开", "光斑效果", "漩涡散景", "焦外成像", "散景形状", "散景光斑", "二线性散景", "圆形散景"],
        "光线": ["自然光", "柔光", "硬光", "侧光", "逆光", "顶光", "底光", "顺光", "侧逆光", "轮廓光", "伦勃朗光", "蝴蝶光", "分割光", "环形光", "夹板光", "电影光", "戏剧光", "舞台光", "霓虹光", "镭射光", "丁达尔效应", "体积光", "光束", "光晕", "光斑", "剪影", "高调", "低调", "中间调", "高反差", "低反差", "柔光箱", "反光板", "柔光罩", "蜂巢", "色片", "滤镜", "ND镜", "偏振镜", "渐变镜"],
        "光影效果": ["柔和过渡", "强烈对比", "戏剧性光影", "明暗交错", "光影斑驳", "光线透过", "影子投射", "光影分割", "光影层次", "光影流动", "高光溢出", "暗部细节", "中间调丰富", "光影节奏", "光影韵律", "光的方向性", "光的质感", "光的颜色", "光的温度", "光的强度"]
    },
    "色彩色调": {
        "色调": ["暖色调", "冷色调", "中性色调", "复古色调", "胶片色调", "电影色调", "日系色调", "韩系色调", "欧美色调", "国风色调", "莫兰迪色系", "马卡龙色系", "糖果色系", "高级灰", "黑白", "单色", "双色调", "三色调", "渐变色", "撞色", "高饱和度", "低饱和度", "去色", "留色", "色调分离"],
        "色彩风格": ["富士胶片感", "柯达胶片感", "宝丽来", "禄来", "哈苏", "徕卡", "理光GR", "美能达", "奥林巴斯", "尼康", "佳能", "索尼", "宾得", "电影感调色", "MV调色", "广告调色", "杂志调色", "ins风", "小红书风", "抖音风", "王家卫风格", "岩井俊二风格", "是枝裕和风格", "韦斯安德森风格", "诺兰风格"]
    },
    "后期处理": {
        "分辨率": ["8K超高清", "4K电影级", "2K高清", "1080p全高清", "720p高清"],
        "画质": ["锐利清晰", "细腻柔和", "胶片颗粒", "数字降噪", "高动态范围", "丰富细节", "清晰通透", "柔和朦胧", "油画质感", "水彩质感", "素描质感", "版画质感", "浮雕效果", "柔焦效果", "模糊效果", "锐化处理", "降噪处理", "去瑕疵", "磨皮处理", "液化处理"],
        "特效": ["光晕特效", "漏光特效", "炫光特效", "星光特效", "雨滴特效", "雪花特效", "花瓣特效", "烟雾特效", "火焰特效", "水波特效", "镜像特效", "双重曝光", "多重曝光", "运动模糊", "径向模糊", "动态模糊", "景深模拟", "晕影效果", "暗角效果", "胶片划痕", "灰尘颗粒", "噪点添加", "像素化", "马赛克", "故障艺术"],
        "质感": ["皮肤质感细腻", "发丝根根分明", "睫毛清晰可见", "瞳孔有神", "唇部水润", "服装纹理清晰", "材质质感真实", "金属反光", "玻璃通透", "水珠晶莹", "光影过渡自然", "色彩过渡平滑", "层次丰富", "立体感强", "空间感足", "空气感", "呼吸感", "生命力", "情感表达", "故事感"]
    },
    "姿势动作": {
        "全身姿势": ["慵懒倚靠沙发", "坐在窗边", "站立靠墙", "躺在地毯上", "蹲在地上", "跳跃瞬间", "旋转跳舞", "漫步行走", "奔跑抓拍", "瑜伽动作", "舞蹈姿势", "运动瞬间", "伸展身体", "蜷缩身体", "俯身低头", "仰头向上", "侧身回眸", "正面直视", "背影", "坐姿优雅", "站姿挺拔", "卧姿放松", "跪姿虔诚", "趴姿慵懒"],
        "手部动作": ["轻抚发丝", "双手抱胸", "手插口袋", "双手合十", "比心手势", "比耶手势", "OK手势", "打招呼", "挥手告别", "伸手触摸", "握拳加油", "张开双臂", "交叉双手", "整理衣领", "调整眼镜", "拿书阅读", "端茶杯", "拿手机自拍", "撑伞", "拿包", "拿花束", "拿气球"],
        "面部表情": ["微笑", "大笑", "露齿笑", "抿嘴笑", "神秘微笑", "忧郁", "沉思", "惊讶", "调皮", "温柔", "高冷", "清冷", "甜美", "可爱", "俏皮", "性感", "妩媚", "诱惑", "无辜", "天真", "自信", "坚定", "迷茫", "疲惫", "放松", "专注", "出神", "期待", "满足", "幸福"],
        "眼神": ["直视镜头", "避开视线", "看向远方", "低头看地", "抬头看天", "侧目斜视", "闭眼", "半睁眼", "眯眼", "瞪大眼", "含情脉脉", "眼神凌厉", "眼神温柔", "眼神坚定", "眼神迷茫", "眼神忧郁", "眼神俏皮", "眼神诱惑", "眼神无辜", "眼神自信", "泪眼朦胧", "眼中带笑", "眼神有光", "眼神深邃", "眼神清澈"]
    },
    "背景选择": {
        "背景类型": ["无", "纯色背景", "渐变背景", "纹理背景", "几何背景", "抽象背景", "自然风景背景", "城市街景背景", "室内环境背景", "梦幻星空背景", "光斑背景", "光晕背景", "烟雾背景", "水波纹背景", "云彩背景", "极简背景", "复古背景", "未来感背景", "赛博朋克背景", "蒸汽波背景", "油画背景", "水彩背景", "素描背景", "漫画背景", "插画背景", "黑板背景", "白板背景", "幕布背景", "窗帘背景", "纱幔背景", "花墙背景", "绿植墙背景", "砖墙背景", "木纹背景", "大理石背景", "金属背景", "玻璃背景", "镜面背景", "LED背景", "投影背景", "五星级酒店", "豪华酒店套房", "商务酒店", "精品酒店", "度假酒店", "海边度假酒店", "山林木屋", "温泉酒店", "民宿客栈", "青年旅舍", "户外露营", "森林营地", "海边沙滩", "山顶风光", "湖畔景色", "田园风光", "雪山之巅", "沙漠绿洲", "草原牧场", "峡谷深处", "著名旅游景点", "历史古迹", "文化遗址", "主题公园", "游乐园", "动物园", "植物园", "海洋公园", "博物馆", "艺术馆", "购物中心", "美食街", "夜市摊位", "步行街", "商业街", "随机"]
    },
    "丝袜类型": {
        "丝袜种类": ["无", "透明丝袜", "肤色丝袜", "黑色丝袜", "白色丝袜", "灰色丝袜", "咖啡色丝袜", "肉色丝袜", "裸色丝袜", "米色丝袜", "渔网袜", "网格袜", "菱形网袜", "大网格袜", "细网格袜", "蕾丝丝袜", "花边丝袜", "刺绣丝袜", "印花丝袜", "波点丝袜", "条纹丝袜", "竖条纹丝袜", "横条纹丝袜", "格子丝袜", "菱格丝袜", "亮丝丝袜", "哑光丝袜", "天鹅绒丝袜", "棉质丝袜", "羊毛丝袜", "过膝丝袜", "大腿袜", "小腿袜", "及膝袜", "短袜", "连裤丝袜", "长筒丝袜", "吊带丝袜", "开裆丝袜", "露趾丝袜", "彩色丝袜", "红色丝袜", "蓝色丝袜", "紫色丝袜", "粉色丝袜", "绿色丝袜", "黄色丝袜", "橙色丝袜", "渐变色丝袜", "荧光丝袜", "破洞丝袜", "做旧丝袜", "磨损丝袜", "补丁丝袜", "拼接丝袜", "随机"]
    },
    "头部配饰": {
        "帽子": ["无", "贝雷帽", "渔夫帽", "棒球帽", "草帽", "礼帽", "绅士帽", "爵士帽", "平顶帽", "圆顶帽", "鸭舌帽", "报童帽", "画家帽", "针织帽", "毛线帽", "雷锋帽", "军帽", "警察帽", "护士帽", "厨师帽", "太阳帽", "遮阳帽", "空顶帽", "发箍帽", "头巾帽", "圣诞帽", "巫师帽", "公主皇冠", "小丑帽", "卡通帽"],
        "口罩": ["无", "医用口罩", "N95口罩", "防尘口罩", "布口罩", "蕾丝口罩", "印花口罩", "黑色口罩", "白色口罩", "彩色口罩", "透明口罩", "面罩", "护目镜", "面纱", "半遮面纱"],
        "眼镜": ["无", "近视眼镜", "远视眼镜", "老花眼镜", "防蓝光眼镜", "太阳镜", "墨镜", "偏光镜", "变色镜", "夜视镜", "金丝眼镜", "银丝眼镜", "黑框眼镜", "半框眼镜", "无框眼镜", "圆框眼镜", "方框眼镜", "椭圆框眼镜", "猫眼镜框", "飞行员眼镜", "复古眼镜", "时尚眼镜", "运动眼镜", "护目镜", "3D眼镜"],
        "头饰": ["无", "发箍", "发带", "发夹", "发簪", "发绳", "发圈", "发卡", "发梳", "发网", "蝴蝶结", "花朵发饰", "珍珠发饰", "水晶发饰", "钻石发饰", "羽毛发饰", "丝带", "蕾丝发带", "缎带", "头纱", "皇冠", "王冠", "头冠", "花环", "桂冠", "耳罩", "耳机", "头戴式耳机", "发箍耳机", "猫耳朵发箍", "兔耳朵发箍", "鹿角发箍", "恶魔角", "天使光环", "精灵耳饰"],
        "项链": ["无", "珍珠项链", "锁骨链", "吊坠项链", "字母项链", "心形吊坠", "星星吊坠", "月亮吊坠", "十字架吊坠", "幸运符吊坠", "choker项圈", "蕾丝choker", "皮质choker", "金属choker", "丝绒choker", "多层项链", "长项链", "短项链", "Y型项链", "钻石项链", "宝石项链", "水晶项链", "玉石项链", "银质项链", "金项链", "白金项链", "玫瑰金项链", "钛钢项链", "合金项链"],
        "耳饰": ["无", "耳钉", "耳环", "耳坠", "耳线", "耳骨夹", "耳扣", "耳挂", "耳链", "耳圈", "珍珠耳钉", "钻石耳钉", "宝石耳环", "流苏耳坠", "几何耳环", "不对称耳饰", "单只耳饰", "多只耳饰", "耳廓饰", "耳屏饰"],
        "其他配饰": ["无", "围巾", "丝巾", "领带", "领结", "胸针", "徽章", "勋章", "胸花", "肩章", "臂章", "袖扣", "领针", "领夹", "领带夹", "手链", "手镯", "手表", "戒指", "指环", "随机"]
    },
    "鞋子类型": {
        "鞋类": ["无", "高跟鞋", "细跟高跟鞋", "粗跟高跟鞋", "坡跟鞋", "方跟鞋", "猫跟鞋", "锥跟鞋", "酒杯跟", "平底鞋", "芭蕾舞鞋", "玛丽珍鞋", "乐福鞋", "牛津鞋", "运动鞋", "跑步鞋", "篮球鞋", "网球鞋", "训练鞋", "帆布鞋", "板鞋", "滑板鞋", "休闲鞋", "豆豆鞋", "靴子", "马丁靴", "切尔西靴", "军靴", "雪地靴", "长筒靴", "过膝靴", "及膝靴", "短靴", "踝靴", "凉鞋", "罗马凉鞋", "夹趾凉鞋", "坡跟凉鞋", "厚底凉鞋", "拖鞋", "人字拖", "毛绒拖鞋", "浴室拖鞋", "居家拖鞋", "皮鞋", "漆皮鞋", "磨砂皮鞋", "鳄鱼皮鞋", "蛇纹皮鞋", "布鞋", "绣花鞋", "老北京布鞋", "舞蹈鞋", "爵士鞋", "雨鞋", "胶鞋", "水鞋", "雨靴", "防水鞋", "随机"]
    },
    "情趣服装": {
        "情趣衣服": ["无", "蕾丝情趣内衣", "吊带丝袜套装", "黑色网纱情趣服", "红色绸缎情趣睡裙", "透视情趣睡衣", "绑带情趣内衣", "开裆情趣丝袜", "学生制服情趣装", "护士情趣制服", "女仆情趣装", "空姐情趣制服", "兔女郎情趣装", "猫咪情趣套装", "狐狸情趣尾巴套装", "天使情趣内衣", "恶魔情趣套装", "皮质情趣套装", "金属链情趣内衣", "珍珠串情趣内衣", "羽毛情趣内衣", "透明情趣雨衣", "亮片情趣舞裙", "渔网情趣套装", "网格情趣内衣", "绑带情趣胸衣", "丁字情趣内裤", "高叉情趣连体衣", "露背情趣连衣裙", "开胸情趣上衣", "露肩情趣睡裙", "高腰情趣短裤", "低腰情趣裙", "镂空情趣连衣裙", "蕾丝花边情趣内衣", "绸缎吊带情趣睡裙", "薄纱情趣套装", "皮质束腰情趣内衣", "金属环情趣套装", "珍珠链情趣内衣", "羽毛披风情趣装", "情趣和服", "情趣旗袍", "情趣汉服", "情趣女警制服", "情趣教师装", "情趣秘书装", "情趣空姐装", "情趣模特装", "情趣舞娘装", "情趣公主裙", "情趣女王装", "情趣精灵装", "情趣美人鱼装", "情趣天使装", "情趣恶魔装", "情趣猫咪装", "情趣兔女郎装", "情趣狐狸装", "情趣豹纹装", "情趣斑马纹装", "情趣蛇皮纹装", "随机"]
    },
    "美瞳种类": {
        "美瞳": ["无", "自然棕", "巧克力色", "深棕色", "浅棕色", "琥珀色", "蜂蜜棕", "亚麻棕", "摩卡棕", "可可棕", "灰色", "银灰色", "烟灰色", "蓝灰色", "碳灰色", "蓝色", "天蓝色", "海蓝色", "冰蓝色", "宝蓝色", "灰蓝色", "绿色", "草绿色", "墨绿色", "橄榄绿", "薄荷绿", "翡翠绿", "紫色", "薰衣草紫", "葡萄紫", "粉紫色", "紫罗兰", "粉色", "樱花粉", "蜜桃粉", "玫瑰粉", "芭比粉", "混血感", "混血灰", "混血蓝", "混血绿", "混血棕", "艺术片", "星河款", "小鹿斑比", "狗狗眼", "猫眼款", "高光款", "锁边款", "蕾丝边", "金粉款", "银河款", "月牙款", "爱心款", "星星款", "雪花款", "彩虹款", "随机"]
    },
    "人种类型": {
        "人种": ["亚洲人", "东亚人", "东南亚人", "南亚人", "西亚人", "欧洲人", "北欧人", "西欧人", "东欧人", "南欧人", "非洲人", "北非人", "撒哈拉以南非洲人", "东非人", "西非人", "美洲人", "北美原住民", "拉丁裔", "印第安人", "因纽特人", "中东人", "阿拉伯人", "波斯人", "犹太人", "突厥人", "高加索人", "斯拉夫人", "日耳曼人", "凯尔特人", "拉丁人", "混血", "欧亚混血", "非亚混血", "拉美混血", "多国混血", "太平洋岛民", "波利尼西亚人", "密克罗尼西亚人", "美拉尼西亚人", "毛利人", "随机"]
    },
    "人物设定": {
        "类型": ["单人", "双人", "情侣", "闺蜜", "兄弟", "家人", "同事", "主仆", "对手", "观众", "路人", "人群", "随机"]
    },
    "景别": {
        "类型": ["全身照", "七分照", "半身照", "特写", "局部特写", "随机"]
    }
}

libraries["NSFW元素"] = {
    "身体强调": ["丰满坚挺的乳房", "深邃诱人乳沟", "硬挺肿胀的乳头", "粉嫩湿润肿胀的阴唇", "晶莹蜜液不断流出的蜜穴", "微微张开的粉嫩私处", "高潮潮吹的蜜穴", "肿胀勃起的阴蒂", "肛门微微收缩", "全身汗湿光泽的肌肤", "极致湿润喷水的私处", "乳头喷奶", "阴唇肿胀流蜜", "潮红高潮的私密部位"],
    "性感姿势": ["双腿大开完全暴露蜜穴", "跪姿高高翘臀后入式", "仰卧M型大开腿", "手指猛烈抽插蜜穴", "舌头伸出滴落口水高潮表情", "潮吹喷水全身颤抖", "后入式双手拉开臀瓣", "骑乘位扭腰猛烈摇摆", "四肢着地狗爬式翘臀", "双手托胸挤出深沟自慰", "高潮痉挛潮吹液体四溅"],
    "情色氛围": ["极致淫乱", "欲火焚身高潮连连", "肉欲横流春心荡漾", "淫靡湿热", "高潮痉挛潮吹", "色情至极", "情欲爆炸", "极致色气满满", "欲仙欲死", "浪叫连连"]
}

action_options = [
    "无", "侧身回眸", "站立靠墙", "坐在窗边", "慵懒倚靠沙发", "双手抱胸", "轻抚发丝", 
    "手插口袋", "抬头望天", "低头沉思", "跪坐姿势", "M字腿", "双腿大开", "撅起臀部", 
    "跪姿翘臀", "分开双腿", "双手托胸", "双手揉胸", "伸舌头", "翻白眼", "咬唇呻吟", 
    "潮吹姿势", "仰卧抬腿", "后入式翘臀", "骑乘位扭腰", "四肢着地狗爬式", 
    "手指插入蜜穴", "舌头伸出流口水", "高潮颤抖", "侧躺抬腿暴露", "站立弯腰翘臀"
]

def get_random_item(category, subcategory):
    if category in libraries and subcategory in libraries[category]:
        items = libraries[category][subcategory]
        valid_items = [item for item in items if item not in ["随机", "无"]]
        if valid_items:
            return random.choice(valid_items)
        return random.choice(items) if items else ""
    return ""

def get_coherent_attributes(style_theme):
    if style_theme == "随机" or style_theme not in style_templates:
        style_theme = random.choice(list(style_templates.keys()))
    template = style_templates[style_theme]
    return {
        "风格主题": style_theme,
        "气质": random.choice(template["气质"]),
        "表情": random.choice(template["表情"]),
        "眼神": random.choice(template["眼神"]),
        "光线": random.choice(template["光线"]),
        "氛围": random.choice(template["氛围"])
    }


class ZImagePromptGeneratorNode:
    CATEGORY = "prompt_generators"

    @classmethod
    def INPUT_TYPES(cls):
        age_options = ["无"] + [f"{i}岁" for i in range(16, 39)]
        body_options = ["无", "苗条修长", "S型火辣曲线", "丰满坚挺", "纤细腰肢蜜桃臀", "高挑匀称", "肉感丰腴", "骨感模特身材", "舞蹈生紧致身材", "健身型健康曲线"]

        all_headwear = list(set([item for sublist in libraries["头部配饰"].values() for item in sublist]))

        return {
            "required": {
                "风格主题": (list(style_templates.keys()) + ["随机", "无"], {"default": "高冷御姐"}),
                "拍摄风格": (libraries["拍摄主题"]["风格"] + ["随机", "无"], {"default": "时尚艺术写真"}),
                "拍摄类型": (libraries["拍摄主题"]["类型"] + ["随机", "无"], {"default": "小香风"}),
                "细节级别": (["简洁级", "普通级", "详细级", "大师级", "极致级", "无"], {"default": "大师级"}),
                "lora触发词1": ("STRING", {"default": "", "multiline": False}),
                "启用1": ("BOOLEAN", {"default": False}),
                "lora触发词2": ("STRING", {"default": "", "multiline": False}),
                "启用2": ("BOOLEAN", {"default": False}),
                "lora触发词3": ("STRING", {"default": "", "multiline": False}),
                "启用3": ("BOOLEAN", {"default": False}),
                "lora触发词4": ("STRING", {"default": "", "multiline": False}),
                "启用4": ("BOOLEAN", {"default": False}),
                "动作": (action_options, {"default": "无"}),
                "年龄": (age_options, {"default": "23岁"}),
                "身材": (body_options, {"default": "舞蹈生紧致身材"}),
                "种族选择": (libraries["人种类型"]["人种"] + ["随机", "无"], {"default": "亚洲人"}),
                "美瞳选择": (libraries["美瞳种类"]["美瞳"] + ["随机"], {"default": "蓝灰色"}),
                "丝袜类型": (libraries["丝袜类型"]["丝袜种类"], {"default": "无"}),
                "头部配饰": (all_headwear, {"default": "无"}),
                "鞋子类型": (libraries["鞋子类型"]["鞋类"], {"default": "无"}),
                "情趣衣服": (libraries["情趣服装"]["情趣衣服"], {"default": "无"}),
                "景别": (libraries["景别"]["类型"], {"default": "全身照"}),
                "NSFW": ("BOOLEAN", {"default": False, "label": "NSFW（漏骨模式）"}),
                "包含姿势描述": ("BOOLEAN", {"default": True}),
                "包含高级细节": ("BOOLEAN", {"default": True}),
                "包含画质参数": ("BOOLEAN", {"default": True}),
                "包含后缀参数": ("BOOLEAN", {"default": True}),
                "启用前景特效": ("BOOLEAN", {"default": False}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "prompt_input": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate"
    OUTPUT_NODE = True

    def generate(self, **kwargs):
        seed = kwargs.get("seed", 0)
        random.seed(seed)

        style_theme = kwargs.get("风格主题", "高冷御姐")
        style = kwargs.get("拍摄风格", "时尚艺术写真")
        type_val = kwargs.get("拍摄类型", "小香风")
        detail_level = kwargs.get("细节级别", "大师级")
        action = kwargs.get("动作", "无")
        selected_age = kwargs.get("年龄", "23岁")
        selected_body = kwargs.get("身材", "舞蹈生紧致身材")
        nsfw = kwargs.get("NSFW", False)

        race_choice = kwargs.get("种族选择", "亚洲人")
        contact_lens_choice = kwargs.get("美瞳选择", "蓝灰色")
        stocking = kwargs.get("丝袜类型", "无")
        headwear = kwargs.get("头部配饰", "无")
        shoes = kwargs.get("鞋子类型", "无")
        sexy_clothing = kwargs.get("情趣衣服", "无")
        framing = kwargs.get("景别", "全身照")

        include_pose = kwargs.get("包含姿势描述", True)
        include_details = kwargs.get("包含高级细节", True)
        include_quality = kwargs.get("包含画质参数", True)
        include_suffix = kwargs.get("包含后缀参数", True)
        enable_foreground = kwargs.get("启用前景特效", False)

        triggers = []
        for i in range(1, 4):
            trigger = kwargs.get(f"lora触发词填充{i}", "").strip()
            enabled = kwargs.get(f"启用{i}", False)
            if trigger and enabled:
                triggers.append(trigger)

        def resolve(value, category, subcategory):
            if value == "随机":
                return get_random_item(category, subcategory)
            elif value == "无":
                return ""
            return value

        style = resolve(style, "拍摄主题", "风格")
        type_val = resolve(type_val, "拍摄主题", "类型")
        race_choice = resolve(race_choice, "人种类型", "人种")
        contact_lens_choice = resolve(contact_lens_choice, "美瞳种类", "美瞳")
        stocking = resolve(stocking, "丝袜类型", "丝袜种类")
        shoes = resolve(shoes, "鞋子类型", "鞋类")
        sexy_clothing = resolve(sexy_clothing, "情趣服装", "情趣衣服")
        framing = resolve(framing, "景别", "类型")

        coherent = get_coherent_attributes(style_theme if style_theme != "无" else None)

        prompt = self._generate_prompt(
            style, type_val, detail_level, action, race_choice, contact_lens_choice,
            stocking, headwear, shoes, sexy_clothing, framing, include_pose,
            include_details, include_quality, include_suffix, enable_foreground,
            coherent, nsfw, selected_age, selected_body
        )

        prompt_input = kwargs.get("prompt_input", "")
        if prompt_input:
            prompt = prompt_input + "\n" + prompt

        if triggers:
            trigger_str = ", ".join(triggers)
            if trigger_str not in prompt:
                prompt = trigger_str + " " + prompt

        return (prompt,)

    def _generate_prompt(self, style, type_val, detail_level, action, race_choice,
                         contact_lens_choice, stocking, headwear, shoes,
                         sexy_clothing, framing, include_pose, include_details,
                         include_quality, include_suffix, enable_foreground,
                         coherent, nsfw=False, selected_age="23岁", selected_body="舞蹈生紧致身材"):

        nsfw_body = random.choice(libraries["NSFW元素"]["身体强调"]) + "，" if nsfw else ""

        if nsfw and (not sexy_clothing or sexy_clothing == "无"):
            sexy_clothing = random.choice([item for item in libraries["情趣服装"]["情趣衣服"] if item not in ["无", "随机"]])
        if nsfw and stocking == "无":
            stocking = random.choice([s for s in libraries["丝袜类型"]["丝袜种类"] if s not in ["无", "随机"]])

        age_str = f"{selected_age}的" if selected_age != "无" else ""
        body_str = f"{selected_body}，" if selected_body != "无" else ""

        race_desc = race_choice if race_choice else get_random_item("模特设定", "人种特征")
        face1 = get_random_item("模特设定", "面部特征")
        face2 = get_random_item("模特设定", "面部特征")
        while face2 == face1:
            face2 = get_random_item("模特设定", "面部特征")
        hair = get_random_item("模特设定", "发型发色")

        if type_val == "古装":
            clothing_type = get_random_item("服装造型", "古装")
        else:
            clothing_type = random.choice([get_random_item("服装造型", "上衣"), get_random_item("服装造型", "连衣裙"), get_random_item("服装造型", "制服校服")])
        
        material = get_random_item("服装造型", "材质")
        color = get_random_item("服装造型", "颜色")

        scene_type = random.choice(["室内场景", "室外场景"])
        scene = get_random_item("场景环境", scene_type)
        time_weather = get_random_item("场景环境", "时间天气")

        atmosphere = coherent["氛围"]

        lens = get_random_item("拍摄参数", "镜头")
        composition = get_random_item("构图光影", "构图")
        depth = get_random_item("构图光影", "景深")
        light_type = coherent["光线"]
        light_effect = get_random_item("构图光影", "光影效果")

        tone = get_random_item("色彩色调", "色调")
        color_style = get_random_item("色彩色调", "色彩风格")
        expression = coherent["表情"]
        eyes = coherent["眼神"]

        pose = action if action != "无" else (get_random_item("姿势动作", "全身姿势") if include_pose else "")

        framing_desc = {
            "全身照": "全身像，从头到脚完整呈现，",
            "七分照": "七分身像，膝盖以上，",
            "半身照": "半身肖像，腰部以上，",
            "特写": "面部特写，胸部以上，",
            "局部特写": "局部细节特写，"
        }.get(framing, "半身肖像，")

        prompt_parts = []
        if style: prompt_parts.append(style)
        if type_val: prompt_parts.append(type_val)
        prompt_parts.append(f"，使用{lens}镜头拍摄。")
        prompt_parts.append(framing_desc)

        prompt_parts.append(f"一位{age_str}{race_desc}年轻女性，{body_str}拥有{face1}，{face2}，{hair}，气质{coherent['气质']}。")

        if contact_lens_choice and contact_lens_choice != "无":
            prompt_parts.append(f"佩戴{contact_lens_choice}美瞳，")
        if sexy_clothing and sexy_clothing != "无":
            prompt_parts.append(f"穿着{sexy_clothing}，")

        clothing_desc = f"身着{color}{material}{clothing_type}，{nsfw_body}"
        if stocking and stocking != "无":
            clothing_desc += f"搭配{stocking}，"
        prompt_parts.append(clothing_desc)

        if headwear and headwear != "无":
            prompt_parts.append(f"佩戴{headwear}，")
        if shoes and shoes != "无":
            prompt_parts.append(f"脚穿{shoes}，")

        if pose:
            prompt_parts.append(f"{pose}，表情{expression}，{eyes}。")
        else:
            prompt_parts.append(f"表情{expression}，{eyes}。")

        prompt_parts.append(f"置身于{time_weather}{scene}，氛围{atmosphere}。")
        prompt_parts.append(f"采用{composition}，景深为{depth}。画面色调为{tone}，{color_style}。")
        prompt_parts.append(f"光线为{light_type}，形成{light_effect}效果。")

        if include_details:
            prompt_parts.append("肌肤细腻，发丝清晰，眼神有神，服装材质层次丰富。")
        if detail_level in ["大师级", "极致级"]:
            prompt_parts.append("电影级光影，极致细节渲染，故事感强。")

        if include_quality:
            prompt_parts.append("8K超高清，锐利清晰，电影感调色。")

        if include_suffix:
            prompt_parts.append(random.choice([" --ar 9:16 --s 750 --v 6", " --ar 3:4 --stylize 650", " --ar 2:3 --style raw"]))

        final_prompt = "".join(prompt_parts).strip("，") + "。"

        return final_prompt


class ZImagePromptLoaderNode:
    CATEGORY = "prompt_generators"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "文件路径": ("STRING", {"default": "prompt_library.json", "multiline": False}),
                "超强模式": ("BOOLEAN", {"default": True, "label": "超强模式（专属词库）"}),
                "古装": ("BOOLEAN", {"default": False, "label": "古装"}),
                "古风": ("BOOLEAN", {"default": False, "label": "古风"}),
                "艺术摄影": ("BOOLEAN", {"default": False, "label": "艺术摄影"}),
                "cos": ("BOOLEAN", {"default": False, "label": "cos"}),
                "糖水少女": ("BOOLEAN", {"default": False, "label": "糖水少女"}),
                "NSFW": ("BOOLEAN", {"default": False, "label": "NSFW"}),
                "抽卡": ("BOOLEAN", {"default": False, "label": "抽卡"}),
                "随机模式": ("BOOLEAN", {"default": False, "label": "随机模式（忽略开关，从全部抽取）"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "load_prompt"
    OUTPUT_NODE = True

    def load_prompt(self, 文件路径, 超强模式, 古装, 古风, 艺术摄影, cos, 糖水少女, NSFW, 抽卡, 随机模式, seed):
        random.seed(seed)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        if 超强模式:
            luori_path = os.path.join(current_dir, "prompt_luori.json")
            if not os.path.exists(luori_path):
                return (f"文件不存在！请把 prompt_luori.json 放到插件目录下。\n路径: {luori_path}",)
            try:
                with open(luori_path, 'r', encoding='utf-8') as f:
                    luori_data = json.load(f)
                luori_prompts = []
                for lst in luori_data.values():
                    if isinstance(lst, list):
                        luori_prompts.extend(lst)
                if luori_prompts:
                    return (random.choice(luori_prompts),)
                return ("prompt_luori.json 中没有可用的提示词",)
            except Exception as e:
                return (f"读取 prompt_luori.json 失败: {str(e)}",)

        full_path = os.path.join(current_dir, 文件路径)
        if not os.path.exists(full_path):
            return (f"文件不存在！请把 prompt_library.json 放到插件目录下。\n路径: {full_path}",)

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if 随机模式:
                all_prompts = []
                for lst in data.values():
                    if isinstance(lst, list):
                        all_prompts.extend(lst)
                if all_prompts:
                    return (random.choice(all_prompts),)
                return ("JSON中没有提示词",)

            selected = []
            if 古装 and "古装" in data: selected.extend(data["古装"])
            if 古风 and "古风" in data: selected.extend(data["古风"])
            if 艺术摄影 and "艺术摄影" in data: selected.extend(data["艺术摄影"])
            if cos and "cos" in data: selected.extend(data["cos"])
            if 糖水少女 and "糖水少女" in data: selected.extend(data["糖水少女"])
            if NSFW and "NSFW" in data: selected.extend(data["NSFW"])
            if 抽卡 and "抽卡" in data: selected.extend(data["抽卡"])

            if selected:
                return (random.choice(selected),)
            else:
                return ("请至少开启一个分类开关，或打开随机模式",)

        except Exception as e:
            return (f"读取失败: {str(e)}",)

class ZImageFashionPresetLoaderNode:
    CATEGORY = "prompt_generators"

    STYLE_ENHANCE = {
        "日系": ["日系清透质感", "柔和漫射光", "通透肤色", "自然治愈氛围", "胶片感色调"],
        "韩系": ["韩系精致水光肌", "温柔奶油色调", "优雅气质", "高级柔光", "都市时尚感"],
        "法式": ["法式慵懒随性", "自然光晕", "浪漫电影感", "柔和对比", "复古胶片质感"],
        "美式": ["美式复古活力", "鲜明色彩碰撞", "街头潮流感", "动感光影", "青春能量"],
        "森系": ["森系文艺自然", "植物柔光", "大地色系", "宁静空灵感", "自然材质纹理"],
        "纯欲": ["纯欲风清透感", "朦胧梦幻光影", "初恋般柔和", "水润光泽", "温柔氛围"],
        "极简": ["极简主义克制美学", "干净利落线条", "高级灰调", "质感光影", "现代建筑感"],
        "暗黑": ["暗黑哥特美学", "强对比戏剧光", "冷冽金属感", "神秘深邃氛围", "硬朗轮廓"],
        "复古港风": ["港风复古华丽", "霓虹色彩", "强烈光影反差", "怀旧电影感", "戏剧性"],
        "运动": ["运动活力动感", "高速快门捕捉", "鲜艳高饱和度", "青春律动", "阳光健康"],
        "洛丽塔": ["洛丽塔甜美梦幻", "柔光童话感", "精致蕾丝细节", "粉嫩色彩", "少女情怀"],
        "中性": ["中性冷淡风格", "干净利落", "低饱和度高级灰", "极简线条", "文艺克制"],
        "度假": ["度假热带风情", "温暖金色阳光", "自然松弛感", "明亮通透", "夏日清新"],
        "盐系": ["盐系清爽透明感", "自然柔光", "素净色调", "日常治愈", "日系简约"],
        "破碎": ["破碎情绪感", "强烈明暗对比", "戏剧光影", "故事叙事性", "细腻情感"],
        "甜辣": ["甜辣街头活力", "荧光色彩", "年轻俏皮", "动感抓拍", "潮流气息"],
        "复古": ["复古怀旧质感", "暖调胶片色", "颗粒感", "时光沉淀", "经典光影"],
        "未来": ["赛博朋克未来感", "霓虹冷光", "金属质感", "科技氛围", "高饱和电子色"],
        "国风": ["国风古韵", "工笔淡彩", "水墨意境", "飘逸线条", "东方美学"],
        "职业": ["职场精英干练", "专业质感", "冷静光影", "现代办公氛围", "利落线条"],
    }

    DEFAULT_ENHANCE = ["顶级摄影质感", "超写实渲染", "丰富细节层次", "电影级光影", "8K超高清", "色彩精准", "构图考究", "艺术感染力"]

    @classmethod
    def INPUT_TYPES(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "fashion_presets.json")
        presets = [("随机", "随机")]
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        if "title" in item and "content" in item:
                            presets.append((item["title"], item["content"]))
            except:
                pass
        dropdown_dict = {p[0]: p[1] for p in presets}
        return {
            "required": {
                "预设选择": (list(dropdown_dict.keys()), {"default": "随机"}),
                "润色模式": ("BOOLEAN", {"default": True, "label": "智能风格润色"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 18446744073709551615}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "load_preset"
    OUTPUT_NODE = True

    def load_preset(self, 预设选择, 润色模式, seed):
        random.seed(seed)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "fashion_presets.json")

        if not os.path.exists(json_path):
            return (f"错误：未找到 fashion_presets.json，请将其放在插件目录下。\n路径: {json_path}",)

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, list) or len(data) == 0:
                return ("JSON 格式错误，应为包含对象的数组。",)

            if 预设选择 == "随机":
                chosen = random.choice(data)
            else:
                chosen = next((item for item in data if item.get("title") == 预设选择), None)
                if chosen is None:
                    chosen = random.choice(data)

            content = chosen.get("content", "无内容")
            title = chosen.get("title", "")

            if 润色模式:
                content = self._polish_prompt(content, title)

            return (content,)

        except Exception as e:
            return (f"读取 JSON 失败: {str(e)}",)

    def _polish_prompt(self, raw_text, title):
        text_for_scan = (title + " " + raw_text).lower()
        matched_styles = []
        for style in self.STYLE_ENHANCE.keys():
            if style in text_for_scan:
                matched_styles.append(style)
        if matched_styles:
            enhance_words = self.STYLE_ENHANCE[matched_styles[0]]
            selected_words = random.sample(enhance_words, min(3, len(enhance_words)))
        else:
            selected_words = random.sample(self.DEFAULT_ENHANCE, min(3, len(self.DEFAULT_ENHANCE)))
        for word in selected_words:
            if word not in raw_text:
                if raw_text.endswith(('。', '.', '！', '!')):
                    raw_text += " " + word + "。"
                else:
                    raw_text += "。" + word + "。"
        if "光线" not in raw_text and "光" not in raw_text:
            light_options = ["自然柔光", "侧逆光", "伦勃朗光", "轮廓光", "漫射光"]
            raw_text += "采用" + random.choice(light_options) + "，塑造立体感。"
        return raw_text


NODE_CLASS_MAPPINGS = {
    "ZImagePromptGeneratorNode": ZImagePromptGeneratorNode,
    "ZImagePromptLoaderNode": ZImagePromptLoaderNode,
    "ZImageFashionPresetLoaderNode": ZImageFashionPresetLoaderNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ZImagePromptGeneratorNode": "✨ Z-image-落日-提示词生成器",
    "ZImagePromptLoaderNode": "✨ Z-image-落日-提示词抽取器",
    "ZImageFashionPresetLoaderNode": "👗 Z-image-落日-穿搭预设选择器",
}
