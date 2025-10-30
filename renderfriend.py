import os
import graphviz
from graphviz import Source

def main():
    
    renderList = os.listdir("DOT")

    for renderMe in renderList:
        # dots = Source.from_file(test)
        dots = Source.from_file(renderMe, directory="DOT")

        # Render the graph to an SVG file
        # The output file will be named 'my_graph.gv.svg' by default, 
        # or you can specify a different filename in the render() method.
        dots.render(format='svg', view=False, directory="SVG", cleanup=True)

        print(f"SVG generated from '{renderMe}'")

    #dotCleanup()

main()