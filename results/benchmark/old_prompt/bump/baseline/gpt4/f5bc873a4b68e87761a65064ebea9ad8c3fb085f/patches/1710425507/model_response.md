```java
  public MavenProject getProject() {
    if (this.project == null) {
      this.project = new MavenProject();
    }
    return this.project;
  }
```