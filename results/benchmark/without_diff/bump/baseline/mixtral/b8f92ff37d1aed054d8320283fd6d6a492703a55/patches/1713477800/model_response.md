Here is a possible patch for the given code:
```java
    static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner();
        directoryScanner.setBasedir(testSrcFolder);
        directoryScanner.setIncludes(TestListResolver.getWildcard());
        directoryScanner.scan();
        return directoryScanner.getClasses();
    }
```
In this patch, I created a new instance of `DirectoryScanner` without passing any arguments to the constructor, and then set the `basedir` and `includes` properties explicitly. This should avoid the "cannot find symbol" error, as it does not rely on any external dependencies.

Note that this patch assumes that the `DirectoryScanner` class has a `setBasedir` method and a `setIncludes` method, which are used to set the base directory and the include patterns, respectively. If these methods are not available in the version of `DirectoryScanner` you are using, you may need to modify the patch accordingly.