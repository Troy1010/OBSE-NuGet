from conans import ConanFile, MSBuild
import subprocess, os, errno

class OBSEPackaging_Conan(ConanFile):
    name = "OBSEPluginDevPackage"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/Troy1010/OBSE-Packaging"
    description = "Development sources for OBSE plugins."
    settings = "os", "compiler", "build_type", "arch"

    def configure(self):
        if self.settings.arch != "x86":
            raise Exception("OBSEPackaging_Conan|The common.vcxproj that this recipe builds does not yet support any arch besides x86")
        if self.settings.compiler != "Visual Studio":
            raise Exception("OBSEPackaging_Conan|This recipe does not yet support any compilers besides VisualStudio")

    def source(self):
        try:
            os.makedirs('Oblivion-Script-Extender')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        os.chdir('Oblivion-Script-Extender')
        subprocess.call(['git', 'clone', 'https://github.com/llde/Oblivion-Script-Extender.git', '.', '--no-checkout'])
        subprocess.call(['git', 'checkout', '338206760744df35711bde343d7efe5367644d75'])
        os.chdir('..')

    def build(self):
        msbuild = MSBuild(self)
        sToolset = self.settings.compiler.toolset #Override the toolset that's defined in upcoming .vcxproj
        msbuild.build_env.runtime = self.settings.compiler.runtime
        msbuild.build("Oblivion-Script-Extender/common/common.vcxproj", toolset=sToolset)

    def package(self):
        self.copy('common.lib',src='Oblivion-Script-Extender/common/Debug/',dst='lib/')
        self.copy('*.h',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.cpp',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.h',src='Oblivion-Script-Extender/obse/',dst='include/obse/')
        self.copy('*.cpp',src='Oblivion-Script-Extender/obse/',dst='include/obse/')

    def package_info(self):
        self.cpp_info.libdirs = ['lib']
        self.cpp_info.libs = ['common.lib']
        self.cpp_info.includedirs = ['include','include/obse/']

    def deploy(self):
        pass
