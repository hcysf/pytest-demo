import subprocess
import sys
from pathlib import Path
"""
功能‌：初始化环境变量和确定项目根目录
subprocess：用于在 Python 脚本中调用系统命令行工具（如 pytest 和 allure）。
sys：用于获取当前 Python 解释器的绝对路径（sys.executable），确保使用正确的 Python 环境运行测试。
pathlib.Path：用于跨平台的路径操作。
Path(__file__).resolve().parent：
__file__：获取当前脚本文件的路径。
.resolve()：将路径转换为绝对路径，并解析符号链接，确保路径唯一且真实。
.parent：获取当前脚本所在文件夹的父目录，将其定义为 BASE_DIR（项目根目录）。这样做的好处是无论在哪里运行脚本，都能动态定位到项目根目录，避免硬编码路径导致的错误。
"""



#把该文件的逻辑父地址作为报告的根目录
BASE_DIR = Path(__file__).resolve().parent
print(f"项目根目录: {BASE_DIR}")

"""
定义测试过程中涉及的文件目录和工具路径
RESULTS：指定 pytest 运行后生成的原始测试数据（JSON格式）的存储位置。Allure 需要读取这些数据来生成报告。
REPORT_DIR：指定最终生成的静态 HTML 报告文件的存储位置。
ALLURE_PATH：指定 Allure 命令行工具的可执行文件路径。这里使用的是 Windows 下的 .bat 批处理文件路径。
‌注意‌：这是一个硬编码路径，如果迁移到其他电脑或 Linux/Mac 环境，需要修改此路径或将其配置到系统环境变量中。
"""
# 路径定义
RESULTS = BASE_DIR / "reports" / "allure-results"    # 存放Allure原始测试JSON数据
REPORT_DIR = BASE_DIR / "reports" / "allure-report"  # 存放最终生成的静态HTML报告
ALLURE_PATH = r"D:\Python\allure-2.46.1\bin\allure.bat"



def main():
    """

    :return:
    """
    """
    功能‌：确保输出目录存在
    mkdir(parents=True, exist_ok=True)：parents=True：如果中间目录（如 reports）不存在，会自动递归创建。
    exist_ok=True：如果目录已经存在，不会抛出异常，而是直接跳过。
    这一步是为了防止后续 pytest 或 allure 因为找不到输出目录而报错
    """
    # 🔹 新增：自动提前创建所有需要的目录，避免目录不存在报错
    #mkdir（）创建目录
    RESULTS.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    """
    功能:‌运行自动化测试用例，并收集结果
    subprocess.run(...)：执行外部命令。
    [sys.executable, "-m", "pytest", ...]：
    使用 sys.executable 确保使用当前脚本所在的 Python 环境运行 pytest，避免虚拟环境或系统全局 Python 版本不一致导致的模块缺失问题。
    --alluredir={str(RESULTS)}：告诉 pytest 将测试结果以 Allure 支持的 JSON 格式保存到 RESULTS 目录。
    --clean-alluredir：在开始新测试前，清空 RESULTS 目录中的旧数据，保证报告只包含本次运行的结果。
    -vs：-v 显示详细信息，-s 允许打印测试过程中的 print 输出。
    cwd=BASE_DIR：指定命令执行的工作目录为项目根目录，确保相对路径引用正确。
    shell=True：在 Windows 上通常建议开启，以便正确处理路径和命令解析（但在 Linux 上需注意安全风险，此处针对 Windows 环境配置）。
    """
    print("执行测试，生成Allure原始结果数据...")
    # 🔹 核心修复：给pytest加上--alluredir参数，指定原始结果输出路径，同时加--clean-alluredir自动清空历史旧数据
    pytest_run = subprocess.run(
        [sys.executable, "-m", "pytest", f"--alluredir={str(RESULTS)}", "--clean-alluredir", "-vs"],
        cwd=BASE_DIR,
        shell=True
    )

    """
    功能‌：容错处理，确保即使测试失败也能生成报告
    pytest_run.returncode：获取 pytest 进程的退出状态码。0 表示全部通过，非 0 表示有失败或错误。
    默认情况下，如果子进程返回非零码，后续逻辑可能会被视为异常。
    这里显式检查并打印信息，目的是‌不让测试失败阻止后续的报告生成步骤‌。
    即使用例挂了，我们也希望看到 Allure 报告来分析失败原因。
    """
    # 兼容pytest用例失败返回非0退出码的场景，不中断后续报告生成
    if pytest_run.returncode != 0:
        print(f"测试执行完成，退出码: {pytest_run.returncode}，继续生成报告。")



    """
    功能‌：将原始的 JSON 数据转换为可视化的 HTML 报告。
    ALLURE_PATH generate：调用 Allure 的生成命令。
    str(RESULTS)：输入目录，即上一步 pytest 生成的 JSON 数据所在目录。
    -o str(REPORT_DIR)：输出目录，指定生成的 HTML 文件存放位置。
    --clean：在生成新报告前，清空输出目录中的旧 HTML 文件。
    check=True：这是一个关键参数。如果 allure generate 执行失败（例如 Allure 路径错误、Java 环境缺失等），subprocess.run 会直接抛出 CalledProcessError 异常，终止脚本。这有助于快速发现环境配置问题，而不是静默失败。
    """
    print("生成可视化Allure报告...")
    subprocess.run(
        [ALLURE_PATH, "generate", str(RESULTS), "-o", str(REPORT_DIR), "--clean"],
        cwd=BASE_DIR,
        shell=True,
        check=True # 新增：如果allure generate执行失败直接抛出异常，方便定位问题
    )
    """
    功能‌：启动一个本地 Web 服务器，自动在浏览器中打开最新的测试报告。
    ALLURE_PATH serve：调用 Allure 的服务命令。
    str(RESULTS)：注意，serve 命令通常直接指向‌原始结果目录‌（即 allure-results），而不是生成的 HTML 目录。Allure 会在内存中动态生成报告并提供访问接口。
    ‌效果‌：执行后，终端会显示类似 Starting web server... 的信息，并自动打开默认浏览器访问 http://localhost:xxxx，展示交互式测试报告。
    ‌阻塞性‌：serve 命令通常会阻塞当前进程，直到你手动在终端按 Ctrl+C 停止服务。
    """
    print("启动本地预览服务，自动打开报告...")
    # 🔹 替换allure open为allure serve，启动本地预览服务，和你之前控制台输出的启动服务逻辑完全匹配
    subprocess.run(
        [ALLURE_PATH, "serve", str(RESULTS)],
        cwd=BASE_DIR,
        shell=True
    )

if __name__ == "__main__":
    main()