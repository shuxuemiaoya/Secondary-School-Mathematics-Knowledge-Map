# Mathematics GraphRAG Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform monolithic secondary school mathematics markdown files into a dual-target GraphRAG system: an Obsidian-native knowledge base (with Canvas maps) AND an LLM-ready graph dataset (JSON).

**Architecture:** A Python-based pipeline consisting of four stages: 
1) **Chunker**: Splits markdown files strictly by `####` headings into atomic nodes, injecting hierarchical YAML metadata (`#`, `##`, `###`), AND replaces the extracted content in the original file with `![[chunk]]` embeds (MOC reconstruction).
2) **Entity Linker**: Scans chunks to extract ALL entities (concepts, methods, formulas) and establishes bidirectional Obsidian `[[links]]`. 
3) **Canvas Builder**: Generates Map of Content (MOC) and Canvas files to group related nodes visually in Obsidian.
4) **Graph Dataset Exporter**: Compiles all chunks, metadata, and extracted links into a structured JSON dataset optimized for LLM RAG injection (GraphRAG schema).

**Tech Stack:** Python 3, `pytest`, JSON for Canvas and LLM datasets.

---

### Task 1: Setup Chunking Test Fixtures

**Files:**
- Create: `tests/test_chunker.py`
- Create: `tests/fixtures/sample_note.md`

- [ ] **Step 1: Create the sample note fixture**
```markdown
# 第一章 函数
## 1.1 函数的概念
### 1.1.1 定义
#### 核心定义
设A、B是非空的数集，如果按照某种确定的对应关系f...
```
*(Write this to `tests/fixtures/sample_note.md`)*

- [ ] **Step 2: Write the failing test for the chunker**
```python
# tests/test_chunker.py
import os
import shutil
from src.chunker import process_file

def test_chunker_creates_atomic_notes():
    fixture_path = "tests/fixtures/sample_note.md"
    
    # We need a copy of the fixture because the chunker modifies it (MOC reconstruction)
    test_file = "tests/output/sample_note.md"
    output_dir = "tests/output"
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    shutil.copy(fixture_path, test_file)
    
    # Process the file
    chunks = process_file(test_file, output_dir)
    
    assert len(chunks) == 1
    chunk_file = os.path.join(output_dir, "原子节点库_sample_note", "核心定义.md")
    assert os.path.exists(chunk_file)
    
    with open(chunk_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "type: atomic_node" in content
        assert "hierarchy:" in content
        assert "设A、B是非空的数集" in content
        
    # Verify MOC reconstruction (original file modified)
    with open(test_file, "r", encoding="utf-8") as f:
        source_content = f.read()
        assert "![[核心定义]]" in source_content
        assert "设A、B是非空的数集" not in source_content # Content should be moved
```

- [ ] **Step 3: Run test to verify it fails**
Run: `pytest tests/test_chunker.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 4: Commit**
```bash
git add tests/
git commit -m "test: add fixture and failing test for chunker with MOC reconstruction"
```

---

### Task 2: Implement the GraphRAG Chunker

**Files:**
- Create: `src/chunker.py`

- [ ] **Step 1: Write minimal implementation**
```python
# src/chunker.py
import os
import re
import json

def sanitize_title(title):
    return "".join(c for c in title if c not in r'/:*?"<>|').strip()

