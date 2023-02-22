import os  # 导入os模块

totalSize = 0
fileNum = 0
dirNum = 0


def visitDir(path):  # 遍历目录
    global totalSize  # 全局变量
    global fileNum  # 全局变量
    global dirNum  # 全局变量
    for lists in os.listdir(path):  # 遍历目录
        sub_path = os.path.join(path, lists)  # 合并路径
        if os.path.isfile(sub_path):  # 判断是否为文件
            fileNum = fileNum+1  # 统计文件数量
            totalSize = totalSize+os.path.getsize(sub_path)  # 统计文件总大小
        elif os.path.isdir(sub_path):  # 判断是否为目录
            dirNum = dirNum+1  # 统计文件夹数量
            visitDir(sub_path)  # 递归遍历子文件夹


def main(path):  # 主函数
    if not os.path.isdir(path):  # 判断是否为目录
        print('Error:"', path, '" is not a directory or does not exist.')  # 输出错误信息
        return  # 返回
    visitDir(path)  # 遍历目录


def sizeConvert(size):  # 单位换算
    K, M, G = 1024, 1024**2, 1024**3  # 定义单位
    if size >= G:  # 如果当前size大于等于G
        return str(size/G)+'G Bytes'  # 返回G单位
    elif size >= M:  # 如果当前size大于等于M
        return str(size/M)+'M Bytes'  # 返回M单位
    elif size >= K:  # 如果当前size大于等于K
        return str(size/K)+'K Bytes'  # 返回K单位
    else:  # 否则
        return str(size)+'Bytes'  # 返回Bytes单位


def output(path):  # 输出函数
    print('The total size of '+path+' is:'+sizeConvert(totalSize) + '('+str(totalSize)+' Bytes)')  # 输出文件夹大小
    print('The total number of files in '+path+' is:', fileNum)  # 输出文件数量
    print('The total number of directories in '+path+' is:', dirNum)  # 输出文件夹数量


if __name__ == '__main__':  # 程序入口
    path = r'd:\\'  # 定义路径
    main(path)  # 调用主函数
    output(path)  # 调用输出函数
