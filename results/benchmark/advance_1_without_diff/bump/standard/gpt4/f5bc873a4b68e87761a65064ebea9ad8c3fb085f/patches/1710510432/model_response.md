-- org.apache.myfaces.tobago.maven.plugin.MavenProject
++ org.apache.maven.project.MavenProject

The library update has removed the class `org.apache.myfaces.tobago.maven.plugin.MavenProject` and added `org.apache.maven.project.MavenProject`. This means that the client code should be updated to use the new class. Here is the fixed code:

```java
public org.apache.maven.project.MavenProject getProject() {
    return project;
}
```