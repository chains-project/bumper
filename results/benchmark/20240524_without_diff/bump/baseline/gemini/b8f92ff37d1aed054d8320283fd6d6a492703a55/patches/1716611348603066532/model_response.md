```java
static List<String> getClassesLoc(File testSrcFolder) {
    File[] files = testSrcFolder.listFiles(new FileFilter() {
        @Override
        public boolean accept(File pathname) {
            return pathname.isFile() && pathname.getName().endsWith(".java");
        }
    });
    List<String> classes = new ArrayList<>();
    for (File file : files) {
        classes.add(file.getAbsolutePath());
    }
    return classes;
}
```