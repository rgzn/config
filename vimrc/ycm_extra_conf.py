import os
import re
import ycm_core

flags = [
    '-Wall',
    '-Wextra',
    '-Wunused',
    '-I', '/opt/local/include',
    '-std=c99',  # Change if not using C
    '-x', 'c',   # Change if not using C
]

# PETSc and MPI
PETSC_DIR = os.getenv('PETSC_DIR')
if not PETSC_DIR:
    PETSC_DIR = os.path.join(os.getenv('HOME'), 'code', 'petsc')
PETSC_ARCH = os.getenv('PETSC_ARCH')
if PETSC_DIR:
    flags.extend(['-I', os.path.join(PETSC_DIR, 'include')])
    if PETSC_ARCH:
        flags.extend(['-I', os.path.join(PETSC_DIR, PETSC_ARCH, 'include')])
if PETSC_DIR and PETSC_ARCH:
    with open(os.path.join(PETSC_DIR, PETSC_ARCH, 'lib', 'petsc', 'conf', 'petscvariables'), 'r') as petsc_variables_file:
        for line in petsc_variables_file:
            if re.match('MPICC_SHOW', line):
                flags.extend([flag for flag in line.split() if flag.startswith('-I')])
                break

# StagBL
STAGBL_DIR = os.getenv('STAGBL_DIR')
if not STAGBL_DIR:
    STAGBL_DIR = os.path.join(os.getenv('HOME'), 'code', 'stagbl')
if STAGBL_DIR:
    flags.extend([
        '-I', os.path.join(STAGBL_DIR, 'include'),
        '-I', os.path.join(STAGBL_DIR, 'include', 'stagbl', 'private'),
    ])

# LaMEM
LAMEM_DIR = os.getenv('LAMEM_DIR')
if LAMEM_DIR:
    flags.extend([
        '-I', os.path.join(LAMEM_DIR, 'src'),
    ])

# pTatin3D
PTATIN_DIR = os.getenv('PTATIN_DIR')
if PTATIN_DIR:
    flags.extend([
        '-I', os.path.join(PTATIN_DIR, 'include'),
        '-I', os.path.join(PTATIN_DIR, 'src'),
    ])


def DirectoryOfThisScript():
    return os.path.dirname(os.path.abspath(__file__))


def MakeRelativePathsInFlagsAbsolute(flags, working_directory):
    if not working_directory:
        return list(flags)
    new_flags = []
    make_next_absolute = False
    path_flags = ['-isystem', '-I', '-iquote', '--sysroot=']
    for flag in flags:
        new_flag = flag

        if make_next_absolute:
            make_next_absolute = False
            if not flag.startswith('/'):
                new_flag = os.path.join(working_directory, flag)

        for path_flag in path_flags:
            if flag == path_flag:
                make_next_absolute = True
                break

            if flag.startswith(path_flag):
                path = flag[len(path_flag):]
                new_flag = path_flag + os.path.join(working_directory, path)
                break

        if new_flag:
            new_flags.append(new_flag)
    return new_flags


def FlagsForFile(filename, **kwargs):
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute(flags, relative_to)

    return {'flags': final_flags, 'do_cache': True}
