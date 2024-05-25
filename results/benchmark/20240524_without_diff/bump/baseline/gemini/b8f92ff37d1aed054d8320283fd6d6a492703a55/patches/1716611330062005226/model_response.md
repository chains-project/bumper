```java
  static List<String> getClassesLoc(File testSrcFolder) {
        List<String> classes = new ArrayList<>();
        for (File file : testSrcFolder.listFiles()) {
            if (file.isFile() && file.getName().endsWith(".java")) {
                classes.add(file.getAbsolutePath());
            }
        }
        return classes;
    }
```