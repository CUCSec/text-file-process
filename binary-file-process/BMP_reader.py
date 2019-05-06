import struct

# 使用 r 读取 b 二进制 模式打开文件
with open('lenna.bmp', 'rb') as f:
  # 读取 14 字节的文件头
  bmp_file_header = f.read(14)

  # BMP 文件头
  # bm 对应 2 字节的标志'BM'
  # size 对应 4 字节无符号整型表示文件大小
  # r1 r2 对应 2 个宽度为 2 字节的保留位置
  # offset 对应 4 字节无符号整型表示图像数据的起始偏移
  bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

  print(bm, size, offset)

  # 读取 40 字节的文件头
  bmp_info_header = f.read(40)

  # 不定长的信息头，一般为 40 字节
  # info_size 对应 4 字节无符号整型表示信息头大小
  # width 对应 4 字节有符号整型表示图像宽度
  # height 对应 4 字节有符号整型表示图像高度
  # planes 对应 2 字节无符号整型表示色彩层数，一般值为 1
  # bits 对应 2 字节无符号整型表示位深度，即用多少比特表示颜色
  # compression 对应 4 字节无符号整型表示压缩方式
  # data_size 对应 4 字节无符号整型表示图像数据大小 = width * height * bits
  # x_res 对应 4 字节有符号整型表示横向（x轴）分辨率（多少像素每米）
  # y_res 对应 4 字节有符号整型表示纵向（y轴）分辨率（多少像素每米）
  # clr_used 对应 4 字节无符号整型表示调色板颜色数量
  # clr_important 对应 4 字节无符号整型表示调色板重要颜色数量
  info_size, width, height, planes, bits, compression, data_size, x_res, y_res, clr_used, clr_important = struct.unpack('<IiiHHIIiiII', bmp_info_header)

  print(info_size, width, height, bits, data_size)

  # 读取 3 字节的颜色，共计 24 bits ，对应 Blue Green Red.
  first_color = f.read(3)

  # 将 BGR 按自己倒序为 RGB 方便显示
  first_color = first_color[::-1]

  print(f'The first pixel color is #{first_color.hex()}.')
