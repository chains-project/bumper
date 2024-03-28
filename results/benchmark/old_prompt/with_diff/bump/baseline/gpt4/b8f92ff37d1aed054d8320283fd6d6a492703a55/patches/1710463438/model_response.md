The error message indicates that the method `getWildcard()` from `TestListResolver` class is not found. Looking at the changes in the new library version, it seems that the method `getWildcard()` has been removed and no new methods have been added to the `TestListResolver` class.

Unfortunately, without knowing the functionality of the `getWildcard()` method, it's difficult to propose a direct replacement. However, if the `getWildcard()` method was used to get a wildcard string for scanning directories, you can replace it with a constant string wildcard. Here is a proposed patch:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    String wildcard = "*"; // replace this with the appropriate wildcard if necessary
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, wildcard);
    return directoryScanner.scan().getClasses();
}
```

This patch replaces the call to `TestListResolver.getWildcard()` with a constant string wildcard `"*"`. If the wildcard is different, please replace the `"*"` with the appropriate wildcard string.