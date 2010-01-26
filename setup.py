from distutils.core import setup

setup(
    name = 'django_messages_framework',
    packages = ['django_messages_framework'],
    version = '1.0.0',
    description = "Backport of django (dev)'s messages framework that works with 1.1.1.",
    author='Michael Huynh',
    author_email='mike@mikexstudios.com',
    url='http://github.com/mikexstudios/django-messages-framework',
    classifiers=[
        'Programming Language :: Python', 
        'Framework :: Django', 
        'License :: OSI Approved :: MIT License',
    ]
)

