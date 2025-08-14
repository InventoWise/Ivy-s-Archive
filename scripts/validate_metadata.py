# validate_metadata.py

import json
import os

def validate_metadata(metadata):
    required_fields = ['title', 'age_band', 'skill_theme', 'resource_type', 'url']
    for field in required_fields:
        if field not in metadata:
            raise ValueError(f'Missing required field: {field}')
    
    if not isinstance(metadata['title'], str) or not metadata['title']:
        raise ValueError('Title must be a non-empty string.')
    
    if metadata['age_band'] not in ['0-2', '2-3', '3-4', '4-5', '5-6', '6-8']:
        raise ValueError('Invalid age band.')
    
    if metadata['skill_theme'] not in ['Literacy', 'Math and Logic', 'Science and Nature', 
                                        'Arts and Crafts', 'Music and Movement', 
                                        'Social and Emotional', 'Physical and Outdoor', 
                                        'Life Skills', 'Bilingual and Phonetics']:
        raise ValueError('Invalid skill theme.')
    
    if not isinstance(metadata['resource_type'], str) or not metadata['resource_type']:
        raise ValueError('Resource type must be a non-empty string.')
    
    if not isinstance(metadata['url'], str) or not metadata['url'].startswith('http'):
        raise ValueError('URL must be a valid HTTP URL.')

def main(metadata_file):
    if not os.path.exists(metadata_file):
        raise FileNotFoundError(f'Metadata file not found: {metadata_file}')
    
    with open(metadata_file, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    try:
        validate_metadata(metadata)
        print('Metadata is valid.')
    except ValueError as e:
        print(f'Validation error: {e}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python validate_metadata.py <metadata_file>')
        sys.exit(1)
    
    main(sys.argv[1])