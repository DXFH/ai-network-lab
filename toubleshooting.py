python -c "
import sys
from pathlib import Path
root = str(Path('api/main.py').resolve().parent.parent)
sys.path.insert(0, root)
print('项目根目录已加入:', root)
try:
    from network_probe.probe import run_probe
    print('✅ 导入成功！')
    print('run_probe() 返回:', run_probe())
except Exception as e:
    print('❌ 导入失败:', type(e).__name__, '-', str(e))
"