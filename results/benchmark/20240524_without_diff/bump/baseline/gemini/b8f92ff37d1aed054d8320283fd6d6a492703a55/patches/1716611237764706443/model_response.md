```java
static List<String> getClassesLoc(File testSrcFolder) {
        File[] files = testSrcFolder.listFiles(new FilenameFilter() {
            @Override
            public boolean accept(File dir, String name) {
                return name.endsWith(".java");
            }
        });

        List<String> classes = new ArrayList<>();
        for (File file : files) {
            String className = file.getName().substring(0, file.getName().length() - 5);
            classes.add(className);
        }
        return classes;
    }
```