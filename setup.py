from setuptools import setup, Extension
import os

# قراءة المحتوى من README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# تحديد مكان الملف وتضمينه أثناء البناء
module = Extension(
    'PM',
    sources=['PM/PMmodule.c', 'PM/pm_encrypt.c'],
    include_dirs=[os.path.join(os.path.dirname(__file__), 'PM')],  # تضمين مجلد PM بشكل كامل
)

setup(
    name='PMteam',
    version='0.5',
    author='NASR',
    author_email='nasr2python@gmail.com',
    description='Powerful encryption library for securing Python data by Team PM',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://t.me/NexiaHelpers',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
    ],
    python_requires='>=3.6',
    ext_modules=[module],
)