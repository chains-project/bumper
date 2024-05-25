```java
  public MavenProject getProject() {
    MavenProject project = null;
    try {
        project = (MavenProject) getPluginContext().get("project");
    } catch (Exception e) {
        e.printStackTrace();
    }
    return project;
  }
```