```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(new String[]{TestListResolver.getWildcard()});
    directoryScanner.scan();
    String[] files = directoryScanner.getIncludedFiles();
    return Arrays.stream(files).map(File::new).map(File::getAbsolutePath).collect(Collectors.toList());
}
```