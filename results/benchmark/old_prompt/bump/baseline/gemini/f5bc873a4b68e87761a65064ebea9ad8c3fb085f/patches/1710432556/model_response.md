```java
public MavenProject getProject() {
  return project != null ? project : new MavenProject();
}
```