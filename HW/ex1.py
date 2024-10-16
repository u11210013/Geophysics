# 引入 obspy 套件
import obspy
from obspy import read

# 讀取地震數據，將 'your_file_path.mseed' 替換為你實際的 mseed 文件路徑
st = read()

# 打印地震數據的基本信息
print(st)

# 取得第一個 Trace 並繪製波形圖
tr = st[0]

# 繪製地震波形圖
tr.plot()
