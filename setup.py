from setuptools import setup, find_packages

setup(
    name='QuantGaussBinomial',
    version='1.9',
    description='A Python package for easy manipulation and calculation with Gaussian and Binomial distributions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This line specifies the format as Markdown
    packages=find_packages(),
    url='https://github.com/RichieSater/QuantGaussBinomial',
    author='Richie Sater',
    author_email='RichieSater@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    keywords='gaussian binomial distributions statistics',
    zip_safe=False
)
