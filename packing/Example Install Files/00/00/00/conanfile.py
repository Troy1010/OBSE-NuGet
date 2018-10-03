from conans import ConanFile

class TM_HelloWorld_Conan(ConanFile):
    requires="OBSEPluginDevPackage/0.1@Troy1010/channel"
    generators="visual_studio"

    import BuildInfoIntegration as BII
    BII.HookBuildInfo('PROJECT.vcxproj','conanbuildinfo.props')