def process_file(source_file, base_output_dir):
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    current_h1, current_h2, current_h3 = "", "", ""
    in_chunk = False
    chunk_title = ""
    chunk_safe_title = ""
    chunk_content = []
    chunks_generated = []
    new_source_lines = []
    
    file_basename = os.path.basename(source_file).replace(".md", "")
    chunk_dir = os.path.join(base_output_dir, f"原子节点库_{file_basename}")
    
    def save_chunk():
        nonlocal in_chunk, chunk_title, chunk_safe_title, chunk_content, chunks_generated
        if not in_chunk: return
        if not os.path.exists(chunk_dir): os.makedirs(chunk_dir)
            
        filepath = os.path.join(chunk_dir, f"{chunk_safe_title}.md")
        hierarchy = [h for h in [current_h1, current_h2, current_h3] if h]
        
        yaml = f"---\ntype: atomic_node\ntags: [math_chunk]\nsource: \"[[{file_basename}]]\"\n"
        if hierarchy:
            yaml += f"hierarchy: {json.dumps(hierarchy, ensure_ascii=False)}\n"
        yaml += "---\n\n"
        
        with open(filepath, 'w', encoding='utf-8') as cf:
            cf.write(yaml + f"#### {chunk_title}\n\n" + "".join(chunk_content))
            
        chunks_generated.append(chunk_safe_title)
        in_chunk = False
        chunk_title = ""
        chunk_safe_title = ""
        chunk_content = []

    for line in lines:
        h1_match = re.match(r'^#\s+(.*)', line)
        h2_match = re.match(r'^##\s+(.*)', line)
        h3_match = re.match(r'^###\s+(.*)', line)
        h4_match = re.match(r'^####\s+(.*)', line)
        
        if h1_match: current_h1 = h1_match.group(1).strip()
        elif h2_match: current_h2 = h2_match.group(1).strip()
        elif h3_match: current_h3 = h3_match.group(1).strip()
            
        if h4_match:
            save_chunk()
            in_chunk = True
            chunk_title = h4_match.group(1).strip()
            chunk_safe_title = sanitize_title(chunk_title)
            new_source_lines.append(f"\n![[{chunk_safe_title}]]\n")
        elif in_chunk:
            if h1_match or h2_match or h3_match:
                save_chunk()
                new_source_lines.append(line)
            else:
                chunk_content.append(line)
        else:
            new_source_lines.append(line)
                
    save_chunk()
    
    if chunks_generated:
        with open(source_file, 'w', encoding='utf-8') as f:
            f.write("".join(new_source_lines))
            
    return chunks_generated
```

- [ ] **Step 2: Run test to verify it passes**
Run: `pytest tests/test_chunker.py -v`
Expected: PASS

- [ ] **Step 3: Commit**
```bash
git add src/chunker.py
git commit -m "feat: implement hierarchical chunker with MOC reconstruction"
```

---

### Task 3: Implement Entity Linker & Universal Extractor

**Files:**
- Create: `tests/test_linker.py`
- Create: `src/linker.py`

- [ ] **Step 1: Write the failing test**
```python
# tests/test_linker.py
import os
from src.linker import link_entities

def test_link_entities(tmp_path):
    chunk_path = tmp_path / "概念笔记.md"
    chunk_path.write_text("使用换元法求导二次函数，可以应用柯西不等式。", encoding="utf-8")
    
    # We test concepts, methods, and formulas together
    entities = ["换元法", "二次函数", "柯西不等式"]
    
    link_entities(str(chunk_path), entities)
    
    content = chunk_path.read_text(encoding="utf-8")
    assert "[[换元法]]" in content
    assert "[[二次函数]]" in content
    assert "[[柯西不等式]]" in content
```

- [ ] **Step 2: Run test to verify it fails**
Run: `pytest tests/test_linker.py -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**
```python
# src/linker.py
import re

def link_entities(filepath, entities):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    sorted_entities = sorted(entities, key=len, reverse=True)
    
    for entity in sorted_entities:
        pattern = re.compile(r'(?<!\[\[)' + re.escape(entity) + r'(?!\]\])')
        content = pattern.sub(f"[[{entity}]]", content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
```

- [ ] **Step 4: Run test to verify it passes & Commit**
Run: `pytest tests/test_linker.py -v`
```bash
git add src/linker.py tests/test_linker.py
git commit -m "feat: implement universal entity linker"
```

---

### Task 4: LLM Graph Dataset Exporter

**Files:**
- Create: `tests/test_exporter.py`
- Create: `src/exporter.py`

- [ ] **Step 1: Write the failing test**
```python
# tests/test_exporter.py
import os
import json
from src.exporter import export_graph_dataset

def test_export_dataset(tmp_path):
    chunk_dir = tmp_path / "chunks"
    chunk_dir.mkdir()
    file_path = chunk_dir / "test.md"
    
    content = "---\nhierarchy: [\"A\", \"B\"]\n---\n#### 核心\n它依赖于[[导数]]和[[极限]]"
    file_path.write_text(content, encoding="utf-8")
    
    output_json = tmp_path / "graph.json"
    export_graph_dataset(str(chunk_dir), str(output_json))
    
    assert output_json.exists()
    data = json.loads(output_json.read_text(encoding="utf-8"))
    
    assert len(data['nodes']) == 1
    assert "导数" in data['nodes'][0]['edges']
    assert "极限" in data['nodes'][0]['edges']
```

