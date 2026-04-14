#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
纷享开发-小黑 - API 文档搜索助手

纷享销客 API 文档搜索工具，用于快速查找和检索纷享销客平台的 API 文档。
支持向量搜索和关键词搜索，提供智能的 API 文档检索功能。

@author: 小黑
@email: locc233@163.com
@version: 1.0.0
@copyright: Copyright (c) 2026 小黑. All rights reserved.
@license: GNU General Public License v3.0
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Optional, Any

# ============================================================
# 向量搜索实例缓存
# ============================================================
_vector_search_cache: Dict[str, 'VectorSearch'] = {}

def _get_vector_search(doc_dir: Path) -> 'VectorSearch':
    """
    获取或创建向量搜索实例（带缓存）
    
    Args:
        doc_dir: 文档目录路径
    
    Returns:
        VectorSearch实例
    """
    doc_dir_str = str(doc_dir)
    if doc_dir_str not in _vector_search_cache:
        try:
            from vector_search import VectorSearch
            _vector_search_cache[doc_dir_str] = VectorSearch(doc_dir_str, use_cache=True)
        except ImportError:
            # 如果导入失败，使用内联实现（无缓存）
            from sklearn.feature_extraction.text import TfidfVectorizer
            from sklearn.metrics.pairwise import cosine_similarity
            
            class VectorSearch:
                def __init__(self, d):
                    self.doc_dir = Path(d)
                    self.vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
                    self.documents = []
                    self.vectors = None
                    self.build_index()
                
                def build_index(self):
                    for md_file in self.doc_dir.rglob('*.md'):
                        try:
                            with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                            title = self._extract_title(content) or md_file.stem
                            self.documents.append({
                                'file': str(md_file), 'content': content,
                                'relative_path': str(md_file.relative_to(self.doc_dir)), 'title': title
                            })
                        except Exception:
                            pass
                    if self.documents:
                        texts = [doc['content'][:2000] for doc in self.documents]
                        self.vectors = self.vectorizer.fit_transform(texts)
                
                def _extract_title(self, content: str) -> str:
                    match = re.search(r'^#\s+(.*)$', content, re.MULTILINE)
                    return match.group(1).strip() if match else ""
                
                def search(self, query: str, top_k: int = 5) -> List[Dict]:
                    if self.vectors is None or self.vectors.shape[0] == 0:
                        return []
                    query_vector = self.vectorizer.transform([query])
                    similarities = cosine_similarity(query_vector, self.vectors)[0]
                    results = []
                    for i, score in enumerate(similarities):
                        if score > 0.05:
                            doc = self.documents[i]
                            results.append({
                                'file': doc['file'], 'relative_path': doc['relative_path'],
                                'title': doc['title'], 'similarity': float(score)
                            })
                    results.sort(key=lambda x: x['similarity'], reverse=True)
                    return results[:top_k]
            
            _vector_search_cache[doc_dir_str] = VectorSearch(doc_dir_str)
    
    return _vector_search_cache[doc_dir_str]

