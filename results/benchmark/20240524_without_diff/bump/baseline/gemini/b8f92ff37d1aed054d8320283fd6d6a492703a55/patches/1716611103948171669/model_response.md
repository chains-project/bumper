```java
static List<String> getClassesLoc(File testSrcFolder) {
        File[] files = testSrcFolder.listFiles();
        List<String> classes = new ArrayList<>();
        if (files != null) {
            for (File file : files) {
                if (file.isFile() && file.getName().endsWith(".java")) {
                    classes.add(file.getAbsolutePath());
                }
            }
        }
        return classes;
    }
```