- [ ] **Step 2: Implement Export logic**
```python
# src/exporter.py
import os
import json
import re

def export_graph_dataset(input_dir, output_json):
    graph = {"nodes": []}
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                edges = re.findall(r'\[\[(.*?)\]\]', content)
                
                hierarchy = []
                h_match = re.search(r'hierarchy:\s*(\[.*?\])', content)
                if h_match:
                    try: hierarchy = json.loads(h_match.group(1))
                    except: pass
                
                graph['nodes'].append({
                    "id": file.replace(".md", ""),
                    "content": content,
                    "hierarchy": hierarchy,
                    "edges": list(set(edges))
                })
                
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)
```

- [ ] **Step 3: Run test & Commit**
Run: `pytest tests/test_exporter.py -v`
```bash
git add src/exporter.py tests/test_exporter.py
git commit -m "feat: add JSON exporter for LLM GraphRAG dataset"
```

---

### Task 5: Pipeline Orchestrator & Canvas Builder

**Files:**
- Create: `tests/test_main.py`
- Create: `src/main.py`

- [ ] **Step 1: Write integration test**
```python
# tests/test_main.py
import os
import shutil
import json
from src.main import run_pipeline

def test_full_pipeline(tmp_path):
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    (input_dir / "math_notes.md").write_text("# 函数\n#### 函数概念\n关于函数和极限的内容", encoding="utf-8")
    
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    
    entities = ["函数", "极限"]
    run_pipeline(str(input_dir), str(output_dir), entities)
    
    # Verify Canvas was created
    canvas_path = output_dir / "原子节点库_math_notes" / "math_notes_KnowledgeGraph.canvas"
    assert canvas_path.exists()
    canvas_data = json.loads(canvas_path.read_text(encoding="utf-8"))
    assert len(canvas_data["nodes"]) == 1
    
    # Verify JSON was exported
    graph_path = output_dir / "graph_dataset.json"
    assert graph_path.exists()
    graph_data = json.loads(graph_path.read_text(encoding="utf-8"))
    assert "[[函数]]" in graph_data["nodes"][0]["content"]
```

- [ ] **Step 2: Implement Pipeline Orchestrator and Canvas generation**
```python
# src/main.py
import os
import json
from src.chunker import process_file
from src.linker import link_entities
from src.exporter import export_graph_dataset

def build_canvas(chunk_dir, file_basename, chunks_generated):
    canvas_path = os.path.join(chunk_dir, f"{file_basename}_KnowledgeGraph.canvas")
    nodes = []
    x, y = 0, 0
    
    for i, chunk_title in enumerate(chunks_generated):
        nodes.append({
            "id": str(i),
            "x": x,
            "y": y,
            "width": 300,
            "height": 100,
            "type": "file",
            "file": f"{os.path.basename(chunk_dir)}/{chunk_title}.md"
        })
        x += 350
        if x > 1400:
            x = 0
            y += 150
            
    canvas_data = {"nodes": nodes, "edges": []}
    with open(canvas_path, 'w', encoding='utf-8') as f:
        json.dump(canvas_data, f, ensure_ascii=False, indent=2)

def run_pipeline(input_dir, output_dir, entities):
    for root, dirs, files in os.walk(input_dir):
        dirs[:] = [d for d in dirs if not d.startswith("原子节点库") and not d.startswith(".")]
        
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                # 1. Chunking
                chunks_generated = process_file(filepath, output_dir)
                
                # 2. Canvas Building
                if chunks_generated:
                    chunk_dir = os.path.join(output_dir, f"原子节点库_{file.replace('.md', '')}")
                    build_canvas(chunk_dir, file.replace(".md", ""), chunks_generated)
                    
    # 3. Entity Linking
    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".md"):
                link_entities(os.path.join(root, file), entities)
                
    # 4. JSON Graph Export
    export_graph_dataset(output_dir, os.path.join(output_dir, "graph_dataset.json"))

if __name__ == "__main__":
    base_dir = r"C:\mygithub\Secondary-School-Mathematics-Knowledge-Map"
    entities = ["函数", "极限", "导数", "集合", "数列"] # Example dictionary
    run_pipeline(base_dir, base_dir, entities)
```

- [ ] **Step 3: Run test & Commit**
Run: `pytest tests/test_main.py -v`
```bash
git add src/main.py tests/test_main.py
git commit -m "feat: complete pipeline orchestrator with Canvas generation"
```
