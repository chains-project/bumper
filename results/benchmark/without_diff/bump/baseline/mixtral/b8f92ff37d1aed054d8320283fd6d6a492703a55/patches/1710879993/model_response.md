Here is a patch for the failing method:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    AntDirectoryScanner directoryScanner = new AntDirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(new String[]{TestListResolver.getWildcard()});
    directoryScanner.scan();
    return directoryScanner.getIncludedFiles();
}
```
In the original code, `DirectoryScanner` is an abstract class and it seems that the concrete implementation used (`directoryScanner`) does not have the necessary method(s) to make the code work. To fix this, I replaced `DirectoryScanner` with `AntDirectoryScanner` which is a concrete implementation of `DirectoryScanner` and has all the necessary methods.

Also, I set the `basedir` and `includes` properties of the `AntDirectoryScanner` before calling the `scan()` method as it was not done in the original code.

Finally, I replaced the `getClasses()` method with `getIncludedFiles()` as the former is not present in `AntDirectoryScanner`.

This code will fix the compilation error, but you might need to check the logic of the code if the expected output is not as desired.