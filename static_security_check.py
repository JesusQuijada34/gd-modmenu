from pathlib import Path

source = Path("src/replayEngine.cpp").read_text(encoding="utf-8")
readme = Path("README.md").read_text(encoding="utf-8")
cmake = Path("CMakeLists.txt").read_text(encoding="utf-8")
assert "is_safe_macro_name" in source
assert 'name.find("..")' in source
assert "name.find('/')" in source
assert "name.find('\\\\')" in source
assert 'return "Invalid macro name"' in source
assert 'Failed to open file for writing' in source
assert "GEODE_SDK" in cmake
assert "AlphaCube" in readme
print("GD_MODMENU_STATIC_SECURITY_CHECK_OK")
