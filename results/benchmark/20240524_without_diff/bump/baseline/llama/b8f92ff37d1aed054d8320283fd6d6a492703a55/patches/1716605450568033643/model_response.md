```java
static List<String> getClassesLoc(File testSrcFolder) {
    List<String> classes = new ArrayList<>();
    File[] files = testSrcFolder.listFiles();
    for (File file : files) {
        if (file.isDirectory()) {
            classes.addAll(getClassesLoc(file));
        } else if (file.getName().endsWith(".java")) {
            classes.add(file.getName().replace(".java", ""));
        }
    }
    return classes;
}
```