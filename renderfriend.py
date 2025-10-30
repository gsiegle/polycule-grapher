import os
import graphviz
from graphviz import Source

def dotCleanup():
    allFiles = os.listdir('DOT')

    for aFile in allFiles:
        if (aFile.split(".")[1].lower() == "dot"):
            print ("Deleting file: " + aFile)
            os.remove("SVG/" + aFile)


def main():
    
    test = 'DOT/sample.dot'

    # Load the DOT file
    # dots = Source.from_file(test)
    dots = Source.from_file(filename="sample.dot", directory = "DOT")

    # Render the graph to an SVG file
    # The output file will be named 'my_graph.gv.svg' by default, 
    # or you can specify a different filename in the render() method.
    dots.render(format='svg', view=True, directory = "SVG")

    #graphviz.render(test, "svg", "SVG/" + "blah.svg")
    print(f"SVG generated from '{test}'")

    dotCleanup()

main()