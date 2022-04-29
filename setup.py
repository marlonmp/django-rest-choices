from setuptools import setup, find_packages

setup(
    name='django-rest-choices',
    packages=find_packages(),
    version='0.1',
    license='MIT',
    description='A small library to list django choices with REST_FRAMEWORK',
    author='Marlon Mosquera',
    url='https://github.com/marlonmp/django-rest-choices',
    keywords=['django', 'django_rest', 'choices'],
    install_requires=[
            'django',
            'djangorestframework',
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
