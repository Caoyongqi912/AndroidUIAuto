# AndroidUIAuto
使用 uiautomator2 做android APP自动化

py + u2  + pytest + allure


- config
  - 读取ini配置文件 提供相关数据
- elements
  - 抽象页面元素成类
- pages
  - 抽象页面操作成方法
- testcases
  - 测试用例
- utils
  - allureOpt.py
    - allure 报告自定义内容
  - assertOpt.py
    - 参数校验
  - deviceInfo.py
    - adb命令操作封装API
  - deviceOpt.py
    - u2 api封装
  - devicePool.py
    - 设备池 适用队列 多设备时可用
  - log
  - shell
  - u
    - 初始化u2 driver


- main
  - pytest 自定义运行