```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner();
        directoryScanner.setIncludes(new String[]{TestListResolver.getWildcard()});
        directoryScanner.setBasedir(testSrcFolder);
        directoryScanner.scan();
        String[] classes = directoryScanner.getIncludedFiles();
        return Arrays.asList(classes);
    }
```