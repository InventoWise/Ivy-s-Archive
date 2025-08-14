# build_index.py

import os

def build_index(resources_dir):
    index = {}
    
    for age_group in os.listdir(resources_dir):
        age_group_path = os.path.join(resources_dir, age_group)
        if os.path.isdir(age_group_path):
            index[age_group] = []
            for resource in os.listdir(age_group_path):
                resource_path = os.path.join(age_group_path, resource)
                if os.path.isfile(resource_path):
                    index[age_group].append(resource)

    return index

def save_index(index, output_file):
    with open(output_file, 'w') as f:
        for age_group, resources in index.items():
            f.write(f"{age_group}:\n")
            for resource in resources:
                f.write(f"  - {resource}\n")
            f.write("\n")

if __name__ == "__main__":
    resources_directory = '../resources'
    output_file_path = '../index.txt'
    
    index = build_index(resources_directory)
    save_index(index, output_file_path)
    print("Index built and saved to", output_file_path)