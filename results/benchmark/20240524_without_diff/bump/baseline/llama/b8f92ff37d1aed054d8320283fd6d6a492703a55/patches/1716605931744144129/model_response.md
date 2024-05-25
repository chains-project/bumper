```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner();
    directoryScanner.setBasedir(testSrcFolder);
    directoryScanner.setIncludes(TestListResolver.getWildcard());
    directoryScanner.scan();
    String[] files = directoryScanner.getIncludedFiles();
    List<String> classes = new ArrayList<>();
    for (String file : files) {
        classes.add(file.replace(".java", "").replace("/", "."));
    }
    return classes;
}
```