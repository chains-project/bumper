Here is a patch for the failing method:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    AntDirectoryScanner directoryScanner = new AntDirectoryScanner(); // use AntDirectoryScanner instead
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(new String[]{TestListResolver.getWildcard()});
    directoryScanner.scan();
    return Arrays.asList(directoryScanner.getIncludedFiles()); // get the included files
}
```
Explanation of the changes:

* We use `AntDirectoryScanner` instead of `DirectoryScanner` as it has been added in the new version and provides more flexibility.
* We set the base directory using `setBasedir` method.
* We set the includes using `setIncludes` method and pass the wildcard returned by `TestListResolver.getWildcard()`.
* We scan the directory using `scan` method.
* Finally, we get the included files using `getIncludedFiles()` method and convert it to a list using `Arrays.asList()`.

Note: The above solution assumes that the `TestListResolver.getWildcard()` method returns a valid wildcard pattern that is supported by `AntDirectoryScanner`. If not, you may need to modify the wildcard pattern accordingly.