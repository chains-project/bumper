```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    java.io.File[] files = testSrcFolder.listFiles();
    java.util.List<java.lang.String> classes = new java.util.ArrayList<>();
    for (java.io.File file : files) {
        if (file.isFile() && file.getName().endsWith(".class")) {
            classes.add(file.getName().replace(".class", ""));
        }
    }
    return classes;
}
```