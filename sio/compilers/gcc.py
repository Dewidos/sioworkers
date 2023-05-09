from __future__ import absolute_import
from sio.compilers.system_gcc import CStyleCompiler


class CCompiler(CStyleCompiler):
    lang = 'c'

    @classmethod
    def gcc_10_2_1_c99(cls):
        obj = cls('gcc.10_2_1')
        obj.options = ['-std=gnu99', '-static', '-O2', '-s', '-lm']
        return obj


class CPPCompiler(CStyleCompiler):
    lang = 'cpp'

    @classmethod
    def gcc_10_2_1_cpp17(cls):
        obj = cls('gcc.10_2_1')
        obj.compiler = 'g++'
        obj.options = ['-std=c++17', '-static', '-O2', '-s', '-lm']
        return obj


def run_gcc4_8_2_c99(environ):
    return CCompiler.gcc_10_2_1_c99().compile(environ)


def run_gcc_default(environ):
    return CCompiler.gcc_10_2_1_c99().compile(environ)


def run_gplusplus4_8_2_cpp11(environ):
    return CPPCompiler.gcc_10_2_1_cpp17().compile(environ)


def run_gplusplus_default(environ):
    return CPPCompiler.gcc_10_2_1_cpp17().compile(environ)


run_c_default = run_gcc_default
run_c_gcc4_8_2_c99 = run_gcc4_8_2_c99
run_cpp_default = run_gplusplus_default
run_cpp_gcc4_8_2_cpp11 = run_gplusplus4_8_2_cpp11
