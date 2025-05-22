1. **環境構築手順**
   - python ver: 3.10.11
   - 仮想環境構築(Venv/pyenv)
   - VScode install ([VScode インストール先](https://code.visualstudio.com/))
   - 各種パッケージのインストール(requirements.txtを参照)
2. **実行／テスト方法**
   - PS> .\CodeingTest\Scripts\activate (仮想環境をアクティブ)
   - PS> uvicorn main:app --reload      (APIを起動)
   - PS> pytest test_endpoint.py (エンドポイントテスト)
   - PS> pytest test_unit.py (ユニットテスト)
