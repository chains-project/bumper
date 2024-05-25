```java
static List<String> getClassesLoc(File testSrcFolder) {
    List<String> classes = new ArrayList<>();
    File[] files = testSrcFolder.listFiles();
    if (files != null) {
        for (File file : files) {
            if (file.isFile() && file.getName().endsWith(".java")) {
                classes.add(file.getName().replace(".java", ""));
            }
        }
    }
    return classes;
}
```