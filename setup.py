from distutils.core import setup

version = __import__('wallet').__version__
install_requires = open('requirements.txt').readlines(),

setup(
    name='wallet',
    version=version,
    author='Bastian Kuhn',
    author_email='mail@bastian-kuhn.de',
    packages=['wallet', 'wallet.test'],
    url='https://github.com/Bastian-Kuhn/wallet',
    license=open('LICENSE.txt').read(),
    description='Passbook file generator',
    long_description=open('README.md').read(),

    install_requires=install_requires,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
