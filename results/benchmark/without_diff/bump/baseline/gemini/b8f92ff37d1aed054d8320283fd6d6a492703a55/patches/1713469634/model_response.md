```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classes = directoryScanner.scan().getClasses();
        return classes.stream().filter(c -> !c.startsWith("package")).collect(Collectors.toList());
    }
```