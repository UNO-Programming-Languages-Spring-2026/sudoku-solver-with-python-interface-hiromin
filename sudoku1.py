import sys, clingo
class ClingoApp(clingo.application.Application):
    # loads all clingo files passed in files list
    # grounds and solves them
    def main(self, ctl, files):
        for f in files:
            ctl.load(f) # Loads file f in string files
            # Ex. ctl.load("solver.lp")
        if not files:
            ctl.load("-") 
            ctl.ground()
            ctl.solve()

    # Prints clingo output atoms in stable models in predefined order
    def print_model(self, model, printer) -> None:
        symbols = sorted(model.symbols(shown=True))
        print(" ".join(str(s) for s in symbols))
        sys.stdout.flush()

            
    # Pass object of class containing these methods to grounder
    if context.load(files):
        ctl.ground(context=context)
        ctl.solve()


# Methds return list type of clingo.Symbols
class Context:
    def color(self) -> List[clingo.Symbol]:
        # Convert string names into constants using clingo.Function()
        self.__colors = [clingo.Function(color) for color in line.split()]
        return self.__colors
    
    def edge(self) -> List[clingo.Symbol]:
        # Convert into tuple using clingo.Tuple()
        origin = clingo.Function(nodes[0])
        destination = clingo.Function(nodes[1])
        edge = clingo.Tuple_((origin, destination))
        self.__edges.append(edge)
        return self.__edges
    
    def set(self) -> List[clingo.Symbol]:
        return [clingo.Number(i) for i in range(1, len(self.__sets)+1)]
    
    def element(self) -> List[clingo.Symbol]:
        sets = zip(range(1, len(self.__sets)+1), self.__sets)
        return [clingo.Tuple_((clingo.Number(i), clingo.Function(e)))]
    # inputs [(1,a), (2,b) ...]
    # outputs [Tuple_(Number(1), Function(a)), Tuple_(Number(2), Function(b))]


# Clingo API https://potassco.org/clingo/python-api/current/clingo/

clingo.application.clingo_main(ClingoApp())

