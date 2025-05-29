import os
import graphviz

# Adicione o caminho onde está o dot.exe
graphviz_path = r'C:\Program Files\Graphviz\bin'

# Adiciona ao PATH na execução atual do Python
os.environ["PATH"] += os.pathsep + graphviz_path

# Teste gerando um grafo
dot = graphviz.Digraph(comment='Test Graph')

dot.node('A', 'Start')
dot.node('B', 'Process')
dot.node('C', 'End')

dot.edges(['AB', 'BC'])

dot.render('test-output/test_graph', view=True, format='pdf')
