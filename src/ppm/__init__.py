import json
import os
import glob

def get_ppm_path():
    '''Get ppm.json path'''
    try:
        ppm = glob.glob('ppm.json')
        if len(ppm) == 0:
            raise Exception('No ppm.json file found')
        return ppm[0]    
    except Exception as e:
        print(e)

def get_ppm():
    '''Get ppm.json as dict'''
    try:
        with open(get_ppm_path()) as ppm_file:
            return json.load(ppm_file)
    except Exception as e:
        print(e)

def get_ppm_by_name(name):
    '''Get ppm.json by name'''
    try:
        return get_ppm()[name]
    except Exception as e:
        print(e)


def generate_requirements():
    '''Generate requirements.txt from ppm.json'''
    try:
        requirements = get_ppm_by_name('requirements')
        requires = []
        for _package, _version in requirements.items():
            requires.append(f'{_package}=={_version}')
        return requires
    except Exception as e:
        print(e)

def install_requirements():
    '''Install requirements.txt'''
    try:
        for _package in generate_requirements():
            os.system(f'pip install {_package}')
    except Exception as e:
        print(e)


# print(get_ppm_path())
# print(get_ppm())
# print(get_ppm_by_name('requirements'))
# print(generate_requirements())