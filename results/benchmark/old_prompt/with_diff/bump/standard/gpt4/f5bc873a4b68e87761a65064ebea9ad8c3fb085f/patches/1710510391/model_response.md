-- org.apache.myfaces.tobago.maven.plugin.MavenProject
++ org.apache.maven.project.MavenProject

Here is the fixed client code:

```java
public org.apache.maven.project.MavenProject getProject() {
    return project;
}
```