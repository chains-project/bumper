```java
static List<String> getClassesLoc(File testSrcFolder) {
    List<String> classes = new ArrayList<>();
    File[] files = testSrcFolder.listFiles((dir, name) -> name.endsWith(".class"));
    if (files != null) {
        for (File file : files) {
            classes.add(file.getName().replace(".class", ""));
        }
    }
    return classes;
}
```