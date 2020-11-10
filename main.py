from transformation_1 import transformation_1
from transformation_2 import transformation_2
from environment import environment

def main():
    project = environment['project']
    dataset = environment['dataset']
    table_prefix = environment['table_prefix']
    transformation_1(project, dataset, table_prefix)
    transformation_2(project, dataset, table_prefix)

if __name__ == "__main__":
    main()