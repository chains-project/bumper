Here is a fixed version of the method that uses a fully qualified class name:

```java
import org.apache.maven.project.MavenProject;

public MavenProject getProject() {
    return project;
}
```

This code imports the fully qualified name of the `MavenProject` class and uses it to declare the return type and the variable `project`. This should fix the "cannot find symbol" error.