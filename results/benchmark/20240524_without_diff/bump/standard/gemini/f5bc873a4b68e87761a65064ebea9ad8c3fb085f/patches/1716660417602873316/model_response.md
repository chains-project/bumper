```java
public org.apache.maven.project.MavenProject getProject() {
    // Get the Maven project from the context
    MavenProject project = (MavenProject) getPluginContext().get("project");

    // Return the Maven project
    return project;
}
```