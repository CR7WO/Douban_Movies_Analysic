#-*-coding:utf-8-*-

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")
#��������
category_number = {}
with open("category.csv" , "r") as fp:
    for line in fp.readlines():
        category_number[line.strip().split(",")[0]] = int(line.strip().split(",")[1])
category = []
number = []
category_number = sorted(category_number.items(),key = lambda dic:dic[1],reverse=True) #�ֵ�����
for name,num in category_number[:10]:   #�õ���Ӧ����Ӱ��Ŀ����10�����
    category.append(name)
    number.append(num)

fig, ax = plt.subplots()
# plt.plot(range(1,len(category)+1),number) #����ͼ
rects1 = plt.bar(range(1,len(category)+1), number, width=0.4, alpha=0.2, color='g',align="center") #����ͼ

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.0, 1.05*height,'%d'%int(height), ha='center', va='bottom')

autolabel(rects1)

plt.xlabel(u"�������",color='r')  #������
plt.ylabel(u"��Ӧ�ĵ�Ӱ��Ŀ",color='r')     #������
plt.title(u"���-��Ŀ �ֲ�ͼ")           #ͼƬ����
plt.xticks(range(1,len(category)+1),category,fontsize=12)      #x������������
plt.yticks(fontsize=10)            #y����������ʾ��С
plt.savefig(u'top10category.png')
plt.show()     #��ʾ