def search_api_docs(query: str, doc_dir: Optional[str] = None) -> Dict[str, Any]:
    """
    搜索API文档并返回相关结果
    
    Args:
        query: 查询关键词
        doc_dir: 文档目录路径，默认为skill内部的Api_Documentation_Markdown
    
    Returns:
        dict: 包含搜索结果的字典
    """
    if doc_dir is None:
        # 使用skill内部的Api_Documentation_Markdown目录
        doc_dir = os.path.join(os.path.dirname(__file__), 'Api_Documentation_Markdown')
    doc_dir = Path(doc_dir)
    results = []
    
    # 1. 执行向量搜索（使用缓存实例）
    vector_search = _get_vector_search(doc_dir)
    vector_results = vector_search.search(query, top_k=10)
    
    # 2. 执行关键词搜索
    keyword_results = []
    for md_file in doc_dir.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # 检查文件是否包含查询关键词
            if query.lower() in content.lower():
                # 提取文件路径和相对路径
                relative_path = str(md_file.relative_to(doc_dir))
                
                # 提取文件标题
                title = extract_title(content)
                if not title:
                    title = md_file.stem
                
                # 提取相关内容片段
                snippets = extract_snippets(content, query, max_snippets=3)
                
                keyword_results.append({
                    'file': str(md_file),
                    'relative_path': relative_path,
                    'title': title,
                    'snippets': snippets,
                    'score': 0.7  # 关键词搜索的默认分数
                })
        except Exception as e:
            print(f"读取文件失败: {md_file} - {e}")
    
    # 3. 合并结果
    # 创建文件路径到结果的映射，避免重复
    file_to_result = {}
    
    # 先添加向量搜索结果
    for vec_result in vector_results:
        file_to_result[vec_result['file']] = {
            'file': vec_result['file'],
            'relative_path': vec_result['relative_path'],
            'title': vec_result['title'],
            'score': vec_result['similarity'],
            'snippets': []  # 稍后填充
        }
    
    # 添加关键词搜索结果，更新或添加
    for kw_result in keyword_results:
        if kw_result['file'] in file_to_result:
            # 如果文件已在向量搜索结果中，使用更高的分数
            file_to_result[kw_result['file']]['snippets'] = kw_result['snippets']
            file_to_result[kw_result['file']]['score'] = max(
                file_to_result[kw_result['file']]['score'],
                kw_result['score']
            )
        else:
            # 如果文件不在向量搜索结果中，添加它
            file_to_result[kw_result['file']] = kw_result
    
    # 4. 按分数排序
    sorted_results = sorted(file_to_result.values(), key=lambda x: x['score'], reverse=True)
    
    # 5. 填充缺失的snippets
    for result in sorted_results:
        if not result.get('snippets'):
            try:
                with open(result['file'], 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                result['snippets'] = extract_snippets(content, query, max_snippets=3)
            except Exception as e:
                print(f"读取文件失败: {result['file']} - {e}")
                result['snippets'] = []
    
    # 6. 移除score字段，保持与原有返回格式一致
    for result in sorted_results:
        if 'score' in result:
            del result['score']
    
    return {
        'query': query,
        'results': sorted_results,
        'total': len(sorted_results)
    }

def extract_title(content: str) -> str:
    """
    从Markdown内容中提取标题
    
    Args:
        content: Markdown内容
    
    Returns:
        str: 提取的标题
    """
    # 查找一级标题
    match = re.search(r'^#\s+(.*)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""

def extract_snippets(content: str, query: str, max_snippets: int = 3, 
                     context_lines: int = 3) -> List[str]:
    """
    从内容中提取包含查询关键词的片段
    
    Args:
        content: 文档内容
        query: 查询关键词
        max_snippets: 最大返回片段数
        context_lines: 每个片段的上下文行数
    
    Returns:
        list: 包含查询关键词的片段列表
    """
    snippets = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if query.lower() in line.lower():
            # 计算上下文范围
            start = max(0, i - context_lines)
            end = min(len(lines), i + context_lines + 1)
            
            # 提取片段
            snippet = '\n'.join(lines[start:end])
            snippets.append(snippet)
            
            if len(snippets) >= max_snippets:
                break
    
    return snippets

def get_api_info(api_name: str, doc_dir: Optional[str] = None) -> Dict[str, Any]:
    """
    获取特定API的详细信息
    
    Args:
        api_name: API名称
        doc_dir: 文档目录路径，默认为skill内部的Api_Documentation_Markdown
    
    Returns:
        dict: API详细信息
    """
    if doc_dir is None:
        # 使用skill内部的Api_Documentation_Markdown目录
        doc_dir = os.path.join(os.path.dirname(__file__), 'Api_Documentation_Markdown')
    doc_dir = Path(doc_dir)
    
    # 查找API对应的文件
    api_file = doc_dir / 'pages' / 'func-apl' / 'api' / api_name / 'index.md'
    
    if not api_file.exists():
        # 尝试其他可能的路径
        alt_paths = [
            doc_dir / 'pages' / 'func-apl' / 'api' / f'{api_name}.md',
            doc_dir / 'pages' / 'func-apl' / 'data-type' / api_name / 'index.md'
        ]
        
        for path in alt_paths:
            if path.exists():
                api_file = path
                break
        else:
            return {'error': f'未找到API文档: {api_name}'}
    
    try:
        with open(api_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        title = extract_title(content)
        
        # 提取API方法（简单实现）
        methods = extract_methods(content)
        
        return {
            'api_name': api_name,
            'title': title,
            'file': str(api_file),
            'methods': methods,
            'content': content[:1000] + '...' if len(content) > 1000 else content
        }
    except Exception as e:
        return {'error': f'读取API文档失败: {e}'}

def extract_methods(content: str) -> List[str]:
    """
    从文档中提取API方法
    
    Args:
        content: 文档内容
    
    Returns:
        list: API方法列表
    """
    methods = []
    
    # 简单的方法提取逻辑，实际可能需要更复杂的解析
    # 这里仅作为示例
    lines = content.split('\n')
    
    for line in lines:
        # 查找可能的方法定义
        method_match = re.search(r'\b(\w+)\s*\(', line)
        if method_match:
            method_name = method_match.group(1)
            if method_name not in methods:
                methods.append(method_name)
    
    return methods

def generate_example_code(api_name: str, method_name: str) -> str:
    """
    生成API调用示例代码
    
    Args:
        api_name: API名称
        method_name: 方法名称
    
    Returns:
        str: 示例代码
    """
    examples = {
        'ObjectDataAPI': {
            'find': '''// 使用 Fx.object.find 查询多条数据
def (Boolean error, QueryResult queryResult, String errorMessage) = Fx.object.find(
    'AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name', 'owner', 'field_4zWog__c'])
        .queryTemplate(QueryTemplate.AND(['name': QueryOperator.LIKE('%公司%')]))
        .limit(10)
        .build()
)
if (!error) {
    log.info(queryResult.dataList)
}''',
            'findOne': '''// 使用 Fx.object.findOne 查询单条数据（推荐）
def (Boolean error, Map data, String errorMessage) = Fx.object.findOne(
    'AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name', 'owner'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.EQ('64b1113e87ec1c0001bfc102')]))
        .build()
)
if (!error) {
    log.info(data)
}''',
            'create': '''// 创建单个对象（使用 Fx.object.create）
Map masterData = [
    name: '测试公司',
    owner: ['1000'],
    field_4zWog__c: '自定义字段值'
]
def (Boolean error, Map data, String errorMessage) = Fx.object.create(
    'AccountObj',
    masterData,
    [:], // 从对象数据，无则为空 Map
    CreateAttribute.builder().build()
)
if (!error) {
    log.info("创建成功，ID: " + data['_id'])
}''',
            'batchCreate': '''// 批量创建对象（最多 500 条/批）
List dataList = [
    [name: '测试订单 1', field_p1M7F__c: Date.now().toTimestamp(), owner: ['1000']],
    [name: '测试订单 2', field_p1M7F__c: Date.now().toTimestamp(), owner: ['1001']]
]
def (Boolean error, List<Map> batchData, String errorMessage) = Fx.object.batchCreate(
    'AccountObj',
    dataList,
    CreateAttribute.builder().build()
)
if (!error) {
    batchData.each { item ->
        log.info("创建成功：" + item['name'] + ", ID: " + item['_id'])
    }
}''',
            'update': '''// 增量更新单个对象（使用 Fx.object.update）
String objectAPIName = 'AccountObj'
String dataId = '64b1113e87ec1c0001bfc102'
Map updateData = [
    name: '更新后的公司名称',
    field_4zWog__c: '更新后的自定义字段值'
]
def (Boolean error, Map data, String errorMessage) = Fx.object.update(
    objectAPIName,
    dataId,
    updateData,
    UpdateAttribute.builder().build()
)
if (!error) {
    log.info("更新成功")
}''',
            'delete': '''// 删除回收站数据（使用 Fx.object.delete）
// 注意：delete 只能删除已作废的数据（回收站中的数据）
def rst = Fx.object.delete(
    'AccountObj',
    '64b1113e87ec1c0001bfc102'
)
log.info(rst)''',
            'remove': '''// 作废数据（使用 Fx.object.remove）
// 将数据放入回收站
def rst = Fx.object.remove(
    'AccountObj',
    '64b1113e87ec1c0001bfc102'
).result() as Map
log.info(rst)''',
            'changeOwner': '''// 变更负责人（使用 Fx.object.changeOwner）
Fx.object.changeOwner(
    'AccountObj',
    '64b1113e87ec1c0001bfc102',
    'new_user_id'
).result()'''
        },
        'String': {
            'length': '''// 获取字符串长度
def str = "Hello World"
log.info(str.length()) // 输出：11''',
            'substring': '''// 截取子字符串
def str = "Hello World"
log.info(str.substring(0, 5)) // 输出："Hello"''',
            'indexOf': '''// 查找字符串位置
def str = "Hello World"
log.info(str.indexOf("World")) // 输出：6''',
            'toLowerCase': '''// 转换为小写
def str = "Hello World"
log.info(str.toLowerCase()) // 输出："hello world"''',
            'toUpperCase': '''// 转换为大写
def str = "Hello World"
log.info(str.toUpperCase()) // 输出："HELLO WORLD"''',
            'trim': '''// 去除首尾空格
def str = "  Hello World  "
log.info(str.trim()) // 输出："Hello World"''' 
        }
    }
    
    if api_name in examples and method_name in examples[api_name]:
        return examples[api_name][method_name]
    
    # 默认示例
    return f'''// {api_name}.{method_name} 示例
// 请参考 Api_Documentation_Markdown 中的文档获取正确的 API 调用方式
// 常用 API: Fx.object.find, Fx.object.findOne, Fx.object.create, Fx.object.update, Fx.object.delete''' 

if __name__ == '__main__':
    # 测试搜索功能
    query = 'ObjectDataAPI'
    results = search_api_docs(query)
    print(f"搜索 '{query}' 结果:")
    print(f"共找到 {results['total']} 个结果")
    # 只显示前5个结果，避免输出过多
    for i, result in enumerate(results['results'][:5], 1):
        print(f"\n{i}. {result['title']}")
        print(f"   文件: {result['relative_path']}")
        print(f"   片段: {result['snippets'][0][:100]}...")
    
    # 测试获取API信息
    api_info = get_api_info('ObjectDataAPI')
    print("\nObjectDataAPI 信息:")
    print(f"标题: {api_info.get('title')}")
    # 只显示前10个方法，避免输出过多
    methods = api_info.get('methods', [])
    print(f"方法: {methods[:10]}..." if len(methods) > 10 else f"方法: {methods}")
    
    # 测试生成示例代码
    example = generate_example_code('ObjectDataAPI', 'find')
    print("\n示例代码:")
    print(example)
