```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(TestListResolver.getWildcard());
    directoryScanner.scan();
    String[] files = directoryScanner.getIncludedFiles();
    List<String> classNames = new ArrayList<>();
    for (String file : files) {
        classNames.add(file.replace(".class", "").replace("/", "."));
    }
    return classNames;
}
```