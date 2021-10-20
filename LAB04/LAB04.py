# Cau 1:  takes a list of integers as its input argument. Let returns a set of those integers occurring two or more times in the list
def find_dups(L):
    """ (list) -> set
    Return the number of duplicates numbers from L.
    >>> find_dups([1, 1, 2, 3, 4, 2, 2])
    {1, 2}
    >>> find_dups([1, 2, 3, 4])
    set()
    """
    elem_set = set()
    dups_set = set()
    for entry in L:
        len_initial = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)
    return(dups_set)
list_integers = [1,1,2,2,3,3,4,5,6,7,8,9]
find_dups(list_integers)

# Cau 2: 
# Read file multimol.pdb. Return the first item is the name of compound
# then list contains type, coordinates of that atom 
def read_molecule(reader):
    # Nếu không có dòng nào thì kết thúc
    line = reader.readline()
    if not line:
        return None
    # Compound name
    key, name = line.split()

    molecule = [name]
    line = reader.readline()
    
    # the atoms in the molecule.
    while not line.startswith('END'):
        key, num, atom_type, x, y, z = line.split()
        molecule.append([atom_type, x, y, z])
        line = reader.readline()
    return molecule

def read_all_molecules(reader):
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule: 
            result.append(molecule)
        else:
            reading = False
    return result
if __name__ == "__main__":
    molecule_file = open('multimol.pdb','r')
    molecules = read_all_molecules(molecule_file)
    print(molecules)

    # Cau 3: Return a set of tuples where each tuple contains a male from males and a female from females.
def mating_pairs(males, females):
    """ >>> mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 
    'Chen'})
    {('Cari', 'Chen'), ('Beatrice', 'Bob'), ('Anne', 'Ali')}
    """
    try:
        pairs = set()
        num_gerbils = len(males)
        for i in range(num_gerbils):
            male = males.pop()
            female = females.pop()
            pairs.add((male, female),)
        return pairs
    except:
        return print("Loi!!! Số lượng Males và Females phải bằng nhau")
males = {'Nam1', 'Nam2', 'Nam3'}
females = {'Nu1', 'Nu2', 'Nu3'}
mating_pairs(males, females)


# Cau 4: Return a list of the authors in PDB files names appear in filenames.
def get_authors(filenames):
    authors = set()
    for filename in filenames:
        for line in open(filename,'r'):
            if line.lower().startswith('author'):
                author = line[6:].strip()
                authors.add(author)
    return authors
if __name__ == "__main__":
    list_file = ['PDB_1.pdb','PDB_2.pdb']
    print(get_authors(list_file))

    # Cau 5:  Takes a single dictionary as an argument and returns the number of distinct values
def count_values(dictionary):
    return len(set(dictionary.values()))
count_values({'A': 1, 'B': 2, 'C': 2, 'D':3})

# Cau 6: Return the particle from particle_to_probability with the lowest probablity.
def least_likely(particle_to_probability):
    smallest = 1
    name = ''
    for particle in particle_to_probability:
        probability = particle_to_probability[particle]
        if probability < smallest:
            smallest = probability
            name = particle
    return name
least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14})

# Cau 7: Returns the number of values that appear two or more times
def count_duplicates(dictionary):
    duplicates = 0
    values = list(dictionary.values())
    for item in values:      
        if values.count(item) >= 2:
            duplicates = duplicates + 1     
            num_occurrences = values.count(item)
            for i in range(num_occurrences):
                values.remove(item)

    return duplicates
count_duplicates({'A': 1, 'B': 2, 'C': 2, 'D': 1, 'E': 3})


# Cau 8:  return True if they represent a balanced color.
def is_balanced(color_to_factor):
    values = list(color_to_factor.values())
    total = sum(values)
    return total == 1.0
is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})


# Cau 9: Return a new dictionary that contains only the key/value pairs that occur in both dict1 and dict2.
def dict_interest(dict1, dict2):
    intersection = {}
    for (key, value) in dict1.items():
        if key in dict2 and value == dict2[key]:
            intersection[key] = value

    return intersection
dict_interest({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'd': 2})

# Cau 10: Return a set of the keys in the inner dictionaries in dict_of_dict.
def db_headings(dict_of_dict):
    inner_keys = set()
    for key in dict_of_dict:
        for inner_key in dict_of_dict[key]:
            inner_keys.add(inner_key)
    return inner_keys
    
db_headings(
{'jgoodall' : {'surname' : 'Goodall',
'forename' : 'Jane',
'born' : 1934,
'died' : None,
'notes' : 'primate researcher',
'author' : ['In the Shadow of Man',
'The Chimpanzees of Gombe']},

'rfranklin' : {'surname' : 'Franklin',
'forename' : 'Rosalind',
'born' : 1920,
'died' : 1957,
'notes' : 'contributed to discovery of DNA'},

'rcarson' : {'surname' : 'Carson',
'forename' : 'Rachel',
'born' : 1907,
'died' : 1964,
'notes' : 'raised awareness of effects of DDT',
'author' : ['Silent Spring']}
}
)


# Cau 11: Return whether all inner dictionaries in dict_of_dict contain the same keys.
def db_consistent(dict_of_dict):
    inner_keys_list = []
    # List of list of keys
    for key in dict_of_dict:
        inner_keys = list(dict_of_dict[key].keys())
        inner_keys.sort()
        inner_keys_list.append(inner_keys)
        
    for i in range(1, len(inner_keys_list)):
        # If the number of keys is different.
        if len(inner_keys_list[0]) != len(inner_keys_list[i]):
            return False

        # If the keys don't match.
        for j in range(len(inner_keys_list[0])):
            if inner_keys_list[0][j] != inner_keys_list[i][j]:
                return False
    return True

db_consistent(
{'jgoodall' : {'surname' : 'Goodall',
'forename' : 'Jane',
'born' : 1934,
'died' : None,
'notes' : 'primate researcher',
'author' : ['In the Shadow of Man',
'The Chimpanzees of Gombe']},

'rfranklin' : {'surname' : 'Franklin',
'forename' : 'Rosalind',
'born' : 1920,
'died' : 1957,
'notes' : 'contributed to discovery of DNA'},

'rcarson' : {'surname' : 'Carson',
'forename' : 'Rachel',
'born' : 1907,
'died' : 1964,
'notes' : 'raised awareness of effects of DDT',
'author' : ['Silent Spring']}
}
)

# Cau 12 a: takes two sparse vectors stored as dictionaries and returns a new dictionary representing their sum.
def sparse_add(vector1, vector2):
    sum_vector = vector1.copy()
    for key in vector2:
        if key in sum_vector:
            sum_vector[key] = sum_vector[key] + vector2[key]
        else:
            sum_vector[key] = vector2[key]

    return sum_vector
sparse_add({1: 3, 2: 3, 3: 4}, {2: 4, 3: 5, 4: 6})

# Cau 12 b: Return the dot product of sparse vectors vector1 and vector2.
def sparse_dot(vector1, vector2):
    dot = 0

    for key1 in vector1:
        if key1 in vector2:
            dot = dot + vector1[key1] * vector2[key1]

    return dot
sparse_dot({1: 3, 2: 3, 3: 4}, {2: 4, 3: 5, 4: 6})