It seems like the method `getWildcard()` is no longer available in the new version of the library. The provided library changes do not show an alternative method to get a wildcard for the `TestListResolver`. Therefore, we might need to manually specify the wildcard.

Here is a potential fix:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    String wildcard = "*"; // Manually specify the wildcard
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, wildcard);
    return directoryScanner.scan().getClasses();
}
```

In this fix, I am assuming that the wildcard is a string that represents a file name pattern. You may need to adjust the wildcard string to fit your specific needs.