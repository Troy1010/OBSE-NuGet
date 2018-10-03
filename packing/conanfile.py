##region Settings
bPause = True
##endregion
from conans import ConanFile, MSBuild
import subprocess, os, errno, ctypes
import TM_CommonPy as TM

##region DoubleclickEvent
if __name__ == "__main__":
    try:
        TM.Run("conan create . Troy1010/channel -pr conanprofile_OBSEPlugin")
    except Exception as e:
        print(e)
        os.system('pause')
        raise
    if bPause:
        print("\n\t\t\tDone\n")
        os.system('pause')
##endregion

class OBSEPackaging_Conan(ConanFile):
    name = "OBSEPluginDevPackage"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/Troy1010/OBSE-Packaging"
    description = "Development sources for OBSE plugins."
    settings = "os", "compiler", "build_type", "arch"
    exports = "RecommendedIntegration.py"

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

    def package(self):
        #---RecommendedIntegration
        self.copy("RecommendedIntegration.py")
        #---common
        self.copy('common.vcxproj',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.h',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.cpp',src='Oblivion-Script-Extender/common/',dst='include/common/')
        self.copy('*.inl',src='Oblivion-Script-Extender/common/',dst='include/common/')
        #---obse
        self.copy('*.h',src='Oblivion-Script-Extender/obse/',dst='include/obse/')
        self.copy('*.cpp',src='Oblivion-Script-Extender/obse/',dst='include/obse/')
        self.copy('*.inl',src='Oblivion-Script-Extender/obse/',dst='include/obse/')

    def package_info(self):
        self.cpp_info.includedirs = ['include','include/obse']
