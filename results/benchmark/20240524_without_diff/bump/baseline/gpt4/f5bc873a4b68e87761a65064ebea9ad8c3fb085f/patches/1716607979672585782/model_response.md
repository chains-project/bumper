```java
  public MavenProject getProject() {
    MavenProject project = null;
    try {
      project = (MavenProject) getPluginContext().get("project");
    } catch (Exception e) {
      // Handle exception
    }
    return project;
  }
```