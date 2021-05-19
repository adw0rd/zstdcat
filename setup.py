from setuptools import find_packages, setup

setup(
    name='zstdcat',
    version='0.1.1',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    license='MIT',
    url='https://github.com/adw0rd/zstdcat',
    install_requires=['zstd==1.5.0.2'],
    keywords=[
        'zstdcat', 'zstdless', 'zstdmore', 'zstd',
        'zstandard', 'cat', 'less', 'more'
    ],
    description='Zstandard console reader',
    long_description="Zstandard console reader",
    scripts=['scripts/zstdcat'],
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
