```java
static List<String> getClassesLoc(File testSrcFolder) {
    List<String> classes = new ArrayList<>();
    File[] files = testSrcFolder.listFiles(new FilenameFilter() {
        @Override
        public boolean accept(File dir, String name) {
            return name.endsWith(".class");
        }
    });
    for (File file : files) {
        classes.add(file.getName().replace(".class", ""));
    }
    return classes;
}
```