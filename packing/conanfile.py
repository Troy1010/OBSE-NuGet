from conans import ConanFile, CMake, tools
import subprocess, os, errno

class OBSEPackaging(ConanFile):
    name = "OBSE_Packaging"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/Troy1010/OBSE-Packaging"
    description = "Packages OBSE as a Conan package."

    def source(self):
        try:
            os.makedirs('Oblivion-Script-Extender')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        os.chdir('Oblivion-Script-Extender')
        subprocess.call(['git', 'clone', 'https://github.com/llde/Oblivion-Script-Extender.git', '.', '--no-checkout'])
        subprocess.call(['git', 'checkout', '338206760744df35711bde343d7efe5367644d75'])

    def build(self):
        msbuild = MSBuild(self)
        sToolset = self.settings.compiler.toolset #Override the toolset that's defined in upcoming .vcxproj
        msbuild.build_env.runtime = self.settings.compiler.runtime
        msbuild.build("Oblivion-Script-Extender/common/common.vcxproj", toolset=sToolset)

    def package(self):
        self.copy('common/*',src='Oblivion-Script-Extender')
        self.copy('obse/*',src='Oblivion-Script-Extender')

    def package_info(self):
        pass
