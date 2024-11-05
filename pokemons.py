class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

    def __repr__(self):
        return f"{self.numero}: {self.nombre} - Tipos: {', '.join(self.tipos)}"


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = [value]  
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, value)
            else:
                self._insert_recursive(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, value)
            else:
                self._insert_recursive(node.right, key, value)
        else:
            node.value.append(value)  
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
        

    def search_by_prefix(self, prefix):
        results = []
        self._search_by_prefix_recursive(self.root, prefix.lower(), results)
        return results

    def _search_by_prefix_recursive(self, node, prefix, results):
        if node is None:
            return
        if node.key.lower().startswith(prefix):
            results.extend(node.value)
        self._search_by_prefix_recursive(node.left, prefix, results)
        self._search_by_prefix_recursive(node.right, prefix, results)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.extend(node.value)
            self._inorder_recursive(node.right, result)

    def level_order(self):
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node:
                result.extend(node.value)
                queue.append(node.left)
                queue.append(node.right)
        return result


nombre_tree = BST()
numero_tree = BST()
tipo_tree = BST()


pokemons = [
    Pokemon("Bulbasaur", 1, ["planta", "veneno"]),
    Pokemon("Charmander", 4, ["fuego"]),
    Pokemon("Squirtle", 7, ["agua"]),
    Pokemon("Pikachu", 25, ["eléctrico"]),
    Pokemon("Jolteon", 135, ["eléctrico"]),
    Pokemon("Lycanroc", 745, ["roca"]),
    Pokemon("Tyrantrum", 697, ["roca", "dragón"]),
]

for p in pokemons:
    nombre_tree.insert(p.nombre, p)
    numero_tree.insert(p.numero, p)
    for tipo in p.tipos:
        tipo_tree.insert(tipo, p)


def buscar_pokemon(numero=None, nombre=None):
    if numero:
        resultado = numero_tree.search(numero)
        if resultado:
            print("Resultado por número:", resultado)
        else:
            print("No se encontró un Pokémon con ese número.")
    if nombre:
        resultado = nombre_tree.search_by_prefix(nombre)
        if resultado:
            print(f"Resultado por nombre que contiene '{nombre}':", resultado)
        else:
            print("No se encontraron Pokémones con ese nombre.")


class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

    def __repr__(self):
        return f"{self.numero}: {self.nombre} - Tipos: {', '.join(self.tipos)}"


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, value)
            else:
                self._insert_recursive(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, value)
            else:
                self._insert_recursive(node.right, key, value)
        else:
            node.value.append(value)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def search_by_prefix(self, prefix):
        results = []
        self._search_by_prefix_recursive(self.root, prefix.lower(), results)
        return results

    def _search_by_prefix_recursive(self, node, prefix, results):
        if node is None:
            return
        if node.key.lower().startswith(prefix) or prefix in node.key.lower():
            results.extend(node.value)
        self._search_by_prefix_recursive(node.left, prefix, results)
        self._search_by_prefix_recursive(node.right, prefix, results)


nombre_tree = BST()
numero_tree = BST()

pokemons = [
    Pokemon("Bulbasaur", 1, ["planta", "veneno"]),
    Pokemon("Ivysaur", 2, ["planta", "veneno"]),
    Pokemon("Charmander", 4, ["fuego"]),
    Pokemon("Squirtle", 7, ["agua"]),
    Pokemon("Pikachu", 25, ["eléctrico"]),
    Pokemon("Jolteon", 135, ["eléctrico"]),
    Pokemon("Lycanroc", 745, ["roca"]),
    Pokemon("Tyrantrum", 697, ["roca", "dragón"]),
    ]


for p in pokemons:
    nombre_tree.insert(p.nombre, p)
    numero_tree.insert(p.numero, p)

def buscar_pokemon_interactivo():
    while True:
        print("\nBúsqueda de Pokémon")
        print("1. Buscar por nombre (búsqueda por proximidad)")
        print("2. Buscar por número")
        print("3. Salir")
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            nombre = input("Ingrese parte del nombre del Pokémon: ")
            resultados = nombre_tree.search_by_prefix(nombre)
            if resultados:
                print(f"\nResultados para nombre que contiene '{nombre}':")
                for pokemon in resultados:
                    print(pokemon)
            else:
                print("No se encontraron Pokémones con ese nombre parcial.")
        
        elif opcion == '2':
            try:
                numero = int(input("Ingrese el número del Pokémon: "))
                resultado = numero_tree.search(numero)
                if resultado:
                    print(f"\nResultado por número {numero}:")
                    print(resultado[0])
                else:
                    print("No se encontró un Pokémon con ese número.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == '3':
            print("Saliendo de la búsqueda.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


buscar_pokemon_interactivo()

# c)
def listado_ordenado():
    print("Listado ordenado por número:")
    for p in numero_tree.inorder():
        print(p)

# d) 
def listado_por_nivel():
    print("Listado por nivel de nombres:")
    for p in nombre_tree.level_order():
        print(p)

# e)
def datos_pokemons_especificos(nombres):
    for nombre in nombres:
        resultado = nombre_tree.search(nombre)
        if resultado:
            print(f"Datos de {nombre}:", resultado[0])
        else:
            print(f"No se encontró a {nombre}.")

# f)
def contar_por_tipo(tipo):
    pokemons_tipo = tipo_tree.search(tipo)
    cantidad = len(pokemons_tipo) if pokemons_tipo else 0
    print(f"Cantidad de Pokémons de tipo '{tipo}':", cantidad)

