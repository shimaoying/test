import unittest
import os
import HTMLTestRunner


dangqian_path=os.path.dirname(os.path.realpath(__file__))#获取当前路径
yongli_path = os.path.join(dangqian_path,"case")
print(yongli_path)

yongli = "test*.py"  #匹配用力的规则
discover = unittest.defaultTestLoader.discover(start_dir=yongli_path,pattern=yongli)

print(discover)
# runner = unittest.TextTestRunner()
# runner.run(discover)

report_file=os.path.join(dangqian_path,"report","baogao.html")
fp = open(report_file,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                     title="接口测试报告",
                                     description="工单接口",
                                     )
runner.run(discover)