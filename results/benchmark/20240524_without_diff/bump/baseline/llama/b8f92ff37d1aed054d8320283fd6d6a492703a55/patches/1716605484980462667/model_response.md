```java
static List<String> getClassesLoc(File testSrcFolder) {
    List<String> classes = new ArrayList<>();
    File[] files = testSrcFolder.listFiles();
    if (files != null) {
        for (File file : files) {
            if (file.isDirectory()) {
                classes.addAll(getClassesLoc(file));
            } else if (file.getName().endsWith(".class")) {
                classes.add(file.getName().replace(".class", ""));
            }
        }
    }
    return classes;
}
```