#! python3
'''
    author:     Longlong @ 2017-12-07
    content:    _86ac, dictionary, include, 
    key: Area Code; Value: Area Name(main, exclude the rest)
'''

_86ac = {}

_86ac[10] = "北京"
_86ac[21] = "上海"
_86ac[22] = "天津"
_86ac[23] = "重庆/涪林"
_86ac[852] = "香港"
_86ac[853] = "澳门"
_86ac[886] = "台湾"
_86ac[311] = "河北 石家庄"
_86ac[310] = "河北 邯郸"
_86ac[312] = "河北 保定"
_86ac[313] = "河北 张家口"
_86ac[314] = "河北 承德"
_86ac[315] = "河北 唐山"
_86ac[316] = "河北 廊坊"
_86ac[317] = "河北 沧州"
_86ac[318] = "河北 衡水"
_86ac[319] = "河北 邢台"
_86ac[335] = "河北 秦皇岛"
_86ac[351] = "山西 太原"
_86ac[350] = "山西 忻州"
_86ac[352] = "山西 大同"
_86ac[353] = "山西 阳泉"
_86ac[354] = "山西 榆次"
_86ac[355] = "山西 长治"
_86ac[356] = "山西 晋城"
_86ac[357] = "山西 临汾"
_86ac[358] = "山西 离石"
_86ac[359] = "山西 运城"
_86ac[24] = "辽宁 沈阳"
_86ac[24] = "辽宁 新民"
_86ac[24] = "辽宁 铁岭"
_86ac[411] = "辽宁 大连/庄河"
_86ac[412] = "辽宁 鞍山"
_86ac[413] = "辽宁 抚顺"
_86ac[414] = "辽宁 本溪"
_86ac[415] = "辽宁 丹东"
_86ac[416] = "辽宁 锦州"
_86ac[417] = "辽宁 营口"
_86ac[418] = "辽宁 阜新"
_86ac[431] = "吉林 长春"
_86ac[432] = "吉林 吉林"
_86ac[433] = "吉林 延吉"
_86ac[434] = "吉林 四平"
_86ac[435] = "吉林 通化"
_86ac[436] = "吉林 白城"
_86ac[437] = "吉林 辽源"
_86ac[439] = "吉林 浑江"
_86ac[25] = "江苏 南京/六合/江宁/江浦"
_86ac[510] = "江苏 无锡/江阴"
_86ac[511] = "江苏 镇江/丹徒"
_86ac[512] = "江苏 苏州/吴县"
_86ac[513] = "江苏 南通"
_86ac[514] = "江苏 扬州/邗江"
_86ac[515] = "江苏 盐城"
_86ac[516] = "江苏 徐州/铜山"
_86ac[517] = "江苏 淮阴/淮安"
_86ac[518] = "江苏 连云港"
_86ac[519] = "江苏 常州/武进"
_86ac[571] = "浙江 杭州"
_86ac[570] = "浙江 衢州/衢县"
_86ac[572] = "浙江 湖州"
_86ac[573] = "浙江 嘉兴"
_86ac[574] = "浙江 宁波/镇海/鄞县"
_86ac[575] = "浙江 绍兴"
_86ac[576] = "浙江 临海"
_86ac[577] = "浙江 温州/欧海"
_86ac[578] = "浙江 丽水"
_86ac[579] = "浙江 金华"
_86ac[551] = "安徽 合肥"
_86ac[550] = "安徽 滁县"
_86ac[551] = "安徽 肥西"
_86ac[552] = "安徽 蚌埠"
_86ac[553] = "安徽 芜湖"
_86ac[554] = "安徽 淮南"
_86ac[555] = "安徽 马鞍山"
_86ac[556] = "安徽 安庆"
_86ac[557] = "安徽 宿县"
_86ac[558] = "安徽 阜阳"
_86ac[559] = "安徽 黄山"
_86ac[591] = "福建 福州"
_86ac[590] = "福建 建阳"
_86ac[592] = "福建 厦门"
_86ac[592] = "福建 同安"
_86ac[593] = "福建 宁德"
_86ac[594] = "福建 莆田"
_86ac[595] = "福建 晋江"
_86ac[595] = "福建 泉州"
_86ac[595] = "福建 石狮"
_86ac[596] = "福建 漳州"
_86ac[597] = "福建 龙岩"
_86ac[598] = "福建 三明"
_86ac[599] = "福建 南平"
_86ac[791] = "江西 南昌"
_86ac[790] = "江西 新余"
_86ac[790] = "江西 分宜"
_86ac[792] = "江西 九江"
_86ac[793] = "江西 上饶"
_86ac[794] = "江西 临川"
_86ac[795] = "江西 宜春"
_86ac[796] = "江西 吉安"
_86ac[797] = "江西 赣州"
_86ac[798] = "江西 景德镇"
_86ac[799] = "江西 萍乡"
_86ac[531] = "山东 济南"
_86ac[530] = "山东 菏泽"
_86ac[532] = "山东 青岛"
_86ac[533] = "山东 淄博"
_86ac[534] = "山东 德州"
_86ac[535] = "山东 烟台"
_86ac[536] = "山东 潍坊"
_86ac[537] = "山东 济宁"
_86ac[538] = "山东 泰安"
_86ac[539] = "山东 临沂"
_86ac[371] = "河南 郑州"
_86ac[370] = "河南 商丘"
_86ac[372] = "河南 安阳"
_86ac[373] = "河南 新乡"
_86ac[374] = "河南 许昌"
_86ac[375] = "河南 平顶山"
_86ac[376] = "河南 信阳"
_86ac[378] = "河南 南阳"
_86ac[379] = "河南 开封"
_86ac[471] = "内蒙古 呼和浩特"
_86ac[472] = "内蒙古 包头"
_86ac[473] = "内蒙古 乌海"
_86ac[474] = "内蒙古 集宁"
_86ac[476] = "内蒙古 赤峰"
_86ac[477] = "内蒙古 东胜"
_86ac[451] = "黑龙江 哈尔滨"
_86ac[452] = "黑龙江 齐齐哈尔"
_86ac[453] = "黑龙江 牡丹江"
_86ac[454] = "黑龙江 佳木斯"
_86ac[455] = "黑龙江 绥化"
_86ac[456] = "黑龙江 黑河"
_86ac[457] = "黑龙江 加格达齐"
_86ac[458] = "黑龙江 伊春"
_86ac[27] = "湖北 武汉"
_86ac[710] = "湖北 襄樊"
_86ac[712] = "湖北 孝感"
_86ac[713] = "湖北 黄冈"
_86ac[714] = "湖北 黄石"
_86ac[715] = "湖北 咸宁"
_86ac[716] = "湖北 江铃"
_86ac[716] = "湖北 沙市"
_86ac[717] = "湖北 宜昌"
_86ac[718] = "湖北 恩施"
_86ac[719] = "湖北 十堰"
_86ac[731] = "湖南 长沙/岳阳/望城/宁乡"
_86ac[732] = "湖南 湘潭"
_86ac[733] = "湖南 株洲"
_86ac[734] = "湖南 衡阳"
_86ac[735] = "湖南 郴州"
_86ac[736] = "湖南 常德"
_86ac[737] = "湖南 益阳/桃江/沅江"
_86ac[738] = "湖南 娄底"
_86ac[739] = "湖南 邵阳"
_86ac[20] = "广东 广州/花都/增城/番禹/从化"
_86ac[660] = "广东 汕尾"
_86ac[662] = "广东 阳江"
_86ac[663] = "广东 揭阳"
_86ac[668] = "广东 茂名"
_86ac[750] = "广东 江门"
_86ac[751] = "广东 韶关/曲江"
_86ac[752] = "广东 惠州"
_86ac[752] = "广东 惠阳"
_86ac[753] = "广东 梅州"
_86ac[754] = "广东 汕头/澄海"
_86ac[755] = "广东 深圳"
_86ac[755] = "广东 宝安"
_86ac[756] = "广东 珠海"
_86ac[756] = "广东 斗门"
_86ac[757] = "广东 佛山"
_86ac[757] = "广东 南海"
_86ac[758] = "广东 肇庆"
_86ac[758] = "广东 高要"
_86ac[759] = "广东 湛江"
_86ac[760] = "广东 中山"
_86ac[762] = "广东 河源"
_86ac[763] = "广东 清远"
_86ac[766] = "广东 云浮"
_86ac[768] = "广东 潮州"
_86ac[769] = "广东 东莞"
_86ac[771] = "广西 南宁"
_86ac[772] = "广西 柳州"
_86ac[773] = "广西 桂林"
_86ac[774] = "广西 梧州"
_86ac[775] = "广西 玉林"
_86ac[777] = "广西 钦州"
_86ac[778] = "广西 河池"
_86ac[779] = "广西 北海"
_86ac[898] = "海南 海口"
_86ac[890] = "海南 儋县"
_86ac[28] = "四川 成都"
_86ac[23] = "四川 "
_86ac[812] = "四川 攀枝花"
_86ac[813] = "四川 自贡"
_86ac[814] = "四川 永川"
_86ac[815] = "四川 温江"
_86ac[816] = "四川 绵阳"
_86ac[817] = "四川 南充"
_86ac[818] = "四川 达县"
_86ac[819] = "四川 万县"
_86ac[831] = "四川 宜宾"
_86ac[832] = "四川 内江"
_86ac[833] = "四川 乐山"
_86ac[834] = "四川 西昌"
_86ac[835] = "四川 雅安"
_86ac[837] = "四川 马尔康"
_86ac[851] = "贵州 贵阳"
_86ac[852] = "贵州 遵义"
_86ac[853] = "贵州 安顺"
_86ac[854] = "贵州 都匀"
_86ac[855] = "贵州 凯里"
_86ac[856] = "贵州 铜仁"
_86ac[857] = "贵州 毕节/纳雍"
_86ac[858] = "贵州 六盘水"
_86ac[859] = "贵州 兴义"
_86ac[871] = "云南 昆明"
_86ac[870] = "云南 昭通"
_86ac[871] = "云南 晋宁/呈贡/宜良"
_86ac[872] = "云南 大理"
_86ac[873] = "云南 个旧"
_86ac[874] = "云南 曲靖"
_86ac[875] = "云南 宝山"
_86ac[876] = "云南 文山"
_86ac[877] = "云南 玉溪"
_86ac[878] = "云南 楚雄"
_86ac[879] = "云南 思茅"
_86ac[891] = "西藏 拉萨"
_86ac[29] = "陕西 西安"
_86ac[910] = "陕西 咸阳"
_86ac[911] = "陕西 延安"
_86ac[912] = "陕西 榆林"
_86ac[913] = "陕西 渭南"
_86ac[913] = "陕西 华县"
_86ac[914] = "陕西 商县"
_86ac[915] = "陕西 安康"
_86ac[916] = "陕西 汉中"
_86ac[916] = "陕西 南郑"
_86ac[917] = "陕西 宝鸡"
_86ac[919] = "陕西 铜川"
_86ac[931] = "甘肃 兰州"
_86ac[930] = "甘肃 临夏"
_86ac[932] = "甘肃 定西"
_86ac[933] = "甘肃 平凉"
_86ac[934] = "甘肃 西峰"
_86ac[935] = "甘肃 武威"
_86ac[936] = "甘肃 张掖"
_86ac[937] = "甘肃 酒泉"
_86ac[938] = "甘肃 天水"
_86ac[939] = "甘肃 武都"
_86ac[971] = "青海 西宁"
_86ac[972] = "青海 平安"
_86ac[973] = "青海 同仁"
_86ac[974] = "青海 共和"
_86ac[977] = "青海 德令哈"
_86ac[978] = "青海 门源"
_86ac[979] = "青海 格尔木"
_86ac[951] = "宁夏 银川"
_86ac[952] = "宁夏 石咀山"
_86ac[991] = "新疆 乌鲁木齐"
_86ac[990] = "新疆 克拉玛依"
_86ac[992] = "新疆 奎屯"
_86ac[993] = "新疆 石河子"
_86ac[995] = "新疆 吐鲁番"
_86ac[996] = "新疆 库尔勒"
_86ac[997] = "新疆 阿克苏"
_86ac[898] = "新疆 喀什"
_86ac[999] = "新疆 伊犁"
