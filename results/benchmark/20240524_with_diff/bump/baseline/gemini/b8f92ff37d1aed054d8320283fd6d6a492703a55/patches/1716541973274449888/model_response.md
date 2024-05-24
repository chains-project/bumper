```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder);
        directoryScanner.setIncludes(new String[]{"**/*.java"});
        directoryScanner.scan();
        List<String> classes = new ArrayList<>();
        for (String file : directoryScanner.getIncludedFiles()) {
            classes.add(file.substring(0, file.length() - ".java".length()));
        }
        return classes;
    }
```