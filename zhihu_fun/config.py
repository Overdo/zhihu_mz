config = {
    'start_url': 'https://www.zhihu.com/search?type=content&q=%E7%BE%8E%E8%85%BF',
    # 'start_url': '',
    'cookie': 'aliyungf_tc=AQAAABhEfBlqkA0AGXFWeAo5u2GHHMsf; _zap=230cfdaa-373c-477e-8f30-e52cf2563989; d_c0="ADAC29YWGAyPTsqGUgtU8GK5QXs99-7MioM=|1500555030"; q_c1=e1f2d0661c3d4ce69df7dbf986fb6bed|1507334199000|1500456858000; s-q=%E8%87%AA%E5%88%B6%E5%8F%91%E7%94%B5%E7%B3%BB%E7%BB%9F; s-i=4; sid=k9n5mqko; _ga=GA1.2.1045317781.1509870060; q_c1=e1f2d0661c3d4ce69df7dbf986fb6bed|1512788818000|1500456858000; capsion_ticket="2|1:0|10:1513754127|14:capsion_ticket|',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.33 Safari/537.36',
    'root_url': 'https://www.zhihu.com',
    'log_level': 'info',  # support debug, info, warn
    'custom_urls': ['https://www.zhihu.com/search?type=content&q=%E7%BE%8E+%E7%BE%8E%E5%A5%B3',
                    'https://www.zhihu.com/topic/19552207/hot',
                    'https://www.zhihu.com/question/51603251',
                    'https://www.zhihu.com/question/51644416',
                    'https://www.zhihu.com/topic/20011035/hot'],
    'keyword': ['美女', '萌', '女生', '腿长', '女性',
                '日系', '可爱', '女神', '美腿', '成长',
                '炼成', '吸引', '美', '健身', '丝袜',
                '容貌', '拍照', '女生', '漂亮', '颜值',
                '搭配', '长得', '好看', '衣服', '姑娘',
                '穿', '俗气', '风格', '眼睛', '锻炼',
                '感觉', '感受', '长的', '大学生'],
    'blacklist': ['男生', '男性', '伪娘', '男友', '男人', '男朋友'],
    'key_number': 2,
    'vote_up': 10,
    'url_generate_time': 30  # second
}
