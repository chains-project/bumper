```java
static List<String> getClassesLoc(File testSrcFolder) {
    List<String> classesLoc = new ArrayList<>();
    File[] files = testSrcFolder.listFiles();
    if (files != null) {
        for (File file : files) {
            if (file.isFile() && file.getName().endsWith(".java")) {
                classesLoc.add(file.getAbsolutePath());
            }
        }
    }
    return classesLoc;
}
```