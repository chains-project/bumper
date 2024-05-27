Here is a possible patch for the failing client code:
```java
import org.apache.maven.model.Project;

public class AbstractThemeMojo {
    // ...
    protected Project currentProject;

    protected void someMethod() {
        // Use currentProject instead of MavenProject
        currentProject = (Project) projectManager.readProject(new File(projectDirectory));
        // ...
    }
    // ...
}
```
In this patch, we have imported `org.apache.maven.model.Project` instead of `org.apache.maven.project.MavenProject`. We have also changed the type of the `currentProject` field to `Project` and updated the method to use `currentProject` instead of `MavenProject`. This should fix the error because `Project` is a superinterface of `MavenProject` and is less likely to have breaking changes.

Note that this patch assumes that the `projectManager` object has a method `readProject` that takes a `File` argument and returns a `Project` object. If this is not the case, the method signature may need to be adjusted accordingly.