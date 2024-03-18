```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(new String[]{TestListResolver.getWildcard()});
    directoryScanner.scan();
    String[] classes = directoryScanner.getIncludedFiles();
    return Arrays.asList(classes);
}
```