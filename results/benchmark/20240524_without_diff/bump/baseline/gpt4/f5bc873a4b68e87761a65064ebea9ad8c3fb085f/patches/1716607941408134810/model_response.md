```java
public MavenProject getProject() {
    MavenProject project = null;
    try {
        project = (MavenProject) getPluginContext().get("project");
    } catch(Exception e) {
        System.out.println("Error getting the project");
    }
    return project;
}
```