```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        directoryScanner.scan();
        List<String> classes = new ArrayList<>();
        for (String file : directoryScanner.getIncludedFiles()) {
            if (file.endsWith(".java")) {
                classes.add(file.substring(0, file.length() - 5));
            }
        }
        return classes;
    }
```