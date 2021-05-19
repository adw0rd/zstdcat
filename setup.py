from setuptools import find_packages, setup

setup(
    name='zstdtools',
    version='0.1.0',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    license='MIT',
    url='https://github.com/adw0rd/zstdtools',
    install_requires=['zstd==1.5.0.2'],
    keywords=[
        'zstdtools', 'zstdcat', 'zstdless', 'zstdmore', 'zstd',
        'zstandard', 'cat', 'less', 'more'
    ],
    description='Zstandard console tools: zstdcat, zstdless',
    long_description="Zstandard console tools: zstdcat, zstdless",
    # long_description_content_type='text/markdown',
    scripts=['scripts/zstdcat', 'scripts/zstdless'],
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
